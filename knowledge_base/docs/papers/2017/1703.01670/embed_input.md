Control Interpretations for First-Order Optimization Methods

Topics include Optimization, Control, Learning.

First-order iterative optimization methods play a fundamental role in large scale optimization and machine learning. This paper presents control interpretations for such optimization methods. First, we give loop-shaping interpretations for several existing optimization methods and show that they are composed of basic control elements such as PID and lag compensators. Next, we apply the small gain theorem to draw a connection between the convergence rate analysis of optimization methods and the input-output gain computations of certain complementary sensitivity functions. These connections suggest that standard classical control synthesis tools may be brought to bear on the design of optimization algorithms.

## Introduction

First-order iterative optimization methods have been widely applied in data science and machine learning. These methods only require access to first-order derivative information, and iterate on the data until satisfactory convergence is achieved. For example, the gradient method is

Such simple methods are often favored over higher order methods such as Newton's method when the dimension of the underlying space is large and computing Hessians is prohibitively expensive.

This paper discussed connections between the analysis of optimization algorithms and classical control-theoretic concepts. Specifically, the gradient method, the Heavy-ball method, and Nesterov's accelerated method were interpreted as combinations of PID and lag compensators. A loop-shaping interpretation was also used to explain several well-known robustness properties of these algorithms.

We invoked the small gain theorem to show that finding worst-case convergence rates for algorithms amounts to computing the gain of a complementary sensitivity function. In addition, we demonstrated a connection between $\mathcal{H}_{\infty}$ state feedback synthesis and stepsize selections of the gradient method. These observations are an encouraging first step toward leveraging tools from control theory for the analysis and eventual synthesis of robust optimization algorithms.

The small gain theorem can be used to check the input-output stability of $\lbrack P,K\rbrack$ when the gains of $P$ and $K$ are both known. Note that there are exogenous signals $r$, $e$ in the setup of $\lbrack P,K\rbrack$ and zero initial conditions on $K$ to ensure that $K$ maps the zero input to a zero output. In contrast, $F_{u}{(P,K)}$ allows any initial condition for $K$, so the optimization method $F_{u}{(P,K)}$ can be initialized at any initial condition $\xi^{0} \in {\mathbb{R}}^{n}$....

When $f$ is a quadratic function, one can accelerate the gradient descent method by incorporating a momentum term into the iteration, such as the Heavy-ball method. Although the Heavy-ball method works extremely well for quadratic objective functions, it can fail to converge for other functions in $\mathcal{F}{(m,L)}$; see \[10, Section 4.6\].

We now demonstrate that the design of state-of-the-art optimization methods is actually consistent with general loop-shaping principles from control theory....
