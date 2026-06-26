<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Regularized Newton Method for Nonconvex Optimization with Global and Local Complexity Guarantees

Topics include Convex optimization, Nonconvex optimization, Neural networks, Optimization.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Finding an epsilon-stationary point of a nonconvex function with a Lipschitz continuous Hessian is a central problem in optimization. Regularized Newton methods are a classical tool and have been studied extensively, yet they still face a trade-off between global and local convergence. Whether a parameter-free algorithm of this type can simultaneously achieve optimal global complexity and quadratic local convergence remains an open question. To bridge this long-standing gap, we propose a new class of regularizers constructed from the current and previous gradients, and leverage the conjugate gradient approach with a negative curvature monitor to solve the regularized Newton equation. The proposed algorithm is adaptive, requiring no prior knowledge of the Hessian Lipschitz constant, and achieves a global complexity of O(epsilon^(-3/2)) in terms of the second-order oracle calls, and tildeO(epsilon^(-7/4)) for Hessian-vector products, respectively. When the iterates converge to a point where the Hessian is positive definite, the method exhibits quadratic local convergence. Preliminary numerical results, including training the physics-informed neural networks, illustrate the competitiveness of our algorithm.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

We focus on the nonconvex optimization problem where $\varphi:\mathbb{R}^{n}\to\mathbb{R}$ is twice differentiable function with globally Lipschitz continuous Hessian. Since finding a global minimum is generally difficult, the typical goal is to instead find an $\epsilon$-stationary point $x^{*}$ such that $\|\nabla\varphi(x^{*})\|\leq\epsilon$ for arbitrary $\epsilon>0$.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The Newton-type method is one of the most powerful tools for solving such problems, known for its quadratic local convergence near a solution with positive definite Hessian. The classical Newton method uses the second-order information at the current iterate $x_{k}$ to construct the following local model $m_{k}(d)$ and generate the next iterate $x_{k+1}=x_{k}+d_{k}$ by minimizing this model: Although this method enjoys a quadratic local rate, it is well-known that it may fail to converge globally (i.e., converge from any initial point) even for a strongly convex function. Various globalization techniques have been developed to ensure global convergence by introducing regularization or constraints in (1.2) to adjust the direction $d_{k}$, including Levenberg-Marquardt regularization, trust-region methods, and damped Newton methods with a linesearch procedure.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, the original versions of these approaches exhibit a slow $O(\epsilon^{-2})$ worst-case performance, leading to extensive efforts to improve the global complexity of second-order methods. Among these, the cubic regularization method overcomes this issue and achieves an iteration complexity of $O(\epsilon^{-\frac{3}{2}})$, which has been shown to be optimal, while retaining the quadratic local rate. Meanwhile, Levenberg-Marquardt regularization, also known as quadratic regularization, with gradient norms as the regularization coefficients $\rho_{k}$, has also received several attentions due to its simplicity and computational efficiency.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This method approximately solves the regularized subproblem $\min_{d}\left\{m_{k}(d)+\frac{\rho_{k}}{2}\|d\|^{2}\right\}$ to generate $d_{k}$ and the next iterate $x_{k+1}=x_{k}+\alpha_{k}d_{k}$, where $\alpha_{k}$ is either fixed or one selected through a linesearch. When the regularized subproblem is strongly convex, it is equivalent to solving the linear equation $(\nabla^{2}\varphi(x_{k})+\rho_{k}\mathrm{I}_{n})d_{k}=-\nabla\varphi(x_{k})$, which is simpler than the cubic-regularized subproblem and can be efficiently implemented using iterative methods such as the *conjugate gradient* (CG).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Furthermore, each CG iteration only requires a Hessian-vector product, facilitating large-scale problem-solving.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

While such gradient regularization can preserve the superlinear local rate, the fast global rate has remained unclear for some time. Recent studies have achieved such iteration complexity for convex problems. Nevertheless, the regularized subproblem may become ill-defined for nonconvex functions. Consequently, modifications to these methods are necessary to address cases involving indefinite Hessians. A possible solution is to apply CG as if the Hessian is positive definite, and choose a first-order direction if evidence of indefiniteness is found, although this may result in a deterioration of the global rate. In contrast, Gratton et al. introduced a method with a near-optimal global rate of $O(\epsilon^{-\frac{3}{2}}\log\frac{1}{\epsilon})$ and a superlinear local rate. Instead of relying on a first-order direction, their method switches to a direction constructed from the *minimal eigenvalue* and the corresponding eigenvector when indefiniteness is encountered.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

On the other hand, Royer et al. proposed the *capped CG* by modifying the standard CG method to monitor whether a negative curvature direction is encountered during the iterations, and switching to such a direction if it exists. It is worth noting that this modification introduces only one additional Hessian-vector product throughout the entire CG iteration process, avoiding the need for the minimal eigenvalue computation used in Gratton et al.. Furthermore, when the regularizer is *fixed*, an $O(\epsilon^{-\frac{3}{2}})$ global rate can be proved. Building on this method, He et al. improved the dependency of the Lipschitz constant by adjusting the linesearch rule, and generalized it to achieve an optimal global rate for Hölder continuous Hessian, without requiring prior knowledge of problem parameters. Despite the appealing global performance, it is unclear whether the superlinear local rate can be preserved using these regularizers. Along similar lines, Zhu and Xiao combined the gradient regularizer with capped CG and established a superlinear local convergence rate, assuming either the error bound condition or global strong convexity.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

*However, it remains unclear whether this holds for nonconvex problems that exhibit local strong convexity.* Motivated by the discussions above, our goal is to *figure out whether the optimal global order can be achieved by the quadratic regularized Newton method without incurring the logarithmic factor, while also improving the local rate to a quadratic one.* Since the Hessian Lipschitz constant $L_{H}$ is typically unknown and large for many problems, in our algorithmic design, we aim to avoid both the minimal eigenvalue computation and the prior knowledge of $L_{H}$, while achieving the optimal dependence on $L_{H}$ in the global rate.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remaining parts of this article are organized as follows: We list the notations used throughout the paper below. Some background, our main results and related works are provided in Section 2. The ideas and techniques underlying our method are presented in Section 3, and the detailed proofs are deferred to the appendix. Finally, we present some preliminary numerical results to illustrate the performance of our algorithm in Section 4, and discuss potential directions in Section 5.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Capped conjugate gradients", "weight": 1.0} -->

The capped CG proposed by Royer et al. solves the equation $\bar{H}\tilde{d}=-g$ using the standard CG, where $\bar{H}=H+2\rho\mathrm{I}_{n}$. It also monitors whether the iterates generated by the algorithm are negative curvature directions, or the algorithm converges slower than expected. If such an evidence is found, the algorithm will output a negative curvature direction.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Complexity of regularized Newton methods", "weight": 1.0} -->

Continuing from Section 1, we further discuss the regularized Newton method. The key to proving a global rate is the following descent inequality, or its variants: The dependence on the future gradient $g_{k+1}$ arises from the inability to establish a lower bound on $\|d_{k}\|$ using only the information available at the current iterate, since once the iterations enter a superlinear convergence region, the descent becomes small. If we were able to choose $\rho_{k}$ such that the descent were at least $\epsilon^{\frac{3}{2}}$, then by telescoping the sum we would obtain $\varphi(x_{k})-\varphi(x_{0})\leq-Ck\epsilon^{\frac{3}{2}}$. The optimal global rate would follow from $\varphi(x_{k})-\varphi(x_{0})\geq-\Delta_{\varphi}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Complexity of regularized Newton methods", "weight": 1.0} -->

In the thread of work starting from Royer et al., $\rho_{k}\propto\sqrt{\epsilon}$, and the desired descent is guaranteed as long as $g_{k+1}\geq\epsilon$; otherwise, $x_{k+1}$ is a desired solution. Another line of works related to Mishchenko; Gratton et al. use $\rho_{k}\propto\sqrt{g_{k}}$. With this choice, the $g_{k}^{\frac{3}{2}}$ descent is achieved when $g_{k+1}\geq g_{k}$. However, when $g_{k+1}<g_{k}$, the descent becomes $g_{k+1}^{2}g_{k}^{-\frac{1}{2}}$, but the control over $g_{k+1}$ is lost.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Complexity of regularized Newton methods", "weight": 1.0} -->

To resolve this issue, the iterations are divided into two sets: a successful set $\mathcal{I}_{s}=\{k:g_{k+1}\geq g_{k}/2\}$ and a failure set $\mathcal{I}_{f}=\mathbb{N}\setminus\mathcal{I}_{s}$. It is shown that when $|\mathcal{I}_{f}|$ is large the gradient will decrease below $\epsilon$ rapidly; and otherwise, sufficient descent is still achieved. The logarithmic factor in the complexity of Gratton et al. can be understood as follows: a sufficient descent occurs at least once in every $O(\log\frac{1}{\epsilon})$ iterations. Yet, as shown in \\lemmareflem:main/iteration-in-a-subsequence, it actually occurs in every $O(\log\log\frac{1}{\epsilon})$ iterations.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Complexity of regularized Newton methods", "weight": 1.0} -->

Furthermore, the logarithmic factor disappears in the convex case because the gradient will not experience abrupt growth.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Complexity of regularized Newton methods", "weight": 1.0} -->

Finally, we note that the superlinear local rate may disappear for a fixed regularizer as it can be verified that this results in a linear rate when applied to $\varphi(x)=\|x\|^{2}$. When using $\rho_{k}\propto g_{k}^{\bar{\nu}}$ for $\bar{\nu}\in(0,1]$, we have a superlinear rate with order $1+\bar{\nu}$.^11^1A sequence $\{a_{k}\}_{k\geq 0}$ has a superlinear local rate of order $1+\bar{\nu}$ if $a_{k+1}=O(a_{k}^{1+\bar{\nu}})$ for sufficiently large $k$. Moreover, by inspecting the choice $\bar{\nu}=\frac{1}{2}$ for the optimal global rate, there appears a global-local trade-off between the regularizers.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Complexity of regularized Newton methods", "weight": 1.0} -->

One possible solution to achieve a quadratic is to drop the regularizer when $\lambda_{\mathrm{min}}(\nabla^{2}\varphi(x_{k}))\geq\sqrt{g_{k}}$ if the minimal eigenvalue computation is allowed, as in Goldfeld et al.; Jiang et al.. We will explore how to bridge this gap without this in Section 3.2.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Our results", "weight": 1.0} -->

We adopt the standard assumption from Royer et al., which also guarantees $\Delta_{\varphi}<\infty$ and $U_{\varphi}<\infty$. While the Lipschitz continuity assumption can be relaxed to hold only on the level set $L_{\varphi}(x_{0})$ using techniques in He et al., we retain this assumption for simplicity, as it is required for the descent lemma (\\lemmareflem:lipschitz-constant-estimation) and is orthogonal to our analysis.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Assumption 2.1 (Smoothness)", "weight": 1.0} -->

The level set $L_{\varphi}(x_{0}):=\{x\in\mathbb{R}^{n}:\varphi(x)\leq\varphi(x_{0})\}$ is compact, and $\nabla^{2}\varphi$ is $L_{H}$-Lipschitz continuous on an open neighborhood of $L_{\varphi}(x_{0})$ containing the trial points generated in Table 2.1, where $x_{0}$ is the initial point.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 2.1 (Smoothness)", "weight": 1.0} -->

Under this assumption, we have the following inequalities (see Nesterov et al.): Our method is presented in Table 2.1. The subroutine NewtonStep closely follows the version of Royer et al. and He et al., utilizing the CappedCG subroutine defined in Appendix A to find a descent direction. The key modification in this subroutine is the linesearch rule for selecting the stepsize when the negative curvature direction is not detected. The criterion (2.4) aligns with the classical globalization approach of Newton methods, and can be shown to generate a unit stepsize (i.e., $\alpha=1$) when the iteration is sufficiently close to a solution with a positive definite Hessian, leading to superlinear convergence (see \\lemmareflem:asymptotic-newton-step). Furthermore, we introduce an additional criterion (2.5) to ensure that the number of function evaluations remains uniformly bounded as the iteration progresses.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 2.1 (Smoothness)", "weight": 1.0} -->

Another modification is the introduction of the fifth parameter $\bar{\rho}$ and the additional TERM state of d_type in CappedCG. This state is triggered when the iteration number exceeds $\tilde{\Omega}(\bar{\rho}^{-\frac{1}{2}})$, and is designed to ensure non-degenerate global complexity in terms of Hessian-vector products.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 2.1 (Smoothness)", "weight": 1.0} -->

At the end of NewtonStep, an estimation of the Lipschitz constant is computed (i.e., $M_{k}$) and will be used in $\rho_{k}=(M_{k}\omega^{\mathrm{t}}_{k})^{\frac{1}{2}}$. If the linesearch of (2.5) or (2.7) exceeds the allowed number of steps (i.e., $m_{\mathrm{max}}$), it indicates $M_{k}$ is an underestimation of the Lipschitz constant $L_{H}$. In such cases, the estimation is updated, and the current iteration is skipped. Otherwise, the subroutine proceeds and the remaining updating rules of $M_{k}$ are based on whether the loss decays as expected. After approximately $\tilde{O}$ iterations, it produces a desirable estimation of $L_{H}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 2.1 (Smoothness)", "weight": 1.0} -->

The main loop of Table 2.1 invokes NewtonStep with varying regularization coefficients, the selection of which is crucial for achieving the optimal rate. We highlight the existence of a fallback step in the main loop, which ensures the validity \\lemmareflem:main/transition-between-subsequences-give-valid-regularizer and will be explained therein. thm:newton-local-rate-boosted,thm:newton-local-rate-boosted-oracle-complexity summarize our main results, and \\tablereftab:rate-comparision-for-rmn compares them with other regularized Newton methods for nonconvex optimization. All parameters aside from the regularizers can be chosen arbitrarily, provided they satisfy the requirements in Table 2.1.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Additional related work", "weight": 1.0} -->

In addition to the previously discussed work, we will discuss other second-order algorithms with fast global rates, and the adaptivity and universality of algorithms.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Second-order methods with fast global rates", "weight": 1.0} -->

The trust-region method is another important approach to globalizing the Newton method. By introducing a ball constraint $\|d\|\leq r_{k}$ to (1.2), it provides finer control over the descent direction. Several variants of this method have achieved optimal or near-optimal rates. For example, Curtis et al.; Jiang et al. incorporated a Levenberg-Marquardt regularizer into the trust-region subproblem. Hamad and Hinder introduced an elegant and powerful trust-region algorithm that does not modify the subproblem, achieving both an optimal global order and a quadratic local rate. In contrast, our results show that the regularized Newton method can also achieve both, while using less memory than Hamad and Hinder, as shown in Section 4. Interestingly, the disjunction of fast gradient decay and sufficient loss decay, as discussed above in the context of regularized Newton methods, is also reflected in several of these works.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Second-order methods with fast global rates", "weight": 1.0} -->

It is worth noting that, previous to Royer et al., a linesearch method with negative detection was proposed by Royer and Wright. For convex problems, damped Newton methods achieving fast rates have also been developed, and the method of Jiang et al. can also be applied.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Adaptive and universal algorithms", "weight": 1.0} -->

Since the introduction of cubic regularization, *adaptive* cubic regularization attaining the optimal rate without using the knowledge of problem parameters (i.e., the Lipschitz constant) were developed by Cartis et al., and *universal* algorithms based on this regularization that are applicable to different problem classes (e.g., functions with Hölder continuous Hessians with unknown Hölder exponents) are studied by Grapiglia and Nesterov; Doikov and Nesterov. Recently, several universal algorithms for regularized Newton methods have also been proposed, including those by He et al.; Doikov et al.. Additionally, some adaptive trust-region methods have also been introduced.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Overview of the techniques", "weight": 1.0} -->

As mentioned in Section 2, the key to establishing a fast global rate is to show that the loss decreases by at least $L_{H}^{-\frac{1}{2}}\epsilon^{\frac{3}{2}}$ (i.e., *sufficient descent*) for as many iterations as possible. We summarize necessary properties of Table 2.1 in \\lemmareflem:lipschitz-constant-estimation, and will subsequently focus on how to leverage them to establish a global rate.

<!-- chunk {"id": "body-0030", "role": "body", "section": "The global iteration complexity", "weight": 1.0} -->

Since under the choices of regularizers, we have either $\omega_{k}^{\mathrm{f}}=\sqrt{g_{k}}$ or $\omega_{k}^{\mathrm{f}}=\sqrt{\epsilon_{k}}$, then ensuring sufficient descent reduces to counting the occurrences of the event $D_{k}\geq(\omega_{k}^{\mathrm{f}})^{3}$. We outline the key steps for it in this section and defer the proofs and intermediate lemmas to Appendices B and C.

<!-- chunk {"id": "body-0031", "role": "body", "section": "The global iteration complexity", "weight": 1.0} -->

Throughout this section, we partition $\mathbb{N}$ into a disjoint union of intervals $\mathbb{N}=\bigcup_{j\geq 1}I_{\ell_{j},\ell_{j+1}}$ such that $0=\ell_{1}$ and $\ell_{j}<\ell_{j+1}$ for $j\geq 1$, where $I_{i,j}=\{i,..,j-1\}$ is defined in the notation section. These intervals are constructed such that the following conditions hold for every $j\geq 1$: In other words, the sequence $\{x_{k}\}_{k\geq 0}$ is divided into subsequences where the gradient norms are non-increasing. The following lemma shows that sufficient descent occurs during the transition between adjacent subsequences, provided that $\ell_{j}-1\notin\mathcal{J}^{1}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "The global iteration complexity", "weight": 1.0} -->

The fallback step is primarily designed to ensure this lemma holds. Without the fallback step, a sudden gradient decrease (i.e., a small $\delta_{k}$) could result in a small regularizer, causing the sufficient descent guaranteed by this lemma to vanish.

<!-- chunk {"id": "body-0033", "role": "body", "section": "The local convergence order", "weight": 1.0} -->

From the compactness of $L_{\varphi}(x_{0})$ in Assumption 2.1 ‣ 2.1 Our results ‣ 2 Background and our results ‣ A Regularized Newton Method for Nonconvex Optimization with Global and Local Complexity Guarantees"), we know there exists a subsequence $\{x_{k_{j}}\}_{j\geq 0}$ converging to some $x^{*}$ with $\nabla\varphi(x^{*})=0$ (see \\theoremrefthm:appendix/global-newton-complexity). In the analysis of the local convergence rate, we need to assume the positive definiteness of $\nabla^{2}\varphi(x^{*})$, under which the whole sequence $\{x_{k}\}_{k\geq 0}$ also converges to $x^{*}$ (see \\objectrefprop:mixed-newton-nonconvex-phase-local-ratesPropositionPropositions).

<!-- chunk {"id": "body-0034", "role": "body", "section": "The local convergence order", "weight": 1.0} -->

The standard analysis of the local rates for Newton methods consists of two steps. The first step shows that the Newton direction (i.e., $(\nabla^{2}\varphi(x_{k})+\omega_{k}\mathrm{I}_{n})^{-1}\nabla\varphi(x_{k})$) yields superlinear convergence, and then the second step shows this direction is eventually taken. Since there are some adjustments in our usage of these results, we provide the proofs in Section E.1 for completeness, and present the statements below.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Preliminary numerical results", "weight": 1.0} -->

In this section, we present some preliminary numerical results.^22^2Our code is available at Our primary goal is to provide an overall sense of our algorithm's performance and the effects of its components. Detailed results are deferred to Appendix F.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Preliminary numerical results", "weight": 1.0} -->

Since the recently proposed trust-region-type method CAT has an optimal rate and shows competitiveness with state-of-the-art solvers, we adopt their experimental setup and compare with it, as well as the regularized Newton-type method AN2CER proposed by Gratton et al.. The experiments are conducted on the 124 unconstrained problems with more than 100 variables from the widely used CUTEst benchmark for nonlinear optimization. The algorithm is considered successful if it terminates with $\epsilon_{k}\leq\epsilon=10^{-5}$ such that $k\leq 10^{5}$. If the algorithm fails to terminate within 5 hours, it is also recorded as a failure.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Preliminary numerical results", "weight": 1.0} -->

In Appendix F, we observe that the fallback step has insignificant impact on performance yet increases computational cost, suggesting it can be relaxed or removed. Furthermore, $\theta\in[0.5,1]$ balances computational efficiency and local behavior and a small $m_{\mathrm{max}}$ is preferable. Finally, the second linesearch step (2.5) and the TERM state of CappedCG are rarely taken in practice. fig:main-algoperf shows our method without the fallback step (see Appendix F for details). It is slightly faster than CAT and AN2CER, as each iteration uses only a few Hessian-vector products, whereas CAT relies on multiple Cholesky factorizations and AN2CER involves minimal eigenvalue computations. Meanwhile, our method requires a similar number of Hessian evaluations as CAT, and slightly fewer than AN2CER. We also note that using a fixed $\omega_{k}=\sqrt{\epsilon}$ in Table 2.1 may lead to failures when $g_{k}\gg\epsilon$, resulting in deteriorated performance.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Preliminary numerical results", "weight": 1.0} -->

Additionally, our method requires significantly less memory ($\sim$`<!-- -->`{=html}6GB) compared to CAT ($\sim$`<!-- -->`{=html}74GB) for the largest problem in the benchmark with 123200 variables, as it avoids constructing the full Hessian.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Discussions", "weight": 1.0} -->

In this paper, we present the adaptive regularized Newton-CG method and show that two classes of regularizers achieve optimal global convergence order and quadratic local convergence. Our techniques in Section 3 can be extended to Riemannian optimization, as only \\lemmareflem:lipschitz-constant-estimation needs to be modified. For the setting with Hölder continuous Hessians, a variant of this lemma can be derived following He et al., and the subsequent proof may also be generalized (see Section E.2 for local rates). However, this case presents additional challenges since the Hölder exponent is also unknown and requires estimation, which we are currently investigating.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Discussions", "weight": 1.0} -->

It would also be interesting to investigate whether these regularizers are suitable for the convex settings studied in Doikov and Nesterov; Doikov et al. and whether they can be extended to inexact methods such as Yao et al. and stochastic optimization.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Discussions", "weight": 1.0} -->

Y. Zhou and J. Zhu are supported by the National Natural Science Foundation of China (Nos. 92270001, 62350080, 62106120), Tsinghua Institute for Guo Qiang, and the High Performance Computing Center, Tsinghua University; J. Zhu was also supported by the XPlorer Prize. C. Bao is supported by the National Key R&D Program of China (No. 2021YFA1001300) and the National Natural Science Foundation of China (No. 12271291). J. Xu is supported in part by PolyU postdoc matching fund scheme of the Hong Kong Polytechnic University (No. 1-W35A), and Huawei's Collaborative Grants "Large scale linear programming solver" and "Solving large scale linear programming models for production planning". C. Ding is supported in part by the National Key R&D Program of China (No. 2021YFA1000300, No. 2021YFA1000301) and CAS Project for Young Scientists in Basic Research (No. YSBR-034).
