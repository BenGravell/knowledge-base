<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A General Analysis of the Convergence of ADMM

Topics include Stability analysis, Optimization, Alternating-direction method of multipliers, Rate of convergence.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We provide a new proof of the linear convergence of the alternating direction method of multipliers (ADMM) when one of the objective terms is strongly convex. Our proof is based on a framework for analyzing optimization algorithms introduced in Lessard et al., reducing algorithm convergence to verifying the stability of a dynamical system. This approach generalizes a number of existing results and obviates any assumptions about specific choices of algorithm parameters. On a numerical example, we demonstrate that minimizing the derived bound on the convergence rate provides a practical approach to selecting algorithm parameters for particular ADMM instances. We complement our upper bound by constructing a nearly-matching lower bound on the worst-case rate of convergence.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The alternating direction method of multipliers (ADMM) seeks to solve the problem

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

with variables $x \in {\mathbb{R}}^{p}$ and $z \in {\mathbb{R}}^{q}$ and constants $A \in {\mathbb{R}}^{r \times p}$, $B \in {\mathbb{R}}^{r \times q}$, and $c \in {\mathbb{R}}^{r}$. ADMM was introduced in Glowinski & Marroco and Gabay & Mercier. More recently, it has found applications in a variety of distributed settings such as model fitting, resource allocation, and classification. A partial list of examples includes Bioucas-Dias & Figueiredo; Wahlberg et al.; Bird; Forero et al.; Sedghi et al.; Li et al.; Wang & Banerjee; Zhang et al.; Meshi & Globerson; Wang et al.; Aslan et al.; Forouzan & Ihler; Romera-Paredes & Pontil; Behmardi et al.; Zhang & Kwok. See Boyd et al. for an overview.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Part of the appeal of ADMM is the fact that, in many contexts, the algorithm updates lend themselves to parallel implementations. The algorithm is given in Algorithm 1. We refer to $\rho > 0$ as the step-size parameter.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

1: Input: functions f and g, matrices A and B, vector c, parameter ρ
7: until meet stopping criterion
Algorithm 1 Alternating Direction Method of Multipliers

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

A popular variant of Algorithm 1 is over-relaxed ADMM, which introduces an additional parameter $\alpha$ and replaces each instance of $Ax_{k + 1}$ in the $z$ and $u$ updates in Algorithm 1 with

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The parameter $\alpha$ is typically chosen to lie in the interval $(0,2\rbrack$, but we demonstrate in Section 8 that a larger set of choices can lead to convergence. Over-relaxed ADMM is described in Algorithm 2. When $\alpha = 1$, Algorithm 2 and Algorithm 1 coincide. We will analyze Algorithm 2.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

1: Input: functions f and g, matrices A and B, vector c, parameters ρ and α
7: until meet stopping criterion
Algorithm 2 Over-Relaxed Alternating Direction Method of Multipliers

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The conventional wisdom that ADMM works well without any tuning, for instance by setting $\rho = 1$, is often not borne out in practice. Algorithm 1 can be challenging to tune, and Algorithm 2 is even harder. We use the machinery developed in this paper to make reasonable recommendations for setting $\rho$ and $\alpha$ when some information about $f$ is available (Section 8).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we give an upper bound on the linear rate of convergence of Algorithm 2 for all $\rho$ and $\alpha$ (Theorem 7), and we give a nearly-matching lower bound (Theorem 8).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Importantly, we show that we can prove convergence rates for Algorithm 2 by numerically solving a $4 \times 4$ semidefinite program (Theorem 6). When we change the parameters of Algorithm 2, the semidefinite program changes. Whereas prior work requires a new proof of convergence for every change to the algorithm, our work automates that process.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our work builds on the integral quadratic constraint framework introduced in Lessard et al., which uses ideas from robust control to analyze optimization algorithms that can be cast as discrete-time linear dynamical systems. Related ideas, in the context of feedback control, appear in Corless; D'Alto & Corless. Our work provides a flexible framework for analyzing variants of Algorithm 1, including those like Algorithm 2 created by the introduction of additional parameters. In Section 7, we compare our results to prior work.

<!-- chunk {"id": "body-0014", "role": "body", "section": "ADMM as a Dynamical System", "weight": 1.0} -->

We group our assumptions together in Assumption 3.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

We assume that $f$ and $g$ are convex, closed, and proper. We assume that for some $0 < m \leq L < \infty$, we have $f \in {S_{p}{(m,L)}}$ and $g \in {S_{q}{(0,\infty)}}$. We assume that $A$ is invertible and that $B$ has full column rank.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

The assumption that $f$ and $g$ are closed (their sublevel sets are closed) and proper (they neither take on the value $- \infty$ nor are they uniformly equal to $+ \infty$) is standard.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

We begin by casting over-relaxed ADMM as a discrete-time dynamical system with state sequence $(\xi_{k})$, input sequence $(\nu_{k})$, and output sequences $(w_{k}^{1})$ and $(w_{k}^{2})$ satisfying the recursions

<!-- chunk {"id": "body-0018", "role": "body", "section": "Convergence Rates from Semidefinite Programming", "weight": 1.0} -->

Now, in Theorem 6, we make use of the perspective developed in Section 3 to obtain convergence rates for Algorithm 2. This is essentially the same as the main result of Lessard et al., and we include it because it is simple and self-contained.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Symbolic Rates for Various $\\rho$ and $\\alpha$", "weight": 1.0} -->

In Section 4, we demonstrated how to use semidefinite programming to produce numerical convergence rates. That is, given a choice of algorithm parameters and the condition number $\kappa$, we could determine the convergence rate of Algorithm 2. In this section, we show how Theorem 6 can be used to prove symbolic convergence rates. That is, we describe the convergence rate of Algorithm 2 as a function of $\rho$, $\alpha$, and $\kappa$. In Theorem 7, we prove the linear convergence of Algorithm 2 for all choices $\alpha \in {}$ and $\rho = {{({\hat{m}\hat{L}})}^{\frac{1}{2}}\kappa^{\varepsilon}}$, with $\varepsilon \in {({- \infty},\infty)}$. This result generalizes a number of results in the literature.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Symbolic Rates for Various $\\rho$ and $\\alpha$", "weight": 1.0} -->

As two examples, Giselsson & Boyd consider the case $\varepsilon = 0$ and Deng & Yin consider the case $\alpha = 1$ and $\varepsilon = 0.5$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Symbolic Rates for Various $\\rho$ and $\\alpha$", "weight": 1.0} -->

The rate given in Theorem 7 is loose by a factor of four relative to the lower bound given in Theorem 8. However, weakening the rate by a constant factor eases the proof by making it easier to find a certificate for use.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Lower Bounds", "weight": 1.0} -->

In this section, we probe the tightness of the upper bounds on the convergence rate of Algorithm 2 given by Theorem 6. The construction of the lower bound in this section is similar to a construction given in Ghadimi et al..

<!-- chunk {"id": "body-0023", "role": "body", "section": "Lower Bounds", "weight": 1.0} -->

Let $Q$ be a $d$-dimensional symmetric positive-definite matrix whose largest and smallest eigenvalues are $L$ and $m$ respectively. Let ${f{(x)}} = {\frac{1}{2}x^{\top}Qx}$ be a quadratic and let ${g{(z)}} = {\frac{\delta}{2}{\| z\|}^{2}}$ for some $\delta \geq 0$. Let $A = I_{d}$, $B = {- I_{d}}$, and $c = 0$. With these definitions, the optimization problem in is solved by $x = z = 0$. The updates for Algorithm 2 are given by

<!-- chunk {"id": "body-0024", "role": "body", "section": "Lower Bounds", "weight": 1.0} -->

Solving for $z_{k}$ in (13b) and substituting the result into (13c) gives $u_{k + 1} = {\frac{\delta}{\rho}z_{k + 1}}$. Then eliminating $x_{k + 1}$ and $u_{k}$ from (13b) using (13a) and the fact that $u_{k} = {\frac{\delta}{\rho}z_{k}}$ allows us to express the update rule purely in terms of $z$ as

<!-- chunk {"id": "body-0025", "role": "body", "section": "Lower Bounds", "weight": 1.0} -->

Note that the eigenvalues of $T$ are given by

<!-- chunk {"id": "body-0026", "role": "body", "section": "Lower Bounds", "weight": 1.0} -->

where $\lambda$ is an eigenvalue of $Q$. We will use this setup to construct a lower bound on the worst-case convergence rate of Algorithm 2 in Theorem 8.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Selecting Algorithm Parameters", "weight": 1.0} -->

In this section, we show how to use the results of Section 4 to select the parameters $\alpha$ and $\rho$ in Algorithm 2 and we show the effect on a numerical example.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Selecting Algorithm Parameters", "weight": 1.0} -->

Recall that given a choice of parameters $\alpha$ and $\rho$ and given the condition number $\kappa$, Theorem 6 gives an upper bound on the convergence rate of Algorithm 2. Therefore, one approach to parameter selection is to do a grid search over the space of parameters for the choice that minimizes the upper bound provided by Theorem 6. We demonstrate this approach numerically for a distributed Lasso problem, but first we demonstrate that the usual range of $$ for the over-relaxation parameter $\alpha$ is too limited, that more choices of $\alpha$ lead to linear convergence. In Figure 4, we plot the largest value of $\alpha$ found through binary search such that is satisfied for some $\tau < 1$ as a function of $\kappa$. Proof techniques in prior work do not extend as easily to values of $\alpha > 2$. In our framework, we simply change some constants in a small semidefinite program.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Distributed Lasso", "weight": 1.0} -->

Following Deng & Yin, we give a numerical demonstration with a distributed Lasso problem of the form

<!-- chunk {"id": "body-0030", "role": "body", "section": "Distributed Lasso", "weight": 1.0} -->

Each $A_{i}$ is a tall matrix with full column rank, and so the first term in the objective will be strongly convex and its gradient will be Lipschitz continuous. As in Deng & Yin, we choose $N = 5$ and $\mu = 0.1$. Each $A_{i}$ is generated by populating a $600 \times 500$ matrix with independent standard normal entries and normalizing the columns. We generate each $b_{i}$ via $b_{i} = {{A_{i}x^{0}} + \varepsilon_{i}}$, where $x^{0}$ is a sparse $500$-dimensional vector with $250$ independent standard normal entries, and $\varepsilon_{i} \sim {\mathcal{N}{(0,{10^{- 3}I})}}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Distributed Lasso", "weight": 1.0} -->

In Figure 5, we compute the upper bounds on the convergence rate given by Theorem 6 for a grid of values of $\alpha$ and $\rho$. Each line corresponds to a fixed choice of $\alpha$, and we plot only a subset of the values of $\alpha$ to keep the plot manageable. We omit points corresponding to parameter values for which the linear matrix inequality in was not feasible for any value of $\tau < 1$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Distributed Lasso", "weight": 1.0} -->

In Figure 6, we run Algorithm 2 for the same values of $\alpha$ and $\rho$. We then plot the number of iterations needed for $z_{k}$ to reach within $10^{- 6}$ of a precomputed reference solution. We plot lines corresponding to only a subset of the values of $\alpha$ to keep the plot manageable, and we omit points corresponding to parameter values for which Algorithm 2 exceeded $1000$ iterations. For the most part, the performance of Algorithm 2 as a function of $\rho$ closely tracked the performance predicted by the upper bounds in Figure 5. Notably, smaller values of $\alpha$ seem more robust to poor choices of $\rho$. The parameters suggested by our analysis perform close to the best of any parameter choices.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Discussion", "weight": 1.5} -->

We showed that a framework based on semidefinite programming can be used to prove convergence rates for the alternating direction method of multipliers and allows a unified treatment of the algorithm's many variants, which arise through the introduction of additional parameters. We showed how to use this framework for establishing convergence rates, as in Theorem 6 and Theorem 7, and how to use this framework for parameter selection in practice, as in Section 8. The potential uses are numerous. This framework makes it straightforward to propose new algorithmic variants, for example, by introducing new parameters into Algorithm 2 and using Theorem 6 to see if various settings of these new parameters give rise to improved guarantees.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Discussion", "weight": 1.5} -->

In the case that Assumption 3 does not hold, the most likely cause is that we lack the strong convexity of $f$. One approach to handling this is to run Algorithm 2 on the modified function ${f{(x)}} + {\frac{\delta}{2}{\| x\|}^{2}}$. By completing the square in the $x$ update, we see that this amounts to an extremely minor algorithmic modification (it only affects the $x$ update).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Discussion", "weight": 1.5} -->

It should be clear that other operator splitting methods such as Douglas--Rachford splitting and forward-backward splitting can be cast in this framework and analyzed using the tools presented here.
