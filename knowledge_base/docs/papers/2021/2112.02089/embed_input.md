<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Regularized Newton Method with Global O(1/k^2) Convergence

Topics include Regularized Newton method, Line search.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a Newton-type method that converges fast from any initialization and for arbitrary convex objectives with Lipschitz Hessians. We achieve this by merging the ideas of cubic regularization with a certain adaptive Levenberg-Marquardt penalty. In particular, we show that the iterates given by x^(k)+1 = x^(k) - bigl(nabla^ f(x^(k)) + sqrt(H|nabla f(x^(k))|) Ibigr)^(-1)nabla f(x^(k)), where H > 0 is a constant, converge globally with a O(1/k^) rate. Our method is the first variant of Newton's method that has both cheap iterations and provably fast global convergence. Moreover, we prove that locally our method converges superlinearly when the objective is strongly convex. To boost the method's performance, we present a line search procedure that does not need prior knowledge of H and is provably efficient.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Overview. The history of Newton's method spans over several centuries and the method has become famous for being extremely fast, and infamous for converging only from initialization that is close to a solution. Despite the latter drawback, Newton's method is a cornerstone of convex optimization and it motivated the development of numerous popular algorithms, such as quasi-Newton and trust-region procedures. Its applications and extensions are countless, so we refer to the study in[conn2000trust]that lists more than 1,000 references in total.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although widely acknowledged, the extreme behaviour of Newton's method is still startling. Why does it converge so efficiently from one initialization and hopelessly diverge from a tiny perturbation of the same initialization? This oddity encourages us to look for a method with a bit slower but more robust convergence, but the existing theory does not offer any good option. All global variants that we are aware of make iterations more expensive by requiring a line search [crockett1955gradient, ortega1970iterative, nesterov2013], solving a subproblem[nesterov2006cubic, nesterov2008accelerating], or solving a series of problems[marteau2019globally, nesterov2020superfast]. Among them, line search is often selected by classic textbooks[boyd2004convex, nesterov2013] as the way to globalize Newton's method, but it is not guaranteed to converge even for convex functions with Lipschitz Hessians[jarre2016simple, mascarenhas2007divergence].

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Unfortunately, and somewhat surprisingly, despite decades of research effort and a strong motivation for practical purposes, no variant of Newton's method is known to both converge globally on the class of smooth convex functions and preserve its simple and easy-to-compute update.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The goal of our work is to show that there is, in fact, a simple fix. The core idea of our approach is to employ an adaptive variant of Levenberg Marquardt regularization to make the update efficient, and to leverage the advanced theory of cubic regularization[nesterov2006cubic] to find an adaptive rule that would work provably. The rest of our paper is organized as follows. Firstly, we formally state the problem, and expand on the related work and motivating approaches. In sec:theory, we give theoretical guarantees of our algorithm and outline the proof. Finally, in sec:numerical, we discuss the numerical performance of our methods and propose ways to make them faster.

<!-- chunk {"id": "body-0007", "role": "body", "section": "and cubic Newton", "weight": 1.0} -->

Let us discuss a very simple connection between the cubic Newton method[griewank1981modification, nesterov2006cubic] and the LevenbergMarquardt method for[eq:min\_f]. The cubic Newton update can be written implicitly as = x^k - \bigl(\nabla^2 f(x^k) + H\|x^{k+1}-x^k\| \mathbf{I} \bigr)^{-1} \nabla f(x^k),$$ where $H>0$ is a constant, $\mathbf{I}$ is the identity matrix, and $\|x^{k+1} - x^k\|$ inside the inversion makes this update implicit.

<!-- chunk {"id": "body-0008", "role": "body", "section": "and cubic Newton", "weight": 1.0} -->

The LevenbergMarquardt method, in turn, is parameterized by a sequence $\{\lambda_k\}_{k=0}^{\infty}$ (usually $\lambda_k \equiv \lambda>0$) and uses the update = x^k - \bigl(\nabla^2 f(x^k) + \lambda_k \mathbf{I} \bigr)^{-1} \nabla f(x^k).$$ The similarity is striking and was immediately pointed out in the work that analyzed cubic Newton[nesterov2018lectures]. Nevertheless, this connection has not yet been exploited to obtain a better method, except for deriving line search procedures[birgin2017use].

<!-- chunk {"id": "body-0009", "role": "body", "section": "and cubic Newton", "weight": 1.0} -->

Marquardt algorithm is usually considered with constant regularization $\lambda_k=\lambda>0$. However, one may notice that whenever $\lambda_k\approx H\|x^{k+1}-x^k\|$, the two updates should produce similar iterates. How can we make the approximation hold? Our main idea is to leverage the property of the cubic update that $\|x^{k+1}-x^k\|\approx \sqrt{\frac{1}{H}\|\nabla f(x^{k+1})\|}$ (see Lemma3 in[nesterov2006cubic]) and use $\lambda_k= \sqrt{H\|\nabla f(x^k)\|}$ to guarantee $\lambda_k\ge H\|x^{k+1}-x^k\|$. And since this choice of $\lambda_k$ does not depend on $x^{k+1}$, the update in[eq:lm\_update]is a closed-form expression.

<!-- chunk {"id": "body-0010", "role": "body", "section": "and cubic Newton", "weight": 1.0} -->

We shall also leverage these ideas to analyze Levenberg Marquardt algorithm for[eq:least\_squares]. The procedure we consider is given by the following update rule: $$x^{k+1}=x^k - \bigl(\mathbf{J}_k^\top \mathbf{J}_k + \lambda_k\mathbf{I} \bigr)^{-1} \mathbf{J}_k^\top F(x^k),$$ where $F$ is the operator in[eq:least\_squares] and $\mathbf{J}_k=\partial F(x^k)$ is its Jacobian.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Contributions", "weight": 1.0} -->

Our goal is twofold. On the one hand, we are interested in designing methods that are useful for applications and can be used without any change as black-box tools. On the other hand, we hope that our theory will serve as the basis for further study of globally-convergent second-order and quasi-Newton methods with superior rates. Although many of the ideas that we discuss in this paper are not new, our analysis, however, is the first of its kind. We hope that our theory will lead to appearance of new methods that are motivated by the theoretical insights of our work.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Contributions", "weight": 1.0} -->

- We obtain the first closed-form Newton-like method with global $\mathcal O\left(\frac{1}{k^2}\right)$ convergence rate on convex functions with Lipschitz Hessians. - We prove that the same algorithm achieves a superlinear convergence rate for strongly convex functions when close to the solution. - We present a line search procedure that allows to run the method without any parameters. Moreover, in contrast to the results for Newton's method and its cubic regularization, our line search provably requires on average only two matrix inversions per iteration. - We extend our theory to the non-linear least squares problem.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Convergence theory", "weight": 1.0} -->

If I have seen further it is by standing on ye sholders of GiantsIsaac Newton In this section, we prove convergence of our regularized Newton method and discuss several extensions. The formal description of our method is given inalg:global\_newton. As reflected by the section's epigraph, most of our findings are based on the prior work of two Giants, Nesterov and Polyak[nesterov2006cubic].

<!-- chunk {"id": "body-0014", "role": "body", "section": "Convex analysis", "weight": 1.0} -->

Before we proceed to the theoretical analysis, we summarize all of the obtained results in tab:summary. The reader may use the table to understand the basic findings of our analysis.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Convex analysis", "weight": 1.0} -->

We begin with a theory for convex objectives $f$. There are nice properties that make the convex analysis simpler and allow us to obtain fast rates. One particularly handy property is that for any point $x\in\mathbb R^d$, the Hessian at $x$ is positive semi-definite, $\nabla^2 f(x)\succcurlyeq 0$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Convex analysis", "weight": 1.0} -->

For any $\lambda_k\in\mathbb R^d$ such that [eq:reg\_newton\_iteration] is defined, the iteration in[eq:reg\_newton\_iteration] satisfies $$\lambda_k(x^{k+1} - x^k) = - \bigl(\nabla f(x^k) + \nabla^2 f(x^k)(x^{k+1}-x^k)\bigr).$$ This identity follows by multiplying the update rule in[eq:reg\_newton\_iteration] by $(\nabla^2 f(x^k) + \lambda_k\mathbf{I})$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Convex analysis", "weight": 1.0} -->

The meaning of lem:update\_direction is very simple: the update of regularized Newton points towards negative gradient, which is a local descent direction, corrected by second-order information $\nabla^2 f(x^k)(x^{k+1}-x^k)$. The correction is important because it allows the algorithm to better approximate the implicit update under as:hessian\_smooth as $\nabla f(x^k) + \nabla^2 f(x^k)(x^{k+1}-x^k) \approx \nabla f(x^{k+1})$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Convex analysis", "weight": 1.0} -->

Another interesting implication of lem:update\_direction is that $\lambda_k$ plays the role of the reciprocal stepsize, since equation[eq:lm\_identity] is equivalent to \overset{eq:lm_identity}{=} x^k - \frac{1}{\lambda_k}\bigl(\nabla f(x^k) + \nabla^2 f(x^k)(x^{k+1}-x^k)\bigr).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Convex analysis", "weight": 1.0} -->

Thus, overall, we have $x^{k+1}\approx x^k - \frac{1}{\lambda_k}\nabla f(x^{k+1})$, which means that we approximate the implicit (proximal) update. The implicit update does not have any restrictions on the stepsize, so the importance of choosing $\lambda_k$ large lies in keeping the approximation valid. The reader interested in why we would want to approximate the implicit update may consult[nesterov2020inexact]. [Regularization is big enough] Let as:hessian\_smooth hold and $f$ be convex. For any $\lambda_k\ge \sqrt{H\|\nabla f(x^k)\|}$, we have By our choice of $\lambda_k$, we have $\|\nabla f(x^k)\|\le\frac{\lambda_k^2}{H}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Convex analysis", "weight": 1.0} -->

A summary of the main ideas and theoretical claims of our work. For reference, $r_k = \|x^{k+1}-x^k\|$ and $\lambda_k = \sqrt{H\|\nabla f(x^k)\|}$, where $H>0$ is given by as:hessian\_smooth.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Convex analysis", "weight": 1.0} -->

| Idea/fact | Expression | Reference | Thus, we have established that our choice of regularization implies $\lambda_k \ge Hr_k$. Remember that, as discussed in Section[sec:lm\_and\_cubic], $Hr_k$ is the value of regularization that is used implicitly in cubic Newton. As our goal was to approximate cubic Newton, the lower bound on $\lambda_k$shows that we are moving in the right direction.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Convex analysis", "weight": 1.0} -->

Next, let us establish a descent lemma that guarantees a decrease of functional values.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Convex analysis", "weight": 1.0} -->

Note that a straightforward corollary of lem:descent is that $$f(x^{k+1}) \le f(x^k) \quad \textrm{for any }k.$$ So far, we have established that alg:global\_newton decreases the values of $f$ but we do not know yet its rate of convergence. To obtain a rate, we need the following assumption, which is standard in the literature on cubic Newton[nesterov2006cubic].

<!-- chunk {"id": "body-0024", "role": "body", "section": "Convex analysis", "weight": 1.0} -->

The objective function $f$ has a finite optimum $x^*$ such that $f(x^*)=\min_{x\in\mathbb R^d} f(x)$. Moreover, the diameter of the sublevel set $\{x: f(x)\le f(x^0)\}$ is bounded by some constant $D>0$, which means that for any $x$ satisfying $f(x)\le f(x^0)$ we have $\|x-x^*\|\le D$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Convex analysis", "weight": 1.0} -->

The assumption above is quite general. For example, it holds for any strongly convex or uniformly convex $f$. In fact, the assumption is satisfied if the function gap $f(x) - f^*$ is lower-bounded by any power function. Indeed, if there exists $\alpha>0$ such that $f(x)-f^*=\Omega(\|x\|^\alpha)$ for any $x\in\mathbb R^d$, then it immediately implies that $\|x-x^*\|\le \|x\|+\|x^*\| = \mathcal O\left(\|x^*\|+ (f(x)-f^*)^{\frac{1}{\alpha}} \right)\le \mathrm{const}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Convex analysis", "weight": 1.0} -->

Equipped with the right assumption, we are ready to show the $\mathcal O\left(\frac{1}{k^2}\right)$ convergence rate of our algorithm on convex problems with Lipschitz Hessians. Notice that the rate is the same as that of cubic Newton and does not require extra assumptions despite not solving a difficult subproblem.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Convex analysis", "weight": 1.0} -->

Let $f$ be convex and Assumptions[as:hessian\_smooth] and [as:distance] be satisfied. If we choose $\lambda_k=\sqrt{H\|\nabla f(x^k)\|}$, then it holds = \mathcal O\left(\frac{1}{k^2}\right).$$ By lem:descent we have $f(x^{k})\le f(x^{k-1})\le\dotsb \le f(x^0)$. Therefore, by as:distance we have $\|x^k - x^*\|\le D$ for any $k$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Convex analysis", "weight": 1.0} -->

If this recursion was true for every $k$, we would get the desired $\mathcal O\bigl(\frac{1}{k^2}\bigr)$ rate from it using the same techniques as in the convergence proof for cubic Newton[nesterov2006cubic]. In reality, it only holds for $k\in\mathcal{I}_{\infty}$. To circumvent this, we are going to work with a subsequence of iterates. Let us enumerate the index set $\mathcal{I}_{\infty}$ as $\mathcal{I}_{\infty}=\{i_t\}_{t=0}^{\infty}$ with $i_0<i_1<\dotsb$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Convex analysis", "weight": 1.0} -->

Since $\alpha_t=\tau^2(f(x^{i_t}) - f^*)$ is based on the subsequence of indices $i_0, i_1,\dotsc$ from $\mathcal{I}_{\infty}$, we need to consider two cases. If there are many good iterates, i.e., the set $\mathcal{I}_k$ is large, then we will immediately obtain a convergence guarantee for $f(x^k) - f^*$ from the convergence of the sequence $\alpha_t$. If, on the other hand, the number of such iterates is small, we will show that the rate would be exponential, which is even faster than $\mathcal O(\frac{1}{k^2})$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Convex analysis", "weight": 1.0} -->

Theorem[th:main] provides the $\mathcal O(1/k^2)$ global rate of convergence for Algorithm[alg:global\_newton]. While this matches the rate of cubic Newton, it is natural to ask if one can prove an even faster convergence. It turns out that the proved rate is tight up to absolute-constant factors, as shown with numerical experiments for cubic Newton in[doikov2020inexact] and for Regularized Newton in a follow-up work[doikov2022super]. The specific example that yields the worst-case behaviour is $f(x)=\frac{1}{3}\|Ax - b\|_3^3$ with a tridiagonal matrix $A$, as detailed in Section 3 of [arjevani2019oracle] or Example 6 of [doikov2020inexact].

<!-- chunk {"id": "body-0031", "role": "body", "section": "Local superlinear convergence", "weight": 1.0} -->

Now we present our convergence result for strongly convex functions that shows superlinear convergence when the iterates are in a neighborhood of the solution.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Local superlinear convergence", "weight": 1.0} -->

To understand why the convergence rate is superlinear, it is helpful to look at one-step improvement implied by th:local: $$\frac{\|\nabla f(x^{k+1})\|}{\|\nabla f(x^{k})\|} \le \frac{2\sqrt{H}}{\mu}\|\nabla f(x^k)\|^{\frac{1}{2}} < 1,$$ where the second inequality follows by the assumption on small initial gradient. As gradient norms get smaller, the one-step improvement gets better. th:local also guarantees that for any $\varepsilon$ to achieve $\|\nabla f(x^k)\|\le \varepsilon$, it is enough to run alg:global\_newton for $k=\mathcal O\left(\log\log\frac{1}{\varepsilon} \right)$iterations.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Line search algorithm", "weight": 1.0} -->

Adaptive Newton (AdaN) Initialize line search with reduced regularization $H_k = \frac{H_{k-1}}{4}$, $n_k = 0$ Start with $H_0$ if $k=0$ Set $H_k \leftarrow 2H_k$ Increase regularization $\lambda_k = \sqrt{H_k\|\nabla f(x^k)\|}$ $x^+ = x^k - (\nabla^2 f(x^k) + \lambda_k \mathbf{I})^{-1}\nabla f(x^k)$ New trial point $\|\nabla f(x^+)\|\le 2\lambda_k r_+$ and $f(x^+)\le f(x^k) - \frac{2}{3}\lambda_k r_+^2$ Now, let us present alg:line\_search, which is a line search version of alg:global\_newton.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Line search algorithm", "weight": 1.0} -->

At iteration $k$, this method tries to estimate $H$ with a small constant $H_k$, and if it is too small, it increases $H_k$ in an exponential fashion until $H_k$ is large enough. Then, it computes $x^{k+1}$and moves on to the next global iteration.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Line search algorithm", "weight": 1.0} -->

To quantify the amount of work that our line search procedure needs, we should compare its run-time to that of alg:global\_newton. To simplify the comparison, it is reasonable to assume that each iteration $x^+ = x - (\nabla^2 f(x) + \lambda\mathbf{I})^{-1}\nabla f(x)$ takes approximately the same amount of time for every $x\in \mathbb R^d$ and $\lambda > 0$. Let us call such iteration a Newton step. In [nesterov2006cubic], the authors showed that cubic Newton can be equipped with a line search so that on average it requires solving roughly two cubic Newton subproblems. Our alg:line\_searchborrows from the same ideas, but instead requires solving roughly two linear systems instead of cubic subproblems.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Line search algorithm", "weight": 1.0} -->

Since each iteration of alg:global\_newton requires exactly one Newton step, its run-time for $k$ iterations is $k$ Newton steps. The following theorem measures the number of Newton steps required by alg:line\_search.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Line search algorithm", "weight": 1.0} -->

Let $n_k$ denote the number of inner iterations in the line search loop at global iteration $k$, and $N_k=n_0+\dotsb + n_k$ be the total number of computed Newton steps in alg:line\_search after $k$ global iterations.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Line search algorithm", "weight": 1.0} -->

It holds \le 2(k+1) + \max\left(0, \log_2 \frac{2H}{H_0} \right).% \le 2(k+1) + \left[\log_2 \frac{H}{H_0} \right]_+,$$ Therefore, since $\mathcal O(\cdot)$ ignores non-asymptotic terms, we have for the iterates of alg:line\_search = \mathcal O\left(\frac{1}{k^2}\right) = \mathcal O\left(\frac{1}{N_k^2}\right).$$ th:ls states that alg:line\_search, which does not require knowledge of the Lipschitz constant $H$, runs at about half the speed of alg:global\_newton in terms of full number of Newton steps.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Line search algorithm", "weight": 1.0} -->

The extra logarithmic term is likely to be small if we take some $y^0\in\mathbb R^d$ as some perturbation of $x^0$ and initialize Since we need to compute $\nabla^2 f(x^0)$ to perform the first step of alg:line\_search anyway, the initialization above should be sufficiently cheap to compute. It is immediate to observe that by definition of $H$, the estimate above satisfies $H_0\le H$. Since the proof of th:ls mostly follows the lines of the proof of Lemma3 in [nesterov2013gradient], we defer it to the appendix.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Line search algorithm", "weight": 1.0} -->

Adaptivity. Notice that every global iteration of alg:line\_search includes division of our current estimate $H_{k-1}$ by a factor of $4$. Since inside the line search we immediately multiply by 2, this means after a single line search iteration, $H_k$ is equal to $\frac{H_{k-1}}{2}$. If the first iteration of line search turns out to be successful, $H_{k}$ remains twice smaller than $H_{k-1}$, so the algorithm may have a decreasing sequence of estimates. This allows it to adapt to the localvalues of smoothness constant, which might be arbitrarily smaller than the global one.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Theory for non-linear least squares", "weight": 1.0} -->

In this section, we turn our attention to the least-squares problem, $$\min_x \varphi(x)\stackrel{\text{def}}{=} \frac{1}{2}\|F(x)\|^2,$$ where $F$ is a smooth operator. The problem is called least squares because it is often used with operator $F(x)=\hat F(x) - y$, where $y$ is a fixed vector of target values. The goal, thus, is to minimize the residuals of approximating $y$. We present the LevenbergMarquardt algorithm with our penalty in alg:lm.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Theory for non-linear least squares", "weight": 1.0} -->

The method is often motivated by the fact that it solves a quadratically-regularized subproblem: $$x^{k+1} = \argmin_x \left\{\|F(x^k)+\mathbf{J}_k(x - x^k)\|^2 + \lambda_k\|x-x^k\|^2 \right\}.$$ In particular, if for some sequence $\{\lambda_k\}_k$ the right-hand side is always larger than $\|F(x)\|^2$, then it would always hold $\|F(x^{k+1})\|\le \|F(x^k)\|$. However, for our theory, we will instead assume a cubic upper bound.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Theory for non-linear least squares", "weight": 1.0} -->

Globally-convergent LevenbergMarquardt Algorithm for problemeq:least\_squares $\mathbf{J}_k = \partial F(x^k)$ Compute the Jacobian of $F$ at point $x^k$ $\lambda_k = \sqrt{c\|\mathbf{J}_k^\top F(x^k)\|}$ $x^{k+1}=x^k - (\mathbf{J}_k^\top \mathbf{J}_k +\lambda_k \mathbf{I})^{-1}\mathbf{J}_k^\top F(x^k)$ Compute $x^{k+1}$ by solving a linear system To study the convergence of alg:lm, let us first state the assumptions on $F$ and some basic notation. As before we denote by $r_k = \|x^{k+1}-x^k\|$ and we use $\partial F(x)$ to denote the Jacobian matrix of $F$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Theory for non-linear least squares", "weight": 1.0} -->

We assume that $F$ is a smooth operator such that for some constants $J, H, c\ge 0$ and for any $x, y\in \mathbb R^d$ it holds $\|\partial F(x)\|\le J$ and \le \|F(x) + \partial F(x) (y-x)\|^2 + c\|y-x\|^3.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Theory for non-linear least squares", "weight": 1.0} -->

To the best of our knowledge, assumption in equation[eq:ls\_cubic] has not been studied in the prior literature. We resort to it for the simple reason that it is the most likely generalization of as:hessian\_smooth to the problem of least squares. We also note that an assumption similar to the cubic growth of squared norm in[eq:ls\_cubic] has appeared in the work[nesterov2007modified], where a quadratic upper bound was used for non-squared norm. However, having our cubic assumption is more conservative when $y$ and $x$ are far from each other, so it makes more sense for studying global convergence. We also note that as:ls\_smooth seems more restrictive than as:hessian\_smooth, but this is expected since we do not assume any type of convexity for objective[eq:least\_squares].

<!-- chunk {"id": "body-0046", "role": "body", "section": "Theory for non-linear least squares", "weight": 1.0} -->

$$\lambda_k (x^{k+1}-x^k)=-\mathbf{J}_k^\top (F(x^k) + \mathbf{J}_k (x^{k+1}-x^k)).$$ Multiplying both sides of the update formula[eq:ls\_update] by $(\mathbf{J}_k^\top \mathbf{J}_k + \lambda_k \mathbf{I})$, we derive $$(\mathbf{J}_k^\top \mathbf{J}_k + \lambda_k\mathbf{I})(x^{k+1}-x^k) which is easy to rearrange into our claim.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Theory for non-linear least squares", "weight": 1.0} -->

If as:ls\_smooth is satisfied and $\lambda_k = \sqrt{c\|\mathbf{J}_k^\top F(x^k)\|}$, then Interestingly, the results of lem:ls\_main are quite similar to what had in lem:new\_grad\_bound, yet lem:new\_grad\_bound required convexity of the objective. The main reason we managed to avoid such assumptions, is that the matrix $\mathbf{J}_k^\top \mathbf{J}_k$ is always positive semi-definite even if $F$ does not have any nice properties. Thanks to this property, we can establish the following theorem.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Theory for non-linear least squares", "weight": 1.0} -->

The rate in th:lm is not particularly impressive, but we should keep in mind that it holds even in the complete absence of convexity. Furthermore, the main feature of the result is that it holds for arbitrary initialization, no matter how far it is from stationary points of the operator $F$. The analysis of th:lm is a bit more involved than that of th:main, but follows the same set of ideas, so we defer it to the appendix.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Theory for non-linear least squares", "weight": 1.0} -->

The result in Theorem [th:lm] is not the first to establish global convergence of LevenbergMarquardt algorithm with regularization based on gradient norm. For instance, [bergou2019convergence] showed, under Lipschitzness of the gradient of $\|F(x)\|^2$, a similar result for regularization $\lambda_k \propto \|F(x_k)\|^2$. Ignoring logarithmic factors, they established convergence rate $\mathcal{O}\left(\frac{1}{k^{1/2}}\right)$. Our theory, however, does not requires Lipschitzness of the gradient of $\|F(x)\|^2$ and relies instead on inequality[eq:ls\_cubic], so the rates are not directly comparable.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Practical considerations and experimentsOur code is available on GitHub and Google Colab", "weight": 1.0} -->

Before presenting a numerical comparison of the methods that we are interested, let us discuss some ways that can improve the performance of our method.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Practical considerations and experimentsOur code is available on GitHub and Google Colab", "weight": 1.0} -->

Newton's method is very popular in practice despite the lack of global convergence, mostly because it does not need any parameters and it is often initialized sufficiently close to the solution. Our alg:global\_newton has the advantage of global convergence, but at the cost of requiring the knowledge of $H$. In contrast, our line search algorithm AdaN does not require parameters and it is guaranteed to converge globally, but it requires evaluation of functional values and is harder to implement. Thus, we ask: can we design an algorithm that would still use some regularization but in a simpler form than in AdaN?

<!-- chunk {"id": "body-0052", "role": "body", "section": "Practical considerations and experimentsOur code is available on GitHub and Google Colab", "weight": 1.0} -->

To find a practical algorithm that would be easier to use than AdaN, let us try to find a smaller regularization estimate by taking a look at lem:new\_grad\_bound. Notice that one of the ways $H$ appears in our bounds is through the error of approximating the next gradient. Motivated by this observation, we can define \stackrel{\text{def}}{=} \frac{\|\nabla f(x^{k+1}) - \nabla f(x^k) - \nabla^2 f(x^k)(x^{k+1}-x^k)\|}{\|x^{k+1}-x^k\|^2}.$$ Using $M_k$ instead of $H$ inalg:global\_newton is perhaps over-optimistic and in some preliminary experiments did not show a stable behaviour.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Practical considerations and experimentsOur code is available on GitHub and Google Colab", "weight": 1.0} -->

However, we observed the following estimation to work better in practice: &H_k = \max\left\{M_k, \frac{H_{k-1}}{2}\right\}, &\lambda_k = \sqrt{H_k\|\nabla f(x^k)\|}.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Practical considerations and experimentsOur code is available on GitHub and Google Colab", "weight": 1.0} -->

The definition of $H_k$ is motivated by the adaptive estimation of the Lipschitz constant of gradient from[malitsky20adaptive], and it achieves two goals. On the one hand, we always have $H_k\ge M_k$, where $M_k$ is the local estimate of the Hessian smoothness. This way, we keep $H_k$ closer to the local value of the Hessian smoothness, which might be much smaller than the global value of $H$. On the other hand, since $M_k$ is only an underestimate of $H$, i.e., $M_k\le H$, we compensate for the potentially over-optimistic value of $M_k$ by using the second condition, $H_k\ge \frac{H_{k-1}}{2}$. All details of the proposed scheme, which we call AdaN+, are given inalg:newton\_heuristic.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Practical considerations and experimentsOur code is available on GitHub and Google Colab", "weight": 1.0} -->

In case of the non-linear least-squares problem, we can similarly estimate The heuristic $H_k = \max\left\{M_k, \frac{H_{k-1}}{2}\right\}$ is not directly supported by our theory, but the resulting method shall be still more robust than the regularization-free method.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Practical considerations and experimentsOur code is available on GitHub and Google Colab", "weight": 1.0} -->

Numerical results on the $\ell_2$-regularized logistic regression problem with `w8a' dataset (two left plots) and `mushrooms' dataset (two right plots). Our non-adaptive method converged exactly the same way as cubic Newton. Overall, our adaptive methods and Newton method with Armijo line search performed the best.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Practical considerations and experimentsOur code is available on GitHub and Google Colab", "weight": 1.0} -->

It is also worth noting that in practice, it is better to avoid the expensive computation of inverse matrices and instead solve linear systems. In particular, if we want to compute $x^{k+1}=x^k - (\nabla^2 f(x^k)+\lambda_k\mathbf{I})^{-1}\nabla f(x^k)$, it would be easier to solve (in $\Delta$) the following linear system: $$(\nabla^2 f(x^k)+\lambda_k\mathbf{I})\Delta = -\nabla f(x^k).$$ The solution $\Delta^k$ of the system above is then used to produce $x^{k+1}=x^k + \Delta^k$. It is a common practice to use some small value $\lambda_k>0$just to avoid issues arising from machine-precision errors. This may give our algorithms an additional advantage if the objective turns out to be ill-conditioned.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Practical considerations and experimentsOur code is available on GitHub and Google Colab", "weight": 1.0} -->

Used methods. We compare our method with a few other standard methods, split into two groups: non-adaptive and adaptive. The non-adaptive methods are: gradient descent with constant stepsize (labeled as `GD' in the plots); Nesterov's accelerated gradient descent with restarts and constant stepsize; cubic Newton with an estimate of $H$; our Algorithm[alg:global\_newton] with the same estimate of $H$ as in cubic Newton. The adaptive methods are: gradient descent with Armijo line search; Nesterov's acceleration with Armijo-like line search from [nesterov2013gradient]; Newton's method with Armijo line search; Adaptive Regularisation with Cubics (ARC) [cartis2011adaptive]; our Algorithms[alg:line\_search] and [alg:newton\_heuristic].

<!-- chunk {"id": "body-0059", "role": "body", "section": "Practical considerations and experimentsOur code is available on GitHub and Google Colab", "weight": 1.0} -->

The Armijo line search [armijo1966] is combined with gradient descent and Newton's method as follows. Given an iterate $x^k$, the gradient descent direction $d^k=-\nabla f(x^k)$ or Newton's direction $d^k=-(\nabla^2 f(x^k))^{-1}\nabla f(x^k)$ is computed. Then, a coefficient $\alpha_k$ is initialized as $2\alpha_{k-1}$ and divided by 2 until it satisfies the Armijo condition: $f(x^k + \alpha_k d^k)\le f(x^k) + \frac{\alpha_k}{2}\<\nabla f(x^k), d^k>$. Once such $\alpha_k$ is found, the iterate is updated as $x^{k+1} = x^k + \alpha_k d^k$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Practical considerations and experimentsOur code is available on GitHub and Google Colab", "weight": 1.0} -->

For the Arc method, we use the same hyperparameters as given in Section 7 of [cartis2011adaptive], except that we additionally divided $\sigma$by 2 for very successful iterations to improve its performance. Additional implementation details can be found in the source code.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Practical considerations and experimentsOur code is available on GitHub and Google Colab", "weight": 1.0} -->

Logistic regression. Our first experiment concerns the logistic regression problem with $\ell_2$ regularization: $$\min_{x\in\mathbb R^d} \frac{1}{n}\sum_{i=1}^n \left(-b_i\log(\sigma(a_i^\top x)) - (1-b_i)\log(1-\sigma(a_i^\top x)) \right) + \frac{\ell}{2}\|x\|^2,$$ where $\sigma\colon\mathbb R\to $ is the sigmoid function, $\mathbf{A}=(a_{ij})\in\mathbb R^{n\times d}$ is the matrix of features, and $b_i\in\{0, 1\}$ is the label of the $i$-th sample.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Practical considerations and experimentsOur code is available on GitHub and Google Colab", "weight": 1.0} -->

We use the `w8a' and `mushrooms' datasets from the LIBSVM package, and set $\ell=10^{-10}$ to make the problem ill-conditioned, where $L=\|\mathbf{A}\|^2/n$ is the Lipschitz constant of the gradient. The results are reported in Figure[fig:log\_reg]. To set $H$, we upper bound the Lipschitz Hessian constant of this function as $\sup_{x\in\mathbb R^d}\|\nabla^3 f(x)\|\le \frac{1}{6\sqrt{3}}\max_{i}\|a_i\| \|\mathbf{A}\|^2$. This estimate is not tight, which causes cubic Newton and alg:global\_newton to converge very slowly. The adaptive estimators, in contrast, converge after a very small number of iterations.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Practical considerations and experimentsOur code is available on GitHub and Google Colab", "weight": 1.0} -->

We implemented the iterations of cubic Newton using a binary search in regularization, which, unfortunately, was many times slower than the fast iterations of our algorithm. Nevertheless, we report iteration convergence in our results to better highlight how close our method stays to cubic Newton in the non-adaptive case. We use initialization $x^0$proportional to the vector of ones to better see the global properties.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Practical considerations and experimentsOur code is available on GitHub and Google Colab", "weight": 1.0} -->

Numerical results on the log-sum-exp objective with different values of $\rho$: $\rho=0.5$ (left), $\rho=0.25$ (middle) and $\rho=0.05$ (right). The top row shows non-adaptive methods and the bottom row shows adaptive methods. Only our methods and Arc converged for $\rho\in\{0.25, 0.05\}$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Practical considerations and experimentsOur code is available on GitHub and Google Colab", "weight": 1.0} -->

Log-sum-exp. In our second experiment, we consider a significantly more ill-conditioned problem of minimizing $$\min_{x\in\mathbb R^d} \rho\log\left(\sum_{i=1}^n \exp\left(\frac{a_i^\top x - b_i}{\rho}\right)\right),$$ where $a_1,\dotsc, a_n\in\mathbb{R}^d$ are some vectors and $\rho, b_1,\dotsc, b_n$ are scalars. This objectives serves as a smooth approximation of function $\max\{a_1^\top x-b_1,\dotsc, a_n^\top x - b_n\}$, with $\rho>0$ controlling the tightness of approximation. We set $n=500$, $d=200$ and randomly generate $a_1,\dotsc, a_n$ and $b_1,\dotsc, b_n$.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Practical considerations and experimentsOur code is available on GitHub and Google Colab", "weight": 1.0} -->

After that, we run our experiments for three choices of $\rho$, namely $\rho\in\{0.5, 0.25, 0.05\}$. The results are reported in Figure[fig:logsumexp]. As one can notice, only Algorithms[alg:line\_search], [alg:newton\_heuristic], and Arc, performed well in all experiments. Armijo line search was the worst in the last two experiments, most likely due to numerical instability and ill conditioning of the objective. Algorithm[alg:newton\_heuristic] was less stable than Algorithm[alg:line\_search], which is expected since the former is a simpler heuristic modification of the latter.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we presented a proof that a simple gradient-based regularization allows Newton method to converge globally. Our proof relies on new techniques and appears to be less trivial than that of cubic Newton. At the same time, our analysis has a lot in common with that of cubic Newton and the regularization technique has been known in the literature for a long time. We hope that many existing extensions of cubic Newton, such as its acceleration[nesterov2008accelerating], will become possible with future work. It would be very exciting to see other extensions, for instance, stochastic variants, and quasi-Newton estimation of the Hessian. global\_newton.bib

<!-- chunk {"id": "body-0068", "role": "body", "section": "Proofs", "weight": 1.0} -->

For the main theorem, we are going to need the following proposition, which has been established as part of the Proof of Theorem 4.1.4 in[nesterov2018lectures].

<!-- chunk {"id": "body-0069", "role": "body", "section": "Proofs", "weight": 1.0} -->

Let nonnegative sequence $\{\alpha_k\}_{k=0}^\infty$ satisfy $\alpha_{k+1}\le \alpha_k - \frac{2}{3}\alpha_k^{3/2}$. Then it holds for any $k$ Although the proof of Proposition[pr:sequence] a bit technical, we provide it here for completeness and better readability.
