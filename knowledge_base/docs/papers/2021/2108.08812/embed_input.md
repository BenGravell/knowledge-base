<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Provable Benefits of Actor-Critic Methods for Offline Reinforcement Learning

Topics include Low-rank models, Reinforcement learning, Bellman equations, Offline algorithms, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Actor-critic methods are widely used in offline reinforcement learning practice, but are not so well-understood theoretically. We propose a new offline actor-critic algorithm that naturally incorporates the pessimism principle, leading to several key advantages compared to the state of the art. The algorithm can operate when the Bellman evaluation operator is closed with respect to the action value function of the actor's policies; this is a more general setting than the low-rank MDP model. Despite the added generality, the procedure is computationally tractable as it involves the solution of a sequence of second-order programs. We prove an upper bound on the suboptimality gap of the policy returned by the procedure that depends on the data coverage of any arbitrary, possibly data dependent comparator policy. The achievable guarantee is complemented with a minimax lower bound that is matching up to logarithmic factors.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The problem of learning a near-optimal policy is a core challenge in reinforcement learning (RL). In many settings, it is beneficial to be able to learn a good policy using only a pre-collected set of data, without further exploration with the environment; this problem is known as *offline or batch policy learning*. The offline setting has unique challenges due to the incomplete information about the Markov decision process (MDP) encoded in the available dataset. For example, due to maximization bias, a naive offline algorithm can return a policy with a severely overestimated value. In order to avoid such undesirable behavior, researchers have introduced the idea of pessimism under uncertainty, and there is now a growing literature (e.g., \[ YTY^+^20\]) on different ways in which pessimism can be incorporated. See Appendix A for additional references and discussion of this body of work.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

At a high level, incorporating pessimism prevents algorithms from settling down on uncertain policies whose value might be misleadingly high under the current dataset due to statistical errors. By using pessimism, uncertain policies are penalized in such a way that only those policies robust to statistical errors are returned. The principle can be implemented in at least two different ways: (a) by penalizing policies that are far from the one that generated the dataset; or (b) by penalizing the value functions of policies not well covered by the dataset. In this paper, we take the latter avenue.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Overview and our contributions", "weight": 1.0} -->

Implementing pessimism with function approximation is challenging for several reasons. First, uncertainty must be estimated with particular care. On one hand, underestimating it can fail to correct the coverage problem. On the other hand, overestimating it leads to policies that are too conservative and thus underperform. Second, the incorporation of pessimism may introduce complex, higher order perturbations into the value function class handled by the algorithm. Similar issues can arise when adding optimistic bonuses in the exploration. The increased complexity of the function class often requires additional assumptions on the model, because the new class needs to interact "nicely" with the Bellman operator. Prior art on pessimism with function approximation has by-passed this problem by making strong model assumptions, such as low-rank transitions or algorithm-specific assumptions.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Actor-critic methods", "weight": 1.0} -->

Most past theoretical work on offline reinforcement learning on finding with high probability the policy with the highest performance has focused on algorithms that are either model or value-based^11^1Exceptions to this include importance-sampling based approaches to selecting among a finite set of policies (e.g. \[MLL^+^14 TdSB^+^19\]); however, such approaches have focused on operating without a Markov assumption and inherently provide much looser guarantees than the ones we and others consider for the Markov setting. \[ YTY^+^20\]; these often incorporate pessimism into the estimates of the policy performance. Actor-critic methods are a hybrid class of methods that mitigate some deficiencies of methods that are either purely policy or purely value-based \[ HWS^+^15 \]; in modern RL, they are widely used in practice (e.g., \[ WZS^+^21 \]). An actor-critic method generally consists of an actor that changes the policy in order to maximize its value as estimated by the critic.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Actor-critic methods", "weight": 1.0} -->

Given their popularity, it is natural to ask the following question: *do actor-critic methods provably offer any advantage in offline RL?* The main contribution of this paper is to give a positive answer to this question: by separating the policy optimization from the policy evaluation, both tasks become simpler to design and the pessimism principle can be incorporated more naturally.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Contributions", "weight": 1.0} -->

More specifically, we study the problem of policy learning using linear function approximation in the offline setting. We assume that we are given a batch data set $\mathcal{D}$, in which each sample consists of a quadruple. The first two components are the state-action pair, corresponding to the state in which a given action was taken, and the last two components correspond to a noisy observation of the reward, and a successor state drawn from the appropriate transition function. Our theory allows for a very general dependence structure among the the state-action pairs in these samples; when the data set is ordered according to how the samples were collected (which need not be related to a trajectory), we allow the state-action pair at any given instant to depend on all past samples. This set-up allows from data collected from arbitrary policies, mixtures of policies, generative models or even in adversarial manner.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Contributions", "weight": 1.0} -->

Given such a data set, our objective is to find the policy that performs best in the face of uncertainty. In particular, we need to account for the fact that the optimal policy $\pi^{\ast}$ for the underlying MDP may not be well covered by the dataset $\mathcal{D}$, in which case the associated uncertainty would be prohibitive. In order to achieve this goal, we design an actor-critic procedure that iteratively optimizes a lower bound on the value of the optimal policy. Suppose that we are interested in optimizing the value function at some given initial $s_{1}$. Our strategy works as follows: for any given policy $\pi$, we construct a family $\mathcal{M}{(\pi)}$ of "statistically plausible" MDPs, and use them to define a simple second-order cone program.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Contributions", "weight": 1.0} -->

By solving this convex program, we obtain value function estimate ${{\underset{¯}{V}}_{M}^{\pi}{(s_{1})}} = {{\arg{\min_{M \in {\mathcal{M}{(\pi)}}}V_{M}^{\pi}}}{(s_{1})}}$ that---for an appropriately constructed family $\mathcal{M}{(\pi)}$---is guaranteed to be a lower bound on the true value function of $\pi$ in the unknown MDP that generated the dataset. Given a procedure for producing such lower bounds, it is then natural to maximize these lower bounds over some family $\Pi$ of policies. This combination leads to the saddle-point problem

<!-- chunk {"id": "body-0011", "role": "body", "section": "Contributions", "weight": 1.0} -->

Note that actor-critic methods fit naturally in this framework: the critic provides a pessimistic evaluation of any given policy $\pi$, and the actor solves the outer maximization problem over policies. This decoupling lends itself to a computationally tractable implementation, along with an analysis of the procedure. In particular, we show that the actor's sequence of estimated policies enjoys online learning-style guarantees with respect to a sequence of pessimistic MDPs implicitly identified by the critic.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Contributions", "weight": 1.0} -->

The way in which we introduce pessimism is a second key component of the algorithmic framework. In particular, in line with our previous paper, we do so without enlarging the prescribed classes of functions and policies. We do so by a direct perturbation of the value functions examined by the critic; there is no addition of pessimistic bonuses or absorbing states. Since the class of value functions is not altered, this method has two main advantages. First, there are no additional model assumptions compared to the standard---that is non-pessimistic---version of the actor-critic method. Second, the complexity of the underlying classes is not increased, thereby allowing us to construct tight confidence intervals and estimation error bounds that are minimax optimal up to logarithmic factors.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Contributions", "weight": 1.0} -->

The remainder of this paper is organized as follows. We begin in Section 2 with background on MDPS, and then introduce the modeling assumptions that underlie the analysis of this paper. In Section 3, we introduce the algorithm studied in this paper, namely the Pessimistic Actor Critic for Learning without Exploration (for short, Pacle) algorithm. Section 4 provides statements of our main results and discussion of their consequences, including an upper bound on the Pacle algorithm in Theorem 1. ‣ 4.1 A guarantee for PACLE ‣ 4 Main results"), and a minimax lower bound in Theorem 2. ‣ 4.2 A lower bound ‣ 4 Main results"). In Section 5, we provide an outline of the proof of Theorem 1. ‣ 4.1 A guarantee for PACLE ‣ 4 Main results"), with various technical details as well as the proof of Theorem 2. ‣ 4.2 A lower bound ‣ 4 Main results") deferred to the appendices. We conclude with a discussion in Section 6.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Markov decision processes", "weight": 1.0} -->

In this paper, we focus on finite-horizon Markov decision processes, for which we provide a very brief introduction here. See the books for more background and detail. A finite-horizon MDP is specified by a positive integer $H$, and events take place over a sequence of stages indexed by the time step $h \in {\lbrack H\rbrack}\overset{def}{=}{\{ 1,\ldots,H\}}$. The underlying dynamics involve a state space $\mathcal{S}$, and are controlled by actions that take values in some action set $\mathcal{A}$. In this paper, we allow the state space to be arbitrary (continous or discrete), whereas our analysis applies to discrete action spaces.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Markov decision processes", "weight": 1.0} -->

For each time step $h \in {\lbrack H\rbrack}$, there is a reward function $r_{h}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$, and for every time step $h$ and state-action pair $(s,a)$, there is a transition function ${\mathbb{P}}_{h}{( \cdot \mid s,a)}$. When at horizon $h$, if the agent takes action $a$ in state $s$, it receives a random reward drawn from a distribution $R_{h}{(s,a)}$ with mean $r_{h}{(s,a)}$, and it then transitions randomly to a next state $s^{+}$ drawn from the transition function ${\mathbb{P}}_{h}{( \cdot \mid s,a)}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Markov decision processes", "weight": 1.0} -->

A policy $\pi_{h}$ at stage $h$ is a mapping from the state space $\mathcal{S}$ to the action space $\mathcal{A}$. Given a full policy $\pi = {(\pi_{1},\ldots,\pi_{H})}$, the state-action value function at time step $h$ is given by

<!-- chunk {"id": "body-0017", "role": "body", "section": "Markov decision processes", "weight": 1.0} -->

where the expectation is over the trajectories induced by $\pi$ upon starting from the pair $(s,a)$. When we omit the starting state-action pair $(s,a)$, the expectation is intended to start from a fixed state denoted by $s_{1}$. The value function associated to $\pi$ is ${V_{h}^{\pi}{(s)}} = {Q_{h}^{\pi}{(s,{\pi_{h}{(s)}})}}$. For a given policy $\pi$, we define the Bellman evaluation operator

<!-- chunk {"id": "body-0018", "role": "body", "section": "Markov decision processes", "weight": 1.0} -->

Under some regularity conditions, there always exists an optimal policy $\pi^{\star}$ whose value and action-value functions are defined as

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 1 (Data generation)", "weight": 1.0} -->

Note that the measurability condition allows the choice of $(s_{i},a_{i})$ to depend arbitrarily on any of the past data with indices $j < i$. The mild assumption allows for considerable freedom. For example, the state-action pairs may be chosen from (mixture) policies, or they can be generated by an adversarial procedure that changes the data acquisition strategy as feedback is received.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Policy and function classes", "weight": 1.0} -->

Next we define the policy space $\Pi$ and the action value function space $\mathcal{Q}$ over which we seek solutions. Let $\phi:{{\mathcal{S} \times \mathcal{A}}\mapsto{\mathbb{R}}^{d}}$ be a $d$-dimensional feature mapping. We assume throughout that these feature mappings are normalized such that ${\|{\phi{(s,a)}}\|}_{2} \leq 1$ uniformly for all $(s,a)$-pairs. We consider action-value functions that are linear in $\phi$, and families of the form

<!-- chunk {"id": "body-0021", "role": "body", "section": "Policy and function classes", "weight": 1.0} -->

where $\rho^{\theta} > 0$ is a second radius.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Policy and function classes", "weight": 1.0} -->

In the context of our actor-critic algorithm, the weight radius $\rho^{w}$ remains fixed for all updates. On the other hand, the actor produces a sequence of soft-max radii ${\{\rho_{t}^{\theta}\}}_{t = 1}^{T}$, indexed by the iterations $t$ of the actor. This sequence is produced via the update rule in Line 5 of Algorithm 1. The policy radius can be large $\rho^{\theta} \gg 1$ but we constrain $\rho^{w} \leq 1$ so that the critic's estimate ${Q_{w}{(s,a)}} = \left\langle {\phi{(s,a)}},w \right\rangle$ is bounded by one, i.e., ${\sup_{(s,a,w)}{|{Q_{w}{(s,a)}}|}} \leq 1$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Policy and function classes", "weight": 1.0} -->

Recall that our MDP consists of sequence of $H$ distinct stages. Our algorithm and theory allows for the possibility of different feature extractors at each step $h \in {\lbrack H\rbrack}$, even with possibly different dimensions. Consequently, in implementing and analyzing the algorithm, there are actually $H$ (possibly different) functional spaces ${\{\mathcal{Q}_{h}\}}_{h = 1}^{H}$, along with the associated soft-max policy classes ${\{\Pi_{h}\}}_{h = 1}^{H}$. So as to simplify notation, we drop the dependence on the radii when referring to the functional spaces, and implicitly assume that the terminal value function is zero.

<!-- chunk {"id": "body-0024", "role": "body", "section": "A range of function class assumptions", "weight": 1.0} -->

In this section, we discuss a range of assumptions that might be imposed on the class of action-value functions. This discussion serves as motivation for the particular assumption (Bellman restricted closedness---cf. Assumption 3. ‣ 2.4 A range of function class assumptions ‣ 2 Background and problem formulation")) that underlies our analysis.

<!-- chunk {"id": "body-0025", "role": "body", "section": "A range of function class assumptions", "weight": 1.0} -->

We begin with the least restrictive condition, which is a very natural starting point in our given set-up. If we seek to find the policy $\pi \in \Pi$ with the highest value function, it seems reasonable to require that the following representation condition (approximately) holds.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Assumption 2 (Linear action-value functions $Q^{\\pi}$)", "weight": 1.0} -->

The MDP admits a linear action-value function representation for all policies in $\Pi$, meaning that for each policy $\pi \in \Pi$ and time step $h \in {\lbrack H\rbrack}$, there exists a vector $w_{h}^{\pi}$ such that

<!-- chunk {"id": "body-0027", "role": "body", "section": "Assumption 2 (Linear action-value functions $Q^{\\pi}$)", "weight": 1.0} -->

This assumption alone turns out to be inadequate to ensure that effective learning is possible; indeed, the recent papers establish that even under this condition, there are instances that require exponentially many samples to do better than a random policy.\

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 2 (Linear action-value functions $Q^{\\pi}$)", "weight": 1.0} -->

Given this fact, if one is interested in procedures with polynomial complexity (in both sample size and running time), stronger conditions need to be imposed. In general, the Bellman evaluation operator, even when applied to a linear action-value function, will return a nonlinear value function.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumption 3 (Bellman Restricted Closedness)", "weight": 1.0} -->

The policy and value function spaces $(\Pi,\mathcal{Q})$ are closed up to $\nu \in {\mathbb{R}}^{H}$ error in the sup-norm if there is a non-negative sequence ${\{\nu_{h}\}}_{h = 1}^{H}$ such that for each $h \in {\lbrack H\rbrack}$, we have

<!-- chunk {"id": "body-0030", "role": "body", "section": "Assumption 3 (Bellman Restricted Closedness)", "weight": 1.0} -->

The restricted closedness assumption measures how well we can fit the action-value function resulting from the application of the Bellman evaluation operator to an action value function in $\mathcal{Q}$ and for a policy in $\Pi$. It enables the analysis of least-squares policy evaluation (e.g., ), which will be our starting point when constructing the critic.\

<!-- chunk {"id": "body-0031", "role": "body", "section": "Assumption 3 (Bellman Restricted Closedness)", "weight": 1.0} -->

Finally, for understanding connections to past work, it is relevant to compare to the *low-rank MDP* assumption that has been analyzed in recent work, including in offline RL with pessimismistic guarantees, as well as in various online settings \[, MCK^+^21, \].

<!-- chunk {"id": "body-0032", "role": "body", "section": "Assumption 4 (Low-Rank MDP)", "weight": 1.0} -->

The following proposition explicates the nested relationship between these three conditions, showing that the low-rank MDP condition is the most restrictive:\

<!-- chunk {"id": "body-0033", "role": "body", "section": "The Pessimistic Actor-Critic", "weight": 1.0} -->

Given the set-up thus far, we are now ready to describe the actor-critic algorithm that we analyze in this paper. We refer to it as the *Pessimistic Actor Critic for Learning without Exploration*, or Pacle for short. We first describe the critic in Section 3.1, and then the actor in Section 3.2. We summarize the actor and critic algorithms, respectively, in pseudocode form in Algorithm 1 and Algorithm 2.

<!-- chunk {"id": "body-0034", "role": "body", "section": "The Critic: Pessimistic Least Square Policy Evaluation", "weight": 1.0} -->

The purpose of the critic is to provide pessimistic value function estimates corresponding to the policy $\pi$ under consideration by the actor. Monte Carlo with importance sampling (IS) is not desirable in this setting, as the policy or distribution that generated the dataset might be unknown and estimation errors on the distribution can accumulate exponentially with the horizon in IS estimators (see e.g. \[LGR^+^18\]). Instead, we use a least-squares temporal difference method for policy evaluation, but suitably perturbed to return pessimistic estimates---i.e., lower bounds on the true value function of the given policy $\pi$. Our method is based on directly perturbing the regression parameters in the least-square estimate. In contrast to bonus-based approaches, this method has the important advantage of ensuring that the action-value function remains linear. The purpose of the perturbations is to compensate for possible statistical errors in estimating the regression parameter due to poor coverage of the given dataset.

<!-- chunk {"id": "body-0035", "role": "body", "section": "The Critic: Pessimistic Least Square Policy Evaluation", "weight": 1.0} -->

Let us now give a precise description of the critic. Given a policy $\pi = {(\pi_{1},\ldots,\pi_{H})}$, the goal of the critic is to minimize the quantity

<!-- chunk {"id": "body-0036", "role": "body", "section": "The Critic: Pessimistic Least Square Policy Evaluation", "weight": 1.0} -->

which is an estimate of the value function $V^{\pi}{(s_{1})}$ for the policy $\pi$ at the initial state $s_{1}$. The parameter $w_{1} \in {\mathbb{R}}^{d}$ is a vector to be adjusted, one that is determined by a backwards-running sequence of regression problems from $h = H$ down to $h = 1$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "The Critic: Pessimistic Least Square Policy Evaluation", "weight": 1.0} -->

We introduce the pessimistic perturbations directly to the solution of these regression problems. They involve a norm defined by the cumulative covariance matrix. Recall that $\mathcal{I}_{h}$ indexes the subset of observations associated with state-action pairs at time step $h$. For each $h \in {\lbrack H\rbrack}$ and $i \in \mathcal{I}_{h}$, let us write the associated sample as the quadruple $(s_{hi},a_{hi},r_{hi},s_{{h + 1},i})$. Introducing the shorthand notation $\phi_{hi} = {\phi_{h}{(s_{hi},a_{hi})}}$, we define the *cumulative covariance matrix*

<!-- chunk {"id": "body-0038", "role": "body", "section": "The Critic: Pessimistic Least Square Policy Evaluation", "weight": 1.0} -->

where $I_{d \times d}$ denotes the $d$-dimensional identity matrix. Notice that the cumulative covariance grows as the number of samples in $\mathcal{I}_{h}$ increases; we do not normalize it by the local sample size $n_{h} = {|\mathcal{I}_{h}|}$, so that $\Sigma_{h}$ effectively represents the amount of information contained in the sub-dataset $\mathcal{D}_{h}$ at time step $h$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "The Critic: Pessimistic Least Square Policy Evaluation", "weight": 1.0} -->

Since $\Sigma_{h}$ is strictly positive definite by construction, it defines a pair of norms

<!-- chunk {"id": "body-0040", "role": "body", "section": "The Critic: Pessimistic Least Square Policy Evaluation", "weight": 1.0} -->

Consider the regression problem that is solved in moving backward from time step $h + 1$ to $h$. Given the weight vector $w_{h + 1}$ at time step $h + 1$, the regularized least-squares estimate of $w_{h}$ is given by

<!-- chunk {"id": "body-0041", "role": "body", "section": "The Critic: Pessimistic Least Square Policy Evaluation", "weight": 1.0} -->

for all $h \in {\lbrack H\rbrack}$. Here the matrices $\Sigma_{h}$ were previously defined in equation.

<!-- chunk {"id": "body-0042", "role": "body", "section": "The Critic: Pessimistic Least Square Policy Evaluation", "weight": 1.0} -->

The convex program consists of a linear objective subject to quadratic constraints; it is a special case of a second order cone program, and can be efficiently solved with standard convex solvers.

<!-- chunk {"id": "body-0043", "role": "body", "section": "The Critic: Pessimistic Least Square Policy Evaluation", "weight": 1.0} -->

1:Input: Dataset 𝒟, starting state s1, learning rate η
2:Set $\theta_{1} = {(\overset{\rightarrow}{0},\ldots,\overset{\rightarrow}{0})}$
4: ${\underset{¯}{w}}_{t}\leftarrow$ Critic(𝒟,πθt,s1)
5: $\theta_{t + 1} = {\theta_{t} + {\eta{\underset{¯}{w}}_{t}}}$
7:Return: Mixture policy πθ1, …, πθT
Algorithm 1 Actor (Mirror Descent)

<!-- chunk {"id": "body-0044", "role": "body", "section": "The Critic: Pessimistic Least Square Policy Evaluation", "weight": 1.0} -->

1:Input: Dataset 𝒟, target policy π, starting state s1, critic radii {ρhw}h = 1, …, H, and parameters {αh}h = 1, …, H
2:Solve the optimization program
3:Return: Optimal weight vector $\underset{¯}{w}$
Algorithm 2 Critic (Plspe)

<!-- chunk {"id": "body-0045", "role": "body", "section": "The Actor: Mirror Descent", "weight": 1.0} -->

We now turn to the behavior of the actor. It applies the mirror descent algorithm based on the Kullback Leibler (KL) divergence. This combination leads to the exponentiated gradient update rule in every timestep $h \in {\lbrack H\rbrack}$, so that the soft-max policy in moving from iteration $t$ to $t + 1$ is updated as

<!-- chunk {"id": "body-0046", "role": "body", "section": "The Actor: Mirror Descent", "weight": 1.0} -->

Here $\eta > 0$ is a stepsize parameter, and our theory specifies a suitable choice.

<!-- chunk {"id": "body-0047", "role": "body", "section": "The Actor: Mirror Descent", "weight": 1.0} -->

If the $Q$-value above from the critic lives in $\mathcal{Q}$, then it is possible to show that $\pi_{{t + 1},h} \in \Pi_{h}$ and the update rule takes a much simpler and computationally more efficient form (cf. Line 5 of Algorithm 1), where ${\underset{¯}{w}}_{t}$ is the gradient of the value function on the pessimistic MDP implicitly identified by the critic. In this case, the spaces $(\mathcal{Q},\Pi)$ are said to be *compatible* \[SMS^+^99 \] and the resulting algorithm is often called the *Natural Policy Gradient* (NPG) (see also ). By construction, the critic maintains a linear action value function even after pessimistic perturbations. As a consequence, the actor policy space is the simple softmax policy class $\Pi$ and the easier update rule can be used. As we explain in the analysis, this has important statistical benefits.

<!-- chunk {"id": "body-0048", "role": "body", "section": "The Actor: Mirror Descent", "weight": 1.0} -->

After $T$ rounds of updates, the mirror descent algorithm that we use here readily achieves online regret rates (in the optimization setting with exact feedback) $\sim {1/T}$ or $\sim {1/\sqrt{T}}$ depending on the analysis and the learning rate, although we mention that these rates could potentially be improved.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Main results", "weight": 1.0} -->

We now turn to the statement of a bound on the performance of the policy $\pi_{\text{Alg}}$ returned by Pacle. This upper bound involves three terms: an optimization error, an uncertainty term, and a model mis-specification term. The *optimization error* is given by ${\mathcal{C}{(T)}}\overset{def}{=}{4H\sqrt{\frac{\log{|\mathcal{A}|}}{T}}}$; it captures the rate at which the error decreases as a function of the iterations of the actor.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Main results", "weight": 1.0} -->

The *mis-specification error* ${\mathcal{E}_{\text{msp}}{(\nu)}}\overset{def}{=}{\sum_{h = 1}^{H}\nu_{h}}$ is simply the sum of all the stage-wise mis-specification errors; notice that the mis-specification error does depend on the choice of the radii for the critic $\rho_{1}^{w},\ldots,\rho_{H}^{w}$ in a problem dependent way (cf. 3. ‣ 2.4 A range of function class assumptions ‣ 2 Background and problem formulation")).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Main results", "weight": 1.0} -->

where the cumulative covariance matrix $\Sigma_{h}$ was defined in equation.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Main results", "weight": 1.0} -->

The amount of information from the dataset $\mathcal{D}$ is fully encoded in the uncertainty function $\mathcal{U}$ through the sequence of cumulative covariance matrices ${\{\Sigma_{h}\}}_{h = 1}^{H}$ and parameters ${\{\alpha_{h}\}}_{h = 1}^{H}$. The more data are available, the more positive definite $\Sigma_{h}$ is and the smaller the uncertainty function $\mathcal{U}{(\pi;\alpha)}$ becomes for a fixed policy $\pi$. If the sampling distribution that generates the dataset is fixed, then we can write ${\mathcal{U}{(\pi;\alpha)}} \lessapprox {c/\sqrt{n}}$ where $c$ does not depend on $n$ and can be interpreted as the coverage of the sampling distribution with respect to policy $\pi$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "A guarantee for PACLE", "weight": 1.0} -->

Our main result holds under Assumption 1. ‣ 2.2 Assumptions on data generation ‣ 2 Background and problem formulation") on the data collection process. It is based on radii ${\{\rho_{h}^{w}\}}_{h = 1}^{H}$ for the action value function^22^2This represents a setting where both the reward and the value function can be as large as $1$ in absolute value. One easily recovers the setting with value functions in $\lbrack 0,H\rbrack$ using a rescaling argument. that lie in the interval $(0,1\rbrack$, and it provides a guarantee relative to the class $\Pi_{\text{all}}$ of all stochastic policies.

<!-- chunk {"id": "body-0054", "role": "body", "section": "A lower bound", "weight": 1.0} -->

Thus far, we have stated an upper bound on the quality of the returned policy for a given procedure. Central to this upper bound is the uncertainty function $\mathcal{U}{(\pi;\alpha)}$. In this section, we show that a term of this form is unavoidable for any procedure. In particular, working within the well-specified setting, we prove a lower bound in terms of the quantity ${\mathcal{U}{(\pi;\sqrt{d})}} = {\sqrt{d}{\sum_{h = 1}^{H}{\|{\overline{\phi}}_{h}^{\pi}\|}_{\Sigma_{h}^{- 1}}}}$. Recalling that our choice of $\alpha$ scales with $\sqrt{d}$ (along with other logarithmic factors), this lower bound shows that our result is tight up to logarithmic factors.

<!-- chunk {"id": "body-0055", "role": "body", "section": "A lower bound", "weight": 1.0} -->

We show that the lower bound actually holds in a setting that is easier for the learner, in the sense that we restrict to low-rank MDPs, where there is no mis-specification error; and the mechanism that generates the dataset is non-adaptive, and so certainly satisfies Assumption 1. ‣ 2.2 Assumptions on data generation ‣ 2 Background and problem formulation").

<!-- chunk {"id": "body-0056", "role": "body", "section": "Comparison to related work", "weight": 1.0} -->

As in the paper, such a factor can be small even when traditional concentrability coefficients are large because they depend on state-action visit ratios (see the literature in Appendix A, e.g., ).

<!-- chunk {"id": "body-0057", "role": "body", "section": "Comparison to related work", "weight": 1.0} -->

With reference to the results in the paper, our work provides improvements in two distinct ways. First, their upper and lower bounds exhibit a gap of the order $dH$, which our analysis closes. Second, our analysis holds under the more permissive 3 *( (Bellman Restricted Closedness).)*. ‣ 2.4 A range of function class assumptions ‣ 2 Background and problem formulation") which includes low-rank MDPs. Of this improvement, a factor of $\sqrt{d}$ is due to the algorithm that we use, and the remainder is due to a more refined construction to certify optimality in Theorem 2. ‣ 4.2 A lower bound ‣ 4 Main results"). To be clear, our upper and lower bounds differ from theirs by a factor of $H$ due to a different normalization in the value function). We also note that the result of Liu et al. can be specialized to the low-rank MDP setting; however, even in this simpler setting, the results would be sub-optimal and also require additional density estimates.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Comparison to related work", "weight": 1.0} -->

Deriving a computationally tractable model-free algorithm without low-rank dynamics but subject to value function perturbations (e.g., optimistic or pessimistic perturbations) is an open problem even in the more heavily studied online exploration setting: there the current state-of-the art \[ DKL^+^21, JKA^+^17\] only present computationally *intractable* algorithms with the exception of for a PAC setting with low inherent Bellman error which however requires an additional "explorability" condition.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Proofs", "weight": 1.0} -->

In this section, we provide an outline of the proof of Theorem 1. ‣ 4.1 A guarantee for PACLE ‣ 4 Main results"). The main components of the proof are guarantees for the pessimistic estimates produced by the critic, and online learning guarantees for the updates taken by the actor. These two guarantees are coupled together via the notion of an induced MDP.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Proofs", "weight": 1.0} -->

The proof outline given here follows a bottom-up approach: (a) starting with the critic in Section 5.1, we first introduce the notion of induced MDP that links the critic's output to the actor's input (see Section 5.1.1), and then discuss how suitable choices of the pessimism parameters $\alpha$ allow us to guarantee that the critic underestimates the true value function (see Sections 5.1.2 and 5.1.3); (b) next in Section 5.2, we provide online-style learning guarantees for the actor, again using the notion of induced MDP to link these guarantees back to the critic; and (c) in Section 5.3, we put together the pieces to prove the theorem itself.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Critic's Analysis", "weight": 1.0} -->

Our goal in analyzing the critic is to relate these critic-estimated value functions to the true value functions ${\{ Q_{h}^{\pi}\}}_{h = 1}^{H}$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Induced MDP", "weight": 1.0} -->

Essential to our analysis is an object that provides the essential link between the critic's output and the actor's input. In particular, it is helpful to understand the critic in the following way: when given a policy $\pi$ as input, the critic computes the estimates ${\{{\underset{¯}{Q}}_{h}^{\pi}\}}_{h = 1}^{H}$, and uses them form a new MDP $\hat{M}{(\pi)}$, which we refer to as the *induced MDP*. This new MDP shares the same state/action space and transition dynamics with the original MDP $M$, differing only in the perturbation of the reward function. In particular, for each $h \in {\lbrack H\rbrack}$, we define the *perturbed reward function*

<!-- chunk {"id": "body-0063", "role": "body", "section": "Induced MDP", "weight": 1.0} -->

The induced MDP $\hat{M}{(\pi)}$ is simply the original MDP that uses this perturbed reward function.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Induced MDP", "weight": 1.0} -->

One important property of the induced MDP---which motivates the definition ---is that the estimates returned by the critic correspond to the *exact value functions* of policy $\pi$ in the induced MDP.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Critic's guarantee under a \"good\" event", "weight": 1.0} -->

We now show that there is a "good event"---call it $\mathcal{G}{(\alpha)}$---under which the critic's value function estimates have some additional desirable properties. Once this event is defined, the core of our proof involves determining the smallest choice of pessimism parameters under which it holds with probability at least $1 - \delta$.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Critic's guarantee under a \"good\" event", "weight": 1.0} -->

We begin with some notation required to define the good event. Let $\mathcal{F}$ denote the space of all real-valued functions on $\mathcal{S} \times \mathcal{A}$. The *regression operator* is a mapping from $\mathcal{F}$ to ${\mathbb{R}}^{d}$, given by

<!-- chunk {"id": "body-0067", "role": "body", "section": "Critic's guarantee under a \"good\" event", "weight": 1.0} -->

Note that $\mathcal{P}_{h}^{\pi}$ is a mapping from $\mathcal{F}$ to ${\mathbb{R}}^{d}$; it returns the weight vector of the best-fitting linear function to the Bellman update $\mathcal{T}_{h}^{\pi}{(F)}$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Critic's guarantee under a \"good\" event", "weight": 1.0} -->

Our good event is defined in terms of the *parameter error operators* $\mathcal{E}_{h}^{\pi}:{\mathcal{F}\rightarrow{\mathbb{R}}^{d}}$ given by

<!-- chunk {"id": "body-0069", "role": "body", "section": "Critic's guarantee under a \"good\" event", "weight": 1.0} -->

For a given sequence $\alpha = {(\alpha_{1},\ldots,\alpha_{H})}$ of pessimism parameters, we define the *good event*

<!-- chunk {"id": "body-0070", "role": "body", "section": "Some intuition", "weight": 1.0} -->

Why is this event relevant for guaranteeing good performance of the critic? In order to gain intuition, let us consider the special case in which there is no approximation error, so that the exact state-action value functions are actually linear. Letting $w_{h}^{\pi}$ denote the parameter associated with the linear action-value function at step $h$, when the good event holds, our choice of $\alpha$ allows us to set

<!-- chunk {"id": "body-0071", "role": "body", "section": "Some intuition", "weight": 1.0} -->

in the constraints (10b). In this way, at each step $h$ the vector ${\underset{¯}{\xi}}_{h}^{\pi}$ can perfectly compensate the noise error $\mathcal{E}_{h}^{\pi_{h + 1}}{(Q_{h + 1}^{\pi})}$ ensuring that the action-value function $Q_{h}^{\pi}$ (compactly encoded in the parameter $w_{h}^{\pi}$) can be perfectly represented. In other words, our choice guarantees that the feasible set for contains the 'true' solution $w_{h}^{\pi}$. Since the convex program involves minimizing over value functions, this feasibility underlies showing the critic returns an underestimate of the true value function for $\pi$ along with some approximation error in the general setting; see equation (23a ‣ Proposition 2.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Some intuition", "weight": 1.0} -->

‣ Some intuition: ‣ 5.1.2 Critic’s guarantee under a “good” event ‣ 5.1 Critic’s Analysis ‣ 5 Proofs")) below for a precise statement. We highlight that such underestimates is only guaranteed at the initial state $s_{1}$ and timestep $h = 1$ as encoded in the objective of the program in equation.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Some intuition", "weight": 1.0} -->

On the other hand, for other policies $\overset{\sim}{\pi}$, we can use the relation to control the difference between the value function $V_{1,{\hat{M}{(\pi)}}}^{\overset{\sim}{\pi}}$ in the induced MDP, and the exact value function $V_{1}^{\overset{\sim}{\pi}}$; see equation (23b ‣ Proposition 2. ‣ Some intuition: ‣ 5.1.2 Critic’s guarantee under a “good” event ‣ 5.1 Critic’s Analysis ‣ 5 Proofs")) for a precise statement of our conclusion.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Choice of pessimism parameters", "weight": 1.0} -->

Based on Proposition 2, our problem is now reduced to determining a choice of $\alpha$ for which the good event holds with probability at least $1 - \delta$. The bulk of our effort in analyzing the critic is devoted to the technical details of this step; we provide only a high-level summary here.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Choice of pessimism parameters", "weight": 1.0} -->

The event needs to hold uniformly over the value function and policy classes used by the algorithm.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Choice of pessimism parameters", "weight": 1.0} -->

For such choice of $R$ and failure probability $\delta \in {}$, suppose that we set

<!-- chunk {"id": "body-0077", "role": "body", "section": "Choice of pessimism parameters", "weight": 1.0} -->

for a suitably large universal constant $c$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Actor's Analysis", "weight": 1.0} -->

In this section, we analyze the mirror descent algorithm---that is, the actor in Algorithm 1. Our analysis exploits the methods in the paper, with some small changes to accommodate our framework; in particular, while our analysis assumes no error in the critic's evaluation, it does involve a sequence of time-varying MDPs.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Combining the pieces", "weight": 1.0} -->

We are now ready to combine the pieces so as to prove Theorem 1. ‣ 4.1 A guarantee for PACLE ‣ 4 Main results"). For each iteration $t \in {\lbrack T\rbrack}$, let $\pi_{t}\overset{def}{=}\pi_{\theta_{t}}$ be the policy chosen by the actor, and let $M_{t} = M_{\pi_{t}}$ be the corresponding induced MDP.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Combining the pieces", "weight": 1.0} -->

Recall that Lemma 2, stated in Section C.2, guarantees that the "good" event $\mathcal{G}$ from equation occurs with probability at least $1 - \delta$. Conditioned on the occurrence of $\mathcal{G}$, the bounds (23a ‣ Proposition 2. ‣ Some intuition: ‣ 5.1.2 Critic’s guarantee under a “good” event ‣ 5.1 Critic’s Analysis ‣ 5 Proofs")) and (23b ‣ Proposition 2. ‣ Some intuition: ‣ 5.1.2 Critic’s guarantee under a “good” event ‣ 5.1 Critic’s Analysis ‣ 5 Proofs")) ensure that for any comparator $\overset{\sim}{\pi}$, we have

<!-- chunk {"id": "body-0081", "role": "body", "section": "Combining the pieces", "weight": 1.0} -->

We now average over the iterations $t \in {\lbrack T\rbrack}$. The equality (18a. ‣ 5.1.1 Induced MDP ‣ 5.1 Critic’s Analysis ‣ 5 Proofs")) from Lemma 1. ‣ 5.1.1 Induced MDP ‣ 5.1 Critic’s Analysis ‣ 5 Proofs") ensures for each iteration $t$, the actor receives as an input a vector ${\underset{¯}{w}}_{t}$ such that

<!-- chunk {"id": "body-0082", "role": "body", "section": "Combining the pieces", "weight": 1.0} -->

Note that under the good event $\mathcal{G}$, the bound holds for any comparator policy $\overset{\sim}{\pi}$, which was the claim of the theorem.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this paper, we have developed and analyzed an actor-critic method procedure, designed for finding near-optimal policies in the offline setting. The Pacle procedure introduces pessimism into the critic's evaluation of a given policy's value function, thereby ensuring that, under suitable parameter choices and assumptions, it maintains (with high probability) a lower bound on the true value function. The actor then performs a form of mirror ascent so as to maximize the value of these lower bounds.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Discussion", "weight": 1.5} -->

An important feature of our method is that it introduces pessimism via direct perturbations of the parameter vectors in a linear function approximation scheme. In this way, we avoid having to impose additional model assumptions; moreover, the pessimism does *not* substantially increase the complexity of our under value/policy classes, which allows us to provide minimax-optimal guarantees. We note that similar approaches have appeared before in the exploration setting; for example, see the recent papers \[ DKL^+^21\]. These methods enjoy similar advantages in terms of theoretical guarantees, but at the expense of computational tractability. In contrast, the method of this paper entails solving a low-dimensional second-order cone program, a simple class of convex programs for which there exist many polynomial-time algorithms. We enjoy this advantage due to some key differences between the offline and online settings of RL. In the offline setting, it is possible to keep the actor's update cleanly separated from the evaluation step of the critic, as we have done here; this separation underlies the computational tractability.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Discussion", "weight": 1.5} -->

Our work leaves open a number of interesting questions for future work. First, it would be interesting to provide some numerical studies of the Pacle's performance, so as to understand its practical behavior relative to the theoretical guarantees provided here. Also, our analysis here has focused purely on approximation using linear basis expansions; extension to more general function classes is an important next step. Finally, it will be interesting to see to what extent these ideas can be translated to the more challenging setting of exploration.
