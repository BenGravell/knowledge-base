<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Stochastic Linear Optimization under Bandit Feedback

Topics include Linear bandits, Bandit feedback, Stochastic optimization, Upper confidence bounds, Regret bounds, Online learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Establishes near-matching regret upper and lower bounds for stochastic linear bandits. It analyzes confidence-bound algorithms, including an efficiently implementable variant for polytopal decision sets, and extends the results to changing feasible sets.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In the classical stochastic k-armed bandit problem, in each of a sequence of T rounds, a decision maker chooses one of k arms and incurs a cost chosen from an unknown distribution associated with that arm. The goal is to minimize regret, defined as the difference between the cost incurred by the algorithm and the optimal cost. In the linear optimization version of this problem (first considered by Auer ), we view the arms as vectors in R^n, and require that the costs be linear functions of the chosen vector. As before, it is assumed that the cost functions are sampled independently from an unknown distribution. In this setting, the goal is to find algorithms whose running time and regret behave well as functions of the number of rounds T and the dimensionality n (rather than the number of arms, k, which may be exponential in n or even infinite). We give a nearly complete characterization of this problem in terms of both upper and lower bounds for the regret. In certain special cases (such as when the decision region is a polytope), the regret is polylog(T).

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In general though, the optimal regret is Θ*(√T) — our lower bounds rule out the possibility of obtaining polylog(T) rates in general. We present two variants of an algorithm based on the idea of “upper confidence bounds.” The first, due to Auer, but not fully analyzed, obtains regret whose dependence on n and T are both essentially optimal, but which may be computationally intractable when the decision set is a polytope. The second version can be efficiently implemented when the decision set is a polytope (given as an intersection of half-spaces), but gives up a factor of √n in the regret bound. Our results also extend to the setting where the set of allowed decisions may change over time.
