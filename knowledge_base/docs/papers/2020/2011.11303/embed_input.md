<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

KPC: Learning-Based Model Predictive Control with Deterministic Guarantees

Topics include Model predictive control, Predictive control, Safety, Robustness, Regression, Optimization, Control, Learning, KPC.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose Kernel Predictive Control (KPC), a learning-based predictive control strategy that enjoys deterministic guarantees of safety. Noise-corrupted samples of the unknown system dynamics are used to learn several models through the formalism of non-parametric kernel regression. By treating each prediction step individually, we dispense with the need of propagating sets through highly non-linear maps, a procedure that often involves multiple conservative approximation steps. Finite-sample error bounds are then used to enforce state-feasibility by employing an efficient robust formulation. We then present a relaxation strategy that exploits on-line data to weaken the optimization problem constraints while preserving safety. Two numerical examples are provided to illustrate the applicability of the proposed control method.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Safety is the number one requirement for any system that operates under physical constraints. For decades, this has been a major concern when control systems incorporate forms of adaptation or learning. A considerable body of literature exists establishing stability and performance guarantees in scenarios of parametric plant-model mismatch (see Lorenzen et al.; Tanaskovic et al.; Bujarbaruah and Vallon for some recent works in this direction). Depending on the final application however, assuming that the exact model structure is available might be unrealistic due to the complex physics behind the system at hand, or to the time-monetary costs associated with the modeling process.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A compelling alternative to the paradigm described above is the use of non-parametric models. These form a flexible class of surrogate functions whose number of parameters grows with the cardinality of the dataset. Relevant examples for the control community include the Nonlinear Set Memebership (NSM) and the Kinky Inference (KI) techniques. Due to the ease of incorporating prior expert knowledge and the inherent uncertainty quantification associated with them, Gaussian processes (GPs) have recently become a popular modeling tool for dynamical systems Capone et al.; Matschek and Findeisen; Arcari et al.; Umlauft and Hirche; Shukla et al.; Yingzhao and Jones. Such function approximators are typically paired with appropriate Model Predictive Control (MPC) schemes that not only take into account the latent function estimate, but also the model variance to act with care in highly uncertain regions of the space (see Koller et al.; Hewing et al. for two examples, and Beckers et al. for an exception to this trend).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

As opposed to Gaussian processes, kernel ridge regression (KRR) and support vector regression (SVR) are deterministic non-parametric tools. These models have the same form of a GP predictive mean: a weighted sum of kernel basis functions. Moreover, with an appropriate choice of regularization constant, a KRR model matches exactly a GP posterior. Connections between the stochastic and the deterministic frameworks are profound and have been long known. Uncertainty can be quantified in the KRR and SVR cases by considering all maps belonging to their underlying reproducing kernel Hilbert space (RKHS) of functions. The RKHSs associated to various kernels, including the widely used squared-exponential, are dense in the space of continuous functions with compact domains.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our contribution: We propose in this paper a predictive control strategy based on non-parametric kernel regression that incorporates deterministic guarantees of safety. Samples from the unknown ground-truth dynamics are used to construct one-step and multi-step ahead models, with an appropriate state-dependent uncertainty quantification obtained from recently derived error-bounds. The available dataset can be contaminated by noise, which is only assumed to be bounded, but otherwise drawn from any distribution. An efficient robust optimization formulation is derived to enforce state-constraint satisfaction. We then present a relaxation strategy that exploits on-line information to alleviate the problem constraints while preserving safety. Two numerical examples are provided and we discuss scalability issues to large datasets.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

We consider a discrete-time nonlinear system of the form

<!-- chunk {"id": "body-0008", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

our goal is to drive the dynamical system from a specified initial condition $x_{0}$ to the set ${\mathbb{X}}_{\text{safe}}$ while satisfying all constraints.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

A frequent instance of this problem is the regulation to a specific fixed point, in which ${\mathbb{X}}_{\text{safe}} = {\{ x_{\text{eq}}\}}$ and ${\pi{(x_{eq})}} = u_{eq}$ is the equilibrium control constant. In order to accomplish our task, we make use of noise-corrupted measurements of our unknown ground-truth and the formalism of non-parametric kernel learning are described next.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Non-Parametric Kernel Learning", "weight": 1.0} -->

In this section only, we consider $n_{x} = 1$ simply to avoid using a cumbersome notation; for $n_{x} > 1$, each output component of $f$ has to be considered separately. Moreover, the shorthand notation ${f{(x,u)}} = {f{(z)}}$ is used. Suppose the map $f$ is unknown, but a collection of $D$ measurement pairs is available to reconstruct it

<!-- chunk {"id": "body-0011", "role": "body", "section": "Non-Parametric Kernel Learning", "weight": 1.0} -->

We make the following two assumptions on our dataset and on the observational model.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The data locations $z_{1},\ldots,z_{D}$ are pairwise distinct.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The approach of kernel machines is employed to learn the unknown dynamics from the available dataset. Next, we recall the basics of such theory, see Schölkopf et al. for a more complete coverage of the topic. A kernel is any real-valued symmetric positive-semidefinite function $k:{{\mathcal{Z} \times \mathcal{Z}}\rightarrow{\mathbb{R}}}$. Each kernel defines a reproducing kernel Hilbert space $\mathcal{H} \subset {\mathbb{R}}^{\mathcal{Z}}$, where ${\forall z} \in \mathcal{Z}$ we have that ${k{(z, \cdot )}} \in \mathcal{H}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Computing the inner-product between a map $h \in \mathcal{H}$ and a partially evaluated kernel $k{(z, \cdot )}$ is equivalent to assessing the value of $h$ at $z$, i.e., ${\langle h,{k{(z, \cdot )}}\rangle}_{\mathcal{H}} = {h{(z)}}$, which is known as the reproducing property. Members $f$ of $\mathcal{H}$ can be seen as linear combinations of partially evaluated kernel functions since $\mathcal{H}$ is the closure of ${{\text{span}{({k{(z, \cdot )}})}},{\forall z}} \in \mathcal{Z}$ with respect to the induced metric.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

For convenience, we define $Z$ as the collection of all dataset inputs $z_{d}$, and $y$ as the collection of all targets $y_{d}$. Also, let $K \in {\mathbb{R}}^{D \times D}$ be the constant matrix of kernel evaluations at $Z$, i.e., $k{(z_{i},z_{j})}$ at its i-th row and j-th column, and let $K_{Zz}:{\mathcal{Z}\rightarrow{\mathbb{R}}^{D}}$ denote the column vector function $z\mapsto\left( {k{(z_{1},z)}},\ldots,{k{(z_{D},z)}} \right)^{\top}$ and $K_{zZ}$ simply represents its transpose.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Finally, the so-called power function is a non-negative map $P:{\mathcal{Z}\rightarrow{\mathbb{R}}_{\geq 0}}$ defined as

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

and evaluates to zero for all $z_{d}$ in the dataset. Note the similarity between the power function $P{(z)}$ and the posterior variance of a Gaussian process.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The estimate $\hat{f}$ is built by minimizing a combination of the mean-squared error and a regularization term to penalize complexity, i.e., the kernel ridge regression (KRR) cost

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

According to the well-known representer theorem, out of all possible maps $h \in \mathcal{H}$, a minimizer exists and is given by a weighted sum of kernels centered at the input locations $Z$. The problem above is therefore equivalent to a finite-dimensional quadratic program whose closed-form solution, our nominal model, is given by

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Note that the map described by has the same form as a Gaussian process posterior distribution conditioned on the data, that is, its predictive mean. Indeed, if $\sigma$ is the noise variance in the GP scenario and $\lambda$ is selected as $\sigma^{2}/D$, the two models are exactly the same. The reader is referred to for a discussion on the existing connections.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

The chosen kernel $k{( \cdot, \cdot )}$ is a strictly positive-definite function.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

The unknown dynamics $f$ are contained in the RKHS of the chosen kernel $k{( \cdot, \cdot )}$, and an upper bound for its norm is available $\Gamma \geq {\| f\|}_{\mathcal{H}}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

The two conditions above are central to the development of the control strategy safety guarantees. Assumption 3 can be satisfied by selecting an appropriate kernel function such as the squared-exponential or the inverse multiquadrics. Assumption 4 encapsulates our knowledge about the complexity of the unknown ground-truth: intuitively, the more kernel basis functions are needed to describe it, the larger the associated norm. The same piece of information is required in the works Koller et al.; Hashimoto et al. as well as in various other recent papers. In Maddalena et al., an example is provided on how $\Gamma$ could be estimated from noiseless samples of the latent function, and how this estimation process is affected by the presence of bounded noise. As shown in the latter work, finite-sample deterministic error bounds exist for KRR models.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 2", "weight": 1.0} -->

When compared to the GP bounds presented in Srinivas et al., the result given in Theorem 3.1). ‣ 3 Non-Parametric Kernel Learning ‣ KPC: Learning-Based Model Predictive Control with Deterministic Guarantees") does not involve information-theoretic measures such as the maximal information gain. The need of estimating such constant hampers the applicability of the former bounds in practical scenarios (see the discussion in Lederer et al. ). When compared to the results, the inequality. ‣ 3 Non-Parametric Kernel Learning ‣ KPC: Learning-Based Model Predictive Control with Deterministic Guarantees")) tends to give rise to tighter bounds as shown in Maddalena et al.; nevertheless, the latter are more unstable at the extremes of the input space. In order to avoid this effect, data have to ideally fill the ground-truth domain while still being well-separated. In the approximation theory community, this interplay between precision and stability is known as the uncertainty principle.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Kernel Predictive Control", "weight": 1.0} -->

One possible approach to tackling our problem is to build a single-step surrogate model for the latent function and employ uncertainty propagation techniques to perform multi-step ahead predictions. Propagating sets through general non-linear maps is challenging and usually involves several overbouding steps. Therefore, we opt for learning various condensed models, one for each of the $N$ prediction steps. Let $F_{1}:{{{\mathbb{X}} \times {\mathbb{U}}}\rightarrow{\mathbb{X}}}$ be the one-step ahead predictor in which each dimension in learned separately by KRR models ${\hat{f}}_{1},\ldots,{\hat{f}}_{n_{x}}$

<!-- chunk {"id": "body-0026", "role": "body", "section": "Kernel Predictive Control", "weight": 1.0} -->

where $\beta{(x,u)}$ denotes the right-hand side of the inequality. ‣ 3 Non-Parametric Kernel Learning ‣ KPC: Learning-Based Model Predictive Control with Deterministic Guarantees")), and $a \pm b$ refers to the set $\left. \{ c \middle| {{a - b} \leq c \leq {a + b}}\} \right.$. Similarly, define also the maps $\mathcal{X}_{2},{\ldots\mathcal{X}_{N}}$, which share the same domain respectively with $F_{2},\ldots,F_{N}$. As a direct consequence of Theorem 3.1). ‣ 3 Non-Parametric Kernel Learning ‣ KPC: Learning-Based Model Predictive Control with Deterministic Guarantees"), we have that

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Training the associated kernel models requires various $N$-step experiments to be performed rather than simply having one-step ones. For instance, the model $F_{N}$ requires multiple tuples $(x_{0},u_{0},\ldots,u_{N - 1})$ as features and (possibly noisy) measurements of the resulting states $x_{N}$ as targets. We highlight that long sequences of linked states, i.e., long experiments, are preferred over various short ones even in classical parametric system identification.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Let $x_{0}$ be a given initial condition for the true dynamical system. Our Kernel Predictive Control formulation is expressed as the finite-horizon optimal control problem

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 3", "weight": 1.0} -->

where $X = {(x_{1},\ldots,x_{N})}$, $U = {(u_{0},\ldots,u_{N - 1})}$ are the decision variables, and $\ell{(x,u)}$ and $\ell_{f}{(x)}$ are appropriately designed stage and final costs. In a receding-horizon implementation, KPC is solved recursively and only the first optimal control inputs are applied to the system.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 4", "weight": 1.0} -->

The maximization in could also be directly converted into its dual form without the reformulation. Although this would not introduce any conservatism, additional decision variables would be created along with nonlinear equality constraints, thus significantly increasing the KPC formulation complexity. The approach adopted above is both economic and exact.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 4", "weight": 1.0} -->

After converting the set constraints (11c) and (11d) into the form, one obtains

<!-- chunk {"id": "body-0032", "role": "body", "section": "Safe Relaxation Strategy", "weight": 1.0} -->

Next we propose a safe relaxation strategy (SRS) that can be used to weaken the optimization problem constraints (17c)-(17d) whenever data from previous KPC iterations are available.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

We illustrate the use of KPC, implemented in a receding-horizon fashion, in two different scenarios. The optimization problems were formulated with the aid of CasADi, the Multi-Parametric Toolbox, and solved with IPOPT ^33^3Additional details about the simulations are available at

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments", "weight": 1.0} -->

Example 1: Consider a continuous stirred-tank reactor (CSTR) whose continuous-time dynamics are given by the differential equations

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiments", "weight": 1.0} -->

where $c_{A}$ and $c_{B}$ denote respectively the concentrations of cyclopentadiene and cyclopentenol, and $u$ represents the feed inflow of cyclopentadiene. We assume that the reactor temperature is constant and simulate the dynamics with the parameter values: ${\rho_{1} = \rho_{2} = {{4.1 \times 10^{- 3}}\text{~h}^{- 1}}},{{\rho_{3} = {{6.3 \times 10^{- 4}}\text{~h}^{- 1}}},{c_{A0} = {5.1\text{~mol/l}}}}$. The constraint sets are ${\mathbb{X}} = \left.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiments", "weight": 1.0} -->

Three distinct random datasets were collected with $300$, $400$ and $500$ points respectively for the one-step, two-step and three-step ahead predictors. The noise affecting our samples was drawn randomly with uniform bound $1 \times 10^{- 3}$. Squared-exponential kernels were chosen and their hyperparameters were adjusted until good fits were obtained; specifically, the lengthscales were set to larger values when dealing with higher-dimensional feature spaces. The exact regressor norms were calculated and an augmentation factor of $150\%$ was used to obtain estimates $\Gamma$. This latter step accounts for the ground-truth complexity in unexplored regions of the space. Finally, standard quadratic stage and terminal costs were employed with positive definite weight matrices.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiments", "weight": 1.0} -->

As is customary in practical non-linear optimal control, the terminal constraint was dropped and only a terminal penalty was employed. The system evolution starting from various initial conditions is shown in Figure 2. The closed-loop trajectories (shown on the left) converged to a neighborhood of $x_{S}$, while all predictions and confidence sets (shown on the right) remained inside the feasible set $\mathbb{X}$ at all time-instants. It is also possible to note how predicting further into the future is more challenging as the lengths of the boxes tended to be larger at the end of the prediction horizon.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experiments", "weight": 1.0} -->

Example 2: The continuous-time angular dynamics of a pendulum with a rigid rod can be described by ${\overset{˙}{x}}_{1} = x_{2}$, ${\overset{˙}{x}}_{2} = {{{{({g/l})}{\sin{(x_{1})}}} - {{({\nu/{({ml^{2}})}})}x_{2}}} + {{({1/{({ml^{2}})}})}u}}$, where $x_{1}$ is its angular position, $x_{2}$ its angular velocity, and $u$ the torque applied to it. The parameters are: $m = 0.15$ the mass of the pendulum, $l = 0.5$ the length of the rod, $g = 9.81$ the gravitational constant, and $\nu = 0.1$ a constant for the friction model.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experiments", "weight": 1.0} -->

Let the constraints be ${|x_{1}|} \leq 3$, ${|x_{2}|} \leq 1$, and the input be limited to ${|u|} \leq 1$. We selected a prediction horizon of $N = 4$ and collected $D = 100$ uniformly random data-points for each of the eight regression tasks. The noise was drawn randomly from a uniform distribution with bound $\overline{\delta} = {0.01\text{1}}$, where $\text{1} \in {\mathbb{R}}^{D}$ is a vector of ones. Similarly to the previous example, we used a squared-exponential kernel with increasing lengthscales and employed an augmentation factor of $300\%$ on the nominal predictor norms to estimate the $\Gamma$ constants. The sampling and control period was $0.2$ seconds. We compared KPC against nominal kernel-MPC, i.e., a certainty equivalence approach where the state-constraints were imposed directly on the nominal predictions (11b).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experiments", "weight": 1.0} -->

In the latter case, uncertainty was not quantified and the confidence sets were not present. The cost used in both formulations was a positive definite function of the states and control inputs, and included a terminal penalty term.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experiments", "weight": 1.0} -->

Predictions and the system angular velocity evolution from two different initial conditions are shown in Figure 3. As can be seen from the plots, imposing the state-constraints on the nominal model predictions was not sufficient to guarantee safety as the closed-loop system behavior violated the $x_{2} \geq {- 1}$ restriction. On the other hand, since KPC quantified and incorporated the associated uncertainty into the optimization problems, the constraints were satisfied. The error bars on the right plot show the all predictions and uncertainty values at each step in the form of error bars. Note that the safety constraints were active at multiple points in time.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

KPC was proposed as a predictive control methodology based on non-parametric kernel models and their associated uncertainty estimates. Its key feature is deterministic constraint satisfaction when a solution to the optimization problem is found. From an approximation theory perspective, future works could study the advantages of employing SVR surrogate models over KRR ones, as well as refining the existing error-bounds, which we believe to be possible. Establishing conditions under which KPC would enjoy additional closed-loop properties such as convergence is deemed as interesting and could guide practical real-world applications of the proposed control scheme.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

This work received support from the Swiss National Science Foundation under the Risk Aware Data-Driven Demand Response project (grant number 200021 175627) and CSEM's Data Program.
