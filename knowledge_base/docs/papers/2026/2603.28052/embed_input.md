<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Meta-Harness: End-to-End Optimization of Model Harnesses

Topics include Large language models, Classification, Accuracy, Online algorithms, Optimization, Meta-harness, Source code, Language models.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The performance of large language model (LLM) systems depends not only on model weights, but also on their harness: the code that determines what information to store, retrieve, and present to the model. Yet harnesses are still designed largely by hand, and existing text optimizers are poorly matched to this setting because they compress feedback too aggressively. We introduce Meta-Harness, an outer-loop system that searches over harness code for LLM applications. It uses an agentic proposer that accesses the source code, scores, and execution traces of all prior candidates through a filesystem. On online text classification, Meta-Harness improves over a state-of-the-art context management system by 7.7 points while using 4x fewer context tokens. On retrieval-augmented math reasoning, a single discovered harness improves accuracy on 200 IMO-level problems by 4.7 points on average across five held-out models. On agentic coding, discovered harnesses surpass the best hand-engineered baselines on TerminalBench-2. Together, these results show that richer access to prior experience can enable automated harness engineering.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Changing the harness around a fixed large language model (LLM) can produce a 6$\times$ performance gap on the same benchmark. The harness---the code that determines what to store, retrieve, and show to the model---often matters as much as the model itself. This sensitivity has led to growing interest in harness engineering, the practice of refining the code around an LLM to improve the overall system's performance. But despite its importance, harness engineering remains largely manual: practitioners inspect failures, adjust heuristics, and iterate on a small number of designs. In this paper, we ask whether this process itself can be automated.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A natural starting point is recent work on text optimization, since harness engineering also involves iteratively improving text and code artifacts using feedback from prior attempts. However, these methods are poorly matched to harness engineering because they typically operate with short-horizon or heavily compressed feedback: some condition only on the current candidate, others rely primarily on scalar scores, and others restrict feedback to short templates or LLM-generated summaries. This is a pragmatic scalability choice, not evidence that longer-range dependencies are uninformative. Harnesses act over long horizons: a single choice about what to store, when to retrieve it, or how to present it can affect behavior many reasoning steps later. Compressed feedback often removes the information needed to trace downstream failures to earlier harness decisions. Across the tasks studied by several representative text optimizers, the available context per optimization step ranges from only 100 to 30,000 tokens (Table 1), far below the diagnostic footprint of harness search. More broadly, work on retrieval and memory-augmented language models suggests that useful context should often be accessed adaptively rather than monolithically packed into a single prompt.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

reflective feedback from rollout traces

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We address this limitation with Meta-Harness, an agentic harness for optimizing harnesses via end-to-end search (Figure 2). Its proposer is a coding agent, i.e., a language-model-based system that can invoke developer tools and modify code. The choice of coding agent (rather than raw LLM) matters because the amount of experience quickly exceeds context limits, so the proposer must decide what to inspect and validate edits through direct interaction with the codebase. Its key design choice is to expose full history through a filesystem, enabling selective diagnosis of raw prior code and execution traces rather than optimization from compressed per-candidate summaries. For every previous candidate harness, the filesystem stores the source code, evaluation scores, and execution traces, which the proposer retrieves via standard operations such as grep and cat rather than ingesting them as a single prompt. In practice, the proposer reads a median of 82 files per iteration in our most demanding setting, referencing over 20 prior candidates per step (Appendix A).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the settings we study, a single evaluation can produce up to 10,000,000 tokens of diagnostic information, roughly three orders of magnitude beyond the largest feedback budgets used in prior text optimization settings (Table 1).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate Meta-Harness on online text classification, mathematical reasoning, and agentic coding. On online text classification, harnesses discovered by Meta-Harness improve over Agentic Context Engineering (ACE, Zhang et al. ) by 7.7 points while using 4$\times$ fewer context tokens, and match the next-best text optimizer's final performance after $60$ proposals with only four (Figure 1). On retrieval-augmented math reasoning, a single discovered harness improves accuracy on 200 IMO-level problems by 4.7 points on average across five held-out models. On TerminalBench-2, the discovered harness surpasses Terminus-KIRA and ranks #1 among all Haiku 4.5 agents.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Meta-Harness: A Harness for Optimizing Harnesses", "weight": 1.0} -->

This section describes Meta-Harness, our outer-loop procedure for searching over task-specific harnesses. Meta-Harness is built on the idea that harness optimization benefits from allowing a proposer to selectively inspect prior code and execution traces via filesystem access, rather than optimizing from lossy summaries or an additional hand-designed search structure. At a high level, it repeatedly proposes, evaluates, and logs new harnesses.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Meta-Harness: A Harness for Optimizing Harnesses", "weight": 1.0} -->

Meta-Harness is itself a harness in the broad sense (hence the name), since it determines what information the proposer model sees during search. Unless otherwise noted, we use *harness* to refer to the task-specific programs being optimized.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Meta-Harness: A Harness for Optimizing Harnesses", "weight": 1.0} -->

Objective. A harness is a stateful program that wraps a language model and determines what context the model sees at each step. The goal is simple: find the harness that makes the underlying model perform best on the target task distribution. Formally, let $M$ denote a fixed language model and $\mathcal{X}$ a task distribution. For a harness $H$ and task instance $x \sim \mathcal{X}$, we execute a rollout trajectory $\tau \sim {p_{M}{(H,x)}}$. The harness constructs prompts for $M$, the model responds, and the harness updates its state after each interaction. A task-specific reward function $r{(\tau,x)}$ scores the trajectory.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Meta-Harness: A Harness for Optimizing Harnesses", "weight": 1.0} -->

When multiple objectives are relevant (e.g., accuracy and context cost), we evaluate candidates under Pareto dominance and report the resulting frontier. In practice, this search has traditionally been carried out by human engineers and researchers, who iteratively refine prompts, context-management rules, and tool-use logic by hand.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Meta-Harness: A Harness for Optimizing Harnesses", "weight": 1.0} -->

Meta-Harness search loop. Meta-Harness uses a single coding-agent proposer with access to a growing filesystem $\mathcal{D}$ that serves as its feedback channel^11^1Based on earlier exploration, we think this workflow only became practical recently, following major improvements in coding-agent capabilities around early 2026.. Here, a coding agent is a language-model-based system that can invoke developer tools and modify code. Unlike prior systems that externalize the improvement logic in a hand-designed search loop, Meta-Harness delegates diagnosis and proposal to the coding agent itself: it decides which prior artifacts to inspect, which failure modes to address, and whether to make a local edit or a more substantial rewrite. Equivalently, the proposer is not a raw next-token model operating on a fixed prompt assembled by the outer loop; it is an agent that retrieves information, navigates prior artifacts, and edits code as part of the search itself. Each evaluated harness contributes a directory containing its source code, scores, and execution traces (such as prompts, tool calls, model outputs, and state updates).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Meta-Harness: A Harness for Optimizing Harnesses", "weight": 1.0} -->

The filesystem is typically far larger than the proposer's context window, so the proposer queries it through terminal tools such as grep and cat rather than ingesting it as a single prompt. At each iteration, the proposer first inspects prior code, scores, and execution traces, then reasons about likely failure modes before generating a new harness.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Meta-Harness: A Harness for Optimizing Harnesses", "weight": 1.0} -->

Meta-Harness maintains a population $\mathcal{H}$ and a Pareto frontier over evaluated harnesses, but imposes no parent-selection rule: the proposer is free to inspect any prior harness and its execution trace when proposing new ones. We run evolution for a fixed number of iterations and perform a final test-set evaluation on the Pareto frontier. This simplicity is deliberate: by leaving diagnosis and edit decisions to the proposer rather than hard-coding search heuristics, Meta-Harness can improve automatically as coding agents become more capable. The proposer never sees test-set results; its only feedback comes from the search set, the subset of task instances used to evaluate candidate harnesses during search and generate the feedback signal for improvement, and from execution traces logged during those search runs.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Meta-Harness: A Harness for Optimizing Harnesses", "weight": 1.0} -->

Advantages of code-space search. Harness optimization occurs in code space, where small changes to retrieval, memory, or prompt-construction logic can affect behavior many steps later, making local search heuristics poorly matched to the problem. By inspecting execution traces, the proposer can often infer *why* a harness failed and which earlier design choices likely contributed to the failure, not just *that* it failed, as illustrated by the search trajectories in Appendices A and A.2. There, we see that the proposer reads broadly across prior code and logs, then uses those traces to identify confounded edits, isolate likely causal changes, and shift toward safer modifications after repeated regressions. The proposer can therefore modify the harness at the level of algorithmic structure, ranging from changes to retrieval, memory, or prompt-construction logic to full program rewrites, rather than filling in templates or applying predefined mutation operators. In practice, it often starts from a strong prior harness, but this is an emergent strategy rather than a hard-coded rule.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Meta-Harness: A Harness for Optimizing Harnesses", "weight": 1.0} -->

Although the search space is large, representing harnesses as programs provides a natural regularization bias: coding models tend to propose coherent algorithms rather than brittle, hard-coded solutions, which biases the search toward reusable context-management procedures. This action space is closely aligned with the read--write--execute workflows on which frontier coding assistants are trained.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Meta-Harness: A Harness for Optimizing Harnesses", "weight": 1.0} -->

Practical implementation. In our experiments, each harness is a single-file Python program that modifies task-specific prompting, retrieval, memory, and orchestration logic. In our experiments, the proposer $P$ is Claude Code with Opus-4.6. The proposer is guided by a minimal domain-specific skill that describes where to write new harnesses, how to inspect previous harnesses and their execution traces, and what files it can and cannot modify. The base model $M$ varies by domain and is always frozen; see Section 4 for details. In our experiments, a typical run evaluates roughly 60 harnesses over 20 iterations. We provide additional tips for implementing Meta-Harness in a new domain in Appendix D.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Meta-Harness: A Harness for Optimizing Harnesses", "weight": 1.0} -->

1:Input: tasks 𝒳, LLM M, proposer P, iterations N
2:Initialize: population ℋ ⊳ Initial set of valid harnesses
3:Initialize: filesystem 𝒟 ← ⌀ ⊳ stores code, scores, traces
8: Proposer P queries filesystem 𝒟 ⊳ inspects prior harnesses and scores
9: Proposer P proposes k new harnesses {H1, …, Hk}
11: if H passes interface validation then
13:return Pareto frontier of harnesses stored in 𝒟
Algorithm 1 Meta-Harness outer loop over harnesses

<!-- chunk {"id": "body-0020", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate Meta-Harness on three task domains: online text classification, math reasoning, and agentic coding. In each domain, we compare harnesses discovered by our search against domain-appropriate baselines using the standard evaluation metric. Please refer to each subsection for the precise experimental setup.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Experiments", "weight": 1.0} -->

We compare against two main classes of methods. Human-designed strategies: these are hand-crafted harnesses for each domain, representing the current state of the art in context construction. We describe these baselines in the corresponding subsections. Program-search methods: these methods search over candidate harnesses using feedback and reward signals, but are designed for smaller-scale settings than harness engineering.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Online Text Classification", "weight": 1.0} -->

We follow the online text classification setup of Zhang et al.; Ye et al.: an LLM receives labeled examples one at a time, updates its memory, and is evaluated on a held-out test set. We use GPT-OSS-120B as the LLM text classifier, and consider the problem of designing a harness for text classification. We use three datasets, chosen for difficulty and domain diversity: LawBench (Law) predicts criminal charges from case descriptions (215 classes); Symptom2Disease (S2D) predicts diseases from symptom descriptions (22 classes); and USPTO-50k \[40 definitive guide to reaction role assignment")\] predicts precursor reactants from product molecules (180 classes). We initialize the search population $\mathcal{H}$ from the main baseline harnesses in this setting: zero-shot, few-shot, ACE, and MCE. We ran 20 evolution iterations with two candidates per iteration, producing 40 candidate harnesses.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Online Text Classification", "weight": 1.0} -->

Comparison vs text optimizers. We compare Meta-Harness against representative methods for optimizing text. For a fair comparison, we use the same proposer configuration (Opus-4.6 with max reasoning), select candidates solely based on search-set performance, and hold out the test sets until the final evaluation. Since evaluation is the main computational bottleneck, we give each method the same budget of proposal harness evaluations.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Online Text Classification", "weight": 1.0} -->

Best-of-N: independent samples from the seed with no search structure; a compute-matched control for whether search matters at all.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Online Text Classification", "weight": 1.0} -->

OpenEvolve: evolutionary search over programs with LLM mutation.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Online Text Classification", "weight": 1.0} -->

TTT-Discover: we use only the text-optimization component of their method, i.e., proposal selection via the PUCT reuse rule.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Online Text Classification", "weight": 1.0} -->

In this setting, Meta-Harness matches the best prior text optimizers (OpenEvolve, TTT-Discover) in $0.1 \times$ the evaluations, and its final accuracy surpasses theirs by more than 10 points (Figures 1 and 4). We attribute this speedup to the intentional design choices that impose minimum necessary structure on the outer loop (Section 3). In particular, Meta-Harness preserves full experience history using a filesystem and allows the proposer to inspect anything necessary, whereas both OpenEvolve and TTT-Discover operate with more structured and substantially more limited proposer inputs than full filesystem access. We note that online text classification is the smallest-context setting we study (Table 1), so if structure-heavy text optimizers already lag here, their limitations may only grow in harder regimes.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Online Text Classification", "weight": 1.0} -->

To isolate which parts of the proposer interface matter most, we compare three conditions in online text classification: a scores-only condition, a scores-plus-summary condition in which the proposer receives LLM-generated summaries but no raw traces, and the full Meta-Harness interface with access to execution traces (Table 3). The results show a large gap in favor of the full interface: scores-only reaches 34.6 median and 41.3 best accuracy, while scores-plus-summary reaches 34.9 median and 38.7 best. By contrast, Meta-Harness reaches 50.0 median and 56.7 best accuracy, and even its median candidate outperforms the best candidate found under either ablation. We interpret this as evidence that full access to execution traces is the most important component of the interface: summaries do not recover the missing signal, and may even hurt by compressing away diagnostically useful details.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Online Text Classification", "weight": 1.0} -->

Comparison vs state-of-the-art harnesses. Our primary points of comparison are hand-designed harnesses for this problem setting: Agentic Context Engineering (ACE, Zhang et al. ), which uses reflective memory curation to build context over time, and Meta Context Engineering (MCE, Ye et al. ), which maintains and evolves a library of natural-language skills for context construction. As additional baselines, we evaluate zero-shot prompting and few-shot prompting with $N \in {\{ 4,8,16,32,\text{all}\}}$ examples. Results in Table 2 show that Meta-Harness improves substantially over prior hand-designed harnesses. The selected Meta-Harness^22^2We slightly overload terminology for brevity: in the tables, Meta-Harness denotes the best discovered harness, whereas elsewhere it refers to the entire harness search procedure. reaches 48.6% accuracy, outperforming ACE by 7.7 points and MCE by 8.6 points. These gains do not come from using more context: Meta-Harness uses only 11.4K context tokens, versus 50.8K for ACE and 28.5K for MCE.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Online Text Classification", "weight": 1.0} -->

Accuracy--Context Tradeoffs. Because Meta-Harness performs free-form optimization over harness code, we can express a joint preference for both accuracy and context cost rather than committing to a single scalar objective in advance. Given only the current metrics and the desired trade-off, the proposer is able to discover harnesses across a broad range of the frontier, yielding a smooth accuracy--context Pareto curve in Figure 3. This allows us to trade additional context for higher test accuracy in a controlled way, rather than committing to a single hand-designed operating point.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Online Text Classification", "weight": 1.0} -->

Out-of-distribution (OOD) task evaluation. We evaluate whether the discovered harness generalizes to entirely new datasets unseen during search. We consider nine diverse datasets, and describe them in detail in Section C.1. The selected Meta-Harness system achieves the best average accuracy (73.1%), outperforming ACE (70.2%) and all few-shot baselines (Table 5). Notably, we observe that naively adding more few-shot examples beyond $32$ hurts performance in $7/9$ tasks. Meta-Harness shows the highest performance on 6/9 datasets, suggesting that the discovered harness captures generally effective strategies for text classification rather than overfitting to the specific datasets used during search.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Harnesses for Retrieval-Augmented Reasoning", "weight": 1.0} -->

We study a somewhat non-standard setup for olympiad math solving: augmenting the model with the ability to retrieve examples from a large corpus. There is a good reason to expect retrieval to help mathematical reasoning in principle, because solutions often share reusable proof patterns, so previous reasoning traces contain information that a model may be able to exploit at inference time. Yet retrieval has not become a standard ingredient in this setting, and prior work suggests that it has been much less successful on reasoning-intensive math benchmarks than in more fact-grounded domains. The difficulty is that naive retrieval rarely surfaces the right traces in the right form. This suggests that success depends less on adding retrieval per se than on discovering the right retrieval policy. Rather than hand-designing that policy, we give Meta-Harness a hard set of olympiad problems and allow the retrieval behavior itself to emerge from search.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Harnesses for Retrieval-Augmented Reasoning", "weight": 1.0} -->

The retrieval corpus contains $\geq$`<!-- -->`{=html}500,000 solved problems from eight open-source datasets. We carefully deduplicated and decontaminated it against both evaluation benchmarks and the search set, confirmed that held-out problems have no exact prefix matches under our string-based filter, and manually inspected top retrievals for held-out examples (Section C.2). We use Meta-Harness to optimize a harness for 40 iterations over a 250-problem search set of Olympiad-difficulty math problems (OlympiadBench + Omni-MATH hard), producing 109 candidate retrieval harnesses. We initialize the search population $\mathcal{H}$ from the main baseline harnesses in this setting: zero-shot, few-shot, and ACE. We select a single harness based on search-set performance using GPT-OSS-20B (Section B.2). We evaluate this harness on $200$ previously unseen IMO-level problems drawn from IMO-AnswerBench, IMO-ProofBench, and ArXivMath.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Harnesses for Retrieval-Augmented Reasoning", "weight": 1.0} -->

In addition to GPT-OSS-20B, we evaluate the same retrieval harness on four models not seen during search: GPT-5.4-nano, GPT-5.4-mini, Gemini-3.1-Flash-Lite, and Gemini-3-Flash. We follow the standard evaluation protocol of prior work and report accuracy averaged over three samples per problem.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Harnesses for Retrieval-Augmented Reasoning", "weight": 1.0} -->

Results. Table 6 compares the discovered harness against no retrieval, dense retrieval using the separate embedding model text-embedding-3-small, random few-shot prompting, and retrieval. In contrast, Meta-Harness operates entirely in code space on top of the same -based lexical retrieval stack as the sparse baseline, rather than introducing an additional dense encoder. The discovered retrieval harness outperforms the no-retrieval baseline across all five held-out models, with an average gain of 4.7 points. It also matches or exceeds the strongest fixed baselines on average, outperforming retrieval by 1.3 points overall, while avoiding the regressions observed with dense retrieval and random few-shot prompting across several models.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Evaluating Agentic Coding Harnesses on TerminalBench-2", "weight": 1.0} -->

TerminalBench-2 evaluates LLM agents on 89 challenging tasks that require long-horizon, fully autonomous execution under complex dependencies, and substantial domain knowledge. Prior work has shown that the choice agent harness has a large effect on performance on this benchmark. We initialize search from two strong open baselines, Terminus 2 and Terminus-KIRA. For this experiment, we perform search and final evaluation on the same 89-task benchmark. We use this benchmark as a discovery problem in which the goal is to discover a harness configuration that improves performance on a hard, publicly contested benchmark. This is standard practice: public writeups already describe repeated benchmark-specific harness iteration on TerminalBench itself \[17; 33"); 24\], and the benchmark is small and expensive enough that introducing a separate split would materially weaken the search signal. We additionally check for overfitting by manual inspection and regex-based audits for task-specific string leakage into evolved harnesses.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Evaluating Agentic Coding Harnesses on TerminalBench-2", "weight": 1.0} -->

We note that although the resulting harness is specialized to the TerminalBench-2 regime, autonomous completion of difficult long-horizon tasks from a single instruction is a core capability, and the benchmark consists of many tasks that frontier models and heavily engineered harnesses struggle.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Evaluating Agentic Coding Harnesses on TerminalBench-2", "weight": 1.0} -->

Results. We report results on the full benchmark in Table 7, evaluated on two base models: Claude Opus 4.6 and Claude Haiku 4.5. On Opus 4.6, Meta-Harness discovers a harness achieving 76.4% pass rate, surpassing the hand-engineered Terminus-KIRA (74.7%) and ranking #2 among all Opus 4.6 agents on the TerminalBench-2 leaderboard. The only higher-scoring Opus 4.6 agent is ForgeCode (81.8%); however, we were unable to reproduce their reported result from the publicly available code alone, suggesting their leaderboard scores depend on components beyond the published repository. On the weaker Haiku 4.5 model, the improvement is larger: Meta-Harness achieves 37.6%, outperforming the next-best reported agent (Goose, 35.5%) by 2.1 points. TerminalBench-2 is an actively contested benchmark with multiple teams directly optimizing for it, so the fact that an automatic search method can achieve benefits at this frontier is encouraging for long-horizon text-optimization loops.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Evaluating Agentic Coding Harnesses on TerminalBench-2", "weight": 1.0} -->

Qualitative behavior of the proposer. The harness search trajectory helps explain why Meta-Harness achieves these gains; we provide a detailed summary in Appendix A. In early iterations, the proposer combined plausible structural fixes with prompt-template edits and observed that both candidates regressed. It then explicitly hypothesized that the regressions were confounded by the shared prompt intervention, isolated the structural changes from the prompt rewrite, and ultimately pivoted toward a safer additive modification that became the best candidate in the run. This provides qualitative evidence that filesystem access enables the proposer to inspect prior experience in enough detail to form causal hypotheses and revise the harness accordingly.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Discussion", "weight": 1.5} -->

Beyond outperforming existing harnesses, Meta-Harness has several practical advantages. Discovered harnesses generalize to out-of-distribution classification datasets (Table 5) and to unseen base models in the math setting (Table 6). A search run completes in a few hours of wall-clock time, yet produces readable, transferable strategies that can be reused across models, including future, stronger ones. Overfitting in code space is also more inspectable: brittle if-chains or hard-coded class mappings are visible on inspection in a way that weight-space overfitting is not. More broadly, our results suggest that the main advantage of Meta-Harness is not just search over code, but search with *selective access to prior diagnostic experience*. The proposer is not limited to scalar rewards or fixed summaries; it can inspect raw code, execution traces, and prior failures, then use that information to form and test hypotheses about what to change. The qualitative search trajectories in Section A.2 illustrate this behavior directly.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Discussion", "weight": 1.5} -->

Our findings reflect a recurring pattern in machine learning: once a search space becomes accessible, stronger general-purpose agents can outperform hand-engineered solutions. A natural next step for future work is to co-evolve the harness and the model weights, letting the strategy shape what the model learns and vice versa. While we evaluate on three diverse domains, our experiments demonstrate that harness search can work with one particularly strong coding-agent proposer (Claude Code); a broader study of how the effect varies across proposer agents remains for future work.
