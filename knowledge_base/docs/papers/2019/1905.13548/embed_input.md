<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sparse Optimal Control of Networks with Multiplicative Noise via Policy Gradient

Topics include Optimal control, Multiplicative noise, Networks, Sensor placement, Actuator placement.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Showed that one can use policy gradient to automatically design the placement of sensors and actuators in a controller for linear systems with multiplicative noise. Achieved by encoding the preference for certain kinds of sparsity patterns with sparsity-promoting convex regularizers in the objective function.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We give algorithms for designing near-optimal sparse controllers using policy gradient with applications to control of systems corrupted by multiplicative noise, which is increasingly important in emerging complex dynamical networks. Various regularization schemes are examined and incorporated into the optimization by the use of gradient, subgradient, and proximal gradient methods. Numerical experiments on a large networked system show that the algorithms converge to performant sparse mean-square stabilizing controllers.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Emerging highly distributed networked dynamical systems, such as critical infrastructure for power, water, and transportation, are high-dimensional and increasingly instrumented with new sensing, actuation, and communication technologies. A key problem is to design high performance control architectures that limit the number of actuators, sensors, and actuator-sensor communication links to reduce complexity and cost. Sparse control architectures may be crucial for managing complexity in emerging complex networks, but require solution of extremely difficult mixed combinatorial-continuous optimization problems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

There is a variety of performance metrics and optimization methodology for sparse control architecture design in the recent literature. Examples include structural rank conditions from Liu et al.; Ruths and Ruths; Olshevsky, controllability and observability Gramians from Pasqualetti et al.; Summers et al.; Tzoumas et al.; Jadbabaie et al., and optimal and robust control metrics from Hassibi et al.; Polyak et al.; Jovanović and Dhingra; Summers; Taha et al.; Zare and Jovanović, which are optimized via greedy algorithms, convex and mixed-integer optimization, and randomization.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Here we develop methods for sparse optimal control design in dynamical networks with multiplicative noise via policy gradient algorithms with sparsity-inducing regularization. Multiplicative noise arises in many networked systems when the weights of edges connecting nodes are stochastic in time. The noise is thus on the system parameters themselves and has a fundamentally different effect on the state evolution than additive noise, and indeed can lead to dramatic robustness issues. Specifically, a noise-ignorant classical optimal linear-quadratic (LQ) controller may actually destabilize a multiplicative noise system in the mean-square sense, even if the system was open-loop mean-square stable. Therefore noise-aware control is imperative to network performance and robustness. Moreover, the policy gradient methods we propose here, which operate directly on policy parameters, facilitate data-driven sparse control design when the model is unknown, a topic we are exploring in ongoing work.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Section 2 we formulate the problem and discusses a policy gradient approach to optimal control design for linear-quadratic systems with multiplicative noise. In Section 3 we propose several sparse control design methods for sensor and actuator selection and communication network design using gradient, subgradient, and proximal algorithms. In Section 4 we present numerical experiments to illustrate the results. Section 5 concludes.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Consider the discrete-time linear quadratic regulator with multiplicative noise (LQRm) optimal control problem

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

where $x_{t} \in {\mathbb{R}}^{n}$ is the system state, $u_{t} \in {\mathbb{R}}^{m}$ is the control input, $x_{0}$ is randomly distributed according to $\mathcal{P}$, expectation is with respect to $x_{0},\delta_{it},\gamma_{jt}$, and $Q \succeq 0$ and $R \succ 0$. The dynamics incorporate multiplicative noise terms modeled by the mutually independent and i.i.d. (over time) zero-mean random variables $\delta_{it}$ and $\gamma_{jt}$, which have variance $\alpha_{i}$ and $\beta_{j}$, respectively.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

The matrices $A_{i} \in {\mathbb{R}}^{n \times n}$ and $B_{i} \in {\mathbb{R}}^{n \times m}$ specify how each noise term affects the system dynamics and input matrices. The goal is to determine an optimal closed-loop feedback policy $\pi$ with $u_{t} = {\pi{(x_{t})}}$. We assume that the problem data $A$, $B$, $\alpha_{i}$, $A_{i}$, $\beta_{j}$, and $B_{j}$ are such that the optimal value of the problem exists and is finite. Feasibility of this problem is ensured if the system is mean-square stabilizable.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Optimal control via value iteration", "weight": 1.0} -->

Dynamic programming can be used to show that the optimal policy is linear state feedback with $u_{t} = {K^{\ast}x_{t}}$ where $K^{\ast} \in {\mathbb{R}}^{m \times n}$ and the resulting optimal cost for a fixed initial state is quadratic with ${V_{K^{\ast}}{(x_{0})}} = {x_{0}^{T}Px_{0}}$ where $P \in {\mathbb{R}}^{n \times n}$ is a symmetric positive definite matrix. When the model parameters are known, there are several known ways to compute the optimal feedback gains and corresponding optimal cost. The optimal cost is given by the solution of the generalized algebraic Riccati equation (ARE) (see, e.g., Damm ).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Optimal control via value iteration", "weight": 1.0} -->

This can be solved via value iteration, and the optimal gain matrix is

<!-- chunk {"id": "body-0013", "role": "body", "section": "Optimal control via policy gradient", "weight": 1.0} -->

For a fixed mean-square stabilizing linear state feedback policy $u_{t} = {Kx_{t}}$, there exists a positive semidefinite cost matrix $P_{K}$ which characterizes the cost by

<!-- chunk {"id": "body-0014", "role": "body", "section": "Optimal control via policy gradient", "weight": 1.0} -->

and is the solution to the generalized Lyapunov equation

<!-- chunk {"id": "body-0015", "role": "body", "section": "Optimal control via policy gradient", "weight": 1.0} -->

Furthermore, there exists a positive semidefinite infinite-horizon aggregate state covariance matrix

<!-- chunk {"id": "body-0016", "role": "body", "section": "Optimal control via policy gradient", "weight": 1.0} -->

which is the solution to the generalized Lyapunov equation

<!-- chunk {"id": "body-0017", "role": "body", "section": "Optimal control via policy gradient", "weight": 1.0} -->

This leads to the idea of performing gradient descent on $J$ (i.e.,

<!-- chunk {"id": "body-0018", "role": "body", "section": "Optimal control via policy gradient", "weight": 1.0} -->

for a fixed step size $\eta$. In this work we consider only the case where the model parameters are known, but the methods presented are immediately usable in the model-unknown case by estimating the gradient from trajectory data.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Gradient domination", "weight": 1.0} -->

It was shown recently by Fazel et al. that although the deterministic LQR cost is nonconvex, it is *gradient dominated*, also known as the Polyak-Łojasiewicz inequality originally due to Polyak. It is simple to show that if a function has a Lipschitz continuous gradient and satisfies this condition then performing gradient descent with a sufficiently small constant step size will result in asymptotic convergence to the optimal function value at a linear rate (see Karimi et al. ). For the LQRm problem, so long as the initial controller is stabilizing the LQRm cost is continuously differentiable over the sublevel set associated with the initial controller and thus the gradient possesses a local Lipschitz constant $L$ on this set. Identifying $L$ and the gradient domination constant is necessary for selection of a step size which is guaranteed to give convergence using gradient descent. Quantifying these constants is difficult but possible via lengthy chains of matrix inequalities as demonstrated by Fazel et al..

<!-- chunk {"id": "body-0020", "role": "body", "section": "Gradient domination", "weight": 1.0} -->

These results extend readily to the LQRm problem with relevant quantities pertaining to Lipschitz continuity of the gradient and the gradient domination conditions modified suitably to accommodate the multiplicative noise. In particular, the effect of the noise is to decrease the maximum step size that can be taken using gradient descent. We now state the relevant lemmas; the proofs are lengthy and can be found in our technical report (see Gravell et al. ).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Sparse control design", "weight": 1.0} -->

Entrywise, row, and column sparsity in $K$ correspond to actuator-sensor communication, actuator, and sensor sparsity respectively. With this in mind, we seek to solve the optimization problem of finding the sparsest set of entries, rows and/or columns of $K$ that achieve some prescribed level of performance in terms of the LQRm cost. However this problem is a nonconvex combinatorial problem which is NP-hard; the number of independent problem instances which must be solved scales factorially with $n$ and/or $m$. We instead turn to regularization as a heuristic to identifying good sparsity patterns.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Insufficiency of naive hard thresholding", "weight": 1.0} -->

The most naïve method of inducing sparsity is hard thresholding of the ARE solution as $K_{ij} = {0\text{~if~}{|K_{ij}|}} < r$. However, in general this is not useful since the resulting gains may not be stabilizing.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Insufficiency of naive hard thresholding", "weight": 1.0} -->

where $I_{n}$ is an $n \times n$ identity matrix. Imposing a hard threshold of $0.4$ on the ARE solution results in

<!-- chunk {"id": "body-0024", "role": "body", "section": "Insufficiency of naive hard thresholding", "weight": 1.0} -->

which gives a closed-loop state transition matrix $A + {BK}$ with an eigenvalue of $1.048223$ outside the unit circle. By contrast, by working with the regularized LQRm cost the optimal gains are always guaranteed to be stabilizing; even in the limit as the regularization weight $\rightarrow\infty$ the sparsity increases until the sparsest stabilizing solution is obtained. In practice, using a small step size helps ensure that each iterate remains inside the domain of $J{(K)}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Regularization", "weight": 1.0} -->

Certain types of regularization are well-known to be capable of inducing sparsity in the solutions to optimization problems. Perhaps the most basic and well-known is $l_{1}$-norm regularization which operates on a vector of decision variables; see Tibshirani for the seminal LASSO problem for sparse least-squares model selection and Hassibi et al. for sparse control design. In the case of a convex objective, increasing the regularization weight tends to increase sparsity by moving the global minimum onto the coordinate axes. Once the regularized problem has been solved, a sparsity pattern can easily be identified from the (near-)zero entries. In the current work we consider only the problem of identifying sparsity patterns, however an additional "polishing" step which involves re-solving the LQRm problem under the sparsity pattern can be performed to further improve the LQRm cost, as in Lin et al..

<!-- chunk {"id": "body-0026", "role": "body", "section": "Regularization", "weight": 1.0} -->

Entrywise sparsity is induced by the vector $l_{1}$-norm

<!-- chunk {"id": "body-0027", "role": "body", "section": "Regularization", "weight": 1.0} -->

Row and column sparsity are induced by using matrix row and column norms respectively defined as

<!-- chunk {"id": "body-0028", "role": "body", "section": "Regularization", "weight": 1.0} -->

where ${\| K^{r,i}\|}_{\infty}$ and ${\| K^{c,i}\|}_{\infty}$ are the maximum absolute values of the $i^{th}$ row and column respectively of $K$. Row and column sparsity are also induced by the row and column group LASSO

<!-- chunk {"id": "body-0029", "role": "body", "section": "Regularization", "weight": 1.0} -->

where ${\| K^{r,i}\|}_{\infty}$ and ${\| K^{c,i}\|}_{\infty}$ are the vector $l_{2}$-norms of the $i^{th}$ row and column respectively of $K$. Combined row and column sparsity can be induced by the row and column sparse group LASSO

<!-- chunk {"id": "body-0030", "role": "body", "section": "Regularization", "weight": 1.0} -->

or by various other weighted combinations of entrywise, row, and column norms. We refer to ${\| K\|}_{M}$ as a generic nondifferentiable sparsity-inducing regularizer.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Stationary point characterization", "weight": 1.0} -->

Before proceeding, we must point out an important consequence of regularizing the LQRm cost. The sum of a convex function and a gradient dominated function is not gradient dominated in general, and in fact can have multiple local minima. For example, consider the scalar function

<!-- chunk {"id": "body-0032", "role": "body", "section": "Stationary point characterization", "weight": 1.0} -->

where $x^{2}$ is strongly convex and $4{({{({x - 8})}^{2} + {3{\sin^{2}{({x - 8})}}}})}$ is gradient dominated. But $f{(x)}$ has two local minima at $x = 5.372$ and $x = 7.459$ and therefore is not gradient dominated.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Stationary point characterization", "weight": 1.0} -->

As a result any local first-order search procedure, such as those used by our algorithms, will not be guaranteed to find the global minimum. We conjecture that for the regularized LQRm problem there are at most two local minima, one associated with the LQRm cost and one associated with the regularization which tends to be more sparse. If this is so then choosing the initial point carefully may help the local search find the desired (sparser) local minimum. For open-loop mean-square systems, this motivates using zero gains as the initial condition. Likewise, in both the open-loop mean-square stable and unstable cases, an effective heuristic is to use the solution to a highly regularized problem instance to "warm start" another nearby problem instance with reduced regularization weight.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Other step directions", "weight": 1.0} -->

Promising choices of step directions other than the gradient ${\nabla_{K}J}{(K)}$ are the natural gradient ${\nabla_{K}J}{(K)}\Sigma_{K}^{- 1}$ and the Gauss-Newton step $R_{K}^{- 1}{\nabla_{K}J}{(K)}\Sigma_{K}^{- 1}$ as given by Fazel et al.. When $\gamma = 0$, these step directions give faster convergence than the gradient step and in fact the convergence proofs are much simpler than that for the gradient step. Unfortunately, adding a regularizer makes these steps more difficult to calculate; it is not simply the sum of the gradient of the regularizer and the unregularized natural gradient or Gauss-Newton step of the LQRm cost. For this reason we restrict our attention to the standard (sub)gradient directions.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Regularized policy subgradient descent", "weight": 1.0} -->

In order to use nondifferentiable regularizers we use subgradient methods which take steps in the direction of subgradients. It is known that using a constant step size gives convergence to a bounded neighborhood of the optimum and that a diminishing step size gives asymptotic, albeit slow, convergence (see Nesterov ). One immediate issue is that subgradients are defined only for convex functions; since the LQRm cost is nonconvex, subgradients do not exist for the regularized LQRm cost. However we simply use the gradient of the LQRm cost plus the subgradient of the regularizer as the step direction. Thus our subgradient descent update is

<!-- chunk {"id": "body-0036", "role": "body", "section": "Algorithm 1 (Policy subgradient update)", "weight": 1.0} -->

Another issue is that there is no guarantee of feasibility of each next step; it is possible to take a step so large that the next point is a mean-square unstable controller giving infinite objective cost. It is not straightforward to obtain restrictions on the step size to guarantee this feasibility. Gradient descent does not suffer from this problem since the gradient is guaranteed to be a true descent direction so there is always a sufficiently small step size to give a feasible next step. Nevertheless, in practice it is rare for a sufficiently small subgradient step to be infeasible.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Proximal policy gradient", "weight": 1.0} -->

Proximal gradient methods have become a preferred way to solve optimization problems of the form

<!-- chunk {"id": "body-0038", "role": "body", "section": "Proximal policy gradient", "weight": 1.0} -->

where $f{(x)}$ has a Lipschitz continuous gradient and $g{(x)}$ is convex and nondifferentiable, as is the case when $g{(x)}$ is a sparsity-inducing regularizer. The proximal gradient method update is

<!-- chunk {"id": "body-0039", "role": "body", "section": "Proximal policy gradient", "weight": 1.0} -->

where the proximity operator is defined as

<!-- chunk {"id": "body-0040", "role": "body", "section": "Proximal policy gradient", "weight": 1.0} -->

Much of the existing literature examines the case where $f{(x)}$ is convex, in which case gradient descent is guaranteed to converge. The proximal operator has closed-form expressions for ${\| K\|}_{1}$ and ${\| K\|}_{glr}$ called soft thresholding and block soft thresholding (see Parikh et al. ).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Algorithm 2 (Proximal policy gradient update)", "weight": 1.0} -->

where $\DeltaK^{(k)}$ is a generic step direction.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Algorithm 2 (Proximal policy gradient update)", "weight": 1.0} -->

A result from Hassan-Moghaddam and Jovanović guarantees convergence at a linear rate to the optimal function value using the proximal gradient method on a function satisfying a proximal gradient domination condition. This condition was shown to be equivalent by one given by Karimi et al. and an inequality from Kurdyka. However, this condition is not guaranteed to hold when $f{(x)}$ is gradient dominated and $g{(x)}$ is convex; the full condition must be checked, which involves interaction between $f{(x)}$ and $g{(x)}$. It is nontrivial to verify that the condition is satisfied for the regularized LQRm cost. Empirically it appears that the inequality may be satisfied since the proximal gradient method converged to solutions similar to those from our other two methods.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Algorithm 3 (Policy gradient update)", "weight": 1.0} -->

Here we use differentiable Huber-type losses ${\| K\|}_{M,h,\phi}$ in place of nondifferentiable regularizers, which replace linear corners with quadratic tips for decision variable values smaller than a specified threshold. Although the solutions produced are not exactly sparse, in practice entries are sufficiently close to zero to identify the sparsity pattern. Furthermore, by iteratively decreasing the threshold the solutions can be made arbitrarily close to truly sparse.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Algorithm 3 (Policy gradient update)", "weight": 1.0} -->

We define the Huber function of a scalar $a$ as

<!-- chunk {"id": "body-0045", "role": "body", "section": "Algorithm 3 (Policy gradient update)", "weight": 1.0} -->

and the $p$-Huber function (like a $p$-norm) of a vector $b$ as

<!-- chunk {"id": "body-0046", "role": "body", "section": "Algorithm 3 (Policy gradient update)", "weight": 1.0} -->

We define the vector Huber loss as

<!-- chunk {"id": "body-0047", "role": "body", "section": "Algorithm 3 (Policy gradient update)", "weight": 1.0} -->

the Huber row and column norms as

<!-- chunk {"id": "body-0048", "role": "body", "section": "Algorithm 3 (Policy gradient update)", "weight": 1.0} -->

and the Huber row and column group LASSO as

<!-- chunk {"id": "body-0049", "role": "body", "section": "Algorithm 3 (Policy gradient update)", "weight": 1.0} -->

Subgradients of two regularizers and the gradients of their differentiable counterparts are given in Table 1.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Simulation results", "weight": 1.0} -->

We considered an example system which represents diffusion dynamics on a particular undirected Erdős-Rényi random graph. It is well known that if $p_{ER} = {{({{\log n} + c})}/n}$ for constant $c \in {\mathbb{R}}$, then ${\lim_{n\rightarrow\infty}{P{({G{(n,p)}\text{~connected}})}}} = e^{- e^{- c}}$ so we chose $n = 51$, $c = 7$ and $p_{ER} = 0.2144$ and with probability $P = 0.999$ obtained a connected graph (see Bollobás and Béla ). The graph was selected so that it was connected, which ensured controllability. The first row and and column of the graph Laplacian were removed in order to fix the system's state reference to the first node which removed the zero eigenvalue otherwise present.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Simulation results", "weight": 1.0} -->

The continuous time system was discretized using a standard bilinear transform (Tustin's approximation) which preserves the open-loop mean stability of this system. Two multiplicative noises act each on $A$ and $B$ whose entries were drawn from a Gaussian distribution. The multiplicative noise variances were set at two levels, low and high, so that the system was open-loop mean-square stable and unstable, respectively.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Simulation results", "weight": 1.0} -->

For the subgradient and proximal gradient methods, we stopped iterating after the best iterate had been held for 100 iterations. For the gradient method, we stopped iterating when the Frobenius norm of the gradient of the cost function fell below a small threshold value, ${0.1 \times \text{card}}{(K)}$. We swept through a range of sparsity levels by solving a problem with low $\gamma$ then increasing $\gamma$ and resolving the problem using the previous solution as the initial guess. The step size $\eta$ was initialized at $10^{- 5}$. For the $l_{1}$-norm and row group LASSO $\gamma$ was initialized at 10 and 100 respectively. For each successive problem, the regularization weight was multiplied by a ratio $r_{\gamma} = \sqrt{2}$ and the step size was multiplied by $r_{\eta} = r_{\gamma}^{- \sqrt{2}}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Simulation results", "weight": 1.0} -->

To determine sparsity patterns we considered a value to be sparse if it was less than 5% than the max value in $K$. For the $l_{1}$-norm the sparsity values were the absolute values of the entries. For the row group lasso norm the sparsity values were the the values are the $l_{2}$-norms of the rows and columns respectively. Sparsity patterns are presented in Figs. 1 and 2 with white cells representing near-zero entries. The LQRm costs given in Figs. 3 and 4 are for the sparse gains without any polishing step applied, which otherwise could significantly reduce the cost. We give the total "wall-clock" computation time in Fig. 4 to capture the aggregate computational expense of each algorithm. The main computational expense came from evaluating the LQRm gradient at each iteration, which required solving a generalized discrete Lyapunov equation.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Simulation results", "weight": 1.0} -->

As seen in Fig. 4, the first iteration had the longest compute time since successive iterations benefited from favorable initial conditions from warm-starting. The compute time increased as the regularization weight was increased and a larger number of smaller steps were required to accommodate the increasing gradient magnitude.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Simulation results", "weight": 1.0} -->

From our empirical studies, the three methods presented all gave very similar results with similar efficacy; arbitrarily entrywise and row sparse mean-square stabilizing solutions were obtained for the low noise setting after a reasonable amount of computation time. Similarly, very sparse solutions for the high noise setting were obtained.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Simulation results", "weight": 1.0} -->

Python code which implements the algorithms and generates the figures reported in this work can be found in the GitHub repository at

<!-- chunk {"id": "body-0057", "role": "body", "section": "Simulation results", "weight": 1.0} -->

The code was run on a desktop PC with a quad-core Intel i7 6700K 4.0GHz CPU, 16GB RAM.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

We developed three policy gradient algorithms for solving the sparse gain design problem for networked dynamical systems with multiplicative noise. We showed that the regularized LQR cost does not necessarily have a unique local minimum, hampering efforts to guarantee global convergence of the algorithms. Nevertheless, efficacy of the algorithms is demonstrated empirically via computational simulations. Through various regularization functions we identified sparsity patterns for near-optimal actuator, sensor, and actuator-sensor link removal. This paves the way for data-driven control design in the model-free setting for such systems.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

Future work will attempt to prove unique local minimization of the regularized LQR cost or provide a set of restrictions under which such a condition holds. A salient issue with policy gradient methods relates to scalability; for large systems the gradient calculation is computationally expensive. Hence we will explore low-rank approximations of the gradient and consequent effects on convergence. We will also extend this work to the unknown-model setting and explore alternative model-based learning schemes.
