<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Super-Universal Regularized Newton Method

Topics include Universal regularized Newton method.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We analyze the performance of a variant of Newton method with quadratic regularization for solving composite convex minimization problems. At each step of our method, we choose regularization parameter proportional to a certain power of the gradient norm at the current point. We introduce a family of problem classes characterized by Hölder continuity of either the second or third derivative. Then we present the method with a simple adaptive search procedure allowing an automatic adjustment to the problem class with the best global complexity bounds, without knowing specific parameters of the problem. In particular, for the class of functions with Lipschitz continuous third derivative, we get the global O(1/k^) rate, which was previously attributed to third-order tensor methods. When the objective function is uniformly convex, we justify an automatic acceleration of our scheme, resulting in a faster global rate and local superlinear convergence. The switching between the different rates (sublinear, linear, and superlinear) is automatic. Again, for that, no a priori knowledge of parameters is needed.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Motivation", "weight": 1.0} -->

Newton's method is one of the most important tools in Numerical Analysis and Continuous Optimization. It has a reputation for being a powerful algorithm, especially due to its ability to solve ill-conditioned problems. The method has a local quadratic convergence, thus converging extremely fast in a neighbourhood of the solution. However, the global behaviour of Newton's method has been remaining an active area of research for several decades.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Motivation", "weight": 1.0} -->

It is widely known that the classical Newton method with a unit stepsize may not converge globally, even if the problem is strongly convex (see, e.g., Example 1.4.3 in ). Consequently, there were many techniques developed for the method to improve its global behaviour, including damped Newton steps combined with line search strategies, Levenberg-Marquardt regularization, and trust-region approach. (See also for an extensive historical overview.) However, it was still difficult to establish global complexity guarantees that are provably better than that of the Gradient Methods.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Motivation", "weight": 1.0} -->

A major shift in the paradigm has been made after the work, where cubic regularization of Newton's method (CNM) with its global convergence guarantees was developed. The main idea was to start with a particular problem class, the functions with Lipschitz continuous Hessian, which naturally leads to a globally convergent second-order scheme. The subproblem becomes the minimization of a quadratic model of the function augmented by the third power of Euclidean norm. While each iteration of the method requires solving a univariate nonlinear equation, the arithmetical cost of such an operation remains of the same order as for the standard Newton step.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Motivation", "weight": 1.0} -->

Later, adaptive and universal second-order methods based on cubic regularization with an adjustment of the Lipschitz constant were developed. In, it was shown that the adaptive search makes the CNM work properly on functions with Hölder continuous Hessian, automatically achieving the correct global complexity, and in the universality of CNM was studied on uniformly convex functions.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Motivation", "weight": 1.0} -->

A parallel line of work was done for the Newton method with quadratic regularization. In, the author proposed to use the gradient norm as a regularization coefficient, which preserves the local quadratic convergence of the Newton iterations. However, to ensure a global rate, it was needed to use some damped steps, which make the convergence slower than that of CNM. The idea to approximate the cubic step by a quadratic regularization probably appeared for the first time, still having a worse rate. Eventually, it was first proven, and independently rediscovered, that the use of square root of the gradient norm as the regularization coefficient provides the method with the fast global rate of CNM, while each iteration requires now just one standard matrix inversion.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Motivation", "weight": 1.0} -->

Another emerging trend in Optimization has been to use higher-order Taylor's model of the objective, which potentially would result in even more powerful methods, called Tensor Methods. The price for such an advancement is clear: the subproblem, which is a minimization of the high-order polynomials, becomes more and more difficult. A valuable observation was made, showing that the regularized Taylor polynomial of a convex function is convex, which makes the subproblem solvable. An efficient procedure for computing the third-order tensor step was also proposed there. Following this direction, and utilizing the fact that the third derivative of a convex function is weak, there were developed efficient third-order type schemes which use only the second-order information.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Motivation", "weight": 1.0} -->

In this paper, we develop a surprisingly simple but very powerful regularization strategy for Newton's method, that provides the method with provably fast and universal global convergence rates.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Motivation", "weight": 1.0} -->

The main idea behind our algorithm is to regularize the second-order model of the objective by the square of Euclidean norm, with regularization coefficient proportional to a certain power of the gradient norm. In the simplest case of unconstrained minimization ${\min_{x \in {\mathbb{R}}^{n}}f}{(x)}$, one iteration of our method is as follows: where ${\nabla f}{(x_{k})}$ is the current gradient, ${\nabla^{2}f}{(x_{k})}$ is the current Hessian, and $I$ is the identity matrix. In this scheme, the power $\alpha$ can be fixed arbitrarily from the range $\lbrack\frac{2}{3},1\rbrack$. At the same time, the regularization constant $H_{k}$ is adjusted automatically by a standard backtracking procedure, based on the following stopping criterion: Thus, at each iteration, the method needs to compute the Hessian once, and the average number of the search steps is only two.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Motivation", "weight": 1.0} -->

The algorithm uses matrix inversion as the basic subroutine, which can be implemented either with Linear Algebra tools, or by using a gradient-type solver in the large-scale setting.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Motivation", "weight": 1.0} -->

We show that our strategy works for a wide range of problem classes, characterized by Hölder continuity of either the third or second derivative. The algorithm itself does not need to know any parameters of the problem class. Therefore, our method automatically achieves the rates of convergence of the Gradient Method, Cubic Newton, and third-order Tensor Methods on the corresponding problem classes. Moreover, when the objective is strictly convex, our new algorithm makes sure to get an acceleration, automatically switching between superlinear, linear, and superlinear rates. We attribute the name Super-Universal to a method possessing all these features.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Contributions", "weight": 1.0} -->

[b] Method Easy implementation Local superlinear convergence Global convergence References Lip. grad. Lip. Hess. Lip. 3rd der. Gradient Method ✓ ✗ ✓ ✗ ✗ Classical Newton ✓ ✓ ✗ ✗ ✗ Universal Cubic Newton ✗ ✓ ✓ ✓ ✗ Universal 3rd-order Tensor Method ✗ ✓ ✗ ✓ ✓ Super-Universal Newton ✓ ✓ ✓ ✓ ✓ Ours Table 1: A conceptual comparison of our method to basic deterministic algorithms. Since accelerated methods work on the same problem classes, we do not include them here. For the convergence rates of our method on convex functions, see Corollary 2.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Contributions", "weight": 1.0} -->

We present our theory gradually starting with basic results and eventually leading to Super-Universal Method. We start with Section 2 under the European Union’s Horizon 2020 research and innovation programme (grant agreement No. 788368). The second author acknowledges support by the French government under the management of the Agence Nationale de la Recherche as part of the “Investissements d’avenir” program, reference ANR-19-P3IA-0001 (PRAIRIE 3IA Institute). The research of the third author was also supported by Multidisciplinary Institute in Artificial intelligence MIAI@Grenoble Alpes (ANR-19-P3IA-0003)."), where we introduce the composite optimization problem and discuss properties of the regularized Newton method.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Contributions", "weight": 1.0} -->

In Section 3 under the European Union’s Horizon 2020 research and innovation programme (grant agreement No. 788368). The second author acknowledges support by the French government under the management of the Agence Nationale de la Recherche as part of the “Investissements d’avenir” program, reference ANR-19-P3IA-0001 (PRAIRIE 3IA Institute). The research of the third author was also supported by Multidisciplinary Institute in Artificial intelligence MIAI@Grenoble Alpes (ANR-19-P3IA-0003)."), we present a family of problem classes characterized by Hölder continuity of the second and third derivatives of the smooth part of the objective. We provide a univariate parametrization $2 \leq q \leq 4$ of these classes, introducing the corresponding smoothness parameter $M_{q}$. The particular cases include Lipschitz continuity of the third derivative $({q = 4})$, Lipschitz continuity of the Hessian $({q = 3})$, and bounded variation (or boundedness) of the Hessian $({q = 2})$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Contributions", "weight": 1.0} -->

Section 4 under the European Union’s Horizon 2020 research and innovation programme (grant agreement No. 788368). The second author acknowledges support by the French government under the management of the Agence Nationale de la Recherche as part of the “Investissements d’avenir” program, reference ANR-19-P3IA-0001 (PRAIRIE 3IA Institute). The research of the third author was also supported by Multidisciplinary Institute in Artificial intelligence MIAI@Grenoble Alpes (ANR-19-P3IA-0003).") contains our main tool, that is the choice of regularization coefficient proportional to a certain power of the gradient norm. We prove several inequalities leading to the global and local convergence of the basic steps, which lead to a simple iterative scheme given in Algorithm 1 under the European Union’s Horizon 2020 research and innovation programme (grant agreement No. 788368).

<!-- chunk {"id": "body-0017", "role": "body", "section": "Contributions", "weight": 1.0} -->

The second author acknowledges support by the French government under the management of the Agence Nationale de la Recherche as part of the “Investissements d’avenir” program, reference ANR-19-P3IA-0001 (PRAIRIE 3IA Institute). The research of the third author was also supported by Multidisciplinary Institute in Artificial intelligence MIAI@Grenoble Alpes (ANR-19-P3IA-0003).").

<!-- chunk {"id": "body-0018", "role": "body", "section": "Contributions", "weight": 1.0} -->

In Section 5 under the European Union’s Horizon 2020 research and innovation programme (grant agreement No. 788368). The second author acknowledges support by the French government under the management of the Agence Nationale de la Recherche as part of the “Investissements d’avenir” program, reference ANR-19-P3IA-0001 (PRAIRIE 3IA Institute). The research of the third author was also supported by Multidisciplinary Institute in Artificial intelligence MIAI@Grenoble Alpes (ANR-19-P3IA-0003)."), we develop Super-Universal Newton Method (Algorithm 2 under the European Union’s Horizon 2020 research and innovation programme (grant agreement No. 788368). The second author acknowledges support by the French government under the management of the Agence Nationale de la Recherche as part of the “Investissements d’avenir” program, reference ANR-19-P3IA-0001 (PRAIRIE 3IA Institute).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Contributions", "weight": 1.0} -->

The research of the third author was also supported by Multidisciplinary Institute in Artificial intelligence MIAI@Grenoble Alpes (ANR-19-P3IA-0003).")) with an adaptive search procedure based on a new stopping criterion. Our method does not need to know any parameters of the objective, and achieves a universal global complexity for all our problem classes. For general convex case, the convergence rate is $O{(k^{1 - q})}$ in terms of the functional residual, where $k$ is the iteration counter.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Contributions", "weight": 1.0} -->

In Section 6 under the European Union’s Horizon 2020 research and innovation programme (grant agreement No. 788368). The second author acknowledges support by the French government under the management of the Agence Nationale de la Recherche as part of the “Investissements d’avenir” program, reference ANR-19-P3IA-0001 (PRAIRIE 3IA Institute). The research of the third author was also supported by Multidisciplinary Institute in Artificial intelligence MIAI@Grenoble Alpes (ANR-19-P3IA-0003)."), we study the global and local convergence of our method on subclasses of strictly convex functions. We introduce a new characteristic of optimization problems called $s$-relative size $D_{s}$ ($s \geq 2$). Our definitions clarify the standard notion of uniform convexity and allow continuous change in the convexity degree. For $s = 2$, our assumption implies strong convexity, and for $s = \infty$ it means that the initial level set is bounded with diameter $D \equiv D_{\infty}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Contributions", "weight": 1.0} -->

We show that our method achieves automatically improved rates on these subclasses.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Contributions", "weight": 1.0} -->

The following table provides a summary of the global complexity guarantees. We are interested in the number of iterations to reach $\varepsilon$ accuracy in terms of the functional residual (presenting only the main terms and omitting absolute constants). $\left. ({M_{q}\frac{D_{s}^{s}D^{q - s}}{V_{F}}} \right)^{\frac{1}{q - 1}} + {\ln{\ln\frac{1}{\varepsilon}}}$​ $\left. ({M_{q}\frac{D_{q}^{q}}{V_{F}}} \right)^{\frac{1}{q - 1}}{\ln\frac{1}{\varepsilon}}$ $\left.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Contributions", "weight": 1.0} -->

({M_{q}\frac{D_{s}^{q}}{\left({V_{F}^{q}\varepsilon^{s - q}} \right)^{1/s}}} \right)^{\frac{1}{q - 1}}$​​ $\left. ({M_{q}\frac{D^{q}}{\varepsilon}} \right)^{\frac{1}{q - 1}}$​​ Table 2: Global Complexity of Super-Universal Newton Method (Algorithm 2). If s = 2, it means the objective is strongly convex, and we have superlinear convergence. VF denotes the size of the initial level set measured by symmetrized Bregman divergence, defined.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Contributions", "weight": 1.0} -->

Qualitatively, the rates are split into two regions with a switching line in the rate of convergence given by the case $s = q$. For $2 \leq s \leq q$, the complexity depends on target accuracy $\varepsilon$ only logarithmically. When $s < q$, the method has a superlinear convergence, and the case $s = q$ gives us the global linear rate. For $s > q$, the dependence on accuracy is polynomial, which corresponds to sublinear rates. The whole picture becomes two-dimensional taking into account the range for the degree of smoothness: $2 \leq q \leq 4$ (see Figure 1 under the European Union’s Horizon 2020 research and innovation programme (grant agreement No. 788368). The second author acknowledges support by the French government under the management of the Agence Nationale de la Recherche as part of the “Investissements d’avenir” program, reference ANR-19-P3IA-0001 (PRAIRIE 3IA Institute).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Contributions", "weight": 1.0} -->

The research of the third author was also supported by Multidisciplinary Institute in Artificial intelligence MIAI@Grenoble Alpes (ANR-19-P3IA-0003).")).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Contributions", "weight": 1.0} -->

Note that our new algorithm provides us with the worst-case complexity bounds for all known problem classes with computable second derivative supported till now by different first-, second- and third-order schemes. Moreover, our Super-Universal Newton Method seems to eliminate the need of using non-accelerated third-order Tensor Methods in Convex Optimization.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Contributions", "weight": 1.0} -->

Finally, we present our numerical experiments in Section 7 under the European Union’s Horizon 2020 research and innovation programme (grant agreement No. 788368). The second author acknowledges support by the French government under the management of the Agence Nationale de la Recherche as part of the “Investissements d’avenir” program, reference ANR-19-P3IA-0001 (PRAIRIE 3IA Institute). The research of the third author was also supported by Multidisciplinary Institute in Artificial intelligence MIAI@Grenoble Alpes (ANR-19-P3IA-0003)."), and provide a discussion on possible future developments in Section 8 under the European Union’s Horizon 2020 research and innovation programme (grant agreement No. 788368). The second author acknowledges support by the French government under the management of the Agence Nationale de la Recherche as part of the “Investissements d’avenir” program, reference ANR-19-P3IA-0001 (PRAIRIE 3IA Institute).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Contributions", "weight": 1.0} -->

The research of the third author was also supported by Multidisciplinary Institute in Artificial intelligence MIAI@Grenoble Alpes (ANR-19-P3IA-0003).").

<!-- chunk {"id": "body-0029", "role": "body", "section": "Overview of the Main Ideas", "weight": 1.0} -->

Before we proceed to formal proofs and detailed explanation of the main results, let us first sketch them here to provide a high-level intuition. For simplicity, we start with a discussion on how to solve the problem ${\min_{x}f}{(x)}$ without any nonsmooth components.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Removing Third Derivatives", "weight": 1.0} -->

An early observation was made in that a third-order Tensor Method can be implemented using second-order oracle calls with an auxiliary procedure that computes the action ${\nabla^{3}f}{(x)}{\lbrack h\rbrack}^{2}$ of the tensor of the third derivative to an arbitary vector $h$. This is in a way similar to how second-order Newton method can be implemented by running a first-order method on a quadratic subproblem. Where the similarity disappears, however, is that third-order subproblem requires only near-constant number of inner iterations, independently of any other function properties.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Removing Third Derivatives", "weight": 1.0} -->

This observation was also used in to design inexact third-order methods that rely solely on second-order oracle, approximating the action of the third derivative by a finite difference. Following upon these results, we find it natural to ask: Is it possible to skip formulating third-order subproblems and show instead that a simple second-order method is sufficient to achieve faster convergence?

<!-- chunk {"id": "body-0032", "role": "body", "section": "Removing Third Derivatives", "weight": 1.0} -->

It turns out that the answer is positive. The first step is to notice that, as stated in Lemma 3, when the third derivative of a convex function is Lipschitz continuous (with constant $M_{4} > 0$), one can show that its impact is always bounded as follows: In other words, the third-order term is fully controlled by a combination of second-order and fourth-order terms. We can immediately plug this in the global upper bound on function, which holds for any $x,y, \in {\mathbb{E}}$, and get Optimizing this upper bound exactly would give a Newton-type iteration, but it still has two disadvantages. Firstly, the coefficient in front of the Hessian is not $\frac{1}{2}$. At the same time, the factor $\frac{1}{2}$ is the best from the local perspective since it is responsible for the local superlinear convergence of the method. Secondly, the last term in the upper bound makes it polynomial of degree four and gives us a subproblem which is not trivially to solve.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Removing Third Derivatives", "weight": 1.0} -->

In our work, we provide a solution to both of these challenges by showing that we do not actually need to minimize the upper bound exactly. Instead, we prove that a regularized Newton iteration is sufficient to decrease the functional values despite not being an exact minimizer of this upper bound.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Gradient Regularization", "weight": 1.0} -->

Our idea to simplify the upper bound in (1 under the European Union’s Horizon 2020 research and innovation programme (grant agreement No. 788368). The second author acknowledges support by the French government under the management of the Agence Nationale de la Recherche as part of the “Investissements d’avenir” program, reference ANR-19-P3IA-0001 (PRAIRIE 3IA Institute). The research of the third author was also supported by Multidisciplinary Institute in Artificial intelligence MIAI@Grenoble Alpes (ANR-19-P3IA-0003).")) stems from the prior results on simplifying the Cubic Newton iteration. In CNM, each iteration is obtained by solving with some constant $M_{3} > 0$. Because of the cubic term, this equation has no closed-form solution. At the same time, it was shown in and later in that if we replace the cubic regularization by a quadratic with an appropriately chosen coefficient, the method would still converge with the same rate.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Gradient Regularization", "weight": 1.0} -->

In particular, if we set $\lambda_{k} = \sqrt{\frac{M_{3}}{3}{\|{{\nabla f}{(x_{k})}}\|}_{\ast}}$ and produce the iterates by solving then the rate of convergence remains the same as for CNM. Conceptually, there is little difference between cubic and quartic regularization as it appears in (1 under the European Union’s Horizon 2020 research and innovation programme (grant agreement No. 788368). The second author acknowledges support by the French government under the management of the Agence Nationale de la Recherche as part of the “Investissements d’avenir” program, reference ANR-19-P3IA-0001 (PRAIRIE 3IA Institute). The research of the third author was also supported by Multidisciplinary Institute in Artificial intelligence MIAI@Grenoble Alpes (ANR-19-P3IA-0003).")). Therefore, we can apply the same ideas and replace the fourth power by the second again.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Gradient Regularization", "weight": 1.0} -->

A simple derivation shows that to lift the quartic regularization to the quadratic one, we need to use $\lambda_{k} = {H_{k}{\|{{\nabla f}{(x_{k})}}\|}_{\ast}^{\frac{2}{3}}}$ with a sufficiently large constant $H_{k} > 0$. An immediate drawback is that this approach requires knowing the problem class to choose the power of the gradient norm in the expression for $\lambda_{k}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Gradient Regularization", "weight": 1.0} -->

Indeed, we have to choose whether to use $\lambda_{k} \propto {\|{{\nabla f}{(x_{k})}}\|}_{\ast}^{\frac{1}{2}}$ or $\lambda_{k} \propto {\|{{\nabla f}{(x_{k})}}\|}_{\ast}^{\frac{2}{3}}$, and this choice is not trivial, since our objective can belong to several problem classes simultaneously. Thus, we must ask: Is it possible to design a method that would not require to know the parameters of the problem?

<!-- chunk {"id": "body-0038", "role": "body", "section": "Super Universality", "weight": 1.0} -->

As we have stated, regularized Newton is applicable to several problem classes at the same time, but it requires different strategies for choosing $\lambda_{k}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Super Universality", "weight": 1.0} -->

In prior works, however, it was shown that one regularization strategy can sometimes work properly for different problem classes. In particular, and studied CNM for functions whose Hessian is Hölder continuous, and the method does not need to know the Hölder parameter. One of our goals, therefore, is to make our Newton method adaptive not just to the class of functions based on whether it is second or third derivative that is Lipschitz continuous, but also to the Hölder constant within each of the classes.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Super Universality", "weight": 1.0} -->

By working in this direction, we managed to obtain a universal regularization rule that works across all considered function classes. It turned out that we can use $\lambda_{k} = {H_{k}{\|{{\nabla f}{(x_{k})}}\|}_{\ast}^{\alpha}}$ with any $\alpha \in {\lbrack\frac{2}{3},1\rbrack}$ fixed in advance, without even knowing what properties the minimized function has. Parameter $H_{k}$ is adjusted automatically by a standard adaptive procedure. This approach makes our Newton method much more universal than any other prior regularization techniques, as for solving unconstrained convex minimization problems.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Composite Optimization", "weight": 1.0} -->

Finally, it is important in many applications to support additional nonsmooth components, such as constraints or $\ell_{1}$-regularization. This corresponds to minimizing ${f{(x)}} + {\psi{(x)}}$, where $\psi{(x)}$ is a nonsmooth function. In first-order optimization, one can use so-called proximal operator that may even have a closed-form solution. In second-order optimization, the subproblem becomes more difficult, which requires minimization of quadratic function with the extra component $\psi$. Thus, for the complex $\psi$, we can no longer solve the iteration as a simple linear system. However, we can use first-order gradient-based solvers for computing an inexact iteration. The composite formulation covers more applications, and we still do not have to worry about which problem class function $f$ belongs to. This extension is more straightforward than the other steps as it has been already considered for regularized Newton method.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Regularized Newton Step", "weight": 1.0} -->

Consider the following composite optimization problem: where function $f{(\cdot)}$ is convex and several times differentiable, and $\psi:{{\mathbb{E}}\rightarrow{{\mathbb{R}} \cup {\{{+ \infty}\}}}}$ is a proper closed convex function with ${{dom}\psi} \subseteq {\mathbb{E}}$. For some $\lambda > 0$, consider the step of a variant of Newton method with quadratic regularization: If the composite part is absent (${\psi{(y)}} \equiv 0$), this step can be rewritten in an explicit form: which is often called the Levenberg-Marquardt regularization. In the presence of $\psi{(\cdot)}$, the point $T = {T_{\lambda}{(x)}}$ satisfies the following stationary condition: for any $y \in {{dom}\psi}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Regularized Newton Step", "weight": 1.0} -->

Let us derive some inequalities for one step of the method. Let $\mu \geq 0$ be a uniform bound for the minimal eigenvalue of the Hessian: ${{\nabla^{2}f}{(x)}} \succeq {\muB}$, ${\forall x} \in {{dom}\psi}$. Note that, for any $s \in {\partial{\psi{(x)}}}$, it holds Therefore, we obtain the following inequality.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Problem Classes", "weight": 1.0} -->

For the differentiable part of our objective function, let us introduce some smoothness characteristics. Namely, let us assume that either its Hessian or its third derivative is Hölder continuous. For that, let us define the following family of constants: where $p = 2$ or $p = 3$ and $\nu \in {\lbrack 0,1\rbrack}$. Since we see that $L_{p,\nu}$ is a log-convex function of $\nu$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Example 1", "weight": 1.0} -->

The second author acknowledges support by the French government under the management of the Agence Nationale de la Recherche as part of the “Investissements d’avenir” program, reference ANR-19-P3IA-0001 (PRAIRIE 3IA Institute). The research of the third author was also supported by Multidisciplinary Institute in Artificial intelligence MIAI@Grenoble Alpes (ANR-19-P3IA-0003).")).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The value $M_{q}$ is finite for at least one $q \in {\lbrack 2,4\rbrack}$: Note that $M_{2} \leq {\sup_{x}{\|{{\nabla^{2}f}{(x)}}\|}}$. Thus, we cover even the standard class for the first-order methods.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

It appears that the global complexity of the regularized Newton method depends on the values $M_{q}$, $2 \leq q \leq 4$, in a very natural and universal way. At the same time, it is important that our super-universal algorithm, presented in Section 5 under the European Union’s Horizon 2020 research and innovation programme (grant agreement No. 788368). The second author acknowledges support by the French government under the management of the Agence Nationale de la Recherche as part of the “Investissements d’avenir” program, reference ANR-19-P3IA-0001 (PRAIRIE 3IA Institute). The research of the third author was also supported by Multidisciplinary Institute in Artificial intelligence MIAI@Grenoble Alpes (ANR-19-P3IA-0003)."), does not need explicit values of these constants.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Gradient Regularization", "weight": 1.0} -->

At each step of our method, we are going to use the following choice of the regularization parameter: where $H > 0$ and $\alpha \in {\lbrack 0,1\rbrack}$ are some constants, and $g:={\|{{{\nabla f}{(x)}} + s}\|}_{\ast}$ for some $s \in {\partial{\psi{(x)}}}$. Let us investigate some properties of this choice, taking into account our smoothness condition (14 under the European Union’s Horizon 2020 research and innovation programme (grant agreement No. 788368). The second author acknowledges support by the French government under the management of the Agence Nationale de la Recherche as part of the “Investissements d’avenir” program, reference ANR-19-P3IA-0001 (PRAIRIE 3IA Institute). The research of the third author was also supported by Multidisciplinary Institute in Artificial intelligence MIAI@Grenoble Alpes (ANR-19-P3IA-0003).")).

<!-- chunk {"id": "body-0049", "role": "body", "section": "Gradient Regularization", "weight": 1.0} -->

We start with the case $2 \leq q < 3$ (Hölder continuity of the Hessian).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Note that inequality (23 under the European Union’s Horizon 2020 research and innovation programme (grant agreement No. 788368). The second author acknowledges support by the French government under the management of the Agence Nationale de la Recherche as part of the “Investissements d’avenir” program, reference ANR-19-P3IA-0001 (PRAIRIE 3IA Institute). The research of the third author was also supported by Multidisciplinary Institute in Artificial intelligence MIAI@Grenoble Alpes (ANR-19-P3IA-0003).")) implies Now, let us look at the simplest way of choosing regularization constants, when parameter $q \in {\lbrack 2,4\rbrack}$ is known and fixed. By Corollary 1 under the European Union’s Horizon 2020 research and innovation programme (grant agreement No. 788368). The second author acknowledges support by the French government under the management of the Agence Nationale de la Recherche as part of the “Investissements d’avenir” program, reference ANR-19-P3IA-0001 (PRAIRIE 3IA Institute).

<!-- chunk {"id": "body-0051", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The research of the third author was also supported by Multidisciplinary Institute in Artificial intelligence MIAI@Grenoble Alpes (ANR-19-P3IA-0003)."), we can take This way, we obtain Algorithm 1 under the European Union’s Horizon 2020 research and innovation programme (grant agreement No. 788368). The second author acknowledges support by the French government under the management of the Agence Nationale de la Recherche as part of the “Investissements d’avenir” program, reference ANR-19-P3IA-0001 (PRAIRIE 3IA Institute). The research of the third author was also supported by Multidisciplinary Institute in Artificial intelligence MIAI@Grenoble Alpes (ANR-19-P3IA-0003).").

<!-- chunk {"id": "body-0052", "role": "body", "section": "Remark 1", "weight": 1.0} -->

By convexity, we get the following progress for one step of this method: This inequality results in a global convergence rate for our process. In the next Section 5 under the European Union’s Horizon 2020 research and innovation programme (grant agreement No. 788368). The second author acknowledges support by the French government under the management of the Agence Nationale de la Recherche as part of the “Investissements d’avenir” program, reference ANR-19-P3IA-0001 (PRAIRIE 3IA Institute). The research of the third author was also supported by Multidisciplinary Institute in Artificial intelligence MIAI@Grenoble Alpes (ANR-19-P3IA-0003)."), we derive it explicitly. However, the main drawback of this scheme is that we need to fix the degree of smoothness $q \in {\lbrack 2,4\rbrack}$ in advance. The parameter $M_{q}$ is also needed. Hence, the above scheme is completely theoretical and cannot be used in practice.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The super-universal method, presented in Section 5 under the European Union’s Horizon 2020 research and innovation programme (grant agreement No. 788368). The second author acknowledges support by the French government under the management of the Agence Nationale de la Recherche as part of the “Investissements d’avenir” program, reference ANR-19-P3IA-0001 (PRAIRIE 3IA Institute). The research of the third author was also supported by Multidisciplinary Institute in Artificial intelligence MIAI@Grenoble Alpes (ANR-19-P3IA-0003)."), resolves both these issues by a simple search procedure.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Super-Universal Method", "weight": 1.0} -->

At each iteration of this scheme, we adjust the regularization constant $H_{k}$ for ensuring inequality (23 under the European Union’s Horizon 2020 research and innovation programme (grant agreement No. 788368). The second author acknowledges support by the French government under the management of the Agence Nationale de la Recherche as part of the “Investissements d’avenir” program, reference ANR-19-P3IA-0001 (PRAIRIE 3IA Institute). The research of the third author was also supported by Multidisciplinary Institute in Artificial intelligence MIAI@Grenoble Alpes (ANR-19-P3IA-0003).")). Degree $\alpha \in {\lbrack\frac{2}{3},1\rbrack}$ of the gradient regularization is chosen in advance and does not depend on a particular problem class.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Strictly Convex Functions", "weight": 1.0} -->

Let us analyze convergence of Algorithm 2 under the European Union’s Horizon 2020 research and innovation programme (grant agreement No. 788368). The second author acknowledges support by the French government under the management of the Agence Nationale de la Recherche as part of the “Investissements d’avenir” program, reference ANR-19-P3IA-0001 (PRAIRIE 3IA Institute). The research of the third author was also supported by Multidisciplinary Institute in Artificial intelligence MIAI@Grenoble Alpes (ANR-19-P3IA-0003).") on some subclasses of strictly convex functions. As we will see, an automatic acceleration on such functions ensures much faster global rates, as well as the local superlinear convergence.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Strictly Convex Functions", "weight": 1.0} -->

As in the previous sections, consider the initial sublevel set We have used the primal norm $\parallel \cdot \parallel$ for measuring its size, denoting However, this is not the only possibility. The other natural measure would be the symmetrized Bregman divergence induced by our objective: for some fixed selection of subgradients $G_{x} \in {\partial{F{(x)}}}$ and $G_{y} \in {\partial{F{(y)}}}$. Note that strict convexity ensures ${\beta_{F}{(x,y)}} > 0$ for $x \neq y$. Defining and assuming its boundedness, we can use the following normalized measure: It is interesting that the relations between these two measures have important consequences for complexity of the corresponding problem (2 under the European Union’s Horizon 2020 research and innovation programme (grant agreement No. 788368).

<!-- chunk {"id": "body-0057", "role": "body", "section": "Strictly Convex Functions", "weight": 1.0} -->

The second author acknowledges support by the French government under the management of the Agence Nationale de la Recherche as part of the “Investissements d’avenir” program, reference ANR-19-P3IA-0001 (PRAIRIE 3IA Institute). The research of the third author was also supported by Multidisciplinary Institute in Artificial intelligence MIAI@Grenoble Alpes (ANR-19-P3IA-0003).")). Let us introduce a new characteristic called $s$-relative size ($s \geq 2$). Denote^11^1We use a conventional notation ${1/\infty} = 0$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Strictly Convex Functions", "weight": 1.0} -->

Thus, by our definition $D_{\infty} = D$. Note that Since the last expression is a pointwise supremum of convex functions, we conclude that $D_{s}$ is a log-convex function of $s$. Hence, if for some $2 \leq s_{1} \leq s_{2}$ we have ${D_{s_{i}} < {+ \infty}},{i \in {\{ 1,2\}}}$, then and $D_{s}$ is continuous on this segment.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Example 3", "weight": 1.0} -->

Let $F$ be uniformly convex of degree $s \geq 2$. Then for all ${G_{x} \in {\partial{F{(x)}}}},{G_{y} \in {\partial{F{(y)}}}}$ and some $\sigma_{s} > 0$. Hence, Let us also prove the following useful lifting property.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

If $s = 2$, this assumption implies strong convexity. If $s = \infty$, it means that the set $\mathcal{F}_{0}$ is bounded.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Since we define the relative size $D_{s}$ for the entire composite objective, parameter $s \geq 2$ is not necessarily consistent with the degree of smoothness $q \in {\lbrack 2,4\rbrack}$. Let us analyze the convergence rate of our method for different ranges of these parameters. We start with establishing the bound on the functional progress during one iteration.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Since ${\lim\limits_{\alpha\rightarrow 0}\frac{x^{\alpha} - y^{\alpha}}{\alpha}} = {\lim\limits_{\alpha\rightarrow 0}\frac{e^{\alpha{\ln x}} - e^{\alpha{\ln y}}}{\alpha}} = {\ln\frac{x}{y}}$, for ${\gamma = 1}\Leftrightarrow{s = q}$, we treat the left-hand side of (46 under the European Union’s Horizon 2020 research and innovation programme (grant agreement No. 788368). The second author acknowledges support by the French government under the management of the Agence Nationale de la Recherche as part of the “Investissements d’avenir” program, reference ANR-19-P3IA-0001 (PRAIRIE 3IA Institute).

<!-- chunk {"id": "body-0063", "role": "body", "section": "Remark 2", "weight": 1.0} -->

The research of the third author was also supported by Multidisciplinary Institute in Artificial intelligence MIAI@Grenoble Alpes (ANR-19-P3IA-0003).")) as its limit, which gives For one step of the method, we have First, let us consider the case $s \geq q$. Then, $\gamma \in {\lbrack 1,2\rbrack}$. Using concavity of ${{y{(x)}} = x^{\gamma - 1}},{x \geq 0}$, and monotonicity of ${\{ F_{k}\}}_{k \geq 0}$, we obtain When $2 \leq s < q$, we have $\gamma < 1$. In this case, we can use concavity of ${{y{(x)}} = x^{1 - \gamma}},{x \geq 0}$. This yields Inequality (46 under the European Union’s Horizon 2020 research and innovation programme (grant agreement No. 788368).

<!-- chunk {"id": "body-0064", "role": "body", "section": "Remark 2", "weight": 1.0} -->

The second author acknowledges support by the French government under the management of the Agence Nationale de la Recherche as part of the “Investissements d’avenir” program, reference ANR-19-P3IA-0001 (PRAIRIE 3IA Institute). The research of the third author was also supported by Multidisciplinary Institute in Artificial intelligence MIAI@Grenoble Alpes (ANR-19-P3IA-0003).")) provides us with a continuous in $\gamma$ characterization of the global behavior of the method. We are ready to describe its global complexity. Let us start with the case $s \geq q$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Polytope Feasibility", "weight": 1.0} -->

We compare our method for $\alpha = \frac{2}{3}$ and $\alpha = 1$ with the following algorithms: Cubic Newton, Gradient Method, and Fast Gradient Method. In all the methods we use adaptive estimation of the regularization parameter.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Polytope Feasibility", "weight": 1.0} -->

We generate data from random uniform distribution on $\lbrack{- 1},1\rbrack$, and start the methods from $x_{0} = {(1,\ldots,1)}^{\top} \in {\mathbb{R}}^{n}$. In many cases, we had degenerate Hessian at the initial point ${\nabla^{2}f}{(x_{0})}$, and so it is impossible to use a Damped Newton Method. The results are shown below^22^2The source code can be found at Thus, the second-order methods demonstrate extremely good performance in terms of the number of iterations (oracle calls). The practical convergence of the Cubic Newton seems to be slightly better than those with quadratic regularization. However, each iteration of the latter methods is cheaper, which results in much better total computational time (see the second graph in each pair).

<!-- chunk {"id": "body-0067", "role": "body", "section": "Soft Maximum", "weight": 1.0} -->

For $\mu > 0$, consider the unconstrained minimization problem ${\min_{x \in {\mathbb{R}}^{n}}f}{(x)}$ with the following objective, The entries of vectors ${a_{1},\ldots,a_{m}} \in {\mathbb{R}}^{n}$ and $b \in {\mathbb{R}}^{m}$ are generated randomly and independently from the uniform distribution on $\lbrack{- 1},1\rbrack$, and $\mu$ is a smoothing parameter. We use the primal norm, with the following matrix: $B = {\sum_{i = 1}^{m}{a_{i}a_{i}^{\top}}}$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Soft Maximum", "weight": 1.0} -->

Then we have (Example 1.3.5 in): Thus, for $\varepsilon > 0$, our method needs to do the following number of iterations: By an appropriate shifting of all vectors ${\{ a_{i}\}}_{i = 1}^{m}$, we can ensure ${{\nabla f}{}} = 0$, placing the optimum to the origin. We run Algorithm 2 under the European Union’s Horizon 2020 research and innovation programme (grant agreement No. 788368). The second author acknowledges support by the French government under the management of the Agence Nationale de la Recherche as part of the “Investissements d’avenir” program, reference ANR-19-P3IA-0001 (PRAIRIE 3IA Institute).

<!-- chunk {"id": "body-0069", "role": "body", "section": "Soft Maximum", "weight": 1.0} -->

The research of the third author was also supported by Multidisciplinary Institute in Artificial intelligence MIAI@Grenoble Alpes (ANR-19-P3IA-0003).") with different values of the gradient power $\alpha = {0,\frac{1}{2},\frac{2}{3},1}$. The results are presented below.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Soft Maximum", "weight": 1.0} -->

The method shows a robust behaviour in terms of the dependence on $\alpha$ (left graph). However, the choice $\alpha:=1$ enforces a more stable range for the regularization parameter $H_{k}$ adjusted by the adaptive search (right graph).

<!-- chunk {"id": "body-0071", "role": "body", "section": "Worst Instances", "weight": 1.0} -->

In this experiment, we apply our methods to unconstrained minimization of the following objective, where $q \geq 2$ is a parameter. Note that the structure of this objective is very similar to the worst-case function from lower bounds for high-order methods, and there is a bound for the smoothness constants: $M_{q} \leq {2^{q}{({q!})}}$. We compare the method with fixed constants of regularization and super-universal methods. The results are shown below.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Worst Instances", "weight": 1.0} -->

We observe a switching point in the behaviour when the number of iterations reaches the dimensionality of the problem. In the case of super-universal methods, the rate becomes superlinear after this moment, and any desirable accuracy can be achieved just in few extra steps.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this paper, we have developed and analyzed the Super-Universal Newton Method based on regularization of the second-order model by the square of Euclidean norm. The regularization parameter is proportional to a power of the gradient norm. Each step of our method is easily computable, employing in the unconstrained case just the standard matrix inversion.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Discussion", "weight": 1.5} -->

We have proved that using a simple adaptive search procedure in each iteration, the method has a universal global convergence rate among problem classes with Hölder continuous second or third derivatives. If the problem is uniformly convex, the method automatically switches between sublinear, linear, and superlinear rates, adjusting to the best possible problem class.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Discussion", "weight": 1.5} -->

A natural extension of our results would be development of accelerated super-universal schemes (see for the line of works on accelerated second- and high-order methods matching the corresponding lower bounds ). One of the major obstacles remains to be the sensitivity of accelerated methods to the parameters of a problem class. In addition, these methods usually require knowledge of the constant of strong/uniform convexity. For practical applications, it is also crucial for a second-order method to have a superlinear convergence (at least locally), which is missing for most of the accelerated schemes.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Discussion", "weight": 1.5} -->

Another important direction is the creation of methods that are suitable for non-Euclidean geometry. In our method we fix the Euclidean norm as a regularizer, while it is also possible to use for that a contraction of the feasible domain, leading to affine-invariant contracting-point methods, or an appropriate Bregman divergence (see also for the framework of relative smoothness).

<!-- chunk {"id": "body-0077", "role": "body", "section": "Discussion", "weight": 1.5} -->

For solving large-scale problems, our method can be equipped with modern stochastic techniques which are able to keep versatile convergence guarantees. Another potential way to make the methods more applicable to high-dimensional objectives is to consider quasi-Newton updates, which at the moment seems to be very challenging due to the lack of theoretical results on their global behavior.
