<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Late Chunking: Contextual Chunk Embeddings Using Long-Context Embedding Models

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Many use cases require retrieving smaller portions of text, and dense vector-based retrieval systems often perform better with shorter text segments, as the semantics are less likely to be over-compressed in the embeddings. Consequently, practitioners often split text documents into smaller chunks and encode them separately. However, chunk embeddings created in this way can lose contextual information from surrounding chunks, resulting in sub-optimal representations. In this paper, we introduce a novel method called late chunking, which leverages long context embedding models to first embed all tokens of the long text, with chunking applied after the transformer model and just before mean pooling - hence the term late in its naming. The resulting chunk embeddings capture the full contextual information, leading to superior results across various retrieval tasks. The method is generic enough to be applied to a wide range of long-context embedding models and works without additional training. To further increase the effectiveness of late chunking, we propose a dedicated fine-tuning approach for embedding models.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Neural information retrieval (IR) relies on text embedding models that are primarily based on the transformer architecture and have been pre-trained using very large text corpora. These models capture important elements of texts' semantics in the form of dense vectors whose spatial relations - particularly cosine distance - are good proxies for text similarity and relevancy. For many neural IR use cases like the well-known RAG (Retrieval Augmented Generation) approach, applications require splitting documents into limited-size text chunks, and storing them and their vector embeddings in a database. At run-time, neural IR techniques are used to retrieve chunks of text relevant to a user's requests, which are, in the case of RAG, presented to an LLM as a basis for synthesizing a response. Furthermore, many other applications require processing small text segments, and therefore rely on chunking, e.g., to quickly navigate a user to the relevant passage in a document Callan.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, while long context embedding models can improve retrieval performance on long texts, they still perform better on short texts. As a result, chunking generally improves retrieval, even with models that support long contexts. (See Appendix A.1.)

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, long-distance semantic dependencies -- when the relevant information to interpret one chunk of text is located in one or more other chunks -- reduce the effectiveness of this search strategy. Figure 1 displays a Wikipedia article^11^1 that is split into chunks of sentences. One can see that phrases like "its" and "the city" referencing "Berlin" which is mentioned only in the first sentence, e.g., it is harder for the embedding model to link it to the respective entity to produce a high-quality representation.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

To overcome this limitation, we introduce a novel technique called *late chunking*. This method leverages the long text embedding capabilities of recently published models to, first, encode all tokens of an entire document with their full in-document context into a sequence of token embeddings, and then break this sequence up into chunks, which receive embeddings via mean pooling of their token embeddings. This way, chunk embeddings include relevant semantic information derived from their place in the whole text.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Berlin is the capital and largest city of Germany, both by area and by population.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Its more than 3.85 million inhabitants make it the European Union’s most populous city, as measured by population within city limits.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The city is also one of the states of Germany, and is the third smallest state in the country in terms of area.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

As an example of how late chunking works, we encode the texts in Figure 1 with a long-context embedding model, jina-embeddings-v2-small, using both naive and late chunking methods. We then calculate the similarity of the resulting embeddings to the embedding of the word "Berlin". Table 1 shows that, with naive chunking, texts that do not contain the word "Berlin" have low similarity scores, even though both sentences, in context, refer to the city of Berlin. With late chunking, you can see that the similarity scores are much higher. The late chunking strategy has encoded "Berlin" into the embeddings of "Its" and "the city" because it sees them in their context before chunking the text.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Late chunking is an architectural change that can be implemented in any long-context text embedding model that uses mean pooling with any chunking technique and does not require additional model training. It leads to superior results compared to naive chunking across a wide range of retrieval benchmarks. To demonstrate the replicability of our results, we are publishing the code via GitHub ^22^2 In particular, we make the following contributions: Late Chunking: We describe our novel late chunking technique in Section 3 and demonstrate that it leads to superior results compared to naive chunking across a wide range of retrieval benchmarks.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Extended Algorithm for Long Documents: For encoding long documents with more tokens than long-context embedding models can handle, we propose a long late chunking approach (see Section 3.1) and prove its effectiveness in Section 4.3.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Training for Late Chunking: While late chunking does not require additional training, we propose a novel training method to further enhance retrieval accuracy when using it (see Section 3.2). We conduct an evaluation to show its advantage over comparable contrastive training in Section 4.4.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Comprehensive Evaluation: We conduct a comprehensive empirical evaluation to identify scenarios where late chunking performs superior to naive chunking and scenarios where the standard method yields comparable or superior results (see Sections 4.1 and 4.2).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Method", "weight": 1.0} -->

*Late chunking* is a strategy for taking advantage of the difference in size between the long context input windows of recent embedding models and the relatively small size of optimal text chunks for most applications. These models support much longer input texts, for example, 8192 tokens for jina-embeddings-v2-small -- roughly ten pages of standard text -- while optimal chunk sizes are typically much smaller, e.g., the size of a paragraph. The reasons can be manifold, one being that LLMs get more inefficient when providing longer context, and a single short embedding vector only has a limited capacity to represent information.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Method", "weight": 1.0} -->

The naive chunking approach (left side in Figure 2) chunks texts before processing them, using sentences or paragraphs, and then applies an embedding model to the resulting chunks. Contrastively, late chunking, as described in Algorithm 1, first tokenizes the entire text, or the largest part of it possible (line 5), and applies the transformer part from the embedding model on it (line 6). This generates a sequence of vector representations $\vartheta_{1},\ldots,\vartheta_{m}$ for each token that encompass textual information from the entire text. To generate a single embedding for a text, many embedding models apply mean pooling to these token representations to output a single vector. Late chunking instead applies mean pooling to smaller segments of this sequence of token vectors, producing embeddings for each chunk that take into account the entire text. It is important to highlight that late chunking still requires boundary cues that are derived from the chunks determined by a chunking algorithm, but these cues are used only *after* obtaining the token-level-embeddings - hence the term *late* in its naming.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Method", "weight": 1.0} -->

Chunking algorithms usually chunk text into sequences of characters. For late chunking, boundary cues corresponding to a sequence of tokens are necessary. Accordingly, Lines 9-17 of the algorithm translate the chunk definition into boundary cues that are used by the pooling step in the lines19-21.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Method", "weight": 1.0} -->

1:Inputs: Text T, Chunking Strategy S 2:Outputs: Chunk Embeddings e1, …, en 5:(τ1, …, τm), (o1, …, om) ← Tokenizer(T) ⊳ τi is a token ID, oi its character length 6:(ϑ1, …, ϑm) ← Model(τ1, …, τm) ⊳ Calculate token embeddings ϑ1, …, ϑm 7:ochunk ← 0, j ← 1, cuestart ← 1, cues ← 9:for i ∈ {1, …, m} do ⊳ For each token 11: if ochunk ≥ |cj| then ⊳ When the current chunk size is reached, save positions 13: cues ← cues ⊕ (cuestart, cueend) 19:for (cuestart, cueend)i ∈ cues do ⊳ Pool token embeddings according to cue positions 20: $e_{i}\leftarrow{\left({\sum_{j = {cue}_{start}}^{{cue}_{end}}\vartheta_{j}}

<!-- chunk {"id": "body-0019", "role": "body", "section": "Long Late Chunking", "weight": 1.0} -->

1:Inputs: Text T, Chunking Strategy S, Maximum Token Length lmax, Overlap Length ω 2:Outputs: Chunk Embeddings E = (e1, e2, …, en) 5:(τ1, τ2, …, τm), (o1, o2, …, om)← Tokenizer(T) ⊳ τi is a token ID, oi its character length 7:if m < lmax then⊳ If the number of tokens is already small, do regular late chunking 13: istart ← max (iend − ω, 1)⊳ Update token positions with overlap 14: iend ← min (istart + lmax, m) 15: (ϑistart, …, ϑiend) ← Model(τistart, …, τiend) ⊳ Calculate token embeddings 17: embeddings ← embeddings ⊕ (ϑistart, …, ϑiend) 19: embeddings ← embeddings ⊕ (ϑistart + ω, …, ϑiend) 23:Carry out steps 4 to 16 of Algorithm 1 with augmented token embeddings ϑ1, …, ϑm.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Long Late Chunking", "weight": 1.0} -->

Algorithm 2 Long Late Chunking Although many embedding models offer a high enough context length to encode a large amount of text at once, the context length might still not be sufficient to encode very large documents in one step. Moreover, the memory required for the encoding increases exponentially with an increasing number of tokens so that encoding all tokens at once becomes infeasible. To solve this problem, we propose using long late chunking as described in Algorithm 2. Thereby, the text is split into larger macro chunks of $l_{max}$ tokens that encompass multiple smaller chunks. Each macro chunk is processed separately by the $LateChunking$ method. To avoid missing context, macro chunks are augmented with a certain number of tokens $\omega$ that overlap with the next chunks. Those additional tokens serve as supplementary context information during late chunking.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Training Method", "weight": 1.0} -->

While late chunking works without further training, models that are trained with mean pooling to create a single embedding representation of a longer text might not be well-suited to encode chunks of token embeddings containing additional information from surrounding tokens. Therefore, we propose a modified text embedding training method, which uses a technique that we call "span pooling" to train the model to encode specifically the relevant information contained in an annotated text span into its token embeddings.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Training Data", "weight": 1.0} -->

To conduct the training, we prepare training data which consist of tuples $(q,d,{\langle{start},{end}\rangle})$ of two text values: a query $q$ and a relevant document $d$, with additional annotation of the relevant span in the document $\langle{start},{end}\rangle$ that contains the answer.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Training Process", "weight": 1.0} -->

The fine-tuning procedure itself follows the pair training stage described in Günther et al., where the model is trained on text pairs using the InfoNCE loss function which is defined on a batch $B = {({(x_{1},y_{1})},\ldots,{(x_{k},y_{k})})}$ of $k$ pairs and the cosine similarity function $s$: Here, the query vectors $x_{i}$ are obtained by applying the embedding model to the query text $q_{i}$ in the usual way. For the document embeddings $y_{i}$, the set of token embeddings $\vartheta_{i,1},\ldots,\vartheta_{i,n}$ is obtained by applying the model on the documents $d_{i}$, and executing the mean pooling operation only to the token embeddings within the span $\langle{start},{end}\rangle$, hence the term "span pooling".

<!-- chunk {"id": "body-0024", "role": "body", "section": "Training Process", "weight": 1.0} -->

As proposed by Günther et al., we use a bi-directional version of the loss $\mathcal{L}_{pairs}$, where $B^{\dagger} = {({(y_{1},x_{1})},\ldots,{(y_{k},x_{k})})}$ is obtained from $B$ by swapping the order of pairs: A description of the datasets, hyperparameters of the training and the evaluation results can be found in Section 4.4.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Evaluation", "weight": 1.0} -->

First, we evaluate late chunking on a variety of models, chunking methods, and retrieval datasets to show its effectiveness in Section 4.1. Section 4.2 investigate the influence of the chunking size and also identifies scenarios where late chunking works optimally, as well as limitations of the method. The long late chunking method is evaluated on datasets with long documents in Section 4.3. The proposed span pooling method for training is evaluated in Section 4.4. Finally, we also conduct a small-scale evaluation to compare late chunking to the LLM-based contextual embedding technique in Section 4.5.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Evaluation on Retrieval Tasks", "weight": 1.0} -->

To test the effectiveness of late chunking, we apply our technique to the smaller retrieval tasks of the BeIR benchmark. We restrict the evaluation on the smaller datasets, as splitting documents into smaller chunks increases the computational effort of the evaluation, which makes a comprehensive evaluation on different models, tasks, and chunking techniques infeasible.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Evaluation on Retrieval Tasks", "weight": 1.0} -->

Those retrieval tasks consist of a query set, a corpus of text documents, and a QRels file that stores information about the IDs of documents that are relevant for each query. To identify the relevant documents of a query, one can chunk the documents, encode and store them into an embedding index, and determine for each query embedding the chunks corresponding to the k-nearest-neighbors (kNN) of their normalized vector representations. As each chunk corresponds to a document, one can convert the kNN ranking of chunks into a kNN ranking of documents (for documents occurring multiple times in the ranking, only the first occurrence is retained). After that, one can compare the resulting ranking with the ranking corresponding to the ground-truth QRels file and calculate retrieval metrics like nDCG@10.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Evaluation on Retrieval Tasks", "weight": 1.0} -->

We run this evaluation for the BeIR datasets with naive chunking, our novel late chunking method, and also report the score obtained without chunking. Both naive chunking and late chunking are evaluated with different chunking techniques, we use: Fixed-Size Boundaries: Each chunk has the same number of tokens (256 in this experiment).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Evaluation on Retrieval Tasks", "weight": 1.0} -->

Sentence Boundaries: Each chunk has the same number of sentences (5 in this experiment).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Evaluation on Retrieval Tasks", "weight": 1.0} -->

Semantic Sentence Boundaries: Each chunk corresponds to multiple sentences. Sentences with high embedding similarity (we use jina-embeddings-v2-small-en) are combined in the same chunk. We use the semantic chunking implementation from llama-index^33^3 with the default parameters.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Evaluation on Retrieval Tasks", "weight": 1.0} -->

We evaluate three embedding models: jina-embeddings-v2-small, jina-embeddings-v3, and nomic-embed-text-v1.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Dealing with Non-Context Tokens", "weight": 1.0} -->

Not all tokens correspond to characters in the original string. For instance, the tokenizers of all models add a \[CLS\] token at the beginning and append a \[SEP\] token at the end of the text. Additionally, jina-embeddings-v3 and nomic-embed-text-v1 prepend an instruction to the string for distinguishing queries and documents. During late chunking, we include all embeddings of prepended tokens in the mean pooling of the first chunk and all embeddings of appended tokens to the last chunk.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Dealing with Non-Context Tokens", "weight": 1.0} -->

We present the evaluation results in Table 2. When comparing the results for the different chunking methods, we observe that replacing naive methods with their late chunking counterparts almost always yields better performance. Averaging results across three models and four datasets, we find a 3.63% relative improvement (1.9% absolute) from naive chunking with sentence boundaries to late chunking using sentence boundaries, a 3.46% improvement (1.8% absolute) from naive chunking to late chunking using fixed-size boundaries, and a 2.70% improvement (1.5% absolute) from naive chunking to late chunking when using semantic sentence boundaries. In all experiments the chunks are non-overlapping, however, additional results demonstrated in appendix A.2 show that overlapping the chunks generally neither improves nor harms the retrieval performance. These findings demonstrate that the late chunking technique effectively and consistently enhances overall performance.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Dealing with Non-Context Tokens", "weight": 1.0} -->

Fixed-Size Boundaries (256 Tokens per Chunk) Sentence Boundaries (5 Sentences per Chunk) Semantic Sentence Boundaries Table 2: Evaluation of different chunking methods on retrieval tasks. Scores are reported as nDCG@10 [%] Models: jina-embeddings-v2-small (J2s), jina-embeddings-v3(J3), nomic-embed-text-v1 (Nom).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Evaluation of Training Method", "weight": 1.0} -->

Table 3 captures the results from our training experiments. The experiments include running both span-based and regular mean pooling training methods on the jina-embeddings-v3 and jina-embeddings-v2-small-en long context embedding models in order to see whether the proposed training method achieves performance gains in combination with late chunking. To evaluate the models after the training we use the same procedure as in Section 4.1. For chunking, we used fixed-size boundaries (64 tokens). For the jina-embeddings-v3 model, we fine-tune only the retrieval adapters, following the same hyperparameter settings of Sturua et al., however with an increased batch size of 512 and training for only 500 steps. The hyperparameters for the fine-tuning of jina-embeddings-v2-small-en model are analogous to those detailed in Günther et al..

<!-- chunk {"id": "body-0036", "role": "body", "section": "Evaluation of Training Method", "weight": 1.0} -->

For the span-based training method, we prepare two datasets into the format described in Section 3.2 and make these publicly available on HuggingFace ^44^4FEVER: Trivia-QA: These two datasets are FEVER and TriviaQA, which are well-suited for this experiment as they contain annotations of where the relevant text can be found in the documents respectively. In the FEVER dataset, these spans take the shape of sentence number annotations, while for TriviaQA the annotations are usually a name, place, or date in the form of a short phrase. For FEVER, we only include pairs where the document provides supporting evidence for the claim. When multiple spans are annotated in these datasets, we select only the span, which occurs earliest in the document.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Evaluation of Training Method", "weight": 1.0} -->

Across the datasets and models, span pooling and mean pooling during training deliver relatively similar results, with span pooling consistently achieving a small improvement. The training dataset selection also has a small effect on the performance, thus resulting in slightly higher results for NarrativeQA when only training on TriviaQA, which is likely due to an overlap of domain and phrasing of query-document pairs of the task and training data.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Evaluation of Training Method", "weight": 1.0} -->

While the span pooling method for training shows promise, the training dataset diversity is quite limited, as both training datasets are sourced from Wikipedia documents. The summed dataset encompasses only $\sim$`<!-- -->`{=html}470k pairs in total for training, which may additionally limit the potential performance gains. It may be possible to achieve higher performance with a larger quantity and more diverse set of training data.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Comparison to Contextual Embedding", "weight": 1.0} -->

The recent SEC filing provided insights into ACME Corp’s performance for Q2 2023.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Comparison to Contextual Embedding", "weight": 1.0} -->

It highlighted a 3% revenue growth over the previous quarter.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Comparison to Contextual Embedding", "weight": 1.0} -->

The company, which had a revenue of $314 million in the prior quarter, showed steady progress.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Comparison to Contextual Embedding", "weight": 1.0} -->

They attributed this growth to strategic initiatives and operational efficiencies.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Comparison to Contextual Embedding", "weight": 1.0} -->

The report emphasized the company’s resilience and ability to navigate market challenges, reflecting positively on their financial health and future prospects.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Comparison to Contextual Embedding", "weight": 1.0} -->

We conduct a small-scale experiment to compare late chunking to the LLM-based contextual embedding approach published in a blog post by Anthropic mentioned in the related work Section 2. Given the chunks obtained from a fictional financial document shown in Table 4 and the query "What is ACME Corp's revenue growth for Q2 2023?", the goal is to identify the relevant chunk. The relevant chunk in this example, "It highlighted a 3% revenue growth over the previous quarter.", however, misses the company's name, which is necessary to determine its relevancy. We implement the method described in the blog post that uses the claude-3-haiku-20240307 model to select relevant contextual information from the whole text and add it to the beginning of each text chunk. Then, we encode the query and the augmented chunks with jinaai/jina-embeddings-v2-small-en to calculate their cosine similarity. Table 4 captures the similarity values and compares them to those obtained from the chunks with late and naive chunking.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Comparison to Contextual Embedding", "weight": 1.0} -->

One can see that both the contextual embedding method and late chunking produce the highest similarity value for the relevant chunk. In contrast, native chunking leads to a much smaller similarity score that is lower than the similarity to other chunks. Furthermore, one can see that contextual embedding and late chunking produce similarity scores that are close to each other across all chunks, with late chunking having the advantage that it does not require using an additional large language model.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we present a novel approach for encoding text chunks with embedding models called *late chunking*. We demonstrate how it can resolve context dependency problems and show that it improves text embeddings across a wide range of retrieval tasks. For handling situations in which the maximum context length of the model is not sufficient, we present a long late chunking approach to effectively solve this problem. Late chunking requires no additional training and is applicable to a wide range of embedding models. Furthermore, we demonstrate that additional training with a custom method can further enhance its performance on retrieval tasks.
