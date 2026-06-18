<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Speed-Robustness Trade-Off for First-Order Methods with Additive Gradient Noise

Topics include Gradient descent, Robustness, Optimization, GD, S heavy Ball, HB, S Fast gradient, FG, Convex function.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the trade-off between convergence rate and sensitivity to stochastic additive gradient noise for first-order optimization methods. Ordinary Gradient Descent (GD) can be made fast-and-sensitive or slow-and-robust by increasing or decreasing the stepsize, respectively. However, it is not clear how such a trade-off can be navigated when working with accelerated methods such as Polyak's Heavy Ball (HB) or Nesterov's Fast Gradient (FG) methods. We consider two classes of functions: strongly convex quadratics and smooth strongly convex functions. For each function class, we present a tractable way to compute the convergence rate and sensitivity to additive gradient noise for a broad family of first-order methods, and we present algorithm designs that trade off these competing performance metrics. Each design consists of a simple analytic update rule with two states of memory, similar to HB and FG. Moreover, each design has a scalar tuning parameter that explicitly trades off convergence rate and sensitivity to additive gradient noise. We numerically validate the performance of our designs by comparing their convergence rate and sensitivity to those of many other algorithms, and through simulations on Nesterov's "bad function".

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

We consider the problem of designing robust first-order methods for unconstrained minimization. Given a continuously differentiable function $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$, consider solving the optimization problem

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

where the algorithm only has access to gradient measurements corrupted by additive stochastic noise.^11^1Preliminary versions of portions of this work appeared in the conference proceedings. Specifically, the algorithm can sample the oracle ${g{(x)}}{: =}{{{\nabla f}{(x)}} + w}$, where $w$ is zero-mean and independent across queries. This form of additive noise arises in various applications. For example, (i) to protect sensitive data, optimization algorithms may intentionally perturb the gradient by Gaussian noise in order to obtain differential privacy; (ii) for some engineering systems, the gradient can only be obtained through noisy measurements; and (iii) in risk minimization in the context of learning algorithms, the objective is to minimize the expectation of the loss function over the population distribution.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many iterative algorithms have been proposed to solve this problem, and most have tunable parameters. For example, Gradient Descent (GD) uses the update

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $t$ is the iteration index and the stepsize $\alpha$ is a tunable parameter. Fig. 1 illustrates how the error $\parallel{x^{t} - x^{\star}}\parallel$ evolves under GD applied to strongly convex quadratic functions for different fixed $\alpha$. The convergence of the error is characterized by an initial transient phase followed by a stationary phase. In the transient phase, the gradient dominates the noise, and the error converges at a linear rate. When the gradient is small enough that the noise becomes significant, the average error of the iterates converges to a constant value.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

This two-phase behavior is typical of stochastic methods.^22^2In the literature, stepsize is also known as *learning rate*. The transient phase is also known as the *search* or *burn-in* phase. The stationary phase is also known as the *convergence* or *steady-state* phase. The fundamental trade-off is that faster initial convergence comes at the cost of larger steady-state error.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Gradient Descent is easy to interpret and tune: the stepsize directly mediates the trade-off between convergence rate and sensitivity. Unfortunately, GD is generally slow to converge, and alternative methods can provide faster convergence rates. Two such methods are Polyak's Heavy Ball and Nesterov's Fast Gradient, which use the updates

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

When using a noisy gradient oracle, these methods exhibit a stationary phase similar to that of GD in Fig. 1. A trade-off between convergence rate and sensitivity to noise must also exist for HB and FG, but there are now two parameters to tune, so it is unclear how they should be modified to mediate this trade-off.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The goal of the present work is to study the trade-off between rate and sensitivity for first-order algorithms, and to design algorithms that trade off these competing performance metrics. We consider two well-studied classes of functions $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ characterized by scalar parameters $m$ and $L$ that satisfy $0 < m \leq L < \infty$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

These classes of functions are nested in the sense that $Q_{m,L} \subseteq F_{m,L}$ with equality occurring when $m = L$. Moreover, all functions in these classes have a unique optimal point $y^{\star} = {{{\arg\min}_{y \in {\mathbb{R}}^{d}}f}{(y)}}$ satisfying ${{\nabla f}{(y^{\star})}} = 0$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $\alpha$, $\beta$, $\eta$ are scalar parameters. This parameterization was first introduced and is further discussed in Section 2.2. Note that GD, HB, FG are special cases of the three-parameter family that use $\beta = \eta = 0$, $\eta = 0$, and $\eta = \beta$, respectively.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Main contributions", "weight": 1.0} -->

Our three main contributions are as follows.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Main contributions", "weight": 1.0} -->

For the function classes $Q_{m,L}$ and $F_{m,L}$, we present a method for efficiently bounding the worst-case convergence rate and sensitivity to additive gradient noise for a wide class of algorithms. The computational effort required to find the rate and sensitivity bounds for a given algorithm is independent of problem dimension $d$ and takes fractions of a second on a laptop.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Main contributions", "weight": 1.0} -->

We present two new algorithms, RHB and RAM, for the function classes $Q_{m,L}$ and $F_{m,L}$, respectively. Each algorithm has the form, where $(\alpha,\beta,\eta)$ are explicit algebraic functions of $m$ and $L$ and a scalar tuning parameter $r$ that directly trades off convergence rate and sensitivity to gradient noise.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Main contributions", "weight": 1.0} -->

We demonstrate through empirical studies that our algorithm designs effectively trade-off convergence rate and sensitivity to gradient noise. We use a brute-force approach to compare our algorithms against a dense sampling of algorithms of the form. We also show that our designs compare favorably to (i) popular algorithms such as nonlinear conjugate gradient and quasi-Newton methods, and (ii) existing designs that use more parameters.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Paper organization", "weight": 1.0} -->

We first provide additional background on the problem and describe our analysis and design methodology. In Section 2, we describe the problem setting and performance measures we will use. Sections 3 and treat $Q_{m,L}$ and $F_{m,L}$, respectively. For each, we present a computationally tractable approach to computing convergence rate and noise sensitivity, and a novel algorithm design. In Section 5, we present empirical studies that support the effectiveness of our designs and compare them to existing algorithms. We conclude in Section 6.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Complexity bounds", "weight": 1.0} -->

The noise-free setting is well-studied, and algorithms have been discovered that achieve optimal worst-case iteration complexity for a variety of different function classes. We discuss these results in Sections 3.2 and 4.5, where we present our algorithm designs for $Q_{m,L}$ and $F_{m,L}$, respectively.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Complexity bounds", "weight": 1.0} -->

In the additive gradient noise setting, there are fundamental lower bounds on the asymptotic convergence rate of iterative methods. No matter what iterative scheme is used, ${\mathbb{E}}{\parallel{x^{t} - x^{\star}}\parallel}^{2}$ cannot decay asymptotically to zero faster than $1/t$. Roughly, this is because the rate at which error can decay is limited by the concentration properties of the gradient noise. This optimal asymptotic rate is achieved by Gradient Descent with a *diminishing stepsize* that decays as $1/t$ \[, Thm. 4.7\] (GDDS). However, GDDS can suffer from poor finite-time performance: iterates may require many steps to reach the asymptotic regime. In practice, algorithms are run for a finite horizon, and if the transient phase persists, the resulting error can remain large. Hence, asymptotic optimality does not imply finite-time efficiency.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Stochastic approximation", "weight": 1.0} -->

In the additive gradient noise setting, a variety of techniques have been proposed to improve transient performance. For the case of least squares regression, a dramatic speedup can be achieved via careful manipulation of the stepsize or by using acceleration. Kulunchakov and Mairal also show that any algorithm that converges linearly for smooth and strongly convex objectives in the noiseless setting can be converted into an algorithm that converges optimally (up to log factors) when additive noise is included.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Stochastic approximation", "weight": 1.0} -->

Ghadimi and Lan propose the AC-SA algorithm, which is a modification of Nesterov's Fast Gradient method that has near-optimal iteration complexity in the smooth and strongly convex setting. Besides characterizing the convergence of the average iterates, they also estimate the performance of the algorithm on a single problem instance. Building on this work, Cohen et al. propose the algorithm AGD+, a "lazy" (dual averaging) counterpart of AC-SA for the smooth and convex setting, along with its extension $\mu$AGD+ for the strongly convex setting. In the strongly convex setting, $\mu$AGD+ improves on the convergence bound of the AC-SA algorithm, but does not achieve the lower complexity bound. In particular, applying \[, Corollary B.5\] with $\gamma_{i} = {c\sqrt{m/L}}$ yields the bound

<!-- chunk {"id": "body-0022", "role": "body", "section": "Stochastic approximation", "weight": 1.0} -->

where we used the definition of strong convexity to bound the distance to optimality in terms of the optimality gap. The parameter $c \in {(0,\sqrt{L/m}\rbrack}$ can be chosen to trade off rate and sensitivity for this algorithm; however, we show that the resulting trade-off is strictly suboptimal (see Fig. 3. ‣ 5.1 Empirical validation ‣ 5 Numerical validation ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise")).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Stochastic approximation", "weight": 1.0} -->

None of the above algorithms achieve the optimal iteration complexity in the smooth strongly convex setting. One way to achieve the optimal complexity, however, is to exploit the rapid convergence of the transient phase by using a piecewise constant stepsize, effectively dividing the convergence into *epochs* or *stages*. This can be done on a predetermined schedule, or by using a statistical test to detect the phase transition which then triggers the parameter change. In Ghadimi and Lan's companion paper, for instance, they propose a multi-stage version of AC-SA that achieves the optimal expected rate of convergence (up to constants) in this setting. Aybat et al. build on Nesterov's Accelerated Stochastic Gradient method to construct the Multi-Stage Accelerated Stochastic Gradient method (M-ASG). This algorithm simultaneously achieves optimal iteration complexity (again, up to constants) in both deterministic and stochastic cases without knowledge of the noise parameters.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Stochastic approximation", "weight": 1.0} -->

The aforementioned multi-stage algorithms tune the single-stage algorithm stepsizes and the restart schedule to achieve desirable transient and asymptotic convergence, and they achieve the optimal complexity up to constants. In the present work work, we focus on analyzing and designing single-stage algorithms with fixed stepsizes that can be tuned via a single scalar parameter to explicitly trade-off convergence rate and sensitivity to noise. In other words, our algorithms can easily be adjusted to be made faster (and more sensitive to noise), or more robust to noise (and slower). When tuned to be as fast as possible, our algorithm designs recover algorithms that are known to converge with the optimal linear rate in the noise-free setting for the respective function classes (see Section 5). Our algorithm designs may be used to converge at a linear rate to a predetermined noise level, or the trade-off parameter may be adjusted over time to construct multi-stage variants^33^3While we do not propose a restart mechanism or time-varying parameter schedule in the present work, we illustrate such an approach in Section 5.3 through a hand-tuned schedule..

<!-- chunk {"id": "body-0025", "role": "body", "section": "Other noise models", "weight": 1.0} -->

While we restrict our attention to additive stochastic gradient noise in the present work, other inexact oracles have been studied in the literature. When the gradient noise is due to sampling a finite-sum objective function, viable strategies include incremental gradient or variance reduction methods such as SVRG, SAGA, and many others.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Other noise models", "weight": 1.0} -->

A prominent alternative model is to assume *deterministic*^44^4Also known as *worst-case* or *adversarial* noise. bounded noise, which may be additive or multiplicative. For instance, Devolder et al. propose an inexact deterministic first-order oracle and show that, under this oracle, acceleration necessarily results in an accumulation of gradient errors in the unconstrained smooth (not strongly convex) case. For this setting, the same authors propose the Intermediate Gradient Method, a family of first-order methods that can be tuned to trade off convergence rate and sensitivity to gradient errors. The same authors also extended this oracle to analyze inexact first-order methods in the strongly convex case; there is still a trade-off between rate and sensitivity, but errors no longer accumulate and can converge linearly to within a constant ball about the optimal solution. Multiplicative deterministic noise has been studied, for which the Robust Momentum (RM) was designed to trade off convergence rate and sensitivity. Stochastic Gradient Descent has also been analyzed under a hybrid additive and multiplicative deterministic oracle.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Methodology", "weight": 1.0} -->

We now provide an overview of our analysis and design framework and point to related techniques. Our method for bounding the convergence rate $r$ and sensitivity $\gamma$ for the class $F_{m,L}$ relies on solving a small linear matrix inequality (LMI). This idea builds upon several related works.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Methodology", "weight": 1.0} -->

The performance estimation problem (PEP) framework uses LMIs to directly search for a problem instance that achieves the worst-case performance. The PEP framework has been successfully applied to numerous algorithms, such as the proximal gradient method, operator splitting methods, and gradient descent using an exact line search with noisy search directions. Of particular interest, uses PEP to analyze iterative algorithms under various noise models when the objective is smooth and convex. This approach searches for a time-varying potential function whose existence certifies a performance bound. To obtain closed-form bounds, increasingly large LMIs are solved and their numerical solutions guide the construction of explicit expressions for the potential function parameters as functions of the iteration index. Alternatively, small PEPs can be formulated and solved to search for potential functions with fixed parameters as.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Methodology", "weight": 1.0} -->

Viewing algorithms as discrete-time dynamical systems, Integral Quadratic Constraints (IQCs) from control theory may be used to search for worst-case performance guarantees. This approach also leads to LMIs that characterize asymptotic performance, although the ensuing performance bounds are not tight in general.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Methodology", "weight": 1.0} -->

Finally, LMIs may be used to directly search for a Lyapunov function, which is a generalized notion of "energy" stored in the system. If a fraction of the energy dissipates at each iteration, this is akin to proving convergence at a specified rate. Similar to IQCs, Lyapunov functions provide asymptotic (albeit more interpretable) performance guarantees.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Methodology", "weight": 1.0} -->

In the present work, we adopt a Lyapunov approach most similar to, but we generalize it to include both convergence rate and sensitivity to noise. We also explain in Section 4.6 how the Lyapunov approach is related to IQCs.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Methodology", "weight": 1.0} -->

Given an LMI that establishes the performance (convergence rate or sensitivity to noise) of a given first-order method, the next step is to design algorithms that exploit this trade-off. Several approaches have been proposed: i) One can parameterize a family of candidate algorithms and search over parameters to effectively trade off convergence rate and sensitivity to noise. Such a problem is typically non-convex, so one must resort to exhaustive search or nonlinear numerical solvers that find local optima. ii) Using convex relaxations or other heuristics such as coordinate descent, the algorithm design problem can be solved approximately. While this approach may lead to conservative designs, it has the benefit of being automated, flexible, and amenable to efficient convex solvers. iii) In certain settings, the controller parameters can be eliminated from the LMI entirely, yielding bounds that hold for all algorithms. This approach has been used to show that the Triple Momentum (TM) method achieves the optimal worst-case rate over the class $F_{m,L}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Methodology", "weight": 1.0} -->

As in the first approach, we use the parameterized family of algorithms and search over the parameters. However, our approach to design is algebraic rather than numeric. We find analytic solutions to the non-convex semidefinite programs that arise when the algorithm parameters are treated as decision variables. This approach enables us to find explicit analytic expressions for our algorithm parameters. Nevertheless, we still make use of numerical approaches in order to validate our choice of parameterization and the efficacy of our designs, and to compare the performance of our designs to that of existing algorithms; see Section 5.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Problem setting and assumptions", "weight": 1.0} -->

To solve the optimization problem, we consider iterative first-order methods described by dynamics of the form

<!-- chunk {"id": "body-0035", "role": "body", "section": "Problem setting and assumptions", "weight": 1.0} -->

where $\xi^{t} \in {\mathbb{R}}^{n \times d}$ is the state of the algorithm, $y^{t} \in {\mathbb{R}}^{1 \times d}$ is where we evaluate the gradient, $u^{t} \in {\mathbb{R}}^{1 \times d}$ is the (exact) gradient, $w^{t} \in {\mathbb{R}}^{1 \times d}$ is the noise, and $t$ is the iteration. The state is the *memory* of the algorithm; its size reflects the number of past iterates that must be stored at each timestep. Given an algorithm $(A,B,C)$, objective function $f$, and initial condition $\xi^{0}$, a *trajectory* is any sequence ${(\xi^{t},u^{t},y^{t},w^{t})}_{t \geq 0}$ that satisfies.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Problem setting and assumptions", "weight": 1.0} -->

This general framework encompasses a wide variety of fixed-parameter first-order iterative methods; we discuss this in more detail in Section 2.2.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 1 (important notational convention)", "weight": 1.0} -->

A necessary condition for ) to represent a valid iterative algorithm is that there exists a fixed point corresponding to the stationary point of the objective function. In other words, there should exist $\xi^{\star} \in {\mathbb{R}}^{n \times d}$ and $y^{\star} \in {\mathbb{R}}^{1 \times d}$ satisfying $\xi^{\star} = {A\xi^{\star}}$ and $y^{\star} = {C\xi^{\star}}$. Taking this condition column-wise, we obtain the following.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Assumption 1 (algorithm form)", "weight": 1.0} -->

The matrix $A$ has an eigenvalue at $1$, and the associated eigenvector $v \in {\mathbb{R}}^{n}$ satisfies ${Cv} \neq 0$.^55^5In the language of control theory, the discrete-time system $(A,B,C)$ has an *observable integrator*.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Performance evaluation", "weight": 1.0} -->

Let $\mathcal{A} = {(A,B,C)}$ denote an algorithm as in and let $\mathcal{F} \in {\{ Q_{m,L},F_{m,L}\}}$ denote one of function classes defined in Section 1.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Convergence rate", "weight": 1.0} -->

The convergence rate describes the first phase of convergence observed in Fig. 1: exponential decrease of the error. In this regime, gradients are relatively large compared to the noise, so we set $w^{t} = 0$ for all $t \geq 0$. For any algorithm $\mathcal{A}$ with initial point $\xi^{0}$ and fixed point $\xi^{\star}$ and any function $f \in \mathcal{F}$, consider the trajectory $(\xi^{0},\xi^{1},\ldots)$ produced by $\mathcal{A}$. We define the linear convergence rate as

<!-- chunk {"id": "body-0041", "role": "body", "section": "Convergence rate", "weight": 1.0} -->

If the convergence rate $r = {\text{rate}{(\mathcal{A},\mathcal{F})}}$ is finite, then for all $\varepsilon > 0$, there exists $c > 0$ such that the trajectory satisfies ${\parallel{\xi^{t} - \xi^{\star}}\parallel} \leq {c{({r + \varepsilon})}^{t}{\parallel{\xi^{0} - \xi^{\star}}\parallel}}$ for all functions $f \in \mathcal{F}$, initial points $\xi^{0} \in {\mathbb{R}}^{n \times d}$, and iterations $t \geq 0$. This definition corresponds to the conventional notion of *linear convergence rate* used in the worst-case analysis of deterministic algorithms.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Convergence rate", "weight": 1.0} -->

If $r < 1$, the algorithm is said to be *globally linearly convergent*, and for all $\varepsilon > 0$, we have ${\parallel{y^{t} - y^{\star}}\parallel} = {O{({({r + \varepsilon})}^{t})}}$. Smaller $r$ corresponds to a faster (worst-case) convergence rate.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Sensitivity", "weight": 1.0} -->

The sensitivity characterizes the steady-state phase of convergence observed in Fig. 1. The steady-state error depends on the noise characteristics. We make the following assumptions on the noise sequence.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Assumption 2 (Noise sequence)", "weight": 1.0} -->

We assume that the noise sequence $w^{0},w^{1},\ldots$ has joint distribution ${\mathbb{P}} \in \mathcal{P}_{\sigma}$, with parameter $\sigma$ to be defined shortly.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Assumption 2 (Noise sequence)", "weight": 1.0} -->

*Independence across time.* For all ${\mathbb{P}} \in \mathcal{P}_{\sigma}$, if $w \sim {\mathbb{P}}$, then $w^{t}$ and $w^{\tau}$ are independent for all $t \neq \tau$. Then we may characterize the joint distribution ${\mathbb{P}} \in \mathcal{P}_{\sigma}$ by its associated marginal distributions $({\mathbb{P}}^{0},{\mathbb{P}}^{1},\ldots)$. We do not assume the ${\mathbb{P}}^{t}$ are necessarily identical.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Assumption 2 (Noise sequence)", "weight": 1.0} -->

. ‣ Sensitivity. ‣ 2.1 Performance evaluation ‣ 2 Problem setting and assumptions ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise") implies $\mathcal{P}_{\sigma}$ is completely characterized by the variance bound $\sigma^{2}$. For algorithm $\mathcal{A}$, function class $\mathcal{F}$, initial $\xi^{0}$, and family of distributions $\mathcal{P}_{\sigma}$, consider the stochastic iterate sequence $y^{0},y^{1},\ldots$ produced by $\mathcal{A}$. We define noise sensitivity as

<!-- chunk {"id": "body-0047", "role": "body", "section": "Assumption 2 (Noise sequence)", "weight": 1.0} -->

For all cases we consider, the normalized definition of sensitivity does not depend on $\sigma$. A smaller sensitivity is desirable because it means the algorithm achieves small error in spite of gradient perturbations. This definition is similar to that used in recent works exploring first-order algorithms using techniques from robust control.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Some previous works have defined sensitivity with respect to the squared-norm of the state ${\|{\xi^{t} - \xi^{\star}}\|}^{2}$. This quantity, however, depends on the state-space realization; performing the coordinate transformation ${(A,B,C)}\mapsto{({TAT^{- 1}},{TB},{CT^{- 1}})}$ for some invertible matrix $T$ does not change the sequence of inputs $u^{t}$ or outputs $y^{t}$, but it transforms the states: $\xi^{t}\mapsto{T\xi^{t}}$. Our definition of sensitivity is invariant under such transformations.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Algorithm parameterization", "weight": 1.0} -->

While our analysis results apply to the general model, for *design* we will further restrict the class of algorithms to those with state dimension $n = 2$. Algorithms of the form have $n^{2} + {2n}$ degrees of freedom in the matrices $A,B,C$, so the case $n = 2$ should require $8$ parameters. However, many of these parameters are redundant, and under. ‣ 2 Problem setting and assumptions ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise"), it turns out the case $n = 2$ is completely characterized by the three-parameter family.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Lemmas 2.1. ‣ 2.2 Algorithm parameterization ‣ 2 Problem setting and assumptions ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise") and 2.2 can also be proved using the notion of a *transfer function* (TF) \[, §2.7\], which is the linear map from the $z$-transform of $({u^{t} + w^{t}})$ to the $z$-transform of $y^{t}$. The TF of is ${G{(z)}} = {C{({{zI} - A})}^{- 1}B}$ and when two dynamical systems have the same TF, they are equivalent in the sense of Lemma 2.1. ‣ 2.2 Algorithm parameterization ‣ 2 Problem setting and assumptions ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise"). When $n = 2$, $G{(z)}$ is a rational function with one zero and two poles, one of which must be at $z = 1$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Remark 3", "weight": 1.0} -->

‣ 2 Problem setting and assumptions ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise"). This leaves three degrees of freedom (the second pole, the zero, and a constant gain). Similarly, it is easy to check that the TF for $\left( {\alpha{({1 - \beta})}},\beta,\frac{\beta}{1 - \beta} \right)$ is ${G{(z)}} = \frac{- \alpha}{z - 1}$, which is independent of $\beta$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Remark 3", "weight": 1.0} -->

In the next two sections, we focus on $Q_{m,L}$ and $F_{m,L}$. For each, we provide a tractable approach for bounding the convergence rate and sensitivity, and we design algorithms of the form that effectively trade off these performance metrics.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Performance bounds for $Q_{m,L}$", "weight": 1.0} -->

Quadratics have been treated extensively in recent works. For this class, the convergence rate has been characterized, and closed-form expressions for the sensitivity of GD, HB, and FG have been obtained. We now present versions of these results adapted to our algorithm class of interest.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Algorithm design for $Q_{m,L}$", "weight": 1.0} -->

For strongly convex quadratic functions, first-order methods can achieve exact convergence in $d$ iterations when there is no gradient noise, where $d$ is the dimension of the domain of $f$. One such example is the Conjugate Gradient (CG) method \[, Thm. 5.4\]. However, when the number of iterations $t$ satisfies $t < d$, exact convergence is not possible in general. Nesterov's lower bound \[, Thm. 2.1.13\]

<!-- chunk {"id": "body-0055", "role": "body", "section": "Algorithm design for $Q_{m,L}$", "weight": 1.0} -->

This lower bound holds for any first-order method such that $y^{t}$ is a linear combination of $y^{0}$ and (the exact) past gradients ${{\nabla f}{(y^{0})}},\ldots,{{\nabla f}{(y^{t - 1})}}$. This class includes not only CG but also methods with unbounded memory.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Algorithm design for $Q_{m,L}$", "weight": 1.0} -->

In the regime $t < d$, the CG method matches Nesterov's lower bound \[, Thm. 5.5\] and is therefore optimal in terms of worst-case rate. However, it is not clear how CG should be adjusted to be robust in the presence of additive gradient noise, since it has no tunable parameters.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Algorithm design for $Q_{m,L}$", "weight": 1.0} -->

The HB method, when tuned as in Table 1, also matches Nesterov's lower bound when applied to the function class $Q_{m,L}$ \[, §3.2.1\], but has a simpler implementation than CG: its updates are linear and its parameters are constant.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Algorithm design for $Q_{m,L}$", "weight": 1.0} -->

We adopted the three-parameter class $(\alpha,\beta,\eta)$ described in Section 2.2 as our search space for optimized algorithms because HB belongs to this class and achieves optimal performance on $Q_{m,L}$ when there is no noise. Substituting the three-parameter algorithm ) into Lemma 3.1. ‣ 3.1 Performance bounds for 𝑄_{𝑚,𝐿} ‣ 3 Strongly convex quadratic functions ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise"), we obtain the following result.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Smooth strongly convex functions", "weight": 1.0} -->

We now consider the class $F_{m,L}$ of strongly convex functions whose gradient is Lipschitz continuous. In contrast to the $Q_{m,L}$ case, the function class $F_{m,L}$ is not readily parameterizable. Therefore, we use a Lyapunov approach to certify performance bounds.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Lyapunov analysis", "weight": 1.0} -->

Our analysis is based on searching for a function that certifies either a particular convergence rate (assuming no noise) or level of sensitivity (assuming noise). When used in the context of certifying stability of dynamical systems, such a function is called a Lyapunov function. This function will depend on the state ${\mathbf{x}}^{t} \in X$ of a (to-be-defined) dynamical system. In Section 4.2, we will show how to construct this augmented system from the algorithm. Before doing so, we first show how to use such a function to certify performance.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Bounds on the rate of convergence", "weight": 1.0} -->

To bound the rate of convergence of an algorithm, we search for a function $V{({\mathbf{x}})}$ that decreases along trajectories and is lower bounded by the squared norm of the iterates.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Bounds on the sensitivity to noise", "weight": 1.0} -->

To bound the sensitivity of an algorithm to noise, we search for a function $V{({\mathbf{x}})}$ that satisfies the following conditions.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Lifted dynamics", "weight": 1.0} -->

To obtain performance bounds, we use a *lifting* approach that searches for certificates of performance that depend on a finite history of past algorithm iterates and function values. The main idea is to lift the state to a higher dimension so that we can search over a broader class of certificates to reduce the conservativeness of the bound. We denote the lifting dimension by $\ell \geq 0$, which dictates the dimension of the lifted state, and we use boldface symbols to denote quantities related to the lifted dynamics.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Lifted dynamics", "weight": 1.0} -->

Multiplying an augmented vector on the left by $Z$ removes the most recent iterate at time $t$, while multiplication by $Z_{+}$ removes the last iterate at time $t - \ell$. Using these augmented vectors, we then define the augmented state

<!-- chunk {"id": "body-0065", "role": "body", "section": "Lifted dynamics", "weight": 1.0} -->

which consists of the deviations of the state $\xi^{t}$ and past inputs $y^{t - 1},\ldots,y^{t - \ell}$, outputs $u^{t - 1},\ldots,u^{t - \ell}$, and function values $f^{t - 1},\ldots,f^{t - \ell}$ of the original system from equilibrium. The augmented dynamics, which follow from Eqs. 7 and, are

<!-- chunk {"id": "body-0066", "role": "body", "section": "Lifted dynamics", "weight": 1.0} -->

where $\mathsf{e}_{1} = {(1,0,\ldots,0)} \in {\mathbb{R}}^{\ell + 1}$. We can recover the iterates of the original system by projecting the augmented state and the input as

<!-- chunk {"id": "body-0067", "role": "body", "section": "Remark 4 (State reduction for noise-free case)", "weight": 1.0} -->

When there is no noise ($w^{t} = 0$), the component ${\mathbf{ξ}}^{t}$ of the augmented state has linearly dependent rows; knowledge of the past state $\xi^{t - \ell}$ and subsequent inputs $u^{t - \ell},\ldots,u^{t - 1}$ is enough to reconstruct the outputs $y^{t - \ell},\ldots,y^{t - 1}$. Thus, in this case, we could work with a smaller lifted state that does not include outputs. Such a reduction does not change the results of the analysis, but makes the semidefinite programs smaller and therefore (slightly) more computationally efficient.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Interpolation conditions", "weight": 1.0} -->

A useful characterization of the function class $F_{m,L}$ is given by the *interpolation conditions*. These are necessary and sufficient conditions on a sequence of points to be interpolable by a function in the class. We state the result from \[, Thm. 4\], rephrased to match our notation.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Performance bounds for $F_{m,L}$", "weight": 1.0} -->

We now use the interpolation conditions to search for a Lyapunov function that depends on the state ${\mathbf{x}}^{t}$ of the lifted system that satisfies the conditions in Section 4.1 to certify either the convergence rate or sensitivity. Motivated by the fact that the nonnegative inequalities in are quadratic in the inputs and outputs of the gradient and linear in the function values, we search for certificates $V:{{{\mathbb{R}}^{{({n + {2\ell}})} \times d} \times {\mathbb{R}}^{\ell}}\rightarrow{\mathbb{R}}}$ of the form

<!-- chunk {"id": "body-0070", "role": "body", "section": "Performance bounds for $F_{m,L}$", "weight": 1.0} -->

where ${\mathbf{x}} = {({\mathbf{ξ}},{\mathbf{f}})}$ is the state of the lifted system, and we search over parameters $P = P^{\mathsf{T}} \in {\mathbb{R}}^{{({n + {2\ell}})} \times {({n + {2\ell}})}}$ and $p \in {\mathbb{R}}^{\ell}$. Since $V$ is quadratic in the augmented state and linear in the augmented function values, we can efficiently search for such Lyapunov functions using the following linear matrix inequalities that leverage the characterization of smooth strongly convex functions in Lemma 4.4.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Remark 5", "weight": 1.0} -->

When the lifting dimension $\ell$ is zero, the lifted system is identical to the original system. In other words, $\xi^{t} = {\mathbf{ξ}}^{t}$. The system matrices also satisfy $A = \mathbf{A}$, and similarly for $B$. As $\ell$ is increased, the LMIs ) and ) have the potential to yield less conservative bounds on the rate and sensitivity, respectively.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Remark 5", "weight": 1.0} -->

Both bounds for the class $F_{m,L}$ in Theorem 4.5. ‣ 4.4 Performance bounds for 𝐹_{𝑚,𝐿} ‣ 4 Smooth strongly convex functions ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise") can be evaluated and optimized efficiently. The sizes of the LMIs depend only on $n$ and $\ell$, which are typically small.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Algorithm design for $F_{m,L}$", "weight": 1.0} -->

For the case with no noise, the Triple Momentum (TM) method attains the fastest-known worst-case convergence rate of $1 - \sqrt{\frac{m}{L}}$ over the function class $F_{m,L}$. Recent work by Drori and Taylor has confirmed that this rate is in fact optimal.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Algorithm design for $F_{m,L}$", "weight": 1.0} -->

We adopted the three-parameter class $(\alpha,\beta,\eta)$ described in Section 2.2 as our search space for optimized algorithms, because it includes TM as a special case, and FG, which is a popular choice for this function class. We begin with the GD baseline.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Remark 6", "weight": 1.0} -->

When $r$ is set to its minimum value of $1 - \sqrt{\frac{m}{L}}$, the Robust Accelerated Method in Theorem 4.7. ‣ 4.5 Algorithm design for 𝐹_{𝑚,𝐿} ‣ 4 Smooth strongly convex functions ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise") reduces to the Triple Momentum Method (see Table 1).

<!-- chunk {"id": "body-0076", "role": "body", "section": "Comparison with IQCs from robust control", "weight": 1.0} -->

We now compare our analysis in Theorem 4.5. ‣ 4.4 Performance bounds for 𝐹_{𝑚,𝐿} ‣ 4 Smooth strongly convex functions ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise") for computing the worst-case convergence rate over $F_{m,L}$ with the use of integral quadratic constraints (IQCs). Specifically, we apply the upper bound on convergence rate from the LMI in \[, Eq. 3.8\] with the weighted off-by-one IQC in \[, Lemma 10\]. The result is summarized below.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Numerical validation", "weight": 1.0} -->

We perform numerical experiments to verify that our designs (i) effectively trade off convergence rate and noise sensitivity, (ii) use an adequate number of parameters (they are neither under- nor over-parameterized), and (iii) outperform popular iterative schemes when applied to a worst-case test function. Our code is available at

<!-- chunk {"id": "body-0078", "role": "body", "section": "Empirical validation", "weight": 1.0} -->

To empirically validate our designs from Theorems 3.4. ‣ 3.2 Algorithm design for 𝑄_{𝑚,𝐿} ‣ 3 Strongly convex quadratic functions ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise") and 4.7. ‣ 4.5 Algorithm design for 𝐹_{𝑚,𝐿} ‣ 4 Smooth strongly convex functions ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise"), we performed a brute-force analysis of algorithms $(\alpha,\beta,\eta)$ and made a scatter plot of sensitivity vs. convergence rate. The following result facilitates sampling by providing bounds on admissible $(\alpha,\beta,\eta)$.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Strongly convex quadratics ($Q_{m,L}$)", "weight": 1.0} -->

We show our brute-force search for the class $Q_{m,L}$ in Fig. 2. ‣ 5.1 Empirical validation ‣ 5 Numerical validation ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise") for $Q_{1,10}$ and $Q_{1,100}$. For this figure, we used the sampling approach based on Lemma 5.1. ‣ 5.1 Empirical validation ‣ 5 Numerical validation ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise") with $500 \times 201 \times 200$ samples for $\alpha$, $\alpha\eta$, and $\beta$, respectively.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Strongly convex quadratics ($Q_{m,L}$)", "weight": 1.0} -->

In Fig. 2. ‣ 5.1 Empirical validation ‣ 5 Numerical validation ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise"), each algorithm $(\alpha,\beta,\eta)$ corresponds to a single gray dot The RHB curve shows each possible tuning as we vary the parameter $r$. We observe that RHB perfectly traces out the boundary of the point cloud, which represents the Pareto-optimal algorithms. In other words, for a fixed convergence rate $r$, RHB with parameter $r$ achieves this rate and is also as robust as possible to additive gradient noise.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Strongly convex quadratics ($Q_{m,L}$)", "weight": 1.0} -->

Fig. 2. ‣ 5.1 Empirical validation ‣ 5 Numerical validation ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise") reveals that GD with $0 < \alpha < \frac{2}{L + m}$ is outperformed by RHB on the function class $Q_{m,L}$. We also plot the performance of GD for $\alpha > \frac{2}{L + m}$, which is even worse as this leads to slower convergence *and* increased sensitivity. Fig. 2. ‣ 5.1 Empirical validation ‣ 5 Numerical validation ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise") also reveals that FG is strictly suboptimal compared to RHB based on the analysis in Theorem 4.5. ‣ 4.4 Performance bounds for 𝐹_{𝑚,𝐿} ‣ 4 Smooth strongly convex functions ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise"), although the optimality gap appears to shrink as $L/m$ gets larger.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Smooth strongly convex functions ($F_{m,L}$)", "weight": 1.0} -->

We show our brute-force search for the class $F_{m,L}$ in Fig. 3. ‣ 5.1 Empirical validation ‣ 5 Numerical validation ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise") for $F_{1,10}$ and $F_{1,100}$. For this figure, we used the same sampling approach as in Fig. 2. ‣ 5.1 Empirical validation ‣ 5 Numerical validation ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise"), with $200 \times 51 \times 50$ samples. When applying Theorem 4.5. ‣ 4.4 Performance bounds for 𝐹_{𝑚,𝐿} ‣ 4 Smooth strongly convex functions ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise"), we used a lifting dimension $\ell = 1$ to compute the rate and $\ell = 6$ to compute the sensitivity. For more details on these choices, see Section 5.4.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Smooth strongly convex functions ($F_{m,L}$)", "weight": 1.0} -->

The Robust Momentum (RM) method interpolates between TM and GD with $\alpha = \frac{1}{L}$ and does trade off convergence rate and sensitivity, but based on our analysis in Theorem 4.5. ‣ 4.4 Performance bounds for 𝐹_{𝑚,𝐿} ‣ 4 Smooth strongly convex functions ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise") it is strictly outperformed by our proposed RAM. The gap in performance between RM and RAM appears to shrink as $L/m$ gets larger.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Smooth strongly convex functions ($F_{m,L}$)", "weight": 1.0} -->

While Fig. 3. ‣ 5.1 Empirical validation ‣ 5 Numerical validation ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise") indicates that RAM effectively trades off rate and robustness, it is strictly suboptimal^77^7Suboptimality is difficult to verify for the function class $F_{m,L}$ since the results depend on the lifting dimension $\ell$. However, we performed extensive numerical computations to ensure that $\ell$ is sufficiently large; see Section 5.4.. Suboptimality becomes most apparent when $L/m$ is small and $r$ is close to $1$. For example, consider RAM with the parameter choice $r = 0.9$, $m = 1$, and $L = 2$, which corresponds to ${(\alpha,\beta,\eta)} = {(0.019,0.66,{- 3.631579})}$. Solving the LMIs in Theorem 4.5.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Smooth strongly convex functions ($F_{m,L}$)", "weight": 1.0} -->

‣ 4.4 Performance bounds for 𝐹_{𝑚,𝐿} ‣ 4 Smooth strongly convex functions ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise") yields the rate $0.9000$ and sensitivity $0.22057$. However, if we change $\eta$ and use the tuning ${(\alpha,\beta,\eta)} = {(0.019,0.66,0.00)}$ instead, we obtain the same rate with the strictly smaller sensitivity $0.1676$. Larger optimality gaps can be found by making $L/m$ even closer to $1$, although such cases are not practical.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Remark 7", "weight": 1.0} -->

The left panel of Fig. 3. ‣ 5.1 Empirical validation ‣ 5 Numerical validation ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise") (${L/m} = 10$) shows a denser point cloud than the right panel (${L/m} = 100$), despite using the same number of sample points. This occurs because the right panel spans a larger range of $\gamma$ values (the vertical axis is truncated), indicating that desirable algorithm tunings become harder to find by random sampling as $L/m$ increases.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Justifying the three-parameter algorithm family", "weight": 1.0} -->

A natural question to ask is whether something as general as our three-parameter family is needed to achieve the performance of our designs. Several recent works have restricted their attention to optimizing algorithms with two parameters $(\alpha,\beta)$ in either Nesterov's FG or Polyak's HB form. From our results in Sections 3.2 and 5.1, the HB form is sufficient for the class $Q_{m,L}$. However, neither the HB or the FG forms are sufficient for $F_{m,L}$. While some algorithms in these restricted classes achieve acceleration, they are incapable of obtaining the same trade-off between convergence rate and sensitivity as a properly-tuned three-parameter method, as illustrated in Fig. 4 (left panel). Indeed, even when there is no noise, no algorithm in the FG or HB families achieves the optimal convergence rate for the function class $F_{m,L}$, which is attained by Van Scoy et al.'s Triple Momentum (TM) method.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Justifying the three-parameter algorithm family", "weight": 1.0} -->

Alternatively, we could ask whether using more than three parameters could lead to further improvement. As explained in Section 2.2, any algorithm with $n = 2$ states can be represented by three parameters. In general, we would need ${2n} - 1$ parameters to represent an algorithm with $n$ states. In principle, our methodology of Section 1.3 can still be applied, but the associated semidefinite programs become substantially more difficult to solve and we were unable to find better designs.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Justifying the three-parameter algorithm family", "weight": 1.0} -->

An alternative approach, presented, used a convex synthesis procedure and bilinear matrix inequalities to numerically construct algorithms that trade off convergence rate and sensitivity. As shown in Fig. 4 (right panel), these synthesized algorithms do not outperform RAM, despite using up to $n = 6$ states.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Simulation of a worst-case test function", "weight": 1.0} -->

We simulated various algorithms on Nesterov's lower-bound function, which is a quadratic with a tridiagonal Hessian \[, §2.1.4\]. We used $d = 100$ with $m = 1$ and $L = 10$ and initialized each algorithm at zero. The results are reported in Fig. 5. We tested both a *low noise* ($\sigma = 10^{- 5}$, left column) and a *higher noise* ($\sigma = 10^{- 2}$, right column) regime. We recorded the mean and standard deviation of the error across $100$ trials for each algorithm (the trials differ only in the noise realization).

<!-- chunk {"id": "body-0091", "role": "body", "section": "Simulation of a worst-case test function", "weight": 1.0} -->

Fig. 5 shows that RHB from Theorem 3.4. ‣ 3.2 Algorithm design for 𝑄_{𝑚,𝐿} ‣ 3 Strongly convex quadratic functions ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise") trades off convergence rate (the initial decreasing slope) with sensitivity to noise (the steady-state value), and compares favorably to other methods. The other methods we tested (first row of Fig. 5) are generally suboptimal compared to RHB, in the sense that there is some choice of tuning parameter $r$ such that RHB is both faster and has smaller steady-state error.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Simulation of a worst-case test function", "weight": 1.0} -->

In addition to GD and FG, we tested Nonlinear Conjugate Gradient (NLCG) with the Polak-Ribière (PR) update scheme.^88^8We also tested other popular NLCG update schemes such as: Fletcher--Reeves, Hestenes--Stiefel, and Dai--Yuan; all produced similar trajectories to PR. NLCG performs similarly to RHB with the most aggressive tuning, which is equivalent to the Heavy Ball method. We also tested the popular quasi-Newton methods Broyden--Fletcher--Goldfarb--Shanno (BFGS) and Symmetric Rank-One (SR1), which performed strictly worse than RHB.^99^9Both NLCG and BFGS use line search; given a current point $y \in {\mathbb{R}}^{d}$ and search direction $s \in {\mathbb{R}}^{d}$, they search for $\alpha \in {\mathbb{R}}$ that minimizes $f{({y + {\alphas}})}$.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Simulation of a worst-case test function", "weight": 1.0} -->

In practice, *inexact* line searches are performed at each timestep with a stopping criterion such as the Wolfe conditions. To show these algorithms in the most charitable light, we used exact line searches but substituted the noisy gradient oracle. Specifically, with ${f{(y)}} = {\frac{1}{2}{({y - y^{\star}})}^{\mathsf{T}}Q{({y - y^{\star}})}}$, the optimal stepsize is $\alpha^{\star} = {- {{({s^{\mathsf{T}}{\nabla f}{(y)}})}/{({s^{\mathsf{T}}Qs})}}}$. We used this formula, but replaced ${\nabla f}{(y)}$ by the noisy ${{\nabla f}{(y)}} + w$ (exact knowledge of $Q$ but not $y^{\star}$).

<!-- chunk {"id": "body-0094", "role": "body", "section": "Simulation of a worst-case test function", "weight": 1.0} -->

In the second row of Fig. 5, we use the same settings as the first row, except iterations are plotted on a log scale as in Fig. 1. We also show a hand-tuned version of RHB with piecewise constant $r$.^1010^10We use a hand-tuned schedule to illustrate our results; more systematic scheduling methods have been proposed, such as the restart+slowdown method. Whenever $r$ is changed, we re-initialize the algorithm via $x^{t - 1} = x^{t}$. In the transient phase, the hand-tuned RHB matches Nesterov's lower bound. In the stationary phase, it matches the asymptotic lower bound (slope of $- {1/2}$) described in Section 1.2.^1111^11The lower bound is $1/t$ for the squared error, hence $1/\sqrt{t}$ for the error, which appears as a line of slope $- {1/2}$ on the log-log scale of Fig. 5, bottom row.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Computational considerations", "weight": 1.0} -->

We used Julia v.1.12.1 for all computation, and our code is available at Applying Theorem 4.5. ‣ 4.4 Performance bounds for 𝐹_{𝑚,𝐿} ‣ 4 Smooth strongly convex functions ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise") required picking $\ell$. Using larger $\ell$ could reduce conservatism, but at the cost of larger LMIs. To this end, we performed a pilot study using the arbitrary-precision solver Hypatia. In Table 2, we apply Theorem 4.5. ‣ 4.4 Performance bounds for 𝐹_{𝑚,𝐿} ‣ 4 Smooth strongly convex functions ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise") and report the performance of FG with standard tuning (see Table 1), with 30 significant digits^1212^12For each case, we computed optimal primal and dual solutions, verified that each was strictly feasible, and ensured the duality gap was less than $10^{- 30}$.. The rate did not improve beyond $\ell = 1$ but the sensitivity bound continued to improve.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Computational considerations", "weight": 1.0} -->

Rate upper bound
Sensitivity upper bound

<!-- chunk {"id": "body-0097", "role": "body", "section": "Computational considerations", "weight": 1.0} -->

To generate Fig. 3. ‣ 5.1 Empirical validation ‣ 5 Numerical validation ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise"), we solved the LMIs from Theorem 4.5. ‣ 4.4 Performance bounds for 𝐹_{𝑚,𝐿} ‣ 4 Smooth strongly convex functions ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise") using JuMP v.1.29.2 with the Mosek solver v.11.0.1 and default settings. We used $\ell = 1$ for the rate, with a bisection search tolerance of $10^{- 6}$, and $\ell = 6$ for the sensitivity. With these choices, finding the rate and sensitivity of a given three-parameter algorithm with 5 significant digits of precision each took about 100 ms on a conventional laptop.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Concluding remarks", "weight": 1.0} -->

For $Q_{m,L}$ and $F_{m,L}$, we provided (i) efficient methods for computing the convergence rate and noise sensitivity for a broad class of first-order methods, and (ii) first-order algorithms designs, each with a single tunable parameter that directly trades off convergence rate and sensitivity to additive gradient noise.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Concluding remarks", "weight": 1.0} -->

An interesting future direction is exploring adaptive versions of these algorithms, where the parameter $r$ is varied over time. We showed in Fig. 5 that a hand-tuned piecewise constant version of RHB can match both Nesterov's lower bound and the gradient lower bound, so more sophisticated adaptive schemes such as those described in Section 1.2 might also work. One could also adjust parameters continually, but proving the convergence of adaptive algorithms is generally more challenging. For example, the well-known ADMM algorithm is often tuned adaptively to improve transient performance, even when convergence guarantees only hold for fixed parameters \[, §3.4.1.\]. Nevertheless, LMI-based approaches have been successfully used to prove convergence of algorithms with time-varying parameters.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Concluding remarks", "weight": 1.0} -->

Another interesting open question is whether our analysis is tight. For $F_{m,L}$ (Theorem 4.5. ‣ 4.4 Performance bounds for 𝐹_{𝑚,𝐿} ‣ 4 Smooth strongly convex functions ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise")), our bounds depend on $\ell$. It is unknown (i) how large $\ell$ needs to be in order to obtain the tightest possible bounds on convergence rate and sensitivity, and (ii) whether Theorem 4.5. ‣ 4.4 Performance bounds for 𝐹_{𝑚,𝐿} ‣ 4 Smooth strongly convex functions ‣ The Speed–Robustness Trade-Off for First-Order Methods with Additive Gradient Noise") always produces tight bounds as $\ell\rightarrow\infty$.
