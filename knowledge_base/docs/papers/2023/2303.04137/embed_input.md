<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Diffusion Policy: Visuomotor Policy Learning via Action Diffusion

Topics include Diffusion policy, Diffusion models, Action diffusion, Machine learning, Imitation learning, Robot learning, Visuomotor policy, Transformers.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Models robot visuomotor policy as a denoising diffusion process over action sequences, enabling multimodal and high-dimensional action distributions that outperform regression-based imitation learning methods on dexterous manipulation benchmarks.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper introduces Diffusion Policy, a new way of generating robot behavior by representing a robot's visuomotor policy as a conditional denoising diffusion process. We benchmark Diffusion Policy across 15 different tasks from 4 different robot manipulation benchmarks and find that it consistently outperforms existing state-of-the-art robot learning methods with an average improvement of 46.9%. Diffusion Policy learns the gradient of the action-distribution score function and iteratively optimizes with respect to this gradient field during inference via a series of stochastic Langevin dynamics steps. We find that the diffusion formulation yields powerful advantages when used for robot policies, including gracefully handling multimodal action distributions, being suitable for high-dimensional action spaces, and exhibiting impressive training stability. To fully unlock the potential of diffusion models for visuomotor policy learning on physical robots, this paper presents a set of key technical contributions including the incorporation of receding horizon control, visual conditioning, and the time-series diffusion transformer. We hope this work will help motivate a new generation of policy learning techniques that are able to leverage the powerful generative modeling capabilities of diffusion models.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Code, data, and training details are available (diffusion-policy.cs.columbia.edu).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Policy learning from demonstration, in its simplest form, can be formulated as the supervised regression task of learning to map observations to actions. In practice however, the unique nature of predicting robot actions --- such as the existence of multimodal distributions, sequential correlation, and the requirement of high precision --- makes this task distinct and challenging compared to other supervised learning problems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Prior work attempts to address this challenge by exploring different action representations (Fig 1 a) -- using mixtures of Gaussians Mandlekar et al., categorical representations of quantized actions Shafiullah et al., or by switching the the policy representation (Fig 1 b) -- from explicit to implicit to better capture multi-modal distributions Florence et al.; Wu et al..

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we seek to address this challenge by introducing a new form of robot visuomotor policy that generates behavior via a "conditional denoising diffusion process Ho et al. on robot action space", Diffusion Policy. In this formulation, instead of directly outputting an action, the policy infers the action-score gradient, conditioned on visual observations, for $K$ denoising iterations (Fig. 1 c). This formulation allows robot policies to inherit several key properties from diffusion models -- significantly improving performance.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Expressing multimodal action distributions. By learning the gradient of the action score function Song and Ermon and performing Stochastic Langevin Dynamics sampling on this gradient field, Diffusion policy can express arbitrary normalizable distributions Neal et al., which includes multimodal action distributions, a well-known challenge for policy learning.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

High-dimensional output space. As demonstrated by their impressive image generation results, diffusion models have shown excellent scalability to high-dimension output spaces. This property allows the policy to jointly infer a sequence of future actions instead of single-step actions, which is critical for encouraging temporal action consistency and avoiding myopic planning.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Stable training. Training energy-based policies often requires negative sampling to estimate an intractable normalization constant, which is known to cause training instability Du et al.; Florence et al.. Diffusion Policy bypasses this requirement by learning the gradient of the energy function and thereby achieves stable training while maintaining distributional expressivity.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our primary contribution is to bring the above advantages to the field of robotics and demonstrate their effectiveness on complex real-world robot manipulation tasks. To successfully employ diffusion models for visuomotor policy learning, we present the following technical contributions that enhance the performance of Diffusion Policy and unlock its full potential on physical robots: Closed-loop action sequences. We combine the policy's capability to predict high-dimensional action sequences with receding-horizon control to achieve robust execution. This design allows the policy to continuously re-plan its action in a closed-loop manner while maintaining temporal action consistency -- achieving a balance between long-horizon planning and responsiveness.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Visual conditioning. We introduce a vision-conditioned diffusion policy, where the visual observations are treated as conditioning instead of a part of the joint data distribution. In this formulation, the policy extracts the visual representation once regardless of the denoising iterations, which drastically reduces the computation and enables real-time action inference.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Time-series diffusion transformer. We propose a new transformer-based diffusion network that minimizes the over-smoothing effects of typical CNN-based models and achieves state-of-the-art performance on tasks that require high-frequency action changes and velocity control.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

We systematically evaluate Diffusion Policy across 15 tasks from 4 different benchmarks Florence et al.; Gupta et al.; Mandlekar et al.; Shafiullah et al. under the behavior cloning formulation. The evaluation includes both simulated and real-world environments, 2DoF to 6DoF actions, single- and multi-task benchmarks, and fully- and under-actuated systems, with rigid and fluid objects, using demonstration data collected by single and multiple users.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Empirically, we find consistent performance boost across all benchmarks with an average improvement of 46.9%, providing strong evidence of the effectiveness of Diffusion Policy. We also provide detailed analysis to carefully examine the characteristics of the proposed algorithm and the impacts of the key design decisions.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

This work is an extended version of the conference paper Chi et al.. We expand the content of this paper in the following ways: Include a new discussion section on the connections between diffusion policy and control theory. See Sec. 4.5.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

Include additional ablation studies in simulation on alternative network architecture design and different pretraining and finetuning paradigms, Sec. 5.4.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

Extend the real-world experimental results with three bimanual manipulation tasks including Egg Beater, Mat Unrolling, and Shirt Folding in Sec. 7.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

The code, data, and training details are publicly available for reproducing our results diffusion-policy.cs.columbia.edu.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Diffusion Policy Formulation", "weight": 1.0} -->

We formulate visuomotor robot policies as Denoising Diffusion Probabilistic Models (DDPMs) Ho et al.. Crucially, Diffusion policies are able to express complex multimodal action distributions and possess stable training behavior -- requiring little task-specific hyperparameter tuning. The following sections describe DDPMs in more detail and explain how they may be adapted to represent visuomotor policies.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Denoising Diffusion Probabilistic Models", "weight": 1.0} -->

DDPMs are a class of generative model where the output generation is modeled as a denoising process, often called Stochastic Langevin Dynamics Welling and Teh.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Denoising Diffusion Probabilistic Models", "weight": 1.0} -->

Starting from $\mathbf{x}^{K}$ sampled from Gaussian noise, the DDPM performs $K$ iterations of denoising to produce a series of intermediate actions with decreasing levels of noise, $\mathbf{x}^{k},\mathbf{x}^{k-1}...\mathbf{x}^{0}$, until a desired noise-free output $\mathbf{x}^{0}$ is formed. The process follows the equation where $\epsilon_{\theta}$ is the noise prediction network with parameters $\theta$ that will be optimized through learning and $\mathcal{N}\bigl(0,\sigma^{2}I\bigl)$ is Gaussian noise added at each iteration.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Denoising Diffusion Probabilistic Models", "weight": 1.0} -->

The above equation 1 may also be interpreted as a single noisy gradient descent step: where the noise prediction network $\epsilon_{\theta}(\mathbf{x},k)$ effectively predicts the gradient field $\nabla E(\mathbf{x})$, and $\gamma$ is the learning rate.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Denoising Diffusion Probabilistic Models", "weight": 1.0} -->

The choice of $\alpha,\gamma,\sigma$ as functions of iteration step $k$, also called noise schedule, can be interpreted as learning rate scheduling in gradient decent process. An $\alpha$ slightly smaller than $1$ has been shown to improve stability Ho et al.. Details about noise schedule will be discussed in Sec 3.3.

<!-- chunk {"id": "body-0025", "role": "body", "section": "DDPM Training", "weight": 1.0} -->

The training process starts by randomly drawing unmodified examples, $\mathbf{x}^{0}$, from the dataset. For each sample, we randomly select a denoising iteration $k$ and then sample a random noise $\mathbf{\epsilon}^{k}$ with appropriate variance for iteration $k$. The noise prediction network is asked to predict the noise from the data sample with noise added.

<!-- chunk {"id": "body-0026", "role": "body", "section": "DDPM Training", "weight": 1.0} -->

As shown in Ho et al., minimizing the loss function in Eq 3 also minimizes the variational lower bound of the KL-divergence between the data distribution $p(\mathbf{x}^{0})$ and the distribution of samples drawn from the DDPM $q(\mathbf{x}^{0})$ using Eq 1.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Diffusion for Visuomotor Policy Learning", "weight": 1.0} -->

While DDPMs are typically used for image generation ($\mathbf{x}$ is an image), we use a DDPM to learn robot visuomotor policies. This requires two major modifications in the formulation: 1. changing the output $\mathbf{x}$ to represent robot actions. 2. making the denoising processes conditioned on input observation $\mathbf{O}_{t}$. The following paragraphs discuss each of the modifications, and Fig. 2 shows an overview.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Diffusion for Visuomotor Policy Learning", "weight": 1.0} -->

Closed-loop action-sequence prediction: An effective action formulation should encourage temporal consistency and smoothness in long-horizon planning while allowing prompt reactions to unexpected observations. To accomplish this goal, we commit to the action-sequence prediction produced by a diffusion model for a fixed duration before replanning. Concretely, at time step $t$ the policy takes the latest $T_{o}$ steps of observation data $\mathbf{O}_{t}$ as input and predicts $T_{p}$ steps of actions, of which $T_{a}$ steps of actions are executed on the robot without re-planning. Here, we define $T_{o}$ as the observation horizon, $T_{p}$ as the action prediction horizon and $T_{a}$ as the action execution horizon. This encourages temporal action consistency while remaining responsive. More details about the effects of $T_{a}$ are discussed in Sec 4.3. Our formulation also allows receding horizon control Mayne and Michalska to futher improve action smoothness by warm-starting the next inference setup with previous action sequence prediction.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Diffusion for Visuomotor Policy Learning", "weight": 1.0} -->

Visual observation conditioning: We use a DDPM to approximate the conditional distribution $p(\mathbf{A}_{t}|\mathbf{O}_{t})$ instead of the joint distribution $p(\mathbf{A}_{t},\mathbf{O}_{t})$ used in Janner et al. for planning. This formulation allows the model to predict actions conditioned on observations without the cost of inferring future states, speeding up the diffusion process and improving the accuracy of generated actions. To capture the conditional distribution $p(\mathbf{A}_{t}|\mathbf{O}_{t})$, we modify Eq 1 to: The training loss is modified from Eq 3 to: The exclusion of observation features $\mathbf{O}_{t}$ from the output of the denoising process significantly improves inference speed and better accommodates real-time control. It also helps to make end-to-end training of the vision encoder feasible. Details about the visual encoder are described in Sec. 3.2.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Key Design Decisions", "weight": 1.0} -->

In this section, we describe key design decisions for Diffusion Policy as well as its concrete implementation of $\epsilon_{\theta}$ with neural network architectures.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Network Architecture Options", "weight": 1.0} -->

The first design decision is the choice of neural network architectures for $\epsilon_{\theta}$. In this work, we examine two common network architecture types, convolutional neural networks (CNNs) Ronneberger et al. and Transformers Vaswani et al., and compare their performance and training characteristics. Note that the choice of noise prediction network $\epsilon_{\theta}$ is independent of visual encoders, which will be described in Sec. 3.2.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Network Architecture Options", "weight": 1.0} -->

CNN-based Diffusion Policy We adopt the 1D temporal CNN from Janner et al. with a few modifications: First, we only model the conditional distribution $p(\mathbf{A}_{t}|\mathbf{O}_{t})$ by conditioning the action generation process on observation features $\mathbf{O}_{t}$ with Feature-wise Linear Modulation (FiLM) Perez et al. as well as denoising iteration $k$, shown in Fig 2 (b). Second, we only predict the action trajectory instead of the concatenated observation action trajectory. Third, we removed inpainting-based goal state conditioning due to incompatibility with our framework utilizing a receding prediction horizon. However, goal conditioning is still possible with the same FiLM conditioning method used for observations.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Network Architecture Options", "weight": 1.0} -->

In practice, we found the CNN-based backbone to work well on most tasks out of the box without the need for much hyperparameter tuning. However, it performs poorly when the desired action sequence changes quickly and sharply through time (such as velocity command action space), likely due to the inductive bias of temporal convolutions to prefer low-frequency signals Tancik et al..

<!-- chunk {"id": "body-0034", "role": "body", "section": "Network Architecture Options", "weight": 1.0} -->

Time-series diffusion transformer To reduce the over-smoothing effect in CNN models Tancik et al., we introduce a novel transformer-based DDPM which adopts the transformer architecture from minGPT Shafiullah et al. for action prediction. Actions with noise $A_{t}^{k}$ are passed in as input tokens for the transformer decoder blocks, with the sinusoidal embedding for diffusion iteration $k$ prepended as the first token. The observation $\mathbf{O}_{t}$ is transformed into observation embedding sequence by a shared MLP, which is then passed into the transformer decoder stack as input features. The "gradient" $\epsilon_{\theta}(\mathbf{O_{t}},\mathbf{A_{t}}^{k},k)$ is predicted by each corresponding output token of the decoder stack.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Network Architecture Options", "weight": 1.0} -->

In our state-based experiments, most of the best-performing policies are achieved with the transformer backbone, especially when the task complexity and rate of action change are high. However, we found the transformer to be more sensitive to hyperparameters. The difficulty of transformer training Liu et al. is not unique to Diffusion Policy and could potentially be resolved in the future with improved transformer training techniques or increased data scale.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Network Architecture Options", "weight": 1.0} -->

Recommendations. In general, we recommend starting with the CNN-based diffusion policy implementation as the first attempt at a new task. If performance is low due to task complexity or high-rate action changes, then the Time-series Diffusion Transformer formulation can be used to potentially improve performance at the cost of additional tuning.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Visual Encoder", "weight": 1.0} -->

The visual encoder maps the raw image sequence into a latent embedding $O_{t}$ and is trained end-to-end with the diffusion policy. Different camera views use separate encoders, and images in each timestep are encoded independently and then concatenated to form $O_{t}$. We used a standard ResNet-18 (without pretraining) as the encoder with the following modifications: 1) Replace the global average pooling with a spatial softmax pooling to maintain spatial information Mandlekar et al.. 2) Replace BatchNorm with GroupNorm Wu and He for stable training. This is important when the normalization layer is used in conjunction with Exponential Moving Average He et al. (commonly used in DDPMs).

<!-- chunk {"id": "body-0038", "role": "body", "section": "Noise Schedule", "weight": 1.0} -->

The noise schedule, defined by $\sigma$, $\alpha$, $\gamma$ and the additive Gaussian Noise $\epsilon^{k}$ as functions of $k$, has been actively studied Ho et al.; Nichol and Dhariwal. The underlying noise schedule controls the extent to which diffusion policy captures high and low-frequency characteristics of action signals. In our control tasks, we empirically found that the Square Cosine Schedule proposed in iDDPM Nichol and Dhariwal works best for our tasks.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Accelerating Inference for Real-time Control", "weight": 1.0} -->

We use the diffusion process as the policy for robots; hence, it is critical to have a fast inference speed for closed-loop real-time control. The Denoising Diffusion Implicit Models (DDIM) approach Song et al. decouples the number of denoising iterations in training and inference, thereby allowing the algorithm to use fewer iterations for inference to speed up the process. In our real-world experiments, using DDIM with 100 training iterations and 10 inference iterations enables 0.1s inference latency on a Nvidia 3080 GPU.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Intriguing Properties of Diffusion Policy", "weight": 1.0} -->

In this section, we provide some insights and intuitions about diffusion policy and its advantages over other forms of policy representations.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Model Multi-Modal Action Distributions", "weight": 1.0} -->

The challenge of modeling multi-modal distribution in human demonstrations has been widely discussed in behavior cloning literature Florence et al.; Shafiullah et al.; Mandlekar et al.. Diffusion Policy's ability to express multimodal distributions naturally and precisely is one of its key advantages.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Model Multi-Modal Action Distributions", "weight": 1.0} -->

Intuitively, multi-modality in action generation for diffusion policy arises from two sources -- an underlying stochastic sampling procedure and a stochastic initialization. In Stochastic Langevin Dynamics, an initial sample $\mathbf{A}^{K}_{t}$ is drawn from standard Gaussian at the beginning of each sampling process, which helps specify different possible convergence basins for the final action prediction $\mathbf{A}^{0}_{t}$. This action is then further stochastically optimized, with added Gaussian perturbations across a large number of iterations, which enables individual action samples to converge and move between different multi-modal action basins. Fig. 3, shows an example of the Diffusion Policy's multimodal behavior in a planar pushing task (Push T, introduced below) without explicit demonstration for the tested scenario.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Synergy with Position Control", "weight": 1.0} -->

We find that Diffusion Policy with a position-control action space consistently outperforms Diffusion Policy with velocity control, as shown in Fig 4. This surprising result stands in contrast to the majority of recent behavior cloning work that generally relies on velocity control Mandlekar et al.; Shafiullah et al.; Zhang et al.; Florence et al.; Mandlekar et al.. We speculate that there are two primary reasons for this discrepancy: First, action multimodality is more pronounced in position-control mode than it is when using velocity control. Because Diffusion Policy better expresses action multimodality than existing approaches, we speculate that it is inherently less affected by this drawback than existing methods. Furthermore, position control suffers less than velocity control from compounding error effects and is thus more suitable for action-sequence prediction (as discussed in the following section). As a result, Diffusion Policy is both less affected by the primary drawbacks of position control and is better able to exploit position control's advantages.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Benefits of Action-Sequence Prediction", "weight": 1.0} -->

Sequence prediction is often avoided in most policy learning methods due to the difficulties in effectively sampling from high-dimensional output spaces. For example, IBC would struggle in effectively sampling high-dimensional action space with a non-smooth energy landscape. Similarly, BC-RNN and BET would have difficulty specifying the number of modes that exist in the action distribution (needed for GMM or k-means steps).

<!-- chunk {"id": "body-0045", "role": "body", "section": "Benefits of Action-Sequence Prediction", "weight": 1.0} -->

In contrast, DDPM scales well with output dimensions without sacrificing the expressiveness of the model, as demonstrated in many image generation applications. Leveraging this capability, Diffusion Policy represents action in the form of a high-dimensional action sequence, which naturally addresses the following issues: Temporal action consistency: Take Fig 3 as an example. To push the T block into the target from the bottom, the policy can go around the T block from either left or right. However, suppose each action in the sequence is predicted as independent multimodal distributions (as done in BC-RNN and BET). In that case, consecutive actions could be drawn from different modes, resulting in jittery actions that alternate between the two valid trajectories.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Benefits of Action-Sequence Prediction", "weight": 1.0} -->

Robustness to idle actions: Idle actions occur when a demonstration is paused and results in sequences of identical positional actions or near-zero velocity actions. It is common during teleoperation and is sometimes required for tasks like liquid pouring. However, single-step policies can easily overfit to this pausing behavior. For example, BC-RNN and IBC often get stuck in real-world experiments when the idle actions are not explicitly removed from training.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Training Stability", "weight": 1.0} -->

While IBC, in theory, should possess similar advantages as diffusion policies. However, achieving reliable and high-performance results from IBC in practice is challenging due to IBC's inherent training instability Ta et al.. Fig 6 shows training error spikes and unstable evaluation performance throughout the training process, making hyperparameter turning critical and checkpoint selection difficult. As a result, Florence et al. evaluate every checkpoint and report results for the best-performing checkpoint. In a real-world setting, this workflow necessitates the evaluation of many policies on hardware to select a final policy. Here, we discuss why Diffusion Policy appears significantly more stable to train.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Training Stability", "weight": 1.0} -->

An implicit policy represents the action distribution using an Energy-Based Model (EBM): where $Z(\mathbf{o},\theta)$ is an intractable normalization constant (with respect to $\mathbf{a}$).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Training Stability", "weight": 1.0} -->

To train the EBM for implicit policy, an InfoNCE-style loss function is used, which equates to the negative log-likelihood of Eq 6: where a set of negative samples ${\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\{\widetilde{\mathbf{a}}^{j}\}^{N_{neg}}_{j=1}}$ are used to estimate the intractable normalization constant $Z(\mathbf{o},\theta)$. In practice, the inaccuracy of negative sampling is known to cause training instability for EBMs Du et al.; Ta et al..

<!-- chunk {"id": "body-0050", "role": "body", "section": "Training Stability", "weight": 1.0} -->

Diffusion Policy and DDPMs sidestep the issue of estimating $Z(\mathbf{a},\theta)$ altogether by modeling the score function Song and Ermon of the same action distribution in Eq 6: where the noise-prediction network $\epsilon_{\theta}(\mathbf{a},\mathbf{o})$ is approximating the negative of the score function $\nabla_{\mathbf{a}}\log p(\mathbf{a}|\mathbf{o})$ Liu et al., which is independent of the normalization constant $Z(\mathbf{o},\theta)$. As a result, neither the inference (Eq 4) nor training (Eq 5) process of Diffusion Policy involves evaluating $Z(\mathbf{o},\theta)$, thus making Diffusion Policy training more stable.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Connections to Control Theory", "weight": 1.0} -->

Diffusion Policy has a simple limiting behavior when the tasks are very simple; this potentially allows us to bring to bear some rigorous understanding from control theory. Consider the case where we have a linear dynamical system, in standard state-space form, that we wish to control: Now imagine we obtain demonstrations (rollouts) from a linear feedback policy: ${\bf a}_{t}=-{\bf K}{\bf s}_{t}.$ This policy could be obtained, for instance, by solving a linear optimal control problem like the Linear Quadratic Regulator. Imitating this policy does not need the modeling power of diffusion, but as a sanity check, we can see that Diffusion Policy does the right thing.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Connections to Control Theory", "weight": 1.0} -->

In particular, when the prediction horizon is one time step, $T_{p}=1$, it can be seen that the optimal denoiser which minimizes where $\sigma_{k}$ is the variance on denoising iteration $k$. Furthermore, at inference time, the DDIM sampling will converge to the global minima at ${\bf a}=-{\bf Ks}.$ Trajectory prediction ($T_{p}>1$) follows naturally. In order to predict ${\bf a}_{t+t^{\prime}}$ as a function of ${\bf s}_{t}$, the optimal denoiser will produce ${\bf a}_{t+t^{\prime}}=-{\bf K}({\bf A}-{\bf BK})^{t^{\prime}}{\bf s}_{t}$; all terms involving ${\bf w}_{t}$ are zero in expectation.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Connections to Control Theory", "weight": 1.0} -->

This shows that in order to perfectly clone a behavior that depends on the state, the learner must implicitly learn a (task-relevant) dynamics model Subramanian and Mahajan; Zhang et al.. Note that if either the plant or the policy is nonlinear, then predicting future actions could become significantly more challenging and once again involve multimodal predictions.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Evaluation", "weight": 1.0} -->

We systematically evaluate Diffusion Policy on 15 tasks from 4 benchmarks Florence et al.; Gupta et al.; Mandlekar et al.; Shafiullah et al.. This evaluation suite includes both simulated and real environments, single and multiple task benchmarks, fully actuated and under-actuated systems, and rigid and fluid objects. We found Diffusion Policy to consistently outperform the prior state-of-the-art on all of the tested benchmarks, with an average success-rate improvement of 46.9%. In the following sections, we provide an overview of each task, our evaluation methodology on that task, and our key takeaways.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Simulation Environments and datasets", "weight": 1.0} -->

Robomimic Mandlekar et al. is a large-scale robotic manipulation benchmark designed to study imitation learning and offline RL. The benchmark consists of 5 tasks with a proficient human (PH) teleoperated demonstration dataset for each and mixed proficient/non-proficient human (MH) demonstration datasets for 4 of the tasks (9 variants in total). For each variant, we report results for both state- and image-based observations. Properties for each task are summarized in Tab 3.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Obj", "weight": 1.0} -->

#PH

<!-- chunk {"id": "body-0057", "role": "body", "section": "Obj", "weight": 1.0} -->

#MH

<!-- chunk {"id": "body-0058", "role": "body", "section": "Obj", "weight": 1.0} -->

Push-T adapted from IBC Florence et al., requires pushing a T-shaped block (gray) to a fixed target (red) with a circular end-effector (blue)s. Variation is added by random initial conditions for T block and end-effector. The task requires exploiting complex and contact-rich object dynamics to push the T block precisely, using point contacts. There are two variants: one with RGB image observations and another with 9 2D keypoints obtained from the ground-truth pose of the T block, both with proprioception for end-effector location.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Obj", "weight": 1.0} -->

Multimodal Block Pushing adapted from BET Shafiullah et al., this task tests the policy's ability to model multimodal action distributions by pushing two blocks into two squares in any order. The demonstration data is generated by a scripted oracle with access to groundtruth state info. This oracle randomly selects an initial block to push and moves it to a randomly selected square. The remaining block is then pushed into the remaining square. This task contains long-horizon multimodality that can not be modeled by a single function mapping from observation to action.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Obj", "weight": 1.0} -->

Franka Kitchen is a popular environment for evaluating the ability of IL and Offline-RL methods to learn multiple long-horizon tasks. Proposed in Relay Policy Learning Gupta et al., the Franka Kitchen environment contains 7 objects for interaction and comes with a human demonstration dataset of 566 demonstrations, each completing 4 tasks in arbitrary order. The goal is to execute as many demonstrated tasks as possible, regardless of order, showcasing both short-horizon and long-horizon multimodality.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Evaluation Methodology", "weight": 1.0} -->

We present the best-performing for each baseline method on each benchmark from all possible sources -- our reproduced result (LSTM-GMM) or original number reported in the paper (BET, IBC). We report results from the average of the last 10 checkpoints (saved every 50 epochs) across 3 training seeds and 50 environment initializations ^11^1Due to a bug in our evaluation code, only 22 environment initializations are used for robomimic tasks. This does not change our conclusion since all baseline methods are evaluated in the same way. (an average of 1500 experiments in total). The metric for most tasks is success rate, except for the Push-T task, which uses target area coverage. In addition, we report the average of best-performing checkpoints for robomimic and Push-T tasks to be consistent with the evaluation methodology of their respective original papers Mandlekar et al.; Florence et al.. All state-based tasks are trained for 4500 epochs, and image-based tasks for 3000 epochs.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Evaluation Methodology", "weight": 1.0} -->

Each method is evaluated with its best-performing action space: position control for Diffusion Policy and velocity control for baselines (the effect of action space will be discussed in detail in Sec 5.3). The results from these simulation benchmarks are summarized in Table 2 and Table 2.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Key Findings", "weight": 1.0} -->

Diffusion Policy outperforms alternative methods on all tasks and variants, with both state and vision observations, in our simulation benchmark study (Tabs 2, 2 and 4) with an average improvement of 46.9%. The following paragraphs summarize the key takeaways.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Key Findings", "weight": 1.0} -->

Diffusion Policy can express short-horizon multimodality. We define short-horizon action multimodality as multiple ways of achieving the same immediate goal, which is prevalent in human demonstration data Mandlekar et al.. In Fig 3, we present a case study of this type of short-horizon multimodality in the Push-T task. Diffusion Policy learns to approach the contact point equally likely from left or right, while LSTM-GMM Mandlekar et al. and IBC Florence et al. exhibit bias toward one side and BET Shafiullah et al. cannot commit to one mode.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Key Findings", "weight": 1.0} -->

Diffusion Policy can express long-horizon multimodality. Long-horizon multimodality is the completion of different sub-goals in inconsistent order. For example, the order of pushing a particular block in the Block Push task or the order of interacting with 7 possible objects in the Kitchen task are arbitrary. We find that Diffusion Policy copes well with this type of multimodality; it outperforms baselines on both tasks by a large margin: 32% improvement on Block Push's p2 metric and 213% improvement on Kitchen's p4 metric.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Key Findings", "weight": 1.0} -->

Diffusion Policy can better leverage position control. Our ablation study (Fig. 4) shows that selecting position control as the diffusion-policy action space significantly outperformed velocity control. The baseline methods we evaluate, however, work best with velocity control (and this is reflected in the literature where most existing work reports using velocity-control action spaces Mandlekar et al.; Shafiullah et al.; Zhang et al.; Florence et al.; Mandlekar et al. ).

<!-- chunk {"id": "body-0067", "role": "body", "section": "Key Findings", "weight": 1.0} -->

The tradeoff in action horizon. As discussed in Sec 4.3, having an action horizon greater than 1 helps the policy predict consistent actions and compensate for idle portions of the demonstration, but too long a horizon reduces performance due to slow reaction time. Our experiment confirms this trade-off (Fig. 5 left) and found the action horizon of 8 steps to be optimal for most tasks that we tested.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Key Findings", "weight": 1.0} -->

Robustness against latency. Diffusion Policy employs receding horizon position control to predict a sequence of actions into the future. This design helps address the latency gap caused by image processing, policy inference, and network delay. Our ablation study with simulated latency showed Diffusion Policy is able to maintain peak performance with latency up to 4 steps (Fig 5). We also find that velocity control is more affected by latency than position control, likely due to compounding error effects.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Key Findings", "weight": 1.0} -->

Diffusion Policy is stable to train. We found that the optimal hyperparameters for Diffusion Policy are mostly consistent across tasks. In contrast, IBC Florence et al. is prone to training instability. This property is discussed in Sec 4.4.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

We explore alternative vision encoder design decisions on the simulated robomimic square task. Specifically, we evaluated 3 different architectures: ResNet-18, ResNet-34 He et al. and ViT-B/16 Dosovitskiy et al.. For each architecture, we evaluated 3 different training strategies: training end-to-end from scratch, using frozen pre-trained vision encoder, and finetuning pre-trained vision encoders (with 10x lower learning rate with respect to the policy network). We use ImageNet-21k Ridnik et al. pretraining for ResNet and CLIP Radford et al. pretraining for ViT-B/16. The quantitative comparison on square task with proficient-human (PH) dataset is shown in Tab. 5.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

We found training ViT from scratch to be challenging (with only 22% success rate), likely due to the limited amount data. We also found training with frozen pretrained vision encoder to yield poor performance, which indicates that diffusion policy prefers different vision representation than what is offered in popular pretraining methods. However, we found finetuning the pretrained vision encoder with a small learning rate (10x smaller vs diffusion policy network) gives the best performance overall. This is especially true for the CLIP-trained ViT-B/16, which reaches 98% success rate with only 50 epochs of training. Overall, the best performance across different architectures is not large, despite their significant theoretical capacity gap. We anticipate that their performance gap could be more pronounced on a complex task.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Realworld Evaluation", "weight": 1.0} -->

We evaluated Diffusion Policy in the realworld performance on 4 tasks across 2 hardware setups -- with training data from different demonstrators for each setup. On the realworld Push-T task, we perform ablations examining Diffusion Policy on 2 architecture options and 3 visual encoder options; we also benchmarked against 2 baseline methods with both position-control and velocity-control action spaces. On all tasks, Diffusion Policy variants with both CNN backbones and end-to-end-trained visual encoders yielded the best performance. More details about the task setup and parameters may be found in supplemental materials.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Realworld Push-T Task", "weight": 1.0} -->

Real-world Push-T is significantly harder than the simulated version due to 3 modifications: 1. The real-world Push-T task is multi-stage. It requires the robot to \\raisebox{-0.9pt}{1}⃝ push the T block into the target and then \\raisebox{-0.9pt}{2}⃝ move its end-effector into a designated end-zone to avoid occlusion. 2. The policy needs to make fine adjustments to make sure the T is fully in the goal region before heading to the end-zone, creating additional short-term multimodality. 3. The IoU metric is measured at the last step instead of taking the maximum over all steps. We threshold success rate by the minimum achieved IoU metric from the human demonstration dataset. Our UR5-based experiment setup is shown in Fig 6. Diffusion Policy predicts robot commands at 10 Hz and these commands then linearly interpolated to 125 Hz for robot execution.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Realworld Push-T Task", "weight": 1.0} -->

Result Analysis. Diffusion Policy performed close to human level with 95% success rate and 0.8 v.s. 0.84 average IoU, compared with the 0% and 20% success rate of best-performing IBC and LSTM-GMM variants. Fig 7 qualitatively illustrates the behavior for each method starting from the same initial condition. We observed that poor performance during the transition between stages is the most common failure case for the baseline method due to high multimodality during those sections and an ambiguous decision boundary. LSTM-GMM got stuck near the T block in 8 out of 20 evaluations (3rd row), while IBC prematurely left the T block in 6 out of 20 evaluations (4th row). We did not follow the common practice of removing idle actions from training data due to task requirements, which also contributed to LSTM and IBC's tendency to overfit on small actions and get stuck in this task. The results are best appreciated with videos in supplemental materials.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Realworld Push-T Task", "weight": 1.0} -->

End-to-end v.s. pre-trained vision encoders We tested Diffusion Policy with pre-trained vision encoders (ImageNet Deng et al. and R3MNair et al. ), as seen in Tab. 6. Diffusion Policy with R3M achieves an 80% success rate but predicts jittery actions and is more likely to get stuck compared to the end-to-end trained version. Diffusion Policy with ImageNet showed less promising results with abrupt actions and poor performance. We found that end-to-end training is still the most effective way to incorporate visual observation into Diffusion Policy, and our best-performing models were all end-to-end trained.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Realworld Push-T Task", "weight": 1.0} -->

Robustness against perturbation Diffusion Policy's robustness against visual and physical perturbations was evaluated in a separate episode from experiments in Tab 6. As shown in Fig 8, three types of perturbations are applied. 1) The front camera was blocked for 3 secs by a waving hand (left column), but the diffusion policy, despite exhibiting some jitter, remained on-course and pushed the T block into position. 2) We shifted the T block while Diffusion Policy was making fine adjustments to the T block's position. Diffusion policy immediately re-planned to push from the opposite direction, negating the impact of perturbation. 3) We moved the T block while the robot was en route to the end-zone after the first stage's completion. The Diffusion Policy immediately changed course to adjust the T block back to its target and then continued to the end-zone. This experiment indicates that Diffusion Policy may be able to synthesize novel behavior in response to unseen observations.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Mug Flipping Task", "weight": 1.0} -->

The mug flipping task is designed to test Diffusion Policy's ability to handle complex 3D rotations while operating close to the hardware's kinematic limits. The goal is to reorient a randomly placed mug to have \\raisebox{-0.9pt}{1}⃝ the lip facing down \\raisebox{-0.9pt}{2}⃝ the handle pointing left, as shown in Fig. 9. Depending on the mug's initial pose, the demonstrator might directly place the mug in desired orientation, or may use additional push of the handle to rotation the mug. As a result, the demonstration dataset is highly multi-modal: grasp vs push, different types of grasps (forehand vs backhand) or local grasp adjustments (rotation around mug's principle axis), and are particularly challenging for baseline approaches to capture.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Mug Flipping Task", "weight": 1.0} -->

Result Analysis. Diffusion policy is able to complete this task with 90% success rate over 20 trials. The richness of captured behaviors is best appreciated with the video. Although never demonstrated, the policy is also able to sequence multiple pushes for handle alignment or regrasps for dropped mug when necessary. For comparison, we also train a LSTM-GMM policy trained with a subset of the same data. For 20 in-distribution initial conditions, the LSTM-GMM policy never aligns properly with respect to the mug, and fails to grasp in all trials.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Sauce Pouring and Spreading", "weight": 1.0} -->

The sauce pouring and spreading tasks are designed to test Diffusion Policy's ability to work with non-rigid objects, 6 Dof action spaces, and periodic actions in real-world setups. Our Franka Panda setup and tasks are shown in Fig 10. The goal for the 6DoF pouring task is to pour one full ladle of sauce onto the center of the pizza dough, with performance measured by IoU between the poured sauce mask and a nominal circle at the center of the pizza dough (illustrated by the green circle in Fig 10). The goal for the periodic spreading task is to spread sauce on pizza dough, with performance measured by sauce coverage. Variations across evaluation episodes come from random locations for the dough and the sauce bowl. The success rate is computed by thresholding with minimum human performance. Results are best viewed in supplemental videos. Both tasks were trained with the same Push-T hyperparameters, and successful policies were achieved on the first attempt.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Sauce Pouring and Spreading", "weight": 1.0} -->

The sauce pouring task requires the robot to remain stationary for a period of time to fill the ladle with viscous tomato sauce. The resulting idle actions are known to be challenging for behavior cloning algorithms and therefore are often avoided or filtered out. Fine adjustments during pouring are necessary during sauce pouring to ensure coverage and to achieve the desired shape.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Sauce Pouring and Spreading", "weight": 1.0} -->

The demonstrated sauce-spreading strategy is inspired by the human chef technique, which requires both a long-horizon cyclic pattern to maximize coverage and short-horizon feedback for even distribution (since the tomato sauce used often drips out in lumps with unpredictable sizes). Periodic motions are known to be difficult to learn and therefore are often addressed by specialized action representations Yang et al.. Both tasks require the policy to self-terminate by lifting the ladle/spoon.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Sauce Pouring and Spreading", "weight": 1.0} -->

Result Analysis. Diffusion policy achieves close-to-human performance on both tasks, with coverage 0.74 vs 0.79 on pouring and 0.77 vs 0.79 on spreading. Diffusion policy reacted gracefully to external perturbations such as moving the pizza dough by hand during pouring and spreading. Results are best appreciated with videos in the supplemental material.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Sauce Pouring and Spreading", "weight": 1.0} -->

LSTM-GMM performs poorly on both sauce pouring and spreading tasks. It failed to lift the ladle after successfully scooping sauce in 15 out of 20 of the pouring trials. When the ladle was successfully lifted, the sauce was poured off-centered. LSTM-GMM failed to self-terminate in all trials. We suspect LSTM-GMM's hidden state failed to capture sufficiently long history to distinguish between the ladle dipping and the lifting phases of the task. For sauce spreading, LSTM-GMM always lifts the spoon right after the start, and failed to make contact with the sauce in all 20 experiments.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Realworld Bimanual Tasks", "weight": 1.0} -->

Beyond single arm setup, we further demonstrate Diffusion Policy on several challenging bimanual tasks. To enable bimanual tasks, the majority of effort was spent on extending our robot stack to support multi-arm teleopration and control. Diffusion Policy worked out of the box for these tasks without hyperparameter tuning.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Observation and Action Spaces", "weight": 1.0} -->

The proprioceptive observation space is extended to include the poses of both end-effectors and the gripper widths of both grippers. We also extend the observation space to include the actual and desired values of these quantities. The image observation space is comprised of two scene cameras and two wrist cameras, one attached to each arm. The action space is extended to include the desired poses of both end-effectors and the desired gripper widths of both grippers.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Teleoperation", "weight": 1.0} -->

For these coordinated bimanual tasks, we found using 2 SpaceMouse simultaneously quite challenging for the demonstrator. Thus, we implemented two new teleoperation modes: using a Meta Quest Pro VR device with two hand controllers, or haptic-enabled control using 2 Haption Virtuose^™^ 6D HF TAO devices using bilateral position-position coupling as described succinctly in the haptics section of Siciliano et al.. This coupling is performed between a Haption device and a Franka Panda arm. More details on the controllers themselves may be found in Sec. D.1. The following provides more details on each task and policy performance.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Bimanual Egg Beater", "weight": 1.0} -->

The bimanual egg beater task is illustrated and described in Fig. 11, using a OXO^™^Egg Beater and a Room Essentials^™^plastic bowl. We chose this task to illustrate the importance of haptic feedback for teleoperating bimanual manipulation even for common daily life tasks such as coordinated tool use. Without haptic feedback, an expert was unable to successfully complete a single demonstration out of 10 trials. 5 failed due to robot pulling the crank handle off the egg beater; 3 failed due to robot losing grasp of the handle; 2 failed due to robot triggering torque limit. In contrast, the same operator could easily perform this task 10 out of 10 times with haptic feedback. Using haptic feedback made it possible for the demonstrations to be both quicker and higher quality than without feedback.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Bimanual Egg Beater", "weight": 1.0} -->

Result Analysis. Diffusion policy is able to complete this task with 55% success rate over 20 trials, trained using 210 demonstrations. The primary failure modes for these were out-of-domain initial positioning of the egg beater, or missing the egg beater crank handle or losing grasp of it. The initial and final states for all rollouts are visualized in 19 and 19.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Bimanual Mat Unrolling", "weight": 1.0} -->

The mat unrolling task is shown and described in Fig. 12, using a XXL Dog Buddy^™^Dog Mat. This task was teleoperated using the VR setup, as it did not require rich haptic feedback to perform the task. We taught this skill to be omnidextrous, meaning it can unroll either to the left or right depending on the initial condition.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Bimanual Mat Unrolling", "weight": 1.0} -->

Result Analysis. Diffusion policy is able to complete this task with 75% success rate over 20 trials, trained using 162 demonstrations. The primary failure modes for these were missed grasps during initial grasp of the mat, where the policy struggled to correct itself and thus got stuck repeating the same behavior. The initial and final states for all rollouts are visualized in 17 and 17.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Bimanual Shirt Folding", "weight": 1.0} -->

The shirt folding task is described and illustrated in Fig. 13, using a short-sleeve T-shirt. This task was also teleoperated using the VR setup as it did not require rich feedback to perform the task. Due to the kinematic and workspace constraints, this task is notably longer and can take up to nine discrete steps. The last few steps require both grippers to come very close towards each other. Having our mid-level controller explicitly handling collision avoidance was especially important for both teleoperation and policy rollout.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Bimanual Shirt Folding", "weight": 1.0} -->

Result Analysis. Diffusion policy is able to complete this task with 75% success rate over 20 trials, trained using 284 demonstrations. The primary failure modes for these were missed grasps for initial folding (the sleeves and the color), and the policy being unable to stop adjusting the shirt at the end. The initial and final states for all rollouts are visualized in 21 and 21.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Limitations and Future Work", "weight": 1.5} -->

Although we have demonstrated the effectiveness of diffusion policy in both simulation and real-world systems, there are limitations that future work can improve. First, our implementation inherits limitations from behavior cloning, such as suboptimal performance with inadequate demonstration data. Diffusion policy can be applied to other paradigms, such as reinforcement learning Wang et al.; Hansen-Estruch et al., to take advantage of suboptimal and negative data. Second, diffusion policy has higher computational costs and inference latency compared to simpler methods like LSTM-GMM. Our action sequence prediction approach partially mitigates this issue, but may not suffice for tasks requiring high rate control. Future work can exploit the latest advancements in diffusion model acceleration methods to reduce the number of inference steps required, such as new noise schedules Chen, inference solvers Karras et al., and consistency models Song et al..

<!-- chunk {"id": "body-0094", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we assess the feasibility of diffusion-based policies for robot behaviors. Through a comprehensive evaluation of 15 tasks in simulation and the real world, we demonstrate that diffusion-based visuomotor policies consistently and definitively outperform existing methods while also being stable and easy to train. Our results also highlight critical design factors, including receding-horizon action prediction, end-effector position control, and efficient visual conditioning, that is crucial for unlocking the full potential of diffusion-based policies. While many factors affect the ultimate quality of behavior-cloned policies --- including the quality and quantity of demonstrations, the physical capabilities of the robot, the policy architecture, and the pretraining regime used --- our experimental results strongly indicate that policy structure poses a significant performance bottleneck during behavior cloning. We hope that this work drives further exploration in the field into diffusion-based policies and highlights the importance of considering all aspects of the behavior cloning process beyond just the data used for policy training.
