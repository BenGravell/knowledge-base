<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Model-Free Linear Quadratic Control via Reduction to Expert Prediction

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Model-free approaches for reinforcement learning (RL) and continuous control find policies based only on past states and rewards, without fitting a model of the system dynamics. They are appealing as they are general purpose and easy to implement; however, they also come with fewer theoretical guarantees than model-based RL. In this work, we present a new model-free algorithm for controlling linear quadratic (LQ) systems, and show that its regret scales as O(T^(xi)+2/3) for any small xi > 0 if time horizon satisfies T > C^/xi for a constant C. The algorithm is based on a reduction of control of Markov decision processes to an expert prediction problem. In practice, it corresponds to a variant of policy iteration with forced exploration, where the policy in each phase is greedy with respect to the average of all previous value functions. This is the first model-free algorithm for adaptive control of LQ systems that provably achieves sublinear regret and has a polynomial computation cost. Empirically, our algorithm dramatically outperforms standard policy iteration, but performs worse than a model-based approach.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reinforcement learning (RL) algorithms have recently shown impressive performance in many challenging decision making problems, including game playing and various robotic tasks. *Model-based* RL approaches estimate a model of the transition dynamics and rely on the model to plan future actions using approximate dynamic programming. *Model-free* approaches aim to find an optimal policy without explicitly modeling the system transitions; they either estimate state-action value functions or directly optimize a parameterized policy based only on interactions with the environment. Model-free RL is appealing for a number of reasons: 1) it is an "end-to-end" approach, directly optimizing the cost function of interest, 2) it avoids the difficulty of modeling and robust planning, and 3) it is easy to implement. However, model-free algorithms also come with fewer theoretical guarantees than their model-based counterparts, which presents a considerable obstacle in deploying them in real-world physical systems with safety concerns and the potential for expensive failures.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we propose a model-free algorithm for controlling linear quadratic (LQ) systems with theoretical guarantees. LQ control is one of the most studied problems in control theory, and it is also widely used in practice. Its simple formulation and tractability given known dynamics make it an appealing benchmark for studying RL algorithms with continuous states and actions. A common way to analyze the performance of sequential decision making algorithms is to use the notion of regret - the difference between the total cost incurred and the cost of the best policy in hindsight. We show that our model-free LQ control algorithm enjoys a $O{(T^{\xi + {2/3}})}$ regret bound. Note that existing regret bounds for LQ systems are only available for model-based approaches.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our algorithm is a modified version of policy iteration with exploration similar to $\epsilon$-greedy, but performed at a fixed schedule. Standard policy iteration estimates the value of the current policy in each round, and sets the next policy to be greedy with respect to the most recent value function. By contrast, we use a policy that is greedy with respect to the *average of all past value functions* in each round. The form of this update is a direct consequence of a reduction of the control of Markov decision processes (MDPs) to expert prediction problems. In this reduction, each prediction loss corresponds to the value function of the most recent policy, and the next policy is the output of the expert algorithm. The structure of the LQ control problem allows for an easy implementation of this idea: since the value function is quadratic, the average of all previous value functions is also quadratic.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

One major challenge in this work is the finite-time analysis of the value function estimation error. Existing finite-sample results either consider bounded functions or discounted problems, and are not applicable in our setting. Our analysis relies on the contractiveness of stable policies, as well as the fact that our algorithm takes exploratory actions. Another challenge is showing boundedness of the value functions in our iterative scheme, especially considering that the state and action spaces are unbounded. We are able to do so by showing that the policies produced by our algorithm are stable assuming a sufficiently small estimation error.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our main contribution is a model-free algorithm for adaptive control of linear quadratic systems with strong theoretical guarantees. This is the first such algorithm that provably achieves sublinear regret and has a polynomial computation cost. The only other computationally efficient algorithm with sublinear regret is the model-based approach of Dean et al. (which appeared in parallel to this work). Previous works have either been restricted to one-dimensional LQ problems, or have considered the problem in a Bayesian setting. In addition to theoretical guarantees, we demonstrate empirically that our algorithm leads to significantly more stable policies than standard policy iteration.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Linear quadratic control", "weight": 1.0} -->

In a linear quadratic control problem, the state transition dynamics and the cost function are given by

<!-- chunk {"id": "body-0009", "role": "body", "section": "Linear quadratic control", "weight": 1.0} -->

The state space is $\mathcal{X} = {\mathbb{R}}^{n}$ and the action space is $\mathcal{A} = {\mathbb{R}}^{d}$. We assume the initial state is zero, $x_{1} = 0$. $A$ and $B$ are unknown dynamics matrices of appropriate dimensions, assumed to be controllable^11^1The linear system is controllable if the matrix $({BAB\cdotsA^{n - 1}B})$ has full column rank.. $M$ and $N$ are known positive definite cost matrices. Vectors $w_{t + 1}$ correspond to system noise; similarly to previous work, we assume that $w_{t}$ are drawn i.i.d. from a known Gaussian distribution $\mathcal{N}{(0,W)}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Linear quadratic control", "weight": 1.0} -->

In the infinite horizon setting, it is well-known that the optimal policy $\pi_{\ast}{(x)}$ corresponding to the lowest average cost $\lambda_{\pi}$ is given by constant linear state feedback, ${\pi_{\ast}{(x)}} = {- {K_{\ast}x}}$. When following any linear feedback policy ${\pi{(x)}} = {- {Kx}}$, the system states evolve as $x_{t + 1} = {{{({A - {BK}})}x_{t}} + w_{t + 1}}$. A linear policy is called *stable* if ${\rho{({A - {BK}})}} < 1$, where $\rho{( \cdot )}$ denotes the spectral radius of a matrix.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Linear quadratic control", "weight": 1.0} -->

It is well-known that the value function $V_{\pi}$ and state-action value function $Q_{\pi}$ of any stable linear policy ${\pi{(x)}} = {- {Kx}}$ are quadratic functions (see e.g. Abbasi-Yadkori et al.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Linear quadratic control", "weight": 1.0} -->

where $H_{\pi} \succ 0$ and $G_{\pi} \succ 0$. We call $H_{\pi}$ the value matrix of policy $\pi$. The matrix $G_{\pi}$ is the unique solution of the equation

<!-- chunk {"id": "body-0013", "role": "body", "section": "Linear quadratic control", "weight": 1.0} -->

The greedy policy with respect to $Q_{\pi}$ is given by

<!-- chunk {"id": "body-0014", "role": "body", "section": "Linear quadratic control", "weight": 1.0} -->

Here, $G_{\pi,{ij}}$ for ${i,j} \in {\{ 1,2\}}$ refers to $(i,j)$'s block of matrix $G_{\pi}$ where block structure is based on state and action dimensions. The average expected cost of following a linear policy is $\lambda_{\pi} = {\operatorname{tr}{({H_{\pi}W})}}$. The stationary state distribution of a stable linear policy is ${\mu_{\pi}{(x)}} = {\mathcal{N}{(\left. x \middle| {0,\Sigma} \right.)}}$, where $\Sigma$ is the unique solution of the Lyapunov equation

<!-- chunk {"id": "body-0015", "role": "body", "section": "Model-free control of LQ systems", "weight": 1.0} -->

Our model-free linear quadratic control algorithm (MFLQ) is shown in algorithm 1, where v1 and v2 indicate different versions. At a high level, MFLQ is a variant of policy iteration with a deterministic exploration schedule. We assume that an initial stable suboptimal policy ${\pi_{1}{(x)}} = {- {K_{1}x}}$ is given. During phase $i$, we first execute policy $\pi_{i}$ for a fixed number of rounds, and compute a value function estimate ${\hat{V}}_{i}$. We then estimate $Q_{i}$ from ${\hat{V}}_{i}$ and a dataset $\mathcal{Z} = {\{{(x_{t},a_{t},x_{t + 1})}\}}$ which includes exploratory actions.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Model-free control of LQ systems", "weight": 1.0} -->

We set $\pi_{i + 1}$ to the greedy policy with respect to the average of all previous estimates ${\hat{Q}}_{1},\ldots,{\hat{Q}}_{i}$. This step is different than standard policy iteration (which only considers the most recent value estimate), and a consequence of using the Follow-the-Leader expert algorithm.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Model-free control of LQ systems", "weight": 1.0} -->

The dataset $\mathcal{Z}$ is generated by executing the policy and taking a random action every $T_{s}$ steps. In MFLQv1, we generate $\mathcal{Z}$ at the beginning, and reuse it in all phases, while in v2 we generate a new dataset $\mathcal{Z}$ in each phase following the execution of the policy. While MFLQ as described stores long trajectories in each phase, this requirement can be removed by updating parameters of $V_{i}$ and $Q_{i}$ in an online fashion. However, in the case of MFLQv1, we need to store the dataset $\mathcal{Z}$ throughout (since it gets reused), so this variant is more memory demanding.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Model-free control of LQ systems", "weight": 1.0} -->

MFLQ (stable policy π1, trajectory length T, initial state x0, exploration covariance Σa)
Execute πi for Tv rounds and compute V̂i using
Compute Q̂i from 𝒵 and V̂i using

<!-- chunk {"id": "body-0019", "role": "body", "section": "Model-free control of LQ systems", "weight": 1.0} -->

CollectData (policy π, traj. length τ, exploration period s, covariance Σa):
Execute the policy π for s − 1 rounds and let x be the final state
Sample a ∼ 𝒩 (0,Σa), observe next state x+, add (x,a,x+) to 𝒵

<!-- chunk {"id": "body-0020", "role": "body", "section": "Model-free control of LQ systems", "weight": 1.0} -->

Assume the initial policy is stable and let $C_{1}$ be the norm of its value matrix. Our main result are the following two theorems.

<!-- chunk {"id": "body-0021", "role": "body", "section": "State value function", "weight": 1.0} -->

In this section, we study least squares temporal difference (LSTD) estimates of the value matrix $H_{\pi}$. In order to simplify notation, we will drop $\pi$ subscripts in this section.

<!-- chunk {"id": "body-0022", "role": "body", "section": "State value function", "weight": 1.0} -->

By multiplying both sides with $\phi_{t}$ and taking expectations with respect to the steady state distribution,

<!-- chunk {"id": "body-0023", "role": "body", "section": "State value function", "weight": 1.0} -->

We estimate $H$ from data generated by following the policy for $\tau$ rounds. Let $\Phi$ be a $\tau \times n^{2}$ matrix whose rows are vectors $\phi_{1},\ldots,\phi_{\tau}$, and similarly let $\Phi_{+}$ be a matrix whose rows are $\phi_{2},\ldots,\phi_{\tau + 1}$. Let $\mathbf{W}$ be a $\tau \times n^{2}$ matrix whose each row is $\text{vec}{(W)}$. Let $\mathbf{c} = {\lbrack c_{1},\ldots,c_{\tau}\rbrack}^{\top}$. The LSTD estimator of $H$ is given by (see e.g.

<!-- chunk {"id": "body-0024", "role": "body", "section": "State value function", "weight": 1.0} -->

where ${(.)}^{\dagger}$ denotes the pseudo-inverse. Given that $H \succ M$, we project our estimate onto the constraint $\hat{H} \succ M$. Note that this step can only decrease the estimation error, since an orthogonal projection onto a closed convex set is contractive.

<!-- chunk {"id": "body-0025", "role": "body", "section": "State value function", "weight": 1.0} -->

Remark. Since the average cost $\operatorname{tr}{({WH})}$ cannot be computed from value function parameters $H$ alone, assuming known noise covariance $W$ seems necessary.

<!-- chunk {"id": "body-0026", "role": "body", "section": "State-action value function", "weight": 1.0} -->

Let $z^{\top} = {(x^{\top},a^{\top})}$, and let $\psi = {\text{vec}{({zz^{\top}})}}$. The state-action value function corresponds to the cost of deviating from the policy, and satisfies

<!-- chunk {"id": "body-0027", "role": "body", "section": "State-action value function", "weight": 1.0} -->

We estimate $G$ based on the above equation, using the value function estimate $\hat{H}$ of the previous section in place of $H$ and randomly sampled actions. Let $\Psi$ be a $\tau \times {({n + d})}^{2}$ matrix whose rows are vectors $\psi_{1},\ldots,\psi_{\tau}$, and let $\mathbf{c} = {\lbrack c_{1},\ldots,c_{\tau}\rbrack}^{\top}$ be the vector of corresponding costs. Let $\Phi_{+}$ be the $\tau \times n^{2}$ matrix containing the next-state features after each random action, and let ${\overline{\Phi}}_{+}$ be its expectation.

<!-- chunk {"id": "body-0028", "role": "body", "section": "State-action value function", "weight": 1.0} -->

and additionally project the estimate onto the constraint $\hat{G} \succeq {(\begin{matrix}

<!-- chunk {"id": "body-0029", "role": "body", "section": "State-action value function", "weight": 1.0} -->

To gather appropriate data, we iteratively execute the policy $\pi$ for $T_{s}$ iterations in order to get sufficiently close to the steady-state distribution,^22^2Note that stable linear systems mix exponentially fast; see Tu and Recht for details. sample a random action $a \sim {\mathcal{N}{(0,\Sigma_{a})}}$, observe the cost $c$ and next state $x_{+}$, and add the tuple $(x,a,x_{+})$ to our dataset $\mathcal{Z}$. We collect $\tau = {0.5T^{{1/2} + \xi}}$ such tuples in each phase of MFLQv2, and $\tau = T^{{2/3} + \xi}$ such tuples in the first phase of MFLQv1.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Analysis of the MFLQ algorithm", "weight": 1.0} -->

In this section, we first show that given sufficiently small estimation errors, all policies produced by the MFLQ algorithm remain stable. Consequently the value matrices, states, and actions remain bounded. We then bound the terms $\alpha_{T}$, $\beta_{T}$, and $\gamma_{T}$ to show the main result. For simplicity, we will assume that $M \succ I$ and $N \succ I$ for the rest of this section; we can always rescale $M$ and $N$ so that this holds true without loss of generality. We analyze MFLQv2; the analysis of MFLQv1 is similar and obtained by a different choice of constants.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Analysis of the MFLQ algorithm", "weight": 1.0} -->

By assumption, $K_{1}$ is bounded and stable. By the arguments in Section 4, the estimation error in the first phase can be made small for sufficiently long phases. In particular, we assume that estimation error in each phase is bounded by $\varepsilon_{1}$ as in Equation (4.2) and that $\varepsilon_{1}$ satisfies

<!-- chunk {"id": "body-0032", "role": "body", "section": "Analysis of the MFLQ algorithm", "weight": 1.0} -->

Here $C_{1} > 1$ is an upper bound on $\left\| H_{1} \right\|$, and $C_{K} = {2{({{3C_{1}\left\| B \right\|\left\| A \right\|} + 1})}}$. Since we take $S^{2}T^{\xi}$ random actions in the first phase, the error factor $S^{- 1}$ is valid as long as $T > {\overline{C}}^{1/\xi}$ for a constant $\overline{C}$ that can be derived from (4.2) and. We prove the following lemma in Appendix B.1.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate our algorithm on two LQ problem instances: the system studied in Dean et al. and Tu and Recht, and the power system studied in Lewis et al., Example 11.5-1, with noise $W = I$. We start all experiments from an all-zero initial state $x_{0} = 0$, and set the initial stable policy $K_{1}$ to the optimal controller for a system with a modified cost $M^{\prime} = {200M}$. For simplicity we set $\xi = 0$ and $T_{s} = 10$ for MFLQv1. We set the exploration covariance to $\Sigma_{a} = I$ for and $\Sigma_{a} = {10I}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments", "weight": 1.0} -->

In addition to the described algorithms, we also evaluate MFLQv3, an algorithm identical to MFLQv2 except that the generated datasets $\mathcal{Z}$ include all data, not just random actions.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiments", "weight": 1.0} -->

Least squares policy iteration (LSPI) where the policy $\pi_{i}$ in phase $i$ is greedy with respect to the most recent value function estimate ${\hat{Q}}_{i - 1}$. We use the same estimation procedure as for MFLQ.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiments", "weight": 1.0} -->

A version RLSVI Osband et al. where we randomize the value function parameters rather than taking random actions. In particular, we update the mean $\mu_{Q}$ and covariance $\Sigma_{Q}$ of a TD estimate of $G$ after each step, and switch to a policy greedy w.r.t. a parameter sample $\hat{G} \sim {(\mu_{Q},{0.2\Sigma_{Q}})}$ every $T^{1/2}$ steps. We project the sample onto the constraint $G \succ \begin{pmatrix}

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiments", "weight": 1.0} -->

A model-based approach which estimates the dynamics parameters $(\hat{A},\hat{B})$ using ordinary least squares. The policy at the end of each phase is produced by treating the estimate as the true parameters (this approach is called *certainty equivalence* in optimal control). We use the same strategy as in the model-free case, i.e. we execute the policy for some number of iterations, followed by running the policy and taking random actions.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experiments", "weight": 1.0} -->

To evaluate stability, we run each algorithm 100 times and compute the fraction of times it produces stable policies in all phases. Figure 1 (left) shows the results as a function of trajectory length. MFLQv3 is the most stable among model-free algorithms, with performance comparable to the model-based approach.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate solution cost by running each algorithm until we obtain 100 stable trajectories (if possible), where each trajectory is of length 50,000. We compute both the average cost incurred during each phase $i$, and true expected cost of each policy $\pi_{i}$. The average cost at the end of each phase is shown in Figure 1 (center and right). Overall, MFLQv2 and MFLQv3 achieve lower costs than MFLQv1, and the performance of MFLQv1 and LSPI is comparable. The lowest cost is achieve by the model-based approach. These results are consistent with the empirical findings of Tu and Recht, where model-based approaches outperform discounted LSTDQ.

<!-- chunk {"id": "body-0040", "role": "body", "section": "DISCUSSION", "weight": 1.5} -->

The simple formulation and wide practical applicability of LQ control make it an idealized benchmark for studying RL algorithms for continuous-valued states and actions. In this work, we have presented MFLQ, an algorithm for model-free control of LQ systems with an $O{(T^{{2/3} + \xi})}$ regret bound. Empirically, MFLQ considerably improves the performance of standard policy iteration in terms of both solution stability and cost, although it is still not cost-competitive with model-based methods.

<!-- chunk {"id": "body-0041", "role": "body", "section": "DISCUSSION", "weight": 1.5} -->

Our algorithm is based on a reduction of control of MDPs to an expert prediction problem. In the case of LQ control, the problem structure allows for an efficient implementation and strong theoretical guarantees for a policy iteration algorithm with exploration similar to $\epsilon$-greedy (but performed at a fixed schedule). While $\epsilon$-greedy is known to be suboptimal in unstructured multi-armed bandit problems, it has been shown to achieve near optimal performance in problems with special structure, and it is worth considering whether it applies to other structured control problems. However, the same approach might not generalize to other domains. For example, Boltzmann exploration may be more appropriate for MDPs with finite states and actions. We leave this issue, as well as the application of $\epsilon$-greedy exploration to other structured control problems, to future work.
