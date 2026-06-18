<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models

Topics include Reinforcement learning, Policy optimization, GRPO, Large language models, Mathematical reasoning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces GRPO (Group Relative Policy Optimization), a memory-efficient RL variant that replaces the PPO critic with group-relative reward normalization. Historically this caused a big buzz in the Machine Learning world because it was used to train DeepSeek R1, an open weights LLM from China that performed nearly as well as leading closed weights LLMs from the USA. Nevertheless, GRPO is very similar to the REINFORCE policy gradient algorithm, c.f. A vision researcher's guide to some RL stuff: PPO & GRPO - Yuge (Jimmy) Shi

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Mathematical reasoning poses a significant challenge for language models due to its complex and structured nature. In this paper, we introduce DeepSeekMath 7B, which continues pre-training DeepSeek-Coder-Base-v1.5 7B with 120B math-related tokens sourced from Common Crawl, together with natural language and code data. DeepSeekMath 7B has achieved an impressive score of 51.7% on the competition-level MATH benchmark without relying on external toolkits and voting techniques, approaching the performance level of Gemini-Ultra and GPT-4. Self-consistency over 64 samples from DeepSeekMath 7B achieves 60.9% on MATH. The mathematical reasoning capability of DeepSeekMath is attributed to two key factors: First, we harness the significant potential of publicly available web data through a meticulously engineered data selection pipeline. Second, we introduce Group Relative Policy Optimization (GRPO), a variant of Proximal Policy Optimization (PPO), that enhances mathematical reasoning abilities while concurrently optimizing the memory usage of PPO.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Large language models (LLM) have revolutionized the approach to mathematical reasoning in artificial intelligence, spurring significant advancements in both the quantitative reasoning benchmark and the geometry reasoning benchmark. Moreover, these models have proven instrumental in assisting humans in solving complex mathematical problems. However, cutting-edge models such as GPT-4 and Gemini-Ultra are not publicly available, and the currently accessible open-source models considerably trail behind in performance.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this study, we introduce DeepSeekMath, a domain-specific language model that significantly outperforms the mathematical capabilities of open-source models and approaches the performance level of GPT-4 on academic benchmarks. To achieve this, we create the DeepSeekMath Corpus, a large-scale high-quality pre-training corpus comprising 120B math tokens. This dataset is extracted from the Common Crawl (CC) using a fastText-based classifier. In the initial iteration, the classifier is trained using instances from OpenWebMath as positive examples, while incorporating a diverse selection of other web pages to serve as negative examples. Subsequently, we employ the classifier to mine additional positive instances from the CC, which are further refined through human annotation. The classifier is then updated with this enhanced dataset to improve its performance. The evaluation results indicate that the large-scale corpus is of high quality, as our base model DeepSeekMath-Base 7B achieves 64.2% on GSM8K and 36.2% on the competition-level MATH dataset, outperforming Minerva 540B.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In addition, the DeepSeekMath Corpus is multilingual, so we notice an improvement in Chinese mathematical benchmarks (Wei et al. Zhong et al., ). We believe that our experience in mathematical data processing is a starting point for the research community, and there is significant room for improvement in the future.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

DeepSeekMath-Base is initialized with DeepSeek-Coder-Base-v1.5 7B, as we notice that starting from a code training model is a better choice compared to a general LLM. Furthermore, we observe the math training also improves model capability on MMLU and BBH benchmarks, indicating it does not only enhance the model's mathematical abilities but also amplifies general reasoning capabilities.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

After pre-training, we apply mathematical instruction tuning to DeepSeekMath-Base with chain-of-thought, program-of-thought (Chen et al. Gao et al., ), and tool-integrated reasoning data. The resulting model DeepSeekMath-Instruct 7B beats all 7B counterparts and is comparable with 70B open-source instruction-tuned models.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Furthermore, we introduce the Group Relative Policy Optimization (GRPO), a variant reinforcement learning (RL) algorithm of Proximal Policy Optimization (PPO). GRPO foregoes the critic model, instead estimating the baseline from group scores, significantly reducing training resources. By solely using a subset of English instruction tuning data, GRPO obtains a substantial improvement over the strong DeepSeekMath-Instruct, including both in-domain (GSM8K: 82.9% $\rightarrow$ 88.2%, MATH: 46.8% $\rightarrow$ 51.7%) and out-of-domain mathematical tasks (e.g., CMATH: 84.6% $\rightarrow$ 88.8%) during the reinforcement learning phase. We also provide a unified paradigm to understand different methods, such as Rejection Sampling Fine-Tuning (RFT), Direct Preference Optimization (DPO), PPO and GRPO. Based on such a unified paradigm, we find that all these methods are conceptualized as either direct or simplified RL techniques. We also conduct extensive experiments, e.g., online v.s. offline training, outcome v.s.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

process supervision, single-turn v.s. iterative RL and so, to deeply investigate the essential elements of this paradigm. At last, we explain why our RL boosts the performance of instruction-tuned models, and further summarize potential directions to achieve more effective RL based on this unified paradigm.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Contributions", "weight": 1.0} -->

Our contribution includes scalable math pre-training, along with the exploration and analysis of reinforcement learning.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Contributions", "weight": 1.0} -->

Our research provides compelling evidence that the publicly accessible Common Crawl data contains valuable information for mathematical purposes. By implementing a meticulously designed data selection pipeline, we successfully construct the DeepSeekMath Corpus, a high-quality dataset of 120B tokens from web pages filtered for mathematical content, which is almost 7 times the size of the math web pages used by Minerva and 9 times the size of the recently released OpenWebMath.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Contributions", "weight": 1.0} -->

Our pre-trained base model DeepSeekMath-Base 7B achieves comparable performance with Minerva 540B, indicating the number of parameters is not the only key factor in mathematical reasoning capability. A smaller model pre-trained on high-quality data could achieve strong performance as well.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Contributions", "weight": 1.0} -->

We share our findings from math training experiments. Code training prior to math training improves models' ability to solve mathematical problems both with and without tool use. This offers a partial answer to the long-standing question: does code training improve reasoning abilities? We believe it does, at least for mathematical reasoning.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Contributions", "weight": 1.0} -->

Although training on arXiv papers is common, especially in many math-related papers, it brings no notable improvements on all mathematical benchmarks adopted in this paper.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Contributions", "weight": 1.0} -->

Exploration and Analysis of Reinforcement Learning

<!-- chunk {"id": "body-0017", "role": "body", "section": "Contributions", "weight": 1.0} -->

We introduce Group Relative Policy Optimization (GRPO), an efficient and effective reinforcement learning algorithm. GRPO foregoes the critic model, instead estimating the baseline from group scores, significantly reducing training resources compared to Proximal Policy Optimization (PPO).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Contributions", "weight": 1.0} -->

We demonstrate that GRPO significantly enhances the performance of our instruction-tuned model DeepSeekMath-Instruct, by solely using the instruction-tuning data. Furthermore, we observe enhancements in the out-of-domain performance during the reinforcement learning process.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Contributions", "weight": 1.0} -->

We provide a unified paradigm to understand different methods, such as RFT, DPO, PPO, and GRPO. We also conduct extensive experiments, e.g., online v.s. offline training, outcome v.s. process supervision, single-turn v.s. iterative reinforcement learning, and so on to deeply investigate the essential elements of this paradigm.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Contributions", "weight": 1.0} -->

Based on our unified paradigm, we explore the reasons behind the effectiveness of reinforcement learning, and summarize several potential directions to achieve more effective reinforcement learning of LLMs.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Summary of Evaluations and Metrics", "weight": 1.0} -->

English and Chinese Mathematical Reasoning: We conduct comprehensive assessments of our models on English and Chinese benchmarks, covering mathematical problems from grade-school level to college level. English benchmarks include GSM8K, MATH, SAT, OCW Courses, MMLU-STEM. Chinese benchmarks include MGSM-zh, CMATH, Gaokao-MathCloze, and Gaokao-MathQA. We evaluate models' ability to generate self-contained text solutions without tool use, and also the ability to solve problems using Python.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Summary of Evaluations and Metrics", "weight": 1.0} -->

On English benchmarks, DeepSeekMath-Base is competitive with the closed-source Minerva 540B, and surpasses all open-source base models (e.g., Mistral 7B and Llemma-34B ), regardless of whether they've undergone math pre-training or not, often by a significant margin. Notably, DeepSeekMath-Base is superior on Chinese benchmarks, likely because we don't follow previous works to collect English-only math pre-training data, and also include high-quality non-English ones. With mathematical instruction tuning and reinforcement learning, the resulting DeepSeekMath-Instruct and DeepSeekMath-RL demonstrate strong performance, obtaining an accuracy of over 50% on the competition-level MATH dataset for the first time within the open-source community.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Summary of Evaluations and Metrics", "weight": 1.0} -->

Formal Mathematics: We evaluate DeepSeekMath-Base using the informal-to-formal theorem proving task from on miniF2F with Isabelle chosen to be the proof assistant. DeepSeekMath-Base demonstrates strong few-shot autoformalization performance.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Summary of Evaluations and Metrics", "weight": 1.0} -->

Natural Language Understanding, Reasoning, and Code: To build a comprehensive profile of models' general understanding, reasoning, and coding capabilities, we evaluate DeepSeekMath-Base on the Massive Multitask Language Understanding (MMLU) benchmark which encompasses 57 multiple-choice tasks covering diverse subjects, BIG-Bench Hard (BBH) which consists of 23 challenging tasks that mostly require multi-step reasoning to solve, as well as HumanEval and MBPP which are widely used to evaluate code language models. Math pre-training benefits both language understanding and reasoning performance.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Data Collection and Decontamination", "weight": 1.0} -->

In this section, we will outline the process of constructing the DeepSeekMath Corpus from Common Crawl. As depicted in Figure, we present an iterative pipeline that demonstrates how to systematically gather a large-scale mathematical corpus from Common Crawl, starting with a seed corpus (e.g., a small but high-quality collection of math-related dataset). It's worth noting that this approach is also applicable to other domains, such as coding.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Data Collection and Decontamination", "weight": 1.0} -->

First, we choose OpenWebMath, a collection of high-quality mathematical web texts, as our initial seed corpus. Using this corpus, we train a fastText model to recall more OpenWebMath-like mathematical web pages. Specifically, we randomly select 500,000 data points from the seed corpus as positive training examples and another 500,000 web pages from Common Crawl as negative ones. We employ an open-source library^11^1 for training, configuring the vector dimension to 256, learning rate to 0.1, the maximum length of word n-gram to 3, the minimum number of word occurrences to 3, and the number of training epochs to 3. To reduce the size of the original Common Crawl, we employ URL-based deduplication and near-deduplication techniques, resulting in 40B HTML web pages. We then recall mathematical web pages from deduplicated Common Crawl with the fastText model. To filter out low-quality mathematical content, we rank the collected pages according to their scores predicted by the fastText model, and only preserve the top-ranking ones.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Data Collection and Decontamination", "weight": 1.0} -->

The volume of data preserved is assessed through pre-training experiments on the top 40B, 80B, 120B, and 160B tokens. In the first iteration, we choose to keep the top 40B tokens.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Data Collection and Decontamination", "weight": 1.0} -->

After the first iteration of data collection, numerous mathematical web pages remain uncollected, mainly because the fastText model is trained on a set of positive examples that lacks sufficient diversity. We therefore identify additional mathematical web sources to enrich the seed corpus, so that we can optimize the fastText model. Specifically, we first organize the entire Common Crawl into disjoint domains; a domain is defined as web pages sharing the same base URL. For each domain, we calculate the percentage of web pages that are collected in the first iteration. Domains where over 10% of the web pages have been collected are classified as math-related (e.g., mathoverflow.net). Subsequently, we manually annotate the URLs associated with mathematical content within these identified domains (e.g., mathoverflow.net/questions). Web pages linked to these URLs, yet uncollected, will be added to the seed corpus. This approach enables us to gather more positive examples, thereby training an improved fastText model capable of recalling more mathematical data in the subsequent iteration. After four iterations of data collection, we end up with 35.5M mathematical web pages, totaling 120B tokens.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Data Collection and Decontamination", "weight": 1.0} -->

In the fourth iteration, we notice that nearly 98% of the data has already been collected in the third iteration, so we decide to cease data collection.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Data Collection and Decontamination", "weight": 1.0} -->

To avoid benchmark contamination, we follow Guo et al. to filter out web pages containing questions or answers from English mathematical benchmarks such as GSM8K and MATH and Chinese benchmarks such as CMATH and AGIEval. The filtering criteria are as follows: any text segment containing a 10-gram string that matches exactly with any sub-string from the evaluation benchmarks is removed from our math training corpus. For benchmark texts that are shorter than 10 grams but have at least 3 grams, we employ exact matching to filter out contaminated web pages.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Validating the Quality of the DeepSeekMath Corpus", "weight": 1.0} -->

MathPile: a multi-source corpus (8.9B tokens) aggregated from textbooks, Wikipedia, ProofWiki, CommonCrawl, StackExchange, and arXiv, with the majority (over 85%) sourced from arXiv;

<!-- chunk {"id": "body-0032", "role": "body", "section": "Validating the Quality of the DeepSeekMath Corpus", "weight": 1.0} -->

OpenWebMath: CommonCrawl data filtered for mathematical content, totaling 13.6B tokens;

<!-- chunk {"id": "body-0033", "role": "body", "section": "Validating the Quality of the DeepSeekMath Corpus", "weight": 1.0} -->

Proof-Pile-2: a mathematical corpus consisting of OpenWebMath, AlgebraicStack (10.3B tokens of mathematical code), and arXiv papers (28.0B tokens). When experimenting on Proof-Pile-2, we follow Azerbayev et al. to use an arXiv:Web:Code ratio of 2:4:1.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Training Setting", "weight": 1.0} -->

We apply math training to a general pre-trained language model with 1.3B parameters, which shares the same framework as the DeepSeek LLMs, denoted as DeepSeek-LLM 1.3B. We separately train a model on each mathematical corpus for 150B tokens. All experiments are conducted using the efficient and light-weight HAI-LLM training framework. Following the training practice of DeepSeek LLMs, we use the AdamW optimizer with $\beta_{1} = 0.9$, $\beta_{2} = 0.95$, and ${{weight}\_{decay}} = 0.1$, along with a multi-step learning rate schedule where the learning rate reaches the peak after 2,000 warmup steps, decreases to its 31.6% after 80% of the training process, and further decreases to 10.0% of the peak after 90% of the training process. We set the maximum value of learning rate to 5.3e-4, and use a batch size of 4M tokens with a 4K context length.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Training Setting", "weight": 1.0} -->

corpora, evaluated using few-shot chain-of-thought prompting. Corpus sizes are calculated using our tokenizer with a vocabulary size of 100K.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Evaluation Results", "weight": 1.0} -->

The DeepSeekMath Corpus is of high quality, covers multilingual mathematical content, and is the largest in size.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Evaluation Results", "weight": 1.0} -->

High-quality: We evaluate downstream performance on 8 mathematical benchmarks using few-shot chain-of-thought prompting Wei et al.. As shown in Table, there is a clear performance lead of the model trained on the DeepSeekMath Corpus. Figure shows that the model trained on the DeepSeekMath Corpus demonstrates better performance than Proof-Pile-2 at 50B tokens (1 full epoch of Proof-Pile-2), indicating the average quality of DeepSeekMath Corpus is higher.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Evaluation Results", "weight": 1.0} -->

Multilingual: The DeepSeekMath Corpus encompasses data in multiple languages, predominantly featuring English and Chinese as the two most represented languages. As shown in Table, training on the DeepSeekMath Corpus enhances mathematical reasoning performance in both English and Chinese. In contrast, existing mathematical corpora, which are primarily English-centric, show limited improvement and may even hinder performance in Chinese mathematical reasoning.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Evaluation Results", "weight": 1.0} -->

Large-scale: The DeepSeekMath Corpus is several times larger than existing mathematical corpora. As depicted in Figure, DeepSeek-LLM 1.3B, when trained on the DeepSeekMath Corpus, shows a steeper learning curve along with more lasting improvements. In contrast, the baseline corpora are much smaller, and have already been repeated multiple rounds during training, with the resulting model performance quickly reaching a plateau.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Training and Evaluating DeepSeekMath-Base 7B", "weight": 1.0} -->

In this section, we introduce DeepSeekMath-Base 7B, a base model with strong reasoning abilities, especially in mathematics. Our model is initialized with DeepSeek-Coder-Base-v1.5 7B and trained for 500B tokens. The distribution of the data is as follows: 56% is from the DeepSeekMath Corpus, 4% from AlgebraicStack, 10% from arXiv, 20% is Github code, and the remaining 10% is natural language data from Common Crawl in both English and Chinese. We mainly adopt the training setting specified in Section 2.2.1, except that we set the maximum value of the learning rate to 4.2e-4 and use a batch size of 10M tokens.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Training and Evaluating DeepSeekMath-Base 7B", "weight": 1.0} -->

We conduct a comprehensive assessment of the mathematical capabilities of DeepSeekMath-Base 7B, focusing on its ability to produce self-contained mathematical solutions without relying on external tools, solve mathematical problems using tools, and conduct formal theorem proving. Beyond mathematics, we also provide a more general profile of the base model, including its performance of natural language understanding, reasoning, and programming skills.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Mathematical Problem Solving with Step-by-Step Reasoning", "weight": 1.0} -->

We evaluate DeepSeekMath-Base's performance of solving mathematical problems using few-shot chain-of-thought prompting, across eight benchmarks in English and Chinese. These benchmarks encompass quantitative reasoning (e.g., GSM8K, MATH, and CMATH ) and multiple-choice problems (e.g., MMLU-STEM and Gaokao-MathQA ), covering diverse fields of mathematics from elementary to college-level complexity.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Mathematical Problem Solving with Step-by-Step Reasoning", "weight": 1.0} -->

As shown in Table, DeepSeekMath-Base 7B leads in performance across all eight benchmarks among the open-source base models (including the widely-used general model Mistral 7B and the recently released Llemma 34B which underwent math training on Proof-Pile-2 ). Notably, on the competition-level MATH dataset, DeepSeekMath-Base surpasses existing open-source base models by over 10% absolute, and outperforms Minerva 540B, a closed-source base model 77 times larger which builds on PaLM and is further trained on mathematical texts.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Mathematical Problem Solving with Step-by-Step Reasoning", "weight": 1.0} -->

71.7% 20.3% 35.3% Table 2: Comparisons between DeepSeekMath-Base 7B and strong base models on English and Chinese mathematical benchmarks. Models are evaluated with chain-of-thought prompting. Minerva results are quoted from Lewkowycz et al..

<!-- chunk {"id": "body-0045", "role": "body", "section": "Mathematical Problem Solving with Tool Use", "weight": 1.0} -->

We evaluate program-aided mathematical reasoning on GSM8K and MATH using few-shot program-of-thought prompting (Chen et al. Gao et al., ). Models are prompted to solve each problem by writing a Python program where libraries such as math and sympy can be utilized for intricate computations. The execution result of the program is evaluated as the answer. As shown in Table, DeepSeekMath-Base 7B outperforms the prior state-of-the-art Llemma 34B.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Formal Mathematics", "weight": 1.0} -->

Formal proof automation is beneficial to ensure the accuracy and reliability of mathematical proofs and enhance efficiency, with increasing attention in recent years. We evaluate DeepSeekMath-Base 7B on the task of informal-to-formal proving from which is to generate a formal proof based on an informal statement, a formal counterpart of the statement, and an informal proof. We evaluate on miniF2F, a benchmark for formal Olympiad-level mathematics, and generate a formal proof in Isabelle for each problem with few-shot prompting. Following Jiang et al., we leverage models to generate proof sketches, and execute the off-the-shelf automated prover Sledgehammer to fill in the missing details. As shown in Table, DeepSeekMath-Base 7B demonstrates strong performance in proof autoformalization.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Natural Language Understanding, Reasoning, and Code", "weight": 1.0} -->

We evaluate model performance of natural language understanding on MMLU, reasoning on BBH, and coding capabilities on HumanEval and MBPP. As shown in Table, DeepSeekMath-Base 7B exhibits significant enhancements in performance on MMLU and BBH over its precursor, DeepSeek-Coder-Base-v1.5, illustrating the positive impact of math training on language understanding and reasoning. Additionally, by including code tokens for continual training, DeepSeekMath-Base 7B effectively maintains the performance of DeepSeek-Coder-Base-v1.5 on the two coding benchmarks. Overall, DeepSeekMath-Base 7B significantly outperforms the general model Mistral 7B on the three reasoning and coding benchmarks.

<!-- chunk {"id": "body-0048", "role": "body", "section": "SFT Data Curation", "weight": 1.0} -->

We construct a mathematical instruction-tuning dataset covering English and Chinese problems from different mathematical fields and of varying complexity levels: problems are paired with solutions in chain-of-thought (CoT), program-of-thought (PoT) (Chen et al. Gao et al., ), and tool-integrated reasoning format. The total number of training examples is 776K.

<!-- chunk {"id": "body-0049", "role": "body", "section": "SFT Data Curation", "weight": 1.0} -->

English mathematical datasets: We annotate GSM8K and MATH problems with tool-integrated solutions, and adopt a subset of MathInstruct along with the training set of Lila-OOD where problems are solved with CoT or PoT. Our English collection covers diverse fields of mathematics, e.g., algebra, probability, number theory, calculus, and geometry.

<!-- chunk {"id": "body-0050", "role": "body", "section": "SFT Data Curation", "weight": 1.0} -->

Chinese mathematical datasets: We collect Chinese K-12 mathematical problems spanning 76 sub-topics such as linear equations, with solutions annotated in both CoT and tool-integrated reasoning format.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Training and Evaluating DeepSeekMath-Instruct 7B", "weight": 1.0} -->

In this section, we introduce DeepSeekMath-Instruct 7B which undergoes mathematical instruction tuning based on DeepSeekMath-Base. Training examples are randomly concatenated until reaching a maximum context length of 4K tokens. We train the model for 500 steps with a batch size of 256 and a constant learning rate of 5e-5.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Training and Evaluating DeepSeekMath-Instruct 7B", "weight": 1.0} -->

We evaluate models' mathematical performance both without and with tool use, on 4 quantitative reasoning benchmarks in English and Chinese.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Training and Evaluating DeepSeekMath-Instruct 7B", "weight": 1.0} -->

Closed-source models include: the GPT family among which GPT-4 and GPT-4 Code Interpreter ^22^2 are the most capable ones, Gemini Ultra and Pro, Inflection-2, Grok-1 ^33^3 as well as models recently released by Chinese companies including Baichuan-3 ^44^4 the latest GLM-4 ^55^5 from the GLM family. These models are for general purposes, most of which have undergone a series of alignment procedures.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Training and Evaluating DeepSeekMath-Instruct 7B", "weight": 1.0} -->

Open-source models include: general models like DeepSeek-LLM-Chat 67B, Qwen 72B, SeaLLM-v2 7B, and ChatGLM3 6B, as well as models with enhancements in mathematics including InternLM2-Math 20B ^66^6 which builds on InternLM2 and underwent math training followed by instruction tuning, Math-Shepherd-Mistral 7B which applys PPO training to Mistral 7B with a process-supervised reward model, the WizardMath series which improves mathematical reasoning in Mistral 7B and Llama-2 70B using evolve-instruct (i.e., a version of instruction tuning that uses AI-evolved instructions) and PPO training with training problems primarily sourced from GSM8K and MATH, MetaMath 70B which is Llama-2 70B fine-tuned on an augmented version of GSM8K and MATH, ToRA 34B Gou et al. which is CodeLlama 34B fine-tuned to do tool-integrated mathematical reasoning, MAmmoTH 70B which is Llama-2 70B instruction-tuned on MathInstruct.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Training and Evaluating DeepSeekMath-Instruct 7B", "weight": 1.0} -->

83.7% 57.4% 72.0% 84.3% DeepSeekMath-RL 7B 86.7% 58.8% 78.4% 87.6% Table 5: Performance of Open- and Closed-Source models with both Chain-of-Thought and Tool-Integrated Reasoning on English and Chinese Benchmarks.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Training and Evaluating DeepSeekMath-Instruct 7B", "weight": 1.0} -->

Scores in gray denote majority votes with 32 candidates; The others are Top1 scores. DeepSeekMath-RL 7B beats all open-source models from 7B to 70B, as well as the majority of closed-source models. Although DeepSeekMath-RL 7B is only further trained on chain-of-thought-format instruction tuning data of GSM8K and MATH, it improves over DeepSeekMath-Instruct 7B on all benchmarks.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Training and Evaluating DeepSeekMath-Instruct 7B", "weight": 1.0} -->

As shown in Table, under the evaluation setting where tool use is disallowed, DeepSeekMath-Instruct 7B demonstrates strong performance of step-by-step reasoning. Notably, on the competition-level MATH dataset, our model surpasses all open-source models and the majority of proprietary models (e.g., Inflection-2 and Gemini Pro) by at least 9% absolute. This is true even for models that are substantially larger (e.g., Qwen 72B) or have been specifically enhanced through math-focused reinforcement learning (e.g., WizardMath-v1.1 7B). While DeepSeekMath-Instruct rivals the Chinese proprietary models GLM-4 and Baichuan-3 on MATH, it still underperforms GPT-4 and Gemini Ultra.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Training and Evaluating DeepSeekMath-Instruct 7B", "weight": 1.0} -->

Under the evaluation setting where models are allowed to integrate natural language reasoning and program-based tool use for problem solving, DeepSeekMath-Instruct 7B approaches an accuracy of 60% on MATH, surpassing all existing open-source models. On the other benchmarks, our model is competitive with DeepSeek-LLM-Chat 67B, the prior state-of-the-art that is 10 times larger.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Group Relative Policy Optimization", "weight": 1.0} -->

Reinforcement learning (RL) has been proven to be effective in further improving the mathematical reasoning ability of LLMs after the Supervised Fine-Tuning (SFT) stage. In this section, we introduce our efficient and effective RL algorithm, Group Relative Policy Optimization (GRPO).

<!-- chunk {"id": "body-0060", "role": "body", "section": "From PPO to GRPO", "weight": 1.0} -->

Proximal Policy Optimization (PPO) is an actor-critic RL algorithm that is widely used in the RL fine-tuning stage of LLMs.

<!-- chunk {"id": "body-0061", "role": "body", "section": "From PPO to GRPO", "weight": 1.0} -->

where $\pi_{\theta}$ and $\pi_{\theta_{old}}$ are the current and old policy models, and $q,o$ are questions and outputs sampled from the question dataset and the old policy $\pi_{\theta_{old}}$, respectively. $\varepsilon$ is a clipping-related hyper-parameter introduced in PPO for stabilizing training. $A_{t}$ is the advantage, which is computed by applying Generalized Advantage Estimation (GAE), based on the rewards $\{ r_{\geq t}\}$ and a learned value function $V_{\psi}$. Thus, in PPO, a value function needs to be trained alongside the policy model and to mitigate over-optimization of the reward model, the standard approach is to add a per-token KL penalty from a reference model in the reward at each token, i.e.,

<!-- chunk {"id": "body-0062", "role": "body", "section": "From PPO to GRPO", "weight": 1.0} -->

where $r_{\varphi}$ is the reward model, $\pi_{ref}$ is the reference model, which is usually the initial SFT model, and $\beta$ is the coefficient of the KL penalty.

<!-- chunk {"id": "body-0063", "role": "body", "section": "From PPO to GRPO", "weight": 1.0} -->

As the value function employed in PPO is typically another model of comparable size as the policy model, it brings a substantial memory and computational burden. Additionally, during RL training, the value function is treated as a baseline in the calculation of the advantage for variance reduction. While in the LLM context, usually only the last token is assigned a reward score by the reward model, which may complicate the training of a value function that is accurate at each token. To address this, as shown in Figure, we propose Group Relative Policy Optimization (GRPO), which obviates the need for additional value function approximation as in PPO, and instead uses the average reward of multiple sampled outputs, produced in response to the same question, as the baseline.

<!-- chunk {"id": "body-0064", "role": "body", "section": "From PPO to GRPO", "weight": 1.0} -->

where $\varepsilon$ and $\beta$ are hyper-parameters, and ${\hat{A}}_{i,t}$ is the advantage calculated based on relative rewards of the outputs inside each group only, which will be detailed in the following subsections. The group relative way that GRPO leverages to calculate the advantages, aligns well with the comparative nature of rewards models, as reward models are typically trained on datasets of comparisons between outputs on the same question. Also note that, instead of adding KL penalty in the reward, GRPO regularizes by directly adding the KL divergence between the trained policy and the reference policy to the loss, avoiding complicating the calculation of ${\hat{A}}_{i,t}$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "From PPO to GRPO", "weight": 1.0} -->

Input initial policy model πθinit; reward models rφ; task prompts 𝒟; hyperparameters ε, β, μ
1:policy model πθ ← πθinit
5: Sample a batch 𝒟b from 𝒟
6: Update the old policy model πθo l d ← πθ
7: Sample G outputs {oi}i = 1G ∼ πθo l d(⋅∣q) for each question q ∈ 𝒟b
8: Compute rewards {ri}i = 1G for each sampled output oi by running rφ
9: Compute Âi, t for the t-th token of oi through group relative advantage estimation.
10: for GRPO iteration = 1, …, μ do
11: Update the policy model πθ by maximizing the GRPO objective (Equation 21)
12: Update rφ through continuous training using a replay mechanism.
Algorithm 1 Iterative Group Relative Policy Optimization

<!-- chunk {"id": "body-0066", "role": "body", "section": "Outcome Supervision RL with GRPO", "weight": 1.0} -->

Formally, for each question $q$, a group of outputs $\{ o_{1},o_{2},\cdots,o_{G}\}$ are sampled from the old policy model $\pi_{\theta_{old}}$. A reward model is then used to score the outputs, yielding $G$ rewards $\mathbf{r} = {\{ r_{1},r_{2},\cdots,r_{G}\}}$ correspondingly. Subsequently, these rewards are normalized by subtracting the group average and dividing by the group standard deviation.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Outcome Supervision RL with GRPO", "weight": 1.0} -->

Outcome supervision provides the normalized reward at the end of each output $o_{i}$ and sets the advantages ${\hat{A}}_{i,t}$ of all tokens in the output as the normalized reward, i.e., ${\hat{A}}_{i,t} = {\overset{\sim}{r}}_{i} = \frac{r_{i} - {{mean}{(\mathbf{r})}}}{{std}{(\mathbf{r})}}$, and then optimizes the policy by maximizing the objective defined in equation.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Process Supervision RL with GRPO", "weight": 1.0} -->

Outcome supervision only provides a reward at the end of each output, which may not be sufficient and efficient to supervise the policy in complex mathematical tasks. Following Wang et al., we also explore process supervision, which provides a reward at the end of each reasoning step.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Process Supervision RL with GRPO", "weight": 1.0} -->

We also normalize these rewards with the average and the standard deviation, i.e., ${\overset{\sim}{r}}_{i}^{index{(j)}} = \frac{r_{i}^{index{(j)}} - {{mean}{(\mathbf{R})}}}{{std}{(\mathbf{R})}}$. Subsequently, the process supervision calculates the advantage of each token as the sum of the normalized rewards from the following steps, i.e., ${\hat{A}}_{i,t} = {\sum_{{index{(j)}} \geq t}{\overset{\sim}{r}}_{i}^{index{(j)}}}$, and then optimizes the policy by maximizing the objective defined in equation.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Iterative RL with GRPO", "weight": 1.0} -->

As the reinforcement learning training process progresses, the old reward model may not be sufficient to supervise the current policy model. Therefore, we also explore the iterative RL with GRPO. As shown in Algorithm, in iterative GRPO, we generate new training sets for the reward model based on the sampling results from the policy model and continually train the old reward model using a replay mechanism that incorporates 10% of historical data. Then, we set the reference model as the policy model, and continually train the policy model with the new reward model.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Training and Evaluating DeepSeekMath-RL", "weight": 1.0} -->

We conduct RL based on DeepSeekMath-Instruct 7B. The training data of RL are chain-of-thought-format questions related to GSM8K and MATH from the SFT data, which consists of around 144K questions. We exclude other SFT questions to investigate the impact of RL on benchmarks that lack data throughout the RL phase. We construct the training set of reward models following. We train our initial reward model based on the DeepSeekMath-Base 7B with a learning rate of 2e-5. For GRPO, we set the learning rate of the policy model as 1e-6. The KL coefficient is 0.04. For each question, we sample $64$ outputs. The max length is set to 1024, and the training batch size is 1024. The policy model only has a single update following each exploration stage. We evaluate DeepSeekMath-RL 7B on benchmarks following DeepSeekMath-Instruct 7B.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Training and Evaluating DeepSeekMath-RL", "weight": 1.0} -->

For DeepSeekMath-RL 7B, GSM8K and MATH with chain-of-thought reasoning can be regarded as in-domain tasks and all the other benchmarks can be regarded as out-of-domain tasks.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Training and Evaluating DeepSeekMath-RL", "weight": 1.0} -->

Table demonstrates the performance of open- and closed-source models with both chain-of-thought and tool-integrated reasoning on English and Chinese benchmarks. We find that: 1) DeepSeekMath-RL 7B attains accuracies of 88.2% and 51.7% on GSM8K and MATH, respectively, utilizing chain-of-thought reasoning. This performance surpasses that of all open-source models in the 7B to 70B range, as well as the majority of closed-source models. 2) Crucially, DeepSeekMath-RL 7B is only trained on chain-of-thought-format instruction tuning data of GSM8K and MATH, starting from DeepSeekMath-Instruct 7B. Despite the constrained scope of its training data, it outperforms DeepSeekMath-Instruct 7B across all evaluation metrics, showcasing the effectiveness of reinforcement learning.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this section, we will share our findings in pre-training and RL experiments.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Lessons Learnt in Pre-Training", "weight": 1.0} -->

We first share our experience in pre-training. Unless otherwise specified, we will adhere to the training settings outlined in Section 2.2.1. It is worth noting that, when referring to the DeepSeekMath Corpus in this section, we use an 89B-token dataset from the second iteration of the data collection process.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Code Training Benefits Mathematical Reasoning", "weight": 1.0} -->

A popular yet unverified hypothesis suggests that code training improves reasoning. We attempt to offer a partial response to this, particularly within the mathematical domain: code training improves models' ability to do mathematical reasoning both with and without tool use.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Code Training Benefits Mathematical Reasoning", "weight": 1.0} -->

Code Training for 400B Tokens $\rightarrow$ Math Training for 150B Tokens: We train DeepSeek-LLM 1.3B for 400B code tokens followed by 150B math tokens;

<!-- chunk {"id": "body-0078", "role": "body", "section": "Code Training Benefits Mathematical Reasoning", "weight": 1.0} -->

General Training for 400B Tokens $\rightarrow$ Math Training for 150B Tokens: As a control experiment, we also experiment with general tokens (sampled from a large-scale general corpus created by DeepSeek-AI) instead of code tokens in the first stage of training, in an attempt to investigate the advantages of code tokens over general tokens in improving mathematical reasoning.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Code Training Benefits Mathematical Reasoning", "weight": 1.0} -->

Math Training for 150B Tokens: We train DeepSeek-LLM 1.3B for 150B math tokens;

<!-- chunk {"id": "body-0080", "role": "body", "section": "Code Training Benefits Mathematical Reasoning", "weight": 1.0} -->

Training on a mixture of 400B Code Tokens and 150B Math Tokens: Math training following code training degrades coding performance. We investigate whether code tokens, when mixed with math tokens for one-stage training, would still improve mathematical reasoning and also alleviate the problem of catastrophic forgetting.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Code Training Benefits Mathematical Reasoning", "weight": 1.0} -->

Training Setting Training Tokens w/o Tool Use w/ Tool Use General Code Math GSM8K MATH CMATH GSM8K+Python MATH+Python No Continual Training – – – 2.9% 3.0% 12.3% 2.7% 2.3% Two-Stage Training Stage 1: General Training 400B – – 2.9% 3.2% 14.8% 3.3% 2.3% Stage 2: Math Training – – 150B 19.1% 14.4% 37.2% 14.3% 6.7% Stage 1: Code Training – 400B – 5.9% 3.6% 19.9% 12.4% 10.0% Stage 2: Math Training – – 150B 21.9% 15.3% 39.7% 17.4% 9.4% One-Stage Training Math Training – – 150B 20.5% 13.1% 37.6% 11.4% 6.5% Code &amp; Math Mixed Training – 400B 150B 17.6% 12.1% 36.3% 19.7% 13.5% Table 6: Investigation of how code affects mathematical reasoning under different training

<!-- chunk {"id": "body-0082", "role": "body", "section": "Code Training Benefits Mathematical Reasoning", "weight": 1.0} -->

We experiment with DeepSeek-LLM 1.3B, and evaluate its mathematical reasoning performance without and with tool use via few-shot chain-of-thought prompting and few-shot program-of-thought prompting, respectively.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Code Training Benefits Mathematical Reasoning", "weight": 1.0} -->

Training Setting Training Tokens MMLU BBH HumanEval (Pass@1) MBPP (Pass@1) General Code Math No Continual Training – – – 24.5% 28.1% 12.2% 13.0% Two-Stage Training Stage 1: General Training 400B – – 25.9% 27.7% 15.2% 13.6% Stage 2: Math Training – – 150B 33.1% 32.7% 12.8% 13.2% Stage 1: Code Training – 400B – 25.0% 31.5% 25.0% 40.0% Stage 2: Math Training – – 150B 36.2% 35.3% 12.2% 17.0% One-Stage Training Math Training – – 150B 32.3% 32.5% 11.6% 13.2% Code &amp; Math Mixed Training – 400B 150B 33.5% 35.6% 29.3% 39.4%
Table 7: Investigation of how different settings of code and math training affect model performance of language understanding, reasoning, and coding. We experiment with DeepSeek-LLM 1.3B.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Code Training Benefits Mathematical Reasoning", "weight": 1.0} -->

We evaluate the models on MMLU and BBH using few-shot chain-of-thought prompting. On HumanEval and MBPP, we conduct zero-shot and few-shot evaluations, respectively.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Results", "weight": 1.0} -->

Table and Table demonstrate the downstream performance under different training settings.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Results", "weight": 1.0} -->

Code training benefits program-aided mathematical reasoning, both under the two-stage training and one-stage training settings. As shown in Table, under the two-stage training setting, code training alone already significantly enhances the ability to solve GSM8K and MATH problems using Python. Math training in the second stage yields further improvements. Interestingly, under the one-stage training setting, mixing code tokens and math tokens effectively mitigates the issue of catastrophic forgetting that arises from two-stage training, and also synergizes coding and program-aided mathematical reasoning.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Results", "weight": 1.0} -->

Code training also improves mathematical reasoning without tool use. Under the two-stage training setting, the initial stage of code training already results in moderate enhancements. It also boosts the efficiency of the subsequent math training, eventually leading to the best performance. However, combining code tokens and math tokens for one-stage training compromises mathematical reasoning without tool use. One conjecture is that DeepSeek-LLM 1.3B, due to its limited scale, lacks the capacity to fully assimilate both code and mathematical data simultaneously.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Results", "weight": 1.0} -->

11.1% 7.7% 50.0% 35.2% 42.6% 7.6% 24.8% Table 8: Effect of math training on different arXiv datasets. Model performance is evaluated with few-shot chain-of-thought prompting.

<!-- chunk {"id": "body-0089", "role": "body", "section": "ArXiv Papers Seem Ineffective in Improving Mathematical Reasoning", "weight": 1.0} -->

ArXiv papers are commonly included as a component of math pre-training data. However, detailed analysis regarding their impact on mathematical reasoning has not been extensively conducted. Perhaps counter-intuitively, according to our experiments, arXiv papers seem ineffective in improving mathematical reasoning. We experiment with models of different sizes, including DeepSeek-LLM 1.3B and DeepSeek-Coder-Base-v1.5

<!-- chunk {"id": "body-0090", "role": "body", "section": "ArXiv Papers Seem Ineffective in Improving Mathematical Reasoning", "weight": 1.0} -->

MathPile: an 8.9B-token corpus developed with cleaning and filtering heuristic rules, over 85% of which are scientific arXiv papers;

<!-- chunk {"id": "body-0091", "role": "body", "section": "ArXiv Papers Seem Ineffective in Improving Mathematical Reasoning", "weight": 1.0} -->

ArXiv-RedPajama: the entirety of arXiv LaTeX files with preambles, comments, macros, and bibliographies removed, totaling 28.0B tokens.

<!-- chunk {"id": "body-0092", "role": "body", "section": "ArXiv Papers Seem Ineffective in Improving Mathematical Reasoning", "weight": 1.0} -->

In our experiments, we separately train DeepSeek-LLM 1.3B for 150B tokens and DeepSeek-Coder-Base-v1.5 7B for 40B tokens on each arXiv corpus. It seems that arXiv papers are ineffective in improving mathematical reasoning. When trained on a arXiv-only corpus, both models display no notable improvements or even deterioration across various mathematical benchmarks of different complexities employed in this study. These benchmarks include quantitative reasoning datasets like GSM8K and MATH, multiple-choice challenges like MMLU-STEM, and formal mathematics like miniF2F.

<!-- chunk {"id": "body-0093", "role": "body", "section": "ArXiv Papers Seem Ineffective in Improving Mathematical Reasoning", "weight": 1.0} -->

However, this conclusion has its limitations and should be taken with a grain of salt.

<!-- chunk {"id": "body-0094", "role": "body", "section": "ArXiv Papers Seem Ineffective in Improving Mathematical Reasoning", "weight": 1.0} -->

The impact of arXiv tokens on specific math-related tasks not included in this research, such as informalization of theorems which is to convert formal statements or proofs to their informal versions;

<!-- chunk {"id": "body-0095", "role": "body", "section": "ArXiv Papers Seem Ineffective in Improving Mathematical Reasoning", "weight": 1.0} -->

The effect of arXiv tokens when combined with other types of data;

<!-- chunk {"id": "body-0096", "role": "body", "section": "ArXiv Papers Seem Ineffective in Improving Mathematical Reasoning", "weight": 1.0} -->

Whether the benefits of arXiv papers would manifest themselves at a larger model scale.

<!-- chunk {"id": "body-0097", "role": "body", "section": "ArXiv Papers Seem Ineffective in Improving Mathematical Reasoning", "weight": 1.0} -->

Thus, further exploration is required, which we leave for future studies.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Towards to a Unified Paradigm", "weight": 1.0} -->

In this section, we provide a unified paradigm to analyze different training methods, such as SFT, RFT, DPO, PPO, GRPO, and further conduct experiments to explore the factors of the unified paradigm.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Towards to a Unified Paradigm", "weight": 1.0} -->

There exist three key components: 1) Data Source $\mathcal{D}$, which determines the training data; 2) Reward Function $\pi_{rf}$, which is the source of the training reward signal; 3) Algorithm $\mathcal{A}$: which processes the training data and the reward signal to the gradient coefficient $GC$ that determines the magnitude of the penalty or reinforcement for the data.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Towards to a Unified Paradigm", "weight": 1.0} -->

Supervised Fine-tuning (SFT): SFT fine-tunes pretrained model on human selected SFT data.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Towards to a Unified Paradigm", "weight": 1.0} -->

Rejection Sampling Fine-tuning (RFT): RFT further fine-tunes the SFT model on the filtered outputs sampled from the SFT model based on SFT questions. RFT filters the outputs based on the correctness of their answers.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Towards to a Unified Paradigm", "weight": 1.0} -->

Direct Preference Optimization (DPO): DPO further refines the SFT model by fine-tuning it on augmented outputs sampled from the SFT model, using pair-wise DPO loss.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Towards to a Unified Paradigm", "weight": 1.0} -->

Online Rejection Sampling Fine-tuning (Online RFT): Different from RFT, Online RFT initiates the policy model using the SFT model and refines it by fine-tuning with the augmented outputs sampled from the real-time policy model.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Towards to a Unified Paradigm", "weight": 1.0} -->

PPO/GRPO: PPO/GRPO initializes the policy model using the SFT model and reinforces it with the outputs sampled from the real-time policy model.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Towards to a Unified Paradigm", "weight": 1.0} -->

We summarize the components of these methods in Table. Please refer to Appendix A.1 for a more detailed derivation process.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Observation about Data Source", "weight": 1.0} -->

We divide the data source into two categories, online sampling, and offline sampling. Online sampling denotes that the training data is from the exploration results of the real-time training policy model, while offline sampling denotes that the training data is from the sampling results of the initial SFT model. RFT and DPO follow the offline style, while Online RFT and GRPO follow the online style.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Observation about Data Source", "weight": 1.0} -->

As shown in Figure, we find that the Online RFT significantly outperforms RFT on two benchmarks. Specifically, Online RFT is comparable to RFT in the early stage of training but gains an absolute advantage in the later stage, demonstrating the superiority of online training. This is intuitive, as in the initial stage, the actor and the SFT model exhibit close resemblance, with the sampled data revealing only minor differences. In the later stage, however, the data sampled from the actor will exhibit more significant differences, and real-time data sampling will offer greater advantages.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Observation about Gradient Coefficient", "weight": 1.0} -->

The algorithm processes the reward signal to the gradient coefficient to update the model parameter. We divide the reward function as 'Rule' and 'Model' in our experiments. Rule refers to judging the quality of a response based on the correctness of the answer, and Model denotes that we train a reward model to score each response. The training data of the reward model is based on the rule judgment. Equations and ‣ A.1 Analysis of Reinforcement Learning ‣ Appendix A Appendix ‣ DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models") highlight a key difference between GRPO and Online RFT: GRPO uniquely adjusts its gradient coefficient based on the reward value provided by the reward model. This allows for differential reinforcement and penalization of responses according to their varying magnitudes. In contrast, Online RFT lacks this feature; it does not penalize incorrect responses and uniformly reinforces all responses with correct answers at the same level of intensity.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Observation about Gradient Coefficient", "weight": 1.0} -->

As demonstrated in Figure, GRPO surpasses online RFT, thereby highlighting the efficiency of altering positive and negative gradient coefficients. In addition, GRPO+PS shows superior performance compared to GRPO+OS, indicating the benefits of using fine-grained, step-aware gradient coefficients. Furthermore, we explore the iterative RL, in our experiments, we conduct two rounds of iteration. As shown in Figure, we notice that the iterative RL significantly improves the performance, especially at the first iteration.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Why RL Works?", "weight": 1.0} -->

In this paper, we conduct reinforcement learning based on a subset of instruction tuning data, and it achieves significant performance enhancement upon the instruction tuning model. To further explain why reinforcement learning works. We evaluate the Pass@K and Maj@K accuracy of the Instruct and RL models on two benchmarks. As shown in Figure, RL enhances Maj@K's performance but not Pass@K. These findings indicate that RL enhances the model's overall performance by rendering the output distribution more robust, in other words, it seems that the improvement is attributed to boosting the correct response from TopK rather than the enhancement of fundamental capabilities. Similarly, identified a misalignment problem in reasoning tasks within the SFT model, showing that the reasoning performance of SFT models can be improved through a series of preference alignment strategies.

<!-- chunk {"id": "body-0111", "role": "body", "section": "How to Achieve More Effective RL?", "weight": 1.0} -->

We demonstrate RL works pretty well in mathematical reasoning tasks. We also provide a unified paradigm to understand different representative training methods. Within this paradigm, all methods are conceptualized as either direct or simplified RL techniques. As summarized in Equation, there exist three key components: Data Source, Algorithm, and Reward Function. We provide some potential future directions about the three components.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Data Source", "weight": 1.0} -->

Data source is the raw material of all training methods. In the context of RL, we specifically refer to the data source as the unlabeled questions with the outputs sampled from the policy model. In this paper, we only use the questions from the instruction tuning stage and a naive nucleus sampling to sample outputs. We think this is a potential reason that our RL pipeline only improves the Maj@K performance. In the future, we will explore our RL pipeline on out-of-distribution question prompts, in conjunction with advanced sampling (decoding) strategies, like those based on tree-search methods. Also, the efficient inference techniques (Xia et al. Leviathan et al. Kwon et al. Xia et al., ), which determines the exploration efficiency of policy models, also play an exceedingly important role.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Algorithms", "weight": 1.0} -->

Algorithms process the data and reward signal to the gradient coefficient to update the model parameter. Based on Equation, to some extent, all methods now fully TRUST the signal of the reward function to increase or decrease the conditional probability of a certain token. However, it is impossible to ensure the reward signal is always reliable, especially in extremely complex tasks. For example, even the PRM800K datasets, which have been carefully annotated by well-trained annotators, still contain approximately 20% of incorrectly annotations^77^7 To this end, we will explore the reinforcement learning algorithm that is robust against noisy reward signals. We believe such WEAK-TO-STRONG alignment methods will bring a fundamental change to the learning algorithms.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Reward Function", "weight": 1.0} -->

Reward function is the source of the training signal. In RL, the reward function is usually the neural reward model. We think there exist three important directions for reward models: 1) How to enhance the generalization ability of the reward model. The reward model must be effectively generalized to handle out-of-distribution questions and advanced decoding outputs; otherwise, reinforcement learning may merely stabilize the distribution of LLMs rather than improve their fundamental capabilities; 2) How to reflect the uncertainty of reward model. The uncertainty could potentially act as a linking bridge between the weak reward model and the weak-to-strong learning algorithms; 3) How to efficiently build high-quality process reward models that can provide fine-grained training signals for the reasoning process.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Conclusion, Limitation, and Future Work", "weight": 1.5} -->

We present DeepSeekMath, which outperforms all open-source models on the competition-level MATH benchmark and approaches the performance of closed models. DeepSeekMath is initialized with DeepSeek-Coder-v1.5 7B and undergoes continual training for 500B tokens, with a significant component of the training data being 120B math tokens sourced from Common Crawl. Our extensive ablation study shows web pages offer significant potential for high-quality mathematical data, while arXiv may not as beneficial as we expected. We introduce Group Relative Policy Optimization (GRPO), a variant of Proximal Policy Optimization (PPO), which can notably improve mathematical reasoning capabilities with less memory consumption. The experiment results show that GRPO is effective even if DeepSeekMath-Instruct 7B has reached a high score on benchmarks. We also provide a unified paradigm to understand a series of methods and summarize several potential directions for more effective reinforcement learning.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Conclusion, Limitation, and Future Work", "weight": 1.5} -->

Although DeepSeekMath achieves impressive scores on quantitative reasoning benchmarks, its capability on geometry and theorem-proof are relatively weaker than closed models. For instance, in our dry run, the model cannot handle problems related to triangles and ellipses, which may indicate data selection bias in pre-training and fine-tuning. In addition, restricted by the model scale, DeepSeekMath is worse than GPT-4 on few-shot capability. GPT-4 could improve its performance with few-shot inputs, while DeepSeekMath shows similar performance in zero-shot and few-shot evaluation. In the future, we will further improve our engineered data selection pipeline to construct more high-quality pre-trained corpus. In addition, we will explore the potential directions (Section 5.2.3) for more effective reinforcement learning of LLMs.
