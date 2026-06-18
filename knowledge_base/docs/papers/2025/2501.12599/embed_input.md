<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Kimi K1.5: Scaling Reinforcement Learning with LLMs

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Language model pretraining with next token prediction has proved effective for scaling compute but is limited to the amount of available training data. Scaling reinforcement learning (RL) unlocks a new axis for the continued improvement of artificial intelligence, with the promise that large language models (LLMs) can scale their training data by learning to explore with rewards. However, prior published work has not produced competitive results. In light of this, we report on the training practice of Kimi k1.5, our latest multi-modal LLM trained with RL, including its RL training techniques, multi-modal data recipes, and infrastructure optimization. Long context scaling and improved policy optimization methods are key ingredients of our approach, which establishes a simplistic, effective RL framework without relying on more complex techniques such as Monte Carlo tree search, value functions, and process reward models. Notably, our system achieves state-of-the-art reasoning performance across multiple benchmarks and modalities - e.g., 77.5 on AIME, 96.2 on MATH 500, 94-th percentile on Codeforces, 74.9 on MathVista - matching OpenAI's o1.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Moreover, we present effective long2short methods that use long-CoT techniques to improve short-CoT models, yielding state-of-the-art short-CoT reasoning results - e.g., 60.8 on AIME, 94.6 on MATH500, 47.3 on LiveCodeBench - outperforming existing short-CoT models such as GPT-4o and Claude Sonnet 3.5 by a large margin (up to +550%).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Language model pretraining with next token prediction has been studied under the context of the scaling law, where proportionally scaling model parameters and data sizes leads to the continued improvement of intelligence. However, this approach is limited to the amount of available high-quality training data. In this report, we present the training recipe of Kimi k1.5, our latest multi-modal LLM trained with reinforcement learning (RL). The goal is to explore a possible new axis for continued scaling. Using RL with LLMs, the models learns to explore with rewards and thus is not limited to a pre-existing static dataset.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

There are a few key ingredients about the design and training of k1.5.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Long context scaling. We scale the context window of RL to 128k and observe continued improvement of performance with an increased context length. A key idea behind our approach is to use partial rollouts to improve training efficiency---i.e., sampling new trajectories by reusing a large chunk of previous trajectories, avoiding the cost to re-generate the new trajectories from scratch. Our observation identifies the context length as a key dimension of the continued scaling of RL with LLMs.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Improved policy optimization. We derive a formulation of RL with long-CoT and employ a variant of online mirror descent for robust policy optimization. This algorithm is further improved by our effective sampling strategy, length penalty, and optimization of the data recipe.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Simplistic Framework. Long context scaling, combined with the improved policy optimization methods, establishes a simplistic RL framework for learning with LLMs. Since we are able to scale the context length, the learned CoTs exhibit the properties of planning, reflection, and correction. An increased context length has an effect of increasing the number of search steps. As a result, we show that strong performance can be achieved without relying on more complex techniques such as Monte Carlo tree search, value functions, and process reward models.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Multimodalities. Our model is jointly trained on text and vision data, which has the capabilities of jointly reasoning over the two modalities.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, we present effective long2short methods that use long-CoT techniques to improve short-CoT models. Specifically, our approaches include applying length penalty with long-CoT activations and model merging.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our long-CoT version achieves state-of-the-art reasoning performance across multiple benchmarks and modalities---e.g., 77.5 on AIME, 96.2 on MATH 500, 94-th percentile on Codeforces, 74.9 on MathVista---matching OpenAI's o1. Our model also achieves state-of-the-art short-CoT reasoning results---e.g., 60.8 on AIME, 94.6 on MATH500, 47.3 on LiveCodeBench---outperforming existing short-CoT models such as GPT-4o and Claude Sonnet 3.5 by a large margin (up to +550%). Results are shown in Figures and.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Approach: Reinforcement Learning with LLMs", "weight": 1.0} -->

The development of Kimi k1.5 consists of several stages: pretraining, vanilla supervised fine-tuning (SFT), long-CoT supervised fine-turning, and reinforcement learning (RL). This report focuses on RL, beginning with an overview of the RL prompt set curation (Section 2.1) and long-CoT supervised finetuning (Section 2.2), followed by an in-depth discussion of RL training strategies in Section 2.3. Additional details on pretraining and vanilla supervised finetuning can be found in Section 2.5.

<!-- chunk {"id": "body-0013", "role": "body", "section": "RL Prompt Set Curation", "weight": 1.0} -->

Through our preliminary experiments, we found that the quality and diversity of the RL prompt set play a critical role in ensuring the effectiveness of reinforcement learning. A well-constructed prompt set not only guides the model toward robust reasoning but also mitigates the risk of reward hacking and overfitting to superficial patterns.

<!-- chunk {"id": "body-0014", "role": "body", "section": "RL Prompt Set Curation", "weight": 1.0} -->

Diverse Coverage: Prompts should span a wide array of disciplines, such as STEM, coding, and general reasoning, to enhance the model's adaptability and ensure broad applicability across different domains.

<!-- chunk {"id": "body-0015", "role": "body", "section": "RL Prompt Set Curation", "weight": 1.0} -->

Balanced Difficulty: The prompt set should include a well-distributed range of easy, moderate, and difficult questions to facilitate gradual learning and prevent overfitting to specific complexity levels.

<!-- chunk {"id": "body-0016", "role": "body", "section": "RL Prompt Set Curation", "weight": 1.0} -->

Accurate Evaluability: Prompts should allow objective and reliable assessment by verifiers, ensuring that model performance is measured based on correct reasoning rather than superficial patterns or random guess.

<!-- chunk {"id": "body-0017", "role": "body", "section": "RL Prompt Set Curation", "weight": 1.0} -->

To achieve diverse coverage in the prompt set, we employ automatic filters to select questions that require rich reasoning and are straightforward to evaluate. Our dataset includes problems from various domains, such as STEM fields, competitions, and general reasoning tasks, incorporating both text-only and image-text question-answering data. Furthermore, we developed a tagging system to categorize prompts by domain and discipline, ensuring balanced representation across different subject areas.

<!-- chunk {"id": "body-0018", "role": "body", "section": "RL Prompt Set Curation", "weight": 1.0} -->

We adopt a model-based approach that leverages the model's own capacity to adaptively assess the difficulty of each prompt. Specifically, for every prompt, an SFT model generates answers ten times using a relatively high sampling temperature. The pass rate is then calculated and used as a proxy for the prompt's difficulty---the lower the pass rate, the higher the difficulty. This approach allows difficulty evaluation to be aligned with the model's intrinsic capabilities, making it highly effective for RL training. By leveraging this method, we can prefilter most trivial cases and easily explore different sampling strategies during RL training.

<!-- chunk {"id": "body-0019", "role": "body", "section": "RL Prompt Set Curation", "weight": 1.0} -->

To avoid potential reward hacking, we need to ensure that both the reasoning process and the final answer of each prompt can be accurately verified. Empirical observations reveal that some complex reasoning problems may have relatively simple and easily guessable answers, leading to false positive verification---where the model reaches the correct answer through an incorrect reasoning process. To address this issue, we exclude questions that are prone to such errors, such as multiple-choice, true/false, and proof-based questions. Furthermore, for general question-answering tasks, we propose a simple yet effective method to identify and remove easy-to-hack prompts. Specifically, we prompt a model to guess potential answers without any CoT reasoning steps. If the model predicts the correct answer within $N$ attempts, the prompt is considered too easy-to-hack and removed. We found that setting $N = 8$ can remove the majority easy-to-hack prompts. Developing more advanced verification models remains an open direction for future research.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Long-CoT Supervised Fine-Tuning", "weight": 1.0} -->

With the refined RL prompt set, we employ prompt engineering to construct a small yet high-quality long-CoT warmup dataset, containing accurately verified reasoning paths for both text and image inputs. This approach resembles rejection sampling (RS) but focuses on generating long-CoT reasoning paths through prompt engineering. The resulting warmup dataset is designed to encapsulate key cognitive processes that are fundamental to human-like reasoning, such as planning, where the model systematically outlines steps before execution; evaluation, involving critical assessment of intermediate steps; reflection, enabling the model to reconsider and refine its approach; and exploration, encouraging consideration of alternative solutions. By performing a lightweight SFT on this warm-up dataset, we effectively prime the model to internalize these reasoning strategies. As a result, the fine-tuned long-CoT model demonstrates improved capability in generating more detailed and logically coherent responses, which enhances its performance across diverse reasoning tasks.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

Given a training dataset $\mathcal{D} = {\{{(x_{i},y_{i}^{\ast})}\}}_{i = 1}^{n}$ of problems $x_{i}$ and corresponding ground truth answers $y_{i}^{\ast}$, our goal is to train a policy model $\pi_{\theta}$ to accurately solve test problems. In the context of complex reasoning, the mapping of problem $x$ to solution $y$ is non-trivial. To tackle this challenge, the *chain of thought* (CoT) method proposes to use a sequence of intermediate steps $z = {(z_{1},z_{2},\ldots,z_{m})}$ to bridge $x$ and $y$, where each $z_{i}$ is a coherent sequence of tokens that acts as a significant intermediate step toward solving the problem.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

When solving problem $x$, thoughts $z_{t} \sim \pi_{\theta}{( \cdot |x,z_{1},\ldots,z_{t - 1})}$ are auto-regressively sampled, followed by the final answer $y \sim \pi_{\theta}{( \cdot |x,z_{1},\ldots,z_{m})}$. We use ${y,z} \sim \pi_{\theta}$ to denote this sampling procedure. Note that both the thoughts and final answer are sampled as a language sequence.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

To further enhance the model's reasoning capabilities, *planning* algorithms are employed to explore various thought processes, generating improved CoT at inference time. The core insight of these approaches is the explicit construction of a search tree of thoughts guided by value estimations. This allows the model to explore diverse continuations of a thought process or backtrack to investigate new directions when encountering dead ends. In more detail, let $\mathcal{T}$ be a search tree where each node represents a partial solution $s = {(x,z_{1:{|s|}})}$. Here $s$ consists of the problem $x$ and a sequence of thoughts $z_{1:{|s|}} = {(z_{1},\ldots,z_{|s|})}$ leading up to that node, with $|s|$ denoting number of thoughts in the sequence. The planning algorithm uses a critic model $v$ to provide feedback $v{(x,z_{1:{|s|}})}$, which helps evaluate the current progress towards solving the problem and identify any errors in the existing partial solution.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

We note that the feedback can be provided by either a discriminative score or a language sequence. Guided by the feedbacks for all $s \in \mathcal{T}$, the planning algorithm selects the most promising node for expansion, thereby growing the search tree. The above process repeats iteratively until a full solution is derived.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

We can also approach planning algorithms from an *algorithmic perspective*. Given past search history available at the $t$-th iteration $(s_{1},{v{(s_{1})}},\ldots,s_{t - 1},{v{(s_{t - 1})}})$, a planning algorithm $\mathcal{A}$ iteratively determines the next search direction $\mathcal{A}{(\left. s_{t} \middle| {s_{1},{v{(s_{1})}},\ldots,s_{t - 1},{v{(s_{t - 1})}}} \right.)}$ and provides feedbacks for the current search progress $\mathcal{A}{(\left. {v{(s_{t})}} \middle| {s_{1},{v{(s_{1})}},\ldots,s_{t}} \right.)}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

Since both thoughts and feedbacks can be viewed as intermediate reasoning steps, and these components can both be represented as sequence of language tokens, we use $z$ to replace $s$ and $v$ to simplify the notations. Accordingly, we view a planning algorithm as a mapping that directly acts on a sequence of reasoning steps $\mathcal{A}{( \cdot |z_{1},z_{2},\ldots)}$. In this framework, all information stored in the search tree used by the planning algorithm is flattened into the full context provided to the algorithm. This provides an intriguing perspective on generating high-quality CoT: Rather than explicitly constructing a search tree and implementing a planning algorithm, we could potentially train a model to approximate this process. Here, the number of thoughts (i.e., language tokens) serves as an analogy to the computational budget traditionally allocated to planning algorithms. Recent advancements in long context windows facilitate seamless scalability during both the training and testing phases. If feasible, this method enables the model to run an implicit search over the reasoning space directly via auto-regressive predictions.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

Consequently, the model not only learns to solve a set of training problems but also develops the ability to tackle individual problems effectively, leading to improved generalization to unseen test problems.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

We thus consider training the model to generate CoT with reinforcement learning (RL). Let $r$ be a reward model that justifies the correctness of the proposed answer $y$ for the given problem $x$ based on the ground truth $y^{\ast}$, by assigning a value ${r{(x,y,y^{\ast})}} \in {\{ 0,1\}}$. For verifiable problems, the reward is directly determined by predefined criteria or rules. For example, in coding problems, we assess whether the answer passes the test cases. For problems with free-form ground truth, we train a reward model $r{(x,y,y^{\ast})}$ that predicts if the answer matches the ground truth. Given a problem $x$, the model $\pi_{\theta}$ generates a CoT and the final answer through the sampling procedure $z \sim \pi_{\theta}{( \cdot |x)}$, $y \sim \pi_{\theta}{( \cdot |x,z)}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

The quality of the generated CoT is evaluated by whether it can lead to a correct final answer. In summary, we consider the following objective to optimize the policy

<!-- chunk {"id": "body-0030", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

By scaling up RL training, we aim to train a model that harnesses the strengths of both simple prompt-based CoT and planning-augmented CoT. The model still auto-regressively sample language sequence during inference, thereby circumventing the need for the complex parallelization required by advanced planning algorithms during deployment. However, a key distinction from simple prompt-based methods is that the model should not merely follow a series of reasoning steps. Instead, it should also learn critical planning skills including error identification, backtracking and solution refinement by leveraging the entire set of explored thoughts as contextual information.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Policy Optimization", "weight": 1.0} -->

We apply a variant of online policy mirror decent as our training algorithm. The algorithm performs iteratively. At the $i$-th iteration, we use the current model $\pi_{\theta_{i}}$ as a reference model and optimize the following relative entropy regularized policy optimization problem,

<!-- chunk {"id": "body-0032", "role": "body", "section": "Policy Optimization", "weight": 1.0} -->

where $\tau > 0$ is a parameter controlling the degree of regularization. This objective has a closed form solution

<!-- chunk {"id": "body-0033", "role": "body", "section": "Policy Optimization", "weight": 1.0} -->

Here $Z = {\sum_{y^{\prime},z^{\prime}}{\pi_{\theta_{i}}{(y^{\prime},\left. z^{\prime} \middle| x \right.)}{\exp{({{r{(x,y^{\prime},y^{\ast})}}/\tau})}}}}$ is the normalization factor. Taking logarithm of both sides we have for *any* $(y,z)$ the following constraint is satisfied, which allows us to leverage off-policy data during optimization

<!-- chunk {"id": "body-0034", "role": "body", "section": "Policy Optimization", "weight": 1.0} -->

This motivates the following surrogate loss

<!-- chunk {"id": "body-0035", "role": "body", "section": "Policy Optimization", "weight": 1.0} -->

To those familiar with policy gradient methods, this gradient resembles the policy gradient of using the mean of sampled rewards as the baseline. The main differences are that the responses are sampled from $\pi_{\theta_{i}}$ rather than on-policy, and an $l_{2}$-regularization is applied. Thus we could see this as the natural extension of a usual on-policy regularized policy gradient algorithm to the off-policy case. We sample a batch of problems from $\mathcal{D}$ and update the parameters to $\theta_{i + 1}$, which subsequently serves as the reference policy for the next iteration. Since each iteration considers a different optimization problem due to the changing reference policy, we also reset the optimizer at the start of each iteration.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Policy Optimization", "weight": 1.0} -->

We exclude the value network in our training system which has also been exploited in previous studies. While this design choice significantly improves training efficiency, we also hypothesize that the conventional use of value functions for credit assignment in classical RL may not be suitable for our context. Consider a scenario where the model has generated a partial CoT $(z_{1},z_{2},\ldots,z_{t})$ and there are two potential next reasoning steps: $z_{t + 1}$ and $z_{t + 1}^{\prime}$. Assume that $z_{t + 1}$ directly leads to the correct answer, while $z_{t + 1}^{\prime}$ contains some errors. If an oracle value function were accessible, it would indicate that $z_{t + 1}$ preserves a higher value compared to $z_{t + 1}^{\prime}$. According to the standard credit assignment principle, selecting $z_{t + 1}^{\prime}$ would be penalized as it has a negative advantages relative to the current policy.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Policy Optimization", "weight": 1.0} -->

However, exploring $z_{t + 1}^{\prime}$ is extremely valuable for training the model to generate long CoT. By using the justification of the final answer derived from a long CoT as the reward signal, the model can learn the pattern of trial and error from taking $z_{t + 1}^{\prime}$ as long as it successfully recovers and reaches the correct answer. The key takeaway from this example is that we should encourage the model to explore diverse reasoning paths to enhance its capability in solving complex problems. This exploratory approach generates a wealth of experience that supports the development of critical planning skills. Our primary goal is not confined to attaining high accuracy on training problems but focuses on equipping the model with effective problem-solving strategies, ultimately improving its performance on test problems.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Length Penalty", "weight": 1.0} -->

We observe an overthinking phenomenon that the model's response length significantly increases during RL training. Although this leads to better performance, an excessively lengthy reasoning process is costly during training and inference, and overthinking is often not preferred by humans. To address this issue, we introduce a length reward to restrain the rapid growth of token length, thereby improving the model's token efficiency. Given $k$ sampled responses ${(y_{1},z_{1})},\ldots,{(y_{k},z_{k})}$ of problem $x$ with true answer $y^{\ast}$, let ${len}{(i)}$ be the length of $(y_{i},z_{i})$, ${\min\_{len}} = {{\min_{i}{len}}{(i)}}$ and ${\max\_{len}} = {{\max_{i}{len}}{(i)}}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Length Penalty", "weight": 1.0} -->

If ${\max\_{len}} = {\min\_{len}}$, we set length reward zero for all responses, as they have the same length. Otherwise the length reward is given by

<!-- chunk {"id": "body-0040", "role": "body", "section": "Length Penalty", "weight": 1.0} -->

In essence, we promote shorter responses and penalize longer responses among correct ones, while explicitly penalizing long responses with incorrect answers. This length-based reward is then added to the original reward with a weighting parameter.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Length Penalty", "weight": 1.0} -->

In our preliminary experiments, length penalty may slow down training during the initial phases. To alleviate this issue, we propose to gradually warm up the length penalty during training. Specifically, we employ standard policy optimization without length penalty, followed by a constant length penalty for the rest of training.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Sampling Strategies", "weight": 1.0} -->

Although RL algorithms themselves have relatively good sampling properties (with more difficult problems providing larger gradients), their training efficiency is limited. Consequently, some well-defined prior sampling methods can yield potentially greater performance gains. We exploit multiple signals to further improve the sampling strategy. First, the RL training data we collect naturally come with different difficulty labels. For example, a math competition problem is more difficult than a primary school math problem. Second, because the RL training process samples the same problem multiple times, we can also track the success rate for each individual problem as a metric of difficulty. We propose two sampling methods to utilize these priors to improve training efficiency.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Curriculum Sampling", "weight": 1.0} -->

We start by training on easier tasks and gradually progress to more challenging ones. Since the initial RL model has limited performance, spending a restricted computation budget on very hard problems often yields few correct samples, resulting in lower training efficiency. Meanwhile, our collected data naturally includes grade and difficulty labels, making difficulty-based sampling an intuitive and effective way to improve training efficiency.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Prioritized Sampling", "weight": 1.0} -->

In addition to curriculum sampling, we use a prioritized sampling strategy to focus on problems where the model underperforms. We track the success rates $s_{i}$ for each problem $i$ and sample problems proportional to $1 - s_{i}$, so that problems with lower success rates receive higher sampling probabilities. This directs the model's efforts toward its weakest areas, leading to faster learning and better overall performance.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Test Case Generation for Coding", "weight": 1.0} -->

Since test cases are not available for many coding problems from the web, we design a method to automatically generate test cases that serve as a reward to train our model with RL. Our focus is primarily on problems that do not require a special judge. We also assume that ground truth solutions are available for these problems so that we can leverage the solutions to generate higher quality test cases.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Test Case Generation for Coding", "weight": 1.0} -->

We utilize the widely recognized test case generation library, CYaRon^11^1 to enhance our approach. We employ our base Kimi k1.5 to generate test cases based on problem statements. The usage statement of CYaRon and the problem description are provided as the input to the generator. For each problem, we first use the generator to produce 50 test cases and also randomly sample 10 ground truth submissions for each test case. We run the test cases against the submissions. A test case is deemed valid if at least 7 out of 10 submissions yield matching results. After this round of filtering, we obtain a set of selected test cases. A problem and its associated selected test cases are added to our training set if at least 9 out of 10 submissions pass the entire set of selected test cases.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Test Case Generation for Coding", "weight": 1.0} -->

In terms of statistics, from a sample of 1,000 online contest problems, approximately 614 do not require a special judge. We developed 463 test case generators that produced at least 40 valid test cases, leading to the inclusion of 323 problems in our training set.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Reward Modeling for Math", "weight": 1.0} -->

One challenge in evaluating math solutions is that different written forms can represent the same underlying answer. For instance, $a^{2} - 4$ and ${({a + 2})}{({a - 2})}$ may both be valid solutions to the same problem.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Reward Modeling for Math", "weight": 1.0} -->

Classic RM: Drawing inspiration from the InstructGPT methodology, we implemented a value-head based reward model and collected approximately 800k data points for fine-tuning. The model ultimately takes as input the "question," the "reference answer," and the "response," and outputs a single scalar that indicates whether the response is correct.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Reward Modeling for Math", "weight": 1.0} -->

Chain-of-Thought RM: Recent research suggests that reward models augmented with chain-of-thought (CoT) reasoning can significantly outperform classic approaches, particularly on tasks where nuanced correctness criteria matter---such as mathematics. Therefore, we collected an equally large dataset of about 800k CoT-labeled examples to fine-tune the Kimi model. Building on the same inputs as the Classic RM, the chain-of-thought approach explicitly generates a step-by-step reasoning process before providing a final correctness judgment in JSON format, enabling more robust and interpretable reward signals.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Reward Modeling for Math", "weight": 1.0} -->

During our manual spot checks, the Classic RM achieved an accuracy of approximately 84.4, while the Chain-of-Thought RM reached 98.5 accuracy. In the RL training process, we adopted the Chain-of-Thought RM to ensure more correct feedback.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Vision Data", "weight": 1.0} -->

To improve the model's real-world image reasoning capabilities and to achieve a more effective alignment between visual inputs and large language models (LLMs), our vision reinforcement learning (Vision RL) data is primarily sourced from three distinct categories: Real-world data, Synthetic visual reasoning data, and Text-rendered data.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Vision Data", "weight": 1.0} -->

The real-world data encompass a range of science questions across various grade levels that require graphical comprehension and reasoning, location guessing tasks that necessitate visual perception and inference, and data analysis that involves understanding complex charts, among other types of data. These datasets improve the model's ability to perform visual reasoning in real-world scenarios.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Vision Data", "weight": 1.0} -->

Synthetic visual reasoning data is artificially generated, including procedurally created images and scenes aimed at improving specific visual reasoning skills, such as understanding spatial relationships, geometric patterns, and object interactions. These synthetic datasets offer a controlled environment for testing the model's visual reasoning capabilities and provide an endless supply of training examples.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Vision Data", "weight": 1.0} -->

Text-rendered data is created by converting textual content into visual format, enabling the model to maintain consistency when handling text-based queries across different modalities. By transforming text documents, code snippets, and structured data into images, we ensure the model provides consistent responses regardless of whether the input is pure text or text rendered as images (like screenshots or photos). This also helps to enhance the model's capability when dealing with text-heavy images.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Vision Data", "weight": 1.0} -->

Each type of data is essential in building a comprehensive visual language model that can effectively manage a wide range of real-world applications while ensuring consistent performance across various input modalities.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Long2short: Context Compression for Short-CoT Models", "weight": 1.0} -->

Though long-CoT models achieve strong performance, it consumes more test-time tokens compared to standard short-CoT LLMs. However, it is possible to transfer the thinking priors from long-CoT models to short-CoT models so that performance can be improved even with limited test-time token budgets. We present several approaches for this long2short problem, including model merging, shortest rejection sampling, DPO, and long2short RL.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Model Merging", "weight": 1.0} -->

Model merging has been found to be useful in maintaining generalization ability. We also discovered its effectiveness in improving token efficiency when merging a long-cot model and a short-cot model. This approach combines a long-cot model with a shorter model to obtain a new one without training. Specifically, we merge the two models by simply averaging their weights.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Shortest Rejection Sampling", "weight": 1.0} -->

We observed that our model generates responses with a large length variation for the same problem. Based on this, we designed the Shortest Rejection Sampling method. This method samples the same question $n$ times (in our experiments, $n = 8$) and selects the shortest correct response for supervised fine-tuning.

<!-- chunk {"id": "body-0060", "role": "body", "section": "DPO", "weight": 1.0} -->

Similar with Shortest Rejection Sampling, we utilize the Long CoT model to generate multiple response samples. The shortest correct solution is selected as the positive sample, while longer responses are treated as negative samples, including both wrong longer responses and correct longer responses (1.5 times longer than the chosen positive sample). These positive-negative pairs form the pairwise preference data used for DPO training.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Long2short RL", "weight": 1.0} -->

After a standard RL training phase, we select a model that offers the best balance between performance and token efficiency to serve as the base model, and conduct a separate long2short RL training phase. In this second phase, we apply the length penalty introduced in Section 2.3.3, and significantly reduce the maximum rollout length to further penalize responses that exceed the desired length while possibly correct.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Pretraining", "weight": 1.0} -->

The Kimi k1.5 base model is trained on a diverse, high-quality multimodal corpus. The language data covers five domains: English, Chinese, Code, Mathematics Reasoning, and Knowledge. Multimodal data, including Captioning, Image-text Interleaving, OCR, Knowledge, and QA datasets, enables our model to acquire vision-language capabilities. Rigorous quality control ensures relevance, diversity, and balance in the overall pretrain dataset. Our pretraining proceeds in three stages: Vision-language pretraining, where a strong language foundation is established, followed by gradual multimodal integration; Cooldown, which consolidates capabilities using curated and synthetic data, particularly for reasoning and knowledge-based tasks; and Long-context activation, extending sequence processing to 131,072 tokens. More details regarding our pretraining efforts can be found in Appendix B.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Vanilla Supervised Finetuning", "weight": 1.0} -->

We create the vanilla SFT corpus covering multiple domains. For non-reasoning tasks, including question-answering, writing, and text processing, we initially construct a seed dataset through human annotation. This seed dataset is used to train a seed model. Subsequently, we collect a diverse of prompts and employ the seed model to generate multiple responses to each prompt. Annotators then rank these responses and refine the top-ranked response to produce the final version. For reasoning tasks such as math and coding problems, where rule-based and reward modeling based verifications are more accurate and efficient than human judgment, we utilize rejection sampling to expand the SFT dataset.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Vanilla Supervised Finetuning", "weight": 1.0} -->

Our vanilla SFT dataset comprises approximately 1 million text examples. Specifically, 500k examples are for general question answering, 200k for coding, 200k for math and science, 5k for creative writing, and 20k for long-context tasks such as summarization, doc-qa, translation, and writing. In addition, we construct 1 million text-vision examples encompassing various categories including chart interpretation, OCR, image-grounded conversations, visual coding, visual reasoning, and math/science problems with visual aids.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Vanilla Supervised Finetuning", "weight": 1.0} -->

We first train the model at the sequence length of 32k tokens for 1 epoch, followed by another epoch at the sequence length of 128k tokens. In the first stage (32k), the learning rate decays from $2 \times 10^{- 5}$ to $2 \times 10^{- 6}$, before it re-warmups to $1 \times 10^{- 5}$ in the second stage (128k) and finally decays to $1 \times 10^{- 6}$. To improve training efficiency, we pack multiple training examples into each single training sequence.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Large Scale Reinforcement Learning Training System for LLM", "weight": 1.0} -->

In the realm of artificial intelligence, reinforcement learning (RL) has emerged as a pivotal training methodology for large language models (LLMs), drawing inspiration from its success in mastering complex games like Go, StarCraft II, and Dota 2 through systems such as AlphaGo, AlphaStar, and OpenAI Dota Five. Following in this tradition, the Kimi k1.5 system adopts an iterative synchronous RL framework, meticulously designed to bolster the model's reasoning capabilities through persistent learning and adaptation. A key innovation in this system is the introduction of a Partial Rollout technique, designed to optimize the handling of complex reasoning trajectories.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Large Scale Reinforcement Learning Training System for LLM", "weight": 1.0} -->

The RL training system as illustrated in Figure 3(a) operates through an iterative synchronous approach, with each iteration encompassing a rollout phase and a training phase. During the rollout phase, rollout workers, coordinated by a central master, generate rollout trajectories by interacting with the model, producing sequences of responses to various inputs. These trajectories are then stored in a replay buffer, which ensures a diverse and unbiased dataset for training by disrupting temporal correlations. In the subsequent training phase, trainer workers access these experiences to update the model's weights. This cyclical process allows the model to continuously learn from its actions, adjusting its strategies over time to enhance performance.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Large Scale Reinforcement Learning Training System for LLM", "weight": 1.0} -->

The central master serves as the central conductor, managing the flow of data and communication between the rollout workers, trainer workers, evaluation with reward models and the replay buffer. It ensures that the system operates harmoniously, balancing the load and facilitating efficient data processing.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Large Scale Reinforcement Learning Training System for LLM", "weight": 1.0} -->

The trainer workers access these rollout trajectories, whether completed in a single iteration or divided across multiple iterations, to compute gradient updates that refine the model's parameters and enhance its performance. This process is overseen by a reward model, which evaluates the quality of the model's outputs and provides essential feedback to guide the training process. The reward model's evaluations are particularly pivotal in determining the effectiveness of the model's strategies and steering the model towards optimal performance.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Large Scale Reinforcement Learning Training System for LLM", "weight": 1.0} -->

Moreover, the system incorporates a code execution service, which is specifically designed to handle code-related problems and is integral to the reward model. This service evaluates the model's outputs in practical coding scenarios, ensuring that the model's learning is closely aligned with real-world programming challenges. By validating the model's solutions against actual code executions, this feedback loop becomes essential for refining the model's strategies and enhancing its performance in code-related tasks.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Partial Rollouts for Long CoT RL", "weight": 1.0} -->

One of the primary ideas of our work is to scale long-context RL training. Partial rollouts is a key technique that effectively addresses the challenge of handling long-CoT features by managing the rollouts of both long and short trajectories. This technique establishes a fixed output token budget, capping the length of each rollout trajectory. If a trajectory exceeds the token limit during the rollout phase, the unfinished portion is saved to the replay buffer and continued in the next iteration. It ensures that no single lengthy trajectory monopolizes the system's resources. Moreover, since the rollout workers operate asynchronously, when some are engaged with long trajectories, others can independently process new, shorter rollout tasks. The asynchronous operation maximizes computational efficiency by ensuring that all rollout workers are actively contributing to the training process, thereby optimizing the overall performance of the system.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Partial Rollouts for Long CoT RL", "weight": 1.0} -->

As illustrated in Figure 3(b), the partial rollout system works by breaking down long responses into segments across iterations (from iter n-m to iter n). The Replay Buffer acts as a central storage mechanism that maintains these response segments, where only the current iteration (iter n) requires on-policy computation. Previous segments (iter n-m to n-1) can be efficiently reused from the buffer, eliminating the need for repeated rollouts. This segmented approach significantly reduces the computational overhead: instead of rolling out the entire response at once, the system processes and stores segments incrementally, allowing for the generation of much longer responses while maintaining fast iteration times. During training, certain segments can be excluded from loss computation to further optimize the learning process, making the entire system both efficient and scalable.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Partial Rollouts for Long CoT RL", "weight": 1.0} -->

The implementation of partial rollouts also offers repeat detection. The system identifies repeated sequences in the generated content and terminates them early, reducing unnecessary computation while maintaining output quality. Detected repetitions can be assigned additional penalties, effectively discouraging redundant content generation in the prompt set.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Hybrid Deployment of Training and Inference", "weight": 1.0} -->

Training Phase: At the outset, Megatron and vLLM are executed within separate containers, encapsulated by a shim process known as checkpoint-engine (Section 2.6.3). Megatron commences the training procedure. After the training is completed, Megatron offloads the GPU memory and prepares to transfer current weights to vLLM.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Hybrid Deployment of Training and Inference", "weight": 1.0} -->

Inference Phase: Following Megatron's offloading, vLLM starts with dummy model weights and updates them with the latest ones transferred from Megatron via Mooncake. Upon completion of the rollout, the checkpoint-engine halts all vLLM processes.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Hybrid Deployment of Training and Inference", "weight": 1.0} -->

Subsequent Training Phase: Once the memory allocated to vLLM is released, Megatron onloads the memory and initiates another round of training.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Hybrid Deployment of Training and Inference", "weight": 1.0} -->

We find existing works challenging to simultaneously support all the following characteristics.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Hybrid Deployment of Training and Inference", "weight": 1.0} -->

Complex parallelism strategy: Megatron may have different parallelism strategy with vLLM. Training weights distributing in several nodes in Megatron could be challenging to be shared with vLLM.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Hybrid Deployment of Training and Inference", "weight": 1.0} -->

Minimizing idle GPU resources: For On-Policy RL, recent works such as SGLang and vLLM might reserve some GPUs during the training process, which conversely could lead to idle training GPUs. It would be more efficient to share the same devices between training and inference.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Hybrid Deployment of Training and Inference", "weight": 1.0} -->

Capability of dynamic scaling: In some cases, a significant acceleration can be achieved by increasing the number of inference nodes while keeping the training process constant. Our system enables the efficient utilization of idle GPU nodes when needed.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Hybrid Deployment of Training and Inference", "weight": 1.0} -->

As illustrated in Figure, we implement this hybrid deployment framework (Section 2.6.3) on top of Megatron and vLLM, achieving less than one minute from training to inference phase and about ten seconds conversely.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Hybrid Deployment Strategy", "weight": 1.0} -->

We propose a hybrid deployment strategy for training and inference tasks, which leverages Kubernetes Sidecar containers sharing all available GPUs to collocate both workloads in one pod.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Hybrid Deployment Strategy", "weight": 1.0} -->

It facilitates efficient resource sharing and management, preventing train nodes idling while waiting for inference nodes when both are deployed on separate nodes.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Hybrid Deployment Strategy", "weight": 1.0} -->

Leveraging distinct deployed images, training and inference can each iterate independently for better performance.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Hybrid Deployment Strategy", "weight": 1.0} -->

The architecture is not limited to vLLM, other frameworks can be conveniently integrated.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Checkpoint Engine", "weight": 1.0} -->

Checkpoint Engine is responsible for managing the lifecycle of the vLLM process, exposing HTTP APIs that enable triggering various operations on vLLM. For overall consistency and reliability, we utilize a global metadata system managed by the etcd service to broadcast operations and statuses.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Checkpoint Engine", "weight": 1.0} -->

It could be challenging to entirely release GPU memory by vLLM offloading primarily due to CUDA graphs, NCCL buffers and NVIDIA drivers. To minimize modifications to vLLM, we terminate and restart it when needed for better GPU utilization and fault tolerance.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Checkpoint Engine", "weight": 1.0} -->

The worker in Megatron converts the owned checkpoints into the Hugging Face format in shared memory. This conversion also takes Pipeline Parallelism and Expert Parallelism into account so that only Tensor Parallelism remains in these checkpoints. Checkpoints in shared memory are subsequently divided into shards and registered in the global metadata system. We employ Mooncake to transfer checkpoints between peer nodes over RDMA. Some modifications to vLLM are needed to load weight files and perform tensor parallelism conversion.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Code Sandbox", "weight": 1.0} -->

We developed the sandbox as a secure environment for executing user-submitted code, optimized for code execution and code benchmark evaluation. By dynamically switching container images, the sandbox supports different use cases through MultiPL-E, DMOJ Judge Server ^22^2 Lean, Jupyter Notebook, and other images.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Code Sandbox", "weight": 1.0} -->

For RL in coding tasks, the sandbox ensures the reliability of training data judgment by providing consistent and repeatable evaluation mechanisms. Its feedback system supports multi-stage assessments, such as code execution feedback and repo-level editing, while maintaining a uniform context to ensure fair and equitable benchmark comparisons across programming languages.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Code Sandbox", "weight": 1.0} -->

We deploy the service on Kubernetes for scalability and resilience, exposing it through HTTP endpoints for external integration. Kubernetes features like automatic restarts and rolling updates ensure availability and fault tolerance.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Code Sandbox", "weight": 1.0} -->

To optimize performance and support RL environments, we incorporate several techniques into the code execution service to enhance efficiency, speed, and reliability.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Code Sandbox", "weight": 1.0} -->

Using Crun: We utilize crun as the container runtime instead of Docker, significantly reducing container startup times.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Code Sandbox", "weight": 1.0} -->

Cgroup Reusing: We pre-create cgroups for container use, which is crucial in scenarios with high concurrency where creating and destroying cgroups for each container can become a bottleneck.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Code Sandbox", "weight": 1.0} -->

Disk Usage Optimization: An overlay filesystem with an upper layer mounted as tmpfs is used to control disk writes, providing a fixed-size, high-speed storage space. This approach is beneficial for ephemeral workloads.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Code Sandbox", "weight": 1.0} -->

(b) Maximum containers started per second on a 16-core machine

<!-- chunk {"id": "body-0097", "role": "body", "section": "Code Sandbox", "weight": 1.0} -->

These optimizations improve RL efficiency in code execution, providing a consistent and reliable environment for evaluating RL-generated code, essential for iterative training and model improvement.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Since k1.5 is a multimodal model, we conducted comprehensive evaluation across various benchmarks for different modalities. The detailed evaluation setup can be found in Appendix C.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Text Benchmark: MMLU, IF-Eval, CLUEWSC, C-EVAL

<!-- chunk {"id": "body-0100", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Reasoning Benchmark: HumanEval-Mul, LiveCodeBench, Codeforces, AIME 2024, MATH-500

<!-- chunk {"id": "body-0101", "role": "body", "section": "Evaluation", "weight": 1.0} -->

Vision Benchmark: MMMU, MATH-Vision, MathVista

<!-- chunk {"id": "body-0102", "role": "body", "section": "K1.5 long-CoT model", "weight": 1.0} -->

The performance of the Kimi k1.5 long-CoT model is presented in Table. Through long-CoT supervised fine-tuning (described in Section 2.2) and vision-text joint reinforcement learning (discussed in Section 2.3), the model's long-term reasoning capabilities are enhanced significantly. The test-time computation scaling further strengthens its performance, enabling the model to achieve state-of-the-art results across a range of modalities. Our evaluation reveals marked improvements in the model's capacity to reason, comprehend, and synthesize information over extended contexts, representing a advancement in multi-modal AI capabilities.

<!-- chunk {"id": "body-0103", "role": "body", "section": "K1.5 short-CoT model", "weight": 1.0} -->

The performance of the Kimi k1.5 short-CoT model is presented in Table. This model integrates several techniques, including traditional supervised fine-tuning (discussed in Section 2.5.2), reinforcement learning (explored in Section 2.3), and long-to-short distillation (outlined in Section 2.4). The results demonstrate that the k1.5 short-CoT model delivers competitive or superior performance compared to leading open-source and proprietary models across multiple tasks. These include text, vision, and reasoning challenges, with notable strengths in natural language understanding, mathematics, coding, and logical reasoning.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Long Context Scaling", "weight": 1.0} -->

We employ a mid-sized model to study the scaling properties of RL with LLMs. Figure illustrates the evolution of both training accuracy and response length across training iterations for the small model variant trained on the mathematical prompt set. As training progresses, we observe a concurrent increase in both response length and performance accuracy. Notably, more challenging benchmarks exhibit a steeper increase in response length, suggesting that the model learns to generate more elaborate solutions for complex problems. Figure indicates a strong correlation between the model's output context length and its problem-solving capabilities. Our final run of k1.5 scales to 128k context length and observes continued improvement on hard reasoning benchmarks.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Long2short", "weight": 1.0} -->

We compared the proposed long2short RL algorithm with the DPO, shortest rejection sampling, and model merge methods introduced in the Section 2.4, focusing on the token efficiency for the long2short problem, specifically how the obtained long-cot model can benefit a short model. In Figure, k1.5-long represents our long-cot model selected for long2short training. k1.5-short w/ rl refers to the short model obtained using the long2short RL training. k1.5-short w/ dpo denotes the short model with improved token efficiency through DPO training. k1.5-short w/ merge represents the model after model merging, while k1.5-short w/ merge + rs indicates the short model obtained by applying shortest rejection sampling to the merged model. k1.5-shortest represents the shortest model we obtained during the long2short training. As shown in Figure, the proposed long2short RL algorithm demonstrates the highest token efficiency compared other mehtods such as DPO and model merge.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Long2short", "weight": 1.0} -->

Notably, all models in the k1.5 series (marked in orange) demonstrate superior token efficiency compared to other models (marked in blue). For instance, k1.5-short w/ rl achieves a Pass@1 score of 60.8 on AIME2024 (averaged over 8 runs) while utilizing only 3,272 tokens on average. Similarly, k1.5-shortest attains a Pass@1 score of 88.2 on MATH500 while consuming approximately the same number of tokens as other short models.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Scaling of model size and context length", "weight": 1.0} -->

Our main contribution is the application of RL to enhance the model's capacity for generating extended CoT, thereby improving its reasoning ability. A natural question arises: how does this compare to simply increasing the model size? To demonstrate the effectiveness of our approach, we trained two models of different sizes using the same dataset and recorded the evaluation results and average inference lengths from all checkpoints during RL training. These results are shown in Figure. Notably, although the larger model initially outperforms the smaller one, the smaller model can achieve comparable performance by utilizing longer CoTs optimized through RL. However, the larger model generally shows better token efficiency than the smaller model. This also indicates that if one targets the best possible performance, scaling the context length of a larger model has a higher upper bound and is more token efficient. However, if test-time compute has a budget, training smaller models with a larger context length may be viable solutions.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Effects of using negative gradients", "weight": 1.0} -->

We investigate the effectiveness of using ReST as the policy optimization algorithm in our setting. The primary distinction between ReST and other RL-based methods including ours is that ReST iteratively refines the model by fitting the best response sampled from the current model, without applying negative gradients to penalize incorrect responses. As illustrated in Figure, our method exhibits superior sample complexity compared to ReST, indicating that the incorporation of negative gradients markedly enhances the model's efficiency in generating long CoT. Our method not only elevates the quality of reasoning but also optimizes the training process, achieving robust performance with fewer training samples. This finding suggests that the choice of policy optimization algorithm is crucial in our setting, as the performance gap between ReST and other RL-based methods is not as pronounced in other domains. Therefore, our results highlight the importance of selecting an appropriate optimization strategy to maximize effectiveness in generating long CoT.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Sampling strategies", "weight": 1.0} -->

We further demonstrate the effectiveness of our curriculum sampling strategy, as introduced in Section 2.3.4. Our training dataset $\mathcal{D}$ comprises a diverse mix of problems with varying levels of difficulty. With our curriculum sampling method, we initially use $\mathcal{D}$ for a warm-up phase and then focus solely on hard questions to train the model. This approach is compared to a baseline method that employs a uniform sampling strategy without any curriculum adjustments. As illustrated in Figure, our results clearly show that the proposed curriculum sampling method significantly enhances the performance. This improvement can be attributed to the method's ability to progressively challenge the model, allowing it to develop a more robust understanding and competency in handling complex problems. By focusing training efforts on more difficult questions after an initial general introduction, the model can better strengthen its reasoning and problem solving capabilities.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We present the training recipe and system design of k1.5, our latest multi-modal LLM trained with RL. One of the key insights we extract from our practice is that the scaling of context length is crucial to the continued improvement of LLMs. We employ optimized learning algorithms and infrastructure optimization such as partial rollouts to achieve efficient long-context RL training. How to further improve the efficiency and scalability of long-context RL training remains an important question moving forward.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Another contribution we made is a combination of techniques that enable improved policy optimization. Specifically, we formulate long-CoT RL with LLMs and derive a variant of online mirror descent for robust optimization. We also experiment with sampling strategies, length penalty, and optimizing the data recipe to achieve strong RL performance.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We show that strong performance can be achieved by long context scaling and improved policy optimization, even without using more complex techniques such as Monte Carlo tree search, value functions, and process reward models. In the future, it will also be intriguing to study improving credit assignments and reducing overthinking without hurting the model's exploration abilities.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We have also observed the potential of long2short methods. These methods largely improve performance of short CoT models. Moreover, it is possible to combine long2short methods with long-CoT RL in an iterative way to further increase token efficiency and extract the best performance out of a given context length budget.
