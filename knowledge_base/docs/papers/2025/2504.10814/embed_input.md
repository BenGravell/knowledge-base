An Operator Splitting Method for Large-Scale CVaR-Constrained Quadratic Programs

We introduce a fast and scalable method for solving quadratic programs with conditional value-at-risk (CVaR) constraints. While these problems can be formulated as standard quadratic programs, the number of variables and constraints grows linearly with the number of scenarios, making general-purpose solvers impractical for large-scale problems. Our method combines operator splitting with a specialized O(mlog m) algorithm for projecting onto CVaR constraints, where m is the number of scenarios. The method alternates between solving a linear system and performing parallel projections, onto CVaR constraints using our specialized algorithm and onto box constraints by simple clipping. Numerical examples from several application domains demonstrate that our method outperforms general-purpose solvers by several orders of magnitude on problems with up to millions of scenarios. Our method is implemented in an open-source package called CVQP.

## Introduction

Many applications in finance and engineering require controlling the risk of extreme outcomes. A widely used measure for tail risk is the *conditional value-at-risk* (CVaR), defined as the expected value of losses exceeding a given quantile. CVaR is a coherent and convex risk measure, so optimization problems involving CVaR can be reliably and efficiently solved.

Many practical applications, from portfolio optimization to quantile regression, can be formulated as quadratic programs with CVaR constraints. While these problems are convex and can be reformulated as standard quadratic programs, the number of variables and constraints grows linearly with the number of scenarios. For problems with many scenarios, general-purpose solvers become prohibitively slow or fail entirely. To address this challenge, we develop a fast and scalable method for solving quadratic programs with CVaR constraints.

### Warm starting

Two effective strategies for choosing the initial point are solving with a reduced set of scenarios and using that solution to initialize the full problem, and using a quadratic approximation of the CVaR constraint to compute an initial point. Similarly, the sorting step in the CVaR projection can be warm-started using the sorted order from the previous ADMM iteration. Since the projection input changes only slightly between iterations, the sorted order is nearly preserved, and an adaptive sorting algorithm can exploit this to reduce the per-iteration cost in practice.

$\eta$: the decrease to the untied entries,

We now present preliminaries that motivate our efficient algorithm for evaluating the projection operator $\Pi_{\mathcal{C}}$, i.e., for solving the problem

At each step, $n_{u}$ either decreases by $1$, or remains the same. At each step, $n_{t}$ increases by $1$. If the algorithm hasn't terminated after $m$ steps, then there are $m$ tied entries, thus the subsequent decrease step will reduce the sum to the desired value, and the algorithm will terminate. Each step of the algorithm has constant complexity, and thus the algorithm (with sorted input) has complexity $O{(m)}$. Therefore, including the sorting and unsorting, the total complexity of the algorithm is $O{({m{\log m}})}$.

We present two main contributions. First, we develop an $O{({m{\log m}})}$ algorithm for projecting onto CVaR constraints, where $m$ is the...
