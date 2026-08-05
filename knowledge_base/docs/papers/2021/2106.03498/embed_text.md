<!-- arxiv-full-text:v1 {"arxiv_id": "2106.03498", "source": "ar5iv"} -->

## Introduction

Inverse reinforcement learning aims to use observations of agents' actions to determine their reward function. The problem has roots in the very early stages of optimal control theory; Kalman raised the question of whether, by observation of optimal policies, one can recover coefficients of a quadratic cost function (see also Boyd et al. ). This question naturally generalizes to the generic framework of Markov decision process and stochastic control.

In the 1970s, these questions were taken up within economics, as a way of determining utility functions from observations. For instance, Keeney and Raiffa set out to determine a proper ordering of all possible states which are deterministic functions of actions. In this setup, the problem is static and the outcome of an action is immediate. Later in Sargent, a dynamic version of a utility assessment problem was studied, under the context of finding the proper wage through observing dynamic labor demand.

As exemplified by Lucas' critique^44^4The critique is best summarized by the quotation: "Given that the structure of an econometric model consists of optimal decision rules of economic agents, and that optimal decision rules vary systematically with changes in the structure of series relevant to the decision maker, it follows that any change in \[regulatory\] policy will systematically alter the structure of econometric models." (Lucas ), in many applications it is not enough to find *some* pattern of rewards corresponding to observed policies; instead we may need to identify *the specific* rewards agents face, as it is only with this information that we can make valid predictions for their actions in a changed environment. In other words, we do not simply wish to learn a reward which allows us to imitate agents in the current environment, but which allows us to predict their actions in other settings.

In this paper, we give a precise characterization of the range of rewards which yield a particular policy for an entropy regularized Markov decision problem. This separates the main task of estimation (of the optimal policy from observed actions) from the inverse problem (of inferring rewards from a given policy). We find that even with perfect knowledge of the optimal policy, the corresponding rewards are not fully identifiable; nevertheless, the space of consistent rewards is parameterized by the value function of the control problem. In other words, the reward can be fully determined given the optimal policy and the value function, but the optimal policy gives us no direct information about the value function.

We further show that, given knowledge of the optimal policy under two different discount rates, or sufficiently different transition laws, we can uniquely identify the rewards (up to a constant shift). We also give conditions under which action-independent rewards, or time-homogenous rewards over finite horizons, can be identified. This demonstrates the fundamental challenge of inverse reinforcement learning, which is to disentangle immediate rewards from future rewards (as captured through preferences over future states).

## Background on reinforcement learning

The motivation behind inverse reinforcement learning is to use observed agent behavior to identify the rewards motivating agents. Given these rewards, one can forecast future behavior, possibly under a different environment. In a typical reinforcement learning^55^5Reinforcement learning and optimal control are closely related problems, where reinforcement learning typically focuses on the challenge of numerically learning a good control policy, while optimal control focuses on the description of the optimizer. In the context of the inverse problem we consider they are effectively equivalent and we will use the terms interchangeably. (RL) problem, an agent learns an optimal policy to maximize her total reward by interacting with the environment.

In order to analyse the inverse reinforcement learning problem, we begin with an overview of the 'primal' problem, that is, how to determine optimal policies given rewards. We particularly highlight a entropy regularized version of the Markov decision process (MDP), which provides a better-posed setting for inverse reinforcement learning. For mathematical simplicity, we focus on discrete-time problems with finitely many states and actions; our results can largely be transferred to continuous settings, with fundamentally the same proofs, however some technical care is needed.

### Discrete Markov decision processes with entropy regularization

### The environment

We consider a simple Markov decision process (MDP) on an infinite horizon. The MDP $\mathcal{M} = {(\mathcal{S},\mathcal{A},\mathcal{T},f,\gamma)}$ is described : a finite state space $\mathcal{S}$; a finite set of actions $\mathcal{A}$; a (Markov) transition kernel $\mathcal{T}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathcal{P}{(\mathcal{S})}}}$, that is, a function $\mathcal{T}$ such that $\mathcal{T}{(s,a)}$ gives probabilities^66^6Here, and elsewhere, we write $\mathcal{P}{(X)}$ for the set of all probability distributions on a set $X$. of each value of $S_{t + 1}$, given the state $S_{t} = s$ and action $A_{t} = a$ at time $t$; and a reward function $f:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$ with discount factor $\gamma \in {\lbrack 0,1)}$.

An agent aims to choose a sequence of actions $\{ A_{0},A_{1},\ldots\}$ from $\mathcal{A}$ in order to to maximize the expected value of total reward It will prove convenient for us to allow randomized policies $\pi$, that is, functions $\pi:{\mathcal{S}\rightarrow{\mathcal{P}{(\mathcal{A})}}}$, where $\pi{(\cdot |s)}$ is the distribution of actions the agent takes when in state $s$. For a given randomized policy $\pi$, we define $\mathcal{T}_{\pi} \in {\mathcal{P}{(\mathcal{S})}}$, the distribution of $S_{t + 1}$ given state $S_{t}$, by Given an initial distribution $\rho \in {\mathcal{P}{(\mathcal{S})}}$ for $S_{0}$ and a policy $\pi:{\mathcal{S}\rightarrow{\mathcal{P}{(\mathcal{A})}}}$, we obtain a (unique) probability measure ${\mathbb{P}}_{\rho}^{\pi}$ such that, and any ${a \in {\mathcal{A},s}},{s' \in \mathcal{S}}$, ${{\mathbb{P}}_{\rho}^{\pi}{({S_{0} = s})}} = {\rho{(s)}}$ and We write ${\mathbb{E}}_{\rho}^{\pi}$ for the corresponding expectation and ${\mathbb{E}}_{s}^{\pi}$ when the initial state is given by $s \in \mathcal{S}$. The classic objective in a MDP is to maximize the expected value ${\mathbb{E}}_{s}^{\pi}\left\lbrack {\sum_{t = 0}^{\infty}{\gamma^{t}f{(S_{t},A_{t})}}} \right\rbrack$. With this objective, one can show (for example, see Bertsekas and Shreve; Puterman) that there is an optimal deterministic control (i.e. a policy $\pi$, taking values zero and one, which maximizes the expected value). This implies that, typically, an optimal agent will only make use of a single action for each state, and the choice of this action will not vary smoothly with changes in the reward, discount rate, or transition kernel.

### Entropy regularised MDP

Given the lack of smoothness in the classical MDP, and to encourage exploration, a well-known variation on the classic MDP introduces a regularization term based on the Shannon entropy. Given a policy $\pi$ and regularization coefficient $\lambda \geq 0$, the entropy regularized value of a policy $\pi$, when starting in state $s$, is defined by Here ${\mathcal{H}{(\pi)}} = {- {\sum_{a \in \mathcal{A}}{\pi{(a)}{\log{({\pi{(a)}})}}}}}$ is the entropy of $\pi$. We call this setting the regularised MDP $\mathcal{M}_{\lambda} = {(\mathcal{S},\mathcal{A},\mathcal{T},f,\gamma,\lambda)}$. The optimal value is given by ${{V_{\lambda}^{\ast}{(s)}}:={{\max_{\pi}V_{\lambda}^{\pi}}{(s)}}},$ where the maximum is taken over all (randomized feedback^77^7Given the Markov structure there is no loss of generality when restricting to policies of feedback form. Further, by replacing $\mathcal{A}$ with the set of maps $\mathcal{S}\rightarrow\mathcal{A}$ if necessary, all feedback controls $a{(s)}$ can be written as deterministic controls $a{(\cdot)}$ in a larger space, so when convenient we can consider controls which do not depend on the state without loss of generality.) policies $\pi:{\mathcal{S}\rightarrow{\mathcal{P}{(\mathcal{A})}}}$.

We define the state-action value of $\pi$ at ${(s,a)} \in {\mathcal{S} \times \mathcal{A}}$ by The dynamic programming principle (e.g. Haarnoja et al.) gives Observing that on the right hand side we are maximizing over a linear function in $m$ plus an entropy term, and applying, we have that for any $s \in S$ and the maximum in is achieved by the randomized policy ${m{(a)}} = {\pi_{\lambda}^{\ast}{(\left. a \middle| s \right.)}}$, where From we see that ${\exp\left({{V_{\lambda}^{\ast}{(s)}}/\lambda} \right)} = {\sum_{a \in \mathcal{A}}{\exp\left({{Q_{\lambda}^{\pi_{\lambda}^{\ast}}{(s,a)}}/\lambda} \right)}}$ and so we can write the optimal policy as | | {\pi_{\lambda}^{\ast}{(\left. a \middle| s \right.)}} & {= {\exp\left(\left({{Q_{\lambda}^{\pi_{\lambda}^{\ast}}{(s,a)}} - {V_{\lambda}^{\ast}{(s)}}} \right)/\lambda \right)}} \\ | | | | | & {{= {\exp\left(\left({{f{(s,a)}} + {{\mathbb{E}}_{s_{1} \sim \mathcal{T}{(\cdot |s,a)}}{\lbrack{{\gammaV_{\lambda}^{\ast}{(s_{1})}} - {V_{\lambda}^{\ast}{(s)}}}\rbrack}}} \right)/\lambda \right)}},} | | | From this analysis, we make the following observations regarding the regularized MDP: The optimal policy will select all actions in $\mathcal{A}$ with some positive probabilities.

If $\lambda$ is increased, this has the effect of 'flattening out' the choice of actions, as seen in the softmax function . Conversely, sending $\lambda\rightarrow 0$ will result in a true maximizer being chosen, and the regularized problem degenerates to the classical MDP.

Adding a constant to the reward does not change the policy.

### Remark 1

In many modern approaches, one replaces dependence on the state with dependence on a space of 'features'. This has benefits when fitting a model, but does not significantly change the problem considered.

## Analysis of inverse reinforcement learning

We now shift our focus to 'inverse' reinforcement learning, that is, the problem of inferring the reward function given observation of agents' actions.

Consider a discrete time, finite-state and finite-action MDP $\mathcal{M}_{\lambda}$, as described in Section 2. Suppose a 'demonstrator' agent acts optimally, and hence generates a *trajectory* of states and actions for the system $\tau = {(s_{1},a_{1},s_{2},a_{2},\ldots)}$. We assume that it is possible for us to observe $\tau$ (over a long period), and seek to infer the reward $f$ which the agent faces.

A first observation is that, assuming each state $s \in \mathcal{S}$ appears infinitely often in the sequence $\tau$, and the agent uses a randomized feedback control $\pi_{\lambda}{(\left. a \middle| s \right.)}$, it is possible to infer this control. A simple consistent estimator for the control is Similarly, assuming each state-action pair $(s,a)$ appears infinitely often in $\tau$, we can infer the controlled transition probabilities $\mathcal{T}{(\left. s' \middle| {s,a} \right.)}$. A simple consistent estimator is given by If our agent is known to follow a regularized optimal strategy, as, and we have a simple accessibility condition^88^8In particular, for every pair of states $s,s'$, there needs to exist a finite sequence ${s = {s_{1},s_{2},\ldots}},{s_{n} = s'}$ of states and $a_{1},\ldots,a_{n - 1}$ of actions such that ${\prod_{k = 1}^{n - 1}{\mathcal{T}{(\left. s_{k + 1} \middle| {s_{k},a_{k}} \right.)}}} > 0$. This is certainly the case, for example, if we assume ${\mathcal{T}{(\left. s' \middle| {s,a} \right.)}} > 0$ for all ${s,s'} \in \mathcal{S}$ and $a \in \mathcal{A}$. on the underlying states, then every state-action pair will occur infinitely often in the resulting trajectory. Therefore, given sufficiently long observations, we will know the values of $\pi{(\left. a \middle| s \right.)}$ and $\mathcal{T}{(\left. s' \middle| {s,a} \right.)}$ for all ${s,s'} \in \mathcal{S}$ and $a \in \mathcal{A}$.

This leads, naturally, to an abstract version of the inverse reinforcement learning problem: Given knowledge of $\pi{(\left. a \middle| s \right.)}$ and $\mathcal{T}{(\left. s' \middle| {s,a} \right.)}$ for all ${s,s'} \in \mathcal{S}$ and $a \in \mathcal{A}$, and assuming $\pi$ is generated by an agent following an entropy-regularized MDP $\mathcal{M}_{\lambda}$, can we determine the initial reward function $f$ that the agent faces?

As observed by Kalman, for an unregularized controller the only thing we can say is that the observed controls are maximizers of the state-action value function, and not even that these maximizers are unique. Therefore, very little can be said about the underlying reward in the unregularized setting. Indeed, as already observed in Russell the problem of constructing a reward using state-action data is fundamentally ill-posed. One pathological case is to simply take $f$ constant, so all actions are optimal. Alternatively, if we infer a unique optimal action $a^{\star}{(s)}$ for each $s$, we then could take any ${f{(s,{a^{\star}{(s)}})}} \in {(0,\infty\rbrack}$ and ${f{(s,a)}} = 0$ for $a \neq {a^{\star}{(s)}}$.

### Further literature

One of the earliest discussions of inverse reinforcement learning (IRL) in the context of machine learning can be found in Ng and Russell. Their method is to first identify a class of reward functions, for an IRL problem with finitely many states and actions, a deterministic optimal strategy, and the assumption that the reward function depends only on the state variable. Then, assuming the reward function is expressable in terms of some known basis functions in the state, a linear programming formulation for the IRL problem is presented, to pick the reward function that maximally differentiates optimal policy from the other policies. This characterization of reward functions demonstrates the general non-uniqueness of solutions to IRL problems.

In past two decades, there have been many algorithms proposed to tackle IRL problems. One significant category of algorithms (MaxEntIRL) arises from the maximum entropy approach to optimal control. In Ziebart, IRL problems were linked with maximum causal entropy problems with statistical matching constraints. Similar models can be found in Abbeel and Ng; Ziebart et al., Levine et al. and Boularias et al.. A connection between maximum entropy IRL and GANs has been established in Finn et al.. Further related papers will be discussed in the text below.

In MaxEntIRL, one assumes that trajectories are generated^99^9As discussed by Levine, for deterministic problems this simplifies to ${P{(\tau)}} \propto {\exp{({\sum_{t}{f{(a_{t},s_{t})}}})}}$, which is often taken as a starting point. with a law for a constant $Z > 0$. Comparing with the distribution of trajectories from an optimal regularized agent, this approach implicitly assumes that ${\pi{(\left. a \middle| s \right.)}} \propto {\exp{\{{f{(a,s)}}\}}}$. Comparing, this is analogous to assuming the value function is a constant (from which we can compute $Z$) and $\lambda = 1$. This has a concrete interpretation: that many IRL methods make the tacit assumption that the demonstrator agent is myopic. As we shall see in Theorem 1, for inverse RL the value function can be chosen arbitrarily, demonstrating the consistency of this approach with our entropy-regularized agents. We discuss connections with MaxEntIRL further in Appendix Appendix: A discussion of guided cost learning and related maximum entropy inverse reinforcement learning models.

### Inverse Markov decision problems

We consider a Markov decision problem as in Section 2. As discussed above, we assume that we have full knowledge of $\mathcal{S},\mathcal{A},\mathcal{T},\gamma$, and of the regularization parameter $\lambda$ and the entropy-regularized optimal control $\pi_{\lambda}$ , but not the reward function $f$.

Our first theorem characterizes the set of all reward functions $f$ which generate a given control policy.

### Theorem 1

For a fixed policy ${\overline{\pi}{(\left. a \middle| s \right.)}} > 0$, discount factor $\gamma \in {\lbrack 0,1)}$, and an arbitrary choice of function $v:{\mathcal{S}\rightarrow{\mathbb{R}}}$, there is a unique corresponding reward function such that the MDP with reward $f$ yields a value function $V_{\lambda}^{\pi_{\lambda}^{\ast}} = v$ and entropy-regularized optimal policy $\pi_{\lambda}^{\ast} = \overline{\pi}$.

### Proof

Fix $f$ as in the statement of the theorem. Then gives the corresponding value function which rearranges to give with ${g{(s)}} = {{({{V_{\lambda}^{\ast}{(s)}} - {v{(s)}}})}/\lambda}$. Applying Jensen's inequality, we can see that, for $\underset{¯}{s} \in {{{\arg\min}_{s \in \mathcal{S}}g}{(s)}}$, However, the sum on the right is a weighted average of the values of $g$, so Combining these inequalities, along with the fact $\gamma < 1$, we conclude that ${g{(s)}} \geq 0$ for all $s \in \mathcal{S}$.

Again applying Jensen's inequality to, for $\overline{s} \in {{{\arg\max}_{s \in \mathcal{S}}g}{(s)}}$ we have As the sum on the right is a weighted average, we know Hence, as $\gamma < 1$, we conclude that ${g{(s)}} \leq 0$ for all $s \in \mathcal{S}$.

Combining these results, we conclude that $g \equiv 0$, that is, $V_{\lambda}^{\ast} = v$. Finally, we substitute the definition of $f$ and the value function $v$ into to see that the entropy-regularized optimal policy is $\pi_{\lambda}^{\ast} = \overline{\pi}$. ∎ As a consequence of this theorem, we observe that the value function is not determined by the observed optimal policy, but can be chosen arbitrarily. We also see that the space of reward functions $f$ consistent with a given policy can be parameterized by the set of value functions.

### Remark 2

A simple degrees-of-freedom argument gives this result intuitively. There are $n = {|\mathcal{S}|}$ possible states and $k = {|\mathcal{A}|}$ possible actions in each state, so the reward function can be described by a vector in ${\mathbb{R}}^{n \times k}$. From the policy, which satisfies ${\sum_{a \in \mathcal{A}}{\pi{(\left. a \middle| s \right.)}}} = 1$ for all $s$, we observe $n \times {({k - 1})}$ linearly independent values. Therefore, the space of consistent rewards has ${{n \times k} - {n \times {({k - 1})}}} = n$ free variables, which we identify with the $n$ values ${\{{v{(s)}}\}}_{s \in \mathcal{S}}$.

### Remark 3

Ng et al. provides a useful insight to our result. In Ng et al. it is assumed that the rewards are of the form $F{(S_{t},A_{t},S_{t + 1})}$; for a fixed MDP, this adds no generality, as we can write ${f{(s,a)}} = {{\mathbb{E}}{\lbrack{{\left. {F{(s,a,S_{t + 1})}} \middle| S_{t} \right. = s},{A_{t} = a}}\rbrack}}$. Ng et al. show that, for any 'shaping potential' $\Upsilon:{\mathcal{S}\rightarrow{\mathbb{R}}}$, the reward $\overset{\sim}{F} = {{F + {\gamma\Upsilon{(S_{t + 1})}}} - {\Upsilon{(S_{t})}}}$ yields the same optimal policies for *every* (unregularized) MDP. However, shaping potentials do not describe the space of all rewards corresponding to a given policy, for fixed transition dynamics. In our results, we instead parameterize a family of costs $f$ in terms of the value function (Theorem 1), and show these are the only costs which lead to the given optimal policy *for a fixed (regularized) MDP*.

Given Theorem 1, we see that it is not possible to fully identify the reward faced by a single agent, given only observations of their policy. Fundamentally, the issue is that the state-action value function $Q$ combines both immediate rewards $f$ with preferences $v$ over the future state. If we provide data which allows us to disentangle these two effects, for example by considering agents with different discount rates or transition functions, then the true reward can be determined up to a constant, as shown by our next result. In order to clearly state the result, we give the following definition.

### Definition 1

Consider a pair of Markov decision problems on the same state and action spaces, but with respective discount rates $\gamma,\overset{\sim}{\gamma}$ and transition probabilities $\mathcal{T},\overset{\sim}{\mathcal{T}}$. We say that this pair is *value-distinguishing* if, for functions ${w,\overset{\sim}{w}}:{\mathcal{S}\rightarrow{\mathbb{R}}}$, the statement implies at least one of $w$ and $\overset{\sim}{w}$ is a constant function.

In this definition, note that constant functions $w,\overset{\sim}{w}$ are always solutions to, in particular for $c \in {\mathbb{R}}$ we can set $w \equiv c$ and $\overset{\sim}{w} \equiv {{{({1 - \gamma})}c}/{({1 - \overset{\sim}{\gamma}})}}$. However, this is a system of ${|\mathcal{A}|} \times {|\mathcal{S}|}$ equations in $2 \times {|\mathcal{S}|}$ unknowns, so the definition will hold provided our agents' actions have sufficiently varied impact on the resulting transition probabilities. In a linear-quadratic context, it is always enough to vary the discount rates (see Corollary 5).

### Theorem 2

Suppose we observe the policies of two agents solving entropy-regularized MDPs, who face the same reward function, but whose discount rates or transition probabilities vary, such that their MDPs are value-distinguishing. Then the reward function consistent with both agents' actions either does not exist, or is identified up to addition of a constant.

### Proof

From Theorem 1, if we can determine the value function for one of our agents, then the reward is uniquely identified. Given we know both agents' policies ($\pi$, $\overset{\sim}{\pi}$) and our agents are optimizing their respective MDPs, for every ${a \in \mathcal{A}},{s \in \mathcal{S}}$, we know the value of where $v,\overset{\sim}{v}$ are the agents' respective value functions. This is an inhomogeneous system of linear equations in ${\{{v{(s)}},{\overset{\sim}{v}{(s)}}\}}_{s \in \mathcal{S}}$. Therefore, by standard linear algebra (in particular, the Fredholm alternative), it is uniquely determined up to the addition of solutions to the homogeneous equation However, as we have assumed our pair of MDPs is value-distinguishing, the only solutions to this equation have at least one of $v$ and $\overset{\sim}{v}$ constant (we assume $v$ without loss of generality). Therefore, the space of solutions to is either empty (in which case no consistent reward exists), or determines $v$ up to the addition of a constant. Given $v$ is determined up to a constant we can use Theorem 1 to determine $f$, again up to the addition of a constant. ∎ Given the addition of a constant to $f$ does not affect the resulting policy (it simply increases the value function by a corresponding quantity), we cannot expect to do better than Theorem 2 without direct observation of the agent's rewards or value function in at least one state.

### Remark 4

Definition 1 is essentially a statement regarding invertibility of a linear system of equations for $w,\overset{\sim}{w}$. This indicates that the stability of the result of Theorem 2 is principally determined by whether this linear system is well conditioned, as can be measured by the ratio of its largest to second smallest singular values (the second smallest is due to the constant functions always being in the kernel of the system) not being too large. Given the inevitable error arising from statistical estimation of policies and transition functions, a well conditioned system is often a key requirement in practice. A similar observation will also be valid for the uniqueness results in later sections.

### Remark 5

Our results show that it is typically sufficient to observe an MDP under *two* environments (transitions and discount factors) in order to identify the reward. This can be contrasted with Amin and Singh and Amin et al. who show that, if the demonstrator is observed in multiple (suitably chosen) environments, the (state-only) reward can be identified up to a scaling and shift (the scaling is natural, given they do not use an entropy regularization). Ratliff et al. consider a finite number of environments, but explicitly do not attempt to estimate the 'true' underlying reward.

## Finite horizon results

Over finite horizons, for general costs, similar results hold to those already seen on infinite horizons. An entropy-regularized optimizing agent will use a policy $\pi^{\ast} = {\{\pi_{t}^{\ast}\}}_{t = 0}^{T - 1}$ which solves the following problem with terminal reward $g$ and (possibly time-dependent) running reward $f$: For any $\pi = {\{\pi_{t}\}}_{t = 0}^{T - 1}$, $s \in \mathcal{S}$, $a \in \mathcal{A}$, and $t \in {\{ 0,\ldots,{T - 1}\}}$ write Then, similarly to the infinite-horizon discounted case discussed in the main text, we have $V_{T}^{\ast} = g$ and for $t \in {\{ 0,\ldots,{T - 1}\}}$, Rearranging this system of equations, for any chosen function $v:{{{\{ 0,\ldots,T\}} \times \mathcal{S}}\rightarrow{\mathbb{R}}}$ with ${v{(T, \cdot)}} = {g{(\cdot)}}$, we see that $\pi_{t}^{\ast}{(\left. a \middle| s \right.)}$ is the optimal strategy for the reward function in which case the corresponding value function is $V^{\ast} = v$. In other words, the identifiability issue discussed earlier remains. We note that identifying $\pi$ in this setting is more delicate than in the infinite-horizon case, as it is necessary to observe many finite-horizon state-action trajectories, rather than a single infinite-horizon trajectory.

### Time-homogeneous finite-horizon identifiability

Following the release of a first preprint version of this paper, Kim et al. was published and presents a closely related analysis, for entropy-regularized deterministic MDPs with zero terminal value. We here give an extension of their result which covers the stochastic case and includes an arbitrary (known) terminal reward.

The key structural assumptions made by Kim et al. are that the reward is time-homogeneous (that is, $f$ does not depend on $t$), and that there is a finite horizon. As discussed in the previous section, there is no guarantee that an arbitrary observed policy will be consistent with these assumptions (that is, whether there exists any $f$ generating the observed policy). However, given a policy consistent with these assumptions, and mild assumptions on the structure of the MDP, we shall see that unique identification of $f$ is possible up to a constant.

Before describing our findings, we first present the following lemma^1010^10Thanks to Victor Flynn for discussion on the formulation and proof of this result. from elementary number theory, which will prove useful in what follows.

### Lemma 1

Let $\mathcal{R} \subset {\mathbb{N}}$ be a set of natural numbers, with the property that $\mathcal{R}$ is closed under addition (if ${a,b} \in \mathcal{R}$ then ${a + b} \in \mathcal{R}$). Suppose $\mathcal{R}$ has greatest common divisor $1$ (i.e. ${\gcd{(\mathcal{R})}} = 1$). Then there exist elements ${a,b} \in \mathcal{R}$ which are coprime (i.e. ${\gcd{(a,b)}} = 1$). Furthermore, for any coprime ${a,b} \in \mathcal{R}$, for all $c \geq {ab}$, we know $c \in \mathcal{R}$, in particular, there exist at least two distinct pairs of nonnegative integers $\lambda,\mu$ such that ${{\lambdaa} + {\mub}} = c$.

### Proof

We first show a coprime pair ${a,b} \in \mathcal{R}$ exists. As $\gcd{({\mathcal{R} \cap {\{ x:{x \leq y}\}}})}$ is decreasing in $y$, and the integers are discrete, there exists a smallest value $y$ such that ${\gcd{({\mathcal{R} \cap {\{ x:{x \leq y}\}}})}} = 1$. Applying Bézout's lemma, there exist integers ${\{\lambda_{k}\}}_{k \leq y}$ such that Rearranging this sum by taking all negative terms to the right hand side, we obtain the desired positive integers $a = {\sum_{\{{{k \in \mathcal{R}},{{k \leq y},{\lambda_{k} > 0}}}\}}{\lambda_{k}k}}$ and $b = {\sum_{\{{{k \in \mathcal{R}},{{k \leq y},{\lambda_{k} < 0}}}\}}{{|\lambda_{k}|}k}}$ which satisfy $a = {b + 1}$ (so $a$ and $b$ are coprime) and ${a,b} \in \mathcal{R}$ (as $\mathcal{R}$ is closed under addition).

We now take an arbitrary coprime pair ${a,b} \in \mathcal{R}$. Again by Bézout's lemma, there exist (possibly negative) integers $\overset{\sim}{\lambda},\overset{\sim}{\mu}$ such that ${{\overset{\sim}{\lambda}a} + {\overset{\sim}{\mu}b}} = 1$, and hence ${{\overset{\sim}{\lambda}ca} + {\overset{\sim}{\mu}cb}} = c$. However, for any integer $k$ it follows that ${{{({{\overset{\sim}{\lambda}c} + {kb}})}a} + {{({{\overset{\sim}{\mu}c} - {ka}})}b}} = c$. Since this holds for all $k \in {\mathbb{Z}}$, we can choose $k$ such that $1 \leq \lambda = {({{\overset{\sim}{\lambda}c} + {kb}})} \leq b$. However, this implies that ${{({{\overset{\sim}{\lambda}c} + {kb}})}a} \leq {ab} \leq c$, and so $\mu = {({{\overset{\sim}{\mu}c} - {ka}})} \geq 0$. As $\mathcal{R}$ is closed under addition, we see that $c = {{\lambdaa} + {\mub}} \in \mathcal{R}$.

To see non uniqueness, we simply observe that if $c \geq {ab}$, in the construction above we have $\mu \geq a$, and hence $({\lambda + b},{\mu - a})$ is an alternative pair of coefficients. ∎ We now present the first assumption on the structure of the MDP.

### Definition 2

We say a MDP has full access at horizon $T$ (from a state $s$) if, for some distribution over actions, for all states $s'$ we have ${{\mathbb{P}}{({S_{T - 1} = \left. s' \middle| S_{0} \right. = s})}} > 0$.

It is easy to verify that this definition does not depend on the choice of distribution over actions (provided it has full support).

This is slightly weaker than assuming that the Markov chain underlying the MDP (with random actions) is irreducible, as there may exist transient states from which we have full access. It is a classical result (commonly stated as a corollary to the Perron--Frobenius theorem) that an irreducible aperiodic Markov chain has full access (from every state). Kim et al. give an alternative graph-theoretic view, based on the closely related notion of $T$-coverings.

### Theorem 3

Consider an MDP with unknown time-homogeneous reward function $f$. In order for $f$ to be identified (up to a global constant) from observation of optimal policies and the resulting transitions up to some horizon $T > 0$, with initialization from some state $s$, it is necessary that the MDP has full access at some horizon $T' \geq T$ (from state $s$).

### Proof

We suppose that $f$ can be identified, and first show that all states can be accessed from $s$, that is, for each $s'$ there exists $T > 0$ such that ${{\mathbb{P}}^{\pi}{({S_{T} = \left. s' \middle| S_{0} \right. = s})}} > 0$, but that $T$ can vary with $s'$. Suppose, for contradiction, there are states which cannot be reached by a path starting in $s$. It is clear that it is impossible to identify the cost associated with any state which cannot be accessed, as we obtain no information about actions in these states.

It remains to show that, if $f$ can be identified, we can reach all states using paths of a common length. We initially focus on the paths from $s$ to $s$. If we can return in precisely $T$ steps, then (by the Markov property) we can also return in $kT$ steps, for any $k \in {\mathbb{N}}$. Therefore either the set $\{ T:{{{\mathbb{P}}^{\pi}{({S_{T} = \left. s \middle| S_{0} \right. = s})}} > 0}\}$ is unbounded, or the state $s$ will never be revisited (in the language of Markov chains, it is ephemeral), and in particular will never be visited by a path starting in any other state. Therefore, it is clear that we can add a constant to its rewards independently of all other states' rewards, as this will not affect decision making -- we leave this state immediately and never return. Therefore the reward cannot be determined up to a global constant.

Next, still focusing on paths from $s$ to $s$, we show that $T$ can take *any* value above some bound. Let $\overline{t}$ be the greatest common divisor of $\mathcal{R} = {\{ t:{{{\mathbb{P}}^{\pi}{({S_{t} = \left. s \middle| S_{0} \right. = s})}} > 0}\}}$. For contradiction, suppose $\overline{t} > 1$. Then our system is periodic, and by classical results on irreducible matrices (e.g. ) we know that there is a partition of $\mathcal{S}$ into $\overline{t}$ sets, such that we will certainly make transitions within the states $\mathcal{S}_{0}\rightarrow\mathcal{S}_{1}\rightarrow\ldots\rightarrow\mathcal{S}_{\overline{t} - 1}\rightarrow\mathcal{S}_{0} \ni s$. By adding $c \in {\mathbb{R}}$ to the rewards of states in $\mathcal{S}_{0}$, and subtracting $c/\gamma$ from rewards of states in $\mathcal{S}_{1}$, we do not affect behavior. Therefore the reward cannot be identified up to a global constant unless $\overline{t} = 1$.

However, if $\overline{t} = 1$ then,as the set $\mathcal{R}$ is closed under addition (by concatenating cycles), Lemma 1 then implies that $\mathcal{R}$ must contain all sufficiently large values, that is, it is possible to return to the initial state in any sufficiently large number of steps.

Finally, we have seen that it is possible to transition from $s$ to $s'$ in a finite number of steps, and that it is possible to transition from $s$ to $s$ in any sufficiently large number of steps. From the Markov property we conclude that for every value of $T'$ sufficently large, for all choices of $s'$ we have ${{\mathbb{P}}^{\pi}{({S_{T'} = \left. s' \middle| S_{0} \right. = s})}} > 0$. ∎ The following definition is most easily expressed by associating our finite state space $\mathcal{S}$ with the set of basis vectors ${\{ e_{k}\}}_{k = 1}^{N} \subset {\mathbb{R}}^{N}$, and writing the transitions $\mathcal{T}{(\left. s' \middle| {s,a} \right.)}$, for $a \in \mathcal{A}$ in terms of the transition matrix ${\mathbb{T}}{(a)}$ with While this definition is quite abstract, we will see that it precisely describes when many IRL problem with fixed terminal reward can be solved.

### Definition 3

We say an $N$-state MDP has full action-rank on horizon $T$, starting at a state $s \equiv e_{i}$, if the matrix with rows given by is of rank $N$ (with the convention that products are taken sequentially on the right, that is ${\prod_{t = 0}^{2}A_{t}} = {A_{0}A_{1}A_{2}}$, and the empty product is the identity).

### Remark 6

Observe that $e_{i}^{\top}{\prod_{t' = 0}^{t - 1}{{\mathbb{T}}{(a_{t'})}}}$ is the expected state of $S_{t}$ given $S_{0} = e_{i}$, when following the actions $\{ a_{0},\ldots,a_{t}\}$. Hence, the quantity $e_{i}^{\top}\left( {\sum_{t = 0}^{T - 1}{\gamma^{t}{\prod_{t' = 0}^{t - 1}{{\mathbb{T}}{(a_{t'})}}}}} \right)$ is a time-weighted expected occupation density for the process, that is, a measurement of how long we spend in each state. We have full action-rank if our actions are sufficiently varied that there are $N$ linearly independent such density vectors (cf., where it is the state--action occupation density which is considered).

### Theorem 4

Suppose our MDP has full action rank and full access, at horizon $T$, from an initial state $s_{0}$. Then the time-homogeneous IRL problem is well posed, that is, knowledge of the (time-dependent) entropy-regularized optimal strategy $\pi_{t}^{\ast}{(\left. a \middle| s \right.)}$, and the terminal reward $g$, is sufficient to uniquely determine a time-homogeneous running reward $f$, if it exists, up to a constant.

Conversely, if our MDP has full access but not full action rank at horizon $T$, from the state $s_{0}$, the IRL problem remains ill posed.

### Proof

We first prove the sufficiency statement. The optimal policy satisfies We write (for notational simplicity), ${\upsilon{(s)}} = {V_{T - 1}^{\ast}{(s)}}$, and hence, given $V_{T}^{\ast} \equiv g$ by assumption, This shows that $f$ is completely determined (if it exists) by the function $\upsilon$.

We also observe that for every $t$ we have the recurrence relation This holds for any choice of action $a$ (unlike the usual dynamic programming relation, which only involves the optimal policy). Writing $\mathbf{V}_{t}$ for the vector with components ${\{{V_{t}^{\ast}{(s)}}\}}_{s \in \mathcal{S}}$ we have the recurrence relation where $\Upsilon_{t}$ is a known vector valued function, with components Solving the recurrence relation, we have, for any sequence of actions $a_{0},\ldots,a_{T - 1}$ (with the convention that the empty matrix product is the identity) From this linear system, we can extract the single row corresponding to the fixed initial state $s_{0}$. Assuming this is the row indicated by the $e_{i}$ basis vector, we have for a known function $G$, expressible in terms of $\gamma$, $g$ and ${\{\pi_{t}^{\ast}\}}_{t = 0}^{T - 1}$.

Now that the MDP has full action-rank, the system of equations, admits at most one solution, denoted by $\overline{\upsilon}$. Substituting into, we have a unique solution to the equation ${V_{0}^{\ast}{(s_{0})}} = 0$. However, we need to consider all possible values of $V_{0}^{\ast}{(s_{0})}$.

For any choice of actions ${\{ a_{t}\}}_{t = 0}^{T - 1}$, Here $\mathbf{1}$ denotes the all-one vector in ${\mathbb{R}}^{N}$. Therefore, the set of all possible $({V_{0}^{\ast}{(s_{0})}},\upsilon)$ pairs is given by From, we conclude that $f$ can be identified up to a constant.

To show necessity, we observe from the above that, if the system is not full action-rank, then there exists a linear subspace of choices of $\upsilon$, which do not differ only by constants, such that we can construct the same value vectors $\mathbf{V}_{t}$ for all $t$, satisfying and hence. It follows that we have a nontrivial manifold of rewards $f$ which generate the same optimal policies, that is, the rewards are not identifiable. ∎ As a corollary, we demonstrate a generalized version of.

### Corollary 1

Suppose $\gamma \neq 0$ and our MDP is deterministic, that is ${\mathcal{T}{(\left. s' \middle| {s,a} \right.)}} \in {\{ 0,1\}}$, and one of the following holds: the underlying Markov chain is irreducible and aperiodic (i.e. with randomly chosen actions, the underlying Markov chain is irreducible and aperiodic) the initial state $s_{0} = e_{i}$ admits a self-loop (i.e. it is possible to transition from this state to itself), and all states can be accessed from the initial state in at most $d$ transitions there exist cycles^1111^11A cycle is a sequence of possible transitions which start and end in the same state. The length of a cycle is defined to be the number of transitions, e.g. a cycle $\{{s_{0}\rightarrow s_{1}\rightarrow s_{2}\rightarrow s_{0}}\}$ has length $3$. An irreducible Markov chain is aperiodic if there is no common factor (greater than one) of the lengths of all cycles. starting at the initial state $s_{0} = e_{i}$ with lengths $R,R'$, such that ${\gcd{(R,R')}} = 1$, and all states can be accessed from the initial state in at most $d$ transitions.

Then there exists a horizon $T$ such that the time-homogeneous IRL problem is well posed (as in Theorem 4). In particular, in case (ii) ‣ Corollary 1. ‣ 4.1 Time-homogeneous finite-horizon identifiability. ‣ 4 Finite horizon results ‣ Identifiability in inverse reinforcement learning"), it is sufficient to take any finite $T \geq {d + 1}$; in case (iii) ‣ Corollary 1. ‣ 4.1 Time-homogeneous finite-horizon identifiability. ‣ 4 Finite horizon results ‣ Identifiability in inverse reinforcement learning") it is sufficient to take any finite $T \geq {d + {RR'}}$.

### Proof

We first observe that it is a classical result on Markov chains (see, for example, ) that the conditions of case (i) ‣ Corollary 1. ‣ 4.1 Time-homogeneous finite-horizon identifiability. ‣ 4 Finite horizon results ‣ Identifiability in inverse reinforcement learning") guarantee those of case (iii) ‣ Corollary 1. ‣ 4.1 Time-homogeneous finite-horizon identifiability. ‣ 4 Finite horizon results ‣ Identifiability in inverse reinforcement learning"), for some choice of ${R,R'} > 0$. The conditions of case (ii) ‣ Corollary 1. ‣ 4.1 Time-homogeneous finite-horizon identifiability. ‣ 4 Finite horizon results ‣ Identifiability in inverse reinforcement learning") also guarantee those of case (iii) ‣ Corollary 1. ‣ 4.1 Time-homogeneous finite-horizon identifiability. ‣ 4 Finite horizon results ‣ Identifiability in inverse reinforcement learning"), with both the cycles being the self-loop. It is therefore sufficient to consider case (iii) ‣ Corollary 1. ‣ 4.1 Time-homogeneous finite-horizon identifiability. ‣ 4 Finite horizon results ‣ Identifiability in inverse reinforcement learning").

To show that the MDP has full action rank, we observe that for every possible path of states, there exists a corresponding sequence of actions, and vice versa. We will therefore use these different perspectives interchangeably. We also observe that, as our MDP is deterministic, $e_{i}^{\top}{\prod_{t' = 0}^{t - 1}{{\mathbb{T}}{(a_{t'})}}}$ is a vector indicating the current state at time $t$, when started in state $e_{i}$. Therefore, is a row vector, containing a time-weighted occupation density -- in particular, if $\gamma = 1$, it simply counts the number of times we have entered each state. (This is in contrast to Remark 6, where we have an *expected* occupation density; here we can simplify given the control problem is deterministic.) Our aim, therefore, is to construct a collection of paths which give a full-rank system of occupation densities.

Starting in state $s_{0} \equiv e_{i}$, consider a shortest path (i.e. a path with the fewest number of transitions) to each state $s'$. Denote these paths $r_{s'} = {\{{s_{0}\rightarrow\ldots\rightarrow s'}\}}$, and the corresponding sequence of actions $a^{s'}$. These paths have lengths $|r_{s}|$ and time-weighted occupation densities ${\mathbb{O}}_{|r_{s}|}{({\{ a_{t}^{s}\}}_{t \geq 0})}$ which are linearly independent (a longer path will contain states not in a shorter path, while paths of the same length will differ in their final state; by reordering the states we can then obtain a lower-triangular structure in the matrix of occupation densities ${\lbrack{{\mathbb{O}}_{|r_{s}|}{({\{ a_{t}^{s}\}}_{t \geq 0})}}\rbrack}_{{\{ a_{t}\}} \subset \mathcal{A}}$). This gives us $N = {|\mathcal{S}|}$ paths, of varying lengths, with linearly independent occupation densities.

We now consider prefixing our paths with cycles, in order to make them the same length. Fix an arbitrary integer value $T' \geq {{{\max_{s}{|r_{s}|}} + {{|Q|}{|Q'|}}} - 1}$. By Lemma 1, for all states $s$, there exist nonnegative integers $\lambda_{s},\mu_{s}$ such that $T' = {{\lambda_{s}{|Q|}} + {\mu_{s}{|Q'|}} + {|r_{s}|}}$. Therefore, taking the concatenated path consisting of $\lambda_{s}$ repeats of cycle $Q$, then $\mu_{s}$ repeats of cycle $Q'$, then our shortest path $r_{s}$, gives us a path from $s_{0}$ to $s$ of length $T'$. Denote each of these paths $P_{s}$.

Concatenation of paths has an elegant effect on the occupation densities: If $Q$ is a cycle and $r$ a path (starting from the terminal state of $Q$), their concatenation $Q \ast r$ and corresponding actions $a^{Q},a^{r},a^{Q \ast r}$, then the occupation densities combine linearly: (observe that the occupation density excludes the (repeated) final state of the cycle).

We now observe that for the initial state, the shortest path is of length zero (i.e. has no transitions). From Lemma 1, as $T' \geq {{|Q|}{|Q'|}}$, we know that there are multiple choices of $\lambda,\mu$ satisfying the stated construction, and therefore there are at least *two* possible paths $P_{s_{0}}$ and ${\overset{\sim}{P}}_{s_{0}}$ with the desired length, from the initial state to itself, using distinct numbers of cycles ^1212^12If the cycles are both a self-loop, then this becomes degenerate, but in the following step the final column and row of the matrix $M$ can be omitted, and the remainder of the argument follows in essentially the same way. $(\lambda_{s_{0}},\mu_{s_{0}})$ and $({\overset{\sim}{\lambda}}_{s_{0}},{\overset{\sim}{\mu}}_{s_{0}})$.

This construction yields a collection of paths with full rank occupation densities. To verify this explicitly, extract the rows corresponding to the paths ${\{ R_{s}\}}_{s \in \mathcal{S}}$ and ${\overset{\sim}{R}}_{s_{0}}$, we use to see that After subtracting the first from the last row of $M$, as $\lambda_{s_{0}} \neq {\overset{\sim}{\lambda}}_{s_{0}}$, we see that $M$ has a simple structure, in particular it is a full-rank matrix with $N + 1$ rows and $N + 2$ columns. As the final matrix on the right hand side of is of rank $N$, this implies that the left hand side of is also of rank $N$ (by Sylvester's rank inequality). As the left hand side of is a selection of rows from the matrix considered in Definition 3, we conclude that our MDP must be of full action rank.

Our collection of paths also shows that our system has full access at horizon $T = {T' + 1}$, and therefore the identification result follows from Theorem 4. By varying $T'$, we see this result holds for any choice of $T \geq {{{|Q|}{|Q'|}} + {\max_{s}{|r_{s}|}}}$, as desired. ∎

### Example 1

Consider the problem with three states $\mathcal{S} = {\{ A,B,C\}}$, with possible transitions $A\rightarrow{\{ B,C\}}$, $B\rightarrow A$ and $C\rightarrow B$. Starting in state $A$, the shortest paths are then given by ${\{ A\}},{\{{A\rightarrow B}\}},{\{{A\rightarrow C}\}}$, and we have cycles $\{{A\rightarrow B\rightarrow A}\}$ and $\{{A\rightarrow C\rightarrow B\rightarrow A}\}$. Writing out the occupation densities of each of these paths (ignoring the terminal state of the two cycles), with $\gamma = 1$, we get the system \end{matrix} \right.} \\{\text{Cycles (excluding final state)}\left\{ \begin{matrix} \end{matrix} \right.} \end{array} & \begin{bmatrix} \end{matrix}\Rightarrow\begin{matrix} This corresponds to the final term on the right hand side of. Clearly, the section above the horizontal line (corresponding to the shortest paths) is lower-triangular, and hence of full rank. We prefix our paths by appropriate numbers of cycles, in order to make them the same length. This implies that, with a horizon $T = 7 = {{2 \times 3} + 1}$, we consider the paths The matrix of occupation densities shown here is the left hand side of and is easily seen to be full rank; the matrix $M$ from is given by We can extend this result to a stochastic setting, assuming that our action space is sufficiently rich.

### Corollary 2

Suppose $\gamma \neq 0$, and our MDP is stochastic and satisfies one of the sets of assumptions ((i) ‣ Corollary 1. ‣ 4.1 Time-homogeneous finite-horizon identifiability. ‣ 4 Finite horizon results ‣ Identifiability in inverse reinforcement learning"), (iii) ‣ Corollary 1. ‣ 4.1 Time-homogeneous finite-horizon identifiability. ‣ 4 Finite horizon results ‣ Identifiability in inverse reinforcement learning") or (ii) ‣ Corollary 1. ‣ 4.1 Time-homogeneous finite-horizon identifiability. ‣ 4 Finite horizon results ‣ Identifiability in inverse reinforcement learning")) of Corollary 1 and that from every state, we have at least as many actions (with linearly independent resulting transition probabilities) as we have possible future states, that is, Then for any initial state $s_{0}$, there exists a horizon $T$ such that the time-homogeneous IRL problem is well posed (as in Theorem 4). The sufficient bounds on $T$ from Corollary 1 also apply.

### Proof

For a given state $s$, consider the space spanned by the basis vector corresponding to the possible future states. Given we have as many actions as possible future states, and the rank-nullity theorem, we know that this space must be the same as the space spanned by the vectors $\{\mathcal{T}{( \cdot |s,a)};a \in \mathcal{A}\}$. In particular, there exists a set of weights $c_{a}$ over actions (which do not need to sum to one or be nonnegative) such that $\sum_{a \in \overline{\mathcal{A}}}{c_{a}{\mathbb{T}}{(a)}}$ is the basis vector corresponding to any possible transition. In other words, there is no difference between the linear span generated by these stochastic transitions and deterministic transitions. As actions at every time can be varied independently, and the requirement that a MDP has full action rank depends only on the space spanned by transition matrices, the problem reduces to the setting of Corollary 1. ∎

## Action-independent rewards

Earlier works such as Amin and Singh, Amin et al., Dvijotham and Todorov and Fu et al. consider the case of action-independent rewards, that is, where $f$ is not a function of $a$. In general, it is not immediately clear whether, for a given observed policy, the IRL problem will admit an action-independent solution. In this section, we obtain a necessary and sufficient condition under which an action-independent time-homogeneous reward function could be a solution to a given entropy-regularized, infinite-time-horizon^1313^13The analogous results for finite-horizon problems with time-inhomogeneous rewards (and general discount factor) can be obtained through the same method. IRL problem with discounting. We shall also obtain a rigorous condition under which a unique reward function can be identified.

Consider an entropy-regularized MDP environment $(\mathcal{S},\mathcal{A},\mathcal{T},\gamma,\lambda)$, as given in Section 2. Without loss of generality, assume that ${{|\mathcal{S}|},{|\mathcal{A}|}} \geq 2$ and $\mathcal{S} = {\{ s_{1},\ldots,s_{|\mathcal{S}|}\}}$. Let $\overline{\pi}:{\mathcal{S}\rightarrow{\mathcal{P}{(\mathcal{A})}}}$ be the observed optimal policy such that ${\overline{\pi}{(\left. a \middle| s \right.)}} > 0$ for any ${(s,a)} \in {\mathcal{S} \times \mathcal{A}}$.

As before, for $a \in \mathcal{A}$ we write ${\overline{\pi}{(a)}} \in {\mathbb{R}}^{|\mathcal{S}|}$ for the probability vector $\begin{pmatrix} {\overline{\pi}{(\left. a \middle| s_{1} \right.)}} & \ldots & {\overline{\pi}{(\left. a \middle| s_{|\mathcal{S}|} \right.)}} \end{pmatrix}^{T}$, and ${{\mathbb{T}}{(a)}} \in {\mathbb{R}}^{{|\mathcal{S}|} \times {|\mathcal{S}|}}$ for the transition matrix with ${\lbrack{{\mathbb{T}}{(a)}}\rbrack}_{ij} = {\mathcal{T}{(\left. s_{j} \middle| {s_{i},a} \right.)}}$. Fix a particular action $a_{0} \in \mathcal{A}$, and write where ${\log\overline{\pi}}{(a)}$ denotes the element-wise application of logarithm over the vector $\overline{\pi}{(a)}$, for any $a \in \mathcal{A}$.

### Theorem 5

The above IRL problem admits a solution with action-independent reward $f:{\mathcal{S}\rightarrow{\mathbb{R}}}$ if and only if the system of equations admits a solution $\upsilon \in {\mathbb{R}}^{|\mathcal{S}|}$. (Note that this is a system of ${|\mathcal{A}|} \times {|\mathcal{S}|}$ equations in $|\mathcal{S}|$ unknowns, so this is a non-trivial assumption.)

### Proof

: Suppose the IRL problem admits an action-independent solution $f:{\mathcal{S}\rightarrow{\mathbb{R}}}$. Then for any ${(s,a)} \in {\mathcal{S} \times \mathcal{A}}$, where $v$ is the corresponding value function. Notice that for any $a \in \mathcal{A}$, for all $s \in \mathcal{S}$, Therefore, taking $\upsilon$ to be the vector with components $v{(s)}$, we have a solution to the system of equations.: Let $\upsilon$ be a solution to the system of equations. By abuse of notation, we may write $\upsilon{(s)}$ for the components of $\upsilon$. Then for any ${(s,a)} \in {\mathcal{S} \times \mathcal{A}}$, Therefore, the quantity ${\hat{f}{(s)}}:={{{\lambda{\log\overline{\pi}}{(\left. a_{0} \middle| s \right.)}} - {\gamma{\sum_{s' \in \mathcal{S}}{\mathcal{T}{(\left. s' \middle| {s,a_{0}} \right.)}\upsilon{(s')}}}}} + {\upsilon{(s)}}}$ is independent of $a$. From Theorem 1, we conclude that $\hat{f}$ is a solution to the IRL problem.

### Corollary 3

Suppose $\gamma \in {\lbrack 0,1)}$. Assuming a solution to exists, the IRL problem is identifiable (i.e. the true action-independent reward function can be inferred up to a constant shift) if and only if, writing $\mathcal{K}{(a)}$ for the kernel of $\Delta{\mathbb{T}}{(a)}$, we know that where $\mathbf{1}$ denotes the all-one vector in ${\mathbb{R}}^{|\mathcal{S}|}$. (Note that ${\{{c\mathbf{1}}:{c \in {\mathbb{R}}}\}} \subset {\mathcal{K}{(a)}}$ for any $a \in {\mathcal{A} \smallsetminus {\{ a_{0}\}}}$ and ${{\mathbb{T}}{(a_{0})}} = 0$ implies ${\mathcal{K}{(a)}} = {\mathbb{R}}^{|\mathcal{S}|}$.)

### Proof

Let $\upsilon_{0}$ be a solution to, which is assumed to exist. By the Fredholm alternative (as in Theorem 2) the solution set ${\mathbb{Y}}_{\mathcal{S}}$ for is given by From Theorem 5, the set of action-independent solutions for the IRL is given by We then observe that the stated condition is sufficient -- if constant vectors are the only valid choices for $\kappa$, then $\upsilon$ and hence $f \in {\mathbb{F}}_{\mathcal{S}}$ will only vary by constants.

To show necessity, denote by $f_{0}$ the solution corresponding to $\upsilon_{0}$. Suppose there exists a vector It follows that ${f_{0} + \Delta} \in {\mathbb{F}}_{\mathcal{S}}$; if $\Delta$ is not a constant, we see that the reward is not uniquely identifiable.

To show $\Delta$ is not a constant, let Then $\underset{¯}{\upsilon} = {\hat{\upsilon}{(\underset{¯}{s})}} < \overset{\sim}{\upsilon} < \overline{\upsilon} = {\hat{\upsilon}{(\overline{s})}}$. We have Therefore, $\Delta$ is not a constant. It follows that our condition is necessary in order to have an identifiable action-independent reward ∎ Under the entropy regularized framework, the long-run total reward depends on actions through the entropy penalty term. Therefore, it cannot be reduced to the scenario in Amin and Singh, where any linear perturbation of the reward function will not affect optimal behavior under any given environment.

### Remark 7

Theorem 5 and Corollary 3 suggest various extensions, in the case when does not admit a solution, but the assumed property on the kernels in Corollary 3 holds. For example, one could consider the least-squares solution to the system (which is defined up to a constant). This gives a choice of value function which, in some sense, minimizes the action-dependence of the resulting cost function (obtained through Theorem 1).

Fu et al. give a result similar to Corollary 3. Unfortunately, the role of the choice of actions in their conditions is not precisely stated, and on some interpretations is insufficient for the result to hold -- as we have seen, the condition of Corollary 3 is both necessary and sufficient for identifiability. We give a variation of their assumptions in what follows.

### Definition 4 (Reward-decomposability)

We say states $s_{1},s_{1}'$ are '1-step linked', if there exist actions ${a,a'} \in \mathcal{A}$ and a state $s_{0} \in \mathcal{S}$ such that ${\mathcal{T}{(\left. s_{1} \middle| {s_{0},a} \right.)}} > 0$ and ${\mathcal{T}{(\left. s_{1}' \middle| {s_{0},a'} \right.)}} > 0$. We extend this definition through transitivity, forming a set of 'linked' states $\mathcal{S}_{1}$. We say say the MDP is reward-decomposable if all its states are linked.

Note that there is no loss of generality if a specific $a'$ is selected in this definition (instead of being allowed to vary).

### Remark 8

An equivalent definition would be that our MDP is reward-decomposable if $\mathcal{S}_{1} = \mathcal{S}$ is the only choice of nonempty set $\mathcal{S}_{1} \subset \mathcal{S}$ such that: there exists a set $\mathcal{S}_{0} \subset \mathcal{S}$ with every transition (with any action) to $\mathcal{S}_{1}$ is from $\mathcal{S}_{0}$, and every transition from $\mathcal{S}_{0}$ is to $\mathcal{S}_{1}$.

(In other words, $X_{t} \in \mathcal{S}_{0}$ if and only if $X_{t + 1} \in \mathcal{S}_{1}$.) We note that Fu et al. simply call this property 'decomposable', but this seems an unfortunate choice of terminology given this alternative characterization.

The following final corollary gives a simple set of conditions under which identification is possible, clarifying (and extending to the stochastic case) the result of.

### Corollary 4

Suppose our MDP either has deterministic transitions ${\mathcal{T}{(\left. s' \middle| {s,a} \right.)}} \in {\{ 0,1\}}$ or we have at least as many actions (with linearly independent resulting transition probabilities) as we have possible future states, that is, Then the (action-independent) IRL problem is identifiable (i.e. the true action-independent reward function can be inferred up to a constant shift) if and only if the MDP is reward-decomposable.

### Proof

We will verify the condition of Corollary 3.

In the stochastic transition case, the proof of Corollary 2 shows that, under the stated assumption on the rank of the transitions, we can perform row operations on our transition matrix (corresponding to linear combinations of actions) to obtain a deterministic transition matrix. In particular, the dimension of $\cap_{a \in \mathcal{A}}{\mathcal{K}{(a)}}$ is the same under the assumption on the rank of the transitions as under the assumption that transitions are deterministic. We can therefore focus our attention on the deterministic transition case.

If transitions are deterministic, the matrix ${\mathbb{T}}{(a)}$ has rows given by the basis vectors indicating the future states; so the matrix $\Delta{\mathbb{T}}{(a)}$ has rows which are the difference of two basis vectors corresponding to one-step linked states. Therefore, a vector $\upsilon \in {\mathcal{K}{(a)}}$ must have entries $\upsilon_{i} = \upsilon_{j}$ whenever $e_{i}$ and $e_{j}$ correspond to these one-step-linked states.

By considering all possible choices of $a$, we see that a vector $\upsilon \in {\cap_{a \in \mathcal{A}}{\mathcal{K}{(a)}}}$ must have entries $\upsilon_{i} = \upsilon_{j}$ whenever $e_{i}$ and $e_{j}$ correspond to any one-step linked states (and this is a sufficient condition to ensure $\upsilon \in {\cap_{a \in \mathcal{A}}{\mathcal{K}{(a)}}}$). However, if our MDP is reward-decomposable, there is no proper subset $\mathcal{S}_{1}$ of $\mathcal{S}$ which is closed under taking one-step linked states. Therefore, if our MDP is reward-decomposable, the only vectors in the kernel of $\Delta{\mathbb{T}}{(a)}$ for every $a$ are the constant vectors, as desired.

Conversely, if our MDP is not reward-decomposable, then there exists a set $\mathcal{S}_{1} \neq \mathcal{S}$ satisfying the conditions above, and hence a nonconstant vector $\upsilon \in {\cap_{a \in \mathcal{A}}{\mathcal{K}{(a)}}}$. The result of Corollary 3 then shows the reward is not identifiable. ∎ It is clear that reward-decomposability is not, by itself, sufficient to guarantee identifiability of rewards -- simply consider the trivial MDP with action space containing only one element (so no information can be gained by watching optimal policies) but all transitions are possible (so the MDP is reward-decomposable).

The necessity of reward-decomposability, in general, can easily be seen as follows: Suppose there are sets ${\mathcal{S}_{0},\mathcal{S}_{1}} \subset \mathcal{S}$ such that every transition from a state in $\mathcal{S}_{0}$ (under every action) is to a state in $\mathcal{S}_{1}$, and every transition to a state in $\mathcal{S}_{1}$ is from $\mathcal{S}_{0}$. Then, if we add $c \in {\mathbb{R}}$ to the reward in $\mathcal{S}_{0} \smallsetminus \mathcal{S}_{1}$, subtract $c/\gamma$ from the reward in $\mathcal{S}_{1} \smallsetminus \mathcal{S}_{0}$, and add ${({1 - {1/\gamma}})}c$ to the reward in state $\mathcal{S}_{0} \cap \mathcal{S}_{1}$, we will have no impact on the overall value or optimal strategies. A reward-decomposability assumption ensures $\mathcal{S}_{0} = \mathcal{S}$ (which implies $\mathcal{S}_{0} = \mathcal{S}$ as every transition into $\mathcal{S}_{1}$ must be from a state in $\mathcal{S}_{0}$), so this is simply a constant shift; otherwise, we see our IRL problem is not identifiable.

## A linear-quadratic-Gaussian problem

We now present the corresponding results for a class of one-dimensional linear-quadratic problems with Gaussian noise, ultimately inspired by Kalman. This simplified framework allows us to explicitly observe the degeneracy of inverse reinforcement learning, even if we add restrictions on the choice of value functions.

### Optimal LQG control

Suppose our agent seeks to control, using a real-valued process $A_{t}$ a discrete time process with dynamics for constants $\overline{\mu},\mu_{s},\mu_{a},\overline{\sigma},\sigma_{s},\sigma_{a}$. The innovations process $Z$ is a Gaussian white noise with unit variance. Our agent uses a randomized strategy $\pi{(\left. a \middle| s \right.)}$ to maximize the expectation of the entropy-regularized infinite-horizon discounted linear-quadratic reward: where ${f{(s,a)}} = {{\alpha_{20}s^{2}} + {\alpha_{11}sa} + {\alpha_{02}a^{2}} + {\alpha_{10}s} + {\alpha_{01}a} + \alpha_{00}}$ and $\mathcal{H}{(\pi)} = - \int_{\mathbb{R}}\pi{(a)}\log{(\pi{(a)}da}$ is the Shannon entropy of $\pi$. We assume the coefficients of $f$ are such that the problem is well posed (i.e. it is not possible to obtain an infinite expected reward).

Just as in the discrete state and action space setting, we can write down the state-action value function Using this, the optimal policy and value function are given by What is particularly convenient about this setting is that $Q$ is a quadratic in $(s,a)$, $V_{\lambda}$ is a quadratic in $s$, and $\pi_{\lambda}^{\ast}{(\cdot |s)}$ is a Gaussian density. In particular, the optimal policy is of the form for some constants ${{k_{1},k_{2}} \in {\mathbb{R}}},{k_{3} > 0}$, which can be determined^1414^14The explicit formulae for $k_{1},k_{2}$ and $k_{3}$, and the coefficients of the value function, can be obtained by equating the coefficients of $f$ with the values obtained. Under the assumption that the optimal control problem is well posed, this has a solution with $k_{3} > 0$. in terms of the known parameters $\mu_{a},\mu_{s},\sigma,\lambda$ and the parameters of the reward function ${\{\alpha_{ij}\}}_{{i + j} \leq 2}$.

### Theorem 6

Consider an agent with a policy of the form. Suppose we also know that the value function $V$ is a quadratic (or, equivalently, that the reward function is a quadratic in $(s,a)$). The space of rewards consistent with this policy is given: | | | ${{(a_{10},a_{01})} = {\left(\frac{- {k_{1}k_{2}}}{k_{3}},\frac{k_{2}}{k_{3}} \right) - {\beta_{2}\left({2\gamma{({{\overline{\mu}\mu_{s}} + {\overline{\sigma}\sigma_{s}}})}},{2\gamma{({{\overline{\mu}\mu_{a}} + {\overline{\sigma}\sigma_{a}}})}} \right)} - {\beta_{1}\left({{\gamma\mu_{s}} + 1},{\gamma\mu_{a}} \right)}}},$ | | | | | | $\left. a_{00},\beta_{2},\beta_{1} \in {\mathbb{R}} \right\}.$ | | |

### Proof

We consider an arbitrary quadratic as a candidate value function. If we have begun from the assumption that the reward function $f$ is quadratic, we know that the corresponding value function is quadratic, so this is not a restrictive assumption.

We then compute the state-action value function using, to give Combining with and, we see that a reward function $f$ is consistent with the observed policy if Rearranging, we conclude that $f$ is given by As $(\beta_{2},\beta_{1},\beta_{0})$ are arbitrary, we have the desired statement. ∎ As in Theorem 1, we see that the inverse reinforcement learning problem only defines the rewards up to the choice of value function, which is arbitrary; the restriction to quadratic rewards or values simply reduces our problem to the smaller range of rewards determined by the three coefficients in the quadratic $V$.

The following theorem gives the linear-quadratic version of Theorem 2. As our agents' actions have a linear effect on the state variable, this leads to a particularly simple set of conditions for identifiability of the reward, given observation of two agents' policies.

### Theorem 7

Suppose we now have two agents, who are both following their respective optimal controls of the form, for the same reward function, but disagree on some combination of the dynamics and discount rate. We write giving us two pairs of vectors $(x_{1},x_{2})$ (for the first agent) and $({\overset{\sim}{x}}_{1},{\overset{\sim}{x}}_{2})$ (for the second agent). We assume we know these vectors for each agent. The quadratic reward function $f$ consistent with both agents' policies, if it exists, is uniquely identified up to the addition of a constant shift, if (and only if)

### Proof

We see from that a single agent's actions identify a space of valid rewards $\mathbb{F}$, which is parameterized by the constant shift $a_{00}$ and the two free variables $\beta_{1},\beta_{2}$. From these free variables, identifies the values of ${\mathbf{a} = {(a_{20},a_{11},a_{02},a_{10},a_{01})}}.$ The reward function $f$ is uniquely defined, up to a constant shift, if we can identify the value of $\mathbf{a}$, which (by assumption) is the same for both agents.

Considering the role of $\beta_{2}$, defines a line in ${\mathbb{R}}^{3}$ of possible values for $(a_{20},a_{11},a_{02})$. If the assumption ${x_{2}/{\| x_{2}\|}} \neq {{\overset{\sim}{x}}_{2}/{\|{\overset{\sim}{x}}_{2}\|}}$ holds, then the lines for our two agents will not be parallel, therefore will either never meet (in which case no consistent reward exists), or will meet at a point, uniquely identifying $(a_{20},a_{11},a_{02})$ and the corresponding values of $\beta_{2}$ for each agent. Conversely, if the assumption does not hold, then the lines will be parallel, so cannot meet in a unique point, in which case there are either zero or infinitely many reward functions consistent with both agents' policies.

Essentially the same argument then applies to the equation for $(a_{10},a_{01})$. Given that $\beta_{2}$ has already been identified for each agent, varying $\beta_{1}$ for each agent defines a pair of lines in ${\mathbb{R}}^{2}$, which are not parallel if and only if the stated assumption on $x_{1},{\overset{\sim}{x}}_{1}$ holds. Therefore, we can uniquely identify $(a_{10},a_{01})$ if and only if the stated assumption holds. ∎ Due to the simplicity of the characterization in Theorem 7, we can easily see that it is enough to observe two agents using different discount rates.

### Corollary 5

Suppose we observe two agents, each using optimal policies of the form, for the same dynamics and rewards, but different discount rates. Then the underlying quadratic reward consistent with both agents' policies is identifiable up to a constant.

### Proof

Simply observe that the value of $\gamma$ introduces a non-scaling change in the vectors $x_{1},x_{2}$ defined in Theorem 7. ∎ We can also easily determine the identifiability of action-independent rewards.

### Corollary 6

For an agent with a policy of the form, there exists an action-independent reward function corresponding to this policy if and only if and this case, the action-independent reward is unique.

### Proof

From Theorem 6, in order to have an action independent reward we must have $a_{11} = a_{02} = a_{01} = 0$. From, we know The statement $k_{1} = {- {{({{\mu_{s}\mu_{a}} + {\sigma_{s}\sigma_{a}}})}/{({\mu_{a}^{2} + \sigma_{a}^{2}})}}}$ is easily seen to be equivalent to stating that these equations are consistent.

The value of $\beta_{1}$ can then always be chosen in a unique way to guarantee $a_{01} = 0$, as required. ∎

## Numerical examples of inverse reinforcement learning

In this section, we present a regularized MDP as in Section 3.1 to illustrate numerically the identifiability issue associated with inverse RL. In particular, we consider a state space $\mathcal{S}$ with $10$ states and an action space $\mathcal{A}$ with $5$ actions, with $\lambda = 1$. We compute optimal policies as in Section 2 and reconstruct the underlying rewards. As discussed in Section 3 the optimal policies and the transition kernel can be inferred from state-action trajectories, so will assumed known. We identify the state and action spaces with the basis vectors in ${\mathbb{R}}^{10}$ and ${\mathbb{R}}^{5}$ respectively, so can write ${f{(a,s)}} = {a^{\top}Rs}$ for the reward function, and ${\mathcal{T}{(\left. s' \middle| {s,a} \right.)}} = {s^{\top}P_{a}{(s')}}$ for the transition function. The true reward $R_{tr}$ and transition matrices ${\{ P_{a}\}}_{a \in \mathcal{A}}$ are randomly generated and fixed; see Figures 1 and 2.

### Non-uniqueness of infinite-sample IRL

We first look at inverse RL starting from a single optimal policy $\pi_{1}$ with discount factor $\gamma_{1} = 0.95$. We represent $\pi_{1}$ as a matrix $\Pi_{1}$ in ${\mathbb{R}}^{5 \times 10}$, where each column gives the probabilities of each action when in the corresponding state.

Figure 1: Underlying true reward matrix Rtr Figure 2: Underlying true transition kernel To solve the inverse RL problem, we numerically find $R,v$ to minimize the loss An Adam optimizer is adopted with $\alpha = 0.002$, ${(\beta_{1},\beta_{2})} = {(0.5,0.9)}$ with overall 2000 minimization steps. The experiments are conducted over 6 different random initializations, sampled from the same distribution as was used to construct the ground truth model. The training loss $L_{sing}$ decays rapidly to close to 0, as shown in Figure 3(a). This indicates that, after the minimization procedure comes to an end, the learnt reward matrix $\hat{R}$ reveals a corresponding optimal policy ${\hat{\Pi}}_{1}$ close to the true optimal policy $\Pi_{1}$; see also Figure 8 for a direct comparison.

However, when comparing the learnt reward $\hat{R}$ and the underlying reward $R_{tr}$, as in Figures 4 and 5(a), as well as the comparison between the corresponding value vectors as in Figure 5(b), we can see that the true reward function $R_{tr}$ has not been correctly inferred. Here this is not an issue of statistical error, as we assume full information on the optimal policy and the Markov transition kernel.

(a) Loss with one optimal policy, under γ1 (b) Loss with two optimal policies, under γ1 and γ2 Figure 3: Training Losses Figure 4: Learning from one optimal policy, under γ1: difference R̂ − Rtr between learnt and true reward matrices (a) ℓ2 error of learnt reward.

(b) ℓ2 error of learnt value function.

Figure 5: Learning from one optimal policy, under γ1: comparisons

### Uniqueness of IRL with multiple discount rates

We now demonstrate that the issue of identifiability can be resolved if there is additional information on an optimal policy under the same reward matrix $R_{tr}$ but different environment. Here, we assume we are given the policy $\Pi_{1}$ optimal with discount factor $\gamma_{1} = 0.95$, and the policy $\Pi_{2}$ optimal with discount factor $\gamma_{2} = 0.25$. Correspondingly, the loss function for the minimization is adjusted to An Adam optimizer is adopted with $\alpha = 0.005$, ${(\beta_{1},\beta_{2})} = {(0.5,0.9)}$ with overall 2000 minimization steps. With the same set of 6 random initializations for the minimization procedure, the training loss $L_{doub}$ also decays rapidly to close to 0. This again suggests that the learnt reward matrix $\overset{\sim}{R}$ can lead to policies ${\overset{\sim}{\Pi}}_{1}$ and ${\overset{\sim}{\Pi}}_{2}$, each optimal when using the corresponding discount factor $\gamma_{1}$ and $\gamma_{2}$, that are close to the given policies $\Pi_{1}$ and $\Pi_{2}$; see Figures 9 and 10. What differs from the single optimal policy case is that, with the additional information $\Pi_{2}$, we are able to consistently recover $R_{tr}$ up to a constant shift; see Figures 6 and 7. Some numerical error remains, due to the optimization algorithm used, as seen by the fact the graphs in Figure 6 do still vary, and the error in the value function $v_{1}$ in 7(a). Nevertheless, the errors are an order of magnitude less than was observed in Figure 5 when using observations under a single discount rate.

Figure 6: Learning from two optimal policies, under γ1 and γ2: difference $\overset{\sim}{R} - R_{tr}$ between learnt and true R matrices. Note scale of 10−1.

(a) ℓ2 error of learnt value function v1 with discount γ1 (b) ℓ2 error of learnt value function v2 with discount γ2 (c) ℓ2 error of learnt reward matrix Figure 7: Two optimal policies under γ1 and γ2: comparisons Figure 8: Learning from optimal policy under γ1: difference Π̂1 − Π1 between optimal policy under the learnt model and the true optimal policy. Note scale of 10−4.

Figure 9: Learning from optimal policies under γ1 and γ2: difference ${\overset{\sim}{\Pi}}_{1} - \Pi_{1}$ between learnt and true policies under γ1. Note scale of 10−3.

Figure 10: Learning from optimal policies under γ1 and γ2: differences ${\overset{\sim}{\Pi}}_{2} - \Pi_{2}$ between learnt and true policies under γ2. Note scale of 10−3.
