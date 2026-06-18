<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Control Interpretations for First-Order Optimization Methods

Topics include Optimization, Control, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

First-order iterative optimization methods play a fundamental role in large scale optimization and machine learning. This paper presents control interpretations for such optimization methods. First, we give loop-shaping interpretations for several existing optimization methods and show that they are composed of basic control elements such as PID and lag compensators. Next, we apply the small gain theorem to draw a connection between the convergence rate analysis of optimization methods and the input-output gain computations of certain complementary sensitivity functions. These connections suggest that standard classical control synthesis tools may be brought to bear on the design of optimization algorithms.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

First-order iterative optimization methods have been widely applied in data science and machine learning. These methods only require access to first-order derivative information, and iterate on the data until satisfactory convergence is achieved. For example, the gradient method is

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Such simple methods are often favored over higher order methods such as Newton's method when the dimension of the underlying space is large and computing Hessians is prohibitively expensive.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

There has been significant recent interest in finding ways to accelerate the convergence of the gradient method while maintaining low iteration costs. For example, the *Heavy-ball* method includes an additional momentum term

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This slight modification can yield a dramatic improvement in worst-case convergence rate if $f$ is quadratic. A similar acceleration scheme, *Nesterov's accelerated method*, can improve the convergence rate for strongly convex $f$ with smooth gradients. These convergence results are derived on a case-by-case basis, and the intuition behind the acceleration is still not fully understood.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent efforts have adopted a dynamical system (or differential equation) perspective in analyzing acceleration for convex objectives, though a more general understanding of acceleration is still lacking (non-convex objectives, inexact computations, etc). This paper aims to bring new insights on how to accelerate first-order optimization methods for objective functions which are not convex in general.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We pose the iterative optimization paradigm as an output regulation problem, which lends itself to a loop-shaping interpretation. In particular, we show that several popular optimization algorithms may be viewed as controllers which are composed of basic PID or lag compensation elements. We also demonstrate that existing parameter tuning guidelines for these optimization methods are consistent with the loop-shaping design guidelines in control theory.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Using the small gain theorem, we draw a connection between the convergence rate analysis of optimization methods (under sector-bounded assumptions) and the input-output gain computation for a particular complimentary sensitivity function. It follows that the *design* of optimization algorithms for sector-bounded functions can be interpreted as $\mathcal{H}_{\infty}$ state feedback synthesis. This explains why acceleration typically requires stronger function assumptions (not necessarily convexity) beyond just sector-bounded gradients.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

A related line of research has emerged in the distributed optimization literature. In, a continuous-time differential equation was used to describe the dynamics of distributed optimization, leading to a natural iterative algorithm which may be interpreted as a PI controller. In, event-triggered control methods were tailored for distributed optimization over networks. In contrast with the work on distributed optimization, the present work is concerned with control-theoretic properties and interpretations of a big class of first-order optimization methods.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

A second related line of research is the unified integral quadratic constraint framework, which provides a numerical tool based on semidefinite programming for use in analyzing optimization algorithms. In contrast with this work, the present work uses a small gain approach with a simple interpretation that interfaces with existing results on complementary sensitivity integrals.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The paper is organized as follows. Section 2 explains notation and problem formulation, Section 3 describes our loop-shaping interpretation for first-order methods, and Section 4 presents our main results involving the small gain theorem and connections to complementary sensitivity.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Spaces and operators", "weight": 1.0} -->

In addition, $K$ is said to be bounded if it has a finite gain. Notice this gain is induced by $\ell_{2}$ signals while the operator $K$ itself is defined on $\ell_{2e}$. This definition makes sense since any bounded operator on $\ell_{2}$ to itself has a natural causal extension to the operator from $\ell_{2e}$ to $\ell_{2e}$. Clearly, every bounded operator must map zero inputs to zero outputs.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Various objective functions in optimization", "weight": 1.0} -->

Consider the unconstrained optimization problem

<!-- chunk {"id": "body-0015", "role": "body", "section": "Various objective functions in optimization", "weight": 1.0} -->

where it is assumed that there exists a unique $x^{\star} \in {\mathbb{R}}^{p}$ satisfying ${{\nabla f}{(x^{\star})}} = 0$. How to solve and find $x^{\star}$ heavily depends on the assumptions about $f$. A simple assumption is that $f$ is quadratic. Two other common assumptions are $L$-*smoothness* and *strong convexity*. A continuously differentiable function $f:{{\mathbb{R}}^{p}\rightarrow{\mathbb{R}}}$ is $L$-smooth if the following inequality holds for all ${x,y} \in {\mathbb{R}}^{p}$

<!-- chunk {"id": "body-0016", "role": "body", "section": "Various objective functions in optimization", "weight": 1.0} -->

We define $\mathcal{L}{(L)}$ to be the set of $L$-smooth functions. The continuously differentiable function $f$ is $m$-strongly convex if the following inequality holds for all ${x,y} \in {\mathbb{R}}^{p}$

<!-- chunk {"id": "body-0017", "role": "body", "section": "Various objective functions in optimization", "weight": 1.0} -->

Note that we recover ordinary convexity in if $m = 0$. We define $\mathcal{F}{(m,L)}$ to be the set of functions that are both $L$-smooth and $m$-strongly convex. The class $\mathcal{F}$ covers a large family of objective functions in machine learning, including $\ell_{2}$-regularized logistic regression, smooth support vector machines, etc. Clearly, ${\mathcal{F}{(m,L)}} \subset {\mathcal{L}{(L)}}$. For all $f \in {\mathcal{F}{(m,L)}}$, the following inequality holds for all $x \in {\mathbb{R}}^{p}$

<!-- chunk {"id": "body-0018", "role": "body", "section": "Various objective functions in optimization", "weight": 1.0} -->

where $I_{p}$ denotes the $p \times p$ identity matrix \[10, Lemma 6\]. On the other hand, a function satisfying the above inequality may not belong to $\mathcal{F}{(m,L)}$, and may not even be convex. The set of continuously differentiable functions satisfying is denoted as $\mathcal{S}{(m,L)}$. This class of functions has sector-bounded gradients, and includes $\mathcal{F}{(m,L)}$ as a subset.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Review of first-order optimization methods", "weight": 1.0} -->

A classical way to solve is the gradient descent method, which uses the iteration to gradually converge to $x^{\star}$. The intuition behind gradient descent method is as follows. At each step $k$, we find a quadratic approximation of $f$ about $x^{k}$, which hopefully captures the local structure of $f$, and we solve the quadratic minimization problem

<!-- chunk {"id": "body-0020", "role": "body", "section": "Review of first-order optimization methods", "weight": 1.0} -->

When $f \in {\mathcal{S}{(m,L)}}$, if $\alpha$ is chosen well, then there exists a constant $\rho \in {}$ and a constant $c \geq 1$ such that

<!-- chunk {"id": "body-0021", "role": "body", "section": "Review of first-order optimization methods", "weight": 1.0} -->

Thus the iterates $\{ x^{k}\}$ converge exponentially to $x^{\star}$. By convention, this is known as *linear convergence* in the optimization literature. For example, we can choose $\alpha = \frac{2}{L + m}$ and obtain $\rho = \frac{L - m}{L + m}$ and $c = 1$. Another popular choice is $\alpha = \frac{1}{L}$, which leads to $\rho = {1 - \frac{m}{L}}$ and $c = 1$. These results are formally documented in \[10, Section 4.4\]. It is emphasized that the proofs of these results only require.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Review of first-order optimization methods", "weight": 1.0} -->

where $\alpha = \frac{1}{L}$ and $\beta = \frac{\sqrt{L} - \sqrt{m}}{\sqrt{L} + \sqrt{m}}$. When $L/m$ is large, Nesterov's accelerated method guarantees a much faster convergence rate compared to the gradient descent method. This fact was stated in \[13, Theorem 2.2.3\].

<!-- chunk {"id": "body-0023", "role": "body", "section": "Review of first-order optimization methods", "weight": 1.0} -->

When $f$ is a quadratic function, one can accelerate the gradient descent method by incorporating a momentum term into the iteration, such as the Heavy-ball method. Although the Heavy-ball method works extremely well for quadratic objective functions, it can fail to converge for other functions in $\mathcal{F}{(m,L)}$; see \[10, Section 4.6\].

<!-- chunk {"id": "body-0024", "role": "body", "section": "Review of first-order optimization methods", "weight": 1.0} -->

The intuitions behind Nesterov's accelerated method and the Heavy-ball method are still not fully understood. Hence, there is no intuitive way to modify these methods to accelerate the convergence when optimizing more general functions, i.e. $f \in {\mathcal{S}{(m,L)}}$ or $f \in {{\mathcal{S}{(m,L)}} \cap {\mathcal{L}{(L)}}}$. Gaining intuition for these methods can be beneficial for designing accelerated schemes for more general classes of objective functions.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Review of first-order optimization methods", "weight": 1.0} -->

Finally, it is worth mentioning that every optimization method mentioned in this section can be cast as the feedback interconnection $F_{u}{(P,K)}$ as shown in Fig 1. Here, $P{: =}{\nabla f}$ is a static nonlinearity and $K$ is a linear time-invariant (LTI) system (the algorithm).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Review of first-order optimization methods", "weight": 1.0} -->

Feedback representations for optimization methods are discussed in \[10, Section 2\]. In, $P$ is a static nonlinear operator that maps $u$ to $v = {Pu}$ as $v^{k} = {{\nabla f}{(u^{k})}}$. However, this is not a bounded operator since it does not map zero inputs to zero outputs. For the convenience of our discussion, we will choose $P$ to be the operator which maps $u$ to $v = {Pu}$ as $v^{k} = {{\nabla f}{({u^{k} + x^{\star}})}}$ where $x^{\star}$ is the unique point satisfying ${{\nabla f}{(x^{\star})}} = 0$. Then this choice of $P$ leads to a bounded operator. One can perform a state shifting argument to the feedback representations in and cast all the mentioned optimization methods as

<!-- chunk {"id": "body-0027", "role": "body", "section": "Review of first-order optimization methods", "weight": 1.0} -->

The optimization method converges to the optimum $x^{\star}$ at a rate $\rho$ if and only if the model drives $\xi^{k}$ to $0$ from any initial conditions at the same rate $\rho$. Using similar arguments, Nesterov's accelerated method and the Heavy-ball method can be written as. In these two cases, the associated state matrices for $K$ are the same as (2.5) and (2.7), although the states have been shifted by $x^{\star}$. When $f \in {\mathcal{S}{(m,L)}}$, the inequality imposes a sector bound on the input/output pair of $P$. Let $v = {Pu}$. Then the following inequality holds for all $k$

<!-- chunk {"id": "body-0028", "role": "body", "section": "Review of first-order optimization methods", "weight": 1.0} -->

The above inequality is important for further analysis of optimization methods.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Input-output stability and small gain theorem", "weight": 1.0} -->

The key analysis tool in this paper is the small gain theorem, which is now briefly reviewed. Suppose two causal operators $P:{\ell_{2e}\rightarrow\ell_{2e}}$ and $K:{\ell_{2e}\rightarrow\ell_{2e}}$ both map zero input to zero output. Let $\lbrack P,K\rbrack$ denote the feedback interconnection of $P$ and $K$ illustrated in Fig.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Input-output stability and small gain theorem", "weight": 1.0} -->

The interconnection $\lbrack P,K\rbrack$ is said to be *well-posed* if the map ${(u,v)}\mapsto{(r,e)}$ defined by has a causal inverse on $\ell_{2e}$. It is (input-output) *stable* if it is well-posed and this inverse causal map from $(r,e)$ to $(u,v)$ is bounded. Clearly, ${u,v} \in \ell_{2}$ for all ${r,e} \in \ell_{2}$ if $\lbrack P,\Delta\rbrack$ is stable. Well-posedness holds only if the solutions to have no finite escape time. The small gain theorem states the following.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Loop-shaping interpretations for optimization methods", "weight": 1.0} -->

This section presents basic control interpretations for the gradient descent method, Nesterov's accelerated method, and the Heavy-ball method with the hope of shedding light on the general principles underlying the design of first-order methods. The goal of the optimization method is to find $x^{\star}$ satisfying ${{\nabla f}{(x^{\star})}} = 0$. Hence the optimization method may be viewed as a controller that regulates the plant "$\nabla f$" to zero. When viewing $\nabla f$ as the plant one wants to control, the unconstrained optimization problem is an output regulation problem, and the LTI part $K$ in the first-order optimization method can be viewed as a controller. The key issue for this output regulation problem is that the equilibrium point $x^{\star}$ is unknown.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Loop-shaping interpretations for optimization methods", "weight": 1.0} -->

Transfer functions for the controller $K$ are listed in Table 1. We use the symbol $\otimes$ to denote the Kronecker product. These products appear because the controllers corresponding to our algorithms of interest are repetitions of a single-input-single-output (SISO) system.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Loop-shaping interpretations for optimization methods", "weight": 1.0} -->

For the gradient descent method, $K$ is a pure integrator. Hence, the gradient descent regulates the nonlinear plant $P$ via pure integral control. Integral action is necessary since the algorithm must converge to $x^{\star}$, which amounts to having zero steady-state error when $K$ tracks a step input.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Loop-shaping interpretations for optimization methods", "weight": 1.0} -->

The Heavy-ball method differs from gradient descent in the inclusion of an additional momentum term. This momentum term may be viewed as a lag compensator.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Loop-shaping interpretations for optimization methods", "weight": 1.0} -->

The first term provides integral action to ensure zero steady-state error as with the gradient method, while the second term is a discrete-time lag compensator. The lag compensation has the net effect of 1) boosting low-frequency response by a factor of roughly $\frac{1}{1 - \beta}$, which improves the tracking speed of the controller and hence the convergence of the algorithm and 2) attenuating high-frequency response by a factor of roughly $\frac{1}{1 + \beta}$. It intuitively makes sense that the Heavy-ball method can accelerate convergence for quadratic objectives, since the plant $P$ becomes a linear operator in this case. However, the lag compensator increases the slope of the loop gain near the crossover frequency, which may have a detrimental effect on the robustness of the closed loop. This qualitative observation is confirmed by the fact that the Heavy-ball method may fail to converge at all if the objective function is relaxed to include more general strongly convex functions.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Loop-shaping interpretations for optimization methods", "weight": 1.0} -->

Unlike the Heavy-ball method, Nesterov's accelerated method performs well when applied to strongly-convex objective functions. A control interpretation is that Nesterov's accelerated method includes derivative control to decrease the slope of the loop gain near the crossover frequency, which significantly improves the robustness of the algorithm for certain classes of nonlinearities. To see the derivative controller in Nesterov's accelerated method, rewrite as

<!-- chunk {"id": "body-0037", "role": "body", "section": "Loop-shaping interpretations for optimization methods", "weight": 1.0} -->

The last term is a difference of the plant output $\nabla f$, and can be viewed as a derivative control.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Loop-shaping interpretations for optimization methods", "weight": 1.0} -->

Nesterov's method may also be interpreted as lag compensation together with integral action, as in the Heavy-ball case. The corresponding controller is

<!-- chunk {"id": "body-0039", "role": "body", "section": "Loop-shaping interpretations for optimization methods", "weight": 1.0} -->

which has a zero at $z = \frac{\beta}{1 + \beta}$, and this helps increase the slope of the Bode plot near the crossover frequency. The control interpretations for different optimization methods are summarized in Table 2.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Loop-shaping interpretations for optimization methods", "weight": 1.0} -->

We now demonstrate that the design of state-of-the-art optimization methods is actually consistent with general loop-shaping principles from control theory. The loop-shaping principle states that the low-frequency loop gain should be sufficiently large to ensure good tracking performance while the high-frequency loop gain should be small enough for the purpose of noise rejection. In addition, the slope of the loop gain near the crossover frequency should be flat (typically around $- 20$ dB/decade) to assure a proper phase margin and good robustness. A thorough discussion on loop-shaping can be found in standard references.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Loop-shaping interpretations for optimization methods", "weight": 1.0} -->

Given a function $f \in {\mathcal{F}{(m,L)}}$, the standard gradient descent stepsize is $\alpha = \frac{1}{L}$, and the standard parameter choice for Nesterov's accelerated method is $\alpha = \frac{1}{L}$ and $\beta = \frac{\sqrt{L} - \sqrt{m}}{\sqrt{L} + \sqrt{m}}$. Other parameter choices, when $f$ is quadratic for example, are documented in \[10, Proposition 1\]. Fig. 3 shows the Bode plots of the resultant controllers $K$ (only the SISO part) for all these parameter choices under the assumption that $m = 0.01$ and $L = 1$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Loop-shaping interpretations for optimization methods", "weight": 1.0} -->

The Bode plots are consistent with the properties of these optimization methods when a loop-shaping intuition is adopted. First, the gradient descent method with the standard stepsize $\alpha = \frac{1}{L}$ is known to be slower than other first-order methods when $f$ is quadratic. This is reflected in the Bode plot, which shows that the gradient method has a relatively low gain particularly in the low-frequency region. Using the optimal tuning of $\alpha = \frac{2}{L + m}$ improves the gain slightly.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Loop-shaping interpretations for optimization methods", "weight": 1.0} -->

Second, the optimal quadratic tuning for all three methods leads to controllers whose crossover frequencies are roughly at $0.5$ Hz. Intuitively, such tuning places excessive weight on tracking performance and is very fragile to noise at the output of the plant $P$. This is consistent with the known robustness properties of these methods as well. For example, the gradient method with $\alpha = \frac{1}{L}$ is known to be very robust to the noise in the gradient computation while the gradient method with $\alpha = \frac{2}{m + L}$ is known to be fragile to such noise \[10, Section 5.2\]. Comparing the high frequency responses of these two cases immediately leads to the same conclusion. Finally, the slope of Bode plot at the crossover frequency supports the fact that Nesterov's method works for a larger class of functions than the Heavy-ball method.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Loop-shaping interpretations for optimization methods", "weight": 1.0} -->

In summary, the intuition brought by the traditional loop-shaping theory is consistent with the known properties of the existing first-order methods. This suggests that loop-shaping intuition may be used as a general high-level guideline in the design of optimization methods. The control interpretations above also indicate that classical PID tuning can be used for optimization algorithm design.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Loop-shaping interpretations for optimization methods", "weight": 1.0} -->

It remains an open question as to how to choose an appropriate $K{(z)}$ subject to different assumptions on the objective function. Since acceleration schemes for the optimization of quadratic functions or functions in $\mathcal{F}{(m,L)}$ already exist, we will focus on the case $f \in {\mathcal{S}{(m,L)}}$. We will derive one connection between such an optimization design problem and classical control synthesis theory.

<!-- chunk {"id": "body-0046", "role": "body", "section": "New feedback representations for first-order methods", "weight": 1.0} -->

The feedback representation for first-order methods involves a nonlinear operator $P$ which belongs to the sector $(m,L)$. This does not coincide perfectly with a gain bound since upper and lower bounds don't match. We will therefore, use a loop-shifted $F_{u}{(P^{\prime},K^{\prime})}$ that ensures the small gain condition on $P^{\prime}$ captures the full sector. Choose $P^{\prime}$ to map $u$ to $v = {Pu}$ as $v^{k} = {u^{k} - {\frac{2}{m + L}{\nabla f}{({u^{k} + x^{\star}})}}}$. Then, substitute $\xi^{k} = u^{k} = {x^{k} - x^{\star}}$ into the gradient descent method to get an alternative feedback interconnection

<!-- chunk {"id": "body-0047", "role": "body", "section": "New feedback representations for first-order methods", "weight": 1.0} -->

Suppose $K = {I_{p} \otimes \overline{K}}$ where $\overline{K}$ is a SISO LTI system. In general, a loop transformation argument can be used to show that any optimization method $F_{u}{(P,K)}$ can also be represented as $F_{u}{(P^{\prime},K^{\prime})}$ where $K^{\prime} = {I_{p} \otimes {\overline{K}}^{\prime}}$ and ${\overline{K}}^{\prime} = {\overline{K}/{({\overline{K} - \frac{2}{m + L}})}}$. Consequently, the feedback interconnection provides another way to model first-order methods.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Recovery of rate results for gradient descent", "weight": 1.0} -->

As a sanity check, we apply Theorem 2 to recover convergence rate results for the gradient descent method applied to functions in $\mathcal{S}{(m,L)}$. Since ${\overline{K}{(z)}} = \frac{- \alpha}{z - 1}$, we have

<!-- chunk {"id": "body-0049", "role": "body", "section": "Recovery of rate results for gradient descent", "weight": 1.0} -->

Clearly, ${\overline{K}}^{\prime}{({\rhoz})}$ is stable for any $\rho > 0$. Moreover, ${\|{{\overline{K}}^{\prime}{({\rhoz})}}\|} = \rho^{- 1}$. By Theorem 2, the gradient descent method converges for any $\rho > \frac{L - m}{L + m}$. This recovers the existing rate result for the gradient method with $\alpha = \frac{2}{L + m}$. Another popular choice for $\alpha = \frac{1}{L}$. In this case, the shifted controller is given by

<!-- chunk {"id": "body-0050", "role": "body", "section": "Recovery of rate results for gradient descent", "weight": 1.0} -->

where $\kappa{: =}\frac{L}{m}$ is the condition number. Hence, one has

<!-- chunk {"id": "body-0051", "role": "body", "section": "Recovery of rate results for gradient descent", "weight": 1.0} -->

Upon simplifying together with $\rho > {\frac{1}{2}{({1 - \frac{1}{\kappa}})}}$, we finally obtain $\rho > {1 - \frac{1}{\kappa}}$, which is the linear convergence rate for the gradient descent method when $\alpha = \frac{1}{L}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Remark 1", "weight": 1.0} -->

A small technical issue in the above analysis is that the rate result proved by the small gain theorem is a strict inequality. This is due to the fact that for LTI systems, input-output stability is slightly stronger than the global uniform stability. See \[5, Remark 1\] for a detailed explanation. This issue is negligible from a practical standpoint.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Connections to complementary sensitivity", "weight": 1.0} -->

This subproblem may be reformulated as an $\mathcal{H}_{\infty}$ state feedback synthesis problem since $\overline{K}$ always contains a pure integrator and the state of the scaled dynamics $\frac{1}{{\rhoz} - 1}$ is accessible at every timestep. Consequently, the only design variable is the state feedback gain, which happens to be the stepsize of the gradient method. This explains why acceleration in this case is difficult even given memory of past iterates. It is worth noting that $\overline{K}{({\rhoz})}$ always has an unstable pole at $z = \rho^{- 1}$. There is a large body of discrete-time complementary sensitivity integral results which could potentially be used in studying the design limits of $\overline{K}$ under the analytic constraints posed by the unstable pole at $\rho^{- 1}$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Connections to complementary sensitivity", "weight": 1.0} -->

From the above connection, we can see that acceleration typically requires some function properties which can be decoded as constraints involving dynamics. The condition is a static constraint, and it is hard to design accelerated schemes with this single constraint. However, it is still possible to accelerate non-convex optimization when other function properties are available, e.g. $f \in {\mathcal{L}{(L)}}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper discussed connections between the analysis of optimization algorithms and classical control-theoretic concepts. Specifically, the gradient method, the Heavy-ball method, and Nesterov's accelerated method were interpreted as combinations of PID and lag compensators. A loop-shaping interpretation was also used to explain several well-known robustness properties of these algorithms.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We invoked the small gain theorem to show that finding worst-case convergence rates for algorithms amounts to computing the gain of a complementary sensitivity function. In addition, we demonstrated a connection between $\mathcal{H}_{\infty}$ state feedback synthesis and stepsize selections of the gradient method. These observations are an encouraging first step toward leveraging tools from control theory for the analysis and eventual synthesis of robust optimization algorithms.
