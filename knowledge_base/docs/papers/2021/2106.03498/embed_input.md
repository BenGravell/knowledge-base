<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Identifiability in Inverse Reinforcement Learning

Topics include Inverse reinforcement learning, Identifiability, Entropy regularization, Markov decision process, Reward learning, Machine learning theory, Optimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Characterizes when reward functions can and cannot be identified from demonstrations in inverse reinforcement learning. The key result is that entropy regularization, multiple discount factors, or sufficiently different environments can break the usual reward ambiguity up to well-defined equivalence classes.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Inverse reinforcement learning attempts to reconstruct the reward function in a Markov decision problem, using observations of agent actions. As already observed in Russell the problem is ill-posed, and the reward function is not identifiable, even under the presence of perfect information about optimal behavior. We provide a resolution to this non-identifiability for problems with entropy regularization. For a given environment, we fully characterize the reward functions leading to a given policy and demonstrate that, given demonstrations of actions for the same reward under two distinct discount factors, or under sufficiently different environments, the unobserved reward can be recovered up to a constant. We also give general necessary and sufficient conditions for reconstruction of time-homogeneous rewards on finite horizons, and for action-independent rewards, generalizing recent results of Kim et al. and Fu et al..

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Inverse reinforcement learning aims to use observations of agents' actions to determine their reward function. The problem has roots in the very early stages of optimal control theory; Kalman raised the question of whether, by observation of optimal policies, one can recover coefficients of a quadratic cost function (see also Boyd et al. ). This question naturally generalizes to the generic framework of Markov decision process and stochastic control.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the 1970s, these questions were taken up within economics, as a way of determining utility functions from observations. For instance, Keeney and Raiffa set out to determine a proper ordering of all possible states which are deterministic functions of actions. In this setup, the problem is static and the outcome of an action is immediate. Later in Sargent, a dynamic version of a utility assessment problem was studied, under the context of finding the proper wage through observing dynamic labor demand.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

As exemplified by Lucas' critique^44^4The critique is best summarized by the quotation: "Given that the structure of an econometric model consists of optimal decision rules of economic agents, and that optimal decision rules vary systematically with changes in the structure of series relevant to the decision maker, it follows that any change in \[regulatory\] policy will systematically alter the structure of econometric models." (Lucas ), in many applications it is not enough to find *some* pattern of rewards corresponding to observed policies; instead we may need to identify *the specific* rewards agents face, as it is only with this information that we can make valid predictions for their actions in a changed environment. In other words, we do not simply wish to learn a reward which allows us to imitate agents in the current environment, but which allows us to predict their actions in other settings.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we give a precise characterization of the range of rewards which yield a particular policy for an entropy regularized Markov decision problem. This separates the main task of estimation (of the optimal policy from observed actions) from the inverse problem (of inferring rewards from a given policy). We find that even with perfect knowledge of the optimal policy, the corresponding rewards are not fully identifiable; nevertheless, the space of consistent rewards is parameterized by the value function of the control problem. In other words, the reward can be fully determined given the optimal policy and the value function, but the optimal policy gives us no direct information about the value function.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We further show that, given knowledge of the optimal policy under two different discount rates, or sufficiently different transition laws, we can uniquely identify the rewards (up to a constant shift). We also give conditions under which action-independent rewards, or time-homogenous rewards over finite horizons, can be identified. This demonstrates the fundamental challenge of inverse reinforcement learning, which is to disentangle immediate rewards from future rewards (as captured through preferences over future states).

<!-- chunk {"id": "body-0009", "role": "body", "section": "The environment", "weight": 1.0} -->

We consider a simple Markov decision process (MDP) on an infinite horizon. The MDP $\mathcal{M} = {(\mathcal{S},\mathcal{A},\mathcal{T},f,\gamma)}$ is described: a finite state space $\mathcal{S}$; a finite set of actions $\mathcal{A}$; a (Markov) transition kernel $\mathcal{T}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathcal{P}{(\mathcal{S})}}}$, that is, a function $\mathcal{T}$ such that $\mathcal{T}{(s,a)}$ gives probabilities^66^6Here, and elsewhere, we write $\mathcal{P}{(X)}$ for the set of all probability distributions on a set $X$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "The environment", "weight": 1.0} -->

of each value of $S_{t + 1}$, given the state $S_{t} = s$ and action $A_{t} = a$ at time $t$; and a reward function $f:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$ with discount factor $\gamma \in {\lbrack 0,1)}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "The environment", "weight": 1.0} -->

An agent aims to choose a sequence of actions $\{ A_{0},A_{1},\ldots\}$ from $\mathcal{A}$ in order to to maximize the expected value of total reward It will prove convenient for us to allow randomized policies $\pi$, that is, functions $\pi:{\mathcal{S}\rightarrow{\mathcal{P}{(\mathcal{A})}}}$, where $\pi{(\cdot |s)}$ is the distribution of actions the agent takes when in state $s$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "The environment", "weight": 1.0} -->

The classic objective in a MDP is to maximize the expected value ${\mathbb{E}}_{s}^{\pi}\left\lbrack {\sum_{t = 0}^{\infty}{\gamma^{t}f{(S_{t},A_{t})}}} \right\rbrack$. With this objective, one can show (for example, see Bertsekas and Shreve; Puterman) that there is an optimal deterministic control (i.e. a policy $\pi$, taking values zero and one, which maximizes the expected value). This implies that, typically, an optimal agent will only make use of a single action for each state, and the choice of this action will not vary smoothly with changes in the reward, discount rate, or transition kernel.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Entropy regularised MDP", "weight": 1.0} -->

Given the lack of smoothness in the classical MDP, and to encourage exploration, a well-known variation on the classic MDP introduces a regularization term based on the Shannon entropy. Given a policy $\pi$ and regularization coefficient $\lambda \geq 0$, the entropy regularized value of a policy $\pi$, when starting in state $s$, is defined by Here ${\mathcal{H}{(\pi)}} = {- {\sum_{a \in \mathcal{A}}{\pi{(a)}{\log{({\pi{(a)}})}}}}}$ is the entropy of $\pi$. We call this setting the regularised MDP $\mathcal{M}_{\lambda} = {(\mathcal{S},\mathcal{A},\mathcal{T},f,\gamma,\lambda)}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Entropy regularised MDP", "weight": 1.0} -->

The optimal value is given by ${{V_{\lambda}^{\ast}{(s)}}:={{\max_{\pi}V_{\lambda}^{\pi}}{(s)}}},$ where the maximum is taken over all (randomized feedback^77^7Given the Markov structure there is no loss of generality when restricting to policies of feedback form. Further, by replacing $\mathcal{A}$ with the set of maps $\mathcal{S}\rightarrow\mathcal{A}$ if necessary, all feedback controls $a{(s)}$ can be written as deterministic controls $a{(\cdot)}$ in a larger space, so when convenient we can consider controls which do not depend on the state without loss of generality.) policies $\pi:{\mathcal{S}\rightarrow{\mathcal{P}{(\mathcal{A})}}}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Entropy regularised MDP", "weight": 1.0} -->

If $\lambda$ is increased, this has the effect of 'flattening out' the choice of actions, as seen in the softmax function. Conversely, sending $\lambda\rightarrow 0$ will result in a true maximizer being chosen, and the regularized problem degenerates to the classical MDP.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Entropy regularised MDP", "weight": 1.0} -->

Adding a constant to the reward does not change the policy.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Remark 1", "weight": 1.0} -->

In many modern approaches, one replaces dependence on the state with dependence on a space of 'features'. This has benefits when fitting a model, but does not significantly change the problem considered.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Analysis of inverse reinforcement learning", "weight": 1.0} -->

We now shift our focus to 'inverse' reinforcement learning, that is, the problem of inferring the reward function given observation of agents' actions.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Analysis of inverse reinforcement learning", "weight": 1.0} -->

Consider a discrete time, finite-state and finite-action MDP $\mathcal{M}_{\lambda}$, as described in Section 2. Suppose a 'demonstrator' agent acts optimally, and hence generates a *trajectory* of states and actions for the system $\tau = {(s_{1},a_{1},s_{2},a_{2},\ldots)}$. We assume that it is possible for us to observe $\tau$ (over a long period), and seek to infer the reward $f$ which the agent faces.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Analysis of inverse reinforcement learning", "weight": 1.0} -->

A first observation is that, assuming each state $s \in \mathcal{S}$ appears infinitely often in the sequence $\tau$, and the agent uses a randomized feedback control $\pi_{\lambda}{(\left. a \middle| s \right.)}$, it is possible to infer this control. A simple consistent estimator for the control is Similarly, assuming each state-action pair $(s,a)$ appears infinitely often in $\tau$, we can infer the controlled transition probabilities $\mathcal{T}{(\left. s' \middle| {s,a} \right.)}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Analysis of inverse reinforcement learning", "weight": 1.0} -->

A simple consistent estimator is given by If our agent is known to follow a regularized optimal strategy, as, and we have a simple accessibility condition^88^8In particular, for every pair of states $s,s'$, there needs to exist a finite sequence ${s = {s_{1},s_{2},\ldots}},{s_{n} = s'}$ of states and $a_{1},\ldots,a_{n - 1}$ of actions such that ${\prod_{k = 1}^{n - 1}{\mathcal{T}{(\left. s_{k + 1} \middle| {s_{k},a_{k}} \right.)}}} > 0$. This is certainly the case, for example, if we assume ${\mathcal{T}{(\left.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Analysis of inverse reinforcement learning", "weight": 1.0} -->

s' \middle| {s,a} \right.)}} > 0$ for all ${s,s'} \in \mathcal{S}$ and $a \in \mathcal{A}$. on the underlying states, then every state-action pair will occur infinitely often in the resulting trajectory. Therefore, given sufficiently long observations, we will know the values of $\pi{(\left. a \middle| s \right.)}$ and $\mathcal{T}{(\left. s' \middle| {s,a} \right.)}$ for all ${s,s'} \in \mathcal{S}$ and $a \in \mathcal{A}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Analysis of inverse reinforcement learning", "weight": 1.0} -->

This leads, naturally, to an abstract version of the inverse reinforcement learning problem: Given knowledge of $\pi{(\left. a \middle| s \right.)}$ and $\mathcal{T}{(\left. s' \middle| {s,a} \right.)}$ for all ${s,s'} \in \mathcal{S}$ and $a \in \mathcal{A}$, and assuming $\pi$ is generated by an agent following an entropy-regularized MDP $\mathcal{M}_{\lambda}$, can we determine the initial reward function $f$ that the agent faces?

<!-- chunk {"id": "body-0024", "role": "body", "section": "Analysis of inverse reinforcement learning", "weight": 1.0} -->

As observed by Kalman, for an unregularized controller the only thing we can say is that the observed controls are maximizers of the state-action value function, and not even that these maximizers are unique. Therefore, very little can be said about the underlying reward in the unregularized setting. Indeed, as already observed in Russell the problem of constructing a reward using state-action data is fundamentally ill-posed. One pathological case is to simply take $f$ constant, so all actions are optimal. Alternatively, if we infer a unique optimal action $a^{\star}{(s)}$ for each $s$, we then could take any ${f{(s,{a^{\star}{(s)}})}} \in {(0,\infty\rbrack}$ and ${f{(s,a)}} = 0$ for $a \neq {a^{\star}{(s)}}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Further literature", "weight": 1.0} -->

One of the earliest discussions of inverse reinforcement learning (IRL) in the context of machine learning can be found in Ng and Russell. Their method is to first identify a class of reward functions, for an IRL problem with finitely many states and actions, a deterministic optimal strategy, and the assumption that the reward function depends only on the state variable. Then, assuming the reward function is expressable in terms of some known basis functions in the state, a linear programming formulation for the IRL problem is presented, to pick the reward function that maximally differentiates optimal policy from the other policies. This characterization of reward functions demonstrates the general non-uniqueness of solutions to IRL problems.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Further literature", "weight": 1.0} -->

In past two decades, there have been many algorithms proposed to tackle IRL problems. One significant category of algorithms (MaxEntIRL) arises from the maximum entropy approach to optimal control. In Ziebart, IRL problems were linked with maximum causal entropy problems with statistical matching constraints. Similar models can be found in Abbeel and Ng; Ziebart et al., Levine et al. and Boularias et al.. A connection between maximum entropy IRL and GANs has been established in Finn et al.. Further related papers will be discussed in the text below.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Further literature", "weight": 1.0} -->

In MaxEntIRL, one assumes that trajectories are generated^99^9As discussed by Levine, for deterministic problems this simplifies to ${P{(\tau)}} \propto {\exp{({\sum_{t}{f{(a_{t},s_{t})}}})}}$, which is often taken as a starting point. with a law for a constant $Z > 0$. Comparing with the distribution of trajectories from an optimal regularized agent, this approach implicitly assumes that ${\pi{(\left. a \middle| s \right.)}} \propto {\exp{\{{f{(a,s)}}\}}}$. Comparing, this is analogous to assuming the value function is a constant (from which we can compute $Z$) and $\lambda = 1$. This has a concrete interpretation: that many IRL methods make the tacit assumption that the demonstrator agent is myopic.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Further literature", "weight": 1.0} -->

As we shall see in Theorem 1, for inverse RL the value function can be chosen arbitrarily, demonstrating the consistency of this approach with our entropy-regularized agents. We discuss connections with MaxEntIRL further in Appendix Appendix: A discussion of guided cost learning and related maximum entropy inverse reinforcement learning models.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Inverse Markov decision problems", "weight": 1.0} -->

We consider a Markov decision problem as in Section 2. As discussed above, we assume that we have full knowledge of $\mathcal{S},\mathcal{A},\mathcal{T},\gamma$, and of the regularization parameter $\lambda$ and the entropy-regularized optimal control $\pi_{\lambda}$, but not the reward function $f$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Inverse Markov decision problems", "weight": 1.0} -->

Our first theorem characterizes the set of all reward functions $f$ which generate a given control policy.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 2", "weight": 1.0} -->

A simple degrees-of-freedom argument gives this result intuitively. There are $n = {|\mathcal{S}|}$ possible states and $k = {|\mathcal{A}|}$ possible actions in each state, so the reward function can be described by a vector in ${\mathbb{R}}^{n \times k}$. From the policy, which satisfies ${\sum_{a \in \mathcal{A}}{\pi{(\left. a \middle| s \right.)}}} = 1$ for all $s$, we observe $n \times {({k - 1})}$ linearly independent values. Therefore, the space of consistent rewards has ${{n \times k} - {n \times {({k - 1})}}} = n$ free variables, which we identify with the $n$ values ${\{{v{(s)}}\}}_{s \in \mathcal{S}}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Ng et al. provides a useful insight to our result. In Ng et al. it is assumed that the rewards are of the form $F{(S_{t},A_{t},S_{t + 1})}$; for a fixed MDP, this adds no generality, as we can write ${f{(s,a)}} = {{\mathbb{E}}{\lbrack{{\left. {F{(s,a,S_{t + 1})}} \middle| S_{t} \right. = s},{A_{t} = a}}\rbrack}}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Ng et al. show that, for any 'shaping potential' $\Upsilon:{\mathcal{S}\rightarrow{\mathbb{R}}}$, the reward $\overset{\sim}{F} = {{F + {\gamma\Upsilon{(S_{t + 1})}}} - {\Upsilon{(S_{t})}}}$ yields the same optimal policies for *every* (unregularized) MDP. However, shaping potentials do not describe the space of all rewards corresponding to a given policy, for fixed transition dynamics. In our results, we instead parameterize a family of costs $f$ in terms of the value function (Theorem 1), and show these are the only costs which lead to the given optimal policy *for a fixed (regularized) MDP*.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Given Theorem 1, we see that it is not possible to fully identify the reward faced by a single agent, given only observations of their policy. Fundamentally, the issue is that the state-action value function $Q$ combines both immediate rewards $f$ with preferences $v$ over the future state. If we provide data which allows us to disentangle these two effects, for example by considering agents with different discount rates or transition functions, then the true reward can be determined up to a constant, as shown by our next result. In order to clearly state the result, we give the following definition.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 4", "weight": 1.0} -->

Definition 1 is essentially a statement regarding invertibility of a linear system of equations for $w,\overset{\sim}{w}$. This indicates that the stability of the result of Theorem 2 is principally determined by whether this linear system is well conditioned, as can be measured by the ratio of its largest to second smallest singular values (the second smallest is due to the constant functions always being in the kernel of the system) not being too large. Given the inevitable error arising from statistical estimation of policies and transition functions, a well conditioned system is often a key requirement in practice. A similar observation will also be valid for the uniqueness results in later sections.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 5", "weight": 1.0} -->

Our results show that it is typically sufficient to observe an MDP under *two* environments (transitions and discount factors) in order to identify the reward. This can be contrasted with Amin and Singh and Amin et al. who show that, if the demonstrator is observed in multiple (suitably chosen) environments, the (state-only) reward can be identified up to a scaling and shift (the scaling is natural, given they do not use an entropy regularization). Ratliff et al. consider a finite number of environments, but explicitly do not attempt to estimate the 'true' underlying reward.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Finite horizon results", "weight": 1.0} -->

Over finite horizons, for general costs, similar results hold to those already seen on infinite horizons.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Finite horizon results", "weight": 1.0} -->

An entropy-regularized optimizing agent will use a policy $\pi^{\ast} = {\{\pi_{t}^{\ast}\}}_{t = 0}^{T - 1}$ which solves the following problem with terminal reward $g$ and (possibly time-dependent) running reward $f$: For any $\pi = {\{\pi_{t}\}}_{t = 0}^{T - 1}$, $s \in \mathcal{S}$, $a \in \mathcal{A}$, and $t \in {\{ 0,\ldots,{T - 1}\}}$ write Then, similarly to the infinite-horizon discounted case discussed in the main text, we have $V_{T}^{\ast} = g$ and for $t \in {\{ 0,\ldots,{T - 1}\}}$, Rearranging this system of equations, for any chosen function $v:{{{\{ 0,\ldots,T\}} \times

<!-- chunk {"id": "body-0039", "role": "body", "section": "Finite horizon results", "weight": 1.0} -->

a \middle| s \right.)}$ is the optimal strategy for the reward function in which case the corresponding value function is $V^{\ast} = v$. In other words, the identifiability issue discussed earlier remains. We note that identifying $\pi$ in this setting is more delicate than in the infinite-horizon case, as it is necessary to observe many finite-horizon state-action trajectories, rather than a single infinite-horizon trajectory.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Time-homogeneous finite-horizon identifiability", "weight": 1.0} -->

Following the release of a first preprint version of this paper, Kim et al. was published and presents a closely related analysis, for entropy-regularized deterministic MDPs with zero terminal value. We here give an extension of their result which covers the stochastic case and includes an arbitrary (known) terminal reward.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Time-homogeneous finite-horizon identifiability", "weight": 1.0} -->

The key structural assumptions made by Kim et al. are that the reward is time-homogeneous (that is, $f$ does not depend on $t$), and that there is a finite horizon. As discussed in the previous section, there is no guarantee that an arbitrary observed policy will be consistent with these assumptions (that is, whether there exists any $f$ generating the observed policy). However, given a policy consistent with these assumptions, and mild assumptions on the structure of the MDP, we shall see that unique identification of $f$ is possible up to a constant.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Time-homogeneous finite-horizon identifiability", "weight": 1.0} -->

Before describing our findings, we first present the following lemma^1010^10Thanks to Victor Flynn for discussion on the formulation and proof of this result. from elementary number theory, which will prove useful in what follows.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Remark 6", "weight": 1.0} -->

We have full action-rank if our actions are sufficiently varied that there are $N$ linearly independent such density vectors (cf., where it is the state--action occupation density which is considered).

<!-- chunk {"id": "body-0044", "role": "body", "section": "Example 1", "weight": 1.0} -->

Consider the problem with three states $\mathcal{S} = {\{ A,B,C\}}$, with possible transitions $A\rightarrow{\{ B,C\}}$, $B\rightarrow A$ and $C\rightarrow B$. Starting in state $A$, the shortest paths are then given by ${\{ A\}},{\{{A\rightarrow B}\}},{\{{A\rightarrow C}\}}$, and we have cycles $\{{A\rightarrow B\rightarrow A}\}$ and $\{{A\rightarrow C\rightarrow B\rightarrow A}\}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Example 1", "weight": 1.0} -->

Writing out the occupation densities of each of these paths (ignoring the terminal state of the two cycles), with $\gamma = 1$, we get the system \end{matrix} \right.} \\{\text{Cycles (excluding final state)}\left\{ \begin{matrix} \end{matrix} \right.} \end{array} & \begin{bmatrix} \end{matrix}\Rightarrow\begin{matrix} This corresponds to the final term on the right hand side of. Clearly, the section above the horizontal line (corresponding to the shortest paths) is lower-triangular, and hence of full rank. We prefix our paths by appropriate numbers of cycles, in order to make them the same length. This implies that, with a horizon $T = 7 = {{2 \times 3} + 1}$, we consider the paths The matrix of occupation densities shown here is the left hand side of and is easily seen to be full rank; the matrix $M$ from is given by We can extend this result to a stochastic setting, assuming that our action space is sufficiently rich.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Action-independent rewards", "weight": 1.0} -->

Earlier works such as Amin and Singh, Amin et al., Dvijotham and Todorov and Fu et al. consider the case of action-independent rewards, that is, where $f$ is not a function of $a$. In general, it is not immediately clear whether, for a given observed policy, the IRL problem will admit an action-independent solution. In this section, we obtain a necessary and sufficient condition under which an action-independent time-homogeneous reward function could be a solution to a given entropy-regularized, infinite-time-horizon^1313^13The analogous results for finite-horizon problems with time-inhomogeneous rewards (and general discount factor) can be obtained through the same method. IRL problem with discounting. We shall also obtain a rigorous condition under which a unique reward function can be identified.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Remark 7", "weight": 1.0} -->

Theorem 5 and Corollary 3 suggest various extensions, in the case when does not admit a solution, but the assumed property on the kernels in Corollary 3 holds. For example, one could consider the least-squares solution to the system (which is defined up to a constant). This gives a choice of value function which, in some sense, minimizes the action-dependence of the resulting cost function (obtained through Theorem 1).

<!-- chunk {"id": "body-0048", "role": "body", "section": "Remark 7", "weight": 1.0} -->

Fu et al. give a result similar to Corollary 3. Unfortunately, the role of the choice of actions in their conditions is not precisely stated, and on some interpretations is insufficient for the result to hold -- as we have seen, the condition of Corollary 3 is both necessary and sufficient for identifiability. We give a variation of their assumptions in what follows.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Remark 8", "weight": 1.0} -->

An equivalent definition would be that our MDP is reward-decomposable if $\mathcal{S}_{1} = \mathcal{S}$ is the only choice of nonempty set $\mathcal{S}_{1} \subset \mathcal{S}$ such that: there exists a set $\mathcal{S}_{0} \subset \mathcal{S}$ with every transition (with any action) to $\mathcal{S}_{1}$ is from $\mathcal{S}_{0}$, and every transition from $\mathcal{S}_{0}$ is to $\mathcal{S}_{1}$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 8", "weight": 1.0} -->

(In other words, $X_{t} \in \mathcal{S}_{0}$ if and only if $X_{t + 1} \in \mathcal{S}_{1}$.) We note that Fu et al. simply call this property 'decomposable', but this seems an unfortunate choice of terminology given this alternative characterization.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Remark 8", "weight": 1.0} -->

The following final corollary gives a simple set of conditions under which identification is possible, clarifying (and extending to the stochastic case) the result of.

<!-- chunk {"id": "body-0052", "role": "body", "section": "A linear-quadratic-Gaussian problem", "weight": 1.0} -->

We now present the corresponding results for a class of one-dimensional linear-quadratic problems with Gaussian noise, ultimately inspired by Kalman. This simplified framework allows us to explicitly observe the degeneracy of inverse reinforcement learning, even if we add restrictions on the choice of value functions.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Optimal LQG control", "weight": 1.0} -->

Suppose our agent seeks to control, using a real-valued process $A_{t}$ a discrete time process with dynamics for constants $\overline{\mu},\mu_{s},\mu_{a},\overline{\sigma},\sigma_{s},\sigma_{a}$. The innovations process $Z$ is a Gaussian white noise with unit variance. Our agent uses a randomized strategy $\pi{(\left.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Optimal LQG control", "weight": 1.0} -->

a \middle| s \right.)}$ to maximize the expectation of the entropy-regularized infinite-horizon discounted linear-quadratic reward: where ${f{(s,a)}} = {{\alpha_{20}s^{2}} + {\alpha_{11}sa} + {\alpha_{02}a^{2}} + {\alpha_{10}s} + {\alpha_{01}a} + \alpha_{00}}$ and $\mathcal{H}{(\pi)} = - \int_{\mathbb{R}}\pi{(a)}\log{(\pi{(a)}da}$ is the Shannon entropy of $\pi$. We assume the coefficients of $f$ are such that the problem is well posed (i.e. it is not possible to obtain an infinite expected reward).

<!-- chunk {"id": "body-0055", "role": "body", "section": "Optimal LQG control", "weight": 1.0} -->

Just as in the discrete state and action space setting, we can write down the state-action value function Using this, the optimal policy and value function are given by What is particularly convenient about this setting is that $Q$ is a quadratic in $(s,a)$, $V_{\lambda}$ is a quadratic in $s$, and $\pi_{\lambda}^{\ast}{(\cdot |s)}$ is a Gaussian density. In particular, the optimal policy is of the form for some constants ${{k_{1},k_{2}} \in {\mathbb{R}}},{k_{3} > 0}$, which can be determined^1414^14The explicit formulae for $k_{1},k_{2}$ and $k_{3}$, and the coefficients of the value function, can be obtained by equating the coefficients of $f$ with the values obtained. Under the assumption that the optimal control problem is well posed, this has a solution with $k_{3} > 0$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Numerical examples of inverse reinforcement learning", "weight": 1.0} -->

In this section, we present a regularized MDP as in Section 3.1 to illustrate numerically the identifiability issue associated with inverse RL. In particular, we consider a state space $\mathcal{S}$ with $10$ states and an action space $\mathcal{A}$ with $5$ actions, with $\lambda = 1$. We compute optimal policies as in Section 2 and reconstruct the underlying rewards. As discussed in Section 3 the optimal policies and the transition kernel can be inferred from state-action trajectories, so will assumed known. We identify the state and action spaces with the basis vectors in ${\mathbb{R}}^{10}$ and ${\mathbb{R}}^{5}$ respectively, so can write ${f{(a,s)}} = {a^{\top}Rs}$ for the reward function, and ${\mathcal{T}{(\left.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Numerical examples of inverse reinforcement learning", "weight": 1.0} -->

s' \middle| {s,a} \right.)}} = {s^{\top}P_{a}{(s')}}$ for the transition function. The true reward $R_{tr}$ and transition matrices ${\{ P_{a}\}}_{a \in \mathcal{A}}$ are randomly generated and fixed; see Figures 1 and 2.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Non-uniqueness of infinite-sample IRL", "weight": 1.0} -->

We first look at inverse RL starting from a single optimal policy $\pi_{1}$ with discount factor $\gamma_{1} = 0.95$. We represent $\pi_{1}$ as a matrix $\Pi_{1}$ in ${\mathbb{R}}^{5 \times 10}$, where each column gives the probabilities of each action when in the corresponding state.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Non-uniqueness of infinite-sample IRL", "weight": 1.0} -->

However, when comparing the learnt reward $\hat{R}$ and the underlying reward $R_{tr}$, as in Figures 4 and 5(a), as well as the comparison between the corresponding value vectors as in Figure 5(b), we can see that the true reward function $R_{tr}$ has not been correctly inferred. Here this is not an issue of statistical error, as we assume full information on the optimal policy and the Markov transition kernel.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Non-uniqueness of infinite-sample IRL", "weight": 1.0} -->

(a) Loss with one optimal policy, under γ1 (b) Loss with two optimal policies, under γ1 and γ2 Figure 3: Training Losses Figure 4: Learning from one optimal policy, under γ1: difference R̂ − Rtr between learnt and true reward matrices (a) ℓ2 error of learnt reward.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Uniqueness of IRL with multiple discount rates", "weight": 1.0} -->

We now demonstrate that the issue of identifiability can be resolved if there is additional information on an optimal policy under the same reward matrix $R_{tr}$ but different environment. Here, we assume we are given the policy $\Pi_{1}$ optimal with discount factor $\gamma_{1} = 0.95$, and the policy $\Pi_{2}$ optimal with discount factor $\gamma_{2} = 0.25$. Correspondingly, the loss function for the minimization is adjusted to An Adam optimizer is adopted with $\alpha = 0.005$, ${(\beta_{1},\beta_{2})} = {(0.5,0.9)}$ with overall 2000 minimization steps.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Uniqueness of IRL with multiple discount rates", "weight": 1.0} -->

With the same set of 6 random initializations for the minimization procedure, the training loss $L_{doub}$ also decays rapidly to close to 0. This again suggests that the learnt reward matrix $\overset{\sim}{R}$ can lead to policies ${\overset{\sim}{\Pi}}_{1}$ and ${\overset{\sim}{\Pi}}_{2}$, each optimal when using the corresponding discount factor $\gamma_{1}$ and $\gamma_{2}$, that are close to the given policies $\Pi_{1}$ and $\Pi_{2}$; see Figures 9 and 10. What differs from the single optimal policy case is that, with the additional information $\Pi_{2}$, we are able to consistently recover $R_{tr}$ up to a constant shift; see Figures 6 and 7. Some numerical error remains, due to the optimization algorithm used, as seen by the fact the graphs in Figure 6 do still vary, and the error in the value function $v_{1}$ in 7(a).

<!-- chunk {"id": "body-0063", "role": "body", "section": "Uniqueness of IRL with multiple discount rates", "weight": 1.0} -->

Nevertheless, the errors are an order of magnitude less than was observed in Figure 5 when using observations under a single discount rate.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Uniqueness of IRL with multiple discount rates", "weight": 1.0} -->

(a) ℓ2 error of learnt value function v1 with discount γ1 (b) ℓ2 error of learnt value function v2 with discount γ2 (c) ℓ2 error of learnt reward matrix Figure 7: Two optimal policies under γ1 and γ2: comparisons Figure 8: Learning from optimal policy under γ1: difference Π̂1 − Π1 between optimal policy under the learnt model and the true optimal policy. Note scale of 10−4.
