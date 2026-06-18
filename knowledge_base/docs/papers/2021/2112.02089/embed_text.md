## Introduction

Overview. The history of Newton's method spans over several centuries and the method has become famous for being extremely fast, and infamous for converging only from initialization that is close to a solution. Despite the latter drawback, Newton's method is a cornerstone of convex optimization and it motivated the development of numerous popular algorithms, such as quasi-Newton and trust-region procedures. Its applications and extensions are countless, so we refer to the study in that lists more than 1,000 references in total.

Although widely acknowledged, the extreme behaviour of Newton's method is still startling. Why does it converge so efficiently from one initialization and hopelessly diverge from a tiny perturbation of the same initialization? This oddity encourages us to look for a method with a bit slower but more robust convergence, but the existing theory does not offer any good option. All global variants that we are aware of make iterations more expensive by requiring a line search, solving a subproblem, or solving a series of problems. Among them, line search is often selected by classic textbooks as the way to globalize Newton's method, but it is not guaranteed to converge even for convex functions with Lipschitz Hessians. Unfortunately, and somewhat surprisingly, despite decades of research effort and a strong motivation for practical purposes, no variant of Newton's method is known to both converge globally on the class of smooth convex functions and preserve its simple and easy-to-compute update.

The goal of our work is to show that there is, in fact, a simple fix. The core idea of our approach is to employ an adaptive variant of Levenberg--Marquardt regularization to make the update efficient, and to leverage the advanced theory of cubic regularization to find an adaptive rule that would work provably. The rest of our paper is organized as follows. Firstly, we formally state the problem, and expand on the related work and motivating approaches. In Section 2 Convergence \bottomtitlebar"), we give theoretical guarantees of our algorithm and outline the proof. Finally, in Section 3 Convergence \bottomtitlebar"), we discuss the numerical performance of our methods and propose ways to make them faster.

### Background

In this work, we are interested in solving the unconstrained minimization problem

where $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ is a twice-differentiable function with Lipschitz Hessian, as well as in the non-linear least-squares problem

where $F:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{d}}$ is an operator with Lipschitz Jacobian.

First-order methods, such as gradient descent and its stochastic variants, are often the methods of choice to solve both of these problems. Their iterations are easy to parallelize and cheap since they require only $\mathcal{O}{(d)}$ computation. However, for problems with ill-conditioned Hessians, the iteration convergence of first-order methods is very slow and the benefit of cheap iterations is often not sufficient to compensate for that.

Second-order algorithms, on the other hand, may take just a few iterations to converge. For instance, Newton's method minimizes at each step a quadratic approximation of problem (1 Convergence \bottomtitlebar")) to improve dependency on the Hessian properties. Unfortunately, the described basic variant of Newton's method is unstable: it works only for strongly convex problems and may diverge exponentially when initialized not very close to the optimum. Furthermore, each iteration requires solving a system with a potentially ill-conditioned matrix, which might lead to numerical precision errors and further instabilities.

There are several ways to globalize Newton and quasi-Newton updates. The simplest and the most popular choice is to use a line search procedure, which takes the update direction of Newton's method and finds the best step length in that direction. Unfortunately, this approach suffers from several issues. First of all, the Hessian might be ill-conditioned or even singular, in which case the direction is not well defined. Secondly, global analyses of line search do not show a clear theoretical advantage over first-order methods. Finally and most importantly, several recent works have shown that on some convex problems with Lipschitz Hessians, Newton's method with line search may never converge.

Another common approach is to derive a sequence of subproblems that have solutions close enough to the current point. Alas, just liked damped Newton method, this approach depends on the self-concordance assumption, which is essentially a combination of strong convexity and Hessian smoothness and does not hold in many applications.

The first method to achieve a superior global complexity guarantee on a large class of functions was *cubic Newton* method, which is based on cubic regularization. It combines all known advantages of full-Hessian second-order methods: superlinear local convergence, adaptivity to the problem curvature and second-order stationarity guarantees on nonconvex problems. Its main limitation, which we are going to address here, is the expensive iteration due to the nontrivial subproblem that requires a special solver.

Our approach to removing the limitation of cubic Newton is based on another idea that came from the literature on non-linear least-squares problem: *quadratic* regularization of Levenberg and Marquardt (LM). The regularization has several notable benefits: it allows the Hessian to have some negative eigenvalues, it improves the subproblem's conditioning, and makes the update robust to inaccuracies. And most importantly, its update requires solving a single linear system.

### LM and cubic Newton

Let us discuss a very simple connection between the cubic Newton method and the Levenberg--Marquardt method for (1 Convergence \bottomtitlebar")). The cubic Newton update can be written implicitly as

where $H > 0$ is a constant, $\mathbf{I}$ is the identity matrix, and $\|{x^{k + 1} - x^{k}}\|$ inside the inversion makes this update implicit. The Levenberg--Marquardt method, in turn, is parameterized by a sequence ${\{\lambda_{k}\}}_{k = 0}^{\infty}$ (usually $\lambda_{k} \equiv \lambda > 0$) and uses the update

The similarity is striking and was immediately pointed out in the work that analyzed cubic Newton. Nevertheless, this connection has not yet been exploited to obtain a better method, except for deriving line search procedures.

Levenberg--Marquardt algorithm is usually considered with constant regularization $\lambda_{k} = \lambda > 0$. However, one may notice that whenever $\lambda_{k} \approx {H{\|{x^{k + 1} - x^{k}}\|}}$, the two updates should produce similar iterates. How can we make the approximation hold? Our main idea is to leverage the property of the cubic update that ${\|{x^{k + 1} - x^{k}}\|} \approx \sqrt{\frac{1}{H}{\|{{\nabla f}{(x^{k + 1})}}\|}}$ (see Lemma 3 in ) and use $\lambda_{k} = \sqrt{H{\|{{\nabla f}{(x^{k})}}\|}}$ to guarantee $\lambda_{k} \geq {H{\|{x^{k + 1} - x^{k}}\|}}$. And since this choice of $\lambda_{k}$ does not depend on $x^{k + 1}$, the update in (3 Convergence \bottomtitlebar")) is a closed-form expression.

We shall also leverage these ideas to analyze Levenberg--Marquardt algorithm for (2 Convergence \bottomtitlebar")). The procedure we consider is given by the following update rule:

where $F$ is the operator in (2 Convergence \bottomtitlebar")) and $\mathbf{J}_{k} = {\partial{F{(x^{k})}}}$ is its Jacobian.

### Related work

We discuss the related literature for problems (1 Convergence \bottomtitlebar")) and (2 Convergence \bottomtitlebar")) together as they are highly related. When discussing potential choices of $\lambda_{k}$ below, we also ignore all constant factors and only discuss how $\lambda_{k}$ depends on the gradient norm. Among papers on Levenberg--Marquardt method, we mention those that use regularization with $\lambda_{k}$ depending on $\|{F{(x^{k})}}\|$ or $\|{\mathbf{J}_{k}^{\top}F{(x^{k})}}\|$, where $\mathbf{J}_{k} = {\partial{F{(x^{k})}}}$. For simplicity, we do not distinguish between the two regularizations in our literature review.

Newton and cubic Newton literature. The literature on Newton, quasi-Newton and cubic regularization is well developed and the theory was propelled by the advances of the work. Tight upper and lower bounds on cubic regularization are available in. Its many variants such as parallel, subspace, incremental and stochastic schemes continue to attract a lot of attention.

A particularly relevant to ours is the work of which suggested to use $\lambda_{k} \propto {\|{{\nabla f}{(x^{k})}}\|}$ to attain both sublinear global and superlinear local convergence. The main limitation of is that its global rate is $\mathcal{O}\left( \frac{1}{k^{1/4}} \right)$, which is drastically slower than our $\mathcal{O}{(\frac{1}{k^{2}})}$ rate. The work also stands out with its one-dimensional cubic Newton procedure that allows for explicit update expression and enjoys global convergence. Alas, despite using second derivatives, it fails to show any rate improvement over first-order coordinate descent. Finally, in, the authors proposed a general family of Newton updates with gradient-norm regularization that allows the objective to be nonconvex, but their rate for convex functions is slightly slower rate than ours.

Levenberg--Marquardt (LM) literature. The question of how to choose $\lambda_{k}$ has been an important topic in the literature for many decades. The early work of proposed the choices $\lambda_{k} \propto {\|{F{(x^{k})}}\|}$ and $\lambda_{k} \propto {\max{\{{\|{F{(x^{k})}}\|},\sqrt{\|{F{(x^{k})}}\|}\}}}$ and showed global convergence, albeit without any rate. Many other works studied local superlinear convergence for $\lambda_{k} \propto {\|{F{(x^{k})}}\|}^{\delta}$, but, to the best of our knowledge, all prior works require line search with unknown overhead, and there is no result establishing fast global convergence. More choices of $\lambda_{k}$ are available, e.g., see the survey in, but they seem to suffer from the same issue.

There has also been some idea exchange between the literature on minimization (1 Convergence \bottomtitlebar")) and least-squares (2 Convergence \bottomtitlebar")). Just as Levenberg--Marquardt was proposed for (2 Convergence \bottomtitlebar")) and found applications in minimization (1 Convergence \bottomtitlebar")), cubic Newton with a line search has also been applied to the least-squares problem. A more general inner linearization framework was also analyzed in. However, the algorithms of used updates different from (4 Convergence \bottomtitlebar")), hence, they are not directly related to the algorithms we are interested in.

Line search, trust-region and counterexamples. The divergence issues of Newton's method with line search seems to be a relatively unknown fact. For instance, classic books on convex optimization present Newton's method with line search procedures, which can be explained by the fact that these books were written when cubic Newton was not known. Nevertheless, line search and trust-region variants of Newton's method have been shown to fail on convex and nonconvex examples.

Dynamical systems. A connection of Newton's method to dynamical systems with faster convergence has been observed in a prior work that used the connection to analyze Levenberg--Marquardt with constant regularization. The connection was also used in to propose a regularized Newton method that runs an expensive subroutine to assert $\lambda_{k} \approx {\|{x^{k + 1} - x^{k}}\|}$, which makes it almost equivalent to a cubic Newton step. A conceptual advantage of our analysis is that we do not require this approximation to hold.

High-order methods. Many other theoretical works have extended the framework of second-order optimization to high-order methods that rely tensors of derivatives up to order $p$. See, for instance, works for basic analysis and for accelerated variants.

Applications. The applications of Levenberg--Marquardt penalty are extremely diverse and recent uses include control, reinforcement learning, computer vision, molecular chemistry, linear programming and deep learning. Since LM regularization can mitigate negative eigenvalues of the Hessian in nonconvex optimization, there is a continuing effort to combine it with Hessian estimates based on backpropagation, quasi-Newton and Kronecker-factored curvature. In all of these works, LM penalty is merely used as a heuristic that can stabilize aggressive second-order updates and is not shown to help theoretically. Moreover, it is used as a constant, in contrast to our adaptive approach.

### Contributions

Our goal is twofold. On the one hand, we are interested in designing methods that are useful for applications and can be used without any change as black-box tools. On the other hand, we hope that our theory will serve as the basis for further study of globally-convergent second-order and quasi-Newton methods with superior rates. Although many of the ideas that we discuss in this paper are not new, our analysis, however, is the first of its kind. We hope that our theory will lead to appearance of new methods that are motivated by the theoretical insights of our work.

3: $\lambda_{k} = \sqrt{H{\|{{\nabla f}{(x^{k})}}\|}}$
4: xk + 1 = xk − (∇2f (xk)+λk I)−1 ∇f (xk) ⊳ Compute xk + 1 by solving a linear system
Algorithm 1 Globally-convergent Regularized Newton Method for minimization

We summarize our key results as follows:

We obtain the first closed-form Newton-like method with global $\mathcal{O}\left( \frac{1}{k^{2}} \right)$ convergence rate on convex functions with Lipschitz Hessians.

We prove that the same algorithm achieves a superlinear convergence rate for strongly convex functions when close to the solution.

We present a line search procedure that allows to run the method without any parameters. Moreover, in contrast to the results for Newton's method and its cubic regularization, our line search provably requires on average only two matrix inversions per iteration.

We extend our theory to the non-linear least squares problem.

## Convergence theory

> If I have seen further it is by standing on ye sholders of Giants

In this section, we prove convergence of our regularized Newton method and discuss several extensions. The formal description of our method is given in Algorithm 1 Convergence \bottomtitlebar"). As reflected by the section's epigraph, most of our findings are based on the prior work of two Giants, Nesterov and Polyak.

### Notation and main assumption

We will denote by $\mathcal{O}{( \cdot )}$ the non-asymptotic big-O notation that hides all constants and only keeps the dependence on the iteration counter $k$.

Our theory is based on the following assumption about second-order smoothness, which is also the key tool in proving the convergence of cubic Newton.

### Assumption 1

We assume that there exists a constant $H > 0$ such that for any ${x,y} \in {\mathbb{R}}^{d}$

Both of these equations hold if the Hessian of $f$ is $({2H})$-Lipschitz, that is, if for all ${x,y} \in {\mathbb{R}}^{d}$ we have ${\|{{{\nabla^{2}f}{(x)}} - {{\nabla^{2}f}{(y)}}}\|} \leq {2H{\|{x - y}\|}}$.

We refer the reader to Lemma 1 in for the proof that bounds (5 Convergence \bottomtitlebar")) and (6 Convergence \bottomtitlebar")) follow from Lipschitzness of $\nabla^{2}f$. We will sometimes refer to $H$ as the *smoothness* constant.

Following the literature on cubic regularization, we will also use the following notation throughout the paper:

For better understanding of our results, we are going to present some lemmas formulated for the update

without specifying the value of $\lambda_{k}$.

### Convex analysis

Before we proceed to the theoretical analysis, we summarize all of the obtained results in Table 1 Convergence \bottomtitlebar"). The reader may use the table to understand the basic findings of our analysis.

We begin with a theory for convex objectives $f$. There are nice properties that make the convex analysis simpler and allow us to obtain fast rates. One particularly handy property is that for any point $x \in {\mathbb{R}}^{d}$, the Hessian at $x$ is positive semi-definite, ${{\nabla^{2}f}{(x)}} \succcurlyeq 0$.

### Lemma 1

For any $\lambda_{k} \in {\mathbb{R}}^{d}$ such that (7 Convergence \bottomtitlebar")) is defined, the iteration in (7 Convergence \bottomtitlebar")) satisfies

### Proof

This identity follows by multiplying the update rule in (7 Convergence \bottomtitlebar")) by $({{{\nabla^{2}f}{(x^{k})}} + {\lambda_{k}\mathbf{I}}})$. ∎

The meaning of Lemma 1 Convergence \bottomtitlebar") is very simple: the update of regularized Newton points towards negative gradient, which is a local descent direction, corrected by second-order information ${\nabla^{2}f}{(x^{k})}{({x^{k + 1} - x^{k}})}$. The correction is important because it allows the algorithm to better approximate the implicit update under 1 Convergence \bottomtitlebar") as ${{{\nabla f}{(x^{k})}} + {{\nabla^{2}f}{(x^{k})}{({x^{k + 1} - x^{k}})}}} \approx {{\nabla f}{(x^{k + 1})}}$.

Another interesting implication of Lemma 1 Convergence \bottomtitlebar") is that $\lambda_{k}$ plays the role of the reciprocal stepsize, since equation (8 Convergence \bottomtitlebar")) is equivalent to

Thus, overall, we have $x^{k + 1} \approx {x^{k} - {\frac{1}{\lambda_{k}}{\nabla f}{(x^{k + 1})}}}$, which means that we approximate the implicit (proximal) update. The implicit update does not have any restrictions on the stepsize, so the importance of choosing $\lambda_{k}$ large lies in keeping the approximation valid. The reader interested in why we would want to approximate the implicit update may consult.

### Lemma 2

\[Regularization is big enough\] Let 1 Convergence \bottomtitlebar") hold and $f$ be convex. For any $\lambda_{k} \geq \sqrt{H{\|{{\nabla f}{(x^{k})}}\|}}$, we have

### Proof

By our choice of $\lambda_{k}$, we have ${\|{{\nabla f}{(x^{k})}}\|} \leq \frac{\lambda_{k}^{2}}{H}$. Therefore, using ${{\nabla^{2}f}{(x^{k})}} \succcurlyeq 0$, we derive

Thus, we have ${Hr_{k}} \leq \lambda_{k}$ and ${\lambda_{k}r_{k}} \leq {\|{{\nabla f}{(x^{k})}}\|}$, which proves (9 Convergence \bottomtitlebar")) and the second part of (10 Convergence \bottomtitlebar")). Combining the implicit update formula from Lemma 1 Convergence \bottomtitlebar") and triangle inequality, we also get

$\lambda_{k} = \sqrt{H\left\| {{\nabla f}\left( x^{k} \right)} \right\|}$

$x^{k + 1} = {x^{k} - {\frac{1}{\lambda_{k}}\left( {{{\nabla f}\left( x^{k} \right)} + {{\nabla^{2}f}\left( x^{k} \right)\left( {x^{k + 1} - x^{k}} \right)}} \right)}}$

λk ≈ H rk (this might not be true and is not proved)

${f\left( x^{k + 1} \right)} \leq {{f\left( x^{k} \right)} - {\frac{2}{3}\lambda_{k}r_{k}^{2}}}$

$k \in \mathcal{I}_{\infty} = \left\{ {i \in {\mathbb{N}}}:{\left\| {{\nabla f}\left( x^{i + 1} \right)} \right\| \geq {\frac{1}{4}\left\| {{\nabla f}\left( x^{i} \right)} \right\|}} \right\}$

Table 1: A summary of the main ideas and theoretical claims of our work. For reference, rk = ∥xk + 1 − xk∥ and $\lambda_{k} = \sqrt{H{\|{{\nabla f}{(x^{k})}}\|}}$, where H &gt; 0 is given by 1.

Thus, we have established that our choice of regularization implies $\lambda_{k} \geq {Hr_{k}}$. Remember that, as discussed in Section 1.2 Convergence \bottomtitlebar"), $Hr_{k}$ is the value of regularization that is used implicitly in cubic Newton. As our goal was to approximate cubic Newton, the lower bound on $\lambda_{k}$ shows that we are moving in the right direction.

Next, let us establish a descent lemma that guarantees a decrease of functional values.

### Lemma 3

Let $f$ be convex and satisfy Assumption 1 Convergence \bottomtitlebar"). If we choose $\lambda_{k} = \sqrt{H{\|{{\nabla f}{(x^{k})}}\|}}$, then

### Proof

The proof is quite simple and revolves around substituting $x^{k + 1}$ and $x^{k}$ into (5 Convergence \bottomtitlebar")):

Note that a straightforward corollary of Lemma 3 Convergence \bottomtitlebar") is that

So far, we have established that Algorithm 1 Convergence \bottomtitlebar") decreases the values of $f$ but we do not know yet its rate of convergence. To obtain a rate, we need the following assumption, which is standard in the literature on cubic Newton.

### Assumption 2

The objective function $f$ has a finite optimum $x^{\ast}$ such that ${f{(x^{\ast})}} = {{\min_{x \in {\mathbb{R}}^{d}}f}{(x)}}$. Moreover, the diameter of the sublevel set $\{ x:{{f{(x)}} \leq {f{(x^{0})}}}\}$ is bounded by some constant $D > 0$, which means that for any $x$ satisfying ${f{(x)}} \leq {f{(x^{0})}}$ we have ${\|{x - x^{\ast}}\|} \leq D$.

The assumption above is quite general. For example, it holds for any strongly convex or uniformly convex $f$. In fact, the assumption is satisfied if the function gap ${f{(x)}} - f^{\ast}$ is lower-bounded by *any* power function. Indeed, if there exists $\alpha > 0$ such that ${{f{(x)}} - f^{\ast}} = {\Omega{({\| x\|}^{\alpha})}}$ for any $x \in {\mathbb{R}}^{d}$, then it immediately implies that ${\|{x - x^{\ast}}\|} \leq {{\| x\|} + {\| x^{\ast}\|}} = {\mathcal{O}\left( {{\| x^{\ast}\|} + {({{f{(x)}} - f^{\ast}})}^{\frac{1}{\alpha}}} \right)} \leq {const}$.

Equipped with the right assumption, we are ready to show the $\mathcal{O}\left( \frac{1}{k^{2}} \right)$ convergence rate of our algorithm on convex problems with Lipschitz Hessians. Notice that the rate is the same as that of cubic Newton and does not require extra assumptions despite not solving a difficult subproblem.

### Theorem 1

Let $f$ be convex and Assumptions 1 Convergence \bottomtitlebar") and 2 Convergence \bottomtitlebar") be satisfied. If we choose $\lambda_{k} = \sqrt{H{\|{{\nabla f}{(x^{k})}}\|}}$, then it holds

### Proof

By Lemma 3 Convergence \bottomtitlebar") we have ${f{(x^{k})}} \leq {f{(x^{k - 1})}} \leq \cdots \leq {f{(x^{0})}}$. Therefore, by 2 Convergence \bottomtitlebar") we have ${\|{x^{k} - x^{\ast}}\|} \leq D$ for any $k$. Thus, by convexity of $f$

Define $\mathcal{I}_{\infty}\overset{\text{def}}{=}{\{{i \in {\mathbb{N}}}:{{\|{{\nabla f}{(x^{i + 1})}}\|} \geq {\frac{1}{4}{\|{{\nabla f}{(x^{i})}}\|}}}\}}$ and $\mathcal{I}_{k}\overset{\text{def}}{=}{\{{i \in \mathcal{I}_{\infty}}:{i \leq k}\}}$. Let us consider any $k \in \mathcal{I}_{\infty}$. Using (10 Convergence \bottomtitlebar")) and the fact that ${Hr_{k}} \leq \lambda_{k}$, we get

Thus, we have $r_{k} \geq \frac{\sqrt{\|{{\nabla f}{(x^{k})}}\|}}{8\sqrt{H}}$. Furthermore, by Lemma 3 Convergence \bottomtitlebar") we get

where $\tau\overset{\text{def}}{=}\frac{1}{96D^{3/2}\sqrt{H}}$. If this recursion was true for every $k$, we would get the desired $\mathcal{O}\left( \frac{1}{k^{2}} \right)$ rate from it using the same techniques as in the convergence proof for cubic Newton. In reality, it only holds for $k \in \mathcal{I}_{\infty}$. To circumvent this, we are going to work with a subsequence of iterates. Let us enumerate the index set $\mathcal{I}_{\infty}$ as $\mathcal{I}_{\infty} = {\{ i_{t}\}}_{t = 0}^{\infty}$ with $i_{0} < i_{1} < \cdots$. Defining $\alpha_{t}\overset{\text{def}}{=}{\tau^{2}{({{f{(x^{i_{t}})}} - f^{\ast}})}} \geq 0$ and using $i_{t + 1} \geq {i_{t} + 1}$, we can rewrite the produced bound as

The remainder of the proof is rather simple. By Proposition 1 Convergence \bottomtitlebar"), the obtained recursion on $\alpha_{t}$ implies convergence $\alpha_{t} = {\mathcal{O}{(\frac{1}{t^{2}})}}$. Since $\alpha_{t} = {\tau^{2}{({{f{(x^{i_{t}})}} - f^{\ast}})}}$ is based on the subsequence of indices $i_{0},i_{1},\ldots$ from $\mathcal{I}_{\infty}$, we need to consider two cases. If there are many "good" iterates, i.e., the set $\mathcal{I}_{k}$ is large, then we will immediately obtain a convergence guarantee for ${f{(x^{k})}} - f^{\ast}$ from the convergence of the sequence $\alpha_{t}$. If, on the other hand, the number of such iterates is small, we will show that the rate would be exponential, which is even faster than $\mathcal{O}{(\frac{1}{k^{2}})}$.

Consider first the case ${|\mathcal{I}_{k}|} \geq \frac{k}{2}$. Let $i = i_{|\mathcal{I}_{k}|} \leq k$ be the largest element from $\mathcal{I}_{k}$. Then, it holds ${{f{(x^{k})}} - {f^{\ast}\overset{()}{\leq}f{(x^{i})}} - f^{\ast}} = {\mathcal{O}{(\frac{1}{{|\mathcal{I}_{k}|}^{2}})}}$. Since we assume ${|\mathcal{I}_{k}|} \geq \frac{k}{2}$, the latter also implies that ${{f{(x^{k})}} - f^{\ast}} = {\mathcal{O}{(\frac{1}{k^{2}})}}$.

In the second case, we assume that ${|\mathcal{I}_{k}|} \leq \frac{k}{2}$. By Lemma 2 Convergence \bottomtitlebar"), we always have ${\|{{\nabla f}{(x^{i + 1})}}\|} \leq {2{\|{{\nabla f}{(x^{i})}}\|}}$, and for $i \notin \mathcal{I}_{k}$ we have ${\|{{\nabla f}{(x^{i + 1})}}\|} \leq {\frac{1}{4}{\|{{\nabla f}{(x^{i})}}\|}}$. Therefore, if ${|\mathcal{I}_{k}|} \leq \frac{k}{2}$, we have ${\frac{{f{(x^{k})}} - f^{\ast}}{D}\overset{()}{\leq}{\|{{\nabla f}{(x^{k})}}\|}} \leq {\frac{1}{4^{k/2}}2^{k/2}{\|{{\nabla f}{(x^{0})}}\|}} = \frac{\|{{\nabla f}{(x^{0})}}\|}{2^{k/2}} = {\mathcal{O}{(\frac{1}{k^{2}})}}$. As we can see, in the case ${|\mathcal{I}_{k}|} \leq \frac{k}{2}$, the rate of convergence is exponential. ∎

Theorem 1 Convergence \bottomtitlebar") provides the $\mathcal{O}{({1/k^{2}})}$ global rate of convergence for Algorithm 1 Convergence \bottomtitlebar"). While this matches the rate of cubic Newton, it is natural to ask if one can prove an even faster convergence. It turns out that the proved rate is tight up to absolute-constant factors, as shown with numerical experiments for cubic Newton in and for Regularized Newton in a follow-up work. The specific example that yields the worst-case behaviour is ${f{(x)}} = {\frac{1}{3}{\|{{Ax} - b}\|}_{3}^{3}}$ with a tridiagonal matrix $A$, as detailed in Section 3 of or Example 6 of.

### Local superlinear convergence

Now we present our convergence result for strongly convex functions that shows superlinear convergence when the iterates are in a neighborhood of the solution.

### Theorem 2 (Local)

Assume that $f$ is $\mu$-strongly convex, i.e., for any $x$ we have ${{\nabla^{2}f}{(x)}} \succcurlyeq {\mu\mathbf{I}}$. If for some $k_{0} \geq 0$ it holds ${\|{{\nabla f}{(x^{k_{0}})}}\|} \leq \frac{\mu^{2}}{4H}$, then for all $k \geq k_{0}$, the iterates of Algorithm 1 Convergence \bottomtitlebar") satisfy

and, therefore, sequence ${\{ x^{k}\}}_{k \geq k_{0}}$ converges superlinearly.

To understand why the convergence rate is superlinear, it is helpful to look at one-step improvement implied by Theorem 2. ‣ 2.3 Local superlinear convergence ‣ 2 Convergence theory ‣ \toptitlebarRegularized Newton Method with Global 𝒪⁢(1/𝑘²) Convergence \bottomtitlebar"):

where the second inequality follows by the assumption on small initial gradient. As gradient norms get smaller, the one-step improvement gets better. Theorem 2. ‣ 2.3 Local superlinear convergence ‣ 2 Convergence theory ‣ \toptitlebarRegularized Newton Method with Global 𝒪⁢(1/𝑘²) Convergence \bottomtitlebar") also guarantees that for any $\varepsilon$ to achieve ${\|{{\nabla f}{(x^{k})}}\|} \leq \varepsilon$, it is enough to run Algorithm 1 Convergence \bottomtitlebar") for $k = {\mathcal{O}\left( {\log{\log\frac{1}{\varepsilon}}} \right)}$ iterations.

### Line search algorithm

3: Initialize line search with reduced regularization $H_{k} = \frac{H_{k - 1}}{4}$, nk = 0 ⊳ Start with H0 if k = 0
5: Set Hk ← 2 Hk ⊳ Increase regularization
7: $\lambda_{k} = \sqrt{H_{k}{\|{{\nabla f}{(x^{k})}}\|}}$
8: x+ = xk − (∇2f (xk)+λk I)−1 ∇f (xk) ⊳ New trial point
Algorithm 2 Adaptive Newton (AdaN)

Now, let us present Algorithm 2 Convergence \bottomtitlebar"), which is a line search version of Algorithm 1 Convergence \bottomtitlebar"). At iteration $k$, this method tries to estimate $H$ with a small constant $H_{k}$, and if it is too small, it increases $H_{k}$ in an exponential fashion until $H_{k}$ is large enough. Then, it computes $x^{k + 1}$ and moves on to the next global iteration.

To quantify the amount of work that our line search procedure needs, we should compare its run-time to that of Algorithm 1 Convergence \bottomtitlebar"). To simplify the comparison, it is reasonable to assume that each iteration $x^{+} = {x - {{({{{\nabla^{2}f}{(x)}} + {\lambda\mathbf{I}}})}^{- 1}{\nabla f}{(x)}}}$ takes approximately the same amount of time for every $x \in {\mathbb{R}}^{d}$ and $\lambda > 0$. Let us call such iteration a *Newton step*. In, the authors showed that cubic Newton can be equipped with a line search so that on average it requires solving roughly two cubic Newton subproblems. Our Algorithm 2 Convergence \bottomtitlebar") borrows from the same ideas, but instead requires solving roughly two linear systems instead of cubic subproblems.

Since each iteration of Algorithm 1 Convergence \bottomtitlebar") requires exactly one Newton step, its run-time for $k$ iterations is $k$ Newton steps. The following theorem measures the number of Newton steps required by Algorithm 2 Convergence \bottomtitlebar").

### Theorem 3

Let $n_{k}$ denote the number of inner iterations in the line search loop at global iteration $k$, and $N_{k} = {n_{0} + \cdots + n_{k}}$ be the total number of computed Newton steps in Algorithm 2 Convergence \bottomtitlebar") after $k$ global iterations. It holds

Therefore, since $\mathcal{O}{( \cdot )}$ ignores non-asymptotic terms, we have for the iterates of Algorithm 2 Convergence \bottomtitlebar")

Theorem 3 Convergence \bottomtitlebar") states that Algorithm 2 Convergence \bottomtitlebar"), which does not require knowledge of the Lipschitz constant $H$, runs at about half the speed of Algorithm 1 Convergence \bottomtitlebar") in terms of full number of Newton steps. The extra logarithmic term is likely to be small if we take some $y^{0} \in {\mathbb{R}}^{d}$ as some perturbation of $x^{0}$ and initialize

Since we need to compute ${\nabla^{2}f}{(x^{0})}$ to perform the first step of Algorithm 2 Convergence \bottomtitlebar") anyway, the initialization above should be sufficiently cheap to compute. It is immediate to observe that by definition of $H$, the estimate above satisfies $H_{0} \leq H$. Since the proof of Theorem 3 Convergence \bottomtitlebar") mostly follows the lines of the proof of Lemma 3 in, we defer it to the appendix.

Adaptivity. Notice that every global iteration of Algorithm 2 Convergence \bottomtitlebar") includes division of our current estimate $H_{k - 1}$ by a factor of $4$. Since inside the line search we immediately multiply by 2, this means after a single line search iteration, $H_{k}$ is equal to $\frac{H_{k - 1}}{2}$. If the first iteration of line search turns out to be successful, $H_{k}$ remains twice smaller than $H_{k - 1}$, so the algorithm may have a decreasing sequence of estimates. This allows it to adapt to the *local* values of smoothness constant, which might be arbitrarily smaller than the global one.

### Theory for non-linear least squares

In this section, we turn our attention to the least-squares problem,

where $F$ is a smooth operator. The problem is called least squares because it is often used with operator ${F{(x)}} = {{\hat{F}{(x)}} - y}$, where $y$ is a fixed vector of target values. The goal, thus, is to minimize the residuals of approximating $y$. We present the Levenberg--Marquardt algorithm with our penalty in Algorithm 3 Convergence \bottomtitlebar"). The method is often motivated by the fact that it solves a quadratically-regularized subproblem:

In particular, if for some sequence ${\{\lambda_{k}\}}_{k}$ the right-hand side is always larger than ${\|{F{(x)}}\|}^{2}$, then it would always hold ${\|{F{(x^{k + 1})}}\|} \leq {\|{F{(x^{k})}}\|}$. However, for our theory, we will instead assume a *cubic* upper bound.

3: Jk = ∂F (xk) ⊳ Compute the Jacobian of F at point xk
4: $\lambda_{k} = \sqrt{c{\|{\mathbf{J}_{k}^{\top}F{(x^{k})}}\|}}$
5: xk + 1 = xk − (Jk⊤ Jk+λk I)−1 Jk⊤ F (xk) ⊳ Compute xk + 1 by solving a linear system
Algorithm 3 Globally-convergent Levenberg–Marquardt Algorithm for problem

To study the convergence of Algorithm 3 Convergence \bottomtitlebar"), let us first state the assumptions on $F$ and some basic notation. As before we denote by $r_{k} = {\|{x^{k + 1} - x^{k}}\|}$ and we use $\partial{F{(x)}}$ to denote the Jacobian matrix of $F$.

### Assumption 3

We assume that $F$ is a smooth operator such that for some constants ${J,H,c} \geq 0$ and for any ${x,y} \in {\mathbb{R}}^{d}$ it holds ${\|{\partial{F{(x)}}}\|} \leq J$ and

To the best of our knowledge, assumption in equation (15 Convergence \bottomtitlebar")) has not been studied in the prior literature. We resort to it for the simple reason that it is the most likely generalization of 1 Convergence \bottomtitlebar") to the problem of least squares. We also note that an assumption similar to the cubic growth of squared norm in (15 Convergence \bottomtitlebar")) has appeared in the work, where a quadratic upper bound was used for non-squared norm. However, having our cubic assumption is more conservative when $y$ and $x$ are far from each other, so it makes more sense for studying *global* convergence. We also note that 3 Convergence \bottomtitlebar") seems more restrictive than 1 Convergence \bottomtitlebar"), but this is expected since we do not assume any type of convexity for objective (2 Convergence \bottomtitlebar")).

### Lemma 4

### Proof

Multiplying both sides of the update formula (4 Convergence \bottomtitlebar")) by $({{\mathbf{J}_{k}^{\top}\mathbf{J}_{k}} + {\lambda_{k}\mathbf{I}}})$, we derive

which is easy to rearrange into our claim. ∎

### Lemma 5

If 3 Convergence \bottomtitlebar") is satisfied and $\lambda_{k} = \sqrt{c{\|{\mathbf{J}_{k}^{\top}F{(x^{k})}}\|}}$, then

Interestingly, the results of Lemma 5 Convergence \bottomtitlebar") are quite similar to what had in Lemma 2 Convergence \bottomtitlebar"), yet Lemma 2 Convergence \bottomtitlebar") required convexity of the objective. The main reason we managed to avoid such assumptions, is that the matrix $\mathbf{J}_{k}^{\top}\mathbf{J}_{k}$ is always positive semi-definite even if $F$ does not have any nice properties. Thanks to this property, we can establish the following theorem.

### Theorem 4

Under 3 Convergence \bottomtitlebar"), the iterates of Algorithm 3 Convergence \bottomtitlebar") satisfy

The rate in Theorem 4 Convergence \bottomtitlebar") is not particularly impressive, but we should keep in mind that it holds even in the complete absence of convexity. Furthermore, the main feature of the result is that it holds for arbitrary initialization, no matter how far it is from stationary points of the operator $F$. The analysis of Theorem 4 Convergence \bottomtitlebar") is a bit more involved than that of Theorem 1 Convergence \bottomtitlebar"), but follows the same set of ideas, so we defer it to the appendix.

The result in Theorem 4 Convergence \bottomtitlebar") is not the first to establish global convergence of Levenberg--Marquardt algorithm with regularization based on gradient norm. For instance, showed, under Lipschitzness of the gradient of ${\|{F{(x)}}\|}^{2}$, a similar result for regularization $\lambda_{k} \propto {\|{F{(x_{k})}}\|}^{2}$. Ignoring logarithmic factors, they established convergence rate $\mathcal{O}\left( \frac{1}{k^{1/2}} \right)$. Our theory, however, does not requires Lipschitzness of the gradient of ${\|{F{(x)}}\|}^{2}$ and relies instead on inequality (15 Convergence \bottomtitlebar")), so the rates are not directly comparable.

5: $H_{k} = {\max\left\{ M_{k},\frac{H_{k - 1}}{2} \right\}}$
6: $\lambda_{k} = \sqrt{H_{k}{\|{{\nabla f}{(x^{k})}}\|}}$
7: xk + 1 = xk − (∇2f (xk)+λk I)−1 ∇f (xk)⊳ Compute xk + 1 by solving a linear system
Algorithm 4 Heuristic Modification of Algorithm 2 (AdaN+)

## Practical considerations and experiments^11^1Our code is available on GitHub and Google Colab: [https://github.com/konstmish/global-newton](https://github.com/konstmish/global-newton) Colab: [https://colab.research.google.com/drive/1-LmO57VfJ1-AYMopMPYbkFvKBF7YNhW2?usp=sharing](https://colab.research.google.com/drive/1-LmO57VfJ1-AYMopMPYbkFvKBF7YNhW2?usp=sharing)

Before presenting a numerical comparison of the methods that we are interested in, let us discuss some ways that can improve the performance of our method.

Newton's method is very popular in practice despite the lack of global convergence, mostly because it does not need any parameters and it is often initialized sufficiently close to the solution. Our Algorithm 1 Convergence \bottomtitlebar") has the advantage of global convergence, but at the cost of requiring the knowledge of $H$. In contrast, our line search algorithm AdaN does not require parameters and it is guaranteed to converge globally, but it requires evaluation of functional values and is harder to implement. Thus, we ask: can we design an algorithm that would still use some regularization but in a simpler form than in AdaN?

To find a practical algorithm that would be easier to use than AdaN, let us try to find a smaller regularization estimate by taking a look at Lemma 2 Convergence \bottomtitlebar"). Notice that one of the ways $H$ appears in our bounds is through the error of approximating the next gradient. Motivated by this observation, we can define

Using $M_{k}$ instead of $H$ in Algorithm 1 Convergence \bottomtitlebar") is perhaps over-optimistic and in some preliminary experiments did not show a stable behaviour. However, we observed the following estimation to work better in practice:

The definition of $H_{k}$ is motivated by the adaptive estimation of the Lipschitz constant of gradient from, and it achieves two goals. On the one hand, we always have $H_{k} \geq M_{k}$, where $M_{k}$ is the local estimate of the Hessian smoothness. This way, we keep $H_{k}$ closer to the local value of the Hessian smoothness, which might be much smaller than the global value of $H$. On the other hand, since $M_{k}$ is only an underestimate of $H$, i.e., $M_{k} \leq H$, we compensate for the potentially over-optimistic value of $M_{k}$ by using the second condition, $H_{k} \geq \frac{H_{k - 1}}{2}$. All details of the proposed scheme, which we call AdaN+, are given in Algorithm 4 Convergence \bottomtitlebar").

In case of the non-linear least-squares problem, we can similarly estimate $H_{k}$ by defining

The heuristic $H_{k} = {\max\left\{ M_{k},\frac{H_{k - 1}}{2} \right\}}$ is not directly supported by our theory, but the resulting method shall be still more robust than the regularization-free method.

Figure 1: Numerical results on the ℓ2-regularized logistic regression problem with ‘w8a’ dataset (two left plots) and ‘mushrooms’ dataset (two right plots). Our non-adaptive method converged exactly the same way as cubic Newton. Overall, our adaptive methods and Newton method with Armijo line search performed the best.

It is also worth noting that in practice, it is better to avoid the expensive computation of inverse matrices and instead solve linear systems. In particular, if we want to compute $x^{k + 1} = {x^{k} - {{({{{\nabla^{2}f}{(x^{k})}} + {\lambda_{k}\mathbf{I}}})}^{- 1}{\nabla f}{(x^{k})}}}$, it would be easier to solve (in $\Delta$) the following linear system:

The solution $\Delta^{k}$ of the system above is then used to produce $x^{k + 1} = {x^{k} + \Delta^{k}}$. It is a common practice to use some small value $\lambda_{k} > 0$ just to avoid issues arising from machine-precision errors. This may give our algorithms an additional advantage if the objective turns out to be ill-conditioned.

Used methods. We compare our method with a few other standard methods, split into two groups: non-adaptive and adaptive. The non-adaptive methods are: gradient descent with constant stepsize (labeled as 'GD' in the plots); Nesterov's accelerated gradient descent with restarts and constant stepsize; cubic Newton with an estimate of $H$; our Algorithm 1 Convergence \bottomtitlebar") with the same estimate of $H$ as in cubic Newton. The adaptive methods are: gradient descent with Armijo line search; Nesterov's acceleration with Armijo-like line search from; Newton's method with Armijo line search; Adaptive Regularisation with Cubics (ARC); our Algorithms 2 Convergence \bottomtitlebar") and 4 Convergence \bottomtitlebar").

The Armijo line search is combined with gradient descent and Newton's method as follows. Given an iterate $x^{k}$, the gradient descent direction $d^{k} = {- {{\nabla f}{(x^{k})}}}$ or Newton's direction $d^{k} = {- {{({{\nabla^{2}f}{(x^{k})}})}^{- 1}{\nabla f}{(x^{k})}}}$ is computed. Then, a coefficient $\alpha_{k}$ is initialized as $2\alpha_{k - 1}$ and divided by 2 until it satisfies the Armijo condition: ${f{({x^{k} + {\alpha_{k}d^{k}}})}} \leq {{f{(x^{k})}} + {\frac{\alpha_{k}}{2}{\langle{{\nabla f}{(x^{k})}},d^{k}\rangle}}}$. Once such $\alpha_{k}$ is found, the iterate is updated as $x^{k + 1} = {x^{k} + {\alpha_{k}d^{k}}}$. For the Arc method, we use the same hyperparameters as given in Section 7 of, except that we additionally divided $\sigma$ by 2 for very successful iterations to improve its performance. Additional implementation details can be found in the source code.

Logistic regression. Our first experiment concerns the logistic regression problem with $\ell_{2}$ regularization:

where $\sigma:{{\mathbb{R}}\rightarrow{}}$ is the sigmoid function, $\mathbf{A} = {(a_{ij})} \in {\mathbb{R}}^{n \times d}$ is the matrix of features, and $b_{i} \in {\{ 0,1\}}$ is the label of the $i$-th sample. We use the 'w8a' and 'mushrooms' datasets from the LIBSVM package, and set $\ell = 10^{- 10}$ to make the problem ill-conditioned, where $L = {{\|\mathbf{A}\|}^{2}/n}$ is the Lipschitz constant of the gradient. The results are reported in Figure 1 Convergence \bottomtitlebar"). To set $H$, we upper bound the Lipschitz Hessian constant of this function as ${\sup_{x \in {\mathbb{R}}^{d}}{\|{{\nabla^{3}f}{(x)}}\|}} \leq {\frac{1}{6\sqrt{3}}{\max_{i}{{\| a_{i}\|}{\|\mathbf{A}\|}^{2}}}}$. This estimate is not tight, which causes cubic Newton and Algorithm 1 Convergence \bottomtitlebar") to converge very slowly. The adaptive estimators, in contrast, converge after a very small number of iterations. We implemented the iterations of cubic Newton using a binary search in regularization, which, unfortunately, was many times slower than the fast iterations of our algorithm. Nevertheless, we report iteration convergence in our results to better highlight how close our method stays to cubic Newton in the non-adaptive case. We use initialization $x^{0}$ proportional to the vector of ones to better see the global properties.

Figure 2: Numerical results on the log-sum-exp objective with different values of ρ: ρ = 0.5 (left), ρ = 0.25 (middle) and ρ = 0.05 (right). The top row shows non-adaptive methods and the bottom row shows adaptive methods. Only our methods and Arc converged for ρ ∈ {0.25, 0.05}.

Log-sum-exp. In our second experiment, we consider a significantly more ill-conditioned problem of minimizing

where ${a_{1},\ldots,a_{n}} \in {\mathbb{R}}^{d}$ are some vectors and $\rho,b_{1},\ldots,b_{n}$ are scalars. This objectives serves as a smooth approximation of function $\max{\{{{a_{1}^{\top}x} - b_{1}},\ldots,{{a_{n}^{\top}x} - b_{n}}\}}$, with $\rho > 0$ controlling the tightness of approximation. We set $n = 500$, $d = 200$ and randomly generate $a_{1},\ldots,a_{n}$ and $b_{1},\ldots,b_{n}$. After that, we run our experiments for three choices of $\rho$, namely $\rho \in {\{ 0.5,0.25,0.05\}}$. The results are reported in Figure 2 Convergence \bottomtitlebar"). As one can notice, only Algorithms 2 Convergence \bottomtitlebar"), 4 Convergence \bottomtitlebar"), and Arc, performed well in all experiments. Armijo line search was the worst in the last two experiments, most likely due to numerical instability and ill conditioning of the objective. Algorithm 4 Convergence \bottomtitlebar") was less stable than Algorithm 2 Convergence \bottomtitlebar"), which is expected since the former is a simpler heuristic modification of the latter.

## Conclusion

In this paper, we presented a proof that a simple gradient-based regularization allows Newton method to converge globally. Our proof relies on new techniques and appears to be less trivial than that of cubic Newton. At the same time, our analysis has a lot in common with that of cubic Newton and the regularization technique has been known in the literature for a long time. We hope that many existing extensions of cubic Newton, such as its acceleration, will become possible with future work. It would be very exciting to see other extensions, for instance, stochastic variants, and quasi-Newton estimation of the Hessian.
