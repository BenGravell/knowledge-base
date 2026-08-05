<!-- arxiv-full-text:v1 {"arxiv_id": "1910.12342", "source": "ar5iv"} -->

## Introduction

Suppose $f:{\text{R}^{n}\rightarrow\text{R}}$ is a convex function, and $\alpha \in \text{R}$. We refer to the function $\min{\{{f{(x)}},\alpha\}}$ as a *clipped convex function*. In this paper we consider the problem of minimizing a sum of clipped convex functions, with variable $x \in \text{R}^{n}$, where $f_{0}:{\text{R}^{n}\rightarrow{\text{R} \cup {\{{+ \infty}\}}}}$ and $f_{i}:{\text{R}^{n}\rightarrow\text{R}}$ for $i = {1,\ldots,m}$ are closed proper convex functions, and $\alpha_{i} \in \text{R}$ for $i = {1,\ldots,m}$. We use infinite values of $f_{0}$ to encode constraints on $x$, i.e., to constrain $x \in \mathcal{X}$ for a closed convex set $\mathcal{X}$ we let ${f_{0}{(x)}} = {+ \infty}$ for all $x \notin \mathcal{X}$. When ${f_{i}{(x)}} > \alpha_{i}$, the value of the $i$th term in the sum is *clipped* to $\alpha_{i}$, which limits how large each term in the objective can be. Many practical problems can be formulated as instances of; we describe a few in §2.

### NP-hardness

In general, problem is nonconvex and as a result can be very difficult to solve. Indeed, is NP-hard. We show this by giving a reduction of the subset sum problem to an instance of.

The subset sum problem involves determining whether or not there exists a subset of a given set of integers $a_{1},\ldots,a_{n}$ that sum to zero. The optimal value of the problem which has the form, is zero if and only if $x_{i} \in {\{ 0,1\}}$, at least one of $x_{i} = 1$, and ${a^{T}x} = 0$; in other words, the set $\{ a_{i}\mid{x_{i} = 1}\}$ sums to zero. Since the subset sum problem can be reduced to an instance of, we conclude that in general our problem is at least as hard as difficult problems like the subset sum problem.

### Global solution

There is a simple (exhaustive) method to solve globally: for each subset $\Omega$ of $\{ 1,\ldots,m\}$, we solve the convex problem with variable $x \in \text{R}^{n}$. The solution to with the lowest optimal value is the solution to. This general method is not practical unless $m$ is quite small, since it requires the solution of $2^{m}$ convex optimization problems.

In some specific instances of problem, we can cut down the search space if we know that a specific choice of $\Omega \subseteq {\{ 1,\ldots,m\}}$ implies which means that the optimal value of is $+ \infty$. In this case, we do not have to solve problem for this choice of $\Omega$, as we know it will be infeasible. One simple example where this happens is when the $\alpha_{i}$-sublevel sets of $f_{i}$ are pairwise disjoint, which implies that we only have to solve $m$ convex problems (as opposed to $2^{m}$) to find the global solution. This idea is used in to guide their proposed search algorithm.

### Related work

The general problem of minimizing a sum of clipped convex functions was recently considered . In their paper, they also show that the problem is NP-hard via a reduction to 3-SAT and give a global solution method in a few special cases whenever $n$ is small. They also provide a heuristic method based on cyclic coordinate descent, leveraging the fact that one-dimensional problems are easy to solve.

The idea of using clipped convex functions has appeared in multiple application areas, the most prominent being statistics. For example, the sum of clipped absolute values (often referred to as the *capped* $\ell_{1}$-norm) has been used as a sparsity-inducing regularizer. In particular, make use of the fact that problem can be written as a difference-of-convex (DC) problem and can be approximately minimized via the convex-concave procedure (see Appendix A). The clipped square function (also known as the *skipped-mean* loss) was also used in to estimate view relations, and in to perform robust image restoration. Similar approaches have been taken for clipped loss functions, where they have been used for robust feature selection, regression, classification, and robust principal component analysis.

### Summary

We begin by presenting some applications of minimizing a sum of clipped convex functions in §2 to empirical risk minimization and control. We then provide some simple heuristics for approximately solving in §3, which we have found to work well in practice. In §4, we describe a method for converting into a mixed-integer convex program, which is amenable to solvers for mixed-integer convex programs. Finally, we describe an open-source Python implementation of the ideas described in this paper in §5 and apply our implementation to a few illustrative examples in §6.

## Applications

In this section we describe some possible applications of minimizing a sum of clipped convex functions.

### Clipped empirical risk minimization

Suppose we have data Here $x_{i}$ is the $i$th feature vector, $y_{i}$ is its corresponding output (or label), and $\mathcal{Y}$ is the output space.

We find parameters $\theta \in \text{R}^{n}$ of a linear model given the data by solving the *empirical risk minimization* (ERM) problem with variable $\theta$, where $l:{{\text{R} \times \mathcal{Y}}\rightarrow\text{R}}$ is the loss function, and $r:{\text{R}^{n}\rightarrow\text{R}}$ is the regularization function. Here the objective is composed of two parts: the loss function, which measures the accuracy of the predictions, and the regularization function, which measures the complexity of $\theta$. We assume that $l$ is convex in its first argument and that $r$ is convex, so the problem is a convex optimization problem.

For a given $x \in \text{R}^{n}$, our prediction of $y$ is where $\theta^{\star}$ is optimal. For example, in linear regression, $\mathcal{Y} = \text{R}$, ${l{(z,w)}} = {({z - w})}^{2}$, and $\hat{y} = {x^{T}\theta^{\star}}$; in logistic regression, $\mathcal{Y} = {\{{- 1},1\}}$, ${l{(z,w)}} = {\log{({1 + e^{- {wz}}})}}$, and $\hat{y} = {{\mathbf{s}\mathbf{i}\mathbf{g}\mathbf{n}}{({x^{T}\theta^{\star}})}}$, where ${\mathbf{s}\mathbf{i}\mathbf{g}\mathbf{n}}{(z)}$ is equal to $1$ if $z \geq 0$ and $- 1$ otherwise.

While ERM often works well in practice, it can perform poorly when there are outliers in the data. One way of fixing this is to clip the loss for each data point to a value $\alpha \in \text{R}$, leading to the *clipped ERM* problem, After solving (or approximately solving) the clipped problem, we can label data points $(x_{i},y_{i})$ where ${l{({x_{i}^{T}\theta^{\star}},y_{i})}} \geq \alpha$ as outliers. The clipped ERM problem is an instance of what is referred to in statistics as a *redescending M-estimator* \[8, §4.8\], since the derivative of the clipped loss goes to $0$ as the magnitude of its input goes to infinity. In this terminology, the clip value $\alpha$ is referred to as the *minimum rejection point*.

In §6.1, we show an example where the normal empirical risk minimization problem fails, while its clipped variant has good performance.

### Clipped control

Suppose we have a linear system with dynamics given by where $x_{t} \in \text{R}^{n}$ is the state of the system and $u_{t} \in \text{R}^{p}$ denotes the input to the system, at time period $t$. The dynamics matrix $A \in \text{R}^{n \times n}$ and the input matrix $B \in \text{R}^{n \times m}$ are given.

We are given stage cost functions $g_{t}:{{\text{R}^{n} \times \text{R}^{p}}\rightarrow\text{R}}$, and an initial state $x^{init} \in \text{R}^{n}$. The standard optimal control problem is where, at time $t$, $\mathcal{X}_{t} \subseteq \text{R}^{n}$ is the convex set of allowable states and $\mathcal{U}_{t} \subseteq \text{R}^{m}$ is the convex set of allowable inputs. The variables in this problem are the states and inputs, $x_{t}$ and $u_{t}$. If the stage cost function $g_{t}$ are convex, the optimal control problem is a convex optimization problem.

We define a *clipped optimal control* problem as an optimal control problem in which the stage costs can be expressed as sums of clipped convex functions, i.e., where, for all $t$ and $i = {1,\ldots,K}$, the functions $g_{t}^{i}:{{\text{R}^{n} \times \text{R}^{m}}\rightarrow\text{R}}$ are convex and $\alpha_{t}^{i} \in \text{R}$. This gives another instance of our general problem.

A simple but practical example of a clipped control problem is described in §6.3. The problem is to design a lane change trajectory for a vehicle; the stage cost is small when the vehicle is centered in either lane, which we express as a sum of two clipped convex functions.

## Heuristic methods

There are many methods for approximately solving. In this section we describe a few heuristic methods that we have observed to work well in practice.

### Bi-convex formulation

Throughout this section, we will make use of a simple reformulation of as the bi-convex problem with variables $\lambda \in \text{R}^{m}$ and $x \in \text{R}^{n}$. (We note that this reformulation was also pointed out in \[23, §3\].) The equivalence follows immediately from the fact that

### Nonlinear programming

When $f_{i}$ are all smooth functions and $\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}f_{0}$ is representable as the sublevel set of a smooth function, it is possible to use general nonlinear solvers to (approximately) solve.

### Alternating minimization

Another possibility is to perform alternating minimization, since each respective minimization is a convex optimization problem. In alternating minimization, at iteration $k$, we solve while fixing $\lambda = \lambda^{k - 1}$, resulting in $x^{k}$. We then solve while fixing $x = x^{k}$, resulting in $\lambda^{k}$. It can be shown that is a solution for minimization over $\lambda$ with fixed $x = x^{k}$.

### Inexact alternating minimization

Although alternating minimization often works well, we have found that inexact minimization over $\lambda$ works better in practice. Instead of fully minimizing over $\lambda$, we instead compute the gradient of the objective with respect to $\lambda$, We then perform a signed projected gradient step on $\lambda$ with a fixed step size $\beta > 0$ (we have found $\beta = 0.1$ works well in practice, though a range of values all appear to work equally as well). This results in the update where $\mathbf{s}\mathbf{i}\mathbf{g}\mathbf{n}$ is applied elementwise to $g$, and $\Pi_{{\lbrack 0,1\rbrack}^{m}}$ denotes the projection onto the unit box, given by The final algorithm is described below.

Algorithm 3.1 *Inexact alternating minimization.* Algorithm 3 is a descent algorithm in the sense that the objective function of decreases after every iteration. It is also guaranteed to terminate in a finite amount of time, since there is a finite number of possible values of $\lambda$. We also note that alternating minimization can be thought of as a special case of algorithm 3 where $\beta \geq 1$. In practice, we have found that algorithm 3 often finds the global optimum in simple problems and appears to work well on more complicated cases. We use algorithm 3 in our generic `cvxpy` implementation (see §5).

## Perspective formulation

In this section we describe the perspective formulation of. The perspective formulation is a mixed-integer convex program (MICP), for which specialized solvers with reasonable practical performance exist. The perspective formulation can also be used to compute a lower bound on the original objective by relaxing the integral constraints, as , as well to obtain good initializations for any of the procedures described in §3.

### Perspective

Following \[15, §8\], we define the perspective (or recession) of the closed convex function $f$ with $0 \in {\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}f}$ as^11^1If $0 \notin {\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}f}$, replace $\gammaf_{0}{({x/\gamma})}$ with $\gammaf_{0}{({y + {x/\gamma}})}$ for any $y \in {\operatorname{\mathbf{d}\mathbf{o}\mathbf{m}}f}$. See \[15, Thm. 8.3\] for more details. for ${(x,t)} \in {\text{R}^{n} \times \text{R}_{+}}$. We will use the fact that the resulting function $f^{p}$ is convex \[3, §3.2.6\].

### Superlinearity assumption

If $f$ is superlinear, i.e., if for all $x \in {\text{R}^{n} \smallsetminus {\{ 0\}}}$, we have since the limit in is equal to the limit in unless $x = 0$.

There are many convex functions that satisfy this superlinearity property. Some examples are the sum of squares function and the indicator function of a compact convex set. Since we will make heavy use of property in this section, we will assume that $f_{0}$ is superlinear for the remainder of this section. If $f_{0}$ is not superlinear, then it can be made superlinear by adding, e.g., a small positive multiple of the sum of squares function.

### Conic representation of the perspective

We note that representing the epigraph of the perspective of a function is often simple if the function has a conic representation. More specifically, if $f$ has a conic representation for some closed convex cone $\mathcal{K}$, then the perspective of $f$ has a conic representation given by This fact allows us to use a conic representation of the perspective and avoid issues of non-differentiability and division-by-zero that we might encounter with direct numerical implementations of the perspective \[12, §2\].

### Perspective formulation

We define the *perspective formulation* of as the following MICP: with variables ${x,z_{i}} \in \text{R}^{n}$ for $i = {1,\ldots,m}$ and $t \in \text{R}^{m}$. Any MICP solver that can handle the functions $f_{i}^{p}$ for $i = {0,\ldots,m}$ can be used to solve.

### Proof of equivalence

To show that is equivalent to the original problem, first take $(x,t,z_{i})$ that are feasible. Since $t$ is Boolean, for each $i$ we have $t_{i} = 0$ or $t_{i} = 1$. Since $f_{0}^{p}{(z_{i},t_{i})}$ must be finite (as this point is feasible), then $t_{i} = 0$ implies that $z_{i} = 0$ (due to). Similarly, when $t_{i} = 1$ we must have $z_{i} = x$. Therefore the $i$th term in the sum becomes Summing over the index $i$ yields that problem is equivalent to Partially minimizing over $t$, we find that $x$ is a feasible point for with the same objective value.

Now take $x$ feasible. Let and $z_{i} = {t_{i}x}$. Then $(x,t,z_{i})$ is feasible for and has the same objective value, and the problems are equivalent.

### Lower bound via relaxation

Since the perspective formulation is equivalent to the original problem, relaxing the Boolean constraint in and solving the resulting convex optimization problem with variables $z_{i}$, $t$, and $x$, yields a lower bound on the objective value of. That is, given any approximate solution of with objective value $p$, the optimal value $q^{\star}$ of yields a certificate guaranteeing that the approximate solution is suboptimal by at most $p - q^{\star}$. Additionally, a solution of the relaxed problem can be used as an initial point for any of the heuristic methods described in §3.

### Efficiently solving the relaxed problem

We note that has $m + 1$ times as many variables as the original problem, so it is worth considering faster solution methods. To do so, we can convert the problem to *consensus form* \[2, §7.1\]; i.e., we introduce additional variables $y_{i} \in \text{R}^{n}$ for $i = {1,\ldots,m}$, and constrain $y_{i} = x$, resulting in the equivalent problem Since the objective is separable in $(y_{i},z_{i},t_{i})$ over $i$, there exist many efficient distributed algorithms for solving this problem, e.g., the alternating direction method of multipliers (ADMM).

## Implementation

Our Python package `sccf` approximately solves generic problems of the form provided all $f_{i}$ can be represented as valid `cvxpy` expressions and constraints. It is available: We provide a method `sccf.minimum`, which can be applied to a `cvxpy` Expression and a scalar to create a `sccf.MinExpression`. The user then forms an objective as a sum of `sccf.MinExpression`s, passes this objective and (possibly) constraints to a `sccf.Problem` object, and then calls the `solve` method, which implements algorithm 3. We take advantage of the fact that the only parameter changing between problems is $\lambda$ by caching the canonicalization procedure. Here is an example of using `sccf` to solve a clipped least squares problem: objective += sccf.minimum(cp.square(A[i]@x-b[i]), 1.0) objective += 0.01 * cp.sum_squares(x) prob = sccf.Problem(objective)

## Examples

All experiments were conducted on a single core of an Intel i7-8700K CPU clocked at 3.7 GHz.

### Clipped regression

In this example we compare clipped regression (§2.1) with standard linear regression and Huber regression (a well known technique for robust regression) on a one-dimensional dataset with outliers. We generated data by sampling 20 data points $(x_{i},y_{i})$ according to We introduced outliers in our data by flipping the sign of $y_{i}$ for 5 random data points.

The problems all have the form where $\phi:{\text{R}\rightarrow\text{R}}$ is a penalty function. In clipped regression, ${\phi{(z)}} = {\min{\{ z^{2},0.5\}}}$. In linear regression, ${\phi{(z)}} = z^{2}$. In Huber regression, Figure 1: Clipped regression, linear regression, and Huber regression on a one-dimensional dataset with outliers. The outliers affect the linear regression and Huber regression models, while the clipped regression model appears to be minimally affected.

Let $\theta^{clip}$ be the clipped regression model; we deem points where ${({{x_{i}\theta^{clip}} - y_{i}})}^{2} \geq 0.5$ as outliers and the remaining points as inliers. In figure 1 we visualize the data points and the resulting models along with the outliers/inliers identified by the clipped regression model. In this figure, the clipped regression model clearly outperforms the linear and Huber regression models since it is able to fully ignore the outliers. Algorithm 3 terminated in 0.13 seconds and took 8 iterations on this instance.

### Lower bound

The relaxed version of the perspective formulation can be used to efficiently find a lower bound on the objective value for the clipped version of. The objective value of for clipped regression was 1.147, while the lower bound we calculated was 0.533, meaning our approximate solution is suboptimal by at most 0.614.

In figure 2 we plot the clipped objective for various values of $\theta$; note that the function is highly nonconvex and that $\theta^{clip}$ is the (global) solution. We also plot the objective of the perspective relaxation as a function of $\theta$, found by partially minimizing over $z_{i}$ and $t$; note that the function is convex and a surprisingly good approximation of the true convex envelope. We note that the minimum of the perspective relaxation and the true minimum are surprisingly close, leading us to believe that the solution to the perspective relaxation could be a good initialization for heuristic methods.

Figure 2: The clipped regression loss and its perspective relaxation.

### Clipped logistic regression

In this example we apply clipped logistic regression (§2.1) to a dataset with outliers. We generated data by sampling 1000 data points $(x_{i},y_{i})$ from a mixture of two Gaussian distributions in $\text{R}^{5}$. We randomly partitioned the data into 100 training data points and 900 test data points and introduced outliers by flipping the sign of $y_{i}$ for 20 random training data points.

We (approximately) solved the *clipped logistic regression* problem with variables $\theta$ and $b$, for various values of $\alpha \in {\lbrack 10^{- 1},10^{1}\rbrack}$. We also solved the problem for $\alpha = {+ \infty}$, i.e., the *standard logistic regression problem*. Over the $\alpha$ values we tried, on average, algorithm 3 took 6.37 seconds and terminated in 9.64 iterations.

Figure 3: Test accuracy of clipped logistic regression (solid), test accuracy of standard logistic regression (gray), and fraction of outliers (dotted dashed) for varying clip values α. Note that the fraction of detected outliers goes down as α goes up. Between roughly α = 10−.5 and α = 100.05, the test accuracy of clipped logistic regression is higher than standard logistic regression. Clipped logistic regression converges to standard logistic regression as α → ∞.

Figure 4: A plot of λ throughout the course of algorithm 3 for the clipped logistic regression example. Note that at some of the iterations (e.g., k = 1, 2, or 3), the gradient of the loss with respect to a certain λi changes sign, causing λi to be updated in the opposite direction.

Figure 3 displays the test loss and fraction of outliers over the range of values of $\alpha$ we approximately minimized. Figure 4 shows the trajectory of the entries of $\lambda$ during each step of the execution of algorithm 3 for the $\alpha$ with the highest test accuracy, while figure 4 plots the histogram of the logistic loss for each of the available data points for this same $\alpha$.

Figure 5: Left: histogram of log logistic loss for each data point in standard logistic regression; right: histogram of log logistic loss for each data point in clipped logistic regression. Note that standard logistic regression attempts to make the loss small for all data points, while its clipped counterpart allows the loss to be high for some of the data points.

### Lane changing

In this example, we consider a control problem where a vehicle traveling down a road at a fixed speed must avoid obstacles, stay in one of two lanes, and provide a comfortable ride. We let $x_{t} \in \text{R}$ denote the lateral position of the vehicle at time $t = {0,\ldots,T}$ ($T$ is the time horizon).

The obstacle avoidance constraints are given as vectors ${x^{\min},x^{\max}} \in \text{R}^{T}$ that represent lower and upper bounds on $x_{t}$ at time $t$.

We can split the objective into the sum of two functions described below.

*Lane cost.* Suppose the two lanes are centered at $x = {- 1}$ and $x = 1$. The lane cost is given by The lane cost incentivizes the vehicle to be in the center of one of the two lanes. The lane cost is evidently a sum of clipped convex functions.

*Comfort cost.* The comfort cost is given by where $D$ is the difference operator and ${\rho_{1},\rho_{2},\rho_{3}} > 0$ are weights to be chosen. The comfort cost is a weighted sum of the squared lateral velocity, acceleration, and jerk.

To find the optimal lateral trajectory we solve the problem where ${x^{start},x^{end}} \in \text{R}$ are given starting and ending points of the trajectory.

Figure 6: Trajectory of a vehicle looking to avoid obstacles (represented by boxes) while optimizing for comfort and lane position.

### Numerical example

We use $T = 100$, $\rho_{1} = 10$, $\rho_{2} = 1$, $\rho_{3} =.1$, $x^{start} = 1$, and $x^{end} = {- 1}$. In figure 6 we show the trajectory resulting from an approximate solution to with three obstacles. For this example, algorithm 3 terminated in 1.2 seconds and took 4 iterations. We are able to find a comfortable trajectory that avoid the obstacles and spends as little time as possible in between the lanes.

### Lower bound

Using the relaxed version of the perspective formulation, we can compute a lower bound on the objective value of the clipped control problem. We found a lower bound value of around 103.55, while the approximate solution we found had an objective value of 119.07, indicating that our approximate solution is no more than 15% suboptimal.
