## Introduction

Learning to make decisions in an uncertain and dynamic environment is a task of fundamental importance in a number of domains. Though it has been the subject of intense research activity since the formulation of the 'dual control problem' in the 1960s, the recent success of reinforcement learning (RL), particularly in games, has inspired a resurgence in interest in the topic. Problems of this nature require decisions to be made with respect to two objectives. First, there is a goal to be achieved, typically quantified as a reward function to be maximized. Second, due to the inherent uncertainty there is a need to gather information about the environment, often referred to as 'learning' via 'exploration'. These two objectives are often competing, a fact known as the exploration/exploitation trade-off in RL, and the 'dual effect' (of decision) in control.

It is important to recognize that the second objective (exploration) is important only in so far as it facilitates the first (maximizing reward); there is no intrinsic value in reducing uncertainty. As a consequence, exploration should be targeted or application specific; it should *not* excite the system arbitrarily, but rather in such a way that the information gathered is useful for achieving the goal. Furthermore, in many real-world applications, it is essential that exploration does not compromise the safe and reliable operation of the system.

This paper is concerned with control of uncertain linear dynamical systems, with the goal of maximizing (minimizing) rewards (costs) that are a quadratic function of states and actions; cf. §2 for a detailed problem formulation. We derive methods to synthesize control policies that balance the exploration/exploitation tradeoff by performing robust, targeted exploration: *robust* in the sense that we optimize for worst-case performance given uncertainty in our knowledge of the system, and *targeted* in the sense that the policy excites the system so as to reduce uncertainty in such a way that specifically minimizes the worst-case cost. To this end, this paper makes the following specific contributions. We derive a high-probability bound on the spectral norm of the system parameter estimation error, in a form that is applicable to both robust control synthesis and design of targeted exploration; cf. §3. We also derive a convex approximation of the worst-case (w.r.t. parameter uncertainty) infinite-horizon linear quadratic regulator (LQR) problem; cf. §4.2. We then combine these two developments to present an approximate solution, via convex semidefinite programing (SDP), to the problem of minimizing the worst-case quadratic costs for an uncertain linear dynamical system; cf. §4. For brevity, we will refer to this as a 'robust reinforcement learning' (RRL) problem.

### Related work

Inspired, perhaps in part, by the success of RL in games, there has been a flurry of recent research activity in the analysis and design of RL methods for linear dynamical systems with quadratic rewards. Works such as employ the so-called 'optimism in the face of uncertainty' (OFU) principle, which selects control actions assuming that the true system behaves as the 'best-case' model in the uncertain set. This leads to optimal regret but requires the solution of intractable non-convex optimization problems. Alternatively, the works of employ Thompson sampling, which optimizes the control action for a system drawn randomly from the posterior distribution over the set of uncertain models, given data. The work of eschews uncertainty quantification, and demonstrates that 'so-called' certainty equivalent control attains optimal regret. There has also been considerable interest in 'model-free' methods for direct policy optimization, as well partially model-free methods based on spectral filtering. Unlike the present paper, none of the works above consider robustness which is essential for implementation on physical systems. Robustness is studied in the so-called 'coarse-ID' family of methods, c.f.. In, sample convexity bounds are derived for LQR with unknown linear dynamics. This approach is extended to adaptive LQR in, however, unlike the present paper, the policies are not optimized for exploration and exploitation jointly; exploration is effectively random. Also of relevance is the field of so-called 'safe RL' in which one seeks to respect certain safety constraints during exploration and/or policy optimization, as well as 'risk-sensitive RL', in which the search for a policy also considers the variance of the reward. Other works seek to incorporate notions of robustness commonly encountered in control theory, e.g. stability. In closing, we mention that related problems of simultaneous learning and control have a long history in control theory, beginning with the study of 'dual control' in the 1960s. Many of these formulations relied on a dynamic programing (DP) solution and, as such, were applicable only in special cases. Nevertheless, these early efforts established the importance of balancing 'probing' (exploration) with 'caution' (robustness). For subsequent developments from the field of control theory, cf. e.g..

## Problem statement

In this section we describe in detail the problem addressed in this paper. Notation is as follows: $A^{\top}$ denotes the transpose of a matrix $A$. $x_{1:n}$ is shorthand for the sequence ${\{ x_{t}\}}_{t = 1}^{n}$. $\lambda_{\text{max}}{(A)}$ denotes the maximum eigenvalue of a matrix $A$. $\otimes$ denotes the Kronecker product. $\text{vec}(A)$ stacks the columns of $A$ to form a vector. ${\mathbb{S}}_{+}^{n}$ (${\mathbb{S}}_{+ +}^{n}$) denotes the cone(s) of $n \times n$ symmetric positive semidefinite (definite) matrices. w.p. means 'with probability.' $\chi_{n}^{2}{(p)}$ denotes the value of the Chi-squared distribution with $n$ degrees of freedom and probability $p$. blkdiag is the block diagonal operator.

### Dynamics and cost function

We are concerned with control of linear time-invariant systems

where $x_{t} \in^{n_{x}}$, $u_{t} \in^{n_{u}}$ and $w_{t} \in^{n}$ denote the state (which is assumed to be directly measurable), input and process noise, respectively, at time $t$. The objective is to design a feedback control policy $u_{t} = {\phi{({\{ x_{1:t},u_{1:{t - 1}}\}})}}$ so as to minimize the cost function $\sum_{t = i}^{T}{c{(x_{t},u_{t})}}$, where ${c{(x_{t},u_{t})}} = {{x_{t}^{\top}Qx_{t}} + {u_{t}^{\top}Ru_{t}}}$ for user-specified positive semidefinite matrices $Q$ and $R$. When the parameters of the true system, denoted $\{ A_{\text{tr}},B_{\text{tr}}\}$, are known this is exactly the finite-horizon LQR problem, the optimal solution of which is well-known. We assume that $\{ A_{\text{tr}},B_{\text{tr}}\}$ are unknown.

### Modeling and data

As $\{ A_{\text{tr}},B_{\text{tr}}\}$ are unknown, all knowledge about the true system dynamics must be inferred from observed data, $\mathcal{D}_{n}:={\{ x_{t},u_{t}\}}_{t = 1}^{n}$. We assume that $\sigma_{w}$ is known, or has been estimated, and that we have access to initial data, denoted (with slight notational abuse) $\mathcal{D}_{0}$, obtained, e.g. during a preliminary experiment. For the model, parameter uncertainty can be quantified as:

### Proposition 2.1

Given observed data $\mathcal{D}_{n}$ from, and a uniform prior over the parameters $\theta = {\text{vec}\left( {\lbrack{AB}\rbrack} \right)}$, i.e., ${p{(\theta)}} \propto 1$, the posterior distribution $p{(\left. \theta \middle| \mathcal{D}_{n} \right.)}$ is given by $\mathcal{N}\left( \mu_{\theta},\Sigma_{\theta} \right)$, where $\mu_{\theta} = {\text{vec}\left( {\lbrack{\hat{A}\hat{B}}\rbrack} \right)} = {{\arg\min_{\theta \in^{n_{x}^{2} + {n_{x}n_{u}}}}}{\sum_{t = 1}^{n - 1}{|{x_{t + 1} - {{{\lbrack{x_{t}^{\top}u_{t}^{\top}}\rbrack} \otimes I_{n_{x}}}\theta}}|}^{2}}}$, i.e., the ordinary least squares estimator, and ${}_{}^{} = {\frac{1}{\sigma_{w}^{2}}{\sum_{t = 1}^{n - 1}{{\begin{bmatrix}
\end{bmatrix}\begin{bmatrix}
\end{bmatrix}^{\top}} \otimes I_{n_{x}}}}}$.

*Proof*: cf. §A.1.1. Based on Proposition 2.1 we can define a high-probability credibility region by:

where $c_{\delta} = {\chi_{n_{x}^{2} + {n_{x}n_{u}}}^{2}{(\delta)}}$ for $0 < \delta < 1$. Then, $\theta_{\text{tr}} = {\text{vec}\left( {\lbrack{A_{\text{tr}}B_{\text{tr}}}\rbrack} \right)} \in {\Theta_{e}{(\mathcal{D}_{n})}}$ w.p. $1 - \delta$.

### Policies

Though not necessarily optimal, we will restrict our attention to static-gain policies of the form $u_{t} = {{Kx_{t}} + {\Sigma^{1/2}e_{t}}}$, where $e_{t} \sim {\mathcal{N}(0,I)}$ represent random excitations for the purpose of learning. A policy comprises $K \in^{p \times n}$ and $\Sigma \in {\mathbb{S}}_{+}^{n_{u}}$, and is denoted $\mathcal{K} = {\{ K,\Sigma\}}$. Let ${\{ t_{i}\}}_{i = 0}^{N} \in {\mathbb{N}}$, with $0 = t_{0} \leq t_{1} \leq \ldots, \leq t_{N} = T$, partition the time horizon $T$ into $N$ intervals. The $i$th interval is of length $T_{i}:={t_{i} - t_{i - 1}}$. We will then design $N$ policies, ${\{\mathcal{K}_{i}\}}_{i = 1}^{N}$, such that $\mathcal{K}_{i} = {\{ K_{i},\Sigma_{i}\}}$ is deployed during the $i$th interval, $t \in {\lbrack t_{i - 1},t_{i}\rbrack}$. For convenience, we define the function $\mathcal{I}:_{+}\mapsto{\mathbb{N}}$ given by ${\mathcal{I}{(t)}}:={\arg{\min_{i \in {\mathbb{N}}}{\{{i:{t \leq t_{j}}}\}}}}$, which maps time $t$ to the index $i = {\mathcal{I}{(t)}}$ of the policy to be deployed. We also make use of the notation $u_{t} = {\mathcal{K}{(x_{t})}}$ as shorthand for $u_{t} = {{Kx_{t}} + {\Sigma^{1/2}e_{t}}}$.

### Worst-case dynamics

We are now in a position to define the optimization problem that we wish to solve in this paper. In the absence of knowledge of the true dynamics, $\{ A_{\text{tr}},B_{\text{tr}}\}$, given initial data $\mathcal{D}_{0}$, we wish to find a sequence of policies ${\{\mathcal{K}_{i}\}}_{i = 0}^{N}$ that minimize the expected cost $\sum_{t = 1}^{T}{c{(x_{t},u_{t})}}$, assuming that, at time $t$, the system evolves according to the *worst-case* dynamics within the high-probability credibility region $\Theta_{e}{(\mathcal{D}_{t})}$, i.e.,

where the expectation is w.r.t. $w_{t} \sim {\mathcal{N}\left( 0,{\sigma_{w}^{2}I_{n_{x}}} \right)}$ and $e_{t} \sim {\mathcal{N}\left( 0,I_{n_{u}} \right)}$. We choose to optimize for the worst-case dynamics so as to bound, with high probability, the cost of applying the policies to the unknown true system. In principle, problems such as can be solved via *dynamic programing* (DP). However, such DP-based solutions require gridding to obtain finite state-action spaces, and are hence computationally intractable for systems of even modest dimension. In what follows, we will present an approximate solution to this problem, which we refer to as a 'robust reinforcement learning' (RRL) problem, that retains the continuous sate-action space formulation and is based on convex optimization. To facilitate such a solution, we require a refined means of quantifying system uncertainty, which we present next.

Figure 1: Cartoon depiction of the problem addressed in this paper. The goal is to design N policies, {𝒦i}i = 1N, so as to minimize the worst-case cost (blue area) over the time horizon [0, T]; cf. §2.

## Modeling uncertainty for robust control

In this paper, we adopt a model-based approach to control, in which quantifying uncertainty in the estimates of the system dynamics is of central importance. From Proposition 2.1 the posterior distribution over parameters is Gaussian, which allows us to construct an 'ellipsoidal' credibility region $\Theta_{e}$, centered about the ordinary least squares estimates of the model parameters, as in.

To allow for an exact convex formulation of the control problem involving the *worst-case* dynamics, cf. §4.2, it is desirable to work with a credibility region that bounds uncertainty in terms of the spectral properties of the parameter error *matrix* $\lbrack{\hat{A} - A_{\text{tr}}},{\hat{B} - B_{\text{tr}}}\rbrack$, where $\{\hat{A},\hat{B}\}$ are the ordinary least squares estimates, i.e. ${\text{vec}\left( {\lbrack{\hat{A}\hat{B}}\rbrack} \right)} = \mu_{\theta}$, cf. Proposition 2.1. To this end, we will work with models of the form ${\mathcal{M}{(\mathcal{D})}}:={\{\hat{A},\hat{B},D\}}$ where $D \in {\mathbb{S}}^{n_{x} + n_{u}}$ specifies the following region, in parameter space, centered about $\{\hat{A},\hat{B}\}$:

The following lemma, cf. §A.1.2 for proof, suggests a specific means of constructing $D$, so as to ensure that $\Theta_{m}$ defines a high probability credibility region:

### Lemma 3.1

Given data $\mathcal{D}_{n}$ from, and $0 < \delta < 1$, let $D = {\frac{1}{\sigma_{w}^{2}c_{\delta}}{\sum_{t = 1}^{n - 1}{\begin{bmatrix}
\end{bmatrix}\begin{bmatrix}
\end{bmatrix}^{\top}}}}$, with $c_{\delta} = {\chi_{n_{x}^{2} + {n_{x}n_{u}}}^{2}{(\delta)}}$. Then ${\lbrack A_{\text{tr}},B_{\text{tr}}\rbrack} \in {\Theta_{m}{(\mathcal{M})}}$ w.p. $1 - \delta$.

For convenience, we will make use of the following shorthand notation: ${\mathcal{M}{(\mathcal{D}_{t_{i}})}} = {\{{\hat{A}}_{i},{\hat{B}}_{i},D_{i}\}}$.

Credibility regions of the form, i.e. bounds on the spectral properties of the estimation error, have appeared in recent works on data-driven and adaptive control, cf. e.g., \[11, Proposition 2.4\] which makes use of results from high-dimensional statistics. The construction in \[11, Proposition 2.4\] requires $\{ x_{t + 1},x_{t},u_{t}\}$ to be independent, and as such is not directly applicable to time series data, without subsampling to attain uncorrelated samples (though more complicated extensions to circumvent this limitation have been suggested ). Lemma 3.1 is directly applicable to correlated time series data, and provides a credibility region that is well suited to the RRL problem, cf. §4.3.

## Convex approximation to robust reinforcement learning problem

Equipped with the high-probability bound on the spectral properties of the parameter estimation error presented in Lemma 3.1, we now proceed with the main contribution of this paper: a convex approximation to the 'robust reinforcement learning' (RRL) problem in.

### Steady-state approximation of cost

In pursuit of a more tractable formulation, we first introduce the following approximation of,

Observe that has introduced two approximations to. First, in we only update the 'worst-case' model at the beginning of each epoch, when we deploy a new policy, rather than at each time step as in. This introduces some conservatism, as model uncertainty will generally decrease as more data is collected, but results in a simpler control synthesis problem. Second, we select the worst-case model from the 'spectral' credibility region $\Theta_{m}$ as defined in, rather than the 'ellipsoidal' region $\Theta_{e}$ defined in. Again, this introduces some conservatism as $\Theta_{e} \subseteq \Theta_{m}$, cf. §A.1.2, but permits convex optimization of the worst-case cost, cf. §4.2. For convenience, we denote

Next, we approximate the cost between epochs with the infinite-horizon cost, scaled appropriately for the epoch duration, i.e., between the $i - 1$th and $i$th epoch we approximate the cost as

This approximation is accurate when the epoch duration $T_{i}$ is sufficiently long relative to the time required for the state to reach the stationary distribution. Substituting into, the cost function that we seek to minimize becomes

The expectation in is w.r.t. to $w_{t}$ and $e_{t}$, as $\mathcal{D}_{t_{i}}$ depends on the random variables $x_{1:t_{i}}$ and $u_{1:t_{i}}$, which evolve according to the worst-case dynamics in.

### Optimization of worst-case cost

The previous subsection introduced an approximation of our 'ideal' problem, based on the worst-case infinite horizon cost, cf.. In this subsection we present a convex approach to the optimization of $J_{\infty}{(\mathcal{K},{\Theta_{m}{(\mathcal{M})}})}$ w.r.t. $\mathcal{K}$, given $\mathcal{M}$. The infinite horizon cost can be expressed as

Under the feedback policy $\mathcal{K}$, the covariance appearing on the RHS of can be expressed as

where $W = {{\mathbb{E}}\left\lbrack {x_{t}x_{t}^{\top}} \right\rbrack}$ denotes the stationary state covariance. For known $A$ and $B$, $W$ is given by the (minimum trace) solution to the Lyapunov inequality

i.e., $\arg{\min_{W}{\text{tr}W\text{s.t.}}}$. To optimize $J_{\infty}{(\mathcal{K},{\Theta_{m}{(\mathcal{M})}})}$ via convex optimization, there are two challenges to overcome: i. non-convexity of jointly searching for $K$ and $W$, satisfying and minimizing, ii. computing $W$ for worst-case ${\{ A,B\}} \in {\Theta_{m}{(\mathcal{M})}}$, rather than known $\{ A,B\}$.

Let us begin with the first challenge: nonconvexity. To facilitate a convex formulation of the RRL problem we write as

and introduce the change of variables $Z = {WK^{\top}}$ and $Y = {{KWK^{\top}} + \Sigma}$, collated in the variable ${\Xi = \begin{bmatrix}
\end{bmatrix}}.$ With this change of variables, minimizing subject to is a convex program.

Now, we turn to the second challenge: computation of the stationary state covariance under the worst-case dynamics. As a sufficient condition, we require to hold for all ${\{ A,B\}} \in {\Theta_{m}{(\mathcal{M})}}$. In particular, we define the following approximation of $J_{\infty}{(\mathcal{K},\mathcal{M})}$

### Lemma 4.1

Consider the worst-case cost $J_{\infty}{(\mathcal{K},\mathcal{M})}$, cf., and the approximation ${\overset{\sim}{J}}_{\infty}{(\mathcal{K},\mathcal{M})}$, cf.. ${{\overset{\sim}{J}}_{\infty}{(\mathcal{K},\mathcal{M})}} \geq {J_{\infty}{(\mathcal{K},\mathcal{M})}}$.

*Proof:* cf. §A.1.3. To optimize ${\overset{\sim}{J}}_{\infty}{(\mathcal{K},\mathcal{M})}$, as defined in, we make use of the following result from:

### Theorem 4.1

The data matrices $(\mathcal{A},\mathcal{B},\mathcal{C},\mathcal{P},\mathcal{F},\mathcal{G},\mathcal{H})$ satisfy, for all $X$ with ${I - {X^{\top}\mathcal{P}X}} \succeq 0$, the robust fractional quadratic matrix inequality

for some $\lambda \geq 0$.

To put in a form to which Theorem 4.1 is applicable, we make use of of the nominal parameters $\hat{A}$ and $\hat{B}$. With $X$ defined as in, such that ${\lbrack{AB}\rbrack} = {{\lbrack{\hat{A}\hat{B}}\rbrack} - X^{\prime}}$, we can express as

where the 'iff' follows from the Schur complement. Given this equivalent representation, by Theorem 4.1, holds for all ${X^{\top}D\mathcal{M}} \preceq I$ (i.e. all ${\{ A,B\}} \in {\Theta_{m}{(\mathcal{M})}}$) iff

which is simply with the substitutions $\mathcal{A} = {- \Xi}$, $\mathcal{B} = {\Xi{\lbrack{\hat{A}\hat{B}}\rbrack}^{\top}}$, $\mathcal{C} = {W - {{\lbrack{\hat{A}\hat{B}}\rbrack}\Xi{\lbrack{\hat{A}\hat{B}}\rbrack}^{\top}}}$, $\mathcal{F} = {\sigma_{w}I}$, $\mathcal{G} = 0$, and $\mathcal{P} = D$. We now have the following result, cf. §A.1.4 for proof.

### Theorem 4.2

The solution to ${\min_{\mathcal{K}}{\overset{\sim}{J}}_{\infty}}{(\mathcal{K},{\Theta_{m}{(\mathcal{M})}})}$, cf., is given by the SDP:

with the optimal policy given by $\mathcal{K} = {\{{Z^{\top}W^{- 1}},{Y - {Z^{\top}W^{- 1}Z}}\}}$.

Note that as ${\min_{\mathcal{K}}{\overset{\sim}{J}}_{\infty}}{(\mathcal{K},{\Theta_{m}{(\mathcal{M})}})}$ is purely an 'exploitation' problem $\Sigma\rightarrow 0$ in the above SDP; in general, $\Sigma \neq 0$ in the RRL setting (i.e. ) where exploration is beneficial.

### Approximate uncertainty propagation

Let us now return to the RRL problem. Given a model $\mathcal{M}$, §4.2 furnished us with a convex method to minimize the worst-case cost. However, at time $t = 0$, we have access only to data $\mathcal{D}_{0}$, and therefore, only $\mathcal{M}{(\mathcal{D}_{0})}$. To optimize we need to approximate the models ${\{{\mathcal{M}{(\mathcal{D}_{t_{i}})}}\}}_{i = 1}^{N - 1}$ based on the future data, ${\{\mathcal{D}_{t_{i}}\}}_{i = 1}^{N - 1}$, that we *expect* to see. To this end, we denote the approximate model, at time $t = t_{j}$ given data $\mathcal{D}_{t_{i}}$, by ${{\overset{\sim}{\mathcal{M}}}_{j}{(\mathcal{D}_{t_{i}})}}:={\{{\overset{\sim}{A}}_{j|i},{\overset{\sim}{B}}_{j|i},{\overset{\sim}{D}}_{j|i}\}} \approx {{\mathbb{E}}\left\lbrack {\mathcal{M}{(\mathcal{D}_{t_{j}})}} \middle| \mathcal{D}_{t_{i}} \right\rbrack}$. We now describe specific choices for ${\overset{\sim}{A}}_{j|i}$, ${\overset{\sim}{B}}_{j|i}$, and ${\overset{\sim}{D}}_{j|i}$, beginning with the latter.

Recall that the uncertainty matrix $D$ at the $i$th epoch is denoted $D_{i}$. The uncertainty matrix at the $i + 1$th epoch is then given by $D_{i + 1} = {D_{i} + {\frac{1}{\sigma_{w}^{2}c_{\delta}}{\sum_{t = t_{i}}^{t_{i + 1}}{\begin{bmatrix}
\end{bmatrix}\begin{bmatrix}
\end{bmatrix}^{\top}}}}}$. We approximate the empirical covariance matrix in this expression with the worst-case state covariance $W_{i}$ as follows:

This approximation makes use of the same calculation appearing in. The equality makes use of the change of variables introduced in §4.2. Note that in proof of Theorem 4.2, cf. §A.1.4, it was shown that $\Xi = \begin{bmatrix}
{K^{\top}W} & {{KWK^{\top}} + \Sigma}
\end{bmatrix}$, when $\Xi$ is the solution of.

Next, we turn our attention to approximating the effect of future data on the nominal parameter estimates $\{\hat{A},\hat{B}\}$. Updating these (ordinary least squares) estimates based on the expected value of future observations involves difficult integrals that must be approximated numerically \[27, §5\]. To preserve convexity in our formulation, we approximate future nominal parameter estimates with the current estimates, i.e., given data $\mathcal{D}_{t_{i}}$ we set ${\overset{\sim}{A}}_{j|i} = {\hat{A}}_{i}$ and ${\overset{\sim}{B}}_{j|i} = {\hat{B}}_{i}$. To summarize, our approximate model at epoch $j$ is given by ${{\overset{\sim}{\mathcal{M}}}_{j}{(\mathcal{D}_{t_{i}})}} = {\{{\hat{A}}_{i},{\hat{B}}_{i},{D_{i} + {\frac{1}{\sigma_{w}^{2}c_{\delta}}{\sum_{k = {i + 1}}^{j}{T_{k + 1}\Xi_{k}}}}}\}}$.

### Final convex program and receding horizon application

We are now in a position to present a convex approximation to our original problem. By substituting ${\overset{\sim}{J}}_{\infty}{( \cdot, \cdot )}$ for $J_{\infty}{( \cdot, \cdot )}$, and ${\overset{\sim}{\mathcal{M}}}_{i}{(\mathcal{D}_{0})}$ for $\mathcal{M}{(\mathcal{D}_{t_{i}})}$ in, we attain the cost function: ${\sum_{i = 1}^{N}{{T_{i} \times {\overset{\sim}{J}}_{\infty}}\left( \mathcal{K}_{i},{\Theta_{m}{({{\overset{\sim}{\mathcal{M}}}_{i - 1}{(\mathcal{D}_{0})}})}} \right)}}.$ Consider the $i$th term in this sum, which can be optimized via the SDP, with $D = {\overset{\sim}{D}}_{i - {1|0}}$. Notice two important facts: 1. for fixed multiplier $\lambda$, the uncertainty ${\overset{\sim}{D}}_{i - {1|0}}$ enters *linearly* in the constraint ${S{( \cdot )}} \succeq 0$, cf.; 2. ${\overset{\sim}{D}}_{i - {1|0}}$ is *linear* in the decision variables ${\{\Xi_{k}\}}_{k = 1}^{i - 1}$, cf. end of §4.3. Therefore, the constraint ${S{( \cdot )}} \succeq 0$ remains linear in the decision variables, which means that the cost function derived by substituting ${\overset{\sim}{\mathcal{M}}}_{i}{(\mathcal{D}_{0})}$ into can be optimized as an SDP, cf. below.

Hitherto, we have considered the problem of minimizing the expected cost over time horizon $T$ given initial data $\mathcal{D}_{0}$. In practical applications, we employ a *receding horizon* strategy, i.e., at the $i$th epoch, given data $\mathcal{D}_{t_{i - 1}}$, we find a sequence of policies ${\{\mathcal{K}_{j}\}}_{j = i}^{i + h}$ that minimize the approximate $h$-step-ahead expected cost

and then apply $\mathcal{K}_{i}$ during the $i$th epoch. At the beginning of the $i + 1$th epoch, we repeat the process; cf. Algorithm1. The problem ${\min_{{\{\mathcal{K}_{j}\}}_{j = i}^{N}}\hat{J}}{(i,h,{\{\mathcal{K}_{j}\}}_{j = i}^{i + h},\mathcal{D}_{t_{i - 1}})}$ can be solved as the SDP:

$\min\limits_{\lambda_{i} \geq {0,{\{\Xi_{j}\}}_{j = i}^{i + h}}}$ ${{{{\sum\limits_{j = i}^{i + h}{\text{tr}\left( {\text{blkdiag}{(Q,R)}\Xi_{j}} \right)}},{\text{s.t.}S{(\lambda_{i},\Xi_{i},{\hat{A}}_{i},{\hat{B}}_{i},D_{i})}}} \succeq 0},{\Xi_{j} \succeq {0{\forall j}}}},$ (40a)
${{{S\left( \lambda_{j},\Xi_{k},{\hat{A}}_{i},{\hat{B}}_{i},{D_{i} + {\frac{1}{\sigma_{w}^{2}c_{\delta}}{\sum\limits_{k = {i + 1}}^{j}{T_{k + 1}\Xi_{k}}}}} \right)} \succeq {0\text{~for~}j} = {i + 1}},{\ldots,{i + h}}}.$ (40b)

### Selecting multipliers

For optimization of ${\overset{\sim}{J}}_{\infty}{(\mathcal{K},\mathcal{M})}$ given a model $\mathcal{M}$, i.e. the simultaneous search for the policy $\mathcal{K}$ and multiplier $\lambda$ is convex, as $D$ is fixed. However, in the RRL setting, '$D$' is a function of the decision variables $\Xi_{i}$, cf. (40b), and so the multipliers ${\{\lambda_{j}\}}_{j = {i + 1}}^{i + h} \in_{+}^{h - 1}$ must be specified in advance. We propose the following method of selecting the multipliers: given $\mathcal{D}_{t_{i - 1}}$, solve $\overline{\mathcal{K}} = {{\arg{\min_{\mathcal{K}}{\overset{\sim}{J}}_{\infty}}}{(\mathcal{K},{\Theta_{m}{({\mathcal{M}{(\mathcal{D}_{t_{i - 1}})}})}})}}$ via the SDP. Then, compute the cost $\hat{J}{(i,h,{\{\overline{\mathcal{K}}\}}_{j = i}^{i + h},\mathcal{D}_{t_{i - 1}})}$ by solving, but with the policies fixed to $\overline{\mathcal{K}}$, and the multipliers ${\{\lambda_{j}\}}_{j = i}^{i + h} \in_{+}^{h}$ as free decision variables. In other words, approximate the worst-case cost of deploying the $\overline{\mathcal{K}}$, $h$ epochs into the future. Then, use the multipliers found during the calculation of this cost for control policy synthesis at the $i$th epoch.

### Computational complexity

The proposed method can be implemented via semidefinite programing (SDP) for which computational complexity is well-understood. In particular, the cost of solving the SDP scales as $\mathcal{O}{({\max{\{ m^{3},{mn^{3}},{m^{2}n^{2}}\}}})}$, where $m = {{{({1/2})}n_{x}{({n_{x} + 1})}} + {{({1/2})}n_{u}{({n_{u} + 1})}} + {n_{x}n_{u}} + 1}$ denotes the dimensionality of the decision variables, and $n = {{3n_{x}} + n_{u}}$ is the dimensionality of the LMI $S \succeq 0$. The cost of solving the SDP is then given, approximately, by the cost of multiplied by the horizon $h$.

1:Input: initial data 𝒟0, confidence δ, LQR cost matrices Q and R, epochs {ti}i = 1N.
3: Compute/update nominal model ℳ (𝒟ti − 1).
4: Solve convex program.
5: Recover policy 𝒦i: Ki = Zi⊤ Wi−1 and Σi = Yi − Zi⊤ Wi−1 Zi.
6: Apply policy to true system for ti − 1 &lt; t ≤ ti, which evolves according to with ut = Ki xt + Σi1/2 et.
7: Form 𝒟ti = 𝒟ti − 1 ∪ {xti − 1: ti, uti − 1: ti} based on newly observed data.
Algorithm 1 Receding horizon application to true system

## Experimental results

### Numerical simulations

In this section, we consider the RRL problem with parameters

Figure 2: Results for the experiments described in §5. (a) total costs (sum of costs at each epoch) for the numerical simulations. On the left, we plot the costs when the methods are applied to the true system. In the middle, we plot the worst-case costs, when the model uncertainty is updated using the data obtained from applying the methods to the true system. On the right, we plot the worst-case costs when the model uncertainty is updated using the theoretical worst-case system behavior. (b) total costs sum of costs at each epoch) for the hardware-in-the-loop experiments. (c) on the left axis, we plot the (median) costs at each epoch for numerical simulations. On the right axis, we plot the information, a scalar measure of uncertainty defined in §5. The shaded region denotes the inter-quartile range. The scenarios are in the same order as (a). (d) (median) costs at each epoch for the hardware-in-the-loop experiments. The shaded region covers the best/worst costs at each epoch.

We partition the time horizon $T = 10^{3}$ into $N = 10$ equally spaced intervals, each of length $T_{i} = 100$. For robustness, we set $\delta = 0.05$. Each experimental trial consists of the following procedure. Initial data $\mathcal{D}_{0}$ is obtained by driving the system forward 6 time steps, excited by ${\overset{\sim}{u}}_{t} \sim {\mathcal{N}(0,I)}$. This open-loop experiment is repeated 500 times, such that $\mathcal{D}_{0} = {\{{\overset{\sim}{x}}_{1:6}^{i},{\overset{\sim}{u}}_{1:6}\}}_{i = 1}^{500}$. We then apply three methods: i. rrl - the method proposed in §4.4, with look-ahead horizon $h = 10$; ii. nom - applying the 'nominal' robust policy $\mathcal{K}_{i} = {{\arg{\min_{\mathcal{K}}{\overset{\sim}{J}}_{\infty}}}{(\mathcal{K},{\Theta_{m}{({\mathcal{M}{(\mathcal{D}_{t_{i}})}})}})}}$, i.e., a pure greedy exploitation policy, with no explicit exploration; iii. greedy - first obtaining a nominal robustly stabilizing policy as with nom, but then optimizing (i.e., increasing, if possible) the exploration variance $\Sigma$ until the greedy policy and the rrl policy have the same theoretical worst-case cost at the current epoch. This is a greedy exploration policy. We perform 100 of these trials and plot the results in Figure 2. In Figure 2(a) we plot the total costs (i.e. the sum of the costs for each epoch over the entire time horizon). In each setting (see caption for details), rrl attains lower total cost than the other methods. In Figure 2(c) we plot the costs at each epoch; as may be expected, nom (which does no explicit exploration) often attains lower cost than rrl at the initial epochs, rrl, which does exploration, achieves lower cost in the end. We emphasize that this balance of exploration/exploitation occurs *automatically*. rrl always outperforms greedy. In Figure 2(c) we also plot the *information*, defined as ${1/\lambda_{\text{max}}}{(D_{i}^{- 1})}$, at the $i$th epoch, which is the (inverse) of the 2-norm of parameter error, cf.. The larger the information, the more certain the system (in an absolute sense). Observe that rrl achieves larger information than nom (which does no exploration), but *less information* than greedy; however, rrl achieves lower cost than greedy. This suggests that rrl is reducing the uncertainty in a structured way, targeting uncertainty reduction in the parameters that 'matter most for control'.

### Hardware-in-the-loop experiment

In this section, we consider the RRL problem for a hardware-in-the-loop simulation comprised of the interconnection of a physical servo mechanism (Quanser QUBE 2) and a synthetic (simulated) LTI dynamical system; cf. Appendix A.2 for full details of the experimental setup. An experimental trial consisted of the following procedure. Initial data was obtained by simulating the system for 0.5 seconds, under closed-loop feedback control (cf. Appendix A.2) with data sampled at 500Hz, to give 250 initial data points. We then applied methods rrl (with horizon $h = 5$) and greedy as described in §5. The total control horizon was $T = 1250$ (2.5 seconds at 500Hz) and was divided into $N = 5$ intervals, each of duration 0.5 seconds. We performed 5 of these experimental trials and plot the results in Figure2. In Figure 2(b) and (d) we plot the total cost (the sum of the costs at each epoch), and the cost at each epoch, respectively, for each method, and observe significantly better performance from rrl in both cases. Additional plots decomposing the cost into that associated with the physical and synthetic system are available in Appendix A.2.
