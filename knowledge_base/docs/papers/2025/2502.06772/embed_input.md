<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

ReasonFlux: Hierarchical LLM Reasoning via Scaling Thought Templates

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present that hierarchical LLM reasoning via scaling thought templates can effectively optimize the reasoning search space and outperform the mathematical reasoning capabilities of powerful LLMs like OpenAI o1-preview and DeepSeek V3. We train our ReasonFlux-32B model with only 8 GPUs and introduces three innovations: (i) a structured and generic thought template library, containing around 500 high-level thought templates capable of generalizing to similar or relevant reasoning problems; (ii) performing hierarchical reinforcement learning on a sequence of thought templates instead of long CoTs, optimizing a base LLM to plan out an optimal template trajectory for gradually handling complex problems; (iii) a brand new inference scaling system that enables hierarchical LLM reasoning by adaptively scaling thought templates at inference time. With a template trajectory containing more explainable reasoning structures than DeepSeek-R1 and o3-mini, our ReasonFlux-32B significantly advances math reasoning capabilities to state-of-the-art levels. Notably, on the MATH benchmark, it achieves an accuracy of 91.2% and surpasses o1-preview by 6.7%.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

On the USA Math Olympiad (AIME) benchmark, ReasonFlux-32B solves an average of 56.7% of problems, surpassing o1-preview and DeepSeek-V3 by 27% and 45%, respectively.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Large Language Models (LLMs) have recently achieved remarkable progress, demonstrating exceptional capabilities in tackling complex reasoning tasks and even surpassing human experts in specific domains. For example, models such as OpenAI's O1, Google's Gemini-2.0, DeepSeek-V3, and Qwen-QwQ are at the forefront of this progress, characterized by their ability to emulate human reasoning through a slower, more deliberate thought process. These models leverage increased inference time to enhance reasoning accuracy. While they have unlocked substantial performance gains, more complex tasks such as mathematical problem solving in AIME, OlympiadBench and code in LiveCodeBench, which demand a more fine-grained search through a vast solution space and more delicate thought for each intricate reasoning step, thus still pose significant challenges.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Subsequent research has focused on enhancing LLMs' reasoning capabilities on complex problems through inference-time strategies. These strategies can be divided into two categories: deliberate search and reward-model-guided methods. Deliberate search methods, like Tree of Thoughts (ToT) and Graph of Thoughts (GoT), allow LLMs to explore multiple reasoning paths and self-evaluate choices to find the optimal trajectory. Reward-model-guided methods leverage reward models to assess reasoning step quality. Best-of-N approaches, which leverage an Outcome Reward Model (ORM) to find the optimal reasoning paths in multiple candidates, while Process Reward Models (PRMs) (Lightman et al. Luo et al. Wang et al., ) guide the model towards promising paths by rewarding high-probability intermediate steps. Building on this, Monte Carlo Tree Search (MCTS) employs a fine-grained search, decomposing tasks into simpler steps and using PRMs to guide action selection within a tree-based search space. However, these methods often incur high computational costs, especially with numerous reasoning steps or vast search spaces, primarily due to the inherent randomness of sampling, which hinders the efficient identification of the optimal reasoning trajectory.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Furthermore, they rely on manually designed search strategies and instance/step-level reward, limiting their generalization ability to diverse and complex reasoning tasks. Essentially, they struggle to effectively balance the exploration-exploitation trade-off during inference scaling. This highlights the need for a more efficient and generalizable inference scaling approach that enhances reasoning without extensive manual effort, while providing a more principled search strategy.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To achieve more efficient and precise search of reasoning paths, a feasible approach is to utilize Retrieval-Augmented Generation (RAG). Recent Buffer of Thought (BoT) constructs a meta-buffer to store informative, high-level thoughts distilled from various problem-solving processes, adaptively retrieving and instantiating relevant thought templates for each specific task. SuperCorrect further utilizes both high-level and detailed thought templates to enhance reasoning ability of small LLMs. Despite significant improvements, such template-based reasoning methods may still face challenges when applied to complex reasoning tasks. Because complex problems often require the integration of multiple templates or diverse pieces of retrieved information, which current methods struggle to address effectively.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

To this end, we introduce ReasonFlux, a novel hierarchical LLM reasoning framework that configures optimal thought template trajectories by automatically retrieving relevant high-level thought templates at inference time, to achieve superior performance on complex reasoning tasks and even outperform OpenAI o1-preview and o1-mini models. To be more specific, we first construct a structured template library, which contains 500 useful compacted thought templates for efficient retrieval and adaptation. Instead of optimizing a long CoT trajectory, we perform hierarchical reinforcement learning on a sequence of high-level thought templates, optimizing a base llm to learn an optimal thought template trajectory from multiple ones and guiding an inference LLM to solve a series of simpler sub-problems. Finally, we develop a new inference scaling system through adaptively scaling thought templates. This hierarchical reasoning paradigm enables ReasonFlux to simplify the search of reasoning paths and enhance the reasoning ability for complex problems by dynamically selecting a most appropriate high-level template for each sub-problem. Our automated template scaling allows ReasonFlux to effectively achieve a better exploration-exploitation trade-off, leading to a more robust and efficient problem-solving process.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Through these innovations, ReasonFlux offers a more efficient, generalizable, and scalable solution for enhancing the complex reasoning capabilities of LLMs.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce ReasonFlux (in Figure 1), a hierarchical LLM reasoning framework that significantly enhances complex reasoning capabilities, outperforming SOTA models like o1-preview and DeepSeek-V3 on challenging MATH and AIME benchmarks (in Table 2).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a structured and compact template library with around 500 thought templates curated from challenging mathematical problems. This library facilitates efficient retrieval and adaptation of relevant high-level thought templates for a series detailed reasoning steps.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We develop hierarchical reinforcement learning on a sequence of high-level thought templates, to enable LLMs to generate an optimal thought template trajectory for a series of simpler sub-problems, effectively simplifying the search space of reasoning paths.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We design an new inference scaling system (in Figure 2) by adaptively scaling thought templates for hierarchical reasoning. This system allows ReasonFlux to dynamically retrieve a series of high-level templates and adaptively perform instantiated reasoning at inference time, achieving a better exploration-exploitation trade-off for robust and efficient problem-solving. Moreover, our ReasonFlux contains more explainable reasoning structures than DeepSeek-R1 and o3-mini.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Learning from Preferences for Language Models", "weight": 1.0} -->

Preference learning is critical for aligning Large Language Models (LLMs) with human expectations and perceptions. Initial approaches, building on pre-training and supervised fine-tuning (SFT), employed PPO in Reinforcement Learning from Human/AI Feedback (RLHF/RLAIF) frameworks (Schulman et al. Christiano et al. Ouyang et al. Xie et al., ). These approaches typically involve training a reward model on preference pairs and subsequently optimizing the LLM to maximize the learned reward. However, PPO's instability and inefficiency motivated alternative approaches like DPO, which directly optimizes a policy from paired preference data. Subsequent research has addressed various challenges. ORPO integrates alignment into SFT, KTO leverages pointwise data, simplifying data acquisition process. Other efforts focus on finer-grained optimization, such as Step-DPO and Cross-DPO that targets intermediate reasoning or reflection steps. SPO employs game-theoretic concepts to address non-transitive preferences, while Multi-turn DPO extends optimization to conversations.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Learning from Preferences for Language Models", "weight": 1.0} -->

However, existing methods often rely on instance or step-level reward units, potentially failing to capture and reward the higher-level cognitive processes inherent in human problem-solving process. To this end, we introduce hierarchical RL-based optimization, a novel preference learning approach that encourages the model to configure a series of high-level thought templates that can handle diverse sub-tasks for complex problems, thereby promoting more human-like problem-solving strategies in LLMs.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Retrieval-Augmented Generation for Language Models", "weight": 1.0} -->

Retrieval-augmented Language Models (RALMs) have become a powerful approach to mitigating hallucinations and enhancing the factual accuracy of LLMs (Asai et al. Mialon et al. Shi et al. Gao et al. Zhao et al., ). By retrieving relevant documents from a large-scale external knowledge source to inform response generation, RALMs have demonstrated superior performance in question-answering, often with fewer parameters than traditional LLMs. Their versatility is further evidenced by successful applications across diverse tasks, including multi-modal generation and biomedical applications (Yasunaga et al. Izacard et al. Wang et al. Zhao et al. Borgeaud et al. Yang et al., ). However, RALMs face challenges in complex reasoning tasks, such as math and code, where retrieving relevant guidelines or templates via standard embedding similarity search proves difficult. While methods like RAFT have attempted to address this by improving retrieval relevance, respectively, their effectiveness decrease as the document size grows. To overcome these limitations, we design a structured and compact template library for efficient and accurate retrieval, specifically targeting complex reasoning problems.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Inference Scaling for LLM Reasoning", "weight": 1.0} -->

The auto-regressive nature of LLMs suggests that solving more complex problems inherently requires generating more tokens. Early work, such as CoT, used prompting techniques like "Let's think step by step" to break down complex reasoning tasks into simpler sub-problems, thus enhancing reasoning performance. Building on this, ToT and GoT employed different data structures to expand the reasoning space, allowing LLMs to explore multiple solution paths. Recent research (Wu et al. Snell et al., ) has formalized the concept of inference scaling laws, which examine the trade-offs between the generation of additional tokens, and the use of various inference strategies. For instance, majority voting and best-of-N methods (Wang et al. Li et al., ) generate multiple candidate solutions and select the best based on frequency among all the results or the reward model's evaluation. Similarly, approaches using Monte Carlo Tree Search (MCTS) leverage greater search and computation to improve accuracy.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Inference Scaling for LLM Reasoning", "weight": 1.0} -->

To enhance search accuracy, Process Reward Models (PRMs) have been introduced to select high-quality reasoning paths, with studies (Setlur et al. Snell et al. Lightman et al. Luo et al. Wang et al., ) demonstrating their effectiveness, particularly in complex reasoning tasks. More recently, methods like BoT utilize thought templates from past reasoning processes to guide exploration, significantly improving efficiency. However, a deeper understanding of the exploration-exploitation trade-off (Tang et al. Setlur et al., ) for these template-based approaches remains an open challenge. Our work addresses this challenge by scaling an hierarchical template-augmented reasoning paradigm that significantly enhances reasoning accuracy, especially for complex tasks, while strategically balancing exploration and exploitation.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Constructing Structured Thought Template Library", "weight": 1.0} -->

Inspired by how humans utilize external resources when tackling complex reasoning problems, RAG methods enhance LLMs by enabling them to retrieve information from external sources. Recent Buffer of Thought (BoT) attempts to create a buffer of high-level thoughts for llm reasoning, and builds an efficient RAG reasoning system. Despite a comprehensive template library to solve similar problems, BoT still faces scalability challenges as template size grows, same as the traditional RAG systems that rely on embedding similarity to search unstructured text corpora.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Constructing Structured Thought Template Library", "weight": 1.0} -->

To address this, our approach focuses on constructing a structured thought template library that enables more precise, targeted retrieval and mitigates scalability challenges. To build this library, we carefully selected a wide and diverse range of challenging mathematical reasoning problems from different sources, ensuring robustness and broad applicability of our template library. We used an LLM to analyze the thought behind the solution and generating concise summaries of problem-solving strategies and identifying common patterns. This process yielded a collection of high-quality, solution-oriented thought templates.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Constructing Structured Thought Template Library", "weight": 1.0} -->

Each template $T_{i}$ in the library is structured for efficient retrieval and application, where $T_{\text{nam}}$ is the name (e.g., "$\sqrt{R^{2} - x^{2}}$ Type Trigonometric Substitution"), $T_{\text{tag}}$ is a set of tags for keyword-based retrieval (e.g., {"Trigonometric Substitution", "Irrational Function Optimization"}), $T_{\text{des}}$ is a description of the underlying principle and applicable scenarios, $T_{\text{sco}}$ defines the scope, specifying the problem types it addresses, $T_{a}$ is a sequence of detailed application steps $\{ a_{1},a_{2},\ldots,a_{k}\}$, and $T_{\text{exa}}$ is a set of examples demonstrating its application.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Constructing Structured Thought Template Library", "weight": 1.0} -->

where $m$ is the total number of templates. Here we present an illustration of a thought template within our library. For the sake of brevity, some fields in the following example have been simplified. Please refer to Appendix A for more detailed examples.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Constructing Structured Thought Template Library", "weight": 1.0} -->

Efficient retrieval is facilitated by leveraging the metadata associated with each template, specifically the name ($n$) and tags ($t$), enabling quick and accurate searching based on keywords or specific problem characteristics. This structured organization, combined with rich metadata, ensures that the most relevant templates are readily available for any given problems.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Hierarchical Reinforcement Learning on Thought Template Trajectory", "weight": 1.0} -->

While our structured template library provides a valuable resource for reasoning, an effective method is needed to utilize this library and select the appropriate templates for handing a given problem. To this end, we perform hierarchical reinforcement learning to train and finally obtain ReasonFlux that can effectively plan out an optimal thought template trajectory for a problem. We retrieve and configure a sequence of relevant templates from the library, assisting in instantiating the retrieved templates on specific sub-problems. ReasonFlux acts as an experienced navigator, providing the optimal trajectory denoted as ${\mathbb{T}}_{\text{traj}}$ that enabling the LLM to instantiate abstract thought templates into concrete sequential problem-solving steps.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Structure-based Finetuning", "weight": 1.0} -->

Our hierarchical RL process begins by leveraging the structured template library $\mathcal{D}_{\text{temp}}$ to construct a knowledge-intensive training dataset $\mathcal{D}_{\text{train}}$. This dataset comprises diverse examples of template names $T_{\text{nam}}$, their associated tags $T_{\text{tag}}$, detailed descriptions of their underlying principles $T_{\text{des}}$, and a clear delineation of their applicable scopes $T_{\text{sco}}$, represented as tuples $(T_{\text{nam}},T_{\text{tag}},T_{\text{des}},T_{\text{sco}})$ extracted from $\mathcal{D}_{\text{temp}}$. We then fine-tune a base LLM, denoted as $\pi$, on this dataset $\mathcal{D}_{\text{train}}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Structure-based Finetuning", "weight": 1.0} -->

This process equips the model with a foundational understanding of the structure, content, and intended use of each template within the library.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Structure-based Finetuning", "weight": 1.0} -->

where the objective is to maximize the likelihood of the model generating the correct description $T_{\text{des}}$ and scope $T_{\text{sco}}$ given the template name $T_{\text{nam}}$ and tags $T_{\text{tag}}$. This ensures that the fine-tuned model can effectively associate the identifying information ($T_{\text{nam}}$ and $T_{\text{tag}}$) of a template with its functional aspects ($T_{\text{des}}$ and $T_{\text{sco}}$). After fine-tuning, we denote the resulting model as $\pi_{\text{struct}}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Preference Learning on Thought Template Trajectory", "weight": 1.0} -->

Based on the finetuned LLM $\pi_{\text{struct}}$, we can further enhance its ability to plan out a sequence of high-level thought templates (i.e., thought template trajectory ${\mathbb{T}}_{\text{traj}}$) for an input problem $x$, associating each step with the most relevant template from the library. This is achieved through our preference learning on thought template trajectory. Specifically, as shown in Figure 1, given an input problem $x$, $\pi_{struct}$ first analyzes and abstracts the problem's conditional information, identifying the core mathematical concepts and relationships involved.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Preference Learning on Thought Template Trajectory", "weight": 1.0} -->

Based on this abstract representation, the navigator $\pi_{\text{struct}}$ then configures a trajectory ${\mathbb{T}}_{\text{traj}} = {\{ s_{1},s_{2},\ldots,s_{n}\}}$, where each $s_{i}$ represents a high-level step in the reasoning process, associated with a specific template name retrieved from the library which could be used to solve the problem, denoted as $T_{i}$. Each retrieved template $T_{i}$ is then instantiated with specific details from the input problem $x$ and provides fine-grained guidance to a separate inference LLM denoted as $\pi_{\text{inf}}$ to solve the problem.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Preference Learning on Thought Template Trajectory", "weight": 1.0} -->

To measure the effectiveness and generalization ability of a given trajectory, we utilize a set of problems $\mathcal{X}_{sim}$ that are similar to the original input problem $x$, including $x$ itself. We then use the instantiated templates along the trajectory ${\mathbb{T}}_{\text{traj}}$ to guide $\pi_{inf}$ in solving each problem $x_{i} \in \mathcal{X}_{sim}$. The average accuracy achieved by $\pi_{inf}$ across these problems serves as the trajectory reward $R{({\mathbb{T}}_{\text{traj}})}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Preference Learning on Thought Template Trajectory", "weight": 1.0} -->

This reward signal is then used to construct optimization pairs, enabling us to further refine the navigator $\pi_{struct}$. To be more specific, for each input problem $x$, we sample multiple different ${\mathbb{T}}_{\text{traj}}$ and evaluate its quality utilizing the template trajectory reward.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Inference Scaling with Scaling Thought Templates", "weight": 1.0} -->

After hierarchical RL process, we refer to optimized navigator $\pi_{\theta}$ as ReasonFlux. Then, we further design a novel inference scaling system by leveraging automatically planned trajectories and dynamically retrieved thought templates. This system, illustrated in Figure 2, involves a multi-round interplay between the ReasonFlux, a structured template library $\mathcal{D}_{\text{temp}}$, and a downstream inference LLM $\pi_{inf}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Inference Scaling with Scaling Thought Templates", "weight": 1.0} -->

Given an input problem $x$, the first task for ReasonFlux is to analyze and extract the core mathematical concepts and relationships embedded within $x$. Based on this abstract representation, denoted as $a{(x)}$. ReasonFlux then configures an optimal template trajectory ${\mathbb{T}}_{\text{traj}}^{\ast}$. This trajectory, represented as a sequence of steps ${\mathbb{T}}_{\text{traj}}^{\ast} = {\{ s_{1}^{\ast},s_{2}^{\ast},\ldots,s_{n}^{\ast}\}}$, is not a rigid, pre-defined path but rather a dynamically generated plan tailored to the specific nuances of the input problem $x$. Each step $s_{i}^{\ast}$ within the trajectory is associated with a specific template name $T_{\text{nam}}$ and $T_{\text{tag}}$ for efficient retrieval.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Inference Scaling with Scaling Thought Templates", "weight": 1.0} -->

ReasonFlux then searches and retrieves a set of most relevant thought templates from the curated thought template library $\mathcal{D}_{\text{temp}}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Inference Scaling with Scaling Thought Templates", "weight": 1.0} -->

where $T_{\text{rag}} = {\{ T_{1},T_{2},\ldots,T_{n}\}}$ is the set of $n$ retrieved templates that equals to the number of steps in the configured trajectory, and each is a structured template.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Inference Scaling with Scaling Thought Templates", "weight": 1.0} -->

The interaction between ReasonFlux and $\pi_{inf}$ is not a one-way process but rather in an iterative manner. After obtaining the instantiated step $\hat{s_{i}}$, it is then evaluated and analyzed by ReasonFlux, and we represented this adjustment as process $\delta_{i} = {\text{ReasonFlux}{({\mathbb{T}}_{\text{traj}}^{\ast},\hat{s_{i}})}}$. Based on this evaluated result and analysis, ReasonFlux decide whether to refine the trajectory, potentially adjusting subsequent steps or even retrieving alternative templates.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Inference Scaling with Scaling Thought Templates", "weight": 1.0} -->

This iterative feedback mechanism between ReasonFlux and $\pi_{inf}$ underscores a crucial aspect of complex problem-solving: the dynamic interplay between planning and execution. By analyzing intermediate results generated during the reasoning process, ReasonFlux gains valuable insights that can inform adjustments to the trajectory. This ability to refine the solution path precisely reflects how humans often uncover more efficient or effective solutions by examining partial results. Furthermore, intermediate steps may reveal previously obscured constraints or opportunities within the problem, allowing for a more informed and targeted approach. Therefore, the hierarchical nature of ReasonFlux, enabled by this iterative refinement, is crucial for navigating the complexities of challenging reasoning tasks and achieving optimal solutions. In summary, ReasonFlux achieves effective problem solving by dynamically configuring and adjusting the template trajectory based on the problem complexity, transcending the limitations of traditional inference methods and offering a more efficient and powerful reasoning framework.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Template Library Construction", "weight": 1.0} -->

As illustrated in Section 3.1, we use Gemini-2.0 to summarize and extracts high-level thoughts from the training sets of various math datasets, such as MATH (7.5K samples), and self-curated CN high-school competition-level data (2K samples), and construct our structured thought template library (approximately 500 thought templates). We provide some template examples in Appendix A.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Training Details", "weight": 1.0} -->

Due to limited GPU resources, we use Qwen2.5-32B-Instruct as the base model and also adopt it as our inference LLM. In our training procedure, we only use 8 NVIDIA A100 GPUs, which is very cost-efficient. In the structure-based finetuning stage (Section 3.2), we train the initialized $\pi_{\text{struct}}$ with the training dataset $\mathcal{D}_{\text{train}}$ containing 15K samples extended from our template library $\mathcal{D}_{\text{temp}}$. We conduct the initialization training for 6 epochs using an AdamW optimizer along with the cosine learning rate scheduler. In the template trajectory optimization process (Section 3.2), we train our ReasonFlux with 10K collected pair-wise trajectories from MATH (7.5k), and self-curated CN high-school competition-level data (2K) for 6 epochs using an AdamW optimizer along with cosine learning rate scheduler.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Evaluation Datasets", "weight": 1.0} -->

To evaluate the complex reasoning capabilities, we choose a broad set of challenging reasoning benchmarks, including MATH, AIME 2024, AMC 2023, OlympiadBench and GaoKao (Chinese College Entrance Exam) En 2023. These benchmarks comprehensively evaluate mathematical reasoning capabilities, and they are all competition-level and Olympic-level problems. Moreover, AIME 2024 and AMC 2023 are highly challenging competition benchmarks, which are of limited sizes of test samples in AMC and AIME and the results are averaged over 16 runs.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Baselines", "weight": 1.0} -->

To demonstrate reasoning ability of ReasonFlux, we compare it with two kinds of strong baseline models: (i) Frontier LLMs contain GPT-4o, Claude, OpenAI o1-preview and o1-mini. We report their performance on our evaluation benchmarks by taking accuracy numbers from different public technical reports. (ii) Open-sourced superior reasoning models contain DeepSeek-Coder-v2-Instruct, Mathstral, NuminaMath-72B, LLaMA3.1, Qwen2.5-Math, SuperCorrect-7B-Instruct, QwQ-32B-Preview, rStar-Math and Sky-T1-32B-Preview (distilled from QwQ-32B-Preview), and DeepSeek-V3, which are widely used and followed open-sourced reasoning models. Both kinds of baselines represent the highest level of mathematical reasoning currently available.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Results on Challenging Reasoning Benchmarks", "weight": 1.0} -->

Table 2 shows the final results of our ReasonFlux with a comprehensive comparison to SOTA reasoning models. We find that our ReasonFlux-32B consistently outperforms both frontier LLMs and open-sourced reasoning LLMs on most challenging mathematical benchmarks, achieving new SOTA performances with only 32B-level parameters. More specifically, on the MATH benchmark, ReasonFlux achieves 91.2% of accuracy, surpassing frontier reasoning models o1-preview by 6.7%, and current SOTA-level open-source LLMs with only 32B parameters. On the AIME 2024 benchmark, ReasonFlux consistently demonstrates its extrodinary reasoning capabilities with 56.7% accuracy, significantly surpassing o1-preview and DeepSeek-V3 by 27% and 45%, respectively, and matching the performance of the proprietary OpenAI o1-mini. On the AMC 2023 benchmark, our method, ReasonFlux, maintains its position within the top tier of all reasoning LLMs with 85.0% accuracy, significantly outperforming other open-source LLMs while achieving performance comparable to proprietary LLMs.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Results on Challenging Reasoning Benchmarks", "weight": 1.0} -->

This further validates the effectiveness of our approach in mathematical reasoning and underscores its substantial potential for further development and application. We provide some reasoning details in Section 4.3.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Results on Challenging Reasoning Benchmarks", "weight": 1.0} -->

Beyond above well-known benchmarks, ReasonFlux-32B also demonstrates impressive generalization and effectiveness on other challenging datasets. Notably, it achieves a 63.3% accuracy on OlympiadBench surpassing DeepSeek-V3 by 14%, and an 83.6% accuracy on the Chinese College Entrance Mathematics Exam (Gaokao) surpassing o1-mini by 7%. These results are particularly noteworthy because our template library was constructed primarily from publicly available datasets, the same template library was used consistently across all evaluation processes. This consistent strong performance across diverse and challenging mathematical reasoning tasks, ranging from competition-level problems to standardized exams, provides compelling evidence for the robust generalization ability and effectiveness of ReasonFlux. It underscores the power of our template-driven approach to capture and apply underlying mathematical principles, regardless of the specific format or context of the problem.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Generalizing to Different Base Models", "weight": 1.0} -->

From Table 2, we also observe that our ReasonFlux can achieve consistent and significant improvement across all evaluation benchmarks when using different base models as both navigator and inference LLM. Notably, our ReasonFlux usually achieves even surpasses the reasoning accuracy of the models in next level. These phenomenons demonstrate both effectiveness and generalization ability of our ReasonFlux.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Generalization Ability of Structured Template Library", "weight": 1.0} -->

We presents additional experiments on MATH benchmark designed to evaluate the generalization ability of our structured template library. To achieve this, we randomly sampled 100 templates from the library, each paired with its corresponding example problem. Subsequently, we employed o1-preview to generate 50 variant problems for each example. These variants were carefully constructed to ensure they differed from the original examples while still assessing the same underlying knowledge and skills.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Generalization Ability of Structured Template Library", "weight": 1.0} -->

We then used these templates as in-context examples to guide different LLMs during inference on the generated variant problems. We compare the average accuracy between our template augmented reasoning and direct reasoning (i.e., solving the problems without template). As illustrated in Table 3, our template-augmented approach significantly improves the reasoning accuracy of different base models compared to direct reasoning. This demonstrates the ability of our structured templates to generalize effectively across a range of similar problems, rather than being limited to specific instances. Furthermore, we observed that smaller-sized LLMs, when guided by our templates, were able to outperform larger-sized LLMs employing direct reasoning. This finding underscores the effectiveness and high quality of our structured template library.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Reasoning Flows over Planned Template Trajectory", "weight": 1.0} -->

We showcase detailed examples of our reasoning flows, as depicted in Figure 3, when tackling challenging mathematical problems. Specifically, ReasonFlux begins by meticulously observing and analyzing the input problem, engaging in deep thought to explore potential solution pathways. Based on this initial assessment, ReasonFlux intelligently configures a dynamic reasoning trajectory, strategically retrieving relevant templates from our structured template library to guide each logical step. Then, ReasonFlux initiates an interactive instruction with the inference LLM, guiding it to follow the prescribed trajectory and execute the reasoning process along the trajectory. Crucially, the results obtained from preceding steps are seamlessly integrated as contextual information, informing and conditioning the subsequent steps. Compare to conventional self-explore and reasoning paradigm, our method could consistently improve the reasoning accuracy and efficiency. Moreover, our ReasonFlux contains more explainable reasoning structures than recent powerful models like DeepSeek-R1 and o3-mini.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Inference Scaling Laws for Template-Augmented Reasoning", "weight": 1.0} -->

Different from traditional inference scaling with Best-of-$N$ and Majority Voting, our ReasonFlux owns a specific interplay-based scaling mechanism. In order to provide a comprehensive understanding of how ReasonFlux automatically trade off between cost and performance. As shown in Figure 4, we demonstrate (i) how number of retrieved templates adaptively scales with increased problem complexity and (ii) how rounds of interplay between ReasonFlux and inference LLMs adaptively scales with increased problem complexity. From the results, we can observe that our ReasonFlux can effectively capture the complexity of input problems, and plan out reasonable template trajectories with appropriate interplay rounds. Utilizing more fine-grained thought templates may boost the scaling effect of our ReasonFlux, and we leave this exploration for future work.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Better Exploration-Exploitation Trade-off", "weight": 1.0} -->

To evaluate the exploration-exploitation trade-off of different reasoning strategies, we conducted an ablation study comparing our proposed interplay method against Best-of-N and MCTS. Each method exhibits a distinct approach to navigating the reasoning space. Best-of-N constructs multiple reasoning trajectories to identify the optimal path, while MCTS iteratively explores the most promising next step during the problem-solving process.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Better Exploration-Exploitation Trade-off", "weight": 1.0} -->

Our method formulates a potential reasoning trajectory and then guides the interactive process with the inference LLM for iterative refinement and adjustments. To ensure a fair comparison, we introduce a unified metric termed "exploration-exploitation cost." This metric quantifies the number of exploration attempts required by each method to correctly solve a given problem. For our method, this denotes the number of interactions between ReasonFlux and the inference LLM. For MCTS, it is represented by the iteration time, and for Best-of-N, it denotes the total number of sampled trajectories.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Better Exploration-Exploitation Trade-off", "weight": 1.0} -->

As illustrated in Figure 5, both MCTS and Best-of-N exhibit an increasing exploration-exploitation cost as problem difficulty escalates. In contrast, our method maintains a consistently lower and more stable exploration cost across all difficulty levels. This superior efficiency of our method can be attributed to the effectiveness of our structured template library. This high-quality library effectively refines the search space, facilitating the identification of correct reasoning paths. Furthermore, the high quality and generalization ability of the templates (experimental analysis in Section 4.2) within the library allows for effective exploitation, guiding the Inference LLM towards accurate and efficient reasoning. Consequently, our approach demonstrates a more balanced and efficient exploration-exploitation trade-off compared to Best-of-N and MCTS.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we present ReasonFlux, a new hierarchical LLM reasoning framework that adaptively scales fundamental and essential thought templates for simplifying the search space of complex reasoning, and outperforming the mathematical reasoning capabilities of powerful LLMs like OpenAI o1-preview and DeepSeek V3. We introduces a structured and compact thought template library, hierarchical reinforcement learning on thought template trajectory and a brand new inference scaling system. Extensive experiments across different challenging math benchmarks demonstrate the superiority of ReasonFlux. We also reveal some key findings, including the scaling laws for our template-augmented reasoning and the superior exploration-exploitation trade-off of our ReasonFlux over previous reasoning strategies.
