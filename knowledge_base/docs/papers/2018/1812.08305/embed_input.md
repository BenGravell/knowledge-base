<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Derivative-Free Methods for Policy Optimization: Guarantees for Linear Quadratic Systems

Topics include Optimization, Derivative-free, Policy optimization.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study derivative-free methods for policy optimization over the class of linear policies. We focus on characterizing the convergence rate of these methods when applied to linear-quadratic systems, and study various settings of driving noise and reward feedback. We show that these methods provably converge to within any pre-specified tolerance of the optimal policy with a number of zero-order evaluations that is an explicit polynomial of the error tolerance, dimension, and curvature properties of the problem. Our analysis reveals some interesting differences between the settings of additive driving noise and random initialization, as well as the settings of one-point and two-point reward feedback. Our theory is corroborated by extensive simulations of derivative-free methods on these systems. Along the way, we derive convergence rates for stochastic zero-order optimization algorithms when applied to a certain class of non-convex problems.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent years have witnessed a number of successes in applying modern reinforcement learning (RL) methods to many fields, including robotics and competitive gaming. Impressively, most of these successes have been achieved by using general-purpose RL methods that are applicable to a host of problems. Prevalent general-purpose RL approaches can be broadly categorized into: (a) *model-based approaches*, in which an agent attempts to learn a model for the dynamics by observing the evolution of its state sequence; and (b) *model-free approaches*, including DQN, and TRPO, in which the agent attempts to learn an optimal policy directly, by observing rewards from the environment. While model-free approaches typically require more samples to learn a policy of equivalent accuracy, they are naturally more robust to model mis-specification.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A literature that is closely related to model-free RL is that of *zero-order or derivative-free* methods for stochastic optimization; see the book by for an overview. Here, the goal is to optimize an unknown function from noisy observations of its values at judiciously chosen points. While most analytical results in this space apply to convex optimization, many of the procedures themselves rely on moving along randomized approximations to the directional derivatives of the function being optimized, and are thus applicable even to non-convex problems. In the particular context of RL, variants of derivative-free methods, including TRPO, PSNG and evolutionary strategies, have been used to solve highly non-convex optimization problems and have been shown to achieve state-of-the-art performance on various RL tasks.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

While many RL algorithms are easy to describe and run in practice, certain theoretical aspects of their behavior remain mysterious, even when they are applied in relatively simple settings. One such setting is the most canonical problem in continuous control, that of controlling a linear dynamical system with quadratic costs, a problem known as the linear quadratic regulator (LQR). A recent line of work has sought to delineate the properties and limitations of various RL algorithms in application to LQR problems. An appealing property of LQR systems from an analytical point of view is that the optimal policy is guaranteed to be linear in the states. Thus, when the system dynamics are known, as in classical control, the optimal policy can be obtained by solving the discrete-time algebraic Ricatti equation.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast, methods in reinforcement learning target the case of unknown dynamics, and seek to learn an optimal policy on the basis of observations. A basic form of model-free RL for linear quadratic systems involves applying derivative-free methods in the space of linear policies. It can be used even when the only observations possible are the costs from a set of rollouts, each referred to as a sample^11^1Such an offline setting with multiple, restarted rollouts should be contrasted with an online setting, in which the agent interacts continuously with the environment, and no hard resets are allowed. In contrast to the offline setting, the goal in the online setting is to control the system for all time steps while simultaneously learning better policies, and performance is usually measured in terms of regret., and when our goal is to obtain a policy whose cost is at most $\epsilon$-suboptimal. The sample complexity of a given method refers to the number of samples, as a function of the problem parameters and tolerance, required to meet a given tolerance $\epsilon$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

With this context, we are led to the following concrete question: *What is the sample complexity of derivative-free methods for the linear quadratic regulator?* This question underlies the analysis in this paper. In particular, we study a standard derivative-free algorithm in an offline setting and derive explicit bounds on its sample complexity, carefully controlling the dependence on not only the tolerance $\epsilon$, but also the dimension and conditioning of the underlying problem.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our analysis treats two distinct forms of randomness in the underlying linear system. In the first setting---more commonly assumed in practice---the linear updates are driven by an additive noise term, whereas in the second setting, the initial state is chosen randomly but the linear dynamics remain deterministic. We refer to these two settings, respectively, as the *additive noise setting*, and the *randomly initialized setting.* We are now in a position to discuss related work on the problem, and to state our contributions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Our contributions", "weight": 1.0} -->

In this paper, we study both randomly initialized and additive-noise linear quadratic systems in the offline setting through the lens of derivative-free optimization. We begin with a general result that characterizes the convergence behavior of a canonical derivative-free algorithm when applied to a general class of functions satisfying certain curvature conditions. In particular, our main contribution is to establish upper bounds on the sample complexity as a function of the dimension, error tolerance, and curvature parameters of the problem instance. We then specialize this result to a variety of LQR models. In contrast to prior work, the rates that we provide are explicit, and the algorithms that we analyze are standard and practical one-point and two-point variants of the random search heuristic. Our results reveal interesting dichotomies between the settings of one-point and two-point feedback, as well as the models involving random initialization and additive noise.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Main Theorem (informal)", "weight": 1.0} -->

*With high probability, one can obtain an $\epsilon$-approximate solution to any linear quadratic system from observing the noisy costs of $\overset{\sim}{\mathcal{O}}{({1/\epsilon^{2}})}$ trajectories from the system, which can be further reduced to $\overset{\sim}{\mathcal{O}}{({1/\epsilon})}$ trajectories when pairs of costs are observed for each trajectory.*\In our theoretical statements, the multiplicative pre-factors are explicit lower-order polynomials of the dimension of the state space, and curvature properties of the cost function. From a technical standpoint, we build upon some known properties of the LQR cost function established in past work on randomly initialized systems, and establish de novo some analogous properties for the additive noise setting.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Main Theorem (informal)", "weight": 1.0} -->

We also isolate and sharpen some key properties that are essential to establishing sharp rates of zero-order optimization; as an example, for the setting with random-initialization and one-point reward feedback studied by Fazel et al., establishing these properties allows us to analyze a natural algorithm that improves^22^2While the rates established by Fazel et al. are not explicit, their analysis is conservative and yields a bound of order $1/\epsilon^{4}$ up to logarithmic factors. To be clear, the properties that we establish also enable us to provide a sharper analysis of their algorithm; see Appendix E to follow. the dependence of the bound on the error tolerance $\epsilon$ from at least $\mathcal{O}\left({1/\epsilon^{4}} \right)$ to $\mathcal{O}\left({1/\epsilon^{2}} \right)$. Crucially, our analysis is complicated by the fact that we must ensure that the iterates are confined to the region in which the linear system is stable, and such stability considerations introduce additional restrictions on the parameters used in our optimization procedure.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Optimization background", "weight": 1.0} -->

We first introduce some standard optimization related background and assumptions, and make the zero-order setting precise.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Stochastic zero-order optimization", "weight": 1.0} -->

We consider optimization problems of the form where $\xi$ is a zero mean random variable^33^3While the zero mean assumption on $\xi$ is not strictly necessary for generic optimization, the canonical (additive noise) LQR settings that we specialize our results to require noise to be zero mean. So we make this assumption at the outset for convenience. that represents the noise in the problem, and the function $f$ above can be non-convex in general with a possibly non-convex domain $\mathcal{X} \subseteq^{d}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Stochastic zero-order optimization", "weight": 1.0} -->

In particular, we consider stochastic zero-order optimization methods with oracle access to noisy function evaluations. We operate under two distinct oracle models. The first is the one-point setting, in which the optimizer specifies a point $x \in \mathcal{X}$, and an evaluation consists of an instantiation of the random variable $F{(x,\xi)}$. The second is the two-point extension of such a setting, in which the optimizer specifies a pair of points $(x,y)$, then an instantiation of the random variable $\xi$ occurs, and the optimizer obtains the values $F{(x,\xi)}$ and $F{(y,\xi)}$. Crucially, the function evaluations $F{(x,\xi)}$ and $F{(y,\xi)}$ share the same noise, so the two-point oracle cannot be reduced to querying the one-point oracle twice (where sharing the same noise across multiple function evaluations cannot be guaranteed). Such two-point settings are known in the optimization literature to enjoy reduced variance of gradient estimates.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Function properties", "weight": 1.0} -->

Before defining the optimization problems considered in this paper by instantiating the pair of functions $(f,F)$, let us precisely define some standard properties that make repeated appearances in the sequel.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Optimal control background", "weight": 1.0} -->

We now turn to some basic background on optimal control and reinforcement learning. An optimal control problem is specified by a dynamics model and a real-valued cost function. The dynamics model consists of a sequence of functions $\left\{ {h_{t}{(s_{t},a_{t},z_{t})}} \right\}_{t \geq 0}$, which models how the state vector $s_{t}$ transitions to the next state $s_{t + 1}$ when a control input $a_{t}$ is applied at a timestep $t$. The term $z_{t}$ captures the noise disturbance in the system. The cost function $c_{t}{(s_{t},a_{t})}$ specifies the cost incurred by taking an action $a_{t}$ in the state $s_{t}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Optimal control background", "weight": 1.0} -->

The goal of the control problem is to find a sequence of control inputs $\left\{ a_{t} \right\}_{t \geq 0}$, dependent on the history of states $\mathcal{H}_{t}: = {(s_{0},s_{1},\ldots,s_{t - 1})}$, so as to solve the optimization problem where the expectation above is with respect to the noise in the transition dynamics as well as any randomness in the selection of control inputs, and $0 < \gamma \leq 1$ represents a multiplicative discount factor. A mapping from histories $\mathcal{H}_{t}$ to controls $a_{t}$ is called a *policy*, and the above minimization is effectively over the space of policies.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Optimal control background", "weight": 1.0} -->

There is a distinction to be made here between the classical fully-observed setting in stochastic control in which the dynamics model $h_{t}$ is known---in this case, such a problem may be solved (at least in principle) by the Bellman recursion, and the system identification setting in which the dynamics are completely unknown. We operate in the latter setting, and accommodate the further assumption that even the cost function $c_{t}$ is unknown.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Optimal control background", "weight": 1.0} -->

In this paper, we assume that the state space is $m$-dimensional, and the control space is $k$-dimensional, so that $s_{t} \in^{m}$ and $a_{t} \in^{k}$. The linear quadratic system specifies particular forms for the dynamics and costs, respectively. In particular, the cost function obeys the quadratic form for a pair of positive definite matrices $(Q,R)$ of the appropriate dimensions. Additionally, the dynamics model is linear in both states and controls, and takes the form where $A$ and $B$ are transition matrices of the appropriate dimension, and the random variable $z_{t}$ models additive noise in the problem which is drawn i.i.d. for each $t$ from a distribution $\mathcal{D}_{\mathsf{a}\mathsf{d}\mathsf{d}}$. We call this setting the *noisy dynamics* model.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Optimal control background", "weight": 1.0} -->

We also consider the *randomly initialized* linear quadratic system without additive noise, in which the state transitions obey and the randomness in the problem comes from choosing the initial state $s_{0}$ at random from a distribution $\mathcal{D}_{0}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Optimal control background", "weight": 1.0} -->

Throughout this paper, we assume^44^4It is important to note that our assumption of identity covariance of the noise distributions can be made without loss of generality: for a problem with known, non-identity (but full-dimensional) covariance $\Sigma$, we may reparametrize the problem with the modifications ${{A' = {\Sigma^{- {1/2}}A\Sigma^{1/2}}},{{B' = {\Sigma^{- {1/2}}B}},{{\text{~and~}s_{t}'} = {\Sigma^{- {1/2}}s_{t}\text{~for all~}t} \geq 0}}},$ in which case the new problem with states $s_{t}'$ and the pair of transition matrices $(A',B')$ is driven by noise satisfying the assumptions.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Optimal control background", "weight": 1.0} -->

that for both distributions $\mathcal{D} \in {\{\mathcal{D}_{\mathsf{a}\mathsf{d}\mathsf{d}},\mathcal{D}_{0}\}}$ and for a random variable $v \sim \mathcal{D}$, we have While we assume boundedness of the distribution for convenience, our results extend straightforwardly to sub-Gaussian distributions by appealing to high-probability bounds for quadratic forms of sub-Gaussian random vectors and standard truncation arguments. The final iteration complexity also changes by at most poly-logarithmic factors in the problem parameters; for brevity, we operate under the assumptions throughout the paper and omit standard calculations for sub-Gaussian distributions.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Optimal control background", "weight": 1.0} -->

By classical results in optimal control theory, the optimal controller for the LQR problem under both of these noise models takes the linear form $a_{t} = {- {K^{\ast}s_{t}}}$, for some matrix $K^{\ast} \in {\mathbb{R}}^{k \times m}$. When the system matrices are known, the controller matrix $K^{\ast}$ can be obtained by solving the discrete-time algebraic Riccati equation.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Optimal control background", "weight": 1.0} -->

With the knowledge that the optimal policy is an invariant linear transformation of the state, one can re-parametrize the LQR objective in terms of the linear class of policies, and focus on optimization procedures that only search over the class of linear policies. Below, we define such a parametrization under the noise models introduced above, and make explicit the connections to the stochastic optimization model.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Random initialization", "weight": 1.0} -->

For each choice of the (random) initial state $s_{0}$, let $\mathcal{C}_{{\mathsf{i}\mathsf{n}\mathsf{i}\mathsf{t}},\gamma}{(K;s_{0})}$ denote the cost of executing a linear policy $K$ from initial state $s_{0}$, so that where we have the noiseless dynamics $s_{t + 1} = {{As_{t}} + {Ba_{t}}}$ and $a_{t} = {- {Ks_{t}}}$ for each $t \geq 0$, and $0 < \gamma \leq 1$. While $\mathcal{C}_{{\mathsf{i}\mathsf{n}\mathsf{i}\mathsf{t}},\gamma}{(K;s_{0})}$ is a random variable that denotes some notion of sample cost, our goal is to minimize the population cost over choices of the policy $K$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Noisy dynamics", "weight": 1.0} -->

0$, and $0 < \gamma < 1$. In contrast to the random initialization setting, the discount factor in this setting obeys $\gamma < 1$, since this is required to keep the costs finite.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Noisy dynamics", "weight": 1.0} -->

Once again, we are interested in optimizing the population cost function From here, the word policy will always refer to a linear policy, and since we work with this natural parametrization of the cost function, our problem has effective dimension $D = {m \cdot k}$, given by the product of state and control dimensions.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Noisy dynamics", "weight": 1.0} -->

A policy $K$ is said to stabilize the system $(A,B)$ if we have ${\rho_{\text{spec}}{({A - {BK}})}} < 1$, where $\rho_{\text{spec}}{( \cdot )}$ denotes the spectral radius of a matrix. We assume throughout that the LQR system to be optimized is controllable, meaning that there exists some policy $K$ satisfying the condition ${\rho_{\text{spec}}{({A - {BK}})}} < 1$. Furthermore, we assume access to *some* policy $K_{0}$ with finite cost; this is a mild assumption that is can be satisfied in a variety of ways; see the related literature by Fazel et al. and Dean et al.. We use such a policy $K_{0}$ as an initialization for our algorithms.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Some properties of the LQR cost function", "weight": 1.0} -->

First, it is important to note that both the population cost functions $\left( {\mathcal{C}_{{\mathsf{i}\mathsf{n}\mathsf{i}\mathsf{t}},\gamma}{(K)}},{\mathcal{C}_{{\mathsf{d}\mathsf{y}\mathsf{n}},\gamma}{(K)}} \right)$ are non-convex. In particular, for any unstable policy, the state sequence blows up and the costs becomes infinite, but as noted by Fazel et al., the stabilizing region $\{ K:{{\rho_{\text{spec}}{({A - {BK}})}} < 1}\}$ is non-convex, thereby rendering our optimization problems non-convex.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Some properties of the LQR cost function", "weight": 1.0} -->

In spite of this non-convexity, the cost functions exhibit many properties that make them amenable to fast stochastic optimization methods. Variants of the following properties were first established by Fazel et al. for the random initialization cost function $\mathcal{C}_{{\mathsf{i}\mathsf{n}\mathsf{i}\mathsf{t}},\gamma}$. The following Lemma 1. ‣ 2.2.1 Some properties of the LQR cost function ‣ 2.2 Optimal control background ‣ 2 Background and problem set-up") and Lemma 2. ‣ 2.2.1 Some properties of the LQR cost function ‣ 2.2 Optimal control background ‣ 2 Background and problem set-up") require certain refinements of their claims, which we prove in Appendix A. Lemma 3. ‣ 2.2.1 Some properties of the LQR cost function ‣ 2.2 Optimal control background ‣ 2 Background and problem set-up") follows directly from Lemma 3 in Fazel et al.. Lemma 4.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Some properties of the LQR cost function", "weight": 1.0} -->

‣ 2.2.1 Some properties of the LQR cost function ‣ 2.2 Optimal control background ‣ 2 Background and problem set-up") relates the population cost of the noisy dynamics model to that of the random initialization model in a pointwise sense.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Stochastic zero-order oracle in LQR", "weight": 1.0} -->

Let us now describe the form of observations that we make in the LQR system. Recall that we are operating in the derivative-free setting, where we have access to only (noisy) function evaluations and not the problem parameters; in particular, the tuple $(A,B,Q,R)$ that parametrizes the LQR problem is unknown.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Stochastic zero-order oracle in LQR", "weight": 1.0} -->

Our observations consist of the noisy function evaluations $\mathcal{C}_{{\mathsf{i}\mathsf{n}\mathsf{i}\mathsf{t}},\gamma}{(K;s_{0})}$ or $\mathcal{C}_{{\mathsf{d}\mathsf{y}\mathsf{n}},\gamma}{(K;\mathcal{Z})}$. We consider both the one-point and two-point settings in the former case. In the one-point setting for the randomly initialized model, a *query* of the function at the point $K$ obtains the noisy function value $\mathcal{C}_{{\mathsf{i}\mathsf{n}\mathsf{i}\mathsf{t}},\gamma}{(K;s_{0})}$ for an initial state $s_{0}$ drawn at random from the distribution $\mathcal{D}_{0}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Stochastic zero-order oracle in LQR", "weight": 1.0} -->

In the two-point setting, a query of the function at the points $(K,K')$ obtains the pair of noisy function values $\mathcal{C}_{{\mathsf{i}\mathsf{n}\mathsf{i}\mathsf{t}},\gamma}{(K;s_{0})}$ and $\mathcal{C}_{{\mathsf{i}\mathsf{n}\mathsf{i}\mathsf{t}},\gamma}{(K';s_{0})}$ for an initial state $s_{0}$ drawn at random; this setting has an immediate operational interpretation as running two policies with the same random initialization. The one-point query model is defined analogously for the noisy dynamics cost $\mathcal{C}_{{\mathsf{d}\mathsf{y}\mathsf{n}},\gamma}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Stochastic zero-order oracle in LQR", "weight": 1.0} -->

A few points regarding our query model merit discussion. First, note that in the context of the control objective, each query produces a noisy sample of the long term trajectory cost, and so our sample complexity is measured in terms of the number of *rollouts*, or trajectories. Such an assumption is reasonable since the "true" sample complexity that also takes into account the length of the trajectories is only larger by a small factor---the truncated, finite cost converges exponentially quickly to the infinite sum for stable policies.^55^5To elaborate further on this point, note that the length of the rollout required to obtain a $\delta$-accurate cost evaluation for policy $K$ will depend on both $\delta$ as well as the eigen-structure of the matrix $A - {BK}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Stochastic zero-order oracle in LQR", "weight": 1.0} -->

However, assuming that this matrix has maximum eigenvalue $\rho < 1$ (which is a common assumption in the related literature ), the dependence on $\delta$ is quite mild: we only require a rollout of length $\mathcal{O}\left( {\log{({1/\delta})}} \right)$, with the constant pre-factor depending on $\rho$ (or equivalently, on $\mathcal{C}{(K_{0})}$. Since we are interested in obtaining $\epsilon$-approximations to the optimal policy, it suffices to obtain ${\mathsf{p}\mathsf{o}\mathsf{l}\mathsf{y}}{(\epsilon)}$-approximate cost evaluations per trajectory to avoid a blow-up of the bias in our estimates (see, e.g., ), and this only adds another factor $\log{({1/\epsilon})}$ to our sample complexity when measured in terms of the number of iterations.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Stochastic zero-order oracle in LQR", "weight": 1.0} -->

To avoid tracking these additional factors, we work with the offline setting defined above. The offline nature of the query model also assumed access to restarts of the system, which can be obtained in a simulation environment. Second, we note that while the one-point query model was studied by Fazel et al. for the random initialization model---albeit with sub-optimal guarantees---we also study a two-point query model, which is known to lead to faster convergence rates in zero-order stochastic optimization.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Stochastic zero-order oracle in LQR", "weight": 1.0} -->

Finally, note that our setting of the problem---in which we are only given access to (noisy) evaluations of the cost of the policy and not to the state sequence---intentionally precludes the use of procedures that rely on observations of the state sequence. This setting allows us to distill the difficulties of truly 'model-free' control, since it prevents any possibility of constructing a dynamics model from our observations; the latter is, loosely speaking, the guiding principle of model-based control. This is not to suggest that practical applications of learning-based LQR control take this form, but rather to provide a concrete framework within which model-based and model-free algorithms can be separated, by endowing them with distinct information oracles. In doing so, we hope to lay the broader foundations for studying derivative-free methods in the context of model-free reinforcement learning.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Main results", "weight": 1.0} -->

We now turn to a statement of our main result, which characterizes the convergence rate of a natural derivative-free algorithm for any (population) function that satisfies certain PL and smoothness properties. We thus obtain, as corollaries, rates of zero-order optimization algorithms when applied to the functions $\mathcal{C}_{{\mathsf{i}\mathsf{n}\mathsf{i}\mathsf{t}},\gamma}$ and $\mathcal{C}_{{\mathsf{d}\mathsf{y}\mathsf{n}},\gamma}$; these corollaries are collected in Section 3.3.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Stochastic zero-order algorithm", "weight": 1.0} -->

We analyze a standard zero-order algorithm for stochastic optimization in application to the LQR problem. We begin by introducing some notation required to describe this algorithm, operating in the general setting where we want to optimize a function $f:{\mathcal{X}\mapsto}$ of the form ${f{(x)}} = {{\mathbb{E}}_{\xi \sim \mathcal{D}}{\lbrack{F{(x;\xi)}}\rbrack}}$. Here we assume the inclusion $\mathcal{X} \subseteq^{d}$, and let $\mathcal{D}$ denote a generic source of randomness in the zero-order function evaluation.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Stochastic zero-order algorithm", "weight": 1.0} -->

The zero-order algorithms that we study here use noisy function evaluations in order to construct near-unbiased estimates of the gradient. Let us now describe how such an estimate is constructed in the one-point and two-point settings. Let ${\mathbb{S}}^{d - 1} = {\{ u \in {{}_{}^{d}:} \parallel u \parallel_{2} = 1\}}$ denote the $d$-dimensional unit shell. Let ${Unif}{({\mathbb{S}}^{d - 1})}$ denote the uniform distribution over the set ${\mathbb{S}}^{d - 1}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Stochastic zero-order algorithm", "weight": 1.0} -->

For a given scalar $r > 0$ and a random direction $u \sim {{Unif}{({\mathbb{S}}^{d - 1})}}$ chosen independently of the random variable $\xi$, consider the one point gradient estimate Here $\xi$ should be viewed as an instantiation of the underlying random variable; in the two point setting, we compute a gradient estimate with the *same instantiation* of the noise used to evaluate $F$ at the points $x \pm {ru}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Stochastic zero-order algorithm", "weight": 1.0} -->

In both the one-point and two-point cases, the resulting ratios are almost unbiased approximations of the secant ratio that defines the derivative at $x$, and these approximations get better and better as the *smoothing radius* $r$ gets smaller. On the other hand, small values of the radius $r$ may result in estimates with large variance. Our algorithms make use of such randomized approximations in a sequence of rounds by choosing appropriate values of the radius $r$; the general form of such an algorithm is stated below.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Stochastic zero-order algorithm", "weight": 1.0} -->

1:Given iteration number T ≥ 1, initial point x0 ∈ 𝒳, step size η > 0 and smoothing radius r > 0 3: Sample ξt ∼ 𝒟 and ut ∼ Unif (𝕊d − 1) 4: ${g{(x_{t})}}\leftarrow\left\{ \begin{array}{lc} operating in one-point setting}} & \\{g_{r}^{2}{(x_{t},u_{t},\xi_{t})}\text{~if operating in two-point \end{array} \right.$ Algorithm 1 Stochastic Zero-Order Method

<!-- chunk {"id": "body-0045", "role": "body", "section": "Convergence guarantees", "weight": 1.0} -->

We now turn to analyzing Algorithm 1 in the settings of interest. In particular, our first (main) theorem is stated as a generic optimization result for non-convex functions which are (locally) smooth and satisfy the PL inequality, which we then specialize to various LQR settings.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Convergence guarantees", "weight": 1.0} -->

As mentioned before, the difficulty of optimizing the LQR cost functions is governed by multiple factors such as stability, non-convexity of the feasible set, and non-convexity of the objective. Furthermore, the Lipschitz gradient and Lipschitz properties for this cost function only hold locally with the radius of locality depending on the current iterate. Most crucially, the function is infinite outside of the region of stability, and so large steps can have disastrous consequences since we do not have access to a projection oracle that brings us back into the region of stability. It is thus essential to control the behavior of our stochastic, high variance algorithm over the entire course of optimization.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Convergence guarantees", "weight": 1.0} -->

Our strategy to overcome these challenges is to perform a careful martingale analysis, showing that the iterates remain bounded throughout the course of the algorithm; the rate depends, among other things, on the variance of the gradient estimates obtained over the course of the algorithm. By showing that the algorithm remains within the region of finite cost, we can also obtain good bounds on the local Lipschitz constants and gradient smoothness parameters, so that our step-size can be set accordingly.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Convergence guarantees", "weight": 1.0} -->

Let us now introduce some notation in order to make this intuition precise. We operate once again in the setting of general function optimization, i.e., we are interested in optimizing a function ${f{(x)}} = {{\mathbb{E}}_{\xi}{\lbrack{F{(x;\xi)}}\rbrack}}$ obeying the (global) PL inequality with constant $\mu$, as well as certain local curvature conditions.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Convergence guarantees", "weight": 1.0} -->

Recall that we are given an initial point $x_{0}$ with finite cost $f{(x_{0})}$; the global upper bound on the cost that we target in the analysis is set according to the cost $f{(x_{0})}$ of this initialization. Given the initial gap to optimality $\Delta_{0}: = f{(x_{0})} - f{(x^{\ast})}$, we define the set corresponding to points $x$ whose cost gap is at most ten times the initial cost gap $\Delta_{0}$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Convergence guarantees", "weight": 1.0} -->

Assume that the function $f$ is $(\phi_{x},\beta_{x4pt})$ locally smooth and $(\lambda_{x},\zeta_{x4pt})$ locally Lipschitz at the point $x$. Thus, both of these properties hold simultaneously within a neighborhood of radius $\rho_{x} = {\min{\{\beta_{x4pt},\zeta_{x4pt}\}}}$ of the point $x$. Now define the quantities By defining these quantities, we have effectively transformed the local properties of the function $f$ into global properties that hold over the bounded set $\mathcal{G}^{0}$. We also define a convenient functional of these curvature parameters $\theta_{0}: = \min\left\{ \frac{1}{2\phi_{0}},\frac{\rho_{0}}{\lambda_{0}} \right\}$, which simplifies the statements of our results.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Convergence guarantees", "weight": 1.0} -->

Importantly, these smoothness properties only hold locally, and so we must also ensure that the steps taken by our algorithm are not too large. This is controlled by both the step-size as well as the norms of our gradient estimate $g$ computed over the course of the algorithm. Define the uniform bounds on the point-wise gradient norm and its variance, respectively. Note that these quantities also depend implicitly on the smoothing radius $r$ and on how the gradient estimate $g$ is computed.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Convergence guarantees", "weight": 1.0} -->

With this set-up, we are now ready to state the main result regarding the convergence rate of Algorithm 1 on the functions of interest. Note that here and throughout the rest of the paper, $C$ denotes some universal constant (which may change from line to line). For two sequences $g_{n}$ and $h_{n}$, we also use the standard notation $g_{n} \sim h_{n}$ and $g_{n} = {\Theta{(h_{n})}}$ interchangeably, to mean that the sequences are within a (universal) constant multiplicative factor of each other.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

Theorem 1 yields immediate consequences for LQR optimization in various settings, and the dependence of the optimization rates on the tolerance $\epsilon$ is summarized by Table 1. We state and discuss precise versions of these results below.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

#queries T

<!-- chunk {"id": "body-0055", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

$\mathcal{O}\left(\sqrt{\epsilon} \right)$ $\overset{\sim}{\mathcal{O}}\left(\epsilon^{- 2} \right)$ $\mathcal{O}\left(\sqrt{\epsilon} \right)$ $\overset{\sim}{\mathcal{O}}\left(\epsilon^{- 1} \right)$ Table 1: Derivative-free complexity of LQR optimization under the two query models, as a function of the final error tolerance ϵ. The multiplicative pre-factors are functions of the effective dimension D and curvature parameters, and differ in the three cases; see the statements of the corollaries below.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

First, let us consider the random initialization model. From the various lemmas in Section 2.2.1, we know that the population objective $\mathcal{C}_{{\mathsf{i}\mathsf{n}\mathsf{i}\mathsf{t}},\gamma}{(K)}$ is locally $(\phi_{K4pt},\beta_{K4pt})$ smooth and $(\lambda_{K4pt},\zeta_{K4pt})$ Lipschitz, and also globally $\mu_{\mathsf{l}\mathsf{q}\mathsf{r}}$-PL. By assumption, we are given a starting point $K_{0}$ having finite population cost $\mathcal{C}_{{\mathsf{i}\mathsf{n}\mathsf{i}\mathsf{t}},\gamma}{(K_{0})}$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

Now define the quantities thereby transforming the local smoothness properties of the function $\mathcal{C}_{{\mathsf{i}\mathsf{n}\mathsf{i}\mathsf{t}},\gamma}$ into global properties that hold over the bounded set $\mathcal{G}^{0}$. Once again, let $\theta_{\mathsf{l}\mathsf{q}\mathsf{r}}: = \min\left\{ \frac{1}{2\phi_{\mathsf{l}\mathsf{q}\mathsf{r}}},\frac{\rho_{\mathsf{l}\mathsf{q}\mathsf{r}}}{\lambda_{\mathsf{l}\mathsf{q}\mathsf{r}}} \right\}$ be a functional of these curvature parameters that simplifies the statements of our results. ^66^6Let us make a brief comment on the finiteness of these quantities in the absence of compactness.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

With this setup, we now establish the following corollaries for derivative-free policy optimization for linear quadratic systems.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Dependence on $\\epsilon$", "weight": 1.0} -->

Our bounds illustrate two distinct dependences on the tolerance parameter $\epsilon$. In particular, the zero-order complexity scales proportional to $\epsilon^{- 2}$ for both one-point settings (Corollaries 1. ‣ 3.3 Consequences for LQR optimization ‣ 3 Main results") and 3. ‣ 3.3 Consequences for LQR optimization ‣ 3 Main results")), but proportional to $\epsilon^{- 1}$ in the two-point setting (Corollary 2. ‣ 3.3 Consequences for LQR optimization ‣ 3 Main results")). As alluded to before, this distinction arises due to the lower variance of the gradient estimator in the two-point setting. Lemma 1. ‣ 2.2.1 Some properties of the LQR cost function ‣ 2.2 Optimal control background ‣ 2 Background and problem set-up") establishes the Lipschitz property of the LQR cost function for each instantiation of the noise variable $s_{0}$, which ensures that the Lipschitz constant of our *sample* cost function is also bounded; therefore, the noise of the problem reduces as we approach the optimum solution.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Dependence on $\\epsilon$", "weight": 1.0} -->

In contrast, the optimization problem with one-point evaluations becomes more difficult the closer we are to the optimum solution, since the noise remains constant, while the "signal" in the problem (measured by the rate of decrease of the population cost function) reduces as we approach the optimum. The $O{({1/\epsilon^{2}})}$ dependence in the one-point settings is reminiscent of the complexity required to optimize strongly convex and smooth functions, and it would be interesting if a matching lower bound could also be proved in this LQR setting^77^7Note that this lower bound follows immediately for the class of PL and smooth functions.. Even in the absence of such a lower bound, the one-point setting is strictly worse than the two-point setting even with respect to the other parameters of the problem, which we discuss next. Figure 2 shows the convergence rate of the algorithm in all three settings as a function of $\epsilon$, where we confirm that scalings in practice corroborate our theory quite accurately.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Dependence on $\\epsilon$", "weight": 1.0} -->

It is also worth noting that model-based algorithms for this problem require $\mathcal{O}\left( \epsilon^{- 1} \right)$ trajectory samples to return an $\epsilon$-approximate policy in the noisy dynamics setting (see, e.g. ). Thus, while a one-point zero-order method is outperformed by these algorithms---note that the comparison is not quite fair, since zero-order algorithms only require access to noise cost evaluations and not the state sequence---a two-point variant is similar to model-based methods in its dependence^88^8Note that the comparison is inherently imprecise, since we are comparing upper bounds to upper bounds. In practice, one would certainly prefer the use of a model-based method when provided access to the state sequence. on $\epsilon$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Dependence on dimension", "weight": 1.0} -->

The dependence on dimension enters once again via our bound on the variance of the gradient estimate, as is typical of many derivative-free procedures. The two-point setting gives rise to the best dimension dependence (linear in $D$), and the reason is similar to why this occurs for convex optimization. It is particularly interesting to compare the dimension dependence to results in model-based control. There, in the noisy dynamics model, the sample complexity scales with the sum of state and control dimensions $m + k$, whereas the dependence in the two-point setting is on their product $D = {m \cdot k}$. However, each observation in that setting consists of a state vector of length $m$, while here we only get access to scalar cost values, and so in that loose sense, the complexities of the two settings are comparable.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Dependence on dimension", "weight": 1.0} -->

In the one-point setting, the dependence on dimension is significantly poorer, and at least quadratic. This of course ignores other dimension-dependent factors such as $C_{m}$, as well as the curvature parameters $(\phi_{\mathsf{l}\mathsf{q}\mathsf{r}},\lambda_{\mathsf{l}\mathsf{q}\mathsf{r}},\mu)$ (see the discussion below).

<!-- chunk {"id": "body-0064", "role": "body", "section": "Dependence on curvature parameters", "weight": 1.0} -->

The iteration complexity scales linearly in the smoothness parameter of the problem $\phi_{\mathsf{l}\mathsf{q}\mathsf{r}}$, and quadratically in the other curvature parameters. See Appendix A.3 ‣ Appendix A Properties of the randomly initialized LQR problem") for precise definitions of these parameters for the LQR problem. In particular, it is worth noting that our tightest bounds for these quantities depend on the dimension of the problem implicitly for some LQR instances, and are actually lower-order polynomials of the initial cost. In practice, however, it is likely that much sharper bounds can be proved on these parameters, e.g., in simulation (see Figure 3), the dependence of the sample complexity on the initial cost is in fact relatively weak---of the order $\mathcal{C}{(K_{0})}^{2}$---and our bounds are clearly not sharp in that sense.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Proofs of main results", "weight": 1.0} -->

In this section, we provide proofs of Theorem 1, and Corollaries 1. ‣ 3.3 Consequences for LQR optimization ‣ 3 Main results"), 2. ‣ 3.3 Consequences for LQR optimization ‣ 3 Main results"), and 3. ‣ 3.3 Consequences for LQR optimization ‣ 3 Main results"). The proofs of the corollaries require many technical lemmas, whose proofs we postpone to the appendix.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Case 1", "weight": 1.0} -->

Assume that $\tau > t$, so that we have the inclusion $x_{t} \in \mathcal{G}^{0}$. In addition, note that the iterate $x_{t + 1}$ is obtained after a stochastic zero-order step whose size is bounded as where we have used the fact that $\eta \leq \frac{\rho_{0}}{G_{\infty}}$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Case 1", "weight": 1.0} -->

We may thus apply Lemma 5 to obtain

<!-- chunk {"id": "body-0068", "role": "body", "section": "Case 2", "weight": 1.0} -->

In this case, we have $\tau \leq t$, so that Now combining the bounds (18a) and (18b) from the the two cases yields the inequality Taking expectations over the sigma-field $\mathcal{F}_{t}$ and then arguing inductively yields Setting ${t + 1} = T$ then establishes the first part of the proposition with substitutions of the various parameters.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Case 2", "weight": 1.0} -->

We now turn to establishing that ${{\mathbb{P}}{\{{\tau > T}\}}} \geq {4/5}$. We do so by setting up a suitable super-martingale on our iterate sequence and appealing to classical maximal inequalities. Recall that we run the algorithm for $2T$ steps for convenience, and thereby obtain a set of $2T$ random variables $\{\Delta_{1},\ldots,\Delta_{2T}\}$. With the stopping time $\tau$ defined as before, define the stopped process Note that by construction, each random variable $Y_{t}$ is non-negative and almost surely bounded by the locally Lipschitz nature of the function.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Case 2", "weight": 1.0} -->

We claim that ${\{ Y_{t}\}}_{t = 0}^{2T}$ is a super-martingale. In order to prove this claim, we first write Beginning by bounding the first term on the right-hand side, we have where step (iii) follows from using inequality.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Case 2", "weight": 1.0} -->

Substituting the bounds (21a) and (21b) into our original inequality, we find that where step (iv) follows from the inequality ${\eta\mu\Delta_{\tau \land t}} \geq 0$. We have thus verified the super-martingale property.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Case 2", "weight": 1.0} -->

Finally, applying Doob's maximal inequality for super-martingales (see, e.g. 15) yields where step (v) follows from the substitutions $T = {\frac{4}{\eta\mu}{\log{({{120\Delta_{0}}/\epsilon})}}}$, and $\eta \leq \frac{\epsilon\mu}{240\phi_{0}G_{2}}$. As long as $\epsilon$ is sufficiently small so as to ensure that ${\epsilon{\log{({{120\Delta_{0}}/\epsilon})}}} < {5\Delta_{0}}$, setting $\nu = {10\Delta_{0}}$ completes the proof.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Second moment control", "weight": 1.0} -->

Using the law of iterated expectations, we have Define the placeholder variable $q$ and now evaluate: where equality (i) follows from the fact that $u$ is a unit vector and inequality (ii) follows from the inequality ${({a - b})}^{2} \leq {2{({a^{2} + b^{2}})}}$. We further simplify this to obtain: where inequality (i) follows from the symmetry of the uniform distribution on the sphere, and inequality (ii) follows from Jensen's inequality. For a fixed $\xi$, we now define $q = {{\mathbb{E}}{\lbrack\left. {F{({x + {ru}},\xi)}} \middle| \xi \right.\rbrack}}$. Substituting this expression yields where inequality (i) follows directly from Lemma 9 in Shamir. The lemma can be applied since we are conditioning on $\xi$, and all the randomness lies in the selection of $u$. We have thus established the claim in part (c).

<!-- chunk {"id": "body-0074", "role": "body", "section": "Gradient estimates are bounded", "weight": 1.0} -->

Note that smoothing radius $r$ satisfies $r \leq \rho_{0}$, where $\rho_{0}$ is the radius within which the function is Lipschitz. Consequently, the local Lipschitz property of $F$ implies that

<!-- chunk {"id": "body-0075", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this paper, we studied the model-free control problem over linear policies through the lens of derivative-free optimization. We derived quantitative convergence rates for various zero-order methods when applied to learn optimal policies based on data from noisy linear systems with quadratic costs. In particular, we showed that one-point and two-point variants of a canonical derivative-free optimization method achieve fast rates of convergence for the non-convex LQR problem. Notably, our proof deals directly with some additional difficulties that are specific to this problem and do not arise in the analysis of typical optimization algorithms. More precisely, our proof involves careful control of both the (potentially) unbounded nature of the cost function, and the non-convexity of the underlying domain. Interestingly, our proof only relies on certain local properties of the function that can be guaranteed over a bounded set; for this reason, the optimization-theoretic result in this paper (stated as Theorem 1) is more broadly applicable beyond the RL setting.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Discussion", "weight": 1.5} -->

While this paper analyzes a canonical zero-order optimization algorithm for model-free control of linear quadratic systems, many open questions remain. One such question concerns lower bounds for LQR problems in the model-free setting, thereby showing quantitative gaps between such a setting and that of model-based control. While we conjecture that the convergence bounds of Corollaries 1. ‣ 3.3 Consequences for LQR optimization ‣ 3 Main results"), 2. ‣ 3.3 Consequences for LQR optimization ‣ 3 Main results"), and 3. ‣ 3.3 Consequences for LQR optimization ‣ 3 Main results") are sharp in terms of their dependence on the error tolerance $\epsilon$, establishing this rigorously will require ideas from the extensive literature on lower bounds in zero-order optimization. Another important direction is establish the sharpness (or otherwise) of our bounds in terms of the dimension of the problem, as well as to obtain tight characterizations of the local curvature parameters of the problem around a particular policy $K$ in terms of the cost at $K$.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Discussion", "weight": 1.5} -->

We also mention that our sharp characterizations of the cost function are likely to be useful in sharpening analyses^99^9Here again, the techniques of Fazel et al. yield a bound of the order $\overset{\sim}{\mathcal{O}}\left( \epsilon^{- 4} \right)$, but we conjecture that this bound should be improvable at least to $\overset{\sim}{\mathcal{O}}\left( \epsilon^{- 2} \right)$. of the natural gradient algorithm as well as in analyzing the popular REINFORCE algorithm as applied to the LQR problem. We leave these interesting questions to future work.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Discussion", "weight": 1.5} -->

In the broader context of model-free reinforcement learning as well, there are many open questions. First, a derivative-free algorithm over linear policies is reasonable even in other systems; can we establish provable guarantees over larger classes of problems? Second, there is no need to restrict ourselves to linear policies; in practical RL systems, derivative-free algorithms are run for policies that parametrized in a much more complex fashion. How does the sample complexity of the problem change with the class of policies over which we are optimizing?
