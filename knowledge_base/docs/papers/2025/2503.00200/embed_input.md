<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Unified Video Action Model

Topics include Vision-language-action models, Video prediction, Robot learning, Action prediction, Unified models, Robotics.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Proposes a unified video-action model that jointly predicts future video and robot actions, using each signal to improve the other. The paper is relevant for robotics world-model and policy-learning work because it tries to combine generative scene understanding with efficient action prediction in one architecture.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A unified video and action model holds significant promise for robotics, where videos provide rich scene information for action prediction, and actions provide dynamics information for video prediction. However, effectively combining video generation and action prediction remains challenging, and current video generation-based methods struggle to match the performance of direct policy learning in action accuracy and inference speed. To bridge this gap, we introduce the Unified Video Action model (UVA), which jointly optimizes video and action predictions to achieve both high accuracy and efficient action inference. The key lies in learning a joint video-action latent representation and decoupling video-action decoding. The joint latent representation bridges the visual and action domains, effectively modeling the relationship between video and action sequences. Meanwhile, the decoupled decoding, powered by two lightweight diffusion heads, enables high-speed action inference by bypassing video generation during inference. Such a unified framework further enables versatile functionality through masked input training. By selectively masking actions or videos, a single model can tackle diverse tasks beyond policy learning, such as forward and inverse dynamics modeling and video generation.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Via an extensive set of experiments, we demonstrate that UVA can serve as a general-purpose solution for a wide range of robotics tasks, such as policy learning, forward/inverse dynamics and video observation prediction, without compromising performance compared to methods tailored for specific applications. Results are best viewed on

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A unified video and action model that jointly learns an agent's actions and their effects on visual observations holds great promise for robotics -- videos provide rich environmental context for predicting actions, while actions reveal how interactions drive visual changes, enabling more accurate modeling of real-world dynamics. However, despite its promise, previous approaches have often failed to fully realize this potential. A key challenge lies in the inherent mismatch between the requirements of action and video generation. Action modeling demands high temporal speed to capture dense, fine-grained motions, while video generation requires high spatial resolution to produce high-fidelity visual outputs, which often results in slower processing speeds.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Previous policy learning approaches have struggled to balance these conflicting requirements, often focusing on one aspect at the expense of the other. For instance, action only methods like bypass video generation entirely. While such approaches reduce computational complexity, they overlook the benefits of video generation -- adding observation supervision helps the model learn scene dynamics, which reduces overfitting to action history and enhances robustness to visual disturbances. On the other hand, video generation methods such as often first generate high-resolution videos and then predict actions based on the generated videos. While this hierarchical approach can utilize existing video models, it also introduces significant drawbacks, including slower processing speeds and the propagation of errors from the generated video into action prediction.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address these limitations, we propose UVA, a Unified Video and Action Model designed to simultaneously model videos and actions -- capturing the underlying interactions between visuals and actions to enhance task understanding, while maintaining high-speed action prediction during inference.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

1\) Unified Latent Video-Action Representation: UVA introduces a unified latent representation that integrates both visual and action data. Unlike traditional video generation based policy methods which rely on a hierarchical video and action generation, UVA is trained simultaneously with supervision from both video and action data. This enables the model to capture the intricate dynamics shared between the visual and action domains with reduced computational overhead. Utilizing the rich scene information encoded in the latent representation unlocks UVA's superior performance in understanding complex environments and delivering precise action predictions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

2\) Decoupled Video-Action Diffusion for Fast Inference: To further enhance efficiency and achieve inference speed comparable to action-only methods, UVA decouples video generation from action prediction. During training, the model employs two lightweight diffusion heads to decode video observations and actions from the unified latent space. At inference, this decoupling allows the system to bypass video generation entirely, directly utilizing the latent representation for fast action prediction. This design enables real-time policy deployment without sacrificing performance, as it still retains the rich representations learned during training from both visual motions and robot action trajectories.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

3\) Mask Training for Flexibility: The ability to predict both videos and actions through unified representations further unlocks the potential to perform a diverse set of functions using masked training. UVA can handle versatile functions that go beyond traditional policy learning by masking inputs and outputs as needed, as illustrated in Unified Video Action Model. This versatility enables the model to tackle complex scenarios, such as operating as a forward or inverse dynamics model, learning effectively from video-only datasets where action labels are unavailable, or simultaneously performing both low-level control and high-level planning.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate UVA on seven publicly available benchmarks to assess its diverse capabilities. UVA outperforms or matches state-of-the-art approaches, demonstrating particularly strong performance in multi-task settings. For instance, UVA outperforms the best baseline by 20% in success rate on PushT Multitask and by 5%. The experiments show that UVA can serve as a general-purpose framework for different robotics tasks without compromising performance compared to methods tailored for specific applications.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Capable: UVA matches the state-of-the-art approaches that are tailored for robot policy learning or planning, especially for multi-task learning.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Practical: The use of decoupled diffusion heads eliminates the need for video generation during policy inference, and the use of lightweight diffusion heads reduces the costs of the denoising process. As a result, UVA achieves a similar speed as Diffusion Policy, making it practical for robot applications.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Versatile: Beyond policy learning, UVA can also serve as a forward dynamics model for planning, as an inverse dynamics model to generate actions, a video generation model, or a combined policy and video planner.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Unified Video Action Model", "weight": 1.0} -->

In robotics, we are interested in learning generalizable policies that map observations to actions. However, this objective often tends to overfit the training data, thereby limiting the ability of learned policies to adapt to new scenarios. In contrast, video generation demonstrates strong generalization to novel scenes and supports training on datasets without actions. However, effectively leveraging video data for policy learning presents challenges such as the ability to match the high temporal speed required for outputting dense, fine-grained motions. In this section, we discuss our approach to leveraging video-generation methods for robotics tasks.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Unified Video Action Model", "weight": 1.0} -->

Each action chunk, e.g., $\mathbf{A}_{\mathbf{t}} \in {\mathbb{R}}^{L \times m}$ consists of $L$ actions, and each action has $m$ dimensions. We set $h = h^{\prime}$ in the experiments. For simplicity, we refer to both as $h$ in the following sections.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Unified Video Action Model", "weight": 1.0} -->

We first introduce the model with complete video and action inputs and outputs (§III-A-§III-C). We then discuss how masked training can flexibly learn from any combination of video and action data (§III-D), enabling UVA to perform various functions, including policy learning, video generation, forward and inverse dynamics, and integrated policy and planning.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Unified Video Action Model", "weight": 1.0} -->

As shown in Figure 2, our method encodes the history of observations and actions (§III-A), along with masked future observations (§III-B), and passes them to the Transformer. For the masked observations, we randomly mask tokens within the future observation frames during training and train the model to reconstruct them. During inference, the model generates the full set of tokens, starting from an empty sequence. In §III-C, we then discuss the choice of decoupling video-action diffusion for fast inference addressing the high temporal speed demand of robot policies.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A Encode History", "weight": 1.0} -->

We first process the historical image observations through a pre-trained VAE encoder (kl-f16) to obtain their latent representations. Each image is encoded into a latent map of dimensions ${\mathbb{R}}^{w \times h \times c}$, where $w$ and $h$ represent the width and height, and $c$ is the latent dimension. The map is then flattened and processed by a fully-connected (FC) layer, projecting each element into a $d$-dimensional latent vector. Thus, each image is represented as a sequence of $N$ visual tokens, each with $d$-dimensional features.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A Encode History", "weight": 1.0} -->

For history actions, we use a higher sampling frequency compared to observations, as observations typically exhibit redundancy and minimal changes over short time intervals. Each image observation (e.g., $\mathbf{O}_{{t - h} + 1}$) corresponds to $L$ actions within an action chunk (e.g., $\mathbf{A}_{t - h}$). We repeat the action chunk $M$ times to match the number of visual tokens as shown in Figure 2. The repeated sequence is then passed through an FC layer, and converted into a sequence of $N$ action tokens, each with a $d$-dimensional latent representation. These history visual and action tokens serve as conditions for predicting future observations and actions.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B Masked Autoencoder for Observation Prediction", "weight": 1.0} -->

Our work is closely related to. Their method focuses on image generation conditioned on class labels. It begins by generating a subset of visual tokens for the image and then sequentially predicts additional tokens based on the previously generated ones, following an autoregressive process to complete the image. This step-by-step autoregressive approach has been shown to outperform the single-step generation of all visual tokens simultaneously. To facilitate step-by-step prediction, they employ a masked autoencoder framework. During training, some visual tokens are randomly masked, and the model is trained to reconstruct these masked tokens.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B Masked Autoencoder for Observation Prediction", "weight": 1.0} -->

We follow this setting for video prediction. Future observation frames $\{\mathbf{O}_{t + 1},\ldots,\mathbf{O}_{t + h}\}$ are processed similarly to historical observations: they are passed through a VAE encoder to extract latent representations, followed by an FC layer, resulting in a sequence of $N$ tokens per frame, each with a $d$-dimensional latent vector. Some tokens are randomly masked out during training. These visual tokens are concatenated channel-wise with historical visual tokens and action tokens, as shown in Figure 2, to form a new sequence of latent features. Latents from $h$ different time steps are then temporally concatenated with latent representations from other time steps to produce a $N \times h$ latent sequence.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B Masked Autoencoder for Observation Prediction", "weight": 1.0} -->

The resulting sequence is passed through a Transformer to fuse the video and action information, resulting in a set of joint video-action latent representations, $\{\mathbf{Z}_{t + 1},\ldots,\mathbf{Z}_{t + h}\}$, where each latent (e.g., $\mathbf{Z}_{t + 1}$) contain $N$ latent tokens. These joint video-action latent tokens are then used to reconstruct the future observations and corresponding action chunks.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B Masked Autoencoder for Observation Prediction", "weight": 1.0} -->

For tasks that involve language instructions, such as, we incorporate language information using cross-attention in the Transformer. The language input is encoded into a $d$-dimensional token using the CLIP text encoder. To emphasize the language, this token is repeated $M$ times and appended to the $N \times h$ video-action tokens, resulting in a total of ${N \times h} + M$ tokens. These tokens are then passed through the Transformer to fuse the multimodal information. We take the first $N \times h$ outputs of the Transformer as the joint video-action latent representations, $\{\mathbf{Z}_{t + 1},\ldots,\mathbf{Z}_{t + h}\}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B Masked Autoencoder for Observation Prediction", "weight": 1.0} -->

To minimize information leakage across different frames, we consistently mask the same positions across all video frames. At inference time, the model generates complete videos by predicting all tokens starting from an empty sequence. At each autoregressive generation step, visual tokens at the same position across all video frames are generated simultaneously as shown in Supplementary §X-A. Unlike image generation conditioned on class labels or text, historical observations provide rich contextual information about the environment. We found that a single-step generation is sufficient to generate high-quality observations, while using additional steps can further enhance the quality.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-C Decoupled Video and Action Diffusions", "weight": 1.0} -->

Previous video generation-based policy learning methods rely on hierarchically generating videos first and then predicting actions, leading to slow speed and accumulated errors. To address this, we propose decoupling video and action prediction while training them jointly. During training, video generation helps the latent representations $\mathbf{Z}$ capture more detailed scene information, which benefits action prediction. During policy inference, where speed is crucial, the decoupled design allows us to skip video generation and decode only the actions. Similarly, for video generation, where quality is the priority, we can perform multi-step autoregressive video generation while bypassing action decoding.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-C Decoupled Video and Action Diffusions", "weight": 1.0} -->

We introduce two lightweight diffusion decoders for action and video prediction (see Figure 2). Instead of performing the denoising over the entire model, our approach restricts the denoising process to the lightweight decoders, delivering more efficient performance. This design preserves the generative strengths of diffusion models while significantly reducing inference time.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-C Decoupled Video and Action Diffusions", "weight": 1.0} -->

The joint latent $\mathbf{Z}$ serves as the conditioning input for the diffusion decoders. The video diffusion decoder processes each latent token $z_{i} \in \mathbf{Z}_{t + 1} = {\{ z_{1},\ldots,z_{N}\}}$ to predict individual patches in the video frame, which are then reshaped and sent to the VAE decoder to reconstruct the full frame $\mathbf{O}_{t + 1}$. For the action diffusion decoder, all latent tokens in $\mathbf{Z}_{t + 1}$ are aggregated using a convolutional layer, followed by an MLP layer, to produce an action latent. This latent encodes both visual and action-related information for the current step and serves as the condition for the action diffusion model to generate the action chunk $\mathbf{A}_{t}$. We use the diffusion head (base size) for both action and video prediction.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-C Decoupled Video and Action Diffusions", "weight": 1.0} -->

During training, the decoders learn to predict the noise added to noisy action chunks or video patches.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-C Decoupled Video and Action Diffusions", "weight": 1.0} -->

where $\mathbf{A}^{(k)}$ represents the noisy actions, $\epsilon$ is the added noise, $k$ is the diffusion timestep, $\mathbf{Z}$ is the joint video-action latent tokens, and $\epsilon_{\theta}{(\left. \mathbf{A}^{(k)} \middle| {k,\mathbf{Z}} \right.)}$ is the predicted noise.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-C Decoupled Video and Action Diffusions", "weight": 1.0} -->

where $\mathbf{O}^{i,{(k)}}$ represents the $i$-th noisy visual token in the video frame $\mathbf{O}^{(k)}$ at diffusion timestep $k$, $N$ is the total number of visual tokens in a video frame, $\epsilon_{i}$ is the added noise to the $i$-th visual token, $z_{i}$ is the latent token in $\mathbf{Z}$, and $\epsilon_{\phi}{(\left. \mathbf{O}^{i,{(k)}} \middle| {k,z_{i}} \right.)}$ is the predicted noise for the $i$-th token.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-C Decoupled Video and Action Diffusions", "weight": 1.0} -->

The total loss at each time step is the combination of the action and video diffusion losses: $\mathcal{L} = {\mathcal{L}_{\text{action}} + \mathcal{L}_{\text{video}}}$. The overall loss is calculated as the sum of these losses over the time horizon $h$. During policy inference or video generation, the decoders iteratively refine pure noise into actions or videos using the learned denoising process.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-D Masked Training with Flexible Objectives", "weight": 1.0} -->

Instead of training the model solely on the task of predicting future observations and actions based on historical data, we propose a masked training approach with multiple training objectives using a unified framework. As illustrated in Unified Video Action Model, the model is trained on five distinct tasks by varying input and output combinations. Unused components are masked and replaced with a learned mask token. The action loss and video loss are selectively applied to supervise the model depending on the specific task.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-D Masked Training with Flexible Objectives", "weight": 1.0} -->

This training approach enables us to fully utilize the data in various combinations and supports the use of incomplete data, such as video data without corresponding actions. This masked training strategy enables the model to perform a diverse range of functions, including acting as a robot policy, video model, forward and inverse dynamics model, and a combined policy and planner. For instance, when given only image observations, the model can function as an inverse dynamics model to generate action labels from videos. Additionally, this strategy helps prevent overfitting to specific tasks, enhancing the model's overall versatility and robustness.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Evaluation", "weight": 1.0} -->

In the following sections, we evaluate UVA's capacities as policy §V, a video generator §VI, a forward dynamics model §VII, and finally an inverse dynamics model §VIII. In each scenario, we compare UVA with methods that are specifically tailored for the corresponding application.

<!-- chunk {"id": "body-0036", "role": "body", "section": "UVA as Policy", "weight": 1.0} -->

We first investigate the effectiveness of UVA on policy learning. As noted by Kim et al., different policy designs excel in different settings. Their experiments show that while Diffusion Policy performs better in single-task setups, it falls behind OpenVLA in multi-task scenarios. To comprehensively evaluate the performance of UVA as a policy, we conduct extensive evaluations in single-task and multi-task settings, and in simulated (Table II) and real environments (Figure 3). For simulation tasks, we used the same random seeds for different methods for a fair comparison. For real-world tasks, to minimize evaluation bias, all evaluations use public benchmarks with released datasets---no additional training data were collected.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-A Simulation Benchmarks", "weight": 1.0} -->

Single-Task Evaluation: We first evaluate single-task scenarios, where different policies are trained for different tasks. We compare UVA with the baselines on the PushT and Toolhang tasks. We report the success rates of the best-performing checkpoint, averaging across 50 rollouts for PushT and Toolhang, respectively.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-A Simulation Benchmarks", "weight": 1.0} -->

Multi-Task Evaluation: We train one policy for multiple task goals defined by image or text. We introduce a new task, PushT-M, which extends the PushT task to include varying target "T" positions. We evaluate the best-performing checkpoint over 50 rollouts and report its average reward. has 10 tasks. We evaluate each task in 50 different environments with varying random seeds and report the average rewards across all 10 tasks. See Supplementary §X-B for details.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-B Real-world Benchmarks", "weight": 1.0} -->

Training Data: We use two publicly available datasets introduced and without collecting any additional training data. Both benchmarks collect data using the handheld UMI device. We used three tasks, including Cup Arrangement, Towel Folding, and Mouse Arrangement, for training, and tested them on the ARX X5 arm.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-B Real-world Benchmarks", "weight": 1.0} -->

Single-Task Evaluation: We train a single-task policy on the Cup task and directly compare it with the Diffusion Policy model provided by the author, both trained on the same data. We evaluate each method over 20 rollouts with varying initial configurations and report the average success rate.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-B Real-world Benchmarks", "weight": 1.0} -->

Multi-Task Evaluation: We train one model with all three tasks and then evaluate their performance on each task independently. We randomly selected 500 episodes from each dataset and combined them into a dataset to train both our model and Diffusion Policy. Since the training data were collected independently in prior works, all evaluation cases are Out-of-Distribution (OOD), involving unseen environments, objects, and robots. To ensure a wide testing distribution, we include cases with varying initial configurations, object distractors, background textures, and an unseen gripper color (green), as shown in Figure 3. Each policy is evaluated over 60 rollouts, with 20 rollouts per task. See Supplementary §X-C for details.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-C Baselines", "weight": 1.0} -->

We compared with the following alternative methods, all methods are trained or fine-tuned on the same data as our model and tested using the same random seed and initial states.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-C Baselines", "weight": 1.0} -->

Diffusion Policy is a state-of-the-art visuomotor policy model. We use both CNN-based network \[DP-C\] and Transformer-based design \[DP-T\] from their original implementation for all simulation tasks. For real-world tasks, we used an improved Diffusion Policy, which is optimized for UMI data. It leverages a CLIP-pretrained ViT-B/16 vision encoder, significantly improving visual understanding. We refer to it as \[DP-UMI\].

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-C Baselines", "weight": 1.0} -->

OpenVLA is a state-of-the art vision-language-action (VLA) built on 7B Llama 2 for multi-task setting. It is trained on a diverse dataset encompassing a wide range of robots, tasks, and environments. We finetune OpenVLA on each task to optimize its performance.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-C Baselines", "weight": 1.0} -->

${\mathbf{π}}_{\mathbf{0}}$ is an open-source VLA model designed for general-purpose robot control. It employs a flow matching based architecture to generate continuous action sequences. Trained on a diverse dataset spanning multiple robot embodiments and tasks, $\pi_{0}$ demonstrates strong zero-shot and fine-tuned performance. We use the officially released checkpoints: $\pi_{0}$ and $\pi_{0}$-FAST, both finetuned on Libero tasks.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-C Baselines", "weight": 1.0} -->

UniPi is a video-based policy model that generates videos first and then predicts actions based on the generated videos. Since the official implementation is not available, we used the code. This implementation relies on pixel-wise video generation, which results in slower video generation speed. For action inference, we train a model that processes two consecutive generated video frames using a pretrained ResNet-50 for the PushT and PushT-M tasks, and a ResNet-152 for the Tool Hang and Cup Arrangement.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-C Baselines", "weight": 1.0} -->

UVA-action is an ablation of UVA, where the video generation part is excluded, and the model is trained solely as a policy model. This baseline aims to evaluate the effectiveness of joint video and action training.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-D Policy Learning Results", "weight": 1.0} -->

We evaluate policy learning results with UVA compared to the baseline methods on a few different axes: 1) action prediction accuracy, 2) inference speed, 3) robustness to visual disturbances, 4) robustness to history length, and 5) the effect of joint video-action modeling.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-D Policy Learning Results", "weight": 1.0} -->

Action Prediction Accuracy (Simulation Tasks): In Table II, we compare UVA with baseline methods in both single-task and multi-task settings. We use the same random seed for our method and baselines to ensure a fair comparison.

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-D Policy Learning Results", "weight": 1.0} -->

Simulation Single-Task: Our method is able to match the performance of the state-of-the-art model DP-C and significantly outperform other video-based methods such as UniPi and vision-language-action model OpenVLA.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-D Policy Learning Results", "weight": 1.0} -->

Simulation Multi-Task: Our method is particularly strong in the multi-task setting. Specifically, UVA surpasses the best baseline by 20% on the PushT-M task and by 5% on the benchmark. This result demonstrates that UVA model is able to better learn and leverage the general dynamics that are shared across tasks and, therefore, improve overall performance in the multi-task setting.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-D Policy Learning Results", "weight": 1.0} -->

Notably, $\pi_{0}$ (3.3B) and $\pi_{0}$-FAST (3.0B) are large models fine-tuned from pretrained checkpoints using the entire Libero dataset, while UVA is smaller (0.5B) and trained only. Moreover, $\pi_{0}$ and $\pi_{0}$-FAST use third-person and wrist-view images plus robot proprioception, while UVA relies only on third-person images. Despite its smaller size, limited input, and no external data, UVA outperforms $\pi_{0}$ and $\pi_{0}$-FAST.

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-D Policy Learning Results", "weight": 1.0} -->

Action Prediction Accuracy (Real-World Tasks): Table III shows the results of real-world tasks. We ensure a fair comparison by keeping the initial placement of objects and grippers identical across different methods for each test rollout.

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-D Policy Learning Results", "weight": 1.0} -->

Real-World Single-Task: First, we evaluate the policy performance in a single-task setting. This evaluation aims to compare our method with a strong baseline in prior works by replicating a similar evaluation setup. Overall, UVA performs comparable with DP-UMI, which is optimized with this particular training dataset. We noticed that the dataset contains extensive recovery data from the moments of failure to correct the policy. This data is particularly useful for models without history dependence, like DP-UMI, which can recover from the new observations included in the recovery data. In contrast, our model uses a longer history, which is advantageous for tasks requiring longer memory. However, in this case, the collected failure recovery data is less impactful for our model, as its longer memory window prioritizes learning from extended temporal patterns. While we could shorten our model's history window, we maintain a consistent design across all tasks rather than tailoring it to this specific task and training data.

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-D Policy Learning Results", "weight": 1.0} -->

Real-World Multi-Task: We train a single model using our method and evaluate it on three tasks individually. DP-UMI is trained and tested in the same manner for a fair comparison. For each task, we test the methods on 20 different cases, as shown in Figure 3. Our approach demonstrates superior performance in the multi-task setting, achieving a 15% higher success rate on the Cup task and a 40% higher success rate on the Mouse task compared to DP-UMI.

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-D Policy Learning Results", "weight": 1.0} -->

In general, our method can successfully complete the task with distractor objects or changing backgrounds but fails when the background color is the same as the objects. Its visual understanding could be enhanced by training on additional video data without action labels. DP-UMI performs well on the towel task but shows less stability when handling pick-and-place cups and grabbing the mouse. However, it performs well across different backgrounds due to its use of a pre-trained vision encoder. When the gripper color is changed to an unseen green, the performance of both methods slightly decreases compared to the orange gripper used for training. However, both UVA and DP-UMI show good generalization to the unseen gripper. Please refer to our website for details.

<!-- chunk {"id": "body-0057", "role": "body", "section": "V-D Policy Learning Results", "weight": 1.0} -->

Inference Speed: Speed is evaluated based on a single action trajectory inference. All methods, except OpenVLA, infer 16 action steps per trajectory with 8 executed steps. OpenVLA infers one action at a time, requiring 8 runs to match the inference time for 8 executed actions. UniPi generates raw pixel videos, resulting in significantly slower inference.

<!-- chunk {"id": "body-0058", "role": "body", "section": "V-D Policy Learning Results", "weight": 1.0} -->

Our method achieves faster inference speeds by performing diffusion iterations only on the lightweight action head, rather than the entire network as DP-C and DP-T. Thanks to the decoupled design, video generation can be skipped during policy inference, further improving efficiency. For simulation tasks, we use 100 denoise steps for action prediction. For DP-C and DP-T, we follow their original implementations and also perform denoising over 100 steps. With the same number of diffusion steps (Table II), our method achieves faster inference compared to DP-C and DP-T. Both $\pi_{0}$ and $\pi_{0}$-FAST achieve faster inference speed than other methods.

<!-- chunk {"id": "body-0059", "role": "body", "section": "V-D Policy Learning Results", "weight": 1.0} -->

For real-world tasks (Table III), both UVA and DP-UMI use 16 denoising steps for real-time manipulation. We found that the UVA Attention module in the Transformer accounts for half of the inference time, making UVA slightly slower than DP-UMI. With future improvements, such as replacing the Attention with Flash Attention, our model could achieve faster speeds. We note that, although DP-UMI uses a pretrained ViT encoder, its model size (171.27M parameters) is smaller than DP-C (262.69M parameters). This explains why DP-C is slower than UVA in Table II and DP-UMI is faster in Table III. Overall, UVA achieves a good balance between speed and performance across diverse settings.

<!-- chunk {"id": "body-0060", "role": "body", "section": "V-D Policy Learning Results", "weight": 1.0} -->

Robustness to Visual Disturbances: We have shown that UVA is robust to visual disturbances in the real-world multi-task setting in Figure 3. All tests are unseen during training, and even with more challenging distractor objects and backgrounds, UVA achieves higher success rates than DP-UMI.

<!-- chunk {"id": "body-0061", "role": "body", "section": "V-D Policy Learning Results", "weight": 1.0} -->

To more rigorously evaluate this visual generalization capability, we perform a systematic evaluation in simulation by procedurally altering visual conditions in the PushT environment. The modifications include changes to the background color, the addition of object distractor, and variations in goal color, as shown in Figure 5. The evaluation was conducted on scenarios outside the training distribution, as the model was trained only in the standard environment in Table II. The results show that video generation methods, such as UniPi and UVA, exhibit superior performance in handling visual disturbances. For example, with changes in goal color, UniPi achieves a success rate of 40%, UVA achieves 64%, while OpenVLA only reaches 32%.

<!-- chunk {"id": "body-0062", "role": "body", "section": "V-D Policy Learning Results", "weight": 1.0} -->

Robustness to History Length: Prior policy learning methods, such as DP-C, often experience performance degradation as the history length increases as shown in Figure 6 evaluated on the PushT-M task. In contrast, UVA can effectively adapt to longer history inputs. By jointly predicting video and action, our model sustains robust performance even as the history length grows. This highlights the better potential of UVA for tasks that require reasoning over extended temporal contexts.

<!-- chunk {"id": "body-0063", "role": "body", "section": "V-D Policy Learning Results", "weight": 1.0} -->

Effect of Joint Video-Action Modeling: We evaluate this by comparing UVA with a baseline (UVA-action) that removes the video generation part. As shown in Table II, this modification led to reduced performance compared to the complete framework, highlighting the critical role of video generation in improving policy learning.

<!-- chunk {"id": "body-0064", "role": "body", "section": "UVA as a Video Generator", "weight": 1.0} -->

UVA can function as a video generation model by bypassing the action diffusion head during inference. We compare UVA with UniPi on video generation results across two datasets: and Cup Arrangement, in Table IV. Performance is evaluated by computing the Fréchet Video Distance (FVD) for 500 videos generated by each method. FVD is a metric for assessing video quality by evaluating visual fidelity and temporal coherence. It compares statistical properties of feature representations from real and generated videos, using a pre-trained Inflated 3D ConvNet. Lower FVD scores indicate greater similarity.

<!-- chunk {"id": "body-0065", "role": "body", "section": "UVA as a Video Generator", "weight": 1.0} -->

The masked autoencoder training in our method (§III-B) facilitates video generation in an autoregressive manner, where visual tokens are generated across all video frames in parallel during the first stage. In the subsequent stage, the next set of tokens is predicted sequentially, conditioned on the previously generated tokens. This iterative token prediction process continues until the entire video is generated. See Supplementary §X-A for details. In Table IV, we show that even with a 1-step process, our method outperforms UniPi on the more challenging Cup Arrangement task, while using 8 steps further improves performance.

<!-- chunk {"id": "body-0066", "role": "body", "section": "UVA as a Forward Dynamics Model", "weight": 1.0} -->

Our model can perform forward dynamics predictions $\mathbf{O}_{t + 1} = {f_{\text{forward}}{(\mathbf{O}_{t},\mathbf{A}_{t})}}$. To evaluate its effectiveness, we use it to guide the behavior of a pretrained policy model, such as the DP-C. We evaluate this approach in a block-pushing environment, where the model is trained to push one block to a specified square and another block to a second square, each randomly assigned. During testing, we aim to control the policy to complete specific tasks, such as pushing the red block to the red square (R-R) or the red block to the green square (R-G). The evaluation considers four distinct settings, as illustrated in Figure 9. Each setting is tested 10 times with varying initial positions of the objects and the robot. Notably, a perfect policy model in this setup would achieve a maximum average success rate of 50%, since training only requires one block to be pushed to any square, while testing specifies exact target assignments for each block.

<!-- chunk {"id": "body-0067", "role": "body", "section": "UVA as a Forward Dynamics Model", "weight": 1.0} -->

At each step, we sample 100 trajectories of 16 future actions using DP-C. The sampled actions, along with historical observations, are input into our model, which predicts future observations by functioning as a forward dynamics model. For each trajectory, we calculate a reward based on the predicted observations, selecting the trajectory with the highest reward. The reward is computed as the distance between the blocks and their target squares, which are identified from the predicted frames. We then execute the first 6 steps of the selected trajectory and resample new trajectories until the task is completed or the episode ends. DP-C can complete the tasks with a success rate of 38% in Table. By leveraging our model to guide the policy, the success rate increases to 60%.

<!-- chunk {"id": "body-0068", "role": "body", "section": "UVA as a Forward Dynamics Model", "weight": 1.0} -->

For comparison, we evaluate the performance of using a ground-truth simulator to render the sampled trajectories and select the best ones. Even with the ground-truth simulator, the success rate is limited to 75% due to suboptimal sampled trajectories and errors in object detection. While our model performs worse than the simulator, it still significantly enhances performance and guides the pretrained policy models to complete required tasks.

<!-- chunk {"id": "body-0069", "role": "body", "section": "UVA as a Inverse Dynamic Model", "weight": 1.0} -->

In this section, we evaluate the effectiveness of the proposed method in an inverse dynamics setting, where actions are inferred as $\mathbf{A}_{t} = {f_{\text{inverse}}{(\mathbf{O}_{t},\mathbf{O}_{t + 1})}}$ using UMI data. For the UMI Cup Arrangement data, the robot's actions are naturally aligned with camera movements, enabling straightforward evaluation of action prediction accuracy using the ground truth camera poses obtained from motion capture (Mocap). Notably, our model had never encountered this test data during training.

<!-- chunk {"id": "body-0070", "role": "body", "section": "UVA as a Inverse Dynamic Model", "weight": 1.0} -->

Baselines: As a comparison, we evaluate the actions (i.e., camera pose) generated by the inverse dynamics model used in UniPi and a well-engineered SLAM system used in UMI, where the SLAM system requires an additional mapping. The UMI actions in the training data are derived from SLAM.

<!-- chunk {"id": "body-0071", "role": "body", "section": "UVA as a Inverse Dynamic Model", "weight": 1.0} -->

For the actions predicted by each method, we compute the L2 distance to the ground truth actions from Mocap, as shown in Table V. The UniPi inverse dynamics model predicts actions from two consecutive images, which may lead to discontinuities in the predicted actions over time. In contrast, our method predicts 16 actions simultaneously, resulting in more consistent and temporally coherent predictions. The action errors produced by SLAM were 0.41 cm for position and 0.30 degrees for rotation. While UVA exhibited slightly higher errors than SLAM, it still demonstrated strong performance with position errors under 1 cm and rotation errors around 1 degree. These results highlight the generalization capability of UVA for action prediction, even on unseen data, and suggest that it could serve as a viable alternative to SLAM, which is difficult to calibrate and suffers from a high failure rate.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Discussion", "weight": 1.5} -->

We propose a unified video-action model that jointly models and separately decodes video and actions. This design enables us to fully leverage video data as additional supervision, resulting in stronger performance and fast action prediction by skipping video decoding during inference. The framework inherently supports masking training, allowing it to fulfill various robotics functions, including acting as a policy, video model, forward and inverse dynamics model, and a combined policy and planner. By fully utilizing video and action data in diverse configurations, our model reduces overfitting to specific tasks, outperforms previous methods, and demonstrates versatility for multi-purpose applications.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Discussion", "weight": 1.5} -->

One limitation of our framework is that it does not currently leverage large amounts of actionless video data, which could provide valuable additional supervision. As a result, our method occasionally achieves only comparable performance to the DP-UMI on real-world tasks. We believe that pretraining the model on web-scale video datasets could significantly enhance its generalization capabilities, and we leave this exploration for future work. Furthermore, our model can be naturally extended to predict modalities beyond video and action, such as sound and force, by incorporating additional diffusion heads, offering a more comprehensive and versatile framework. This remains a promising direction for future research.
