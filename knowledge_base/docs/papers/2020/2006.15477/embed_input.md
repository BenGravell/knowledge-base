<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Convex Data-driven Approach for Nonlinear Control Synthesis

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider a class of nonlinear control synthesis problems where the underlying mathematical models are not explicitly known. We propose a data-driven approach to stabilize the systems when only sample trajectories of the dynamics are accessible. Our method is founded on the density function based almost everywhere stability certificate that is dual to the Lyapunov function for dynamic systems. Unlike Lyapunov based methods, density functions lead to a convex formulation for a joint search of the control strategy and the stability certificate. This type of convex problem can be solved efficiently by invoking the machinery of the sum of squares (SOS). For the data-driven part, we exploit the fact that the duality results in the stability theory of the dynamical system can be understood using linear Perron-Frobenius and Koopman operators. This connection allows us to use data-driven methods developed to approximate these operators combined with the SOS techniques for the convex formulation of control synthesis. The efficacy of the proposed approach is demonstrated through several examples.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The celebrated Lyapunov theory lays the foundation for stability analysis of nonlinear dynamical systems. Lyapunov functions provide stability certificates for a nonlinear system. For a given system, searching for a proper Lyapunov function can often be formulated as a convex optimization problem and thus easy to address. For instance, for polynomial dynamics, this is achieved through the sum of squares (SOS). Regardless of its similarity to stability analysis, the problem of nonlinear controller synthesis is more challenging. Other than a few special cases such as linear quadratic control problems, the joint search for Lyapunov stability certificate and control strategy can no longer be cast as convex optimization problems. This is exacerbated by the fact that in many applications, the underlying mathematical models are not available. Our objective in this paper is to establish a principled approach for nonlinear control synthesis when the mathematical models of the underlying dynamics are not explicitly given.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide a systematic approach for data-driven control synthesis for a class of control affine nonlinear systems of the form The objective is to design state feedback controller $\mathbf{u} = {\mathbf{u}{(\mathbf{x})}}$ such that the closed-loop system is asymptotically stable. To achieve this objective, we use density function-based dual stability formulation introduced by Rantzer for almost everywhere stability analysis and synthesis for nonlinear control systems. Unlike Lyapunov function-based approach for control design, the co-design problem of simultaneously finding the density function and almost everywhere stabilizing controller is a convex optimization problem. We exploit this convexity property for data-driven control synthesis. In, it was shown that the duality between density and Lyapunov function in the stability theory could be understood using linear operator theoretic framework. In particular, the duality between Koopman and Perron-Frobenius operators is at the heart of the duality in the stability theory. This linear operator theoretic framework is also exploited for the data-driven control design.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The recent advances in the data-driven approximation of the Koopman operator are used to discover a data-driven approach for the nonlinear control synthesis. In Koopman theory, a nonlinear system is lifted to, albeit infinite-dimensional, a linear system. This lifting can be approximated using data generated from the underlying nonlinear dynamics by the well-known Extended Dynamic Mode Decomposition (EDMD) algorithm. These tools have been successfully applied in many domains, such as fluid dynamics, power systems, to understand the principle components/modes of given nonlinear dynamics. Recently, Koopman theory has been introduced to the control synthesis tasks, hoping that the controller designed in the lifted space could be easier than that in the original state space. It turns out to be a challenging problem since the lifting argument in the presence of control is no longer valid. Regardless of the progress that has been made in this direction during the last few years, a principle data-driven approach for nonlinear control synthesis is not yet available. We use the EDMD algorithm combined with the duality results for the data-driven approximation of the Perron-Frobenius (P-F) operator corresponding to the control system.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This linear P-F operator for the control system is used to formulate a convex optimization problem for control synthesis. This optimization is over polynomials and can be solved using the SOS solvers. The complexity of the resulting optimization problem depends on the polynomial basis used to approximate the linear operators. Since control often doesn't require high fidelity models, we expect to construct a reliable controller using a relatively small number of basis functions. We envision that this method can be applied to low dimensional and medium dimensional dynamical systems (e.g. robotics, distributed power-electronics control applications).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rest of the paper is organized as follows. In Section II, we provide a review on density function methods, SOS, and Koopman theory; these are the ingredients of our approach. Problem formulation and the details of our method are presented in Section III. This is followed by several numerical examples in Section IV and a short concluding remark in Section V.

<!-- chunk {"id": "body-0008", "role": "body", "section": "II-A Density function approach for control synthesis", "weight": 1.0} -->

Consider control-affine system with feedback control $\mathbf{u}{(\mathbf{x})}$ and $\mathbf{x} \in {\mathbb{R}}^{n}$. This closed-loop system is asymptotically stable with respect to the origin $\mathbf{x} = 0$ if there exists a Lyapunov function $V$ such that Thus, for the purpose of control synthesis, one seeks a pair $(V,\mathbf{u})$ such that holds. Note that this inequality is bilinear with respect to $V,\mathbf{u}$ and is thus a non-convex problem. This is the major obstacle preventing Lyapunov theory being widely used in control synthesis. In, a dual to Lyapunov's stability theorem was established.

<!-- chunk {"id": "body-0009", "role": "body", "section": "II-B Sum of squares", "weight": 1.0} -->

SOS optimization is a relaxation of positive polynomial constraints appearing in polynomial optimization problems which are generally difficult to solve. SOS polynomials are in a set of polynomials which can be described as a finite linear combinations of monomials, i.e., $p = {\sum_{i = 1}^{\ell}{d_{i}p_{i}^{2}}}$ where $p$ is a SOS polynomial; $p_{i}$ are monomials; and $d_{i}$ are coefficients. Hence, SOS is a sufficient condition for nonnegativity of a polynomial and thus SOS relaxation provides a lower bound on the minimization problems of polynomial optimizations.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-B Sum of squares", "weight": 1.0} -->

Using the SOS relaxation, any polynomial optmization problems with positive constraints can be formulated as SOS optimization as follows: | | {{{\min\limits_{\mathbf{d}}{\mathbf{w}^{\top}\mathbf{d}s}}.t.{{{p_{s}{(\mathbf{x},\mathbf{d})}} \in {\Sigma{\lbrack\mathbf{x}\rbrack}}},{{p_{e}{(\mathbf{x};\mathbf{d})}} = 0}}},} | | | where $\Sigma{\lbrack\mathbf{x}\rbrack}$ denotes SOS set; $\mathbf{w}$ is weighting coefficients; $p_{s}$ and $p_{e}$ are polynomials with coefficients $\mathbf{d}$. The problem in is translated into Semidefinite Programming (SDP).

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-B Sum of squares", "weight": 1.0} -->

There are readily available SOS optimization packages such as SOSTOOLS and SOSOPT to solve.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-C Linear Koopman and Perron-Frobenius Operators", "weight": 1.0} -->

For a dynamical system, $\overset{˙}{\mathbf{x}} = {\mathbf{F}{(\mathbf{x})}}$, there are two different ways of linearly lifting the finite dimensional nonlinear dynamics from state space to infinite dimension space of functions, $\mathcal{F}$, namely Koopman and Perron-Frobenius operators. Denote the solution of system by $\phi_{t}{(\mathbf{x})}$. The definitions of these operators along with the infinitesimal generators of these operators are defined as follows.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Data-driven control synthesis", "weight": 1.0} -->

We are interested in data-driven control synthesis for multivariate nonlinear dynamics^11^1we use bold symbols to denote column vectors unless it is specified as a row vector or a matrix.: where state $\mathbf{x} \in {\mathbb{R}}^{n}$ and control inputs $\mathbf{u}$; and $\mathbf{F}$ represents open-loop dynamics; and ${\mathbf{G}{(\mathbf{x})}} = {({\mathbf{G}_{1}{(\mathbf{x})}},\ldots,{\mathbf{G}_{m}{(\mathbf{x})}})}$ constitutes feedback control loop corresponding to control inputs $\mathbf{u} = {\lbrack u_{1},\ldots,u_{m}\rbrack}^{\top}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Data-driven control synthesis", "weight": 1.0} -->

The explicit description of $\mathbf{F}$ and $\mathbf{G}$ are not available, but we have access to a set of sample trajectories generated from this system. Our goal is a state feedback strategy $\mathbf{u}$ that globally stabilizes.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A Density function approach reformulation", "weight": 1.0} -->

Based on the density function method, proposed an implementable algorithm using SOS. In particular, the parameterization where $a$ and $\mathbf{c} = {\lbrack c_{1},\ldots,c_{m}\rbrack}^{\top}$ are polynomials, $b$ is a positive polynomial (positive at $\mathbf{x} \neq 0$), and $\alpha$ is a sufficiently large number such that the integrability condition in Theorem (1 ‣ II-A Density function approach for control synthesis ‣ II Background ‣ A convex data-driven approach for nonlinear control synthesis")) holds.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A Density function approach reformulation", "weight": 1.0} -->

With this parametrization, becomes The positive polynomial $b$ can be chosen as a quadratic control Lyapunov function for the linearized dynamics at the origin $\mathbf{x} = 0$. The control synthesis then becomes finding polynomials $a$ and $\mathbf{c}$ such that which is clearly a standard SOS problem.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-B Data-driven approximation of linear operators", "weight": 1.0} -->

The fundamental object of interest in the data-driven control synthesis is the approximation of the infinitesimal generator of P-F operator shown in (7 ‣ II-C Linear Koopman and Perron-Frobenius Operators ‣ II Background ‣ A convex data-driven approach for nonlinear control synthesis")) corresponding to vector fields $\mathbf{F}$ and $\mathbf{G}$ affine in control system. For the finite dimensional approximate representation of inequality, we will approximate the divergence terms, i.e., $\nabla \cdot {(\mathbf{F} \cdot)}$ and $\nabla \cdot {(\mathbf{G}_{i} \cdot)}$ for $i = {1,\ldots,m}$, using Koopman and P-F generators. We adopt the technique from for the approximation of these two generators.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-B Data-driven approximation of linear operators", "weight": 1.0} -->

In particular, data generated from the control system with zero input and unit step inputs for each control input is used for the approximation of the generators $\mathcal{P}_{\mathbf{F}}$ and $\mathcal{P}_{\mathbf{F} + \mathbf{G}_{i}}$ respectively. Using linearity property, the infinitesimal generator for $\mathbf{G}_{i}$ i.e., $\mathcal{P}_{\mathbf{G}_{i}}$ is approximated from ${\mathcal{P}_{\mathbf{F} + \mathbf{G}_{i}} - \mathcal{P}_{\mathbf{F}}} = \mathcal{P}_{\mathbf{G}_{i}}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-B Data-driven approximation of linear operators", "weight": 1.0} -->

Using similar argument, it also follows that Furthermore, we notice that the P-F generator for vector field $\mathbf{F}$ can be written as This allows us to approximate the P-F generator using algorithm known for the approximation of Koopman operator such as Extended Dynamics Mode Decomposition (EDMD). We show that the multiplication operator corresponding to $\nabla \cdot \mathbf{F}$ in can also be approximated using the approximate Koopman operator.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-B Data-driven approximation of linear operators", "weight": 1.0} -->

For the data-driven approximation, let $\mathbf{\phi}{(t,\mathbf{x};\mathbf{u})}$ denote a solution of at time $t$ starting from $\mathbf{x}$ with control input $\mathbf{u}$. First, we collect time-series data from the dynamical system in by injecting different control inputs: i) zero control inputs (i.e., $\mathbf{u} = 0$), and ii) unit step control inputs, i.e., $\mathbf{u} = \mathbf{e}_{j}$ for $j = {1,\ldots,m}$ for a finite time horizon with sampling step $\deltat$, where $\mathbf{e}_{j} \in {\mathbb{R}}^{m}$ denotes unit vectors (i.e., $j$th entry of $\mathbf{e}_{j}$ is 1, otherwise 0).

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B Data-driven approximation of linear operators", "weight": 1.0} -->

The time-series data of the system responses corresponding to each control input case are collected: with $i = {0,1,\ldots,m}$ for zero and unity control inputs, where $\mathbf{y} = {\mathbf{\phi}{({t + {\deltat}},\mathbf{x};\mathbf{u})}}$; and $T_{i}$ are the number of time-series data points collected for each input case. The samples in $\mathbf{X}_{i}$ do not have to be from a single trajectory; $\mathbf{X}_{i}$ can be a concatenation of multiple experiment/simulation trajectories.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-B Data-driven approximation of linear operators", "weight": 1.0} -->

We construct a polynomial basis denoted by as a vector of monomials up to $q$th order. The total number of monomials in the basis, $Q = \binom{n + q}{q}$. Using the EDMD algorithm, the Koopman operator, ${\mathbb{K}}_{i}$^22^2For notational simplicity, we do not explicitly denote the Koopman operator dependence on the sampling time $\deltat$ i.e., ${\mathbb{K}}_{\deltat}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-B Data-driven approximation of linear operators", "weight": 1.0} -->

The Koopman generator for vector field, $\mathbf{F}$, can now be approximated as We approximate the multiplication operator corresponding to the divergence of vector field $\mathbf{F}$ as follows where ${\mathcal{C}}_{x}$ is a coefficient vector corresponding to the original states in the basis function $\mathbf{\Psi}$ i.e., $\mathbf{x} = {{\mathcal{C}}_{x}^{\top}\mathbf{\Psi}}$. Since, $\mathbf{\Psi}$ are assumed to be monomials basis, we can extract $\mathbf{x}$ from $\mathbf{\Psi}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-C Convex Control Synthesis: Combining SOS with Koopman", "weight": 1.0} -->

In this section, we formulate convex control synthesis using SOS optimization and Koopman operator described in previous sections.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-C Convex Control Synthesis: Combining SOS with Koopman", "weight": 1.0} -->

The polynomial in is linear in terms of the coefficients of the polynomials, $a{(\mathbf{x})}$, $c_{j}{(\mathbf{x})}$, $j = {1,\ldots,m}$, hence we can solve SOS problem with as a SOS constraint, given as below: where $\mathbf{d} = {\lbrack\mathbf{z}_{a}^{\top},\mathbf{z}_{c}^{\top}\rbrack}^{\top}$ and the objective function is $\ell_{1}$-norm minimization to promote sparsity and robustness of solution. The last term in reflects the constraint, $\rho > 0$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-C Convex Control Synthesis: Combining SOS with Koopman", "weight": 1.0} -->

Subsequent to solving, we can construct a controller ${u_{j}{(\mathbf{x})}} = {{{c_{j}{(\mathbf{x})}}/a}{(\mathbf{x})}}$, $j = {1,\ldots,m}$ to stabilize the dynamical system. The steps of the proposed method described here in Section III is summarized in Fig. 1.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-A Van der Pol Oscillator", "weight": 1.0} -->

Dynamics of Van der Pol Oscillator is given as below: We collect time-series data points of zero and unit step input responses in $\mathbf{X}_{1 \sim 2}$ and $\mathbf{Y}_{1 \sim 2}$ shown, by doing repeated simulations. Simulation time spans from $0$ to $0.01$ \[s\] with time step ${\deltat} = 0.01$ \[s\], and we choose $10^{4}$ uniformly-distributed random initial points from ${\lbrack x_{1},x_{2}\rbrack} = {\lbrack{- 5},5\rbrack}^{2}$. In this case, number of data points for each input response case, $T_{1} = 9968$, $T_{2} = 9970$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-A Van der Pol Oscillator", "weight": 1.0} -->

Results of the control synthesis are shown in Fig. 2 where trajectories starting from some initial points converge to the origin.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-B Non-Polynomial System Example: Inverted Pendulum", "weight": 1.0} -->

Dynamics of a simple two-dimensional inverted pendulum is given as below: which is non-polynomial due to a sinusoidal function. We collect time-series data points for zero and unit step inputs in $\mathbf{X}_{1 \sim 2}$ and $\mathbf{Y}_{1 \sim 2}$, by doing repeated simulations, from $0$ to $0.001$ \[s\] with time step ${\deltat} = 0.001$ \[s\], starting from $10^{4}$ uniformly-distributed random initial points from ${\lbrack x_{1},x_{2}\rbrack} = {\lbrack{- \pi},\pi\rbrack}^{2}$. Number of data points for both input response cases, $T_{1} = T_{2} = 10^{4}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-B Non-Polynomial System Example: Inverted Pendulum", "weight": 1.0} -->

We choose $\alpha = 4$, ${b{(\mathbf{x})}} = {\mathbf{x}^{\top}\mathbf{x}}$, ${a{(\mathbf{x})}} = 1$, and $c{(\mathbf{x})}$ to be a polynomial with degree from $1$ to $3$. Following the proposed algorithm in Section III, a control solution is computed, ${u{(\mathbf{x})}} = {c{(\mathbf{x})}} = {{0.1553x_{1}^{3}} - {1.9884x_{1}}}$. Figure 3 shows trajectories of the dynamics with the synthesized control, starting from some initial points, demonstrating that the control solution from the proposed method can effectively stabilizes non-polynomial dynamical systems.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-C Lorenz System Dynamics", "weight": 1.0} -->

Dynamics of Lorenz attractor is given: where $\rho = 28$, $\sigma = 10$, and $\beta = \frac{8}{3}$. We sample the time-series data points from repeated simulations, from $0$ to $0.001$ \[s\], with time step ${\deltat} = 0.001$ \[s\], and uniformly distributed initial points collected from ${\lbrack x_{1},x_{2},x_{3}\rbrack} = {\lbrack{- {5 \times 5}}\rbrack}^{3}$. The data points collected for all input cases, $T_{1} = T_{2} = 9945$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-C Lorenz System Dynamics", "weight": 1.0} -->

For the parameters of stability conditions, we choose $\alpha = 4$, ${b{(\mathbf{x})}} = {\mathbf{x}^{\top}\mathbf{x}}$, ${a{(\mathbf{x})}} = 1$, and $c{(\mathbf{x})}$ to be a polynomial with degree from $1$ to $3$. Following the proposed method described in Section III, we get the solution, ${u{(\mathbf{x})}} = {c{(\mathbf{x})}} = {{- {26.9591x_{1}}} - {6x_{2}}}$, and the result of the control synthesis is depicted in Fig. 4, showing trajectories of the open-loop dynamics as well as the controlled dynamics, starting from different initial conditions. We can see that chaotic dynamics of the Lorenz attractor is stabilized to the origin by the control synthesized by our proposed method.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-D Rigid Body Control", "weight": 1.0} -->

Time-series data points are sampled from repeated time-domain simulations for four control input cases, i.e., $\mathbf{u} = 0$, $\mathbf{u} = \mathbf{e}_{1 \sim 3}$. Simulation time spans from $0$ to $0.001$ \[s\] with time step ${\deltat} = 0.001$ \[s\], starting from uniformly distributed random initial points, ${\lbrack{\mathbf{ω}}^{\top},{\mathbf{ψ}}^{\top}\rbrack} = {\lbrack{- {3 \times 3}}\rbrack}^{6}$. Each data matrix, $\mathbf{X}_{1 \sim 4}$, $\mathbf{Y}_{1 \sim 4}$ has 9986 time-series data points.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-D Rigid Body Control", "weight": 1.0} -->

Figure 5 shows trajectories of the states ${\mathbf{ω}}_{1 \sim 3}$ and ${\mathbf{ψ}}_{1 \sim 3}$, starting from some initial points, which demonstrates that the proposed method can deal with higher dimensional dynamical systems.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Concluding Remark", "weight": 1.0} -->

A systematic convex optimization-based framework is provided for data-driven stabilization of control affine nonlinear systems. The proposed approach relies on a combination of SOS optimization methods and recent advances in the data-driven computation of the Koopman operator. Future research efforts will focus on data-driven optimal control of the nonlinear system and the robust counterpart of this work by exploiting the sample complexity of Koopman and P-F operator.
