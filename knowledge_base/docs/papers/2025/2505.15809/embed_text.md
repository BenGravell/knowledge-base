<!-- arxiv-full-text:v1 {"arxiv_id": "2505.15809", "source": "arxiv-html"} -->

## Introduction

Large language models (LLMs) have revolutionized natural language processing (NLP) by achieving state-of-the-art performance in diverse tasks, from text generation (e.g., ChatGPT ) to complex reasoning (e.g., DeepSeek-R1 ). Inspired by their success, the research community has extended LLMs to the multimodal domain, giving rise to multimodal large language models (MLLMs) or vision-language models (VLMs), such as GPT-4 and Gemini. These models aim to provide a unified framework for both understanding and generating across heterogeneous modalities---text, images, and beyond.

Early multimodal approaches combined language models with diffusion models to handle discrete (e.g., text) and continuous (e.g., image) modalities separately. Subsequent autoregressive (AR) methods simplified architectures by training a single transformer with next-token prediction, unifying discrete and continuous generation in a single model. Another line of work leverages modality-specific training objectives within a shared architecture: for example, Show-o and Transfusion combine autoregressive and diffusion modeling for modeling textual and visual semantics, respectively.

Loss for Language Loss for Vision UniGRPO with Diversified RM UniGRPO with Diversified RM Und. (with Reasoning) Image Gen. (with Reasoning) Text Gen. (with Reasoning) Table 1: Specific design choices employed by different unified multimodal foundation model families, including their core loss functions. The next-token prediction loss is defined as ℒNTP = 𝔼xi[−log Pθ(xi ∣ x < i)], representing the standard negative log-likelihood of generating the next token xi conditioned on its preceding context x < i. The training objective for continuous diffusion models is given by ℒDiff-cont = 𝔼t, x0 ∼ q(x0), ϵ ∼ 𝒩(0, I), c[∥ϵ − ϵθ(xt, t, c)∥2], where xt denotes the noised version of the original data x0 at timestep t, and c is an optional conditioning signal. The model learns to predict the noise ϵ added to the data, thereby enabling the reconstruction of x0 through an iterative denoising process defined as xt − 1 = ℱθ(xt, t). The discrete diffusion (masked token prediction) loss is given by $\mathcal{L}_{\text{Diff-disc}}=\mathbb{E}_{z_{i}^{*}}\left[-\frac{1}{|M|}\sum_{i\in M}\log p_{\theta}(z_{i}^{*}|\mathbf{z}_{\text{masked}}^{(M)})\right]$, which measures the average negative log-likelihood of correctly predicting the original discrete tokens zi* at positions masked by the set M, given the visible context provided by the masked sequence zmasked(M).

Although recent advancements have explored diffusion-based architectures for global context modeling and parallel generation, existing unified multimodal foundation models predominantly focus on model architecture design and pretraining strategies, leaving a critical gap in the exploration of post-training methodologies, particularly in non-autoregressive settings.

To address this gap, we systematically investigate the design space for unified multimodal diffusion foundation models, introducing a novel framework that advances both architectural and training paradigms (a comprehensive comparison in table˜1). This work bridges the gap between pretraining and post-training in unified multimodal diffusion models, offering a holistic framework for future research in this emerging field. Our contributions can be summarized as: Unified Diffusion Foundation Architecture: We propose MMaDA, a class of diffusion-based models that extend traditional generators into generalist task solvers via a shared probabilistic formulation and modality-agnostic architecture. This design eliminates modality-specific components while maintaining strong performance across tasks.

Mixed Long-CoT Post-Training: We introduce mixed long chain-of-thought (CoT) finetuning to enable cold-start training. By curating a unified CoT format across tasks, we align reasoning processes between modalities (e.g., textual and visual), fostering cross-modal synergy and learning intermediate reasoning before final output generation.

Unified Reinforcement Learning (UniGRPO): We develop a unified diffusion-centric reinforcement learning algorithm (UniGRPO) tailored for multimodal generation. This approach leverages diversified reward modeling to enhance the model's ability to perform complex reasoning and maintain factual consistency in generation.

State-of-the-Art Performance: MMaDA achieves superior and balanced performance across three critical tasks: textual reasoning, multimodal understanding, and text-to-image generation. Notably, it outperforms both autoregressive and diffusion-based baselines in terms of accuracy, efficiency, and task adaptability.

Figure 1: Qualitative comparison across three tasks (more results in section˜10 and section˜11.).

Figure 2: An overview of MMaDA pipeline.

## MMaDA: Multimodal Large Diffusion Language Models

### Pretraining with Unified Diffusion Architecture and Objective

### Data Tokenization

To establish a unified modeling framework capable of processing both textual and visual data, we adopt a consistent discrete tokenization strategy across both modalities. This design enables the model to operate under a single modeling objective, i.e., the prediction of discrete masked tokens. For text tokenization, we utilize the tokenizer from LLaDA, which serves as the backbone for our MMaDA model. For image tokenization, we leverage the pretrained image quantizer adopted from Show-o, which is based on the MAGVIT-v2 architecture and converts raw image pixels into sequences of discrete semantic tokens. Given an input image with dimensions $H\times W$, the encoder generates a token map with dimensions $\frac{H}{f}\times\frac{W}{f}$, where $f$ represents the downsampling factor. In this implementation, we employ a downsampling factor of $f=16$ and a codebook size of 8192. This configuration transforms a $512\times 512$ pixel image into a sequence of $32\times 32=1024$ discrete tokens. The transformed discrete image tokens are used in both understanding and generation modeling tasks.

### Unified Probabilistic Formulation for Pretraining

Recent unified multimodal frameworks aim to integrate multiple modeling objectives---such as autoregressive generation and diffusion-based denoising---into a single architecture for joint understanding and generation tasks (see preliminaries in section˜8.1). However, these approaches often introduce complex hybrid mechanisms that hinder model efficiency and coherence. In contrast, we propose a streamlined framework that not only simplifies the architectural complexity but also introduces a unified diffusion objective to model both visual and textual modalities under a shared probabilistic formulation. By aligning the noise corruption and semantic recovery processes across modalities, we enable more effective cross-modal interactions during pretraining, facilitating seamless integration of heterogeneous data sources.

Specifically, we formulate MMaDA as a mask token predictor (for both image and text tokens), a parametric model $p_{\theta}(\cdot|x_{t})$ that takes $x_{t}$ as input and predicts all masked tokens simultaneously. The model is trained with a unified cross-entropy loss computed only on the masked image/text tokens: where $x_{0}$ is ground truth, the timestep $t$ is sampled uniformly from $$, and $x_{t}$ is obtained by applying the forward diffusion process to $x_{0}$. $\textbf{I}[\cdot]$ denotes the indicator function to ensure that the loss is computed only over the masked tokens. Specific pretraining tasks are detailed in section˜4.

### Post-Training with Mixed Long-CoT Finetuning

### Cold Start Long-CoT Data Curation

We investigate how CoT mechanisms can enhance post-training for our unified multimodal diffusion framework and observe their effectiveness in promoting cross-modal synergies. To this end, we curate a compact dataset of long CoT trajectories across three core tasks: textual reasoning, multimodal reasoning, and text-to-image generation. This dataset enables stable post-training of our pretrained MMaDA model through the following principles: Unified CoT Format: A critical challenge in vision-language foundation models is the heterogeneity of output formats across tasks (e.g., text vs. image generation). We propose a task-agnostic CoT format: \|\<special_token\>\|\<reasoning_process\>\|\<special_token\>\|\<result\>. The '\<reasoning_process\>' encodes step-by-step reasoning trajectories preceding the final output. This unified structure bridges modality-specific outputs and facilitates knowledge transfer between tasks. For instance, enhanced textual reasoning capabilities directly improve the realism of generated images by aligning semantic logic with visual synthesis.

Diversity, Complexity, and Accuracy: We leverage open-source large language and vision-language models (LLM/VLMs) to generate diverse reasoning trajectories across tasks (in figure˜2). To ensure quality, we employ state-of-the-art models as verifiers to filter out inaccurate or shallow reasoning, selecting only high-quality, long-form CoT samples. Unlike prior unified models that focus on generic understanding and generation, our MMaDA is explicitly designed: Reasoning-intensive tasks (e.g., mathematical problem-solving), and World-knowledge-aware text-to-image generation, where factual consistency is critical.

### Mixed Long-CoT Finetuning

Leveraging our unified diffusion architecture and probabilistic formulation, we develop a mixed-task long-CoT finetuning strategy to jointly optimize the model across heterogeneous tasks. This approach not only enhances task-specific capabilities but also creates a strong initialization for subsequent reinforcement learning (RL) stages. The training process follows these steps: Prompt Preservation and Token Masking: We retain the original prompt $p_{0}$ and independently mask tokens in the result ($x_{0}$), denoted as $r_{t}$.

Joint Input and Loss Computation: The concatenated input $[p_{0},r_{t}]$ is fed into our pre-trained mask predictor to compute the loss. This enables the model to reconstruct masked regions ($r_{0}$) using contextual information from both the prompt and corrupted result.

The objective function is defined as: where $L^{\prime}$ denotes the sequence length. Here, $[p_{0},r_{0}]$ and $[p_{0},r_{t}]$ correspond to the clean data $x_{0}$ and its noisy counterpart $x_{t}$, respectively. This formulation ensures the model learns to recover masked tokens while maintaining alignment with the original prompt and task-specific reasoning logic.

### Post-Training with Unified Reinforcement Learning

### Unified GRPO for Diffusion Foundation Models

With our mixed long-CoT fine-tuning, MMaDA demonstrates the ability to generate unified and coherent reasoning chains prior to final outputs. To further enhance its performance on knowledge-intensive tasks and complex reasoning/generation scenarios, we propose UniGRPO, a novel policy-gradient-based reinforcement learning algorithm tailored for diffusion foundation models. This approach enables a diffusion-centric RL training framework that unifies task-specific objectives across diverse modalities and reasoning paradigms. The method is structured into two core components: a unified mathematical formulation for diffusion-based RL, and diversified reward modeling to align policy gradients with task-specific rewards.

### Challenges in Adapting Autoregressive GRPO to Diffusion Models

The original GRPO relies on computing token-level log-likelihoods $\pi_{\theta}(o_{i,t}|q,o_{i,<t})$ and sequence-level probabilities $\pi_{\theta}$ and $\pi_{ref}$ (preliminary in section˜8.2). In autoregressive (AR) LLMs, these metrics are efficiently derived via the chain rule of generation. However, diffusion models introduce three critical challenges: \(1\) Local Masking Dependency: Token-level log-likelihoods $\log\pi_{\theta}(o_{i,t}|q,o_{i,<t})$ are only valid within masked regions during the diffusion process, unlike AR models where all tokens are valid.

\(2\) Mask Ratio Sensitivity: A uniform mask ratio must be sampled for the response segment to approximate the policy distribution $\pi_{\theta}$, as diffusion dynamics depend on masking patterns.

\(3\) Non-Autoregressive Sequence-Level Likelihoods: The sequence-level log-likelihood cannot be directly accumulated from token-level probabilities due to the absence of an autoregressive chain rule in diffusion models.

Prior approaches address these issues with suboptimal strategies. LLaDA employs Monte Carlo sampling over numerous mask ratios (e.g., 128 samples), incurring high computational costs for on-policy RL. d1 fixes the mask ratio and randomizes question masking, which reduces noise diversity and ignores the multi-step denoising nature of diffusion.

### Unified Formulation for Diffusion GRPO

To overcome these limitations, we introduce UniGRPO, a computationally efficient approximation algorithm designed for diffusion architectures. Given a batch of responses $\{o_{i}\}_{i=1}^{G}$ for a query $q$, each response is fixed during gradient updates to ensure stable policy evaluation. We highlight three critical points of our UniGRPO as: Structured Noising Strategy: For each $o_{i}$, we sample a masking ratio $p_{i}\in$ uniformly and construct a perturbed version $\tilde{o}_{i,p}$ by replacing tokens with \[MASK\]. The random seed for $p_{i}$ varies across gradient steps. This strategy aims to preserve stochasticity while ensuring the model is exposed to various stages of the diffusion denoising process, from nearly fully masked to nearly fully denoised answers. By doing so, UniGRPO learns from multi-step denoising information, which is consistent with conventional training methodologies for diffusion models and allows for the full utilization of their multi-step generative power.

Efficient Log-Likelihood Approximation: We define the expected per-token log-likelihood under the perturbed distribution as: The sequence-level log-likelihood is then approximated by averaging over masked tokens: Policy Gradient Objective: The per-token reward is computed as the ratio between current and old policy likelihoods: $r_{i,t}^{\prime}(\theta)=\frac{\pi^{\prime}_{\theta}(o_{i,t}\mid q,\tilde{o},p_{i})}{\pi^{\prime}_{\text{old}}(o_{i,t}\mid q,\tilde{o},p_{i})}.$ The final UniGRPO objective integrates clipped surrogate rewards and KL regularization: | | $\displaystyle\mathcal{J}_{\text{UniGRPO}}(\theta)$ | $\displaystyle=\mathbb{E}_{(q,a)\sim\mathcal{D},\{o_{i}\}_{i=1}^{G}\sim\pi_{\theta_{\text{old}}}(\cdot\mid q),\{p_{i}\in\}_{i=1}^{G}}\Bigg[\frac{1}{G}\sum_{i=1}^{G}\frac{1}{|o_{i}|}\sum_{t=1}^{|o_{i}|}\Bigg(\min\Big(r_{i,t}^{\prime}(\theta)\hat{A}_{i,t},$ | | \(5\) | | | | $\displaystyle\quad\quad\text{clip}\Big(r_{i,t}^{\prime}(\theta),1-\varepsilon,1+\varepsilon\Big)\hat{A}_{i,t}\Big)-\beta D_{\text{KL}}(\pi^{\prime}_{\theta}||\pi^{\prime}_{\text{ref}})\Bigg)\Bigg],$ | | | where $\hat{A}_{i,t}$ denotes the advantage estimate, $\varepsilon$ controls the clipping range, and $\beta$ balances the KL divergence penalty.

Through this design, UniGRPO captures the essential multi-step denoising dynamics of diffusion models. By allowing the model to predict answers under diverse masking conditions while preserving the natural structure of the input, it avoids the pitfalls of both computational inefficiency (as in LLaDA) and oversimplified prediction (as in d1). The training procedure of UniGRPO is outlined in algorithm˜1. For further details on the UniGRPO algorithm, please refer to section˜9 and section˜5.2.

1:Reference model πref, prompt distribution 𝒟, number of completions per prompt G, number of inner updates μ, diffusion steps T 2:Initialize policy πθ ← πref 3:while not converged do 6: Sample G completions oi ∼ πold(⋅ ∣ q), for i ∈ [G] 7: For each oi, compute reward ri and advantage Aik(πold) using equation˜15 8: Sample a starting timestep t0 ∼ 𝒰(0, T − 1) 9: Generate μ − 1 uniformly spaced timesteps t1, …, tμ − 1 from [t0, T] 10: for gradient update iterations n = 1, …, μ do 12: Sample a starting mask ratio r1 ∼ 𝒰 and compute initial timestep t1 = ⌊r1 ⋅ T⌋ 14: Uniformly divide remaining timesteps: $t_{n}=\lfloor\frac{(n-1)}{(\mu-1)}\cdot(T-t_{1})+t_{1}\rfloor$ 15: Construct input (q, masked oi) using timestep tn (with q always unmasked) 16: For πθ, πold, πref, estimate log-probabilities of masked tokens in oi at tn 17: Compute UniGRPO objective equation˜5 and update πθ via gradient descent Algorithm 1 UniGRPO Policy Gradient Optimization

### Diversified Reward Modeling

We further simplify the optimization objective of UniGRPO (equation˜5) as follows: where $R^{\text{Uni}}(o)$ denotes the reward obtained from the model-generated response $o$, $P(\cdot)$ is the penalty term, which denotes the KL divergence as specified in equation˜5. This is a unified rule-based reward system, where $R^{\text{Uni}}(\cdot)$ can be instantiated with diverse rewards for different tasks. To address the varied requirements of different tasks, we have defined a range of rewards under the unified formulation equation˜6, providing tailored RL optimization directions for each task branch. We mainly adopt three types of rewards: Textual Reasoning Rewards: We apply UniGRPO on the training split of the GSM8K dataset and define a composite reward. This includes a Correctness Reward of $2.0$ for a correct answer, and a Format Reward of $0.5$ if the response adheres to our predefined format: "\<think\>...\</think\>".

Multimodal Reasoning Rewards: For mathematical tasks such as GeoQA and CLEVR, we adopt the same Correctness and Format Rewards as in textual reasoning. In addition, for caption-based tasks, we further introduce a CLIP Reward of $0.1\cdot\text{CLIP}(\text{image},\text{text})$, where the original CLIP score measuring text-image alignment is scaled by $0.1$ to balance its influence.

Text-to-Image Generation Rewards: For image generation tasks, we incorporate the same CLIP Reward to assess text-image semantic alignment, alongside an Image Reward that reflects human preference scores. Both rewards are scaled by a factor of $0.1$ to ensure balanced contribution during optimization.

## Flexible Sampling Strategies at Inference Time

### Semi-Autoregressive Sampling for Text Generation

For text generation, we adopt the semi-autoregressive denoising strategy introduced in LLaDA, which integrates autoregressive decoding with diffusion-based denoising. Specifically, the output sequence is partitioned into multiple blocks and generated from left to right. Within each block, logits are computed for all masked positions, and a subset of tokens is selected---either randomly or based on confidence scores---for denoising. The masking schedule follows a linear schedule, consistent with LLaDA. The denoising process is repeated for given steps.

In our evaluation, we set the total sequence length to $N=1024$ and perform $\frac{N}{2}=512$ denoising steps. The sequence is divided into blocks of 64 tokens. At each step, we unmask the 2 tokens with the lowest confidence within the current block, irrespective of their positions. Once all tokens in a block are denoised, the process proceeds to the next block. A qualitative comparison is provided below. As shown, a semi-autoregressive denoising strategy tends to generate more intricate and detailed descriptions, whereas non-autoregressive fixed-length generation often produces very short responses. This observation is consistent with findings reported for LLaDA. For instruction-tuned models, given that the training process incorporates a substantial number of \|EOS\| tokens, directly applying the lowest-confidence remasking strategy without dividing into blocks leads to an unnaturally high frequency of \|EOS\| tokens in the generated sentences.

### Parallel Non-Autoregressive Sampling for Image Generation

For image generation, we adopt a low-confidence remasking strategy and follow a cosine noise schedule, consistent with the setup in MAGVIT-v2. In contrast to text generation, we do not employ a semi-autoregressive approach; instead, the entire output sequence is treated as a single generation block. During evaluation, we generate sequences of length 1024, corresponding to 512$\times$`<!-- -->`{=html}512 resolution images. The denoising process consists of 50 timesteps, and we apply classifier-free guidance with a guidance scale set to 3.5.

Unified Understanding & Generation Table 2: Evaluation on Multimodal Understanding Benchmarks.

## Experiments

### Experimental Setup

### Datasets

To train MMaDA, we utilized a diverse range of datasets tailored for corresponding training stages as follows: Foundational Language and Multimodal Data: For basic text generation capabilities, we adopt the RefinedWeb dataset. For multimodal understanding and generation tasks, we incorporate widely-used open-sourced image-text datasets. Instruction Tuning Data: To enhance instruction-following capabilities, we use Alpaca for textual instructions and LLaVA-1.5 for visual instruction tuning. Reasoning Data: For Mixed Long-CoT finetuning, we curated a diverse set of reasoning datasets. For textual mathematical and logical reasoning, we employed datasets from ReasonFlux, LIMO, s1k, OpenThoughts, and AceMath-Instruct. For multimodal reasoning, we used the LMM-R1 model to generate responses on GeoQA and CLEVR, and retained correctly answered instances. Additionally, for world knowledge-aware image generation, we used GPT-4.1 to synthesize factual item-description pairs spanning science, culture, and landmarks, formatted into unified CoT-style traces. Reinforcement Learning Data: For UniGRPO training, we adopt the original mathematical and logical datasets used in Reasoning.

### Evaluation and Baselines

We evaluate our MMaDA on three distinct tasks using task-specific metrics and baselines: Multimodal Understanding: Following LLaVA, we evaluate on POPE, MME VQAv2, GQA, and MMMU, and compare against understanding-only models, as well as unified models. Image Generation: We assess generation quality using 50K prompts from our test set to compute CLIP Score and ImageReward to evaluate textual alignment and human preference alignment. We adopt GenEval for general evaluation and WISE for evaluating world knowledge-based generation, comparing against generation-specific models and unified baselines. Text Generation: we evaluate instruction-following and reasoning performance on MMLU, GSM8K, and related benchmarks, comparing with LLaMA2-7B, Qwen2-7B, and LLaDA-8B.

### Implementation Details

We initialize MMaDA with LLaDA-8B-Instruct's pretrained weights and an image tokenizer with Show-o's pretrained ones. We perform joint training across three stages: Stage1: The initial model is trained for 200K steps using foundational language and multimodal data, including RefinedWeb for text generation, ImageNet-1k for class-conditional image generation, and additional image-text datasets for captioning. This is followed by another 400K steps where ImageNet is replaced with more diverse image-text pairs. Stage2: The model is then jointly trained for 50,000 steps using Instruction Tuning Data and Reasoning Data. Stage3: This final stage consists of UniGRPO training with Reinforcement Learning Data for 50,000 steps. Training is performed on 64 A100 (80GB) GPUs using a global batch size of 1,280. The AdamW optimizer is employed with an initial learning rate of 5e-5 and a cosine learning rate scheduler.

### Multimodal Understanding

Table 2 reports the multimodal understanding performance of our method on standard benchmarks, including POPE, MME VQAv2, GQA, and MMMU. For outputs from MMaDA that contain reasoning traces, we use the final answer as the prediction. Compared with dedicated understanding-only models such as LLaVA-v1.5, InstructBLIP, and Qwen-VL-Chat, our model achieves comparable or superior results across most benchmarks, despite being trained under a unified objective. When compared to other unified models (e.g., SEED-X, DreamLLM, Janus, Emu3, and Show-o), our method consistently outperforms them across several benchmarks, particularly benefiting from the proposed Mixed Long-CoT Finetuning and UniGRPO Reinforcement Learning stages. Notably, this is the first demonstration of a diffusion-based MLLM exhibiting strong understanding capabilities, highlighting the potential of our unified architecture in bridging generation and understanding tasks. Qualitative results are in section˜10 ‣ MMaDA: Multimodal Large Diffusion Language Models") and section˜11 ‣ MMaDA: Multimodal Large Diffusion Language Models").

### Text-to-Image Generation

Unified Understanding & Generation Table 3: Evaluation on Image Generation Benchmarks.

Table 3 presents the evaluation results on text-to-image generation benchmarks. Our model achieves the highest performance in both CLIP Score and ImageReward across generation-only and unified models, attributed to the UniGRPO training stage with rewards explicitly aligned to these metrics. Furthermore, our method demonstrates superior compositionality and object counting capabilities on GenEval, benefiting from the reasoning-intensive training of the understanding branch. Notably, on WISE Cultural benchmark, which is designed to evaluate world knowledge-aware generation, our model significantly outperforms prior approaches, owing to its joint training on text-based reasoning, which is typically absent in existing unified models. Qualitative results are in section˜10 ‣ MMaDA: Multimodal Large Diffusion Language Models") and section˜11 ‣ MMaDA: Multimodal Large Diffusion Language Models").

### Textual Reasoning

Table 4: Evaluation on LLM Benchmarks. table˜4 details the language modeling performance of MMaDA across a range of benchmarks, encompassing general tasks such as MMLU, ARC-C, and TruthfulQA, as well as mathematical tasks including GSM8K, MATH, and GPQA. Despite being trained on limited task-specific tokens and solely open-source text data, MMaDA achieves comparable performance compared to strong baselines such as Qwen2-7B and LLaMA3-8B on MMLU, ARC-C, and consistently outperforms LLaDA-8B on math benchmarks. Notably, MMaDA (Ours) pioneers the joint training of a unified diffusion model for text generation, multimodal reasoning, and image generation---a multi-task configuration rarely explored in prior unified architectures. These results underscore the viability of diffusion-based models as general-purpose LLMs and indicate potential for stronger future performance through enhanced text data and scaling. Qualitative results are in section˜10 ‣ MMaDA: Multimodal Large Diffusion Language Models").

## Observations, Analysis and Conclusion

### Ablation Study

We present quantitative ablation results of our MMaDA across different training stages: Mixed Long-CoT fine-tuning and UniGRPO. All results generated follow the sampling process in section˜3. As shown in the table˜5, after Stage 1, our model still lags behind most baselines. In Stage 2, Mixed Long-CoT fine-tuning substantially enhances the model's reasoning capabilities, particularly in mathematical and geometric domains. In Stage 3, UniGRPO further improves performance, allowing the model to achieve results comparable to state-of-the-art methods across various tasks, including mathematical reasoning, geometric problem-solving, and image generation benchmarks such as CLIP Score and ImageReward. These results demonstrate that UniGRPO effectively boosts both the model's understanding/reasoning and generative capabilities.

### Design Choices of UniGRPO

### Effect of General Masking Strategy

Figure 3: Comparison of different masking strategies on GSM8K reward trends during training.

To evaluate the impact of our proposed masking strategy, we first conduct a comparative analysis with d1 within our reinforcement learning framework. Given the substantial computational cost associated with large-scale ablation studies, we perform these experiments on the GSM8K dataset, utilizing 8 A100 GPUs. Both the original d1 methodology and our UniGRPO approach are applied to this dataset, starting from the same pre-trained checkpoint of our MMaDA. We present the reward trends during training in figure˜3. As shown in the figure, our method consistently achieves higher reward values during training, aligning well with our theoretical analysis. In contrast to d1, UniGRPO removes masking from the question and applies partial masking to the answer rather than masking it entirely. This results in input sequences that retain partial noise, encouraging the model to learn across multiple denoising timesteps. Consequently, this better leverages the intrinsic characteristics of diffusion models and improves the overall learning capacity.

### Effect of Uniformly Random masking

Figure 4: Comparison of different random masking strategies on GSM8K reward trends during training.

In place of fully random masking across iterations, we adopt a uniformly random masking strategy for the answer portion. Specifically, we first sample a random starting timestep, and then uniformly generate the remaining denoising timesteps across the full diffusion timesteps (set to 1000 in our experiments). For instance, given a randomly selected starting timestep of 100 and a total of 5 training iterations, the remaining timesteps are uniformly spaced and set to 300, 500, 700, and 900. This design ensures a more consistent coverage of the diffusion process while retaining randomness. We illustrate the training reward trends resulting from this structured masking strategy in figure˜4. As shown, the baseline approach with fully random timestep selection tends to introduce instability during training, leading to more frequent reward fluctuations and requiring a greater number of steps to converge. In contrast, our uniformly spaced sampling strategy effectively approximates the behavior of Monte Carlo averaging in log-likelihood estimation, resulting in improved stability and faster convergence.

Figure 5: Qualitative Illustration of Synergy Across Modalities.

MMaDA After Stage 1

+ Mixed Long-CoT Finetuning Table 5: Ablations on Mixed Long-CoT fine-tuning and UniGRPO

### Synergy Across Various Tasks

Figure 6: Key Performance Metrics Across Three Tasks.

Throughout the joint training process, we observe a clear synergy across the three task categories---text generation, multimodal understanding, and image generation. As shown in figure˜6, all key performance metrics exhibit consistent improvements during Stage 2 (training steps 120K--200K), reflecting the mutually beneficial nature of our unified training framework. This synergy is also evident qualitatively: as illustrated in figure˜5, the model's responses---both textual and visual---become increasingly complex and coherent. Specifically, textual outputs grow more informative and logically structured, while visual understanding yields more precise and grounded descriptions. Consequently, for the same prompt, the generated images become more accurate, detailed, and better aligned with the given instructions, demonstrating the effectiveness of joint optimization in enhancing cross-modal alignment and compositionality.

### Sampling Efficiency

Table 6: Generation performance of MMaDA under different denoising steps. * Metrics: CLIP Score for image generation and multimodal understanding, MMLU accuracy for text generation.

We identify sampling efficiency as a key advantage of diffusion models over autoregressive (AR) approaches. Unlike AR models, which generate tokens sequentially, diffusion models enable parallel token generation within each denoising step, substantially reducing the number of forward passes required. To quantify this advantage, we evaluate the performance of MMaDA under varying numbers of denoising steps. In our setup, generation begins from 1024 \[MASK\] tokens, allowing up to 1024 denoising steps---corresponding to a $512\times 512$ resolution image. As shown in table˜6, image generation maintains strong performance even with as few as 15 or 50 steps. For text and multimodal tasks, coherent outputs can be achieved with just a quarter or half of the full steps. These results underscore the efficiency potential of diffusion-based language models and suggest that future advances in sampling techniques or higher-order solvers could further enhance their speed and quality.

### Task Extension

Figure 7: Inpainting Task Extension.

A notable advantage of diffusion-based models is their natural ability to perform inpainting and extrapolation without requiring additional fine-tuning. This stems from the fact that these tasks can be formulated as masked token prediction problems, which are inherently integrated into the training objective of diffusion models. While prior work such as Show-o demonstrates this property only in the context of image generation, MMaDA extends it further to multimodal understanding and text generation. As illustrated in Figure 7, our model supports inpainting across three modalities: (i) predicting missing spans in text sequences, (ii) completing answers in visual question answering given an image and partial input, and (iii) performing image inpainting conditioned on incomplete visual prompts. These examples showcase the flexibility and generalization capabilities of our unified diffusion architecture across diverse generation and reasoning tasks.

## Related Work

### Multimodal Large Language Models for Multimodal Understanding

Recent developments in large language models (LLMs) such as Gemini-2.0, o1-preview, and DeepSeek-R1 have improved the evolution of multimodal large language models (MLLMs). Early efforts in this domain, including LLaVA, MiniGPT-4, and InstructBLIP, showcased impressive capabilities in multimodal understanding. These studies advanced the integration of LLMs into multimodal contexts by projecting features from pre-trained modality-specific encoders, such as CLIP, into the input space of LLMs, thereby facilitating multimodal understanding and reasoning within a unified transformer. Many efforts have been made for MLLMs regarding vision encoders, alignment adapters, and curated datasets, and most of them follow an autoregressive generation paradigm that has been proven effective for text generation in LLMs. However, they are usually not capable of performing textual and multimodal reasoning concurrently. In this work, MMaDA develops diffusion foundation models to fill this gap.

### Diffusion Models and Autoregressive Models for Visual Generation

A large number of diffusion models have demonstrated notable success in visual generation. In addition to the typical denoising diffusion process on the continuous space, a series of frameworks, such as D3PM and VQ-Diffusion, adopt discrete diffusion modeling for visual generation. Specifically, the image is denoted as a sequence of discrete tokens using pretrained image tokenizers. In tthe raining stage, the model is optimized to recover the original values of a portion of these tokens that are randomly masked. Transformer series has demonstrated significant capabilities in autoregressive modeling for NLP tasks. Many approaches try to apply the autoregressive modeling to perform visual generation by modeling semantic dependency within visual details. For example, LlamaGen employs Llama architectures and refines codebook design to enhance the performance of discrete tokenizers in class-conditional image generation. VAR replaces the "next-token prediction" paradigm with "next-scale prediction" by designing a multi-scale image tokenizer. However, existing autoregressive methods still lag behind diffusion methods in terms of visual generation capabilities. In this work, MMaDA train diffusion models to model textual and visual contents, and infer efficiently with AR or Semi-AR sampling.

### Unified Vision-Language Foundation Models

Recently, numerous studies have focused on developing unified multimodal foundation models that excel in both understanding and generation. Approaches such as SEED-X and DreamLLM, along with others, represent all modalities as a series of tokens and employ a unified transformer architecture to train the entire system end-to-end. For example, Emu3 trains a single transformer from scratch using a mixture of multimodal tokenized sequences, optimized solely with next-token prediction. While these unified autoregressive models show promise, they can struggle with visual generation tasks. Transfusion and Show-o employ autoregressive modeling for text generation and diffusion modeling for visual generation. Nevertheless, they mainly focus on pretraining strategies. Exploring effective post-training designs is still lacking for existing unified multimodal foundation models.

## Conclusion

This work introduces a unified diffusion foundation model, namely MMaDA, that integrates textual reasoning, multimodal understanding, and generation within a single probabilistic framework. To the best of our knowledge, MMaDA is the first to systematically explore the design space of diffusion-based foundation models, proposing novel post-training strategies. Extensive experiments across diverse vision-language tasks demonstrate that MMaDA is comparable to or even better than specialized models, highlighting the potential of diffusion models as a next-generation foundation paradigm for multimodal intelligence. However, MMaDA also has limitations due to its current model size (8B parameters), and we will use a larger model size for better performance.
