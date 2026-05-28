import { env, pipeline } from 'https://cdn.jsdelivr.net/npm/@xenova/transformers@2.17.2';

env.allowLocalModels = false;
env.useBrowserCache = true;

const INDEX_URL = '../javascripts/semantic-search-index.json';
const DEFAULT_LIMIT = 24;
const DEFAULT_SCORE_THRESHOLD = 0.25;

let manifest = null;
let vectors = null;
let extractor = null;
let initPromise = null;

self.addEventListener('message', event => {
  const message = event.data || {};
  if (message.type === 'init') {
    ensureReady().catch(reportError);
  } else if (message.type === 'query') {
    search(message.query, message.limit).catch(reportError);
  }
});

async function ensureReady() {
  if (initPromise) return initPromise;
  initPromise = (async () => {
    postStatus('Loading semantic index...');
    manifest = await fetchJson(INDEX_URL);
    if (!manifest || !manifest.count || !manifest.dimension) {
      throw new Error('Semantic search index is empty. Run python semantic_search/generate_semantic_search_index.py from knowledge_base/.');
    }

    const vectorUrl = new URL(manifest.vectors || 'semantic-search-vectors.i8', new URL(INDEX_URL, self.location.href));
    const vectorBuffer = await fetchArrayBuffer(vectorUrl.href);
    vectors = new Int8Array(vectorBuffer);
    const expectedLength = Number(manifest.count) * Number(manifest.dimension);
    if (vectors.length !== expectedLength) {
      throw new Error(`Vector index shape mismatch: expected ${expectedLength} values, found ${vectors.length}.`);
    }

    postStatus('Loading browser embedding model...');
    extractor = await pipeline('feature-extraction', manifest.browserModel || 'Xenova/all-MiniLM-L6-v2', {
      quantized: true,
      progress_callback: progress => {
        if (progress && progress.status) {
          postStatus(modelProgressMessage(progress));
        }
      },
    });

    self.postMessage({
      type: 'ready',
      count: manifest.count,
      model: manifest.browserModel || manifest.model,
      scoreThreshold: scoreThreshold(),
    });
  })();
  return initPromise;
}

async function search(query, limit) {
  const text = String(query || '').trim();
  if (!text) {
    self.postMessage({ type: 'results', query: text, results: [], elapsedMs: 0 });
    return;
  }

  await ensureReady();
  postStatus('Embedding query...');
  const output = await extractor(text, { pooling: 'mean', normalize: true });
  const queryVector = Array.from(output.data || output.tolist()[0]);
  if (queryVector.length !== manifest.dimension) {
    throw new Error(`Query embedding dimension mismatch: expected ${manifest.dimension}, got ${queryVector.length}.`);
  }

  const started = performance.now();
  const results = topMatches(queryVector, Math.max(1, Number(limit) || DEFAULT_LIMIT));
  self.postMessage({
    type: 'results',
    query: text,
    results,
    scoreThreshold: scoreThreshold(),
    elapsedMs: performance.now() - started,
  });
}

function scoreThreshold() {
  const threshold = Number(manifest && manifest.scoreThreshold);
  return Number.isFinite(threshold) && threshold >= 0 && threshold <= 1
    ? threshold
    : DEFAULT_SCORE_THRESHOLD;
}

function topMatches(queryVector, limit) {
  const dimension = Number(manifest.dimension);
  const scale = Number((manifest.quantization || {}).scale || 127);
  const count = Number(manifest.count);
  const scores = [];

  for (let row = 0; row < count; row += 1) {
    let dot = 0;
    const offset = row * dimension;
    for (let col = 0; col < dimension; col += 1) {
      dot += (vectors[offset + col] / scale) * queryVector[col];
    }
    scores.push({
      index: row,
      score: dot,
    });
  }

  scores.sort((a, b) => b.score - a.score);
  return scores.slice(0, limit).map(item => ({
    score: Math.max(-1, Math.min(1, item.score)),
    paper: manifest.papers[item.index],
  }));
}

async function fetchJson(url) {
  const response = await fetch(url, { cache: 'no-cache' });
  if (!response.ok) throw new Error(`Could not load ${url}: ${response.status}`);
  return response.json();
}

async function fetchArrayBuffer(url) {
  const response = await fetch(url, { cache: 'no-cache' });
  if (!response.ok) throw new Error(`Could not load ${url}: ${response.status}`);
  return response.arrayBuffer();
}

function postStatus(message) {
  self.postMessage({ type: 'status', message });
}

function modelProgressMessage(progress) {
  if (progress.status === 'progress' && progress.file) {
    const loaded = Number(progress.loaded || 0);
    const total = Number(progress.total || 0);
    const percent = total ? ` ${Math.round((loaded / total) * 100)}%` : '';
    return `Loading ${progress.file}${percent}...`;
  }
  if (progress.status === 'ready') return 'Model ready.';
  if (progress.status === 'initiate' && progress.file) return `Requesting ${progress.file}...`;
  return 'Loading browser embedding model...';
}

function reportError(error) {
  self.postMessage({
    type: 'error',
    message: error && error.message ? error.message : String(error),
  });
}
