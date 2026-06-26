<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

LeARN: Learnable and Adaptive Representations for Nonlinear Dynamics in System Identification

Topics include Robustness, System identification, Neural networks, Attention mechanisms, Meta-learning, Datasets, Online algorithms, Generalization, Learning, LeARN, DNN, Nonlinear systems, Nonlinear system identification.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

System identification, the process of deriving mathematical models of dynamical systems from observed input-output data, has undergone a paradigm shift with the advent of learning-based methods. Addressing the intricate challenges of data-driven discovery in nonlinear dynamical systems, these methods have garnered significant attention. Among them, Sparse Identification of Nonlinear Dynamics (SINDy) has emerged as a transformative approach, distilling complex dynamical behaviors into interpretable linear combinations of basis functions. However, SINDy relies on domain-specific expertise to construct its foundational "library" of basis functions, which limits its adaptability and universality. In this work, we introduce a nonlinear system identification framework called LeARN that transcends the need for prior domain knowledge by learning the library of basis functions directly from data. To enhance adaptability to evolving system dynamics under varying noise conditions, we employ a novel meta-learning-based system identification approach that uses a lightweight deep neural network (DNN) to dynamically refine these basis functions. This not only captures intricate system behaviors but also adapts seamlessly to new dynamical regimes. We validate our framework on the Neural Fly dataset, showcasing its robust adaptation and generalization capabilities.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Despite its simplicity, our LeARN achieves competitive dynamical error performance compared to SINDy. This work presents a step toward the autonomous discovery of dynamical systems, paving the way for a future where machine learning uncovers the governing principles of complex systems without requiring extensive domain-specific interventions.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Robustness of robotic systems in unstructured environments requires adaptive control laws, yet their efficacy is fundamentally contingent upon the accuracy of the underlying plant model. Historically, these models have relied on physics-based equations to ensure reliability and physical interpretability under ideal conditions. However, such models face critical limitations: Complex nonlinear dynamics: Many robotic systems operate in high-dimensional spaces with nonlinear interactions, making precise modeling difficult.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Unknown or un-modeled dynamics: Environmental disturbances and uncertainties often introduce dynamics that are challenging to capture using predefined equations.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

High-dimensional inputs: Robots with numerous sensors and actuators generate large-scale data that physics-based models may struggle to incorporate.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Traditional system identification typically relies on physics-based models, which, despite their theoretical grounding, are often constrained by a reliance on domain expertise and frequently fail to capture complex nonlinear behaviors and un-modeled environmental disturbances. Although early extensions like the Wiener and Volterra series attempted to address this, the field has increasingly pivoted toward data-driven methods, with neural networks proving effective for identifying nonlinear systems. Modern deep learning approaches, such as universal approximators and Physics-Informed Neural Networks (PINNs), excel in high-dimensional modeling, but lack the interpretability required for safety-critical robotics. In contrast, Sparse Identification of Nonlinear Dynamics (SINDy) ensures interpretability through sparsity, but remains limited by its dependence on predefined domain-specific basis libraries. This necessity for prior knowledge hinders scalability and flexibility when encountering unknown or evolving dynamics. Unlike previous autoencoder-based approaches that attempt to resolve this by learning latent coordinate transformations to fit fixed, human-designed libraries; although the requirement for domain expertise is effectively addressed there, the interpretability of the resulting learned dynamics equations is significantly diminished because of the latent space coordinate representation; we instead introduce LeARN.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Our framework meta-learns the functional basis library itself directly from data in the physical state space, bridging the gap between deep learning's expressiveness and SINDy's interpretability while enabling rapid adaptation to unseen dynamics via Model-Agnostic Meta-Learning (MAML). Our key contributions are: Unlike traditional SINDy, our method does not require a predefined function library, thus enhancing flexibility and eliminating the need for domain expertise.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

By meta-learning the library of basis functions, LeARN enables adaptability to changing dynamics and noisy conditions.

<!-- chunk {"id": "body-0010", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

By employing light-weight deep neural networks, we retain the ability to model complex nonlinearities while the learned basis functions facilitate structural interpretability in terms of identifying the input features contributing dominantly to system dynamics.

<!-- chunk {"id": "body-0011", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In this paper, we test our approach on the Neural Fly dataset, which provides a challenging benchmark for nonlinear system identification. Therefore, throughout the paper, our principal robotic system of interest for the demonstration of our framework will be a quadrotor.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Sparse System Identification", "weight": 1.0} -->

SINDy (Sparse Identification for Nonlinear Dynamics) employs sparse regression to model system dynamics, identifying the terms that contribute prominently to the dynamical model. SINDy models the dynamics as follows: where $\Theta(\cdot)$ constitutes candidate basis functions. $\mathcal{E}$ is a matrix of coefficients for terms obtained by processing $\Theta(X)$, where $X$ represents our features of interest to model the dynamics.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Sparse System Identification", "weight": 1.0} -->

Choosing basis functions for $\Theta(\cdot)$ is a problem-specific and non-trivial task. Since the best choice is often not clear, we attempt to address the problem in this paper. Since our system of interest is a quadrotor, the features of interest $X$ comprise the states and control inputs as detailed in Sec IV.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B Meta-Learning", "weight": 1.0} -->

Meta-Learning is a mechanism of learning to learn. It seeks parameters that optimize a meta-objective over a distribution of tasks. Model Agnostic Meta-Learning (MAML) provides a gradient-based framework to leverage meta-learning approaches to different kinds of tasks while being agnostic to the learning framework and the architecture of the neural network model. For MAML, the bi-level meta-learning problem can be formulated as where the optimal meta-parameters $\theta^{*}$ minimize the average evaluation loss across $M$ tasks. Each task $i$ is associated with a task-specific loss function $\ell_{i}$, a training dataset $\mathcal{D}_{i}^{\text{train}}$, and an evaluation dataset $\mathcal{D}_{i}^{\text{eval}}$. The task-specific parameters $\phi_{i}$ are derived by applying a gradient-based adaptation mechanism which adapts the meta-parameters $\theta$ to the task using the task's training dataset.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B Meta-Learning", "weight": 1.0} -->

Here, $\mu_{\text{meta}}\geq 0$ is the regularization coefficient. This formulation ensures that the meta-parameters $\theta$ are well-suited for adaptation across a variety of tasks. Meta-learning based approaches have been applied to system identification in linear time-varying settings and for Koopman-based modeling of nonlinear systems with parametric uncertainty. They have also been used in adaptive control to model residual aerodynamical interactions, for control. meta-learns an adaptive controller based on closed-loop tracking simulations. Our work differs in that we use meta-learning to learn the basis function library used in SINDy-style sparse identification, operating directly on the physical state and control variables rather than on a latent representation. As we will see in Sec. III, meta-learning provides an effective initialization for parameterized basis functions, ensuring rapid adaptation across varying system dynamics.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A Problem Formulation", "weight": 1.0} -->

Since our system of interest in this paper is a quadrotor, we consider the following dynamics. where the global position vector $p\in\mathbb{R}^{3}$, velocity vector $v\in\mathbb{R}^{3}$, attitude rotation matrix $R\in\mathbf{SO}$ and body angular velocity $\omega\in\mathbb{R}^{3}$ give the states of the quadrotor. Furthermore, $m$ is the mass of the quadrotor, $J$ is the inertia matrix, $g$ is gravitational acceleration, $f_{a}$ is the external disturbance force, $S(\cdot)$ is the skew-symmetric mapping, $\tau_{u}$ and $\tau_{a}$ are control and external disturbance torques, respectively.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A Problem Formulation", "weight": 1.0} -->

We first model partial dynamics of the quadrotor for which we will use the following formulation of: where based on Eq, we model the evolution of the translational dynamics as a function of its state $v$ and the control input $Rf_{u}$, where $f_{u}=\begin{bmatrix}0&0&T\end{bmatrix}^{\mathrm{T}}$, $T$ being the magnitude of the thrust generated by the quadrotor motors at the sampling time instant.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-A Problem Formulation", "weight": 1.0} -->

The quadrotor output wrench $\eta=\begin{bmatrix}T&\tau_{x}&\tau_{y}&\tau_{z}\end{bmatrix}^{\mathrm{T}}$ is linearly related to the squared motor speeds $u=\begin{bmatrix}n_{1}^{2}&n_{2}^{2}&n_{3}^{2}&n_{4}^{2}\end{bmatrix}^{\mathrm{T}}$ by $\eta=B_{0}u$, where $B_{0}$ models the coefficients of rotor force and torque. Therefore, inspired by Eq, for our analysis, we will model the partial attitude dynamics for the quadrotor as follows: Finally, based on Eq and Eq, we model the full system dynamics as follows: We model a progression of partial and full dynamics to highlight the fact, as we will see in Sec IV, that LeARN becomes progressively more competitive against SINDy as the dimension of the state space increases.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A Problem Formulation", "weight": 1.0} -->

Now, our objective is to identify the mappings $f(\cdot)$ and $g(\cdot)$ and by extension the full dynamics $h(\cdot)$, as in Eq, and respectively, without relying on a pre-defined library of basis functions (e.g., polynomial or trigonometric terms) as mandated by SINDy.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B LeARN Framework", "weight": 1.0} -->

Before introducing our framework, it is imperative to note that the greatest advantage of employing SINDy is its interpretability. For instance, an example dynamical evolution of a state vector $\textbf{x}\in\mathbb{R}^{3}$ could be learned via the SINDy framework and identified as follows: where $sin(\cdot)$ and $cos(\cdot)$ comprise the candidate basis function library $\Theta(\cdot)$. Thus, any move away from SINDy will hamper its intepretability, as we see, which relies on latent coordinate transformations of system state vectors. Therefore, our attempt while designing the LeARN framework is to find a middle ground, as discussed next.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B LeARN Framework", "weight": 1.0} -->

To avoid manual design (as in SINDy), we learn the basis function library directly from the data by parameterizing it via deep neural networks. We also seek to retain some key elements of the dynamical evolution, while employing the expressiveness of neural networks.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B LeARN Framework", "weight": 1.0} -->

Thus, our LeARN framework decomposes the dynamics into a learned basis function library and a feature selection matrix as shown in Fig 1. For an augmented input feature vector $X$ (combining state and control inputs), we model the dynamical evolution $y\approx\dot{\mathbf{x}}$ as Figure 1: For a concatenated feature vector X ∈ ℝ1 × (I + U) of the form, $X=\begin{bmatrix}x&u\end{bmatrix}$, where x ∈ ℝ1 × I is the state feature vector and u ∈ ℝ1 × U is the control input corresponding to x, Θ(X; ψ) ∈ ℝ1 × P(I + U) is the learned basis function library for a total of P basis functions, where mp represents the pth basis function and ℰ(X; ϕ) ∈ ℝI × P(I + U) is the learned feature selection matrix, for a total of n = I sets of coefficients, ek ∈ ℝ1 × (P + U) is coefficient for kth state feature in X.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B LeARN Framework", "weight": 1.0} -->

Here, $\Theta(\cdot;\psi)$ is a lightweight DNN parameterized by $\psi$ that learns a representation for the basis function library $\Theta(\cdot)$, and $\mathcal{E}(\cdot;\phi)$ is a second DNN parameterized by $\phi$ that acts as a feature selection matrix. This decomposition structure mimics that of SINDy ($y=\Theta\xi$), where we can identify the terms contributing to the dynamics but replaces the fixed library with a learned parametrized representation of $\Theta$. Compared to Eq 8, LeARN could estimate the dynamical evolution of some state vector $\textbf{x}\in\mathbb{R}^{3}$ as follows: where $m_{1}(\cdot)$ and $m_{2}(\cdot)$ are the outputs of the DNN $\Theta(\cdot;\psi)$ as illustrated in Fig 1. In Eq 8, the functional relationship and the dominant terms that contribute to the dynamics are apparent.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-B LeARN Framework", "weight": 1.0} -->

LeARN retains the latter, from Eq 10, we infer that $x$ and $x$ contribute predominantly to the dynamical evolution of $\textbf{x}\in\mathbb{R}^{3}$, while $x$ does not contribute to its evolution. Note that while each $m_{p}(\cdot)$ takes the full feature vector $X$ as input (see Fig. 1), interpretability here refers to the sparsity structure of $\mathcal{E}$, which identifies dominant input features, rather than to the functional form of $m_{p}$ itself.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-C Meta-Training and Adaptation", "weight": 1.0} -->

We start training by employing a Model-Agnostic Meta-Learning (MAML) approach to learn $\psi$ and $\phi$. The training loop samples tasks $\mathcal{T}_{i}$ corresponding to different wind conditions from the training distribution. Since we are evaluating our methods on the Neural Fly dataset, the different task objectives involve modeling the system dynamics accurately for a quadrotor being flown using a nonlinear baseline controller under different wind conditions. In the inner loop, the parameters are adapted to minimize the dynamical estimation loss $L_{i}=\|\dot{v}_{i}-\Theta_{\psi}\mathcal{E}_{\phi}^{T}\|_{2}^{2}$. The outer loop updates the initial parameters to ensure that they serve as a robust initialization for rapid adaptation to unseen environments. The algorithm is presented in a concise manner in Alg. 1.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-C Meta-Training and Adaptation", "weight": 1.0} -->

Input: [v(W), Rfu(W)]: feature distributions over 𝒟itrain Output: ϕ, ψ: meta-trained parameters Hyperparameters: α, β, n (step sizes, inner rounds) /* Randomly initialize ϕ and ψ (parameters of the DNN giving ℰ and basis library functions in Θ) */while not done do Sample batch of tasks 𝒯i(vi, Rfui) ∼ [v(W), Rfu(W)]; for all 𝒯i(vi, Rfui) do Evaluate basis Θψ(vi, Rfui) and selection ℰϕ(vi, Rfui); // Evaluate the task objective (dynamical estimation) loss: // Compute adapted parameters ϕ′ and ψ′: Sample query points Di′ = {vi′, Rfui′} from 𝒯i; // Consider meta-loss Li′ and perform meta-update: Algorithm 1 The Meta-Training Loop of LeARN Once, we have the meta-trained parameters, we perform online adaptation while deployment on unseen new tasks as discussed in Eq. While online adaptation, we assume that the state features are $L$ Lipschitz continuous, and add a regularizer to guide the training process as follows: where we

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-C Meta-Training and Adaptation", "weight": 1.0} -->

initialize $\psi_{\textit{t}}$ and $\phi_{\textit{t}}$, with the meta-trained parameters $\psi$ and $\phi$ respectively at $t=0$, while adapting to a new task i.e. a new wind condition for the quadrotor to fly, $X_{\textit{t}}$ is sampled from the new task and $L_{\textit{adapt}}$ gives us the adaptation loss as follows: where $\lambda$ is a hyperparameter and the regularizer ensures $L$ Lipschitz continuity of the state inputs.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-A Experimental Setup", "weight": 1.0} -->

We present a comparative performance analysis of our framework LeARN against SINDy. Based on the Neural Fly dataset, we use data gathered by the quadrotor using the baseline controller in the wind conditions as documented in Table I for meta-training the parameters $\psi$ and $\phi$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-A Experimental Setup", "weight": 1.0} -->

We employ SINDy with the sparsity threshold set to 0.2. Before delving into further results, it is important to note that for the adaptation wind tasks in the Neural Fly dataset, the data was collected by maneuvering the quadrotor in a figure-eight trajectory. The figure-eight trajectory is inherently oscillatory, which makes it naturally suited to modeling by trigonometric functions. Although DNNs are universal approximators, their capacity is constrained by their architecture and training data. A finite-capacity DNN may have insufficient expressive power to capture the intricate oscillatory behavior of such trajectories, particularly in unobserved regions of the input space, resulting in suboptimal generalization performance.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-A Experimental Setup", "weight": 1.0} -->

Ground Truth Adaptation Generalization Figure 2: Qualitative results of the full dynamics modeled by SINDy and LeARN across different wind conditions. The horizontal axis runs across 2511 data points collected over a time period of 50.2s sampled at 0.02s and the vertical axis represents the value.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-B Comparative Performance Analysis", "weight": 1.0} -->

For the analysis of adaptation and generalization performance, we evaluate the mean-squared error (MSE) between the ground truth and the dynamical predictions. Throughout, adaptation performance refers to the MSE evaluated on the support data used for online gradient updates, and generalization performance refers to the MSE on held-out query data from the same task on which no gradient updates are performed. Despite the limitations discussed above, we observe that LeARN delivers a much more competitive generalization performance as the input feature space begins to increase in dimension even with a light-weight DNN. It can be observed that the average difference in the generalization performance across the different adaptation wind tasks reduces from 0.043737 in Tables III to 0.002853 in Table (IV), and further down to 0.001811 in Table V, as the dimensionality of the concatenated input feature $X$ increases. We use the PySINDy package to model the SINDy dynamics representations and the Higher package to implement the bi-level MAML training loop.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we introduced LeARN, a novel algorithm for meta-learning the basis functions for nonlinear system identification. Our proposed approach demonstrates significant adaptability and generalization capabilities in modeling dynamical systems, as evidenced by its performance on unseen wind conditions in the Neural Fly dataset. Unlike the SINDy algorithm, our approach learns the library of basis functions directly from the data. The proposed algorithm yields a parameterized basis function library optimized for adaptability to new, unseen environments. This is intended to improve robustness without requiring system-specific redesigns when encountering new dynamic regimes. Notably, we demonstrated that LeARN significantly narrows the performance gap with SINDy, particularly as the dimensionality of the input feature space increases, underscoring its suitability for capturing higher dimensional, complex nonlinear dynamical interactions. In the future, we aim to explore higher dimensional input feature spaces and techniques for learning basis functions for modeling intrinsic residual dynamics.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Looking ahead, our study sets the groundwork for addressing the broader goal of enabling robots to autonomously model and adapt to dynamic unstructured environments. Furthermore, our approach paves the way for developing robust, versatile, and adaptive robotic systems capable of operating safely and effectively in the real-world where such approaches can be utilized for health monitoring of these systems via data-driven system identification.
