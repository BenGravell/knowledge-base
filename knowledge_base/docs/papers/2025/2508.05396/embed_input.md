<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Real-Time Iteration Scheme for Diffusion Policy

Topics include Diffusion policy, Real-time iteration, Robotics, Robot manipulation, Diffusion inference, Latency reduction, Discrete actions, Contractivity, Imitation learning, Real-time control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

This preprint transfers the RTI idea from online optimal control to diffusion-policy inference, reusing previous denoising solutions so robots can update actions with less latency. It is conceptually useful in the RTI-MPC cluster because it generalizes the same "one cheap update per cycle" principle to learned policies, including a scaling method for discrete manipulation actions and contractivity conditions for choosing the starting denoising step.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Diffusion Policies have demonstrated impressive performance in robotic manipulation tasks. However, their long inference time, resulting from an extensive iterative denoising process, and the need to execute an action chunk before the next prediction to maintain consistent actions limit their applicability to latency-critical tasks or simple tasks with a short cycle time. While recent methods explored distillation or alternative policy structures to accelerate inference, these often demand additional training, which can be resource-intensive for large robotic models. In this paper, we introduce a novel approach inspired by the Real-Time Iteration (RTI) Scheme, a method from optimal control that accelerates optimization by leveraging solutions from previous time steps as initial guesses for subsequent iterations. We explore the application of this scheme in diffusion inference and propose a scaling-based method to effectively handle discrete actions, such as grasping, in robotic manipulation. The proposed scheme significantly reduces runtime computational costs without the need for distillation or policy redesign. This enables a seamless integration into many pre-trained diffusion-based models, in particular, to resource-demanding large models. We also provide theoretical conditions for the contractivity which could be useful for estimating the initial denoising step.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Quantitative results from extensive simulation experiments show a substantial reduction in inference time, with comparable overall performance compared with Diffusion Policy using full-step denoising. Our project page with additional resources is available : this https URL.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Robotic manipulation has seen significant advancements enabled by diffusion models. These models, especially Diffusion Policy (DP), have demonstrated success in a wide range of tasks, improving control, adaptability, and generalization in complex manipulation scenarios.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

However, one main drawback of diffusion models is the slow inference process. Standard diffusion models begin inference from a standard Gaussian distribution and refine it through a denoising process with hundreds of steps. This impedes high-frequency control in demanding tasks, such as contact-rich or high-speed manipulations, which require continuous and timely correction, to prevent irrecoverable errors or even outright failures.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The inability to react quickly limits the application of diffusion-based policies in real-world robotics and bottleneck task throughput in repetitive execution. The prolonged waiting time for policies to generate actions results in sluggish, non-smooth robot movements, reducing productivity and making them significantly less responsive compared to human performance. Consequently, addressing the inference efficiency in diffusion-based policies is critical to broadening their applicability in robotic practice.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Recent works have explored various approaches to accelerating inference in diffusion models. One prominent direction involves distillation techniques, which aim to condense the iterative denoising process into a one-step consistency model. While this method achieves faster inference, they often come with drawbacks such as high computational costs during training and reduced policy quality and diversity. Another line of research focuses on designing alternative policy structures, where the policy structure itself is redesigned to facilitate faster decision-making while maintaining performance. Although these methods can be effective, they are often impractical to apply to pre-trained large-scale robotic models, as they require complete retraining. Given that retraining large models is computationally expensive and resource-intensive, there is a pressing need for solutions that enable efficient policy acceleration without requiring extensive model modifications or retraining.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In this paper, we propose a real-time method, Real-Time Iteration for Diffusion Policy (RTI-DP) that requires neither retraining nor distillation. Our approach is inspired by the Real-Time Iteration Scheme in optimal control, which leverages predictions from previous steps as initialization for the next step, significantly accelerating optimization. Specifically, our method first computes an initial action chunk using the same approach as the standard diffusion policy. For subsequent action chunks, it utilizes the previous one as an initial guess and applies denoising on top of it with a reduced number of time steps. A key insight of our approach is the importance of initialization, which stems from the spatiotemporal consistency of physical systems. This consistency implies that actions exhibit continuity and bounded changes over time, ensuring that initialization remains effective across consecutive action steps. As a result, RTI serves as a natural extension for diffusion policy inference. Theoretical results can be derived from the consistency assumption, stating with a well-chosen initial guess can efficiently converge to a high-quality prediction demanding hundreds of denoising steps. This analysis aids in identifying the optimal initial denoising step to maintain high inference quality.

<!-- chunk {"id": "body-0010", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Our contribution can be summarized as follows: We propose a real-time inference method that leverages the initial guess from the previous prediction, enabling direct application to pre-trained models.

<!-- chunk {"id": "body-0011", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We provide theoretical conditions for contractive errors by infererring from the proposed initial guess.

<!-- chunk {"id": "body-0012", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We show the proposed method can empirically boost the real-time performance in various manipulation tasks through simulation experiments.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-A Preliminaries", "weight": 1.0} -->

The Denoising Diffusion Probabilistic Model employs a forward noising process that gradually adds Gaussian noise, generating a sequence of states that, in the diffusion-policy setting, represent the action $\mathbf{A}$: where $\bar{\alpha}_{k}=\Pi^{t}_{s=1}\alpha_{s}$ is the noise schedule and $\epsilon\sim\mathcal{N}(0,\mathbf{I})$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A Preliminaries", "weight": 1.0} -->

Conventionally, the reverse process starts from pure Gaussian noise, but this approach requires many denoising steps to recover the underlying data, leading to high computational costs and increased inference latency.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A Preliminaries", "weight": 1.0} -->

By contrast, in the control domain, RTI is an efficient strategy for Nonlinear Model Predictive Control (NMPC) in time-critical applications. Traditional NMPC requires solving a nonlinear optimization problem at each sampling instant, which can be computationally prohibitive for large systems with fast dynamics, similar to diffusion models. The RTI scheme addresses this challenge through a single-iteration optimization strategy that leverages the similarity between consecutive control problems to achieve real-time performance.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A Preliminaries", "weight": 1.0} -->

| $\displaystyle\quad\mathbf{z_{i+1}}=f(\mathbf{z_{i}},\mathbf{u_{i}}),\quad i=k,\dots,N-1$ | | | | | | $\displaystyle\quad\mathbf{z_{k}}=\mathbf{x}(t_{k})$ | | | where $\mathbf{\{z_{i}\}}$ is the state trajectory and $\mathbf{\{u_{i}\}}$ is the control sequence. One of the keys to RTI's computational efficiency lies in its initialization procedure. Rather than starting from arbitrary initial guesses, RTI employs: Preparation: RTI first computes an initial guess across the entire horizon and prepares the offline Jacobian matrix and the gradient vector.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A Preliminaries", "weight": 1.0} -->

Feedback response: At each time step, RTI computes the incremental step changes and applies the resulting control to the real system.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A Preliminaries", "weight": 1.0} -->

Transition: RTI updates the next initial guess by incorporating the step changes and shrinking the prediction horizon by one.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A Preliminaries", "weight": 1.0} -->

By leveraging this scheme, computation time can be reduced by a factor of hundreds to thousands.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A Preliminaries", "weight": 1.0} -->

Diffusion Policy and NMPC share fundamental similarities when interacting with physical controllable systems. Control methods operating in the real world must inherently respect the spatio-temporal consistency, as robots cannot change states discontinuously across space or time.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A Preliminaries", "weight": 1.0} -->

Spatiotemporal Consistency in robot visuomotor policies is the property that a robot's trajectory evolves smoothly over time and in space. It ensures that state transitions are bounded in magnitude, such that the difference between the state at one time step and the next will not be arbitrarily large.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A Preliminaries", "weight": 1.0} -->

Formally, let $x_{t}^{\phi}\in\Phi$ denote the trajectory's configuration expressed in a smooth manifold $\Phi$. The consistency constraint is expressed as: where $d(\cdot,\cdot)$ is a distance metric defined on the manifold $\Phi$, and $L$ is a Lipschitz-like constant that bounds the maximum allowable change in the robot's state between timesteps. This stipulates that the trajectory evolves continuously and smoothly over time in space, without abrupt changes between consecutive timesteps.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A Preliminaries", "weight": 1.0} -->

By harnessing the *spatiotemporal* consistency properties, both Diffusion Policy and NMPC can leverage action guesses that effectively build on previous predictions. However, key differences remain: diffusion models evolve according to stochastic differential equations (SDEs), whereas NLP-based NMPC solves ordinary differential equations (ODEs). As a result, it requires distinct approaches for handling NMPC and Diffusion Policy.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A Preliminaries", "weight": 1.0} -->

In the following section, we introduce Real-Time Scheme for Diffusion Policy, providing an analysis about its effectiveness on retaining performance with fewer denoising steps.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B Method", "weight": 1.0} -->

Our method begins by computing the first action prediction using standard Diffusion Policy with full denoising. As this initial step is performed offline, computation time is not a primary concern. For subsequent predictions, we treat the outcome of the previous prediction as an initial guess and apply a reduced number of denoising steps to refine it. This process is repeated iteratively, with each new prediction building upon the last, enabling the policy to operate efficiently in real time---one step at a time---while maintaining fast inference.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-B Method", "weight": 1.0} -->

0: Mθ: denoising model, Ot: observation at time t, At = [, at + 1, …, at + T − 1]: action chunk at time t with an action horizon of T, G ∼ 𝒩(0, I): initial guess sampled from a standard Gaussian distribution, K: denoising steps while NOT FINISHED do {Compute the initial action chunk with full-step denoising} {Iterative refinement using previous predictions} G ← [at + 1, at + 2, …, at + T − 1, at + T − 1] {Shift and repeat last action} Algorithm 1 Real-time Iteration for Diffusion Policy

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B1 Discrete action space", "weight": 1.0} -->

Our method is based on the fundamental assumption of spatiotemporal consistency in action states, meaning that consecutive timesteps exhibit bounded changes in actions. However, this assumption may be violated, particularly in scenarios involving discrete actions, such as a binary command of grasping. In such cases, abrupt transitions can pose challenges for diffusion-based approaches, potentially leading to corrupted predictions.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B1 Discrete action space", "weight": 1.0} -->

To address this issue, we introduce a scaling factor to transform the discrete dimensions of data, allowing the change of discrete actions to be better captured within a continuous representation. This transformation enables the diffusion model to smoothly interpret and denoise actions, preserving trajectory consistency while retaining the expressiveness of the original discrete signals.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-B1 Discrete action space", "weight": 1.0} -->

We explore two strategies: For pre-trained policies, we directly scale the discrete initial guess by a factor that remains manageable within the denoising steps. For example, for an initial guess of a discrete action $g_{d}$, $g_{d}=\frac{g_{d}}{10}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B1 Discrete action space", "weight": 1.0} -->

For retrainable tasks, a more effective approach is to preprocess the discrete actions in the dataset using a scaling factor, ensuring robust performance in handling discrete actions. For example, the discrete action $a_{d}$ in the dataset is changed to $\frac{a_{d}}{10}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-C Why is initialization important?", "weight": 1.0} -->

Diffusion models reveal the data distribution by employing a reverse diffusion process that starts from a predefined prior distribution, referred to here as the initialization. Typically, the prior is chosen as a unimodal Gaussian distribution due to its mathematical simplicity and analytical tractability. Since a Gaussian prior does not encode information about specific data modes, it provides a mode-agnostic initialization. Then the learned reverse diffusion process can effectively guide noisy samples toward diverse modes within the data distribution, facilitating flexible adaptation of the robot to various potential actions during inference. While this multimodality is beneficial for generating diverse behaviors, it is not always favorable during real-time execution, where consistency and stability are critical. As the policy execution progresses, the mode naturally collapses, as a system cannot follow multiple modes simultaneously. With a limited conditional context, the policy may oscillate between different modes, potentially becoming trapped in conflicting movement decisions instead of progressing toward the goal. This phenomenon is also observed in DP experiments, where performance deteriorates as the action horizon decreases from its optimal value. Therefore, during the robot execution, starting inference from a point near the same mode can alleviate this issue, reduce the chance of mode switch and keep consistency.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-C Why is initialization important?", "weight": 1.0} -->

Another challenge arising from an uninformative initialization is the difficulty in achieving a fully closed-loop system while maintaining consistency. This challenge is exacerbated by the absence of mode consistency between consecutive predictions. To address this, in DP, an action chunk must be predicted to ensure a sequence of consistent actions. This design choice inherently results in only partially closed-loop behavior. This limitation stems from their open-loop operation between predictions, where a sequence of actions is generated from a single observation and executed without intermediate feedback. This design represents a trade-off necessitated by the long prediction time and the need to preserve mode consistency. Consequently, closing the loop becomes challenging, despite its fundamental importance for real-time control.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-C Why is initialization important?", "weight": 1.0} -->

Our method preserves multimodal capabilities by selecting the mode in the initial step based on the standard diffusion policy while ensuring stable execution through predictions from previous time steps, thereby maintaining consistency with local behavior modes. To achieve a fully closed-loop system, we adopt a one-action-per-prediction strategy, enabling continuous feedback without compromising performance. This approach maintains real-time adaptability while ensuring computational efficiency.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-D Local Contractivity of Real-Time Iterations", "weight": 1.0} -->

Assume we have a forward chain of actions $\{{\mathbf{A}_{k}}\}$ generated from the clean ${\mathbf{A}_{0}}$. Suppose we do not start from $\{{\mathbf{A}}_{K}\}$ in the reverse process, but from an intermediate step $K^{\prime}<K$ with some $\mathbf{{A}}_{K^{\prime}}$. Following the spatiotemporal consistency inherent in physical systems, the actions predicted from the observation $\mathbf{O}_{t}$ tend to closely ensemble those predicted at a previous time step with $\mathbf{O}_{t-1}$ if they belong to the same behavioral mode. Consequently, the estimated $\mathbf{\tilde{A}}_{K^{\prime}}$ remains close to the true $\mathbf{A}_{K^{\prime}}$, enabling the reverse chain to stay near the original trajectory and ultimately converge toward $\mathbf{A}_{0}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-D Local Contractivity of Real-Time Iterations", "weight": 1.0} -->

Since denoising follows a Markov chain structure, each step depends only on the preceding one. For a contractive Markov, small errors are corrected rather than accumulated, ensuring stability.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark On Estimating the Step $K^{\\prime}$", "weight": 1.0} -->

In the current implementation, $K^{\prime}$ is chosen empirically. However, the contractivity property established above offers a theoretical foundation for choosing $K^{\prime}$ to automate the selection, striking a balance between denoising steps and errors. Possibly, one could estimate $K^{\prime}$ offline by running the full denoising steps to obtain $\mathbf{A}_{0}$, and selecting $K^{\prime}$ to minimize the deviation between the initial guess and the forward diffusion mean.

<!-- chunk {"id": "body-0037", "role": "body", "section": "EXPERIMENTAL EVALUATION", "weight": 1.0} -->

We demonstrate the effectiveness of Real-Time Iteration Scheme in achieving high accuracy and fast inference across diverse robotics benchmarks, spanning both image-based and state-based control in tasks of varying complexity and horizons. The specific questions we want to address with the experiments are: To what extent does RTI-DP enhance inference time, and how significant is the speed-up compared to competing methods?

<!-- chunk {"id": "body-0038", "role": "body", "section": "EXPERIMENTAL EVALUATION", "weight": 1.0} -->

How does RTI-DP compare to existing approaches in terms of performance across different robotics tasks? Will a faster but non-full-denoising inference degrade task performance?

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-A Baselines", "weight": 1.0} -->

RTI is evaluated against several state-of-the-art diffusion-based policies designed to enhance inference speed. Specifically, we compare it with image-based Consistency Policy, which utilizes consistency distillation for rapid sampling, and Streaming Diffusion Policy, which improves inference speed by generating a partially denoised action trajectory.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-A Baselines", "weight": 1.0} -->

Additionally, since Real-Time Scheme is built on a diffusion policy, we include the CNN-based Diffusion Policy as a baseline. For tasks involving grasping, we evaluate two RTI-DP setups: RTI-DP-scale and RTI-DP-clip. RTI-DP-scale applies scaling at the dataset level, while RTI-DP-clip is used for a pre-trained policy and tested on the same benchmarks as DP.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-B Simulation Experiment", "weight": 1.0} -->

We assess the performance of RTI-DP across seven tasks spanning three established benchmarks: Robomimic, Push-T, and Block-pushing. These benchmarks are widely used for both visuomotor and state-based policy learning and have been previously tested in studies such as Diffusion Policy and Consistency Policy.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-B1 Robomimic", "weight": 1.0} -->

Robomimic is a comprehensive benchmark for assessing robotic manipulation in imitation learning and offline reinforcement learning. It includes five tasks---can, lift, transport, tool hang, and square---encompassing both short and long horizons, single and dual-robot setups, high-precision actions, and scenarios involving single or multiple objects.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-B2 Push-T", "weight": 1.0} -->

Push-T requires an agent to push a T-shaped block toward a fixed target using a circular end-effector. The task incorporates variability by randomizing the initial positions of both the block and the end-effector. Effective execution demands precise control over contact-rich interactions, utilizing point contacts to guide the block accurately. This task is available in two formats: one based on RGB image observations and another utilizing nine 2D keypoints derived from the ground-truth pose of the T block.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-B3 Multimodal Block Pushing", "weight": 1.0} -->

This task evaluates a policy's ability to model multimodal action distributions by requiring the agent to push two blocks into two designated squares in any order.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-C Implementation", "weight": 1.0} -->

We assess inference time and success rates across three checkpoints, each initialized with different random seeds. All experiments are conducted using an NVIDIA A100-SXM4-40GB GPU, maintaining consistent hardware setup throughout. Policies are trained for a maximum of 48 hours, except for CP, which is trained for double the duration. To minimize data-related variability, all policies are trained using the dataset provided. Additionally, DP and RTI-DP-clip are evaluated using the provided checkpoints.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-D Results", "weight": 1.0} -->

The results, presented in Tables I, II, and III, demonstrate that our methods significantly accelerate inference while maintaining performance comparable to Diffusion Policy with full denoising steps. Compared to other state-of-the-art inference acceleration methods, our approach achieves substantial speedups while preserving a good performance, particularly in precision-critical tasks such as image-based Tool-Hang. Additionally, in tasks with only continuous action spaces, such as Push-T and BlockPush, our approach demonstrates a clear advantage over other acceleration methods, further highlighting its effectiveness and validating our method's grounding in the continuity of physical systems.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-D Results", "weight": 1.0} -->

Notably, in state-based tasks such as Push-T and BlockPush, RTI-DP even surpasses DP with full denoising steps, further demonstrating the advantage of our method and underscoring the importance of fully closed-loop control.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-D Results", "weight": 1.0} -->

Most RTI-DP-scale results achieve effective denoising within just three steps. However, RTI-DP-clip exhibits slightly lower performance than RTI-DP-scale and requires additional time, as scaling directly on initial guesses degraded their quality.

<!-- chunk {"id": "body-0049", "role": "body", "section": "DISCUSSION", "weight": 1.5} -->

RTI-DP offers a clear advantage over existing approaches by achieving substantial speedups without compromising performance, or requiring retraining, making it well-suited for real-time robotic applications. Beyond diffusion models, similar improvements could extend to flow-based models with a denoising component, further reducing computational overhead while maintaining expressive power. Future research could investigate how to integrate optimized initialization techniques with flow-based models, which might achieve even greater speedups than diffusion models, particularly given their inherent smoothness.

<!-- chunk {"id": "body-0050", "role": "body", "section": "DISCUSSION", "weight": 1.5} -->

While fast inference offers many advantages, some dynamical systems with minimal environmental disturbances---such as static tasks like picking up a cup---do not necessarily benefit from speed improvements, as execution time is not a limiting factor. However, the efficiency of our method creates a larger time budget for prediction with less powerful GPUs. This, in turn, could potentially lower the hardware requirements for visuomotor policies and deployment in edge devices without needing additional training.

<!-- chunk {"id": "body-0051", "role": "body", "section": "DISCUSSION", "weight": 1.5} -->

For a system with minimal noise, convergence is typically achieved within three steps. However, in environments with significant or unpredictable noise, additional tuning may be necessary. Dynamically adjusting the step sequence---such as selectively skipping steps---can sometimes reduce inference time while preserving performance. Although we provide a method for selecting the initial denoising step, the choice of the parameters still requires tuning. Also, in systems with large action changes, additional denoising steps may be required. Future work could explore strategies for selecting denoising steps that simplify the tuning process.

<!-- chunk {"id": "body-0052", "role": "body", "section": "DISCUSSION", "weight": 1.5} -->

While most imitation learning methods depend on the quality of the teleoperated data, our method is even more reliant on it. Under the primary assumption of limited action changes over time, our method performs well when the demonstrated motion has low accelerations and relatively constant velocities. However, the method may struggle to reach the target actions within a limited number of inference steps when attempting to replicate sudden changes from the expert data.

<!-- chunk {"id": "body-0053", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

In this paper, we present the Real-Time Iteration Scheme for Diffusion Policy, a simple yet efficient approach to accelerating inference in diffusion-based policies through an informed initialization strategy. Using a reduced number of denoising steps, RTI-DP allows low-latency execution while maintaining good policy performance. Our method can be seamlessly integrated with other pre-trained models, enabling fast inference for large-scale pre-trained robotic models. We provide conditions for the contractivity of denoising dynamics and as potential guidelines for selecting the appropriate number of denoising steps. Simulation experiments demonstrate that RTI delivers both rapid inference and good performance simultaneously, without requiring retraining of existing policies.

<!-- chunk {"id": "body-0054", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

Beyond diffusion models, our approach could also benefit flow-based models with denoising components, offering further opportunities to enhance inference speed. Additionally, while our method requires multiple steps for denoising, there remains a potential for one-step denoising without altering the policy structure.
