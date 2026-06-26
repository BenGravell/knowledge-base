<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Optimality Guarantees for Particle Belief Approximation of POMDPs

Topics include Partial observability, Benchmarks, Online algorithms, Sampling-based methods, Control, Sampling, PB-MDP, Markov decision process.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Partially observable Markov decision processes (POMDPs) provide a flexible representation for real-world decision and control problems. However, POMDPs are notoriously difficult to solve, especially when the state and observation spaces are continuous or hybrid, which is often the case for physical systems. While recent online sampling-based POMDP algorithms that plan with observation likelihood weighting have shown practical effectiveness, a general theory characterizing the approximation error of the particle filtering techniques that these algorithms use has not previously been proposed. Our main contribution is bounding the error between any POMDP and its corresponding finite sample particle belief MDP (PB-MDP) approximation. This fundamental bridge between PB-MDPs and POMDPs allows us to adapt any sampling-based MDP algorithm to a POMDP by solving the corresponding particle belief MDP, thereby extending the convergence guarantees of the MDP algorithm to the POMDP. Practically, this is implemented by using the particle filter belief transition model as the generative model for the MDP solver.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

While this requires access to the observation density model from the POMDP, it only increases the transition sampling complexity of the MDP solver by a factor of O(C), where C is the number of particles. Thus, when combined with sparse sampling MDP algorithms, this approach can yield algorithms for POMDPs that have no direct theoretical dependence on the size of the state and observation spaces. In addition to our theoretical contribution, we perform five numerical experiments on benchmark POMDPs to demonstrate that a simple MDP algorithm adapted using PB-MDP approximation, Sparse-PFT, achieves performance competitive with other leading continuous observation POMDP solvers.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Maintaining safety and acting efficiently in the midst of uncertainty is an important aspect in a diverse set of challenges from transportation to autonomous scientific exploration, to healthcare and ecology. The partially observable Markov decision process (POMDP) is a flexible framework for sequential decision making in uncertain environments.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

One common method for solving POMDPs is online tree search, which is attractive for several reasons. First, the approach scales to very large problems because it uses sampled trajectories, making it insensitive to the dimensionality of the state and observation spaces. Second, since online computation focuses on the current states and states likely to be encountered in the future, it can reduce the need for offline computation and end-to-end training. Third, tree search is applicable to a wide range of problems, for example hybrid continuousdiscrete and problems with many local optima, because it only depends on a minimal set of problem structure requirements.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently proposed POMDP tree search algorithms have been shown empirically to work on continuous state and observation spaces. Theoretical analysis, however, has lagged behind. While there are algorithms that have performance guarantees and algorithms that perform well empirically, there has been little progress on a general theory describing why this family of algorithms can enjoys such good performance. Though there have been some algorithm-specific results (outlined in Section 2.4), a considerable gap in the connection between POMDPs and practical approximations using particle methods still remains.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This manuscript formally justifies that optimality guarantees in a finite sample particle belief MDP (PB-MDP) approximation of a POMDP/belief MDP yield optimality guarantees in the original POMDP as well. We accomplish this by showing that the Q -values of the POMDP and PBMDP are close with high probability by using an intermediary theoretical algorithm called Sparse Samplingω. Specifically, we prove that the Sparse Samplingω Q -value estimates are close to both optimal Q -values of the POMDP and PB-MDP with high probability. Since there exists an algorithm that approximates both Q -values accurately with high probability, the optimal Q -values of the POMDP and PB-MDP themselves must be close to each other with high probability. This probability scales as 1 -O ( C D exp ( -t · C )), where C is the number of particles; D is the planning depth; and t is a number determined by the POMDP reward function and probability distributions, number of particles, and desired accuracy.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notably, this convergence rate does not directly depend on the size of the state space nor the observation space, but rather depends on the R´ enyi divergence that links the probabilities concerning state and observation trajectories and the planning horizon D.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

This fundamental bridge between PB-MDPs and POMDPs allows us to adapt any samplingbased MDP algorithm of choice to a POMDP by solving the corresponding particle belief MDP approximation and to preserve the convergence guarantees in the POMDP. Practically, this means additionally assuming we have an explicit observation model Z and swapping out the state transition generative model with a particle filtering-based model. This change only increases the computational complexity of transition generation by a factor of O ( C ), with C the number of particles in a particle belief state. This allows us to devise algorithms such as Sparse Particle Filter Tree (Sparse-PFT), which enjoys algorithmic simplicity, theoretical guarantees, and practicality, since it is equivalent to upper confidence trees (UCT), with particle belief states.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this paper proceeds as follows: First, Section 2 reviews preliminary definitions and previous related work. Section 3 formalizes the notion of particle belief MDPs (PB-MDPs).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Approximate the POMDP as a Particle Belief MDP Solve the Particle Belief MDP to make a decision in the POMDP Figure 1: Illustration of the proof of our main theorem, Theorem 3: Since Sparse Samplingω algorithm Q -value estimator converges to both the optimal Q -values of POMDP and PBMDP, such an existence of algorithm implies that the optimal Q -values of POMDP and PB-MDP are also close to each other with high probability. This enables us to approximate the POMDP problem as a PB-MDP, and then solve the PB-MDP with an MDP algorithm to make a decision in the original POMDP while retaining the guarantees and computational efficiencies of the original MDP algorithm.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Then, Section 4 introduces Sparse Samplingω algorithm, and proves its coupled convergence towards the optimal Q -values of a POMDP and its corresponding PB-MDP in Theorem 2. Section 5 formally bridges the gap between POMDPs and PB-MDPs by leveraging the coupled convergence of Sparse Samplingω. In this section, we present two main theorems: Theorem 3 shows the optimal Q -value bounds between POMDP and PB-MDP, and Theorem 4 shows the near-optimality of planning with a PB-MDP to solve a POMDP by applying an online Q -value-estimating algorithm repeatedly in a closed loop with observations from the environment. We also introduce Sparse-PFT, a practical example of generating a PB-MDP approximation algorithm from an MDP algorithm. Finally, Section 6 empirically shows the performance of Sparse-PFT and other practical continuous observation POMDP algorithms over five different simulation experiments, and validates the improvements in performance of PB-MDP approximation with the increase in number of particles C while keeping other hyperparameters fixed.

<!-- chunk {"id": "body-0013", "role": "body", "section": "POMDPs", "weight": 1.0} -->

The partially observable Markov decision process (POMDP) is a mathematical formalism that can represent a wide range of sequential decision making problems. In a POMDP, an agent chooses actions based on observations to maximize the expectation of a cumulative reward signal. A POMDP is defined by the 7-tuple ( S, A, O, T, Z, R, γ ). In this tuple, S, A, and O are sets of all possible states, actions, and observations, respectively. These sets can be discrete, e.g. { 1, 2 }, continuous, e.g. R 2, or hybrid. The conditional probability distributions T and Z define state transitions and observation emissions, respectively. The transition probability distribution is conditioned on the current state s and action a and is denoted T ( s ′ | s, a ). The observation probability is conditioned on the previous action and current state 1 and denoted Z ( o | a, s ′ ). The reward function, R ( s, a ), maps states and actions to an expected reward, and γ ∈ [ 0, 1 ) is a discount factor. The agent plans starting from b 0, the initial state distribution or the initial belief.

<!-- chunk {"id": "body-0014", "role": "body", "section": "POMDPs", "weight": 1.0} -->

Some POMDP algorithms only require samples from the transition, observation, or reward models rather than explicit knowledge of T, Z, or R. Such samples can be produced using a so-called generative model denoted with s ′, o, r ← G ( s, a ). In some algorithms, only one or two of the outputs of G are used and the others are discarded, e.g. the notation ' o ← G ( s, a ) ' indicates that s ′ and r are discarded.

<!-- chunk {"id": "body-0015", "role": "body", "section": "POMDPs", "weight": 1.0} -->

The objective of a POMDP is to find an optimal policy, π ∗, that selects actions that maximizes the discounted sum of future rewards, with an appropriate tie-breaking method: In general, the actions may be chosen based on the entire history of actions and observations, However, because of the Markov property, it can be shown that optimal decisions can be made based only on the conditional distribution of the state given the history, known as the belief, This belief can be updated using Bayes's rule or an efficient approximation such as a Kalman filter or particle filter, and it is often more straightforward to determine actions based on beliefs rather than the history. Since the belief and history fulfill the Markov property, a POMDP is a Markov decision process (MDP) on the belief or history space, commonly referred to as the belief MDP.

<!-- chunk {"id": "body-0016", "role": "body", "section": "POMDPs", "weight": 1.0} -->

In order to maximize the objective in Eq., the policy must take into account both the immediate reward from taking the action in the current state and whether that action will lead to states favorable for attaining rewards in the future. For a history h and a corresponding belief b, the history-action and belief-action value functions, defined as take both of these factors into account. When π is also used for the current step, the expected accumulated reward from a history or belief is denoted with V π (h) = V π (b) = Q π (b, π (b)). When π is an optimal policy, these value functions are denoted with Q ∗ and V ∗. If Q ∗ can be calculated, an optimal policy π ∗ can simply be extracted with π ∗ (h) = argmax a Q ∗ (h, a). Thus, a common strategy for solving POMDPs involves iteratively improving estimates of Q ∗ denoted simply with Q for brevity.

<!-- chunk {"id": "body-0017", "role": "body", "section": "POMDPs", "weight": 1.0} -->

Early research sought to find optimal solutions to POMDPs offline; that is, they attempted to optimize actions for every possible belief before interacting with the environment. However, since POMDPs are generally intractable, it is often impossible to find a complete solution for a POMDP offline. Instead, we seek to compute solutions online only for the part of the problem that may be reached in the immediate future. 1. It is possible to use observation probability distributions additionally conditioned on the previous state, Z (o | s, a, s ′), in all algorithms discussed in this paper, but we use Z (o | a, s ′) for brevity.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Importance Sampling and Particle Filtering", "weight": 1.0} -->

In many real-world applications, updating the belief exactly based on a new action and observation is impractical. Fortunately, Monte Carlo methods provide simple and effective tools for approximate reasoning about distributions such as beliefs.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Importance Sampling and Particle Filtering", "weight": 1.0} -->

We often need to reason about a random variable X ∼P based only on samples from another related random variable, Y ∼ Q. Importance sampling allows us to, among other tasks, calculate the expectation of a function by observing that where { yi } N i = 1 are samples from distribution Q. The convergence property of this approximation relevant to the present work is described formally in Section 4.2.1.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Importance Sampling and Particle Filtering", "weight": 1.0} -->

The particle filter is an application of Monte Carlo estimation to the task of Bayesian belief updating. The simplest form is an unweighted particle filter, in which the belief is represented by a collection of N states, known as particles, ˜ b = { si } N i = 1. The density is approximated by ˜ b ( s ) ≈ ∑ N i = 1 δ ( si = s ), where δ ( · ) is a Dirac or Kronecker delta function depending on the form of the state space. At each step of the POMDP, after an action a is taken and an observation o is received, a new state s ′ i and observation oi is simulated once or more for each of the particles to create the new belief, ˜ b ′ = { s ′ i: oi = o }. In most cases, few particles will match o so it is difficult to maintain a large number of particles in the belief. Various domainspecific techniques can be used to reduce this problem, but it is difficult to solve completely in the unweighted particle filter.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Importance Sampling and Particle Filtering", "weight": 1.0} -->

The weighted particle filter is usually much more effective. The belief is represented by a collection of state particles and corresponding weights, ˜ b = { ( si, wi ) } N i = 1. The density is approximated with ˜ b ( s ) ≈ ∑ N i = 1 wi δ ( si = s ) ∑ N i = 1 wi. A belief update consists of simulating each particle once or more and then calculating the new weight according to the importance sampling correction: w ′ i = wi · Z ( o | s, a, s ′ i ). Typically, the weights of a few particles grow much larger than the others, so a resampling step creates many particles from those with large weights and eliminates those with very small weights.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Online POMDP Solvers", "weight": 1.0} -->

Monte Carlo tree search (MCTS) is a common solution technique for Games, MDPs, and POMDPs. In an MDP context, MCTS constructs a tree consisting of state and state-action nodes. In a POMDP context, each node corresponds to an actionor observation-terminated history node, estimating Q ( h, a ) at each action-terminated history node. The most common variant is called partially observable upper confidence trees (PO-UCT) or par- tially observable Monte Carlo planning (POMCP) 2 and constructs the tree by using Upper Confidence Bound (UCB), asymmetrically favoring regions of the history and action spaces that are likely to be visited when the optimal policy is executed.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Online POMDP Solvers", "weight": 1.0} -->

In addition to the PO-UCT algorithm described above, there are several other approaches to solve POMDPs through online planning. Early solvers attempted to use exact Bayesian belief updates on discrete state spaces, however, these are much less scalable than PO-UCT. Two other popular solvers with scalability similar to UCT are determinized sparse partially observable trees (DESPOT) and adaptive belief trees (ABT). DESPOT uses a small number of determinized scenarios instead of independent random simulations to reduce variance and relies on heuristic tree search guided by upper and lower bounds rather than Monte Carlo tree search. ABT is designed to efficiently adapt to changes in the environment without discarding previous computation.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Online POMDP Solvers", "weight": 1.0} -->

Since PO-UCT, DESPOT, and ABT all rely on unweighted particle belief representations, they will fail to find optimal policies in continuous observation spaces because the probability of generating the same observation twice, and hence creating beliefs with multiple particles, is zero. Partially observable Monte Carlo planning with observation widening (POMCPOW) approaches the continuous observation challenge by introducing a weighted particle filter and the continuous action challenge with progressive widening. DESPOTα incorporates a similar weighting scheme and uses the α -vector concept to generalize value estimates between sibling nodes. Adaptive online packing-guided search (AdaOPS) fuses similar observation branches in the search tree to improve performance. Lazy Belief Extraction for Continuous Observation POMDPs (LABECOP) builds the planning tree by re-weighting particles and extracting belief sequence values efficiently.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Theoretical Analysis of Particle-based POMDP Algorithms", "weight": 1.0} -->

Several previous studies have analyzed particle-based POMDP algorithms from a theoretical perspective. Silver and Veness claim that POMCP value estimates converge to the optimal value for discrete POMDPs on the basis that it equivalent to applying UCT to the history MDP corresponding to the POMDP. However, as mentioned above, POMCP does not converge in continuous observation POMDPs. Ye et al. analyzed the approximation of a POMDP with a finite set of scenarios, which essentially correspond to random seeds that are fixed across different possible action sequences, and bounded the performance of the DESPOT algorithm that uses these scenarios. However, these bounds depend on the size of the observation space, | O |, and thus cannot be applied to continuous observation spaces. This analysis was expanded by Luo et al. to cover a case in which scenarios are selected from an importance distribution.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Theoretical Analysis of Particle-based POMDP Algorithms", "weight": 1.0} -->

Bai et al. also provide convergence guarantees for their Monte Carlo value iteration (MCVI) algorithm which uses simulations in a manner somewhat akin to particle filtering. Their analysis extends to continuous observation spaces, but the algorithm is best suited for offline use, unlike the algorithms we focus. According to Bai et al., MCVI spends hours computing a policy graph that can be executed quickly online. 2. Strictly speaking, POMCP also includes a specialized unweighted particle filter update that re-uses simulations from the planning step, but the term is often used informally as a synonym for PO-UCT.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Theoretical Analysis of Particle-based POMDP Algorithms", "weight": 1.0} -->

Lim et al. presented the first theoretical analysis of online POMDP tree search algorithms that use weighted particle filtering. However, the partially observable weighted sparse sampling (POWSS) algorithm analyzed in that work is not efficient enough to be practically useful. Wu et al. provide analytical performance guarantees for a simplified version of AdaOPS, a recent particle belief tree search POMDP solver included in our numerical analysis in Section 6. However, the full AdaOPS algorithm used in the numerical experiments is more complex than the simplified version used in the theoretical portion of the work.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Theoretical Analysis of Particle-based POMDP Algorithms", "weight": 1.0} -->

Du et al. analyzed the number of particles needed to control partially observable linear systems. Finally, there is a large body of work on particle filters without consideration of decision making. Some results from this field are summarized by Crisan and Doucet.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Theoretical Analysis of Particle-based POMDP Algorithms", "weight": 1.0} -->

In contrast to these works that provide guarantees for individual algorithms or limited cases, the analysis in this paper provides a general bound for particle belief approximation of a broad class of POMDPs, giving justification for MDP algorithms to be adapted to solve POMDPs efficiently.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Particle Belief MDPs (PB-MDPs)", "weight": 1.0} -->

In this section, we define the corresponding particle belief MDP (PB-MDP) for a given POMDP. Deriving the corresponding particle belief MDP of a POMDP is equivalent to approximating the belief MDP with a finite number of particles.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Particle Belief MDPs (PB-MDPs)", "weight": 1.0} -->

- Σ: State space over particle beliefs ¯ bd. An element in this set, ¯ bd ∈ Σ, is a particle collection, ¯ bd = { (sd, i, wd, i) } C i = 1, where sd, i ∈ S, wd, i ∈ R +. 3 For the sake of brevity in the rest of the paper, we drop C i = 1 and render a particle belief as { sd, i, wd, i }. The beliefs are not assumed to be permutation invariant, meaning that particle beliefs with different particle orders are considered different elements in Σ. This simplifies derivation of the transition distribution (see Eq.) because each particle transition is independent. - A: Action space. Remains the same as the original action space.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Particle Belief MDPs (PB-MDPs)", "weight": 1.0} -->

- τ: Transition density τ (¯ bd + 1 | ¯ bd, a): We define the likelihood weights wd, i of particles sd, i to be updated through unnormalized Bayes rule: Then, the transition probability from ¯ bd to ¯ bd + 1 by taking the action a can be defined as: The first term in the integrand product P (¯ bd + 1 | ¯ bd, a, o) is the conditional transition density given some observation o. Since each new state particle is generated independently and the likelihood weight updates are deterministic given sd, i, sd + 1, i, a and o, this term can be written in terms of T and Z: 3. The d subscript, the number of steps, is included for subscript order consistency with the rest of the paper, but is not meaningful in this context.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Particle Belief MDPs (PB-MDPs)", "weight": 1.0} -->

The second term in the integrand product P (o | ¯ bd, a) is the observation likelihood given a particle belief and an action. This is equivalent to weighted sum of observation likelihoods conditioning on the observation having been generated from the respective i -th particle: Note that this density τ is usually impossible or very difficult to calculate explicitly. However, it is rather easy to sample from it using generative models.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Particle Belief MDPs (PB-MDPs)", "weight": 1.0} -->

Note that if R is bounded by R max, ρ is also bounded with || ρ || ∞ ≤ R max, since the normalized weights sum to 1.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Particle Belief MDPs (PB-MDPs)", "weight": 1.0} -->

- γ: Discount factor. Remains the same as the original discount factor.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Particle Belief MDPs (PB-MDPs)", "weight": 1.0} -->

The significance of defining a corresponding particle belief MDP is that we can directly adapt any sampling-based MDP algorithm to approximately solve a POMDP by only changing the transition generative model. The transition generative model will now be a sampler based on particle filtering, as the particle belief MDP deals with particle belief states. Furthermore, this allows Q -value convergence guarantees of the MDP algorithms to translate nicely into solving the POMDP, as we will prove later in this paper that the optimal Q -values of the POMDP Q ∗ P and PB-MDP Q ∗ MP are close with high probability.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Sparse Samplingω", "weight": 1.0} -->

In order to show that the optimal Q -values of the POMDP, Q ∗ P, and PB-MDP, Q ∗ MP, are approximately equivalent, we first introduce an algorithm called Sparse Samplingω (sparse sampling with weights), which will serve as a theoretical bridge between POMDP and PB-MDP. Sparse Samplingω is a sparse sampling solver that uses particle belief states with particle likelihood weighting to deal with observation uncertainty. As is evident from the name, Sparse Samplingω takes inspiration from sparse sampling for continuous state MDPs, using particle belief

<!-- chunk {"id": "body-0038", "role": "body", "section": "Algorithm 1 Sparse Samplingω", "weight": 1.0} -->

Output: New updated particle belief set ¯ b ′ { (s ′ i, w ′ i) }, mean reward ρ. particle belief set ¯ b = { (si, wi) }, depth d.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Algorithm 1 Sparse Samplingω", "weight": 1.0} -->

Input: particle belief set ¯ b = { ( si, wi ) }, action a, depth d.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Algorithm 1 Sparse Samplingω", "weight": 1.0} -->

Output: A scalar ˆ Q ∗ d (¯ b, a) that is an estimate of Q ∗ d (b, a). states. Note that Sparse Samplingω is purely a theoretical intermediary tool to bridge POMDPs and PB-MDPs, and fully expanding the state and action nodes is extremely computationally inefficient. Rather, this theoretically well-behaved algorithm is what lets us effectively bridge the gap between Q ∗ P and Q ∗ MP.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Algorithm Definition", "weight": 1.0} -->

The Sparse Samplingω algorithm is defined with the procedures listed in Algorithm 1. The global variables are the discount factor γ, the generative model G, the observation width and number of particles C, and the planning depth D. GENPF is the helper function to generate the next-step particle belief set, where the particles are evolved according to the transition density T and the weights are updated through the observation density Z. In GENPF, the sampled states s ′ i are inserted into each next-step particle belief set baoj with the new weights w ′ i = wi · Z ( oj | a, s ′ i ), which are the adjusted probability of hypothetically sampling observation oj from state s ′ i. Furthermore, the reward returned by GENPF is the particle likelihood weighted reward ρ = ∑ i wiri / ∑ i wi of the current particle belief state, which is a constant output for a fixed pair of ¯ b, a.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Algorithm Definition", "weight": 1.0} -->

The main planning functions in Sparse Samplingω are the ESTIMATEV and ESTIMATEQ procedures. We use particle belief set ¯ b at every step d, which contain pairs ( si, wi ) that correspond to the generated sample and its corresponding weight. ESTIMATEV is a subroutine that returns the value function V, for an estimated state or belief, by calling ESTIMATEQ for each action and returning the maximum. Similarly, ESTIMATEQ performs sampling and recursively calls ESTIMATEV to estimate the Q -function at a given step with a weighted average. In ESTIMATEQ, Sparse Samplingω samples the next particle belief state using GENPF.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Algorithm Definition", "weight": 1.0} -->

Consequently, the Sparse Samplingω policy action can be obtained by calling the value estimation function ESTIMATEV ( ¯ b 0, 0 ) at the root node and taking an action that maximizes the Q -value.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Algorithm Definition", "weight": 1.0} -->

The particle belief set is initialized by drawing samples from b 0 and setting weights to 1 / C, as the samples were drawn directly from b 0. Sparse Samplingω is not computationally efficient as it fully expands the sparsely sampled tree with full particle belief states. It serves only to demonstrate theoretical convergence and is only practically applicable to very small toy POMDP problems.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Algorithm Definition", "weight": 1.0} -->

Sparse Samplingω is identical to the sparse sampling algorithm planning on a particle belief MDP. It also is a slight modification of the previously-published POWSS algorithm. Specifically, whereas POWSS generates exactly one observation and corresponding new belief for each particle in a belief, Sparse Samplingω randomly selects a state to generate the observation each time GENPF is called in Line 2 of Algorithm 1. This means that Sparse Samplingω performs a Monte Carlo sampling estimate of the next step value, while POWSS performs an importance weighted summation over the estimates.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Algorithm Definition", "weight": 1.0} -->

Most importantly, this duality of being a modification of POWSS algorithm maintaining similar convergence guarantees for POMDPs while simultaneously being an adaptation of the sparse sampling algorithm for particle belief MDP makes it the ideal candidate to bridge POMDPs and PB-MDPs together. As an added benefit, the definition of Sparse Samplingω is much simpler than the original POWSS algorithm, while still allowing us to use similar analysis techniques used in both POWSS and sparse sampling.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Theoretical Analysis", "weight": 1.0} -->

In this section, we will prove that Sparse Samplingω algorithm can be made to approximate both optimal Q -values of the POMDP Q ∗ P and PB-MDP Q ∗ MP arbitrarily closely by increasing the observation width C. Theorem 2 proves that the Sparse Samplingω algorithm approximates these Q -values with high probability by combining results from self-normalized importance sampling estimators and POWSS optimality proofs to prove the optimality in Q ∗ P, and sparse sampling proof to prove the optimality in Q ∗ MP.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IMPORTANCE SAMPLING", "weight": 1.0} -->

We begin the theoretical portion of this work by stating an important property about self-normalized importance sampling estimators (SN estimators). We have previously published this property but present it again here because of its importance to our analysis. One goal of importance sampling is to estimate an expected value of a function f ( x ) where x is drawn from a distribution P while the estimator only has access to another distribution Q along with the importance weights w P / Q ( x ) ∝ P ( x ) / Q ( x ). This technique is crucial for Sparse Samplingω because we wish to estimate the value for beliefs conditioned on observation sequences while only being able to sample from the marginal distribution of states for a given action sequence.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IMPORTANCE SAMPLING", "weight": 1.0} -->

We define the following quantities: Of particular importance is the infinite R´ enyi Divergence, d ∞, which can be rewritten as an almost sure bound on the ratio of P and Q: Assuming d ∞ (P||Q) is finite, we prove an estimator concentration bound in the following theorem.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IMPORTANCE SAMPLING", "weight": 1.0} -->

Theorem 1 (SN d ∞ -Concentration Bound). Let P and Q be two probability measures on the measurable space (X, F) with P absolutely continuous w.r.t. Q and d ∞ (P||Q) < + ∞. Let x 1,..., xN be N independent identically distributed random variables with distribution Q, and f: X → R be a bounded function (∥ f ∥ ∞ < + ∞). Then, for any λ > 0 and N large enough such that λ > ∥ f ∥ ∞ d ∞ (P||Q) / √ N, the following bound holds with probability at least 1 -3exp (-N · t 2 (λ, N)): Theorem 1 builds upon the derivation in Proposition D.3 of Metelli et al., which provides a polynomially decaying bound by assuming d 2 is bounded. Here, we compromise by further assuming that d ∞ exists and is bounded to get an exponentially decaying bound. The proof of Theorem 1 is given in Appendix A, and the intuitive explanation of the d ∞ assumption in the POMDP planning context is given in Section 4.2.2.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IMPORTANCE SAMPLING", "weight": 1.0} -->

This exponential decay is important for the proofs in this section. We need to ensure that all nodes of the Sparse Samplingω tree at all depths d reach convergence. The branching of the tree induces a factor proportional to C D. Theorem 1 applied with N = C will not only help offset the C D factor even with increasing depths, but also be consistent with Hoeffding-type bound exponential error rate that we also use to bound intermediate estimator errors.

<!-- chunk {"id": "body-0052", "role": "body", "section": "ASSUMPTIONS FOR ANALYZING SPARSE SAMPLINGω", "weight": 1.0} -->

- (i) S and O are continuous spaces, and the action space has a finite number of elements, | A | < + ∞. - (ii) The densities Z, T, b 0 have the property that, for any observation sequence {, j } d n = 1, the R´ enyi divergence of the target distribution P d and sampling distribution Q d (Eqs. and) is bounded above by d max ∞ for all d = 0,...,

<!-- chunk {"id": "body-0053", "role": "body", "section": "ASSUMPTIONS FOR ANALYZING SPARSE SAMPLINGω", "weight": 1.0} -->

- (iii) The reward function R is bounded by a finite constant R max, and hence the value function is bounded by V max ≡ R max 1 -γ. - (iv) We can sample from the generating function G and evaluate the observation density Z. - (v) The POMDP terminates after no more than D < ∞ steps.

<!-- chunk {"id": "body-0054", "role": "body", "section": "ASSUMPTIONS FOR ANALYZING SPARSE SAMPLINGω", "weight": 1.0} -->

- (vi) We restrict our analysis to all the beliefs b ∈ B that are realizable from the initial belief b 0 through Bayesian updates with action sequences { an } and observation sequences { on }.

<!-- chunk {"id": "body-0055", "role": "body", "section": "ASSUMPTIONS FOR ANALYZING SPARSE SAMPLINGω", "weight": 1.0} -->

Intuitively, condition (ii) means that the ratio of the observation probability conditioned on the true state to the marginal observation probability cannot be too high. Additionally, the results still hold even when either of S or O are discrete, so long as it does not violate condition (ii), by appropriately switching the integrals to sums.

<!-- chunk {"id": "body-0056", "role": "body", "section": "ASSUMPTIONS FOR ANALYZING SPARSE SAMPLINGω", "weight": 1.0} -->

Although our analysis is restricted to the case when γ < 1 and the problem has a finite horizon, we believe that similar results can be derived for either when γ = 1 for a finite horizon or for infinite horizon problems when γ < 1 by using the common argument that eventually future discounted rewards will be small. Furthermore, while the results from this section repeat steps taken in proving POWSS, we significantly modify the details for Sparse Samplingω.

<!-- chunk {"id": "body-0057", "role": "body", "section": "PARTICLE LIKELIHOOD WEIGHTING ACCURACY", "weight": 1.0} -->

As a precursor to Theorem 2, we establish a general result about function estimation using state particles with likelihood weights. This is useful because the inductive proof for showing Sparse Samplingω convergence in Lemma 2 relies heavily upon an SN estimator concentration inequality as well as a Hoeffding-type inequality.

<!-- chunk {"id": "body-0058", "role": "body", "section": "PARTICLE LIKELIHOOD WEIGHTING ACCURACY", "weight": 1.0} -->

Lemma 1 (Particle Likelihood SN Estimator Convergence). Suppose a function f is bounded by a finite constant ∥ f ∥ ∞ ≤ f max, and a particle belief state ¯ bd = { sd, i, wd, i } at depth d represents bd with particle likelihood weighting that is recursively updated as wd, i = wd -1, i · Z (od | a, sd). Then, for all d = 0,..., D -1, the following weighted average is the SN estimator of f under the belief bd corresponding to the actions { an } d -1 n = 0 and observations { on } d n = 1, for all beliefs bd ∈ B that are realizable given the initial belief b 0: and the following concentration bound holds with probability at least 1 -3exp (-C · t 2 max (λ, C)), Proof.

<!-- chunk {"id": "body-0059", "role": "body", "section": "PARTICLE LIKELIHOOD WEIGHTING ACCURACY", "weight": 1.0} -->

We only outline the important steps here, and defer the detailed proof of this lemma to Appendix B. The key of this proof lies in the fact that the state particles trajectories { sn, 1 },..., { sn, C } are independent identically distributed random variable sequences of depth d, as GENPF independently generates each state sequence i according to the transition density T. While GENPF generates highly correlated observation sequences and histories { on } d n = 1, the dependence on observation sequence for a given particle belief state is only through the particle likelihood weights.

<!-- chunk {"id": "body-0060", "role": "body", "section": "PARTICLE LIKELIHOOD WEIGHTING ACCURACY", "weight": 1.0} -->

We abbreviate some terms of interest with the following notation: where d is the depth, and i is the index of the state sample. Intuitively, T i 1: d is the transition density of the i th state sequence, { sn, i } d n = 1, and Z i 1: d is the conditional density of observation sequence { on } given the i th state sequence from the root node to depth d. Additionally, b i d denotes bd (sd, i) and wd, i the weight of sd, i.

<!-- chunk {"id": "body-0061", "role": "body", "section": "PARTICLE LIKELIHOOD WEIGHTING ACCURACY", "weight": 1.0} -->

Then, we apply importance sampling to our system for all depths d = 0,..., D -1. Here, P d is the normalized measure of the state sequence { sn, i } d n = 0 conditioned on the observation sequence { on } d n = 1 and action sequence { an } d -1 n = 0 up to the node at depth d, and Q d is the measure of the state sequence conditioned only on the action sequence. For simplicity, we use Z 1: d to denote the product of observation likelihoods ∏ d n = 1 Z (on | an -1, sn) and T 1: d to denote the product of transition densities ∏ d n = 1 T (sn | sn -1, an -1). Then, for an arbitrary action sequence { an }, the following describes the densities necessary to define importance weighting: Here, the integral to calculate the normalizing constant is taken over S d + 1, the Cartesian product of the state space S over d + 1 steps.

<!-- chunk {"id": "body-0062", "role": "body", "section": "PARTICLE LIKELIHOOD WEIGHTING ACCURACY", "weight": 1.0} -->

Now, we can show that the recursive likelihood updating scheme in Lemma 1 produces valid likelihood weights up to a normalization by simply expanding the weight wd, i: Consequently, we conclude that the weighted average with particle likelihood weights indeed corresponds to the proper SN estimator: We can apply the SN concentration inequality in Theorem 1 to obtain the concentration bound.

<!-- chunk {"id": "body-0063", "role": "body", "section": "PARTICLE LIKELIHOOD WEIGHTING ACCURACY", "weight": 1.0} -->

Note that proving this lemma allows us to apply the particle likelihood weighting SN inequality whenever we encounter weighted averages with particle likelihood weights for a realizable particle belief. Also, this result does not depend on any specific choice of observation sequence { on }.

<!-- chunk {"id": "body-0064", "role": "body", "section": "COUPLED CONVERGENCE OF SPARSE SAMPLINGω", "weight": 1.0} -->

The theorem below describes Sparse Samplingω 's coupled convergence to both optimal Q -values of the POMDP Q ∗ P and PB-MDP Q ∗ MP, as C is increased.

<!-- chunk {"id": "body-0065", "role": "body", "section": "COUPLED CONVERGENCE OF SPARSE SAMPLINGω", "weight": 1.0} -->

Theorem 2 (Sparse Samplingω Coupled Optimality). Suppose conditions (i)-(vi) are satisfied. Then, for any λ > 0 and 0 < δ ≤ 1, choosing particle count constant C that satisfies: the Q-function estimates ˆ Q ∗ ω, d (¯ bd, a) obtained for all depths d = 0,..., D -1, realized beliefs or histories bd encountered in the Sparse Samplingω tree, and actions a are jointly near-optimal with respect to Q ∗ P, d and Q ∗ MP, d with probability at least 1 -δ: To prove Theorem 2, we follow a similar proof strategy from our previous proof for POWSS to show that Eq. holds, and a similar strategy of the original sparse sampling proof to show that Eq. holds. In essence, this Sparse Samplingω convergence guarantee builds on POWSS and sparse sampling convergence guarantees, providing coupled convergence results to optimal Q -values of the POMDP Q ∗ P and PB-MDP Q ∗ MP.

<!-- chunk {"id": "body-0066", "role": "body", "section": "COUPLED CONVERGENCE OF SPARSE SAMPLINGω", "weight": 1.0} -->

First, we use induction in Lemma 2 to prove a concentration inequality for the value function at all nodes in the tree, starting at the leaves and proceeding up to the root. Consequently, proving Lemma 2 allows us to prove Theorem 2, with some justifications of how the parameter C can actually be explicitly chosen with the choice of λ, δ. The detailed proof for Theorem 2 is in Appendix D.

<!-- chunk {"id": "body-0067", "role": "body", "section": "COUPLED CONVERGENCE OF SPARSE SAMPLINGω", "weight": 1.0} -->

Lemma 2 (Sparse Samplingω Estimator Q -Value Coupled Convergence). For all d = 0,..., D -1 and a, the following bounds hold with probability at least 1 -6 | A | (4 | A | C) D exp (-C · ˜ t 2): Proof. We outline how we use the particle likelihood SN estimator inequality and Hoeffding inequality to bound the Q -values, and defer the detailed proof to Appendix C.

<!-- chunk {"id": "body-0068", "role": "body", "section": "COUPLED CONVERGENCE OF SPARSE SAMPLINGω", "weight": 1.0} -->

The optimal d -step Q -values for the POMDP Q ∗ P and the corresponding PB-MDP Q ∗ MP are The Sparse Samplingω value estimates are mathematically equal to where { Ii } are C independent identically distributed random variables with finite discrete distribution pw, d with probability mass pw, d (I = j) = (wd, j / ∑ k wd, k), and particle belief state ¯ b ′ [Ii] d + 1 is updated by an observation generated from sd, Ii. This reflects the fact that GENPF randomly selects a state particle so with probability wd, o / ∑ k wd, k C times independently to generate a new observation for the particle belief state after next step.

<!-- chunk {"id": "body-0069", "role": "body", "section": "COUPLED CONVERGENCE OF SPARSE SAMPLINGω", "weight": 1.0} -->

POMDP Value Convergence: First, we show that Eq. is satisfied, which is an adapted and substantially modified proof of POWSS convergence. Using the triangle inequality for a given step d of the inductive proof, we split the difference into two terms, the reward estimation error (A) and the next-step value estimation error (B): The reward estimation error (A) is exactly the particle likelihood importance sampling error for estimating the reward function R (·, a), which can be bounded by applying Lemma 1. This also proves the base case.

<!-- chunk {"id": "body-0070", "role": "body", "section": "COUPLED CONVERGENCE OF SPARSE SAMPLINGω", "weight": 1.0} -->

To bound the next-step value estimation error (B), we introduce particle likelihood SN estimators and Monte Carlo average estimators to bridge the following quantities (detailed definitions and bounds of each terms are in Appendix D): PB-MDP Value Convergence: Second, we show that Eq. is satisfied, which is an adapted and substantially modified proof of sparse sampling convergence.

<!-- chunk {"id": "body-0071", "role": "body", "section": "COUPLED CONVERGENCE OF SPARSE SAMPLINGω", "weight": 1.0} -->

Once again, we split the difference between the SN estimator and the Q ∗ MP function into two terms, the reward estimation error (A) and the next-step value estimation error (B): Since our particle belief MDP induces no reward estimation error, the term (A) is always 0 and proving the base case d = D -1 is trivial as (A) and (B) are both 0. Then, we show that the difference (B) is bounded for all d = 0,..., D -1. We use the triangle inequality repeatedly to separate it into two terms; the MC transition approximation error, and the inductive function estimation error (detailed definitions and bounds of each terms are in Appendix D): Combining the probability bounds used in both of these procedures results in a worst case O (exp (-t · C)) probability factor, where t is some constant, as both the SN concentration bound and the Hoeffding bound are exponentially decaying.

<!-- chunk {"id": "body-0072", "role": "body", "section": "COUPLED CONVERGENCE OF SPARSE SAMPLINGω", "weight": 1.0} -->

Since this upper bound on the estimation error needs to hold for all steps d = 0,..., D -1, we must apply the worst case union bound on the probability to ensure that every node in the tree achieves the desired concentration bound. This results in a worst case probability factor that is O (C D). Therefore, we can obtain the Q -value estimator concentration inequality, with convergence rate O (C D exp (-t · C)).

<!-- chunk {"id": "body-0073", "role": "body", "section": "Particle Belief MDP Approximation Guarantees", "weight": 1.0} -->

In this section, we establish the theoretical guarantees for using any approximately optimal MDP planning algorithm to solve the POMDP problem P by planning in the particle belief MDP MP. Theorem 3 shows that the Q -values Q ∗ P and Q ∗ MP are close to each other with high probability, and Theorem 4 shows that using any approximately optimal MDP planning algorithm A in the particle belief MDP MP as a policy yields near-optimal value in the original POMDP if applied repeatedly in a closed loop with the environment and an exact belief updater.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Particle Belief MDP Q -Value Approximation Optimality", "weight": 1.0} -->

We introduce Theorem 3, which probabilistically bridges the POMDP P and its corresponding particle belief MDP MP. In essence, this theorem claims that the two optimal Q -values Q ∗ P and Q ∗ MP are close with high probability, because creating a very accurate Q -value estimator via Sparse Samplingω that is close to both Q ∗ P and Q ∗ MP happens with high probability.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Particle Belief MDP Q -Value Approximation Optimality", "weight": 1.0} -->

Theorem 3 (Particle Belief MDP Q -Value Approximation Optimality). Given a finite horizon POMDP P and its corresponding particle belief MDP MP, there exists a number of particles C for which the optimal Q-value of the POMDP problem Q ∗ P (b, a) can be approximated by the optimal Q-value of the particle belief MDP problem Q ∗ MP (¯ b, a) with arbitrary precision. Namely, under the regularity conditions (i)-(vi), the following bound holds for a given realizable belief b, corresponding sampled particle belief ¯ b, and all available actions a with probability at least 1 -δ MP for a desired accuracy ε MP: Proof. The main idea of the proof is that we bridge the two Q -values, Q ∗ P and Q ∗ MP, via approximation through Sparse Samplingω with C particles. From Theorem 2, we have established that there exists an algorithm, Sparse Samplingω, which is jointly optimal in both senses of POMDP P and its corresponding particle belief MDP MP.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Particle Belief MDP Q -Value Approximation Optimality", "weight": 1.0} -->

Then, if we were to hypothetically perform Sparse Samplingω of depth D, the sum of the errors between the three types of Q -values at the root node, Q ∗ P, Q ∗ MP and ˆ Q ∗ ω, are jointly bounded with probability at least 1 -δ MP through Theorem 2, where δ MP = δ for notational clarity in this context. We use the fact that Q ∗ P and Q ∗ MP are the optimal Q -values at d = 0 for the POMDP and PB-MDP, respectively: Since this bound holds with high probability for creating any hypothetical Sparse Samplingω tree, this must mean that | Q ∗ P (b, a) -Q ∗ MP (¯ b, a) | ≤ ε MP in general with high probability.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Particle Belief MDP Q -Value Approximation Optimality", "weight": 1.0} -->

The convergence rate of δ MP is O ( C D exp ( -˜ t · C )). This means that as we increase the number of particles, we can expect better performance by approximately solving a POMDP via particle belief approximation.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Particle Belief MDP Planning Optimality", "weight": 1.0} -->

Corollary 1 (Particle Belief MDP Planning Optimality). Under regularity conditions necessary for both the particle belief MDP and an MDP planning algorithm A, if the optimal planner can approximate Q-values with arbitrary precision ε A with probability at least 1 -δ A in the corresponding particle belief MDP of a given POMDP, then the planning algorithm can approximate the POMDP Q-values within ε MP + ε A with probability at least 1 -δ MP -δ A: Proof. This is a straightforward application of triangle inequality for the Q -value estimation accuracy and worst case union bound for the probability.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Particle Belief MDP Planning Optimality", "weight": 1.0} -->

Note that it would also be possible to devise an expected value version of the bounds by converting the probability statement into an expected value statement.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Particle Belief MDP Planning Optimality", "weight": 1.0} -->

Essentially, Corollary 1 means that we can use any approximately optimal MDP planning algorithm to solve the POMDP problem by planning in the particle belief MDP instead, and still retain similar optimality guarantees. The most remarkable thing about this result is that it does not directly depend on the size of the state space nor the observation space. However, the dependence may indirectly come through the observation density and thus the R´ enyi divergence factor, and in practice, the generative model sampling complexity often depends on the dimensionality of the state space. Moreover, even though this approach is insensitive to the state and observation space size, the guarantees and practical algorithms are highly sensitive to the planning horizon D.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Particle Belief MDP Planning Optimality", "weight": 1.0} -->

In most practical cases, this method would usually incur an additional O ( C ) compute time factor in a given transition sampling step as single particle belief state generation now needs to propagate C particles forward instead of a single particle/state. Moreover, if the algorithm requires storing the beliefs, the memory requirements are increased by an O ( C ) factor compared with the MDP algorithm. Fortunately, as demonstrated in Section 6, a modest number of particles often gives adequate performance in practice.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Particle Belief MDP Planning Optimality", "weight": 1.0} -->

Proving Corollary 1 allows us to prove Theorem 4 with additional results from Kearns et al. and Singh and Yee. Through the near-optimality of the Q -functions, we conclude that the value obtained by employing a near-optimal MDP policy in the PB-MDP is also near-optimal in the original POMDP with further assumptions on the closed-loop POMDP system. In this context, we mean a near-optimal MDP planning algorithm A to be an algorithm with small values of ε A, δ A that would satisfy the conditions required in the proof of the theorem. Examples of such algorithms include sparse sampling and others. The detailed proof for Theorem 4 is in Appendix E.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Particle Belief MDP Planning Optimality", "weight": 1.0} -->

Theorem 4 (Particle Belief MDP Approximate Policy Convergence). Suppose a near-optimal MDP planning algorithm A is used to plan with particle belief MDP MP repeatedly in a closed loop with POMDP environment P and an exact Bayesian belief updater to process observations from the environment. Further assume that regularity conditions (i)-(vi) are met for MP and that A can approximate the Q-values of MP with arbitrary precision ε A with probability at least 1 -δ A.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Sparse Particle Filter Tree (Sparse-PFT)", "weight": 1.0} -->

By utilizing the results in Theorem 3 and Theorem 4, we can promote a variant of sampling-based MDP planning algorithm Upper Confidence Tree (UCT), Sparse UCT, into Sparse Particle Filter Tree (Sparse-PFT) and retain similar convergence guarantees for the POMDP. This results in an algorithm that is simple to implement, and enjoys both theoretical guarantees and high performance in practice.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Sparse Particle Filter Tree (Sparse-PFT)", "weight": 1.0} -->

The entry point of Sparse-PFT is the PLAN procedure which repeatedly calls the the SIMULATE procedure to construct the tree and choose an action. Both of these procedures are defined in Algorithm 2. The set of global variables for Sparse-PFT includes the same global variables used for Sparse Samplingω with the addition of n, the number of tree search queries, and c UCB and β UCB, the polynomial Upper Confidence Bound parameters that determine the amount of exploration in Line 3. The SIMULATE function is analogous to the function of the same name from UCT, with the only difference being that Sparse-PFT manages particle belief sets through GENPF (defined in Algorithm 1) rather than states directly.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Sparse Particle Filter Tree (Sparse-PFT)", "weight": 1.0} -->

In the above algorithm definition, C ( · ) represents the list of children nodes, N ( · ) the number of visits to the node, Q ( · ) the estimated Q -value at the node, and c UCB the Upper Confidence Bound exploration parameter. These lists are all implicitly initialized to 0 or / 0. The ROLLOUT procedure is an optional heuristic that runs a simulation with a heuristic rollout policy for d steps to estimate the value, while avoiding building a large computation tree at each step of simulation.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Sparse Particle Filter Tree (Sparse-PFT)", "weight": 1.0} -->

With the introduction of Sparse-PFT, we can view the recent POMDP algorithms as practical extensions of Sparse-PFT. For instance, PFT-DPW is a simple particle belief set ¯ b = { (si, wi) }, depth d.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Sparse Particle Filter Tree (Sparse-PFT)", "weight": 1.0} -->

Output: Ascalar q that is the total discounted reward of one simulated trajectory sample.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Numerical simulation experiments were conducted in order to evaluate and compare the performances of our new simple algorithm, Sparse-PFT, along with other solvers. In particular, we also ran experiments for Adaptive online packing-guided search (AdaOPS), a recent solver with practical performance and partial theoretical guarantees. We also show performances of other hallmark algorithms like QMDP and POMCP along with random policy to demonstrate the need for continuous observation POMDP solvers that can handle more general assumptions.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

The following sections contain descriptions of the evaluation problems along with discussion of solver performance. In all five of the numerical experiments shown in Fig. 3, the POMDP solvers were limited to at most 1 second of planning time per step. For closed-loop planning, whenever an observation was received from the environment, the belief was updated with a particle filter independent of the particle filter used in planning, and no part of the planning tree was saved for re-use on subsequent steps as done by Silver and Veness. Since the observations received from the environment in this outer simulation loop were not generated from state particles in the filter, a larger number particles compared to GENPF are used to ensure likely states are present. A total of 5000 simulation experiments were conducted for each configuration combination of solver and environment in order to obtain the Monte Carlo mean and standard error estimates for the Laser Tag and VDP tag environments, and 1000 simulation experiments for the Light Dark and Sub Hunt problems since planners typically yielded more consistent performances for these problems.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

The tabular summary of all results is given in Table 1, and corresponding figure summary of all results for different planning time allotments is given in Fig. 4. We also vary belief particle count C with SIMULATE calls held constant to demonstrate the effect of particle belief approximation resolution on the quality of the resulting policy in Fig. 10 by using the optimized hyperparameters from Table 2 with 1000 simulation experiments for Laser Tag, Light Dark and Sub Hunt, and 100 for VDP Tag and Discrete VDP Tag. The open source code for the experiments is built on the POMDPs.jl framework, and is available: github.com/WhiffleFish/PFTExperiments. The hyperparameter values used for the experiments are shown in Appendix F.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Laser Tag", "weight": 1.0} -->

The Laser Tag POMDP (Fig. 5) is taken from the DESPOT benchmarks wherein a robot is required to use laser sensors to localize with the ultimate goal of catching an evading robot. The agent's laser sensors extend radially in 8 evenly spaced directions and each return a rounded sensed distance sampled from a normal distribution given by N ( d, 2. 5 ) where d is the true distance to the nearest obstacle. Although the observation space is not continuous, it is sufficiently large (on the order of 10 6 ) that most online solvers would have to treat this as close to continuous.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Laser Tag", "weight": 1.0} -->

From the results, we find that the PFT methods outperform both POMCPOW and AdaOPS: Figure 5: Example Sparse-PFT operating in Laser Tag: as indicated by the belief (yellow), the agent (green) has roughly located the evading robot at bottom right corner.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Laser Tag", "weight": 1.0} -->

PFT-DPW consistently outperforms both planners across different planning times, and Sparse-PFT outperforms all other planners with increased planning time. This suggests that for Laser Tag, having a full particle belief approximation rather than dynamically varying particle size is helpful for keeping track of likely particle hypotheses. Furthermore, this also suggests that the double progressive widening has diminishing returns when the action space has a fixed small size.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Laser Tag", "weight": 1.0} -->

We note that POMCP particularly struggles on this problem compared to all other algorithms. The large observation space forces the trees constructed by POMCP to become extremely shallow due to each unique sampled observation resulting in a new leaf node. This hinders POMCP's ability to develop a non-myopic multi-step plan and yield accurate action values, empirically showing the importance of particle weighting. On the other hand, QMDP exhibits performance similar to the modern solvers. While the agent does not initially know its own location, it has sufficient information to localize using the laser sensor observations after some steps, and the evading robot behavior leads it reliably to the corners. Thus, since this problem requires less active information gathering, the crude QMDP approximation performs well.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Laser Tag", "weight": 1.0} -->

| | Laser Tag (D, D, D) | Light Dark (D, D, C) | Sub Hunt (D, D, C) |

<!-- chunk {"id": "body-0097", "role": "body", "section": "Light Dark", "weight": 1.0} -->

The 1-dimensional Light Dark POMDP is designed to require active information gathering. The state is an integer representing the position of the agent and the action space is A = {-10, -1, 0, 1, 10 }. Deterministic transitions are given by s ′ = s + a. The reward, dictates that the optimal policy drive the state to the origin as quickly as possible. Because the state is not immediately known, inferences over the true state must be made over noisy observations that grow in variance proportional to the Figure 6: Example Sparse-PFT trajectory for Light Dark, successfully localizing in the light region to reach the goal in the dark region. agent's distance from the light location at s = 10. The observation distribution is N (s, | s -10 | + ε), where ε is some small constant included to prevent observation weights from reaching + ∞ due to a collapse to a Dirac distribution when the agent arrives at the light location.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Light Dark", "weight": 1.0} -->

The planners that yield the highest expected reward in the Light Dark domain roughly follow a 2step plan: first localizing at the light location, then traveling down to the goal location. Essentially, the light location becomes a necessary subgoal. We can demonstrate this by creating a heuristic policy that initially steers towards the light region via certainty-equivalent control, and then takes action a = -10 down to the goal. This heuristic policy yields an expected reward of 62. 0 ± 0. 19 which is as good or better than any planner shown in Table 1.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Light Dark", "weight": 1.0} -->

Surprisingly, higher planning times do not necessarily correspond to increasing expected rewards in the Light Dark domain. For AdaOPS, the solver converges to its peak expected reward with a planning time as low as 0.01 seconds leading to marginal improvement with further increases in planning time. Within a planning time interval of [ 0. 03, 0. 1 ] seconds, the performance of POMCPOW decreases, indicating that the planner becomes increasingly confident in a suboptimal plan. One possible source of this overconfidence is beliefs represented by a single particle. This same behavior becomes evident in PFT planners when the PFT planner is supplied with a single rollout value estimation. However, by increasing the number of sampled particles that are chosen as the true state in belief-based rollouts, the belief value estimate is granted lower variance and greater accuracy, effectively reducing the time spent exploring suboptimal branches of the constructed tree.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Light Dark", "weight": 1.0} -->

Because Light Dark requires costly information gathering, QMDP performs suboptimally. Specifically, regardless of belief distribution entropy, QMDP myopically steers directly towards the goal location but rarely commits to taking action 0 within the simulation horizon due to high state uncertainty. POMCP also performs poorly due to the high branching factor introduced by the continuous observation space.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Sub Hunt", "weight": 1.0} -->

In the Sub Hunt POMDP, from the POMCPOW benchmark, the agent controls a submarine with the goal of finding and destroying an opposing submarine. The state space consists of the grid locations of both the agent and enemy submarines, a Boolean determining whether or not the enemy is aware of the agent's presence, and the enemy's goal direction ( { 1,..., 20 } 4 × { aware, unaware }×{ N, S, E, W } ). The agent is given the option to move three steps in any of the four cardinal directions, attack the enemy, or ping the enemy with active sonar while the enemy randomly chooses between taking two steps forward or one step diagonally forward.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Sub Hunt", "weight": 1.0} -->

In the Sub Hunt domain, PFT methods dominate all other planners over all planning times, with Sparse-PFT having a slight edge over all other planners. Because the state space is discrete, value iteration can be used to calculate Q -values for the fully observable MDP, and QMDP can be used for the rollout policy. With this strong belief-based rollout policy, both PFT-DPW and Sparse-PFT are able to construct nearly-optimal policies with planning times as low as 0.01 seconds, leading to no noticeable further improvement over longer planning times. Conversely, POMCPOW and AdaOPS have gradually increasing planning curves in Fig. 4, with AdaOPS nearly reaching the performance of PFT planners at 1 second and POMCPOW reaching an earlier inflection point, resulting in a final performance lower than the other three planners. POMCP and QMDP perform poorly due to the large branching factor and inability to perform costly information gathering, respectively.

<!-- chunk {"id": "body-0103", "role": "body", "section": "VDP Tag", "weight": 1.0} -->

The Van Der Pol Tag (VDP Tag) POMDP formulation tasks the agent with moving through a twodimensional space to catch an opponent whose dynamics are governed by the Van Der Pol differential equations, for which we use scaling constant µ = 2. Because this problem has a continuous state space (S = R 4), a continuous action space (A =[0, 2 π) ×{ 0, 1 }) and a continuous observation space (O = R 8), discrete value iteration is no longer admissible as input for a value estimation policy. AdaOPS is unable to handle continuous action spaces thus it is omitted from this benchmark. For the actiondiscretized VDP Tag, the available movement directions are 20 evenly spaced angles from 0 ◦ to 360 ◦.

<!-- chunk {"id": "body-0104", "role": "body", "section": "VDP Tag", "weight": 1.0} -->

The continuous VDP Tag domain is the first in which there exists a noticeable performance gap between Sparse-PFT and PFT-DPW, indicating that action progressive widening offers some utility over fixed widening in continuous action space problems. Furthermore, PFT-DPW and POMCPOW have similar performances across different planning times, suggesting that the main challenge of VDP Tag is being able to handle continuity of state, action, and observation spaces, while the particle belief approximation resolution does not affect the performance as much.

<!-- chunk {"id": "body-0105", "role": "body", "section": "VDP Tag", "weight": 1.0} -->

For discrete VDP Tag, we come across two new peculiarities: AdaOPS performance decreases with increased planning time, and PFT methods perform orders of magnitude worse than other planners at very low allotted planning times. This is likely attributable to a large Figure 9: An example Van Der Pol vector field (µ = 0. 5) which defines the target dynamics. Unlike the agent, the target is not blocked by the barriers. action space (|A| = 20) and a relatively expensive simulation function (RK4 integration). Because PFT methods propagate a collection of particles upon tree expansion, belief value estimates tend to be more accurate at the cost of added computation scaling linearly with the number of particles representing each belief. Thus, expanding all possible actions while using a computationally expensive simulator on all particles takes a long time, leading to very shallow trees.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Experimental Validation of Particle Belief Approximation Convergence", "weight": 1.0} -->

In order to test the effect of particle belief approximation resolution, or the number of belief particles C, on planner performance, we vary C while fixing the number of SIMULATE calls and using optimal hyperparameters found in Appendix F for Sparse-PFT planner. By increasing the the number of belief particles, the particle belief becomes a more accurate representation of the actual belief function, and should lead to a better optimal Q -value estimation.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Experimental Validation of Particle Belief Approximation Convergence", "weight": 1.0} -->

Across all five problem domains, increasing the number of particles C results in a roughly monotonic non-decreasing performance gain as shown in Fig. 10. In particular, we see a gradual performance increase for Laser Tag, VDP Tag, and Discrete VDP Tag as we increase the number of particles, while Light Dark and Sub Hunt problems reach their performance capacity rather quickly at less than 10 particles. However, when applying this principle to promote MDP algorithms into PB-MDP algorithms, the particle filtering transition generative model requires an extra O ( C ) computation and memory factor, so it is important to balance computational resource needs and value estimation accuracy when deploying these algorithms in practice.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Experimental Validation of Particle Belief Approximation Convergence", "weight": 1.0} -->

These results offer two valuable insights. First, the experiment outcomes are consistent with the general trend suggested by the theoretical analysis: increasing the number of particles results in improved performance, presumably because the Q -value estimates are more likely to be accurate as established in Section 5. Second, not all problems benefit the same way from increasing the number of particles. Light Dark and Sub Hunt have rather simple state spaces, and adding more particles did not significantly improve the policy performance. In contrast, the other three problems continually benefited from having increased resolution of belief approximation. The belief approximation resolution is not the only factor contributing to the problem difficulty, but also other factors like action space cardinality and existence of simple rollout policies that perform well will contribute to the problem difficulty.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we formally show that optimality guarantees in a finite sample particle belief MDP (PB-MDP) approximation of a POMDP yields optimality guarantees in the original POMDP as well, which allows for simple yet powerful adaptations of MDP algorithms to solve POMDPs. By proving that the Sparse Samplingω Q -value estimates are close to both optimal Q -values of the POMDP and PB-MDP with high probability, we conclude that the optimal Q -values of the POMDP and PBMDP themselves are close with high probability. This fundamental bridge between PB-MDPs and POMDPs allows us to adapt any sampling-based MDP algorithm of choice to a POMDP by solving the corresponding particle belief MDP approximation and to preserve the convergence guarantees in the POMDP. The transformation only increases the computational complexity of transition generation by a factor of O ( C ) by using particle filtering-based generative models. Our convergence result is not directly dependent on the size of the state space nor the observation space, but rather dependent on the R´ enyi divergence that links the probabilities concerning state and observation trajectories.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This motivates particle belief-based POMDP algorithms such as Sparse Particle Filter Tree (Sparse-PFT), which enjoys algorithmic simplicity, theoretical guarantees, and practicality.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Conclusion", "weight": 1.5} -->

There are many interesting avenues for future research. First, the broader theoretical justification of more complex algorithms, such as POMCPOW and DESPOTα, still do not exist. Showing theoretical validity of these algorithms would help to close the gap between theory and practice even further. In addition, as seen in our numerical experiments, the best performing algorithm varies across different types of benchmarks. Further theoretical and empirical characterization of which algorithms are most effective for which problems could greatly aid practitioners. Also, the particle number sweep suggests a method to characterize the difficulty of a POMDP problem, which may be of interest for both practitioners and researchers alike. Lastly, while the algorithms presented here perform well in low dimensional continuous observation spaces, tree search for more difficult POMDPs, such as those with high dimensional observations and continuous/hybrid action spaces is more difficult, and further analytical and empirical research is warranted.
