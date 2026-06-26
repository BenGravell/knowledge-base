<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning near Optimal Policies with Low Inherent Bellman Error

Topics include Low-rank models, Reinforcement learning, Bellman equations, Value iteration, Bandits, Regret bounds, Online algorithms, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the exploration problem with approximate linear action-value functions in episodic reinforcement learning under the notion of low inherent Bellman error, a condition normally employed to show convergence of approximate value iteration. First we relate this condition to other common frameworks and show that it is strictly more general than the low rank (or linear) MDP assumption of prior work. Second we provide an algorithm with a high probability regret bound widetilde O(sum_t = 1^(H) d_t sqrt(K) + sum_t = 1^(H) sqrt(d_t) IBE K) where H is the horizon, K is the number of episodes, IBE is the value if the inherent Bellman error and d_t is the feature dimension at timestep t. In addition, we show that the result is unimprovable beyond constants and logs by showing a matching lower bound.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This has two important consequences: 1) it shows that exploration is possible using only batch assumptions with an algorithm that achieves the optimal statistical rate for the setting we consider, which is more general than prior work on low-rank MDPs 2) the lack of closedness (measured by the inherent Bellman error) is only amplified by sqrt(d_t) despite working in the online setting. Finally, the algorithm reduces to the celebrated \textsc{LinUCB} when H = 1 but with a different choice of the exploration parameter that allows handling misspecified contextual linear bandits. While computational tractability questions remain open for the MDP setting, this enriches the class of MDPs with a linear representation for the action-value function where statistically efficient reinforcement learning is possible.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Improving the sample efficiency of reinforcement learning (RL) algorithms through effective exploration-exploitation strategies is a major focus of the recent theoretical literature. Strong results are available with a generative model as well as in the *online* setting when the learning performance is measured by the cumulative regret, i.e., the difference between the performance of the optimal policy and the reward accumulated by the learner. For finite horizon problems, UCBVI achieves worst-case optimal regret, while algorithms with domain adaptive bounds have been introduced by and. Randomized and model-free variants have also been proposed, together with methods with other beneficial properties. Similar results are also available in the infinite horizon setting.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Approximate dynamic programming. While the results for tabular settings are encouraging, function approximation is normally required to tackle problems where the state or action spaces may be intractably large. In this case, even when the Bellman operator can be applied exactly, simple dynamic programming algorithms coupled with linear architectures may diverge, thus suggesting that effective approximate RL may not be feasible in the general case.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Convergence guarantees and finite-sample analyses are available for the least-squares policy improvement (LSPI) algorithm under the assumption that the value function of *all policies can be well approximated* within the chosen function class (*LSPI conditions*, for short). For concreteness, let $\epsilon$ be the worst-case misspecification error of a $d$-dimensional linear function approximator over the policy action-value functions (i.e., for any policy $\pi$, there exists an approximation ${\hat{Q}}^{\pi}$ such that ${\|{{\hat{Q}}^{\pi} - Q^{\pi}}\|} \leq \epsilon$). Recently, showed that when using highly misspecified approximators $\epsilon \gtrapprox {1/\sqrt{d}}$ the worst-case sample complexity may be exponential in $d$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

At the same time, when $\epsilon \lessapprox {1/\sqrt{d}}$, and showed algorithms with $\sqrt{d}$ loss times the misspecification level $\epsilon$. In particular, showed that LSPI attains polynomial sample complexity using $G$-optimal design with a $\approx {\sqrt{d}\epsilon}$ additive error using a *generative model*.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Similarly, for the least-squares value iteration algorithm (LSVI) convergence guarantees and finite sample analysis are also available under the assumption of low inherent Bellman error (IBE), (*LSVI conditions*, for short). Given a function class $\mathcal{F}$, the IBE measures the error in approximating the image of any function in $\mathcal{F}$ through the Bellman operator. Whenever the IBE is not small, it is easy to show that approximation errors may be amplified by a constant factor at each application of the Bellman operator, leading to divergence. Although methods exist to limit this amplification of errors, the question of when sample-efficient value-based RL is possible remains open even in the absence of misspecification.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we focus on the problem of exploration-exploitation using LSVI approaches in settings with low IBE. We make several contributions.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Exploration with low inherent Bellman error. We first show that the notion of inherent Bellman error is distinct from the LSPI condition, and more general than the low-rank assumption on the dynamics used in a series of recent works on exploration with linear function approximation. For a finite horizon MDP, when the LSVI conditions are satisfied either exactly or approximately (i.e., the inherent Bellman error is either zero or small) we propose *Efficient Linear Exploration of Actions by Nonlinear Optimization of the Residuals* (Eleanor), an optimistic generalization of the popular LSVI algorithm. We analyze Eleanor and derive the first regret bound for this setting and show it is unimprovable in terms of statistical rates, though we leave its computational tractability open.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our analysis shows that the performance of Eleanor degrades gracefully in the case of positive inherent Bellman error. Interestingly, we recover a similar $\sqrt{d}$ amplification of the misspecification error (the IBE in our case) as for LSPI, despite the fact that we consider the more challenging online setting as opposed to the generative model by Lattimore & Szepesvari.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Low-rank MDPs and contextual misspecified linear bandits. Our result applies to low-rank MDPs and improves upon the best-known regret bound for that setting by a $\sqrt{d}$ factor. When applied to contextual linear bandits, our algorithm reduces to the celebrated LinUCB (or Oful) algorithm of. In addition, however, it *can handle contextual misspecified linear bandits while retaining computationally tractability*, making this the first algorithm and analysis for this setting, although we require knowledge of the misspecification level. A similar result was recently derived for a different algorithm based on $G$-experimental design for the more restrictive setting of non-contextual (i.e., with features not depending on the state and fixed action space) misspecified linear bandits; however, their approach is agnostic to the misspecification level.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Core ideas. LSVI-based algorithms have been successfully analyzed for low-rank MDPs by adding exploration bonuses at every experienced state, thereby ensuring optimism by backward induction. In contrast, our more general setting demands that the value function stays linear, ruling out approaches based on exploration bonuses. In fact, if the value function used for backup is not linear, low inherent Bellman error does not provide any guarantee about how errors may propagate, which can be exponential in the general case.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our proposal extends the LSVI algorithm to return an optimistic solution at the initial state through *global* optimization over the value function parameters, while still enforcing linearity of the representation. This has two advantages: 1) (*handling of the bias*) it enables us to use the concept of inherent Bellman error, requiring that the Bellman operator be applied to *linear* action-value functions and avoiding a $\sqrt{d}$ amplification of the value function error at every step; 2) (*handling of the variance*) it keeps the complexity of the action-value functional space small (linear), enabling the use of confidence intervals that are as tight as those used in the bandit literature, yielding the optimal finite-sample statistical rate.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Linear Value Function Frameworks", "weight": 1.0} -->

In this section we introduce basic notation and assumptions for linear function approximation, we define the concept of inherent Bellman error, and we investigate connections with alternative settings.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Linear Value Function Frameworks", "weight": 1.0} -->

Whenever the state space $\mathcal{S}$ is too large or continuous, value functions cannot be represented by enumerating their values at each state or state-action pair. A common approach is to define a feature map $\phi_{t}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}^{d_{t}}}$, possibly different at any $t \in {\lbrack H\rbrack}$, embedding each state-action pair $(s,a)$ into a $d_{t}$-dimensional vector $\phi_{t}{(s,a)}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Linear Value Function Frameworks", "weight": 1.0} -->

The action-value functions are then represented as a linear combination between the features $\phi_{t}$ and a vector parameter $\theta_{t} \in {\mathbb{R}}^{d_{t}}$, such that ${Q_{t}{(s,a)}} = {\phi_{t}{(s,a)}^{\top}\theta_{t}}$. This effectively reduces the complexity of the problem from $|{\mathcal{S} \times \mathcal{A}}|$ down to $d_{t}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Linear Value Function Frameworks", "weight": 1.0} -->

We define the space of parameters $\theta$ inducing uniformly bounded action-value functions We will later require the constant $D \in {\mathbb{R}}$ to be chosen to satisfy Asm. 1. ‣ 5 Main Result: Regret Upper Bound ‣ Learning Near Optimal Policies with Low Inherent Bellman Error"). For instance, $D = 1$ requires the value function to be in $\lbrack{- 1},{+ 1}\rbrack$ and complies with the assumption.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Linear Value Function Frameworks", "weight": 1.0} -->

Each parameter $\theta$ identifies an (action) value function and the associated functional spaces Inherent Bellman error. The value iteration algorithm can be used to compute an optimal policy and it smoothly extends to linear approximators. The procedure repeatedly applies the Bellman operator $\mathcal{T}_{t}$ to an action-value function^11^1One can reason with either the value function $V$ or the action-value function $Q$. $Q_{t} \in \mathcal{Q}_{t}$ and projects the computed point $\mathcal{T}_{t}Q_{t}$ back to $\mathcal{Q}_{t + 1}$ using a (e.g., least-squares) projection operator $\Pi_{t}$. The projection error is precisely the inherent Bellman error, which can be thought of as how close the space $\mathcal{Q}_{t}$ is w.r.t. the Bellman operator $\mathcal{T}_{t}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Algorithm", "weight": 1.0} -->

We consider the standard online learning protocol in finite-horizon problems, where at each episode $k$, the learner executes a policy $\pi_{k}$, records the samples in the trajectory, updates the policy and reiterates over the next episode. We first recall the standard LSVI. At the beginning of episode $k$, consider timestep $t$ and assume the next-step parameter is fixed and equal to $\theta_{t + 1}$. The objective function of the regularized least-square is where ${\{\phi_{ti}\}}_{i = {1,\ldots,{k - 1}}}$ are the features observed at timestep $t$ in state $s_{ti}$ and $r_{ti}$ are the corresponding rewards.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Algorithm", "weight": 1.0} -->

We introduce an optimistic variant of LSVI, where the optimistic parameters are chosen by solving a global optimization problem across the whole horizon $H$. At each episode, Eleanor (in Alg. 1) solves the following problem.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 1 (Main Assumption)", "weight": 1.0} -->

In particular, if the reward are in $\lbrack 0,1\rbrack$ and $D = 1$ in eq. 1, which gives ${\overline{V}{(\cdot)}} \in {\lbrack{- 1},1\rbrack}$, then this condition is automatically satisfied. Finally, the bound on the parameter limits the bias introduced by regularization which scales with the norm of the parameter, but a psedoinverse computation would relax this requirement.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 1 (Main Assumption)", "weight": 1.0} -->

After rescaling, however, our assumptions are much weaker the the usual setting that requires ${r_{t}{( \cdot, \cdot )}} \in {\lbrack 0,1\rbrack}$ and ${V_{t}^{\pi}{( \cdot )}} \in {\lbrack 0,H\rbrack}$ since we allow the reward to be of the same order as the value function after rescaling and even be negative. This is a harder setting.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 1 (Main Assumption)", "weight": 1.0} -->

\[Main Result\]thmMainResult Under assumption 1. ‣ 5 Main Result: Regret Upper Bound ‣ Learning Near Optimal Policies with Low Inherent Bellman Error") with $\lambda = 1$, with probability at least $1 - \delta$ jointly over all episodes it holds that the regret of Eleanor is bounded: There are no additional "lower order" terms in the above display, although the $\overset{\sim}{O}{(\cdot)}$ notation hides, as usual, logarithms of $d_{t},H,K,{1/\delta}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 1 (Main Assumption)", "weight": 1.0} -->

Care must be taken when comparing across settings with different scaling. In particular, *rescaling the problem* (i.e., the reward function) *by $H$* increases the sub-Gaussian norm of the rewards and transitions, and the value of the inherent Bellman error alike, yielding *an extra $H$ factor in the regret bound*. For example, in the setting that the rewards are bounded in $\lbrack 0,1\rbrack$ and the value function is in $\lbrack 0,H\rbrack$ with $d_{1} = \cdots = d_{H}\overset{def}{=}d$ and $\mathcal{I} = 0$ for simplicity, the above regret bound reduces (with $T = {KH}$) to $\overset{\sim}{O}{({dH^{\frac{3}{2}}\sqrt{T}})}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Assumption 1 (Main Assumption)", "weight": 1.0} -->

Low-rank MDPs As explained in definition 1, our result applies to low-rank MDPs; surprisingly, this shows that at least $\sqrt{d}$ improvement is possible in the main rate compared to the best-known $\overset{\sim}{O}{({{({dH})}^{3/2}\sqrt{T}})}$ of upper bound despite Eleanor is not specifically tailored to handle low-rank MDPs. This is possible because Eleanor looks for optimistic solutions directly in the $\theta$ parameter space instead of perturbing the value function by an exploration bonus as. When the value function is perturbed by a bonus, it grows in complexity as it departs from the linear space; this requires an additional union bound over a more complicated value function class and ultimately loses a $\sqrt{d}$ factor. Finally, the inherent Bellman error covers the notion of approximate low-rank MDPs, and on the misspecification regret term we save a $\sqrt{d}$ factor as well thanks to a more careful projection argument in lemma 8.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Assumption 1 (Main Assumption)", "weight": 1.0} -->

‣ C.6 Projection Bound ‣ Appendix C Eleanor ‣ Learning Near Optimal Policies with Low Inherent Bellman Error").

<!-- chunk {"id": "body-0028", "role": "body", "section": "Contextual Misspecified Linear Bandits", "weight": 1.0} -->

Our framework reduces to bandits with linear approximators when $H = 1$ (we drop the time subscript $t$ in this case): Eleanor can handle *contextual misspecified linear bandits*, where contextual refers to allowing the action set to change as the feature extractor can be a function of the context. It follows from the definition that the inherent Bellman error is the reward function misspecification in this case.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Lower Bounds", "weight": 1.0} -->

In terms of statistical rate, Eleanor is unimprovable due to a lower bound directly borrowed from the bandit literature.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Propagation of errors", "weight": 1.0} -->

This representational constraint unfortunately rules out adding exploration bonuses as in prior low-rank work as well as in tabular MDPs; their addition can have the backup $\mathcal{T}_{t}{\overline{Q}}_{t + 1}$ leave the linear space (which is equivalent to having large $\mathcal{I}$) and can lead to divergence of the repeated least-square procedure.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Propagation of errors", "weight": 1.0} -->

Inherent Bellman error Cauchy-Schwartz and a projection argument (lemma 8. ‣ C.6 Projection Bound ‣ Appendix C Eleanor ‣ Learning Near Optimal Policies with Low Inherent Bellman Error")) gives: The inability to correctly represent the application of the Bellman operator could be exploited adversarially to introduce an error that grows with $\sqrt{k}$ (where $k$ is the number of episodes). On average, however, the $\Sigma_{tk}^{- 1}$-norm of those features that are selected shrinks as ${\|{\phi_{t}{(s,a)}}\|}_{\Sigma_{tk}^{- 1}} \approx \sqrt{d_{t}/k}$. While the agent can select a $(s,a)$ pair where the product ${\|{\phi_{t}{(s,a)}}\|}_{\Sigma_{tk}^{- 1}}\sqrt{k}\mathcal{I}$ can be large, this cannot happen for too long.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Propagation of errors", "weight": 1.0} -->

Intuitively, a large prediction error is made only on features that are significantly different from those seen in the past, but trying those features reveals the correct prediction, which decreases the prediction error for that direction in the future.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Propagation of errors", "weight": 1.0} -->

Noise error and covering argument Cauchy-Schwartz again gives where $\beta_{tk}$ follows from the self normalizing bound of modified to cover the functional space $\mathcal{V}_{t}$. The covering argument is necessary since the noise depends on ${\overline{V}}_{t + 1}$ which is itself random. More precisely, we can write $\sqrt{\beta_{tk}} \lessapprox \sqrt{{\ln{\det{(\Sigma_{tk})}^{\frac{1}{2}}}} + {\ln\mathcal{N}}}$, where $\mathcal{N}$ is the covering number to $\epsilon$ accuracy of $\mathcal{V}_{t + 1}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Propagation of errors", "weight": 1.0} -->

Therefore, despite having an additional union bound compared to because of the moving target ${\overline{V}}_{t + 1}$, our confidence intervals are of the same order of magnitude.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Propagation of errors", "weight": 1.0} -->

This is the place where a $\sqrt{d_{t}}$ can be saved compared to for example, which need to do a union bound over a more complicated function class because of the exploration bonuses.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Propagation of errors", "weight": 1.0} -->

Final expression Adding $\phi_{t}{(s,a)}^{\top}{\overline{\xi}}_{t}$ to both sides of eq. 8 and using the bounds just derived gives ${|{\left({{\overline{Q}}_{t} - {\mathcal{T}_{t}{\overline{Q}}_{t + 1}}} \right){(s,a)}}|} =$ It remains to define $\alpha_{tk}$, which controls the size of optimization parameters, justifying eq. 6.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Feasibility, best approximator and optimism", "weight": 1.0} -->

A key point of optimistic approaches for exploration is to overestimate the value of policies by assigning them a statistically plausible return, and play the policy with the highest such value.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Feasibility, best approximator and optimism", "weight": 1.0} -->

Since the optimal value function is an upper bound to the value of all policies, technically an optimistic learner is only required to identify a policy with value at least as high as $V_{1}^{\star}$ while satisfying some confidence intervals. To show it possible to achieve this with our formulation, we will find a feasible solution to the program of definition 2. ‣ 4 Algorithm ‣ Learning Near Optimal Policies with Low Inherent Bellman Error") that is "close" to $V^{\star}$. In general $V_{t}^{\star} \notin \mathcal{V}_{t}$, and so we need to define the "best" approximator in $\mathcal{V}_{t}$ for $V_{t}^{\star}$. We denote its parameter with $\theta_{t}^{\star} \in \mathcal{B}_{t}$, inductively defined (see def. 4.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Feasibility, best approximator and optimism", "weight": 1.0} -->

‣ C.3 Best Approximant and its Properties ‣ Appendix C Eleanor ‣ Learning Near Optimal Policies with Low Inherent Bellman Error") in appendix) as the parameter one obtains by applying the *exact* Bellman operator and then by minimizing the $\infty$ norm of the Bellman residual: $\theta_{t}^{\star}\overset{def}{=}$ If $\mathcal{I} = 0$ then ${\phi_{t}{(s,a)}^{\top}\theta_{t}^{\star}} = {Q_{t}^{\star}{(s,a)}}$ inductively follows.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Feasibility, best approximator and optimism", "weight": 1.0} -->

Computation of $\alpha_{tk}$ Under an inductive argument, assume the program of definition 2. ‣ 4 Algorithm ‣ Learning Near Optimal Policies with Low Inherent Bellman Error") admits a partial solution ${\overline{\xi}}_{t + 1},\ldots,{\overline{\xi}}_{H}$ that satisfies ${{\overline{\theta}}_{t + 1} = {\theta_{t + 1}^{\star},\ldots}},{{\overline{\theta}}_{H} = \theta_{H}^{\star}}$ (the parameters for timesteps less than $t + 1$ have not been decided yet). and adding $\phi_{t}{(s,a)}^{\top}{\overline{\xi}}_{t}$ back to eq.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Feasibility, best approximator and optimism", "weight": 1.0} -->

8 evaluated with ${\overline{Q}}_{t + 1} = {Q_{t + 1}{(\theta_{t + 1}^{\star})}}$ can "undo" the effect of noise and approximation error at timestep $t$, producing (recall ${\overline{\theta}}_{t} = {{\hat{\theta}}_{t} + {\overline{\xi}}_{t}}$) Comparing with eq. 10 we can claim ${\overline{\theta}}_{t} = \theta_{t}^{\star}$, completing the induction. Thus, the best approximator defined through $\theta_{t}^{\star}$ is a feasible solution to the program of definition 2. ‣ 4 Algorithm ‣ Learning Near Optimal Policies with Low Inherent Bellman Error").

<!-- chunk {"id": "body-0042", "role": "body", "section": "Feasibility, best approximator and optimism", "weight": 1.0} -->

The corresponding value function $V_{t}{(\theta_{t}^{\star})}$ can make an error of size $\mathcal{I}$ in representing the Bellman backup, and this accumulates linearly, and hence Eleanor is ultimately nearly-optimistic: As we'll see in a second, this near-optimism is enough to obtain a solid regret bound. Finally, eq. 11 gives: which matches eq. 6 after adding the regularization term.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have introduced an algorithm for online exploration with linear approximators under the notion of low-inherent Bellman error with an optimal regret bound with regards to statistical rates and the lack of closedness of the Bellman operator. The construction reveals that a shift to global optimization might be unavoidable with more general linear approximators than prior low-rank work, making computational tractability harder to achieve. A core idea is that by working directly in the parameter space we enable a linear propagation of the errors (as opposed to exponential) and we limit the complexity of the value function class, which can serve as inspiration to improve the statistical efficiency for other algorithms as well. Finally, a noteworthy contribution is our analysis for misspecified contextual linear bandit, which explains that a simple modification of a mainstream algorithm is sufficient to handle such setting.
