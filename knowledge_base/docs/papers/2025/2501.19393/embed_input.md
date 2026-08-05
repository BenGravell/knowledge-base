<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

s1: Simple Test-time Scaling

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Test-time scaling is a promising new approach to language modeling that uses extra test-time compute to improve performance. Recently, OpenAI's o1 model showed this capability but did not publicly share its methodology, leading to many replication efforts. We seek the simplest approach to achieve test-time scaling and strong reasoning performance. First, we curate a small dataset s1K of 1,000 questions paired with reasoning traces relying on three criteria we validate through ablations: difficulty, diversity, and quality. Second, we develop budget forcing to control test-time compute by forcefully terminating the model's thinking process or lengthening it by appending "Wait" multiple times to the model's generation when it tries to end. This can lead the model to double-check its answer, often fixing incorrect reasoning steps. After supervised finetuning the Qwen2.5-32B-Instruct language model on s1K and equipping it with budget forcing, our model s1-32B exceeds o1-preview on competition math questions by up to 27% (MATH and ).

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Further, scaling s1-32B with budget forcing allows extrapolating beyond its performance without test-time intervention: from 50% to 57% . Our model, data, and code are open-source at

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Performance improvements of language models (LMs) over the past years have largely relied on scaling up train-time compute using large-scale self-supervised pretraining. The creation of these powerful models has set the stage for a new scaling paradigm built on top of them: test-time scaling. The aim of this approach is to increase the compute at test time to get better results. There has been much work exploring this idea, and the viability of this paradigm was recently validated by OpenAI o1. o1 has demonstrated strong reasoning performance with consistent gains from scaling test-time compute. OpenAI describes their approach as using large-scale reinforcement learning (RL) implying the use of sizable amounts of data. This has led to various attempts to replicate their models relying on techniques like Monte Carlo Tree Search, multi-agent approaches, and others. Among these approaches, DeepSeek R1 has successfully replicated o1-level performance, also employing reinforcement learning via millions of samples and multiple training stages. However, despite the large number of o1 replication attempts, none have openly replicated a clear test-time scaling behavior. Thus, we ask: what is the simplest approach to achieve both test-time scaling and strong reasoning performance?

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that training on only 1,000 samples with next-token prediction and controlling thinking duration via a simple test-time technique we refer to as budget forcing leads to a strong reasoning model that scales in performance with more test-time compute. Specifically, we construct s1K, which consists of 1,000 carefully curated questions paired with reasoning traces and answers distilled from Gemini Thinking Experimental. We perform supervised fine-tuning (SFT) of an off-the-shelf pretrained model on our small dataset requiring just 26 minutes of training on 16 H100 GPUs. After training, we control the amount of test-time compute our model spends using budget forcing: (I) If the model generates more thinking tokens than a desired limit, we forcefully end the thinking process by appending an end-of-thinking token delimiter. Ending the thinking this way makes the model transition to generating its answer. (II) If we want the model to spend more test-time compute on a problem, we suppress the generation of the end-of-thinking token delimiter and instead append "Wait" to the model's current reasoning trace to encourage more exploration.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Equipped with this simple recipe -- SFT on 1,000 samples and test-time budget forcing -- our model s1-32B exhibits test-time scaling (Figure 1). Further, s1-32B is the most sample-efficient reasoning model and outperforms closed-source models like OpenAI's o1-preview (Figure 2).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We conduct extensive ablation experiments targeting (a) our selection of 1,000 (1K) reasoning samples and (b) our test-time scaling. For (a), we find that jointly incorporating difficulty, diversity, and quality measures into our selection algorithm is important. Random selection, selecting samples with the longest reasoning traces, or only selecting maximally diverse samples all lead to significantly worse performance (around $-$`<!-- -->`{=html}30% on on average). Training on our full data pool of 59K examples, a superset of s1K, does not offer substantial gains over our 1K selection. This highlights the importance of careful data selection and echoes prior findings for instruction tuning. For (b), we define desiderata for test-time scaling methods to compare different approaches. Budget forcing leads to the best scaling as it has perfect controllability with a clear positive slope leading to strong performance.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In summary, our contributions are: We develop simple methods for creating a sample-efficient reasoning dataset (§2) and test-time scaling (§3); Based on these we build s1-32B which is competitive with o1-preview (§4); We ablate subtleties of data (§5.1) and test-time scaling (§5.2). We end with a discussion to motivate future work on simple reasoning (§6). Our code, model, and data are open-source at Figure 2: s1K and s1-32B. (left) s1K is a dataset of 1,000 high-quality, diverse, and difficult questions with reasoning traces. (right) s1-32B, a 32B parameter model finetuned on s1K is on the sample-efficiency frontier. See LABEL:tab:perf for details on other models.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Reasoning data curation to create s1K", "weight": 1.0} -->

In this section, we describe our process for creating a large dataset first in §2.1 and then filtering it down to s1K in §2.2.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Initial collection of 59K samples", "weight": 1.0} -->

We collect an initial 59,029 questions from 16 sources following three guiding principles. Quality: Datasets should be high-quality; we always inspect samples and ignore datasets, e.g., poor formatting; Difficulty: Datasets should be challenging and require significant reasoning effort; Diversity: Datasets should stem from various fields to cover different reasoning tasks.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Curation of existing datasets", "weight": 1.0} -->

Our largest source is NuminaMATH with 30,660 mathematical problems from online websites. We also include historical AIME problems. To enhance diversity, we add OlympicArena with 4,250 questions spanning Astronomy, Biology, Chemistry, Computer Science, Geography, Mathematics, and Physics from various Olympiads. OmniMath adds 4,238 competition-level mathematics problems. We also include 2,385 problems from AGIEval, which features questions from standardized tests like SAT and LSAT, covering English, Law, and Logic. We refer to Table 7 in §C for our other sources.

<!-- chunk {"id": "body-0012", "role": "body", "section": "New datasets in quantitative reasoning", "weight": 1.0} -->

To complement these existing datasets, we create two original datasets. s1-prob consists of 182 questions from the probability section of Stanford University's Statistics Department's PhD Qualifying Exams, accompanied by handwritten solutions that cover difficult proofs. The probability qualifying exam is held yearly and requires professional-level mathematical problem-solving. s1-teasers comprises 23 challenging brain-teasers commonly used in interview questions for quantitative trading positions. Each sample consists of a problem and solution taken from PuzzledQuant. We only take examples with the highest difficulty level ("Hard").

<!-- chunk {"id": "body-0013", "role": "body", "section": "New datasets in quantitative reasoning", "weight": 1.0} -->

For each question, we generate a reasoning trace and solution using the Google Gemini Flash Thinking API extracting its reasoning trace and response. This yields 59K triplets of a question, generated reasoning trace, and generated solution. Examples from our dataset are in §D.2. We decontaminate all samples against our evaluation questions (MATH500, GPQA Diamond §C.5) using 8-grams and deduplicate the data.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Final selection of 1K samples", "weight": 1.0} -->

We could directly train on our pool of 59K questions, however, our goal is to find the simplest approach with minimal resources. Thus, we go through three stages of filtering to arrive at a minimal set of 1,000 samples relying on our three guiding data principles: Quality, Difficulty, and Diversity.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Quality", "weight": 1.0} -->

We first remove any questions where we ran into any API errors reducing our dataset to 54,116 samples. Next, we filter out low-quality examples by checking if they contain any string patterns with formatting issues, such as ASCII art diagrams, non-existent image references, or inconsistent question numbering reducing our dataset to 51,581 examples. From this pool, we identify 384 samples for our final 1,000 samples from datasets that we perceive as high-quality and not in need of further filtering (see §C.4 for details).

<!-- chunk {"id": "body-0016", "role": "body", "section": "Difficulty", "weight": 1.0} -->

For difficulty, we use two indicators: model performance and reasoning trace length. We evaluate two models on each question: Qwen2.5-7B-Instruct and Qwen2.5-32B-Instruct, with correctness assessed by Claude 3.5 Sonnet comparing each attempt against the reference solution (see §C.3 for the grading protocol). We measure the token length of each reasoning trace to indicate problem difficulty using the Qwen2.5 tokenizer. This relies on the assumption that more difficult problems require more thinking tokens. Based on the grading, we remove questions that either Qwen2.5-7B-Instruct or Qwen2.5-32B-Instruct can solve correctly and thus may be too easy. By using two models we reduce the likelihood of an easy sample slipping through our filtering due to a rare mistake on an easy question of one of the models. This brings our total samples down to 24,496, setting the stage for the next round of subsampling based on diversity.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Difficulty", "weight": 1.0} -->

While filtering with these two models may be optimized for our setup as we will also use Qwen2.5-32B-Instruct as our model to finetune, the idea of model-based filtering generalizes to other setups.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Diversity", "weight": 1.0} -->

To quantify diversity, we classify questions into domains using Claude 3.5 Sonnet based on the Mathematics Subject Classification (MSC) system (e.g., geometry, combinatorics, etc.) from the American Mathematical Society.^11^1 The taxonomy focuses on topics in mathematics but also includes other sciences such as biology, physics, and economics. To select our final examples from the pool of 24,496 questions, we first choose one domain uniformly at random. Then, we sample one problem from this domain according to a distribution that favors longer reasoning traces (see §C.4 for details) as motivated in Difficulty. We repeat this process until we have 1,000 total samples spanning 50 domains.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Diversity", "weight": 1.0} -->

In §5.1, we will show that using our three criteria in combination is important, as only relying on quality, diversity, or difficulty in isolation leads to worse datasets. Some distilled generations are incorrect, which we allow in our data as we focus on capturing the reasoning process rather than entirely correct solutions. Our grader (§C.3) deems 53.6% correct in s1K and 63.0% in our follow-up s1K-1.1 (see §A).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Method", "weight": 1.0} -->

We classify test-time scaling methods into 1) Sequential, where later computations depend on earlier ones (e.g., a long reasoning trace), and 2) Parallel, where computations run independently (e.g., majority voting). We focus on sequential scaling as intuitively we believe it should scale better, since later computations can build on intermediate results, allowing for deeper reasoning and iterative refinement. We propose new sequential scaling methods and ways to benchmark them.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Budget forcing", "weight": 1.0} -->

We propose a simple decoding-time intervention by forcing a maximum and/or minimum number of thinking tokens. Specifically, we enforce a maximum token count by simply appending the end-of-thinking token delimiter and optionally "Final Answer:" to early exit the thinking stage and make the model provide its current best answer. To enforce a minimum, we suppress the generation of the end-of-thinking token delimiter and optionally append the string "Wait" to the model's current reasoning trace to encourage the model to reflect on its current generation. Figure 3 contains an example of how this simple approach can lead the model to arrive at a better answer.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Baselines", "weight": 1.0} -->

We benchmark budget forcing: (I) Conditional length-control methods, which rely on telling the model in the prompt how long it should generate. We group them by granularity into (a) Token-conditional control: We specify an upper bound of thinking tokens in the prompt; (b) Step-conditional control: We specify an upper bound of thinking steps, where each step is around 100 tokens; (c) Class-conditional control: We write two generic prompts that tell the model to either think for a short or long amount of time (see §E.1 for details). (II) Rejection sampling, which samples until a generation fits a predetermined compute budget. This oracle captures the posterior over responses conditioned on its length.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Metrics", "weight": 1.0} -->

We establish a set of desiderata as evaluation metrics to measure test-time scaling across methods. Importantly, we do not only care about the accuracy a method can achieve but also its controllability and test-time scaling slope. For each method we consider, we run a set of evaluations $a \in \mathcal{A}$ varying test-time compute on a fixed benchmark, e.g.. This produces a piece-wise linear function $f$ with compute as the x-axis measured in thinking tokens and accuracy as the y-axis (see Figure 1, where the rightmost dot for corresponds to ${f{}} = {57\%}$). We measure three metrics: where $a_{\text{min}},a_{\text{max}}$ refer to a pre-specified minimum and maximum amount of test-time compute; in our case thinking tokens. We usually only constrain $a_{\text{max}}$. As tokens generated correspond to the amount of test-time compute spent, this metric measures the extent to which a method allows controllability over the use of that test-time compute.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Metrics", "weight": 1.0} -->

We report it as a percentage with 100% being perfect control.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Metrics", "weight": 1.0} -->

Scaling is the average slope of the piece-wise linear function. It must be positive for useful methods and larger is better.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Metrics", "weight": 1.0} -->

Performance is simply the maximum performance the method achieves on the benchmark. A method with monotonically increasing scaling achieves 100% performance on any benchmark in the limit. However, the methods we investigate eventually flatten out or further scaling fails due to control or context window limitations.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Metrics", "weight": 1.0} -->

(a) Sequential scaling via budget forcing (b) Parallel scaling via majority voting Figure 4: Sequential and parallel test-time scaling. (a): Budget forcing shows clear scaling trends and extrapolates to some extent. For the three rightmost dots, we prevent the model from stopping its thinking 2/4/6 times, each time appending “Wait” to its current reasoning trace. (b): For Qwen2.5-32B-Instruct we perform 64 evaluations for each sample with a temperature of 1 and visualize the performance when majority voting across 2, 4, 8, 16, 32, and 64 of these.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Training", "weight": 1.0} -->

We perform supervised finetuning on Qwen2.5-32B-Instruct using s1K to obtain our model s1-32B using basic hyperparameters outlined in §D. Finetuning took 26 minutes on 16 NVIDIA H100 GPUs with PyTorch FSDP.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Evaluation", "weight": 1.0} -->

We select three representative reasoning benchmarks widely used in the field: has 30 problems that were used in the 2024 American Invitational Mathematics Examination (AIME) held from January 31 -- February 1, 2024. AIME tests mathematical problem-solving with arithmetic, algebra, counting, geometry, number theory, probability, and other secondary school math topics. High-scoring high school students in the test are invited to participate in the United States of America Mathematics Olympiad (USAMO). All AIME answers are integers ranging from $000$ to $999$, inclusive. Some AIME problems rely on figures that we provide to our model using the vector graphics language Asymptote as it cannot take image inputs. MATH500 is a benchmark of competition math problems of varying difficulty. We evaluate on the same 500 samples selected by OpenAI in prior work. GPQA Diamond consists of 198 PhD-level science questions from Biology, Chemistry and Physics. Experts with PhDs in the corresponding domains only achieved 69.7% on GPQA Diamond. When we write "GPQA" in the context of evaluation in this work, we always refer to the Diamond subset. We build on the "lm-evaluation-harness" framework.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Unless otherwise specified, we evaluate with a temperature of 0 (greedy) and measure accuracy (equivalent to pass@1).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Other models", "weight": 1.0} -->

We benchmark s1-32B against: OpenAI o1 series, closed-source models that popularized test-time scaling; DeepSeek r1 series, open-weight reasoning models with up to o1-level performance; Qwen's QwQ-32B-preview, a 32B open-weight reasoning model without disclosed methodology; Sky-T1-32B-Preview and Bespoke-32B, open models with open reasoning data distilled from QwQ-32B-preview and r1; Google Gemini 2.0 Flash Thinking Experimental, the API that we distill. As it has no official evaluation scores, we use the Gemini API to benchmark it ourselves. However, the "recitation error" of the Gemini API makes evaluation challenging.^22^2 We circumvent this, by manually inserting all 30 questions in its web interface where the error does not appear. However, we leave out MATH500 (500 questions) and GPQA Diamond (198 questions), thus they are N.A. in LABEL:tab:perf. Our model, s1-32B, is fully open including weights, reasoning data, and code.

<!-- chunk {"id": "body-0032", "role": "body", "section": "ex", "weight": 1.0} -->

Open Weights and Open Data Table 1: s1-32B is a strong open reasoning model. We evaluate s1-32B, Qwen, and Gemini (some entries are unknown (N.A.), see §4). Other results are from the respective reports. # ex. = number examples used for reasoning finetuning; BF = budget forcing. See §A for our better s1.1 model.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Sample-efficiency", "weight": 1.0} -->

In Figure 2 (right) and LABEL:tab:perf we compare s1-32B with other models. We find that s1-32B is the most sample-efficient open data reasoning model. It performs significantly better than our base model (Qwen2.5-32B-Instruct) despite just training it on an additional 1,000 samples. The concurrently released r1-32B shows stronger performance than s1-32B while also only using SFT. However, it is trained on 800 $\times$ more reasoning samples. It is an open question whether one can achieve their performance with just 1,000 samples. Finally, our model nearly matches Gemini 2.0 Thinking. As the data for s1-32B is distilled from Gemini 2.0, this shows our distillation procedure was likely effective.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Sample-efficiency", "weight": 1.0} -->

Alice and Bob play the following game. A stack of n tokens lies before them. The players take turns with Alice going first. On each turn, the player removes either 1 token or 4 tokens from the stack. Whoever removes the last token wins. Find the number of positive integers n less than or equal to 2024 for which there exists a strategy for Bob that guarantees that Bob will win the game regardless of Alice’s play. The problem asks for the number of positive integers n ≤ 2024 such that Bob has a winning strategy. This is a typical impartial game that can be analyzed using the Sprague-Grundy theorem or by directly finding the winning and losing positions. Let W be the set of winning positions (number of tokens n such that the player whose turn it is can force a win) and L be the set of losing positions. […] Let P(n) be the statement ”the player whose turn it is when there are n tokens has a winning strategy. P is false (the player whose turn it is and faces 0 tokens has already lost). Consider the small values of n: n = 1: The player whose turn it is can take 1 token and win.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Sample-efficiency", "weight": 1.0} -->

So P is true. 1 ∈ W. n = 2: The player whose turn it is can take 1 token, leaving 1 token for the opponent. Since 1 ∈ W, the opponent wins. So P is false. 2 ∈ L. n = 3: The player whose turn it is can take 1 token, leaving 2 tokens for the opponent. Since 2 ∈ L, the player whose turn it is wins. So P is true. 3 ∈ W.[…] We are looking for the number of positive integers n ≤ 2024 for which Bob has a winning strategy. This means that if the game starts with n tokens, and Alice goes first, Bob can win. This happens if and only if n is a losing position (because if n ∈ L, then Alice’s first move must lead to a winning position for Bob). […] Let’s try to find a pattern in the losing positions L = {0, 2, 5, 7, 10, 12, 15, 17, 20, 22, …}. Differences between consecutive terms: 2, 3, 2, 3, 2, 3, 2, 3, 2, … The pattern of differences is alternating 2, 3.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Sample-efficiency", "weight": 1.0} -->

[…] The losing positions are of the form 5m or 5m + 2, where m ≥ 0. We need to find the number of positive integers n ≤ 2024 that are in the set of losing positions L. […] Case 1: n = 5m, where m ≥ 1. 1 ≤ 5m ≤ 2024 1/5 ≤ m ≤ 2024/5 = 404.8 Since m is an integer, 1 ≤ m ≤ 404. The number of values of m is 404. Case 2: n = 5m + 2, where m ≥ 0. 5m + 2 ≤ 2024 5m ≤ 2022 m ≤ 2022/5 = 404.4 Since m is an integer, 0 ≤ m ≤ 404. The number of values of m is 404 − 0 + 1 = 405. The total number of positive integers n ≤ 2024 that are losing positions is ${404 + 405} = \boxed{809}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Sample-efficiency", "weight": 1.0} -->

[MATH500] Find the projection of a onto $b = \begin{pmatrix} \end{pmatrix}$ if a ⋅ b = 8. The projection of vector a onto vector b is given by the formula: proj_b a = a ⋅b∥b∥2 b We are given $\mathbf{b} = \begin{pmatrix} \end{pmatrix}$ and a ⋅ b = 8. First, we need to find the magnitude squared of b, which is ∥b∥2.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Sample-efficiency", "weight": 1.0} -->

∥b∥^2 = b ⋅b = 2^2 + 6^2 + 3^2 = 4 + 36 + 9 = 49. Now we can plug the values into the projection formula: proj_b a = 849 b Substitute the vector b: proj_b a = 849 (2 6 3) Multiply the scalar by each component of the vector: proj_b a = (849×2 849×6 849×3) = Final Answer: The final answer is $$\begin{pmatrix} [GPQA] A quantum mechanical particle of mass m moves in two dimensions in the following potential, as a function of the polar coordinates (r, θ): V(r, θ) = 12 k r^2 + 32 k r^2 cos^2(θ) Find the energy spectrum. Hint: Write the potential in Cartesian coordinates. The problem asks for the energy spectrum of a particle in a given 2D potential. The potential is given in polar coordinates (r, θ): V(r, θ) = 12 kr^2 + 32 kr^2 cos^2(θ).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Sample-efficiency", "weight": 1.0} -->

We can rewrite the potential as: V(r, θ) = 12 kr^2 (1 + 3cos^2(θ)). The Hamiltonian for a particle in 2D is given: H = -ℏ22m (∂2∂x2 + ∂2∂y2) + V(x, y). In polar coordinates (r, θ), the Laplacian operator is: ∇^2 = 1r ∂∂r (r ∂∂r) + 1r2 ∂2∂θ2. So the Hamiltonian in polar coordinates is: H = -ℏ22m [1r ∂∂r (r ∂∂r) + 1r2 ∂2∂θ2] + V(r, θ). The time-independent Schrödinger equation is Hψ = Eψ. We can try to separate variables by assuming a solution of the form ψ(r, θ) = R(r)Θ(θ). […] This confirms the energy spectrum is: E = ℏkm (2n_x + n_y + 32).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Data Quantity, Diversity, and Difficulty", "weight": 1.0} -->

In §2 we outlined our three guiding principles in curating s1K: Quality, Difficulty, and Diversity. Here we test the importance of combining them and the overall efficacy of our selection. Only Quality (1K-random): After obtaining our high-quality reasoning chains from Gemini, we select 1,000 samples at random; not relying on our difficulty and diversity filtering at all. Table 2 shows this approach performs much worse than s1K across all benchmarks. Only Diversity (1K-diverse): For this dataset, we sample uniformly across domains to maximize diversity disregarding any notion of difficulty. This approach also leads to poor performance similar to 1K-random. Only Difficulty (1K-longest): Here we rely on one of our difficulty indicators introduced in §2 by selecting the 1,000 samples with the longest reasoning traces. This approach significantly boosts GPQA performance but overall still falls short of using s1K. Maximize Quantity: Finally, we compare with just training on all of our 59K samples, a superset of all the 1K-sample versions. This leads to a strong model but uses much more resources.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Data Quantity, Diversity, and Difficulty", "weight": 1.0} -->

To finetune on 59K samples, we use 394 H100 GPU hours while s1-32B only required 7 H100 GPU hours. Moreover, relying only on s1K is extremely competitive as shown in §2. Overall, combining all three criteria -- Quality, Difficulty, Diversity -- via our methodology in §2 is key for sample-efficient reasoning training.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Budget forcing", "weight": 1.0} -->

In Table 3 we compare the test-time scaling methods we have introduced in §3. Overall, we find that budget forcing provides perfect control, good scaling, and leads to our best score. Thus, this is the method we use for s1-32B in Figure 1 and in §4. In Table 4, we compare different strings for extrapolating performance. We find that "Wait" generally gives the best performance.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Budget forcing", "weight": 1.0} -->

Class-conditional control We provide benchmark scores for this method in §E.1 and summarize three findings here: Token-conditional control fails without budget forcing, as our model cannot reliably count tokens - even when trained to do so. Under step-conditional control, the model generates a similar total number of tokens when given different step targets, as the model goes from few steps with many tokens per step, to many steps with few tokens in each step. Thus, the model learns to hack its way around the compute constraint making the controllability of this method mediocre. Class-conditional control can work - telling a model to simply think longer can increase its test-time compute and performance, which leads good scaling in Table 3.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Rejection sampling", "weight": 1.0} -->

Surprisingly, we find that simply sampling until the generation fits a specific length leads to an inverse scaling trend as depicted in Figure 6. In §E.2 we inspect a question, which was answered correctly by the model when rejection sampling for $\leq 4000$, but not for the $\leq 8000$ token setting. In the $\leq 4000$ setting the model directly jumps to the correct approach, while for the $\leq 8000$ setting it backtracks a lot. We hypothesize that there is a correlation such that shorter generations tend to be the ones where the model was on the right track from the start, whereas longer ones tend to be ones where the model made mistakes and thus backtracks or questions itself. This leads to longer samples often being wrong when rejection sampling and thus the inverse scaling trend.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Models", "weight": 1.0} -->

There are a number of concurrent efforts to build models that replicate the performance of o1. For example, DeepSeek-r1 and k1.5 are built with reinforcement learning methods, while others rely on SFT using tens of thousands of distilled examples. We show that SFT on only 1,000 examples suffices to build a competitive reasoning model matching o1-preview and produces a model that lies on the pareto frontier (Figure 2). Further, we introduce budget forcing which combined with our reasoning model leads to the first reproduction of OpenAI's test-time scaling curves. Why does supervised finetuning on just 1,000 samples lead to such performance gains? We hypothesize that the model is already exposed to large amounts of reasoning data during pretraining which spans trillions of tokens. Thus, the ability to perform reasoning is already present in our model. Our sample-efficient finetuning stage just activates it and we scale it further at test time with budget forcing. This is similar to the "Superficial Alignment Hypothesis" presented in LIMA, where the authors find that 1,000 examples can be sufficient to align a model to adhere to user preferences.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Benchmarks and methods", "weight": 1.0} -->

To evaluate and push the limits of these models, increasingly challenging benchmarks have been introduced, such as Olympiad-level science competitions and others. To enhance models' performance on reasoning-related tasks, researchers have pursued several strategies: Prior works have explored continuing training language models on specialized corpora related to mathematics and science, sometimes even synthetically generated data. Others have developed training methodologies specifically aimed at reasoning performance. Another significant line of work focuses on prompting-based methods to elicit and improve reasoning abilities, including methods like Chain-of-Thought prompting. These combined efforts aim to advance the reasoning ability of language models, enabling them to handle more complex and abstract tasks effectively.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Methods", "weight": 1.0} -->

As we introduce in §3, we differentiate two methods to scale test-time compute: parallel and sequential. The former relies on multiple solution attempts generated in parallel and selecting the best outcome via specific criteria. These criteria include choosing the most frequent response for majority voting or the best response based on an external reward for Best-of-N. Unlike repeated sampling, previous sequential scaling methods let the model generate solution attempts sequentially based on previous attempts, allowing it to refine each attempt based on previous outcomes. Tree-based search methods offer a hybrid approach between sequential and parallel scaling, such as Monte-Carlo Tree Search (MCTS) and guided beam search. REBASE employs a process reward model to balance exploitation and pruning during tree search. Empirically, REBASE has been shown to outperform sampling-based methods and MCTS. Reward models play a key role in these methods. They come in two variants: outcome reward models and process reward models. Outcome reward models assign a score to complete solutions and are particularly useful in Best-of-N selection, while process reward models assess individual reasoning steps and are effective in guiding tree-based search methods.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Limits to further test-time scaling", "weight": 1.0} -->

We have shown that budget forcing allows extrapolating test-time compute in §4, e.g., improving performance from 50% to 57%. However, it has two key limitations when scaling further: it eventually flattens out (Figure 4), and the context window of the underlying language model constrains it. Despite these constraints, our work shows test-time scaling across a wide range of accuracies (Figure 1), partly because scaling down test-time compute behaves predictably and does not suffer from these constraints.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Limits to further test-time scaling", "weight": 1.0} -->

Continuing test-time scaling will require approaches that can further extrapolate test-time compute. How can we get such extrapolation? There may be improvements to budget forcing such as rotating through different strings, not only "Wait", or combining it with frequency penalties or higher temperature to avoid repetitive loops. An exciting direction for future work is also researching whether applying budget forcing to a reasoning model trained with reinforcement learning yields better extrapolation; or if RL allows for new ways of test-time scaling beyond budget forcing. Our work defines the right metrics (§3.2) -- Control, Scaling, and Performance -- to enable future research and progress on extrapolating test-time compute.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Parallel scaling as a solution", "weight": 1.0} -->

Parallel scaling offers one solution to the limits of sequential scaling, thus we augment our sequentially scaled model with two methods: (I) Majority voting: After generating $k$ solutions, the final solution is the most frequent one across generations; (II) Tree search via REBASE: We use the REBASE process reward model, which is initialized from LLaMA-34B and further finetuned on a synthetic process reward modeling dataset. We then aggregate the solutions generated by REBASE via majority voting. As shown in Figure 7, augmenting our model with REBASE scales better than majority voting, and even sequential scaling in this scenario. However, REBASE requires an additional forward pass at each step for the reward model adding some computation overhead. For sequential scaling, when prompted to use up to 512 steps, for 12 out of the 30 evaluation questions the model generates a response that exceeds the context window leading to a large performance drop. Overall, we find that these parallel scaling methods complement sequential scaling thus they offer an avenue for scaling test-time compute even further; beyond fixed context windows.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Impact Statement", "weight": 1.0} -->

Language models with strong reasoning capabilities have the potential to greatly enhance human productivity, from assisting in complex decision-making to driving scientific breakthroughs. However, recent advances in reasoning, such as OpenAI's o1 and DeepSeek's r1, lack transparency, limiting broader research progress. Our work aims to push the frontier of reasoning in a fully open manner, fostering innovation and collaboration to accelerate advancements that ultimately benefit society.
