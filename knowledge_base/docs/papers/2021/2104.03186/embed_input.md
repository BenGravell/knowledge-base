<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Temporal Parallelization of Dynamic Programming and Linear Quadratic Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This article proposes a general formulation for temporal parallelization of dynamic programming for optimal control problems. We derive the elements and associative operators to be able to use parallel scans to solve these problems with logarithmic time complexity rather than linear time complexity. We apply this methodology to problems with finite state and control spaces, linear quadratic tracking control problems, and to a class of nonlinear control problems. The computational benefits of the parallel methods are demonstrated via numerical simulations run on a graphics processing unit.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

O PTIMAL control theory (see, e.g., -) is concerned with designing control signals to steer a system such that a given cost function is minimised, or equivalently, a performance measure is maximised. The system can be, for example, an airplane or autonomous vehicle which is steered to follow a given trajectory, an inventory system, a chemical reaction, or a mobile robot, -.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Dynamic programming, in the form first introduced by Bellman 1950's, is a general method for determining feedback laws for optimal control and other sequential decision problems, -, and it also forms the basis of reinforcement learning, which is a subfield of machine learning. The classic dynamic programming algorithm is a sequential procedure that proceeds backwards from the final time step to the initial time step, and determines the value (cost-to-go) function as well as the optimal control law in time complexity of O ( T ), where T is the number of time steps. The algorithm is optimal in the sense that no sequential algorithm that processes all the T time steps can have a time-complexity less than O ( T ).

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

However, the complexity O ( T ) is only optimal in a computer with one single-core central processing unit (CPU). Nowadays, even general-purpose computers typically have multi-core CPUs with tens of cores and higher-end computers can have hundreds of them. Furthermore, graphics processing units (GPUs) have become common accessories of generalpurpose computers and current high-end GPUs can have tens of thousands of computational cores that can be used to parallelise computations and lower the time-complexity.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

S. S¨ arkk¨ a is with the Department of Electrical Engineering and Automation, Aalto University, 02150 Espoo, Finland (email: simo.sarkka@aalto.fi).

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

A. F. Garc´ ıa-Fern´ andez is with the Department of Electrical Engineering and Electronics, University of Liverpool, Liverpool L69 3GJ, United Kingdom, and also with the ARIES Research Centre, Universidad Antonio de Nebrija, Madrid, Spain (email: angel.garciafernandez@liverpool.ac.uk).

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Dynamic programming algorithms that parallelise computations at each time step, but operate sequentially, are provided, for discrete states, and in for the Riccati recursion in linear quadratic problems. Another approach to speed up computations for model predictive control (MPC) in linear quadratic problems is partial condensing which is based on splitting the problem into temporal blocks and eliminating the intermediate states algebraically. The required block-conversion can be done in parallel and the resulting modified linear quadratic problem can be solved using parallel methods such as. However, the complexity of the resulting algorithm is still linear in time.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The previous dynamic programming algorithms have linear time-complexity O ( T ), but there are some approaches in literature to lower this complexity by using parallelisation across time. One idea applied in the context of an allocation process can be found in [9, Sec. I.30], where the time interval is divided into two, and the two problems are solved in parallel. Various forms of parallel algorithms for dynamic programming with discrete states are given. Reference presents a partitioned dynamic programming suitable for parallelisation for linear quadratic control problems, though it has the disadvantage that some required inverse matrices may not exist. An iterated method for linear quadratic control problems, with constraints, in which each step can be parallelised is proposed, though it requires positive definite matrices in the cost function and may require regularisation. An algorithm to approximately solve an optimal control problem by solving different subproblems with partially overlapping time windows is provided, and an approximate parallel algorithm for linear MPC is given. Reference provides combination rules to separate the dynamic programming algorithm into different subproblems across the temporal domain. These combination rules are the foundation for temporal parallelisation.

<!-- chunk {"id": "body-0010", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The main contribution of this paper is to present a parallel formulation of dynamic programming that is exact and has a time complexity O (log T ). None of the previous works achieve these two aspects simultaneously. The central idea is to reformulate dynamic programming in terms of associative operators, which enable the use of parallel scan algorithms, to parallelise the algorithm. The resulting algorithm has a span-complexity of O (log T ), which translates into a time-complexity of O (log T ) with a large enough number of computational cores. The algorithm can therefore speed up the computations significantly for long time horizons.

<!-- chunk {"id": "body-0011", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

In this paper, we first provide the general formulation to parallelise dynamic programming by defining conditional value functions between two different time steps and combining them via the rule. We also show how to obtain the optimal control laws and resulting trajectories making use of parallel computation. Then, we explain how this general methodology can be directly applied to problems with finite state and control spaces. The second contribution of this paper is to specialise the methodology to linear quadratic optimal control problems, that is, to linear quadratic trackers (LQTs). The parallel LQT formulation is not straightforward, as it requires the propagation of the dual function associated with the conditional value function to avoid numerical problems. Our third contribution is to extend the parallel LQT algorithm to approximately solve certain nonlinear control problems by iterated linearisations, as. Finally, we have implemented these algorithms in TensorFlow, which enables parallel computations on GPUs, to experimentally show that the parallel algorithms provide a significant speedup also in practice.

<!-- chunk {"id": "body-0012", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The present approach is closely related to the temporal parallelisation of Bayesian smoothers and hidden Markov model inference recently considered in -. These approaches use a similar scan-algorithm-based parallelisation in the context of state-estimation problems. The combination rule is also related to so-called max-plus algebras for dynamic programming which have been considered, for example, in -.

<!-- chunk {"id": "body-0013", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The structure of the paper is the following. In Section II we provide a brief background on dynamic programming and parallel computing, in Section III we provide the parallel methods to general and finite-state problems, in Section IV we consider the parallel solution to LQT problems, in Section V, we discuss some practical implementation aspects and computational complexity, in Section VI we experimentally illustrate the performance of the methods on a GPU platform, and finally we conclude the article in Section VII.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Deterministic control problem", "weight": 1.0} -->

We consider a deterministic control problem that consists of a difference equation and a cost function of the form where, for k = S,..., T, x k is the state (typically x k ∈ R n x), f k (·) is the function that models the state dynamics at time step k, u S: T -1 = (u S,..., u T -1) is the control/decision sequence (typically u k ∈ R n u with n u ≤ n x), and ℓ k (·) is a lower bounded function that indicates the cost at time step k. The initial state x S is known. The aim is now to find a feedback control law or policy u k (x k) such that if at step k the state is x k, the cost function C [u S: T -1] for the steps from S to T is minimized with the sequence u S (x S),..., u T (x T).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Deterministic control problem", "weight": 1.0} -->

In Bellman's dynamic programming the idea is to form a cost-to-go or value function V k (x k) which gives the cost of the trajectory when we follow the optimal decisions for the remaining steps up to T starting from state x k. It can be shown that the value function admits the recursion with V T (x T) = ℓ T (x T), which determines the optimal control law via Given the control law for all time steps, we can compute the optimal trajectory from time steps S + 1 to T, which is denoted as (x ∗ S +1,..., x ∗ T), by an additional forward pass starting at x ∗ S = x S and

<!-- chunk {"id": "body-0016", "role": "body", "section": "Linear quadratic tracker", "weight": 1.0} -->

The LQT problem is the solution to a linear quadratic control problem of the form for n = S,..., T -1. We assume that X n and U n are symmetric matrices such that X n ≥ 0, U n > 0.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Linear quadratic tracker", "weight": 1.0} -->

In this setting, the objective is that a linear combination of the states H k x k follows a reference trajectory r k from time step S to T. The linear quadratic regulator is a special case of the LQT problem by setting r k = 0, c k = 0, and H k = I ∀ k.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Linear quadratic tracker", "weight": 1.0} -->

In this case, the value function is where v k is an n x × 1 vector and S k is an n x × n x symmetric matrix and, throughout the paper, we use z to denote an undetermined constant that does not affect the calculations. The parameters v k and S k can be obtained recursively backwards. Starting with v T = H ⊤ T X T r N and S T = H ⊤ T X T H T, we obtain The optimal control law is The optimal trajectory resulting from applying the optimal control law can be computed with an additional forward pass starting at x S and with control law.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Linear quadratic tracker", "weight": 1.0} -->

It should be noted that the derivation of LQT in does not include time-varying matrices or parameter c k in the problem formulation, but it is straightforward to include these. It is also possible to use the LQT solution as a basis for approximate non-linear control by linearizing the system along a nominal trajectory (see and Sec. IV-D.3).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Associative operators and parallel computing", "weight": 1.0} -->

Parallel computing (see, e.g. ) refers to programming and algorithm design methods that take the availability of multiple computational cores into account. When some parts of the problem can be solved independently, then those parts can be solved in parallel to reduce the computational time. The more parts we can solve in parallel, the more speed-up we get.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Associative operators and parallel computing", "weight": 1.0} -->

Sequential problems which at first glance do not seem to be parallelisable can often be parallelised using so called parallel scan or all-prefix-sums algorithms,. Given a sequence of elements a 1,..., a T and an associative operator ⊗ defined on them, such as summation, multiplication, or minimisation, the parallel scan algorithm computes the allprefix-sums operation which returns the values s 1,..., s T such that in O (log T) time. The key aspect is that because the operator ⊗ is associative, we can rearrange the computations in various ways which generate independent sub-problems, for example, and, by a suitable combination of the partial solutions, we can obtain the result in O (log T) parallel steps. The specific combination requires an up-sweep and a down-sweep on a binary tree of computations. A pseudocode is given in Algorithm 1. Clearly, the prefix sums can also be computed in parallel in the backward direction (a 1 ⊗···⊗ a T,..., a T -1 ⊗ a T, a T).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Associative operators and parallel computing", "weight": 1.0} -->

It should be noted that while parallel scans significantly lower the wall-clock time to compute all-prefix-sums, they have the drawback that the number of total computations is higher than in the sequential algorithm. This implies that they require higher energy, which may not be suitable for small-scale mobile systems.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Associative operators and parallel computing", "weight": 1.0} -->

Algorithm 1 Parallel-scan algorithm. The algorithm in this form assumes that T is a power of 2, but it can easily be generalized to an arbitrary T.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Associative operators and parallel computing", "weight": 1.0} -->

Input: The elements a k for k = 1,..., T and an associative operator ⊗.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Associative operators and parallel computing", "weight": 1.0} -->

Output: The all prefix sums are returned in a k for k =

<!-- chunk {"id": "body-0026", "role": "body", "section": "PARALLEL OPTIMAL CONTROL", "weight": 1.0} -->

In this section, we start by defining conditional value functions and their combination rules (Section III-A) and then we use them to define the associative operators and elements for parallelisation (Section III-B). We also derive the parallel solution of the resulting optimal trajectory (Section III-C), and finally, we discuss the case where the state space and controls take values in finite sets (Section III-D).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Conditional value functions and combination rules", "weight": 1.0} -->

In this section, we present the conditional value functions and their combination rules, which are required to design the parallel algorithms.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Conditional value functions and combination rules", "weight": 1.0} -->

Definition 1 (Conditional value function): The conditional value function V k → i (x k, x i) is the cost of the optimal trajectory starting from x k and ending at x i, that is If there is no path connecting x k and x i, then the constraint cannot be met and V k → i (x k, x i) = ∞.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Conditional value functions and combination rules", "weight": 1.0} -->

The combination rule for conditional value functions is provided in the following theorem.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Conditional value functions and combination rules", "weight": 1.0} -->

Theorem 2: The recursions for the value functions and conditional value functions can be written as Proof: See Appendix I.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Conditional value functions and combination rules", "weight": 1.0} -->

As part of the minimisation, we also get the minimizing state x i. Due to the principle of optimality, this value is the state at time step i that is on the optimal trajectory from x k until time T. Similarly, the argument of minimisation x j in is part of the optimal trajectory from x k to x i.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Associative operator for value functions", "weight": 1.0} -->

The associative element a of the parallel scan algorithm is defined to be a conditional value function V a (·, ·): R n x × R n x → R such that The combination rule for two elements a = V a (x, y) and b = V b (x, y) is then given as follows.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Associative operator for value functions", "weight": 1.0} -->

Definition 3: Given elements a and b of the form, the binary associative operator for dynamic programming is This operator is an associative operator because min operation is associative. This is summarized in the following lemma.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Associative operator for value functions", "weight": 1.0} -->

Lemma 4: The operator in Definition 3 is associative.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Associative operator for value functions", "weight": 1.0} -->

Proof: For three elements a, b, and c, we have which shows that (a ⊗ b) ⊗ c = a ⊗ (b ⊗ c).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Associative operator for value functions", "weight": 1.0} -->

The elements and combination rule allows us to construct the conditional and conventional value functions as follows.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Associative operator for value functions", "weight": 1.0} -->

Theorem 5: If we initialize the elements a k for k = S,..., T as Proof: Equation results from the sequential application of forward, and from the sequential application backwards.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Associative operator for value functions", "weight": 1.0} -->

Theorem 5 implies that we can compute all value functions V k ( · ) by initializing the elements as, using the associative operator in Definition 3 and computing for k = S,..., T -1, which corresponds to a (reverted) all-prefixsum operation. Because the initialisation is fully parallelisable, we can directly use the parallel scan algorithm (see Algorithm 1) to compute all value functions in O (log T ) parallel steps.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Associative operator for value functions", "weight": 1.0} -->

Remark 6: After computing all the value functions, we can obtain all the control laws u k ( x k ) for k = S, · · ·, T -1 by using. This operation can be done in parallel for each k.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Associative operator for value functions", "weight": 1.0} -->

Remark 7: If we are interested in evaluating V S → k ( x S, x k ) at a given x S, as we are in trajectory recovery, then instead of first using with initialisation, and then evaluating the result at x S, we can also initialise an extra element

<!-- chunk {"id": "body-0041", "role": "body", "section": "Optimal trajectory recovery", "weight": 1.0} -->

Once we have obtained the optimal control laws in parallel, we can compute the resulting optimal trajectory (x ∗ S +1,..., x ∗ T) in parallel using two methods. 1) Method 1: In the first method for trajectory recovery, the state of the optimal trajectory at time step k can be computed by using and the composition of functions We can compute using parallel scans as follows. The associative element a is defined to be a function on x, a = f a (·) and the operator is the function composition in the following definition.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Optimal trajectory recovery", "weight": 1.0} -->

Definition 8: Given elements a = f a (·) and b = f b (·), the binary associative operator for optimal trajectory recovery is where ◦ denotes the composition of two functions, which is an associative operator. We should note that the order of the function composition is reverted.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Optimal trajectory recovery", "weight": 1.0} -->

Then, we can recover the optimal trajectory via the following lemma.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Optimal trajectory recovery", "weight": 1.0} -->

Lemma 9: If we initialize element a S as the function f ∗ S (·), which is given, evaluated at x S and, for k = S +1,..., T -1, a k is initialised as the function where x ∗ k is the state of the optimal trajectory at time step k. 2) Method 2: An alternative method, which resembles the max-product algorithm in probabilistic graphical models, is based on noticing that, from the definition of the conditional value function and the value function, the state of the optimal trajectory at time step k is given by where we recall that x S is the initial known state. That is, we can just minimise the sum of the forward conditional value function V S → k (x S, x k) and the (backwards) value function V k (x k), which can be calculated using parallel scans via and, respectively. Then, the minimisation can be done for each node in parallel.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Optimal trajectory recovery", "weight": 1.0} -->

It should be noted that both approaches for optimal trajectory recovery require two parallel scans, one forward and one backwards, and one minimisation for each node.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Finite state and control spaces", "weight": 1.0} -->

The case in which the state and the control input belong to finite state spaces is important as we can solve the control problem in both sequential and parallel forms in closed-form. Let x k ∈ { 1,..., D x } and u k ∈ { 1,..., D u } where D x and D u are natural numbers. Then, f k ( x k, u k ) and ℓ n ( x n, u n ) can be represented by matrices of dimensions D x × D u, V k ( x k ) by a vector of dimension D x, u k ( x k ) by a vector of dimension D x, and V k → i ( x k, x i ) by a matrix of size D x × D x. Due to the finite state space, the required minimisations in and, can be performed by exhaustive search, which can also be parallelised.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Finite state and control spaces", "weight": 1.0} -->

For Method 1 for optimal trajectory recovery, the function f ∗ k ( · ) can be represented as a vector of dimension D x, and the function composition in can be performed by evaluating all cases.

<!-- chunk {"id": "body-0048", "role": "body", "section": "PARALLEL LINEAR QUADRATIC TRACKER", "weight": 1.0} -->

In this section, we provide the parallel solution to the LQT case. In Section IV-A, we derive the conditional value functions and combination rules. In Section IV-B, we derive the associative elements to obtain the value functions V S → k ( x S, x k ) and V k ( x k ). In Section IV-C, we address the computation of the optimal trajectory. Finally, in Section IV-D, we discuss extensions to stochastic and non-linear problems.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Conditional value functions and combination rules", "weight": 1.0} -->

For the LQT problem, V k → i (x k, x i) in is a quadratic program with affine equality constraints that we represent by its dual problem where λ is a Lagrange multiplier n x × 1 vector and the dual function g k → i (·, ·, ·) has the parameterisation If C k,i is invertible, one can solve by calculating the gradient of with respect to λ and setting it equal to zero, to obtain In this case, we can also interpret the conditional value function in terms of conditional Gaussian distributions as where N(·; x, P) denotes a Gaussian density with mean x and covariance matrix P, and N I (·; η, J) denotes a Gaussian density parameterised in information form with information vector η and information matrix J. A Gaussian distribution with mean x and covariance matrix P can be written in its information form as η = P -1 x and J = P -1.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conditional value functions and combination rules", "weight": 1.0} -->

Nevertheless, in general, C k,i is not invertible so it is suitable to keep the dual function parameterisation.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conditional value functions and combination rules", "weight": 1.0} -->

Lemma 10: Given two elements V k → j (x k, x j) and V j → i (x j, x i) of the form, their combination V k → i (x k, x i), which is obtained using Theorem 2, is of the form and characterised by where I is an identity matrix of size n x.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conditional value functions and combination rules", "weight": 1.0} -->

The proof is provided in Appendix I-B. It should be noted that the combination rule is equivalent to the combination rule for the parallel linear and Gaussian filter, which also considers Gaussian densities of the form [27, Lem. 8].

<!-- chunk {"id": "body-0053", "role": "body", "section": "Associative elements to obtain the value functions", "weight": 1.0} -->

The following lemma establishes how to define the elements of the parallel scan algorithms to obtain the value functions V S → k ( x S, x k ) and V k ( x k ).

<!-- chunk {"id": "body-0054", "role": "body", "section": "Associative elements to obtain the value functions", "weight": 1.0} -->

Lemma 11: If we initialize the elements a k for k = S,..., T as: Furthermore, V k (x k) is of the form with Once we obtain v k +1 and S k +1 using Lemma 11, we can compute the optimal control u k using.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Associative elements to obtain the value functions", "weight": 1.0} -->

Remark 12: If we are interested in evaluating the conditional value functions V S → k ( x S, x k ) for a given x S, then we can also directly initialise by

<!-- chunk {"id": "body-0056", "role": "body", "section": "Optimal trajectory recovery", "weight": 1.0} -->

We proceed to explain how the two optimal trajectory recovery methods explained in Section III-C work for the LQT problem. 1) Method 1: Plugging the optimal control law into the dynamic equation, the optimal trajectory function in becomes We denote a conditional optimal trajectory from time step k to i as Lemma 13: Given two elements f ∗ k → j (x k, x j) and f ∗ j → i (x j, x i) of the form, their combination f ∗ k → i (x k, x i), given by Definition 8, is a function f ∗ k → i (x k, x i) of the form with Proof: The proof of this lemma is direct by using function compositions.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Optimal trajectory recovery", "weight": 1.0} -->

How to recover the optimal trajectory using parallel scans is indicated in the following lemma.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Optimal trajectory recovery", "weight": 1.0} -->

Lemma 14: If we initialise the elements of the parallel scan as a k = f ∗ k → k +1 (x k), with for k ∈ { S +1,..., T -1 }, and, for k = S, we set ˜ F S,S +1 = 0 and ˜ c S,S +1 = ˜ F S x S + ˜ c S, then, where x ∗ k is the state of the optimal trajectory at time step k. 2) Method 2: This method makes use of to recover the optimal trajectory. It first runs a forward pass to compute V S → k (x S, x k) and then a backward pass to compute V k (x k). Then, the optimal trajectory is obtained via the following lemma.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Optimal trajectory recovery", "weight": 1.0} -->

Lemma 15: Given V k ( x k ) of the form and V S → k ( x S, x k ) of the form, the state of the optimal trajectory at time step k, which is obtained using, is

<!-- chunk {"id": "body-0060", "role": "body", "section": "Extensions", "weight": 1.0} -->

In this section, the aim is to discuss some straightforward extensions of the parallel LQT. 1) Extension to stochastic control: Although the extension of the general framework introduced in this article to stochastic control problems is hard, the stochastic LQT case follows easily. Stochastic LQT is concerned with models of the form where ℓ T (x T) and ℓ n (x n) are as given, and w k is a zero mean white noise process with covariance Q k, G k is a given matrix, and E[·] denotes expectation over the state trajectory. It turns out that due to certainty equivalence property of linear stochastic control problems the optimal control is still given by and the solution exactly matches the deterministic solution, that is, it is independent of Q k and G k. The optimal value functions both in deterministic and stochastic cases have the form, but the value of the (irrelevant) constant is different.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Extensions", "weight": 1.0} -->

It also results from the certainty equivalence property that the optimal control solution to the partially observed linear (affine) stochastic control problem with function and dynamic and measurement models where y k is a measurement, O k is a measurement model matrix, d k is a deterministic bias, and e k is a zero mean Gaussian measurement noise, is given, where the state x k is replaced with its Kalman filter estimate.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Extensions", "weight": 1.0} -->

- 2) Extension to more general cost functions: Sometimes (such as in the nonlinear case below) we are interested in generalising the cost function in to the following form for n < T: We can now transform into the form using the factorisation we get a system of the form. This system can then be solved for (x n, ˜ u n), and the final control signal can be recovered via 3) Extension to nonlinear control: The equations for solving the LQT problem can be extended to approximately solve nonlinear LQT systems by performing iterated linearisations, as. Let us consider a system of the form where f k (·), g n (·) and h n (·) are possibly nonlinear functions. Given a nominal trajectory ¯ x k, ¯ u k for k ∈ S,..., T, we can linearise the nonlinear functions using first-order Taylor series as where J x f k represents the Jacobian of function f k (·) evaluated at ¯ x k, ¯ u k with respect to variable x.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Extensions", "weight": 1.0} -->

Starting with a nominal trajectory ¯ x 1 k, ¯ u 1 k for k ∈ S,..., T, we linearise the system using, obtain the value functions using parallel scans (see Lemma 11), and obtain a new optimal trajectory ¯ x 2 k and control ¯ u 2 k. Then, we can repeat this procedure of linearisation and optimal trajectory/control computation until convergence. The procedure may be initialised, for example, with ¯ x 1 k = 0, ¯ u 1 k = 0 or ¯ x 1 k = x S, ¯ u 1 k = 0 ∀ k.

<!-- chunk {"id": "body-0064", "role": "body", "section": "IMPLEMENTATION AND COMPUTATIONAL COMPLEXITY", "weight": 1.0} -->

In this section, we first discuss the practical implementation of the methods in Section V-A. We then analyse the computational complexity in Section V-B. Finally, we explain how to perform parallelisation in blocks in Section V-C.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Practical implementation of parallel control", "weight": 1.0} -->

Given the associative operators and the elements, the solutions to the dynamic programming and trajectory prediction problems reduce to an initialisation step followed by a single call to a parallel scan algorithm routine parameterised by these operators and elements. Given the result of the scan, there can also be a result-extraction step which computes the final optimal control from the scan results.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Practical implementation of parallel control", "weight": 1.0} -->

- 1) Initialisation: Compute the elements A k,k +1, b k,k +1, C k,k +1, η k,k +1, and J k,k +1 defined in Lemma 11 for all k in parallel. - 2) Parallel scan: Call the backward parallel scan routine and, as its arguments, give the initialised elements above along with pointer to the operator in Lemma 10. This returns V k (x k) for all k, see and. - 3) Extraction: Compute the optimal control using in parallel for all k.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Practical implementation of parallel control", "weight": 1.0} -->

The control law for a finite-state control problem is initialised with the conditional value functions in Theorem 5 and the parallel scan routine is given a pointer to the operator in Definition 3. The control law computation is finally done with using the value functions computed in parallel.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Practical implementation of parallel control", "weight": 1.0} -->

Sometimes, we also need to compute the actual trajectory and the corresponding optimal controls forward in time. For example, in iterative non-linear extensions of LQT discussed in Section IV-D.3 we need to linearise the trajectory with respect to the optimal trajectory and control obtained at the previous iteration. In this case, after computing the control laws, we need to do another computational pass.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Practical implementation of parallel control", "weight": 1.0} -->

- 1) Initialisation: Compute the elements ˜ F k,k +1 and ˜ c k,k +1 using Lemma 14 for all k in parallel.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Practical implementation of parallel control", "weight": 1.0} -->

- 2) Parallel scan: Call the forward parallel scan routine and, as its arguments, give the initialised elements above along with pointer to the operator given in Lemma 13. - 3) Extraction: The optimal trajectory can be extracted from the forward scan results as the elements ˜ c S,k, see Lemma 14.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Practical implementation of parallel control", "weight": 1.0} -->

The steps for Method 1 in the finite-state case are analogous, but the elements are initialised according to Lemma 9 and the combination operator is given in Definition 8.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Practical implementation of parallel control", "weight": 1.0} -->

When using Method 2 for optimal trajectory recovery, the operator is the same as in the backward computation for the control law. The parallel scan is done in the forward direction and the final results still need to be evaluated at x S unless initialisation is done using Remark 12. Furthermore, after computing the backward and forward scans, we still need to compute the optimal states by using, which in the case of LQT reduces to

<!-- chunk {"id": "body-0073", "role": "body", "section": "Computational complexity", "weight": 1.0} -->

We proceed to analyse the computational complexity of the proposed methods. For this purpose it is useful to assume that the computer that we have operates according to the PRAM (parallel random access machine) model of computation (see, e.g. ). In this model, we assume that we have a bounded number P of identical processors controller by a common clock with a read/write access to a shared random access memory. This model is quite accurate for multi-core CPUs and GPUs.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Computational complexity", "weight": 1.0} -->

The combination rule computations can also be parallelised, and their complexity will therefore depend on whether they are parallelised or not. For example, if we do not parallelise the computations in the LQT combination rule given in Lemma 10, then their complexity is O ( n 3 x ) due to the matrix inverses (or equivalent LU-factorisations) involved. If we perform the parallelisation, these LU-factorisations can be performed in parallel in O ( n x ) span time. The following analysis is based on assuming that we in fact use parallel matrix routines to implement the operations at the combination steps, along with all the other steps.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Computational complexity", "weight": 1.0} -->

For the parallel algorithms we obtain the following results. Lemma 16: In a PRAM computer with large enough number of processors ( P → ∞ ) and the finite-state control problem, the span time complexity of

<!-- chunk {"id": "body-0076", "role": "body", "section": "Computational complexity", "weight": 1.0} -->

- computing value functions and the control law is O (log D u +(log T) (log D x)); - recovering the trajectory is O (log T) with Method 1, and O (log D u +log D x +(log T) (log D x)) with Method 2.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Computational complexity", "weight": 1.0} -->

Proof: The initialisation of the value function computation is done using which has a time (span) complexity of O (log D u ) due to the minimisation operation over the control input. The associative operator in Definition 3 is fully parallelisable in summation, but the span complexity of the minimisation over the state is O (log D x ). The control law computation also has the complexity O (log D u ) and hence the total span complexity follows. For trajectory recovery with Method 1, we notice that each of the steps of initialisation and associative operator application are fully parallelisable. In Method 2, the initialisation and value function computation have the same complexity as in the backward value function computation and the minimisation at the final combination step takes O (log D x ) time.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Computational complexity", "weight": 1.0} -->

Lemma 17: In a PRAM computer with large enough number of processors ( P → ∞ ) and the LQT problem, the span time complexity of

<!-- chunk {"id": "body-0079", "role": "body", "section": "Computational complexity", "weight": 1.0} -->

- computing value functions and the control law is O (n u + n x log T); - recovering the trajectory is O (log n u +(log T) (log n x)) with Method 1, and O (n x + n x log T) with Method 2.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Computational complexity", "weight": 1.0} -->

Proof: A product of n × n matrices can be computed in parallel in O (log n ) time, and an n × n LU factorisation can be computed in parallel in O ( n ) time. Hence the initialisation requires O ( n u ) time as the contribution of the matrix products is negligible. The time complexity of the associative operator is dominated by the LU factorisations which take O ( n x ) time and the matrix factorisations at the control law computation can be performed in O ( n u ) time. The matrix products required in initialisation have negligible effect and therefore, the total complexity follows. In trajectory recovery Method 1, the matrix products at the initialisation can be computed in O (log n u ) time and the associative operators in O (log n x ) time. In Method 2, the initialisation is again negligible, and associative operations take O ( n x ) time, and the final combination O ( n x ) time.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Computational complexity", "weight": 1.0} -->

It should be noted that, according to Lemmas 16 and 17, Method 1 is computationally more efficient than Method 2 for large D u or large D x in the discrete case, and for large n x and n u in the LQT case. Nevertheless, a benefit of Method 2 is that it can be run in parallel with the backward pass.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Computational complexity", "weight": 1.0} -->

Although the above analysis results give a guideline for performance in large number of processors (computational cores), with finite number of processors, we can expect worse performance as we cannot allocate a single task to single processor. However, at the time of writing the typical number of cores in a GPU was already ∼ 10k, and therefore the above analysis can be expected to become more and more accurate in the future with the steadily increasing number of computational cores.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Block processing", "weight": 1.0} -->

Up to now, we have considered parallelisation of control problems at a single time step level. That is, we initialise the element a k for all k using and then apply the parallel scan algorithm. Another option is to apply the parallel scan algorithm to non-overlapping blocks of B time steps. That is, we can initialise the elements of the parallel scan with V k → k + B for k = S + nB, with n = 0, 1,..., T /B -1. The initialisation of each element can be done using in B -1 sequential steps. Then, we can apply the parallel scan algorithm to fuse the information from all blocks. In this case, the time-complexity in a PRAM computer with large enough number of processors is O ( B +log( N/B )), so it is optimal to choose B = 1. Nevertheless, this approach can be useful if we have a limited number of processors.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Block processing", "weight": 1.0} -->

In the case of LQT, an efficient implementation of the above can achieved by using partial condensing where the idea is to reformulate the problem in terms of blocks of states and controls of size B: By elimination of the state variables inside each block, we can reformulate the problem in terms of the initial states of blocks only, x 0, x B, x 2 B,..., which reduces the state dimensions from full state blocks to the original state dimension. The resulting problem is still a LQT problem, but with modified states and inputs, and hence we can use the proposed parallel LQT algorithms to solve it.

<!-- chunk {"id": "body-0085", "role": "body", "section": "EXPERIMENTAL RESULTS", "weight": 1.0} -->

In this section, we experimentally evaluate the performance of the methods in simulated applications. We implemented the methods using the open-source TensorFlow 2.6 software library using its Python 3.8 interface, which provides means to run parallel vectorised operations and parallel associative scans on GPUs. The experiments were run using NVIDIA A100-SXM GPU with 80GB of memory. In the experiments, we concentrate on the computational speed benefits because the sequential and parallel version of the algorithm compute exactly the same solution (provided that it is unique), the only difference being in the computational speed. The computation speeds were measured by averaging over 10 runs and the time taken to (jit) compile the code was not included in the measurement.

<!-- chunk {"id": "body-0086", "role": "body", "section": "EXPERIMENTAL RESULTS", "weight": 1.0} -->

We would like to point out that, as we are using TensorFlow with GPUs, the matrix operations on the individual time steps of the sequential algorithms are parallelised. Therefore, the sequential LQT algorithms can be interpreted as a TensorFlow parallel implementation of the Riccati recursion.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Experiment with basic LQT", "weight": 1.0} -->

The aim of the experiment is to demonstrate the benefit of the proposed parallelization method over the classical sequential solution in an LQT problem. We consider a 2-D tracking problem obeying Newton's law [2, Example 4.4.2]. In this LQT problem, the aim is to steer an object to follow a given trajectory of reference points in 2-D by using applied forces as the control signals.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Experiment with basic LQT", "weight": 1.0} -->

Fig. 1. Simulated trajectory from the linear control problem and optimal trajectory produced by LQT (see Section VI-A). The trajectory starts.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Experiment with basic LQT", "weight": 1.0} -->

The state consists of the positions and velocities x = [p x p y v x v y] ⊤ and the control signal u = [a x a y] ⊤ contains the accelerations (forces divided by the mass which is unity in our case). If we assume that the control signal is kept fixed over each discretisation interval [t k, t k +1], then the dynamic model can be written as and ∆ t k = t k +1 -t k is the sampling interval. Fig. 1 illustrates the scenario.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Experiment with basic LQT", "weight": 1.0} -->

The dynamic trajectory is discretized so that we add 10 intermediate steps between each of the reference point time steps which then results in a total of T times steps (giving ∆ t k = 0. 1). The cost function parameters are for k = 0,..., T -1 selected to be where c k = 100 when there is a reference point at step k and 10 -6 otherwise. At the final step we set H T = I 4 × 4 and X T = I 4 × 4. The reference trajectory contains the actual reference points at every 10th step k, and the intermediate steps are set equal to the previous reference point. At the final step the reference velocity is also zero. Together with the value c k = 10 -6 at these intermediate points this results in tiny regularisation of the intermediate paths, but the effect on the final result is practically negligible. It would also be possible to put c k = 0 for the intermediate steps to yield almost the same result.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Experiment with basic LQT", "weight": 1.0} -->

Fig. 2. LQT control law computation run times on GPU. The sequential and parallel run times are shown in the top left figure, and a zoom to the parallel run time is shown in the top right figure. The speed-up provided by the parallelisation is shown in figure at the bottom.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Experiment with basic LQT", "weight": 1.0} -->

Fig. 3. The GPU run times (left) and zoomed run times of the parallel methods (right) for combined control law computation and trajectory recovery (Methods 1 & 2) in LQT.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Experiment with basic LQT", "weight": 1.0} -->

The results computing the control law (i.e, the backward pass) of the classic sequential LQT and the proposed parallel LQT on the GPU for T = 10 2,..., 10 5 are shown in Fig. 2. The figure shows the run times of both in log-log scale on the top right figure and the parallel result up to 10 4 is shown in linear scale on the top right. The speed-up, computed as the ratio of sequential and parallel run times, is shown in the bottom figure. It can be seen that the parallel version is significantly faster than the sequential version (illustrated in the top left figure) and the logarithmic scaling of the parallel algorithm can also be seen (illustrated in the top right figure). The speed-up (illustrated in the bottom figure) is of the order of ∼ 470 with 10 5 time points and although it is close to saturating, it still increases a bit.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Experiment with basic LQT", "weight": 1.0} -->

We also ran the combined control law computation pass and the trajectory recovery pass on GPU, and the results are shown in Fig. 3. The advantage of parallel version over the sequential version can again be clearly seen. Furthermore, in this case, Method 1 for the parallel trajectory recovery is faster than Method 2.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Experiment with partial condensing", "weight": 1.0} -->

In this experiment we compare the proposed parallelisation method for LQT to partial condensing, based parallelisation. We also demonstrate how parallel condensing can be combined with the proposed methodology to yield improved results. The same 2-D tracking problem and data are used as in Sec. VI-A.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Experiment with partial condensing", "weight": 1.0} -->

Fig. 4. Result of partial condensing with different values of block size B when the LQT is implemented by using parallel matrix operations within sequential Riccati solution and trajectory reconstruction.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Experiment with partial condensing", "weight": 1.0} -->

Fig. 5. Run times of partial condensing for T = 10 5 with different values of block size B when the LQT is implemented by using parallel matrix operations within sequential Riccati solution and trajectory reconstruction.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Experiment with partial condensing", "weight": 1.0} -->

As discussed in Sec. V-C, the idea of partial condensing is to reduce a control problem of length T to a control problem of length T/B by dividing the problem into blocks of length B. In each of these blocks we can eliminate all but the state at the beginning of the block, which effectively reduces a control problem with state dimension n x, input dimension Bn u, and length T/B. The required computations are 1) conversion of the model into block form, 2) computation of LQT solution of length T/B, and 3) reconstruction of the intermediate states in each block. Partial condensing allows for parallelisation of the computations because steps 1) and 3) are fully parallelisable and step 2) can be efficiently implemented by using parallel matrix operations within the sequential Riccati solution and trajectory reconstruction -.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Experiment with partial condensing", "weight": 1.0} -->

The GPU run times of the aforementioned parallel condensing method with B = 2, 4, 8,..., 256 are shown Fig. 4. The run times of the classical backward-forward sequential LQT solution for trajectory recovery and of the proposed parallel method with trajectory recovery with Method 1 are also shown in the figure. The trajectory lengths were T = 10 2,..., 10 5. It can be seen that the run times of partial condensing methods are significantly lower than of the classical sequential LQT while still, for the most of the cases, higher than of the proposed parallel method. It can be seen that with short trajectory lengths the partial condensing method is faster than the proposed parallel method when B = 16 or 32. However, with larger trajectory lengths the proposed parallel method is faster.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Experiment with partial condensing", "weight": 1.0} -->

Fig. 6. Result of partial condensing with different values of N c when the LQT is implemented by using the proposed parallel methods.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Experiment with partial condensing", "weight": 1.0} -->

In the results of Fig. 4 we can see some evidence of an effect that when increasing B, the run time no longer decreases after a certain value. This is confirmed in Fig. 5 which shows the run times of the partial condensing over trajectory of length T = 10 5 with different values of B. It can be seen that the run time attains minimum somewhere around B = 200 and after that the run time starts to increase.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Experiment with partial condensing", "weight": 1.0} -->

Fig. 7. Run times of partial condensing for T = 10 5 with different values of B when the LQT is implemented by using the proposed parallel methods.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Experiment with partial condensing", "weight": 1.0} -->

As discussed in Sec. V-C, it is also possible to combine partial condensing with the proposed parallelization methodology. This can be done by implementing the LQT solution (of length T/B ) by using one of the parallel methods. Fig. 6 shows the results of using this combined approach. It can be seen that the partial condensing can be used to improve run time of the proposed parallel methods when B is in suitable range (2-64 in this case). When B is too large ( 128 or 256 ), then partial condensing no longer improves the run times. This also happens with B = 64 when the trajectory length is short. Fig. 7 shows the run times with T = 10 5 as function of B. It can be seen in the figure that the minimum run time is attained roughly at value B = 15.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Experiment with partial condensing", "weight": 1.0} -->

Fig. 8. Illustration of the mass-spring-damper problem (see Section VI-C).

<!-- chunk {"id": "body-0105", "role": "body", "section": "Experiment with increasing state dimensionality", "weight": 1.0} -->

In this experiment the aim is to test the scaling of run time when the dimensionality of the state increases. For this purpose, we use a slight modification of a mass-spring-damper problem [43, Section 2.5.3], where we have removed the control constraints, as we do not consider them in this paper. This is a linear model for controlling a chain of N masses m = 1 kg connected with springs with constants c = 1 kg/s 2 and dampers with constants d = 0. 2 kg/s. The control is applied to the first and last mass. The model is thus (see Fig. 8): where i = 2,..., N -1. The state of the system is x = [y 1 ˙ y 1 · · · y N ˙ y N] ⊤. Similar to the case, the aim is to control the system to origin from an initial condition where the first mass and middle mass, with index i = ⌊ N 2 ⌋ +1, are started at position 1 m.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Experiment with increasing state dimensionality", "weight": 1.0} -->

The model is uniformly discretised, with closed-form zero-order-hold (ZOH) discretisation, using varying number of time steps T = 10 2,..., 10 3 such that the total control interval length is 10 s.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Experiment with increasing state dimensionality", "weight": 1.0} -->

The cost function is Fig. 9 shows the results of sequential LQT and proposed parallel LQT. Due to parallelisation of the matrix operations on the individual steps of the sequential LQT, its run time is essentially independent of the state dimension. The parallel method, however, experiences significant run time increase with larger state dimension. Although when the number of masses N is 2-64, the run times of the parallel methods are shorter than those of the sequential method, with N = 128 the parallel method is slower with small numbers of time steps and with N = 256 it is slower with all the time step counts.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Experiment with finite state space", "weight": 1.0} -->

In this experiment, we consider an aircraft routing problem [2, Example 6.1.1], where an aircraft proceeds from left to right, and the aim is to control up and down movement on a finite grid so that the total cost is minimised. Each of the grid points incurs a cost { 0, 1, 2 } which is related to the fuel required to go through it. Taking a control up or down costs a single unit, and proceeding straight costs nothing. The scenario is illustrated in Fig. 10.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Experiment with finite state space", "weight": 1.0} -->

Fig. 9. Run times of the mass-spring-damper problem with different number of masses N corresponding to state dimensionalities 2 N.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Experiment with finite state space", "weight": 1.0} -->

Fig. 10. Finite state space scenario where the aim is to find a minimum cost path from left to right by steering up or down (see Section VI-D). The gray scale values show the cost function values.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Experiment with finite state space", "weight": 1.0} -->

In this case we tested the finite-state control law computation using different state dimensionalities as the parallel combination rule can be expected to have a dependence on the state dimensionality when the number of computational cores is limited. The GPU speed-ups for state dimensions D x ∈ { 5, 11, 21 } are shown in Fig. 11. It can be seen that with state dimensionality D x = 5 the speed-up reaches ∼ 1500 with T = 10 5 and is still slightly increasing. With the state dimensionality D x = 11 the maximum achieved speed-up is roughly ∼ 700, and with state dimensionality D x = 21 the speed-up saturates to a value around 350. However, with all of the state dimensionalities parallelisation provides a significant speed-up.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Experiment with nonlinear LQT", "weight": 1.0} -->

This experiment is concerned with a non-linear dynamic model where we control a simple unicycle [34, Sec. 13.2.4.1] whose state consists of 2-D position, orientation, and speed x = [p x p y θ s] ⊤. The aim is to steer the device to follow a given position and orientation trajectory which corresponds to going around a fixed race track multiple times. The control signal consists of the tangential acceleration and turn rate u = [a ω] ⊤. The discretized nonlinear model has the form Fig. 11. Finite state space GPU speed-ups for control law computation (parallel vs. sequential) with state dimensions 5, 11, and 21. and ∆ t k = t k +1 -t k. Fig. 12 shows the trajectory and the optimal trajectory produced by the nonlinear LQT.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Experiment with nonlinear LQT", "weight": 1.0} -->

The cost function parameters were selected to be the following for k = 0,..., T -1: where c k = 100, d k = 1000, when there is a reference point at step k, and 10 -6 otherwise. The latter values were also used for the terminal step k = T. The time step length was ∆ t k = 0. 1.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Experiment with nonlinear LQT", "weight": 1.0} -->

An iterated nonlinear LQT using a Taylor series approximation was applied to the model, and the number of iterations was fixed to 10. Fig. 13 shows the run times for GPU. It can be seen that parallelisation provides a significant speedup over sequential computation. When the Method 1 was used to compute the recovered trajectory at each iteration step, the speed-up grows to around 800 for T = 10 5 on GPU. Method 2 reaches a speed-up of around 600.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Experiment with nonlinear LQT", "weight": 1.0} -->

Fig. 12. Simulated trajectory from the nonlinear control problem and optimal trajectory produced by nonlinear LQT (see Section VI-E).

<!-- chunk {"id": "body-0116", "role": "body", "section": "Experiment with nonlinear LQT", "weight": 1.0} -->

Fig. 13. Nonlinear LQT GPU run times and speedup for 10 iterations.

<!-- chunk {"id": "body-0117", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

In this paper, we have shown how dynamic programming solutions to optimal control problems and their linear quadratic special case, the linear quadratic tracker (LQT), can be parallelised in the temporal domain by defining the corresponding associative operators and making use of parallel scans. The parallel methods have logarithmic complexity with respect to the number of time steps, which significantly reduces the linear complexity of standard (sequential) methods for long time horizon control problems. These benefits are shown via numerical experiments run on a GPU. This paper shows that the contribution is timely as it can leverage modern hardware and software for parallel computing, such as GPUs and TensorFlow.

<!-- chunk {"id": "body-0118", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

An interesting future extension of the framework would be parallel stochastic dynamic programming solution to stochastic control problems,. As discussed in Section IV-D, this is straightforward in the LQT case due to certainty equivalence, but the general stochastic case is not straightforward. Formally it is possible to replace the state x k with the distribution of the state p k and consider condition value functionals of the form V i → j [ p i, p j ] and value functionals of the form V i [ p i ]. The present framework then, in principle, applies as such. In particular, when the distributions have finite-dimensional sufficient statistics, this can lead to tractable methods. Unfortunately, unlike in the sequential dynamic programming case, more generally, this approach does not seem to lead to a tractable algorithm.

<!-- chunk {"id": "body-0119", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

Another interesting extension is to consider continuous optimal control problems in which case also the stochastic control solution has certain group properties which might allow for parallelisation. However, the benefit of parallelisation in the continuous case is not as clear as in discrete-time case because of the infinite number of time steps.
