<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Dynamic Policy Programming

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we propose a novel policy iteration method, called dynamic policy programming (DPP), to estimate the optimal policy in the infinite-horizon Markov decision processes. We prove the finite-iteration and asymptotic l\infty-norm performance-loss bounds for DPP in the presence of approximation/estimation error. The bounds are expressed in terms of the l\infty-norm of the average accumulated error as opposed to the l\infty-norm of the error in the case of the standard approximate value iteration (AVI) and the approximate policy iteration (API). This suggests that DPP can achieve a better performance than AVI and API since it averages out the simulation noise caused by Monte-Carlo sampling throughout the learning process. We examine this theoretical results numerically by com- paring the performance of the approximate variants of DPP with existing reinforcement learning (RL) methods on different problem domains. Our results show that, in all cases, DPP-based algorithms outperform other RL methods by a wide margin.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many problems in robotics, operations research and process control can be represented as a control problem that can be solved by finding the optimal policy using *dynamic programming* (DP). DP is based on the estimating some measures of the value of state-action $Q^{\ast}{(x,a)}$ through the Bellman equation. For high-dimensional discrete systems or for continuous systems, computing the value function by DP is intractable. The common approach to make the computation tractable is to approximate the value function using function-approximation and Monte-Carlo sampling. Examples of such approximate dynamic programming (ADP) methods are approximate policy iteration (API) and approximate value iteration (AVI).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

ADP methods have been successfully applied to many real world problems, and theoretical results have been derived in the form of finite iteration and asymptotic performance guarantee of the induced policy. The asymptotic $\ell_{\infty}$-norm performance-loss bounds of API and AVI are expressed in terms of the supremum, with respect to (w.r.t.) the number of iterations, of the approximation errors: where $\gamma$ denotes the discount factor, $\parallel \cdot \parallel$ is the $\ell_{\infty}$-norm w.r.t. the state-action pair $(x,a)$. Also, $\pi_{k}$ and $\epsilon_{k}$ are the control policy and the approximation error at round $k$ of the ADP algorithms, respectively. In many problems of interest, however, the supremum over the normed-error $\left\| \epsilon_{k} \right\|$ can be large and hard to control due to the large variance of estimation caused by Monte-Carlo sampling.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In those cases, a bound which instead depends on the average accumulated error ${\overline{\epsilon}}_{k} = {{1/{({k + 1})}}{\sum{{}_{j = 0}^{k}\epsilon_{j}^{}}}}$ is preferable. This is due to the fact that the errors associated with the variance of estimation can be considered as the instances of some zero-mean random variables. Therefore, one can show, by making use of a law of large numbers argument, that those errors are asymptotically *averaged out* by accumulating the approximation errors of all iterations.^11^1The law of large numbers requires the errors to satisfy some stochastic assumptions, e.g., they need to be identically and independently distributed (i.i.d.) samples or martingale differences.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose a new mathematically-justified approach to estimate the optimal policy, called dynamic policy programming (DPP). We prove finite-iteration and asymptotic performance loss bounds for the policy induced by DPP in the presence of approximation. The asymptotic bound of approximate DPP is expressed in terms of the average accumulated error $\|{\overline{\epsilon}}_{k}\|$ as opposed to $\|\epsilon_{k}\|$ in the case of AVI and API. This result suggests that DPP may perform better than AVI and API in the presence of large variance of estimation since it can average out the estimation errors throughout the learning process. The dependency on the average error $\|{\overline{\epsilon}}_{k}\|$ follows naturally from the incremental policy update of DPP which at each round of policy update, unlike AVI and API, accumulates the approximation errors of the previous iterations, rather than just minimizing the approximation error of the current iteration.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This article is organized as follows. In Section 2, we present the notations which are used in this paper. We introduce DPP and we investigate its convergence properties in Section 3. In Section 4, we demonstrate the compatibility of our method with the approximation techniques. We generalize DPP bounds to the case of function approximation and Monte-Carlo simulation. We also introduce a new convergent RL algorithm, called DPP-RL, which relies on an approximate sample-based variant of DPP to estimate the optimal policy. Section 5, presents numerical experiments on several problem domains including the optimal replacement problem and a stochastic grid world. In Section 6 we briefly review some related work. Finally, we discuss some of the implications of our work in Section 7.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Markov Decision Processes", "weight": 1.0} -->

A discounted MDP is a quintuple $(\mathcal{X},\mathcal{A},P,\mathcal{R},\gamma)$, where $\mathcal{X}$ and $\mathcal{A}$ are, respectively, the state space and the action space. $P$ shall denote the state transition distribution and $\mathcal{R}$ denotes the reward kernel. $\gamma \in {\lbrack 0,1)}$ denotes the discount factor. The transition $P$ is a probability kernel over the next state upon taking action $a$ from state $x$, which we shall denote by $P{( \cdot |x,a)}$. $\mathcal{R}$ is a set of real-valued numbers. A reward ${r{(x,a)}} \in \mathcal{R}$ is associated with each state $x$ and action $a$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Markov Decision Processes", "weight": 1.0} -->

To keep the representation succinct, we shall denote the joint state-action space $\mathcal{X} \times \mathcal{A}$ by $\mathcal{Z}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Assumption 1 (MDP Regularity)", "weight": 1.0} -->

A policy kernel $\pi{(\cdot | \cdot)}$ determines the distribution of the control action given the past observations. The policy is called stationary and Markovian if the distribution of the control action is independent of time and only depends on the last state $x$. Given the last state $x$, we shall denote the stationary policy by $\pi{(\cdot |x)}$. A stationary policy is called deterministic if for any state $x$ there exists some action $a$ such that $\pi{(\cdot |x)}$ concentrates on this action. Given the policy $\pi$ its corresponding value function $V^{\pi}:{\mathcal{X}\rightarrow{\mathbb{R}}}$ denotes the expected value of the long-term discounted sum of rewards in each state $x$, when the action is chosen by policy $\pi$ which we denote by $V^{\pi}{(x)}$. Often it is convenient to associate value functions not with states but with state-action pairs.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Assumption 1 (MDP Regularity)", "weight": 1.0} -->

Therefore, we introduce $Q^{\pi}:{\mathcal{Z}\rightarrow{\mathbb{R}}}$ as the expected total discounted reward upon choosing action $a$ from state $x$ and then following policy $\pi$, which we shall denote by $Q^{\pi}{(x,a)}$. We define the *Bellman operator* $\mathcal{T}^{\pi}$ on the action-value functions: We also notice that $Q^{\pi}$ is the fixed point of $\mathcal{T}^{\pi}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Assumption 1 (MDP Regularity)", "weight": 1.0} -->

The goal is to find a policy $\pi^{\ast}$ that attains the *optimal value function*, ${V^{\ast}{(x)}} \triangleq {\sup_{\pi}{V^{\pi}{(x)}}}$, at all states $x \in \mathcal{X}$. The optimal value function satisfies the Bellman equation: Likewise, the *optimal action-value function* $Q^{\ast}$ is defined by ${Q^{\ast}{(x,a)}} = {\sup_{\pi}{Q^{\pi}{(x,a)}}}$ for all ${(x,a)} \in \mathcal{Z}$. We shall define the *Bellman optimality operator* $\mathcal{T}$ on the action-value functions as: Likewise, $Q^{\ast}$ is the fixed point of $\mathcal{T}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Assumption 1 (MDP Regularity)", "weight": 1.0} -->

Both $\mathcal{T}$ and $\mathcal{T}^{\pi}$ are contraction mappings, w.r.t. the supremum norm, with the factor $\gamma$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption 1 (MDP Regularity)", "weight": 1.0} -->

In other words, for any two action-value functions $Q$ and $Q'$, we have: The policy distribution $\pi$ defines the state-action transition kernel $P^{\pi}:{{M{(\mathcal{Z})}}\rightarrow{M{(\mathcal{Z})}}}$, where $M$ is the space of all probability measures defined on $\mathcal{Z}$, as: From this kernel a right-linear operator $P^{\pi} \cdot$ is defined: Further, we define two other right-linear operators $\pi \cdot$ and $P \cdot$: We define the max operator $\mathcal{M}$ on the action value functions by ${{({\mathcal{M}Q})}{(x)}} \triangleq {{\max_{a \in \mathcal{A}}Q}{(x,a)}}$, for all $x \in \mathcal{X}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Dynamic Policy Programming", "weight": 1.0} -->

In this section, we derive the DPP algorithm starting from the Bellman equation. We first show that by adding a relative entropy term to the reward we can control the deviations of the induced policy from a baseline policy. We then derive an iterative double-loop approach which combines value and policy updates. We reduce this double-loop iteration to just a single iteration by introducing DPP algorithm. We emphasize that the purpose of the following derivations is to motivate DPP, rather than to provide a formal characterization. Subsequently, in Subsection 3.2 and Section 4, we theoretically investigate the finite-iteration and the asymptotic behavior of DPP and prove its convergence.

<!-- chunk {"id": "body-0016", "role": "body", "section": "From Bellman Equation to DPP Recursion", "weight": 1.0} -->

Consider the relative entropy between the policy $\pi$ and some baseline policy $\overline{\pi}$: We define a new value function $V_{\overline{\pi}}^{\pi}$, for all $x \in \mathcal{X}$, which incorporates $g$ as a penalty term for deviating from the base policy $\overline{\pi}$ and the reward under the policy $\pi$: where $\eta$ is a positive constant and $r_{t + k}$ is the reward at time $t + k$. Also, the expected value is taken w.r.t. the state transition probability distribution $P$ and the policy $\pi$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "From Bellman Equation to DPP Recursion", "weight": 1.0} -->

The optimal value function ${V_{\overline{\pi}}^{\ast}{(x)}} \triangleq {\sup_{\pi}{V_{\overline{\pi}}^{\pi}{(x)}}}$ then satisfies the following Bellman equation for all $x \in \mathcal{X}$: Equation is a modified version of where, in addition to maximizing the expected reward, the optimal policy ${\overline{\pi}}^{\ast}$ also minimizes the distance with the baseline policy $\overline{\pi}$. The maximization in can be performed in closed form.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Dynamic Policy Programming with Approximation", "weight": 1.0} -->

Algorithm 1 (DPP) only applies to small problems with a few states and actions. One can generalize the DPP algorithm for the problems of practical scale by using function approximation techniques. Also, to compute the optimal policy by DPP an explicit knowledge of model is required. In many real world problems, this information is not available instead it may be possible to simulate the state transition by Monte-Carlo sampling and then approximately *estimate* the optimal policy using these samples. In this section, we provide results on the performance-loss of DPP in the presence of approximation/estimation error. We then compare $\ell_{\infty}$-norm performance-loss bounds of DPP with the standard results of AVI and API. Finally, We introduce new approximate algorithms for implementing DPP with Monte-Carlo sampling (DPP-RL) and linear function approximation (SADPP).

<!-- chunk {"id": "body-0019", "role": "body", "section": "The $\\ell_{\\infty}$-norm performance-loss bounds for approximate DPP", "weight": 1.0} -->

Let us consider a sequence of action preferences $\{\Psi_{0},\Psi_{1},\Psi_{2},\ldots\}$ such that, at round $k$, the action preferences $\Psi_{k + 1}$ is the result of approximately applying the DPP operator by the means of function approximation or Monte-Carlo simulation, i.e., for all ${(x,a)} \in \mathcal{Z}$: ${\Psi_{k + 1}{(x,a)}} \approx {\mathcal{O}\Psi_{k}{(x,a)}}$. The error term $\epsilon_{k}$ is defined as the difference of $\mathcal{O}\Psi_{k}$ and its approximation: The approximate DPP update rule is then given: We begin by finite iteration analysis of the approximate DPP. The following theorem establishes an upper-bound on the performance loss of DPP in the presence of approximation error.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Reinforcement Learning with Dynamic Policy Programming", "weight": 1.0} -->

To compute the optimal policy by DPP one needs an explicit knowledge of model. In many problems we do not have access to this information but instead we can generate samples by simulating the model. The optimal policy can then be *learned* using these samples. In this section, we introduce a new RL algorithm, called DPP-RL, which relies on a sampling-based variant of DPP to update the policy. The update rule of DPP-RL is very similar to.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Reinforcement Learning with Dynamic Policy Programming", "weight": 1.0} -->

The only difference is that, in DPP-RL, we replace the Bellman operator $\mathcal{T}^{\pi}\Psi{(x,a)}$ with its sample estimate ${\mathcal{T}_{k}^{\pi}\Psi{(x,a)}} \triangleq {{r{(x,a)}} + {\pi\Psi{(y_{k})}}}$, where the next sample $y_{k}$ is drawn from $P{( \cdot |x,a)}$:^44^4We assume, hereafter, that we have access to the generative model of MDP, i.e., given the state-action pair $(x,a)$ we can generate the next sample $y$ from $P{( \cdot |x,a)}$ for all ${(x,a)} \in \mathcal{Z}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Reinforcement Learning with Dynamic Policy Programming", "weight": 1.0} -->

The pseudo-code of DPP-RL algorithm is shown in Algorithm 2.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Reinforcement Learning with Dynamic Policy Programming", "weight": 1.0} -->

a \middle| x \right.)}} = \frac{\exp{({\eta\Psi_{K}{(x,a)}})}}{\underset{a^{\prime}\in\mathcal{A}}{\sum}{\exp{({\eta\Psi_{K}{(x,a')}})}}}$; Algorithm 2 (DPP-RL) Reinforcement learning with DPP Equation is just an approximation of DPP update rule. Therefore, the convergence result of Corollary 2 does not hold for DPP-RL. However, the new algorithm still converges to the optimal policy since one can show that the errors associated with approximating are asymptotically *averaged out* by DPP-RL, as postulated by Corollary 5 ‣ 4.1 The ℓ_∞-norm performance-loss bounds for approximate DPP ‣ 4 Dynamic Policy Programming with Approximation ‣ Dynamic Policy Programming"). The following theorem establishes the asymptotic convergence of the policy induced by DPP-RL to the optimal policy.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Approximate Dynamic Policy Programming with Linear Function Approximation", "weight": 1.0} -->

In this subsection, we consider DPP with *linear function approximation* (LFA) and *least-squares regression*. Given a set of basis functions $\mathcal{F}_{\phi} = \left\{ \phi_{1},\ldots,\phi_{k} \right\}$, where each $\phi_{i}:{\mathcal{Z}\rightarrow\Re}$ is a bounded real valued function, the sequence of action preferences $\{\Psi_{0},\Psi_{1},{\Psi_{2}\cdots}\}$ are defined as a linear combination of these basis functions: $\Psi_{k} = {\theta_{k}^{\mathsf{T}}\Phi}$, where $\Phi$ is a $m \times 1$ column vector with the entries ${\{\phi_{i}\}}_{{i = 1}:m}$ and $\theta_{k} \in \Re^{m}$ is a $m \times 1$ vector of parameters.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Approximate Dynamic Policy Programming with Linear Function Approximation", "weight": 1.0} -->

The action preference function $\Psi_{k + 1}$ is an approximation of the DPP operator $\mathcal{O}\Psi_{k}$. In case of LFA the common approach to approximate DPP operator is to find a vector $\theta_{k + 1}$ that projects $\mathcal{O}\Psi_{k}$ on the column space spanned by $\Phi$ by minimizing the loss function: where $\mu$ is a probability measure on $\mathcal{Z}$. The best solution, that minimize $J$, is called the least-squares solution: where the expectation is taken w.r.t. ${(x,a)} \sim \mu$. In principle, to compute the least squares solution equation requires to compute $\mathcal{O}\Psi_{k}$ for all states and actions. For large scale problems this becomes infeasible.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Approximate Dynamic Policy Programming with Linear Function Approximation", "weight": 1.0} -->

Instead, we can make a sample estimate of the least-squares solution by minimizing the empirical loss ${\overset{\sim}{J}}_{k}{(\theta;\Psi)}$: where ${\{{(X_{n},A_{n})}\}}_{{n = 1}:N}$ is a set of $N$ i.i.d. samples drawn from the distribution $\mu$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Approximate Dynamic Policy Programming with Linear Function Approximation", "weight": 1.0} -->

The empirical least-squares solution which minimizes ${\overset{\sim}{J}}_{k}{(\theta;\Psi)}$ is given: Algorithm 3 presents the *sampling-based approximate dynamic policy programming* (SADPP) in which we rely on to approximate DPP operator at each iteration.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

In this section, we analyze empirically the effectiveness of the proposed algorithms on different problem domains. We first examine the convergence properties of DPP-RL (Algorithm 2) on several discrete state-action problems and compare it with two standard algorithms: a synchronous variant of Q-learning (QL) and the model-based *Q*-value iteration (VI) of Kearns and Singh. Next, we investigate the finite-time performance of SADPP (Algorithm 3) in the presence of function approximation and a limited sampling budget per iteration. In this case, we consider a variant of the optimal replacement problem described in Munos and Szepesvári and compare our method with regularized least-squares fitted $Q$-iteration (RFQI). The source code of all tested algorithms are freely available in

<!-- chunk {"id": "body-0029", "role": "body", "section": "DPP-RL", "weight": 1.0} -->

We consider the following large-scale MDPs as benchmark problems: Figure 1: Linear MDP: Illustration of the linear MDP problem. Nodes indicate states. States x1 and x2500 are the two absorbing states and state xk is an example of interior state. Arrows indicate possible transitions of these three nodes only. From xk any other node is reachable with transition probability (arrow thickness) proportional to the inverse of the distance to xk (see the text for details).: this problem consists of states ${x_{k} \in \mathcal{X}},{k = {\{ 1,2,\ldots,2500\}}}$ arranged in a one-dimensional chain (see Figure 1). There are two possible actions $\mathcal{A} = {\{{- 1},{+ 1}\}}$ (left/right) and every state is accessible from any other state except for the two ends of the chain, which are absorbing states. A state $x_{k} \in \mathcal{X}$ is called absorbing if ${P{(\left.

<!-- chunk {"id": "body-0030", "role": "body", "section": "DPP-RL", "weight": 1.0} -->

The transition probability for an interior state $x_{k}$ to any other state $x_{l}$ is inversely proportional to their distance in the direction of the selected action, and zero for all states corresponding to the opposite direction. Formally, consider the following quantity $n{(x_{l},a,x_{k})}$ assigned to all non-absorbing states $x_{k}$ and to every ${(x_{l},a)} \in \mathcal{Z}$: We can write the transition probabilities as: Any transition that ends up in one of the interior states has associated reward $- 1$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "DPP-RL", "weight": 1.0} -->

The optimal policy corresponding to this problem is to reach the closest absorbing state as soon as possible.: the combination lock problem considered here is a stochastic variant of the reset state space models introduced in Koenig and Simmons, where more than one reset state is possible (see Figure 2).

<!-- chunk {"id": "body-0032", "role": "body", "section": "DPP-RL", "weight": 1.0} -->

In our case we consider, as before, a set of states ${x_{k} \in \mathcal{X}},{k \in {\{ 1,2,\ldots,2500\}}}$ arranged in a one-dimensional chain and two possible actions $\mathcal{A} = {\{{- 1},{+ 1}\}}$. In this problem, however, there is only one absorbing state (corresponding to the state *lock-opened*) with associated reward of $1$. This state is reached if the all-ones sequence $\{{+ 1},{+ 1},\ldots,{+ 1}\}$ is entered correctly. Otherwise, if at some state $x_{k}$, $k < 2500$, action $- 1$ is taken, the lock automatically resets to some previous state $x_{l}$, $l < k$ randomly (in the original combination lock problem, the reset state is always the initial state $x_{1}$).

<!-- chunk {"id": "body-0033", "role": "body", "section": "DPP-RL", "weight": 1.0} -->

For every intermediate state, the rewards of actions $- 1$ and $+ 1$ are set to $0$ and $- 0.01$, respectively. The transition probability upon taking the wrong action $- 1$ is, as before, inversely proportional to the distance of the states. That is Note that this problem is more difficult than the linear MDP since the goal state is only reachable from one state, $x_{2499}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "DPP-RL", "weight": 1.0} -->

This means that both the top-left absorbing state and the central state have the least possible reward ($- 1$), and that the remaining absorbing states have reward which increases proportionally to the distance to the state in the bottom-right corner (but are always negative).

<!-- chunk {"id": "body-0035", "role": "body", "section": "DPP-RL", "weight": 1.0} -->

The transition probabilities are defined in the following way: taking action $a$ from any non-absorbing state $x$ results in a one-step transition in the direction of action $a$ with probability $0.6$, and a random move to a state $y \neq x$ with probability inversely proportional to their Euclidean distance $1/\left\| {c_{x} - c_{y}} \right\|_{2}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "DPP-RL", "weight": 1.0} -->

The optimal policy then is to *survive* in the grid as long as possible by avoiding both the absorbing firewalls and the center of the grid. Note that because of the difference between the cost of firewalls, the optimal control prefers the states near the bottom-right corner of the grid, thus avoiding absorbing states with higher cost.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experimental Setup and Results", "weight": 1.0} -->

We describe now our experimental setting. The convergence properties of DPP-RL are compared with two other algorithms: a synchronous variant of Q-learning (QL), which, like DPP-RL, updates the action-value function of all state-action pairs at each iteration, and the model-based Q-value iteration (VI) of Kearns and Singh. VI is a batch reinforcement learning algorithm that first estimates the model using the whole data set and then performs value iteration on the learned model.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experimental Setup and Results", "weight": 1.0} -->

All algorithms are evaluated in terms of $\ell_{\infty}$-norm performance loss of the action-value function $\left\| {Q^{\ast} - Q^{\pi_{k}}} \right\|$ obtained by policy $\pi_{k}$ induced at iteration $k$. We choose this performance measure in order to be consistent with the performance measure used in Section 4. The discount factor $\gamma$ is fixed to $0.995$ and the optimal action-value function $Q^{\ast}$ is computed with high accuracy through value iteration.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experimental Setup and Results", "weight": 1.0} -->

We consider QL with polynomial learning step $\alpha_{k} = 1/{(k + 1)}^{\omega}$ where $\omega \in {\{ 0.51,0.75\}}$ and the linear learning step $\alpha_{k} = {1/{({k + 1})}}$. Note that $\omega$ needs to be larger than $0.5$, otherwise QL can asymptotically diverge.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experimental Setup and Results", "weight": 1.0} -->

To achieve the best rate of convergence for DPP-RL, we fix $\eta$ to $+ \infty$ (see Section 3.2). This replaces the soft-max operator $\mathcal{M}_{\eta}$ in the DPP-RL update rule with the max operator $\mathcal{M}$, resulting in a greedy policy $\pi_{k}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experimental Setup and Results", "weight": 1.0} -->

To have a fair comparison of the three algorithms, since each algorithm requires different number of computations per iteration, we fix the total computational budget of the algorithms to the same value for each benchmark. The computation time is constrained to $30$ seconds in the case of linear MDP and the combination lock problems. For the grid world, which has twice as many actions as the other benchmarks, the maximum run time is fixed to $60$ seconds. We also fix the total number of samples, per state-action, to $1 \times 10^{5}$ samples for all problems and algorithms. Significantly less number of samples leads to a dramatic decrease of the quality of the obtained solutions using all the approaches.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Experimental Setup and Results", "weight": 1.0} -->

Algorithms were implemented as MEX files (in C++) and ran on a Intel core i5 processor with 8 GB of memory. cpu time was acquired using the system function times which provides process-specific cpu time. Randomization was implemented using gsl_rng_uniform function of the GSL library, which is superior to the standard rand.^55^5 Sampling time, which is the same for all algorithms, were not included in cpu time.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Experimental Setup and Results", "weight": 1.0} -->

First, we see that DPP-RL converges very fast achieving near optimal performance after a few seconds. DPP-RL outperforms both QL and VI in all the three benchmarks. The minimum and maximum errors are attained for the linear MDP problem and the Grid world, respectively. We also observe that the difference between DPP-RL and QL is very significant, about two orders of magnitude, in both the linear MDP and the Combination lock problems. In the grid world DPP-RL's performance is more than $4$ times better than that of QL.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Experimental Setup and Results", "weight": 1.0} -->

QL shows the best performance for $\omega = 0.51$. The quality of the QL solution degrades as a function of $\omega$. Concerning VI, its error shows a sudden decrease on the first error caused by the model estimation.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Experimental Setup and Results", "weight": 1.0} -->

The standard deviations of the performance-loss give an indication of how robust are the solutions obtained by the algorithms. Table 1 shows the final numerical outcomes of DPP-RL, QL and VI (standard deviations between parenthesis). We can see that the variance of estimation of DPP-RL is substantially smaller than those of QL and VI.

<!-- chunk {"id": "body-0046", "role": "body", "section": "SADPP", "weight": 1.0} -->

In this subsection, we illustrate the performance of the SADPP algorithm in the presence of function approximation and limited sampling budget per iteration. We compare SADPP with a modification of regularized fitted $Q$-iteration (RFQI) which make use of a fixed number of basis functions. RFQI can be regarded as a Monte-Carlo sampling implementation of approximate value iteration with action-state representation. We compare SADPP with RFQI since both methods make use of $\ell_{2}$-regularization. The purpose of this subsection is to analyze numerically the sample complexity, i.e, the number of samples required to achieve a near optimal performance with a low variance, of SADPP. The benchmark we consider is a variant of the *optimal replacement problem* presented in Munos and Szepesvári. In the following subsection we describe the problem and subsequently we present the results.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Optimal replacement problem", "weight": 1.0} -->

This problem is an infinite-horizon, discounted MDP. The state measures the accumulated use of a certain product and is represented as a continuous, one-dimensional variable. At each time-step $t$, either the product is kept ${a{(t)}} = 0$ or replaced ${a{(t)}} = 1$. Whenever the product is replaced by a new one, the state variable is reset to zero ${x{(t)}} = 0$, at an additional cost $C$. The new state is chosen according to an exponential distribution, with possible values starting from zero or from the current state value, depending on the latest action: The reward function is a monotonically increasing function of the state $x$ if the product is kept ${r{(x,0)}} = {- {c{(x)}}}$ and constant if the product is replaced ${r{(x,1)}} = {{- C} - {c{}}}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Optimal replacement problem", "weight": 1.0} -->

The optimal action is to keep as long as the accumulated use is below a threshold or to replace otherwise: Following Munos and Szepesvári, $\overline{x}$ can be obtained exactly via the Bellman equation and is the unique solution to

<!-- chunk {"id": "body-0049", "role": "body", "section": "Experimental setup and results", "weight": 1.0} -->

For both SADPP and RFQI we map the state-action space using $20$ radial basis functions ($10$ for the continuous one-dimensional state variable $x$, spanning the state space $\mathcal{X}$, and $2$ for the two possible actions). Other parameter values where chosen to be the same as in Munos and Szepesvári, that is, ${\gamma = 0.6},{{\beta = 0.5},{C = 30}}$ and ${c{(x)}} = {4x}$, which results in $\overline{x} \simeq 4.8665$. We also fix an upper bound for the states, $x_{\max} = 10$ and modify the problem definition such that if the next state $y$ happens to be outside of the domain $\lbrack 0,x_{\max}\rbrack$ then the product is replaced immediately, and a new state is drawn as if action $a = 1$ were chosen in the previous time step.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Experimental setup and results", "weight": 1.0} -->

To compare both Algorithms we discretize the state space in $K = 100$ bins and use the following error measure: where $\hat{a}$ is the action selected by the Algorithm. Note that, unlike RFQI which selects the action by choosing the action with the highest action-value function, SADPP induces a stochastic policy, that is, a distribution over actions. We select $\hat{a}$ for SADPP by choosing the most probable action from the induced soft-max policy, and then use this to compute. Both algorithms were implemented in MatLab and executed under the same hardware specifications of the previous section.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Experimental setup and results", "weight": 1.0} -->

We analyze the effect of using different number of samples $N$ per iteration, $N \in {\{ 50,150,500\}}$.^66^6For both algorithms a new independent set of samples are generated at each iteration. The results are averages over $200$ runs, where at the beginning of each run the vector $\theta$ is initialized in the interval $\lbrack{- 1},1\rbrack$ for both algorithms. The rest of the parameters, including the regularization factor $\alpha$ and $\eta$, were optimized for the best asymptotic performance for each $N$ independently.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Discussion and Future Works", "weight": 1.5} -->

We have presented a new approach, dynamic policy programming (DPP), to compute the optimal policy in infinite-horizon discounted-reward MDPs. We have theoretically proven the convergence of DPP to the optimal policy for the tabular case. We have also provided performance-loss bounds for DPP in the presence of approximation. The bounds have been expressed in terms of supremum norm of average accumulated error as opposed to standard results for AVI and API which expressed in terms of supremum norm of the errors. We have then introduced a new incremental model-free RL algorithm, called DPP-RL, which relies on a sample estimate instance of DPP update rule to estimate the optimal policy. We have proven the asymptotic convergence of DPP-RL to the optimal policy and then have compared its, numerically, with the standard RL methods. Experimental results on various MDPs have been provided showing that, in all cases, DPP-RL is superior to other RL methods in terms of convergence rate.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Discussion and Future Works", "weight": 1.5} -->

This may be due to the fact that DPP-RL, unlike other incremental RL methods, does not rely on stochastic approximation for estimating the optimal policy and therefore it does not suffer from the slow convergence caused by the presence of the decaying learning step in stochastic approximation.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Discussion and Future Works", "weight": 1.5} -->

In this work, we are only interested in the estimation of the optimal policy and not the problem of exploration. Therefore, we have not compared our algorithms to the PAC-MDP methods, in which the choice of the exploration policy impacts the behavior of the learning algorithm. Also, in this paper, we have not compared our results with those of (PG)AC since they rely on a different kind of sampling strategy: Both DPP-RL and SADPP rely on a generative model for sampling, whereas AC makes use of some trajectories of the state-action pairs, generated by Monte-Carlo simulation, to estimate the optimal policy.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Discussion and Future Works", "weight": 1.5} -->

In this study, we provide $\ell_{\infty}$-norm performance-loss bounds for approximate DPP. However, most supervised learning and regression algorithms rely on minimizing some form of $\ell_{p}$-norm error. Therefore, it is natural to search for a kind of performance bound that relies on the $\ell_{p}$-norm of approximation error. Following Munos, $\ell_{p}$-norm bounds for approximate DPP can be established by providing a bound on the performance loss of each component of value function under the policy induced by DPP. This would be a topic for future research.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Discussion and Future Works", "weight": 1.5} -->

Another direction for future work is to provide finite-sample *probably approximately correct* (PAC) bounds for SADPP and DPP-RL in the spirit of previous theoretical results available for fitted value iteration and fitted $Q$-iteration. In the case of SADPP, this would require extending the error propagation result of Theorem 4 ‣ 4.1 The ℓ_∞-norm performance-loss bounds for approximate DPP ‣ 4 Dynamic Policy Programming with Approximation ‣ Dynamic Policy Programming") to an $\ell_{2}$-norm analysis and combining it with the standard regression bounds.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Discussion and Future Works", "weight": 1.5} -->

Finally, an important extension of our results would be to apply DPP for large-scale action problems. In that case, we need an efficient way to approximate $\mathcal{M}_{\eta}\Psi_{k}{(x)}$ in update rule since computing the exact summations become expensive. One idea is to sample estimate $\mathcal{M}_{\eta}\Psi_{k}{(x)}$ using Monte-Carlo simulation, since $\mathcal{M}_{\eta}\Psi_{k}{(x)}$ is the expected value of $\Psi_{k}{(x,a)}$ under the soft-max policy $\pi_{k}$.
