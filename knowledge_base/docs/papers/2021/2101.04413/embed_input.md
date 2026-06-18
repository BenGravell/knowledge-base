<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Regularized Limited Memory BFGS Method for Large-Scale Unconstrained Optimization and Its Efficient Implementations

Topics include Robustness, Optimization, Limited memory BFGS, L-BFGS, Line search.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The limited memory BFGS (L-BFGS) method is one of the popular methods for solving large-scale unconstrained optimization. Since the standard L-BFGS method uses a line search to guarantee its global convergence, it sometimes requires a large number of function evaluations. To overcome the difficulty, we propose a new L-BFGS with a certain regularization technique. We show its global convergence under the usual assumptions. In order to make the method more robust and efficient, we also extend it with several techniques such as nonmonotone technique and simultaneous use of the Wolfe line search. Finally, we present some numerical results for test problems in CUTEst, which show that the proposed method is robust in terms of solving number of problems.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

---l--- x∈R\^nf(x), where $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is a smooth function. For solving it, we focus on the quasi-Newton type method as

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The standard solution methods to solve such as the steepest descent method, Newton's method and the BFGS method are not suitable for large-scale problems. This is because the steepest descent method generally converges slowly, while Newton's method needs to compute the Hessian matrix and solve linear equations at each iteration. Moreover, the BFGS method requires $O{(n^{2})}$ memory to store and calculate the approximate Hessian of $f$, which causes some difficulty for large-scale problem.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

One of the popular quasi-Newton methods for solving large-scale problem is the limited memory BFGS(L-BFGS), which uses small memory to store an approximate Hessian of $f$. The L-BFGS method stores the last $m$ vector pairs of ${(s_{k - i},y_{k - i})},$ ${i = {0,1,\ldots,{m - 1}}},$ to compute a search direction $d_{k}$, where

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The usual L-BFGS adopts the Wolfe line search to guarantee its global convergence. The line search sometimes needs a large number of function evaluations. Thus, it is preferable to reduce the number of function evaluations as much as possible.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The trust region method (TR-method) can guarantee the global convergence. It is known that the TR-method needs fewer function evaluations than the line search. The L-BFGS method combined with the TR-method produces good performance for many benchmark problems in terms of the number of function evaluations. However, the TR-method must solve the constrained subproblem

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

in each step, where $\Delta_{k}$ is the trust-region radius and $B_{k}$ is an approximate Hessian obtained by L-BFGS. It takes a considerable amount of time to solve (1.1).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

To overcome the difficulty we consider adopting a regularization technique instead of the TR-method. This is motivated by the regularized Newton method proposed by Ueda and Yamashita.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $\mu_{k} > 0$ is called a regularized parameter. If $\mu_{k}$ coincides with the value of the optimal Lagrange multiplier at a solution of problem (1.1), then $d$ is a solution of (1.1). Note that the linear equations (1.2) are simpler than subproblem (1.1) of the TR-method. The regularized Newton method controls the parameter $\mu_{k}$ instead of computing the step length to guarantee global convergence. However, since the regularized Newton method in is based on Newton's method, it must compute the Hessian matrix of $f$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we propose a novel approach that combines the L-BFGS method with the regularization technique. We call the proposed method regularized L-BFGS method. One of natural ways to implement the idea is to use a solution of the following equations as a search direction,

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Note that the term $\mus_{k}$ in ${\hat{y}}_{k}{(\mu)}$ plays the role of regularization. Then, the search direction $d_{k}$ can be computed in $O{({mn})}$ time like the conventional L-BFGS method. For global convergence, we also control the regularized parameter $\mu_{k}$ in a way similar to the regularized Newton method. We then show that the proposed algorithm ensures global convergence.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

A drawback of the proposed method is that a step $d_{k}$ sometimes becomes small, and it causes a large number of iterations. To get a longer step, we propose two techniques: a nonmonotone technique and a simultaneous use of the Wolfe line search. Recall that the step length given by the Wolfe condition is allowed to be larger than 1, and hence the step can explore a larger area. Thus, if ${f{({x_{k} + {\alphad_{k}}})}} < {f{({x_{k} + d_{k}})}}$ for $\alpha > 1$, it would be reasonable to find $\alpha$ via the Wolfe line search.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

The paper is organized as follows. The regularized L-BFGS is presented in section 2, and its global convergence is shown in section 3. In section 4 we discuss some implementation issues, such as a simultaneous use of RL-BFGS and a nonmonotone technique. In section 5, we present numerical results by comparing three algorithms: the L-BFGS, the regularized L-BFGS, and the regularized L-BFGS with line search. Section 6 concludes the paper.

<!-- chunk {"id": "body-0015", "role": "body", "section": "The regularized L-BFGS method", "weight": 1.0} -->

In this section, we propose a regularized L-BFGS method that controls the regularized parameter at each iteration. In the following, $x_{k}$ denotes the $k$-th iterative point, $B_{k}$ denotes the approximate Hessian of $f{(x_{k})}$, and $H_{k}^{- 1} = B_{k}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "The regularized L-BFGS method", "weight": 1.0} -->

We consider combining the L-BFGS method with the regularized Newton method (1.2). For this purpose, we may replace the Hessian ${\nabla^{2}f}{(x_{k})}$ in equation (1.2) with the approximate Hessian $B_{k}$, that is, we define a search direction $d_{k}$ as a solution of

<!-- chunk {"id": "body-0017", "role": "body", "section": "The regularized L-BFGS method", "weight": 1.0} -->

However, since the L-BFGS method updates $H_{k}$, it is not easy to construct $B_{k}$ explicitly. Furthermore, even if we obtain $B_{k}$, it takes a considerable amount of time to solve the linear equation (2.1) in large-scale cases.

<!-- chunk {"id": "body-0018", "role": "body", "section": "The regularized L-BFGS method", "weight": 1.0} -->

The proposed method generates the next iterate as $x_{k + 1} = {x_{k} + {d_{k}{(\mu)}}}$ without a step length. We control the parameter $\mu$ to guarantee the global convergence as. We exploit the idea of updating the trust-region radius in the TR-method to control $\mu$ to find an appropriate search direction, that is, we use the ratio of the reduction in the objective function value to that of the model function value. We define a ratio function $r_{k}{({d_{k}{(\mu)}},\mu)}$ by

<!-- chunk {"id": "body-0019", "role": "body", "section": "The regularized L-BFGS method", "weight": 1.0} -->

Based on the above ideas, we propose the following regularized L-BFGS method.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Algorithm 2.1", "weight": 1.0} -->

: If some stopping criteria are satisfied, then terminate. Otherwise go to step 2.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Algorithm 2.1", "weight": 1.0} -->

In Step 2-1 we compute $d_{k}{(\mu)}$ from $(s_{k},{{\hat{y}}_{k}{(\mu)}})$ by the L-BFGS updating scheme. The details of step 2-1 are given as follows.\

<!-- chunk {"id": "body-0022", "role": "body", "section": "Algorithm 2.2", "weight": 1.0} -->

: Repeat the following process with ${i = {{k - 1},{k - 2},\ldots,{k - l}}};$

<!-- chunk {"id": "body-0023", "role": "body", "section": "Algorithm 2.2", "weight": 1.0} -->

: Repeat the following process with ${i = {{k - t},{{k - t} + 1},\ldots,{k - 1}}};$

<!-- chunk {"id": "body-0024", "role": "body", "section": "Algorithm 2.2", "weight": 1.0} -->

It is important to note that when $\mu$ varies, the regularized L-BFGS does not have to store ${\hat{y}}_{k}{(\mu)}$ because the L-BFGS stores $s_{k}$ and $y_{k}$ explicitly, and thus we can get ${\hat{y}}_{k}{(\mu)}$ immediately.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Global convergence", "weight": 1.0} -->

In this section, we show the global convergence of the proposed algorithm. To this end, we need the following assumptions.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

: \(i\) The objective function $f$ is twice continuously differentiable.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

: \(iii\) There exist positive constants $M_{1}$ and $M_{2}$ such that

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

: \(v\) There exists a constant $\underset{¯}{\gamma}$ such that $\gamma_{k} \geq \underset{¯}{\gamma} > 0$ for all $k$, where $\gamma_{k}$ is a parameter in (2.2).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

The above assumptions are the same as those for the global convergence of the original L-BFGS method.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

Under these assumptions, we have the following several properties. First, let

<!-- chunk {"id": "body-0031", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

It then follows from Taylor's theorem that

<!-- chunk {"id": "body-0032", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

Since the sequence $\{ x_{k}\}$ is included in the compact set $\Omega$ and $f$ is twice continuously differentiable under Assumption 3.1 (i) and (ii), there exists a positive constant $L_{f}$ such that

<!-- chunk {"id": "body-0033", "role": "body", "section": "Implementation issues", "weight": 1.0} -->

The regularized L-BFGS method does not use a line search, and hence it can not take a longer step. Moreover in our experience, the trust-region ratio of the regularized L-BFGS does not improve well and the regularized parameter $\mu$ becomes very large for some large-scale test problems. Both cases result in a short step, and hence the method conducts a large number of iteration to reach a solution. To overcome this difficulty we propose two techniques in this section. We also discuss how to set $\gamma_{k}$ in the initial matrix ${\hat{H}}_{k}{(\mu)}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Simultaneous use with Wolfe line search", "weight": 1.0} -->

The next iterate with line search is given as

<!-- chunk {"id": "body-0035", "role": "body", "section": "Simultaneous use with Wolfe line search", "weight": 1.0} -->

where $\alpha_{k}$ is a step length. The usual L-BFGS uses a step length $\alpha_{k}$ that satisfies the Wolfe conditions,

<!-- chunk {"id": "body-0036", "role": "body", "section": "Simultaneous use with Wolfe line search", "weight": 1.0} -->

where $0 < c_{1} < c_{2} < 1$. Note that $\alpha_{k}$ can be larger than 1. Thus, $\alpha_{k}d_{k}$ might be larger, and make a large reduction of $f$. Thus, it might be reasonable to use a line search as well as the regularization technique. However, finding $\alpha_{k}$ takes much time, and hence we must avoid it if $\alpha_{k}d_{k}$ does not enough improvement.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Simultaneous use with Wolfe line search", "weight": 1.0} -->

For the efficient use of the line search, we exploit curvature condition (4.3). It is known that the curvature condition ensures that the step is not too short. Therefore, after step 3 of Algorithm 2.1, we first check weather $x_{k} + {d_{k}{(\mu)}}$ satisfies curvature condition ($\alpha_{k} = 1$ in (4.3)) or not. The dissatisfaction of the curvature condition implies that $x_{k} + {d_{k}{(\mu)}}$ is a short step. Thus, we compute $\alpha_{k}$ by the strong Wolfe condition so that we can take a longer step.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Simultaneous use with Wolfe line search", "weight": 1.0} -->

We now discuss the conditions under which we conduct the Wolfe line search. As mentioned above, we exploit the strong Wolfe condition (4.3) when the following conditions hold,

<!-- chunk {"id": "body-0039", "role": "body", "section": "Simultaneous use with Wolfe line search", "weight": 1.0} -->

Note that ${\|{d_{k}{(\mu_{min})}}\|} \geq {\|{d_{k}{(\mu)}}\|}$ if $\mu > \mu_{min}$. Thus, $d_{k}{(\mu_{min})}$ is the largest step when we apply RL-BFGS only. Condition (4.5) implies whenever $x_{k} + {d_{k}{(\mu_{min})}}$ to make better progress, we take a longer step via a strong Wolfe line search. We call this method regularized L-BFGS with strong Wolfe line search method (RL-BFGS-SW) as an extended version of the proposed method. Now, we propose the RL-BFGS-SW as follows.\

<!-- chunk {"id": "body-0040", "role": "body", "section": "Algorithm 4.1", "weight": 1.0} -->

RL-BFGS with line search (RL-BFGS-SW)\

<!-- chunk {"id": "body-0041", "role": "body", "section": "Algorithm 4.1", "weight": 1.0} -->

: If some stopping criteria are satisfied, then terminate. Otherwise go to step 2.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Algorithm 4.1", "weight": 1.0} -->

Note that we do not need to evaluate a new function and gradient values for conditions (4.5) since we have the gradient and function values to calculate the ratio $r_{k}{({d_{k}{(\mu)}},\mu_{k})}$. Note also that Algorithm 4.1 still has the global convergence property since ${f{({x_{k} + {d_{k}{(\mu)}}})}} > {f{({x_{k} + {{({1 + \alpha_{k}})}d_{k}{(\mu)}}})}}$ from (4.2) and (4.5).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Nonmonotone decreasing technique", "weight": 1.0} -->

In Algorithm 2.1, we control the regularized parameter $\mu$ to satisfy the descent condition ${f{(x_{k + 1})}} < {f{(x_{k})}}$. However, $\mu$ sometimes becomes quite large for some ill-posed problems. In this situation, we require a large number of function evaluations. Therefore, we use the concept of a nonmonotone line search technique to overcome the difficulty.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Nonmonotone decreasing technique", "weight": 1.0} -->

and $M$ is a nonnegative integer constant. This modification retains the global convergence of the regularized L-BFGS method.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Nonmonotone decreasing technique", "weight": 1.0} -->

In the numerical experiments reported in the next section, when $k < M$, we use the original ratio function $r_{k}{({d_{k}{(\mu)}},\mu)}$, and if $k \geq M$ then we use the new ratio function ${\overline{r}}_{k}{({d_{k}{(\mu)}},\mu)}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Scaling initial matrix", "weight": 1.0} -->

The parameter $\gamma_{k}$ represents the scale of ${\nabla^{2}f}{(x)}$. Thus, we exploit the scaling parameter $\gamma_{k}$ used, that is, we set

<!-- chunk {"id": "body-0047", "role": "body", "section": "Numerical results", "weight": 1.0} -->

In this section, we compare the L-BFGS, the regularized L-BFGS (RL-BFGS), and the regularized L-BFGS with line search (RL-BFGS-SW). For the regularized ones, we adopt the nonmonotone techniques and the initial matrix discussed in Section 4. We have used MCSRCH (Line search routine) and parameters of the original L-BFGS to find a step length in the RL-BFGS-SW.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Numerical results", "weight": 1.0} -->

We have solved 313 problems chosen from CUTEst. All algorithms were coded in MATLAB 2018a. We have used Intel Core i5 1.8 GHz CPU with 8 GB RAM on Mac OS. We have chosen an initial point $x_{0}$ given in CUTEst.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Numerical results", "weight": 1.0} -->

We set the same termination criteria as in the original L-BFGS, that is,

<!-- chunk {"id": "body-0050", "role": "body", "section": "Numerical results", "weight": 1.0} -->

where $n_{f}$ is the number of function evaluations. These criteria are similar to those. We regard the trails as fail when $n_{f} > 10000$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Numerical results", "weight": 1.0} -->

We compare the algorithms from the distribution function proposed. Let $\mathcal{S}$ be a set of solvers and let $\mathcal{P}_{\mathcal{S}}$ be a set of problems that can be solved by all algorithms in $\mathcal{S}$. We measure required evaluations to solve problem $p$ by solver $s \in \mathcal{S}$ as $t_{p,s}$, and the best $t_{p,s}$ for each $p$ as $t_{p}^{\ast},$ which means $t_{p}^{\ast} = {\text{min}\left. \{ t_{p,s} \middle| {s \in \mathcal{S}}\} \right.}$. The distribution function $F_{s}^{\mathcal{S}}{(\tau)}$, for a method $s$ is defined,

<!-- chunk {"id": "body-0052", "role": "body", "section": "Numerical results", "weight": 1.0} -->

The algorithm whose $F_{s}^{\mathcal{S}}{(\tau)}$ is close to 1 is considered to be superior compare to other algorithm in $\mathcal{S}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Numerical behavior for some parameters in RL-BFGS", "weight": 1.0} -->

Since the RL-BFGS uses several parameters, we need to investigate the effect of these parameters so that we choose optimal ones.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Numerical behavior for some parameters in RL-BFGS", "weight": 1.0} -->

First we consider $\gamma_{1}$ and $\gamma_{2}$ that control regularized parameters. We perform numerical experiments with $9$ different sets of $(\gamma_{1},\gamma_{2})$ in Table 5.1. The remaining parameters are set to

<!-- chunk {"id": "body-0055", "role": "body", "section": "Numerical behavior for some parameters in RL-BFGS", "weight": 1.0} -->

Table 5.1 shows the number of success and rate of success for all $313$ problems. Figure 5.3 shows the distribution function of these parameter sets in terms of the CPU time.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Numerical behavior for some parameters in RL-BFGS", "weight": 1.0} -->

Table 5.1: The number of success and rate of success at each (γ1,γ2).

<!-- chunk {"id": "body-0057", "role": "body", "section": "Numerical behavior for some parameters in RL-BFGS", "weight": 1.0} -->

From Table 5.1 and Figure 5.3 it is clear that ${(\gamma_{1},\gamma_{2})} = {(0.1,10.0)}$ is the best. Therefore, we set $\gamma_{1} = 0.1$ and $\gamma_{2} = 10.0$ for all further experiments.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Numerical behavior for some parameters in RL-BFGS", "weight": 1.0} -->

Next, we compare the number $m$ of vector pairs in the L-BFGS procedure. Note that the original L-BFGS usually choose it in $3 \leq m \leq 7$. Thus, we compare $m = {3,5,7}$. The remaining parameters are set to

<!-- chunk {"id": "body-0059", "role": "body", "section": "Numerical behavior for some parameters in RL-BFGS", "weight": 1.0} -->

Table 5.2: The number of success and rate of success at each m.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Numerical behavior for some parameters in RL-BFGS", "weight": 1.0} -->

From Table 5.2 we see that $m = 7$ is the best, while Figure 5.3 shows that $m = 5$ is initially better in terms of CPU time. Therefore, we set $m = 5$ for further experiments.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Numerical behavior for some parameters in RL-BFGS", "weight": 1.0} -->

Finally, we compare the behavior of nonmonotone parameters $M$. We compare $M = {0,4,6,8,10,12}$. Note that $M = 0$ implies the usual monotone decreasing case. The remaining parameters are set to

<!-- chunk {"id": "body-0062", "role": "body", "section": "Numerical behavior for some parameters in RL-BFGS", "weight": 1.0} -->

From Table 5.3 and Figure 5.3 it is clear that $M = 10$ is better. Therefore, we use $M = 10$ in the next section.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Numerical behavior for some parameters in RL-BFGS", "weight": 1.0} -->

Table 5.3: The number of success and rate of success at each M.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Comparisons of RL-BFGS-SW, RL-BFGS and L-BFGS method", "weight": 1.0} -->

We compare the RL-BFGS-SW, the RL-BFGS and the L-BFGS methods in terms of function evaluations and CPU time.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Comparisons of RL-BFGS-SW, RL-BFGS and L-BFGS method", "weight": 1.0} -->

Table 5.4 shows the results of the number of successes and rate of successes for all 313 test problems. Figures 5.5 and 5.5 show the results of $\mathcal{P}_{\mathcal{S}}$ in terms of function evaluations and CPU time, respectively. Here $\mathcal{S}$ is the set of problems that are solved by all three algorithms.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Comparisons of RL-BFGS-SW, RL-BFGS and L-BFGS method", "weight": 1.0} -->

Table 5.4: The number of success and rate of success for 313 problems.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Comparisons of RL-BFGS-SW, RL-BFGS and L-BFGS method", "weight": 1.0} -->

Table 5.4 shows that L-BFGS can solve 71.9% of test problems while both RL-BFGS and RL-BFGS-SW can solve 83.4% of problems. On the other hand, Figures 5.5 and 5.5 show that L-BFGS is faster than the regularized ones for the solved problems.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Comparisons of RL-BFGS-SW, RL-BFGS and L-BFGS method", "weight": 1.0} -->

We define the large-scale problem whose dimension is over or equal to $1000$. Table 5.5 shows the number of success and rate of success for the 151 large-scale problems. Furthermore, Figures 5.7 and 5.7 shows performances for $\mathcal{P}_{\mathcal{S}^{large}}$, where $\mathcal{P}_{\mathcal{S}^{large}}$ denotes all the 151 large-scale test problems from the $\mathcal{P}_{\mathcal{S}}$.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Comparisons of RL-BFGS-SW, RL-BFGS and L-BFGS method", "weight": 1.0} -->

Table 5.5: The number of success and rate of success for 151 large-scale problems.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Comparisons of RL-BFGS-SW, RL-BFGS and L-BFGS method", "weight": 1.0} -->

Table 5.5 shows that the L-BFGS can solve 70.9% of test problems while both the RL-BFGS and RL-BFGS-SW can solve 82.8% of test problems. It concludes that both proposed methods can solve more number of test problems as compare to the L-BFGS. On the other hand the above figures show that the L-BFGS requires fewer function evaluations than the proposed method.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Comparisons of RL-BFGS-SW, RL-BFGS and L-BFGS method", "weight": 1.0} -->

The above numerical results indicate that the numerical behaviors of the RL-BFGS and the RL-BFGS-SW are almost same. To see the differences we present the numerical results which compare the performance of each test problem.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Comparisons of RL-BFGS-SW, RL-BFGS and L-BFGS method", "weight": 1.0} -->

We observed that the RL-BFGS-SW performs the line search for 93 problems, and does not use it for the remaining problems. Therefore, we compare the results for those 93 problems. Table 5.6 shows the comparison in terms of the number of function evaluations and Algorithm X $<$ Algorithm Y means that the number of function evaluations of the Algorithm X is fewer than that of the Algorithm Y. From the Table 5.6 we see that RL-BFGS-SW requires fewer number of function evaluations than that of RL-BFGS for 38 test problems while RL-BFGS requires fewer number of function evaluations than that of RL-BFGS-SW for 34 test problems among 93 test problems. Moreover, for the large-scale test problems, RL-BFGS-SW requires fewer number of function evaluations than that of RL-BFGS for 13 test problems while RL-BFGS requires fewer number of the function evaluations than that of RL-BFGS-SW for 20 test problems among 39 large-scale test problems. It concludes that the RL-BFGS with line search works well for some problems.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Comparisons of RL-BFGS-SW, RL-BFGS and L-BFGS method", "weight": 1.0} -->

Table 5.6: comparison for 93 problems solved by at least one algorithm (RL-BFGS or RL-BFGS-SW) in terms of nf.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper we have proposed a combination of the L-BFGS and the regularization technique. We showed the global convergence under appropriate assumptions. We have also presented some efficient implementations. In numerical results, the overall comparison shows that the proposed method can solve more problems than the original L-BFGS. This result indicates that the proposed method is robust in terms of solving number of problems.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Conclusion", "weight": 1.5} -->

For future work, we may consider proposing the stochastic version of the proposed method to solve empirical risk minimization problems.
