<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis

Topics include Gradient descent, Stochastic gradients, Robotics, Robustness, Optimization, Control, Learning, Sampling, Policy gradients.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Domain randomization is a simple, effective, and flexible scheme for obtaining robust feedback policies aimed at reducing the sim-to-real gap due to model mismatch. While domain randomization methods have yielded impressive demonstrations in the robotics-learning literature, general and theoretically motivated principles for designing optimization schemes that effectively leverage the randomization are largely unexplored. We address this gap by considering a stochastic policy gradient descent method for the domain randomized linear-quadratic regulator synthesis problem, a situation simple enough to provide theoretical guarantees. In particular, we demonstrate that stochastic gradients obtained by repeatedly sampling new systems at each gradient step converge to global optima with appropriate hyperparameters choices, and yield better controllers with lower variability in the final controllers when compared to approaches that do not resample. Sampling is often a quick and cheap operation, so computing policy gradients with newly sampled systems at each iteration is preferable to evaluating gradients on a fixed set of systems.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Domain randomization (DR) has gained wide adoption in reinforcement learning and robot learning for enabling sim-to-real transfer. By harnessing massive GPU parallelism, DR trains controllers across randomized environments to robustify controllers against model uncertainty by minimizing expected cost over a sampled uncertainty distribution. In contrast, control theoretic approaches typically handle uncertainty via robust control, designing for the worst case over the uncertainty set. While the robust control methods come with theoretical guarantees that are largely absent in DR, robust control methods frequently suffer from over-conservatism due to their pessimistic formulation. DR trades these theoretical guarantees for straightforward implementation and effective use of GPU computing resources, which are major contributor to DR's practical success.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

An intermediate formulation between DR and robust control, introduced by Fujinami et al., is the domain‑randomized linear‑quadratic regulator (DR‑LQR), which retains DR's ease of implementation while adding stability guarantees. The only missing benefit of DR in Fujinami et al. is the effective utilization of available compute resources, which we address in our work. While Fujinami et al. can scale their policy gradient method with available GPU compute, their approach is inherently limited by the surrogate cost function employed instead of the DR cost function, which we directly optimize with stochastic gradient descent (SGD) methods.

<!-- chunk {"id": "body-0005", "role": "body", "section": "I-A Related Work: LQR Policy Gradient Methods", "weight": 1.0} -->

The seminal work in applying policy gradient methods to LQR synthesis is Fazel et al., which established that the policy gradient satisfies a gradient-domination condition that can find global optimal solutions to (LQR) synthesis problem despite nonconvexity in the cost-function and feasible set. This has been greatly refined and extended over the past decade; many other optimal control synthesis problems also support globally convergent policy optimization, notably $H_{2}/H_{\infty}$ and $H_{\infty}$ control synthesis, Markov jump linear system control synthesis, and even to the reinforcement learning settings. Despite the impact of Fazel et al. in the control-literature, many extensions to LQR-synthesis problems possess convex-optimization formulations so policy-gradient methods are not the only techniques that can produce optimal controllers. A notable exception is that of the domain randomized LQR (DR-LQR) problem where Fujinami et al. show that gradient descent applied to a surrogate sample-average cost converges to a nearly optimal controller.

<!-- chunk {"id": "body-0006", "role": "body", "section": "I-A Related Work: LQR Policy Gradient Methods", "weight": 1.0} -->

In contrast, we show that an optimal controller can be found by applying stochastic gradient descent directly to the DR-LQR objective.

<!-- chunk {"id": "body-0007", "role": "body", "section": "I-B Related Work: Domain Randomization", "weight": 1.0} -->

Domain randomization, popularized in the reinforcement learning and robotics literature, randomizes simulator parameters towards reducing the sim-to-real gap. While the parameters chosen for randomization are highly task dependent, tasks employing dynamics simulations typically vary physical constants like masses, geometries, or scaling factors. Similarly, when vision is an important component for solving the task at hand, randomization is typically employed over features like textures, lighting, or field-of-view of the vision system. This randomization is typically employed by sampling new parameters at each training episode, as opposed to fixed at the outset as in predecessors to DR, like the scenario-approach from robust control or ensemble randomization techniques from robot learning. This ability to sample and roll out randomized environments in parallel is a key factor in the success of domain randomization: we show how this capability can be leveraged to efficiently compute an optimal DR-LQR controller.

<!-- chunk {"id": "body-0008", "role": "body", "section": "I-C Main Contributions", "weight": 1.0} -->

Stochastic Policy Gradient Convergence: We establish the first proof of linear convergence of minibatched SGD to a $\varepsilon$-suboptimal solution of the DR-LQR problem. We further characterize sufficient conditions on the amount of samples a minibatch should containas a function of this suboptimality level.

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-C Main Contributions", "weight": 1.0} -->

Computational Advantage: We empirically show that, for a fixed computational budget, solving the DR-LQR problem via SGD yields a policy that outperforms a controller obtained from the surrogate sample-average formulation of.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Description", "weight": 1.0} -->

where $w_{t} \sim {\mathcal{N}{(0,\Sigma_{w})}}$ and we assume that $\Sigma_{w} \succeq I$. For fixed system parameters, $\theta:={\lbrack A,B\rbrack}$ the infinite-horizon stochastic LQR cost is given,

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Description", "weight": 1.0} -->

where $P{(K,\theta)}$ is the cost-to-go matrix and satisfies,

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Description", "weight": 1.0} -->

Further, the superscript $K$ indicates that the expectation is taken under the closed-loop policy $u_{t} = {- {Kx_{t}}}$ with respect to the noise process $w_{t}$. We also assume that the quadratic cost parameter $\mathcal{Q} ≔ \begin{bmatrix}
\end{bmatrix}$ satisfies $\mathcal{Q} \succeq I$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Description", "weight": 1.0} -->

Solving problem (DR-LQR) is challenging because both the objective and constraint set is nonconvex, and neither the objective nor its gradient can be exactly computed. Nevertheless, we show that we can solve (DR-LQR) via the minibatched SGD scheme in Algorithm 1. In § III, we first show that despite the nonconvexity of the underlying problem, gradient descent converges to a global optimum as the objective function enjoys a *gradient dominance* property. In § IV, we then show that stochastic gradient descent implemented with approximate gradients estimated via minibatch sampling also converge to a globally optimal solution, albeit at a degraded rate.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Description", "weight": 1.0} -->

1: Input: System Probability Distribution pΘ (⋅), Minibatch Size M, Step-Size, η, Number of Gradient Steps t, Starting Point K0
5: Sample M systems from pΘ

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Description", "weight": 1.0} -->

Algorithm 1 DR Minibatched Stochastic Gradient Descent

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Description", "weight": 1.0} -->

Proofs of all intermediate results, as well as exact expressions for constants and polynomials appearing in the sequel can be found in the appendix of our extended version available.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Convergence Analysis of Gradient Descent for DR-LQR", "weight": 1.0} -->

We begin with the idealized setting in which the exact gradient ${\nabla J_{DR}}{(K)}$ of the DR-LQR objective is available. Even in this case, establishing convergence of gradient descent to a global optimum is nontrivial since the DR-LQR cost function is nonconvex in the feedback gain $K$. This difficulty already arises in the LQR problem parameterized by the control policy, where global convergence of policy gradient methods is shown by exploiting a *gradient dominance property* and suitable smoothness conditions. In particular, in addition to establishing gradience dominance, smoothness is needed to ensure that each update

<!-- chunk {"id": "body-0018", "role": "body", "section": "Convergence Analysis of Gradient Descent for DR-LQR", "weight": 1.0} -->

remains *stabilizing*, i.e., in the feasible set of gains.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Convergence Analysis of Gradient Descent for DR-LQR", "weight": 1.0} -->

In the standard LQR setting, Hu et al. address this challenge through a modified smoothness argument: by restricting attention to line segments between feasible policies, they establish a form of local smoothness that guarantees cost decrease under an appropriately chosen step size. Here, we extend this reasoning to the DR-LQR setting by showing that the DR-LQR cost function is coercive, $L$-smooth (i.e., has $L$-Lipschitz gradients) on any sublevel set, and satisfies a (local) gradient dominance property near the optimal solution. To show convergence, we also assume that an initial controller $K_{0}$ is available which simultaneously stabilizes all systems in $\Theta$, i.e, that $K_{0} \in \mathcal{K}_{\Theta}:={\{ K:{{\sup_{\theta \in \Theta}{J{(K,\theta)}}} < \infty}\}}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A DR-LQR Cost is Coercive", "weight": 1.0} -->

We note that for any $\theta \in \Theta$, the LQR cost $J{(K,\theta)}$ is coercive over any sub-level set $\{ K:{{J{(K,\theta)}} \leq c}\}$ for $c < \infty$ \[19, Lemma 3.7\]. A minor modification of Lemma 3.7 in shows that $J{(K,\theta)}$ satisfies the uniform in $\theta$ quadratic lower bound ${J{(K,\theta)}} \geq {\lambda_{\min}{(\Sigma_{w})}{\| K\|}_{F}^{2}}$. Taking expectations of both sides then allows us to conclude coercivity of the DR-LQR cost ${J_{DR}{(K)}}.$

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-B DR-LQR Cost is Locally L-Smooth", "weight": 1.0} -->

The cost $J_{DR}{(K)}$ is not globally $L$-smooth because for any fixed $\theta \in \Theta$, the cost $J{(K,\theta)}$ rapidly becomes infinite at the boundary between stable and unstable controllers, violating traditional smoothness conditions: hence we do not expect the DR-LQR cost $J_{DR}{(K)}$ to satisfy global smoothness either. Instead, we fix a performance level $c > o$, and show that within $c$-sublevel sets ${S_{c} ≔ {\{ K:{{J_{DR}{(K)}} \leq c}\}}},$ local smoothness can be established.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-C Gradient Dominance of DR-LQR Cost", "weight": 1.0} -->

Fujinami et al. show that a sample average surrogate of the DR-LQR cost enjoys gradient dominance in a neighborhood of the optimal policy under suitable heterogeneity assumptions, as captured by ${diam}{(\Theta)}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-C Gradient Dominance of DR-LQR Cost", "weight": 1.0} -->

We show here that this argument can be extended to the true DR-LQR cost function $J_{DR}{(K)}$ under analogous assumptions. Our strategy is to first show that the DR-LQR cost satisfies an approximate gradient dominance property, then argue that this guarantees gradient dominance in a suitable neighborhood of the optimal controller $K^{\star}.$

<!-- chunk {"id": "body-0024", "role": "body", "section": "Convergence Analysis of SGD for DR-LQR", "weight": 1.0} -->

This section provides an end-to-end convergence analysis for the minibatch SGD procedure in Algorithm 1, where the primary goal is find hyperparameters guaranteeing a $\varepsilon$-suboptimal solution with probability at least $1 - \delta$. This requires explicit characterization of a minibatch size $M$, step size $\eta$, and number of descent steps, $N$. The main technical challenge is the potential for infeasibility arising from gradient approximation. While we know from Proposition 1. ‣ III-B DR-LQR Cost is Locally L-Smooth ‣ III Convergence Analysis of Gradient Descent for DR-LQR ‣ On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis") that gradient steps maintain feasibility, it is possible for approximate gradient steps to fail to maintain feasibility due to gradient-approximation errors.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-A SGD Analysis Setup", "weight": 1.0} -->

Throughout this section we assume that $J_{DR}{(K)}$, is $L_{K}$-smooth on its sublevel-sets as previously established in Section III, and $\mu$-gradient dominated on $\mathcal{S}$ (as in Proposition 2), and on a fixed sublevel set $S_{c}$. Further, we define, the minibatch gradient $g{(K)}$, exact gradient step $K^{gd}$, and stochastic gradient step $K^{sgd}$ as

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-A SGD Analysis Setup", "weight": 1.0} -->

To analyze how accurately $g{(K)}$ must estimate the gradients, it is helpful to interpret the stochastic gradient update as a perturbation to the gradient update,

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-A SGD Analysis Setup", "weight": 1.0} -->

Employing this with known feasibility guarantees on $J{(K,\theta)}$, like the ones in Fazel et al., allows us to derive similar guarantees for $J_{DR}{(K)}$. We condense and summarize the contents of lemma 22 through 27, relegating its proof to the appendix.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-B One-Step Decomposition", "weight": 1.0} -->

To analyze the iterates obtained by SGD eq. MB-SGD, we first decompose the cost at each iteration into an exact gradient update step perturbed by an error due to sampling.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-C Concentration of minibatched-gradient estimators", "weight": 1.0} -->

for some choice of gradient estimation error $\varepsilon_{\nabla}$. We achieve this by invoking the Matrix Bernstein inequalities, which require that we find norm and variance bounds on (MB-G). This can be achieved by defining the zero-mean symmetrized matrix,

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-C Concentration of minibatched-gradient estimators", "weight": 1.0} -->

that we will bound with the rectangular matrix Bernstein inequality, found in Vershynin \[20, Exercise 5.4.15\], adapted to the task at hand. Bounds on the support norm $\overline{G}$ and variance proxy $\sigma^{2}$ as expressions in the problem constants are characterized in our appendix. Essentially, we employ the mean-value theorem to obtain these in terms of problem specific parameters and ${diam}{(\Theta)}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-D Convergence of Stochastic Gradient Descent", "weight": 1.0} -->

Finally, we have all of the expressions needed to find an explicit set of hyperparameters to make algorithm 1 converge to an $\varepsilon$-suboptimal policy, expressed solely in terms of the problem specifications.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We demonstrate that we can solve the DR-LQR problem defined in equation (DR-LQR) in practice with minibatched SGD. In our experiments, we consider stabilizing a cart-pole system linearized by automatic differentiation and discretized using the matched transformation. For our randomization domain, $\Theta$, we randomize pendulum lengths that we assume come from a uniform distribution supported on ${\lbrack 0.2,0.8\rbrack}m$, a cart mass of $1$kg, a pendulum mass of 1kg, a track-cart coefficient of friction $0.25$, and a pendulum joint friction ${0.01N} \cdot m$. To generate our figures, we plot data from 1000 independent trials, with step-size $\eta = {5 \times 10^{- 8}}$ and number of gradient steps $t = 10000$. We do not use Theorem 2.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

‣ IV-D Convergence of Stochastic Gradient Descent ‣ IV Convergence Analysis of SGD for DR-LQR ‣ On Globally Optimal Stochastic Policy Gradient Methods for Domain Randomized LQR Synthesis") directly to find $M$, $N$ or $\eta$, instead finding them empirically by hyperparameter tuning. Our conservative step size was tuned specifically to ensure convergence on all batch sizes for equal comparisons of optimizer progress versus number of gradient steps. All other implementation details will be relegated to the appendix.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We also compare this to the sample-averaged (SA) approximation to the DR cost, which first fixes $M = 8$ systems to form a surrogate cost function to optimize with as. This is illustrates the case of limited memory, where the optimizer employed only has enough memory to store $M$ systems, where differences between DR and SA are more substantial. We observe that the controllers found by DR achieve lower costs, and have lower variability compared to their SA counterparts in the sense that the $25^{th}$ and $75^{th}$ percentiles are closer together. Further, the right-figure plotting the $\ell_{2}$ norm of the eventual controller shows that in the parameter space, there is substantially lower variation in controllers found by DR when compared to SA. Finally, we emphasize that while the stochasticity in the DR cost in 1 (center) suggest that the controllers synthesized by DR can vary significantly in cost, this stems from the DR cost approximation, not from inconsistency in the final converged controller.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In our experiments, the SA optimization procedure of Fujinami et al. takes 33.1 s (on average) to synthesize a controller for a fixed set of $M = 8$ systems, while the DR optimization routine takes 40.5 s (on average) to run on a Nvidia A100 GPU. For a modest 22% increase in runtime, we obtain controllers with lower DR cost and lower ${\| K\|}_{2}$ variance. This demonstrates a clear and practical advantage of the DR formulation; for a marginal increase in computational effort, the algorithm produces controllers that are not only higher-performing but, critically, are also substantially more reliable and consistent.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

We have studied a stochastic policy gradient method for the domain randomized linear-quadratic regulator problem. We showed that repeatedly sampling new systems at each gradient step led to convergence to global optima under appropriate hyperparameter choices. Compared to approaches that rely on a fixed set of systems, our method produced better controllers with lower variability in the final performance. Since sampling is often computationally inexpensive, evaluating gradients on freshly sampled systems proves to be more effective than using a static collection.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Conclusions and Future Work", "weight": 1.0} -->

Our future directions are primarily targeted as loosening the heterogeneity conditions employed to establish gradient-dominance, as the ones employed here are very restrictive. Further, we also believe it is possible to strengthen our methods to yield globally convergent SGD instead of just $\varepsilon$-suboptimality. As this is the case in analyses of SGD under conditions of gradient dominance, we suspect that the extension to settings with nonconvex feasible sets in accessible with the tools developed here and more broadly in the optimization literature.
