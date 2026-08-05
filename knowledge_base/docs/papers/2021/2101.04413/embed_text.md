<!-- arxiv-full-text:v1 {"arxiv_id": "2101.04413", "source": "ar5iv"} -->

## Introduction

In this paper we consider the large-scale unconstrained optimization problem: ---l--- x∈R\^nf(x), where $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is a smooth function. For solving it, we focus on the quasi-Newton type method as where $x_{k} \in {\mathbb{R}}^{n}$ is the $k^{th}$ iteration and $d_{k} \in {\mathbb{R}}^{n}$ denotes a search direction obtained by a certain quasi-Newton method.

The standard solution methods to solve such as the steepest descent method, Newton's method and the BFGS method are not suitable for large-scale problems. This is because the steepest descent method generally converges slowly, while Newton's method needs to compute the Hessian matrix and solve linear equations at each iteration. Moreover, the BFGS method requires $O{(n^{2})}$ memory to store and calculate the approximate Hessian of $f$, which causes some difficulty for large-scale problem.

One of the popular quasi-Newton methods for solving large-scale problem is the limited memory BFGS(L-BFGS), which uses small memory to store an approximate Hessian of $f$. The L-BFGS method stores the last $m$ vector pairs of ${(s_{k - i},y_{k - i})},$ ${i = {0,1,\ldots,{m - 1}}},$ to compute a search direction $d_{k}$, where and computes $d_{k}$ in $O{({mn})}$ time.

The usual L-BFGS adopts the Wolfe line search to guarantee its global convergence. The line search sometimes needs a large number of function evaluations. Thus, it is preferable to reduce the number of function evaluations as much as possible.

The trust region method (TR-method) can guarantee the global convergence. It is known that the TR-method needs fewer function evaluations than the line search. The L-BFGS method combined with the TR-method produces good performance for many benchmark problems in terms of the number of function evaluations. However, the TR-method must solve the constrained subproblem in each step, where $\Delta_{k}$ is the trust-region radius and $B_{k}$ is an approximate Hessian obtained by L-BFGS. It takes a considerable amount of time to solve (1.1).

To overcome the difficulty we consider adopting a regularization technique instead of the TR-method. This is motivated by the regularized Newton method proposed by Ueda and Yamashita. The method computes a search direction $d_{k}$ as a solution of the following linear equations: where $\mu_{k} > 0$ is called a regularized parameter. If $\mu_{k}$ coincides with the value of the optimal Lagrange multiplier at a solution of problem (1.1), then $d$ is a solution of (1.1). Note that the linear equations (1.2) are simpler than subproblem (1.1) of the TR-method. The regularized Newton method controls the parameter $\mu_{k}$ instead of computing the step length to guarantee global convergence. However, since the regularized Newton method in is based on Newton's method, it must compute the Hessian matrix of $f$.

In this paper we propose a novel approach that combines the L-BFGS method with the regularization technique. We call the proposed method regularized L-BFGS method. One of natural ways to implement the idea is to use a solution of the following equations as a search direction, where $B_{k}$ is an approximate Hessian given by a certain quasi-Newton method. However when $B_{k}$ is calculated by the L-BFGS method, it is difficult to compute ${({B_{k} + {\muI}})}^{- 1}$. Therefore, we try to directly construct ${({B_{k} + {\muI}})}^{- 1}$ by the L-BFGS method for ${f{(x)}} + {\mu{\| x\|}^{2}}$, that is we use $(s_{k},{{\hat{y}}_{k}{(\mu)}})$, where ${{\hat{y}}_{k}{(\mu)}} = {y_{k} + {\mus_{k}}}$, instead of $(s_{k},y_{k})$. Note that the term $\mus_{k}$ in ${\hat{y}}_{k}{(\mu)}$ plays the role of regularization. Then, the search direction $d_{k}$ can be computed in $O{({mn})}$ time like the conventional L-BFGS method. For global convergence, we also control the regularized parameter $\mu_{k}$ in a way similar to the regularized Newton method. We then show that the proposed algorithm ensures global convergence.

A drawback of the proposed method is that a step $d_{k}$ sometimes becomes small, and it causes a large number of iterations. To get a longer step, we propose two techniques: a nonmonotone technique and a simultaneous use of the Wolfe line search. Recall that the step length given by the Wolfe condition is allowed to be larger than 1, and hence the step can explore a larger area. Thus, if ${f{({x_{k} + {\alphad_{k}}})}} < {f{({x_{k} + d_{k}})}}$ for $\alpha > 1$, it would be reasonable to find $\alpha$ via the Wolfe line search.

The paper is organized as follows. The regularized L-BFGS is presented in section 2, and its global convergence is shown in section 3. In section 4 we discuss some implementation issues, such as a simultaneous use of RL-BFGS and a nonmonotone technique. In section 5, we present numerical results by comparing three algorithms: the L-BFGS, the regularized L-BFGS, and the regularized L-BFGS with line search. Section 6 concludes the paper.

Throughout the paper, we use the following notations. For a vector $x \in {\mathbb{R}}^{n}$, $\| x\|$ denotes the Euclidean norm defined by ${\| x\|}:=\sqrt{x^{T}x}$. For a symmetric matrix $M \in {\mathbb{R}}^{n \times n}$, we denote the maximum and minimum eigenvalues of $M$ as $\lambda_{\max}{(M)}$ and $\lambda_{\min}{(M)}$. Moreover, $\| M\|$ denotes the $l_{2}$ norm of $M$ defined by ${\| M\|}:=\sqrt{\lambda_{\max}{({M^{T}M})}}$. If $M$ is a symmetric positive-semidefinite matrix, then ${\| M\|} = {\lambda_{\max}{(M)}}$. Next, we give a definition of Lipschitz continuity.

### Definition 1.1 (Lipschitz continuity)

Let $S$ be a subset of ${\mathbb{R}}^{n}$ and $f:{S\rightarrow{\mathbb{R}}}$.

The function $f$ is said to be Lipschitz continuous on $S$ if there exists a positive constant $L_{f}$ such that Suppose that the function $f$ is differentiable. $\nabla f$ is said to be Lipschitz continuous on $S$ if there exists a positive constant $L_{g}$ such that

## The regularized L-BFGS method

In this section, we propose a regularized L-BFGS method that controls the regularized parameter at each iteration. In the following, $x_{k}$ denotes the $k$-th iterative point, $B_{k}$ denotes the approximate Hessian of $f{(x_{k})}$, and $H_{k}^{- 1} = B_{k}$.

We consider combining the L-BFGS method with the regularized Newton method (1.2). For this purpose, we may replace the Hessian ${\nabla^{2}f}{(x_{k})}$ in equation (1.2) with the approximate Hessian $B_{k}$, that is, we define a search direction $d_{k}$ as a solution of However, since the L-BFGS method updates $H_{k}$, it is not easy to construct $B_{k}$ explicitly. Furthermore, even if we obtain $B_{k}$, it takes a considerable amount of time to solve the linear equation (2.1) in large-scale cases.

Now, we may regard $B_{k} + {\muI}$ as an approximation of ${{\nabla^{2}f}{(x)}} + {\muI}$. Since $B_{k}$ is the approximate Hessian of $f{(x_{k})}$, the matrix $B_{k} + {\muI}$ is an approximate Hessian of ${f{(x)}} + {\frac{\mu}{2}{\| x\|}^{2}}$. The L-BFGS method uses the vector pair $(s_{k},y_{k})$ to construct the approximate Hessian, where $s_{k} = {x_{k + 1} - x_{k}}$ and $y_{k} = {{{\nabla f}{(x_{k + 1})}} - {{\nabla f}{(x_{k})}}}$. Note that $y_{k}$ consists of the gradients of $f$. Therefore, when we compute the approximate Hessian of ${f{(x)}} + {\frac{\mu}{2}{\| x\|}^{2}}$, we use the gradients of ${f{(x)}} + {\frac{\mu}{2}{\| x\|}^{2}}$. That is, we adopt the following ${\hat{y}}_{k}{(\mu)}$ instead of $y_{k}$: Let ${\hat{H}}_{k}{(\mu)}$ be a matrix constructed by the L-BFGS method with vector pairs ${(s_{i},{{\hat{y}}_{i}{(\mu)}})},$ $i = {1,\ldots,m}$ and an appropriate initial matrix ${\hat{H}}_{k}^{}{(\mu)}$. Then, the search direction $d_{k} = {- {{\hat{H}}_{k}{(\mu)}{\nabla f}{(x_{k})}}}$ is calculated in $O{({mn})}$ time, which is the same as the original L-BFGS.

Note that if ${s_{k}^{T}{\hat{y}}_{k}{(\mu)}} > 0$ and ${\hat{H}}_{k}^{}$ is positive-definite, then ${\hat{H}}_{k}{(\mu)}$ is positive definite. When ${s_{k}^{T}{\hat{y}}_{k}{(\mu)}} > 0$ is not satisfied, we may replace ${\hat{y}}_{k}{(\mu)}$ by ${\overset{\sim}{y}}_{k}{(\mu)}$: Then, the inequality ${s_{k}^{T}{\overset{\sim}{y}}_{k}{(\mu)}} > 0$ is always holds because In the following, ${\hat{H}}_{k}{(\mu)}$ is the matrix constructed by the L-BFGS method using the initial matrix ${\hat{H}}_{k}^{}{(\mu)}$ and the vector pairs ${{{(s_{k - i},{{\hat{y}}_{k - i}{(\mu)}})},i} = 1},{\cdots,m}$, and the search direction is given as ${d_{k}{(\mu)}} = {- {{\hat{H}}_{k}{(\mu)}{\nabla f}{(x_{k})}}}$.

The usual L-BFGS method uses $\gamma_{k}I$ as the initial matrix $H_{k}^{}$, where $\gamma_{k}$ is a certain positive constant. Since ${(B_{k}^{})}^{- 1} = H_{k}^{}$ and ${\hat{H}}_{k}^{}$ is an approximation of ${({B_{k}^{} + {\muI}})}^{- 1}$, we may set the initial matrix ${\hat{H}}_{k}^{}{(\mu)}$ as The proposed method generates the next iterate as $x_{k + 1} = {x_{k} + {d_{k}{(\mu)}}}$ without a step length. We control the parameter $\mu$ to guarantee the global convergence as. We exploit the idea of updating the trust-region radius in the TR-method to control $\mu$ to find an appropriate search direction, that is, we use the ratio of the reduction in the objective function value to that of the model function value. We define a ratio function $r_{k}{({d_{k}{(\mu)}},\mu)}$ by where $q_{k}:{{{\mathbb{R}}^{n} \times {\mathbb{R}}}\rightarrow{\mathbb{R}}}$ is given by Note that we do not have to compute the matrix ${\hat{H}}_{k}{(\mu)}^{- 1}$ explicitly in $q_{k}{(d_{k},\mu)}$. Since ${d_{k}{(\mu)}} = {- {{\hat{H}}_{k}{(\mu)}{\nabla f}{(x_{k})}}}$, we have ${d_{k}{(\mu)}^{T}{\hat{H}}_{k}{(\mu)}^{- 1}d_{k}{(\mu)}} = {- {d_{k}{(\mu)}^{T}{\nabla f}{(x_{k})}}}$. If the ratio $r_{k}{({d_{k}{(\mu)}},\mu)}$ is large, i.e., the reduction in the objective function $f$ is sufficiently large compared to that of the model function, we adopt $d_{k}{(\mu)}$ and decrease the parameter $\mu$. On the other hand, if $r_{k}{(d_{k},\mu)}$ is small, i.e., ${f{(x_{k})}} - {f{({x_{k} + d_{k}})}}$ is small, we increase $\mu$ and compute $d_{k}{(\mu)}$ again.

Based on the above ideas, we propose the following regularized L-BFGS method.

### Algorithm 2.1

: Choose the parameters $\mu_{0},\mu_{min},\gamma_{1},\gamma_{2},\eta_{1},\eta_{2},m$ such that ${0 < \mu_{min} \leq \mu_{0}},{0 < \gamma_{1} \leq 1 < \gamma_{2}},{0 < \eta_{1} < \eta_{2} \leq 1}$ and $m > 0$. Choose initial point $x_{0} \in {\mathbb{R}}^{n}$ and an initial matrix ${\hat{H}}_{k}^{0}$. Set $k:=0$.: If some stopping criteria are satisfied, then terminate. Otherwise go to step 2.: Set $l_{k}:=0$ and ${{\overline{\mu}}_{l_{k}} = \mu_{k}}.$: Compute $d_{k}{(\overline{\mu_{l_{k}}})}$ using Algorithm 2.2.: Compute $r_{k}{({d_{k}{({\overline{\mu}}_{l_{k}})}},{\overline{\mu}}_{l_{k}})}$. If ${{r_{k}{({d_{k}{({\overline{\mu}}_{l_{k}})}},{\overline{\mu}}_{l_{k}})}} < \eta_{1}},$ then update ${\overline{\mu}}_{l_{k + 1}} = {\gamma_{2}{\overline{\mu}}_{l_{k}}}$, set ${l_{k} = {l_{k} + 1}},$ and go to Step 2-1. Otherwise, go to Step $3$.: If $\eta_{1} \leq {r_{k}{({d_{k}{({\overline{\mu}}_{l_{k}})}},{\overline{\mu}}_{l_{k}})}} < \eta_{2}$ then update $\mu_{k + 1} = {\overline{\mu}}_{l_{k}}$.\If ${r_{k}{({d_{k}{({\overline{\mu}}_{l_{k}})}},{\overline{\mu}}_{l_{k}})}} \geq \eta_{2}$ then update $\mu_{k + 1} = {\text{max}{\lbrack\mu_{\text{min}},{\gamma_{1}\overline{\mu_{l_{k}}}}\rbrack}}$. Update ${x_{k + 1} = {x_{k} + {d_{k}{({\overline{\mu}}_{l_{k}})}}}}.$ Set $k = {k + 1}$ and go to Step 1.

In Step 2-1 we compute $d_{k}{(\mu)}$ from $(s_{k},{{\hat{y}}_{k}{(\mu)}})$ by the L-BFGS updating scheme . The details of step 2-1 are given as follows.\

### Algorithm 2.2

L-BFGS with $(s_{k},{{\hat{y}}_{k}{(\mu)}})$: Set ${p\leftarrow{{\nabla f}{(x_{k})}}}.$: Repeat the following process with ${i = {{k - 1},{k - 2},\ldots,{k - l}}};$ where ${\tau_{i} = {({s_{i}^{T}{({y_{k} + {\mus_{k}}})}})}^{- 1}}.$: Set ${q\leftarrow{{\hat{H}}_{k}^{0}{(\mu)}p}}.$: Repeat the following process with ${i = {{k - t},{{k - t} + 1},\ldots,{k - 1}}};$: Get the search direction by ${{d_{k}{(\mu)}} = {- q}}.$ It is important to note that when $\mu$ varies, the regularized L-BFGS does not have to store ${\hat{y}}_{k}{(\mu)}$ because the L-BFGS stores $s_{k}$ and $y_{k}$ explicitly, and thus we can get ${\hat{y}}_{k}{(\mu)}$ immediately.

## Global convergence

In this section, we show the global convergence of the proposed algorithm. To this end, we need the following assumptions.

### Assumption 3.1

: \(i\) The objective function $f$ is twice continuously differentiable.: \(ii\) The level set of $f$ at the initial point $x_{0}$ is compact, i.e., $\Omega = \left. \{{x \in {\mathbb{R}}^{n}} \middle| {{f{(x)}} \leq {f{(x_{0})}}}\} \right.$ is compact.: \(iii\) There exist positive constants $M_{1}$ and $M_{2}$ such that: \(iv\) There exists a minimum $f_{\min}$ of $f$.: \(v\) There exists a constant $\underset{¯}{\gamma}$ such that $\gamma_{k} \geq \underset{¯}{\gamma} > 0$ for all $k$, where $\gamma_{k}$ is a parameter in (2.2).

The above assumptions are the same as those for the global convergence of the original L-BFGS method.

Under these assumptions, we have the following several properties. First, let It then follows from Taylor's theorem that Furthermore, since $s_{k} = {x_{k + 1} - x_{k}}$ and $y_{k} = {{{\nabla f}{(x_{k + 1})}} - {{\nabla f}{(x_{k})}}}$, we have and hence we have It follows from Assumption 3.1 (iii) that ${\lambda_{\min}{({\overline{G}}_{k})}} \geq M_{1}$ and ${\lambda_{\max}{({\overline{G}}_{k})}} \leq M_{2}$. Therefore, we have that Since the sequence $\{ x_{k}\}$ is included in the compact set $\Omega$ and $f$ is twice continuously differentiable under Assumption 3.1 (i) and (ii), there exists a positive constant $L_{f}$ such that Now, we investigate the behavior of the eigenvalues of ${\hat{B}}_{k}{(\mu)}$, which is the inverse of ${\hat{H}}_{k}{(\mu)}$. Note that the matrix ${\hat{B}}_{k}{(\mu)}$ is constructed by the BFGS formula with vector pairs ($s_{k},{{\hat{y}}_{k}{(\mu)}}$) and initial matrix ${{\hat{B}}_{k}^{}{(\mu)}} = {{\hat{H}}_{k}^{}{(\mu)}^{- 1}}$. Thus, we have where ${\overset{\sim}{m}}_{k} = {\min{\{{k + 1},m\}}}$ and $j_{l} = {{k - \overset{\sim}{m}} + l}$. Note that these expressions are used.

We now focus on the trace and determinant of ${\hat{B}}_{k}{(\mu)}$. First, we show that the trace of ${\hat{B}}_{k}^{(l)}{(\mu)}$ is $O{(\mu)}$.

### Lemma 3.1

Suppose that Assumption 3.1 holds. Then, where ${M_{3} = {\frac{n}{\underset{¯}{\gamma}} + {mM_{2}}}}.$

### Proof

We have from Assumption 3.1, (3.1), and (3.3) that From the updating formula $$ of matrix ${\hat{B}}_{k}{(\mu)}$, It then follows from (3.6) that This completes the proof. $\square$ The next lemma gives a lower bound for the determinant of ${\hat{B}}_{k}{(\mu)}$.

### Lemma 3.2

Suppose that Assumption 3.1 holds. Then,

### Proof

Note that the determinant of the approximate matrix updated by the BFGS updating scheme has the following property: Since $B_{k}^{}{(\mu)}$ is symmetric positive-definite, Lemma 3.1 implies that ${\lambda_{\max}{({{\hat{B}}_{k}^{(l)}{(\mu)}})}} \geq {M_{3} + {{({{2m} + n})}\mu}}$. Furthermore, we have $\frac{s_{j_{l}}^{T}{\hat{y}}_{j_{l}}{(\mu)}}{{\| s_{j_{l}}\|}^{2}} \geq {M_{1} + \mu}$ from $$. Therefore, it follows that This completes the proof. $\square$ From the above two lemmas, we have ${\lambda_{\max}{({{\hat{H}}_{k}{(\mu)}})}}\rightarrow 0$ as $\mu\rightarrow\infty$.

### Lemma 3.3

Suppose that Assumption 3.1 holds. Then, for all $k \geq 0$, Furthermore, ${{\lim_{\mu\rightarrow\infty}{\lambda_{\max}{({{\hat{H}}_{k}{(\mu)}})}}} = 0}.$

### Proof

We have from Lemmas 3.1 and 3.2 that Since ${\hat{B}}_{k}{(\mu)}$ is symmetric positive-definite, we have It then follows from Assumption 3.1 (v) that | | | $=$ | $\frac{1}{\lambda_{\min}{({{\hat{B}}_{k}{(\mu)}})}}$ | | | Since $\mu \geq \mu_{\min}$, we have It then follows from (3.7) that This completes the proof. $\square$ Now, we give an upper bound for $\|{d_{k}{(\mu)}}\|$.

### Lemma 3.4

Suppose that Assumption 3.1 holds. Then,

### Proof

From the definition of $d_{k}{(\mu)}$, (3.4), and Lemma 3.3, we have that This completes the proof. $\square$ Lemma 3.4 implies that Moreover, since $\Omega + {B{(0,U_{d})}}$ is compact and $f$ is twice continuously differentiable, ${\nabla f}{(x_{k})}$ is Lipschitz continuous on $\Omega + {B{(0,U_{d})}}$. That is, there exists a positive constant $L_{g}$ such that Next, we investigate the values of $\mu$ that satisfy the termination condition $r_{k}{(d_{k}{(\mu)},}$ $\mu) \geq \eta_{1}$ in the inner iterations of Step 2-2 in Algorithm 2.1.

### Lemma 3.5

Suppose that Assumption 3.1 holds. Then, we have

### Proof

We have from Taylor's theorem that From the Lipschitz continuity of ${\nabla f}{(x_{k})}$ in (3.8), we get This completes the proof. $\square$ From Lemma 3.5, if $\mu$ satisfies that is, the inner loops of Algorithm 2.1 must terminate.

Next, we give an upper bound for the parameter $\mu_{k}$.

### Lemma 3.6

Suppose that Assumption 3.1 holds. Then, for any $k \geq 0$,

### Proof

If ${\overline{\mu}}_{l_{k}}$ satisfies (3.9), then ${r_{k}{({d_{k}{({\overline{\mu}}_{l_{k}})}},{\overline{\mu}}_{l_{k}})}} \geq \eta_{1}$ from Lemma 3.5. Therefore, the inner loops must terminate, and we set $\mu_{k}^{\ast} = {\overline{\mu}}_{l_{k}}$.

Now, we give the termination condition on $\mu$ for the inner loop. We have from Lemma 3.3 that It then follows from (3.9) that the termination condition of the inner loop holds when Note that if the inner loop terminates at $l_{k}$, then (3.12) does not hold with $\mu = \mu_{l_{k} - 1}$, that is, Since $\mu_{k}^{\ast} = {\overline{\mu}}_{l_{k}} = {\gamma_{2}{\overline{\mu}}_{l_{k} - 1}}$, we have This completes the proof. $\square$ Next, we give a lower bound for the reduction in the model function $q_{k}$.

### Lemma 3.7

Suppose that Assumption 3.1 holds. Then, we have

### Proof

It follows from the definition of the model function $q_{k}{({d_{k}{(\mu)}},\mu)}$ and Lemmas 3.1, 3.6 that This completes the proof. $\square$ From this lemma, we can give a lower bound for the reduction in the objective function value when $x_{k}$ is not a stationary point.

### Lemma 3.8

Suppose that Assumption 3.1 holds. If there exists a positive constant $\epsilon_{g}$ such that ${\|{{\nabla f}{(x_{k})}}\|} \geq \epsilon_{g}$, then we have ${{f{(x_{k})}} - {f{(x_{k + 1})}}} \geq {\rho\epsilon_{g}^{2}}$, where $\rho = {\eta_{1}M_{6}}$.

### Proof

It follows from Lemmas 3.6 and 3.7 that This completes the proof. $\square$ We are now in a position to prove the main theorem of this section.

### Theorem 3.1

Suppose that Assumption 3.1 holds. Then, ${\operatorname{lim\ inf}_{k\rightarrow\infty}{\|{{\nabla f}{(x_{k})}}\|}} = 0$ or there exists $K \geq 0$ such that ${\|{{\nabla f}{(x_{K})}}\|} = 0$.

### Proof

Suppose the contrary, that is, there exists a positive constant $\epsilon_{g}$ such that ${\|{{\nabla f}{(x_{k})}}\|} \geq \epsilon_{g}$ for all $k \geq 0$. It follows from Lemma 3.8 that Taking $k\rightarrow\infty$, the right-hand side of the final inequality goes to infinity, and hence This contradicts the existence of $f_{\min}$ in Assumption 3.1 (iv). This completes the proof. $\square$

## Implementation issues

The regularized L-BFGS method does not use a line search, and hence it can not take a longer step. Moreover in our experience, the trust-region ratio of the regularized L-BFGS does not improve well and the regularized parameter $\mu$ becomes very large for some large-scale test problems. Both cases result in a short step, and hence the method conducts a large number of iteration to reach a solution. To overcome this difficulty we propose two techniques in this section. We also discuss how to set $\gamma_{k}$ in the initial matrix ${\hat{H}}_{k}{(\mu)}$.

### Simultaneous use with Wolfe line search

The next iterate with line search is given as where $\alpha_{k}$ is a step length. The usual L-BFGS uses a step length $\alpha_{k}$ that satisfies the Wolfe conditions, where $0 < c_{1} < c_{2} < 1$. Note that $\alpha_{k}$ can be larger than 1. Thus, $\alpha_{k}d_{k}$ might be larger, and make a large reduction of $f$. Thus, it might be reasonable to use a line search as well as the regularization technique. However, finding $\alpha_{k}$ takes much time, and hence we must avoid it if $\alpha_{k}d_{k}$ does not enough improvement.

For the efficient use of the line search, we exploit curvature condition (4.3). It is known that the curvature condition ensures that the step is not too short. Therefore, after step 3 of Algorithm 2.1, we first check weather $x_{k} + {d_{k}{(\mu)}}$ satisfies curvature condition ($\alpha_{k} = 1$ in (4.3)) or not. The dissatisfaction of the curvature condition implies that $x_{k} + {d_{k}{(\mu)}}$ is a short step. Thus, we compute $\alpha_{k}$ by the strong Wolfe condition so that we can take a longer step. More precisely, we search $\alpha_{k}$ from $x_{k} + {d_{k}{(\mu)}}$ with the direction $d_{k}{(\mu)}$ so that (4.2)-(4.4) hold with $x_{k}:={x_{k} + {d_{k}{(\mu)}}}$, ${d_{k}:={d_{k}{(\mu)}}},$ and then set $x_{k + 1} = {x_{k} + {{({1 + \alpha_{k}})}d_{k}{(\mu)}}}$.

We now discuss the conditions under which we conduct the Wolfe line search. As mentioned above, we exploit the strong Wolfe condition (4.3) when the following conditions hold, Note that ${\|{d_{k}{(\mu_{min})}}\|} \geq {\|{d_{k}{(\mu)}}\|}$ if $\mu > \mu_{min}$. Thus, $d_{k}{(\mu_{min})}$ is the largest step when we apply RL-BFGS only. Condition (4.5) implies whenever $x_{k} + {d_{k}{(\mu_{min})}}$ to make better progress, we take a longer step via a strong Wolfe line search. We call this method regularized L-BFGS with strong Wolfe line search method (RL-BFGS-SW) as an extended version of the proposed method. Now, we propose the RL-BFGS-SW as follows.\

### Algorithm 4.1

RL-BFGS with line search (RL-BFGS-SW)\: Choose the parameters $\mu_{0},\mu_{min},\gamma_{1},\gamma_{2},\eta_{1},\eta_{2},m$ such that ${0 < \mu_{min} \leq \mu_{0}},{0 < \gamma_{1} \leq 1 < \gamma_{2}},{0 < \eta_{1} < \eta_{2} \leq 1}$ and $m > 0$. Choose initial point $x_{0} \in {\mathbb{R}}^{n}$ and an initial matrix ${\hat{H}}_{k}^{0}$. Set $k:=0$.: If some stopping criteria are satisfied, then terminate. Otherwise go to step 2.: Set $l_{k}:=0$ and ${\overline{\mu}}_{l_{k}} = \mu_{k}$.: Compute $d_{k}{(\overline{\mu_{l_{k}}})}$ by Algorithm 2.2.: Compute $r_{k}{({d_{k}{({\overline{\mu}}_{l_{k}})}},{\overline{\mu}}_{l_{k}})}$. If ${{r_{k}{({d_{k}{({\overline{\mu}}_{l_{k}})}},{\overline{\mu}}_{l_{k}})}} < \eta_{1}},$ then update\${\overline{\mu}}_{l_{k + 1}} = {\gamma_{2}{\overline{\mu}}_{l_{k}}}$, set ${l_{k} = {l_{k} + 1}},$ and go to Step 2-1. Otherwise, go to Step $3$.: If $\eta_{1} \leq {r_{k}{({d_{k}{({\overline{\mu}}_{l_{k}})}},{\overline{\mu}}_{l_{k}})}} < \eta_{2}$ then update $\mu_{k + 1} = {\overline{\mu}}_{l_{k}}$.\If ${r_{k}{({d_{k}{({\overline{\mu}}_{l_{k}})}},{\overline{\mu}}_{l_{k}})}} \geq \eta_{2}$ then update $\mu_{k + 1} = {\text{max}{\lbrack\mu_{\text{min}},{\gamma_{1}\overline{\mu_{l_{k}}}}\rbrack}}$. then find $\alpha_{k}$ by strong Wolfe line search and set $x_{k + 1} = {x_{k} + d_{k} + {\alpha_{k}d_{k}}}$.\Set $k = {k + 1}$ and go to Step 1.

Under this procedure, we must replace $s_{k}$ and ${\hat{y}}_{k}{(\mu)}$ whenever we use the strong Wolfe line search. We summarize $y_{k},{{\hat{y}}_{k}{(\mu)}}$ and $s_{k}$ in Table 4.1.

(when line search is used) Table 4.1: Comparison of yk, ŷk and sk.

Note that we do not need to evaluate a new function and gradient values for conditions (4.5) since we have the gradient and function values to calculate the ratio $r_{k}{({d_{k}{(\mu)}},\mu_{k})}$. Note also that Algorithm 4.1 still has the global convergence property since ${f{({x_{k} + {d_{k}{(\mu)}}})}} > {f{({x_{k} + {{({1 + \alpha_{k}})}d_{k}{(\mu)}}})}}$ from (4.2) and (4.5).

### Nonmonotone decreasing technique

In Algorithm 2.1, we control the regularized parameter $\mu$ to satisfy the descent condition ${f{(x_{k + 1})}} < {f{(x_{k})}}$. However, $\mu$ sometimes becomes quite large for some ill-posed problems. In this situation, we require a large number of function evaluations. Therefore, we use the concept of a nonmonotone line search technique to overcome the difficulty. We replace the ratio function $r_{k}{({d_{k}{(\mu)}},\mu)}$ with the following new ratio function ${\overline{r}}_{k}{({d_{k}{(\mu)}},\mu)}$: and $M$ is a nonnegative integer constant. This modification retains the global convergence of the regularized L-BFGS method.

In the numerical experiments reported in the next section, when $k < M$, we use the original ratio function $r_{k}{({d_{k}{(\mu)}},\mu)}$, and if $k \geq M$ then we use the new ratio function ${\overline{r}}_{k}{({d_{k}{(\mu)}},\mu)}$.

### Scaling initial matrix

The regularized L-BFGS method uses the following initial matrix in each iteration: The parameter $\gamma_{k}$ represents the scale of ${\nabla^{2}f}{(x)}$. Thus, we exploit the scaling parameter $\gamma_{k}$ used, that is, we set It is known that the L-BFGS method with this scaling in the initial matrix has an efficient performance. Note that we require $\gamma_{k} > 0$ to ensure the positive-definiteness of ${\hat{H}}_{k}^{}{(\mu)}$. If ${s_{k - 1}^{T}y_{k - 1}} < {\alpha{\| s_{k - 1}\|}^{2}}$, then we set $\gamma_{k} = {\alpha\frac{{\| s_{k - 1}\|}^{2}}{{\| y_{k - 1}\|}^{2}}}$, where $\alpha$ is a small positive constant.

## Numerical results

In this section, we compare the L-BFGS, the regularized L-BFGS (RL-BFGS), and the regularized L-BFGS with line search (RL-BFGS-SW). For the regularized ones, we adopt the nonmonotone techniques and the initial matrix discussed in Section 4. We have used MCSRCH (Line search routine) and parameters of the original L-BFGS to find a step length in the RL-BFGS-SW.

We have solved 313 problems chosen from CUTEst. All algorithms were coded in MATLAB 2018a. We have used Intel Core i5 1.8 GHz CPU with 8 GB RAM on Mac OS. We have chosen an initial point $x_{0}$ given in CUTEst.

We set the same termination criteria as in the original L-BFGS, that is, where $n_{f}$ is the number of function evaluations. These criteria are similar to those. We regard the trails as fail when $n_{f} > 10000$.

We compare the algorithms from the distribution function proposed. Let $\mathcal{S}$ be a set of solvers and let $\mathcal{P}_{\mathcal{S}}$ be a set of problems that can be solved by all algorithms in $\mathcal{S}$. We measure required evaluations to solve problem $p$ by solver $s \in \mathcal{S}$ as $t_{p,s}$, and the best $t_{p,s}$ for each $p$ as $t_{p}^{\ast},$ which means $t_{p}^{\ast} = {\text{min}\left. \{ t_{p,s} \middle| {s \in \mathcal{S}}\} \right.}$. The distribution function $F_{s}^{\mathcal{S}}{(\tau)}$, for a method $s$ is defined, The algorithm whose $F_{s}^{\mathcal{S}}{(\tau)}$ is close to 1 is considered to be superior compare to other algorithm in $\mathcal{S}$.

### Numerical behavior for some parameters in RL-BFGS

Since the RL-BFGS uses several parameters, we need to investigate the effect of these parameters so that we choose optimal ones.

First we consider $\gamma_{1}$ and $\gamma_{2}$ that control regularized parameters. We perform numerical experiments with $9$ different sets of $(\gamma_{1},\gamma_{2})$ in Table 5.1. The remaining parameters are set to Table 5.1 shows the number of success and rate of success for all $313$ problems. Figure 5.3 shows the distribution function of these parameter sets in terms of the CPU time.

Table 5.1: The number of success and rate of success at each (γ1, γ2).

From Table 5.1 and Figure 5.3 it is clear that ${(\gamma_{1},\gamma_{2})} = {(0.1,10.0)}$ is the best. Therefore, we set $\gamma_{1} = 0.1$ and $\gamma_{2} = 10.0$ for all further experiments.

Next, we compare the number $m$ of vector pairs in the L-BFGS procedure. Note that the original L-BFGS usually choose it in $3 \leq m \leq 7$. Thus, we compare $m = {3,5,7}$. The remaining parameters are set to Table 5.2: The number of success and rate of success at each m.

From Table 5.2 we see that $m = 7$ is the best, while Figure 5.3 shows that $m = 5$ is initially better in terms of CPU time. Therefore, we set $m = 5$ for further experiments.

Finally, we compare the behavior of nonmonotone parameters $M$. We compare $M = {0,4,6,8,10,12}$. Note that $M = 0$ implies the usual monotone decreasing case. The remaining parameters are set to Figure 5.3 shows the distribution function of the nonmonotone parameter in terms of the CPU time.

From Table 5.3 and Figure 5.3 it is clear that $M = 10$ is better. Therefore, we use $M = 10$ in the next section.

Table 5.3: The number of success and rate of success at each M.

### Comparisons of RL-BFGS-SW, RL-BFGS and L-BFGS method

We compare the RL-BFGS-SW, the RL-BFGS and the L-BFGS methods in terms of function evaluations and CPU time. For all numerical results, the parameters in RL-BFGS and RL-BFGS-SW are as follows: Table 5.4 shows the results of the number of successes and rate of successes for all 313 test problems. Figures 5.5 and 5.5 show the results of $\mathcal{P}_{\mathcal{S}}$ in terms of function evaluations and CPU time, respectively. Here $\mathcal{S}$ is the set of problems that are solved by all three algorithms.

Table 5.4: The number of success and rate of success for 313 problems.

Figure 5.5: Comparison of CPU time.

Table 5.4 shows that L-BFGS can solve 71.9% of test problems while both RL-BFGS and RL-BFGS-SW can solve 83.4% of problems. On the other hand, Figures 5.5 and 5.5 show that L-BFGS is faster than the regularized ones for the solved problems.

We define the large-scale problem whose dimension is over or equal to $1000$. Table 5.5 shows the number of success and rate of success for the 151 large-scale problems. Furthermore, Figures 5.7 and 5.7 shows performances for $\mathcal{P}_{\mathcal{S}^{large}}$, where $\mathcal{P}_{\mathcal{S}^{large}}$ denotes all the 151 large-scale test problems from the $\mathcal{P}_{\mathcal{S}}$.

Table 5.5: The number of success and rate of success for 151 large-scale problems.

Figure 5.7: Comparison of CPU time (LS).

Table 5.5 shows that the L-BFGS can solve 70.9% of test problems while both the RL-BFGS and RL-BFGS-SW can solve 82.8% of test problems. It concludes that both proposed methods can solve more number of test problems as compare to the L-BFGS. On the other hand the above figures show that the L-BFGS requires fewer function evaluations than the proposed method.

The above numerical results indicate that the numerical behaviors of the RL-BFGS and the RL-BFGS-SW are almost same. To see the differences we present the numerical results which compare the performance of each test problem.

We observed that the RL-BFGS-SW performs the line search for 93 problems, and does not use it for the remaining problems. Therefore, we compare the results for those 93 problems. Table 5.6 shows the comparison in terms of the number of function evaluations and Algorithm X $<$ Algorithm Y means that the number of function evaluations of the Algorithm X is fewer than that of the Algorithm Y. From the Table 5.6 we see that RL-BFGS-SW requires fewer number of function evaluations than that of RL-BFGS for 38 test problems while RL-BFGS requires fewer number of function evaluations than that of RL-BFGS-SW for 34 test problems among 93 test problems. Moreover, for the large-scale test problems, RL-BFGS-SW requires fewer number of function evaluations than that of RL-BFGS for 13 test problems while RL-BFGS requires fewer number of the function evaluations than that of RL-BFGS-SW for 20 test problems among 39 large-scale test problems. It concludes that the RL-BFGS with line search works well for some problems.

Table 5.6: comparison for 93 problems solved by at least one algorithm (RL-BFGS or RL-BFGS-SW) in terms of nf.

## Conclusion

In this paper we have proposed a combination of the L-BFGS and the regularization technique. We showed the global convergence under appropriate assumptions. We have also presented some efficient implementations. In numerical results, the overall comparison shows that the proposed method can solve more problems than the original L-BFGS. This result indicates that the proposed method is robust in terms of solving number of problems.

For future work, we may consider proposing the stochastic version of the proposed method to solve empirical risk minimization problems.
