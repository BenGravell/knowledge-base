<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Temporal Parallelization of Dynamic Programming and Linear Quadratic Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This article proposes a general formulation for temporal parallelization of dynamic programming for optimal control problems. We derive the elements and associative operators to be able to use parallel scans to solve these problems with logarithmic time complexity rather than linear time complexity. We apply this methodology to problems with finite state and control spaces, linear quadratic tracking control problems, and to a class of nonlinear control problems. The computational benefits of the parallel methods are demonstrated via numerical simulations run on a graphics processing unit.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Optimal control theory (see, e.g., ) is concerned with designing control signals to steer a system such that a given cost function is minimised, or equivalently, a performance measure is maximised. The system can be, for example, an airplane or autonomous vehicle which is steered to follow a given trajectory, an inventory system, a chemical reaction, or a mobile robot.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Dynamic programming, in the form first introduced by Bellman 1950's, is a general method for determining feedback laws for optimal control and other sequential decision problems, and it also forms the basis of reinforcement learning, which is a subfield of machine learning. The classic dynamic programming algorithm is a sequential procedure that proceeds backwards from the final time step to the initial time step, and determines the value (cost-to-go) function as well as the optimal control law in time complexity of $O{(T)}$, where $T$ is the number of time steps. The algorithm is optimal in the sense that no sequential algorithm that processes all the $T$ time steps can have a time-complexity less than $O{(T)}$.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, the complexity $O{(T)}$ is only optimal in a computer with one single-core central processing unit (CPU). Nowadays, even general-purpose computers typically have multi-core CPUs with tens of cores and higher-end computers can have hundreds of them. Furthermore, graphics processing units (GPUs) have become common accessories of general-purpose computers and current high-end GPUs can have tens of thousands of computational cores that can be used to parallelise computations and lower the time-complexity.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Dynamic programming algorithms that parallelise computations at each time step, but operate sequentially, are provided in for discrete states, and in for the Riccati recursion in linear quadratic problems. Another approach to speed up computations for model predictive control (MPC) in linear quadratic problems is partial condensing, which is based on splitting the problem into temporal blocks and eliminating the intermediate states algebraically. The required block-conversion can be done in parallel and the resulting modified linear quadratic problem can be solved using parallel methods such as. However, the complexity of the resulting algorithm is still linear in time.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The previous dynamic programming algorithms have linear time-complexity $O{(T)}$, but there are some approaches in literature to lower this complexity by using parallelisation across time. One idea applied in the context of an allocation process can be found in \[9, Sec. I.30\], where the time interval is divided into two, and the two problems are solved in parallel. Various forms of parallel algorithms for dynamic programming with discrete states are given. Reference presents a partitioned dynamic programming suitable for parallelisation for linear quadratic control problems, though it has the disadvantage that some required inverse matrices may not exist. An iterated method for linear quadratic control problems, with constraints, in which each step can be parallelised is proposed, though it requires positive definite matrices in the cost function and may require regularisation. An algorithm to approximately solve an optimal control problem by solving different subproblems with partially overlapping time windows is provided, and an approximate parallel algorithm for linear MPC is given. Reference provides combination rules to separate the dynamic programming algorithm into different subproblems across the temporal domain. These combination rules are the foundation for temporal parallelisation.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main contribution of this paper is to present a parallel formulation of dynamic programming that is exact and has a time complexity $O{({\log T})}$. None of the previous works achieve these two aspects simultaneously. The central idea is to reformulate dynamic programming in terms of associative operators, which enable the use of parallel scan algorithms to parallelise the algorithm. The resulting algorithm has a span-complexity of $O{({\log T})}$, which translates into a time-complexity of $O{({\log T})}$ with a large enough number of computational cores. The algorithm can therefore speed up the computations significantly for long time horizons.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we first provide the general formulation to parallelise dynamic programming by defining conditional value functions between two different time steps and combining them via the rule. We also show how to obtain the optimal control laws and resulting trajectories making use of parallel computation. Then, we explain how this general methodology can be directly applied to problems with finite state and control spaces. The second contribution of this paper is to specialise the methodology to linear quadratic optimal control problems, that is, to linear quadratic trackers (LQTs). The parallel LQT formulation is not straightforward, as it requires the propagation of the dual function associated with the conditional value function to avoid numerical problems. Our third contribution is to extend the parallel LQT algorithm to approximately solve certain nonlinear control problems by iterated linearisations, as. Finally, we have implemented these algorithms in TensorFlow, which enables parallel computations on GPUs, to experimentally show that the parallel algorithms provide a significant speed-up also in practice.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The present approach is closely related to the temporal parallelisation of Bayesian smoothers and hidden Markov model inference recently considered. These approaches use a similar scan-algorithm-based parallelisation in the context of state-estimation problems. The combination rule is also related to so-called max-plus algebras for dynamic programming which have been considered, for example,.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The structure of the paper is the following. In Section 2 we provide a brief background on dynamic programming and parallel computing, in Section 3 we provide the parallel methods to general and finite-state problems, in Section 4 we consider the parallel solution to LQT problems, in Section 5, we discuss some practical implementation aspects and computational complexity, in Section 6 we experimentally illustrate the performance of the methods on a GPU platform, and finally we conclude the article in Section 7.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Deterministic control problem", "weight": 1.0} -->

We consider a deterministic control problem that consists of a difference equation and a cost function of the form

<!-- chunk {"id": "body-0013", "role": "body", "section": "Deterministic control problem", "weight": 1.0} -->

In Bellman's dynamic programming the idea is to form a cost-to-go or value function $V_{k}{(x_{k})}$ which gives the cost of the trajectory when we follow the optimal decisions for the remaining steps up to $T$ starting from state $x_{k}$. It can be shown that the value function admits the recursion

<!-- chunk {"id": "body-0014", "role": "body", "section": "Deterministic control problem", "weight": 1.0} -->

Given the control law for all time steps, we can compute the optimal trajectory from time steps $S + 1$ to $T$, which is denoted as $(x_{S + 1}^{\ast},\ldots,x_{T}^{\ast})$, by an additional forward pass starting at $x_{S}^{\ast} = x_{S}$ and

<!-- chunk {"id": "body-0015", "role": "body", "section": "Linear quadratic tracker", "weight": 1.0} -->

The LQT problem is the solution to a linear quadratic control problem of the form

<!-- chunk {"id": "body-0016", "role": "body", "section": "Linear quadratic tracker", "weight": 1.0} -->

In this setting, the objective is that a linear combination of the states $H_{k}x_{k}$ follows a reference trajectory $r_{k}$ from time step $S$ to $T$. The linear quadratic regulator is a special case of the LQT problem by setting $r_{k} = 0$, $c_{k} = 0$, and $H_{k} = {I{\forall k}}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Linear quadratic tracker", "weight": 1.0} -->

In this case, the value function is

<!-- chunk {"id": "body-0018", "role": "body", "section": "Linear quadratic tracker", "weight": 1.0} -->

The optimal trajectory resulting from applying the optimal control law can be computed with an additional forward pass starting at $x_{S}$ and with control law.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Linear quadratic tracker", "weight": 1.0} -->

It should be noted that the derivation of LQT in does not include time-varying matrices or parameter $c_{k}$ in the problem formulation, but it is straightforward to include these. It is also possible to use the LQT solution as a basis for approximate non-linear control by linearizing the system along a nominal trajectory (see and Sec. 4.4.3).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Associative operators and parallel computing", "weight": 1.0} -->

Parallel computing (see, e.g., ) refers to programming and algorithm design methods that take the availability of multiple computational cores into account. When some parts of the problem can be solved independently, then those parts can be solved in parallel to reduce the computational time. The more parts we can solve in parallel, the more speed-up we get.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Associative operators and parallel computing", "weight": 1.0} -->

Sequential problems which at first glance do not seem to be parallelisable can often be parallelised using so called parallel scan or all-prefix-sums algorithms. Given a sequence of elements $a_{1},\ldots,a_{T}$ and an associative operator $\otimes$ defined on them, such as summation, multiplication, or minimisation, the parallel scan algorithm computes the all-prefix-sums operation which returns the values $s_{1},\ldots,s_{T}$ such that

<!-- chunk {"id": "body-0022", "role": "body", "section": "Associative operators and parallel computing", "weight": 1.0} -->

in $O{({\log T})}$ time. The key aspect is that because the operator $\otimes$ is associative, we can rearrange the computations in various ways which generate independent sub-problems, for example,

<!-- chunk {"id": "body-0023", "role": "body", "section": "Associative operators and parallel computing", "weight": 1.0} -->

and, by a suitable combination of the partial solutions, we can obtain the result in $O{({\log T})}$ parallel steps. The specific combination requires an up-sweep and a down-sweep on a binary tree of computations. A pseudocode is given in Algorithm 1. Clearly, the prefix sums can also be computed in parallel in the backward direction $({a_{1} \otimes \cdots \otimes a_{T}},\ldots,{a_{T - 1} \otimes a_{T}},a_{T})$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Associative operators and parallel computing", "weight": 1.0} -->

It should be noted that while parallel scans significantly lower the wall-clock time to compute all-prefix-sums, they have the drawback that the number of total computations is higher than in the sequential algorithm. This implies that they require higher energy, which may not be suitable for small-scale mobile systems.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Associative operators and parallel computing", "weight": 1.0} -->

Input: The elements ak for k = 1, …, T and an associative operator ⊗.
Output: The all prefix sums are returned in ak for k = 1, …, T.
1: // Save the input:
2: for i ← 1 to T do {Compute in parallel}
7: for i ← 0 to T − 1 by 2d + 1 do {Compute in parallel}
13: aT ← 0 {Here, 0 is the neutral element for ⊗}
16: for i ← 0 to T − 1 by 2d + 1 do {Compute in parallel}
25: for i ← 1 to T do {Compute in parallel}
Algorithm 1 Parallel-scan algorithm. The algorithm in this form assumes that T is a power of 2, but it can easily be generalized to an arbitrary T.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Parallel optimal control", "weight": 1.0} -->

In this section, we start by defining conditional value functions and their combination rules (Section 3.1) and then we use them to define the associative operators and elements for parallelisation (Section 3.2). We also derive the parallel solution of the resulting optimal trajectory (Section 3.3), and finally, we discuss the case where the state space and controls take values in finite sets (Section 3.4).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Conditional value functions and combination rules", "weight": 1.0} -->

In this section, we present the conditional value functions and their combination rules, which are required to design the parallel algorithms.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Associative operator for value functions", "weight": 1.0} -->

The combination rule for two elements $a = {V_{a}{(x,y)}}$ and $b = {V_{b}{(x,y)}}$ is then given as follows.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 6", "weight": 1.0} -->

After computing all the value functions, we can obtain all the control laws $u_{k}{(x_{k})}$ for $k = {S,\cdots,{T - 1}}$ by using. This operation can be done in parallel for each $k$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 7", "weight": 1.0} -->

If we are interested in evaluating $V_{S\rightarrow k}{(x_{S},x_{k})}$ at a given $x_{S}$, as we are in trajectory recovery, then instead of first using with initialisation, and then evaluating the result at $x_{S}$, we can also initialise an extra element

<!-- chunk {"id": "body-0031", "role": "body", "section": "Optimal trajectory recovery", "weight": 1.0} -->

Once we have obtained the optimal control laws in parallel, we can compute the resulting optimal trajectory $(x_{S + 1}^{\ast},\ldots,x_{T}^{\ast})$ in parallel using two methods.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Method 1", "weight": 1.0} -->

In the first method for trajectory recovery, the state of the optimal trajectory at time step $k$ can be computed by using and the composition of functions

<!-- chunk {"id": "body-0033", "role": "body", "section": "Method 1", "weight": 1.0} -->

We can compute using parallel scans as follows. The associative element $a$ is defined to be a function on $x$, $a = {f_{a}{( \cdot )}}$ and the operator is the function composition in the following definition.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Method 2", "weight": 1.0} -->

An alternative method, which resembles the max-product algorithm in probabilistic graphical models, is based on noticing that, from the definition of the conditional value function (15 ‣ 3.1 Conditional value functions and combination rules ‣ 3 Parallel optimal control ‣ Temporal Parallelisation of Dynamic Programming and Linear Quadratic Control")) and the value function, the state of the optimal trajectory at time step $k$ is given by

<!-- chunk {"id": "body-0035", "role": "body", "section": "Method 2", "weight": 1.0} -->

where we recall that $x_{S}$ is the initial known state. That is, we can just minimise the sum of the forward conditional value function $V_{S\rightarrow k}{(x_{S},x_{k})}$ and the (backwards) value function $V_{k}{(x_{k})}$, which can be calculated using parallel scans via and, respectively. Then, the minimisation can be done for each node in parallel.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Method 2", "weight": 1.0} -->

It should be noted that both approaches for optimal trajectory recovery require two parallel scans, one forward and one backwards, and one minimisation for each node.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Finite state and control spaces", "weight": 1.0} -->

The case in which the state and the control input belong to finite state spaces is important as we can solve the control problem in both sequential and parallel forms in closed-form. Let $x_{k} \in \left\{ 1,\ldots,D_{x} \right\}$ and $u_{k} \in \left\{ 1,\ldots,D_{u} \right\}$ where $D_{x}$ and $D_{u}$ are natural numbers.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Finite state and control spaces", "weight": 1.0} -->

Then, $f_{k}\left( x_{k},u_{k} \right)$ and $\ell_{n}{(x_{n},u_{n})}$ can be represented by matrices of dimensions $D_{x} \times D_{u}$, $V_{k}{(x_{k})}$ by a vector of dimension $D_{x}$, $u_{k}{(x_{k})}$ by a vector of dimension $D_{x}$, and $V_{k\rightarrow i}{(x_{k},x_{i})}$ by a matrix of size $D_{x} \times D_{x}$. Due to the finite state space, the required minimisations in and, can be performed by exhaustive search, which can also be parallelised.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Finite state and control spaces", "weight": 1.0} -->

For Method 1 for optimal trajectory recovery, the function $f_{k}^{\ast}{( \cdot )}$ can be represented as a vector of dimension $D_{x}$, and the function composition in can be performed by evaluating all cases.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Parallel linear quadratic tracker", "weight": 1.0} -->

In this section, we provide the parallel solution to the LQT case. In Section 4.1, we derive the conditional value functions and combination rules. In Section 4.2, we derive the associative elements to obtain the value functions $V_{S\rightarrow k}{(x_{S},x_{k})}$ and $V_{k}{(x_{k})}$. In Section 4.3, we address the computation of the optimal trajectory. Finally, in Section 4.4, we discuss extensions to stochastic and non-linear problems.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Conditional value functions and combination rules", "weight": 1.0} -->

For the LQT problem, $V_{k\rightarrow i}{(x_{k},x_{i})}$ in (15 ‣ 3.1 Conditional value functions and combination rules ‣ 3 Parallel optimal control ‣ Temporal Parallelisation of Dynamic Programming and Linear Quadratic Control")) is a quadratic program with affine equality constraints that we represent by its dual problem

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conditional value functions and combination rules", "weight": 1.0} -->

where $\lambda$ is a Lagrange multiplier $n_{x} \times 1$ vector and the dual function $g_{k\rightarrow i}( \cdot, \cdot, \cdot )$ has the parameterisation

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conditional value functions and combination rules", "weight": 1.0} -->

If $C_{k,i}$ is invertible, one can solve by calculating the gradient of with respect to $\lambda$ and setting it equal to zero, to obtain

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conditional value functions and combination rules", "weight": 1.0} -->

In this case, we can also interpret the conditional value function in terms of conditional Gaussian distributions as

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conditional value functions and combination rules", "weight": 1.0} -->

where $N{( \cdot;\overline{x},P)}$ denotes a Gaussian density with mean $\overline{x}$ and covariance matrix $P$, and $N_{I}( \cdot;\eta,J)$ denotes a Gaussian density parameterised in information form with information vector $\eta$ and information matrix $J$. A Gaussian distribution with mean $\overline{x}$ and covariance matrix $P$ can be written in its information form as $\eta = {P^{- 1}\overline{x}}$ and $J = P^{- 1}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Conditional value functions and combination rules", "weight": 1.0} -->

Nevertheless, in general, $C_{k,i}$ is not invertible so it is suitable to keep the dual function parameterisation.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Associative elements to obtain the value functions", "weight": 1.0} -->

The following lemma establishes how to define the elements of the parallel scan algorithms to obtain the value functions $V_{S\rightarrow k}{(x_{S},x_{k})}$ and $V_{k}{(x_{k})}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Remark 12", "weight": 1.0} -->

If we are interested in evaluating the conditional value functions $V_{S\rightarrow k}{(x_{S},x_{k})}$ for a given $x_{S}$, then we can also directly initialise by

<!-- chunk {"id": "body-0049", "role": "body", "section": "Optimal trajectory recovery", "weight": 1.0} -->

We proceed to explain how the two optimal trajectory recovery methods explained in Section 3.3 work for the LQT problem.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Method 1", "weight": 1.0} -->

Plugging the optimal control law into the dynamic equation, the optimal trajectory function in becomes

<!-- chunk {"id": "body-0051", "role": "body", "section": "Method 1", "weight": 1.0} -->

We denote a conditional optimal trajectory from time step $k$ to $i$ as

<!-- chunk {"id": "body-0052", "role": "body", "section": "Method 2", "weight": 1.0} -->

This method makes use of to recover the optimal trajectory. It first runs a forward pass to compute $V_{S\rightarrow k}{(x_{S},x_{k})}$ and then a backward pass to compute $V_{k}{(x_{k})}$. Then, the optimal trajectory is obtained via the following lemma.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Extensions", "weight": 1.0} -->

In this section, the aim is to discuss some straightforward extensions of the parallel LQT.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Extension to stochastic control", "weight": 1.0} -->

Although the extension of the general framework introduced in this article to stochastic control problems is hard, the stochastic LQT case follows easily. Stochastic LQT is concerned with models of the form

<!-- chunk {"id": "body-0055", "role": "body", "section": "Extension to stochastic control", "weight": 1.0} -->

where $\ell_{T}{(x_{T})}$ and $\ell_{n}{(x_{n})}$ are as given, and $w_{k}$ is a zero mean white noise process with covariance $Q_{k}$, $G_{k}$ is a given matrix, and $E\lbrack \cdot \rbrack$ denotes expectation over the state trajectory. It turns out that due to certainty equivalence property of linear stochastic control problems, the optimal control is still given by and the solution exactly matches the deterministic solution, that is, it is independent of $Q_{k}$ and $G_{k}$. The optimal value functions both in deterministic and stochastic cases have the form, but the value of the (irrelevant) constant is different.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Extension to stochastic control", "weight": 1.0} -->

It also results from the certainty equivalence property that the optimal control solution to the partially observed linear (affine) stochastic control problem with function and dynamic and measurement models

<!-- chunk {"id": "body-0057", "role": "body", "section": "Extension to stochastic control", "weight": 1.0} -->

where $y_{k}$ is a measurement, $O_{k}$ is a measurement model matrix, $d_{k}$ is a deterministic bias, and $e_{k}$ is a zero mean Gaussian measurement noise, is given, where the state $x_{k}$ is replaced with its Kalman filter estimate.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Extension to more general cost functions", "weight": 1.0} -->

We can now transform into the form using the factorisation

<!-- chunk {"id": "body-0059", "role": "body", "section": "Extension to more general cost functions", "weight": 1.0} -->

we get a system of the form. This system can then be solved for $(x_{n},{\overset{\sim}{u}}_{n})$, and the final control signal can be recovered via

<!-- chunk {"id": "body-0060", "role": "body", "section": "Extension to nonlinear control", "weight": 1.0} -->

The equations for solving the LQT problem can be extended to approximately solve nonlinear LQT systems by performing iterated linearisations, as. Let us consider a system of the form

<!-- chunk {"id": "body-0061", "role": "body", "section": "Extension to nonlinear control", "weight": 1.0} -->

where $f_{k}{( \cdot )}$, $g_{n}{( \cdot )}$ and $h_{n}{( \cdot )}$ are possibly nonlinear functions. Given a nominal trajectory ${\overline{x}}_{k},{\overline{u}}_{k}$ for $k \in {S,\ldots,T}$, we can linearise the nonlinear functions using first-order Taylor series as

<!-- chunk {"id": "body-0062", "role": "body", "section": "Implementation and computational complexity", "weight": 1.0} -->

In this section, we first discuss the practical implementation of the methods in Section 5.1. We then analyse the computational complexity in Section 5.2. Finally, we explain how to perform parallelisation in blocks in Section 5.3.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Practical implementation of parallel control", "weight": 1.0} -->

Given the associative operators and the elements, the solutions to the dynamic programming and trajectory prediction problems reduce to an initialisation step followed by a single call to a parallel scan algorithm routine parameterised by these operators and elements. Given the result of the scan, there can also be a result-extraction step which computes the final optimal control from the scan results.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Practical implementation of parallel control", "weight": 1.0} -->

*Parallel scan:* Call the backward parallel scan routine and, as its arguments, give the initialised elements above along with pointer to the operator in Lemma 10. This returns $V_{k}{(x_{k})}$ for all $k$, see and.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Practical implementation of parallel control", "weight": 1.0} -->

*Extraction:* Compute the optimal control using in parallel for all $k$.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Practical implementation of parallel control", "weight": 1.0} -->

The control law for a finite-state control problem is initialised with the conditional value functions in Theorem 5 and the parallel scan routine is given a pointer to the operator in Definition 3. The control law computation is finally done with using the value functions computed in parallel.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Practical implementation of parallel control", "weight": 1.0} -->

Sometimes, we also need to compute the actual trajectory and the corresponding optimal controls forward in time. For example, in iterative non-linear extensions of LQT discussed in Section 4.4.3 we need to linearise the trajectory with respect to the optimal trajectory and control obtained at the previous iteration. In this case, after computing the control laws, we need to do another computational pass. For example, in the LQT case when using Method 1 from Section 4.3,

<!-- chunk {"id": "body-0068", "role": "body", "section": "Practical implementation of parallel control", "weight": 1.0} -->

*Parallel scan:* Call the forward parallel scan routine and, as its arguments, give the initialised elements above along with pointer to the operator given in Lemma 13.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Practical implementation of parallel control", "weight": 1.0} -->

*Extraction:* The optimal trajectory can be extracted from the forward scan results as the elements ${\overset{\sim}{c}}_{S,k}$, see Lemma 14.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Practical implementation of parallel control", "weight": 1.0} -->

The steps for Method 1 in the finite-state case are analogous, but the elements are initialised according to Lemma 9 and the combination operator is given in Definition 8.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Practical implementation of parallel control", "weight": 1.0} -->

When using Method 2 for optimal trajectory recovery, the operator is the same as in the backward computation for the control law. The parallel scan is done in the forward direction and the final results still need to be evaluated at $x_{S}$ unless initialisation is done using Remark 12. Furthermore, after computing the backward and forward scans, we still need to compute the optimal states by using, which in the case of LQT reduces to

<!-- chunk {"id": "body-0072", "role": "body", "section": "Computational complexity", "weight": 1.0} -->

We proceed to analyse the computational complexity of the proposed methods. For this purpose it is useful to assume that the computer that we have operates according to the PRAM (parallel random access machine) model of computation (see, e.g., ). In this model, we assume that we have a bounded number $P$ of identical processors controller by a common clock with a read/write access to a shared random access memory. This model is quite accurate for multi-core CPUs and GPUs.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Computational complexity", "weight": 1.0} -->

The combination rule computations can also be parallelised, and their complexity will therefore depend on whether they are parallelised or not. For example, if we do not parallelise the computations in the LQT combination rule given in Lemma 10, then their complexity is $O{(n_{x}^{3})}$ due to the matrix inverses (or equivalent LU-factorisations) involved. If we perform the parallelisation, these LU-factorisations can be performed in parallel in $O{(n_{x})}$ span time. The following analysis is based on assuming that we in fact use parallel matrix routines to implement the operations at the combination steps, along with all the other steps.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Computational complexity", "weight": 1.0} -->

For the parallel algorithms we obtain the following results.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Block processing", "weight": 1.0} -->

Up to now, we have considered parallelisation of control problems at a single time step level. That is, we initialise the element $a_{k}$ for all $k$ using and then apply the parallel scan algorithm. Another option is to apply the parallel scan algorithm to non-overlapping blocks of $B$ time steps. That is, we can initialise the elements of the parallel scan with $V_{k\rightarrow{k + B}}$ for $k = {S + {nB}}$, with $n = {0,1,\ldots,{{T/B} - 1}}$. The initialisation of each element can be done using in $B - 1$ sequential steps. Then, we can apply the parallel scan algorithm to fuse the information from all blocks. In this case, the time-complexity in a PRAM computer with large enough number of processors is $O{({B + {\log{({N/B})}}})}$, so it is optimal to choose $B = 1$. Nevertheless, this approach can be useful if we have a limited number of processors.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Block processing", "weight": 1.0} -->

By elimination of the state variables inside each block, we can reformulate the problem in terms of the initial states of blocks only, ${x_{0},x_{B},x_{2B},\ldots},$ which reduces the state dimensions from full state blocks to the original state dimension. The resulting problem is still a LQT problem, but with modified states and inputs, and hence we can use the proposed parallel LQT algorithms to solve it.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

In this section, we experimentally evaluate the performance of the methods in simulated applications. We implemented the methods using the open-source TensorFlow 2.6 software library using its Python 3.8 interface, which provides means to run parallel vectorised operations and parallel associative scans on GPUs. The experiments were run using NVIDIA A100-SXM GPU with 80GB of memory. In the experiments, we concentrate on the computational speed benefits because the sequential and parallel version of the algorithm compute exactly the same solution (provided that it is unique), the only difference being in the computational speed. The computation speeds were measured by averaging over 10 runs and the time taken to (jit) compile the code was not included in the measurement.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

We would like to point out that, as we are using TensorFlow with GPUs, the matrix operations on the individual time steps of the sequential algorithms are parallelised. Therefore, the sequential LQT algorithms can be interpreted as a TensorFlow parallel implementation of the Riccati recursion.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Experiment with basic LQT", "weight": 1.0} -->

The aim of the experiment is to demonstrate the benefit of the proposed parallelization method over the classical sequential solution in an LQT problem. We consider a 2-D tracking problem obeying Newton's law \[2, Example 4.4.2\]. In this LQT problem, the aim is to steer an object to follow a given trajectory of reference points in 2-D by using applied forces as the control signals.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Experiment with basic LQT", "weight": 1.0} -->

The state consists of the positions and velocities $x = \begin{bmatrix}
\end{bmatrix}^{\top}$ and the control signal $u = \begin{bmatrix}
\end{bmatrix}^{\top}$ contains the accelerations (forces divided by the mass which is unity in our case). If we assume that the control signal is kept fixed over each discretisation interval $\lbrack t_{k},t_{k + 1}\rbrack$, then the dynamic model can be written as

<!-- chunk {"id": "body-0081", "role": "body", "section": "Experiment with basic LQT", "weight": 1.0} -->

and ${\Deltat_{k}} = {t_{k + 1} - t_{k}}$ is the sampling interval. Fig. 1 illustrates the scenario.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Experiment with basic LQT", "weight": 1.0} -->

The dynamic trajectory is discretized so that we add 10 intermediate steps between each of the reference point time steps which then results in a total of $T$ times steps (giving ${\Deltat_{k}} = 0.1$). The cost function parameters are for $k = {0,\ldots,{T - 1}}$ selected to be

<!-- chunk {"id": "body-0083", "role": "body", "section": "Experiment with basic LQT", "weight": 1.0} -->

where $c_{k} = 100$ when there is a reference point at step $k$ and $10^{- 6}$ otherwise. At the final step we set $H_{T} = I_{4 \times 4}$ and $X_{T} = I_{4 \times 4}$. The reference trajectory contains the actual reference points at every 10th step $k$, and the intermediate steps are set equal to the previous reference point. At the final step the reference velocity is also zero. Together with the value $c_{k} = 10^{- 6}$ at these intermediate points this results in tiny regularisation of the intermediate paths, but the effect on the final result is practically negligible. It would also be possible to put $c_{k} = 0$ for the intermediate steps to yield almost the same result.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Experiment with basic LQT", "weight": 1.0} -->

The results computing the control law (i.e, the backward pass) of the classic sequential LQT and the proposed parallel LQT on the GPU for $T = {10^{2},\ldots,10^{5}}$ are shown in Fig. 2. The figure shows the run times of both in log-log scale on the top right figure and the parallel result up to $10^{4}$ is shown in linear scale on the top right. The speed-up, computed as the ratio of sequential and parallel run times, is shown in the bottom figure. It can be seen that the parallel version is significantly faster than the sequential version (illustrated in the top left figure) and the logarithmic scaling of the parallel algorithm can also be seen (illustrated in the top right figure). The speed-up (illustrated in the bottom figure) is of the order of $\sim$`<!-- -->`{=html}470 with $10^{5}$ time points and although it is close to saturating, it still increases a bit.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Experiment with basic LQT", "weight": 1.0} -->

We also ran the combined control law computation pass and the trajectory recovery pass on GPU, and the results are shown in Fig. 3. The advantage of parallel version over the sequential version can again be clearly seen. Furthermore, in this case, Method 1 for the parallel trajectory recovery is faster than Method 2.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Experiment with partial condensing", "weight": 1.0} -->

In this experiment we compare the proposed parallelisation method for LQT to partial condensing based parallelisation. We also demonstrate how parallel condensing can be combined with the proposed methodology to yield improved results. The same 2-D tracking problem and data are used as in Sec. 6.1.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Experiment with partial condensing", "weight": 1.0} -->

As discussed in Sec. 5.3, the idea of partial condensing is to reduce a control problem of length $T$ to a control problem of length $T/B$ by dividing the problem into blocks of length $B$. In each of these blocks we can eliminate all but the state at the beginning of the block, which effectively reduces a control problem with state dimension $n_{x}$, input dimension $Bn_{u}$, and length $T/B$. The required computations are 1) conversion of the model into block form, 2) computation of LQT solution of length $T/B$, and 3) reconstruction of the intermediate states in each block. Partial condensing allows for parallelisation of the computations because steps 1) and 3) are fully parallelisable and step 2) can be efficiently implemented by using parallel matrix operations within the sequential Riccati solution and trajectory reconstruction.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Experiment with partial condensing", "weight": 1.0} -->

The GPU run times of the aforementioned parallel condensing method with $B = {2,4,8,\ldots,256}$ are shown Fig. 4. The run times of the classical backward-forward sequential LQT solution for trajectory recovery and of the proposed parallel method with trajectory recovery with Method 1 are also shown in the figure. The trajectory lengths were $T = {10^{2},\ldots,10^{5}}$. It can be seen that the run times of partial condensing methods are significantly lower than of the classical sequential LQT while still, for the most of the cases, higher than of the proposed parallel method. It can be seen that with short trajectory lengths the partial condensing method is faster than the proposed parallel method when $B = 16$ or $32$. However, with larger trajectory lengths the proposed parallel method is faster.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Experiment with partial condensing", "weight": 1.0} -->

In the results of Fig. 4 we can see some evidence of an effect that when increasing $B$, the run time no longer decreases after a certain value. This is confirmed in Fig. 5 which shows the run times of the partial condensing over trajectory of length $T = 10^{5}$ with different values of $B$. It can be seen that the run time attains minimum somewhere around $B = 200$ and after that the run time starts to increase.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Experiment with partial condensing", "weight": 1.0} -->

As discussed in Sec. 5.3, it is also possible to combine partial condensing with the proposed parallelization methodology. This can be done by implementing the LQT solution (of length $T/B$) by using one of the parallel methods. Fig. 6 shows the results of using this combined approach. It can be seen that the partial condensing can be used to improve run time of the proposed parallel methods when $B$ is in suitable range (2--64 in this case). When $B$ is too large ($128$ or $256$), then partial condensing no longer improves the run times. This also happens with $B = 64$ when the trajectory length is short. Fig. 7 shows the run times with $T = 10^{5}$ as function of $B$. It can be seen in the figure that the minimum run time is attained roughly at value $B = 15$.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Experiment with increasing state dimensionality", "weight": 1.0} -->

In this experiment the aim is to test the scaling of run time when the dimensionality of the state increases. For this purpose, we use a slight modification of a mass-spring-damper problem \[43, Section 2.5.3\], where we have removed the control constraints, as we do not consider them in this paper. This is a linear model for controlling a chain of $N$ masses $m = 1$ kg connected with springs with constants $c = 1$ kg/s^2^ and dampers with constants $d = 0.2$ kg/s. The control is applied to the first and last mass. The model is thus (see Fig.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Experiment with increasing state dimensionality", "weight": 1.0} -->

where $i = {2,\ldots,{N - 1}}$. The state of the system is $x = \begin{bmatrix}
y_{1} & {\overset{˙}{y}}_{1} & \cdots & y_{N} & {\overset{˙}{y}}_{N}
\end{bmatrix}^{\top}$. Similar to the case, the aim is to control the system to origin from an initial condition where the first mass and middle mass, with index $i = {\left\lfloor \frac{N}{2} \right\rfloor + 1}$, are started at position $1$ m. The model is uniformly discretised, with closed-form zero-order-hold (ZOH) discretisation, using varying number of time steps $T = {10^{2},\ldots,10^{3}}$ such that the total control interval length is $10$ s.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Experiment with increasing state dimensionality", "weight": 1.0} -->

Fig. 9 shows the results of sequential LQT and proposed parallel LQT. Due to parallelisation of the matrix operations on the individual steps of the sequential LQT, its run time is essentially independent of the state dimension. The parallel method, however, experiences significant run time increase with larger state dimension. Although when the number of masses $N$ is 2--64, the run times of the parallel methods are shorter than those of the sequential method, with $N = 128$ the parallel method is slower with small numbers of time steps and with $N = 256$ it is slower with all the time step counts.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Experiment with finite state space", "weight": 1.0} -->

In this experiment, we consider an aircraft routing problem \[2, Example 6.1.1\], where an aircraft proceeds from left to right, and the aim is to control up and down movement on a finite grid so that the total cost is minimised. Each of the grid points incurs a cost $\{ 0,1,2\}$ which is related to the fuel required to go through it. Taking a control up or down costs a single unit, and proceeding straight costs nothing. The scenario is illustrated in Fig. 10.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Experiment with finite state space", "weight": 1.0} -->

In this case we tested the finite-state control law computation using different state dimensionalities as the parallel combination rule can be expected to have a dependence on the state dimensionality when the number of computational cores is limited. The GPU speed-ups for state dimensions $D_{x} \in {\{ 5,11,21\}}$ are shown in Fig. 11. It can be seen that with state dimensionality $D_{x} = 5$ the speed-up reaches $\sim$`<!-- -->`{=html}1500 with $T = 10^{5}$ and is still slightly increasing. With the state dimensionality $D_{x} = 11$ the maximum achieved speed-up is roughly $\sim$`<!-- -->`{=html}700, and with state dimensionality $D_{x} = 21$ the speed-up saturates to a value around $350$. However, with all of the state dimensionalities parallelisation provides a significant speed-up.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Experiment with nonlinear LQT", "weight": 1.0} -->

This experiment is concerned with a non-linear dynamic model where we control a simple unicycle \[34, Sec. 13.2.4.1\] whose state consists of 2-D position, orientation, and speed $x = \begin{bmatrix}
\end{bmatrix}^{\top}$. The aim is to steer the device to follow a given position and orientation trajectory which corresponds to going around a fixed race track multiple times. The control signal consists of the tangential acceleration and turn rate $u = \begin{bmatrix}
\end{bmatrix}^{\top}$. The discretized nonlinear model has the form

<!-- chunk {"id": "body-0097", "role": "body", "section": "Experiment with nonlinear LQT", "weight": 1.0} -->

and ${\Deltat_{k}} = {t_{k + 1} - t_{k}}$. Fig. 12 shows the trajectory and the optimal trajectory produced by the nonlinear LQT.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Experiment with nonlinear LQT", "weight": 1.0} -->

where ${c_{k} = 100},{d_{k} = 1000}$, when there is a reference point at step $k$, and $10^{- 6}$ otherwise. The latter values were also used for the terminal step $k = T$. The time step length was ${\Deltat_{k}} = 0.1$.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Experiment with nonlinear LQT", "weight": 1.0} -->

An iterated nonlinear LQT using a Taylor series approximation was applied to the model, and the number of iterations was fixed to $10$. Fig. 13 shows the run times for GPU. It can be seen that parallelisation provides a significant speed-up over sequential computation. When the Method 1 was used to compute the recovered trajectory at each iteration step, the speed-up grows to around $800$ for $T = 10^{5}$ on GPU. Method 2 reaches a speed-up of around $600$.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we have shown how dynamic programming solutions to optimal control problems and their linear quadratic special case, the linear quadratic tracker (LQT), can be parallelised in the temporal domain by defining the corresponding associative operators and making use of parallel scans. The parallel methods have logarithmic complexity with respect to the number of time steps, which significantly reduces the linear complexity of standard (sequential) methods for long time horizon control problems. These benefits are shown via numerical experiments run on a GPU. This paper shows that the contribution is timely as it can leverage modern hardware and software for parallel computing, such as GPUs and TensorFlow.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Conclusion", "weight": 1.5} -->

An interesting future extension of the framework would be parallel stochastic dynamic programming solution to stochastic control problems. As discussed in Section 4.4, this is straightforward in the LQT case due to certainty equivalence, but the general stochastic case is not straightforward. Formally it is possible to replace the state $x_{k}$ with the distribution of the state $p_{k}$ and consider condition value functionals of the form $V_{i\rightarrow j}{\lbrack p_{i},p_{j}\rbrack}$ and value functionals of the form $V_{i}{\lbrack p_{i}\rbrack}$. The present framework then, in principle, applies as such. In particular, when the distributions have finite-dimensional sufficient statistics, this can lead to tractable methods. Unfortunately, unlike in the sequential dynamic programming case, more generally, this approach does not seem to lead to a tractable algorithm.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Another interesting extension is to consider continuous optimal control problems in which case also the stochastic control solution has certain group properties which might allow for parallelisation. However, the benefit of parallelisation in the continuous case is not as clear as in discrete-time case because of the infinite number of time steps.
