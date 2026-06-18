DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models

Topics include Reinforcement learning, Policy optimization, GRPO, Large language models, Mathematical reasoning.

Introduces GRPO (Group Relative Policy Optimization), a memory-efficient RL variant that replaces the PPO critic with group-relative reward normalization. Historically this caused a big buzz in the Machine Learning world because it was used to train DeepSeek R1, an open weights LLM from China that performed nearly as well as leading closed weights LLMs from the USA. Nevertheless, GRPO is very similar to the REINFORCE policy gradient algorithm, c.f. A vision researcher's guide to some RL stuff: PPO & GRPO - Yuge (Jimmy) Shi

Mathematical reasoning poses a significant challenge for language models due to its complex and structured nature. In this paper, we introduce DeepSeekMath 7B, which continues pre-training DeepSeek-Coder-Base-v1.5 7B with 120B math-related tokens sourced from Common Crawl, together with natural language and code data. DeepSeekMath 7B has achieved an impressive score of 51.7% on the competition-level MATH benchmark without relying on external toolkits and voting techniques, approaching the performance level of Gemini-Ultra and GPT-4. Self-consistency over 64 samples from DeepSeekMath 7B achieves 60.9% on MATH. The mathematical reasoning capability of DeepSeekMath is attributed to two key factors: First, we harness the significant potential of publicly available web data through a meticulously engineered data selection pipeline. Second, we introduce Group Relative Policy Optimization (GRPO), a variant of Proximal Policy Optimization (PPO), that enhances mathematical reasoning abilities while concurrently optimizing the memory usage of PPO.

## Introduction

Large language models (LLM) have revolutionized the approach to mathematical reasoning in artificial intelligence, spurring significant advancements in both the quantitative reasoning benchmark and the geometry reasoning benchmark. Moreover, these models have proven instrumental in assisting humans in solving complex mathematical problems. However, cutting-edge models such as GPT-4 and Gemini-Ultra are not publicly available, and the currently accessible open-source models considerably trail behind in performance.

In this study, we introduce DeepSeekMath, a domain-specific language model that significantly outperforms the mathematical capabilities of open-source models and approaches the performance level of GPT-4 on academic benchmarks. To achieve this, we create the DeepSeekMath Corpus, a large-scale high-quality pre-training corpus comprising 120B math tokens. This dataset is extracted from the Common Crawl (CC) using a fastText-based classifier. In the initial iteration, the classifier is trained using instances from OpenWebMath as positive examples, while incorporating a diverse selection of other web pages to serve as negative examples.

DeepSeekMath-Base is initialized with DeepSeek-Coder-Base-v1.5 7B, as we notice that starting from a code training model is a better choice compared to a general LLM. Furthermore, we observe the math training also improves model capability on MMLU and BBH benchmarks, indicating it does not only enhance the model's mathematical abilities but also amplifies general reasoning capabilities.

Furthermore, we introduce the Group Relative Policy Optimization (GRPO), a variant reinforcement learning (RL) algorithm of Proximal Policy Optimization (PPO). GRPO foregoes the critic model, instead estimating the baseline from group scores, significantly reducing training resources. By solely using a subset of English instruction tuning data, GRPO obtains a substantial improvement over the strong DeepSeekMath-Instruct, including both in-domain (GSM8K: 82.9% $\rightarrow$ 88.2%, MATH: 46.8% $\rightarrow$ 51.7%) and out-of-domain mathematical tasks (e.g., CMATH: 84.6% $\rightarrow$ 88.8%) during the reinforcement learning phase.

## Discussion

In this section, we will share our findings in pre-training and RL experiments.
