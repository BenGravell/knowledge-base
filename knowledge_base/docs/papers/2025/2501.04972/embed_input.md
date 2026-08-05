<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Algebraic Characterization of Equivalence between Oracle-based Iterative Algorithms

Topics include Convex optimization, Linear transformations, Optimization, Control.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

When are two algorithms the same? How can we be sure a recently proposed algorithm is novel, and not a minor variation on an existing method? In this paper, we present a framework for reasoning about equivalence between a broad class of iterative algorithms, with a focus on algorithms designed for convex optimization. We propose several notions of what it means for two algorithms to be equivalent, and provide computationally tractable means to detect equivalence. Our main definition, oracle equivalence, states that two algorithms are equivalent if they result in the same sequence of calls to the function oracles (for suitable initialization). Borrowing from control theory, we use state-space realizations to represent algorithms and characterize algorithm equivalence via transfer functions. Our framework can also identify and characterize equivalence between algorithms that use different oracles that are related via a linear fractional transformation. Prominent examples include linear transformations and function conjugation. To support the paper, we have developed a software package named Linnaeus that implements the framework to identify other iterative algorithms that are equivalent to an input algorithm.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Large-scale optimization problems in machine learning, signal processing, and imaging have fueled ongoing interest in iterative optimization algorithms. New optimization algorithms are regularly proposed to capture more complicated models, reduce computational burdens, or obtain stronger performance and convergence guarantees.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, the novelty of an algorithm can be difficult to establish because algorithms can be written in different equivalent forms. For example, Algorithm 1.1 was originally proposed by Popov in the context of solving saddle point problems. This method was later generalized by Chiang et al. [2, § 4.1] in the context of online optimization. Algorithm 1.2 is a reformulation of Algorithm 1.1 adapted for use in generative adversarial networks (GANs). Algorithm 1.3 is an adaptation of Optimistic Mirror Descent used by Daskalakis et al. and also used to train GANs. Finally, Algorithm 1.4 was proposed by Malitsky for solving monotone variational inequality problems. In all four algorithms, the vectors x k 1 and x k 2 are algorithm states, η is a tunable parameter, and F is the gradient of the loss function.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

| Algo. 1.1 (Modified Arrow-Hurwicz) | Algo. 1.2 (Extrapolation from the past) | Algorithms 1.1-1.4 are equivalent in the sense that when suitably initialized, the sequences (x k 1) k ≥ 0 and (x k 2) k ≥ 0 are identical for all four algorithms. 1 Although these particular equivalences are not difficult to verify and many have been explicitly pointed out in the literature, for example, algorithm equivalence is not always immediately apparent.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we present a framework for reasoning about algorithm equivalence, with the ultimate goal of making the analysis and design of algorithms more principled and streamlined.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

- Auniversal way of representing algorithms, inspired by methods from control theory. - A computationally efficient way to verify whether two algorithms are equivalent. - Sensible definitions of what it means for algorithms to be equivalent.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

1 In their original formulations, Algorithms 1.1, 1.2 and 1.4 included projections onto convex constraint sets. We assume an unconstrained setting here for illustrative purposes. Some of the equivalences no longer hold in the constrained case.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

- A software package implementing this framework named Linnaeus. The software takes an algorithm described using natural syntax as input, and returns a canonical form with known names and pointers to relevant literature.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper studies equivalence of oracle-based algorithms at the oracle interface; any underlying optimization problem is external to the framework.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Briefly, our method is to parse each algorithm to a standard form as a linear system in feedback with a nonlinearity; to compute the transfer function of each linear system; and to check whether certain key relationships hold between the transfer functions of the algorithms in question.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper is organized as follows. In Section 2, we briefly summarize existing literature related to our work. In Section 3, we introduce four examples of equivalent algorithms that motivate our framework. In Section 4, we briefly review important background on linear systems and optimization used throughout the paper and in Section 5, we present our control-inspired mathematical framework for algorithm representation. We formally define three notions of algorithm equivalence: oracle equivalence (Section 6), shift equivalence (Section 7), and LFT equivalence (Section 8) to handle cases: one oracle, multiple oracles, and different but related oracles, respectively. We discuss further generalizations and applications in Section 9 and conclude in Section 11.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Motivating examples", "weight": 1.0} -->

Algorithms 1.1-1.4 discussed in Section 1 were equivalent in a strong sense; the iterates were in exact correspondence. In this paper, we adopt a broader view of equivalence, which we now illustrate with four motivating examples. Each example provides a different way that we consider two algorithms to be equivalent.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Motivating examples", "weight": 1.0} -->

First consider Algorithms 3.1 and 3.2. We may transform the iterates of Algorithm 3.1 by the invertible linear map ξ k 1 = 2 x k 1 -x k 2, ξ k 2 = -x k 1 + x k 2 to yield the iterates of Algorithm 3.2. Although the iterates are not in exact correspondence as in Algorithms 1.1-1.4, the sequences ( x k 1 ) k ≥ 0 and ( x k 2 ) k ≥ 0 are equivalent to the sequences ( ξ k 1 ) k ≥ 0 and ( ξ k 2 ) k ≥ 0 up to an invertible linear transformation.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Motivating examples", "weight": 1.0} -->

The second example consists of Algorithms 3.3 and 3.4. Algorithm 3.4 is ordinary gradient descent. These algorithms do not even have the same number of state variables, so these algorithms are not equivalent up to an invertible linear transformation. But when suitably initialized, we may transform the iterates of Algorithm 3.3 by the linear map ξ k = -x k 1 +2 x k 2 to yield the iterates of Algorithm 3.4. This transformation is linear but not invertible. Instead, notice that the sequence of calls to the gradient oracle are identical: the algorithms satisfy oracle equivalence, a notion we will define formally later in this paper. Note that Algorithms 3.1 and 3.3 look similar, yet Algorithm 3.1 is not equivalent to gradient descent.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Motivating examples", "weight": 1.0} -->

| Algo. 3.5 (Douglas-Rachford) | Algo. 3.6 (Simplified ADMM) | The third example consists of Algorithms 3.5 and 3.6. These algorithms are known as Douglas-Rachford splitting and a special case of the alternating direction method of multipliers (ADMM) [13, § 8], respectively. With suitable initialization, they will generate the same sequence of calls to the proximal operators, ignoring the very first call to one of the oracles. Specifically, Algorithm 3.6 is initialized as ξ 0 2 = x 1 1, ξ 0 3 = x 0 3 -x 1 1 and the first call to prox f in Algorithm 3.5 is ignored. We will say they are equivalent up to a prefix or shift: they satisfy shift equivalence. We will revisit these algorithms in Section 7.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Motivating examples", "weight": 1.0} -->

| Algo. 3.7 (Proximal gradient) for k = 0, 1, 2,... do y k = x k - t ∇ f (x k) x k +1 = prox tg (y k) end for | Algo. 3.8 (Conjugate proximal gradient) for k = 0, 1, 2,... do y k = x k - t ∇ f (x k) x k +1 = y k - t prox 1 t g ∗ (1 t y k) end for | Finally, consider Algorithms 3.7 and 3.8. These algorithms do not even call the same oracles; the first algorithm calls ∇ f and prox tg while the other calls ∇ f and prox 1 t g ∗ (the proximal operator of the Fenchel conjugate of g).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Motivating examples", "weight": 1.0} -->

Nevertheless, these two oracles are related via Moreau's identity: x = prox tg (x) + t prox 1 t g ∗ (1 t x) and applying this identity immediately relates Algorithms 3.7 and 3.8. These algorithms satisfy LFT equivalence and we will revisit them in Section 8.1.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Motivating examples", "weight": 1.0} -->

In Sections 6-8, we will develop increasingly general notions of equivalence that cover all the motivating examples above and more. Before we can formally define algorithm equivalence, we begin by introducing the mathematical representation, borrowed from control theory, that we use to describe iterative algorithms.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Oracle-based iterative algorithms", "weight": 1.0} -->

We assume an oracle-based model for our iterative algorithms. The algorithm can query a set of oracles at discrete query points [21, § 4][22, § 1][23, § 1]. Common examples of oracles include gradients, proximal operators, and projection onto a constraint set [24, § 6][25, § 2][26, § 1]. We assume that the oracle outputs are unique and deterministic once any exogenous choices have been fixed. For example, a subgradient oracle might return the subgradient of minimum norm, and a stochastic gradient oracle might return the gradient corresponding to a particular sample path.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Oracle-based iterative algorithms", "weight": 1.0} -->

For an iterative algorithm that uses oracles (ϕ 1,..., ϕ p), we assume the following. 1. The algorithm maintains an internal state x k ∈ V n that is initialized to some x 0 before the algorithm begins. 2. During iteration k, each oracle ϕ i is queried exactly once. We call the associated query point y k i ∈ V and the query result u k i ∈ V. In other words, u k i = ϕ i (y k i). This convention ensures that query points and results are well defined and unambiguous. If an oracle must be queried multiple times during each iteration, we can simply treat each query as a separate oracle (see Repeated oracles in Section 9). 3. During iteration k, the oracles are queried in a prescribed order ϕ i 1,..., ϕ i p. Each query point y k i j is a linear function of the state x k and possibly of the query results u k i 1,..., u k i j -1 obtained thus far.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Oracle-based iterative algorithms", "weight": 1.0} -->

4. Once all oracles have been queried, the internal state x k is updated to x k +1 using a linear function of x k ∈ V n and of u k ∈ V p. 5. All aforementioned linear functions are the same at every iteration (independent of k). In other words, the algorithm is time-invariant.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Oracle-based iterative algorithms", "weight": 1.0} -->

We will see that this class of algorithms includes commonly used algorithms, such as accelerated methods, proximal methods, operator splitting methods, and more.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Oracle-based iterative algorithms", "weight": 1.0} -->

Our framework excludes algorithms whose parameters explicitly depend on the iterate index k, such as gradient-based methods with diminishing stepsizes. We view time-varying algorithms as schemes for switching between different time-invariant algorithms. Thus, in our framework, the notion of algorithm equivalence pertains to the time-invariant algorithmic components, while the time variation is captured separately by the switching scheme. Since our aim is to reason about algorithm equivalence, we therefore restrict attention to time-invariant algorithms.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Oracle-based iterative algorithms", "weight": 1.0} -->

Here is a pseudo-code implementation of a generic iterative algorithm that satisfies the assumptions above.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Oracle-based iterative algorithms", "weight": 1.0} -->

Initialize: x 0 ∈ V n for k = 0, 1, 2,... do for i = 1,..., p do y k i = ∑ n j =1 c ij x k j + ∑ i -1 j =1 d ij u k j ▷ Evaluate query point for i th oracle. u k i = ϕ i (y k i) ▷ Query i th oracle. end for x k +1 = Ax k + Bu k ▷ Update internal state. end for Algo. 4.1 Implementation of a generic iterative algorithm

<!-- chunk {"id": "body-0027", "role": "body", "section": "State-space form", "weight": 1.0} -->

We can write the updates in Algorithm 4.1 in the more compact form where A ∈ R n × n, B ∈ R n × p, C = [c ij] ∈ R p × n, and D = [d ij] ∈ R p × p. The equations can also be represented visually using a block diagram, as in Fig. 1.

<!-- chunk {"id": "body-0028", "role": "body", "section": "State-space form", "weight": 1.0} -->

Remark 1. In Algorithm 4.1, we assumed the oracles were queried in the order ϕ 1,..., ϕ p, so the D = [ d ij ] matrix is strictly lower triangular. If the oracles were queried in a different order, the rows and columns of D would be permuted accordingly.

<!-- chunk {"id": "body-0029", "role": "body", "section": "State-space form", "weight": 1.0} -->

Fig. 1: Block diagram representation of a generic iterative algorithm.

<!-- chunk {"id": "body-0030", "role": "body", "section": "State-space form", "weight": 1.0} -->

The representation of Fig. 1 separates the oracles, which map y k ↦→ u k, from the algorithm, which maps ( x 0, u 0, u 1,..., u k ) ↦→ y k. This decomposition was first developed. The algorithm is characterized by the matrices ( A,B,C,D ), which are called a state-space realization, and are a widely used representation for linear time-invariant dynamical systems.

<!-- chunk {"id": "body-0031", "role": "body", "section": "State-space form", "weight": 1.0} -->

We now present a few examples that illustrate how to find a state-space realization.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Example: Reflected Gradient Method", "weight": 1.0} -->

Consider Algorithm 1.4, which uses oracle F and has update equation Since the update for x k +1 1 depends on both x k 1 and x k -1 1, we augment the internal state to include this past iterate. To this effect, we define x k 2:= x k -1 1 and obtain update equations with state (x k 1, x k 2) that only depend on the previous timestep: Define the oracle query point y k and query result u k. We can now express Eq. in the form of Algorithm 4.1 and Eq.: Therefore, a state-space realization for Algorithm 1.4 is given by

<!-- chunk {"id": "body-0033", "role": "body", "section": "Example: simplified ADMM", "weight": 1.0} -->

Consider Algorithm 3.6 (simplified ADMM), which uses state variables (ξ k 1, ξ k 2, ξ k 3), oracles (prox f, prox g), and update equations Define the oracle query points (y k 1, y k 2) and query results (u k 1, u k 2). We can now express Eq. in the form of Algorithm 4.1 and Eq.: Therefore, a state-space realization for Algorithm 3.6 is given by

<!-- chunk {"id": "body-0034", "role": "body", "section": "Explicit and implicit implementations", "weight": 1.0} -->

Given a state-space realization ( A,B,C,D ) where A ∈ R n × n, B ∈ R n × p, C ∈ R p × n, and D ∈ R p × p, when is it possible to construct a corresponding step-by-step implementation in the form of Algorithm 4.1? By Remark 1, it is possible provided there exists a permutation matrix P such that P ⊤ DP is strictly lower-triangular. The permutation P describes the order in which the oracles ϕ 1,..., ϕ p will be evaluated in Algorithm 4.1. Put another way, if we view D as the adjacency matrix for a directed graph, the corresponding graph should be a directed acyclic graph (DAG).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Explicit and implicit implementations", "weight": 1.0} -->

If the D matrix does not correspond to a DAG, the graph will exhibit a cycle, which will manifest itself as an implicit equation involving oracles. 2 For example, consider the realization (A,B,C,D) = (1, -t, 1, -t). This algorithm has the update equation 2 also known as an 'algebraic loop' or a 'circular dependency'.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Explicit and implicit implementations", "weight": 1.0} -->

The D matrix is not strictly lower-triangular and x k +1 is defined implicitly.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Explicit and implicit implementations", "weight": 1.0} -->

Definition 2. If the state-space realization ( A,B,C,D ) for an algorithm has the property that there exists a permutation matrix P such that P ⊤ DP is strictly lowertriangular, we say that the algorithm has an explicit implementation. Otherwise, we say it has an implicit implementation.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Explicit and implicit implementations", "weight": 1.0} -->

The same algorithm may have an explicit implementation with one oracle and an implicit implementation with another oracle. For example, consider Eq. and let ϕ = ∇ f, where f is convex. Then, by the first-order optimality conditions, we have In other words, using the oracle prox tf yields an explicit implementation, but using the oracle ∇ f yields an implicit implementation. We will see later (Section 8.1) how to automatically detect such equivalences.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Explicit and implicit implementations", "weight": 1.0} -->

State-space realizations conveniently parametrize a large class of explicit and implicit algorithms in terms of matrices ( A,B,C,D ), but the representation is not unique. For example, Algorithms 1.1-1.4 have different realizations ( A,B,C,D ) despite having identical state sequences. In the next section, we show how tools from control theory can clarify the relations between these sorts of representations.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Algorithm representation", "weight": 1.0} -->

In this section, we explain how to represent algorithms using transfer functions, a standard tool in linear systems and control theory [29, § 1-3][28, § 1,2,5]. We will give an overview of relevant terminology and show how to convert an algorithm to and from the transfer function representation.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Algorithm representation", "weight": 1.0} -->

In Section 4, we discussed algorithms that have a state-space realization We represent semi-infinite sequences such as (x 0, x 1,...) using their z -transforms. That is, we define the formal power series 3 and similarly for ˆ u (z) and ˆ y (z). When taking the z -transform of the forward-shifted sequence (x 1, x 2, · · ·), we have: Evaluating the z -transform of, we obtain: The (matrix-valued) functions ˆ O (z) and ˆ H (z) are convenient to work with because they relate ˆ y (z) and ˆ u (z) via conventional matrix multiplication. The function ˆ H (z) is called the transfer function, and this is how we will represent the state-space system (A,B,C,D). We use the special notation Since these transfer functions arise from linear state-space systems, they are rational matrix-valued functions of z, so the identities required for our equivalence tests reduce to exact algebraic identities between rational functions.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Algorithm representation", "weight": 1.0} -->

For ease of notation, we will often omit the '(z)' after each transfer function, so when we write ˆ H 1 = ˆ H 2, we mean that ˆ H 1 (z) = ˆ H 2 (z) for all z. We will also overload oracles so that they may apply to the z -transforms directly by threading across coefficients. Namely, if Φ(y k) = u k for k = 0, 1,..., we will write: Therefore, the block diagram of Fig. 1 can be written in terms of transfer functions and z -transforms as in Fig. 2.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Algorithm representation", "weight": 1.0} -->

3 The use of z -1 as the variable in the z -transform is a common convention in control theory.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Algorithm representation", "weight": 1.0} -->

Fig. 2: Block diagram representation of a generic optimization algorithm expressed in terms of its transfer function ˆ H and the z -transforms of its inputs and outputs.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Algorithm representation", "weight": 1.0} -->

Applying the formula to the state-space matrices of simplified ADMM (Algorithm 3.6), we obtain the transfer function The transfer function can be readily computed directly from the update equations by replacing each state by its z -transform, neglecting initial conditions, and eliminating the state variables. The following Python code computes the transfer function for Algorithm 3.6 (Eq.) starting from the update equations.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Algorithm representation", "weight": 1.0} -->

from sympy import Eq, var, solve, simplify, linear_eq_to_matrix # Define the symbols var(' z xi1 xi2 xi3 y1 y2 u1 u2 ') # Unknowns to solve for unknowns = (xi1, xi2, xi3, y1, y2) # State -update and output equations eqns = [Eq(z*xi1, u2), # xi1[k+1] = u2[k] Eq(z*xi2, u1), # xi2[k+1] = u1[k] Eq(z*xi3, xi3 + z*xi1 -z*xi2), # xi3[k+1] = xi3[k] + xi1[k+1] -xi2[k+1] Eq(y1, z*xi1 + xi3), # y1[k] = xi1[k+1] + xi3[k] Eq(y2, xi2 -xi3), # y2[k] = xi2[k] -xi3[k]] # Solve

<!-- chunk {"id": "body-0047", "role": "body", "section": "Algorithm representation", "weight": 1.0} -->

for states and outputs in terms of inputs sol = solve(eqns, unknowns) # Algorithm inputs and outputs inputs = (u1, u2) outputs = (sol[y1], sol[y2]) # Extract transfer matrix H from y = H u H, _ = linear_eq_to_matrix(outputs, inputs) H = simplify(H) Eq. shows that state-space systems have two components: 1. The map from initial state to output, ˆ O. 2. The transfer function, ˆ H.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Algorithm representation", "weight": 1.0} -->

We argue that the transfer function ˆ H alone is a sufficiently rich representation for the purpose of evaluating the equivalence of state-space systems. Roughly, when two state space systems have the same transfer function, we can find initial conditions that cause the systems to have identical input-output maps. In other words, from the perspective of the oracle, the algorithms are indistinguishable. We state this result as Proposition 3 below.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Algorithm representation", "weight": 1.0} -->

Proposition 3. Suppose system i ∈ { 1, 2 } has state-space realization (A i, B i, C i, D i), initial state x 0 i, and associated transfer function ˆ H i. The following are equivalent. 2. There exist x 1 and x 2 such that both systems have the same input-output map.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Algorithm representation", "weight": 1.0} -->

Under additional mild assumptions about the state-space realization, we can strengthen the forward implication of Proposition 3 to include any initial condition.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Algorithm representation", "weight": 1.0} -->

Proposition 4. Consider the setting of Proposition 3 and further assume that both systems have minimal state-space realizations. The following are equivalent. 2. For every initialization of one system, there exists a unique initialization of the other system such that both systems have the same input-output map.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Algorithm representation", "weight": 1.0} -->

Minimality (see Appendix A.1) means that the realization contains no redundant internal state. Equivalently, among all state-space realizations that induce the same transfer function, a minimal realization has the smallest possible state dimension. In the present context, this means that the realization stores exactly the internal memory needed to reproduce the same oracle-input/output behavior, and no more. Minimality is a mild assumption because from any non-minimal realization, one can construct a minimal realization with the same transfer function.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Algorithm representation", "weight": 1.0} -->

For proofs of Propositions 3 and 4 and further details on how to construct minimal realizations, see Appendices A.2 and A.3, respectively.

<!-- chunk {"id": "body-0054", "role": "body", "section": "From transfer functions to algorithms", "weight": 1.0} -->

In this paper, we study the equivalence of algorithms by analyzing their transfer functions. We always start with update equations, which lead to state-space realizations, which lead to transfer functions. For completeness, we also provide a complete characterization of when the process can be reversed, including a method to construct the update equations from the transfer function when possible, in Appendix A.3.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Algorithm equivalence", "weight": 1.0} -->

In the following three sections, we propose three notions of algorithm equivalence, each increasingly more general. 1. Oracle equivalence. For use when comparing algorithms that each use the same single oracle. 2. Shift equivalence. For use when comparing algorithms that each use the same set of oracles. Oracle equivalence is a special case of shift equivalence. 3. LFT equivalence. For use when comparing algorithms that use oracles that are related via a linear fractional transforms (LFTs), which we define in Section 8. Oracle equivalence and shift equivalence are both special cases of LFT equivalence.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Algorithm equivalence", "weight": 1.0} -->

Although the above notions of equivalence cover all examples of algorithm equivalence we have observed in practice, there are limitations to our definitions. We discuss limitations and possible extensions in Section 9.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Oracle equivalence", "weight": 1.0} -->

The idea behind oracle equivalence is to ask the question: 'are the algorithms indistinguishable from the point of view of the oracle?' In other words, if the algorithms are suitably initialized, would using the same algorithm inputs (oracle outputs) ( u 0, u 1,... ) for both algorithms always produce the same algorithm outputs (oracle inputs) ( y 0, y 1,... )? If the answer is 'yes', then the algorithms are oracle equivalent.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Oracle equivalence", "weight": 1.0} -->

Motivated by Propositions 3 and 4, we will formally define oracle equivalence using the notion of transfer functions.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Oracle equivalence", "weight": 1.0} -->

Definition 5 (oracle equivalence). Two algorithms that use the same oracles are oracle equivalent if they have have the same transfer function.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Oracle equivalence", "weight": 1.0} -->

Oracle equivalence is a useful notion of algorithm equivalence: 1. There are many ways to re-parameterize an algorithm that change the state-space matrices (A,B,C,D) or the internal state x k. A sensible notion of equivalence should be independent of such transformations. Oracle equivalence achieves this independence by bypassing the state entirely and treating the algorithm as the map (u 0, u 1,...) ↦→ (y 0, y 1,...). 2. Since oracle-equivalent algorithms generate identical oracle-input and oracle-output sequences, many analytical properties of interest are preserved, especially those commonly studied for optimization algorithms. For example, if the oracle is the gradient of a differentiable function, u k = ∇ f (y k), then any quantity determined solely by the gradient queries and responses evolves identically for the two algorithms, including the sequence of gradient norms ∥∇ f (y k) ∥, the sequence of queried objective values f (y k), and any certificate or bound expressed in terms of these quantities.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Invariance under linear state transformations", "weight": 1.0} -->

Oracle equivalence (Definition 5) is invariant under linear transformations of state. Specifically, define ˜ x k = Tx k for each k, where T is an invertible matrix. The statespace equations expressed in terms of the new state variable ˜ x k become Substituting into Eq., we can verify that both systems have the same transfer function. 4 If we initialize the transformed system with ˜ x 0 = Tx 0 and apply the same input (u 0, u 1,...) to both systems, we will obtain the same output (y 0, y 1,...), although the respective states x k and ˜ x k will generally be different. This invariance is the key to understanding when two optimization algorithms are the same, even if they look different as written. For example, this idea alone suffices to show that Algorithms 3.1 and 3.2 are equivalent.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Invariance under linear state transformations", "weight": 1.0} -->

4 Both systems will also have the same Markov parameters and Hankel matrices (see Appendix A.1).

<!-- chunk {"id": "body-0063", "role": "body", "section": "Invariance under linear state transformations", "weight": 1.0} -->

When using linear state transformations, the number of states (size of the A matrix) is preserved. However, realizations with a different number of states can also be oracle equivalent. Although a realization with a larger A matrix will generally lead to a transfer function with higher degree (via Eq. ), there may be common factors that cancel from the numerator and denominator, leading to lower-degree transfer functions that could have been obtained from a realization with a smaller A matrix. This idea is related to the notion of minimality (see Appendix A.1) and explains why Algorithms 3.3 and 3.4 are equivalent.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Examples of oracle equivalence", "weight": 1.0} -->

Now, we will revisit the first and second motivating examples and apply Definition 5 to show oracle equivalence. Specifically, we will compute transfer functions using Eq. and verify that they are the same.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Algorithms 3.1 and 3.2", "weight": 1.0} -->

The state-space realization and transfer function of Algorithms 3.1 and 3.2 are Since ˆ H 3. 1 = ˆ H 3. 2, Algorithms 3.1 and 3.2 are oracle-equivalent by Definition 5. Algorithm 3.1 can also be transformed to Algorithm 3.2 as in Eq. via T =.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Algorithms 3.3 and 3.4", "weight": 1.0} -->

The state-space realization and transfer function of Algorithms 3.3 and 3.4 are Since ˆ H 3. 3 = ˆ H 3. 4, Algorithms 3.3 and 3.4 are oracle-equivalent by Definition 5. The transfer functions are the same due to the cancellation of the common factor (z -2) in the numerator and denominator of ˆ H 3. 3.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Algorithms 1.1-1.4", "weight": 1.0} -->

Using the same approach as above, we can derive the transfer functions for Algorithms 1.1-1.4 and show that they are all equal to ˆ H ( z ) = -η (2 z -1) z ( z -1). Therefore, Algorithms 1.1-1.4 are oracle-equivalent by Definition 5.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Accelerated gradient methods", "weight": 1.0} -->

Accelerated gradient methods are a class of optimization algorithms designed to improve the convergence speed of gradient-based methods, especially for convex optimization problems. Accelerated methods incorporate momentum-like terms and interpolated iterates that help the optimization process converge faster. Two well-know methods include Polyak's Heavy Ball (HB) and Nesterov's Accelerated Gradient Method (NAG), shown below as Algorithms 6.1 and 6.2. These techniques and their stochastic variants are widely used in machine learning, signal processing, and numerical optimization.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Accelerated gradient methods", "weight": 1.0} -->

| Algo. 6.1 (Polyak's Heavy Ball) | Algo. 6.2 (Nesterov's Method) | Several works have proposed unified momentum algorithms and associated analyses that generalize HB and NAG and allow the algorithm designer to interpolate between both algorithms. Examples include: Triple Momentum Method, Quasi-Hyperbolic Momentum, Stochastic Unified Method, and Unified Stochastic Momentum, listed below as Algorithms 6.3-6.6, respectively.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Accelerated gradient methods", "weight": 1.0} -->

| Algo. 6.3 (Triple Momentum Method) | Algo. 6.4 (Quasi-Hyperbolic Momentum) | The transfer functions for HB and NAG are clearly different: However, the transfer functions for Algorithms 6.3-6.6 are: Each of the above transfer functions are of the form -a (z -c) (z -1)(z -b) for some a, b, c and can be made equal to one another (oracle equivalent) via suitable choices of the algorithm parameters. In other words, these algorithms parameterize the same space of possible algorithms (which also includes HB and NAG); they are equally general.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Distributed optimization", "weight": 1.0} -->

For our final example of this section, we consider synchronous distributed optimization, where a network of computing nodes work collaboratively to solve the problem Each node i maintains a local state x k i ∈ R d and can access the oracle ∇ f i. At every timestep, each node can gossip (obtain the local states of its neighboring nodes x k j), evaluate its local oracle, and perform computations to update its local state. There are two goals: consensus: the nodes' local states should converge to a common value, and optimality: the common value should be x ⋆, a solution of Eq.. For convenience, we use the shorthand notation Gossip is modeled as matrix multiplication Wx k, where W = ˜ W ⊗ I d and ˜ W ∈ R n × n is a (typically sparse) row-stochastic matrix; it satisfies 0 ≤ ˜ W ≤ 1 and W 1 = 1.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Distributed optimization", "weight": 1.0} -->

Under suitable assumptions on W, the algorithm x k +1 = Wx k achieves consensus at a linear rate, but the consensus value will be the mean of the x 0 i rather than x ⋆ (no optimality). Likewise, if the f i are smooth and strongly convex, gradient descent x k +1 = x k -α ∇ f ( x k ) achieves local but not global optimality: each node converges to the minimizer of its local f i rather than the minimizer of ∑ n i =1 f i. A simple algorithm that achieves both consensus and optimality is distributed gradient descent, which combines features of both gossip and gradient descent: x k +1 = Wx k -α k ∇ f ( x k ). However, this algorithm only converges sublinearly, even with strongly convex f i, and requires a diminishing stepsize α k → 0 to converge at all.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Distributed optimization", "weight": 1.0} -->

The first algorithm to guarantee linear convergence for strongly convex f i was EXTRA, and since then many papers have developed new algorithms or refined existing ones to solve Eq. with a linear convergence rate. Two such well-known algorithms are NIDS and Exact Diffusion, shown below.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Distributed optimization", "weight": 1.0} -->

| Algo. 6.7 NIDS | Algo. 6.8 Exact Diffusion | These algorithms were developed using different approaches. NIDS used a gradientdifferencing intuition similar to EXTRA to achieve linear convergence (storing the past gradient and updating based on the difference, as in Algorithm 6.7). In contrast, Exact Diffusion used an adapt-correct-combine concept (corresponding to the three update equations in Algorithm 6.8, respectively).

<!-- chunk {"id": "body-0075", "role": "body", "section": "Distributed optimization", "weight": 1.0} -->

However, NIDS and Exact Diffusion are (oracle) equivalent ! We can detect this equivalence automatically by computing the transfer function for each algorithm. In this case, we obtain ˆ H 6. 7 ( z ) = ˆ H 6. 8 ( z ) = -α ( z -1) W ( z 2 I -2 zW + W ) -1.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Shift equivalence", "weight": 1.0} -->

Now consider Algorithms 3.5 and 3.6 from the third motivating example. We can calculate that the algorithms have different transfer functions: so they are not oracle-equivalent. We can represent the equations for Algorithms 3.5 and 3.6 using block diagrams that are unrolled in time; see Fig. 3. Based on the diagram, it is clear that the algorithms are just shifted versions of one another. If we initialize Algorithm 3.6 using ξ 0 2 = x 1 1 and ξ 0 3 = x 0 3 -x 1 1, then it will make the same oracle calls as Algorithm 3.5, but with a time shift.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Shift equivalence", "weight": 1.0} -->

This example motivates us to define shift equivalence. As with oracle equivalence, we ask whether the algorithms are indistinguishable from the point of view of the oracle for suitably chosen input channel delays and state initializations. Before we define shift equivalence, we will formalize the notion of shifting.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Shift equivalence", "weight": 1.0} -->

Shifting (delaying) a semi-infinite sequence (y 0, y 1,...) by m time steps corresponds to multiplication of its z -transform by z -m: Fig. 3: Block diagrams representing Algorithm 3.5 (left) and Algorithm 3.6 (right). These algorithms are shift equivalent because when suitably initialized, they make the same calls to the oracles, albeit with a time shift. The updates are exactly the same for both algorithms, but using transformed variables.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Shift equivalence", "weight": 1.0} -->

Without loss of generality, we can assume ϕ = 0, 5 and since the oracle ϕ applies element-wise to each y k, the oracle ϕ commutes with the shift operation. We can represent this relationship by a commutative diagram; see Fig. 4.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Shift equivalence", "weight": 1.0} -->

For a vector-valued signal, we can delay each component by a different amount. This motivates the definition of the multi-shift.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Shift equivalence", "weight": 1.0} -->

5 If ϕ = 0, we can redefine the shift operation to pad the first m entries with ϕ instead of 0, which will ensure that ϕ commutes with the shift operation. Alternatively, we can re-center the algorithm states to be measured with respect to a fixed point of the dynamics, as is standard in control theory [41, § 4.2].

<!-- chunk {"id": "body-0082", "role": "body", "section": "Shift equivalence", "weight": 1.0} -->

Fig. 4: Commutative diagram visualizing that the shift (delay) operation commutes with the application of the oracle ϕ. The foreground shows the z -transformed versions of the signals, where the shift becomes multiplication by a power of z -1.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Shift equivalence", "weight": 1.0} -->

Definition 6 (multi-shift). We define the multi-shift ˆ ∆ m (z) for nonnegative integers m:= (m 1,..., m p) as the transfer function For example, consider the semi-infinite sequence (y 0, y 1, y 2,...), where each y k is partitioned into blocks y k 1, y k 2, y k 3, where the y k i are the same size for all k. Then, The multi-shift also commutes with any time-invariant oracle Φ = (ϕ 1,..., ϕ p). In terms of z -transforms, Φ(ˆ y) = ˆ ∆ -1 m Φ(ˆ ∆ m ˆ y). By rearranging the block diagram, we can move the multi-shifts from the oracle to the algorithm; see Fig. 5.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Shift equivalence", "weight": 1.0} -->

The transformation in Fig. 5 shows that from the point of view of the oracle Φ, the algorithms ˆ H and ˆ ∆ m ˆ H ˆ ∆ -1 m are indistinguishable. This motivates our definition of shift equivalence.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Shift equivalence", "weight": 1.0} -->

Definition 7 (shift equivalence). Suppose we are given two LTI algorithms that each use the same p oracles and have transfer functions ˆ H 1 and ˆ H 2, respectively. We say they are shift-equivalent and write ˆ H 1 ∼ ˆ H 2 if there exists a multi-shift ˆ ∆ m such that Fig. 5: Equivalent block diagram representing shift equivalence. We use the fact that the oracle Φ commutes with any multi-shift ˆ ∆ m. However, ˆ ∆ m need not commute with ˆ H, which means equivalent algorithms can have different transfer functions.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Shift equivalence", "weight": 1.0} -->

Our choice of the word equivalence is justified by the fact that shift equivalence is an equivalence relation.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Shift equivalence", "weight": 1.0} -->

Lemma 8. Shift equivalence, as defined in Definition 7, is an equivalence relation. That is, it satisfies the properties of reflexivity, symmetry, and transitivity.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Shift equivalence", "weight": 1.0} -->

Remark 9. Oracle equivalence is a special case of shift equivalence (with ˆ ∆ m = I ). Moreover, shift equivalence reduces to oracle equivalence when p = 1 (a single oracle). In this case, the transfer functions and multi-shifts are scalars rather than matrices, so they trivially commute: z -m ˆ H 1 = ˆ H 2 z -m ⇐⇒ ˆ H 1 = ˆ H 2.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Efficient enumeration of shift-equivalent algorithms", "weight": 1.0} -->

Given an algorithm ˆ H using oracles Φ = (ϕ 1,..., ϕ p), how can we generate all possible shift-equivalent algorithms? In other words, what are the possible transfer functions ˆ H ′ and multi-shifts ˆ ∆ m such that Since ˆ H ′ must be a proper transfer function (or strictly proper, depending on whether we require explicit implementations; see Appendix A.3), each ˆ H ij (z) z m j -m i must also be proper. Here, proper means that each entry is a rational function whose numerator degree is no larger than its denominator degree, while strictly proper means the numerator degree is strictly smaller. To determine the set of possible ˆ H ′, let r ij be the relative degree of ˆ H ij.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Efficient enumeration of shift-equivalent algorithms", "weight": 1.0} -->

That is, write ˆ H ij (z) = N ij (z) /D ij (z) (ratio of polynomials), and Then, properness of ˆ H ′ amounts to finding m i such that Since the set of feasible m i is translation-invariant, we can normalize each solution so that min i m i = 0, and each distinct solution { m i } will correspond to a distinct ˆ H ′ that is shift-equivalent to ˆ H. For an example of how we can enumerate solutions, see the primal-dual three-operator splitting example in Section 7.1.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Efficient determination of shift equivalence", "weight": 1.0} -->

Given two algorithms ˆ H and ˆ H ′ that use the same oracles (ϕ 1,..., ϕ p), we can efficiently check whether these algorithms are shift-equivalent by carrying out the following steps. 1. Check to make sure ˆ H ii = H ′ ii for all i (the diagonal entries must always match). Otherwise, they are not equivalent. 2. Check to make sure that for all i = j, either ˆ H ij = ˆ H ′ ij = 0, or H ij = 0 and ˆ H ′ ij = 0. In other words, ˆ H and ˆ H ′ must have matching sparsity patterns. Otherwise, they are not equivalent. 3. For all i = j such that ˆ H ij = 0, check to make sure that H ′ ij (z) / ˆ H ij (z) = z b ij for some integers b ij. In other words, corresponding entries of the algorithm's transfer functions must by related by multiplication by a power of z.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Efficient determination of shift equivalence", "weight": 1.0} -->

4. Consider the set of linear equations b ij = m j -m i for all i = j such that ˆ H ij = 0. Write the corresponding linear equations compactly as M ⊤ m = b. If this system of equations has a solution, then ˆ H ∼ ˆ H ′. Otherwise, they are not equivalent. Note that if a solution exists, we can always find a solution with integer m, since M is an incidence matrix and therefore is totally unimodular.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Douglas-Rachford splitting and ADMM", "weight": 1.0} -->

As computed in Eq., the transfer functions for Algorithms 3.5 and 3.6 are given by ˆ H 3. 5 = [ -1 z -1 1 z -1 2 z -1 z -1 -1 z -1 ] and ˆ H 3. 6 = [ -1 z -1 z z -1 2 z -1 z ( z -1) -1 z -1 ]. We see that they are related via.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Primal-dual three-operator splitting", "weight": 1.0} -->

For our next example, we consider algorithms for solving the optimization problem using the oracles prox τf, prox σg ∗, and ∇ h. Only recently have methods been proposed to solve this problem. Examples include the Condat-V˜ u algorithm independently proposed by Condat and V˜ u, the primal-dual three-operator (PD3O) algorithm, and the primal-dual Davis-Yin (PDDY) algorithm. See and references therein for a recent survey on this problem. To illustrate our approach, we will focus on the primal-dual three-operator algorithm (PD3O), shown below.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Algo. 7.1 Primal-dual three-operator splitting (PD3O)", "weight": 1.0} -->

The state-space realization and transfer function for PD3O is 6 In, the authors show a reformulation of PD3O and state that it was obtained by changing the order of the variables and substituting ¯ x k = 2 x k -z k -τ ∇ h (x k) -τA ⊤ s k. After these changes, the reformulation is given by Algorithm 7.2 below.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Algo. 7.2", "weight": 1.0} -->

We can obtain the equivalence between Algorithms 7.1 and 7.2 immediately. Indeed, Algorithms 7.1 and 7.2 are shift equivalent because This is not the only possible shift-equivalence transformation. Applying the method outlined in Eq., the relative degree matrix of ˆ H 7. 1 is given by We seek nonnegative integers (m 1, m 2, m 3) normalized so that min i m i = 0 satisfying 6 We have removed identity matrices from the transfer function to simplify exposition. For example, entries in ˆ H 7. 1 (z) that read 1 z should be replaced by 1 z I.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Algo. 7.2", "weight": 1.0} -->

Algorithm 7.1 corresponds to the trivial solution, and Algorithm 7.2 corresponds to. By inspection, we see there are three solutions. The third solution is and it corresponds to the new algorithm One possible realization of Algorithm 7.3 is given below.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Algo. 7.3 Another reformulation of PD3O", "weight": 1.0} -->

We stress that these equivalences are tedious to work out by hand, and since there are now three oracles, the equivalences are far from obvious. For example, here is another way to realize Algorithm 7.2. This time, the transfer functions are the same, so Algorithms 7.2 and 7.4 are oracle-equivalent.

<!-- chunk {"id": "body-0099", "role": "body", "section": "LFT equivalence", "weight": 1.0} -->

In Sections 6 and 7, we considered equivalence between algorithms that use the same oracles. In this section, we consider equivalence between algorithms that use different but related oracles.

<!-- chunk {"id": "body-0100", "role": "body", "section": "LFT equivalence", "weight": 1.0} -->

In convex optimization, algorithm conjugation naturally relates some oracles to others [13, § 2]: for example, if ( ∂f )( x ):= { g | f ( y ) ≥ f ( x ) + g ⊤ ( y -x ) for all y } is the subdifferential of f, prox f ( v ):= argmin x ( f ( x ) + 1 2 ∥ x -v ∥ 2 ) is the proximal operator of f, and f ∗ ( y ):= sup x { x ⊤ y -f ( x ) } is the Fenchel conjugate of f [25, § 3], we have the following identities relating the different operators.

<!-- chunk {"id": "body-0101", "role": "body", "section": "LFT equivalence", "weight": 1.0} -->

- x = prox tf (x) + t prox 1 t f ∗ (1 t x) (Moreau's identity) We can rewrite any algorithm in terms of different, also easily computable, oracles using these identities. Consider a simple example: we will obfuscate the proximal gradient method (Algorithm 8.1 [24, § 10]) by rewriting it in terms of the conjugate of the original oracle prox g, using Moreau's identity, as Algorithm 8.2. These are the same as our motivating examples of Algorithms 3.7 and 3.8.

<!-- chunk {"id": "body-0102", "role": "body", "section": "LFT equivalence", "weight": 1.0} -->

| Algo. 8.1 Proximal gradient for k = 0, 1, 2,... do y k = x k - t ∇ f (x k) x k +1 = prox tg (y k) end for | Algo. 8.2 Conjugate proximal gradient for k = 0, 1, 2,... do y k = x k - t ∇ f (x k) x k +1 = y k - t prox 1 t g ∗ (1 t y k) end for | We can also use the relationship between the proximal and subdifferential operators to obtain versions of Algorithms 8.1 and 8.2 that use subdifferentials instead.

<!-- chunk {"id": "body-0103", "role": "body", "section": "LFT equivalence", "weight": 1.0} -->

| Algo. 8.3 Subdifferential | Algo. 8.4 Conjugate Subdifferential | Note that the update equations for Algorithms 8.3 and 8.4 involving subdifferentials are implicit. The transfer functions for Algorithms 8.1-8.4 are shown below, along with their associated oracles. We use the symbol ⋄ to show that an algorithm is used with a given set of oracles.

<!-- chunk {"id": "body-0104", "role": "body", "section": "LFT equivalence", "weight": 1.0} -->

Although the transfer functions of the algorithms change when we rewrite the algorithm to call a different oracle, the sequence of states is preserved ( x k and y k have the same values for all algorithms provided they are initialized the same way). This motivates us to define a general notion of equivalence that applies when two algorithms use different oracles that are related in a particular way.

<!-- chunk {"id": "body-0105", "role": "body", "section": "LFT equivalence", "weight": 1.0} -->

Definition 10 (Operator graph). Given an oracle Φ: V p →V p, we define its graph as the set of possible input-output pairs (in the z -domain). We adopt the linear algebraic notation R (range) overloaded as follows: Likewise, given an algorithm ˆ H, we define its dual graph as: Definition 11 (Linearly equivalent oracles). Let Φ 1 and Φ 2 be oracles. We say that Φ 1 is linearly equivalent to Φ 2 and we write Φ 1 ˆ M ∼ Φ 2, if their graphs are related by an invertible linear transformation ˆ M. In other words, Φ 1 ˆ M ∼ Φ 2 if This is equivalent to saying that: We will omit ˆ M and simply write Φ 1 ∼ Φ 2 to mean that there exists some invertible ˆ M such that Φ 1 ˆ M ∼ Φ 2.

<!-- chunk {"id": "body-0106", "role": "body", "section": "LFT equivalence", "weight": 1.0} -->

For example, prox f ∼ ∂f because: Since each x corresponds to some y and vice versa, it also holds for the z -transforms of arbitrary sequences (x 0, x 1,...) and corresponding (y 0, y 1,...) using the same 2 × 2 matrix.

<!-- chunk {"id": "body-0107", "role": "body", "section": "LFT equivalence", "weight": 1.0} -->

Proposition 12. (Special cases of linear relations) 1. Identity: If ϕ 1 = ϕ 2, then ϕ 1 ˆ M ∼ ϕ 2 with ˆ M = [I 0 0 I]. 2. Commutation: If ϕ (ˆ C ˆ y) = ˆ Cϕ (ˆ y) for all ˆ y, then ϕ ˆ M ∼ ϕ with ˆ M = [ˆ C 0 0 ˆ C]. 3. Equivariance: If ϕ 1 (ˆ A ˆ y) = ˆ Bϕ 2 (ˆ y) for all ˆ y, then ϕ 1 ˆ M ∼ ϕ 2 with ˆ M = [ˆ A 0 0 ˆ B]. 4. Concatenation: If ψ i ˆ M i ∼ ϕ i with ˆ M i = [ˆ P i ˆ Q i ˆ R i ˆ S i] for i = 1,..., p, then (ψ 1,..., ψ p) ˆ M ′ ∼ (ϕ 1,..., ϕ p) with ˆ M ′ = [diag (ˆ P i) diag (ˆ Q i) diag (ˆ R i) diag (ˆ S i)].

<!-- chunk {"id": "body-0108", "role": "body", "section": "LFT equivalence", "weight": 1.0} -->

When Φ 1 ˆ M ∼ Φ 2 and these oracles are used with algorithms ˆ H 1 and ˆ H 2, respectively, we must have ˆ y 1 = ˆ H 1 ˆ u 1 and ˆ y 2 = ˆ H 2 ˆ u 2. Incorporating this with Definition 11, we can define a natural generalization of equivalence that holds in this setting.

<!-- chunk {"id": "body-0109", "role": "body", "section": "LFT equivalence", "weight": 1.0} -->

Definition 13 (LFT equivalence). Consider ˆ H 1 ⋄ Φ 1 and ˆ H 2 ⋄ Φ 2, where Φ 1 ˆ M ∼ Φ 2. We say the algorithms are LFT-equivalent and write ˆ H 1 ⋄ Φ 1 ˆ M ∼ ˆ H 2 ⋄ Φ 2, if We justify the name 'LFT' in Remark 17 and 'equivalence' in Remark 14.

<!-- chunk {"id": "body-0110", "role": "body", "section": "LFT equivalence", "weight": 1.0} -->

We omit ˆ M and simply write ˆ H 1 ⋄ Φ 1 ∼ ˆ H 2 ⋄ Φ 2 when ˆ M is the same as that for which Φ 1 ˆ M ∼ Φ 2, and therefore clear from context.

<!-- chunk {"id": "body-0111", "role": "body", "section": "LFT equivalence", "weight": 1.0} -->

Remark 14. Linear equivalence Φ 1 ∼ Φ 2 and LFT equivalence ˆ H 1 ⋄ Φ 1 ∼ ˆ H 2 ⋄ Φ 2 satisfy reflexivity and symmetry, and transitivity, so they are equivalence relations.

<!-- chunk {"id": "body-0112", "role": "body", "section": "LFT equivalence", "weight": 1.0} -->

Our main result of this section is an algebraic characterization of LFT equivalence between algorithms defined in Definition 13.

<!-- chunk {"id": "body-0113", "role": "body", "section": "LFT equivalence", "weight": 1.0} -->

Theorem 15 (algebraic characterization of LFT equivalence). Suppose Φ 1 ˆ M ∼ Φ 2. Then ˆ H 1 ⋄ Φ 1 ˆ M ∼ ˆ H 2 ⋄ Φ 2 if and only if Proof. See Appendix B.2.

<!-- chunk {"id": "body-0114", "role": "body", "section": "LFT equivalence", "weight": 1.0} -->

We can apply Theorem 15 to solve for ˆ H 1 in terms of ˆ H 2 or vice versa.

<!-- chunk {"id": "body-0115", "role": "body", "section": "LFT equivalence", "weight": 1.0} -->

Corollary 16. Consider the setting of Theorem 15 with ˆ M = [ˆ P ˆ Q ˆ R ˆ S]. Then we have ˆ H 1 (ˆ R ˆ H 2 + ˆ S) = (ˆ P ˆ H 2 + ˆ Q). In particular, Remark 17. The relationships between ˆ H 1 and ˆ H 2 in Eq. are commonly called linear fractional transformations (LFTs), which is why we chose the name LFT equivalence.

<!-- chunk {"id": "body-0116", "role": "body", "section": "LFT equivalence", "weight": 1.0} -->

The results above can also be derived by direct manipulation of the block diagram as we demonstrated with shift equivalence in Fig. 5. In this case, the manipulation is a bit more involved; see Fig. 6.

<!-- chunk {"id": "body-0117", "role": "body", "section": "LFT equivalence", "weight": 1.0} -->

The dashed box in Fig. 6 represents the equivalent ˆ H 2. Based on the block diagram, we obtain the following algebraic relationships: Fig. 6: Equivalent block diagrams representing LFT equivalence. Starting from the top left, we augment the algorithm and oracle, we transform the oracle using the linear equivalence Φ 1 ˆ M ∼ Φ 2, and finally we isolate the equivalent ˆ H 2 in feedback with Φ 2.

<!-- chunk {"id": "body-0118", "role": "body", "section": "LFT equivalence", "weight": 1.0} -->

These equations can be resolved in various ways. Most relevant for our purpose, we eliminate ˆ y 2 and seek an identity that holds for all ˆ u 2, which leads to: This expression can be further simplified to obtain the relationships in Theorem 15 and Corollary 16.

<!-- chunk {"id": "body-0119", "role": "body", "section": "LFT equivalence", "weight": 1.0} -->

The special cases of Proposition 12 lead to simple expressions for LFT equivalence between algorithms.

<!-- chunk {"id": "body-0120", "role": "body", "section": "LFT equivalence", "weight": 1.0} -->

Corollary 18 (commutation). Suppose ϕ ( ˆ C ˆ y ) = ˆ Cϕ (ˆ y ) for all ˆ y. Then ˆ H 1 ⋄ ϕ ˆ M ∼ ˆ H 2 ⋄ ϕ with ˆ M = [ ˆ C 0 0 ˆ C ]. Consequently, ˆ H 1 = ˆ C ˆ H 2 ˆ C -1. If we let ˆ C = ˆ ∆ m (multi-shift), then we see that shift equivalence is a special case of LFT equivalence.

<!-- chunk {"id": "body-0121", "role": "body", "section": "LFT equivalence", "weight": 1.0} -->

Corollary 19 (equivariance). Suppose ϕ 1 (ˆ A ˆ y) = ˆ Bϕ 2 (ˆ y) for all ˆ y. Then We are also interested in the special case of algorithms ˆ H 1 ⋄ (Ψ, ϕ 1) and ˆ H 2 ⋄ (Ψ, ϕ 2), where Ψ is some set of oracles common to both algorithms, and ϕ 1 ˆ M ∼ ϕ 2 with ˆ M = [ˆ P ˆ Q ˆ R ˆ S] In this case, by concatenation (Proposition 12), we have (Ψ, ϕ 1) ˆ M ′ ∼ (Ψ, ϕ 2). Therefore, we immetiately obtain the following corollary.

<!-- chunk {"id": "body-0122", "role": "body", "section": "LFT equivalence", "weight": 1.0} -->

Corollary 20 (LFT equivalence with common oracles). Suppose ϕ 1 ˆ M ∼ ϕ 2 with ˆ M = [ ˆ P ˆ Q ˆ R ˆ S ]. Let Ψ be another oracle. Then ˆ H 1 ⋄ (Ψ, ϕ 1 ) ˆ M ′ ∼ ˆ H 2 ⋄ (Ψ, ϕ 2 ) with ˆ M ′ defined above, if (see Corollary 16): ˆ H 1 ([ 0 0 0 ˆ R ] ˆ H 2 + [ I 0 0 ˆ S ]) = [ I 0 0 ˆ P ] ˆ H 2 + [ 0 0 0 ˆ Q ].

<!-- chunk {"id": "body-0123", "role": "body", "section": "Efficient determination of LFT equivalence", "weight": 1.0} -->

To determine whether ˆ H 1 ⋄ Φ 1 ∼ ˆ H 2 ⋄ Φ 2, we must first establish how Φ 1 and Φ 2 are related. If there exists some ˆ M such that Φ 1 ˆ M ∼ Φ 2, then we can apply Theorem 15, and we have ˆ H 1 ⋄ Φ 1 ∼ ˆ H 2 ⋄ Φ 2 if [ I -ˆ H 1 ] ˆ M [ ˆ H 2 I ] = 0. For an example of how this result can be used in practice, see the end of Section 8.2.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Efficient determination of LFT equivalence", "weight": 1.0} -->

If there are many different ˆ M matrices that work, say Φ 1 ˆ M ∼ Φ 2 for all ˆ M ∈ M, then it follows from Definition 11 that M is a multiplicative group. Determining equivalence amounts to checking feasiblity of the problem [I -ˆ H 1] ˆ M [ˆ H 2 I] = 0 with ˆ M ∈ M. We saw at the end of Section 7 how to solve this problem for the special case of shift-equivalence (M is the set of multi-shifts). However, we suspect that solving this problem for different M would require a case-by-case analysis.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Proxes, subdifferentials, and their conjugates", "weight": 1.0} -->

We are now ready to return to the motivating examples of Algorithms 8.1-8.4. The oracles { ∂f, ∂f ∗, prox tf, prox 1 t f ∗ } are linearly equivalent to one another. Using the identities at the beginning of Section 8, these relationships can be derived as in Eq.. The associated matrices ˆ M corresponding to Definition 11 are given in Fig. 7.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Proxes, subdifferentials, and their conjugates", "weight": 1.0} -->

Fig. 7: Matrices ˆ M conforming to Definition 11 for all possible linear equivalences between the oracles { ∂f, ∂f ∗, prox tf, prox 1 t f ∗ }.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Proxes, subdifferentials, and their conjugates", "weight": 1.0} -->

Note that the diagonal entries of Fig. 7 are identity LFT matrices (see Proposition 12). Applying Corollary 20 to the matrices in Fig. 7, we can obtain a set of algorithms equivalent when we swap one oracle for another.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Proxes, subdifferentials, and their conjugates", "weight": 1.0} -->

Corollary 21 (LFT equivalence for prox). Suppose ˆ H is an algorithm that uses oracles partitioned as (Ψ, prox tg ). Then, the following transfer functions correspond to LFT-equivalent algorithms.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Proxes, subdifferentials, and their conjugates", "weight": 1.0} -->

Corollary 22 (LFT equivalence for subdifferentials). Suppose ˆ H is an algorithm that uses oracles partitioned as (Ψ, ∂g ). Then, the following transfer functions correspond to LFT-equivalent algorithms.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Proxes, subdifferentials, and their conjugates", "weight": 1.0} -->

Remark 23. If there is no Ψ in Corollaries 21 and 22 (the prox or subdifferential is the only oracle), then we can extract the blocks of all submatrices and we obtain LFT-equivalence among: Remark 24. In Corollary 22, ˆ H 22 must be invertible. We may want to also ensure that ˆ H -1 22 is proper, as this is necessary if we want an implementable algorithm. The condition that a transfer function ˆ H be invertible and proper can be characterized precisely [50, Lem. 3.15]; it is equivalent to requiring that D = lim z →∞ ˆ H (z) is invertible. One possible state-space realization of the inverse transfer function ˆ H -1 is

<!-- chunk {"id": "body-0131", "role": "body", "section": "Algorithms 8.1-8.4", "weight": 1.0} -->

We can verify equivalence of Algorithms 8.1-8.4 by directly applying Corollary 21. Specifically, substituting ˆ H = [ 0 1 z -t 1 z ] in Corollary 21, we immediately obtain the transfer functions in Eq..

<!-- chunk {"id": "body-0132", "role": "body", "section": "Oracle swapping and deletion", "weight": 1.0} -->

Although we did not cover oracle swapping or deletion, both of these notions are trivial to check in our framework. In fact, they are special cases of LFT equivalence.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Oracle swapping and deletion", "weight": 1.0} -->

Most splitting methods are not symmetric with respect to oracle swapping since the different oracles usually have different properties that the algorithm is trying to exploit. Nevertheless, one might be interested, e.g., Davis-Yin splitting where f and g are swapped (see Algorithm 8.6). This is called dual Davis-Yin. Given ˆ H ⋄ Ψ, if Ψ is a permutation of the oracles Φ, then we can write Ψ( Px ) = P Φ( x ), where P is a permutation matrix. By Corollary 19, we have ˆ H ⋄ Ψ = P ⊤ ˆ HP ⋄ Φ, i.e., permute the corresponding rows and columns of the transfer matrix. We exploit this fact later in this section when we show that PD3O is LFT-equivalent to Davis-Yin splitting.

<!-- chunk {"id": "body-0134", "role": "body", "section": "DR and Chambolle-Pock", "weight": 1.0} -->

We can use LFT equivalence to show the relation between Douglas-Rachford (DR), Algorithm 3.5, and the primal-dual optimization method proposed by Chambolle and Pock (Algorithm 8.5 ).

<!-- chunk {"id": "body-0135", "role": "body", "section": "Algo. 8.5", "weight": 1.0} -->

Comparing Algorithm 8.5 and Algorithm 3.5, we should first set τ = σ = 1 so that the oracles correspond properly. Now, computing transfer functions, we have: Applying Corollary 21, we will have LFT-equivalence between these algorithms if Therefore, Algorithms 3.5 and 8.5 are LFT-equivalent if M = I.

<!-- chunk {"id": "body-0136", "role": "body", "section": "More three-operator splitting", "weight": 1.0} -->

An algorithm that has recently attracted considerable attention is the three-operator splitting algorithm of Davis and Yin. This algorithm solves the problem using the oracles prox f, prox g, and ∇ h. The algorithm and its transfer function are given as follows.

<!-- chunk {"id": "body-0137", "role": "body", "section": "More three-operator splitting", "weight": 1.0} -->

Algo. 8.6 Davis-Yin three-operator splitting Suppose we wanted to design an equivalent algorithm that used the oracles (prox tf, prox g ∗, ∇ h) instead. We proceed in steps: Now, compare this algorithm to PD3O (Algorithm 7.1), which is We can see that the algorithms are LFT-equivalent upon setting A = I, τ = t, σ = 1 t. Although this result is known, the benefit of systematizing algorithm equivalence is that these sorts of equivalences can be determined straightforwardly. We can directly verify the equivalence above by applying Theorem 15 with ˆ M = [t 0 t -t] taken from Fig.

<!-- chunk {"id": "body-0138", "role": "body", "section": "One algorithm, many interpretations and implementations", "weight": 1.0} -->

Is it useful to have many different forms of an algorithm, if all the forms are LFTequivalent? Yes: different rewritings of one algorithm often yield different ('physical') intuition. For example, Algorithm 1.1 uses the current loss function for extrapolation; while Algorithm 1.2 seems to extrapolate from the previous loss function. The distributed algorithms Algorithms 6.7 and 6.8, although equivalent, were developed using very different intuition. The former used a gradient differencing scheme whereas the latter used an adapt-correct-combine approach.

<!-- chunk {"id": "body-0139", "role": "body", "section": "One algorithm, many interpretations and implementations", "weight": 1.0} -->

Equivalent algorithms can differ in memory usage, computational efficiency, or numerical stability. For example, implementations of Algorithms 1.3 and 1.4 lead to different memory usage. At each time step k, Algorithm 1.3 needs to store x k +1 2 and F ( x k 2 ), but Algorithm 1.4 only needs to store x k 1 in memory. These different rewritings also naturally yield different generalizations, for example, by projecting different state variables. Likewise, Douglas-Rachford (Algorithm 3.5) only requires storing x k 3 at each time step k, whereas simplified ADMM (Algorithm 3.6) requires storing ξ k 2 and ξ k 3. This is evident from Fig. 3; the dotted lines cross one arrow for Douglas-Rachford and two arrows for ADMM.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Stochastic and randomized algorithms", "weight": 1.0} -->

Our framework applies to stochastic or randomized algorithms with almost no modifications, simply by allowing random oracles. For example, we can accept oracles like random search min i =1,...,k f ( x, ω i ), stochastic gradient ∇ f ( x ) + ω, or noisy gradient ∇ f ( x + ω ). The definition of oracle equivalence requires a slight modification in this setting: for algorithms that use randomized oracles, two algorithms are oracleequivalent if they generate identical sequences of oracle calls when evaluated along the same sample path.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Time-varying algorithms", "weight": 1.0} -->

The linear time-invariant (LTI) algorithm assumption is critical, as the ability to relate the z -transforms of the input and output via multiplication with a transfer function (ˆ y = ˆ H ˆ u ) critically relies on the map ( u 0, u 1,... ) ↦→ ( y 0, y 1,... ) being LTI.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Time-varying algorithms", "weight": 1.0} -->

Nevertheless, many of the other concepts from Section 5 do extend to systems that are time varying. For example, an algorithm with parameters that change on a fixed schedule but is otherwise linear, such as gradient descent with a diminishing stepsize, can be regarded as a linear time-varying (LTV) system, and the notion of a transfer function has been generalized to LTV systems. If, instead, the parameters change adaptively based on the other state variables, the system can be regarded as a linear parameter varying (LPV) system or a switched system. Examples of such algorithms include nonlinear conjugate gradient methods and quasi-Newton methods.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Oracle structure", "weight": 1.0} -->

We assumed throughout this paper that all oracles were nonlinear and time-invariant. If we weaken this assumption, and let the oracles be nonlinear and time-varying, the notion of oracle equivalence is still meaningful: it holds if the two algorithms invoke the same sequence of oracle calls. However, shift equivalence no longer works because time-varying operators do not commute with time shifts.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Oracle structure", "weight": 1.0} -->

If we strengthen the assumption instead, and assume the oracles are endowed with additional structure, then further equivalences are possible. Indeed, every commutation relation satisfied by the oracle leads to a new notion of equivalence!

<!-- chunk {"id": "body-0145", "role": "body", "section": "Oracle structure", "weight": 1.0} -->

For example, an oracle that is linear and time-invariant would commute with any other LTI system (not just multi-shifts). As an example, consider DR (Algorithm 3.5) where f is known to be a quadratic function. In this case, the oracle L = prox f is linear and therefore commutes with any LTI system.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Oracle structure", "weight": 1.0} -->

For example, it commutes with the dynamical system: Assuming x 0 = 0, this dynamical system maps (u 0, u 1,...) ↦→ (y 0, y 1,...), with This transformation clearly commutes with a linear oracle L, because left-multiplying each u k by L and then applying the transformation is the same as applying first and then left-multiplying by L. In other words, Since DR uses oracles (prox f, prox g) and only prox f is assumed to be linear, the special commutation relation only holds for prox f, and we may write So when f is a quadratic function, we have via Corollary 18 that ˆ H 1 ⋄ (prox f, prox g) ∼ ˆ H 2 ⋄ (prox f, prox g) if ˆ H 2 = [1 z -α 0 0 1] -1 ˆ H 1 [1 z -α 0 0 1]. Letting ˆ H 1 = ˆ H 3. 5, we obtain the equivalent algorithm: One possible realization of the new algorithm is given below.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Algo. 9.1 Quadraticf variant of DR", "weight": 1.0} -->

Therefore, Algorithms 3.5 and 9.1 are equivalent for all α when f is a quadratic function, but they cease to be equivalent when we remove this constraint on f. Specific equivalence results that require one of the oracles to be linear can be found, for example, in [58, Theorem 4]. However, the approach presented above is far more general, as it allows one to systematically derive entire families of equivalent algorithms.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Algo. 9.1 Quadraticf variant of DR", "weight": 1.0} -->

Moving beyond linearity, different notions of equivalence could conceivably be developed for other classes of oracles, such as dynamic oracles (oracles with memory), or multi-dimensional oracles that have structure, such as sparsity.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Nonlinear state updates", "weight": 1.0} -->

Our main exposition only considers algorithms defined by state-space equations: a linear map relates ( x k, u k ) to ( x k +1, y k ). However, this assumption can be relaxed: linear state updates is a sufficient condition, but it is not necessary. We only require that the map ( u 0, u 1,... ) ↦→ ( y 0, y 1,... ) be LTI. For example, consider Algorithm 9.2, which is related to ordinary gradient descent (Algorithm 3.4) via a nonlinear state transformation.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Algo. 9.2", "weight": 1.0} -->

for k = 0, 1, 2,... do x k +1 = x k exp(-1 5 ∇ f (log x k)) end for Although the state update equations for Algorithm 9.2 are nonlinear, if we identify the oracle input y k = log x k and the oracle output u k = ∇ f (y k), we can eliminate x k and write the algorithm as y k +1 = y k -1 5 u k, which is a linear system with transfer function -1 5 1 z -1.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Repeated oracles", "weight": 1.0} -->

Some algorithms make multiple calls to the same oracle at each iteration. One such example is the extragradient method, given as Algorithm 9.3, which calls oracles π (a projection) and ϕ (a gradient) twice at each iteration. We can model such algorithms in our framework by treating the repeated oracles as separate oracles. Here, ˆ H 9. 3 assumes the ordering (π 1, π 2, ϕ 1, ϕ 2), where π 1 refers to the first time the projection oracle π is called and similarly for π 2, ϕ 1, ϕ 2. Checking for equivalence therefore means checking for shift equivalence and oracle permutation among the repeated oracles.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Repeated oracles", "weight": 1.0} -->

We can also envision an algorithm that trivially iterates a simpler algorithm multiple times, such as 'double gradient descent', given as Algorithm 9.4 below, which assumes an oracle Φ = (∇ f, ∇ f). In our framework we do not consider Algorithm 9.4 to be equivalent to ordinary gradient descent with stepsize γ, because the oracles have different sizes and there would be a type mismatch if we tried to equate the sequences of oracle calls between the two algorithms.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Computational complexity", "weight": 1.0} -->

Checking for equivalence in our framework is straightforward using a computer algebra system to verify relations between transfer functions, as demonstrated in Section 5. Importantly, the transfer functions that arise here are not arbitrary symbolic expressions; they come from linear state-space representations, so each entry is a rational function of z (see Appendix A.3). Thus, equivalence can be checked entrywise using exact algebra on rational functions, for example by reducing each entry to numerator/denominator form and verifying the resulting polynomial identities, or equivalently by cross-multiplying and checking that the difference is the zero polynomial.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Computational complexity", "weight": 1.0} -->

If an algorithm uses p oracles and has state dimension n, then checking oracle or shift equivalence is polynomial in p and n (see the end of Section 7). Checking LFT equivalence also has similar complexity (see the paragraph before Section 8.1) provided the number of ˆ M matrices to check is fixed or polynomial in p. That being said, as far as we know, all algorithms have n ≤ 3 and p ≤ 3, so computational complexity is not a difficulty in practice.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Beyond optimization algorithms", "weight": 1.0} -->

The ideas in this paper are not limited to optimization algorithms, but can be applied to any iterative algorithm involving oracle evaluations and linear updates. For example, algorithms for solving monotone inclusions, variational inequalities, fixed point problems, or equilibrium computation can all be represented as linear dynamical systems in feedback with oracles. Other examples include algorithms for numerical linear algebra (linear systems of equations, least squares, eigenvalue problems) and algorithms for solving differential equations (linear multistep methods, Runge-Kutta methods).

<!-- chunk {"id": "body-0156", "role": "body", "section": "Software implementation", "weight": 1.0} -->

We implemented our framework as a web-based application called Linnaeus 7, available at software/. The user input is a proposed algorithm described using natural syntax, and the output is a list of all algorithms in the library that are equivalent to the input algorithm, along with the parameter settings that make them equivalent and pointers to relevant literature. Linnaeus can reproduce all equivalence results mentioned in this paper. The software is open source and we welcome contributions to the library of algorithms and equivalence results.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our work presents first steps towards systematizing the study of optimization algorithms. When viewed as dynamical systems and characterized in terms of their input-output maps, algorithms are distilled to their essential function: a causal map that produces the next oracle input based on past oracle outputs.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Looking forward, control theory is well-positioned to advance the fields of algorithm discovery, analysis, and design. Control theory is concerned with the analysis and synthesis of dynamical systems with the goal of obtaining desirable overall behavior, such as stability or robustness to noise. In particular, tools from robust control have been used to analyze and design optimization algorithms with optimized convergence rates or noise-robustness properties, for example.

<!-- chunk {"id": "body-0159", "role": "body", "section": "Conclusion", "weight": 1.5} -->

7 Named after Carl Linnaeus, creator of the modern system for naming organisms.
