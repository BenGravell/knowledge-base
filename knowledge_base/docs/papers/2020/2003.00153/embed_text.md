## Introduction

Improving the sample efficiency of reinforcement learning (RL) algorithms through effective exploration-exploitation strategies is a major focus of the recent theoretical literature. Strong results are available with a generative model as well as in the *online* setting when the learning performance is measured by the cumulative regret, i.e., the difference between the performance of the optimal policy and the reward accumulated by the learner. For finite horizon problems, UCBVI achieves worst-case optimal regret, while algorithms with domain adaptive bounds have been introduced by and. Randomized and model-free variants have also been proposed, together with methods with other beneficial properties. Similar results are also available in the infinite horizon setting.

Approximate dynamic programming. While the results for tabular settings are encouraging, function approximation is normally required to tackle problems where the state or action spaces may be intractably large. In this case, even when the Bellman operator can be applied exactly, simple dynamic programming algorithms coupled with linear architectures may diverge, thus suggesting that effective approximate RL may not be feasible in the general case.

Convergence guarantees and finite-sample analyses are available for the least-squares policy improvement (LSPI) algorithm under the assumption that the value function of *all policies can be well approximated* within the chosen function class (*LSPI conditions*, for short). For concreteness, let $\epsilon$ be the worst-case misspecification error of a $d$-dimensional linear function approximator over the policy action-value functions (i.e., for any policy $\pi$, there exists an approximation ${\hat{Q}}^{\pi}$ such that ${\|{{\hat{Q}}^{\pi} - Q^{\pi}}\|} \leq \epsilon$). Recently, showed that when using highly misspecified approximators $\epsilon \gtrapprox {1/\sqrt{d}}$ the worst-case sample complexity may be exponential in $d$. At the same time, when $\epsilon \lessapprox {1/\sqrt{d}}$, and showed algorithms with $\sqrt{d}$ loss times the misspecification level $\epsilon$. In particular, showed that LSPI attains polynomial sample complexity using $G$-optimal design with a $\approx {\sqrt{d}\epsilon}$ additive error using a *generative model*.

Similarly, for the least-squares value iteration algorithm (LSVI) convergence guarantees and finite sample analysis are also available under the assumption of low inherent Bellman error (IBE), (*LSVI conditions*, for short). Given a function class $\mathcal{F}$, the IBE measures the error in approximating the image of any function in $\mathcal{F}$ through the Bellman operator. Whenever the IBE is not small, it is easy to show that approximation errors may be amplified by a constant factor at each application of the Bellman operator, leading to divergence. Although methods exist to limit this amplification of errors, the question of when sample-efficient value-based RL is possible remains open even in the absence of misspecification.

In this paper we focus on the problem of exploration-exploitation using LSVI approaches in settings with low IBE. We make several contributions.

Exploration with low inherent Bellman error. We first show that the notion of inherent Bellman error is distinct from the LSPI condition, and more general than the low-rank assumption on the dynamics used in a series of recent works on exploration with linear function approximation. For a finite horizon MDP, when the LSVI conditions are satisfied either exactly or approximately (i.e., the inherent Bellman error is either zero or small) we propose *Efficient Linear Exploration of Actions by Nonlinear Optimization of the Residuals* (Eleanor), an optimistic generalization of the popular LSVI algorithm. We analyze Eleanor and derive the first regret bound for this setting and show it is unimprovable in terms of statistical rates, though we leave its computational tractability open.

Our analysis shows that the performance of Eleanor degrades gracefully in the case of positive inherent Bellman error. Interestingly, we recover a similar $\sqrt{d}$ amplification of the misspecification error (the IBE in our case) as for LSPI, despite the fact that we consider the more challenging online setting as opposed to the generative model by Lattimore & Szepesvari.

Low-rank MDPs and contextual misspecified linear bandits. Our result applies to low-rank MDPs and improves upon the best-known regret bound for that setting by a $\sqrt{d}$ factor. When applied to contextual linear bandits, our algorithm reduces to the celebrated LinUCB (or Oful) algorithm of. In addition, however, it *can handle contextual misspecified linear bandits while retaining computationally tractability*, making this the first algorithm and analysis for this setting, although we require knowledge of the misspecification level. A similar result was recently derived for a different algorithm based on $G$-experimental design for the more restrictive setting of non-contextual (i.e., with features not depending on the state and fixed action space) misspecified linear bandits; however, their approach is agnostic to the misspecification level.

Core ideas. LSVI-based algorithms have been successfully analyzed for low-rank MDPs by adding exploration bonuses at every experienced state, thereby ensuring optimism by backward induction. In contrast, our more general setting demands that the value function stays linear, ruling out approaches based on exploration bonuses. In fact, if the value function used for backup is not linear, low inherent Bellman error does not provide any guarantee about how errors may propagate, which can be exponential in the general case.

Our proposal extends the LSVI algorithm to return an optimistic solution at the initial state through *global* optimization over the value function parameters, while still enforcing linearity of the representation. This has two advantages: 1) (*handling of the bias*) it enables us to use the concept of inherent Bellman error, requiring that the Bellman operator be applied to *linear* action-value functions and avoiding a $\sqrt{d}$ amplification of the value function error at every step; 2) (*handling of the variance*) it keeps the complexity of the action-value functional space small (linear), enabling the use of confidence intervals that are as tight as those used in the bandit literature, yielding the optimal finite-sample statistical rate.

## Notation

We consider an undiscounted finite-horizon MDP $M = {(\mathcal{S},\mathcal{A},p,r,H)}$ with state space $\mathcal{S}$, action space $\mathcal{A}$, and horizon length $H \in {\mathbb{N}}^{+}$. For every $t \in {\lbrack H\rbrack}\overset{def}{=}{\{ 1,\ldots,H\}}$, every state-action pair is characterized by an expected reward $r_{t}{(s,a)}$ with an associated reward random variable $R_{t}{(s,a)}$ and a transition kernel $p_{t}{( \cdot \mid s,a)}$ over next state. We assume $\mathcal{S}$ to be a measurable, possibly infinite, space and $\mathcal{A}$ can be any (compact) time and state dependent set (we omit this dependency for brevity). For any $t \in {\lbrack H\rbrack}$ and ${(s,a)} \in {\mathcal{S} \times \mathcal{A}}$, the state-action value function of a non-stationary policy $\pi = {(\pi_{1},\ldots,\pi_{H})}$ is defined as ${Q_{t}^{\pi}{(s,a)}} = {{r_{t}{(s,a)}} + {{\mathbb{E}}\left\lbrack {{\sum_{l = {t + 1}}^{H}{r_{l}{(s_{l},{\pi_{l}{(s_{l})}})}}} \mid {s,a}} \right\rbrack}}$ and the value function is ${V_{t}^{\pi}{(s)}} = {Q_{t}^{\pi}{(s,{\pi_{t}{(s)}})}}$. Since the horizon is finite, under some regularity conditions, e.g. there always exists an optimal policy $\pi^{\star}$ whose value and action-value functions are defined as ${V_{t}^{\star}{(s)}}\overset{def}{=}{V_{t}^{\pi^{\star}}{(s)}} = {\sup_{\pi}{V_{t}^{\pi}{(s)}}}$ and ${Q_{t}^{\star}{(s,a)}}\overset{def}{=}{Q_{t}^{\pi^{\star}}{(s,a)}} = {\sup_{\pi}{Q_{t}^{\pi}{(s,a)}}}$.

The value iteration (or backward induction) algorithm computes $\pi^{\star}$ and $V^{\star}$ as follows: it starts from ${V_{H + 1}^{\star}{(s)}} = 0$ for all $s \in \mathcal{S}$ and it computes $Q_{t}^{\star}$ using the Bellman equation in each state-action pair recursively from $t = H$ down to $1$ and it returns the optimal policy ${\pi_{t}^{\star}{(s)}} = {{\arg{\max_{a}Q_{t}^{\star}}}{(s,a)}}$. In particular, the Bellman operator $\mathcal{T}_{t}$ applied to $Q_{t + 1}$ is defined as

## Linear Value Function Frameworks

In this section we introduce basic notation and assumptions for linear function approximation, we define the concept of inherent Bellman error, and we investigate connections with alternative settings.

Whenever the state space $\mathcal{S}$ is too large or continuous, value functions cannot be represented by enumerating their values at each state or state-action pair. A common approach is to define a feature map $\phi_{t}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}^{d_{t}}}$, possibly different at any $t \in {\lbrack H\rbrack}$, embedding each state-action pair $(s,a)$ into a $d_{t}$-dimensional vector $\phi_{t}{(s,a)}$. The action-value functions are then represented as a linear combination between the features $\phi_{t}$ and a vector parameter $\theta_{t} \in {\mathbb{R}}^{d_{t}}$, such that ${Q_{t}{(s,a)}} = {\phi_{t}{(s,a)}^{\top}\theta_{t}}$. This effectively reduces the complexity of the problem from $|{\mathcal{S} \times \mathcal{A}}|$ down to $d_{t}$.

We define the space of parameters $\theta$ inducing uniformly bounded action-value functions

We will later require the constant $D \in {\mathbb{R}}$ to be chosen to satisfy Asm. 1. ‣ 5 Main Result: Regret Upper Bound ‣ Learning Near Optimal Policies with Low Inherent Bellman Error"). For instance, $D = 1$ requires the value function to be in $\lbrack{- 1},{+ 1}\rbrack$ and complies with the assumption.

Each parameter $\theta$ identifies an (action) value function

and the associated functional spaces

Inherent Bellman error. The value iteration algorithm can be used to compute an optimal policy and it smoothly extends to linear approximators. The procedure repeatedly applies the Bellman operator $\mathcal{T}_{t}$ to an action-value function^11^1One can reason with either the value function $V$ or the action-value function $Q$. $Q_{t} \in \mathcal{Q}_{t}$ and projects the computed point $\mathcal{T}_{t}Q_{t}$ back to $\mathcal{Q}_{t + 1}$ using a (e.g., least-squares) projection operator $\Pi_{t}$. The projection error is precisely the inherent Bellman error, which can be thought of as how close the space $\mathcal{Q}_{t}$ is w.r.t. the Bellman operator $\mathcal{T}_{t}$.

### Definition 1

The inherent Bellman error^22^2A different definition, more suitable for generative models with stationary policies using a $p$-norm induced by the sampling distribution is provided by. of an MDP with a linear feature representation $\phi$ is denoted with $\mathcal{I}$ and is the maximum over the timesteps $t \in {\lbrack H\rbrack}$ of

Our definition of inherent Bellman error is *natural* in the sense that it is defined with respect to the linear action-value function class without additional clipping if the value function exceeds a prescribed threshold and is not enlarged to incorporate exploration bonuses (see e.g., ). Alternative definitions may enlarge the underlying functional space in an artificial, non linear, possibly algorithm-dependent way, and result in a much more restrictive definition of inherent Bellman error. We notice that while our definition is less restrictive, it rules out traditional forms of exploration based on *adding exploration bonuses*, making it harder to design effective exploration strategies.

Properties. We discuss the properties of MDPs with $\mathcal{I} = 0$. An immediate consequence of def. 1 is that when $\mathcal{I} = 0$ the reward function is linear, and so is the transition kernel *when applied to elements of* $\mathcal{V}_{t + 1}$.

\[Linearity of Rewards and Restricted Linearity of Transitions\]proplinearity Given an MDP and a linear feature representation with $\mathcal{B}_{t} = {\mathbb{R}}^{d_{t}}$ and inherent Bellman error $\mathcal{I} = 0$ we have that the rewards are linear in the sense that:

and the transition have a linear effect on members of $\mathcal{V}_{t + 1}$

If $\mathcal{I} = 0$, the application of the Bellman operator $\mathcal{T}_{t}$ to members of $\mathcal{Q}_{t + 1}$ always produces a member of $\mathcal{Q}_{t}$, i.e., ${\mathcal{T}_{t}\mathcal{Q}_{t + 1}} \subseteq \mathcal{Q}_{t}$. From here, we can immediately see that the zero inherent Bellman error assumption is more general than low-rank MDPs. Indeed, in low-rank MDPs the Bellman operator returns a function in the range of the features (i.e., in $\mathcal{Q}_{t}$) *regardless of value function $Q_{t + 1}$*, while problems with zero inherent Bellman error are only required to map elements of $\mathcal{Q}_{t + 1}$ to $\mathcal{Q}_{t}$, and are thus more general approximators.

\[Low Rank $\subseteq$ LSVI Conditions\]propLowrankVsNOIBE Let $\mathcal{B}_{t} = {\mathbb{R}}^{d_{t}}$, and consider an MDP with associated linear feature representation $\phi$. If the MDP is a low rank (or linear) MDP, i.e., for a parameter $\theta_{t}^{R} \in {\mathbb{R}}^{d_{t}}$ and a measure function^33^3a positive function such that ${\|\Psi_{t}\|}_{TV} = 1$ $\psi_{t}{( \cdot )}$:

then $\mathcal{I} = 0$. However, the converse does not hold, i.e., there exists an MDP and a linear feature extractor $\phi$ with $\mathcal{I} = 0$ which is not a linear MDP in the sense of LABEL:eqn:LinearMDPequations.

Another assumption often made on the approximation space is that the action-value functions for *all policies* do belong to $\mathcal{Q}_{t}$ (LSPI condition), a condition normally employed to show convergence of LSPI. This assumption is also strictly less restrictive than low-rank (see also for a claim in one direction).

\[Low Rank $\subseteq$ LSPI Conditions\]propLowrankVsLP If a given MDP is low rank in the sense of LABEL:eqn:LinearMDPequations then the value function of all policies admit a linear parameterization:

However, there exists an MPD and a linear approximator with feature extractor $\phi$ which satisfies the above display but there exists no $\psi_{t}$ such that LABEL:eqn:LinearMDPequations holds.

One may wonder what is the relation between MDPs with no inherent Bellman error and MDPs where all action-value function for all policies are linear, i.e., the LSVI and LSPI conditions. These are two very distinct assumptions: the former deals with policies *that are optimal with respect to a parameter*, while the latter deals with arbitrary policies. Conversely, the latter deals with the $Q$ values that actually corresponds to $Q$ values of policies, while the former measures the error with respect to any function in the class.

\[LSVI Conditions $\neq$ LSPI Conditions\]propNOIBEvsLP There exists an MDP and a linear representation with feature extractor $\phi$ with $\mathcal{I} = 0$ and yet the policies are not linearly parameterizable in the sense that:

Vice-versa, there exists an MDP and a feature representation such that all action-value functions of all policies admit a linear parameterization:

and yet the inherent Bellman is non-zero: $\mathcal{I} > 0$.

The final connection we make is with settings with *low Bellman rank*, see. It is possible to show that if the LSVI conditions are satisfied, the Bellman rank is at most $d$, where $d$ is the dimensionality of the features. However, no statistically efficient algorithm exists for this setting, because Olive from has an explicit dependence on the size of the action space, which can be very large or infinite in the setting we consider here.

## Algorithm

We consider the standard online learning protocol in finite-horizon problems, where at each episode $k$, the learner executes a policy $\pi_{k}$, records the samples in the trajectory, updates the policy and reiterates over the next episode. We first recall the standard LSVI. At the beginning of episode $k$, consider timestep $t$ and assume the next-step parameter is fixed and equal to $\theta_{t + 1}$. The objective function of the regularized least-square is

where ${\{\phi_{ti}\}}_{i = {1,\ldots,{k - 1}}}$ are the features observed at timestep $t$ in state $s_{ti}$ and $r_{ti}$ are the corresponding rewards. For any $\lambda > 0$ the prior display has a closed-form solution

with $\Sigma_{tk}\overset{def}{=}{{\sum_{i = 1}^{k - 1}{\phi_{ti}\phi_{ti}^{\top}}} + {\lambdaI}}$ as the empirical covariance.

We introduce an optimistic variant of LSVI, where the optimistic parameters are chosen by solving a global optimization problem across the whole horizon $H$. At each episode, Eleanor (in Alg. 1) solves the following problem.

### Definition 2 (Planning Optimization Program)

As we will show in the technical analysis, a feasible solution $(\theta_{1}^{\star},\ldots,\theta_{H}^{\star})$, corresponding to the best approximator (in eq. 10) always exists and so the program is well posed.

The least-square solution ${\hat{\theta}}_{t}$ is used as a constraint and perturbed by adding a vector ${\overline{\xi}}_{t}$ as optimization variable,^44^4We add the subscript $k$ later to indicate the actual variable chosen by the optimization procedure in episode $k$. subject to

where $\alpha_{tk}$ is designed to account for the noise, misspecification, and regularization bias. The actual bound is a function of the allowable radius $\mathcal{R} \leq \sqrt{d_{t}}$ for the parameter (as in assumption 1. ‣ 5 Main Result: Regret Upper Bound ‣ Learning Near Optimal Policies with Low Inherent Bellman Error")) and the noise parameter $\sqrt{\beta_{tk}} = {\overset{\sim}{O}{(\sqrt{d_{t}})}}$ stems from self-normalizing concentration inequalities as described in the technical analysis later, while $\mathcal{I}$ is the inherent Bellman error. The resulting parameter ${\overline{\theta}}_{t} = {{\hat{\theta}}_{t} + {\overline{\xi}}_{t}}$ must satisfy the constraint ${\overline{\theta}}_{t} \in \mathcal{B}_{t}$. This is equivalent to clipping the value function to avoid out-of-range values, with the difference that such clipping occurs directly in the parameter space as opposed to state by state, and thus preserves linearity.

We emphasize that the optimization over the ${\overline{\xi}}_{t}$'s is *global*, in stark contrast to the tabular setting and even the setting of linear MDPs considered by, where any perturbation (clipping, exploration bonus, etc) can be done state by state. For example, define ${{\overline{Q}}_{t}{(s,a)}}\overset{\text{redefined}}{=}{\min{\{ 1,{{\phi_{t}{(s,a)}^{\top}{\overline{\theta}}_{t}} + \text{Bonus}}\}}}$ where the bonus is the result of maximizing ${\overline{\xi}}_{t}$ state by state. This trick works in the low-rank setting of, since any non-linear component is filtered out by the low-rank projector. Eleanor instead pushes that maximization over the ${\overline{\xi}}_{t}$'s "outside" of local states, i.e., it performs a *global maximization* to ensure linearity of the value function representation, a mandatory condition in our setting to avoid an exponential propagation of the errors.

When linear representations are enforced, however, the algorithm cannot choose a value function everywhere optimistic due to values in different states possibly being negatively correlated. Eleanor shoots for being optimistic at the initial state, but in general the algorithm does not play optimistic actions in the encountered states at later timesteps. Fortunately, this is enough to attain a rate-optimal efficiency.

1: Input: failure probability δ, regularization λ = 1, feature extractor ϕ, inherent Bellman residual ℐ
4: Receive starting state s1 k
5: Set ${\overline{\theta}}_{{H + 1},k} = {\hat{\theta}}_{{H + 1},k} = {\overline{\xi}}_{{H + 1},k} = 0$
6: Solve program of definition 2.
7: Execute $\pi_{k}:{{(s,t)}\mapsto{{{\arg\max}_{a}\phi_{t}}{(s,a)}^{\top}{\overline{\theta}}_{tk}}}$ and collect (st k,at k,rt k) for t ∈ [H].

Although Eleanor is proved to be near optimal, it is difficult to implement the algorithm efficiently. This should not be seen as a fundamental barrier, however. The issue of computational tractability arises even for tabular problems, but of course the problem is more pronounced when function approximators are implemented, and even for low-rank MDPs the first regret result has been obtained at the expense of a practical algorithm. Fortunately, later work has made progress on the computational aspects for many of these settings. For now, we leave this to future work.

Relaxations. With an eye towards a possible relaxation, we notice that the constraint ${\overline{\theta}}_{t} \in \mathcal{B}_{t}$ can be expensive to evaluate because it would require checking that every product $\phi_{t}{( \cdot, \cdot )}^{\top}{\overline{\theta}}_{t}$ is bounded. However, one can use simpler, more restrictive geometries and assume $\mathcal{B}_{t}$ is a unit ball, bypassing this problem. The algorithm regret bound for this case is the same as that of 1. ‣ 5 Main Result: Regret Upper Bound ‣ Learning Near Optimal Policies with Low Inherent Bellman Error").

Finally, it is possible to avoid the regularization in the least square objective of eq. 4 and relax the requirement ${\|{\overline{\theta}}_{t}\|}_{2} \leq \sqrt{d_{t}}$ as presented later in assumption 1. ‣ 5 Main Result: Regret Upper Bound ‣ Learning Near Optimal Policies with Low Inherent Bellman Error"). In fact, the constraint on $\mathcal{B}_{t}$ suffices to avoid ill-conditioned solutions, but then one would need to resort to pseudo-inverse computations, making the algorithm / analysis more complicated.

## Main Result: Regret Upper Bound

### Assumption 1 (Main Assumption)

${|{Q_{t}^{\pi}{(s,a)}}|} \leq {1,{\forall\pi},{\forall{(s,a,t)}}}$

${{\|{\phi_{t}{(s,a)}}\|}_{2} \leq L_{\phi} \leq 1},{\forall{(s,a,t)}}$

For any $Q_{t} \in \mathcal{Q}_{t}$ and any ${(s,a,t)} \in {\mathcal{S} \times \mathcal{A} \times {\lbrack H\rbrack}}$ define the random variable^55^5Here, $R_{t}{(s,a)}$ is the reward random variable, and $s^{\prime} \sim {p_{t}{(s,a)}}$ is the successor state random variable under the distribution $p_{t}{(s,a)}$. $X = {{R_{t}{(s,a)}} + {{\max_{a^{\prime}}Q_{t + 1}}{(s^{\prime},a^{\prime})}}}$. Then the noise $\eta = {X - {{\mathbb{E}}X}}$ is $1$-subgaussian

${{{\forall t} \in {\lbrack H\rbrack}},{{\forall\theta_{t}} \in \mathcal{B}_{t}}},$ it holds that ${\|\theta_{t}\|} \leq \mathcal{R}_{t} \leq \sqrt{d_{t}}$, and $\mathcal{B}_{t}$ is compact

The first condition is a condition on the scaling of the problem and the bound on the feature norm is without loss of generality. The sub-Gaussianity is standard already for linear bandits. In particular, if the reward are in $\lbrack 0,1\rbrack$ and $D = 1$ in eq. 1, which gives ${\overline{V}{( \cdot )}} \in {\lbrack{- 1},1\rbrack}$, then this condition is automatically satisfied. Finally, the bound on the parameter limits the bias introduced by regularization which scales with the norm of the parameter, but a psedoinverse computation would relax this requirement.

After rescaling, however, our assumptions are much weaker the the usual setting that requires ${r_{t}{( \cdot, \cdot )}} \in {\lbrack 0,1\rbrack}$ and ${V_{t}^{\pi}{( \cdot )}} \in {\lbrack 0,H\rbrack}$ since we allow the reward to be of the same order as the value function after rescaling and even be negative. This is a harder setting.

\[Main Result\]thmMainResult Under assumption 1. ‣ 5 Main Result: Regret Upper Bound ‣ Learning Near Optimal Policies with Low Inherent Bellman Error") with $\lambda = 1$, with probability at least $1 - \delta$ jointly over all episodes it holds that the regret of Eleanor is bounded by:

There are no additional "lower order" terms in the above display, although the $\overset{\sim}{O}{( \cdot )}$ notation hides, as usual, logarithms of $d_{t},H,K,{1/\delta}$.

Care must be taken when comparing across settings with different scaling. In particular, *rescaling the problem* (i.e., the reward function) *by $H$* increases the sub-Gaussian norm of the rewards and transitions, and the value of the inherent Bellman error alike, yielding *an extra $H$ factor in the regret bound*. For example, in the setting that the rewards are bounded in $\lbrack 0,1\rbrack$ and the value function is in $\lbrack 0,H\rbrack$ with $d_{1} = \cdots = d_{H}\overset{def}{=}d$ and $\mathcal{I} = 0$ for simplicity, the above regret bound reduces (with $T = {KH}$) to $\overset{\sim}{O}{({dH^{\frac{3}{2}}\sqrt{T}})}$.

Low-rank MDPs As explained in definition 1, our result applies to low-rank MDPs; surprisingly, this shows that at least $\sqrt{d}$ improvement is possible in the main rate compared to the best-known $\overset{\sim}{O}{({{({dH})}^{3/2}\sqrt{T}})}$ of upper bound despite Eleanor is not specifically tailored to handle low-rank MDPs. This is possible because Eleanor looks for optimistic solutions directly in the $\theta$ parameter space instead of perturbing the value function by an exploration bonus as in. When the value function is perturbed by a bonus, it grows in complexity as it departs from the linear space; this requires an additional union bound over a more complicated value function class and ultimately loses a $\sqrt{d}$ factor. Finally, the inherent Bellman error covers the notion of approximate low-rank MDPs, and on the misspecification regret term we save a $\sqrt{d}$ factor as well thanks to a more careful projection argument in lemma 8. ‣ C.6 Projection Bound ‣ Appendix C Eleanor ‣ Learning Near Optimal Policies with Low Inherent Bellman Error").

## Contextual Misspecified Linear Bandits

Our framework reduces to bandits with linear approximators when $H = 1$ (we drop the time subscript $t$ in this case): Eleanor can handle *contextual misspecified linear bandits*, where contextual refers to allowing the action set to change as the feature extractor can be a function of the context. It follows from the definition that the inherent Bellman error is the reward function misspecification in this case.

### Corollary 1 (LinUCB Regret on Contextual Misspecified Linear Bandits)

Consider a misspecified contextual linear bandit problem with reward response

with ${|{\phi{(s,a)}^{\top}\theta^{\star}}|} \leq 1$, ${\|\theta^{\star}\|}_{2} \leq \sqrt{d}$, ${\|{\phi{(s,a)}}\|}_{2} \leq 1$, misspecification ${|{f{(s,a)}}|} \leq \mathcal{I}$ and $1$ sub-Gaussian noise $\eta$. If Eleanor is informed that $H = 1$ then the algorithm reduces to the LinUCB (aka Oful) algorithm of with arm selection strategy ${{\arg\max}_{{a \in \mathcal{A}},{{\|\overline{\xi}\|}_{\Sigma_{k}} \leq \sqrt{\alpha_{k}}}}\phi}{(s_{k},a)}^{\top}\left( {{\hat{\theta}}_{k} + {\overline{\xi}}_{k}} \right)$ but a different confidence interval: ${{\|{{\overline{\theta}}_{k} - {\hat{\theta}}_{k}}\|}_{\Sigma_{k}} = {\|{\overline{\xi}}_{k}\|}_{\Sigma_{k}} \leq \sqrt{\alpha_{k}}}.$ The arm selection strategy admits the closed-form solution ${\arg\max}_{a \in \mathcal{A}}\left\lbrack {{\phi{(s_{k},a)}^{\top}{\hat{\theta}}_{k}} + {{\|{\phi{(s_{k},a)}}\|}_{\Sigma_{k}^{- 1}}\sqrt{\alpha_{k}}}} \right\rbrack$ and the algorithm has a high probability regret bound

The corollary above is immediate upon substituting $H = 1$ in 1. ‣ 5 Main Result: Regret Upper Bound ‣ Learning Near Optimal Policies with Low Inherent Bellman Error") and verifying that our assumptions match the setting described in the corollary, which is the standard linear bandit setting^66^6We drop the constraint $\theta \in \mathcal{B}$ for simplicity with the addition of misspecification (few more details in appendix E).

Due to the equivalence to LinUCB the algorithm is computationally tractable when applied to bandits; the *key* difference with vanilla LinUCB resides in the width of the confidence intervals, parameter $\alpha_{k}$. In the absence of misspecification ($\mathcal{I} = 0$), $\sqrt{\alpha_{k}} = {\sqrt{\beta_{k}} + {\sqrt{\lambda}\mathcal{R}}} = {\overset{\sim}{O}{(\sqrt{d})}}$, as in the work of. When misspecification is present, however, there is a correction factor $\sqrt{k}\mathcal{I}$ in the definition of $\sqrt{\alpha_{k}}$, see equation eq. 6. In other words, this is the factor one should add to the exploration bonus for an LinUCB-like algorithm in case of (potentially adversarial) misspecification.

The recent result by applies here (see also the work of ). They show that for large misspecification $\mathcal{I} \gtrapprox {1/\sqrt{d}}$ an exponential sample complexity is unavoidable to identify an arm with positive return. This does not contradict our result, because our regret is $\overset{\sim}{O}{(K)}$ under such large misspecification, which is vacuous as the maximum loss up to episode $K$ is exactly $K$.

Notice that the equivalence is established by informing Eleanor of the setting (through the horizon $H = 1$) unlike. Finally, if the corruption $f{( \cdot )}$ is only a function of the context then it is possible to do much better.

This surprising connection with the popular LinUCB makes Eleanor (or LinUCB with a correction on the exploration bonus) the first algorithm capable of handling misspecified *contextual* linear bandits, although we are not the first to consider misspecification in linear bandits per se: propose an algorithm that switches to tabular if misspecification is detected and consider the case that the misspecification is less than roughly the action gap; comment on the lower bound by using the Eluder dimension. Finally, have recently obtained a result similar to ours, but for a different setting. Their algorithm can leverage having finitely many actions (where a $\sqrt{d}$ factor can be saved; otherwise their regret is the same as ours) but relies heavily on $G$-experimental design: the algorithm will not work without a stationary action set, ruling out the important case of contextual linear bandits where the action is allowed to depend on the context. However, our correction to vanilla LinUCB relies on having knowledge of the misspecification, while the approach of is agnostic. Furthermore, concurrently to our work also consider the same modification to LinUCB as we do here, and provide proof that the algorithm can fail if no modification is implemented. However, these definitions of misspecification are adversarial in nature, and for less pathological problems the algorithm is expected to perform well.

## Lower Bounds

In terms of statistical rate, Eleanor is unimprovable due to a lower bound directly borrowed from the bandit literature.

### Proposition 1 (Lower Bound Without Misspecification)

Let $\overset{\sim}{d}\overset{def}{=}{\sum_{t = 1}^{H}d_{t}}$. There exist a class of $H$-horizon MDPs that satisfy asm. 1. ‣ 5 Main Result: Regret Upper Bound ‣ Learning Near Optimal Policies with Low Inherent Bellman Error") and $H$ feature maps ${\phi_{t}{( \cdot, \cdot )}} \in {\mathbb{R}}^{d_{t}}$, with $\overset{\sim}{d} \geq {2H}$ such that for $K = {\Omega{({\overset{\sim}{d}}^{2})}}$ the expected regret of any algorithm is $\Omega{({\overset{\sim}{d}\sqrt{K}})}$.

The fact that our result matches the lower bound can appear surprising, because our work relies on a sub-Gaussian conditions and disregards the variance in the process. It does not use a "law of total variance" argument, which was necessary in the past to obtain rate-optimal algorithms for tabular settings. One may wonder whether a $\sqrt{H}$ factor can be saved by that argument for MDPs parameterized by linear action-value function. Due to the bandit lower bound, no such improvement is possible with linear function approximations, unless the structure is restricted further. The reason is that our setting is a superset of tabular RL and contains harder instances than the lower bound for tabular RL (in particular, a linear bandit problem at a single timestep) but the law of total variance would bring no benefit to those structures.

Approximation error Our positive result regarding misspecification matches the LSPI analysis of but for the harder *online* setting. Although the two respective frameworks (i.e., LSPI vs LSVI conditions) are incompatible as explained in definition 1, we notice a similar effect: a square-root factor of the problem dimensionality multiplies the "misspecification" error. While the LSPI analysis of relies on having features from $G$-optimal design to query the system, *in the online setting we're not free to choose arbitrary features anywhere in the state-action space*. As a result, the agent can learn on an ill-conditioned basis, and the prediction error on features much different from those experienced can be very large. Our analysis shows that while this can indeed be the case, the situation of high prediction error cannot persist for too long and the $\sqrt{d}$ loss in prediction accuracy is, *on average*, recovered. Using the recent result by, we can augment 1. ‣ 7 Lower Bounds ‣ Learning Near Optimal Policies with Low Inherent Bellman Error") by including a sequence of misspecified linear bandits, obtaining the following result (see also appendix D):

\[Lower Bound for Inherent Bellman Error Setting\]thmLowerBound There exist feature maps $\phi_{1},\ldots,\phi_{H}$ that define an MDP class $\mathcal{M}$ such that every MDP in that class satisfies assumption 1. ‣ 5 Main Result: Regret Upper Bound ‣ Learning Near Optimal Policies with Low Inherent Bellman Error") with inherent Bellman error $\mathcal{I}$ and such that the expected regret of any algorithm on at least a member of the class (for ${A \geq 3},{{d_{t} \geq 3},{K = {\Omega{({({\sum_{t = 1}^{H}d_{t}})}^{2})}}}}$) is $\Omega{({{\sum_{t = 1}^{H}{d_{t}\sqrt{K}}} + {\sum_{t = 1}^{H}{\sqrt{d_{t}}\mathcal{I}K}}})}$, that is:

## Proof Overview

We now give a quick proof sketch and highlighting how working in the parameter space allows us to 1) avoid an exponential propagation of the errors by leveraging the notion of inherent Bellman error (handling of the bias) and 2) preserve confidence intervals that are as tight as in a bandit problem (handling of the variance). Our objective is to bound the regret: ${\text{Regret}{(K)}}\overset{def}{=}{\sum_{k = 1}^{K}{\left( {V_{1}^{\star} - V_{1}^{\pi_{k}}} \right){(s_{1k})}}}$ for the chosen policies $\pi_{k}$, but first we need to discuss how the errors propagate and how to ensure optimism.

### Propagation of errors

The inherent Bellman error condition ensures that there exists a parameter ${\mathring{\theta}}_{t}$ and a Bellman residual function ${\mathring{\Delta}}_{t}$, both depending on ${\overline{Q}}_{t + 1}$, such that ${{\mathring{\Delta}}_{t}{({\overline{Q}}_{t + 1})}{(s,a)}} =$

with $\parallel {\mathring{\Delta}}_{t}{({\overline{Q}}_{t + 1})}) \parallel_{\infty} \leq \mathcal{I}$ *provided that* ${\overline{Q}}_{t + 1} \in \mathcal{Q}_{t + 1}$. In other words, we can successfully represent $\mathcal{T}_{t}{\overline{Q}}_{t + 1}$ up to an additive error $\mathcal{I}$ *if the next-step ${\overline{Q}}_{t + 1}$ function is linear*.

This representational constraint unfortunately rules out adding exploration bonuses as in prior low-rank work as well as in tabular MDPs; their addition can have the backup $\mathcal{T}_{t}{\overline{Q}}_{t + 1}$ leave the linear space (which is equivalent to having large $\mathcal{I}$) and can lead to divergence of the repeated least-square procedure.

Error decomposition We aim to compute the error encountered in minimizing eq. 4 with $V_{t + 1} = {\overline{V}}_{t + 1}$ fixed and no regularization. Denote with $s_{ti}$ the $i$-th state encountered at timestep $t$ of episode $i$, and let $a_{ti} = {\pi_{ti}{(s_{ti})}}$. Define the $i$-th sample noise ${\eta_{ti}{({\overline{V}}_{t + 1})}}\overset{def}{=}{{{r_{ti} - {r_{t}{(s_{ti},a_{ti})}}} + {{\overline{V}}_{t + 1}{(s_{{t + 1},i})}}} - {{{\mathbb{E}}_{s^{\prime} \sim {p_{t}{(s_{ti},a_{ti})}}}{\overline{V}}_{t + 1}}{(s^{\prime})}}}$ and the misspecification ${{\mathring{\Delta}}_{ti}{({\overline{Q}}_{t + 1})}}\overset{def}{=}{{\mathring{\Delta}}_{t}{({\overline{Q}}_{t + 1})}{(s_{ti},a_{ti})}}$. Premultiply ${\hat{\theta}}_{tk}$ (which minimizes eq. 4) by $\phi_{t}{(s,a)}^{\top}$ and use the definitions just introduced: ${\phi_{t}{(s,a)}^{\top}{\hat{\theta}}_{tk}} =$

We discuss the main error terms below.

Inherent Bellman error Cauchy-Schwartz and a projection argument (lemma 8. ‣ C.6 Projection Bound ‣ Appendix C Eleanor ‣ Learning Near Optimal Policies with Low Inherent Bellman Error")) gives:

The inability to correctly represent the application of the Bellman operator could be exploited adversarially to introduce an error that grows with $\sqrt{k}$ (where $k$ is the number of episodes). On average, however, the $\Sigma_{tk}^{- 1}$-norm of those features that are selected shrinks as ${\|{\phi_{t}{(s,a)}}\|}_{\Sigma_{tk}^{- 1}} \approx \sqrt{d_{t}/k}$. While the agent can select a $(s,a)$ pair where the product ${\|{\phi_{t}{(s,a)}}\|}_{\Sigma_{tk}^{- 1}}\sqrt{k}\mathcal{I}$ can be large, this cannot happen for too long. Intuitively, a large prediction error is made only on features that are significantly different from those seen in the past, but trying those features reveals the correct prediction, which decreases the prediction error for that direction in the future.

Noise error and covering argument Cauchy-Schwartz again gives

where $\beta_{tk}$ follows from the self normalizing bound of modified to cover the functional space $\mathcal{V}_{t}$. The covering argument is necessary since the noise depends on ${\overline{V}}_{t + 1}$ which is itself random. More precisely, we can write $\sqrt{\beta_{tk}} \lessapprox \sqrt{{\ln{\det{(\Sigma_{tk})}^{\frac{1}{2}}}} + {\ln\mathcal{N}}}$, where $\mathcal{N}$ is the covering number to $\epsilon$ accuracy of $\mathcal{V}_{t + 1}$. The determinant-trace inequality (see lemma 10 of ) bounds the volume of the covariance matrix ${\ln{\det{(\Sigma_{tk})}^{\frac{1}{2}}}} = {\overset{\sim}{O}{(d_{t})}}$; fortunately the metric entropy $\ln\mathcal{N}$ is of the same order. To see this, remember that to cover $\mathcal{V}_{t}$ it is sufficient to cover $\mathcal{B}_{t}$, which is a $d_{t}$ dimensional object ($\subset {\mathbb{R}}^{d_{t}}$), and hence ${\ln\mathcal{N}} = {\overset{\sim}{O}{(d_{t})}}$. Therefore, despite having an additional union bound compared to because of the moving target ${\overline{V}}_{t + 1}$, our confidence intervals are of the same order of magnitude.

This is the place where a $\sqrt{d_{t}}$ can be saved compared to for example, which need to do a union bound over a more complicated function class because of the exploration bonuses.

Final expression Adding $\phi_{t}{(s,a)}^{\top}{\overline{\xi}}_{t}$ to both sides of eq. 8 and using the bounds just derived gives ${|{\left( {{\overline{Q}}_{t} - {\mathcal{T}_{t}{\overline{Q}}_{t + 1}}} \right){(s,a)}}|} =$

It remains to define $\alpha_{tk}$, which controls the size of optimization parameters, justifying eq. 6.

### Feasibility, best approximator and optimism

A key point of optimistic approaches for exploration is to overestimate the value of policies by assigning them a statistically plausible return, and play the policy with the highest such value.

Since the optimal value function is an upper bound to the value of all policies, technically an optimistic learner is only required to identify a policy with value at least as high as $V_{1}^{\star}$ while satisfying some confidence intervals. To show it possible to achieve this with our formulation, we will find a feasible solution to the program of definition 2. ‣ 4 Algorithm ‣ Learning Near Optimal Policies with Low Inherent Bellman Error") that is "close" to $V^{\star}$. In general $V_{t}^{\star} \notin \mathcal{V}_{t}$, and so we need to define the "best" approximator in $\mathcal{V}_{t}$ for $V_{t}^{\star}$. We denote its parameter with $\theta_{t}^{\star} \in \mathcal{B}_{t}$, inductively defined (see def. 4. ‣ C.3 Best Approximant and its Properties ‣ Appendix C Eleanor ‣ Learning Near Optimal Policies with Low Inherent Bellman Error") in appendix) as the parameter one obtains by applying the *exact* Bellman operator and then by minimizing the $\infty$ norm of the Bellman residual: $\theta_{t}^{\star}\overset{def}{=}$

If $\mathcal{I} = 0$ then ${\phi_{t}{(s,a)}^{\top}\theta_{t}^{\star}} = {Q_{t}^{\star}{(s,a)}}$ inductively follows.

Computation of $\alpha_{tk}$ Under an inductive argument, assume the program of definition 2. ‣ 4 Algorithm ‣ Learning Near Optimal Policies with Low Inherent Bellman Error") admits a partial solution ${\overline{\xi}}_{t + 1},\ldots,{\overline{\xi}}_{H}$ that satisfies ${{\overline{\theta}}_{t + 1} = {\theta_{t + 1}^{\star},\ldots}},{{\overline{\theta}}_{H} = \theta_{H}^{\star}}$ (the parameters for timesteps less than $t + 1$ have not been decided yet).

and adding $\phi_{t}{(s,a)}^{\top}{\overline{\xi}}_{t}$ back to eq. 8 evaluated with ${\overline{Q}}_{t + 1} = {Q_{t + 1}{(\theta_{t + 1}^{\star})}}$ can "undo" the effect of noise and approximation error at timestep $t$, producing (recall ${\overline{\theta}}_{t} = {{\hat{\theta}}_{t} + {\overline{\xi}}_{t}}$)

Comparing with eq. 10 we can claim ${\overline{\theta}}_{t} = \theta_{t}^{\star}$, completing the induction. Thus, the best approximator defined through $\theta_{t}^{\star}$ is a feasible solution to the program of definition 2. ‣ 4 Algorithm ‣ Learning Near Optimal Policies with Low Inherent Bellman Error"). The corresponding value function $V_{t}{(\theta_{t}^{\star})}$ can make an error of size $\mathcal{I}$ in representing the Bellman backup, and this accumulates linearly, and hence Eleanor is ultimately nearly-optimistic:

As we'll see in a second, this near-optimism is enough to obtain a solid regret bound. Finally, eq. 11 gives:

which matches eq. 6 after adding the regularization term.

### Regret Bound

Finally, we can present the regret bound, which now follows similarly to prior analyses for model free algorithms (e.g., ). Consider the usual decomposition from the starting state $s_{1k}$:

The first term inside the parenthesis can be bounded by eq. 12; we can expand the second term using eq. 9 where $\pi_{k}$ is the agent's policy in episode $k$ and $a_{tk} = {\pi_{tk}{(s_{tk})}}$ for short. For a generic timestep $t$ we obtain

Now write ${{\mathbb{E}}_{s^{\prime} \sim {p_{t}{(s_{tk},a_{tk})}}}\left( {{\overline{V}}_{{t + 1},k} - V_{t + 1}^{\pi_{k}}} \right)}{(s^{\prime})}$ as $\left( {{\overline{V}}_{{t + 1},k} - V_{t + 1}^{\pi_{k}}} \right){(s_{{t + 1},k})}$ plus a martingale term ${\overset{˙}{\zeta}}_{tk}$ which we ignore for brevity (details in appendix). Induction over $t \in {\lbrack H\rbrack}$ and summing over $k \in {\lbrack K\rbrack}$ gives $\sum_{k = 1}^{K}{\sum_{t = 1}^{H}{\left( {{\overline{V}}_{1k} - V_{1}^{\pi_{k}}} \right){(s_{1k})}}}$

Recall ${\sum_{k = 1}^{K}{\|{\phi_{t}{(s_{tk},a_{tk})}}\|}_{\Sigma_{tk}^{- 1}}} = {\overset{\sim}{O}{(\sqrt{d_{t}K})}}$ from; substituting this concludes.

## Conclusion

We have introduced an algorithm for online exploration with linear approximators under the notion of low-inherent Bellman error with an optimal regret bound with regards to statistical rates and the lack of closedness of the Bellman operator. The construction reveals that a shift to global optimization might be unavoidable with more general linear approximators than prior low-rank work, making computational tractability harder to achieve. A core idea is that by working directly in the parameter space we enable a linear propagation of the errors (as opposed to exponential) and we limit the complexity of the value function class, which can serve as inspiration to improve the statistical efficiency for other algorithms as well. Finally, a noteworthy contribution is our analysis for misspecified contextual linear bandit, which explains that a simple modification of a mainstream algorithm is sufficient to handle such setting.
