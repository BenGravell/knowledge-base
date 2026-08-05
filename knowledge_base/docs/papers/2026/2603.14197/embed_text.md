<!-- arxiv-full-text:v1 {"arxiv_id": "2603.14197", "source": "arxiv-html"} -->

## Introduction

Domain randomization (DR) has gained wide adoption in reinforcement learning and robot learning for enabling sim-to-real transfer. By harnessing massive GPU parallelism, DR trains controllers across randomized environments to robustify controllers against model uncertainty by minimizing expected cost over a sampled uncertainty distribution. In contrast, control theoretic approaches typically handle uncertainty via robust control, designing for the worst case over the uncertainty set. While the robust control methods come with theoretical guarantees that are largely absent in DR, robust control methods frequently suffer from over-conservatism due to their pessimistic formulation. DR trades these theoretical guarantees for straightforward implementation and effective use of GPU computing resources, which are major contributor to DR's practical success.

An intermediate formulation between DR and robust control, introduced by Fujinami et al., is the domain‑randomized linear‑quadratic regulator (DR‑LQR), which retains DR's ease of implementation while adding stability guarantees. The only missing benefit of DR in Fujinami et al. is the effective utilization of available compute resources, which we address in our work. While Fujinami et al. can scale their policy gradient method with available GPU compute, their approach is inherently limited by the surrogate cost function employed instead of the DR cost function, which we directly optimize with stochastic gradient descent (SGD) methods.

### I-A Related Work: LQR Policy Gradient Methods

The seminal work in applying policy gradient methods to LQR synthesis is Fazel et al., which established that the policy gradient satisfies a gradient-domination condition that can find global optimal solutions to (LQR) synthesis problem despite nonconvexity in the cost-function and feasible set. This has been greatly refined and extended over the past decade; many other optimal control synthesis problems also support globally convergent policy optimization, notably $H_{2}/H_{\infty}$ and $H_{\infty}$ control synthesis, Markov jump linear system control synthesis, and even to the reinforcement learning settings. Despite the impact of Fazel et al. in the control-literature, many extensions to LQR-synthesis problems possess convex-optimization formulations so policy-gradient methods are not the only techniques that can produce optimal controllers. A notable exception is that of the domain randomized LQR (DR-LQR) problem where Fujinami et al. show that gradient descent applied to a surrogate sample-average cost converges to a nearly optimal controller. In contrast, we show that an optimal controller can be found by applying stochastic gradient descent directly to the DR-LQR objective.

### I-B Related Work: Domain Randomization

Domain randomization, popularized in the reinforcement learning and robotics literature, randomizes simulator parameters towards reducing the sim-to-real gap. While the parameters chosen for randomization are highly task dependent, tasks employing dynamics simulations typically vary physical constants like masses, geometries, or scaling factors. Similarly, when vision is an important component for solving the task at hand, randomization is typically employed over features like textures, lighting, or field-of-view of the vision system. This randomization is typically employed by sampling new parameters at each training episode, as opposed to fixed at the outset as in predecessors to DR, like the scenario-approach from robust control or ensemble randomization techniques from robot learning. This ability to sample and roll out randomized environments in parallel is a key factor in the success of domain randomization: we show how this capability can be leveraged to efficiently compute an optimal DR-LQR controller.

### I-C Main Contributions

Stochastic Policy Gradient Convergence: We establish the first proof of linear convergence of minibatched SGD to a $\varepsilon$-suboptimal solution of the DR-LQR problem. We further characterize sufficient conditions on the amount of samples a minibatch should containas a function of this suboptimality level.

Computational Advantage: We empirically show that, for a fixed computational budget, solving the DR-LQR problem via SGD yields a policy that outperforms a controller obtained from the surrogate sample-average formulation of.

## Problem Description

Consider a fully observed linear dynamical system, with state $x_{t}\in\mathbb{R}^{n_{x}}$, input $u_{t}\in\mathbb{R}^{n_{u}}$, and noise $w_{t}\in\mathbb{R}^{n_{x}}$. The system evolves as where $w_{t}\sim\mathcal{N}(0,\Sigma_{w})$ and we assume that $\Sigma_{w}\succeq I$. For fixed system parameters, $\theta:=[A,B]$ the infinite-horizon stochastic LQR cost is given, where $P(K,\theta)$ is the cost-to-go matrix and satisfies, Further, the superscript $K$ indicates that the expectation is taken under the closed-loop policy $u_{t}=-Kx_{t}$ with respect to the noise process $w_{t}$. We also assume that the quadratic cost parameter $\mathcal{Q}\coloneqq\begin{bmatrix}Q&S\\S^{\top}&R\end{bmatrix}$ satisfies $\mathcal{Q}\succeq I$.

We model the system parameters $\theta$ as random variables supported on a convex and compact set $\Theta$ with density $p_{\Theta}$, and define the *domain randomized linear-quadratic-regulator* (DR-LQR) synthesis problem as seeking a feedback gain $K$ which minimizes the expecation of the LQR cost with respect to the system parameters: We define $J_{DR}(K):=\mathbb{E}_{\theta}[J(K,\theta)]$ and drop the expecation subscript, as all expectations will be with respect to $\theta$, i.e., $J_{DR}(K)=\mathbb{E}[J(K,\theta)]$.

Solving problem (DR-LQR) is challenging because both the objective and constraint set is nonconvex, and neither the objective nor its gradient can be exactly computed. Nevertheless, we show that we can solve (DR-LQR) via the minibatched SGD scheme in Algorithm 1. In § III, we first show that despite the nonconvexity of the underlying problem, gradient descent converges to a global optimum as the objective function enjoys a *gradient dominance* property. In § IV, we then show that stochastic gradient descent implemented with approximate gradients estimated via minibatch sampling also converge to a globally optimal solution, albeit at a degraded rate.

1: Input: System Probability Distribution pΘ(⋅), Minibatch Size M, Step-Size, η, Number of Gradient Steps t, Starting Point K0 5: Sample M systems from pΘ 6: Compute the minibatched gradients $$g(K)\leftarrow\frac{1}{M}\sum_{i=1}^{M}\nabla J(K,\theta_{i})$$ 7: Take a minibatched gradient step, Algorithm 1 DR Minibatched Stochastic Gradient Descent Proofs of all intermediate results, as well as exact expressions for constants and polynomials appearing in the sequel can be found in the appendix of our extended version available.

## Convergence Analysis of Gradient Descent for DR-LQR

We begin with the idealized setting in which the exact gradient $\nabla J_{DR}(K)$ of the DR-LQR objective is available. Even in this case, establishing convergence of gradient descent to a global optimum is nontrivial since the DR-LQR cost function is nonconvex in the feedback gain $K$. This difficulty already arises in the LQR problem parameterized by the control policy, where global convergence of policy gradient methods is shown by exploiting a *gradient dominance property* and suitable smoothness conditions. In particular, in addition to establishing gradience dominance, smoothness is needed to ensure that each update remains *stabilizing*, i.e., in the feasible set of gains.

In the standard LQR setting, Hu et al. address this challenge through a modified smoothness argument: by restricting attention to line segments between feasible policies, they establish a form of local smoothness that guarantees cost decrease under an appropriately chosen step size. Here, we extend this reasoning to the DR-LQR setting by showing that the DR-LQR cost function is coercive, $L$-smooth (i.e., has $L$-Lipschitz gradients) on any sublevel set, and satisfies a (local) gradient dominance property near the optimal solution. To show convergence, we also assume that an initial controller $K_{0}$ is available which simultaneously stabilizes all systems in $\Theta$, i.e, that $K_{0}\in\mathcal{K}_{\Theta}:=\{K\,:\,\sup_{\theta\in\Theta}J(K,\theta)<\infty\}$.

### III-A DR-LQR Cost is Coercive

We note that for any $\theta\in\Theta$, the LQR cost $J(K,\theta)$ is coercive over any sub-level set $\{K\,:\,J(K,\theta)\leq c\}$ for $c<\infty$ \[19, Lemma 3.7\]. A minor modification of Lemma 3.7 in shows that $J(K,\theta)$ satisfies the uniform in $\theta$ quadratic lower bound $J(K,\theta)\geq\lambda_{\min}(\Sigma_{w})\|K\|_{F}^{2}$. Taking expectations of both sides then allows us to conclude coercivity of the DR-LQR cost $J_{DR}(K).$

### III-B DR-LQR Cost is Locally L-Smooth

The cost $J_{DR}(K)$ is not globally $L$-smooth because for any fixed $\theta\in\Theta$, the cost $J(K,\theta)$ rapidly becomes infinite at the boundary between stable and unstable controllers, violating traditional smoothness conditions: hence we do not expect the DR-LQR cost $J_{DR}(K)$ to satisfy global smoothness either. Instead, we fix a performance level $c>o$, and show that within $c$-sublevel sets $S_{c}\coloneqq\{K:J_{DR}(K)\leq c\},$ local smoothness can be established.

### Lemma 1 (Policy-Smoothness)

Fix $c>0$. The cost $\mathbb{E}[J(K,\theta)]$ is $L_{K}$-smooth at any $K\in S_{c}$, with $L_{K}$ given by Where the operator norm is given by the maximum singular value. Here, We note that all quantities in eq. 2. ‣ III-B DR-LQR Cost is Locally L-Smooth ‣ III Convergence Analysis of Gradient Descent for DR-LQR ‣ On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis") can be bounded above by polynomials in problem specific parameters and $c$.

### Proof

The Hessian of $J(K,\theta)$ is given in Bu et al.. Employing this Hessian, submultiplicativity, subadditivity, the shorthands introduced, and finally noting that, by Appendix Corollary 2. ‣ VIII-C Lipschitz, and Gradient Norm/Variance Bounds ‣ VIII Appendix ‣ On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis"), $\|\mathbb{E}[D_{K}^{2}J(K,\theta)]\|_{\text{op}}\leq L_{K}$. ∎ We next show that local $L$-smoothness can be used to select a step-size for gradient descent that ensures that the DR-LQR cost decreases at each iteration. The following is an adaptation of Hu et al. \[9, Theorem 1\] to obtain the following feasibility lemma.

### Proposition 1 (Theorem 1 of Hu et al. )

Let $K_{1},K_{2}\in S_{c}$ be two arbitrary policies in the sublevel set $S_{c}$. Denote by $\mathcal{I}(K_{1},K_{2})=\{\phi K_{1}+(1-\phi)K_{2}:\phi\in\},$ the line segment connecting $K_{1},K_{2}$. If $\mathcal{I}(K_{1},K_{2})\subseteq S_{c}$, then for $L_{K}$ as given in equation (2. ‣ III-B DR-LQR Cost is Locally L-Smooth ‣ III Convergence Analysis of Gradient Descent for DR-LQR ‣ On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis")), we have that We can apply this result to show that if $K_{0}\in S_{c}$, then all future iterates $K_{\ell}$ of gradient descent applied with step-size $\eta=L_{K}^{-1}$ remain in $S_{c}$. In particular, it holds that for any $K\in S_{c}$, the segment $\mathcal{I}(K,K-L_{K}^{-1}\nabla\mathbb{E}[J(K,\theta)])\subseteq S_{c}$, so that by Prop. 1. ‣ III-B DR-LQR Cost is Locally L-Smooth ‣ III Convergence Analysis of Gradient Descent for DR-LQR ‣ On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis"): This is called the *implicit regularization property* by Hu et al., and importantly ensures that all iterates of gradient descent remain in $\mathcal{K}_{\Theta}$ if the initial iterate $K_{0}\in\mathcal{K}_{\Theta}.$

### III-C Gradient Dominance of DR-LQR Cost

Fujinami et al. show that a sample average surrogate of the DR-LQR cost enjoys gradient dominance in a neighborhood of the optimal policy under suitable heterogeneity assumptions, as captured by $\operatorname{diam}(\Theta)$.

We show here that this argument can be extended to the true DR-LQR cost function $J_{DR}(K)$ under analogous assumptions. Our strategy is to first show that the DR-LQR cost satisfies an approximate gradient dominance property, then argue that this guarantees gradient dominance in a suitable neighborhood of the optimal controller $K^{\star}.$

### Lemma 2 (Approximate Gradient-Domination)

Fix $c>0$ and $K\in S_{c}$. Then the following bound holds:

### Proof

This proof is an adapation of Fujinami et al. Lemma III.3. By the almost-smoothness lemma of Fazel et al., combined with the monotonic property of the integrals, we have that: Where $(\cdot)$ is $\operatorname{vec}(K-K^{\star})$; the result follows by employing completion of squares and adding/subtracting $\Sigma(K,\theta)$. ∎ From here, we see that if we can bound the remainder term $R(K,K^{\star})$ by a sufficiently small multiple of $\mathbb{E}[J(K,\theta)-J(K^{\star},\theta)]$, we can ensure gradient domination---this is the approach taken in Lemma III.4 of Fujinami et al.. We do so in the following Lemma, which extends the arguments of \[3, Lemmas III.5-7\] to the DR-LQR cost $J_{DR}$.

### Proposition 2

Let the diameter of the set be bounded above, where $\Theta_{B}$ is the support of $B$. Within the set, Convergence of Gradient Descent: We now have all the ingredients needed to prove convergence of gradient descent to an optimal solution to problem (DR-LQR) assuming an initial stabilizing controller $K_{0}\in\mathcal{K}_{\Theta}\cap S$.^11^1We show in the appendix that under gradient dominance, a slight modification of the discounted-annealing scheme proposed in Fujinami et al. enables one to find such an initial controller $K_{0}\in\mathcal{K}_{\Theta}\cap\mathcal{S}$.

### Theorem 1 (Linear Convergence)

Let $K_{0}\in\mathcal{K}_{\Theta}\cap\mathcal{S}$, set $\eta\leq L_{K}^{-1}$, and consider the gradient descent iterates Then, the following are true: For all $\ell=0,1,2,...$, we have that $K_{\ell}\in\mathcal{K}_{\Theta}\cap S.$ The iterates satisfy gradient descent steps, we achieve suboptimality,

### Proof

The result follows by \[9, Theorem 1\]. In particular, we have proved that for any $K\in\mathcal{K}_{\Theta}\cap S$, the DR-LQR cost $J_{DR}(K)$ is coercive and is $L_{K}$-smooth (Lem. 1. ‣ III-B DR-LQR Cost is Locally L-Smooth ‣ III Convergence Analysis of Gradient Descent for DR-LQR ‣ On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis")). Further note that if $K_{0}\in\mathcal{K}_{\Theta}\cap S$ then all future iterates $K_{\ell}$ also belong to the set $\mathcal{K}_{\Theta}\cap S$ follows from the descent guarantee following Prop. 1. ‣ III-B DR-LQR Cost is Locally L-Smooth ‣ III Convergence Analysis of Gradient Descent for DR-LQR ‣ On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis") and the definition of $\mathcal{S}$, as gradient norms of iterates are bounded by a monotonically decreasing function. Finally, as the DR-LQR cost function satisfies a gradient dominance property of degree 2 with parameter $\mu=\frac{1}{8}$, the linear convergence rate (4. ‣ III-C Gradient Dominance of DR-LQR Cost: ‣ III Convergence Analysis of Gradient Descent for DR-LQR ‣ On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis")) is guaranteed. ∎

## Convergence Analysis of SGD for DR-LQR

This section provides an end-to-end convergence analysis for the minibatch SGD procedure in Algorithm 1, where the primary goal is find hyperparameters guaranteeing a $\varepsilon$-suboptimal solution with probability at least $1-\delta$. This requires explicit characterization of a minibatch size $M$, step size $\eta$, and number of descent steps, $N$. The main technical challenge is the potential for infeasibility arising from gradient approximation. While we know from Proposition 1. ‣ III-B DR-LQR Cost is Locally L-Smooth ‣ III Convergence Analysis of Gradient Descent for DR-LQR ‣ On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis") that gradient steps maintain feasibility, it is possible for approximate gradient steps to fail to maintain feasibility due to gradient-approximation errors.

### IV-A SGD Analysis Setup

Throughout this section we assume that $J_{DR}(K)$, is $L_{K}$-smooth on its sublevel-sets as previously established in Section III, and $\mu$-gradient dominated on $\mathcal{S}$ (as in Proposition 2), and on a fixed sublevel set $S_{c}$. Further, we define, the minibatch gradient $g(K)$, exact gradient step $K^{\operatorname{gd}}$, and stochastic gradient step $K^{\operatorname{sgd}}$ as This section analyzes the convergence properties of the SGD iterates: To analyze how accurately $g(K)$ must estimate the gradients, it is helpful to interpret the stochastic gradient update as a perturbation to the gradient update, Employing this with known feasibility guarantees on $J(K,\theta)$, like the ones in Fazel et al., allows us to derive similar guarantees for $J_{DR}(K)$. We condense and summarize the contents of lemma 22 through 27, relegating its proof to the appendix.

### Proposition 3 (DR Feasible Step Size)

Consider any $K$ belonging to a sublevel set $S_{c}$ of $J_{DR}$. If Furthermore, the entire line segment, $\mathcal{I}(K,K^{\operatorname{sgd}})$ is feasible.

The derivations of the constant $c_{g}$ and $L_{cost}$, follow by application of matrix calculus identities are provided in the appendix of the extended version of this work. Proposition 3. ‣ IV-A SGD Analysis Setup ‣ IV Convergence Analysis of SGD for DR-LQR ‣ On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis") ensures that we possess enough smoothness for gradient descent to be tunable and yield feasible iterates, a key step in invoking gradient-domination bounds.

### IV-B One-Step Decomposition

To analyze the iterates obtained by SGD eq. MB-SGD, we first decompose the cost at each iteration into an exact gradient update step perturbed by an error due to sampling.

### Lemma 3 (Cost Decomposition, Thm. 31)

Assume that $\|K^{\operatorname{gd}}-K^{\operatorname{sgd}}\|$ satisfies Proposition 3. ‣ IV-A SGD Analysis Setup ‣ IV Convergence Analysis of SGD for DR-LQR ‣ On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis"). The cost difference can be bounded above ,

### Proof

By Proposition 1. ‣ III-B DR-LQR Cost is Locally L-Smooth ‣ III Convergence Analysis of Gradient Descent for DR-LQR ‣ On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis"), we have that $K^{\mathrm{gd}}$ is feasible, and thus satisfies: Adding and subtracting $J_{DR}(K^{\operatorname{sgd}})$ to the left-hand side, rearranging the terms, and applying Proposition 3. ‣ IV-A SGD Analysis Setup ‣ IV Convergence Analysis of SGD for DR-LQR ‣ On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis") yields the result. ∎ This one-step decomposition reveals the terms that need to be controlled to establish convergence of SGD. In the upper bound of eq. 6. ‣ IV-B One-Step Decomposition ‣ IV Convergence Analysis of SGD for DR-LQR ‣ On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis"), we have a contraction term of eq. 4. ‣ III-C Gradient Dominance of DR-LQR Cost: ‣ III Convergence Analysis of Gradient Descent for DR-LQR ‣ On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis"), perturbed by an error term due to gradient approximation. We use a sufficient condition for descent adapted from Fazel et al., which accounts for the error as a contraction rate degradation.

### Lemma 4 (Degraded Contraction)

Fix a desired suboptimality $\varepsilon$. For $\ell\in\{0,\ldots,N-1\}$, if we have we obtain the degraded contraction rate

### Proof

This follows by an induction, following \[4, Theorem 31\], Lemma 3. ‣ IV-B One-Step Decomposition ‣ IV Convergence Analysis of SGD for DR-LQR ‣ On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis"), and the additional assumptions we make.

### Corollary 1 (Gradient Estimation Error)

If, at each iteration, we have that then we obtain the degraded contraction rate of Lemma 4. ‣ IV-B One-Step Decomposition ‣ IV Convergence Analysis of SGD for DR-LQR ‣ On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis").

A direct consequence of Corollary 1. ‣ Proof. ‣ Lemma 4 (Degraded Contraction). ‣ IV-B One-Step Decomposition ‣ IV Convergence Analysis of SGD for DR-LQR ‣ On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis"), is a link between allowable gradient estimation errors to and the corresponding policy errors. We can arrive at an expression for the required accuracy of the minibatch gradients to remain feasible, and yield a degraded linear convergence rate. All of these quantities can be expressed in terms of problem specific constants. Finally, we address the issue of minibatch-gradient concentration.

### IV-C Concentration of minibatched-gradient estimators

We start by denoting the gradient estimation error by $\varepsilon_{\nabla}$, where we would like to ensure that: for some choice of gradient estimation error $\varepsilon_{\nabla}$. We achieve this by invoking the Matrix Bernstein inequalities, which require that we find norm and variance bounds on (MB-G). This can be achieved by defining the zero-mean symmetrized matrix, that we will bound with the rectangular matrix Bernstein inequality, found in Vershynin \[20, Exercise 5.4.15\], adapted to the task at hand. Bounds on the support norm $\bar{G}$ and variance proxy $\sigma^{2}$ as expressions in the problem constants are characterized in our appendix. Essentially, we employ the mean-value theorem to obtain these in terms of problem specific parameters and $\operatorname{diam}(\Theta)$.

Figure 1: All figures are generated with 1000 independent trials with 10000 gradient steps. Left: We plot the median and the 25% and 75% percentiles for 1000 independent trials of optimizing the domain randomization cost with varying minibatch size. To approximate the DR-cost we employ the sample average estimator, $J_{DR}(K)\approx\frac{1}{n_{\text{dr}}}\sum_{i=1}^{n_{\text{dr}}}J(K,\theta_{i})$ with a large amount of samples (ndr = 105) used to visualize the descent dynamics of the DR-cost. Center: We provide a zoomed in figure for the descent dynamics of the SA synthesized controller of and the DR synthesized controller by algorithm 1 in this work with M = 8 for both optimization procedures, as well as the 25% and 75% percentiles of the cost trajectories. Right: We plot the empirical distribution (on a logarithmic scale) of the ℓ2 norm of the final obtained controller to illustrate the reduced variance in the controller synthesized by DR versus SA.

### Lemma 5 (Matrix Bernstein Inequality)

Let $G_{i}$ be defined as, and assume that, with probability at least $1-\delta$, each gradient-estimation error is bounded above by $\varepsilon_{\nabla}$.

### Proof

The matrix Bernstein inequality we use is expressed as a Frobenius norm; the conversion and expression in problem dependent constants is covered in Appendix Lemma 10. ‣ VIII-C Lipschitz, and Gradient Norm/Variance Bounds ‣ VIII Appendix ‣ On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis").

### IV-D Convergence of Stochastic Gradient Descent

Finally, we have all of the expressions needed to find an explicit set of hyperparameters to make algorithm 1 converge to an $\varepsilon$-suboptimal policy, expressed solely in terms of the problem specifications.

### Theorem 2 (High-Probability Convergence of Minibatch SGD)

Consider (DR-LQR) problem where the conditions of Proposition 2 are satisfied. Then, we have that $J_{DR}(K)$ is $\mu$-gradient dominated with $\mu=1/8$ and with access to a feasible starting controller $K_{0}\in\mathcal{S}$. Pick a desired suboptimality, $\varepsilon$ and failure probability $\delta$. If we run algorithm 1: then, with probability at least $1-\delta$ over the randomness of the minibatch sampling, Where all constants depend only on $\mu$, $K_{0}$, $\mathcal{Q}$, $\Sigma_{w}$, $n_{x}$, $n_{u}$, $\operatorname{diam}(\Theta)$, $\|\bar{\theta}\|$, $\varepsilon$, and $\delta$.

### Proof

We already have expressions for the step size and the number of iterations, (that can also account for the degraded contraction rate) from eq. 2. ‣ III-B DR-LQR Cost is Locally L-Smooth ‣ III Convergence Analysis of Gradient Descent for DR-LQR ‣ On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis") and eq. 5. ‣ III-C Gradient Dominance of DR-LQR Cost: ‣ III Convergence Analysis of Gradient Descent for DR-LQR ‣ On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis"),where we use the degraded contraction rate of Lemma 4. ‣ IV-B One-Step Decomposition ‣ IV Convergence Analysis of SGD for DR-LQR ‣ On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis"). However, to find a minibatch size, we need to ensure that all $N$ iterations to succeed. If we specify a probability of success $\delta$, and set the failure probability at each stage to be $\delta/N$, then $M$ is given by Lemma 5. ‣ IV-C Concentration of minibatched-gradient estimators ‣ IV Convergence Analysis of SGD for DR-LQR ‣ On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis"). Finally, to find $\varepsilon_{\nabla},\bar{G},\sigma^{2}$, we employ Corollary 1. ‣ Proof. ‣ Lemma 4 (Degraded Contraction). ‣ IV-B One-Step Decomposition ‣ IV Convergence Analysis of SGD for DR-LQR ‣ On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis") and Lemma 3. ‣ IV-B One-Step Decomposition ‣ IV Convergence Analysis of SGD for DR-LQR ‣ On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis") to express $\varepsilon_{\nabla}$ in terms of problem dependent parameters and a starting point, and Lemma 10. ‣ VIII-C Lipschitz, and Gradient Norm/Variance Bounds ‣ VIII Appendix ‣ On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis") to express $\bar{G}$ and $\sigma^{2}$ in terms of in terms of problem dependent parameters and a starting point. ∎ We emphasize that with this batch size $M$, the intermediate iterates are also feasible with high-probability, and that Algorithm 1 with parameters prescribed by Theorem 2. ‣ IV-D Convergence of Stochastic Gradient Descent ‣ IV Convergence Analysis of SGD for DR-LQR ‣ On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis") only yields a $\varepsilon$-suboptimal controller, but taking any additional steps is not guaranteed to yield any further progress. Refinements with step size tunings that yield globally convergent SGD we leave for future work.

## Numerical Experiments

We demonstrate that we can solve the DR-LQR problem defined in equation (DR-LQR) in practice with minibatched SGD. In our experiments, we consider stabilizing a cart-pole system linearized by automatic differentiation and discretized using the matched transformation. For our randomization domain, $\Theta$, we randomize pendulum lengths that we assume come from a uniform distribution supported on $[0.2,0.8]\,\mathrm{m}$, a cart mass of $1$kg, a pendulum mass of 1kg, a track-cart coefficient of friction $0.25$, and a pendulum joint friction $0.01\,\mathrm{N}\cdot m$. To generate our figures, we plot data from 1000 independent trials, with step-size $\eta=5\times 10^{-8}$ and number of gradient steps $t=10000$. We do not use Theorem 2. ‣ IV-D Convergence of Stochastic Gradient Descent ‣ IV Convergence Analysis of SGD for DR-LQR ‣ On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis") directly to find $M$, $N$ or $\eta$, instead finding them empirically by hyperparameter tuning. Our conservative step size was tuned specifically to ensure convergence on all batch sizes for equal comparisons of optimizer progress versus number of gradient steps. All other implementation details will be relegated to the appendix.

Figure 1 (left) illustrates that that increasing minibatch size leads to more accurate estimates of the gradient which leads to faster convergence of minibatched SGD. Further, more accurate gradients lead to better estimation of the global optima due to the lower gradient error incurred by sampling, as predicted by standard SGD theory and tighter concentration of the minibatch gradient about $\nabla J_{DR}(K)$.

We also compare this to the sample-averaged (SA) approximation to the DR cost, which first fixes $M=8$ systems to form a surrogate cost function to optimize with as . This is illustrates the case of limited memory, where the optimizer employed only has enough memory to store $M$ systems, where differences between DR and SA are more substantial. We observe that the controllers found by DR achieve lower costs, and have lower variability compared to their SA counterparts in the sense that the $25^{\mathrm{th}}$ and $75^{\mathrm{th}}$ percentiles are closer together. Further, the right-figure plotting the $\ell_{2}$ norm of the eventual controller shows that in the parameter space, there is substantially lower variation in controllers found by DR when compared to SA. Finally, we emphasize that while the stochasticity in the DR cost in 1 (center) suggest that the controllers synthesized by DR can vary significantly in cost, this stems from the DR cost approximation, not from inconsistency in the final converged controller.

In our experiments, the SA optimization procedure of Fujinami et al. takes 33.1 s (on average) to synthesize a controller for a fixed set of $M=8$ systems, while the DR optimization routine takes 40.5 s (on average) to run on a Nvidia A100 GPU. For a modest 22% increase in runtime, we obtain controllers with lower DR cost and lower $\|K\|_{2}$ variance. This demonstrates a clear and practical advantage of the DR formulation; for a marginal increase in computational effort, the algorithm produces controllers that are not only higher-performing but, critically, are also substantially more reliable and consistent.

## Conclusions and Future Work

We have studied a stochastic policy gradient method for the domain randomized linear-quadratic regulator problem. We showed that repeatedly sampling new systems at each gradient step led to convergence to global optima under appropriate hyperparameter choices. Compared to approaches that rely on a fixed set of systems, our method produced better controllers with lower variability in the final performance. Since sampling is often computationally inexpensive, evaluating gradients on freshly sampled systems proves to be more effective than using a static collection.

Our future directions are primarily targeted as loosening the heterogeneity conditions employed to establish gradient-dominance, as the ones employed here are very restrictive. Further, we also believe it is possible to strengthen our methods to yield globally convergent SGD instead of just $\varepsilon$-suboptimality. As this is the case in analyses of SGD under conditions of gradient dominance, we suspect that the extension to settings with nonconvex feasible sets in accessible with the tools developed here and more broadly in the optimization literature.
