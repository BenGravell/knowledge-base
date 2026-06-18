<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Physics-Informed Machine Learning for Modeling and Control of Dynamical Systems

Topics include Stability analysis, System identification, Control, Learning, PIML, Machine learning, Physical law.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Physics-informed machine learning (PIML) is a set of methods and tools that systematically integrate machine learning (ML) algorithms with physical constraints and abstract mathematical models developed in scientific and engineering domains. As opposed to purely data-driven methods, PIML models can be trained from additional information obtained by enforcing physical laws such as energy and mass conservation. More broadly, PIML models can include abstract properties and conditions such as stability, convexity, or invariance. The basic premise of PIML is that the integration of ML and physics can yield more effective, physically consistent, and data-efficient models. This paper aims to provide a tutorial-like overview of the recent advances in PIML for dynamical system modeling and control. Specifically, the paper covers an overview of the theory, fundamental concepts and methods, tools, and applications on topics of: 1) physics-informed learning for system identification; 2) physics-informed learning for control; 3) analysis and verification of PIML models; and 4) physics-informed digital twins. The paper is concluded with a perspective on open challenges and future research opportunities.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Modern engineering systems generate large amounts of data either via sensors in the physical world or via simulation of virtual environments. The increased storage and computational power of the underlying hardware and communication infrastructure paved the way for the use of data-driven algorithms. Machine learning (ML) methods leverage a large amount of data to achieve remarkable success, especially in areas such as games, speech recognition, or image processing. These recorded successes especially occur in the areas where there is an abundance of data and where the underlying processes have hard-to-discover governing laws and are driven by non-obvious fundamental principles. In such cases, ML shows strong capabilities in learning non-obvious relations that allow to achieve the desired tasks if a sufficient amount of representative data is available.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Due to such successes, a number of investigations have started involving the application of ML to other domains, including physical systems, such as automotive, aerospace, process control, energy systems, and robotics. However, these traditional engineering applications are governed by fundamental principles and physical constraints that have been studied for centuries and are thus better understood or well-known. Some examples include conservation laws of mass or energy, fundamental laws of motion or electromagnetism, ranges of constants such as efficiencies and physical dimensions or gravitational constants. For physical systems, there may be expectations that ML models will satisfy such principles and constraints. While the prediction accuracy of ML methods may be as good in the computer science domains, the lack of satisfaction of fundamental principles and underlying physics and safety constraints represent a significant limitation to actual deployment of ML models in real-world applications.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Properly enforcing physical laws and constraints in ML may result in several benefits, affecting training, performance, and trust of the ML result such as: $(i)$ reduced data requirement of the ML model due to learning in lower dimensional, manifolds; $({ii})$ higher precision and improved generalization since the underlying physical principles will be satisfied and the errors related to violating them will be avoided; $({iii})$ increased interpretability and trust by the application engineers by upholding the known domain principles. However, most of the standard ML approaches cannot leverage physical principles and constraints, resulting in a limited real-world impact of ML in the safety-critical domains.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The cautious adoption of modern ML methods in real-world engineering domains is a direct result of the research priorities in the historical developments within the computer science domains. More specifically, ML methods have been primarily developed in domains related to human aspects and behaviors, such as vision or language recognition, where the safety requirements are less strict. Furthermore, those domains consist of underlying physical principles that are still partially unexplained or extremely complex to describe and hence hard to be embedded directly in the ML algorithms.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In recent years, researchers from both computer science and engineering domains have recognized the potential of bridging this gap by developing new methods that combine algorithms and tools from machine learning with well-known engineering models and principles. This quest to extend machine learning to account for the physical principles and constraints of the underlying process gave rise to the so-called Physics Informed Machine Learning (PIML), also referred to as Scientific Machine Learning (SciML). Related surveys in this area include PIML methods for partial differential equations (PDEs) or generic dynamical systems. However, to the author's best knowledge, there is no tutorial overview of the PIML methods for the control of dynamical systems. This paper aims to bridge this gap. The rest of the paper is structured as follows, section II. reviews the landscape of PIML methods for modeling and control of dynamical systems, including PIML methods for system identification, control design, and formal verification. Section III. briefly summarizes current challenges and opportunities. While section IV. concludes the paper.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Landscape of Physics-Informed Machine Learning Methods for Modeling and Control", "weight": 1.0} -->

In this paper, we define PIML as follows.

<!-- chunk {"id": "body-0009", "role": "body", "section": "II-A Physics-informed learning for system identification", "weight": 1.0} -->

One of the first applications of PIML in control is to learn dynamical models for a physical system given some prior knowledge and time series data. Conventional dynamical system and control theories usually use *white-box* modeling to develop models from physical principles and system specifications, which often require extraordinary effort and expertise. On the other hand, purely data-driven approaches employ *black-box* modeling, which learns models purely from data without making any prior physical assumptions, relying on ML techniques such as neural networks and regression trees (RT). While *gray-box* modeling and physics-informed machine learning (PIML) both aim to bridge the gap between the white-box and black-box modeling paradigms by integrating physical laws into models, they take different approaches. *Gray-box* modeling starts from the same physical principles used in white-box modeling that are subsequently simplified to obtain a reduced-order model structure, which can be used to fit data to identify its parameters. Therefore the *gray-box* approach still requires significant expert knowledge and often ignores nonlinear phenomena, causing accuracy loss.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Physics-informed learning for system identification", "weight": 1.0} -->

On the other hand, \\AcPIML starts from the black-box modeling end and embeds prior knowledge of the system's physics into ML methods to yield models that are more interpretable, robust, accurate, and physically consistent for generalization tasks while maintaining the relative ease of use of *black-box* ML methods. This section reviews the main PIML approaches for incorporating physics into the data-driven modeling of dynamical systems. Namely, physics-informed model architecture, physics-informed loss function design, or a combination of the two.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A1 Structural priors in discrete-time models", "weight": 1.0} -->

Discrete-time dynamical models are represented by a general class of state-space models (SSM) given as

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A1 Structural priors in discrete-time models", "weight": 1.0} -->

with $x_{k} \in {\mathbb{R}}^{n_{x}}$ and $u_{k} \in {\mathbb{R}}^{n_{u}}$ being system states and control inputs, respectively. Most of the structural PIML approaches are concerned with designing the functional form of to offer increased expressivity compared to classical linear SSM while satisfying desired properties.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A1 Structural priors in discrete-time models", "weight": 1.0} -->

Recent examples include neural SSM, deep Koopman models, Hammerstein-Wiener neural models, graph neural network-based (GNN) time-stepper models, or SINDY-type methods based on sparse regression of candidate basis functions. Further examples include architectures such as Non-Autonomous Input-Output Stable Nets (NAIS-Nets) with guaranteed asymptotic stability of its forward pass dynamics based on stable matrix factorization of the state dynamics, joint learning of the Koopman model representation and state observer while ensuring observability, or so-called Gumbel Graph Networks (GGN) for modeling network dynamics. While authors in introduced physically consistent NN inspired by resistance-capacitance (RC) networks applied to modeling building thermal dynamics.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A2 Structural priors in continuous-time models", "weight": 1.0} -->

Continuous-time models are, in general, represented by a set of ordinary differential equations (ODE) given as

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A2 Structural priors in continuous-time models", "weight": 1.0} -->

with $\mathbf{x} \in {\mathbb{R}}^{n_{x}}$ and $\mathbf{u} \in {\mathbb{R}}^{n_{u}}$ being system states and control inputs, respectively. Neural ODEs have been proposed as black-box counterparts to white-box ODEs for data-driven modeling of dynamical systems. In NODEs, the right-hand side (RHS) of the differential equation is approximated by deep neural network $NN{(\mathbf{x},\theta)}$ with trainable parameters $\theta$. However, purely black-box NODEs may require prohibitively large training data and may struggle with generalization and physical laws. Researchers have been looking at ways to design the structure of the RHS in to balance conflicting criteria such as the expressivity of black-box models and the physical consistency of white-box models.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A2 Structural priors in continuous-time models", "weight": 1.0} -->

Examples include incorporated stability-promoting priors in NODEs via spectral element method, multiple-shooting integration schemes, neural delay differential euquations, or extensions supporting uncertainty quantification (UQ) such as Bayesian NODEs, stochastic NODEs, or jump stochastic NODEs capable of handling discrete events. Most recently, universal differential equations (UDE) have been proposed as an extension to NODEs to allow for a systematic combination of white-box components and black-box components. Specific examples of PIML structured continuous models include the use of UDEs for modeling networked dynamical systems, or continuous graph neural networks (CGNNs) also called graph neural ordinary differential equations (GDEs). Related approaches include energy-based model architectures such as Hamiltonian or Lagrangian neural networks, and their various extensions such as graph Hamiltonian neural networks (HNN), Hamiltonian dynamics with dissipative forces, HNN with explicit constraints, or non-canonical Hamiltonian systems. Such approaches have also been extended to learn dynamics of rigid body systems with contacts and collisions or to learn Lagrangian dynamics from high-dimensional video data. Others have proposed jointly learning Neural Lyapunov functions together with the forward dynamics model.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A2 Structural priors in continuous-time models", "weight": 1.0} -->

The main advantage of these energy-based approaches is that they can satisfy conservation laws or enforce properties such as stability or dissipativity by design.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-A3 Matrix factorizations", "weight": 1.0} -->

Linear algebra components are ubiquitous in machine learning, including weights in neural networks, operators such as Koopman or Perron-Frobenius, or Jacobian matrices of differential equations. Many matrix factorization methods exist for designing desired properties such as sparsity, symmetry, positive definiteness, eigenvalue placement, or invertibility. Naturally, researchers have exploited various matrix factorizations in weights of deep neural networks, with examples including Perron-Frobenius, orthogonal, spectral, symplectic, anti-symmetric, Gershgorin disc, and Schur Decomposition weights. Let's consider spectral factorization as an example. In this approach, the weight matrix $\mathbf{W}$ is parametrized by the components of singular value decomposition (SVD) method as follows,

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-A3 Matrix factorizations", "weight": 1.0} -->

Where $\mathbf{\Sigma}$ is a matrix of singular values, $\lambda_{\text{min}}$ and $\lambda_{\text{max}}$ represent lower and upper bounds for singular values, $\sigma$ is a sigmoid activation function, $s$ is a vector of trainable singular value parameters, and $\mathbf{U}$ and $\mathbf{V}$ are trainable orthogonal matrices that can be either designed via Householder reflectors or via soft constraint penalties. Authors in used the matrix factorizations to enforce dissipativity in neural SSM for modeling building thermal dynamics.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-A4 PIML loss functions", "weight": 1.0} -->

This approach incorporates physics through *learning biases* by imposing appropriate penalties during learning. In its general form, the composite physics-informed loss function $\mathcal{L}$ is defined as

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-A4 PIML loss functions", "weight": 1.0} -->

where $\ell_{\text{data}}^{i}$ represents $n$ number of data-driven objective terms, $\ell_{\text{physics}}^{j}$ define $m$ number of physics-based regularization terms.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-A4 PIML loss functions", "weight": 1.0} -->

Examples include using soft penalties on eigenvalues or singular values of the neural network weights to promote stability, promoting boundedness, and smoothness, using penalties to regularize black-box GNN components, regularizing error and stiffness estimates in NODEs for improved accuracy and speed, and penalizing the violations of the Lyapunov stability conditions as additional loss term in training NODEs. Others have proposed Jacobian regularization for promoting stability, or using surrogate loss functions for faster training of NODEs.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-A5 Case Study: Incorporating physics in the model via structural priors", "weight": 1.0} -->

This case study is adopted from and demonstrates the use of universal differential equations (UDE) for data-driven modeling of networked dynamical systems. The method illustrated in Fig. 1.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-A5 Case Study: Incorporating physics in the model via structural priors", "weight": 1.0} -->

Specifically, the UDE model used in is given as follows,

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-A5 Case Study: Incorporating physics in the model via structural priors", "weight": 1.0} -->

In general, the gradients of $F{(x;\Theta)}$ can be computed in two ways via the adjoint sensitivity method as used in NODE or via automatic differentiation of the computational graph of the unrolled ODE solver. The loss function is formulated as regularized mean squared error (MSE) between predictions and measurements, given as,

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-A5 Case Study: Incorporating physics in the model via structural priors", "weight": 1.0} -->

where $\mathbf{X}$ and $\hat{\mathbf{X}}$ are measured and predicted state trajectories, respectively. Scalar $m$ represents a number of samples. The second term represents $\ell_{1}$ penalty for promoting sparsity in the adjacency matrix $\mathbf{A}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-A5 Case Study: Incorporating physics in the model via structural priors", "weight": 1.0} -->

The authors in demonstrate the utility of this UDE modeling approach in a case study with coupled nonlinear oscillators. The benefit of the UDE model in the form is improved generalization and interoperability, as opposed to purely black-box NODE. This is because the structure of is closer to the governing physics of a general class of networked systems. To demonstrate their utility, the authors deploy the trained models on networked systems with never-before-seen topology. Fig. 2 compares the phase portraits and time series of the never-before-seen system against the predictions generated by the UDE model 5 trained on data from a networked system with different topology. What is being demonstrated are the generalization capabilities of the UDE model 5 to qualitatively reproduce physically plausible transient behavior, including the reconstruction of limit cycle attractors outside of the distribution of the training data.

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-B Physics-informed learning for control", "weight": 1.0} -->

PIML models have been widely used in model-based control methods, such as model predictive control (MPC) or model-based reinforcement learning (RL). This is typically done by combining physics-based priors with various regression methods to improve the control performance. Subsequently, with the spread of learning methods embedded with uncertainty quantification (UQ) measures, robust and stochastic model-based controllers have been developed to exploit the uncertainty information provided by these PIML models. Including UQ methods makes the controller cautious and is of great significance where only a limited amount of data is available. More recently, the use of PIML has been extended to different areas such as learning control Lyapunov functions, tuning model-based controllers, designing dual control strategies, developing safe control frameworks, and learning explicit control policies. PIML has also found applications in differentiable programming-based methods, which allows the designer to embed physical models and constraints while training a controller using automatic differentiation-based (AD) solvers, e.g., with physics-informed priors in actor-critics and model-based RL methods.

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-B1 PIML dynamics models for MPC", "weight": 1.0} -->

Data-driven models have been widely used in MPC; see for a comprehensive review of these methods up to 2020. With recent advances, many approaches have been proposed for incorporating PIML and physical priors into MPC. These methods employ learned PIML dynamic models (Section II-A) in the MPC optimization formulation, therefore implicitly leveraging physical priors through the models. Authors in used structured neural SSM in MPC to control the nonlinear behavior of a robotic hand in cutting tasks. In a physics-informed NN is used with MPC in order to control a robotic arm. Others have demonstrated the utility of using the sparse identification of nonlinear dynamics (SINDY) method for learning models for MPC, in the so-called SINDY-MPC framework. The use of ML models in MPC with guarantees can be traced back to. The authors propose a robust control method that uses two models: the first is a simple physics-based linear model that accounts for the safety of the system used to ensure constraint satisfaction, while the second is an ML model used to maximize the performance of the controller.

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-B1 PIML dynamics models for MPC", "weight": 1.0} -->

A different approach is presented, where a Gaussian process (GP) is used to learn the error dynamics to improve the physics-based model and hence the controller performance. Another MPC algorithm that uses kernel-based methods is presented. While the work in demonstrates the utility of even a simple physics-informed ARMAX model for building control tasks using MPC.

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-B2 Learning Lyapunov and Barrier functions", "weight": 1.0} -->

(Control) Lyapunov functions are crucial tools for determining the stability properties of dynamical systems, quantifying the domain of attraction and the robustness to perturbation, designing controllers, or designing terminal ingredients for MPC. However, methods for synthesizing Lyapunov functions in closed-form for nonlinear dynamical systems, even with known models, are generally not available. Early approaches for learning Lyapunov functions with NNs date back to the 90s. Recently, different authors introduced neural Lyapunov functions, representing neural architectures that satisfy Lyapunov function properties by design. Subsequently, authors in have used these neural Lyapunov functions as verification tools for safe learning-based controllers, while used neural Lyapunov function for online tuning of MPC parameters, and in neural Lyapunov function was trained in conjunction with neural control policy. Another example is, where NNs are employed to learn compositional Lyapunov functions. This work takes inspiration from recent methods that solve high-dimensional PDEs using NNs by exploiting suitable structural properties.

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-B2 Learning Lyapunov and Barrier functions", "weight": 1.0} -->

As Lyapunov functions can also be represented by PDEs, PIML methods for learning PDEs can also be used to learn Lyapunov functions. Control barrier functions (CBF) recently became a very popular computationally efficient method for safe learning-based control. However, similarly to Lyapunov functions, CBFs are in general, hard to design analytically for general nonlinear dynamical systems. To alleviate this problem, different authors have proposed learning CBFs from data. In, use NNs to approximate the signed distance functions and subsequently use second-order cone programming to synthesize the control policy. Authors in utilize imitation learning to learn CBFs from expert demonstrations of safe trajectories. While others present architectures for constructing neural barrier functions for multi-agent control, and robust neural Lyapunov-barrier functions for safe nonlinear control.

<!-- chunk {"id": "body-0033", "role": "body", "section": "II-B3 Differentiable Control", "weight": 1.0} -->

These methods leverage automatic differentiation (AD) for computing gradients of the physics model or optimal control problem that can be used as part of the learning algorithm. An example is to use AD for computing the backward gradients of the underlying MPC optimization problem. In principle, this can be done in two ways, by differentiating the KKT conditions constructed analytically or by unrolling the computational graph of the MPC problem. The advantage of the methods based on differentiable programming (DP) is that they allow for end-to-end training of different components of the optimal control problem. Thanks to its versatility, this method has been used to learn system dynamical models, weighting factors of the objective functions, neural control policies, or safety filters based on differentiable projections, and differentiable control barrier function. Most recent applications of differentiable control include autonomous vehicles, robotics, building control, traffic flow, epidemic processes, or visuomotor control via differentiable rendering. Naturally, physical priors can be incorporated into the MPC formulation through the system model, which will be taken into account when the optimization problem is differentiated.

<!-- chunk {"id": "body-0034", "role": "body", "section": "II-B3 Differentiable Control", "weight": 1.0} -->

Most recently, several differentiable optimization and control libraries have emerged in the open-source domain The DP approach has also been used to develop differentiable physics models to control partial differential equations (PDEs).

<!-- chunk {"id": "body-0035", "role": "body", "section": "II-B4 \\\\AcPIML for safe data-driven control", "weight": 1.0} -->

Another use of PIML models in combination with control-like algorithms is in safety frameworks. Given a safety-critical system, i.e., a dynamical system subject to state and input constraints, a safety framework can certify whether a proposed control input is safe to apply or not. Whenever a proposed input is unsafe, the safety framework can propose an alternative safe control input, which usually is as close as possible to the proposed one. For instance, present safety frameworks that use an MPC like structure to determine the input that satisfies input and state constraints and is as close as possible to the proposed potentially unsafe input. Safety frameworks are also known under other names such as active set reachability, Safety Handling Exploration with Risk Perception Algorithm (SHERPA), and model predictive safety filter. Other approaches use control barrier functions and reachability analysis to ensure safety. A unified approach that brings predictive safety filters and control barrier functions, called predictive control barrier functions, has been recently presented

<!-- chunk {"id": "body-0036", "role": "body", "section": "II-B4 \\\\AcPIML for safe data-driven control", "weight": 1.0} -->

Safety frameworks have also been proposed for learning-based control, where machine learning (ML) is used to learn either the system model or the control law. uses an MILP formulation to train NN-based controllers to satisfy input constraints, safety constraints, and stability conditions. uses differentiable projections to enforce Lyapunov stability conditions while minimizing a performance objective-based loss function (e.g., LQR) during training of a NN-based control law. Cautious control methods employ the uncertainty of the learned model to ensure safety constraints and become less conservative when the model is updated.

<!-- chunk {"id": "body-0037", "role": "body", "section": "II-B5 Physics-informed RL", "weight": 1.0} -->

PIML has been used in RL to improve its accuracy and physical consistency. Model-based reinforcement learning methods rely on a model of the environment and its dynamics with which the agent interacts. The models can be generated via high-fidelity physics-based simulations or learned from data. Deep-RL methods employ NNs to generate data-driven models. Approaches similar to those presented in the MPC section can be used to ensure physically consistent models. For example, uses a physically consistent NN to learn a dynamical model of a building, which is then used with a deep RL agent. In, a model-based policy search method, called PILCO, is developed where prior physics knowledge can be introduced in a GP model. Physics-informed RL schemes informed by the underlying dynamics have been employed to tackle aircraft conflict resolution problems and power system optimization problems. Recent works in provide a systematic framework for using RL to tune the parameters of optimization-based MPC policies. This RL-MPC framework combines the advantages of both approaches, namely the flexibility of RL with constraints satisfaction and stability of MPC. It has recently found applications in building energy system control.

<!-- chunk {"id": "body-0038", "role": "body", "section": "II-B6 Case study: Physics-informed safety filters for data-driven control", "weight": 1.0} -->

The work shows how to deploy RL algorithms on safety-critical systems, i.e., systems subject to state and input constraints, without violating constraints. The proposed approach makes use of predictive safety filters, namely, an optimization-based algorithm that receives the proposed control input and decides, based on the current system state, if it can be safely applied to the real system or if it has to be modified otherwise. Given a dynamical system of the form, the predictive safety filter solves each time-step the following optimization problem,

<!-- chunk {"id": "body-0039", "role": "body", "section": "II-B6 Case study: Physics-informed safety filters for data-driven control", "weight": 1.0} -->

where $u_{L}$ is the input proposed by a potentially unsafe controller, e.g., an RL algorithm and $\mathcal{S}^{t}$ is a terminal invariant set for the dynamical system $f{(x_{k},u_{k})}$. The predictive safety filter minimizes the difference between the proposed input and a safe input in order to be as less invasive as possible. The input $u_{k}$ is then applied. While the aforementioned approach relies on a perfect knowledge of the system dynamics, in practice a perfect model is never available. The predictive safety filter can deal with the uncertain system by exploiting robust and stochastic model predictive control techniques. A parametric model $x_{k + 1} = {f{(x_{k},u_{k},\theta)}}$ is considered where $\theta$ is an unknown parameter vector that is either bounded or has a known prior distribution $p{(\theta)}$ with mean ${\mathbb{E}}{\lbrack\theta\rbrack}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "II-B6 Case study: Physics-informed safety filters for data-driven control", "weight": 1.0} -->

In the aforementioned paper, the safety filter is applied to the swing-up of an inverted pendulum and the control of a quad-copter. In both cases, unsafe controllers are employed and the safety filter demonstrates how it is possible to satisfy constraints.

<!-- chunk {"id": "body-0041", "role": "body", "section": "II-C Analysis and verification of ML models", "weight": 1.0} -->

In addition to system identification and control design, PIML has been incorporated into the analysis and verification of dynamical systems. Firstly, consider a learning structure, (e.g., NN, GP) on which PIML methods typically rely. Properties of these structures, such as input-to-state stability, input-output bounds, and estimation of Lipschitz constants, are important to determine how these structures behave in a closed-loop setting. Secondly, learned system dynamics would ideally have inherent physical properties, e.g., passivity, stability, and invariance, from the physical systems they are approximating. Guarantees that such physical properties hold can be beneficial for future control design in addition to ensuring a better representation of the physical system itself. Finally, learning-based control policies may lack guarantees of closed-loop stability or invariance. Verification methods, including sampling-based and reachability, can be used to guarantee such desirable properties of the closed-loop system. In the following, we survey the literature with respect to analysis and verification methods developed for PIML.

<!-- chunk {"id": "body-0042", "role": "body", "section": "II-C1 Analysis and verification of learned system dynamics", "weight": 1.0} -->

These are methods for analyzing and verifying properties of learned models of dynamical systems in the open-loop setting. They can be categorized by the class of system properties addressed as follows.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Stability", "weight": 1.0} -->

The stability and attractors of recurrent neural networks have been studied in continuous time. Authors in study Lyapunov spectra and Lyapunov exponents of RNNs. Authors in empirically study stability of deep neural architectures in the context of solving forward-backward stochastic differential equations. analyzes the dissipativity of autonomous neural dynamics. proposes a method for synthesis of Lyapunov NNs while providing formal guarantees-using satisfiability modulo theories (SMT). defines deep neural network (DNN) structure to approximate compositional Lyapunov functions for a system where the approximation error is dependent on the number of neurons in the network. uses mixed-integer programming in a sampling-based Lyapunov function verification method for piece-wise linear NN approximations of nonlinear autonomous systems for estimating their region of attraction. uses Koopman operator theory and sample-based methods to learn a neural network-based Lyapunov function and region of attraction of a given open-loop system. uses GP-based approximate dynamic programming with a sample-based method to learn a Lyapunov function and region of attraction of an open loop system.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Stability", "weight": 1.0} -->

analyzes the Input-to-State (ISS) stability of long short-term memory (LSTM) networks by recasting them in the state space form. The authors in use contraction analysis to design an implicit model structure that allows for a convex parameterization of stable RNN models. uses non-Euclidean contraction theory to establish well-posedness, contraction, and $l_{\infty}$-Lipschitz properties of implicit NNs.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Lipschitz properties", "weight": 1.0} -->

shows that determining the Lipschitz constant of a NN is an NP-hard problem and proposes algorithms to estimate the Lipschitz constant. Methods for data-driven Lipschitz estimation for controller design and safe policy iteration in ADP are proposed. In, the authors propose a method for training deep feedforward NNs with bounded Lipschitz constants. poses the Lipschitz constant estimation problem for deep neural networks as a semidefinite program (SDP). shows how to train continuous-time RNNs with constrained Lipschitz constants to guarantee stability. develops neural Lipschitz observers with guaranteed performance.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Robustness and other safety properties", "weight": 1.0} -->

The authors in use the data Jacobian matrix to analyze the behavior of deep neural networks by means of their singular values. develops an analyzer for deep convolutional networks with ReLU activations based on an over-approximation that can guarantee robustness. proposes a method of verification for binarized NNs using existing boolean satisfiability solvers, which is tested for adversarial robustness to $l_{\infty}$ perturbations. uses mixed-integer linear programming (MILP) formulations to analyze robustness of NNs.

<!-- chunk {"id": "body-0047", "role": "body", "section": "II-C2 Analysis and verification of learned control policies", "weight": 1.0} -->

These methods analyze and verify properties of learned control policies in the closed-loop setting. They are categorized by the considered class of properties as follows.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Stability", "weight": 1.0} -->

provides deterministic stability guarantees for learning-based MPC (LBMPC) based on linear state space models. The authors in propose sampling-based probabilistic performance guarantees for approximate MPC policies based on the Hoeffding inequality. uses semidefinite programming to certify stability for model-based RL policies. uses Lyapunov stability verification to certify model-based RL policies. uses GP to estimate the region of attraction of a closed-loop system. Recently, uses sample-based $\delta$-covers of system domains to ensure input-to-state stability to a set of a closed-loop system when an NN is used as a state estimator or a closed-loop control law. develops a neural contraction metric, i.e., an NN approximation of a contraction metric, which, coupled with a learning-based controller, ensures exponential convergence to a target trajectory. guarantees stability by combining the worst-case approximation error of the NN controller with its Lipschitz constant, utilizing an MILP framework. proposes a framework for the stability verification of MILP representable control policies.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Stability", "weight": 1.0} -->

simultaneously learns an NN controller and Lyapunov function, guided by MILP stability verification, which either verifies stability or gives counter-examples that can help improve the candidate controller and the Lyapunov function. learns an MPC policy and a "dual policy," which enables them to keep a check on the approximated MPC's optimality online during the control process to filter out suboptimal control inputs and invoke a backup controller with a bounded probability.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Invariance and other safety properties", "weight": 1.0} -->

uses constrained zonotopes and reachability analysis to determine reachable sets for safety verification of NN controllers. uses sampled trajectories of a closed-loop system to learn the control barrier function, which can be parameterized by an NN and can ensure invariance of the safe set. uses an MILP formulation to perform an output range analysis of a trained NN controller to guarantee constraint satisfaction and asymptotic stability of the NN controller.

<!-- chunk {"id": "body-0051", "role": "body", "section": "II-C3 Case study: Verification of a NN controller for a DC-DC power converter", "weight": 1.0} -->

The following section provides a case study on the verification of a NN controller for a DC-DC power converter. To carry out this verification, we employ the EVANQP framework, developed, which utilizes MILPs as its underlying verification technique. By utilizing this framework, we not only demonstrate the closed-loop stability of the NN policy, but we can also validate the satisfaction of constraints in closed-loop operation. The example is adopted from \[160, Section V\].

<!-- chunk {"id": "body-0052", "role": "body", "section": "II-C3 Case study: Verification of a NN controller for a DC-DC power converter", "weight": 1.0} -->

The use of neural network (NN) policies in power converter applications is primarily motivated by the desire to achieve comparable performance to that of an optimal MPC policy while requiring lower computational complexity and memory. Optimal MPC policies are often too computationally demanding to be run in real-time on low-cost microprocessor hardware, making NN policies an attractive alternative. Despite the successful deployment of an NN policy on real hardware, their approach lacks guarantees of stability and constraint satisfaction. In the following, we address these shortcomings. We will focus on the approach described in where the baseline policy $\psi_{1}{( \cdot )}$ represented by a robust MPC is approximated by a NN policy $\psi_{2}{( \cdot )}$. Specifically, we consider the robust Tube MPC approach proposed, which is robust against additive input disturbances in the set ${\mathbb{W}} = \left\{ {w \in {\mathbb{R}}^{m}} \middle| {{\| w\|}_{\infty} \leq \hat{\gamma}} \right\}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "II-C3 Case study: Verification of a NN controller for a DC-DC power converter", "weight": 1.0} -->

By verifying that the NN policy has a worst-case approximation error,

<!-- chunk {"id": "body-0054", "role": "body", "section": "II-C3 Case study: Verification of a NN controller for a DC-DC power converter", "weight": 1.0} -->

over a bounded polytopic set $\mathbb{X}$ that is smaller than $\hat{\gamma}$, we can prove that the NN policy $\psi_{2}{( \cdot )}$ is asymptotically stable in closed-loop and satisfies constraints on the feasible region of the robust MPC policy $\psi_{1}{( \cdot )}$ \[160, Theorem 1\]. Notably, this is achieved by reformulating as a MILP, with the NN policy and the optimal solution map of the robust MPC scheme as MILP constraints. A wide range of candidate policies including ReLU NNs, optimal solution maps of parametric QPs, and MPC policies can be exactly represented using MILP constraints. We refer to such functions as MILP-representable, as they can be expressed exactly using linear equality and inequality constraints with both continuous and binary decision variables. The MILP-representable functions are piecewise linear in nature, enabling their exact representation using MILP constraints.

<!-- chunk {"id": "body-0055", "role": "body", "section": "II-C3 Case study: Verification of a NN controller for a DC-DC power converter", "weight": 1.0} -->

The model of the DC-DC converter is linearized and discretized, giving us the following two-state $x = {(i_{L},v_{O})}$ (current and voltage), and one-input (duty cycle) linear system

<!-- chunk {"id": "body-0056", "role": "body", "section": "II-C3 Case study: Verification of a NN controller for a DC-DC power converter", "weight": 1.0} -->

For the robust MPC we assume the uncertain dynamics

<!-- chunk {"id": "body-0057", "role": "body", "section": "II-C3 Case study: Verification of a NN controller for a DC-DC power converter", "weight": 1.0} -->

The control law is then given by ${\psi_{1}{(x)}} = {{K{({x - {z_{0}^{\star}{(x)}}})}} + {v_{0}^{\star}{(x)}}}$. To approximate the robust Tube MPC, we employ a neural network (NN) with 2 hidden layers and 50 neurons each. A saturation layer is added at the end to ensure that the input is clipped between -1 and 1. We use 5000 samples of the Tube MPC uniformly distributed in the feasible region for training the NN, following standard techniques. The NN controller learns an approximation of the MPC policy by minimizing a least-squares loss function. The resulting NN controller and the original Tube MPC can be visualized in Figure 3.

<!-- chunk {"id": "body-0058", "role": "body", "section": "II-C3 Case study: Verification of a NN controller for a DC-DC power converter", "weight": 1.0} -->

We employ the EVANQP framework to describe the MPC formulation and NN controller and solve the resulting Mixed-Integer Linear Program (MILP) to determine the worst-case approximation error. Our analysis yields a value of $\gamma = 0.073$. As we designed our controller to be robust for input perturbations with a maximum magnitude of $0.1$, our results demonstrate that the NN controller satisfies constraints and converges asymptotically to the steady-state.

<!-- chunk {"id": "body-0059", "role": "body", "section": "II-D Learning from physics-informed digital twin simulations", "weight": 1.0} -->

Advancements in computing and the wide availability of modeling toolkits have yielded high-fidelity simulation software (an essential component of so-called "digital twins" ) across a range of domains. Simulation has become a critical tool for researchers to perform experiments in a scalable, safe, and repeatable manner. Data generated from digital twins can complement, or offer a powerful alternative to field experiments, which are typically time-consuming, and often require extensive guardrails to ensure expensive equipment/personnel are not subject to harm, or are difficult to repeat. Some high-fidelity simulators include Modelica (cyber-physical systems, building energy systems ), CESM (climate models ), STK (spacecraft ), OpenFOAM (fluid flow ), and ChainQueen (soft robotics ), to name a few.

<!-- chunk {"id": "body-0060", "role": "body", "section": "II-D Learning from physics-informed digital twin simulations", "weight": 1.0} -->

In the prior section on physics-informed system identification, data was assumed to have been obtained from the system under consideration, and an incomplete mathematical representation of the system dynamics is available from domain knowledge (or 'physics'). In this subsection, the 'physics' is integrated within the data via the data-generating source: the high-fidelity simulator. However, because the simulators comprise software modules that require high modeling complexity and are typically strongly interconnected to one another, directly considering analytical forms of these simulators is unwieldy and impractical. It is generally easier to construct machine learning tools that can directly use data generated by the simulators.

<!-- chunk {"id": "body-0061", "role": "body", "section": "II-D1 Controller design using simulation data", "weight": 1.0} -->

To ensure that a high-fidelity simulator can be effectively utilized for controller design tasks, it must first be calibrated with real-world data generated by the system of interest. This calibration step is important for ensuring the underlying assumptions and parameter values have been adequately selected to best mimic the true system. However, the complex representation of most high-fidelity simulators implies that the model calibration step can be challenging to solve, especially compared to alternative black-box modeling approaches (e.g., deep neural networks) that do not require prior physical knowledge. A natural question arising from this comparison is: Why not directly work with standard machine learning algorithms and forego the high-fidelity simulator altogether? In the context of real-world engineering systems, the answer almost always boils down to a lack of accurate system data. For example, deep learning methodologies have become mainstream solutions in a variety of important applications, such as natural language processing and image classification; however, they often require massive amounts of high-quality labeled training data to surpass human performance.

<!-- chunk {"id": "body-0062", "role": "body", "section": "II-D1 Controller design using simulation data", "weight": 1.0} -->

A key advantage of high-fidelity simulators is that they can be calibrated using substantially less training data, which is a direct consequence of the constraints imposed by the underlying first-principles models. Once calibrated, the simulator can then be treated as a data-generation source that can be more confidently extrapolated outside of observed training instances. This data generation feature is useful for building control-relevant (or reduced-order) models, which are critical components of modern model-based control algorithms, such as MPC, that can handle constrained nonlinear systems with strong multivariate interactions.

<!-- chunk {"id": "body-0063", "role": "body", "section": "II-D1 Controller design using simulation data", "weight": 1.0} -->

No matter the selected structure, a controller will still depend on design (or tuning) parameters that can strongly affect closed-loop performance and safety. Historically, these tuning parameters have been selected using a combination of heuristics and/or trial-and-error experimentation on the true system. To reduce the required testing and validation time, it has been recently proposed to perform controller tuning using the high-fidelity simulator. However, the tuning process is not straightforward due to the computationally expensive nature of high-fidelity simulators. As such, there has also been significant interest in the development of efficient data-driven automated calibration (or auto-tuning) strategies. In particular, Bayesian optimization (BO) has emerged as a powerful approach for handling these types of auto-tuning problems due to its ability to handle expensive black-box functions corrupted by random noise. Several recent works have demonstrated the promise of BO for auto-tuning of MPC and other complex control structures. Many interesting extensions of BO have also been pursued in the context of auto-tuning, including multi-objective and robust formulations.

<!-- chunk {"id": "body-0064", "role": "body", "section": "II-D2 Improving generalization of learners via simulations", "weight": 1.0} -->

A unique opportunity afforded to us by the use of physics-informed simulation tools comes from the ability to generate useful data for analysis and design. This generation phase is typically not assumed in most current PIML research, where the more standard assumption is that data and domain knowledge pertaining to the 'target' system under consideration is available. Contrarily, digital twins comprise parameterized components whose physical parameters or physics-informed structure can be modified in software to generate data from multiple 'source' systems that are similar to the target system but not necessarily identical. The implication in modeling and control is that we can use leverage this multi-source dataset to evaluate performance on a range of similar dynamical systems and embed this data into the design pipeline for a target system from which only a few data points are available. Two classes of ML algorithms are naturally suited to learning from multi-source data: (i) meta-learning (also referred to as few-shot learning) and (ii) transfer learning.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Meta-learning", "weight": 1.0} -->

In meta-learning, two objective functions are typically used in the training phase: an outer-loop loss function for learning commonalities among the multi-source systems and an inner-loop loss function for quickly adapting to a new system with minimal data. At inference, the outer-loop parameters are used to initialize the network, and a few inner-loop iterations are deemed sufficient for adaptation to the target system. Importantly, the learner structure does not change for the inference task, and the meta-learning algorithm learns to optimize the learning process itself; that is, for a classification problem, the meta-learner may not infer a classification output, but instead may infer a set of hyper-parameters for a classifier network such as loss function parameters or parameters relating to the neural architecture itself. GP models have been used recently in order to meta-learn predictive models for MPC by using dynamic trajectory data from similar systems, and neural networks have been used to meta-learn adaptive control policies in for robotics. Some meta-learning algorithms do not require re-training or bi-level optimization for adaptation.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Meta-learning", "weight": 1.0} -->

Instead, they adapt based on contextualization; that is, with the same inputs, the inference changes due to contextual inputs additionally provided to the network. These context-based meta-learners, such as neural processes and deep kernel networks, have also been investigated recently for parameter learning using physics-informed simulators of building energy systems.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Transfer and multi-fidelity learning", "weight": 1.0} -->

Conversely, transfer learning relies on learning good representations from the multi-source dataset. At inference, the final network architecture is different from the network that was pre-trained, with the head of the network being inherited from the trained network, while the penultimate layers are altered to fit the learning task on the target system. Furthermore, the task performed by both the network architectures, e.g., classification, are identical. So far, the utility of transfer learning in modeling and control has mainly been demonstrated in energy systems where control policies or neural network-based surrogate thermal dynamics models are constructed by using simulations of buildings situated in various climate zones and exhibiting a wide range of architectures.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Transfer and multi-fidelity learning", "weight": 1.0} -->

A generalized version of the transfer learning problem also arises in controller auto-tuning. Although auto-tuning strategies applied to the high-fidelity simulator can compensate for the error between the control-relevant model and the simulator, they implicitly assume the error between the simulator and the true system is negligible, which is not always the case in practice. One way to address this additional source of error is through the framework of multi-fidelity optimization wherein we assume access to a family of information sources controlled by a collection of "fidelity" parameters that can be generally continuous or discrete. In the simplest case, we would have one binary fidelity parameter that denotes two distinct but correlated levels, i.e., the simulator and the true system. Due to the general structure of the BO framework, several multi-fidelity BO methods have been developed in the literature, with some being applied directly to the controller auto-tuning problem. The main advantage of these types of multi-fidelity optimization methods is their ability to efficiently reconcile discrepancies between the high-fidelity simulator and the true system, which can allow for a significant reduction in the amount of testing required on the true system of interest.

<!-- chunk {"id": "body-0069", "role": "body", "section": "II-D3 Sim2Real in Reinforcement Learning", "weight": 1.0} -->

Model-free controllers, e.g. a class of (deep) reinforcement learning algorithms can potentially obtain near-optimal control policies without the need for a mathematical model. This is typically done by the control agent interacting with its environment (or plant) and learning to associate the states to advantageous control actions. The exploration-exploitation trade-off governs this interaction: in order for the agent to gather new knowledge, it needs to explore unknown effects of its actions by choosing them, e.g., randomly at times. This feature has three drawbacks for controlling real-world systems. For one, for large state-space systems, the agent may never see all possible states and/or all possible state-action combinations, especially those that may occur infrequently. Second, the amount of data needed for convergence may be large, and consequently the learning times prohibitively long. Third, the agent may choose actions that violate safety constraints, which may not be permissible in certain plants.

<!-- chunk {"id": "body-0070", "role": "body", "section": "II-D3 Sim2Real in Reinforcement Learning", "weight": 1.0} -->

To overcome this issue the sim2real paradigm has been introduced, i.e., the notion that the agent is (pre-)trained in a physically accurate simulator before the deployment on the real system. This way, the agent can be provided with the equivalent of decades of experience and a large variety of potential states. The sim2real paradigm has been successfully explored by developing a variety of simulators for robotics and general purpose physics, and demonstrating applications mainly in robotics and automotive. Of course, the physics fidelity of the simulators can determine the success and quality of the subsequent deployment, and also its applicability for sim2real. If it is computationally too expensive to run extensive simulation models, they are not suitable to be used in pre-training learning controllers. Here, PIML approaches can be very advantageous in providing physically accurate, yet computationally efficient environments, which can greatly improve the quality of the learning process.

<!-- chunk {"id": "body-0071", "role": "body", "section": "II-E Case Study: Violation-aware Bayesian optimization for energy consumption minimization of HVAC with constraints", "weight": 1.0} -->

We consider the problem of safely tuning set-points of an HVAC system as introduced, also referred to as a vapor compression system (VCS). A VCS typically consists of a compressor, a condenser, an expansion valve, and an evaporator. Physics-based models of these systems can be formulated as large sets of nonlinear differential-algebraic equations (DAE) to simulate VCS dynamics. To inject realistic refrigerant dynamics and fluid flow, these models contain software blocks that exhibit significant numerical complexity. This motivates directly using data from VCS digital twin simulations to estimate energy consumption under different operating conditions, to assign set-points to the VCS actuators using data-driven, black-box optimization methods such as Bayesian optimization. A high-fidelity digital twin of the VCS was constructed using Modelica; see Fig. 4. Physics-based models of the compressor, expansion valve, accumulator, and both heat exchangers were interconnected. The final DAE model comprises 12114 equations; further modeling details can be found.

<!-- chunk {"id": "body-0072", "role": "body", "section": "II-E Case Study: Violation-aware Bayesian optimization for energy consumption minimization of HVAC with constraints", "weight": 1.0} -->

Recklessly changing VCS actuator set-points can drive the system into operating modes that reduce the reliability or lifespan of the system. To avoid these harmful effects, one can add several constraints during the tuning process. One such constraint is the compressor discharge temperature; as high temperatures can result in the breakdown of refrigerant oils and increase wear and tear, shortening the product's lifespan. Furthermore, high temperatures are connected to high pressures, which may cause mechanical fatigue in refrigerant pipes. An advantage is that small constraint violations over a short period of time are acceptable. Authors in proposed a violation-aware Bayesian optimization (VABO) to minimize energy use in the VCS while trading off constraint violations. The feedback loop is closed from compressor frequency to room temperature, leaving the set of three tunable set points as the expansion valve position and the indoor/outdoor fan speeds. The effects of these set points on power and discharge temperature are not easy to model, and no simple closed-form representation exists.

<!-- chunk {"id": "body-0073", "role": "body", "section": "II-E Case Study: Violation-aware Bayesian optimization for energy consumption minimization of HVAC with constraints", "weight": 1.0} -->

Authors in report that the energy use induced by VABO decreases slightly faster than generic constrained BO (cBO) and significantly faster than safe BO. At the same time, the method manages the violation cost well under the violation cost budget. cBO incurs large discharge temperatures at many iterations because it makes large adjustments to the expansion valve position while maintaining the indoor fan speed at a low value, a combination that is not penalized during exploration. VABO reduces the energy by about $9\%$ compared to the most power-efficient initial safe set-points. Authors also observed that large discharge temperature violations are entirely possible without violation awareness, as demonstrated by cBO. Safe BO tends to waste a lot of evaluations to enlarge the safe set, which leads to slow convergence; conversely, VABO implicitly encodes the safe set exploration into the acquisition function and only enlarges the safe set when necessary for optimization, while keeping the violation risk small.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Challenges and Opportunities of PIML for Control", "weight": 1.0} -->

This section reflects on open challenges and opportunities of PIML methods from various perspectives, including data and prior knowledge requirements, computational demands, safety and performance guarantees, availability of software tools and learning materials, as well as new promising application domains.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Challenges and Opportunities of PIML for Control", "weight": 1.0} -->

Modeling of human behaviors in interactive human-autonomous systems (e.g., autonomous vehicle in mixed traffic). Autonomous system physics is known, but human reaction needs to be learned from real data to model human-in-the-loop systems at scale.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Challenges and Opportunities of PIML for Control", "weight": 1.0} -->

Modeling of high dimensional and distributed physics in multi-physics systems. An example includes combustion processes where physics is impossible to model compactly by first principles, but there may be good surrogate models that retain core physical properties.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Challenges and Opportunities of PIML for Control", "weight": 1.0} -->

Generation of structured PIML controllers for multi-component systems with awareness of interconnections of the sub-components. This would lead to improved interpretability and allow for the localization of failures.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Challenges and Opportunities of PIML for Control", "weight": 1.0} -->

Constructing surrogate PIML models for the hard-to-optimize physics-based optimization problems or cost functions. This could significantly speed up the solution of hard optimization problems using cheaper surrogates.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Challenges and Opportunities of PIML for Control", "weight": 1.0} -->

Synthesis of explicit model predictive control policies for large-scale systems leading to a significant reduction in online computational requirements. Thus allowing for the execution of complex control policies in applications with limited communication bandwidths and small sampling rates or enabling deployment on edge devices.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Challenges and Opportunities of PIML for Control", "weight": 1.0} -->

Providing safety and performance guarantees for a broad class of learning-based control methods. Particularly applicable to applications with time-varying dynamics that require online adaptive processes to cope with constant changes in a safe manner.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Challenges and Opportunities of PIML for Control", "weight": 1.0} -->

Dealing with sim2real gap and allowing for automated tuning of PIML controllers from simulation and experimental data.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Challenges and Opportunities of PIML for Control", "weight": 1.0} -->

Integration of multi-modal inputs into modern control systems. Examples include a combination of video and audio signals with physical measurements processed for downstream decision-making by advanced controls.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Challenges and Opportunities of PIML for Control", "weight": 1.0} -->

How to quantify the uncertainty and modeling errors for PIML-based models?

<!-- chunk {"id": "body-0084", "role": "body", "section": "Challenges and Opportunities of PIML for Control", "weight": 1.0} -->

How to quantify minimal data requirements for training PIML models and controllers?

<!-- chunk {"id": "body-0085", "role": "body", "section": "Challenges and Opportunities of PIML for Control", "weight": 1.0} -->

How to effectively select representative training data for sampling-based PIML approaches?

<!-- chunk {"id": "body-0086", "role": "body", "section": "Challenges and Opportunities of PIML for Control", "weight": 1.0} -->

How to automate the training and hyperparameter tuning process of PIML models?

<!-- chunk {"id": "body-0087", "role": "body", "section": "Challenges and Opportunities of PIML for Control", "weight": 1.0} -->

How to avoid training failures of PIML models getting stuck in local optima. Can we obtain convergence guarantees for certain classes of PIML models?

<!-- chunk {"id": "body-0088", "role": "body", "section": "Challenges and Opportunities of PIML for Control", "weight": 1.0} -->

How to guarantee stability and safety of a real-world system in closed-loop with PIML-based controllers in the presence of noise and plant-model mismatch?

<!-- chunk {"id": "body-0089", "role": "body", "section": "Challenges and Opportunities of PIML for Control", "weight": 1.0} -->

How can verification methods for PIML be scaled up for large-scale or networked systems?

<!-- chunk {"id": "body-0090", "role": "body", "section": "Challenges and Opportunities of PIML for Control", "weight": 1.0} -->

How to reduce the computational requirements of high-fidelity digital twins without sacrificing accuracy?

<!-- chunk {"id": "body-0091", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In the last two decades, the use of machine learning (ML) methods revolutionized a range of industries, from retail, advertisement, entertainment, healthcare, finance, digital arts, and social networks, to surveillance. Although highly diverse, these applications have some common denominators, which is that their ML systems are primarily designed for pattern recognition from multi-modal data sources. However, as we move towards real-world engineering systems with humans-in-the-loop, such as autonomous vehicles, collaborative robotics, process control of chemical plants, or power grid, the primary focus is steered toward optimization and control of these dynamical systems with guarantees of safe operation. In recent years, physics-informed machine learning (PIML) has emerged as a class of methods that systematically combine data-driven ML with physics-based modeling and numerical solvers from engineering.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Conclusions", "weight": 1.0} -->

This tutorial paper provides an overview of the most recent PIML methods applied to the modeling and control of dynamical systems. Specifically, PIML techniques for system identification include structural priors in the architecture of the ML model, matrix factorizations, and physics-informed loss functions. PIML approaches to control cover learning dynamics models for model predictive control (MPC), learning Lyapunov and barrier functions, differentiable-programming-based control, safe data-driven control, and physics-informed reinforcement learning (RL). Obtaining safety and performance guarantees of PIML models and control policies requires rigorous tools verifying properties such as stability, robustness, Lipschitz properties, invariance, and other safety considerations such as constraint satisfaction. The paper also presents methods combining ML with high-fidelity digital twin models suitable for controller design and tuning via meta and transfer learning and dealing with sim2real gap in RL. Each major category of PIML methods is accompanied by a representative tutorial case study.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Conclusions", "weight": 1.0} -->

The use of PIML methods in control presents us with new exciting opportunities that include applications in systems with human-in-the-loop, multi-scale and multi-physics systems, and providing benefits such as improved interpretability and modularity, scalability to large-scale complex systems, safety guarantees for adaptive data-driven systems, or integration of multi-modal input data in the control systems.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Conclusions", "weight": 1.0} -->

However, several open questions remain that need to be addressed before the adoption of these methods in real-world applications. These include uncertainty quantification (UQ), data requirements and efficient sampling strategies, automated training, hyperparameter optimization, convergence guarantees, scalability of the verification methods, and computational requirements of high-fidelity physics simulators.
