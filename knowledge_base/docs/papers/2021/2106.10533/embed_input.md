<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning to Reach, Swim, Walk and Fly in One Trial: Data-Driven Control with Scarce Data and Side Information

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We develop a learning-based control algorithm for unknown dynamical systems under very severe data limitations. Specifically, the algorithm has access to streaming and noisy data only from a single and ongoing trial. It accomplishes such performance by effectively leveraging various forms of side information on the dynamics to reduce the sample complexity. Such side information typically comes from elementary laws of physics and qualitative properties of the system. More precisely, the algorithm approximately solves an optimal control problem encoding the system's desired behavior. To this end, it constructs and iteratively refines a data-driven differential inclusion that contains the unknown vector field of the dynamics. The differential inclusion, used in an interval Taylor-based method, enables to over-approximate the set of states the system may reach. Theoretically, we establish a bound on the suboptimality of the approximate solution with respect to the optimal control with known dynamics. We show that the longer the trial or the more side information is available, the tighter the bound. Empirically, experiments in a high-fidelity F-16 aircraft simulator and MuJoCo's environments illustrate that, despite the scarcity of data, the algorithm can provide performance comparable to reinforcement learning algorithms trained over millions of environment interactions.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Besides, we show that the algorithm outperforms existing techniques combining system identification and model predictive control.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Learning how to achieve a complex task has found numerous applications ranging from robotics to fluid dynamics. However, learning algorithms generally suffer from high sample complexity, often requiring millions of samples to achieve the desired performance. Such data requirements limit the practicability of learning algorithms in real-world scenarios where an excessive number of trials cannot be performed on a physical system. A rather extreme example of such a scenario is an aircraft trying to retain a certain degree of control after abrupt changes in its dynamics, e.g., due to the loss of an engine. In such a scenario, there is a need to learn the dynamics after the abrupt changes using data from only the current trajectory.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Wedevelop a learning-based control algorithm that utilizes data from a single trial and leverages side information on the unknown dynamics to reduce the sample complexity. The data include finitely many noisy samples of the states, the states' derivatives, and the control signals applied. Under such a severe limitation on the amount of available data, learning can be performed efficiently only by incorporating already known invariant properties of the dynamical system. We refer to such extra knowledge as side information. The side information, typically derived from elementary laws of physics, may be a priori knowledge of the regularity of the dynamics, monotonicity or bounds on the vector field, algebraic constraints on the states, or knowledge of parts of the vector field.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The developed algorithm, using the data and side information available to it, computes an over-approximation of the set of states the system may reach. Then, it incorporates such an overapproximation into a constrained short-horizon optimal control problem, which is solved on the fly.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Specifically, it leverages a data-driven differential inclusion to compute over-approximations of the reachable sets of the system. It first constructs a differential inclusion that contains the unknown vector field. Next, it builds on set contractor programming to refine the differential inclusion as more data become available. Then, it computes over-approximations of the reachable sets of all dynamics described by the differential inclusion through an interval Taylorbased method that can enforce constraints from the side information to reduce the width of the over-approximations.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The obtained over-approximations enable to formulate the data-driven optimal control problem as a nonconvex and uncertain optimization problem. Specifically, we encode the control task as a sequential optimization of a cost function over a time horizon. Even for convex cost functions, the control problem is typically nonconvex. Besides, the predictions of the states' values at future times cannot be computed due to the unknown dynamics. The developed algorithm leverages the obtained over-approximations to optimize the nonconvex problem under the uncertain states' predictions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The algorithm computes approximate solutions to the nonconvex optimization problem through convex relaxations. We develop a sequential convex optimization scheme that uses the obtained over-approximation and iteratively linearizes its nonconvex constraint around the previous iteration solution. Thus, each iteration solves a convex optimization problem, and we leverage trust regions to account for the potential errors due to the linearization.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Theoretically, we establish a bound on the suboptimality of the approximate solution with respect to the optimal control solution in the case where the dynamics were known. The bound is proportional to the width of the obtained over-approximations. We show that the longer the trial or the more the side information available, the tighter the over-approximations. Thus, the algorithm achieves near-optimal control as more data streams or more side information is available.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Empirically, through a series of simulation examples, we show that the algorithm can provide performance comparable to reinforcement learning (RL) algorithms, such as D4PG and SAC, while outperforming the system identification technique with model predictive control SINDYc. We train SAC and D4PG over millions of environment interactions before comparing to our approach. We emphasize that if we had made fair comparisons, i.e., the baselines RL algorithms were also trained using streaming data from only the ongoing and single episode, the developed algorithm would have achieved significantly higher performance than any of these baselines since they cannot learn with such constraints on the amount of data. Specifically, in several control tasks from MuJoCo, we provide promising and comparative results to D4PG and SAC. Further, in a ground collision avoidance scenario of an F-16 aircraft, we show that the algorithm outperforms SINDYc and the tuned F-16's linear-quadratic regulator controller.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Related Work. In our prior work, we described a data-driven algorithm similar to the algorithm developed in this paper. However, the algorithm works only for control-affine dynamics. Further, most of the considered side information is not tailored for robotics systems, and only one-step optimal control problems were investigated. In contrast, the algorithm in this paper is applicable for a more general class of dynamics with polynomial dependency in control. We also evaluate the developed algorithm on highly-complex systems and consider a larger set of side information, e.g., algebraic constraints on states and unknown terms. Besides, we investigate short-horizon rather than one-step optimal control problems.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Several approaches for data-driven control combine model predictive control with system identification or data-driven reachable set estimation. These approaches achieve system identification through sparse regression over a library of nonlinear functions, regression over the set of polynomials of fixed degree with physics-based side information, spectral properties of the collected data, Koopman theory, or Gaussian processes. The approaches achieve data-driven estimation of the reachable sets of partially unknown dynamics using either supervised learning or Gaussian processes. They provide only probabilistic guarantees of the correctness of the computed reachable sets while our algorithm computes correct over-approximations. Recent work and DeePC have proposed data-driven control techniques based on the behavioral systems theory foundation, which bypass the system identification step. These techniques mostly assume linear time-invariant dynamical systems and are extremely performant in such a setting. Except for Ahmadi and El Khadir that considers limited side information and builds on computationally expensive semidefinite programs solvers, none of the above approaches (in their current form) can exploit the side information in this paper.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Besides, through extensive comparisons with SINDYc, DeePC, and Gaussian-based approaches, Djeumou et al. empirically demonstrates that: (a) For simple systems such as a unicycle, these techniques achieve significant lower performance (computation time and control suboptimality) than an approach that can exploit side information; (b) These techniques struggle to learn on high-dimensional and complex systems (e.g., quadrotor). Thus, this paper compares against RL techniques even though they work in a drastically different regime of data.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Model-free and model-based RL algorithms have been widely used for data-driven control of complex systems. Model-free algorithms can achieve high performance at the expense of high sample complexity while model-based algorithms are more data-efficient but are conservative and generally achieve lower performance than model free approaches. In contrast, our algorithm can work with data from only the system's current trajectory, and increases the data efficiency through side informationon the dynamics.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

This paper considers nonlinear dynamics with polynomial dependency in the control inputs as where d ∈ N, α p ∈ N m is known, the state x: R + ↦→ X is a continuous-time signal evolving in X ∈ IR n, u [α p] = u α p 1 1 · · · u α p m m is a monomial with variables from the control signal u: R + ↦→U where U ∈ IR m. The vector-valued functions f = [f k]: R n ↦→ R n and g p = [g p,k]: R n ↦→ R n are considered to be nonlinear and unknown. Note that even if the dynamics are not in the class above, Taylor expansion provides a tight approximation of the dynamics that lies in such a class.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Assumption 1 (LIPSCHITZ SYSTEMS) Given a set A ⊆ R n, f k and g p,k admit local Lipschitz constants L w f k, L w g p,k > 0 on A, for some w ∈ R n + and for all k ∈ N [1,n ], p ∈ N [1,d ].

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Assumption 1 is common in the framework of optimal control. We emphasize that even though we use the weighted norm to define the Lipschitz constants, the results of this paper can be straightforwardly extended to general modulus of continuity assumption on f and g p. The weighted norm has the advantage of providing information on the relative importance of each variable in the function.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Besides, the domain X ∈ IR n is bounded. Thus, by Assumption 1, f k and g p,k admit global Lipschitz constants on X. We exploit such a knowledge by assuming known upper bounds on the Lipschitz constants. That is, we have access to ¯ L f k ∈ R + and ¯ L g p,k ∈ R + as known upper bounds on the Lipschitz constants L w f k and L w g p,k, respectively, for k ∈ N [1,n ] and p ∈ N [1,d ]. We emphasize that the Lipschitz bounds can be directly estimated from data at the expense of weakening some of the guarantees in this paper. Our numerical experiments use Lipschitz bounds estimated from data.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

In a discrete-time setting, we denote the initial time by t 1 ≥ 0 and the current time by t j > t 1 for some j > 1. Let T j = { (˜ x i, ˜ ˙ x i, u i ) } j -1 i =1 be the finite-length set of observations obtained between t 1 and t j. The dataset T j contains j -1 noisy samples of the exact state x i = x ( t i ), the derivative ˙ x i = ˙ x ( t i ) of the state, and the applied input u i = u ( t i ). We build on the widely-used bounded noise assumption and consider that | x ( t ) -˜ x ( t ) | ≤ η, | ˙ x ( t ) -˜ ˙ x ( t ) | ≤ ¯ η for all t ∈ R + and for some vector values η, ¯ η ∈ R n +. Here the absolute value and the comparison are conducted elementwise.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We seek to control the unknown dynamical system by finding u j,..., u j + N ∈ U that are solutions of the N -step optimal control problem where N is the planning horizon, c is a known cost function, x j = x (t j) is the known current state of the system, t q = t j + (q -j)∆ t, ∆ t is a constant time step, and x q +1 = x (t q +1; x q, u q) is the state at t q +1, i.e., a solution of the differential equation at t q +1 when x q is the initial state and u q is the constant control applied between [t q, t q +1]. The optimization problem is generally nonconvex since the state at t q +1 is nonconvex due to the nonlinear dynamics. Besides, x q +1 cannot be computed due to the unknown dynamics.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Problem 1 Given the dataset T j, the current state ˜ x j, compute an approximate solution to the N -step optimal control problem and characterize the suboptimality of such approximation.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Reachable Set Over-Approximation via Data-Based Differential Inclusions", "weight": 1.0} -->

In this section, we first construct a differential inclusion ˙ x ∈ f ( x ) + ∑ d p =1 g p ( x ) u [ α p ] that contains the unknown vector field. Then, we adapt an interval Taylor-based method to over-approximate the reachable set of dynamics described by the constructed differential inclusion. Finally, we show how additional side information constrains the Taylor expansion to provide tighter over-approximations.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Reachable Set Over-Approximation via Data-Based Differential Inclusions", "weight": 1.0} -->

Lemma 1 (OVER-APPROXIMATION OF f AND g p ) Let the set E j = { (˜ x i, C F i, C G i ) } j -1 i =0 be such that C F i = [ C F i k ] ∈ IR n and C G i = [ C G i p,k ] ∈ IR d × n satisfy f k (˜ x i ) ∈ C F i k and g p,k (˜ x i ) ∈ C G i p,k for all p ∈ N [1,d ] and k ∈ N [1,n ].

<!-- chunk {"id": "body-0025", "role": "body", "section": "Reachable Set Over-Approximation via Data-Based Differential Inclusions", "weight": 1.0} -->

Then, the interval-valued functions f = [ f k ]: IR n → IR n and g p = [ g p,k ]: IR n → IR n, defined by f k ( A ) = ⋂ (˜ x i,C F i, · ) ∈ E j C F i k + f k η w ( A -˜ x i ) and g p,k ( A ) = ⋂ (˜ x i, ·,C G i ) ∈ E j C G i p,k + g p,k η w ( A -˜ x i ), are such that R ( f k, A ) ⊆ f k ( A ) and R ( g p,k, A ) ⊆ g p,k ( A ) for all A ⊆ X. Furthermore, the function η w: IR n ↦→ IR can be any straightforward interval extension of the weighted norm || · || w.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Reachable Set Over-Approximation via Data-Based Differential Inclusions", "weight": 1.0} -->

We provide a proof of the lemma and an expression for η w in the extended version of the paper. Intuitively, Lemma 1 states that if a set E j = { (˜ x i, C F i, C G i ) } j -1 i =0 is known, it is possible to obtain an analytic formula to over-approximate the unknown f and g p via the Lipschitz bounds. Lemma 2 enables to compute the set E j based on the data T j.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Reachable Set Over-Approximation via Data-Based Differential Inclusions", "weight": 1.0} -->

Lemma 2 (REFINEMENT VIA CONTRACTOR) Given a data point (˜ x i, ˜ ˙ x i, u i) ∈ T j, an interval F i = [F i k] ∈ IR n such that f (˜ x i) ∈ F i, and an interval G i = [G i p,k] ∈ IR d × n such that g p,k (˜ x i) ∈ G i p,k for all p ∈ N [1,d], k ∈ N [1,n]. Let the intervals C F i ∈ IR n and C G i ∈ IR d × n defined by for successive values of k ∈ N [1,n] and for all p ∈ N [1,d] with ˜ N i k = [˜ ˙ x i -¯ η, ˜ ˙ x i +¯ η]. Then, C F i and C G i are the smallest intervals enclosing f (˜ x i) and g p (˜ x i), given only the data (˜ x i, ˜ ˙ x i, u i), F i, G i.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Reachable Set Over-Approximation via Data-Based Differential Inclusions", "weight": 1.0} -->

Algorithm 1 Construct: Compute E j required to over-approximate f and g p at each data point of a given trajectory.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Reachable Set Over-Approximation via Data-Based Differential Inclusions", "weight": 1.0} -->

Input: Dataset T j and a parameter M > 0. Output: E j = { (˜ x i, C F i, C G i ) } j -1 i =0.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Reachable Set Over-Approximation via Data-Based Differential Inclusions", "weight": 1.0} -->

Algorithm 2 Refine: Update E j with data.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Reachable Set Over-Approximation via Data-Based Differential Inclusions", "weight": 1.0} -->

Input: A point (˜ x j, ˜ ˙ x j, u j ), E j containing past over-approximations, T j, and the noise bound ¯ η.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Reachable Set Over-Approximation via Data-Based Differential Inclusions", "weight": 1.0} -->

- 1: Compute F j = f (˜ x j), G j = [g p,k (˜ x j)] via Lemma 1 and E j - 2: Compute C F j, C G j via Lemma 2 The proof of the lemma is provided in the extended version of the paper. Lemma 2 provides tighter sets C F i ⊆ F i and C G i ⊆ G i that prune out from F i and G i some values f (˜ x i) and g p (˜ x i) that do not satisfy the dynamics constraint ˙ x i = f (x i)+ ∑ d p =1 g p (x i) u i [α p].

<!-- chunk {"id": "body-0033", "role": "body", "section": "Reachable Set Over-Approximation via Data-Based Differential Inclusions", "weight": 1.0} -->

Theorem 1 (DATA-DRIVEN DIFFERENTIAL INCLUSION) Given a dataset T j, the bounds f k and g p,k, it holds that the unknown vector field of the dynamics satisfies where f and g p are obtained from Lemma 1 with E j taken as the output of Algorithm 1.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Reachable Set Over-Approximation via Data-Based Differential Inclusions", "weight": 1.0} -->

Remark 1 (PERSISTENT EXCITATION) The quality of the differential inclusion depends on how much information on f and g p can be obtained from the dataset T j. This is the classical observability problem, sometimes referred to as persistent excitation. Thus, the learning algorithm should sometimes take suboptimal actions through persistent excitations of the system.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Reachable Set Over-Approximation via Data-Based Differential Inclusions", "weight": 1.0} -->

Finally, we compute over-approximations of the reachable sets of all dynamics described by the differential inclusion. Theorem 2 provides a closed-form expression for such a set.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Reachable Set Over-Approximation via Data-Based Differential Inclusions", "weight": 1.0} -->

Theorem 2 (DATA-DRIVEN REACHABLE SET OVER-APPROXIMATION) Given the dataset T j, a constant control signal u: t ↦→ u q on the interval [t q, t q +1] with u q ∈ U, and the uncertain set R q ∈ IR n of states x q at time t q. Then, a closed-form expression for R q +1 ⊇ { x (t q +1; u q, x q) ∈ X| x q ∈ R q }, which over-approximates the reachable set at t q +1 for all x q ∈ R q, is given by where the matrices J f = [J f k,l] ∈ IR n × n and J g p = [J g p k,l] ∈ IR n × n, over-approximations of the Jacobian of f and g p, are such that J f k,l = w k f k and J g p k,l = w k g p,k for all p ∈ N [1,d] and k, l ∈ N [1,n].

<!-- chunk {"id": "body-0037", "role": "body", "section": "Reachable Set Over-Approximation via Data-Based Differential Inclusions", "weight": 1.0} -->

Further, the set P q, a rough enclosure of { x (t q +1; u q, x q) ∈ X| x q ∈ R q }, is a solution of the fixpoint equation R q + [0, ∆ t] h (P q, u q) ⊆ P q.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Reachable Set Over-Approximation via Data-Based Differential Inclusions", "weight": 1.0} -->

We provide the proof of Theorem 2 in the extended paper. It merges the differential inclusion with an interval Taylor-based expansion of order 2 to obtain the result.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Reachable Set Over-Approximation via Data-Based Differential Inclusions", "weight": 1.0} -->

Theorem 2, as it is, does not incorporate side information other the regularity assumption. We describe in the following how to incorporate a-priori knowledge to tighten R q +1 given.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Reachable Set Over-Approximation via Data-Based Differential Inclusions", "weight": 1.0} -->

Side information 1 (PARTIAL DYNAMICS KNOWLEDGE) The vector field of contains both known and unknown terms. That is, ˙ x = ∑ S s =1 f s ( x ) · f s ( x )+ ∑ d p =1 ∑ S s =1 g s p ( x ) · g s p ( x ) u [ α p ], where · denotes the elementwise product between vectors or matrices, f s and g s p ( x ) are known functions, and f s, g s p are unknown functions satisfying Assumption 1.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Reachable Set Over-Approximation via Data-Based Differential Inclusions", "weight": 1.0} -->

Given E s j containing past over-approximations of f s, g s p and a new data point (˜ x j, ˜ ˙ x j, u j ), the refinement (Algorithm 2) is adapted to compute in line 1 over-approximations f s (˜ x j ) and g s p (˜ x j ) via Lemma 1 and E s j. Then, line 2 is modified such that each f s (˜ x j ) and g s p (˜ x j ) are contracted according to the new dynamics' constraint ˙ x j = ∑ S s =1 f s ( x j ) · f s ( x j ) + ∑ d p =1 ∑ S s =1 g s p ( x j ) · g s p ( x j ) u j [ α p ]. The contracted sets can be obtained straightforwardly by slight changes in the scheme described by Lemma 2 or by calling an algorithm such as HC4-Revise.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Reachable Set Over-Approximation via Data-Based Differential Inclusions", "weight": 1.0} -->

Thus, the new differential inclusion is given by h ( x, u ) = ∑ S s =1 f s ( x ) · f s ( x ) + ∑ d p =1 ∑ S s =1 g s p ( x ) · g s p ( x ) u [ α p ], where f s and g s are interval extensions of known f s and g s p. Furthermore, we compute the new Jacobian terms J f and J g p used in R q +1 by applying chain rules and exploiting the Lipschitz bounds.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Reachable Set Over-Approximation via Data-Based Differential Inclusions", "weight": 1.0} -->

Side information 2 (ALGEBRAIC CONSTRAINTS) We are given a constraint r ( ˙ x ( · ), x ( · )) ≥ 0 where r is a differential map. Such a constraint typically derives from conservation laws of physics.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Reachable Set Over-Approximation via Data-Based Differential Inclusions", "weight": 1.0} -->

Without loss of generality, we consider that r: R n × R n ↦→ R. This side information provides tighter over-approximations on f, g p, J f, and J g p locally. Specifically, this constraint can be formulated as the new constraint w ( f ( x ), [ g p,k ( x )], u, x ) ≥ 0. In some cases, another constraint z ( f ( x ), [ g p,k ( x )], ∂f ∂x ( x ), [ ∂g p,k ∂x ( x )], u, x ) ≥ 0 can be derived by differentiating w. The new constraints w and z can be incorporated in the computation of R q +1 through contractors. More specifically, the refinement algorithm and the interval extensions of the Jacobian can be improved by additionally contracting with respect to the constraints w and z. Thus, such side information enables to obtain a tighter R q +1. We develop on more side information in the extended paper.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Approximate Optimal Control", "weight": 1.0} -->

In this section, we develop an algorithm that computes approximate solutions to the optimal control problem using over-approximations of the reachable sets. Further, we characterize the suboptimality of the approximate solutions with respect to the case of known dynamics.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Approximate Optimal Control", "weight": 1.0} -->

The nonconvexity in the optimal control problem is due to the possibly nonconvex cost function c and the nonconvex constraint x q +1 = x ( t q +1; x q, u q ). We replace such an expression by x q +1 = ˆ h θ ( x q, u q ) ∈ R q +1, where the function ˆ h θ, parameterized with θ ∈ R n, is a trajectory picked inside R q +1. For example, a straightforward choice can be ˆ h θ ( x q, u q ) = θ R q +1 + (1 -θ ) R q +1, for θ ∈ n. Then, we solve the nonconvex problem by sequentially linearizing x q +1 and the cost function c around the solution of the s th iteration. This results into a convex subproblem that is solved to full optimality. The obtained solutions are then used at the ( s +1) th iteration.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Approximate Optimal Control", "weight": 1.0} -->

Linearization. Let x = [x j +1;...; x j + N +1] ∈ R nN and u = [u j;...; u j + N] ∈ R mN. We denote the solutions of the s th iteration by x s = [x j +1,s;...; x j + N +1,s] and u s = [u j,s;...; x j + N,s]. Then, we can approximate the gradient of h θ (or x (t q +1; x q, u q)) around x s, u s as follows: where I is the identity matrix of appropriate dimensions. The jacobian J f (x q,s), J g p (x q,s) are exactly J f and J g p when no extra side information are given. With side information, the matrices are computed through chain rules as described in side information 1. Note that since we neglect the term in ∆ t 2, A q,s and B q,s are approximations of the actual range of the gradients of h θ.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Approximate Optimal Control", "weight": 1.0} -->

Next, we define the variables ∆x = x -x s, ∆x q = x q -x q,s, ∆u = u -u s, and ∆u q = u q -u q,s in terms of the unknown solutions of the current iteration x and u. Thus, at the (s +1) th iteration, the first-order approximation of x q +1 = ˆ h θ (x q, u q) around the previous solution (x q,s, u q,s) is where v = [v j;...; v j + N] are penalty variables that enable the linearization to be always feasible.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Approximate Optimal Control", "weight": 1.0} -->

Further, to ensure that the variable v q is used only when necessary, we augment the cost function with the sufficiently large penalization weight λ > 0. Thus, the solution for the (s +1) th iteration, optimizes the penalized and linearized cost given by L s (∆x, ∆u) = ∑ j + N (c (x q,s, u q,s, x q +1,s) + ∇ c (x q,s, u q,s, x q +1,s)[∆x; ∆u]) + λ ∑ q = j ‖ v q ‖, where we also linearize the possibly nonconvex function c given that ∇ c is its gradient, and ‖ · ‖ can be either the infinity norm or 1 -norm. In order to verify the linearization accuracy, we also define the nonlinear realized cost J (x, u) = ∑ j + N q = j c (x q, u q, x q +1) + λ ∑ j + N q = j ‖ x q +1 -h θ (x q, u q) ‖.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Approximate Optimal Control", "weight": 1.0} -->

Trust region constraints and linearized problem. Weimpose the trust region constraint ‖ ∆u ‖ ≤ r s to ensure that u does not deviate significantly from the control input u s obtained in the previous iteration, where r s will be updated at each iteration so that the x remains close to x s. This update rule enables to keep the solutions within the region where the linearization is accurate. As a consequence, each iteration of our algorithm solves the following linear optimization problem: The optimal solution of the linearized problem is either accepted and used in the next iteration or rejected until convergence. When the linearization is considered accurate, i.e., the realized cost J and linearized cost L s are similar, the solution is accepted and the trust region is expanded. Otherwise, the solution is rejected and the trust region is contracted.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Approximate Optimal Control", "weight": 1.0} -->

Theorem 3 (SUBOPTIMALITY BOUND) Assume that L c with the 2 -norm is the Lipschitz constant of the cost c on X × U × X. Let C ⋆ j and ˆ C j be the optimal costs of the N -step control problem when the dynamics are known, e.g. x q +1 = x ( ·, x q, u q ) is known, and the dynamics are unknown, e.g., x q +1 = h θ ( x q, u q ) ∈ R q +1. Then, | C ∗ j -C j | ≤ L c ( ‖ wd( R j + N +1 U ) ‖ 2 + ∑ j + N q = j +1 2 ‖ wd( R q U ) ‖ 2 ) holds with wd( A ) = A-A being the width of the interval A. The interval R q +1 U is the over-approximation of the reachable set at time index t q +1 from the initial uncertain set R q U (with R j U = ˜ x j ) and for all u q ∈ U.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Approximate Optimal Control", "weight": 1.0} -->

Theorem 3 provides that the suboptimality bound is proportional to the width of the overapproximation of the reachable set. Thus, our algorithm achieves near-optimal control with more data along the trajectory and more side information, as the over-approximations become tighter.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In this section, we empirically demonstrate that the algorithm, using data from only the current trial and the least amount of side information necessary to learn, can achieve performance comparable to the highly-tuned implementations of D4PG and SAC trained over ten million of interactions with the environments. We emphasize that the comparison is unfair to our algorithm since, at each evaluating episode, it learns from only the thousand data obtained during the episode. Further, we show in an F-16 aircraft simulator, a 13 -states and 4 -control inputs nonlinear dynamics with polynomial control, that (a) The algorithm outperforms system identification approaches such as SINDYc; (b) The algorithm can meet real-time requirements. We provide further details on the numerical experiments in the extended paper. A video of the simulations is, and the code.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Experiments in MuJoCo. The equations of motion for multi-joint dynamical systems in the MuJoCo environment are as follows: M ( q )¨ q + b ( ˙ q, q ) = h ( u ) + J T c ( q ) F c ( ˙ q, q, u ), where q is the system's state, M ( q ) is the inertial matrix, b ( ˙ q, q ) contains coriolis, centrifugal, gravitational and passive forces, J T c ( q ) is the contact Jacobian matrix, and F c ( ˙ q, q, u ) is the contact force.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

For each environment, the cost function is provided by MuJoCo, and we perform numeric differentiation in order to find its gradient. The Lipschitz bounds are under-estimated using only 1000 data points obtained prior to the on-the-fly control. The Reacher environment does not consider any side information other than the Lipschitz bounds, while Swimmer and Cheetah consider that M ( q ) is known (Side information 1) in order to start learning. Indeed, without such side information, our algorithm fails to learn to control due to the large over-approximations of reachable sets. M ( q ) is typically obtained for a robot through Euler-Lagrange formulation that uses the kinetic and potential energy. Further, we reduce the over-approximation of the contact force F c by considering the Coulomb law of friction. That is, via Side information 2, we impose the constraints F 1 c ≥ 0 and F 1 c ≥ √ ( F 2 c ) 2 µ 1 +( F 3 c ) 2 µ 2 at each contact point, where F 1 c is the normal force value, F 2 c and F 3 c are the tangential forces, and µ 1, µ 2 are the friction coefficients.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Data-driven control of an F-16 aircraft. We consider a scenario involving an F-16 aircraft diving towards the ground at a low altitude and a high downward pitch angle. We show how our algorithm can prevent a ground collision using only the measurements obtained during the dive and elementary laws of physics as side information. We compare our algorithm with the linear-quadratic regulator (LQR) of the simulator, a pre-trained neural network for the task, and SINDYc achieving sparse system identification from a library of functions.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Our algorithm considers the structural knowledge of rigid-body dynamics while assuming that the aerodynamics forces and moments are completely unknown. In other words, the effect of the control inputs on the aircraft is unknown. For example, from the first principles, the lateral velocity's derivative is given by rv -qw -g sin θ + F u /m, where the structure is generic but the aerodynamic force F u (specific to the aircraft) is unknown. We use the library PySINDY for the comparison with system identification. We considered monomials (up to degree 6), sines and cosines of the state, and the products of these func- Figure 3: Our algorithm enables the F-16 to avoid the ground collision while the embedded LQR controller and SINDYc fail to avoid the crash. Further, it can be applied in real time since the compute time is less than the control time step enforced by the simulator. tions with the control inputs as the library functions. We provide the noisy measurements of the state and its derivatives to both SINDYc and our algorithm. Our algorithm uses Lipschitz bounds estimated using 1000 data points. Finally, the neural network baseline was trained via policy optimization.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Figure 3 empirically demonstrates the effectiveness of the proposed approach.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper develops a learning-based, data-efficient control algorithm for unknown systems using streaming data from an ongoing trial and available side information. The experiments demonstrate that it is possible, with data from a single episode and side information, to perform comparably to learning algorithms trained over millions of environment interactions. Further, we empirically show that the algorithm is fast and can be used in a scenario with real-time constraints.
