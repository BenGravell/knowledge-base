<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Robust Accelerated Optimization Algorithm for Strongly Convex Functions

Topics include Robustness, Optimization, Control, Robust momentum method, Convex function, Gradient method.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This work proposes an accelerated first-order algorithm we call the Robust Momentum Method for optimizing smooth strongly convex functions. The algorithm has a single scalar parameter that can be tuned to trade off robustness to gradient noise versus worst-case convergence rate. At one extreme, the algorithm is faster than Nesterov's Fast Gradient Method by a constant factor but more fragile to noise. At the other extreme, the algorithm reduces to the Gradient Method and is very robust to noise. The algorithm design technique is inspired by methods from classical control theory and the resulting algorithm has a simple analytical form. Algorithm performance is verified on a series of numerical simulations in both noise-free and relative gradient noise cases.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Consider the unconstrained optimization problem where $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is $L$-smooth and $m$-strongly convex. The strong convexity of $f$ guarantees that there exists a unique minimizer $x_{\star}$ satisfying ${{\nabla f}{(x_{\star})}} = 0$. First-order methods are widely used for solving when the Hessian is prohibitively expensive to compute, e.g., when the problem dimension is large. A simple first-order algorithm for solving is the Gradient Method (GM), For smooth and strongly convex $f$, the GM with a well-chosen stepsize converges linearly to the optimizer.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

That is, for some $c \geq 0$ and $\rho \in {\lbrack 0,1)}$, we have For example, the standard choice $\alpha = {1/L}$ leads to a linear rate $\rho = {1 - \frac{m}{L}}$, while the choice $\alpha = \frac{2}{L + m}$ results in the improved linear rate $\rho = \frac{L - m}{L + m}$.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The issue with the Gradient Method, however, is that the convergence rate is slow, especially for ill-conditioned problems where the ratio $\frac{L}{m}$ is large. A common method of accelerating convergence is to use *momentum*. A well-established momentum algorithm for smooth and strongly convex $f$ is Nesterov's Fast Gradient Method^11^1Also called Neterov's accelerated gradient method., (FGM) described by the iteration The FGM tuned with $\alpha = \frac{1}{L}$ and $\beta = \frac{\sqrt{L} - \sqrt{m}}{\sqrt{L} + \sqrt{m}}$ converges with rate $\rho^{2} < {1 - \sqrt{m/L}}$, which is faster than the GM rate^22^2A numerical study in revealed that the standard rate bound for FGM derived in is conservative. Nevertheless, the bound has a simple algebraic form and is asymptotically tight..

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rate can be improved to $\rho = {1 - \sqrt{m/L}}$ using an accelerated algorithm called the Triple Momentum Method. This is the fastest known worst-case convergence rate for this class of problems.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Robustness issues arise naturally in many optimization problems. For example, achieving the above rates associated with each first-order method requires knowledge of $L$ and $m$, which may not be accurately accessible in practice. In addition, the gradient evaluation can be inexact for certain applications. These issues motivate the need for accelerated first-order methods that are robust to underlying design assumptions.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

As observed in \[3, §5.2\], optimization algorithm design involves a tradeoff between performance and robustness. For example, consider stepsize tuning for the GM. Using $\alpha = \frac{2}{L + m}$ optimizes the convergence rate, but makes the algorithm fragile to gradient noise. The more conservative choice $\alpha = \frac{1}{L}$ results in slower convergence, but more robustness to noise. This is consistent with the intuition that a smaller stepsize can improve the algorithm's robustness at the price of degrading its performance. For momentum methods, exploiting the tradeoff between performance and robustness is less straightforward, since one has to tune multiple algorithm parameters in a coupled manner to achieve acceleration. This tradeoff is exploited in for first-order methods applied to smooth convex problems. In this work, we design a first-order method that exploits the tradeoff between robustness and performance for smooth strongly convex problems.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Robust Momentum Method", "weight": 1.0} -->

Our proposed algorithm is parameterized by a scalar $\rho$ that represents the worst-case convergence rate of the algorithm in the noise-free case. Specifically, the iteration is governed by the following recursion with arbitrary initialization ${x_{0},x_{- 1}} \in {\mathbb{R}}^{n}$ where $\alpha$, $\beta$, and $\gamma$ depend directly on the parameter $\rho$ as We now state the key convergence property of the Robust Momentum Method in the noise-free case.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Convergence rate proof", "weight": 1.0} -->

In this section, we derive a proof for Theorem 1. The approach that follows is similar to the one used, with one important difference. In addition to proving a rate bound as, we also derive a Lyapunov function that yields intuition for the algorithm's behavior and robustness properties.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Control design interpretations", "weight": 1.0} -->

In this section, we cast the problem of algorithm analysis as a robust control problem. Specifically, we can view the problem of algorithm analysis as being equivalent to solving a Lur'e problem. The Lur'e setup is illustrated in Figure 1, where a linear dynamical system $G$ is in feedback with a static nonlinearity $\phi$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Control design interpretations", "weight": 1.0} -->

The Robust Momentum Method (as well as the Fast Gradient Method and ordinary Gradient Method) can be written in this way by setting $\phi = {\nabla f}$ and choosing $A$, $B$, and $C$ appropriately. For example, the Robust Momentum Method is given by Here, we shifted all signals so they are measured relative to the steady-state value $x_{\star}$ and therefore assumed that ${{\nabla f}{}} = 0$. We also assumed without loss of generality that $u_{k}$ and $y_{k}$ are scalars. This interpretation was used in to provide a unified analysis framework.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Control design interpretations", "weight": 1.0} -->

Traditionally, Lur'e systems were analyzed in the frequency domain rather than the time domain. For the case of the Robust Momentum Method, the (discrete-time) transfer function of the linear block is given by It was observed in Section 2.1 that the Robust Momentum Method becomes the Gradient Method if $\rho = {1 - {1/\kappa}}$. This fact can be directly verified using the transfer function. Substituting this $\rho$ and the parameter values into, there is a pole-zero cancellation and we obtain ${G{(z)}} = \frac{- 1}{L{({z - 1})}}$, which is the transfer function for the Gradient Method with stepsize $\alpha = \frac{1}{L}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Frequency-domain condition", "weight": 1.0} -->

Continuing with the frequency-domain interpretation, Lur'e systems can be analyzed using the formalism of Integral Quadratic Constraints (IQCs). To this end, the nonlinearity is characterized by a quadratic inequality that holds between its input and output where $\hat{y}$ and $\hat{u}$ are the $z$-transforms of $\{ y_{k}\}$ and $\{ u_{k}\}$, respectively, and $\Pi{(z)}$ is a para-Hermitian matrix. For convenience, we use a loop-shifting transformation to move the nonlinearity $\phi = {\nabla f}$ from the sector $(m,L)$ to the sector $(0,{\kappa - 1})$. We also scale the frequency variable $z$ by a factor of $\rho$ so that we can reduce the problem of certifying exponential stability (finding a linear rate) to that of certifying BIBO stability. This procedure is described.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Frequency-domain condition", "weight": 1.0} -->

The nonlinearity of interest is sector-bounded and slope-restricted because it is the gradient of a function $g \in {\mathcal{F}{(0,{\kappa - 1})}}$. We may therefore represent the nonlinearity with a Zames--Falb IQC as, leading to The transformed transfer function is To certify stability of the feedback interconnection, we must have $\overset{\sim}{G}{({\rhoz})}$ stable and for all ${|z|} = 1$, Equation has a graphical interpretation; that the Nyquist plot of ${F{(z)}}{: =}{{({1 - {\rhoz^{- 1}}})}\left({{{({\kappa - 1})}\overset{\sim}{G}{({\rhoz})}} - 1} \right)}$ should lie entirely in the left half-plane.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Graphical design for robustness", "weight": 1.0} -->

The frequency-domain condition can provide useful intuition for the design of robust accelerated optimization methods. We can visualize different algorithms by choosing the parameters $\alpha,\beta,\gamma$ appropriately.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Graphical design for robustness", "weight": 1.0} -->

In Figure 2 (left panel), we show the Nyquist plot for the Gradient Method using the sector IQC. To this effect, we set $\beta = \gamma = 0$ and use either $\alpha = \frac{2}{L + m}$ or $\alpha = \frac{1}{L}$. As we increase $\rho$, the Nyquist plots become ellipses in the left half-plane. At the fastest certifiable rate (smallest $\rho$), the plots become vertical lines. When $\alpha = \frac{2}{L + m}$, the vertical line coincides with the imaginary axis, whereas when $\alpha = \frac{1}{L}$, the vertical line is shifted left. This result confirms our intuition that since the imaginary axis is the stability boundary, robust stability is achieved as the Nyquist contour moves further left, away from the boundary.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Graphical design for robustness", "weight": 1.0} -->

The Robust Momentum Method was designed such that the Nyquist diagram forms a vertical line passing through the point $({- \nu},0)$. In other words, we solved for $(\alpha,\beta,\gamma)$ such that holds with the right-hand side replaced by $- \nu$. Constraining the Nyquist plot as such directly leads to the choice with $\nu$ related to $\rho$ via. In Figure 2 (right panel), we show the Nyquist plot for the Robust Momentum Method using the Zames--Falb IQC (for $\nu = 0$ and $\nu = \frac{1}{2}$). We also show Nyquist plots that certify a convergence rate of $\rho$ that is larger than the corresponding algorithm parameter. This leads to ellipses as with the Gradient Method. Note that although the RMM and GM plots look similar, the RMM $\rho$-values are generally smaller due to acceleration.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Graphical design for robustness", "weight": 1.0} -->

In contrast, the FGM (center panel) does not produce a vertical line in the Nyquist plot but still touches the stability boundary at the optimal $\rho$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Graphical design for robustness", "weight": 1.0} -->

(b) Fast Gradient Method (c) Robust Momentum Method Figure 2: Frequency-domain plots of various algorithms for κ = 10 and different values of the convergence rate ρ. The system is stable if the entire curve lies in the left half-plane. (a) Gradient Method for α = 1/L (solid) and α = 2/(L + m) (dashed). The latter is right on the stability boundary while the former is shifted left (more robust). (b) Fast Gradient Method. (c) Robust Momentum Method for ν = 1/2 (solid) and ν = 0 (dashed). Again, the latter is right on the stability boundary while the former is shifted left (more robust).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Further robustness interpretations", "weight": 1.0} -->

The parameter $\nu$ can be interpreted as the input feed-forward passivity index (IFP), which is a measure of the shortage or excess of passivity of the system $F{(z)}$ defined above. In the frequency domain, the discrete-time definition of the IFP index is given by^33^3Most sources use a negative feedback convention. The definition we give in uses the positive feedback convention. where $\lambda_{\text{max}}{(\cdot)}$ denotes the largest eigenvalue and $F^{\ast}$ is the conjugate transpose of $F$. For the SISO case, reduces to $\nu = {- {{\max_{{|z|} = 1}{Re}}{({F{(z)}})}}}$, which is the shortest distance between each curve and the imaginary axis in Figure 2.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Further robustness interpretations", "weight": 1.0} -->

We can also interpret $\nu$ as a robustness margin in the time domain using the Lyapunov function defined. In the proof of Theorem 1, when we substitute the definition for $V_{k}$ into, we obtain Proving the desired rate bound only requires to hold, so the term $\nu{\parallel{{\nabla g}{(y_{k})}}\parallel}^{2}$ can be interpreted as an additional margin that ensures the inequality $V_{k + 1} \leq {\rho^{2}V_{k}}$ will hold even if underlying assumptions such as exactness in gradient evaluations or accurate knowledge of $L$ and $m$ are violated. As we increase $\rho$, the linear rate becomes slower, but $\nu$ also increases via, which serves to increase the robustness margin in the inequality.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Robustness to gradient noise", "weight": 1.0} -->

The Robust Momentum Method has a single parameter, which can be used to tune the performance. In this section, we provide both simulations and numerical rate analyses to verify the performance of the algorithm when the gradient is subject to relative deterministic noise. Specifically, we will suppose that instead of measuring the gradient ${\nabla f}{(y_{k})}$, we measure $u_{k} = {{{\nabla f}{(y_{k})}} + r_{k}}$ where $r_{k} \in {\mathbb{R}}^{n}$ satisfies ${\parallel r_{k}\parallel} \leq {\delta{\parallel{{\nabla f}{(y_{k})}}\parallel}}$. For a given fixed $\delta \geq 0$, we will bound the worst-case performance of the algorithm over all $f \in {\mathcal{F}{(m,L)}}$ and feasible $\{ r_{k}\}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Numerical rate analysis", "weight": 1.0} -->

To find the worst-case performance, we adopt the methodology from \[3, Eq. 5.1\]. There, the authors formulate a linear matrix inequality parameterized by $\hat{\rho}$ and $\delta$ whose feasibility provides a sufficient condition for convergence with linear rate $\hat{\rho}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Numerical rate analysis", "weight": 1.0} -->

In Figure 3, we plot the computed convergence rate as a function of noise strength $\delta$ for the Gradient Method, Fast Gradient Method, and Robust Momentum Method. Note that the worst-case rate in closed form for the Gradient Method is given.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Numerical rate analysis", "weight": 1.0} -->

First, consider the Robust Momentum Method. When $\nu = 0$ and there is no gradient noise ($\delta = 0$), the method achieves the fast convergence rate $1 - {1/\sqrt{\kappa}}$. Increasing the noise level above $\delta > 0.13$, however, leads to a loss of convergence guarantee. As we increase $\nu$, the convergence rate becomes slower but the method is capable of tolerating larger noise levels. In the limiting case as $\nu = {1 - \frac{1}{2\kappa}}$ the Robust Momentum Method becomes the Gradient Method with $\alpha = \frac{1}{L}$ (dashed black line).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Numerical rate analysis", "weight": 1.0} -->

It is interesting to note that the Fast Gradient Method has a faster convergence bound than the Robust Momentum Method for noise levels $0.26 < \delta < 0.41$. However, the Fast Gradient Method is also unstable for $\delta > 0.5$ while the Robust Momentum Method can be tuned so that it converges with noise levels up to $\delta\rightarrow 1$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Numerical simulations", "weight": 1.0} -->

To illustrate the noise robustness properties of different tunings of the Robust Momentum Method, we compared it to the Fast Gradient Method when applied to a simple two-dimensional quadratic function. We used the gradient where the gradient noise is $r_{k} = {- {\delta{\nabla f}{(y_{k})}}}$. See Figure 4. The RMM with $\nu = 0$ has the fastest convergence rate in the noiseless case ($\delta = 0$), but quickly diverges when noise is present. The FGM is more robust to noise, but also diverges when the noise magnitude $\delta$ is too large. The RMM with $\nu = 0.55$ remains stable for large amounts of noise, although in the absence of noise the convergence rate is slower than both other methods.
