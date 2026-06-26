<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Data-driven Discovery of Koopman Eigenfunctions for Control

Topics include Predictive control, Regression, Online algorithms, Control, KRONIC, Nonlinear systems.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Data-driven transformations that reformulate nonlinear systems in a linear framework have the potential to enable the prediction, estimation, and control of strongly nonlinear dynamics using linear systems theory. The Koopman operator has emerged as a principled linear embedding of nonlinear dynamics, and its eigenfunctions establish intrinsic coordinates along which the dynamics behave linearly. Previous studies have used finite-dimensional approximations of the Koopman operator for model-predictive control approaches. In this work, we illustrate a fundamental closure issue of this approach and argue that it is beneficial to first validate eigenfunctions and then construct reduced-order models in these validated eigenfunctions. These coordinates form a Koopman-invariant subspace by design and, thus, have improved predictive power. We show then how the control can be formulated directly in these intrinsic coordinates and discuss potential benefits and caveats of this perspective. The resulting control architecture is termed Koopman Reduced Order Nonlinear Identification and Control (KRONIC). It is demonstrated that these eigenfunctions can be approximated with data-driven regression and power series expansions, based on the partial differential equation governing the infinitesimal generator of the Koopman operator.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Validating discovered eigenfunctions is crucial and we show that lightly damped eigenfunctions may be faithfully extracted from EDMD or an implicit formulation. These lightly damped eigenfunctions are particularly relevant for control, as they correspond to nearly conserved quantities that are associated with persistent dynamics, such as the Hamiltonian. KRONIC is then demonstrated on a number of relevant examples, including 1) a nonlinear system with a known linear embedding, 2) a variety of Hamiltonian systems, and 3) a high-dimensional double-gyre model for ocean mixing.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast to linear systems, a generally applicable and scalable framework for the control of nonlinear systems remains an engineering grand challenge. Improved nonlinear control has the potential to transform our ability to interact with and manipulate complex systems across broad scientific, technological, and industrial domains. From turbulence control to brain-machine interfaces, emerging technologies are characterized by high-dimensional, strongly nonlinear, and multiscale phenomena that lack simple models suitable for control design. This lack of simple equations motivates *data-driven* control methodologies, which include system identification for model discovery. Alternatively, one can seek transformations that embed nonlinear dynamics in a global linear representation, as in the Koopman framework. The goal of this work is to reformulate controlled nonlinear dynamics in a Koopman-eigenfunction framework, referred to as *Koopman Reduced Order Nonlinear Identification and Control* (KRONIC), that shows improved predictive power and is amenable to powerful linear optimal and robust control techniques.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A wide range of data-driven and nonlinear control approaches exist in the literature, including model-free adaptive control, extremum-seeking, gain scheduling, feedback linearization, describing functions, sliding mode control, singular perturbation, geometric control, back-stepping, model predictive control, reinforcement learning, and machine learning control. Although considerable progress has been made in the control of nonlinear systems, methods are generally tailored to a specific class of problems, require considerable mathematical and computational resources, or don't readily generalize to new applications. Currently there is no overarching framework for nonlinear control, that is generically applicable to a wide class of potentially high-dimensional systems, as exists for linear systems. Generally applicable frameworks, such as dynamic programming, Pontryagin's maximum principle, and model-predictive control (MPC), often suffer from the curse of dimensionality and require considerably computational effort, e.g. solving adjoint equations, when applied to nonlinear systems, which can be mitigated to some degree by combining these with low-dimensional, linear representations.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Fortunately, the rise of big data, advances in machine learning, and new approaches in dynamical systems are changing how we approach these canonically challenging nonlinear control problems. For instance, recently deep reinforcement learning has been combined with MPC, yielding impressive results in the large-data limit.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Koopman operator theory has recently emerged as a leading framework to obtain linear representations of nonlinear dynamical systems from data. This operator-theoretic perspective complements the more standard geometric and probabilistic perspectives. The ability to embed nonlinear dynamics in a linear framework (see Fig. 1) is particularly promising for the prediction, estimation, and control of nonlinear systems.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In 1931, Koopman showed that a nonlinear dynamical system may be represented by an infinite-dimensional linear operator acting on the space of measurement functions of the state of the system. Formulating dynamics in terms of measurements is appealing in the era of big data. Since the seminal work of Mezić and Banaszuk and Mezić, Koopman theory has been the focus of efforts to characterize nonlinear systems. Many classical results have been extended to the Koopman formalism. For example, level sets of Koopman eigenfunctions form invariant partitions and may be used to analyze mixing. The Hartman-Grobman theorem has also been generalized to provide a linearizing transform in the entire basin of attraction of a stable or unstable equilibrium or periodic orbit.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, Koopman theory has been applied for system identification, estimation and control of nonlinear systems. The Koopman operator is infinite-dimensional, and control laws are typically based on a finite-dimensional approximation. Dynamic mode decomposition (DMD) approximates the Koopman operator with a best-fit linear model. However, DMD is based on linear measurements, which do not span a Koopman invariant subspace for many nonlinear systems. Current data-driven methods to approximate the Koopman operator include extended DMD (EDMD) and the variational approach of conformation dynamics (VAC). EDMD was recently used for model predictive control with promising results. However, EDMD models may suffer from closure issues for systems with multiple fixed points or attractors, as a linear model only has a single fixed point, which may lead to corrupted dynamics and emphasizes the importance of model validation. For instance, some eigenfunctions may be distorted when projected onto a finite-dimensional measurement subspace, and it may be advantageous to construct a reduced-order description from validated eigenfunctions, that exhibit behavior as predicted by their associated eigenvalue.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

For chaotic systems, delay coordinates provides a promising embedding. Obtaining useful data-driven coordinate transformations that approximate Koopman eigenfunctions remains an open challenge in data-driven dynamical systems.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the present work, we build on the existing EDMD and reformulate the Koopman-based control problem in eigenfunction coordinates and provide strategies to identify lightly damped eigenfunctions from data, that can be subsequently used for control. In particular: Koopman eigenfunctions provide a principled linear embedding of nonlinear dynamics resulting in an intrinsic coordinate system, in which the system is closed under the action of the Koopman operator. We formulate the incorporation of control in these intrinsic coordinates and discuss benefits and caveats of this approach. Further, Koopman eigenfunctions can be associated with geometric system properties and coherent structures. Thus, the designed controller may be employed to manipulate particular coherent structures. For example, the Hamiltonian energy is a Koopman eigenfunction, and we are able to control the system by manipulating this function.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Smooth eigenfunctions in the point spectrum of the Koopman operator can be discovered from given data using sparse regression providing interpretable representations. We propose sparsity-promoting algorithms to regularize EDMD or to discover eigenfunctions directly in an implicit formulation.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We further demonstrate the importance of model validation to distinguish accurately identified eigenfunctions from spurious ones. Lightly damped eigenfunctions are often not corrupted and can be used to construct reduced-order Koopman models.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

These nonlinear control techniques generalize to *any* lightly damped eigenfunction. As a more sophisticated example, we consider the double gyre flow, which is a model for ocean mixing. The discovery of intrinsic coordinates for optimized nonlinear control establishes our data-driven KRONIC framework^22^2Code at shown in Fig. 2.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

\begin{overpic}[width=433.62pt]{} \put(32.5,12.5){Section~{}Sec:Regression} \put(73.5,12.5){Section~{}Sec:KRONIC} \end{overpic} Figure 2: Control of nonlinear systems via reduced Koopman-invariant representations in eigenfunction coordinates.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

The present work is outlined as follows: In Sec. 2, we demonstrate the importance of eigenfunction validation and motivate the use of sparse regression for their discovery. In Sec. 3, key results in Koopman spectral theory and corresponding data-driven approaches are summarized, and a brief background on optimal control is provided. The approach for identifying of Koopman eigenfunctions from data using sparse regression is outlined in Sec. 5. In Sec. 4, it is shown how control can be incorporated in the eigenfunction formulation. An analytical example is examined in Sec. 6 to illustrate the control problem in terms of Koopman eigenfunction coordinates. The KRONIC framework is then demonstrated on several Hamiltonian systems (Sec. 7), for basin-hopping in an asymmetric double potential well (Sec. 8), and the autonomous and non-autonomous double gyre flow (Sec. 9). A discussion and outlook on future directions is provided in Sec. 10.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Motivation", "weight": 1.0} -->

Finite-dimensional approximations of the Koopman operator are typically obtained as its projection onto a specified basis or dictionary. Extended dynamic mode decomposition (EDMD) has emerged as the leading numerical approach by solving a least-squares problem. A well-known issue arises when trying to identify the full operator in a finite set of basis functions, that sometimes the finite-dimensional approximation is not closed and spurious eigenfunctions may appear. For this reason, it can be important to perform consistency checks, such as validating the linearity property of eigenfunctions. The present work builds on EDMD addressing this limitation by re-formulating the regression problem for the direct identification of Koopman eigenfunctions. Further, we demonstrate how EDMD may be regularized to obtain more accurate eigenfunction representations. In the following, we illustrate the closure problem using a polynomial basis. As a motivating example (examined in detail in Sec. 6), we consider a system with quadratic nonlinearity that gives rise to a slow manifold: with $\mu = {- 0.1}$ and $\lambda = {- 1}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Motivation", "weight": 1.0} -->

By a clever choice of observable functions $\mathbf{y}$, the nonlinear system may be represented as a linear system: where $\mathbf{K}$ represents a finite-dimensional approximation of the Koopman operator. The system is one of few analytical examples, for which a closed, finite-dimensional, linear Koopman approximation exists.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Motivation", "weight": 1.0} -->

The EDMD model fit on the first $9$ monomials (up to third degree) is shown in Fig. 3(a).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Motivation", "weight": 1.0} -->

Some of the eigenvectors are *spurious* (see Fig. 3(c)), i.e. the evolution of the eigenfunction $\varphi{({\mathbf{x}{(t)}})}$ obtained by evaluating the eigenfunction on a trajectory $\mathbf{x}{(t)}$ does not correspond to the linear prediction using the eigenvalue, $e^{\lambdat}\varphi{({\mathbf{x}{(t_{0})}})}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Motivation", "weight": 1.0} -->

These additional terms, that are not in the span of $\{ y_{1},\cdots,y_{9}\}$, will be *aliased* in the corresponding row equations corrupting the system matrix $\mathbf{K}$. Thus, some of the eigenfunctions will be spurious, affecting the prediction accuracy of the model based on $\mathbf{K}$. However, it may be possible to identify a subset of the eigenfunctions that are not corrupted, e.g. those eigenpairs that show good agreement in Fig. 3(c), and use these to construct a reduced-order model with improved prediction. Alternatively, EDMD may be regularized using sparsity-promoting techniques to regress a (approximate) closed model on a subset of basis functions.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Motivation", "weight": 1.0} -->

For instance, choosing the five observable functions ${(y_{1},y_{2},y_{3},y_{4},y_{5})} = {(x_{1},x_{2},x_{1}^{2},{x_{1}x_{2}},x_{1}^{3})}$, which are a subset of the nine monomials used above, yields: which is a 5-dim. linear system, that remains closed under the action of the Koopman operator.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Motivation", "weight": 1.0} -->

Measurements from real-world systems are generally corrupted by noise, which can be more challenging for model identification procedures. Figure 4(c) shows the poor prediction performance of the EDMD model trained on noisy data (displayed in Fig. 4(a)).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Motivation", "weight": 1.0} -->

More eigenfunctions are inaccurate as a result of an increasing number of non-vanishing coefficients in the state matrix compared with the noise-free situation in Fig. 3. The least-squares solution overfits resulting in a full matrix with small, but non-vanishing coefficients. By sparsifying the EDMD state matrix or constructing a reduced-order model based on accurate eigenfunctions (validated from Fig. 4(b)) higher prediction accuracy and robustness to noise can be achieved (compare models in Figure 4(c)). Ideally, it would be possible to learn *good* eigenfunctions directly, which are designed to behave linearly and evolve as predicted by their associated eigenvalue, which would potentially significantly increase prediction accuracy and reduce the dimension of the model.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Koopman spectral theory", "weight": 1.0} -->

The classical geometric theory of dynamical systems considers a set of coupled ordinary differential equations in terms of the state of the system $\mathbf{x} \in \mathcal{M}$, where $\mathcal{M}$ is a differentiable manifold, often given by $\mathcal{M} = {\mathbb{R}}^{n}$. In discrete time, the dynamics are given by where $\mathbf{F}$ may be the flow map of the dynamics: Discrete-time systems are more general and form a superset, containing those induced by continuous-time dynamics. Moreover, discrete-time dynamics are often more consistent with experimental measurements, and may be preferred for numerical analysis. The geometric perspective then considers fixed points and invariant structures of the dynamics.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Koopman spectral theory", "weight": 1.0} -->

In 1931, B. O. Koopman introduced the operator theoretic perspective, showing that there exists an infinite-dimensional linear operator, given by $\mathcal{K}$, that acts to advance all measurement functions $g:{\mathcal{M}\rightarrow{\mathbb{R}}}$ of the state with the flow of the dynamics: Thus, the Koopman operator advances measurements linearly: For smooth dynamics, there is a continuous system where $\mathcal{K}$ is the infinitesimal generator of the one-parameter family of Koopman operators $K$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Koopman spectral theory", "weight": 1.0} -->

The Koopman operator is linear, which is appealing, but is infinite dimensional, posing issues for representation and computation. Instead of capturing the evolution of all measurement functions in a Hilbert space, applied Koopman analysis approximates the evolution on a subspace spanned by a finite set of measurement functions. It is possible to obtain a finite-dimensional matrix representation of the Koopman operator by restricting it to an invariant subspace. A Koopman invariant subspace is spanned by any set of eigenfunctions of the Koopman operator. A Koopman eigenfunction $\varphi{(\mathbf{x})}$ corresponding to eigenvalue $\lambda$ satisfies In continuous-time, a Koopman eigenfunction ${\varphi{(\mathbf{x})}}:{\mathcal{M}\rightarrow{\mathbb{C}}}$ satisfies Obtaining Koopman eigenfunctions from data or analytically is a central applied challenge in modern dynamical systems. Discovering these eigenfunctions enables globally linear representations of strongly nonlinear systems in terms of these *intrinsic* observables.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Koopman spectral theory", "weight": 1.0} -->

The evolution equation describes the unactuated behavior, which will be extended to incorporate the effect of control in our KRONIC framework (compare the third box in Fig. 2 and for further details we refer to Sec. 4 and 5).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Dynamic mode decomposition", "weight": 1.0} -->

Dynamic mode decomposition (DMD) is a simple numerical algorithm that approximates the Koopman operator with a best-fit linear model that advances measurements from one time step to the next. DMD was originally introduced in the fluid dynamics community to decompose large data sets into dominant spatial-temporal coherent structures, and a connection with Koopman theory was soon established. In addition to fluid dynamics, DMD has been widely applied to a range of problems in neuroscience, robotics, epidemiology, and video processing. The DMD algorithm has also been extended to include sparsity and compressed sensing, actuation and control, multi-resolution analysis, de-noising, and streaming variants.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Dynamic mode decomposition", "weight": 1.0} -->

In DMD, the infinite-dimensional Koopman operator in is approximated with a finite-dimensional matrix $\mathbf{A}$ that advances the system state $\mathbf{x}$: Given data from a nonlinear system, it is possible to stack snapshots into a matrix $\mathbf{X} = {\lbrack{\mathbf{x}_{1}\mathbf{x}_{2}\ldots\mathbf{x}_{m - 1}}\rbrack}$ and a time-shifted matrix $\mathbf{X}^{'} = {\lbrack{\mathbf{x}_{2}\mathbf{x}_{3}\ldots\mathbf{x}_{m}}\rbrack}$. In terms of these data matrices, becomes Various DMD algorithms then compute the leading eigendecomposition of the best-fit linear operator $\mathbf{A}$, given by where $\parallel \cdot \parallel_{F}$ is the Frobenius norm.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Dynamic mode decomposition", "weight": 1.0} -->

The best-fit $\mathbf{A}$ is given by $\mathbf{A} = {\mathbf{X}^{'}\mathbf{X}^{\dagger}}$, where $\dagger$ is the pseudo-inverse, which is computed via singular value decomposition.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Dynamic mode decomposition", "weight": 1.0} -->

DMD has proven to be an extremely useful technique for the analysis of high-dimensional dynamical systems data. However, DMD is based on linear measurements of the system, which do not typically span a Koopman-invariant subspace of a general nonlinear system. For example, a linear DMD model may perfectly capture the periodic attractor dynamics of a system on a limit cycle, but will fail to capture the nonlinear transients if the system is perturbed off the attractor. DMD has since been augmented with nonlinear measurements to enrich the model in EDMD and VAC. EDMD models have been used with success for estimation and model predictive control. However, EDMD models are based on a large set of nonlinear measurements of the state, and there is no guarantee that these measurements form a Koopman invariant subspace. In fact, EDMD measurement subspaces will generally *not* be closed.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Dynamic mode decomposition", "weight": 1.0} -->

For example, there is no finite-dimensional Koopman invariant subspace that includes the state of the system $\mathbf{x}$ for any dynamical system that has multiple attractors (e.g., fixed points, periodic orbits, etc.), since the resulting finite-dimensional linear model cannot be topologically conjugate to the original dynamics. This is closely related to the representation of the Koopman operator in a polynomial basis, similar to Carleman linearization. Thus, EDMD as well as other models are often plagued with spurious eigenfunctions that do not behave linearly as predicted by the associated eigenvalue. Fortunately, although these models may have corrupted eigenvalues and eigenfunctions, eigenfunctions corresponding to lightly damped eigenvalues may be faithfully extracted.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Optimal control", "weight": 1.0} -->

The overarching goal of Koopman control is to reformulate strongly nonlinear dynamics in a linear framework to enable the use of powerful optimal and robust control techniques available for linear systems. Here, we summarize key results in optimal control theory that will be used for control in Koopman eigenfunction coordinates. We consider the nonlinear system affected by an external input with multi-channel control input $\mathbf{u} \in {\mathbb{R}}^{q}$ and continuously differentiable dynamics ${{\mathbf{f}}{(\mathbf{x},\mathbf{u})}}:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{q}}\rightarrow{\mathbb{R}}^{n}}$. Without loss of generality, the origin is an equilibrium: ${{\mathbf{f}}{(\mathbf{0},\mathbf{0})}} = \mathbf{0}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Optimal control", "weight": 1.0} -->

Infinite-horizon optimal control minimizes the following quadratic cost functional with state and input weight matrices $\mathbf{Q} \in {\mathbb{R}}^{n \times n}$ and $\mathbf{R} \in {\mathbb{R}}^{q \times q}$. Both matrices are symmetric and fulfill $\mathbf{Q} > 0$ and $\mathbf{R} \geq 0$. A full-state feedback control law with gain $\mathbf{C}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{q \times n}}$ is sought that minimizes the cost function subject to the state dynamics to drive the system to the origin, i.e. ${\lim\limits_{t\rightarrow\infty}{\mathbf{x}{(t)}}} = {\mathbf{0},{\forall\mathbf{x}}}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Koopman operator control in eigenfunctions", "weight": 1.0} -->

We now propose a general control architecture in Koopman eigenfunction coordinates, referred to as *Koopman Reduced Order Nonlinear Identification and Control* (KRONIC)(see Fig. 2). This eigenfunction perspective relies on a model constructed from validated Koopman eigenfunctions, which is closed and linear by design. First, we derive how the effect of actuation affects the dynamics of these eigenfunction coordinates. Second, the optimal control problem is formulated in these coordinates and a corresponding feedback controller is then developed, yielding a possibly nonlinear control law in the original state variables. Control in eigenfunction coordinates is quite general, encompassing the stabilization of fixed points and periodic orbits, e.g. via the Hamiltonian eigenfunction, or the manipulation of more general spatial-temporal coherent structures given by level sets of other eigenfunctions.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Control--affine systems", "weight": 1.0} -->

We first examine how adding control to a dynamical system affects a single Koopman eigenfunction. This formulation then readily generalizes to multiple eigenfunctions. Consider a control-affine system with a multi-channel input $\mathbf{u} \in {\mathbb{R}}^{q}$, continuously differentiable dynamics ${{\mathbf{f}}{(\mathbf{x})}}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n}}$ associated with the unforced dynamics, and each $\mathbf{b}_{i}{(\mathbf{x})}$ is a vector field acting on the state space.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Control--affine systems", "weight": 1.0} -->

Starting with the Koopman operator associated with the uncontrolled, autonomous system (see Sec. 3.1), we examine how the control terms in affect the dynamics of its eigenfunctions. By applying the chain rule, we obtain This equation differs from Eq. in the additional second term associated with the control terms. The $\varphi{(\mathbf{x})}$ is a Koopman eigenfunction associated with the autonomous Koopman operator for the unforced dynamics $\mathbf{f}{(\mathbf{x})}$. For instance, a Hilbert space of the Lebesque square-integrable functions may be considered as function space. The control enters the dynamics of $\varphi$ via the additional term leading to a control-affine system, which is linear in $\varphi$ and possibly nonlinear in the control.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Control--affine systems", "weight": 1.0} -->

Without loss of generality, we assume in the examples presented in later sections a linear control term: with control matrix $\mathbf{B} \in {\mathbb{R}}^{n \times q}$, so that the dynamics of the eigenfunctions become

<!-- chunk {"id": "body-0040", "role": "body", "section": "Nonaffine control systems", "weight": 1.0} -->

More generally, we may be interested in the control of a nonlinear, non-affine system: with continuously differentiable dynamics ${{\mathbf{f}}{(\mathbf{x},\mathbf{u})}}:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{q}}\rightarrow{\mathbb{R}}^{n}}$. We may now consider an observable $g{(\mathbf{x},\mathbf{u})}$ as a function of the extended state space $\mathcal{M} \times \mathcal{U}$, where $\mathbf{x} \in \mathcal{M}$ and $\mathbf{u} \in \mathcal{U}$, and the non-autonomous Koopman operator acting on these observables.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Nonaffine control systems", "weight": 1.0} -->

For discrete-time dynamics with discrete map $\mathbf{F}{(\mathbf{x},\mathbf{u})}$, the Koopman operator propagates scalar measurements according to ${Kg{(\mathbf{x}_{k},\mathbf{u}_{k})}} = {g{({\mathbf{F}{(\mathbf{x}_{k},\mathbf{u}_{k})}},\mathbf{u}_{k + 1})}}$ by assuming the Koopman operator acts on the extended state space in the same manner as the Koopman operator associated with the autonomous, unforced system. This assumption has been previously considered, where the extended space was defined as the product of the original state-space and the space of all control sequences. Since the first appearance of this article, they have been further studies examining the approximation of the Koopman operator for the non-affine control system.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Nonaffine control systems", "weight": 1.0} -->

In, it is in more detail discussed how the Koopman operator formulation can be modified based on the dynamics of $\mathbf{u}$ itself, e.g. open-loop versus closed-loop control. As associated function space, in which observables are defined on the extended state space, a Hilbert space of the Lebesque square-integrable functions or polynomial functions defined on a compact set may be considered. If the dynamics on $\mathbf{u}$ are governed by a specific feedback law of the form $\mathbf{u} = {\mathbf{C}{(\mathbf{x})}}$, that is only a function of the state $\mathbf{x}$, then choices about the function space for the controlled system are equivalent to those applying to the autonomous system.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Nonaffine control systems", "weight": 1.0} -->

Instead, we may specify that $\varphi{(\mathbf{x},\mathbf{u})}$ reduces to the eigenfunction $\varphi{(\mathbf{x},\overline{\mathbf{u}})}$ of $\overset{˙}{\mathbf{x}} = {{\mathbf{f}}{(\mathbf{x},\overline{\mathbf{u}})}}$ for all locked $\overline{\mathbf{u}} \in \mathcal{U}$, as. In this case, the eigenfunction is *parametrized* by the input $\overline{\mathbf{u}}$ These are eigenfunctions of the parametrized Koopman generator, which is autonomous for each locked $\overline{\mathbf{u}}$ and can be defined on the commonly used function spaces as stated above. This perspective is also assumed within the gEDMD framework and its extension for control.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Nonaffine control systems", "weight": 1.0} -->

The Koopman generator $\mathcal{K}$ is approximated as a finite-rank matrix $\mathbf{K}$ parametrized by the discrete control input using EDMD. The control problem is then solved by optimizing switching times among the finite set of discrete control inputs and associated models.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Nonaffine control systems", "weight": 1.0} -->

If we augment the eigenfunction vector with the input $\mathbf{u}$, we obtain where we view $\overset{˙}{\mathbf{u}}$ as the input to the Koopman linear system, and the ${\nabla_{\mathbf{u}}\varphi}{(\mathbf{x},\mathbf{u})}$ matrix varies based on $\mathbf{x}$ and $\mathbf{u}$. Thus, we may enact a gain-scheduled control law.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Nonaffine control systems", "weight": 1.0} -->

Summarizing, if the original dynamics are nonlinear and control-affine, the dynamics in Koopman eigenfunction coordinates are control-affine and split into a linear part associated with the nonlinear unforced dynamics and a bilinear part associated with the control term. If the original dynamics are nonlinear and non-affine in the control, the eigenfunction dynamics can become linear if the Koopman operator is defined on the extended state. Considering practical implications, it is also possible to modify these dynamics so that these consist of a linear part and a bilinear control term as in Eq.. We also point out, that while the control is generally nonlinear in the state $\mathbf{x}$, it may become linear in the eigenfunction coordinates for special cases, such as ${{{\nabla\varphi}{(\mathbf{x})}} = {const}}.$

<!-- chunk {"id": "body-0047", "role": "body", "section": "Formulation of the optimal control problem", "weight": 1.0} -->

We now formulate the infinite-horizon, optimal control problem for a reduced set of Koopman eigenfunctions. The control objective is a quadratic cost functional: where ${\mathbf{φ}} = {\lbrack{\varphi_{1}\varphi_{2}\ldots\varphi_{r}}\rbrack}^{T}$ comprises $r$ eigenfunctions with $\varphi_{j}$ associated with eigenvalue $\lambda_{j}$. For this cost function to be equivalent to the cost in the original state $\mathbf{x}$, a modified weight matrix may be considered such that ${{\mathbf{φ}}^{T}\mathbf{Q}_{\varphi}{\mathbf{φ}}} \approx {\mathbf{x}^{T}{\mathbf{Q}\mathbf{x}}}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Formulation of the optimal control problem", "weight": 1.0} -->

This can only be achieved exactly if the state itself is an eigenfunction of the Koopman operator; however, it can be sufficient requiring this only for a subset of states that enter the cost function. Alternatively, it is possible to estimate $\mathbf{x}$ via the inverse mapping $\varphi^{- 1}$. Eigenfunctions may generally not be invertible exactly. Nevertheless, the inverse mapping may be approximated using multidimensional scaling as in or learned jointly with $\varphi$ itself using autoencoders. More generally, the matrix $\mathbf{Q}_{\varphi}$ allows one to weight particular eigenfunction directions, which are related to properties of the underlying system and coherent structures. The selection of a specific set of eigenfunctions, in which a model is constructed and which are used to formulate the cost functional, is problem specific.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Formulation of the optimal control problem", "weight": 1.0} -->

However, given a target state $\mathbf{x}^{REF}$ in the original state space, the associated target value of the eigenfunctions may be directly determined by evaluating the eigenfunctions on the target state, i.e. ${\mathbf{φ}}^{REF}:={{\mathbf{φ}}{(\mathbf{x}^{REF})}}$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Formulation of the optimal control problem", "weight": 1.0} -->

For the general case, it is possible to augment the state with the control input and include the derivative of the control as new input $\hat{\mathbf{u}}:=\overset{˙}{\mathbf{u}}$: with $q \times q$ identity matrix $\mathbf{I}_{q}$. This may be interpreted as integral control. The cost functional is then given by with some restrictions on $\hat{\mathbf{R}}$. Modifying the system structure, by moving the nonlinearity in the control term into the state dynamics, improves the tractability of the problem.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Formulation of the optimal control problem", "weight": 1.0} -->

In the following, we will focus on multiple-input, control-affine systems, for which the dynamics in intrinsic coordinates becomes with $\mathbf{\Lambda} = {{diag}{(\lambda_{1},\ldots,\lambda_{r})}}$. Depending on the structure of ${\mathbf{φ}}{(\mathbf{x})}$ and $\mathbf{B}$, the actuation matrix $\mathbf{B}_{\varphi} = {{{\nabla_{\mathbf{x}}{\mathbf{φ}}}{(\mathbf{x})}} \cdot \mathbf{B}}$ may be a function of $\mathbf{x}$. A state-dependent control term may be interpreted as a gain-scheduled control.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Formulation of the optimal control problem", "weight": 1.0} -->

A feedback controller is now sought in the Koopman representation of the form We may also consider reference tracking, $\mathbf{u} = {- {\mathbf{C}_{\varphi}{(\mathbf{x})}\left\lbrack {{{\mathbf{φ}}{(\mathbf{x})}} - {\mathbf{φ}}^{REF}} \right\rbrack}}$, with a modified cost functional. The objective is then to determine the gain function $\mathbf{C}_{\varphi}$ by minimizing $J{({\mathbf{φ}},\mathbf{u})}$ and the resulting control $\mathbf{u}$ may be directly applied to the original system, for which the control problem may be suboptimal.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Formulation of the optimal control problem", "weight": 1.0} -->

Generally, Koopman eigenfunction control can be used in two ways depending on which means of control one has access to: internally driven swimmers or particles, which state is given by $\mathbf{x}$ and which dynamics are subject to an external field, such as a fluid flow or magnetic field; or driving an external field, represented in terms of these eigenfunctions, in which these swimmers or particles drift.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Solving the optimal control problem", "weight": 1.0} -->

The model may be combined with any model-based control strategy. In the following, we discuss ways to solve the optimal control problem formulated above using standard techniques.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Solving the optimal control problem", "weight": 1.0} -->

In the simplest case, for which Eq. becomes fully linear, the optimal gain matrix $\mathbf{C}_{\varphi}$ can be determined by solving the associated algebraic Riccati equation leading to a linear quadratic regulator (LQR) formulated in Koopman eigenfunctions. For the more general case, where the control term becomes nonlinear, other techniques are required. A common extension of LQR for nonlinear systems considers state-dependent state and control matrices as outlined in Sec. A.3 and solves the state-dependent Riccati equation. Here, the state dynamics would be constant and linear, i.e. $\mathbf{A} = \mathbf{\Lambda}$, and only the control matrix $\mathbf{B}_{\varphi}:={\nabla_{\mathbf{x}}{\varphi \cdot \mathbf{B}}}$ depends on the state $\mathbf{x}$: We note that parametrizations for the dynamics in $\mathbf{x}$ are unique for scalar systems, but generally nonunique for multivariable systems.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Solving the optimal control problem", "weight": 1.0} -->

In contrast, the state-dependent dynamics in eigenfunction coordinates are unique with respect to $\mathbf{x}$ and $\mathbf{\Lambda}$ is constant. These are not a result from the factorization. The (non)uniqueness of the factorization is generally related to global optimal control and global optimal stability. However, further studies are required to connect these properties for solutions in eigenfunction coordinates to the state dynamics in $\mathbf{x}$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Solving the optimal control problem", "weight": 1.0} -->

We examine the effect of an error $\varepsilon\psi{(\mathbf{x})}$ in the representation of a Koopman eigenfunction, ${\hat{\varphi}{(\mathbf{x})}}:={{\varphi{(\mathbf{x})}} + {\varepsilon\psi{(\mathbf{x})}}}$, on its closed-loop dynamics based on and provide an upper bound for the error (for details see Appendix B). We assume control-affine dynamics of the underlying system, access to full-state measurements $\mathbf{x}$, and control vector fields are known. Further, we reformulate ${\mathbf{B}{(\mathbf{x})}\mathbf{u}}:={\sum_{i = 1}^{q}{\mathbf{b}_{i}{(\mathbf{x})}u_{i}}}$ for simplicity.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Solving the optimal control problem", "weight": 1.0} -->

For small $\varphi{(\mathbf{x})}$ the contribution of $\varepsilon\psi{(\mathbf{x})}$ becomes important/may be dominant.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Solving the optimal control problem", "weight": 1.0} -->

More generally, Koopman control in eigenfunction coordinates may be combined with any model-based control approach. Under certain conditions, it may also be possible to feedback linearize the dynamics. The data-driven identification of Koopman eigenfunctions can be challenging and they may only be approximated accurately in a certain domain. Further, dynamics may also drift away from the situations captured in the training data due to external disturbances. Especially in these cases it is advantageous to couple the resulting model with a receding horizon estimator and controller to adapt quickly to changing conditions. In particular, model predictive control has gained increasing popularity over the last decade due to its success in a wide range of applications and its ability to incorporate customized cost functions and constraints.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Identifying Koopman eigenfunctions from data", "weight": 1.0} -->

The overarching goal of this work is to control nonlinear systems in intrinsic Koopman eigenfunction coordinates. A leading method for approximating the Koopman operator is EDMD relying on a set of basis or dictionary functions. Here, we aim to address the well-known closure issue, i.e. the model may not be closed in the set of basis functions and can therefore have spurious eigenfunctions, by assuming an eigenfunction perspective. Approximating these eigenfunctions from data is an ongoing challenge. Building on EDMD, we propose a strategy to directly identify dominant Koopman eigenfunctions associated with lightly damped eigenvalues, that can then be utilized to construct low-dimensional, closed models. Further, we show that it is possible to sparsify the state-transition matrix $\mathbf{K}$ of EDMD to improve the representation of eigenfunctions within the selected basis.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Identifying Koopman eigenfunctions from data", "weight": 1.0} -->

It has long been recognized that numerical regularization via the truncation of the SVD in the computation of the pseudoinverse, as it is done for DMD/EDMD, is crucial to reduce noise corruption. However, this does not produce a sparser approximation of $\mathbf{K}$, which is crucial for systems that are inherently sparse in their representation. An additional $L1$ regularization is here advantageous as it is able to improve the predictive power of the model and eigenfunctions become more accurately represented in the chosen function library preventing overfitting. Interestingly, the infinitesimal generator of the Koopman operator may be sparse even when the Koopman operator itself is not. However, even in these cases, the approach may benefit from a sparsity constraint to counteract spurious non-zero entries arising from noise and numerical approximation. More generally, non-compactness or continuous spectra of the Koopman operator can pose issues for the numerical analysis requiring some form of regularization (see for a detailed discussion for the Koopman operator and regarding the Perron-Frobenius operator).

<!-- chunk {"id": "body-0062", "role": "body", "section": "Identifying Koopman eigenfunctions from data", "weight": 1.0} -->

In the following we formulate a framework using sparsity-promoting techniques to identify Koopman eigenfunctions directly building on the partial differential equation (PDE) governing the evolution of an eigenfunction. Applying the chain rule to yields Combined, this results in a linear PDE for the eigenfunction $\varphi{(\mathbf{x})}$: This formulation assumes continuous and differentiable dynamics and that the eigenfunctions are smooth.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Identifying Koopman eigenfunctions from data", "weight": 1.0} -->

Spectral properties of the Koopman operator have been shown to relate to intrinsic time scales, geometrical properties, and the long-term behavior of dynamical systems. It has been shown, that the evolution of observables can be described by a linear expansion in Koopman eigenfunctions for systems which consist only of the point spectrum, i.e. smooth dynamical systems exhibiting, e.g., hyperbolic fixed points, limit cycles and tori. If systems with a mixed spectrum are considered, it may be possible to restrict the following analysis to the point spectrum as.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Data-driven discovery of continuous-time eigenfunctions", "weight": 1.0} -->

Sparse identification of nonlinear dynamics (SINDy) is used to identify Koopman eigenfunctions for a particular value of $\lambda$. This formalism assumes that the system has a point or mixed spectrum, for which eigenfunctions with distinct eigenvalues exist. A schematic is displayed in Fig. 5.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Data-driven discovery of continuous-time eigenfunctions", "weight": 1.0} -->

First, we build a library of candidate functions: We choose $\mathbf{\Theta}$ large enough so that the Koopman eigenfunction may be well approximated in this library: Given data $\mathbf{X} = {\lbrack{\mathbf{x}_{1}\mathbf{x}_{2}\cdots\mathbf{x}_{m}}\rbrack}$, the time derivative $\overset{˙}{\mathbf{X}} = {\lbrack{{\overset{˙}{\mathbf{x}}}_{1}{\overset{˙}{\mathbf{x}}}_{2}\cdots{\overset{˙}{\mathbf{x}}}_{m}}\rbrack}$ can be approximated numerically from $\mathbf{x}{(t)}$ if not measured directly. The total variation derivative is recommended for noise-corrupted measurements.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Data-driven discovery of continuous-time eigenfunctions", "weight": 1.0} -->

It is then possible to construct $\mathbf{\Gamma}$ from data: For a specific eigenvalue $\lambda$, the Koopman PDE in may be evaluated on data, yielding: The formulation in is implicit, so that $\mathbf{ξ}$ will be in the null-space of the matrix ${\lambda\mathbf{\Theta}{(\mathbf{X})}} - {\mathbf{\Gamma}{(\mathbf{X},\overset{˙}{\mathbf{X}})}}$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Data-driven discovery of continuous-time eigenfunctions", "weight": 1.0} -->

The right null-space of for a given $\lambda$ is spanned by the right singular vectors of ${{\lambda\mathbf{\Theta}{(\mathbf{X})}} - {\mathbf{\Gamma}{(\mathbf{X},\overset{˙}{\mathbf{X}})}}} = {\mathbf{U}\mathbf{\Sigma}\mathbf{V}^{\ast}}$ (i.e., columns of $\mathbf{V}$) corresponding to zero-valued singular values. It is possible to identify the few active terms in an eigenfunction by finding the sparsest vector in the null-space, which is used, e.g., in the implicit-SINDy algorithm. This is a nonconvex approach based on alternating directions (adm) with linear scaling, which can be adapted to our problem. In this formulation, the eigenvalues $\lambda$ are not known *a priori*, and must be learned online along with the approximate eigenfunction.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Data-driven discovery of continuous-time eigenfunctions", "weight": 1.0} -->

In Alg. 1, we propose an implicit formulation, which starts with an initial guess of the eigenvalues given by the least-squares solution, and subsequently alternates between an searching for the sparsest vector in the null-space and updating of the eigenvalue. As the approach in depends on the initial condition, we evaluate all initial conditions given by each row in the nullspace $\mathbf{N}:={{null}{({{\mathbf{\Gamma}{(\mathbf{X},\overset{˙}{\mathbf{X}})}} - {\lambda\mathbf{\Theta}{(\mathbf{X})}}})}}$. An additional soft-thresholding with parameter $\alpha$ and validation on a test dataset is applied to select the best eigenvector for each initial condition. While the approach has been observed to converge to accurate eigenvalues in clean data, the found eigenvector in the solution set may not be unique.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Data-driven discovery of continuous-time eigenfunctions", "weight": 1.0} -->

This approach solves for each eigenpair separately; however, it may also be possible to extend it to solve for eigenpairs jointly which is part of ongoing research. From a practical standpoint, data in $\mathbf{X}$ does not need to be sampled from full trajectories, but can be obtained using more sophisticated strategies such as latin hypercube sampling or sampling from a distribution over the phase space. It may also be possible to directly identify a recursion relationship to obtain a power series expansion as shown in Appendix C and.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Data-driven discovery of continuous-time eigenfunctions", "weight": 1.0} -->

Koopman eigenfuntions and eigenvalues can also be determined as the solution to the eigenvalue problem ${{\mathbf{ξ}}_{\alpha}\mathbf{K}} = {\lambda_{\alpha}{\mathbf{ξ}}_{\alpha}}$, where $\mathbf{K} = {\mathbf{\Theta}^{\dagger}\mathbf{\Gamma}}$ is obtained via least-squares (LS) regression. While many eigenfunctions are spurious, i.e. these eigenfunctions do not behave linearly as predicted by the corresponding eigenvalue, those corresponding to lightly damped eigenvalues can be well approximated, and a reduced-order Koopman model may developed on these coordinates (see also Sec. 2). The accuracy of eigenfunctions of $\mathbf{K}$ can be improved, by improving the recovery of $\mathbf{K}$ itself, which can be achieved by sparsifying $\mathbf{K}$ directly.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Data-driven discovery of continuous-time eigenfunctions", "weight": 1.0} -->

The minimization problem, where $\rho$ is a regularization term that promotes the sparsity of $\mathbf{k}_{i}$, i.e. the number of non-zero coefficients, is solved separately for each row in $\mathbf{K} = {\lbrack\mathbf{k}_{1}^{T},\ldots,\mathbf{k}_{p}^{T}\rbrack}$. For instance, an $L_{1}$ constraint on the coefficients in $\mathbf{k}_{i}$ may be chosen and $\mathbf{k}_{i}$ may equivalently be determined as in SINDy. In general, the problem can be solved using standard techniques, such as LASSO, Least Angle Regression, or an iterated least-squares thresholding method.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Data-driven discovery of continuous-time eigenfunctions", "weight": 1.0} -->

This formulation is closely related to the gEDMD framework, a generalization of the EDMD method to approximate the infinitesimal generator of the Koopman operator. The gEDMD least-squares formulation is solved here row-wise with an additional sparsity constraint. There are also similarities to sparsity-promoting DMD and variants, which aims to reconstruct a signal through a sparse combination of modes/eigenfunctions, which have been computed from a least-squares solution. In contrast to these works, we argue that the sparse representation of eigenfunctions themselves should be promoted. Alternatively, it is also possible to use the dominant terms in accurately identified eigenfunctions, generally associated with lightly damped eigenvalues, as guidance to select observables to regress. Since the first appearance of this article, further promising methods have been proposed to identify Koopman eigenfunctions directly.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Data-driven discovery of discrete-time eigenfunctions", "weight": 1.0} -->

In discrete-time, an eigenfunction evaluated at a number of data points in $\mathbf{X}$ will satisfy: Again, searching for such an eigenfunction $\varphi{(\mathbf{x})}$ in a library $\mathbf{\Theta}{(\mathbf{x})}$ yields the matrix system: where $\mathbf{X}' = \begin{bmatrix} \mathbf{x}_{2} & \mathbf{x}_{3} & \cdots & \mathbf{x}_{m + 1} \end{bmatrix}$ is a time-shifted matrix. This formalism directly identifies the functional representation of a Koopman eigenfunction with eigenvalue $\lambda$.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Data-driven discovery of discrete-time eigenfunctions", "weight": 1.0} -->

If we seek the best *least-squares* fit to, this reduces to the extended DMD formulation: Again, it is necessary to confirm that predicted eigenfunctions actually behave linearly on trajectories.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Koopman model reduction and validation", "weight": 1.0} -->

For any data-driven modeling framework cross-validation is critical to ensure predictive and generalization capabilities. Approximations of the Koopman operator allow a systematic evaluation based on its linearity property. We can learn a finite-rank approximation using any EDMD-like method or learn eigenfunctions directly. In either case, it is critical to validate that any candidate eigenfunction $\varphi{({\mathbf{x}{(t)}})}$ actually behaves linearly on trajectories $\mathbf{x}{(t)}$ as the eigenvalue $\lambda$ predicts. The error of an eigenfunction can be defined as evaluated on a test trajectory $\mathbf{x}{(t)}$ and identified eigenfunctions can be ranked according to the error $E$. All eigenfunctions with error below a threshold may then be used to construct a reduced-order model: analogous to Eq.. This model is closed and behaves linearly by design and we demonstrate in the following its increased predictive power.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Identification of eigenfunctions and models", "weight": 1.0} -->

We consider a system with quadratic nonlinearity that gives rise to a slow manifold: with $\mu = {- 0.1}$ and $\lambda = {- 1}$. In the following, we apply the methods outlined in Sec. 5 to the dynamical system. For all models, a library of the first $9$ monomials (up to the third degree) is considered. Noise corruption in measurement data can be particularly problematic. Here, we examine the recovery of eigenfunctions and prediction performance for different noise magnitudes $\eta = 0.1$ and $\eta = 0.9$. Further, reduced-order models are constructed based on eigenpairs $(\beta,{\varphi{(\mathbf{x})}})$ that are deemed accurate, i.e. have a small $L_{2}$ error when compared with the prediction using the associated eigenvalue, here denoted by $\beta$. The threshold for the selection of eigenfunctions is $1$ and $3$ for noise magnitudes $\eta = 0.1$ and $\eta = 0.9$, respectively.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Identification of eigenfunctions and models", "weight": 1.0} -->

The $L_{1}$ regularized problem is solved using the iterative least-squares thresholding algorithm (ITLS) as in SINDy and least angle regression (LARS); however, detailed results are only shown for LARS as these have equivalent performance. LARS has the advantage that the number of iterations scales with the number of candidate functions; only $10$ iterations are required here. The sparse solution is then selected when there is minimal improvement in the absolute value of correlation with the evolving residual. The soft thresholding parameter in the implicit formulation is set to $\alpha = 0.1$ and $\alpha = 0.2$ for $\eta = 0.1$ and $\eta = 0.9$, respectively.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Identification of eigenfunctions and models", "weight": 1.0} -->

The results are displayed in Figs. 6 and 7 for the two noise cases. We observe that with increasing noise level, the EDMD state transition matrix becomes denser due to overfitting (see (d)). In contrast, the implicit approach and $L_{1} -$regularized EDMD (termed 'LARS' or 'ITLS' in the following) yield sparse matrices, which is more apparent for large noise magnitude. Note that the state matrix for the implicit formulation is reconstructed using the identified eigenfunctions on the set of candidate functions for visualization purposes, i.e. there are many zero entries and candidate functions that do not contribute to the actual dynamics. Lightly damped eigenfunctions can be recovered for all approaches. Eigenfunctions, or specifically eigenpairs $(\beta,{\varphi{(\mathbf{x})}})$, are deemed as recovered, if the prediction error falls below a threshold (marked as dashed line in (f)).

<!-- chunk {"id": "body-0079", "role": "body", "section": "Identification of eigenfunctions and models", "weight": 1.0} -->

The prediction error is computed by evaluating the eigenfunction on a test trajectory and comparing it with the evolution as predicted by the associated eigenvalue; the evolution is displayed in (e). These *good* eigenpairs (colored as blue bars in (f)) are then used to construct reduced-order models (ROMs), that are by design linear and closed (subject to small errors). Note that solution from the implicit formulation may not be unique, i.e. there are several identical eigenpairs. However, only unique eigenpairs are used to construct the reduce-order model. This is the reason why, e.g. in Fig. (f), the error for all eigenpairs falls below the threshold, but only unique ones (marked in blue) are selected to construct the ROM.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Identification of eigenfunctions and models", "weight": 1.0} -->

For small noise magnitude (Fig. 6), the identified models and ROMs perform all well, except the EDMD-based ROM, as one crucial eigenfunction associated with $\beta = {- 0.19}$ falls above the threshold and is not selected. The eigenvalue is correct, but not the associated eigenfunction. If the eigenfunction is included in the model (yellow bar in (f) and yellow dashed line in (g)), i.e. the model is constructed from blue and yellow marked eigenpairs, it yields a similar performance as the full-state EDMD model. It can also be observed that even in the low noise setting sparsification yields improvements. We note that the full-state model and ROM obtained from the implicit formulation are identical, as all discovered eigenpairs fall below the threshold (in (f)) and only unique pairs are selected to construct either model. We note that the 4D-ROM from the implicit formulation can achieve better accuracy with one dimension lower compared with EDMD and the sparse EDMD model identified using LARS.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Identification of eigenfunctions and models", "weight": 1.0} -->

Moreover, while all eigenpairs from the implicit formulation are accurate, both EDMD and LARS yield also non-physical eigenfunctions. The overall $L_{2}$ prediction error on the test trajectory in the original state is summarized for the full-state models and ROMs in (b) and (c), respectively.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Identification of eigenfunctions and models", "weight": 1.0} -->

For higher noise levels (Fig. 7), the performance differences become more apparent. LARS still yields several more accurate eigenfunctions than EDMD, so that LARS and the LARS-ROM significantly outperform EDMD and the EDMD-based ROM. The performance of EDMD does not improve here by truncating the SVD when computing the pseudo-inverse. The implicit formulation is more noise sensitive, as it is searching for eigenfunctions in the nullspace of a matrix 42, and is only able to discover one accurate eigenfunction. Interestingly, despite this caveat, the 2D model is able to outperform EDMD and the EDMD-based ROM. The implicit model is unable to predict the exact transient behavior; however, it accurately predicts the convergence to the steady state. The implicit ROM model, however, is insufficient with just one eigenfunction ${\varphi{(\mathbf{x})}} = x_{1}$ and is unable to predict the evolution of the second state $x_{2}$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Identification of eigenfunctions and models", "weight": 1.0} -->

When selecting one or two additional eigenfunctions for the EDMD-based ROM (in yellow shown in (g) for two additional eigenfunctions, i.e. in total six eigenfunctions marked by blue and yellow in (f)), the prediction performance improves considerably, although it is still unable to predict the steady-state behavior.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Identification of eigenfunctions and models", "weight": 1.0} -->

Summarizing, EDMD is suffering from overfitting and sparsity-promoting formulations can yield significant performance enhancements. Model validation in terms of eigenfunctions is a crucial step and can be used to construct better performing and lower-dimensional reduced-order models. More generally, these results also demonstrate the importance of not just selecting *good*, but also the *right* eigenfunctions.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Control design", "weight": 1.0} -->

We now demonstrate control in intrinsic Koopman coordinates for the controlled system: where the control vector is $\mathbf{B} \in {\mathbb{R}}^{2}$. This system can be represented as a finite-dimensional, linear system in a special choice of observable functions, making it amenable to optimal control. KRONIC in intrinsic coordinates provides a powerful alternative if the system does not allow for a fully controllable, linear representation.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Control design", "weight": 1.0} -->

The system exhibits slow and fast dynamics for ${|\lambda|} \ll {|\mu|}$ and has a single fixed point at the origin. This nonlinear system can be embedded in a higher-dimensional space ${(y_{1},y_{2},y_{3})} = {(x_{1},x_{2},x_{1}^{2})}$ where the unforced dynamics form a closed linear system in a Koopman-invariant subspace: However, $\mathbf{B}_{y}$ may be a function of $\mathbf{y}$, and hence of state $\mathbf{x}$, depending on the specific choice of $\mathbf{B}$.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Control design", "weight": 1.0} -->

Koopman eigenfunctions of the unforced system, i.e. $\mathbf{B} \equiv {\lbrack 0\,\, 0\rbrack}^{T}$, are $\varphi_{\mu} = x_{1}$ and $\varphi_{\lambda} = {x_{2} - {bx_{1}^{2}}}$ with $b = \frac{\lambda}{\lambda - {2\mu}}$ with eigenvalues $\lambda$ and $\mu$, respectively. These eigenfunctions remain invariant under the Koopman operator $\mathbf{K}$ and can be interpreted as intrinsic coordinates.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Control design", "weight": 1.0} -->

The dynamics of the Koopman eigenfunctions are affected by the additional control term $\mathbf{B} \neq {\lbrack 0\,\, 0\rbrack}^{T}$ according to (see also Eq.) Here, the first term represents the unforced, uncoupled, linear dynamics of the eigenfunctions and the second term a possibly state-dependent control term $\nabla{{\mathbf{φ}} \cdot \mathbf{B}}$, that incorporates the effect of control on each eigenfunction.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Control design", "weight": 1.0} -->

The controller shall stabilize the unstable fixed point at the origin if either $\mu$ or $\lambda$ are unstable. The control objective is to minimize the quadratic cost function with $\mathbf{Q} = \begin{bmatrix} \end{bmatrix}$ and $R = 1$, weighing state and control expenditures equally. Analogously, we can define a cost function in observable functions, and in intrinsic coordinates, Here, $\mathbf{Q}_{y}$ and $\mathbf{Q}_{\varphi}$ are chosen to yield the same cost in $\mathbf{x}$. Linear optimal control is then directly applied to to derive the control law, which is then incorporated.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Control design", "weight": 1.0} -->

The controller is linear in $\mathbf{y}$ and $\mathbf{φ}$ and yields a nonlinear controller in the state $\mathbf{x}$: where $\mathbf{C}_{y} \in {\mathbb{R}}^{1 \times 3}$ and $\mathbf{C}_{\varphi} \in {\mathbb{R}}^{1 \times 3}$ are the control gain vectors in observable or intrinsic coordinates, respectively.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Stabilization with unstable fast dynamics", "weight": 1.0} -->

First, we consider the system with $\mu = {- 0.1}$ and $\lambda = 1$ with an unstable $x_{2}$ direction. The control vector is $\mathbf{B} = {\lbrack 0\;1\rbrack}^{T}$, resulting in a constant vector in $\mathbf{y}$ or $\mathbf{φ}$ coordinates, $\mathbf{B}_{y} = \mathbf{B}_{\varphi} = {\lbrack 0\;1\;0\rbrack}^{T}$. Note that the first direction is uncontrollable, but also stable.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Stabilization with unstable fast dynamics", "weight": 1.0} -->

Standard LQR results are compared (see Fig. 8) for the linearized dynamics, truncated Koopman system in $\mathbf{y}$, truncated Koopman system in $\mathbf{φ}$ (KRONIC), as well as with feedback linearization ($u_{FL} = {{\lambdax_{1}^{2}} - {\mathbf{C}_{FL}\mathbf{x}}}$) and with numerically solving the nonlinear control problem as a two-point boundary value problem (TPBV), with performance evaluated in terms of the cumulative cost ${\hat{J}}_{x}^{t} = {\sum_{\tau = 0}^{t}{J_{x}{(\tau)}}}$. Both controllers, in observable functions and intrinsic coordinates, achieve the same performance and outperform linearized LQR and feedback linearization. The results for the truncated Koopman system in observables correspond to those presented.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Stabilization with unstable fast dynamics", "weight": 1.0} -->

There is no difference between those results and the control results of the system in intrinsic coordinates, as these systems are connected via an invertible linear transformation. One advantage of a formulation in intrinsic coordinates will become apparent in the next case, where the stable and unstable directions are reversed.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Stabilization with unstable slow dynamics", "weight": 1.0} -->

We now consider where the stable and unstable directions are reversed, i.e. $\mu = 0.1$ and $\lambda = {- 1}$. The control input now affects the first state $x_{1}$ with $\mathbf{B} = {\lbrack 1\;0\rbrack}^{T}$, otherwise this state is uncontrollable. As elaborated, in this case the linear system in observables will become nonlinear in the control term and, more importantly, will become unstabilizeable as the third state $y_{3}$ has a positive eigenvalue $2\mu$. Analogously, the Koopman system in intrinsic coordinates has an uncontrollable, unstable direction in $\varphi_{2\mu}$.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Stabilization with unstable slow dynamics", "weight": 1.0} -->

However, the dynamics of the Koopman eigenfunctions are uncoupled, thus the third direction can be discarded and the controller is developed in the controllable subspace: Note that the third direction $\phi_{2\mu}{(x)}$ is a harmonic of $\phi_{\mu}{(x)}$, i.e., $\phi_{2\mu} = \phi_{\mu}^{2}$. Thus, these two directions may not be independently controllable with a single input. Here, the controller for $\mathbf{x}$ is determined by solving the SDRE (see Sec. 4.3) at each time instant to account for the nonlinear control term. In a truncated Koopman eigenfunction system like in this example, the weights in $J_{\mathbf{φ}}$ can generally not be modified to directly replicate the cost $J_{\mathbf{x}}$.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Stabilization with unstable slow dynamics", "weight": 1.0} -->

Performance results are summarized in Fig. 9. It is also possible to combine KRONIC with MPC allowing for more general objective functions. Then, the control could be formulated in terms of $J_{\mathbf{x}}$ by computing the inverse ${\mathbf{φ}}^{- 1}:{{\mathbb{R}}^{r}\rightarrow{\mathbb{R}}^{n}}$ if it exists or estimating $\mathbf{x}$ from $\mathbf{φ}$ using, e.g., multidimensional scaling as. Control in Koopman intrinsic coordinates allows one to discard uncontrollable, unstable directions, for which standard control toolboxes such as Matlab's lqr fail. Note that feedback linearization fails in this case too: The control law is of the form $u_{FL} = {x_{1}^{- 1}\mathbf{C}_{FL}\mathbf{x}}$. As the system approaches the origin, the control input becomes unboundedly large.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Example: Hamiltonian energy control", "weight": 1.0} -->

\begin{overpic}[width=433.62pt]{} \end{overpic} Figure 10: KRONIC demonstrated for several Hamiltonian systems.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Example: Hamiltonian energy control", "weight": 1.0} -->

Conserved quantities, such as the Hamiltonian, are Koopman eigenfunctions associated with the eigenvalue $\lambda = 0$. Hamiltonian systems represent a special class of systems for which we can easily discover a Koopman eigenfunction directly from data.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Example: Hamiltonian energy control", "weight": 1.0} -->

The dynamics of a Hamiltonian system are governed by where $\mathbf{q}$ and $\mathbf{p}$ are the generalized state and momenta vectors, respectively. The Hamiltonian $\mathcal{H} = {\mathcal{H}{(\mathbf{q},\mathbf{p})}}$ considered here is time-independent, representing the conserved energy in the system. Trajectories of the system evolve on constant energy hypersurfaces $\{{(\mathbf{q},\mathbf{p})}:{{\mathcal{H}{(\mathbf{q},\mathbf{p})}} = \mathcal{E}}\}$, which may be interpreted as oscillatory modes. Thus, energy level stabilization is a form of oscillation control and corresponds to stabilizing invariant manifolds in phase space. Also nonlinear fixed point stabilization may correspond to stabilizing a particular value of the Hamiltonian energy.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Example: Hamiltonian energy control", "weight": 1.0} -->

We may develop the control directly for the eigenfunction equation where $\varphi = \mathcal{H}$. This equation also represents the energy conservation law of the system: A change in the energy, i.e. the Hamiltonian, corresponds to the external supplied work via $\mathbf{u}$. The infinite-time horizon cost function to be minimized is $J = {{\lim_{t\rightarrow\infty}{\frac{1}{2}{\int_{0}^{t}{Q\left({\mathcal{H}{({\mathbf{x}{(t)}})}} \right)^{2}}}}} + {\mathbf{u}^{T}{(t)}{\mathbf{R}\mathbf{u}}{(t)}dt}}$ with scalar $Q$ penalizing energy deviations and $\mathbf{R}$ penalizing the cost expenditure.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Example: Hamiltonian energy control", "weight": 1.0} -->

Assuming a single input $u$, the control law is given by $u = {- {{sign}{(B_{\mathcal{H}})}\sqrt{Q/R}\mathcal{H}{(\mathbf{x})}}}$ feeding back the current energy level $\mathcal{H}{(\mathbf{x})}$. The ratio $Q/R$ determines how aggressive the controller is. A more aggressive controller, with $Q > R$, leads to a faster but also more costly convergence to the desired state, and vice versa. For the specific case $Q = R$, the control law reduces further to $u = {- {{sign}{(B_{\mathcal{H}})}\mathcal{H}{(\mathbf{x})}}}$. Note that this feedback control law is linear in the Hamiltonian function, but nonlinear in the state $\mathbf{x}$.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Example: Hamiltonian energy control", "weight": 1.0} -->

In the following, we demonstrate the control approach for several Hamiltonian systems by solving the SDRE; an overview is provided in Fig. 10, where colored curves represent Koopman controlled trajectories. We assume $Q = R = 1$ for all examples.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Frictionless pendulum", "weight": 1.0} -->

Koopman control has improved performance over an LQR controller based on linearized dynamics near the center.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Frictionless pendulum", "weight": 1.0} -->

We further compare the controller resulting from solving the state-dependent Riccati equation with an energy-based control (EC), which is developed from physical considerations: If the functional representation of the Koopman eigenfunction, or specifically here the Hamiltonian energy function, is identified from data as in KRONIC, the feedback gain can be precomputed and does not need to be computed on-line. In Fig. 11, the state-dependent feedback law is shown for both controllers as color-coded phase plots, where negative values are depicted by blue and positive values by red. The extrema are identical. The control input from the EC controller is here slightly modified compared with (59b) by moving the term $- {\cos{(x_{1})}}$ into $u$ itself. Then the effective control and performance are displayed in terms of $\hat{u} = {- {{\cos{(x_{1})}}u}}$ for a fair comparison; otherwise, the EC controller would appear less performing.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Frictionless pendulum", "weight": 1.0} -->

The pendulum dynamics are locally controllable as long as $u$ does not vanish, which is achieved if $x_{1} \neq {\pi/2}$ and $x_{2} \neq 0$ for the EC controller and if $x_{2} \neq 0$ for the SDRE controller. Both controllers yield a bang-bang strategy and successfully steer the system to the desired energy level, though the SDRE controller is performing slightly better.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Duffing system", "weight": 1.0} -->

Certain damped or forced oscillators are described by the Duffing equation (Fig. 10). The system is steered towards the energy level $\mathcal{E} = 0$, which corresponds to the separatrix cycle (yellow dashed lines) yielding a periodic solution. The origin is a saddle point leading to a homoclinic orbit defined by $x_{2}^{\ast} = {\pm {x_{1}^{\ast}\sqrt{1 - {{1{(x_{1}^{\ast})}^{2}}/2}}}}$ for $x_{1}^{\ast} \leq {\pm \sqrt{2}}$. It is possible to stabilize the center fixed points by commanding a lower reference energy; however, because of symmetry in the system, both fixed points are indistinguishable in eigenfunction coordinates. This illustrates a fundamental *uncertainty* associated with Koopman eigenfunction control.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Duffing system", "weight": 1.0} -->

For the eigenvalue $\lambda = 0$, becomes ${- {\mathbf{\Gamma}{(\mathbf{X},\overset{˙}{\mathbf{X}})}{\mathbf{ξ}}}} = \mathbf{0}$, and hence a sparse $\mathbf{ξ}$ is sought in the null-space of $- {\mathbf{\Gamma}{(\mathbf{X},\overset{˙}{\mathbf{X}})}}$. Polynomials up to fourth order are employed to construct a library of candidate functions in -. A single time series for $t \in {\lbrack 0,10\rbrack}$ with time step ${\Deltat} = 0.001$ starting at the initial state $\mathbf{x}_{0} = {\lbrack 0,{- 2.8}\rbrack}^{T}$ is collected. Thus, each row in and corresponds to a time instant of the trajectory.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Duffing system", "weight": 1.0} -->

The prediction and associated error of the identified eigenfunction are displayed in Fig. 12.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Duffing system", "weight": 1.0} -->

Here, the energy is predicted over the full state space using the identified eigenfunction, the Hamiltonian energy function, which is trained from a single trajectory. The magnitude of the error is very small of $\mathcal{O}{(10^{- 17})}$. However, the eigenfunction evaluate on a trajectory would oscillate with a tiny amplitude around the true energy level.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Duffing system", "weight": 1.0} -->

The error of the regression problem, the computational time for identifying the eigenfunction, and the control performance (steering towards $\mathcal{E} = 0$) for an increasing number of measurements in the estimation step are displayed in Fig. 13. The identified Koopman eigenfunction with $\lambda = 0$ from 1792 measurements (kink in Fig. 13(b)) is ${\varphi{(\mathbf{x})}} = {\begin{bmatrix} \end{bmatrix}\begin{bmatrix} {- {\frac{2}{3}\frac{2}{3}\frac{1}{3}}} \end{bmatrix}^{T}}$ with error $\mathcal{O}{(10^{- 8})}$. This eigenfunction represents a perfect recovery of the Hamiltonian up to a scaling, as a Hamiltonian multiplied by a constant scalar is also a conserved quantity.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Duffing system", "weight": 1.0} -->

Using a larger time step of ${\Deltat} = 0.05$, 56 measurements are sufficient to learn the eigenfunction with error $\mathcal{O}{(10^{- 6})}$.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Example: Basin hopping in a double well", "weight": 1.0} -->

A Koopman eigenfunction represents a topography over the state; e.g., the Hamiltonian function depicts the energy landscape of the system. Trajectory control of a set of particles based on a single Koopman eigenfunction is driven by the difference between the current and desired value in this topography. While the Koopman eigenfunction is a global, linear representation of the system, the control of the particle is local, e.g. by solving a suboptimal SDRE. This is illustrated for a particle in an asymmetric double potential ${V{(x_{1})}} = {{{\frac{1}{4}x_{1}^{4}} - {\frac{1}{2}x_{1}^{2}} - {\frac{a}{3}x_{1}^{3}}} + {ax_{1}}}$ with $a = {- 0.25}$ (Fig. 14(a)).

<!-- chunk {"id": "body-0113", "role": "body", "section": "Example: Basin hopping in a double well", "weight": 1.0} -->

The Hamiltonian is $\mathcal{H} = {{x_{2}^{2}/2} + {V{(x_{1})}}}$ and the dynamics are For an initial condition in the left well (blue dots in Fig. 14(a)) the controller will fail to steer the state to the fixed point $\mathbf{x}^{\ast} = {\lbrack 1\,\, 0\rbrack}^{T}$ in the center of the right well as the trajectory will become trapped in the bottom of the left well. Instead, the controller must first increase the energy level to the saddle transition, and after the trajectory passes to the right basin, the energy can be decreased further.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Example: Basin hopping in a double well", "weight": 1.0} -->

We propose a switching control strategy that exploits the Koopman eigenfunctions to transport particles between basins of different heights associated with different fixed points. In particular, the following control strategy steers particles from the left to the right basin: A particle on an energy level lower than $\mathcal{H}{({\lbrack a,1\rbrack})}$, associated with the saddle point, is first steered onto a trajectory with slightly higher energy than the homoclinic orbit connecting the two basins. On this orbit, control is turned off and the particle travels to the right well exploiting the intrinsic system dynamics. As soon as it passes the saddle point, control is turned on again directing it to the lowest energy level $\mathcal{H}{({\lbrack 1,0\rbrack})}$ at the desired fixed point. The controller is demonstrated for two initial conditions, as shown in Fig. 14(b-d), driving both to the desired energy level.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Example: Basin hopping in a double well", "weight": 1.0} -->

This controller can be fully derived from data: First, relevant Koopman eigenfunctions can be identified from data, as shown in Sec. 5. By analyzing roots and extrema of the eigenfunction corresponding to $\lambda = 0$, equilibrium and saddle points can be identified. The homoclinic and heteroclinic orbits associated with the saddles can be used as natural transit paths between basins. In each basin, eigenfunction control drives the system to the desired state. Future applications for this control strategy include space mission design and multi-stable systems such as proteins.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Example: Double Gyre flow", "weight": 1.0} -->

We now consider a high-dimensional, spatially evolving, non-autonomous dynamical system, with time-dependent Koopman eigenfunctions. The periodically driven double gyre flow models the transport between convection cells in the Rayleigh-Bénard flow due to lateral oscillations, yielding a simple model for the gulf stream ocean front. We employ here the same parameters as in Shadden et al.'s seminal work on Lagrangian coherent structures.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Example: Double Gyre flow", "weight": 1.0} -->

The control objective is to steer an ensemble of trajectories to a level set of the stream function. This can be interpreted as the control of an ensemble of active drifters or autonomous gliders in the ocean, which drift due to hydrodynamic forces associated with $v_{x}$ and $v_{y}$. The dynamics of the $i$th drifter are ${\frac{d}{dt}\begin{bmatrix} \end{bmatrix}} = \begin{bmatrix} {v_{x} + {\gamma_{i}{\sin\left(\theta_{i} \right)}}} \\{v_{y} + {\gamma_{i}{\cos\left(\theta_{i} \right)}}} \end{bmatrix} = {\begin{bmatrix} \end{bmatrix} + {\begin{bmatrix} \end{bmatrix}\mathbf{u}}}$.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Example: Double Gyre flow", "weight": 1.0} -->

For the autonomous and unforced flow with $\varepsilon = 0$, the stream function is a Koopman eigenfunction associated with the eigenvalue $\lambda = 0$. The forced system becomes: Without control, the stream function $\Psi$ is conserved, as it is the negative of the Hamiltonian. The particles follow streamlines, which are isolines of the stream function.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Example: Double Gyre flow", "weight": 1.0} -->

In the non-integrable case, with $\varepsilon > 0$, the total derivative of the stream function is given by where the vanishing term in is not displayed. The first term in arises from the time derivative $\frac{\partial}{\partial t}\Psi{(x,y,t)}$ and is reformulated into a linear-like structure in $\Psi$: ${\partial{\Psi/{\partial t}}} = {A\pi{\cos{({\pif{(x,t)}})}}{\sin{({\piy})}}{({\partial{f/{\partial t}}})}} = {\pi{\tan^{- 1}{({\pif{(x,t)}})}}{({\partial{f/{\partial t}}})}\Psi} = {A_{\Psi}\Psi}$. The second term is the time-dependent analogue of the corresponding term.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Example: Double Gyre flow", "weight": 1.0} -->

For both cases, $\varepsilon = 0$ and $\varepsilon > 0$, a controller is developed for the stream function. The control is then applied to an ensemble of drifters to steer them towards the level set $\Psi = 0.2$. As in the previous examples a quadratic cost function with $Q = 1$ and $\mathbf{R} = {(\begin{matrix} \end{matrix})}$ is considered. In both cases, $\mathbf{B}_{\Psi}$ and $A_{\Psi}$ depend on the state, and for $\varepsilon > 0$ also on time. Thus, the state-dependent Riccati equation is solved at each point in space and time. The controller successfully drives an ensemble of drifters distributed over the domain to the desired level, as shown in Fig. 15(a). Trajectories are integrated using a $4$th-order Runge-Kutta scheme from $t \in {\lbrack 0,10\rbrack}$.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Example: Double Gyre flow", "weight": 1.0} -->

Example trajectories of the non-autonomous system, with and without control, are presented in Fig. 15(b-c).

<!-- chunk {"id": "body-0122", "role": "body", "section": "Example: Double Gyre flow", "weight": 1.0} -->

Note that in the non-autonomous case, the reference isocurve $\Psi_{REF} = 0.2$ (white dashed in Fig. 15(b)) oscillates from left to right while being periodically compressed and expanded in $x$-direction. The particles follow the moving isocurve resulting in a small oscillation around the desired value (see Fig. 15(c)).

<!-- chunk {"id": "body-0123", "role": "body", "section": "Example: Double Gyre flow", "weight": 1.0} -->

Koopman eigenfunction control can be interpreted in two ways: applying local control to internally driven swimmers or particles in an external field such as a fluid flow or magnetic field; or driving the external field in which the swimmers or particles drift. In the latter case, control drives the amplitude of the stream function at each point to the desired value. For the double gyre flow with a constrained spatial domain, the spatially distributed gain may be precomputed.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Discussion and conclusions", "weight": 1.5} -->

In summary, we extend the Koopman operator formalism to include actuation, and demonstrate how a nonlinear control problem may be converted into a bilinear control problem in eigenfunction coordinates. Next, we have presented a data-driven framework to identify leading eigenfunctions of the Koopman operator and sparsity-promoting extensions to EDMD. We find that lightly damped or undamped eigenfunctions may be accurately approximated from data via regression, as these eigenfunctions correspond to persistent phenomena, such as conserved quantities. Moreover, these are often the structures that we seek to control, since they affect long-time behavior. We have demonstrated the efficacy of this new data-driven control architecture on a number of nonlinear systems, including Hamiltonian systems and a challenging high-dimensional ocean mixing model. These results suggest that identifying and controlling Koopman eigenfunctions may enable significant progress towards the ultimate goal of a universal data-driven nonlinear control strategy.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Discussion and conclusions", "weight": 1.5} -->

Finite-dimensional approximations of the Koopman operator are typically obtained as its projection onto a specified basis, which may suffer from a well-known closure issue. The matrix $\mathbf{K}$ is usually large, as the state is lifted to a high-dimensional space, and the resulting model rarely closes and spurious eigenfunctions may appear. Building on EDMD, we construct a reduced-order model using validated Koopman eigenfunctions, so that the resulting model will be closed by design. Both KRONIC and EDMD with control provide Koopman-based system identification that can be leveraged for model-based control, such as MPC or LQR, as shown in Fig. 16. However, there are a number of key differences: KRONIC directly identifies Koopman eigenfunctions, while EDMDc approximates the Koopman operator restricted to a high-dimensional span of observables. EDMD augments the state vector with nonlinear measurements, increasing the dimension of the system. In contrast, KRONIC yields a reduced-order model in terms of a few Koopman eigenfunctions.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Discussion and conclusions", "weight": 1.5} -->

Control is incorporated in EDMDc as an approximated affine linear term. KRONIC derives an expression for how eigenfunctions are affected by control through the generator equation. However, this may render the control term bilinear (nonlinear in the state). The cost function for EDMDc is defined in the state or measurement space, while KRONIC defines the cost in eigenfunctions; note that these cost functions are not always transferable. Finally, KRONIC readily admits more complicated solutions, such as limit cycle stabilization, as these correspond to level sets of the eigenfunctions.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Discussion and conclusions", "weight": 1.5} -->

As with previous studies, this work further cements the importance of accurate identification and representation of Koopman eigenfunctions. Future work will continue to develop algorithms to extract approximate eigenfunctions from data, and it is likely that these efforts will benefit from advances in machine learning. In addition, there is a fundamental uncertainty principle in representing Koopman eigenfunctions, as these eigenfunctions may themselves be irrepresentable, as are the long-time flow maps for chaotic systems. Instead of seeking perfect Koopman eigenfunctions, which may not be attainable, it will be important to incorporate uncertainty quantification into the data-driven Koopman framework. Model uncertainties may then be managed with robust control.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Discussion and conclusions", "weight": 1.5} -->

The present work also highlights an important choice of perspective when working with Koopman approximations. Generally, Koopman eigenfunctions are global objects, such as the Hamiltonian energy function. Although a global, linear representation of the dynamics is appealing, there is also information that is stripped from these representations. For example, in the case of the Hamiltonian eigenfunction, information about specific fixed points and spatial locations are folded into a single scalar energy. If the Hamiltonian is viewed as a topography over the phase space, then this eigenfunction only carries information about the *altitude*, and not the *location*. In contrast, Lan and Mezić show that it is possible to extend the Hartman-Grobman theorem to the entire basin of attraction of certain fixed points and periodic orbits, providing a *local* linear embedding of the dynamics. Connecting these perspectives will continue to yield interesting and important advances in Koopman theory. In addition, there are known connections between the eigenvalues of geometric structures in phase space and the spectrum of the Koopman operator. This knowledge may guide the accurate identification of Koopman eigenfunctions.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Discussion and conclusions", "weight": 1.5} -->

Formulating control in terms of Koopman eigenfunctions requires a change of perspective as the control objective may now be defined in eigenfunctions coordinates. Eigenfunctions characterize, e.g., geometric properties of the system, such as fixed points and limit cycles, as particular level sets, and the control objective can be equivalently formulated to steer the system towards these objects. Further, particular eigenfunctions represent coherent structures, i.e. persistent features of the system, which have been targeted in control for a long time. However, the specific selection of eigenfunctions to control and their interpretation regarding specific control goals remains an open problem. Nevertheless, it may still be possible to formulate the control in the original state space, e.g. by incorporating the state as observables, modifying the state weight matrix appropriately, or by learning an approximation of the inverse mapping, which can be more easily incorporated in the context of model predictive control. This also motivates additional work to understand how controllability and observability in these coordinates relate to properties of the nonlinear system.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Discussion and conclusions", "weight": 1.5} -->

The degree of observability and controllability will generally vary with different eigenfunctions, so that it may be possible to obtain balanced realizations. Moreover, classic results, such as the PBH test, indicate that multi-channel actuation may be necessary to simultaneously control different eigenfunctions corresponding to the same eigenvalue, such as the Hamiltonian energy and conserved angular momentum. The additional degrees of freedom arising from multi-channel inputs can also be used for eigenstructure assignment to shape Koopman eigenfunctions. Thus, actuation may modify both the shape of coherent structures (i.e., Koopman modes associated with a particular eigenfunction) and their time dynamics. It may also be possible to use Koopman linear embeddings to optimize sensor and actuator placement for nonlinear systems.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Discussion and conclusions", "weight": 1.5} -->

Finally, as undamped or lightly damped eigenfunctions correspond to conserved or nearly conserved quantities, there are many potential applications of the proposed control strategy. For example, symmetries give rise to other conserved quantities, which will likewise yield new Koopman eigenfunctions. In many physical systems, simultaneously controlling the system energy and angular momentum may be an important goal. Much of the present work was formulated with the problem of space mission design in mind. Energy efficient transport throughout the solar system has long driven advances in theoretical and computational dynamical systems, and may stand to benefit from control based on Koopman eigenfunctions. More generally, there is a broad range of applications that stand to benefit from improved nonlinear control, include self-driving cars, the control of turbulence, suppressing the spread of disease, stabilizing financial markets, human machine interfaces, prosthetics and rehabilitation, and the treatment of neurological disorders, to name only a few.
