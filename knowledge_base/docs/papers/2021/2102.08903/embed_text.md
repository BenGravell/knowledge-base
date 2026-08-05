<!-- arxiv-full-text:v1 {"arxiv_id": "2102.08903", "source": "arxiv-pdf"} -->

## Introduction

Two-player zero-sum Markov game is a popular setting with many applications, such as Go, StarCraft II, and poker. In this setting, the goal of player one is to find a policy that achieves the maximum reward against player two who plays optimally to minimize the reward in response to player one's policy.

Policy optimization methods are widely used for solving zero-sum games. These algorithms often constrain the policy in a parametric form, and compute the gradient of the cumulative reward with respect to the parameters using the policy gradient theorem or its variants to update the parameters iteratively (Sutton et al., 2000; Kakade, 2002; Silver et al., Jason D. Lee Princeton University Simon S. Du University of Washington Meta AI Research Proceedings of the 25 th International Conference on Artificial Intelligence and Statistics (AISTATS) 2022, Valencia, Spain. PMLR: Volume 151. Copyright 2022 by the author(s). 2014). Due to its flexibility, a wide range of successful results are attained by policy optimization methods. For example, Lockhart et al. performed direct policy optimization against worst-case opponents and empirically demonstrate their effectiveness in Kuhn Poker and Goofspiel card game. Foerster et al. invented LOLA where each agent shapes the learning of other agents. It gave the highest average returns on the iterated prisoners' dilemma (IPD).

Despite the large body of empirical work using policy optimization methods for two-player zero-sum Markov games, theoretical studies are very limited. In this paper, we aim to answer the following fundamental question: Can we design a provably efficient policy optimization algorithm with function approximation for two-player zero-sum Markov games with a large state-action space?

We answer the above question affirmatively. We summarize our contributions below.

Our contributions. We design a new, provably efficient policy optimization algorithm for two-player zero-sum Markov games based on the natural policy gradient (NPG) method. On a high level, our algorithm has the two-step style as in previous work on value-based algorithms for two-player zero-sum Markov games. In the Greedy step, we aim to find a pair of policies that approximately solves matrix games for a given value function, and in the Iteration step, we aim to update the value function upon the current policy. In contrast to their value-based algorithm where function approximation is used for value functions, our results are entirely policy-based. We only have function approximation for policies. Therefore, we need to tackle additional challenges which are absent in value-based algorithms. 1. First, in the Greedy step, the algorithms in requires solving twoplayer zero-sum matrix games for every state in a value-based manner. The computational complexity scales with the size of the state-action space, which can be infeasible. For finding the equilibria for state-wise matrix games, we employ policy-based methods whose sample complexity only scales with the complexity of the function class (e.g., feature dimension for linear function approximation) instead of the size of stateaction space. Specifically, we design a subroutine that combines two-player policy gradients with the optimistic mirror descent (OMD) updates to solve the zero-sum matrix game in a computational and statistical efficient way. 2. Second, in the Iteration step, Perolat et al. used Generalized Policy Iteration to evaluate the value function while we only have function approximation for policies. We leverage recent developments on NPG in single-agent RL to update policies in this step and represent the value function using policies instead of explicitly storing the value function. 3. Third, technically, we incorporates policy-based methods into value-based schemes, and develop new perturbation analyses for policy-based methods, both of which may be of independent interest.

Theoretically, first, to illustrate the main idea of our algorithm, in Section 4, we study an idealized 'population" tabular Markov game setting where we can access the population quantities, including the true policy gradients and the Fisher information. We prove an ˜ O ( 1 T ) rate, 1 where T is the number of iterations. This result is interesting in its own right because this matches the rate in the single-agent RL setting. We further obtain an improved rate in the entropy-regularized setting.

We present our main algorithm and theoretical results in Section 5 where we study Markov games with a large state-action space, and log-linear policy parameterization is used for generalization. Instead of the idealized 'population" setting, we study the realistic online setting, where we can only access the model through interactions. We prove an ˜ O ( 1 √ T + 1 N 1 / 4 ) rate where T is the number of iterations and N is the number of samples (interaction with the model). To our knowledge, this is the first quantitative analysis of online policy optimization methods with function approximation for two-player zero-sum Markov games.

1 ˜ O ( · ) hides logarithmic factors.

## Related Work

A large number of empirical works have proven the validity and efficiency of PG/NPG based methods in games and other applications. Below we mostly focus on relevant algorithmic and theoretical papers.

There is a long line of work developing computationally efficient algorithms for multi-agent RL in Markov games. Value-based approaches try to find the optimal value function. When the size of the state-action space is large, Approximate Dynamic Programming (ADP) techniques are often incorporated into value-based methods. Extending the error propagation scheme of ADP developed by Scherrer et al. to two-player zero-sum games, Perolat et al. obtained a performance bound in general norms. Using this error propagation scheme on ADP, Pérolat et al. adapted three value-based algorithms (PSDP, NSVI, NSPI) to the two-player zero-sum setting. Recently, Yu et al. replaced the policy evaluation step of Approximate Modified Policy Iteration (AMPI) introduced by Scherrer et al. with function approximation in a Reproducing Kernel Hilbert Space (RKHS) and proved linear convergence to l ∞ -norm up to a statistical error. While focusing on policy-based methods, our paper also leverages the error propagation analysis.

Another type of algorithms on two-player zero-sum Markov games is policy-based. One family of algorithms is based on fictitious play. Fictitious play is a classical strategy proposed by Brown, where each player adopts a policy that best responds to the average policy of other agents inferred from historical data. For example, Heinrich et al. introduced two variants of fictitious play: 1) an algorithm for extensive-form games which is realization-equivalent to its normalform counterpart, 2) Fictitious Self-Play (FSP) which is a framework computing the best response via fitted Q -iteration. Our paper also aims to find the best response iteratively. Another family of policybased methods is based on the idea of counterfactual regret minimization (CFR). Brown and Sandholm invented a novel CFR variant which utilizes techniques such as reweighting iterations and leveraging optimistic regret matching. Although these two families of algorithms are similar to ours in spirit, they are quite different technically and their theoretical analysis does not apply to our setting.

The current paper focuses on using NPG techniques for solving two-player zero-sum Markov games. NPG is first introduced by Kakade to better explore the underlying structure of the reinforcement learning (RL) problem instance. Extensions of NPG methods are also used to solve zero-sum games. Zhang et al.; Bu et al. applied projected natural nested gradient under a linear quadratic setting, a significant class of zero-sum Markov games. Extensions to imitation learning were also studied .

In terms of theoretical analysis on PG/NPG methods, Agarwal et al. showed that tabular NPG could provide an O ( 1 / T ) iteration complexity, as well as a sample complexity of O ( 1 / N 1 4 ) for online NPG with function approximation. In contrast, we provide bounds for the two-player zero-sum case, which is significantly more challenging. In two-player zero-sum games, the non-stationary environment faced by each individual agent invalidates the stationary structure of the single-agent setting, and thus precludes the direct application of the convergence proof from the singleagent setting. Furthermore, each agent in two-player zero-sum games must adapt to the other agent's policy, which poses additional difficulties. Zhang et al. proposed a new variant of PG methods that yielded unbiased estimates of policy gradients, which enabled non-convex optimization tools to be applied in establishing global convergence. Despite being nonconvex, Agarwal et al.; Bhandari and Russo identified structural properties of finite Markov decision processes (MDPs): the objective function has no suboptimal local minimum. They further gave conditions under which any local minimum is nearoptimal.

Schulman et al. developed a practical algorithm called TRPO which could be seen as a KL divergenceconstrained variant of NPG. They show monotonic improvements of the expected return during optimization. Shani et al. considered a sample-based TRPO and proved an ˜ O ( 1 / √ N ) convergence rate to the global optimum, which could be improved to ˜ O ( 1 / N ) when regularized. Cen et al. showed that fast convergence rate of NPG methods can be obtained with entropy regularization. Applying NPG to linear quadratic games, Zhang et al. and Bu et al. proved that: for finding Nash equilibrium, NPG enjoys sublinear convergence rate. Both analyses rely on the linearity of the dynamics which does not hold in general Markov games considered in this paper.

Recently, Daskalakis et al. showed independent policy gradient methods converge to a min-max equilibrium. Compared to our work, they focused on the tabular case and did not study the function approximation. They also assumed that the probability of stopping at any state is bounded below from a certain positive number, which is not a standard modelling approach and is hard to validate empirically. We instead use concentrability coefficients as a characterization of the game structure (cf. Definition 1). In general, these two conditions do not imply each other. Comparing with their work, ours is cheap in sample complexity. To find an ϵ -optimal solution, their sample complexity has an O ( ϵ -12. 5 ) scaling whereas ours has an O ( ϵ -6 ) scaling.

Our work is related to Optimistic Mirror Descent (OMD) and its behavior in zero-sum games, which have received more attention lately. Daskalakis et al. proposed the use of optimistic mirror decent for training Wasserstein GANs to address the limit cycling problem in experiments. They also proved convergence to a equilibrium in bilinear zero-sum games. Generalizing, Mertikopoulos et al. showed OMD converged in a class of nonmonotone problems satisfying coherence. Their work made concrete steps toward establishing convergence beyond convex-concave games.

## Preliminaries

In this section, we introduce the material background on two-player zero-sum Markov games and specify several quantities which will be used to analyze our algorithms for different settings.

## Two-Player zero-sum Markov Games

In this paper, we consider the centralized setting where we can control both players in the training phase to learn good policies. we focus on infinite-horizon discounted two-player zero-sum Markov games, which can be described by a tuple M = (S, A, P, r, γ): a set of states S, a set of actions A, a transition probability P: S × A × A → ∆(S), a reward function r: S ×A×A →, and a discount factor γ ∈ [0, 1). We let σ to be the initial state distribution and define policies as probability distributions over the action space: x, f ∈ S → ∆(A). 2 The value function V x,f: S → R is defined as: 2 For clarity we assume two players share the same set of actions, it is straight forward to generalize to the setting where two action sets are different. See Section 5. we use distribution σ as the optimization measure we use to train the policy and use distribution ρ as the performance measure of our interest. We remark that these two separate measures are widely used in analyzing approximate dynamic programming and policy gradient. We overload notations and define V x,f (ρ) as the expected value function of interest, i.e. V x,f (ρ):= E s ∼ ρ V x,f (s).

In a two-player zero-sum Markov game, player one (x) wants to maximize the value function and the other player (f) wants to minimize it. We define the Markov game's state-action value function Q x,f: S ×A×A → R, the advantage function A x,f: S × A × A → R, and the state visitation function d x,f s 0: S → as where s 0 ∈ S is an initial state, respectively. With the state visitation function at hand, we are prepared to introduce NPG for two-player zero-sum games which relies on the Fisher information matrix. Given player one's policy x, player two's policy f parameterized by θ, and starting state distribution σ, we define the Fisher information matrix F σ (θ) as: where we denote d x,f σ = E s 0 ∼ σ d x,f s 0 by the expectation form of the state visitation distribution.

One important concept in RL is the Bellman operator. For two-player zero-sum Markov games and two behavior policies x and f, we define P x,f ( s ′ | s ) = E a ∼ x ( ·| s ),b ∼ f ( ·| s ) P ( s ′ | s, a, b ) which performs as the transition kernel from s to any s ′ ∈ S and r x,f ( s ) = E a ∼ x ( ·| s ),b ∼ f ( ·| s ) r ( s, a, b ) which represents the reward each player can expect with policies ( x, f ). Bellman operators T x,f, T x, T act on any value function v: S → R and update it

- T x,f v:= r x,f + γ P x,f v, which generalizes the standard Bellman operator. - T x v:= inf f T x,f v, which is an asymmetric operator by letting f to be optimal. 3 - T v:= sup x T x v = sup x inf f T x,f v, which generalizes the standard Bellman optimality operator. It reflects notions of minimax equilibrium in essence.

3 Here we focus on max player x (see Eq. 3). If we replace x by f, we will have an analogous notation for min player.

Perolat et al. introduced these operators as generalized counterparts of single agent RL. We are able to adopt the dynamic programming scheme only once the Bellman operators are introduced.

Since we are considering a learning problem, we need to collect samples from the environment. We assume we can stop and restart at any time. With this, we can have the following sampling oracle.

Episodic Sampling Oracle For a fixed state-action distribution ν 0, we can start from s 0, a 0, b 0 ∼ ν 0, act according to any policy pair (x, f), and terminate when desired. We obtain unbiased estimates of the on policy state-action distribution which can be used for acquiring an unbiased Q x,f (s, a, b) where s, a, b ∼ ν x,f ν 0. See for a sampler.

This oracle essentially requires that we can terminate at any time and restart, therefore many real-world applications including games and physics simulation (e.g., OpenFOAM ) admit this oracle. This oracle is also used in the analysis (see Algorithm 1,3 and Assumption 6.3 therein).

The oracle is essential in analysis, technically because policy gradient methods need to estimate the values. This is the same reason as in the single-agent setting. Moreover, we believe this sampling oracle is not a strong assumption: it only requires that we can terminate at any time and restart. This is much weaker than the generative model assumption. The generative model assumes that one can query any state-action pair where we only require we can restart from a fixed initial distribution.

Shapley show that (x ∗, f ∗) is a pair of Nash equilibrium (NE) if the following inequalities hold for any state distribution ρ and policy pair (x, f): NE always exists for discounted two-player zero-sum Markov Games. In practice, we seek to find an approximate pair of NE instead of an exact solution. The goal of this paper is to output a policy x that makes the metric small where ρ is some state distribution of interest. This metric measures the performance of x against the worst-case f. If it is less than ϵ, we call x an one-sided ϵ -approximate NE, 4 it has been used.

## Function Approximation

This paper studies function approximation to generalize across a large state space in Section 5. To represent both behavior policies x and f, we adopt a log-linear parameterization: for a coefficient vector θ ∈ R d, the associated probability of choosing action a under state s, π θ ( a | s ), is given by exp ( θ ⊤ φ s,a ) ∑ a ′ ∈A exp( θ ⊤ φ s,a ′ ) where φ s,a is a feature vector representation of s and a. This parameterization has been used . We impose a regularity condition such that every ‖ φ s,a ‖ 2 ≤ D. Note that log-linear parameterization is D 2 -smooth in terms of θ. 5 This term is also known as Policy Smoothness when analyzing PG methods.

## Problem-Dependent Quantities

Our analysis relies on several problem-dependent quantities. We denote weighted L p -norm of function f on state space S as ‖ f ‖ p,ρ = (∑ s ∈S ρ ( s ) | f ( s ) | p ) 1 p.

The first problem-dependent quantity is used to measure the inherent dynamics of Markov games.

Definition 1 (Concentrability Coefficients). Given two distributions over states: ρ and σ. When σ is element-wise positive, define Here, x 1, f 1, · · · x j, f j are j pairs of policies. Intuitively, the first term quantifies the distribution shift after taking j pairs of steps starting from ρ. The second term describes the accumulative effect of discounted distribution shifts. Finally, the last term represents the additive performance of (k -l) accumulative distribution shift and thus it is often considered as stricter condition. See for a thorough comparison on these coefficients. Generally speaking, if σ is sufficiently diverse across states, then these quantities are bounded from above. pointed out that small concentrability coefficients reflect a restriction on the MDPs dynamics. Concentrability coefficients are widely used in analyzing the convergence of approximate dynamic programming algorithms and recently in analyzing PG methods. In particular, gave an example to show the dependency on concentrability coefficients is necessary. In these papers, their upper bounds all depend on the concentrability coefficients. For our two-player setting, we use the same definition of concentrability coefficients as.

4 From an optimization perspective, the sampling complexity of finding a solution so that both the min and max player are approximate NE scales only twice as large as that in one-sided case, since we may apply algorithms with the roles switched.

5 We follow standard smoothness definition. A function f is said to be β -smooth if for all x, x ′ ∈ R d: ‖∇ f ( x ) -∇ f ( x ′ ) ‖ 2 ≤ β ‖ x -x ′ ‖ 2.

The second quantity measures how well a parameterized class can approximate in terms of a metric.

Definition 2 (Approximation Error). Given a space W and a loss function L: W → R, we define ϵ approx = min w ∈W L ( w ) as the approximation error of W.

This concept is widely used for analyzing function approximation, state abstractions schemes and representation learning in RL. It explicitly describes the capacity of a parameter set.

## Warm-up: Population Algorithm for Tabular Case

We first introduce the population version algorithm for the tabular case with the exact Fisher information matrix and policy gradients. The algorithm is spiritually similar to fictitious play. We enforce x, f to be tabular softmax parameterized by ξ, θ ∈ R |S|×|A| Parameterization For vector θ ∈ R |S|×|A|, the probability associates to choosing action a under state s, π θ (a | s), equals exp (θ s,a) ∑ a ′ ∈A exp(θ s,a ′). One can verify that π θ is 1 -smooth in terms of θ.

This algorithm can be viewed as a prototypical algorithm and in the subsequent section, we will generalize to the online setting. The pseudo-code is listed in Algorithm 1.

In Algorithm 1, we perform K outer loops and obtain a near-optimal x and value function V K. We note that this algorithm is asymmetric since our metric (Eq. 3)

## Algorithm 1 Population Two-Player NPG

Input: V 0 = 0 a value function. Output: Approximate policy x K at Nash equilibrium

## Greedy Step

Run Algorithm 2 with A s defined in Eq. 4 and returns x k ( ·| s ) for every state s.

## Iteration Step

## Algorithm 2 Subroutine: OMD for tabular case

Input: f 0, g ′ 0, x 0, y ′ 0 ∈ Unif ( A ), β = 1 T ′ 2, and A s for s ∈ S.

## min player

Output: Approximate optimal ¯ x T ′ for max player for t = 1, 2, · · ·, T ′ do

## max player

## end for

is only considering max player x while taking the best response of min player f.

Each outer iteration begins with a Greedy Step. For current V k -1, we aim to find approximate equilibrium ( x, f ) with which T x,f V ≈ T V k -1. This step is spiritually equivalent to finding minimax equilibrium of a matrix game for every state s. In intuition, this step helps to update V k -1 towards V ∗ (cf. contraction Lemma).

Let us take a closer look at Greedy Step. Consider an approximate two-player zero-sum matrix game: for every state s ∈ S, we try to solve Here A s represents a set of matrices related to current value function V k -1. Instead of value-based approaches (PI, VI) which are often inefficient, we solve these matrix games by policy-based methods for efficiency and sub-optimality guarantee. We adopt the Optimistic Mirror Descent for two players by assuming access to population quantities, e.g., A s π in Eq. 4. Note that each A s (a, b) ∈ [0, 1 1 -γ] because V k -1 ∈ [0, 1 1 -γ).

For clarity, we follow notations . Denote φ ( f, x ) = x ⊤ A s f which is convex w.r.t. f when fixing x and concave w.r.t. x when fixing f, and the domains for x, f are X, F respectively. Thus T V k -1 ( s ):= sup x ∈X inf f ∈F φ ( f, x ). we denote { y t } and { g t } as secondary sequences of { x t } and { f t } respectively. We refer readers to Appendix B for how we set the adaptive stepsizes η t and η ′ t.

We perform simultaneous updates for T ′ iterations in Algorithm 2 to minimize the following terms, Suppose two infs are achieved at f ∗ and x ∗ respectively. With these two inequalities, we can derive an upper bound of Greedy Step: to guarantee x k is near-optimal with respect to V k -1.

After obtaining x k from Greedy Step, the Iteration Step aims to evaluate the value function while fixing x = x k. We run T updates to find f ∗ = arg min f V x,f. In the competitive multi-agent RL literature, this step is equivalent to finding the best response of min player (namely, f ∗ ) when fixing x = x k. The intuition is that when the max player's policy is very close to its optimal policy at NE and f takes f ∗, their accumulative value function is also close to V ∗ at NE. This step can be viewed as running NPG for a single-agent RL problem.

The following theorem gives the performance guarantee for Algorithm 1.

Theorem 1. For Algorithm 1, set η ≥ (1 -γ) 2 log |A|. After K outer loops we have V ∗ (ρ) -inf f V x K,f (ρ) upper bounded by We remind that σ is the optimization measure we use to train the policy and ρ is the performance measure of our interest.

Theorem 1 explicitly characterizes the performance of the output x K in terms of the number of iterations and the concentrability coefficients. Viewing concentrability coefficients to be constants (which is the case when σ is sufficiently diverse) and looking at the dependency on T and K, we find the dependency on T is a fast 1 /T rate, matching the same rate in the single agent NPG analysis. The dependency on K is exponential ( γ K ) which means we only need a few outer loops. The first term has an (1 -γ ) -4 dependency on the discount factor, which may not be tight and we leave it as a future work to improve. In Theorem 1 and 2, we set η to have a lower bound to simplify the convergence bounds. We can also derive η -dependent bounds. Note that the 'large step size" phenomenon is also consistent with the single-agent setting (see Theorem 5.3 in and discussion therein).

The proof of Theorem 1 further requires the following parts: mirror-descent type analysis of NPG used in and simultaneous mirror descent for matrix games proposed . The full proof is deferred to Appendix B.

## Extension: Entropy regularization

Following, we give an extension of entropy-regularized NPG in the Iteration Step for Algorithm 1. Denote τ as the regularization term, the entropy regularized value function is formulated as where H (σ, f) = 1 1 -γ E s ∼ d x,f σ E b ∼ f log 1 f (b | s) is the entropy term w.r.t. min player f. Note that V x,f τ (s) ∈ [-τ log |A|, 1], ∀ s ∈ S.

Entropy regularization requires us to minimize V τ instead of original value function V. Denote V ∗ τ (σ) = min f V x,f τ (σ) = V x,f ∗ τ (σ) -τ H (σ, f ∗ τ), the following sandwich bound holds Therefore, the regularized problem and the original problem are close when τ is small.

NPG methods with entropy regularization. Let η = 1 -γ τ, we have the NPG update rule The following theorem shows the performance improvement over Theorem 1.

Theorem 2. For entropy regularized Algorithm 1, after K outer loops, one-sided measure V ∗ (ρ) -inf f V x K,f (ρ) is bounded by Here, µ ∗ τ is the one-sided stationary distribution w.r.t. x which satisfies: µ ∗ τ = d x,f ∗ τ µ ∗ τ. This argument indicates that the state visitation distribution remains unchanged if the initial state is already in a steady state. See Appendix B.1 for the full proof.

Recently, Perolat et al. studied learning algorithms for extensive-form zero-sum games and they also used entropy regularization. Compared with their work, the differences include 1) we use policy optimization instead of value-based methods used in their paper. 2) our entropy regularization is a simple extension whereas the entropy regularization is crucial : the regularization term gives strong convergence guarantees in monotone games.

## Online Algorithm with Function Approximation

In this section, we extend Algorithm 1 to the realistic online setting with function approximation, in which the parameterization we adopt is defined in Section 3.2. In this setting, we only observe samples (instead of the population quantities in Section 4). The pseudo-code is listed in Algorithm 3.

To obtain estimates of quantities, we adopt the episodic sampling oracle (cf. Section 3) to provide transition tuples for estimating A s ( a, b ) in Greedy Step (cf. Eq. 4). This sampling oracle is also used in the Iteration Step to estimate value functions and gradients. See Appendix C for more details about how we use the sampling oracle.

In Section 2, we have pointed out that our algorithm has a smaller sample complexity of O ( ϵ -6 ) comparing to O ( ϵ -12. 5 ). As for the computational complexity, we remark that we only need projecting onto an L 2 -norm ball in Algorithm 3, 4, which has the same time complexity as computing the gradient (linear in the dimension of θ ), so our algorithms are computationally efficient.

Now we describe our algorithm. Specifically, we let ξ and θ be parameters of x and f, respectively. 6 The output and motivation of the Greedy Step and the Iteration Step are analogous to those in Algorithm 1. In both steps, we need to take sample-based NPG updates which are forced to be constrained in a convex set W = { w: ‖ w ‖ 2 ≤ W } for analysis. From now, we denote W as the bound of this norm-constrained convex set where each NPG update lies.

6 We assume that the two players share the same pa- Again, we first discuss the Greedy Step whose pseudo-code is listed in Algorithm 4. Our goal is still to obtain a near-optimal x k with respect to T V k -1. Algorithm 4 is similar to Algorithm 2 in spirit. The main difference is that we use a sample-based NPG update rule for both x and f. Ideally, we wish to find simultaneous updates w ∗ f and w ∗ x for the players. Both are minimizers of quadratic loss After obtaining x k from the Greedy Step, we adapt NPG updates (Eq. 7) in Algorithm 1 to the online setting.

Then the updates take the form θ t +1 = θ t -ηw ∗ f and ξ t +1 = ξ t + ηw ∗ x. Along the way, the sampling oracle is used to approximate w ∗ f, w ∗ x. After T ′ iterations, we are able to output an approximate solution ¯ x T ′ by averaging { x t } T ′ t =1.

Denote ν t = ν x,f t ν 0 for simplicity. Ideally, NPG update in the Iteration Step takes the form We perform sample-based quadratic loss minimization, which shares similarity with the former step: it takes N steps of projected gradient descent to return an approximate update.

Now we state our main theorem. rameter set only for clarity. We only need some minor modifications in the analysis to extend our results to the setting where two opposing players have different capabilities. Specifically, we only need to treat W (norm-bound of updates), D (regularity condition on features), and η separately for each agent.

## Algorithm 3 Online Two-Player NPG

Input: V 0 = 0 value function Output: Approximate policy x K at NE

## k · · · Greedy Step

Run Algorithm 4 returns x k with T ′ iterations.

## Iteration Step

Sample s, a, b ∼ ν t, then obtain ˆ Q ( s, a, b ) using the sampling oracle.

## end for

Randomly sample f from f t ( t = 0, 1 · · · T -1 ). Denote V k for V x,f.

## end for

where error terms ϵ, ϵ ′ are defined as Here ϵ approx and ϵ ′ approx are approximation errors coming from Greedy and Iteration Steps (cf. Definition 2). We remind that D is a regularity condition on features, with which we could show log-linear parameterization is D 2 -smooth (cf. Section 3.2). See Appendix C for specific expressions.

Similarly, the exponential γ K in Theorem 3 implies that we only need a few outer iterations. When considering concentrability coefficients as constants, the dependency on T is a slower T -1 / 2 rate while the sampling efficiency takes a N -1 / 4 rate. Both match the rates in the sampling-based single-agent NPG analysis. We note that iteration counts T, T ′ and sample counts N,N ′ have the same exponent. There is no explicit dependence on Algorithm 4 Online Greedy Step with FunctionApprox state-space S in the theorem, hence our online algorithm proves nice guarantees for function approximation even in the infinite-state setting. Instead, the bounds have parametric representation-related terms: D upper bounds feature norms ‖ φ s,a ‖ and W restricts each NPG update. The term ι bounds two policy probabilities from below and it must be greater than 0 since we adopt log-linear parameterization. In spirit, ι is similar to concentrability coefficients which reflect the inherent dynamics of Markov games.

In the worst case, the concentrability coefficient scales as large as the number of states, and the bounds for function approximation are only meaningful in the benign case where the concentrability coefficient is small. However, we note that that, the dependency on concentrability is unavoidable: A hard example for the single-agent setting was given . Since our Markov-Game (MG) setting is a generalization of the single-agent setting, their hard example also applies to our setting. Moreover, we argue that the coefficients can be small when there are some restrictions in the dynamics (see discussions in ). We also use the same definition as in the prior work value-based learning. The recent work also assumed this structure of MGs to analyze policy-based methods.

## Conclusion

This paper gave the first quantitative analysis of policy gradient methods for general two-player zero-sum Markov games with function approximation. We quantified the performance gap of the output policy in terms of the number of iterations, number of samples, concentrability coefficients, and approximation error. An interesting direction is to extend our results to more advanced PG methods such as PPO.
