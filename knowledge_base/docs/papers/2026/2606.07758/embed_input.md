<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Koopman Meets Input-Output Data: Data-Driven Output-Feedback Control of Nonlinear Systems with Closed-Loop Guarantees

Topics include Data-driven control, Output feedback, Koopman operator, Nonlinear systems, Input-output data, Closed-loop guarantees, Bilinear surrogate models, Exponential stability.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Combines Koopman operator ideas with input-output trajectory data to design output-feedback controllers for nonlinear systems with closed-loop guarantees. The method constructs an extended-state bilinear surrogate directly from measurements, then applies robust state-feedback design while proving convergence back for the original nonlinear state.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Data-driven control of nonlinear systems from input-output measurements remains a fundamental challenge, as existing approaches with rigorous closed-loop guarantees predominantly require access to full state measurements. In this paper, we address this gap by proposing a data-driven output-feedback controller design method for nonlinear systems that provides provable closed-loop guarantees while operating solely on measured input-output data. Our approach combines Koopman operator theory with an extended state representation of the nonlinear system constructed from input-output trajectories. This allows us to obtain a bilinear surrogate model directly from data, on which robust state-feedback design methods can be applied. By exploiting the observability of the underlying nonlinear system, we establish exponential stability of the extended state, which in turn implies exponential convergence of the original system state to the origin. Finally, we validate our theoretical findings in numerical simulations.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Data-driven control of dynamical systems has emerged as a powerful paradigm for designing controllers directly from measured data, bypassing the need for first-principles model derivation. This is particularly appealing in practice, where complex system dynamics are often difficult or expensive to model analytically, yet plenty of measurement data are readily available. For linear systems, data-driven control is by now relatively well understood. Willems' fundamental lemma provides a non-parametric characterization of all trajectories of a linear time-invariant system in terms of a single persistently excited experiment, forming the basis of a large body of work on data-driven predictive control and stabilization. Extensions to output-feedback settings for linear systems have been pursued in several directions, including robust output-feedback controllers, verification of dissipativity properties from input-output data, and data-driven output-feedback control of linear MIMO systems. However, extending these results to the nonlinear setting remains substantially more challenging and is largely open.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

For nonlinear systems, data-driven control with closed-loop guarantees typically relies on state or state-derivative data, and extensions to the output-feedback case are rare. A notable exception is the work of Dai et al. 2023; Dai et al. 2025, who design dynamic output feedback controllers for discrete-time nonlinear systems directly from input-output data with local stability guarantees, requiring that an auxiliary input-output representation of the system can be expressed through a known dictionary of basis functions. Constructing such representations from input-output data in a principled way remains an open challenge, and a natural starting point is the identification of nonlinear systems from data, which has been studied extensively. Classical approaches include lifting to higher-dimensional feature spaces via basis function expansions, such as LPV or polynomial approximations, local or piecewise linear subspace identification, and probabilistic approaches based on expectation-maximization or Gaussian processes. A particularly relevant subclass is the class of bilinear systems, which arise naturally as finite-dimensional Koopman representations of nonlinear dynamics and for which subspace identification methods have been developed, including kernel-based variants that avoid the exponential growth of data matrices with system order.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finite-sample guarantees for bilinear system identification have also been studied recently, direct data-driven controller design has been proposed via LMIs and model predictive control, and first end-to-end guarantees from identification to closed-loop control have been established in Chatzikiriakos et al. 2026.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Complementary to system identification, observer design for nonlinear and bilinear systems is a classical and active research area; see Besançon 2007a; Besançon 2007b; Isidori 2017; Bernard 2019; Bernard et al. 2022. Fundamental notions of nonlinear observability have been established from geometric and system-theoretic perspectives, with further results for polynomial and discrete-time systems. For nonlinear systems more broadly, early results on state reconstruction and convergence of the estimation error are due to Thau 1973. For bilinear systems specifically, observability conditions and stable state estimators have been developed, though observer convergence in this setting typically depends on the applied input sequence.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

A promising framework for handling nonlinear dynamics in a data-driven fashion is Koopman operator theory, which lifts nonlinear system dynamics into an infinite-dimensional, linear space through the action of the Koopman operator on observable functions. This viewpoint has sparked a rich literature on data-driven approximation of the Koopman operator, including extended dynamic mode decomposition, kernel-based variants, and deep learning approaches. Crucially, it has been established that linear Koopman approximations are generally insufficient for controlled systems, and that bilinear structures naturally emerge in Koopman representations of input-affine nonlinear systems; see also Haseli and Cortés 2023a; Haseli and Cortés 2023b; Haseli and Cortés 2023c; Haseli and Cortés 2026; Shang et al. 2026 for further theoretical developments on the structure of controlled Koopman operators. Further, Lian et al. 2021; Shang et al. 2024; Xiong et al. 2025 propose extensions of Willems' fundamental lemma to the nonlinear setting using Koopman embeddings, though typically under restrictive invariance assumptions on the chosen dictionary.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, Lazar 2025 addresses these limitations by constructing the Koopman operator on a product Hilbert space formed as the tensor product of state and input observable spaces, relaxing dictionary invariance and measure preservation requirements. This allows the author to derive a nonlinear fundamental lemma for input-*output* data by combining the resulting exact *infinite*-dimensional bilinear representation with Hankel operators and a frame-based persistency of excitation condition. However, the approach inherently relies on infinite-dimensional representations and requires state measurements during the offline data collection phase to construct the lifted Hankel operator. While finite-dimensional EDMD approximations via a Khatri-Rao scheme are proposed, no finite-sample error bounds or closed-loop guarantees are established, limiting its applicability to rigorous data-driven controller design.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

A key insight for practical applicability is that the Koopman operator can be approximated using delay-coordinate embeddings, which are directly constructed from input-output time-series data without requiring state measurements. These findings directly led to Hankel DMD and latent EDMD. Koopman operator approximations based on delay-coordinate embeddings connect naturally to Takens' theorem and have been exploited in MPC and various engineering applications such as flow prediction, soft robotics, and grip force prediction. Finite-data error bounds for Koopman approximations are provided in Mezić 2022; Nüske et al. 2023; Schaller et al. 2023; Zhang and Zuazua 2023; Yadav and Mauroy 2025 for EDMD and in Philipp et al. 2024; Kurdila et al. 2024; Köhne et al. 2025; Bold et al. 2025b; Philipp et al. 2025a; Strässer et al. 2025c for kernel-based EDMD variants.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, Strässer et al. 2025d; Strässer et al. 2026a; Strässer et al. 2025a; Strässer et al. 2025b establish first closed-loop guarantees for Koopman-based controllers, including Koopman-based MPC; see the recent overview paper Strässer et al. 2026b. However, all of the above results with closed-loop guarantees require state measurements for the construction of the Koopman surrogate model and the subsequent controller design. Obtaining full state measurements is often impractical or infeasible in real-world applications, where only input-output data are available, motivating the need for output-feedback approaches that avoid this restrictive assumption.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

On the observer and estimation side, the Koopman framework has been used to design state estimators via various lifting strategies, including bilinear, linear observable, and dual Koopman forms, as well as kernel-based and neural-network-enhanced Kalman filters; see Otto and Rowley 2021; Shi et al. 2026 for surveys. Further approaches include robust observer synthesis using linear Koopman approximations with frequency-domain error characterization, and the construction of LPV Koopman models from noisy output data using deep state-space encoders. However, these approaches either rely on the restrictive assumption of an exactly invariant Koopman dictionary or do not provide guarantees for the designed observer. More broadly, output-feedback control using Koopman embeddings remains largely restricted to settings that assume exact Koopman invariance, linear Koopman approximations, or LPV surrogate models with frequency-domain error characterization, and a rigorous data-driven output-feedback design for nonlinear systems with provable closed-loop guarantees is missing from the literature.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

To solve this gap, we propose a data-driven output-feedback controller design method for nonlinear systems. In particular, we combine Koopman operator theory with an extended state representation of nonlinear systems based on input-output data. This allows us to build on robust state-feedback design schemes from the literature to exponentially stabilize the nonlinear extended-state system and, thereby, establish closed-loop guarantees for the underlying nonlinear system from input-output data. By exploiting the observability of the system, we show exponential convergence to the origin of the corresponding system's state. The proposed approach is the first Koopman-based controller design method that relies solely on input-output data and provides closed-loop guarantees for the underlying nonlinear system, paving the way forward to rigorous data-driven output-feedback control with closed-loop guarantees. Finally, we validate our theoretical findings in numerical simulations.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

The paper is structured as follows. In Section 2, we introduce the problem setting and necessary background for the results developed in this paper. Section 3 is devoted to an input-output representation of nonlinear systems. Section 4 contains our main contributions, namely a data-driven output-feedback controller design for nonlinear systems on the basis of a bilinear Koopman surrogate model. Finally, the theoretical results are illustrated in Section 5 using numerical simulations, before concluding the paper in Section 6.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem setting and background", "weight": 1.0} -->

First, we introduce the problem setting in Section 2.1. Then, we provide the necessary background on Koopman operator theory and its usage for controlled nonlinear systems in Section 2.2.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 2.1 (Smoothness)", "weight": 1.0} -->

The maps $f,h\in C^{1}$, i.e., the maps are continuously differentiable, and the sets $\mathbb{X}$, $\mathbb{U}$, $\mathbb{Y}$ are compact, convex, and contain the origin in its interior. Further, $f=0$ and $h=0$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 2.1 (Smoothness)", "weight": 1.0} -->

For a given initial state $\bar{x}\in\mathbb{X}$ and an input sequence $\mathbf{u}_{0:L-1}\in\mathbb{U}^{L}$, we define the corresponding state trajectory recursively via such that $x_{j}$ is the state at time $j$ starting from the initial condition $\bar{x}$ at time zero. The corresponding output is $y_{j}=h(x_{j},u_{j})$. Further, we write which corresponds to applying the map $f$ $j$ times.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 2.1 (Smoothness)", "weight": 1.0} -->

To find a suitable system representation, the unknown system dynamics are estimated from data, where, however, the state $x$ is inaccessible and only input-output measurements are available. In particular, we collect $d\in\mathbb{N}$ input-output trajectories of length $L+1$, i.e., Note that we use only input-*output* data instead of input-*state* data. For the Koopman surrogate established later, each trajectory of length $L+1$ will be associated with a data triplet of a delay embedding, its successor, and its input. This yields a total of $d$ data triplets used for the data-driven surrogate characterization.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Remark 2.2", "weight": 1.0} -->

As usual in data-driven control, we may also collect one single trajectory instead of multiple shorter input-output trajectories. More precisely, instead of the data $\mathcal{D}$ we could also collect a trajectory of length $L+d+1$, i.e., $\{u_{t},y_{t}\}_{t=-L}^{d}$. Based on this trajectory, we could again define $d$ extended state triplets, leading to the proposed Koopman-based surrogate. Then, all results established in this paper remain valid.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 2.2", "weight": 1.0} -->

To characterize when the full system behavior can be inferred from input-output data alone, we define the following.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Koopman operator background", "weight": 1.0} -->

Consider a discrete-time autonomous dynamical system $x_{k+1}=f(x_{k})$ with $x_{k}\in\mathbb{X}\subseteq\mathbb{R}^{n}$ and state-transition map $f:\mathbb{X}\to\mathbb{X}$. Instead of evolving the state directly, the *Koopman operator* $\mathcal{K}$ acts on scalar-valued observable functions $\varphi:\mathbb{X}\to\mathbb{R}$ by composing them with $f$, i.e., Although the underlying dynamics $f$ may be nonlinear, $\mathcal{K}$ is a *linear* operator acting on an, in general, infinite-dimensional function space.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Koopman operator background", "weight": 1.0} -->

In practice, one works with a finite-dimensional approximation by selecting a dictionary of $N$ observables, i.e., and seeking a matrix $K\in\mathbb{R}^{N\times N}$ such that A standard data-driven method for identifying $K$ is *extended dynamic mode decomposition*. Given a dataset of $d+1$ consecutive state pairs $\{(x_{j},\,x_{j+1})\}_{j=0}^{d}$ collected along one or more system trajectories, EDMD computes the least-squares solution where the snapshot matrices collect the lifted current and successor states, respectively, and $(\cdot)^{\dagger}$ denotes the Moore--Penrose pseudoinverse.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Koopman operator background", "weight": 1.0} -->

For a controlled discrete-time system the Koopman framework is extended by treating the input as a parameter of the operator. Assuming $u_{k}$ is held constant over each sampling interval, consistent with a sample-and-hold implementation, a family of input-dependent Koopman operators $\{\mathcal{K}^{u}\}_{u\in\mathbb{U}}$ is defined by compare Haseli and Cortés 2026. Each operator $\mathcal{K}^{u}$ remains linear in the observable space for fixed $u$. Introducing the same dictionary of observable functions $\Psi$ as before, one seeks a finite-dimensional approximation from data.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Koopman operator background", "weight": 1.0} -->

In linear EDMD with control, one builds a lifted *linear* model where the matrices $A\in\mathbb{R}^{N\times N}$ and $B\in\mathbb{R}^{N\times m}$ can be identified simultaneously via a least-squares regression over snapshot data. Although this linear evolution of the lifted state would be desirable, as it enables the direct application of linear systems theory and control design to the originally nonlinear controlled system, it introduces fundamental approximation errors. In particular, representations of the above form impose severe limitations on the original system. This fact prevents closed-loop guarantees and thereby safe control of the underlying nonlinear system. Instead, at least *bilinear* Koopman surrogates are required to approximate the infinite-dimensional Koopman action. In particular, the Koopman-based control framework proposed in Strässer 2026 leverages the bilinear Koopman surrogate modeling approaches SafEDMD and kEDMD to ensure closed-loop properties of the underlying nonlinear system.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Koopman operator background", "weight": 1.0} -->

More precisely, the resulting bilinear Koopman surrogate reads where the residual can be *proportionally* bounded by and the matrices $A\in\mathbb{R}^{N\times N}$, $B_{0}\in\mathbb{R}^{N\times m}$, and $\tilde{B}\in\mathbb{R}^{N\times Nm}$ are either computed via kernel methods or least-squares regression over snapshot data, i.e., where $U=\begin{bmatrix}u_{0}&\cdots&u_{d-1}\end{bmatrix}$ and $U_{X}=\begin{bmatrix}u_{0}\otimes\Psi(x_{0})&\cdots&u_{d-1}\otimes\Psi(x_{d-1})\end{bmatrix}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Koopman operator background", "weight": 1.0} -->

The main limitation of the bilinear surrogate model (2.14) is its dependence on the state $x$, which is typically not accessible in practice and therefore restrictive. This manifests in two ways: first, learning the surrogate model requires state measurements; second, the resulting state-space representation relies on the state for both prediction and controller design. In the remainder of this paper, we circumvent these issues by generalizing the state-dependent Koopman surrogate models introduced above, deriving an input-output characterization that is independent of the unknown state $x$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Input-output representation of nonlinear systems", "weight": 1.0} -->

In this section, we discuss input-output representations of nonlinear systems, extending the ideas of linear systems, which we recall in Appendix A for completeness. We note that the results developed in this section may be of independent interest beyond Koopman-based control; see Remark 3.3.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Input-output representation of nonlinear systems", "weight": 1.0} -->

Consider the nonlinear system (2.1) with $x\in\mathbb{X}\subseteq\mathbb{R}^{n}$, $u\in\mathbb{U}\subseteq\mathbb{R}^{m}$, and $y\in\mathbb{Y}\subseteq\mathbb{R}^{p}$, where the state $x$ is inaccessible but only input-output measurements are available. Since the original internal state $x$ is unknown, the core idea is to use past input-output measurements to infer knowledge about the initial condition. In particular, we seek an equivalent input-output representation of the nonlinear system (2.1) based on an extended state of delayed input-output measurements. To this end, we construct a delay embedding $\xi$ of past input-output measurements over a finite horizon $L$, which we call the extended-state vector, as common in the data-driven control literature.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Input-output representation of nonlinear systems", "weight": 1.0} -->

More precisely, we define In the following, we investigate under which conditions there exists a smooth map $\mathcal{R}_{L}$ such that the initial state $\bar{x}$ is uniquely reconstructable from a finite input-output sequence. In particular, we aim at the representation compare the reconstructability map in Iacob et al. 2025. If such $\mathcal{R}_{L}$ exists, we can substitute it into the combined dynamics and output equation to obtain an equivalent closed-form input-output relation that does not rely on the original state $x_{k-L}$. This is exactly characterized by uniform observability of the underlying nonlinear system (2.1), compare Definition 2.4. ‣ 2.1 Problem setting ‣ 2 Problem setting and background ‣ Koopman meets input-output data: Data-driven output-feedback control of nonlinear systems with closed-loop guarantees"). In the following, we characterize under which conditions this observability property holds and, thereby, an equivalent input-output representation exists.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Input-output representation of nonlinear systems", "weight": 1.0} -->

Based on Assumption 2.1. ‣ 2.1 Problem setting ‣ 2 Problem setting and background ‣ Koopman meets input-output data: Data-driven output-feedback control of nonlinear systems with closed-loop guarantees"), we directly deduce $\mathcal{O}_{L}\in C^{1}$, i.e., we can compute the Jacobian of $\mathcal{O}_{L}$ w.r.t. $\bar{x}$. In particular, where $H_{j}$ and $F_{j}$ depend on the trajectory $x_{j}$, i.e., on both the initial condition $\bar{x}$ and the input sequence $\mathbf{u}_{0:j}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Assumption 3.1 (Uniform injectivity of the observability map)", "weight": 1.0} -->

Assumption 3.1. ‣ 3 Input-output representation of nonlinear systems ‣ Koopman meets input-output data: Data-driven output-feedback control of nonlinear systems with closed-loop guarantees") can be understood as a quantitative injectivity ensuring observability of the underlying system. A *pointwise* condition that is typically easier to verify in practice compared to Assumption 3.1. ‣ 3 Input-output representation of nonlinear systems ‣ Koopman meets input-output data: Data-driven output-feedback control of nonlinear systems with closed-loop guarantees") is for all $\bar{x}\in\mathbb{X}$ and all $\mathbf{u}_{0:L-1}\in\mathbb{U}^{L}$, where $\sigma_{\min}$ denotes the smallest singular value. However, this pointwise condition does not imply (3.4. ‣ 3 Input-output representation of nonlinear systems ‣ Koopman meets input-output data: Data-driven output-feedback control of nonlinear systems with closed-loop guarantees")) in general, and the stronger Assumption 3.1.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Assumption 3.1 (Uniform injectivity of the observability map)", "weight": 1.0} -->

‣ 3 Input-output representation of nonlinear systems ‣ Koopman meets input-output data: Data-driven output-feedback control of nonlinear systems with closed-loop guarantees") is required for the following result. There, we explain a given input-output trajectory of (2.1) by an extended-state system if there is a bijection between the given trajectory and the extended-state trajectory.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 3.2", "weight": 1.0} -->

Takens' theorem analyzes the delay-coordinate map $\mathcal{O}_{L}$ defined in Definition 2.3. ‣ 2.1 Problem setting ‣ 2 Problem setting and background ‣ Koopman meets input-output data: Data-driven output-feedback control of nonlinear systems with closed-loop guarantees") in the autonomous case (i.e., without control input $u$). It states that, for generic systems and output maps, the map $\mathcal{O}_{L}$ generically becomes an embedding for $L\geq 2n$. In contrast, uniform observability according to Definition 2.4. ‣ 2.1 Problem setting ‣ 2 Problem setting and background ‣ Koopman meets input-output data: Data-driven output-feedback control of nonlinear systems with closed-loop guarantees") requires injectivity for a fixed system and uniformly over all input sequences $\mathbf{u}_{0:L-1}\in\mathbb{U}^{L}$, while the lower bound in Assumption 3.1.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 3.2", "weight": 1.0} -->

‣ 3 Input-output representation of nonlinear systems ‣ Koopman meets input-output data: Data-driven output-feedback control of nonlinear systems with closed-loop guarantees") further strengthens this to a quantitative (well-conditioned) embedding, which is not guaranteed by Takens.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

In the remainder of the paper, we use the input-output representation established by Proposition 3.1. ‣ 3 Input-output representation of nonlinear systems ‣ Koopman meets input-output data: Data-driven output-feedback control of nonlinear systems with closed-loop guarantees") to derive a Koopman-based output-feedback controller design method. We note, however, that Proposition 3.1. ‣ 3 Input-output representation of nonlinear systems ‣ Koopman meets input-output data: Data-driven output-feedback control of nonlinear systems with closed-loop guarantees") is not specific to Koopman-based methods and could serve as a foundation for generalizing other nonlinear data-driven state-feedback designs to the output-feedback setting; see Martin et al. 2023 for an overview of such designs with closed-loop guarantees.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

For example, one could define a set of basis functions and apply a nonlinear data-driven control approach as in Lazar 2024, or construct a polynomial approximation of the nonlinear input-output dynamics in the extended state $\xi$ and combine it with robust control and sum-of-squares (SOS) optimization as in Martin and Allgöwer 2024; Martin 2024. In the present work, Koopman is a particularly natural choice given that the nonlinear dynamics (2.1) and the associated maps $f_{\xi}$, $h_{\xi}$ are unknown.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Data-driven output-feedback controller design for nonlinear systems", "weight": 1.0} -->

After establishing an input-output representation of unknown nonlinear systems, we leverage Koopman operator theory to design an output-feedback controller for nonlinear systems with rigorous closed-loop guarantees. To this end, Section 4.1 is devoted to deriving a bilinear surrogate model for the nonlinear input-output representation of the underlying system. Then, we use this surrogate to design an output-feedback controller in Section 4.2.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Koopman-based bilinear surrogate of nonlinear input-output behavior", "weight": 1.0} -->

Based on the nonlinear input-output representation (3.6. ‣ 3 Input-output representation of nonlinear systems ‣ Koopman meets input-output data: Data-driven output-feedback control of nonlinear systems with closed-loop guarantees")) of the underlying nonlinear system (2.1) established by Proposition 3.1. ‣ 3 Input-output representation of nonlinear systems ‣ Koopman meets input-output data: Data-driven output-feedback control of nonlinear systems with closed-loop guarantees"), we employ a Koopman lifting to bilinearize the representation, which is subsequently learned via data.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Koopman-based bilinear surrogate of nonlinear input-output behavior", "weight": 1.0} -->

To this end, we follow the line of thoughts presented in Strässer et al. 2026a; Strässer et al. 2026b and introduce the vector-valued observable function $\Psi:\mathbb{R}^{L(m+p)}\to\mathbb{R}^{N}$ with The observables $\psi_{k}$, $k=L(m+p)+1,...,N$, satisfy $\psi_{k}\in C^{1}(\mathbb{R}^{L(m+p)},\mathbb{R})$ with $\psi_{k}=0$. Then, $\Psi$ is pointwise bounded by for all $\xi\in\mathbb{E}\coloneqq\mathbb{U}^{L}\times\mathbb{Y}^{L}\subseteq\mathbb{R}^{L(m+p)}$ with some $L_{\Psi}\in\mathbb{R}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Koopman-based bilinear surrogate of nonlinear input-output behavior", "weight": 1.0} -->

Since the nonlinear system (2.1) and its input-output representation (3.6. ‣ 3 Input-output representation of nonlinear systems ‣ Koopman meets input-output data: Data-driven output-feedback control of nonlinear systems with closed-loop guarantees")) are unknown, we characterize the dynamics via data. In particular, we collect input-output data $\mathcal{D}$ consisting of $d$ trajectories of length $L+1$ as defined in (2.4). This trajectory allows us to arrange the data according to the defined extended state (3.1) for delay depth $L$, i.e., we obtain the extended-state data consisting of $d$ triplets of extended state, its successor, and its input, where $u_{k}=u_{0}^{(k)}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Koopman-based bilinear surrogate of nonlinear input-output behavior", "weight": 1.0} -->

In the following, we present two different data-driven surrogate representations derived using the data $\mathcal{D}$. In Section 4.1.1, we first assume the existence of an *exact* Koopman bilinearization. Since this is typically not the case for general nonlinear systems, we allow for perturbations in the Koopman-based bilinear surrogate in Section 4.1.2.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Exact Koopman bilinearization", "weight": 1.0} -->

The first presented data-driven surrogate model relies on the following (possibly restrictive) assumption on the employed Koopman bilinearization, which allows for the use of straightforward arguments. We stress, however, that the main results developed in this paper do not rely on this assumption, and the subsequent section considers a realistic and more general setting.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Assumption 4.1", "weight": 1.0} -->

The Koopman operator action corresponding to the nonlinear input-output representation (3.6. ‣ 3 Input-output representation of nonlinear systems ‣ Koopman meets input-output data: Data-driven output-feedback control of nonlinear systems with closed-loop guarantees")) admits an *exact* finite-dimensional bilinear representation of the form for all $\xi\in\mathbb{E}$ and $u\in\mathbb{U}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Assumption 4.1", "weight": 1.0} -->

The unknown matrices $A_{\mathrm{tr}},B_{0,\mathrm{tr}},\tilde{B}_{\mathrm{tr}}$ of the bilinear Koopman representation (4.4) are estimated from measured data. To this end, we solve the linear regression problem with the data matrices The regression problem (4.5) has a unique solution if i.e., the stacked data matrix has full column rank. Thus, we obtain This leads to the following intermediate result.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Koopman bilinearization with proportionally bounded residual", "weight": 1.0} -->

Since Assumption 4.1 is typically hard to satisfy for general nonlinear systems, we loosen the assumption and allow for errors in the bilinear representation satisfying a proportional error bound.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Assumption 4.2", "weight": 1.0} -->

The Koopman operator action corresponding to the nonlinear input-output representation (3.6. ‣ 3 Input-output representation of nonlinear systems ‣ Koopman meets input-output data: Data-driven output-feedback control of nonlinear systems with closed-loop guarantees")) admits a finite-dimensional perturbed bilinear representation of the form where the residual $r_{\Psi}(\xi_{k},u_{k})$ is proportionally bounded by for all $\xi\in\mathbb{E}$ and $u\in\mathbb{U}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Assumption 4.2", "weight": 1.0} -->

The proportional structure of bound (4.13) on the residual error is validated in Strässer et al. 2026a and represents a standard assumption in Koopman-based control. This bound captures both the bilinear approximation error of the Koopman operator and the projection error arising from the finite-dimensional lifting function $\Psi$. For the latter, the proportional structure is widely assumed in the literature and explicitly verified, e.g., in the kernel setting. Moreover, Strässer et al. 2026a establishes a proportional bound on the Koopman-bilinearization error for control-affine nonlinear systems.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Assumption 4.2", "weight": 1.0} -->

As before, we estimate the unknown system matrices $A_{\mathrm{tr}},B_{0,\mathrm{tr}},\tilde{B}_{\mathrm{tr}}$ using the collected data, i.e., by solving for (4.8) if the rank condition (4.7) is satisfied. This leads us to the first main result of this paper.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Remark 4.4", "weight": 1.0} -->

If the full state is measurable, i.e., $h(x,u)=x$, Theorem 4.3 provides an alternative characterization of the *learning* error of the Koopman operator approximation from input-state data. In particular, in this case, no extended state is needed, but we can replace $\xi$ by $x$ to obtain for all $x\in\mathbb{X}$ and $u\in\mathbb{U}$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 4.4", "weight": 1.0} -->

Here, similar to Assumption 4.2, we assume the existence of a finite-dimensional perturbed bilinear representation of the form where $r_{\Psi}$ is bounded by (4.24b) for some $c_{\Psi,x},c_{\Psi,u}\geq 0$, and compute $A,B_{0},\tilde{B}$ based on the linear regression problem with the data matrices $X$, $X^{+}$, $U$, $U_{X}$ defined analogously to the matrices in (4.6) and In contrast, SafEDMD derive proportional error bounds for bilinear approximations of the controlled Koopman generator and controlled Koopman operator by combining multiple autonomous variants and building on the respective error bounds in Schaller et al. 2023 and Nüske et al. 2023, respectively. This, however, requires multiple data sets collected under specific *constant* control inputs with i.i.d. samples, a sampling strategy that may be restrictive in practice.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Remark 4.4", "weight": 1.0} -->

Instead, Theorem 4.3 and, more specifically, the state-data surrogate (4.24) characterize the learning error for *any* data trajectory, without restricting to particular input choices and data requirements, relying instead on results from noisy least-squares optimization. Thus, Theorem 4.3 is of independent interest beyond the input-output case, and may allow for more flexible sampling strategies, a broader class of control problems to be addressed within the Koopman framework, and potentially more interpretable error bounds due to its direct reliance on noisy least-squares optimization.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Remark 4.5", "weight": 1.0} -->

If the input-output data is subject to noise, i.e., the nonlinear input-output dynamics (3.6. ‣ 3 Input-output representation of nonlinear systems ‣ Koopman meets input-output data: Data-driven output-feedback control of nonlinear systems with closed-loop guarantees")) satisfy for $\|w_{k}\|\leq\bar{w}$, the estimate can be straightforwardly adapted. In particular, the noise enters the lifted data matrix $\Psi(\Xi^{+})$ and therefore deteriorates the least-squares estimate. Then, the mismatch between true values and the least-squares solution is bounded by where we assume Lipschitz continuity of the lifting function $\Psi$. Thus, the structure of the residual bound on $r_{\Delta}(\xi,u)$ remains unchanged.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Remark 4.6", "weight": 1.0} -->

In this section, we establish a Koopman-based bilinear *input-output* surrogate representation with guaranteed *proportional* error bounds. This is particularly desirable as it allows for the application of Koopman-based controller designs for bilinear systems with closed-loop guarantees. Here, we exploit the (nonlinear) input-output representation (3.6. ‣ 3 Input-output representation of nonlinear systems ‣ Koopman meets input-output data: Data-driven output-feedback control of nonlinear systems with closed-loop guarantees")) of the unknown nonlinear system (2.1), relying on uniform observability of the underlying system. A possible alternative approach would be to first Koopman bilinearize the original nonlinear system, i.e., employing a state-based lifting function to obtain a bilinear surrogate in the lifted Koopman space, again with proportionally bounded residual error. Since this bilinear representation is unknown and the (state-based) lifting function is not accessible, we could use again input-output data to construct a representation with the same input-output behavior as the bilinear surrogate using an extended state.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Remark 4.6", "weight": 1.0} -->

Comparing both approaches, i.e., 1) input-output characterization for nonlinear systems, then Koopman bilinearization, or 2) Koopman bilinearization, then input-output characterization for bilinear systems, is an interesting direction for future research.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Koopman-based output-feedback controller design", "weight": 1.0} -->

In the following, we use the Koopman-based input-output surrogate established in Theorem 4.3 to design a robust output-feedback controller with closed-loop guarantees for the nonlinear system (2.1). To this end, we build on the state-feedback controller designs established in Strässer et al. 2026a using linear matrix inequalities and in Strässer et al. 2025a using SOS optimization. Then, we use the proposed extended-state representation (3.6. ‣ 3 Input-output representation of nonlinear systems ‣ Koopman meets input-output data: Data-driven output-feedback control of nonlinear systems with closed-loop guarantees")) of the underlying nonlinear system (2.1) to define an output-feedback control law. While the generalization from state-feedback to output-feedback design can be done for any robust controller design for bilinear Koopman surrogates with (proportionally) bounded residual error, we rely on the SOS-based design proposed in Strässer et al. 2025a as it provides the least conservative (guaranteed) closed-loop properties available in the literature.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Koopman-based output-feedback controller design", "weight": 1.0} -->

Before stating our main theorem, we introduce some necessary SOS notation. We denote the set of all polynomials $s$ in the variable $z\in\mathbb{R}^{N}$ with degree $n_{d}$ and real coefficients by $\mathbb{R}[z,n_{d}]$. Similarly, we write $\mathbb{R}[z,n_{d}]^{p\times q}$ for the set of all $p\times q$-matrices with elements in $\mathbb{R}[z,n_{d}]$. We call $S\in\mathbb{R}[z,2n_{d}]^{p\times p}$ an SOS matrix in $x$, denoted by $S\in\mathrm{SOS}[z,2n_{d}]^{p}$, if it can be decomposed as $S=T^{\top}T$ for some $T\in\mathbb{R}[z,n_{d}]^{q\times p}$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Remark 4.9", "weight": 1.0} -->

Given the possibly high-dimensional lifting dimension $N$, the SOS program (4.30. ‣ 4.2 Koopman-based output-feedback controller design ‣ 4 Data-driven output-feedback controller design for nonlinear systems ‣ Koopman meets input-output data: Data-driven output-feedback control of nonlinear systems with closed-loop guarantees")) may be computationally challenging to solve. While we leave a structured analysis of possible model order reduction techniques for the proposed output-feedback controller design to future work, a direct dimensionality reduction follows from combining the uncertainty characterizations of both residual terms $r_{\Psi}$ and $r_{\Delta}$. More precisely, solving instead of (4.30. ‣ 4.2 Koopman-based output-feedback controller design ‣ 4 Data-driven output-feedback controller design for nonlinear systems ‣ Koopman meets input-output data: Data-driven output-feedback control of nonlinear systems with closed-loop guarantees")) in order to obtain the control law $\mu$ in (4.32.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Remark 4.9", "weight": 1.0} -->

‣ 4.2 Koopman-based output-feedback controller design ‣ 4 Data-driven output-feedback controller design for nonlinear systems ‣ Koopman meets input-output data: Data-driven output-feedback control of nonlinear systems with closed-loop guarantees")) reduces the dimension of the SOS program by introducing additional conservatism through the combination of the two residual error bounds.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Numerical example", "weight": 1.0} -->

In this section, we illustrate our theoretical findings in numerical simulations. All our simulations are conducted on an i7 notebook using Yalmip with the semi-definite programming solver MOSEK in MATLAB R2026a.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We consider the continuous-time nonlinear dynamical system which is discretized with a 4th order Runge-Kutta method for the sampling time $T_{s}=0.1$. Let $\mathbb{X}=[-1.5,1.5]^{2}$, $\mathbb{U}=$, and $\mathbb{Y}=$. We collect $d$ data trajectories of length $L$, where we uniformly sample the initial state from $\mathbb{X}$ and evaluate the dynamics to obtain the corresponding input-output measurements. This allows us to construct the extended-state data as in (4.3).

<!-- chunk {"id": "body-0061", "role": "body", "section": "Numerical example", "weight": 1.0} -->

In the following, we illustrate the effectiveness of the proposed Koopman-based surrogate model for prediction (Section 5.1) as well as for an output-feedback controller design (Section 5.2).

<!-- chunk {"id": "body-0062", "role": "body", "section": "Open-loop prediction", "weight": 1.0} -->

First, we investigate the prediction capability of the proposed Koopman-based bilinear surrogate for the input-output behavior of the underlying nonlinear system. To this end, we employ a polynomial lifting function $\Psi(\xi)$, which contains all monomials up to degree $n_{d}$. Then, we choose $d=100$ and vary the delay length $L$ as well as the degree $n_{d}$ to build the surrogate in (4.14) purely based on input-output data. We consider the nominal bilinear surrogate and compare the open-loop prediction error for random inputs $u_{k}$ uniformly sampled from $\mathbb{U}$. The resulting open-loop prediction error, averaged over 50 runs, is depicted in Fig. 1a. Here, we illustrate different combinations of $L$ and $n_{d}$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Open-loop prediction", "weight": 1.0} -->

We emphasize that choosing $\Psi(\xi)=\xi$, i.e., $n_{d}=1$, yields a satisfactory prediction error for a sufficiently large delay length $L$. Further, as we see for $n_{d}=2$, increasing $L$ improves the prediction capabilities of the proposed bilinear surrogate. Here, the initial prediction error at $t=0$ indicates the approximation quality of the employed delay embedding of depth $L$ together with the $N$-dimensional nonlinear lifting function $\Psi$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Open-loop prediction", "weight": 1.0} -->

We compare the prediction error to a *linear* EDMDc-based Koopman surrogate as in (2.13), i.e., where we use the same polynomial lifting function $\Psi(\xi)$ and the same collected data. Notably, the prediction error of EDMDc is worse than our proposed bilinear surrogate for all combinations of $n_{d}$ and $L$ studied in this paper. More precisely, the prediction error of EDMDc may quickly explode and, therefore, EDMDc is sensitive to the employed delay length $L$ and chosen degree $n_{d}$ of the lifting function. Thus, our proposed bilinear Koopman surrogate (4.12) offers a more robust prediction w.r.t. the employed lifting and input-output characterization of the underlying nonlinear system.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Closed-loop simulation", "weight": 1.0} -->

Now, we apply the proposed output-feedback controller design in Theorem 4.7. ‣ 4.2 Koopman-based output-feedback controller design ‣ 4 Data-driven output-feedback controller design for nonlinear systems ‣ Koopman meets input-output data: Data-driven output-feedback control of nonlinear systems with closed-loop guarantees") to show that the output of the nonlinear system converges to the origin. To this end, we choose $d=100$ with $L=1$ and a polynomial lifting function $\Psi(\xi)$ including all monomials up to degree $n_{d}=2$. For the bilinearization error in Assumption 4.2, we assume the residual error bound (4.13) to hold with constants $c_{\Psi,\xi}=c_{\Psi_{u}}=1\mathrm{e}-4$. Then, we compute the constants $c_{\Delta,\xi}$, $c_{\Delta,u}$ for the error bound (4.15) on the residual $r_{\Delta}$ according to (4.16).

<!-- chunk {"id": "body-0066", "role": "body", "section": "Closed-loop simulation", "weight": 1.0} -->

To solve the SOS program (4.30. ‣ 4.2 Koopman-based output-feedback controller design ‣ 4 Data-driven output-feedback controller design for nonlinear systems ‣ Koopman meets input-output data: Data-driven output-feedback control of nonlinear systems with closed-loop guarantees")), we choose $\alpha=\beta=1$ and Then, the output-feedback control law is computed as in (4.32. ‣ 4.2 Koopman-based output-feedback controller design ‣ 4 Data-driven output-feedback controller design for nonlinear systems ‣ Koopman meets input-output data: Data-driven output-feedback control of nonlinear systems with closed-loop guarantees")). To demonstrate its effectiveness, we sample 100 initial conditions $x_{-L}$ uniformly from $\mathbb{X}$ and simulate the nonlinear dynamics under a random input sequence $\mathbf{u}_{-L,-1}$, drawn uniformly from $\mathbb{U}^{L}$, to initialize the extended state as in (3.7.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Closed-loop simulation", "weight": 1.0} -->

‣ 3 Input-output representation of nonlinear systems ‣ Koopman meets input-output data: Data-driven output-feedback control of nonlinear systems with closed-loop guarantees")). The resulting input-output measurements are used to construct the extended state $\xi_{0}$, after which the control law (4.32. ‣ 4.2 Koopman-based output-feedback controller design ‣ 4 Data-driven output-feedback controller design for nonlinear systems ‣ Koopman meets input-output data: Data-driven output-feedback control of nonlinear systems with closed-loop guarantees")) is applied. Fig. 2 shows the closed-loop output trajectories $y$ for all 100 initial conditions, each of which converges to the origin.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Closed-loop simulation", "weight": 1.0} -->

We compare the resulting closed-loop behavior against one of the most widely used Koopman-based controller design approaches in the literature, namely a linear-quadratic regulator (LQR) designed on the linear EDMDc surrogate (5.4). The LQR control law takes the form $\mu_{\mathrm{LQR}}(\xi)=-K\Psi(\xi)$, where $K_{\mathrm{LQR}}$ is obtained by solving the corresponding Riccati equation with $Q=R=I$. Unlike our proposed output-feedback controller (4.32. ‣ 4.2 Koopman-based output-feedback controller design ‣ 4 Data-driven output-feedback controller design for nonlinear systems ‣ Koopman meets input-output data: Data-driven output-feedback control of nonlinear systems with closed-loop guarantees")), the LQR controller $\mu_{\mathrm{LQR}}$ offers no closed-loop stability guarantees and fails to reliably stabilize the system.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Closed-loop simulation", "weight": 1.0} -->

By exploiting the bilinear Koopman surrogate of the input-output representation within an SOS framework, we obtain rigorous closed-loop guarantees (Corollary 4.8. ‣ 4.2 Koopman-based output-feedback controller design ‣ 4 Data-driven output-feedback controller design for nonlinear systems ‣ Koopman meets input-output data: Data-driven output-feedback control of nonlinear systems with closed-loop guarantees")) and successfully stabilize all initial conditions.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Closed-loop simulation", "weight": 1.0} -->

In the simulation above, we choose a delay length of $L=1$ for the extended state $\xi$ and design the output-feedback controller $\mu$ accordingly. As observed in the prediction results of Section 5.1, a larger delay length $L$ and richer lifting function $\Psi(\xi)$ would generally be beneficial. However, the SOS-based controller design is computationally demanding with a computational complexity of $\mathcal{O}((N^{2\alpha+1})^{6})$ and therefore limited in the dimension of the extended state and the nonlinear lifting $\Psi$ that can be practically handled. An important direction for future work is thus the investigation of model order reduction schemes for the bilinear Koopman surrogate, which would render the controller design feasible for more appropriate choices of $L$ and $\Psi(\xi)$. Beyond SOS, combining the derived bilinear Koopman surrogate with other controller design techniques, such as MPC, offers another compelling direction to address this limitation.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we proposed a data-driven output-feedback controller design method for nonlinear systems that provides provable closed-loop guarantees while relying solely on measured input-output data. By combining Koopman operator theory with an extended state representation constructed from input-output trajectories, we derived a bilinear surrogate model directly from data, on which we applied robust state-feedback methods. Exploiting the observability of the underlying nonlinear system, we established exponential stability of the extended state and, consequently, exponential convergence of the original system state to the origin, with numerical simulations confirming the theoretical findings. To the best of our knowledge, this is the first Koopman-based controller design framework that operates exclusively on input-output data with rigorous closed-loop guarantees, addressing a fundamental gap in the data-driven control literature. Important directions for future work include extending the framework to handle noisy measurements with finite-sample error quantification or combining the design with model order reduction techniques to enhance practical applicability.
