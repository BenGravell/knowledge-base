<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Derivative-Free Methods for Policy Optimization: Guarantees for Linear Quadratic Systems

Topics include Optimization, Derivative-free, Policy optimization.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study derivative-free methods for policy optimization over the class of linear policies. We focus on characterizing the convergence rate of these methods when applied to linear-quadratic systems, and study various settings of driving noise and reward feedback. We show that these methods provably converge to within any pre-specified tolerance of the optimal policy with a number of zero-order evaluations that is an explicit polynomial of the error tolerance, dimension, and curvature properties of the problem. Our analysis reveals some interesting differences between the settings of additive driving noise and random initialization, as well as the settings of one-point and two-point reward feedback. Our theory is corroborated by extensive simulations of derivative-free methods on these systems. Along the way, we derive convergence rates for stochastic zero-order optimization algorithms when applied to a certain class of non-convex problems.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent years have witnessed a number of successes in applying modern reinforcement learning (RL) methods to many fields, including [tobin17, levine15] and competitive gaming[silver16, mnih15]. Impressively, most of these successes have been achieved by using general-purpose RL methods that are applicable to a host of problems. Prevalent general-purpose RL approaches can be broadly categorized into: (a) model-based approaches[deisenroth2012,gu2016,lillicrap2015], in which an agent attempts to learn a model for the dynamics by observing the evolution of its state sequence; and (b) model-free approaches, including DQN[mnih15], and TRPO[schulman15], in which the agent attempts to learn an optimal policy directly, by observing rewards from the environment. While model-free approaches typically require more samples to learn a policy of equivalent accuracy, they are naturally more robust to model mis-specification.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A literature that is closely related to model-free RL is that of zero-order or derivative-free methods for stochastic optimization; see the book by[spall03] for an overview. Here, the goal is to optimize an unknown function from noisy observations of its values at judiciously chosen points. While most analytical results in this space apply to convex optimization, many of the procedures themselves rely on moving along randomized approximations to the directional derivatives of the function being optimized, and are thus applicable even to non-convex problems. In the particular context of RL, variants of derivative-free methods, including TRPO[schulman15], PSNG[rajeswaran17] and evolutionary strategies[salimans2017], have been used to solve highly non-convex optimization problems and have been shown to achieve state-of-the-art performance on various RL tasks.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

While many RL algorithms are easy to describe and run in practice, certain theoretical aspects of their behavior remain mysterious, even when they are applied in relatively simple settings. One such setting is the most canonical problem in continuous control, that of controlling a linear dynamical system with quadratic costs, a problem known as the linear quadratic regulator (LQR). A recent line of [abbasi2011, abbasi2018, abeille2017, cohen18, dean17, dean18, faradonbeh17, kakade18, tu18, tu182] has sought to delineate the properties and limitations of various RL algorithms in application to LQR problems. An appealing property of LQR systems from an analytical point of view is that the optimal policy is guaranteed to be linear in the states[kalman60,]. Thus, when the system dynamics are known, as in classical control, the optimal policy can be obtained by solving the discrete-time algebraic Ricatti In contrast, methods in reinforcement learning target the case of unknown dynamics, and seek to learn an optimal policy on the basis of observations.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A basic form of model-free RL for linear quadratic systems involves applying derivative-free methods in the space of linear policies. It can be used even when the only observations possible are the costs from a set of rollouts, each referred to as a Such an offline setting with multiple, restarted rollouts should be contrasted with an online setting, in which the agent interacts continuously with the environment, and no hard resets are allowed. In contrast to the offline setting, the goal in the online setting is to control the system for all time steps while simultaneously learning better policies, and performance is usually measured in terms of regret., and when our goal is to obtain a policy whose cost is at most $\epsilon$-suboptimal. The sample complexity of a given method refers to the number of samples, as a function of the problem parameters and tolerance, required to meet a given tolerance $\epsilon$. With this context, we are led to the following concrete question: What is the sample complexity of derivative-free methods for the linear quadratic regulator? This question underlies the analysis in this paper.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In particular, we study a standard derivative-free algorithm in an offline setting and derive explicit bounds on its sample complexity, carefully controlling the dependence on not only the tolerance $\epsilon$, but also the dimension and conditioning of the underlying problem.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our analysis treats two distinct forms of randomness in the underlying linear system. In the first setting more commonly assumed in practicethe linear updates are driven by an additive noise term[dean17], whereas in the second setting, the initial state is chosen randomly but the linear dynamics remain deterministic[kakade18]. We refer to these two settings, respectively, as the additive noise setting, and the randomly initialized setting. We are now in a position to discuss related work on the problem, and to state our contributions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Quantitative gaps between model-based and model-free reinforcement learning have been studied extensively in the setting of finite [agrawal2017, dann2017, azar2017], and several interesting questions here still remain open.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

For continuous state-action spaces and in the specific context of the linear quadratic systems, classical system identification has been model-based, with a particular focus on asymptotic results (e.g., see [ljung1987] as well as references therein). Non-asymptotic guarantees for model-based control of linear quadratic systems were first obtained by[fietcher97], who studied the offline problem under additive noise and obtained non-asymptotic rates for parameter identification using nominal control procedures. In more recent work, Dean et al.[dean17] proposed a robust alternative to nominal control, showing an improved sample complexity as well as better-behaved policies. The online setting for model-based control of linear quadratic systems has also seen extensive study, with multiple algorithms known to achieve sub-linear regret[dean18, abbasi2011, abeille2017, ibrahimi12, cohen19].

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we study model-free control of these systems, a problem that has seen some recent work in both the offline online[abbasi2018] settings. Most directly relevant to our work is the paper of Fazel et al.[kakade18], who studied the offline setting for the randomly initialized variant of the LQR, and showed that a population version of gradient descent (and natural gradient descent), when run on the non-convex LQR cost objective, converges to the global optimum. In order to turn this into a derivative-free algorithm, they constructed near-exact gradient estimates from reward samples and showed that the sample complexity of such a procedure is bounded polynomially in the parameters of the problem; however, the dependence on various parameters is not made explicit in their analysis. We remark that Fazel et al. also show polynomially bounded sample complexity for a zero order algorithm which builds near exact estimates of the naturalgradient, although this requires access to a stronger oracle than the one assumed in this paper.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Also of particular relevance to our paper is the extensive literature on zero-order optimization. Flaxman et al. [flax04] showed that these methods can be analyzed for convex optimization by making an explicit connection to function smoothing, and Agarwal et al.[agarwal10] improved some of these convergence rates. Results are also available for strongly convex[jamrec12], smooth[ghalan13] and convex[nesterov11, duchi15, wang17] functions, with Shamir characterizing the fundamental limits of many problems in this space[shamir12, shamir17]. Broadly speaking, all of the methods in this literature can be seen as variants of stochastic search: they proceed by constructing estimates of directional derivatives of the function from randomly chosen zero order evaluations. In the regime where the function evaluations are stochastic, different convergence rates are obtained based on whether such a procedure uses a one-point estimate that is obtained from a single function evaluation[flax04], or a $k$-point estimate[agarwal10] for some $k \geq 2$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

There has also been some recent work on zero-order optimization of non-convex functions satisfying certain smoothness properties that are motivated by statistical estimation[wang18].

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we study both randomly initialized and additive-noise linear quadratic systems in the offline setting through the lens of derivative-free optimization. We begin with a general result that characterizes the convergence behavior of a canonical derivative-free algorithm when applied to a general class of functions satisfying certain curvature conditions. In particular, our main contribution is to establish upper bounds on the sample complexity as a function of the dimension, error tolerance, and curvature parameters of the problem instance. We then specialize this result to a variety of LQR models. In contrast to prior work, the rates that we provide are explicit, and the algorithms that we analyze are standard and practical one-point and two-point variants of the random search heuristic. Our results reveal interesting dichotomies between the settings of one-point and two-point feedback, as well as the models involving random initialization and additive noise. Our main contribution is stated in the following informal theorem (to be stated more precisely in the sequel): Main Theorem (informal).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

With high probability, one can obtain an $\epsilon$-approximate solution to any linear quadratic system from observing the noisy costs of $\widetilde{\mathcal{O}}(1 / \epsilon^2)$ trajectories from the system, which can be further reduced to $\widetilde{\mathcal{O}}(1 /\epsilon)$ trajectories when pairs of costs are observed for each In our theoretical statements, the multiplicative pre-factors are explicit lower-order polynomials of the dimension of the state space, and curvature properties of the cost function. From a technical standpoint, we build upon some known properties of the LQR cost function established in past work on randomly initialized [kakade18], and establish de novo some analogous properties for the additive noise setting.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

We also isolate and sharpen some key properties that are essential to establishing sharp rates of zero-order optimization; as an example, for the setting with random-initialization and one-point reward feedback studied by Fazel et al.[kakade18], establishing these properties allows us to analyze a natural algorithm that improves While the rates established by Fazel et al. are not explicit, their analysis is conservative and yields a bound of order $1/\epsilon^4$ up to logarithmic factors. To be clear, the properties that we establish also enable us to provide a sharper analysis of their algorithm; see Appendixapp:fazel to follow. the dependence of the bound on the error tolerance $\epsilon$ from at least $\order{1/\epsilon^4}$ to $\order{1/\epsilon^2}$. Crucially, our analysis is complicated by the fact that we must ensure that the iterates are confined to the region in which the linear system is stable, and such stability considerations introduce additional restrictions on the parameters used in our optimization

<!-- chunk {"id": "body-0017", "role": "body", "section": "Optimization background", "weight": 1.0} -->

We first introduce some standard optimization related background and assumptions, and make the zero-order setting precise.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Optimization background", "weight": 1.0} -->

Stochastic zero-order optimization: We consider optimization problems of the form \min_{\x \in \mathcal{X}} \ensuremath{f}(\x) &:\,= \Exs_{\xi \sim \mathcal{D}}{\left[\ensuremath{F}(\x, \xi)\right]}, where $\xi$ is a zero mean random variable While the zero mean assumption on $\xi$ is not strictly necessary for generic optimization, the canonical (additive noise) LQR settings that we specialize our results to require noise to be zero mean. So we make this assumption at the outset for convenience. that represents the noise in the problem, and the function $\ensuremath{f}$ above can be non-convex in general with a possibly non-convex domain $\mathcal{X} \subseteq \ensuremath{\mathbb{R}}^{\ensuremath{d}}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Optimization background", "weight": 1.0} -->

In particular, we consider stochastic zero-order optimization methods with oracle access to noisy function evaluations. We operate under two distinct oracle models. The first is the one-point setting, in which the optimizer specifies a point $x \in \mathcal{X}$, and an evaluation consists of an instantiation of the random variable $\ensuremath{F}(\x, \xi)$. The second is the two-point extension of such a setting, in which the optimizer specifies a pair of points $(\x, y)$, then an instantiation of the random variable $\xi$ occurs, and the optimizer obtains the values $\ensuremath{F}(\x, \xi)$ and $\ensuremath{F}(y, \xi)$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Optimization background", "weight": 1.0} -->

Crucially, the function evaluations $\ensuremath{F}(\x, \xi)$ and $\ensuremath{F}(y, \xi)$ share the same noise, so the two-point oracle cannot be reduced to querying the one-point oracle twice (where sharing the same noise across multiple function evaluations cannot be guaranteed). Such two-point settings are known in the optimization literature to enjoy reduced variance of gradient estimates[agarwal10, duchi15, shamir17].

<!-- chunk {"id": "body-0021", "role": "body", "section": "Optimization background", "weight": 1.0} -->

Function properties: Before defining the optimization problems considered in this paper by instantiating the pair of functions $(f, F)$, let us precisely define some standard properties that make repeated appearances in the sequel.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Optimization background", "weight": 1.0} -->

A continuously differentiable function $\ensuremath{g}$ with domain $\ensuremath{\mathcal{X}}$ is said to have $(\phi, \beta)$ locally Lipschitz gradients at $x \in \ensuremath{\mathcal{X}}$ if \euclidnorm{\nabla \ensuremath{g}{(\y)} - \nabla \ensuremath{g}{(\x)}} \leq \phi \euclidnorm{\y - \x} \qquad \mbox{for all $y \in \ensuremath{\mathcal{X}}$ with $\|x-y\|_2 \leq \beta$.} We often say that $\ensuremath{g}$ has locally Lipschitz gradients, by which we mean for each $x \in \ensuremath{\mathcal{X}}$ the function $\ensuremath{g}$ has locally Lipschitz gradients, albeit with constants $(\phi, \beta)$ that may depend on

<!-- chunk {"id": "body-0023", "role": "body", "section": "Optimization background", "weight": 1.0} -->

This property guarantees that the function $\ensuremath{g}$has at most quadratic growth locally around every point, but the shape of the quadratic and the radius of the ball within which such an approximation holds may depend on the A continuously differentiable function $\ensuremath{g}$ with domain $\ensuremath{\mathcal{X}}$ is said to be $(\ensuremath{\lambda}, \zeta)$ locally Lipschitz at $x \in \ensuremath{\mathcal{X}}$ if \vert \ensuremath{g}{(\y)} - \ensuremath{g}{(\x)} \vert \leq \ensuremath{\lambda} \euclidnorm{\y - \x} \qquad \mbox{for all $\y \in \ensuremath{\mathcal{X}}$ such that $\|x-y\|_2 \leq As before, when we say that the function $\ensuremath{g}$ is locally Lipschitz, we mean that this condition holds for all

<!-- chunk {"id": "body-0024", "role": "body", "section": "Optimization background", "weight": 1.0} -->

$x \in \ensuremath{\mathcal{X}}$, albeit with parameters $(\ensuremath{\lambda}, \zeta)$ that may depend on $x$. The local Lipschitz property guarantees that the function $\ensuremath{g}$ grows no faster than neighborhood around each point.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Optimization background", "weight": 1.0} -->

A continuously differentiable function $\ensuremath{g}$ with domain $\ensuremath{\mathcal{X}}$ and a finite global minimum $\ensuremath{g}^*$ is said to be $\ensuremath{\mu}$-PL if it satisfies the Polyak-ojasiewicz (PL) inequality with constant $\ensuremath{\mu} > 0$, given by \vecnorm{\ensuremath{\nabla} \ensuremath{g}{(\x)}}^2 & \geq \ensuremath{\mu} \; \big(\ensuremath{g}{(\x)} - \ensuremath{g}^* \big) \qquad \mbox{for all $x \in \ensuremath{\mathcal{X}}$.} The PL condition, first introduced by Polyak[polyak63] and Lojasiewicz[loj63], is a relaxation of the notion of strong convexity.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Optimization background", "weight": 1.0} -->

It allows for a certain degree of non-convexity in the function $\ensuremath{g}$. Note that inequality[EqnPLInequality] yields an upper bound on the gap to optimality that is proportional to the squared norm of the gradient. Thus, while the condition admits non-convex functions, it requires that all first-order stationary points also be global minimizers. Karimi et al.[schmidt16]recently showed that many standard first-order convex optimization algorithms retain their attractive convergence guarantees over this more general

<!-- chunk {"id": "body-0027", "role": "body", "section": "Optimal control background", "weight": 1.0} -->

We now turn to some basic background on optimal control and reinforcement learning. An optimal control problem is specified by a dynamics model and a real-valued cost function. The dynamics model consists of a sequence of functions \control[t], z\_t)}\_{t \geq 0}$, which models how the state vector $\state[t]$ transitions to the next state $\state[t+1]$ when a control input $\control[t]$ is applied at a timestep $t$. The term $z_t$ captures the noise disturbance in the system. The cost function $c_t(\state[t], \control[t])$ specifies the cost incurred by taking an action $\control[t]$ in the state $\state[t]$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Optimal control background", "weight": 1.0} -->

The goal of the control problem is to find a sequence of control inputs $\braces{\control[t]}_{t \geq 0}$, dependent on the history of states $\mathcal{H}_t:\,= (\state, \state, \ldots, \state[t-1])$, so as to solve the optimization \min \mathbb{E} \left[\sum_{t \geq 0} \gamma^t c_t(\state[t], \control[t]) \right] \qquad \text{s.t. } \state[t+1] = where the expectation above is with respect to the noise in the transition dynamics as well as any randomness in the selection of control inputs, and $0 < \gamma \le 1$ represents a multiplicative discount factor. A mapping from histories $\mathcal{H}_t$ to controls $\control[t]$ is called a policy, and the above minimization is effectively over the space of policies.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Optimal control background", "weight": 1.0} -->

There is a distinction to be made here between the classical fully-observed setting in stochastic control in which the dynamics $h_t$ is knownin this case, such a problem may be solved (at least in principle) by the Bellman recursion[bertsekas2005], and the system identification setting in which the dynamics are completely unknown. We operate in the latter setting, and accommodate the further assumption that even the cost function $c_t$is unknown.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Optimal control background", "weight": 1.0} -->

In this paper, we assume that the state space is $m$-dimensional, and the control space is $k$-dimensional, so that $\state[t] \in \ensuremath{\mathbb{R}}^m$ and $\control[t] \in \ensuremath{\mathbb{R}}^k$. The linear quadratic system specifies particular forms for the dynamics and costs, respectively. In particular, the cost function obeys the quadratic form c_t = \state[t]^{\top} Q \state[t] + \control[t]^{\top} R \control[t] for a pair of positive definite matrices $(Q, R)$ of the appropriate dimensions. Additionally, the dynamics model is linear in both states and controls, and takes the form \state[t+1] = A \state[t] + B \control[t] + \error[t], where $A$ and $B$ are transition matrices of the appropriate dimension, and the random variable $\error[t]$ models additive noise in the problem which is drawn i.i.d.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Optimal control background", "weight": 1.0} -->

for each $t$ from a distribution $\mathcal{D}_{{\sf add}}$. We call this setting the noisy dynamics model.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Optimal control background", "weight": 1.0} -->

We also consider the randomly initialized linear quadratic system without additive noise, in which the state transitions obey \state[t+1] &= A \state[t] + B \control[t], and the randomness in the problem comes from choosing the initial state $\state$ at random from a distribution $\mathcal{D}_0$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Optimal control background", "weight": 1.0} -->

Throughout this paper, we assume It is important to note that our assumption of identity covariance of the noise distributions can be made without loss of generality: for a problem with known, non-identity (but full-dimensional) covariance $\Sigma$, we may reparametrize the problem with the modifications A' = ^-1/2 A ^1/2, B' = ^-1/2 B, and s'\_t = ^-1/2 s\_#1[t] for all t 0, in which case the new problem with states $s'_t$ and the pair of transition matrices $(A', B')$ is driven by noise satisfying the that for both distributions $\mathcal{D} \in \{ \mathcal{D}_{{\sf add}}, \mathcal{D}_0\}$ and for a random variable $v \sim \mathcal{D}$, we have \ensuremath{\mathbb{E}} [v] = 0, \quad \ensuremath{\mathbb{E}} [vv^\top] = I,

<!-- chunk {"id": "body-0034", "role": "body", "section": "Optimal control background", "weight": 1.0} -->

\text{ and } \| v \|_2^2 \leq While we assume boundedness of the distribution for convenience, our results extend straightforwardly to sub-Gaussian distributions by appealing to high-probability bounds for quadratic forms of sub-Gaussian random vectors and standard truncation arguments.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Optimal control background", "weight": 1.0} -->

The final iteration complexity also changes by at most poly-logarithmic factors in the problem parameters; for brevity, we operate under the assumptions[eq:propnoise] throughout the paper and omit standard calculations for sub-Gaussian By classical results in optimal control [kalman60,], the optimal controller for the LQR problem under both of these noise models takes the linear form $\control[t] = -K^* \state[t]$, for some matrix $K^* \in \mathbb{R}^{k \times m}$. When the system matrices are known, the controller matrix $K^*$ can be obtained by solving the discrete-time algebraic Riccati equation[riccati1700].

<!-- chunk {"id": "body-0036", "role": "body", "section": "Optimal control background", "weight": 1.0} -->

With the knowledge that the optimal policy is an invariant linear transformation of the state, one can re-parametrize the LQR objective in terms of the linear class of policies, and focus on optimization procedures that only search over the class of linear policies. Below, we define such a parametrization under the noise models introduced above, and make explicit the connections to the stochastic optimization model[eqn:general\_zero\_order\_prob].

<!-- chunk {"id": "body-0037", "role": "body", "section": "Optimal control background", "weight": 1.0} -->

For each choice of the (random) initial state $\state$, let $\PlainC_{{\sf init}, \gamma}(\K; s_0)$ denote the cost of executing a linear policy $\K$ from initial state $s_0$, so that \PlainC_{{\sf init}, \gamma}(\K; s_0):\,= \sum_{t=0}^{\infty} \gamma^t \bigg(\state[t]^{\top} Q \state[t] + \control[t]^{\top} R \control[t] \bigg), where we have the noiseless dynamics $\state[t+1] = A\state[t] + B \control[t]$ and $\control[t] = -\K \state[t]$ for each $t \geq 0$, and $0 < \gamma \le 1$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Optimal control background", "weight": 1.0} -->

While $\PlainC_{{\sf init}, \gamma}(\K; s_0)$ is a random variable that denotes some notion of sample cost, our goal is to minimize the population cost \PlainC_{{\sf init}, \gamma}(\K):\,= \mathbb{E}_{s_0 \sim \mathcal{D}_0} [\PlainC_{{\sf init}, \gamma}(\K; s_0)] over choices of the policy $\K$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Optimal control background", "weight": 1.0} -->

In this case, the noise in the problem is given by the sequence of $\mathcal{Z} = \{\error[t] \}_{t \geq 0}$, and for every instantiation of $\mathcal{Z} \sim \mathcal{D}_{{\sf add}}^{\mathbb{N}}:\,= (\mathcal{D}_{{\sf add}} \otimes \mathcal{D}_{{\sf add}} \otimes \ldots)$, our sample cost is given by the function \PlainC_{{\sf dyn}, \gamma}(\K; \mathcal{Z}):\,= \sum_{t = 0}^{\infty} \gamma^t \bigg(\state[t]^{\top} Q \state[t] + \control[t]^{\top} R \control[t] where we have $\state = 0$, random state evolution $\state[t+1] = A \state[t] + B

<!-- chunk {"id": "body-0040", "role": "body", "section": "Optimal control background", "weight": 1.0} -->

\control[t] + \error[t]$ and action $\control[t] = -\K \state[t]$ for each $t \geq 0$, and $0 < \gamma < 1$. In contrast to the random initialization setting, the discount factor in this setting obeys $\gamma < 1$, since this is required to keep the costs finite.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Optimal control background", "weight": 1.0} -->

From here, the word policy will always refer to a linear policy, and since we work with this natural parametrization of the cost function, our problem has effective dimension $\ensuremath{D} = m \cdot k$, given by the product of state and control dimensions. $\K$ is said to stabilize the system $(A,B)$ if we have $\rho_\text{spec}(A-B\K) < 1$, where $\rho_\text{spec}(\cdot)$ denotes the spectral radius of a matrix. We assume throughout that the LQR system to be optimized is controllable, meaning that there exists some policy $\K$ satisfying the condition $\rho_\text{spec}(A-B\K) < 1$. Furthermore, we assume access tosome policy $\K$ with finite cost; this is a mild assumption that is can be satisfied in a variety of ways; see the related literature by Fazel et al.[kakade18] and Dean et al.[dean18]. We use such a policy $\K$as an initialization for our algorithms.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Some properties of the LQR cost function", "weight": 1.0} -->

Let us turn to establishing properties of the pair of population cost $\left(\PlainC_{{\sf init}, \gamma}(\K), \PlainC_{{\sf dyn}, \gamma}(\K) \right)$ and their respective sample variants $\left(\PlainC_{{\sf init}, \gamma}(\K, s_0), \PlainC_{{\sf dyn}, \gamma}(\K; \mathcal{Z}) \right)$, in order to place the problem within the context of First, it is important to note that both the population cost functions $\left(\PlainC_{{\sf init}, \gamma}(\K), \PlainC_{{\sf dyn}, \gamma}(\K) \right)$ are non-convex.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Some properties of the LQR cost function", "weight": 1.0} -->

In particular, for any unstable policy, the state sequence blows up and the costs becomes infinite, but as noted by Fazel et al.[kakade18], the stabilizing region $\{\K: \rho_\text{spec}(A-B\K) < 1 \}$is non-convex, thereby rendering our optimization problems non-convex.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Some properties of the LQR cost function", "weight": 1.0} -->

In spite of this non-convexity, the cost functions exhibit many properties that make them amenable to fast stochastic optimization methods. Variants of the following properties were first established [kakade18] for the random initialization cost function $\PlainC_{{\sf init}, \gamma}$. The following Lemma [lem:lipschitz\_cost\_lqr] and Lemma [lem:lipschitz\_gradient\_lqr] require certain refinements of their claims, which we prove in Appendix[sec:randint\_appendix]. Lemma[lem:pl\_inequality] follows directly from Lemma 3 in Fazel et al.[kakade18]. Lemma[lem:noisy-random]relates the population cost of the noisy dynamics model to that of the random initialization model in a pointwise sense.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Some properties of the LQR cost function", "weight": 1.0} -->

Given any linear policy $\K$, there exist positive scalars $(\lipconK{\K}, \widetilde{\lipconK{\K}}, \radiustwo{\K})$, depending on the function value $\PlainC_{{\sf init}, \gamma}(\K)$, such that for all policies $K'$ satisfying ${\fronorm{K' - \K} \leq \radiustwo{\K}}$, and for all initial states $s_0$, we have \vert \PlainC_{{\sf init}, \gamma}(K') - \PlainC_{{\sf init}, \gamma}(\K) \vert &\leq \lipconK{\K} \fronorm{K' - \K}, \text{ and} \\\vert \PlainC_{{\sf init}, \gamma}(K'; s_0) - \PlainC_{{\sf init}, \gamma}(\K; s_0)

<!-- chunk {"id": "body-0046", "role": "body", "section": "Some properties of the LQR cost function", "weight": 1.0} -->

Given any linear policy $\K$, there exist positive scalars $(\radiusone{\K}, \smoothnessK{\K})$, depending on the function value $\PlainC_{{\sf init}, \gamma}(\K)$, such that for all policies $K'$ satisfying $\fronorm{K' - \K} \leq \radiusone{\K}$, we have \fronorm{\ensuremath{\nabla} \PlainC_{{\sf init}, \gamma}(K') - \ensuremath{\nabla} \PlainC_{{\sf init}, \gamma}(\K)} \leq \smoothnessK{\K} There exists a universal constant $\ensuremath{\mu_{{\sf lqr}}} > 0$ such that for all stable policies $\K$, we have \fronorm{\ensuremath{\nabla} \PlainC_{{\sf init}, \gamma}(\K)}^2 \geq

<!-- chunk {"id": "body-0047", "role": "body", "section": "Some properties of the LQR cost function", "weight": 1.0} -->

For the sake of exposition, we have stated these properties without specifying the various smoothness and PL constants. Appendix[sec:randint\_appendix] collects explicit expressions for the tuple $(\lipconK{\K}, \widetilde{\lipconK{\K}}, \smoothnessK{\K}, \radiusone{\K}, \radiustwo{\K}, \ensuremath{\mu_{{\sf lqr}}})$as functions of the parameters of the LQR problem.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Some properties of the LQR cost function", "weight": 1.0} -->

For all policies $\K$, we have \PlainC_{{\sf dyn}, \gamma}(\K) = \frac{\gamma}{1 - \gamma} \PlainC_{{\sf init}, \gamma}(\K). [lem:noisy-random] thus shows that, at least in a population sense, both the noisy dynamics and random initialization models behave identically when driven by noise with the same first two moments. Hence, the properties posited by Lemmas[lem:lipschitz\_cost\_lqr], [lem:lipschitz\_gradient\_lqr], and[lem:pl\_inequality] for the population cost function $\PlainC_{{\sf init}, \gamma}(\K)$ also carry over to the function $\PlainC_{{\sf dyn}, \gamma}(\K)$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Some properties of the LQR cost function", "weight": 1.0} -->

In particular, the cost function $\PlainC_{{\sf dyn}, \gamma}(\K)$ is also $\left(\frac{\gamma}{1 - \gamma} \smoothnessK{\K}, \radiusone{\K} \right)$ locally smooth and $\left(\frac{\gamma}{1 - \gamma} \lipconK{\K}, \radiustwo{\K} \right)$ locally Lipschitz, and also globally $\frac{\gamma}{1 - \gamma}\ensuremath{\mu_{{\sf lqr}}}$-PL. We stress that although the population costs are very similar, the observed costs in the two cases are quite different.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Stochastic zero-order oracle in LQR", "weight": 1.0} -->

Let us now describe the form of observations that we make in the LQR system. Recall that we are operating in the derivative-free setting, where we have access to only (noisy) function evaluations and not the problem parameters; in particular, the tuple $(A,B,Q,R)$that parametrizes the LQR Our observations consist of the noisy function evaluations $\PlainC_{{\sf init}, \gamma}(\K; s_0)$ or $\PlainC_{{\sf dyn}, \gamma}(\K; \mathcal{Z})$. We consider both the one-point and two-point settings in the former case. In the one-point setting for the randomly initialized model, a query of the function at the point $\K$ obtains the noisy function value $\PlainC_{{\sf init}, \gamma}(\K; s_0)$ for an initial state $s_0$ drawn at random from the distribution $\mathcal{D}_0$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Stochastic zero-order oracle in LQR", "weight": 1.0} -->

In the two-point setting, a query of the function at the points $(\K,\ensuremath{K'})$ obtains the pair of noisy function values $\PlainC_{{\sf init}, \gamma}(\K; s_0)$ and $\PlainC_{{\sf init}, \gamma}(\ensuremath{K'}; s_0)$ for an initial state $s_0$ drawn at random; this setting has an immediate operational interpretation as running two policies with the same random initialization. The one-point query model is defined analogously for the noisy dynamics cost $\PlainC_{{\sf dyn}, \gamma}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Stochastic zero-order oracle in LQR", "weight": 1.0} -->

A few points regarding our query model merit discussion. First, note that in the context of the control objective, each query produces a noisy sample of the long term trajectory cost, and so our sample complexity is measured in terms of the number of trajectories. Such an assumption is reasonable since the true" sample complexity that also takes into account the length of the trajectories is only larger by a small factorthe truncated, finite cost converges exponentially quickly to the infinite sum for stable To elaborate further on this point, note that the length of the rollout required to obtain a $\delta$-accurate cost evaluation for policy $K$ will depend on both $\delta$ as well as the eigen-structure of the matrix $A - BK$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Stochastic zero-order oracle in LQR", "weight": 1.0} -->

However, assuming that this matrix has maximum eigenvalue $\rho < 1$ (which is a common assumption in the related literature), the dependence on $\delta$ is quite mild: we only require a rollout of length $\order{\log (1 / \delta)}$, with the constant pre-factor depending on $\rho$ (or equivalently, on $\mathcal{C}(K_0)$. Since we are interested in obtaining $\epsilon$-approximations to the optimal policy, it suffices to obtain $\mathsf{poly}(\epsilon)$-approximate cost evaluations per trajectory to avoid a blow-up of the bias in our estimates (see, e.g.,), and this only adds another factor $\log (1 / \epsilon)$ to our sample complexity when measured in terms of the number of iterations. To avoid tracking these additional factors, we work with the offline setting defined above.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Stochastic zero-order oracle in LQR", "weight": 1.0} -->

The offline nature of the query model also assumed access to restarts of the system, which can be obtained in a simulation environment. Second, we note that while the one-point query model was studied by Fazel et al.[kakade18] for the random initialization modelalbeit with sub-optimal guaranteeswe also study a two-point query model, which is known to lead to faster convergence rates in zero-order stochastic optimization[duchi15].

<!-- chunk {"id": "body-0055", "role": "body", "section": "Stochastic zero-order oracle in LQR", "weight": 1.0} -->

Finally, note that our setting of the problem in which we are only given access to (noisy) evaluations of the cost of the policy and not to the state sequenceintentionally precludes the use of procedures that rely on observations of the state sequence. This setting allows us to distill the difficulties of truly `model-free' control, since it prevents any possibility of constructing a dynamics model from our observations; the latter is, loosely speaking, the guiding principle of model-based control. This is not to suggest that practical applications of learning-based LQR control take this form, but rather to provide a concrete framework within which model-based and model-free algorithms can be separated, by endowing them with distinct information oracles. In doing so, we hope to lay the broader foundations for studying derivative-free methods in the context of model-free reinforcement learning.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Main results", "weight": 1.0} -->

We now turn to a statement of our main result, which characterizes the convergence rate of a natural derivative-free algorithm for any (population) function that satisfies certain PL and smoothness properties. We thus obtain, as corollaries, rates of zero-order optimization algorithms when applied to the functions $\PlainC_{{\sf init}, \gamma}$ and $\PlainC_{{\sf dyn}, \gamma}$; these corollaries are collected in Section[sec:cons-lqr].

<!-- chunk {"id": "body-0057", "role": "body", "section": "Stochastic zero-order algorithm", "weight": 1.0} -->

We analyze a standard zero-order algorithm for stochastic [agarwal10,shamir17] in application to the LQR problem. We begin by introducing some notation required to describe this algorithm, operating in the general setting where we want to optimize a function $\ensuremath{f}: \mathcal{X} \mapsto \ensuremath{\mathbb{R}}$ of the form $\ensuremath{f}(x) = \mathbb{E}_{\xi \sim\mathcal{D}} [F(x; \xi)]$. Here we assume the inclusion $\mathcal{X} \subseteq \ensuremath{\mathbb{R}}^d$, and let $\mathcal{D}$denote a generic source of randomness in the zero-order function evaluation.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Stochastic zero-order algorithm", "weight": 1.0} -->

The zero-order algorithms that we study here use noisy function evaluations in order to construct near-unbiased estimates of the gradient. Let us now describe how such an estimate is constructed in the one-point and two-point settings. Let $\ensuremath{\mathbb{S}}^{\ensuremath{d} - 1} = \{u \in \ensuremath{\mathbb{R}}^d: \| u \|_2 = 1\}$ denote the $d$-dimensional unit shell. Let $\ensuremath{\operatorname{Unif}}(\ensuremath{\mathbb{S}}^{\ensuremath{d} - 1})$ denote the uniform distribution over the set $\ensuremath{\mathbb{S}}^{\ensuremath{d} - 1}$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Stochastic zero-order algorithm", "weight": 1.0} -->

For a given scalar $r > 0$ and a random direction $u \sim \ensuremath{\operatorname{Unif}}(\ensuremath{\mathbb{S}}^{\ensuremath{d} - 1})$ chosen independently of the random variable $\xi$, consider the one point gradient \frac{\ensuremath{d}}{r} \ensuremath{u}, and its two-point analogue r u, \xi) \big] \; \frac{\ensuremath{d}} Here $\xi$ should be viewed as an instantiation of the underlying random variable; in the two point setting, we compute a gradient estimate with the same instantiation of the noise used to evaluate $F$ at the points $x \pm r u$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Stochastic zero-order algorithm", "weight": 1.0} -->

In both the one-point and two-point cases, the resulting ratios are almost unbiased approximations of the secant ratio that defines the derivative at and these approximations get better and better as the smoothing radius $r$ gets smaller. On the other hand, small values of the radius $r$ may result in estimates with large variance. Our algorithms make use of such randomized approximations in a sequence of rounds by choosing appropriate values of the radius $r$; the general form of such an algorithm is stated below.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Stochastic zero-order algorithm", "weight": 1.0} -->

Stochastic Zero-Order Method Given iteration number $T \geq 1$, initial point $\x \in \mathcal{X}$, step size $\eta > 0$ and smoothing radius Sample $\xi_t \sim \mathcal{D}$ and $u_t \sim \mbox{Unif}(\ensuremath{\mathbb{S}}^{\ensuremath{d} - 1})$ operating in one-point setting} \\ \mathrm{g}\_r^2(\x[t], u\_t, \xi\_t) \; \text{ if operating in two-point $\x[t+1] \gets \x[t] - \eta \mathrm{g} (x_t)$ $\x[T]$

<!-- chunk {"id": "body-0062", "role": "body", "section": "Convergence guarantees", "weight": 1.0} -->

We now turn to analyzing Algorithm [sgd\_simple]in the settings of interest. In particular, our first (main) theorem is stated as a generic optimization result for non-convex functions which are (locally) smooth and satisfy the PL inequality, which we then specialize to various LQR settings.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Convergence guarantees", "weight": 1.0} -->

As mentioned before, the difficulty of optimizing the LQR cost functions is governed by multiple factors such as stability, non-convexity of the feasible set, and non-convexity of the objective. Furthermore, the Lipschitz gradient and Lipschitz properties for this cost function only hold locally with the radius of locality depending on the current iterate. Most crucially, the function is infinite outside of the region of stability, and so large steps can have disastrous consequences since we do not have access to a projection oracle that brings us back into the region of stability. It is thus essential to control the behavior of our stochastic, high variance algorithm over the entire course of optimization.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Convergence guarantees", "weight": 1.0} -->

Our strategy to overcome these challenges is to perform a careful martingale analysis, showing that the iterates remain bounded throughout the course of the algorithm; the rate depends, among other things, on the variance of the gradient estimates obtained over the course of the algorithm. By showing that the algorithm remains within the region of finite cost, we can also obtain good bounds on the local Lipschitz constants and gradient smoothness parameters, so that our step-size can be set accordingly.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Convergence guarantees", "weight": 1.0} -->

Let us now introduce some notation in order to make this intuition precise. We operate once again in the setting of general function optimization, i.e., we are interested in optimizing a function = \mathbb{E}\_{\xi} [\ensuremath{F}(\x; \xi)]$ obeying the (global) PL inequality with constant $\mu$, as well as certain local curvature Recall that we are given an initial point $\x$ with finite cost $\ensuremath{f}(\x)$; the global upper bound on the cost that we target in the analysis is set according to the cost $\ensuremath{f}(\x)$ of this initialization.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Convergence guarantees", "weight": 1.0} -->

Given the initial gap to optimality $\Delta\_0:\,= \ensuremath{f}(\x) - \ensuremath{f}(x^{*})$, we define the set \boundedset{0}:\,= \bigr \{ \x \mid \ensuremath{f}(\x) - \ensuremath{f}(x^{*}) \leq 10 corresponding to points $\x$ whose cost gap is at most ten times the initial cost gap $\diff{0}$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Convergence guarantees", "weight": 1.0} -->

Assume that the function $\ensuremath{f}$ is $(\ensuremath{\phi}_x, \radiusone{\x})$ locally smooth and $(\ensuremath{\lambda}_{\x}, \radiustwo{\x})$ locally Lipschitz at the point $\x$. Thus, both of these properties hold simultaneously within a neighborhood of radius $\rho_{\x} = \min\{ \radiusone{\x}, \radiustwo{\x} \}$ of the point $\x$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Convergence guarantees", "weight": 1.0} -->

Now define \globalSmooth{0}:\,= \sup_{\x \in \boundedset{0}} \ensuremath{\phi}_x, \qquad \ensuremath{\lambda}_{0}:\,= \sup_{\x \in \boundedset{0}} \ensuremath{\lambda}_{\x}, \quad \text{ and } \quad \rho_{0}:\,= \inf_{\x \in \boundedset{0}} By defining these quantities, we have effectively transformed the local properties of the function $\ensuremath{f}$ into global properties that hold over the bounded set $\boundedset{0}$.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Convergence guarantees", "weight": 1.0} -->

We also define a convenient functional of these curvature parameters $\ensuremath{\theta}_{0}:\,= \min \left\{ \frac{1}{2 \globalSmooth{0} }, \frac{\rho_{0}}{\ensuremath{\lambda}_{0}} \right\}$, which simplifies the statements of our results. Importantly, these smoothness properties only hold locally, and so we must also ensure that the steps taken by our algorithm are not too large. This is controlled by both the step-size as well as the norms of our gradient estimate $\mathrm{g}$ computed over the course of the algorithm.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Convergence guarantees", "weight": 1.0} -->

Note that these quantities also depend implicitly on the smoothing radius $r$ and on how the gradient estimate $\mathrm{g}$is With this set-up, we are now ready to state the main result regarding the convergence rate of Algorithm [sgd\_simple] on the functions of Note that here and throughout the rest of the paper, $C$ denotes some universal constant (which may change from line to line). For two sequences $g_n$ and $h_n$, we also use the standard notation $g_n \sim h_n$ and $g_n = \Theta(h_n)$ interchangeably, to mean that the sequences are within a (universal) constant multiplicative factor of each other.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Convergence guarantees", "weight": 1.0} -->

A few comments on Theorem[thm:mainthm] are in order. First, notice that the algorithm is guaranteed to return an $\epsilon$-accurate solution with constant probability $\frac{3}{4}$. This probability bound of $\frac{3}{4}$ in itself can be sharpened by a slightly more refined analysis with different constants. Additionally, by examining the proof, it can be seen that we establish a result (cf. Proposition[prop:thm] in Section[sec:proofs]) that is slightly stronger than Theorem[thm:mainthm], and then obtain the theorem from this more general result. The proof of the theorem itself is relatively short, and makes use of a carefully constructed martingale along with an appropriately defined stopping time. As mentioned before, the main challenge in the proof is to ensure that we have bounded iterates while still preserving the strong convergence properties of zero-order stochastic methods for smooth functions that satisfy the PL property.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Convergence guarantees", "weight": 1.0} -->

It should be noted that Theorem [thm:mainthm] is a general guarantee: it characterizes the zero-order complexity of optimizing locally smooth functions that satisfy a PL inequality in terms of properties of the gradient estimates obtained over the course of the algorithm. In particular, two properties of these estimates appear: the variance of the estimate, as well as a uniform bound on its size. These quantities, in turn, depend on both the noise in the zero-order evaluations as well as our choice of query model. In the next section, we specialize Theorem[thm:mainthm]so as to derive particular consequences for the LQR models introduced above.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

[thm:mainthm] yields immediate consequences for LQR optimization in various settings, and the dependence of the optimization rates on the tolerance $\epsilon$ is summarized by Table[tab:lqr]. We state and discuss precise versions of these | 2-5 1r|Parameter settings | 2*c]@c@Smoothing radius $r$ | 2*c]@c@Variance $\ensuremath{G}_2$ | 2*c]@c@Step-size $\eta$ | 2*c]@c@ #queries $T$ | Derivative-free complexity of LQR optimization under the two query models, as a function of the final error tolerance $\epsilon$. The multiplicative pre-factors are functions of the effective dimension $\ensuremath{D}$ and curvature parameters, and differ in the three cases; see the statements of the corollaries below.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

First, let us consider the random initialization model. From the various lemmas in Section [sec:lqrprop], we know that the population objective $\PlainC_{{\sf init}, \gamma}(\K)$ is locally $(\smoothnessK{\K}, \radiusone{\K})$ smooth and $(\lipconK{\K}, \radiustwo{\K})$ Lipschitz, and also globally $\ensuremath{\mu_{{\sf lqr}}}$-PL. By assumption, we are given a starting point $\K$ having finite population cost $\PlainC_{{\sf init}, \gamma}(\K)$.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

Proceeding as in the previous section, we may thus define the set \boundedset{\ensuremath{{\sf lqr}}}:\,= \braces{ \K \mid \PlainC_{{\sf init}, \gamma}(\K) - \PlainC_{{\sf init}, \gamma}(K^*) corresponding to point $\x$ whose cost gap is at most ten times the initial cost gap to optimality $\diff{0} = \PlainC_{{\sf init}, \gamma}(\K) - \PlainC_{{\sf init}, \gamma}(K^*)$.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

Let us make a brief comment on the finiteness of these quantities in the absence of compactness. The quantity $\phi_{\ensuremath{{\sf lqr}}}$ is finite, simply by definition of the set $\boundedset{\ensuremath{{\sf lqr}}}$. In the sequel, we show that for any $K \in \boundedset{\ensuremath{{\sf lqr}}}$, $\phi_K$ can be bounded by a polynomial of $10 \Delta_0$. Hence, $\phi_\ensuremath{{\sf lqr}}$ can also be bounded by a polynomial of $10 \Delta_0$, implying it is finite. A similar argument shows that $\lambda_\ensuremath{{\sf lqr}}$ is finite and $\rho_\ensuremath{{\sf lqr}}>0$.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

With this setup, we now establish the following corollaries for derivative-free policy optimization for linear quadratic systems.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

If the initial state distribution $\mathcal{D}_0$ is also Gaussian, the $C_{\statedim}^2$ term in the step-size bound above can be AP This case is interesting, but the Gaussian distribution doesn't satisfy the uniform boundedness condition required to bound $\ensuremath{G}_{\infty}$. Should probably leave it out.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

Let us parse this result briefly. Treating the other parameters as constants, note that it is valid to choose the above result then shows that with a choice of step-size $\eta \sim \epsilon^2$, the canonical zero-order algorithm converges using $T \sim \eta^{-1} \log (1 / \epsilon) = \ordertil{\epsilon^{-2}}$steps. This is in spite of the high-variance estimates obtained by the algorithm, and the theorem also guarantees stability of all the iterates with constant probability.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

Interestingly, the result above (or more generally, Theorem [thm:mainthm]) also yields an $\ordertil{\epsilon^{-2}}$ convergence rate for the family of high-variance minibatch derivative-free algorithms, where $k$ zero-order samples are used to estimate the gradient at any point, thereby reducing its variance. The canonical algorithm corresponds to the case $k = 1$, while that of Fazel et al. corresponds to the case of In particular, choosing a minibatch of size $k$ results in the variance of the gradient $G_2$ being reduced by a factor $k$, allowing us to increase our step-size proportionally and converge in $1/k$-fraction of the number of iterations (but with the same number of zero-order evaluations in total).

<!-- chunk {"id": "body-0081", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

For completeness, we provide an analysis tailored to the algorithm of Fazel et al.[kakade18] in Appendix[app:fazel], which shows that our techniques can be used to sharpen their rates to guarantee $\epsilon$-approximate policy optimization with $\ordertil{\epsilon^{-2}}$zero-order Let us also briefly discuss the upper bounds on the step-size that are required for the corollary to hold. As stated, the step-size is required to satisfy the bound $\eta \leq \frac{r \rho_{\ensuremath{{\sf lqr}}}}{10 \PlainC_{{\sf init}, \gamma}(\K)}$, but this condition is an artifact of the analysis and can be removed (see Appendix[app:fazel]). In addition, the step-size is also required to be bounded by the curvature properties of the function. Operationally speaking, this means that for larger step-sizes, we are unable to guarantee stability of the policies obtained over the course of the algorithm.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

Such a bottleneck is in fact also observed in practice, as shown in Figure[fig:plt\_minibatch] for both the one-point and two-point settings.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

We now turn to the two-point setting, in which we obtain two noisy evaluations per query.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

Then for any error tolerance $\epsilon$ such that $\epsilon \log (120 \Delta_0 / \epsilon) < \frac{10}{3} \Delta_0$, running Algorithm[sgd\_simple] for $\ensuremath{T} = \frac{4}{\eta \ensuremath{\mu}} \log\left(\frac{ 120 \diff{0}}{\epsilon} \right)$ iterations yields an iterate $\K[\ensuremath{T}]$ such that \PlainC_{{\sf init}, \gamma}(\K[\ensuremath{T}]) - \PlainC_{{\sf init}, \gamma}(K^*) \leq \epsilon with probability greater than $3/4$.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

As known from the literature on zero-order optimization in convex settings[duchi15, shamir17], the two-point query model allows us to substantially reduce the variance of our gradient estimate, thus ensuring much faster convergence than with one-point evaluations. The most salient difference is the fact that we now converge with $\ordertil{1/\epsilon}$ iterations as opposed to the $\ordertil{1/\epsilon^2}$ iterations required in Corollary[cor:init1]. This gap between the two settings is substantial and merits further investigation, but in general, it is clear that two-point evaluations should certainly be used if available. This gap, and other differences, are discussed shortly.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

Let us now turn to establishing convergence results for the noisy dynamics model in the one-point setting. Note that [lem:noisy-random] provides a way to directly relate the population costs of the random initialization and noisy dynamics models; furthermore, the set $\boundedset{\ensuremath{{\sf lqr}}}$ is exactly the same. In addition, since we look at a discounted cost $\PlainC_{{\sf dyn}, \gamma}$ in this setting, the corresponding curvature parameters have an inherent dependence on $\gamma$ which we denote using corresponding subscripts. With an additional computation of the variance and norm of the gradient estimates, we then obtain the following corollary for one-point optimization of the noisy dynamics model.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

AP modify above bound with correct noise variance, and by introducing factors of $\gamma$ as necessary.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

If the noise distribution $\mathcal{D}_{{\sf add}}$ is also Gaussian, we may instead use the bound \ensuremath{G}_{2, \ensuremath{{\sf lqr}}} \leq \frac{D^2}{r^2} \cdot \left(20 \PlainC_{{\sf dyn}, \gamma} AP Similarly to above, this case is interesting, but the Gaussian distribution doesn't satisfy the uniform boundedness condition required to bound $\ensuremath{G}_{\infty}$. Should probably Thus, we have shown that the one-point settings for both the random initialization and noisy dynamics models exhibit similar behaviors in the different parameters. Reasoning heuristically, such a behavior is due to the fact that the additional additive noise in the dynamics is quickly damped away by the discount factor, so that the cost is dominated by the noise in the initial iterates. The variance bound, however, is substantially different, and this leads to the differing dependence on the smoothness parameters and dimension of the problem.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

Another interesting problem studied in the noisy dynamics model is one of bounding the regret of online procedures. Equipped with a high probability bound on convergence as opposed to the constant probability bound currently posited by Corollary[cor:noisydyn]the offline guarantee and associated algorithm can in principle be turned into a no-regret learner in the online setting. We leave this extension to future work.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

Let us now briefly discuss the dependence of the various bounds on the different parameters of the LQR objective, in the various cases above.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

| [xlabel=$\epsilon^{-1}$, ylabel=Zero Order Complexity, label style=font=, legend style=legend pos=north west,font=, log base y=10, log base x=10, ymin=20, ymax=10000000, xmajorgrids=true, ymajorgrids=true, grid style=dashed, style=thick, max space between ticks=30] [color = blue, dotted, forget plot] coordinates (1, 660.185269305) (10^2, 706742.1451); [color=blue, smooth, only marks=True, mark=*,] coordinates (1.93069773, 1742) (3.72759372, 4298) (7.19685673, 10684) (13.89495494, 22411) (26.82695795, 99713) (51.79474679, 254031); $\C{K_0} = \C{K^*} + 3$ |

<!-- chunk {"id": "body-0092", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

plot] coordinates (1, 489.554518103) (10^2, 7639307.60407); [color=blue, smooth, only marks=True, mark=*,] coordinates (3.72759372, 6478) (7.19685673, 26831) (13.89495494, 115073) (26.82695795, 569382) (51.79474679, 2441412); $\C{K_0} = \C{K^*} + 3$ | Number of samples required to reach an error tolerance of $\epsilon$, plotted against $1/\epsilon$, for (a) Randomly initialized LQR with one-point evaluations (b) Randomly initialized LQR with two-point evaluations for differing values of the initial cost, and (c) Noisy dynamics LQR model with one-point evaluations.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

We use $\mathcal{C}$ to denote the population cost in the various cases, and the plots were obtained by averaging $20$ runs of Algorithmsgd\_simple. Each dotted line represents the line of best fit for the corresponding data points. For more problem details, see Appendixsec:additional\_exp.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

Dependence on $\epsilon$: Our bounds illustrate two distinct dependences on the tolerance parameter $\epsilon$. In particular, the zero-order complexity scales proportional to $\epsilon^{-2}$ for both one-point settings (Corollaries[cor:init1] and[cor:noisydyn]), but proportional to $\epsilon^{-1}$ in the two-point setting (Corollary[cor:init2]). As alluded to before, this distinction arises due to the lower variance of the gradient estimator in the two-point setting. Lemma[lem:lipschitz\_cost\_lqr] establishes the Lipschitz property of the LQR cost function for each instantiation of the noise variable $s_0$, which ensures that the Lipschitz constant of our sample cost function is also bounded; therefore, the noise of the problem reduces as we approach the optimum solution.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

In contrast, the optimization problem with one-point evaluations becomes more difficult the closer we are to the optimum solution, since the noise remains constant, while the signal" in the problem (measured by the rate of decrease of the population cost function) reduces as we approach the optimum. The $O(1/ \epsilon^2)$ dependence in the one-point settings is reminiscent of the complexity required to optimize strongly convex and smooth functions[agarwal10, shamir12], and it would be interesting if a matching lower bound could also be proved in this LQR setting Note that this lower bound follows immediately for the class of PL and smooth. Even in the absence of such a lower bound, the one-point setting is strictly worse than the two-point setting even with respect to the other parameters of the problem, which we discuss next. Figure[fig:plt\_eps] shows the convergence rate of the algorithm in all three settings as a function of $\epsilon$, where we confirm that scalings in practice corroborate our theory quite accurately.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

It is also worth noting that model-based algorithms for this problem require $\order{\epsilon^{-1}}$ trajectory samples to return an $\epsilon$-approximate policy in the noisy dynamics setting (see, e.g.[dean17]). Thus, while a one-point zero-order method is outperformed by these algorithmsnote that the comparison is not quite fair, since zero-order algorithms only require access to noise cost evaluations and not the state sequencea two-point variant is similar to model-based methods in its dependence Note that the comparison is inherently imprecise, since we are comparing upper bounds to upper bounds. In practice, one would certainly prefer the use of a model-based method when provided access to the state sequence.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

Dependence on dimension: The dependence on dimension enters once again via our bound on the variance of the gradient estimate, as is typical of many derivative-free procedures[duchi15, shamir17]. The two-point setting gives rise to the best dimension dependence (linear in $\ensuremath{D}$), and the reason is similar to why this occurs for convex optimization[shamir17]. It is particularly interesting to compare the dimension dependence to results in model-based control. There, in the noisy dynamics model, the sample complexity scales with the sum of state and control dimensions $m + k$, whereas the dependence in the two-point setting is on their product $\ensuremath{D} = m \cdot k$. However, each observation in that setting consists of a state vector of length $m$, while here we only get access to scalar cost values, and so in that loose sense, the complexities of the two settings are In the one-point setting, the dependence on dimension is significantly poorer, and at least quadratic.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

This of course ignores other dimension-dependent factors such as the curvature parameters $(\ensuremath{\phi}_{\ensuremath{{\sf lqr}}}, \ensuremath{\lambda}_{\ensuremath{{\sf lqr}}}, \mu)$(see the discussion below).

<!-- chunk {"id": "body-0099", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

| [xlabel=$\C{K_0}$, ylabel=Zero Order Complexity, label style=font=, legend style=legend pos=south east,font=, log base y=10, log base x=10, ymin=500, xmax = 1000, xmajorgrids=true, ymajorgrids=true, grid style=dashed, style=thick, max space between ticks=30] [color = blue, dotted, forget plot] coordinates (8, 1189.46848832) (512, 4931430.23943); [color=blue, smooth, only marks=True, mark=*,] coordinates (8, 641*2) (32, 9596*2) (64, 28020*2) (128, 286034*2) (256, 619056*2) (512, 1940659*2); $\epsilon = 0.1$ | [xlabel=$\C{K_0}$, ylabel=Zero Order Complexity, label style=font=, legend style=legend pos=south

<!-- chunk {"id": "body-0100", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

east,font=, log base y=10, log base x=10, ymin=200, xmax = 1000, xmajorgrids=true, ymajorgrids=true, grid style=dashed, style=thick, max space between ticks=30] [color = blue, dotted, forget plot] coordinates (4, 395.588600654) (512, 164551.927279); [color=blue, smooth, only marks=True, mark=*,] coordinates; $\epsilon = 1$ | Number of samples required to reach a fixed error tolerance of $\ensuremath{\epsilon}$, plotted against the cost of the initialization $K_0$, for (a) Randomly initialized LQR with two-point evaluations (b) Noisy dynamics LQR with one-point evaluations.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

The plots were obtained by averaging 20 runs of Algorithmsgd\_simple. Each dotted line represents the line of best fit for the corresponding data points. For more problem details, see Appendixsec:additional\_exp.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Consequences for LQR optimization", "weight": 1.0} -->

Dependence on curvature parameters: The iteration complexity scales linearly in the smoothness parameter of the problem $\ensuremath{\phi}_{\ensuremath{{\sf lqr}}}$, and quadratically in the other curvature parameters. See Appendix[sec:polynomials\_bounded] for precise definitions of these parameters for the LQR problem. In particular, it is worth noting that our tightest bounds for these quantities depend on the dimension of the problem implicitly for some LQR instances, and are actually lower-order polynomials of the initial cost. In practice, however, it is likely that much sharper bounds can be proved on these parameters, e.g., in simulation (see Figure[fig:plt\_init]), the dependence of the sample complexity on the initial cost is in fact relatively weakof the order $\mathcal{C}(\K)^2$and our bounds are clearly not sharp in that sense.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Proofs of main results", "weight": 1.0} -->

In this section, we provide proofs of Theorem [thm:mainthm], and Corollaries[cor:init1],[cor:init2], and[cor:noisydyn]. The proofs of the corollaries require many technical lemmas, whose proofs we postpone to the appendix.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this paper, we studied the model-free control problem over linear policies through the lens of derivative-free optimization. We derived quantitative convergence rates for various zero-order methods when applied to learn optimal policies based on data from noisy linear systems with quadratic costs. In particular, we showed that one-point and two-point variants of a canonical derivative-free optimization method achieve fast rates of convergence for the non-convex LQR problem. Notably, our proof deals directly with some additional difficulties that are specific to this problem and do not arise in the analysis of typical optimization algorithms. More precisely, our proof involves careful control of both the (potentially) unbounded nature of the cost function, and the non-convexity of the underlying domain. Interestingly, our proof only relies on certain local properties of the function that can be guaranteed over a bounded set; for this reason, the optimization-theoretic result in this paper [thm:mainthm]) is more broadly applicable beyond the RL setting.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Discussion", "weight": 1.5} -->

While this paper analyzes a canonical zero-order optimization algorithm for model-free control of linear quadratic systems, many open questions remain. One such question concerns lower bounds for LQR problems in the model-free setting, thereby showing quantitative gaps between such a setting and that of model-based control. While we conjecture that the convergence bounds of [cor:init1],[cor:init2], and[cor:noisydyn] are sharp in terms of their dependence on the error tolerance $\epsilon$, establishing this rigorously will require ideas from the extensive literature on lower bounds in zero-order optimization[shamir12]. Another important direction is establish the sharpness (or otherwise) of our bounds in terms of the dimension of the problem, as well as to obtain tight characterizations of the local curvature parameters of the problem around a particular policy $\K$ in terms of the cost at $\K$.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Discussion", "weight": 1.5} -->

We also mention that our sharp characterizations of the cost function are likely to be useful in sharpening analyses Here again, the techniques of Fazel et al. yield a bound of the order $\ordertil{\epsilon^{-4}}$, but we conjecture that this bound should be improvable at least to $\ordertil{\epsilon^{-2}}$. of the natural gradient algorithm[kakade18]as well as in analyzing the popular REINFORCE algorithm as applied to the LQR problem. We leave these interesting questions In the broader context of model-free reinforcement learning as well, there are many open questions. First, a derivative-free algorithm over linear policies is reasonable even in other systems; can we establish provable guarantees over larger classes of problems? Second, there is no need to restrict ourselves to linear policies; in practical RL systems, derivative-free algorithms are run for policies that parametrized in a much more complex fashion. How does the sample complexity of the problem change with the class of policies over which
