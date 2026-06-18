<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Minimizing a Sum of Clipped Convex Functions

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider the problem of minimizing a sum of clipped convex functions; applications include clipped empirical risk minimization and clipped control. While the problem of minimizing the sum of clipped convex functions is NP-hard, we present some heuristics for approximately solving instances of these problems. These heuristics can be used to find good, if not global, solutions and appear to work well in practice. We also describe an alternative formulation, based on the perspective transformation, which makes the problem amenable to mixed-integer convex programming and yields computationally tractable lower bounds. We illustrate one of our heuristic methods by applying it to various examples and use the perspective transformation to certify that the solutions are relatively close to the global optimum. This paper is accompanied by an open-source implementation.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Suppose $f:{\text{R}^{n}\rightarrow\text{R}}$ is a convex function, and $\alpha \in \text{R}$. We refer to the function $\min{\{{f{(x)}},\alpha\}}$ as a *clipped convex function*. In this paper we consider the problem of minimizing a sum of clipped convex functions,

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

When ${f_{i}{(x)}} > \alpha_{i}$, the value of the $i$th term in the sum is *clipped* to $\alpha_{i}$, which limits how large each term in the objective can be. Many practical problems can be formulated as instances of; we describe a few in §2.

<!-- chunk {"id": "body-0005", "role": "body", "section": "NP-hardness", "weight": 1.0} -->

In general, problem is nonconvex and as a result can be very difficult to solve. Indeed, is NP-hard. We show this by giving a reduction of the subset sum problem to an instance of.

<!-- chunk {"id": "body-0006", "role": "body", "section": "NP-hardness", "weight": 1.0} -->

The subset sum problem involves determining whether or not there exists a subset of a given set of integers $a_{1},\ldots,a_{n}$ that sum to zero. The optimal value of the problem

<!-- chunk {"id": "body-0007", "role": "body", "section": "NP-hardness", "weight": 1.0} -->

which has the form, is zero if and only if $x_{i} \in {\{ 0,1\}}$, at least one of $x_{i} = 1$, and ${a^{T}x} = 0$; in other words, the set $\{ a_{i}\mid{x_{i} = 1}\}$ sums to zero. Since the subset sum problem can be reduced to an instance of, we conclude that in general our problem is at least as hard as difficult problems like the subset sum problem.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Global solution", "weight": 1.0} -->

There is a simple (exhaustive) method to solve globally: for each subset $\Omega$ of $\{ 1,\ldots,m\}$, we solve the convex problem

<!-- chunk {"id": "body-0009", "role": "body", "section": "Global solution", "weight": 1.0} -->

with variable $x \in \text{R}^{n}$. The solution to with the lowest optimal value is the solution to. This general method is not practical unless $m$ is quite small, since it requires the solution of $2^{m}$ convex optimization problems.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Global solution", "weight": 1.0} -->

In some specific instances of problem, we can cut down the search space if we know that a specific choice of $\Omega \subseteq {\{ 1,\ldots,m\}}$ implies

<!-- chunk {"id": "body-0011", "role": "body", "section": "Global solution", "weight": 1.0} -->

which means that the optimal value of is $+ \infty$. In this case, we do not have to solve problem for this choice of $\Omega$, as we know it will be infeasible. One simple example where this happens is when the $\alpha_{i}$-sublevel sets of $f_{i}$ are pairwise disjoint, which implies that we only have to solve $m$ convex problems (as opposed to $2^{m}$) to find the global solution. This idea is used in to guide their proposed search algorithm.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Summary", "weight": 1.0} -->

We begin by presenting some applications of minimizing a sum of clipped convex functions in §2 to empirical risk minimization and control. We then provide some simple heuristics for approximately solving in §3, which we have found to work well in practice. In §4, we describe a method for converting into a mixed-integer convex program, which is amenable to solvers for mixed-integer convex programs. Finally, we describe an open-source Python implementation of the ideas described in this paper in §5 and apply our implementation to a few illustrative examples in §6.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Applications", "weight": 1.0} -->

In this section we describe some possible applications of minimizing a sum of clipped convex functions.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Clipped empirical risk minimization", "weight": 1.0} -->

Here $x_{i}$ is the $i$th feature vector, $y_{i}$ is its corresponding output (or label), and $\mathcal{Y}$ is the output space.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Clipped empirical risk minimization", "weight": 1.0} -->

We find parameters $\theta \in \text{R}^{n}$ of a linear model given the data by solving the *empirical risk minimization* (ERM) problem

<!-- chunk {"id": "body-0016", "role": "body", "section": "Clipped empirical risk minimization", "weight": 1.0} -->

with variable $\theta$, where $l:{{\text{R} \times \mathcal{Y}}\rightarrow\text{R}}$ is the loss function, and $r:{\text{R}^{n}\rightarrow\text{R}}$ is the regularization function. Here the objective is composed of two parts: the loss function, which measures the accuracy of the predictions, and the regularization function, which measures the complexity of $\theta$. We assume that $l$ is convex in its first argument and that $r$ is convex, so the problem is a convex optimization problem.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Clipped empirical risk minimization", "weight": 1.0} -->

For a given $x \in \text{R}^{n}$, our prediction of $y$ is

<!-- chunk {"id": "body-0018", "role": "body", "section": "Clipped empirical risk minimization", "weight": 1.0} -->

While ERM often works well in practice, it can perform poorly when there are outliers in the data. One way of fixing this is to clip the loss for each data point to a value $\alpha \in \text{R}$, leading to the *clipped ERM* problem,

<!-- chunk {"id": "body-0019", "role": "body", "section": "Clipped empirical risk minimization", "weight": 1.0} -->

After solving (or approximately solving) the clipped problem, we can label data points $(x_{i},y_{i})$ where ${l{({x_{i}^{T}\theta^{\star}},y_{i})}} \geq \alpha$ as outliers. The clipped ERM problem is an instance of what is referred to in statistics as a *redescending M-estimator* \[8, §4.8\], since the derivative of the clipped loss goes to $0$ as the magnitude of its input goes to infinity. In this terminology, the clip value $\alpha$ is referred to as the *minimum rejection point*.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Clipped empirical risk minimization", "weight": 1.0} -->

In §6.1, we show an example where the normal empirical risk minimization problem fails, while its clipped variant has good performance.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Clipped control", "weight": 1.0} -->

Suppose we have a linear system with dynamics given by

<!-- chunk {"id": "body-0022", "role": "body", "section": "Clipped control", "weight": 1.0} -->

where $x_{t} \in \text{R}^{n}$ is the state of the system and $u_{t} \in \text{R}^{p}$ denotes the input to the system, at time period $t$. The dynamics matrix $A \in \text{R}^{n \times n}$ and the input matrix $B \in \text{R}^{n \times m}$ are given.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Clipped control", "weight": 1.0} -->

where, at time $t$, $\mathcal{X}_{t} \subseteq \text{R}^{n}$ is the convex set of allowable states and $\mathcal{U}_{t} \subseteq \text{R}^{m}$ is the convex set of allowable inputs. The variables in this problem are the states and inputs, $x_{t}$ and $u_{t}$. If the stage cost function $g_{t}$ are convex, the optimal control problem is a convex optimization problem.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Clipped control", "weight": 1.0} -->

We define a *clipped optimal control* problem as an optimal control problem in which the stage costs can be expressed as sums of clipped convex functions, i.e.,

<!-- chunk {"id": "body-0025", "role": "body", "section": "Clipped control", "weight": 1.0} -->

A simple but practical example of a clipped control problem is described in §6.3. The problem is to design a lane change trajectory for a vehicle; the stage cost is small when the vehicle is centered in either lane, which we express as a sum of two clipped convex functions.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Heuristic methods", "weight": 1.0} -->

There are many methods for approximately solving. In this section we describe a few heuristic methods that we have observed to work well in practice.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Bi-convex formulation", "weight": 1.0} -->

Throughout this section, we will make use of a simple reformulation of as the bi-convex problem

<!-- chunk {"id": "body-0028", "role": "body", "section": "Bi-convex formulation", "weight": 1.0} -->

with variables $\lambda \in \text{R}^{m}$ and $x \in \text{R}^{n}$. (We note that this reformulation was also pointed out in \[23, §3\].) The equivalence follows immediately from the fact that

<!-- chunk {"id": "body-0029", "role": "body", "section": "Nonlinear programming", "weight": 1.0} -->

When $f_{i}$ are all smooth functions and $\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}f_{0}$ is representable as the sublevel set of a smooth function, it is possible to use general nonlinear solvers to (approximately) solve.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Alternating minimization", "weight": 1.0} -->

Another possibility is to perform alternating minimization, since each respective minimization is a convex optimization problem. In alternating minimization, at iteration $k$, we solve while fixing $\lambda = \lambda^{k - 1}$, resulting in $x^{k}$. We then solve while fixing $x = x^{k}$, resulting in $\lambda^{k}$. It can be shown that

<!-- chunk {"id": "body-0031", "role": "body", "section": "Alternating minimization", "weight": 1.0} -->

is a solution for minimization over $\lambda$ with fixed $x = x^{k}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Inexact alternating minimization", "weight": 1.0} -->

Although alternating minimization often works well, we have found that inexact minimization over $\lambda$ works better in practice. Instead of fully minimizing over $\lambda$, we instead compute the gradient of the objective with respect to $\lambda$,

<!-- chunk {"id": "body-0033", "role": "body", "section": "Inexact alternating minimization", "weight": 1.0} -->

We then perform a signed projected gradient step on $\lambda$ with a fixed step size $\beta > 0$ (we have found $\beta = 0.1$ works well in practice, though a range of values all appear to work equally as well). This results in the update

<!-- chunk {"id": "body-0034", "role": "body", "section": "Inexact alternating minimization", "weight": 1.0} -->

where $\mathbf{s}\mathbf{i}\mathbf{g}\mathbf{n}$ is applied elementwise to $g$, and $\Pi_{{\lbrack 0,1\rbrack}^{m}}$ denotes the projection onto the unit box, given by

<!-- chunk {"id": "body-0035", "role": "body", "section": "Inexact alternating minimization", "weight": 1.0} -->

The final algorithm is described below.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Inexact alternating minimization", "weight": 1.0} -->

Algorithm 3 is a descent algorithm in the sense that the objective function of decreases after every iteration. It is also guaranteed to terminate in a finite amount of time, since there is a finite number of possible values of $\lambda$. We also note that alternating minimization can be thought of as a special case of algorithm 3 where $\beta \geq 1$. In practice, we have found that algorithm 3 often finds the global optimum in simple problems and appears to work well on more complicated cases. We use algorithm 3 in our generic `cvxpy` implementation (see §5).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Perspective formulation", "weight": 1.0} -->

In this section we describe the perspective formulation of. The perspective formulation is a mixed-integer convex program (MICP), for which specialized solvers with reasonable practical performance exist. The perspective formulation can also be used to compute a lower bound on the original objective by relaxing the integral constraints, as, as well to obtain good initializations for any of the procedures described in §3.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Perspective", "weight": 1.0} -->

for ${(x,t)} \in {\text{R}^{n} \times \text{R}_{+}}$. We will use the fact that the resulting function $f^{p}$ is convex \[3, §3.2.6\].

<!-- chunk {"id": "body-0039", "role": "body", "section": "Superlinearity assumption", "weight": 1.0} -->

since the limit in is equal to the limit in unless $x = 0$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Superlinearity assumption", "weight": 1.0} -->

There are many convex functions that satisfy this superlinearity property. Some examples are the sum of squares function and the indicator function of a compact convex set. Since we will make heavy use of property in this section, we will assume that $f_{0}$ is superlinear for the remainder of this section. If $f_{0}$ is not superlinear, then it can be made superlinear by adding, e.g., a small positive multiple of the sum of squares function.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Conic representation of the perspective", "weight": 1.0} -->

We note that representing the epigraph of the perspective of a function is often simple if the function has a conic representation. More specifically, if $f$ has a conic representation

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conic representation of the perspective", "weight": 1.0} -->

for some closed convex cone $\mathcal{K}$, then the perspective of $f$ has a conic representation given by

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conic representation of the perspective", "weight": 1.0} -->

This fact allows us to use a conic representation of the perspective and avoid issues of non-differentiability and division-by-zero that we might encounter with direct numerical implementations of the perspective \[12, §2\].

<!-- chunk {"id": "body-0044", "role": "body", "section": "Lower bound via relaxation", "weight": 1.0} -->

Since the perspective formulation is equivalent to the original problem, relaxing the Boolean constraint in and solving the resulting convex optimization problem

<!-- chunk {"id": "body-0045", "role": "body", "section": "Lower bound via relaxation", "weight": 1.0} -->

with variables $z_{i}$, $t$, and $x$, yields a lower bound on the objective value of. That is, given any approximate solution of with objective value $p$, the optimal value $q^{\star}$ of yields a certificate guaranteeing that the approximate solution is suboptimal by at most $p - q^{\star}$. Additionally, a solution of the relaxed problem can be used as an initial point for any of the heuristic methods described in §3.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Efficiently solving the relaxed problem", "weight": 1.0} -->

We note that has $m + 1$ times as many variables as the original problem, so it is worth considering faster solution methods. To do so, we can convert the problem to *consensus form* \[2, §7.1\]; i.e., we introduce additional variables $y_{i} \in \text{R}^{n}$ for $i = {1,\ldots,m}$, and constrain $y_{i} = x$, resulting in the equivalent problem

<!-- chunk {"id": "body-0047", "role": "body", "section": "Efficiently solving the relaxed problem", "weight": 1.0} -->

Since the objective is separable in $(y_{i},z_{i},t_{i})$ over $i$, there exist many efficient distributed algorithms for solving this problem, e.g., the alternating direction method of multipliers (ADMM).

<!-- chunk {"id": "body-0048", "role": "body", "section": "Implementation", "weight": 1.0} -->

Our Python package `sccf` approximately solves generic problems of the form provided all $f_{i}$ can be represented as valid `cvxpy` expressions and constraints.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Implementation", "weight": 1.0} -->

We provide a method `sccf.minimum`, which can be applied to a `cvxpy` Expression and a scalar to create a `sccf.MinExpression`. The user then forms an objective as a sum of `sccf.MinExpression`s, passes this objective and (possibly) constraints to a `sccf.Problem` object, and then calls the `solve` method, which implements algorithm 3. We take advantage of the fact that the only parameter changing between problems is $\lambda$ by caching the canonicalization procedure.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Implementation", "weight": 1.0} -->

objective += sccf.minimum(cp.square(A[i]@x-b[i]), 1.0)
objective += 0.01 * cp.sum_squares(x)

<!-- chunk {"id": "body-0051", "role": "body", "section": "Examples", "weight": 1.0} -->

All experiments were conducted on a single core of an Intel i7-8700K CPU clocked at 3.7 GHz.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Clipped regression", "weight": 1.0} -->

In this example we compare clipped regression (§2.1) with standard linear regression and Huber regression (a well known technique for robust regression) on a one-dimensional dataset with outliers. We generated data by sampling 20 data points $(x_{i},y_{i})$ according to

<!-- chunk {"id": "body-0053", "role": "body", "section": "Clipped regression", "weight": 1.0} -->

We introduced outliers in our data by flipping the sign of $y_{i}$ for 5 random data points.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Clipped regression", "weight": 1.0} -->

The problems all have the form

<!-- chunk {"id": "body-0055", "role": "body", "section": "Clipped regression", "weight": 1.0} -->

Let $\theta^{clip}$ be the clipped regression model; we deem points where ${({{x_{i}\theta^{clip}} - y_{i}})}^{2} \geq 0.5$ as outliers and the remaining points as inliers. In figure 1 we visualize the data points and the resulting models along with the outliers/inliers identified by the clipped regression model. In this figure, the clipped regression model clearly outperforms the linear and Huber regression models since it is able to fully ignore the outliers. Algorithm 3 terminated in 0.13 seconds and took 8 iterations on this instance.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Lower bound", "weight": 1.0} -->

The relaxed version of the perspective formulation can be used to efficiently find a lower bound on the objective value for the clipped version of. The objective value of for clipped regression was 1.147, while the lower bound we calculated was 0.533, meaning our approximate solution is suboptimal by at most 0.614.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Lower bound", "weight": 1.0} -->

In figure 2 we plot the clipped objective for various values of $\theta$; note that the function is highly nonconvex and that $\theta^{clip}$ is the (global) solution. We also plot the objective of the perspective relaxation as a function of $\theta$, found by partially minimizing over $z_{i}$ and $t$; note that the function is convex and a surprisingly good approximation of the true convex envelope. We note that the minimum of the perspective relaxation and the true minimum are surprisingly close, leading us to believe that the solution to the perspective relaxation could be a good initialization for heuristic methods.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Clipped logistic regression", "weight": 1.0} -->

In this example we apply clipped logistic regression (§2.1) to a dataset with outliers. We generated data by sampling 1000 data points $(x_{i},y_{i})$ from a mixture of two Gaussian distributions in $\text{R}^{5}$. We randomly partitioned the data into 100 training data points and 900 test data points and introduced outliers by flipping the sign of $y_{i}$ for 20 random training data points.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Clipped logistic regression", "weight": 1.0} -->

We (approximately) solved the *clipped logistic regression* problem

<!-- chunk {"id": "body-0060", "role": "body", "section": "Clipped logistic regression", "weight": 1.0} -->

with variables $\theta$ and $b$, for various values of $\alpha \in {\lbrack 10^{- 1},10^{1}\rbrack}$. We also solved the problem for $\alpha = {+ \infty}$, i.e., the *standard logistic regression problem*. Over the $\alpha$ values we tried, on average, algorithm 3 took 6.37 seconds and terminated in 9.64 iterations.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Lane changing", "weight": 1.0} -->

In this example, we consider a control problem where a vehicle traveling down a road at a fixed speed must avoid obstacles, stay in one of two lanes, and provide a comfortable ride. We let $x_{t} \in \text{R}$ denote the lateral position of the vehicle at time $t = {0,\ldots,T}$ ($T$ is the time horizon).

<!-- chunk {"id": "body-0062", "role": "body", "section": "Lane changing", "weight": 1.0} -->

The obstacle avoidance constraints are given as vectors ${x^{\min},x^{\max}} \in \text{R}^{T}$ that represent lower and upper bounds on $x_{t}$ at time $t$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Lane changing", "weight": 1.0} -->

We can split the objective into the sum of two functions described below.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Lane changing", "weight": 1.0} -->

*Lane cost.* Suppose the two lanes are centered at $x = {- 1}$ and $x = 1$. The lane cost is given by

<!-- chunk {"id": "body-0065", "role": "body", "section": "Lane changing", "weight": 1.0} -->

The lane cost incentivizes the vehicle to be in the center of one of the two lanes. The lane cost is evidently a sum of clipped convex functions.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Lane changing", "weight": 1.0} -->

*Comfort cost.* The comfort cost is given by

<!-- chunk {"id": "body-0067", "role": "body", "section": "Lane changing", "weight": 1.0} -->

where $D$ is the difference operator and ${\rho_{1},\rho_{2},\rho_{3}} > 0$ are weights to be chosen. The comfort cost is a weighted sum of the squared lateral velocity, acceleration, and jerk.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Lane changing", "weight": 1.0} -->

To find the optimal lateral trajectory we solve the problem

<!-- chunk {"id": "body-0069", "role": "body", "section": "Lane changing", "weight": 1.0} -->

where ${x^{start},x^{end}} \in \text{R}$ are given starting and ending points of the trajectory.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We use $T = 100$, $\rho_{1} = 10$, $\rho_{2} = 1$, $\rho_{3} =.1$, $x^{start} = 1$, and $x^{end} = {- 1}$. In figure 6 we show the trajectory resulting from an approximate solution to with three obstacles. For this example, algorithm 3 terminated in 1.2 seconds and took 4 iterations. We are able to find a comfortable trajectory that avoid the obstacles and spends as little time as possible in between the lanes.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Lower bound", "weight": 1.0} -->

Using the relaxed version of the perspective formulation, we can compute a lower bound on the objective value of the clipped control problem. We found a lower bound value of around 103.55, while the approximate solution we found had an objective value of 119.07, indicating that our approximate solution is no more than 15% suboptimal.
