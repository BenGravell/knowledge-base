<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Regularized Newton Method with Global O(1/k^2) Convergence

Topics include Regularized Newton method, Line search.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a Newton-type method that converges fast from any initialization and for arbitrary convex objectives with Lipschitz Hessians. We achieve this by merging the ideas of cubic regularization with a certain adaptive Levenberg-Marquardt penalty. In particular, we show that the iterates given by x^(k)+1 = x^(k) - bigl(nabla^ f(x^(k)) + sqrt(H|nabla f(x^(k))|) Ibigr)^(-1)nabla f(x^(k)), where H > 0 is a constant, converge globally with a O(1/k^) rate. Our method is the first variant of Newton's method that has both cheap iterations and provably fast global convergence. Moreover, we prove that locally our method converges superlinearly when the objective is strongly convex. To boost the method's performance, we present a line search procedure that does not need prior knowledge of H and is provably efficient.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Overview. The history of Newton's method spans over several centuries and the method has become famous for being extremely fast, and infamous for converging only from initialization that is close to a solution. Despite the latter drawback, Newton's method is a cornerstone of convex optimization and it motivated the development of numerous popular algorithms, such as quasi-Newton and trust-region procedures. Its applications and extensions are countless, so we refer to the study in that lists more than 1,000 references in total.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although widely acknowledged, the extreme behaviour of Newton's method is still startling. Why does it converge so efficiently from one initialization and hopelessly diverge from a tiny perturbation of the same initialization? This oddity encourages us to look for a method with a bit slower but more robust convergence, but the existing theory does not offer any good option. All global variants that we are aware of make iterations more expensive by requiring a line search, solving a subproblem, or solving a series of problems. Among them, line search is often selected by classic textbooks as the way to globalize Newton's method, but it is not guaranteed to converge even for convex functions with Lipschitz Hessians. Unfortunately, and somewhat surprisingly, despite decades of research effort and a strong motivation for practical purposes, no variant of Newton's method is known to both converge globally on the class of smooth convex functions and preserve its simple and easy-to-compute update.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The goal of our work is to show that there is, in fact, a simple fix. The core idea of our approach is to employ an adaptive variant of Levenberg--Marquardt regularization to make the update efficient, and to leverage the advanced theory of cubic regularization to find an adaptive rule that would work provably. The rest of our paper is organized as follows. Firstly, we formally state the problem, and expand on the related work and motivating approaches. In Section 2 Convergence \bottomtitlebar"), we give theoretical guarantees of our algorithm and outline the proof. Finally, in Section 3 Convergence \bottomtitlebar"), we discuss the numerical performance of our methods and propose ways to make them faster.

<!-- chunk {"id": "body-0006", "role": "body", "section": "and cubic Newton", "weight": 1.0} -->

Let us discuss a very simple connection between the cubic Newton method and the Levenberg--Marquardt method for (1 Convergence \bottomtitlebar")). The cubic Newton update can be written implicitly as where $H > 0$ is a constant, $\mathbf{I}$ is the identity matrix, and $\|{x^{k + 1} - x^{k}}\|$ inside the inversion makes this update implicit. The Levenberg--Marquardt method, in turn, is parameterized by a sequence ${\{\lambda_{k}\}}_{k = 0}^{\infty}$ (usually $\lambda_{k} \equiv \lambda > 0$) and uses the update The similarity is striking and was immediately pointed out in the work that analyzed cubic Newton. Nevertheless, this connection has not yet been exploited to obtain a better method, except for deriving line search procedures.

<!-- chunk {"id": "body-0007", "role": "body", "section": "and cubic Newton", "weight": 1.0} -->

And since this choice of $\lambda_{k}$ does not depend on $x^{k + 1}$, the update in (3 Convergence \bottomtitlebar")) is a closed-form expression.

<!-- chunk {"id": "body-0008", "role": "body", "section": "and cubic Newton", "weight": 1.0} -->

We shall also leverage these ideas to analyze Levenberg--Marquardt algorithm for (2 Convergence \bottomtitlebar")). The procedure we consider is given by the following update rule: where $F$ is the operator in (2 Convergence \bottomtitlebar")) and $\mathbf{J}_{k} = {\partial{F{(x^{k})}}}$ is its Jacobian.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Contributions", "weight": 1.0} -->

Our goal is twofold. On the one hand, we are interested in designing methods that are useful for applications and can be used without any change as black-box tools. On the other hand, we hope that our theory will serve as the basis for further study of globally-convergent second-order and quasi-Newton methods with superior rates. Although many of the ideas that we discuss in this paper are not new, our analysis, however, is the first of its kind. We hope that our theory will lead to appearance of new methods that are motivated by the theoretical insights of our work.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Contributions", "weight": 1.0} -->

3: $\lambda_{k} = \sqrt{H{\|{{\nabla f}{(x^{k})}}\|}}$ 4: xk + 1 = xk − (∇2f (xk) + λk I)−1 ∇f (xk) ⊳ Compute xk + 1 by solving a linear system Algorithm 1 Globally-convergent Regularized Newton Method for minimization We summarize our key results as follows: We obtain the first closed-form Newton-like method with global $\mathcal{O}\left(\frac{1}{k^{2}} \right)$ convergence rate on convex functions with Lipschitz Hessians.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Contributions", "weight": 1.0} -->

We prove that the same algorithm achieves a superlinear convergence rate for strongly convex functions when close to the solution.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Contributions", "weight": 1.0} -->

We present a line search procedure that allows to run the method without any parameters. Moreover, in contrast to the results for Newton's method and its cubic regularization, our line search provably requires on average only two matrix inversions per iteration.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Contributions", "weight": 1.0} -->

We extend our theory to the non-linear least squares problem.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Convergence theory", "weight": 1.0} -->

> If I have seen further it is by standing on ye sholders of Giants In this section, we prove convergence of our regularized Newton method and discuss several extensions. The formal description of our method is given in Algorithm 1 Convergence \bottomtitlebar"). As reflected by the section's epigraph, most of our findings are based on the prior work of two Giants, Nesterov and Polyak.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

We refer the reader to Lemma 1 in for the proof that bounds (5 Convergence \bottomtitlebar")) and (6 Convergence \bottomtitlebar")) follow from Lipschitzness of $\nabla^{2}f$. We will sometimes refer to $H$ as the *smoothness* constant.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Following the literature on cubic regularization, we will also use the following notation throughout the paper: For better understanding of our results, we are going to present some lemmas formulated for the update without specifying the value of $\lambda_{k}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Convex analysis", "weight": 1.0} -->

Before we proceed to the theoretical analysis, we summarize all of the obtained results in Table 1 Convergence \bottomtitlebar"). The reader may use the table to understand the basic findings of our analysis.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Convex analysis", "weight": 1.0} -->

We begin with a theory for convex objectives $f$. There are nice properties that make the convex analysis simpler and allow us to obtain fast rates. One particularly handy property is that for any point $x \in {\mathbb{R}}^{d}$, the Hessian at $x$ is positive semi-definite, ${{\nabla^{2}f}{(x)}} \succcurlyeq 0$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Equipped with the right assumption, we are ready to show the $\mathcal{O}\left( \frac{1}{k^{2}} \right)$ convergence rate of our algorithm on convex problems with Lipschitz Hessians. Notice that the rate is the same as that of cubic Newton and does not require extra assumptions despite not solving a difficult subproblem.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Local superlinear convergence", "weight": 1.0} -->

Now we present our convergence result for strongly convex functions that shows superlinear convergence when the iterates are in a neighborhood of the solution.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Line search algorithm", "weight": 1.0} -->

3: Initialize line search with reduced regularization $H_{k} = \frac{H_{k - 1}}{4}$, nk = 0 ⊳ Start with H0 if k = 0 5: Set Hk ← 2 Hk ⊳ Increase regularization 7: $\lambda_{k} = \sqrt{H_{k}{\|{{\nabla f}{(x^{k})}}\|}}$ 8: x+ = xk − (∇2f (xk) + λk I)−1 ∇f (xk) ⊳ New trial point Algorithm 2 Adaptive Newton (AdaN) Now, let us present Algorithm 2 Convergence \bottomtitlebar"), which is a line search version of Algorithm 1 Convergence \bottomtitlebar"). At iteration $k$, this method tries to estimate $H$ with a small constant $H_{k}$, and if it is too small, it increases $H_{k}$ in an exponential fashion until $H_{k}$ is large enough.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Line search algorithm", "weight": 1.0} -->

Then, it computes $x^{k + 1}$ and moves on to the next global iteration.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Line search algorithm", "weight": 1.0} -->

To quantify the amount of work that our line search procedure needs, we should compare its run-time to that of Algorithm 1 Convergence \bottomtitlebar"). To simplify the comparison, it is reasonable to assume that each iteration $x^{+} = {x - {{({{{\nabla^{2}f}{(x)}} + {\lambda\mathbf{I}}})}^{- 1}{\nabla f}{(x)}}}$ takes approximately the same amount of time for every $x \in {\mathbb{R}}^{d}$ and $\lambda > 0$. Let us call such iteration a *Newton step*. In, the authors showed that cubic Newton can be equipped with a line search so that on average it requires solving roughly two cubic Newton subproblems. Our Algorithm 2 Convergence \bottomtitlebar") borrows from the same ideas, but instead requires solving roughly two linear systems instead of cubic subproblems.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Line search algorithm", "weight": 1.0} -->

Since each iteration of Algorithm 1 Convergence \bottomtitlebar") requires exactly one Newton step, its run-time for $k$ iterations is $k$ Newton steps. The following theorem measures the number of Newton steps required by Algorithm 2 Convergence \bottomtitlebar").

<!-- chunk {"id": "body-0025", "role": "body", "section": "Theory for non-linear least squares", "weight": 1.0} -->

In this section, we turn our attention to the least-squares problem, where $F$ is a smooth operator. The problem is called least squares because it is often used with operator ${F{(x)}} = {{\hat{F}{(x)}} - y}$, where $y$ is a fixed vector of target values. The goal, thus, is to minimize the residuals of approximating $y$. We present the Levenberg--Marquardt algorithm with our penalty in Algorithm 3 Convergence \bottomtitlebar"). The method is often motivated by the fact that it solves a quadratically-regularized subproblem: In particular, if for some sequence ${\{\lambda_{k}\}}_{k}$ the right-hand side is always larger than ${\|{F{(x)}}\|}^{2}$, then it would always hold ${\|{F{(x^{k + 1})}}\|} \leq {\|{F{(x^{k})}}\|}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Theory for non-linear least squares", "weight": 1.0} -->

However, for our theory, we will instead assume a *cubic* upper bound.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Theory for non-linear least squares", "weight": 1.0} -->

3: Jk = ∂F (xk) ⊳ Compute the Jacobian of F at point xk 4: $\lambda_{k} = \sqrt{c{\|{\mathbf{J}_{k}^{\top}F{(x^{k})}}\|}}$ 5: xk + 1 = xk − (Jk⊤ Jk + λk I)−1 Jk⊤ F (xk) ⊳ Compute xk + 1 by solving a linear system Algorithm 3 Globally-convergent Levenberg–Marquardt Algorithm for problem To study the convergence of Algorithm 3 Convergence \bottomtitlebar"), let us first state the assumptions on $F$ and some basic notation. As before we denote by $r_{k} = {\|{x^{k + 1} - x^{k}}\|}$ and we use $\partial{F{(x)}}$ to denote the Jacobian matrix of $F$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

We assume that $F$ is a smooth operator such that for some constants ${J,H,c} \geq 0$ and for any ${x,y} \in {\mathbb{R}}^{d}$ it holds ${\|{\partial{F{(x)}}}\|} \leq J$ and To the best of our knowledge, assumption in equation (15 Convergence \bottomtitlebar")) has not been studied in the prior literature. We resort to it for the simple reason that it is the most likely generalization of 1 Convergence \bottomtitlebar") to the problem of least squares. We also note that an assumption similar to the cubic growth of squared norm in (15 Convergence \bottomtitlebar")) has appeared in the work, where a quadratic upper bound was used for non-squared norm. However, having our cubic assumption is more conservative when $y$ and $x$ are far from each other, so it makes more sense for studying *global* convergence.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

We also note that 3 Convergence \bottomtitlebar") seems more restrictive than 1 Convergence \bottomtitlebar"), but this is expected since we do not assume any type of convexity for objective (2 Convergence \bottomtitlebar")).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Practical considerations and experiments^11^1Our code is available on GitHub and Google Colab: Colab", "weight": 1.0} -->

Before presenting a numerical comparison of the methods that we are interested, let us discuss some ways that can improve the performance of our method.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Practical considerations and experiments^11^1Our code is available on GitHub and Google Colab: Colab", "weight": 1.0} -->

Newton's method is very popular in practice despite the lack of global convergence, mostly because it does not need any parameters and it is often initialized sufficiently close to the solution. Our Algorithm 1 Convergence \bottomtitlebar") has the advantage of global convergence, but at the cost of requiring the knowledge of $H$. In contrast, our line search algorithm AdaN does not require parameters and it is guaranteed to converge globally, but it requires evaluation of functional values and is harder to implement. Thus, we ask: can we design an algorithm that would still use some regularization but in a simpler form than in AdaN?

<!-- chunk {"id": "body-0032", "role": "body", "section": "Practical considerations and experiments^11^1Our code is available on GitHub and Google Colab: Colab", "weight": 1.0} -->

To find a practical algorithm that would be easier to use than AdaN, let us try to find a smaller regularization estimate by taking a look at Lemma 2 Convergence \bottomtitlebar"). Notice that one of the ways $H$ appears in our bounds is through the error of approximating the next gradient. Motivated by this observation, we can define Using $M_{k}$ instead of $H$ in Algorithm 1 Convergence \bottomtitlebar") is perhaps over-optimistic and in some preliminary experiments did not show a stable behaviour. However, we observed the following estimation to work better in practice: The definition of $H_{k}$ is motivated by the adaptive estimation of the Lipschitz constant of gradient, and it achieves two goals. On the one hand, we always have $H_{k} \geq M_{k}$, where $M_{k}$ is the local estimate of the Hessian smoothness. This way, we keep $H_{k}$ closer to the local value of the Hessian smoothness, which might be much smaller than the global value of $H$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Practical considerations and experiments^11^1Our code is available on GitHub and Google Colab: Colab", "weight": 1.0} -->

On the other hand, since $M_{k}$ is only an underestimate of $H$, i.e., $M_{k} \leq H$, we compensate for the potentially over-optimistic value of $M_{k}$ by using the second condition, $H_{k} \geq \frac{H_{k - 1}}{2}$. All details of the proposed scheme, which we call AdaN+, are given in Algorithm 4 Convergence \bottomtitlebar").

<!-- chunk {"id": "body-0034", "role": "body", "section": "Practical considerations and experiments^11^1Our code is available on GitHub and Google Colab: Colab", "weight": 1.0} -->

In case of the non-linear least-squares problem, we can similarly estimate $H_{k}$ by defining The heuristic $H_{k} = {\max\left\{ M_{k},\frac{H_{k - 1}}{2} \right\}}$ is not directly supported by our theory, but the resulting method shall be still more robust than the regularization-free method.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Practical considerations and experiments^11^1Our code is available on GitHub and Google Colab: Colab", "weight": 1.0} -->

It is also worth noting that in practice, it is better to avoid the expensive computation of inverse matrices and instead solve linear systems. In particular, if we want to compute $x^{k + 1} = {x^{k} - {{({{{\nabla^{2}f}{(x^{k})}} + {\lambda_{k}\mathbf{I}}})}^{- 1}{\nabla f}{(x^{k})}}}$, it would be easier to solve (in $\Delta$) the following linear system: The solution $\Delta^{k}$ of the system above is then used to produce $x^{k + 1} = {x^{k} + \Delta^{k}}$. It is a common practice to use some small value $\lambda_{k} > 0$ just to avoid issues arising from machine-precision errors. This may give our algorithms an additional advantage if the objective turns out to be ill-conditioned.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Practical considerations and experiments^11^1Our code is available on GitHub and Google Colab: Colab", "weight": 1.0} -->

Used methods. We compare our method with a few other standard methods, split into two groups: non-adaptive and adaptive. The non-adaptive methods are: gradient descent with constant stepsize (labeled as 'GD' in the plots); Nesterov's accelerated gradient descent with restarts and constant stepsize; cubic Newton with an estimate of $H$; our Algorithm 1 Convergence \bottomtitlebar") with the same estimate of $H$ as in cubic Newton. The adaptive methods are: gradient descent with Armijo line search; Nesterov's acceleration with Armijo-like line search; Newton's method with Armijo line search; Adaptive Regularisation with Cubics (ARC); our Algorithms 2 Convergence \bottomtitlebar") and 4 Convergence \bottomtitlebar").

<!-- chunk {"id": "body-0037", "role": "body", "section": "Practical considerations and experiments^11^1Our code is available on GitHub and Google Colab: Colab", "weight": 1.0} -->

Then, a coefficient $\alpha_{k}$ is initialized as $2\alpha_{k - 1}$ and divided by 2 until it satisfies the Armijo condition: ${f{({x^{k} + {\alpha_{k}d^{k}}})}} \leq {{f{(x^{k})}} + {\frac{\alpha_{k}}{2}{\langle{{\nabla f}{(x^{k})}},d^{k}\rangle}}}$. Once such $\alpha_{k}$ is found, the iterate is updated as $x^{k + 1} = {x^{k} + {\alpha_{k}d^{k}}}$. For the Arc method, we use the same hyperparameters as given in Section 7 of, except that we additionally divided $\sigma$ by 2 for very successful iterations to improve its performance. Additional implementation details can be found in the source code.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Practical considerations and experiments^11^1Our code is available on GitHub and Google Colab: Colab", "weight": 1.0} -->

Logistic regression. Our first experiment concerns the logistic regression problem with $\ell_{2}$ regularization: where $\sigma:{{\mathbb{R}}\rightarrow{}}$ is the sigmoid function, $\mathbf{A} = {(a_{ij})} \in {\mathbb{R}}^{n \times d}$ is the matrix of features, and $b_{i} \in {\{ 0,1\}}$ is the label of the $i$-th sample. We use the 'w8a' and 'mushrooms' datasets from the LIBSVM package, and set $\ell = 10^{- 10}$ to make the problem ill-conditioned, where $L = {{\|\mathbf{A}\|}^{2}/n}$ is the Lipschitz constant of the gradient. The results are reported in Figure 1 Convergence \bottomtitlebar").

<!-- chunk {"id": "body-0039", "role": "body", "section": "Practical considerations and experiments^11^1Our code is available on GitHub and Google Colab: Colab", "weight": 1.0} -->

To set $H$, we upper bound the Lipschitz Hessian constant of this function as ${\sup_{x \in {\mathbb{R}}^{d}}{\|{{\nabla^{3}f}{(x)}}\|}} \leq {\frac{1}{6\sqrt{3}}{\max_{i}{{\| a_{i}\|}{\|\mathbf{A}\|}^{2}}}}$. This estimate is not tight, which causes cubic Newton and Algorithm 1 Convergence \bottomtitlebar") to converge very slowly. The adaptive estimators, in contrast, converge after a very small number of iterations. We implemented the iterations of cubic Newton using a binary search in regularization, which, unfortunately, was many times slower than the fast iterations of our algorithm. Nevertheless, we report iteration convergence in our results to better highlight how close our method stays to cubic Newton in the non-adaptive case.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Practical considerations and experiments^11^1Our code is available on GitHub and Google Colab: Colab", "weight": 1.0} -->

We use initialization $x^{0}$ proportional to the vector of ones to better see the global properties.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Practical considerations and experiments^11^1Our code is available on GitHub and Google Colab: Colab", "weight": 1.0} -->

Log-sum-exp. In our second experiment, we consider a significantly more ill-conditioned problem of minimizing where ${a_{1},\ldots,a_{n}} \in {\mathbb{R}}^{d}$ are some vectors and $\rho,b_{1},\ldots,b_{n}$ are scalars. This objectives serves as a smooth approximation of function $\max{\{{{a_{1}^{\top}x} - b_{1}},\ldots,{{a_{n}^{\top}x} - b_{n}}\}}$, with $\rho > 0$ controlling the tightness of approximation. We set $n = 500$, $d = 200$ and randomly generate $a_{1},\ldots,a_{n}$ and $b_{1},\ldots,b_{n}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Practical considerations and experiments^11^1Our code is available on GitHub and Google Colab: Colab", "weight": 1.0} -->

After that, we run our experiments for three choices of $\rho$, namely $\rho \in {\{ 0.5,0.25,0.05\}}$. The results are reported in Figure 2 Convergence \bottomtitlebar"). As one can notice, only Algorithms 2 Convergence \bottomtitlebar"), 4 Convergence \bottomtitlebar"), and Arc, performed well in all experiments. Armijo line search was the worst in the last two experiments, most likely due to numerical instability and ill conditioning of the objective. Algorithm 4 Convergence \bottomtitlebar") was less stable than Algorithm 2 Convergence \bottomtitlebar"), which is expected since the former is a simpler heuristic modification of the latter.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we presented a proof that a simple gradient-based regularization allows Newton method to converge globally. Our proof relies on new techniques and appears to be less trivial than that of cubic Newton. At the same time, our analysis has a lot in common with that of cubic Newton and the regularization technique has been known in the literature for a long time. We hope that many existing extensions of cubic Newton, such as its acceleration, will become possible with future work. It would be very exciting to see other extensions, for instance, stochastic variants, and quasi-Newton estimation of the Hessian.
