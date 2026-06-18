<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Robust Exploration in Linear Quadratic Reinforcement Learning

Topics include Convex optimization, Reinforcement learning, Robustness, Uncertainty, Optimization, Control, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper concerns the problem of learning control policies for an unknown linear dynamical system to minimize a quadratic cost function. We present a method, based on convex optimization, that accomplishes this task robustly: i.e., we minimize the worst-case cost, accounting for system uncertainty given the observed data. The method balances exploitation and exploration, exciting the system in such a way so as to reduce uncertainty in the model parameters to which the worst-case cost is most sensitive. Numerical simulations and application to a hardware-in-the-loop servo-mechanism demonstrate the approach, with appreciable performance and robustness gains over alternative methods observed in both.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Learning to make decisions in an uncertain and dynamic environment is a task of fundamental importance in a number of domains. Though it has been the subject of intense research activity since the formulation of the 'dual control problem' in the 1960s, the recent success of reinforcement learning (RL), particularly in games, has inspired a resurgence in interest in the topic. Problems of this nature require decisions to be made with respect to two objectives. First, there is a goal to be achieved, typically quantified as a reward function to be maximized. Second, due to the inherent uncertainty there is a need to gather information about the environment, often referred to as 'learning' via 'exploration'. These two objectives are often competing, a fact known as the exploration/exploitation trade-off in RL, and the 'dual effect' (of decision) in control.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

It is important to recognize that the second objective (exploration) is important only in so far as it facilitates the first (maximizing reward); there is no intrinsic value in reducing uncertainty. As a consequence, exploration should be targeted or application specific; it should *not* excite the system arbitrarily, but rather in such a way that the information gathered is useful for achieving the goal. Furthermore, in many real-world applications, it is essential that exploration does not compromise the safe and reliable operation of the system.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper is concerned with control of uncertain linear dynamical systems, with the goal of maximizing (minimizing) rewards (costs) that are a quadratic function of states and actions; cf. §2 for a detailed problem formulation. We derive methods to synthesize control policies that balance the exploration/exploitation tradeoff by performing robust, targeted exploration: *robust* in the sense that we optimize for worst-case performance given uncertainty in our knowledge of the system, and *targeted* in the sense that the policy excites the system so as to reduce uncertainty in such a way that specifically minimizes the worst-case cost. To this end, this paper makes the following specific contributions. We derive a high-probability bound on the spectral norm of the system parameter estimation error, in a form that is applicable to both robust control synthesis and design of targeted exploration; cf. §3. We also derive a convex approximation of the worst-case (w.r.t.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

parameter uncertainty) infinite-horizon linear quadratic regulator (LQR) problem; cf. §4.2. We then combine these two developments to present an approximate solution, via convex semidefinite programing (SDP), to the problem of minimizing the worst-case quadratic costs for an uncertain linear dynamical system; cf. §4. For brevity, we will refer to this as a 'robust reinforcement learning' (RRL) problem.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Problem statement", "weight": 1.0} -->

In this section we describe in detail the problem addressed in this paper. Notation is as follows: $A^{\top}$ denotes the transpose of a matrix $A$. $x_{1:n}$ is shorthand for the sequence ${\{ x_{t}\}}_{t = 1}^{n}$. $\lambda_{\text{max}}{(A)}$ denotes the maximum eigenvalue of a matrix $A$. $\otimes$ denotes the Kronecker product. $\text{vec}(A)$ stacks the columns of $A$ to form a vector. ${\mathbb{S}}_{+}^{n}$ (${\mathbb{S}}_{+ +}^{n}$) denotes the cone(s) of $n \times n$ symmetric positive semidefinite (definite) matrices. w.p.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Problem statement", "weight": 1.0} -->

means 'with probability.' $\chi_{n}^{2}{(p)}$ denotes the value of the Chi-squared distribution with $n$ degrees of freedom and probability $p$. blkdiag is the block diagonal operator.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Dynamics and cost function", "weight": 1.0} -->

We are concerned with control of linear time-invariant systems

<!-- chunk {"id": "body-0010", "role": "body", "section": "Modeling and data", "weight": 1.0} -->

As $\{ A_{\text{tr}},B_{\text{tr}}\}$ are unknown, all knowledge about the true system dynamics must be inferred from observed data, $\mathcal{D}_{n}:={\{ x_{t},u_{t}\}}_{t = 1}^{n}$. We assume that $\sigma_{w}$ is known, or has been estimated, and that we have access to initial data, denoted (with slight notational abuse) $\mathcal{D}_{0}$, obtained, e.g. during a preliminary experiment.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Worst-case dynamics", "weight": 1.0} -->

We are now in a position to define the optimization problem that we wish to solve in this paper. In the absence of knowledge of the true dynamics, $\{ A_{\text{tr}},B_{\text{tr}}\}$, given initial data $\mathcal{D}_{0}$, we wish to find a sequence of policies ${\{\mathcal{K}_{i}\}}_{i = 0}^{N}$ that minimize the expected cost $\sum_{t = 1}^{T}{c{(x_{t},u_{t})}}$, assuming that, at time $t$, the system evolves according to the *worst-case* dynamics within the high-probability credibility region $\Theta_{e}{(\mathcal{D}_{t})}$, i.e.,

<!-- chunk {"id": "body-0012", "role": "body", "section": "Worst-case dynamics", "weight": 1.0} -->

where the expectation is w.r.t. $w_{t} \sim {\mathcal{N}\left( 0,{\sigma_{w}^{2}I_{n_{x}}} \right)}$ and $e_{t} \sim {\mathcal{N}\left( 0,I_{n_{u}} \right)}$. We choose to optimize for the worst-case dynamics so as to bound, with high probability, the cost of applying the policies to the unknown true system. In principle, problems such as can be solved via *dynamic programing* (DP). However, such DP-based solutions require gridding to obtain finite state-action spaces, and are hence computationally intractable for systems of even modest dimension. In what follows, we will present an approximate solution to this problem, which we refer to as a 'robust reinforcement learning' (RRL) problem, that retains the continuous sate-action space formulation and is based on convex optimization. To facilitate such a solution, we require a refined means of quantifying system uncertainty, which we present next.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Modeling uncertainty for robust control", "weight": 1.0} -->

In this paper, we adopt a model-based approach to control, in which quantifying uncertainty in the estimates of the system dynamics is of central importance. From Proposition 2.1 the posterior distribution over parameters is Gaussian, which allows us to construct an 'ellipsoidal' credibility region $\Theta_{e}$, centered about the ordinary least squares estimates of the model parameters, as.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Modeling uncertainty for robust control", "weight": 1.0} -->

To allow for an exact convex formulation of the control problem involving the *worst-case* dynamics, cf. §4.2, it is desirable to work with a credibility region that bounds uncertainty in terms of the spectral properties of the parameter error *matrix* $\lbrack{\hat{A} - A_{\text{tr}}},{\hat{B} - B_{\text{tr}}}\rbrack$, where $\{\hat{A},\hat{B}\}$ are the ordinary least squares estimates, i.e. ${\text{vec}\left( {\lbrack{\hat{A}\hat{B}}\rbrack} \right)} = \mu_{\theta}$, cf. Proposition 2.1. To this end, we will work with models of the form ${\mathcal{M}{(\mathcal{D})}}:={\{\hat{A},\hat{B},D\}}$ where $D \in {\mathbb{S}}^{n_{x}

<!-- chunk {"id": "body-0015", "role": "body", "section": "Convex approximation to robust reinforcement learning problem", "weight": 1.0} -->

Equipped with the high-probability bound on the spectral properties of the parameter estimation error presented in Lemma 3.1, we now proceed with the main contribution of this paper: a convex approximation to the 'robust reinforcement learning' (RRL) problem.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Steady-state approximation of cost", "weight": 1.0} -->

In pursuit of a more tractable formulation, we first introduce the following approximation of,

<!-- chunk {"id": "body-0017", "role": "body", "section": "Steady-state approximation of cost", "weight": 1.0} -->

Observe that has introduced two approximations to. First, in we only update the 'worst-case' model at the beginning of each epoch, when we deploy a new policy, rather than at each time step as. This introduces some conservatism, as model uncertainty will generally decrease as more data is collected, but results in a simpler control synthesis problem. Second, we select the worst-case model from the 'spectral' credibility region $\Theta_{m}$ as defined, rather than the 'ellipsoidal' region $\Theta_{e}$ defined. Again, this introduces some conservatism as $\Theta_{e} \subseteq \Theta_{m}$, cf. §A.1.2, but permits convex optimization of the worst-case cost, cf. §4.2. For convenience, we denote

<!-- chunk {"id": "body-0018", "role": "body", "section": "Steady-state approximation of cost", "weight": 1.0} -->

Next, we approximate the cost between epochs with the infinite-horizon cost, scaled appropriately for the epoch duration, i.e., between the $i - 1$th and $i$th epoch we approximate the cost as

<!-- chunk {"id": "body-0019", "role": "body", "section": "Steady-state approximation of cost", "weight": 1.0} -->

This approximation is accurate when the epoch duration $T_{i}$ is sufficiently long relative to the time required for the state to reach the stationary distribution. Substituting into, the cost function that we seek to minimize becomes

<!-- chunk {"id": "body-0020", "role": "body", "section": "Steady-state approximation of cost", "weight": 1.0} -->

The expectation in is w.r.t. to $w_{t}$ and $e_{t}$, as $\mathcal{D}_{t_{i}}$ depends on the random variables $x_{1:t_{i}}$ and $u_{1:t_{i}}$, which evolve according to the worst-case dynamics.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Optimization of worst-case cost", "weight": 1.0} -->

The previous subsection introduced an approximation of our 'ideal' problem, based on the worst-case infinite horizon cost, cf.. In this subsection we present a convex approach to the optimization of $J_{\infty}{(\mathcal{K},{\Theta_{m}{(\mathcal{M})}})}$ w.r.t. $\mathcal{K}$, given $\mathcal{M}$. The infinite horizon cost can be expressed as

<!-- chunk {"id": "body-0022", "role": "body", "section": "Optimization of worst-case cost", "weight": 1.0} -->

Under the feedback policy $\mathcal{K}$, the covariance appearing on the RHS of can be expressed as

<!-- chunk {"id": "body-0023", "role": "body", "section": "Optimization of worst-case cost", "weight": 1.0} -->

where $W = {{\mathbb{E}}\left\lbrack {x_{t}x_{t}^{\top}} \right\rbrack}$ denotes the stationary state covariance. For known $A$ and $B$, $W$ is given by the (minimum trace) solution to the Lyapunov inequality

<!-- chunk {"id": "body-0024", "role": "body", "section": "Optimization of worst-case cost", "weight": 1.0} -->

i.e., $\arg{\min_{W}{\text{tr}W\text{s.t.}}}$. To optimize $J_{\infty}{(\mathcal{K},{\Theta_{m}{(\mathcal{M})}})}$ via convex optimization, there are two challenges to overcome: i. non-convexity of jointly searching for $K$ and $W$, satisfying and minimizing, ii. computing $W$ for worst-case ${\{ A,B\}} \in {\Theta_{m}{(\mathcal{M})}}$, rather than known $\{ A,B\}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Optimization of worst-case cost", "weight": 1.0} -->

Let us begin with the first challenge: nonconvexity. To facilitate a convex formulation of the RRL problem we write as

<!-- chunk {"id": "body-0026", "role": "body", "section": "Optimization of worst-case cost", "weight": 1.0} -->

and introduce the change of variables $Z = {WK^{\top}}$ and $Y = {{KWK^{\top}} + \Sigma}$, collated in the variable ${\Xi = \begin{bmatrix}
\end{bmatrix}}.$ With this change of variables, minimizing subject to is a convex program.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Optimization of worst-case cost", "weight": 1.0} -->

Now, we turn to the second challenge: computation of the stationary state covariance under the worst-case dynamics. As a sufficient condition, we require to hold for all ${\{ A,B\}} \in {\Theta_{m}{(\mathcal{M})}}$. In particular, we define the following approximation of $J_{\infty}{(\mathcal{K},\mathcal{M})}$

<!-- chunk {"id": "body-0028", "role": "body", "section": "Approximate uncertainty propagation", "weight": 1.0} -->

This approximation makes use of the same calculation appearing. The equality makes use of the change of variables introduced in §4.2. Note that in proof of Theorem 4.2, cf. §A.1.4, it was shown that $\Xi = \begin{bmatrix}
{K^{\top}W} & {{KWK^{\top}} + \Sigma}
\end{bmatrix}$, when $\Xi$ is the solution of.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Final convex program and receding horizon application", "weight": 1.0} -->

Hitherto, we have considered the problem of minimizing the expected cost over time horizon $T$ given initial data $\mathcal{D}_{0}$. In practical applications, we employ a *receding horizon* strategy, i.e., at the $i$th epoch, given data $\mathcal{D}_{t_{i - 1}}$, we find a sequence of policies ${\{\mathcal{K}_{j}\}}_{j = i}^{i + h}$ that minimize the approximate $h$-step-ahead expected cost

<!-- chunk {"id": "body-0030", "role": "body", "section": "Selecting multipliers", "weight": 1.0} -->

For optimization of ${\overset{\sim}{J}}_{\infty}{(\mathcal{K},\mathcal{M})}$ given a model $\mathcal{M}$, i.e. the simultaneous search for the policy $\mathcal{K}$ and multiplier $\lambda$ is convex, as $D$ is fixed. However, in the RRL setting, '$D$' is a function of the decision variables $\Xi_{i}$, cf. (40b), and so the multipliers ${\{\lambda_{j}\}}_{j = {i + 1}}^{i + h} \in_{+}^{h - 1}$ must be specified in advance.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Selecting multipliers", "weight": 1.0} -->

Then, compute the cost $\hat{J}{(i,h,{\{\overline{\mathcal{K}}\}}_{j = i}^{i + h},\mathcal{D}_{t_{i - 1}})}$ by solving, but with the policies fixed to $\overline{\mathcal{K}}$, and the multipliers ${\{\lambda_{j}\}}_{j = i}^{i + h} \in_{+}^{h}$ as free decision variables. In other words, approximate the worst-case cost of deploying the $\overline{\mathcal{K}}$, $h$ epochs into the future. Then, use the multipliers found during the calculation of this cost for control policy synthesis at the $i$th epoch.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Computational complexity", "weight": 1.0} -->

The proposed method can be implemented via semidefinite programing (SDP) for which computational complexity is well-understood. In particular, the cost of solving the SDP scales as $\mathcal{O}{({\max{\{ m^{3},{mn^{3}},{m^{2}n^{2}}\}}})}$, where $m = {{{({1/2})}n_{x}{({n_{x} + 1})}} + {{({1/2})}n_{u}{({n_{u} + 1})}} + {n_{x}n_{u}} + 1}$ denotes the dimensionality of the decision variables, and $n = {{3n_{x}} + n_{u}}$ is the dimensionality of the LMI $S \succeq 0$. The cost of solving the SDP is then given, approximately, by the cost of multiplied by the horizon $h$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Computational complexity", "weight": 1.0} -->

1:Input: initial data 𝒟0, confidence δ, LQR cost matrices Q and R, epochs {ti}i = 1N.
3: Compute/update nominal model ℳ (𝒟ti − 1).
4: Solve convex program.
5: Recover policy 𝒦i: Ki = Zi⊤ Wi−1 and Σi = Yi − Zi⊤ Wi−1 Zi.
6: Apply policy to true system for ti − 1 &lt; t ≤ ti, which evolves according to with ut = Ki xt + Σi1/2 et.
7: Form 𝒟ti = 𝒟ti − 1 ∪ {xti − 1: ti, uti − 1: ti} based on newly observed data.
Algorithm 1 Receding horizon application to true system

<!-- chunk {"id": "body-0034", "role": "body", "section": "Numerical simulations", "weight": 1.0} -->

In this section, we consider the RRL problem with parameters

<!-- chunk {"id": "body-0035", "role": "body", "section": "Numerical simulations", "weight": 1.0} -->

We partition the time horizon $T = 10^{3}$ into $N = 10$ equally spaced intervals, each of length $T_{i} = 100$. For robustness, we set $\delta = 0.05$. Each experimental trial consists of the following procedure. Initial data $\mathcal{D}_{0}$ is obtained by driving the system forward 6 time steps, excited by ${\overset{\sim}{u}}_{t} \sim {\mathcal{N}(0,I)}$. This open-loop experiment is repeated 500 times, such that $\mathcal{D}_{0} = {\{{\overset{\sim}{x}}_{1:6}^{i},{\overset{\sim}{u}}_{1:6}\}}_{i = 1}^{500}$. We then apply three methods: i. rrl - the method proposed in §4.4, with look-ahead horizon $h = 10$; ii.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Numerical simulations", "weight": 1.0} -->

nom - applying the 'nominal' robust policy $\mathcal{K}_{i} = {{\arg{\min_{\mathcal{K}}{\overset{\sim}{J}}_{\infty}}}{(\mathcal{K},{\Theta_{m}{({\mathcal{M}{(\mathcal{D}_{t_{i}})}})}})}}$, i.e., a pure greedy exploitation policy, with no explicit exploration; iii. greedy - first obtaining a nominal robustly stabilizing policy as with nom, but then optimizing (i.e., increasing, if possible) the exploration variance $\Sigma$ until the greedy policy and the rrl policy have the same theoretical worst-case cost at the current epoch. This is a greedy exploration policy. We perform 100 of these trials and plot the results in Figure 2. In Figure 2(a) we plot the total costs (i.e. the sum of the costs for each epoch over the entire time horizon).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Numerical simulations", "weight": 1.0} -->

In each setting (see caption for details), rrl attains lower total cost than the other methods. In Figure 2(c) we plot the costs at each epoch; as may be expected, nom (which does no explicit exploration) often attains lower cost than rrl at the initial epochs, rrl, which does exploration, achieves lower cost in the end. We emphasize that this balance of exploration/exploitation occurs *automatically*. rrl always outperforms greedy. In Figure 2(c) we also plot the *information*, defined as ${1/\lambda_{\text{max}}}{(D_{i}^{- 1})}$, at the $i$th epoch, which is the (inverse) of the 2-norm of parameter error, cf.. The larger the information, the more certain the system (in an absolute sense). Observe that rrl achieves larger information than nom (which does no exploration), but *less information* than greedy; however, rrl achieves lower cost than greedy.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Numerical simulations", "weight": 1.0} -->

This suggests that rrl is reducing the uncertainty in a structured way, targeting uncertainty reduction in the parameters that 'matter most for control'.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Hardware-in-the-loop experiment", "weight": 1.0} -->

In this section, we consider the RRL problem for a hardware-in-the-loop simulation comprised of the interconnection of a physical servo mechanism (Quanser QUBE 2) and a synthetic (simulated) LTI dynamical system; cf. Appendix A.2 for full details of the experimental setup. An experimental trial consisted of the following procedure. Initial data was obtained by simulating the system for 0.5 seconds, under closed-loop feedback control (cf. Appendix A.2) with data sampled at 500Hz, to give 250 initial data points. We then applied methods rrl (with horizon $h = 5$) and greedy as described in §5. The total control horizon was $T = 1250$ (2.5 seconds at 500Hz) and was divided into $N = 5$ intervals, each of duration 0.5 seconds. We performed 5 of these experimental trials and plot the results in Figure2. In Figure 2(b) and (d) we plot the total cost (the sum of the costs at each epoch), and the cost at each epoch, respectively, for each method, and observe significantly better performance from rrl in both cases.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Hardware-in-the-loop experiment", "weight": 1.0} -->

Additional plots decomposing the cost into that associated with the physical and synthetic system are available in Appendix A.2.
