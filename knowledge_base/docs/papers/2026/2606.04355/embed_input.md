<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Think Fast and Far: Long-Horizon Online POMDP Planning via Rapid State Sampling

Topics include POMDPs, Online planning, Horizon, Sampling methods, Partial observability, Robotics, Sampling-based planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Targets long-horizon online POMDP planning with a rapid state-sampling strategy that searches farther ahead under partial observability. The paper contributes to the practical planning side of POMDPs, where computation must be spent selectively during online decision making.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Partially Observable Markov Decision Processes (POMDPs) are a general and principled framework for motion planning under uncertainty. Despite tremendous improvement in the scalability of POMDP solvers, long-horizon POMDPs remain difficult to solve. To alleviate the difficulty, this paper proposes a new approximate online POMDP solver, called Reference-Based Online POMDP Planning via Rapid State Space Sampling (ROP-RAS3). ROP-RAS3 uses novel extremely fast sampling-based motion planning techniques to sample the state space and generate a diverse set of macro actions online, which are then used to bias belief-space sampling and infer high-quality policies without requiring exhaustive enumeration of the action space - a fundamental constraint for modern online POMDP solvers. ROP-RAS3 converges to a near-optimal reference-based solution at a rate that depends on the number of sampled actions, rather than the size of the action space. ROP-RAS3 is evaluated on various long-horizon POMDPs with up to 3000 lookahead steps and 35-dimensional state spaces, where the state, action and observation spaces can be continuous, discrete, or a hybrid of discrete and continuous.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Although the reference-based optimal solution may not be the same as the optimal POMDP solution, empirical results indicate that in all of these problems, in terms of success rate, ROP-RAS3 outperforms other state-of-the-art methods by up to multiple folds. We also demonstrate the capability of our approach on a physical robot demonstration. This work extends the theory and empirical results of our paper. Code can be found at \texttt{

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motion planning in partially observed and non-deterministic environments is a critical component of reliable and robust robot operation. Partially Observable Markov Decision Processes (pomdps) (SS1973; klc1998) are a natural way to formulate such problems. The key insight of the pomdp framework is to represent uncertainty on the effects of actions, perceptions and initial states as probability distributions, and then reason about the best strategy to perform with respect to distributions over the problem's state space, called *beliefs*, rather than the state space itself.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although pomdps' methodical reasoning about uncertainty comes at the cost of high computational complexity (PT1987), the pomdp framework is practical for many robotics problems, thanks in large part to sampling-based approaches. These approaches relax the problem of finding an optimal solution to an approximate one by sampling states from the belief space and computing the best action from only the samples. Scalable anytime methods under this approach (surveyed by kurniawatiSurvey) have been proposed for solving large pomdp problems. However, computing good solutions to long-horizon (*e.g.*, $\geq 15$ look-ahead steps) pomdps remains difficult. Here, look-ahead steps refer to the minimum number of actions needed for the agent to identify which action is most beneficial to reach the goal under the partially observable characteristics of the problem.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Early results from the literature (KDHL2011) indicate that Sampling-Based Motion Planning (sbmp)---sampling-based approaches designed for deterministic motion planning---can be used to tackle the challenges of long-horizon problems in offline pomdp planning. Specifically, sbmps can be used to generate suitable macro-actions (*i.e.*, sequences of actions) to reduce the effective planning horizon for a pomdp solver. Macro-actions generated via sbmp automatically adapt to geometric features of the valid region and tend to cover diverse paths in the state space.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although this approach performs well for offline pomdp planning, it is often impractical for online planning for two reasons. First is the speed of sbmps, which historically required hundreds of milliseconds to tens of seconds to find a single motion plan. Second, most online pomdp planners (sv10; kurniawati2016online; despot17) exhaustively enumerate each action at each sampled belief in computing the best action to perform. Such enumerations limit the number of actions sampled at run time, hence restricting online planners to quickly cover a good reachable belief space, from which the optimal solution can be computed efficiently (easypomdp). However, the recently proposed Vector-Accelerated Motion Planning (vamp) framework (tkk23) enables sbmps to find solutions on microsecond timescales, multiple orders of magnitude faster than prior approaches. Concurrently, recently proposed *reference-based pomdp planners* (kkk23) remove the requirement for exhaustive enumeration of the entire action space to compute approximately optimal POMDP solutions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Leveraging the above two advances, we propose an online pomdp solver, called Reference-Based Online pomdp Planning via Rapid State Space Sampling (rop-r a s 3 ), which is a reference-based pomdp planner that employs a vamp-enhanced macro-action sampler as its underlying reference policy. We modify the formulation from kkk23 so that the reference is defined as a policy instead of a belief-to-belief transition, which makes it easier to generate suitable macro-actions and apply them to the reference-based pomdp solving approach. We show that the modified reference-based Bellman backup naturally allows processing continuous action spaces by replacing the optimization procedures in the pomdp Bellman backup with expectations. By adopting the analysis strategy used:IJCAI; lim2023optimality, we show a convergence rate that depends on $C_{\mathcal{A}}$, the number of actions a planner samples at each belief node instead of $|\mathcal{A}|$, the size of the action space reported:IJCAI; lim2023optimality.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although an optimal solution of a reference-based pomdp can be different from the original pomdp, the empirical section of our work demonstrates how this formulation enables us to solve challenging robotics tasks. We evaluate rop-r a s 3 on multiple long-horizon pomdps, including 4 navigation tasks and 3 manipulation tasks, which require planning horizons of hundreds to thousands of steps. Comparisons with state-of-the-art online pomdp planners---including pomcp (sv10), a pomcp modification that uses vamp to generate macro-actions, and despot (despot17) with learned macro-actions (lee.rss; KL2023)---indicate that rop-r a s 3 substantially outperforms state-of-the-art methods in all evaluation scenarios. Learning-based methods like magic (lee.rss) do not naturally extend to high-dimensional motion planning domains, but rop-r a s 3 is able to solve problems with dimensionality up to 35. rop-r a s 3 is also deployed to a Hello-Robot Stretch 3 mobile base manipulator.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In our pedestrian crossing scenario, rop-r a s 3 is the only method that demonstrates smart maneuvers to dodge a moving pedestrian and navigate to the goal. Our code will be released after publication.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Remark. This work extends our paper Liang2024Scaling. We modified the original algorithm to deal with continuous action and observation spaces and provided a neater way to do backups in the belief tree. The convergence analysis of rop-r a s 3 is added together with 3 new manipulation simulations and 1 physical robot demonstrations.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Sampling-Based Motion Planners", "weight": 1.0} -->

Sampling-based motion planning (sbmp) is a common, effective family of algorithms (*e.g.*, Kavraki1996; Kuffner2000) for solving *deterministic* motion planning problems (LaValle2006). They are able to find collision-free motions for high degree-of-freedom (d o f) robots in environments containing many obstacles by drawing samples from a robot's *configuration space*, the set of all possible robot configurations, $q\in Q$. Collisions between the robot and the environment or with itself partition the configuration space into *valid* ($Q_{\text{free}}$) and *invalid* ($Q\setminus Q_{\text{free}}$) configurations.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Sampling-Based Motion Planners", "weight": 1.0} -->

A deterministic *motion planning problem* is then a tuple $(Q_{\text{free}},q_{I},Q_{G})$ representing the task of finding a continuous path, $p:\rightarrow Q_{\text{free}}$, from an initial configuration, $q_{I}$, to a goal region, $Q_{G}\subseteq Q_{\text{free}}$ (*i.e.*, $p=q_{I}$ and $p\in Q_{G}$). sbmps solve such problems by building a discrete approximation of $Q_{\text{free}}$ as a graph or tree connecting sampled configurations in $Q_{\text{free}}$ by short, local motions. Once both $q_{I}$ and $Q_{G}$ are connected by this structure, a valid robot motion plan can be found with graph search methods. The solutions are deterministic, open-loop plans, and may not be robust against uncertainties or changes in configuration spaces.

<!-- chunk {"id": "body-0015", "role": "body", "section": "POMDP Background", "weight": 1.0} -->

An infinite-horizon pomdp is defined as the tuple $\langle\mathcal{S},\mathcal{A},\mathcal{O},\mathcal{T},\mathcal{Z},R,{\gamma},b_{0}\rangle$ where $\mathcal{S}$ denotes the set of all possible states of the system being considered, $\mathcal{A}$ denotes the set of all possible actions, and $\mathcal{O}$ denotes the set of all possible observations. We assume measures are properly defined for these spaces. In our context, the state space encompasses the robot's configuration space ($\mathcal{S}\equiv Q$). The transition function $\mathcal{T}({s^{\prime}}\,|\,s,a)$ is the conditional probability that the robot will be in state ${s^{\prime}}\in\mathcal{S}$ after performing action $a\in\mathcal{A}$ from state $s\in\mathcal{S}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "POMDP Background", "weight": 1.0} -->

The observation function $\mathcal{Z}(o\,|\,{s^{\prime}},a)$ is the conditional probability that the agent perceives $o\in\mathcal{O}$ when it is in state ${s^{\prime}}\in\mathcal{S}$ after performing action $a\in\mathcal{A}$. The reward is a bounded real-valued function $R:\mathcal{S}\times\mathcal{A}\rightarrow\mathbb{R}$. The parameter ${\gamma}\in$ is the discount factor which ensures the objective function is well-defined.

<!-- chunk {"id": "body-0017", "role": "body", "section": "POMDP Background", "weight": 1.0} -->

In general, the robot does not know the true state. At each time-step, the robot maintains a *belief* about its state, which is a probability distribution over the state space. The space of all possible beliefs is denoted by $\mathcal{B}:=\varDelta(\mathcal{S})$. The agent starts from a given initial belief, denoted as $b_{0}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "POMDP Background", "weight": 1.0} -->

If $b^{\prime}$ denotes the agent's next belief after taking an action $a\in\mathcal{A}$ and receiving the corresponding observation $o\in\mathcal{O}$, then the updated belief is given by For any given belief $b$ and action $a$, the expected reward is given by $R(b,a):=\int_{s\in\mathcal{S}}R(s,a)b(s)\textup{d}s$. A (stochastic) *policy* is a mapping ${\pi}:\mathcal{B}\rightarrow\varDelta(\mathcal{A})$. We denote its distribution for any given input $b\in\mathcal{B}$ by ${\pi}(\cdot\,|\,b)$. A policy is *deterministic* if it only has support at a single point $a\in\mathcal{A}$. Let $\Pi$ be the class of all policies.

<!-- chunk {"id": "body-0019", "role": "body", "section": "POMDP Background", "weight": 1.0} -->

Given a policy ${\pi}\in\Pi$, we define the *value function* $V^{\pi}:\mathcal{B}\rightarrow\mathbb{R}$ to be the expected total discounted reward, $V^{\pi}(b):=\mathbb{E}[\sum_{t=0}^{\infty}{\gamma}^{t}R\big(b_{t},a_{t})\big)]$, where the expectation is taken with respect to the policy and the transition probability.

<!-- chunk {"id": "body-0020", "role": "body", "section": "POMDP Background", "weight": 1.0} -->

In this paper, a *solution* to the pomdp is a deterministic policy ${{\pi}}^{*}\in\Pi$ satisfying on $\mathcal{B}$. The Bellman equation is satisfied by the optimal value function $V^{{{\pi}}^{*}}$. The intrinsic conditional probability is the probability that the agent perceives $o$, having performed the action $a$, under the belief $b$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Long-Horizon POMDPs", "weight": 1.0} -->

Solving long-horizon pomdps is a significant challenge: the branching factor as a result of actions and observation grows exponentially with respect to the planning horizon. Planning over *macro-actions* (i.e., a set of action sequences) is a common approach to deal with long-horizon pomdps (theo2003; he10:puma; KDHL2011; flaspohler; lee.rss; KL2023). Although this reduces the effective planning horizon, choosing a set of good macro-actions for planning is critical and automatic construction of macro-actions can require significant effort; *e.g.*, the learning time for magic (lee.rss) can be on the order of hours.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Long-Horizon POMDPs", "weight": 1.0} -->

Irrespective of macro-action use, most online pomdp planners (sv10; kurniawati2016online; despot17) exhaustively enumerate all actions from each sampled belief in order to estimate the optimal action. Many efficient optimization methods, which are generally based on gradient ascent, cannot be used effectively because computing the gradient of the pomdp value function is very expensive. Therefore, existing planners seldom explore long-term information and tend to perform poorly for horizons greater than 15 steps.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Long-Horizon POMDPs", "weight": 1.0} -->

Recently, kkk23 have mitigated this limitation by solving a *reference-based pomdp*: a reformulated pomdp whose reward objective incurs a kl-penalty for deviating too far from a given stochastic *reference belief-to-belief transition*: $\bar{U}(a,o\mid b):=P(o\mid a,b)\bar{{\pi}}(a\,|\,b)$ where $\bar{{\pi}}$ is a given stochastic reference policy. The reward with respect to $U$ is defined as $R(b,U):=\int_{\mathcal{A},\mathcal{O}}R(b,a)\allowbreak U(a,o\mid b)\textup{d}a\textup{d}o$. The value of a belief is given by where $\mathcal{U}(b)\subseteq\Delta(\mathcal{A}\times\mathcal{O})$ is the set of admissible transitions at belief $b$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Long-Horizon POMDPs", "weight": 1.0} -->

The rhs can be optimized analytically, effectively removing the need for enumerative optimization in online pomdp solving and thereby reducing the branching factor of the belief tree. Preliminary results from kkk23 indicate that policies generated by this procedure can outperform state-of-the-art pomdp benchmarks on long-horizon pomdps. However, the assumption of having access to a belief-to-belief transition is very strong and cumbersome to work with in practice. kkk23 also employs relatively crude reference policies and does not incorporate macro-actions into planning.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Convergence of Online Sampling-based POMDP Planners", "weight": 1.0} -->

Despite many empirical advances for online pomdp planning, little theoretical justification for the convergence rates of these planners has been provided. Recently,:IJCAI; lim2023optimality formally showed that a planner that uses observation likelihood weightings (a technique adopted by many online pomdp planners) can estimate Q-values accurately with a convergence rate $\mathcal{O}(|\mathcal{A}|(|\mathcal{A}|C_{\mathcal{S}})^{D}\exp(-t_{\max}C_{\mathcal{S}}))$, where $|\mathcal{A}|$ is the size of the action space, $C_{\mathcal{S}}$ is the number of state samples in a belief node, $D$ is the depth of the belief tree and $t_{\max}$ is a problem-specific bounding constant. The key of their analysis is to treat observation likelihood weighting as a self-normalized (SN) importance sampling process (shachter1990simulation).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Convergence of Online Sampling-based POMDP Planners", "weight": 1.0} -->

The latter aims to estimate the expectation of an arbitrary function $f(x)$ where $x$ is drawn from distribution $\mathcal{P}$, while the estimator only has access to another distribution $\mathcal{Q}$ along with the importance weights $\omega_{\mathcal{P}/\mathcal{Q}}\propto\mathcal{P}/\mathcal{Q}$. The following three quantities related to importance sampling are frequently used, Here, is the SN importance weight, is the Rényi divergence and is the SN estimator. Central to their analysis is the following self-normalized $d_{\infty}$-concentration bound, where $d_{\infty}$ is the infinite Rényi divergence.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Continuous Reference-Based POMDPs over Stochastic Actions", "weight": 1.0} -->

The concept of a reference-based pomdp was introduced in kkk23 as a generalization to pomdps of the mdp formulations using kl-penalization in azar12; todorov. One limitation is that the formulation given by is somewhat artificial in that reference policies are stated with respect to *belief-to-belief* transitions (see discussion in §8 of kkk23). In this paper, we will use a more natural formulation of a reference-based pomdp over *stochastic policies* rather than *belief-to-belief transitions* as in kkk23. This allows us to directly work with reference policies which are easy to define and handcraft compared to belief-to-belief transitions. Further, the latter is less realistic as one does not have the choice of picking specific observations that resulted in the desired transitions, but is allowed to choose heuristic reference policies. Note that in doing so, all the benefits of the formulation in kkk23 are still preserved.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Continuous Reference-Based POMDPs over Stochastic Actions", "weight": 1.0} -->

Specifically, a reference-based pomdp over stochastic actions is specified by the tuple $\langle\mathcal{S},\mathcal{A},\mathcal{O},\mathcal{Z},\mathcal{T},R,{\gamma},\eta,{\bar{{\pi}}}\rangle$. The presentation here treats the state, action and observation spaces as continuous spaces and assumes that the associated Borel $\sigma$-algebra exists and probability measures are properly defined with respect to the underlying $\sigma$-algebra. In addition to the standard parameters, we have a *temperature* parameter $\eta>0$ and a given (stochastic) *reference policy* ${\bar{{\pi}}}(\cdot\,|\,b)$. We assume that ${\bar{{\pi}}}(\cdot\mid b)>0,\forall b\in\mathcal{B}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Continuous Reference-Based POMDPs over Stochastic Actions", "weight": 1.0} -->

The value $\mathcal{V}$ (distinguished from the pomdp $V$-value) of a reference-based pomdp for a given $b\in\mathcal{B}$ satisfies the reference-based Bellman equation, where $R(b,{\pi}):=\int_{\mathcal{A},\mathcal{S}}R(s,a){\pi}(a\,|\,b)b(s)\;\textup{d}a\;\textup{d}s$ is the reward estimate. A *solution* is a stochastic policy ${\pi}\in\Pi$ that maximizes $\mathcal{V}$. The problem can therefore be viewed as a kl-penalized pomdp whose objective is modified to trade off two (potentially competing) objectives: abide by the reference policy, and maximize reward.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Continuous Reference-Based POMDPs over Stochastic Actions", "weight": 1.0} -->

The trade-off is balanced by $\eta$ and the *quality* of the reference policy---higher-quality reference policies are those that reduce the kl-divergence between the solution of the unpenalized pomdp and the reference policy. The kl-penalty implies that ${\pi}(\cdot\mid b)\ll{\bar{{\pi}}}(\cdot\mid b)$ for any $b\in\mathcal{B}$. When the optimal policy is used as the reference policy, we trivially obtain the optimal policy as the solution, since the optimal policy is deterministic and the only solution that maximizes rewards and minimizes KL divergence is itself.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Continuous Reference-Based POMDPs over Stochastic Actions", "weight": 1.0} -->

For an arbitrary ${\bar{{\pi}}}$, the supremum in can be attained analytically by extending an argument of azar11; azar12 to pomdps,

<!-- chunk {"id": "body-0032", "role": "body", "section": "Algorithm", "weight": 1.0} -->

3: sample source state, s ∼ b̄ 4: sample target state, s′ ∼ 𝒥(⋅ ∣ b̄) 5: construct a motion plan, p ← sbmp(s, s′) 6: convert a motion plan to a macro-action, $\vec{a}=\textsc{PathToMacroAction}(p)$ 7: append the new action, l = l ∪ {a⃗} Algorithm 1 Online pomdp Planner Tree Expansions with sbmp-Generated Macro Actions We introduce Reference-Based Online pomdp Planning via Rapid State Space Sampling (rop-r a s 3), our online anytime planner that uses sampling techniques to rapidly estimate $\mathcal{V}$-Values and $\mathcal{Q}$-Values for inferring good actions to execute. We motivate its design by briefly outlining vamp's capability to induce high-quality reference policies. A general algorithm is proposed to utilize vamp to infer actions for online pomdp planning. Then we elaborate rop-r a s 3 and analyze its online convergence rate.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Vector Accelerated Motion Planning (VAMP)", "weight": 1.0} -->

Towards fast deterministic motion planning, recent works have introduced new perspectives on *hardware-accelerated* sampling-based motion planning (sbmps), using either cpu single-instruction, multiple-data (simd) (tkk23) or gpu single-instruction, multiple-thread (simt) (sundaralingam2023curobo) parallelism to find complete motion plans in tens of microseconds to tens of milliseconds. In particular, the authors of vamp (tkk23) proposed a simd-vectorized approach to computing sbmp primitives (*i.e.*, local motion validation) that applies to all sbmps thus, it is now possible to generate probabilistically-complete, global, collision-free trajectories for high-d o f systems at kilohertz rates---on the scale of tens of thousands of plans per second. The key insight of this work is to lift the "primitive" operations of the sbmp (e.g. forward kinematics and collision checking) to operate over *vectors* of configurations in parallel.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Vector Accelerated Motion Planning (VAMP)", "weight": 1.0} -->

Robot-specific code that uses these vector primitives is generated from a URDF using a tracing compiler---this pre-processing step is general to any robot. Functionally, this enables checking validity of a spatially distributed set of configurations over a candidate motion in parallel for the cost of a single collision check, massively lowering the expected time it takes to find colliding configurations along said motion. This development has called into question previously held perceptions that sbmps are relatively time-expensive subroutines and---in the context of planning under uncertainty---opens the door to using sbmps to guide pomdp planning on the fly.

<!-- chunk {"id": "body-0035", "role": "body", "section": "POMDP Planning with SBMP-Generated Trajectories", "weight": 1.0} -->

A stochastic reference policy can be constructed from a deterministic policy. In robotics, such a representation can be naturally obtained by integrating deterministic motion plans with belief space sampling. We begin by presenting a general tree node expansion mechanism in Algorithm 1 to integrate belief-space sampling of a canonical online pomdp planner with state space sampling to generate macro-actions using sbmp. Since an expansion mechanism to get new actions for a new belief node is universal in online pomdp planning, Algorithm 1 can use any sbmp planner and can generalize to most existing online particle-based pomdp planners, such as pomcp (sv10), despot (despot17) and their derivatives (kurniawati2016online; hypdespot21; lee.rss; KL2023).

<!-- chunk {"id": "body-0036", "role": "body", "section": "POMDP Planning with SBMP-Generated Trajectories", "weight": 1.0} -->

At a newly encountered belief node $\bar{b}$, SBMPExpand in Algorithm 1 aims to expand $C_{\mathcal{A}}$ of actions by firstly sampling a source state from the belief particles. In line 4, a target state is drawn from a distribution $\mathcal{J}(\cdot\mid\bar{b})$, a distribution over the state space $\mathcal{S}$ conditioned on the current belief particles. In robotics, target states can be states that reveal a certain amount of information to the robot, including states with high reward or penalty and states with observations. A deterministic motion plan is then constructed using any existing sbmp in line 6. The path is converted to a macro-action via PathToMacroAction and added to the return list.

<!-- chunk {"id": "body-0037", "role": "body", "section": "POMDP Planning with SBMP-Generated Trajectories", "weight": 1.0} -->

The choice of sbmp is an essential component for achieving high-quality policies online. vamp enables rapid generation of collision-free state space paths to goals or to highly informative states, which in turn can be used as macro-actions for the pomdp planner. Thus, promising macro-actions can be dynamically created as a subroutine (line 5 in SBMPExpandTree) *within* a pomdp planner itself in fractions of a second. In contrast, the state-of-the-art planner magic (lee.rss) takes on the order of hours to learn macro-actions.

<!-- chunk {"id": "body-0038", "role": "body", "section": "POMDP Planning with SBMP-Generated Trajectories", "weight": 1.0} -->

However, fast macro-action sampling alone is not sufficient, as current online pomdp planners perform numerical optimization via enumeration of *all* (macro) actions at each sampled belief, which results in a time and space complexity of $\mathcal{O}(|\vec{\mathcal{A}}|^{h})$, where $\vec{\mathcal{A}}$ denotes the space of the macro-actions, $h$ is the planning horizon. This complexity significantly limits the number of macro-actions and the depth of the tree it can construct, thereby significantly limiting the benefit of sbmp for pomdp solving. To tackle this problem, we propose rop-r a s 3 next that draws on insights from Section 4 while, in tandem, exploiting the speed of vamp (tkk23)---an implementation of simd-vectorized sbmp---to create a rich set of diverse macro-actions, which the planner uses to efficiently explore relevant parts of the belief space.

<!-- chunk {"id": "body-0039", "role": "body", "section": "ROP-RAS3", "weight": 1.0} -->

1:Initialize tree T rooted at b̄ 2:while time permitting do 5:$\vec{a}\leftarrow\textsc{ActionProgressiveWiden}(\bar{b},s)$ 6:Sample (s′, o⃗, r(s, a⃗; γ)) from generative model 𝒢(s, a⃗) 10: sample o⃗ from 𝒞(b̄a) w.p $\frac{M(\bar{b}\vec{a}\vec{o})}{\sum_{\vec{o}}M(\bar{b}\vec{a}\vec{o})}$ 12:Create nodes for b̄a⃗ and b̄a⃗o⃗ if not created already 13:Add s′ to belief particles of b̄a⃗o⃗ 14:return ${{\mathcal{V}}}(\bar{b})\leftarrow\textsc{Backup}(\bar{b},\vec{a},\vec{o},r)$ 2: return $\textsc{SampleMacroActionSBMP}(\bar{b},s)$

<!-- chunk {"id": "body-0040", "role": "body", "section": "ROP-RAS3", "weight": 1.0} -->

4:Sample a⃗ from b̄.children uniformly 1:Get the current configuration qstart from s (assert free) 2:$q_{\text{goal}}\leftarrow\textsc{SampleHeuristics}(\bar{b})$ (assert free) 3:Plan path p from qstart to qgoal using fast sbmp 4:return $\vec{a}=\textsc{PathToMacroAction}(p)$ 1:$r\rightarrow r+{\gamma}\textsc{SIMULATE}(b\vec{a}\vec{o})$ 4:$\mathcal{Q}(\bar{b}\vec{a})\leftarrow\mathcal{Q}(\bar{b}\vec{a})+\frac{r-\mathcal{Q}(\bar{b}\vec{a})}{N(\bar{b}\vec{a})}$

<!-- chunk {"id": "body-0041", "role": "body", "section": "ROP-RAS3", "weight": 1.0} -->

5:$\mathcal{V}(\bar{b})\leftarrow\frac{1}{\eta}\log\Big[\exp(\eta\mathcal{V}(\bar{b}))+\frac{\exp(\eta\mathcal{Q}(\bar{b}\vec{a}))-\exp(\eta\mathcal{V}(\bar{b}))}{N(\bar{b})}\Big]$ We propose rop-r a s 3 (Algorithm 2), a practical and scalable reference-based pomdp online planner for motion planning under uncertainty.

<!-- chunk {"id": "body-0042", "role": "body", "section": "ROP-RAS3", "weight": 1.0} -->

We use arrows on top of letters to indicate macro elements associated to that letter (e.g. $\vec{a}$ is a macro action). With a slight abuse of notation, $\bar{b}$ denotes the belief node in a tree, $\bar{b}\vec{a}$ denotes the action node $\vec{a}$ associated with $\bar{b}$ and $\bar{b}\vec{a}\vec{o}$ is the next belief node given $\vec{a}$ and $\vec{o}$. The curly $\mathcal{C}(\cdot)$ indicates the children of a belief node (e.g. $\mathcal{C}({\bar{b}})$ returns all actions associated with $\bar{b}$). And $N(\cdot)$ denotes the visitation count of a node. Values are initialized to zero by default.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Numerical Backup", "weight": 1.0} -->

Recall from Theorem 2, the reference-based Bellman backup can be broken down into two parts, the $\mathcal{Q}$-value defined in and the $\mathcal{V}$-value defined. The $\mathcal{Q}$-value can be viewed as an expected total future reward, $\mathcal{Q}(\bar{b}\vec{a})\approx\frac{1}{N(\bar{b}\vec{a})}\sum_{i=1}^{N}R_{i}$, where $R_{i}$ is the reward return from the $i$-th simulation at the node $\bar{b}\vec{a}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Numerical Backup", "weight": 1.0} -->

From, by realizing that $\exp(\eta\mathcal{V}(b))=\mathbb{E}[\exp(\eta\mathcal{Q}(b,a))]$, we can then estimate this term with $\frac{1}{N(\bar{b}\vec{a})}\sum_{i=1}^{N}\exp(\eta\mathcal{Q}(b,a))$. The iterative versions of both estimators are given in line 4 and 5 of the Backup function in Algorithm 2. Further details and convergence rates of such nested Monte Carlo Estimators can be found in rainforth2018nesting.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Numerical Backup", "weight": 1.0} -->

Due to the closed-form solution found in Theorem 2, we do not need to solve the bandit problem, which is typical of many online pomdp planners, dropping the need for UCB-like techniques. Second, without the need to expand all actions encountered at a given new node and restarting search from the root node, we can search deeper earlier by continuing to simulate from the newly sampled action, prioritizing long-horizon search commonly found in many robotics problems. Such tree search strategy is tightly linked to the backup equation.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Planning Tree Construction", "weight": 1.0} -->

rop-r a s 3 uses unweighted belief particles. This has the speed advantage of only retaining particles that have been sampled and obtained from the generative model during simulations. In simulation, rop-r a s 3 aims to get an action and query the generative model to simulate for the next state, rewards and observations. Since both the action space and the observation space can be continuous, we apply the double progressive widening technique (sunberg2018online) to ensure sampled elements can be revisited again in a new simulation. Our progressive widening technique is different to the standard implementation in the sense that we only need to uniformly sample from the existing actions and observations if the widenning condition is not met, thanks to Monte Carlo estimations in our backup procedures. If the condition of expanding a new action is met, then rop-r a s 3 proceeds to query a macro action $\vec{a}$ from a reference policy induced from a sbmp (see SampleMacroActionSBMP), instead of uniformly sampling from the free action space as done in (sunberg2018online).

<!-- chunk {"id": "body-0047", "role": "body", "section": "Planning Tree Construction", "weight": 1.0} -->

The generative model $\mathscr{G}$ is used to simulate for the next state, reward and observations. The macro action, observation, and the next state is added to the tree if they are not created yet. This repeats up to a predefined depth $D$. When the required depth is reached, rop-r a s 3 obtains an estimate of the node's value by rollouts, a standard operation used by other online planners. The planner then approximates the exact backup (Backup) by carefully *maintaining* an empirical expectation, repeating backups on the simulated belief-tree path up to the root node. The above procedure is repeated until exhausting a computation budget (e.g., time), at which point the estimate of the optimal policy is read off from the tree's root node via.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Reference Policy", "weight": 1.0} -->

The simplicity offered by the formulation comes at a cost: if the optimal policy of the pomdp with an unmodified objective is too far from the reference policy (in the sense of the kl-divergence), pure reward maximization can be compromised. Of course, the optimal policy and hence this divergence are not known a priori. Instead rop-r a s 3 assumes that reference policies generated by accelerated sbmps (vamp) provide a reasonable starting point, leveraging them to rapidly sample high-quality deterministic policies to induce a reasonable partially observed reference policy which it deforms online. The subroutine SampleMacroActionSBMP acts as the foundation for our reference policies. It lifts vamp to belief space by sampling a state from the input belief particles, pick a target state with information (observation or reward) and query vamp to build a deterministic motion plan connecting the two states. This motion plan is then converted to macro actions for rop-r a s 3. The target states can be either uniformly drawn from the free space or dynamically sampled based on the belief of the agent.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Reference Policy", "weight": 1.0} -->

Sampling these informative states ensure our planning tree only cover a compact reachable belief space, retaining optimal solution while reducing the search complexity as uninformative path occurs less frequently.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Reference Policy", "weight": 1.0} -->

We emphasize that this modification is not negligible. Indeed, our results show that the performance deteriorates with problem complexity if the agent only executes the sbmp reference policy as an open-controller without planning for uncertainty. More implementation details are discussed in Section 5 and our code website.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

$\hat{Q}_{d}(\bar{b},a)=\frac{\sum_{i=1}^{C_{\mathcal{S}}}\omega_{i}r_{i}+{\gamma}\textsc{Estimate-}\mathcal{V}(\bar{b}^{\prime},d+1)}{\sum_{i=1}^{C_{\mathcal{S}}}\omega_{i}}$ Algorithm 3 Reference-based Sparse Sampling With the maximization steps in pomdp planning being replaced by an expectation estimation, rop-r a s 3 's convergence can be analyzed by bounding $\mathcal{Q}$-value estimations and $\mathcal{V}$-Value estimations at all nodes of the tree.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

To make analysis tractable, we simplify rop-r a s 3 and distill its core computations into a theoretical algorithm, Reference-based Sparse Sampling (Algorithm 3). At the core of RBSS is a recursive self-normalized importance sampling process to estimate the beliefs based on the observation weightings. At a belief node, RBSS expands all sampled actions and observations to obtain a full belief particle set in the next step. This does not have the same computational advantage of only updating those particles that are sampled for the next step simulation as done in rop-r a s 3, but allows us to leverage Theorem 1 to provide anytime estimation error bounds at all nodes.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

Further, by noticing that the reference policy in rop-r a s 3 is created from deterministic motion plans by sampling the source state from the belief and the target state from a heuristic, we assume that the reference policy ${\bar{{\pi}}}$ used in RBSS is also created from an underlying fully observable policy $\pi^{\text{fo}}:\mathcal{S}\rightarrow\Delta\mathcal{A}$ as a pushforward measure of $b(s)$, where $\delta$ denotes the Dirac measure. Such representation allows us to compute the weights of an action based on the particle representation of the belief.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Experiments", "weight": 1.0} -->

Since these scenarios are goal-reaching problems, the minimum planning horizon of the pomdp problem must be higher than the respective $H_{\textup{min}}$. Discrete(x) indicates the action space consists of x discrete actions. None corresponds to no observation due to partial observability. Discretized motion path refers to snapping primitive actions to a motion path.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluated rop-r a s 3 on seven different long-horizon simulated pomdp problems, systematically analyzing the effects of its respective components on its performance. The simulated testing scenarios include 2D navigation, 3D navigation, multi-robot tag, and manipulation problems. We also demonstrate rop-r a s 3 's practicality by deploying it to a Hello-Robot Stretch 3 mobile manipulator. Finally, an ablation study is carried out to understand rop-r a s 3 's performance as the reference policy gradually deteriorates to a purely uniform policy. Empirically, we show that the success of rop-r a s 3 is a combination of the new tree search method and reference policies induced from vamp.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Simulation Scenarios and Benchmark Methods", "weight": 1.0} -->

The scenarios are described next, while a summary of the corresponding pomdp models is provided in Table 1. More detailed pomdp definitions of each scenario are described in Appendices A.2.1, Table 6 and Table 7.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Simulation Scenarios and Benchmark Methods", "weight": 1.0} -->

Light Dark (Figure 1(a)).: A variation of the classical Light Dark problem. The agent needs to navigate to a goal region with an initially unknown location. It can only localize in the light stripe.: This is a long-horizon problem, modified from the discrete 2D Navigation scenario in KDHL2011. A 2-d o f mobile robot must navigate from one of the two potential initial positions to a goal region without entering a danger zone and dodge obstacles. The robot receives position readings with small Gaussian noise inside the landmarks and no observations otherwise. This limited localization capability results in a minimum of 100 primitive actions to reach the goal, as the robot must take detours to localize and avoid danger zones.: A 3D navigation problem with randomly placed obstacles, landmarks, danger zones and goals. The goals are initialized to be far away from the initial position of the drone. We systematically evaluate rop-r a s 3 on environments with progressively increasing obstacle density. The chance that the sbmp fails to find a path due to narrow passages within a given time limit increases with the obstacle density and a pomdp planner needs to consider more diverse macro-actions to find a good motion strategy.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Simulation Scenarios and Benchmark Methods", "weight": 1.0} -->

Multi-Drone with A Teleporting Target (Figure 1(d)).: In a 3D open area, four drones need to work together to capture a moving target (in green) whose initial position is not known to the drones. Moreover, the target can teleport to the opposite side of the map once it collides with the map boundaries but drones cannot. The target is equipped with the strategy of moving away from the closest drone. This strategy is known to the drones. The drone can only detect the target if they are within a small detection range. And the target is captured as long as one drone is within the capture radius (smaller than detection range).

<!-- chunk {"id": "body-0059", "role": "body", "section": "Simulation Scenarios and Benchmark Methods", "weight": 1.0} -->

Sphere-Search (Figure 2(a)). ‣ 5.1 Simulation Scenarios and Benchmark Methods ‣ 5 Experiments ‣ Think Fast and Far: Long-Horizon Online POMDP Planning via Rapid State Sampling")):. A 7-DOF manipulator needs to move from its initial configuration to an initially unknown goal location. The robot needs to take a detour to reach a light using its end-effector and observe the exact goal location.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Simulation Scenarios and Benchmark Methods", "weight": 1.0} -->

Ray-Detect (Figure 2(b)). ‣ 5.1 Simulation Scenarios and Benchmark Methods ‣ 5 Experiments ‣ Think Fast and Far: Long-Horizon Online POMDP Planning via Rapid State Sampling")):. A 7-DOF manipulator is tasked to use a fixed line of sight detector mounted at its end effector to scan environments, receives noisy readings of the obstacle positions and find a robust way to reach the target cylinder at the center of the table.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Simulation Scenarios and Benchmark Methods", "weight": 1.0} -->

Shelf-Move (Figure 2(c)). ‣ 5.1 Simulation Scenarios and Benchmark Methods ‣ 5 Experiments ‣ Think Fast and Far: Long-Horizon Online POMDP Planning via Rapid State Sampling")):. This is the hardest problem that incorporates the difficulties of the other scenarios. A 7-DOF manipulator can move its end-effector close to obstacles to sense their positions. It is tasked to retrieve a target can, placed at the back of the shelf where the front is packed with obstacles, and put the target can at the intended location on the top shelf. The robot can remove the blocking obstacles, but needs to be careful not to place the obstacles at the location reserved for the target.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Simulation Scenarios and Benchmark Methods", "weight": 1.0} -->

The following baselines are used for comparisons,:. The planner maintains the belief of the current state of the agent, but only takes actions returned by vamp's macro-action sampler *without* pomdp planning. It resembles the reference policy used by rop-r a s 3.:. A reference-based pomdp planner with a uniform sampling reference policy but no vamp.:. A standard benchmark for online pomdp planning.:. An instantiation of Algorithm 1 using pomcp with macro-actions generated by the same reference policy as rop-r a s 3, but a finite set of macro-actions is sampled for each belief node over which pomcp optimizes. The sample size at each node is set to be roughly equal to that of rop-r a s 3 after progressive widening for fair comparisons.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Simulation Scenarios and Benchmark Methods", "weight": 1.0} -->

MAGIC (lee.rss):. A variation of despot (despot17) that uses learnable macro-actions generated via an actor-critic approach.:. despot with macro-action learning boosted by recurrent neural networks.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Sampling Heuristics", "weight": 1.0} -->

We detail the sampling heuristics (see SampleMacroActionSBMP in Algorithm 2) used to create the reference policies for each problem. Biased sampling of informative states is not in itself a new idea, e.g., KDHL2011; flaspohler; however, using such an idea to construct reference policies is fundamental to the success of rop-r a s 3. Although it is generally impossible to encode (near) optimal solutions as the reference policy, it is much easier to create a reference policy that has compact support over actions that cover the optimal reachable belief space, which in turn makes pomdps efficient to solve easypomdp. In our case, such a policy can be obtained by constructing deterministic motion plans to informative states in the world. Informative states refer to states with observations (e.g., landmarks) and rewards (e.g., goals). When these states are not known exactly by the agent, they are modeled as part of the state variable so we can sample these states from the belief particles.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Sampling Heuristics", "weight": 1.0} -->

We create two types of sampling heuristics for ablation purposes to understand the importance of the level of information revealed to the agent. The Uniform heuristic samples informative states in a uniform manner. It samples the goal state with probability 0.5 and samples the rest of informative states uniformly. The Dynamic heuristic varies its sampling strategy according to the belief such that when it is well informed, it is steered towards reaching the goal and when it is less informed, it inclines to gather information. Specifically, it samples the goal with probability $1-\mathcal{H}(b_{t})$, where $\mathcal{H}(b_{t})$ is the normalized entropy of the current belief $b_{t}$. With probability $\mathcal{H}(b_{t})$, it samples the rest of the informative states with probability inversely proportional to the distance of the agent to those states.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Sampling Heuristics", "weight": 1.0} -->

An exception is the Multi-Drone problem due to its multi-agent and limited information nature. Since information is only revealed when the drones detect the target, previous heuristics would not be enough to cover the optimal solution as the target can teleport elsewhere but drones cannot. Instead, we create a sampling heuristic that commands the nearest drone to move towards a possible target location sampled from the belief and the rest of the drones spread out uniformly. To further understand how well our method performs, we also conduct ablation studies that gradually remove the information carried by the sampling heuristics in Section 5.6.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

For evaluation, all variants of rop-r a s 3 are implemented in Python following zheng2020pomdp_py. vamp is implemented in C++ and is used via a Python api. We avoid implementing benchmark methods from scratch for a fairer comparison; the pomcp implementation is from zheng2020pomdp_py and the implementations of pomcp, magic, rmag and Ref-Basic all use the code implemented by their respective authors (lee.rss; KL2023). PyBullet coumans2021 is used as a visualizer only. For the first four navigation problems, all methods are provided with the same planning time of 1s in all scenarios with the exception of Light Dark where the planning time is 0.1s. For manipulation problems, we fix the number of simulations per planning iteration and report the average planning time, as these problems have more computational overhead compared to navigation problems. The temperature parameter $\eta$ for rop-r a s 3 and Ref-Basic is $\eta=0.2$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

The action progressive widening parameter is set to $\beta_{a}=6$ and $\alpha_{a}=0.05$. magic and rmag are trained on a 4070 GPU with data collected in 500,000 runs ($\sim$`<!-- -->`{=html}3 hours of training). The parameters have been tuned to optimize performance for each problem. Other implementation details can be found in Appendix A.2.2.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Results and Discussions", "weight": 1.0} -->

#3: 300 obstacles, 10 danger zones. #4: 400 obstacles, 5 danger zones. R.P stands for reference policy.)

<!-- chunk {"id": "body-0070", "role": "body", "section": "Results and Discussions", "weight": 1.0} -->

Ray-Detect (Planning Horizon: 500) Shelf-Move (Planning Horizon: 1500) Table 5: Results on Ray-Detect and Shelf-Move (Red indicates the best result and blue indicates the second best.)

<!-- chunk {"id": "body-0071", "role": "body", "section": "Results and Discussions", "weight": 1.0} -->

We ran all methods 30$\times$ for each scenario and method, and the results are summarized in Tables 2, 3, 4 and 5. Regardless of success or failure, the \"Sims. #\" and \"Planning Times\" columns present the average number of episodes simulated or the time spent in seconds in one planning call, whereas the steps column records the average execution steps for each run. Reward columns indicate the average total reward, and the standard errors are put in brackets. In Table 3, \"R.P. Fail %\" column indicates the percentage of reference policy failures across 30 runs. Variants of magic and rmag were run only on Light Dark and Maze2D because they do not naturally extend to high-dimensional motion planning problems (e.g. manipulation and multi-agent tasks). pomcp and Ref-Basic failed on all runs of Random3D and Multi Drones Tag and are therefore excluded from the corresponding tables. Subsequently, we do not expect that these two methods will perform well on manipulation tasks with even longer horizons and higher state dimensions, and hence they are excluded from those experiments.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Results and Discussions", "weight": 1.0} -->

Refer to Figure 6 to Figure 10 in the Appendix for examples of critical time stamps of rop-r a s 3 in performing each tasks.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Results and Discussions", "weight": 1.0} -->

The results indicate that all variants of rop-r a s 3 substantially outperform all baseline methods in all evaluation scenarios. The improvement provided by rop-r a s 3 is the smallest for Light Dark and Sphere Search (the simplest evaluation scenarios for navigation and manipulations respectively) where all variants of rop-r a s 3 achieved a success rate of up to 28% higher than R-pomcp, magic, and rmag. The reason is that both of these scenarios require a much lower planning horizon and have less uncertainties compared to other scenarios. In Light Dark, this simplicity is indicated by the good performance of methods that do not use macro-actions, such as pomcp and Ref-Basic, and by the good performance of B-vamp, which reasons with respect to only a sampled state of the belief.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Results and Discussions", "weight": 1.0} -->

In Sphere Search, the bimodal uncertainties associated with the goal cause troubles to B-vamp, however, since the partial observability is fully resolved by reaching the light once and the light is not placed too far away from the manipulator, this problem has a relatively short effective horizon compared to other problems and therefore both R-pomcp and rop-r a s 3 perform well with rop-r a s 3 outperforming R-pomcp by 30%.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Results and Discussions", "weight": 1.0} -->

In the other scenarios, all variants of rop-r a s 3 improved the success rate of the benchmark methods by many folds. When the scenario requires a much longer planning horizon (e.g., Maze2D, Shelf-Move) or has higher uncertainty and more complex geometric structures (e.g. Ray-Detect and Shelf-Move), the benefit of rop-r a s 3 increases. By using vamp, rop-r a s 3 can quickly generate much more diverse macro-actions that capture the geometric features of the problem well. Simultaneously, the reference-based pomdp objective enables rop-r a s 3 to utilize the sampled macro-actions more efficiently than other benchmark methods. The result is that rop-r a s 3 can consistently find the most robust motion path (often requiring longer horizons but has overall greater accumulated rewards) to interact with the environment and reach the goal. Unlike rop-r a s 3, R-pomcp expands all reference policy actions at once when encountering a new belief node in the tree, which means the actions being expanded cannot be adaptive as new belief particles were introduced to the node during planning.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Results and Discussions", "weight": 1.0} -->

By growing the tree in a depth-first-search manner, rop-r a s 3 expands a new action edge at a belief node every time a new particle is added; this way, it benefits the most from the underlying reference policy. As theoretically shown, rop-r a s 3 removes the cumbersome optimization procedures in traditional methods with Monte-Carlo estimations, significantly reducing the number of samples of simulations required to achieve a high success rate in all benchmarks. For the most sophisticated benchmark---Shelf-Move, rop-r a s 3 only requires 100 simulations with under 10s planning time to achieve high success rate (see Table 5). Learning-based methods perform poorly in Maze2D due to the difficulty in learning suitable macro-actions with fixed length. In contrast, by using sbmp, rop-r a s 3 is able to better capture the fine motions the robot needs to navigate the geometric features of the environment.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Results and Discussions", "weight": 1.0} -->

For the high-dimensional navigation planning problem---Multi-Drones Tag, rop-r a s 3 performs at least 4 times better than the rest of the methods as it is the only method that exhibits strategies where drones actively discover and spread out to surround the tag. Both B-vamp and pomcp cannot easily adapt to the uncertainties from deterministic planning. B-vamp does not incorporate any uncertainty in the effects of actions and pomcp fixes a set of macro-actions from the reference policy for each belief node based only on a *single* sampled particle. Hence, the expanded set could be insufficient to fully represent the support of the belief, which is a problem that can be further compounded if the reference policy keeps failing.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Results and Discussions", "weight": 1.0} -->

In Ray-Detect (Table 5), rop-r a s 3 is the only method that consistently realizes that the most robust way to reach the cylinder is to use the ray to observe obstacles on the path and swing around the obstacles to avoid getting trapped by cluttered obstacles. Although the belief tree from R-pomcp can reach the same depth as rop-r a s 3, the UCB action selection strategy used by R-pomcp ignores the benefits brought by the sampling heuristics and converges more slowly to find the optimal action. Interestingly, we found out that R-pomcp benefits more from a uniform sampling strategy than a more complex dynamic sampling strategy, as expanding all actions at once requires the underlying sampling strategy to have built-in action diversity, whereas rop-r a s 3 expands action as new particles are introduced to a node, tremendously benefiting from the dynamic sampling strategy.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Results and Discussions", "weight": 1.0} -->

Shelf-Move is the most sophisticated problem that combines the difficulties of previous problems. Besides requiring very long horizon ($H=3000$) to deliberately put obstacle cylinders away at carefully planned locations so that the target cylinder can be retrieved and placed at the target location, the scenario itself consists of a non-trivial amount of uncertainties and the clutter of the environment implies occasional failures of finding a deterministic path. Unlike previous problems with a single winning strategy, this problem has many different choices for grasping and placing the cylinders. rop-r a s 3 equipped with the dynamic sampling heuristic is the only one that demonstrates smart grasping and placing of these objects (see the 3rd row of Figure 10). It often identifies that removing two obstacles away at non-target locations will clear a sufficiently large path to retrieve the target cylinder at the back, and place it at the intended location. In case of mistakenly placing an obstacle at the target location, rop-r a s 3 can often find a way to arrange the obstacles correctly for the placement of the target cylinder. Other methods do not exhibit this kind of long horizon thinking and their successful runs were often lucky runs.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Physical Robot Demonstrations", "weight": 1.0} -->

We deploy rop-r a s 3 on a Hello-Robot Stretch 3 in an uncertain and dynamic environment. In a lab environment, a pedestrian whose position is not exactly known to Stretch moves across the lab with a roughly constant speed. Stretch is tasked to navigate to a goal placed on the other side of the pedestrian. The pedestrian's speed is set such that if going straight, Stretch would most likely run into the pedestrian. The state space has 16 dimensions, of which 13 comes from Stretch, and the remaining 3 are the pedestrian's location as we model the pedestrian as a sphere. We discretize the action space into 45 primitive open loop twist controls that correspond to straight-line and curved motions of the mobile base. The mobile base of Stretch is controlled by twist controllers. We use a simple Euler integrator as the transition function and add noises to it to compensate for the errors between the realized Stretch motion and integrated solution. Stretch can query its IMU sensors to provide actual observations for belief updates. Such an update serves as a filtering step to better localize Stretch and reduce odometry uncertainties.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Physical Robot Demonstrations", "weight": 1.0} -->

The problem horizon is set to 75, with the planning horizon set to 25. A reward of 800 is provided to the agent for reaching the goal. A -800 penalty is provided for colliding with the pedestrian. A -20 penalty is given for being too close (within 0.3m) to the pedestrian. Otherwise, a -1 penalty is given for each primitive step taken. We compare rop-r a s 3 with B-vamp and R-pomcp in a few trials. As shown in Figure 3 and Figure 11, rop-r a s 3 is the only method that demonstrates a consistent smart and robust strategy of taking an efficient detour to go behind the moving pedestrian without colliding with other parts of the environment. B-vamp in Figure 11 steers straight and bumps the pedestrian as it does not incorporate pomdp planning, whereas R-pomcp took a long detour and ran into the tables. See Appendix A.2.3 for more details on the Stretch implementations.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Explorative Reference Policy", "weight": 1.0} -->

One might be concerned that limiting state sampling to only hand-picked information states in the reference policy (see Section 5.2) is too restrictive. Therefore, we also evaluate rop-r a s 3 when these states are sampled in an $\epsilon$-greedy fashion, where with probability $\epsilon$, the sampling heuristic samples from the entire state space, and it samples those information states with $(1-\epsilon)$ probability. When $\epsilon$ is 0, it corresponds to the unmodified sampling strategy, and when $\epsilon$ is 1, the hand-crafted sampling strategy is purely replaced with uniform random sampling of the state space.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Explorative Reference Policy", "weight": 1.0} -->

For this ablation study, we test the above sampling strategy on the Maze2D and Multi-Drone Tag scenarios. We also increase the planning time per step from 1s to 3s to allow proper belief space coverage due to the increase of sampling possibilities. For a fair comparison, we also ran the strong baseline, R-pomcp, on the two scenarios for 3s planning time per step.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Explorative Reference Policy", "weight": 1.0} -->

The results are displayed in Figure 4. As expected, when the reference policy gradually approaches uniform, rop-r a s 3 's performance decreases. The reference policy becomes farther away from the deterministic optimal policy with respect to the KL-divergence, as a result the found policy can only perturb the reference policy so much to collect more rewards. However, the performance drop is not linear with respect to $\epsilon$. For instance, in Maze2D, significant amount of drop is seen when $\epsilon$ is increased from 0.6 to 1.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Explorative Reference Policy", "weight": 1.0} -->

Despite the decreasing performance of rop-r a s 3, it generally still performs better than the strong baseline R-pomcp (without any $\epsilon-$explorations when sampling actions). In Maze2D, rop-r a s 3 with pure explorative reference policy (ie., $\epsilon=1$) still outperforms R-pomcp, with 13% success rate when the policy is generated using rop-r a s 3 and 0% success rate when using R-pomcp. In Multi-Drone scenario, with $\epsilon<=0.8$, rop-r a s 3 outperforms R-pomcp scenario, indicating the importance of our novel tree search and backup steps.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Explorative Reference Policy", "weight": 1.0} -->

Finally, this ablation study indicates rop-r a s 3 is less sensitive to the sampling heuristics in Multi-Drone Tag, as its worst success rate is retained at 40%. This is due to the fact that Maze2D is more geometrically complex than Multi-Drone Tag, that is, the chance of sampling the right states to form a robust path is much less in Maze2D than that in Multi-Drone Tag (there are many different ways to surround and capture the target).

<!-- chunk {"id": "body-0087", "role": "body", "section": "Effect of Tree Search Depth", "weight": 1.0} -->

Hyperparameters such as the tree search depth are important to the performance of rop-r a s 3. Under tight computational budgets (e.g., one second of planning), the right tree search depth needs to balance collecting long horizon information and Monte Carlo estimation accuracies. This ablation study perturbs the tree search depth across two experiments for rop-r a s 3 with the Uniform sampling heuristic. Results are shown in Figure 5. We see that performance drops as the tree depth increases or decreases; a good rule-of-thumb we found is to set the tree depth to be roughly the number of steps needed to solve the problem under deterministic settings.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Summary", "weight": 1.0} -->

This paper presents a continuous reference-based pomdp framework to handle large scale robotic problems. The objective of the Reference-based pomdp can be partially solved analytically, resulting in a backup equation that can be estimated with sampling without online numerical optimizations. We then present a new online approximate Reference-based pomdp solver, Reference-Based Online pomdp Planning via Rapid State Space Sampling (rop-r a s 3 ), which uses vamp to sample the state space and rapidly generate a large number of macro-actions online. These macro-actions reduce the effective planning horizon required and are adaptive to geometric features of the robot's free space. Since Reference-based pomdp planners use macro-actions only to bias belief-space sampling and do not require exhaustive enumeration of macro-actions, rop-r a s 3 can efficiently exploit many diverse macro-actions to compute good pomdp policies fast. It is shown that the number of belief particles and actions sampled controls the convergence of rop-r a s 3 s online planning. Evaluations on various long horizon pomdps indicate that rop-r a s 3 outperforms state-of-the-art methods by multiple factors.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Summary", "weight": 1.0} -->

Avenues of future works abounds. Hinted in the ablation study, a poorly selected reference policy could lead to inferior performance, and one may ask what are the characteristics of a reference policy that can guarantee a certain level of performance. Overall, the substantial increase in the capability of online approximate pomdp solvers in long horizon problems brought by rop-r a s 3 enables improved robustness in wide ranges of robotics applications.
