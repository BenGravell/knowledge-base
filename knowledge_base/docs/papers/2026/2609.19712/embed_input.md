<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

(Cheap) Stochastic Policy Gradient Converges with High Probability for Linear Quadratic Regulator

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the convergence of the vanilla stochastic policy gradient method applied to the linear quadratic regulator (LQR) problem. The method is cheap in the following sense: at each iteration only tildeO interactions with the environment are needed, therefore allowing frequent policy improvement steps, and to ensure stability throughout and convergence to an epsilon-optimal policy with probability 1-delta, only O(mathttPolylog(1/delta)/epsilon) interactions are needed. To the best of our knowledge, this appears to be the first time that a stochastic model-free policy optimization method for LQR converges with high probability with tildeO per-iteration computation and polylogarithmic dependence on the confidence level. The convergence analysis presented here is agnostic to LQR specifics and hence could be potentially generalized to a broader class of problems.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

We consider the following undiscounted infinite-horizon linear quadratic regulator (LQR) problem:^11^ 1 As will be seen in Section 2.1 Stochastic Policy Gradient Converges with High Probability for Linear Quadratic Regulator"), the analysis to be discussed in this manuscript can be extended to the discounted-cost and the average-cost settings without essential changes. where $Q\in\mathbb{R}^{n\times n}$, $R\in\mathbb{R}^{m\times m}$ are positive definite matrices, and We assume in addition that $\lVert x_{0}\rVert\leq D_{X}$ for some $D_{X}>0$. To facilitate our discussion, for any policy $K$, we define $\Delta(K)=f(K)-f^{*}$, where $f^{*}=\min_{K}f(K)$. We assume there exists a policy with finite cost, so that $f^{*}<\infty$.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

It is well known that the restriction to linear Markov policies in (1.2 Stochastic Policy Gradient Converges with High Probability for Linear Quadratic Regulator")) suffices to obtain optimality for (1.1 Stochastic Policy Gradient Converges with High Probability for Linear Quadratic Regulator")) over the class of all history-dependent nonlinear policies.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We can roughly categorize the solution methods for solving LQR into three classes. Let us first operate in the idealized setting where the underlying model parameters $(A,B,Q,R)$ are known. The first class builds upon the observation that the optimal policy $K^{*}$ of (1.1 Stochastic Policy Gradient Converges with High Probability for Linear Quadratic Regulator")) can be computed via solving the algebraic Riccati equation (ARE), and therefore designs specialized numerical linear algebra methods for solving the ARE. The second class of methods based on the dynamic programming principle either operates in the policy space or value space. In recent years, a new class of first-order methods based on nonlinear programming has received considerable attention in MDPs and later in LQR. Such methods iteratively update the policy via its first-order (gradient) information. The global convergence of (natural) policy gradient applied to LQR, despite the latter being a non-convex function, has been established, followed by an active line of research.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Let us now consider the setting when the exact parameters are unknown. Solution methods in this case largely operate based on partially learning about the system by interacting with the environment.^22^ 2 In this manuscript we refer to one interaction as one state transition after committing an action. We choose not to refer to such interactions as samples as in some prior work, since there is no randomness in such transitions for the undiscounted setting. Note that LQR with stochastic transitions only makes sense for the discounted-cost or average-cost settings. In principle all three aforementioned classes of solution methods have their counterparts in this setting. A natural idea underlying such development is to first estimate the system parameters after collecting enough interactions, followed by solving a nominal LQR with the estimated parameters. We refer to this idea as the model-based principle. A particular question is therefore to determine the number of interactions needed for dynamics estimation in order to find an $\epsilon$-optimal policy. This question has been discussed in for the average-cost setting with potential stochastic transition dynamics.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

It should be noted that for (1.1 Stochastic Policy Gradient Converges with High Probability for Linear Quadratic Regulator")), a constant number of interactions is sufficient for forming a linear system that uniquely identifies system parameters provided the query state-action pair provides sufficient coverage.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

An alternative principle for designing interaction-based methods for LQR is to avoid explicit estimation of model parameters altogether, which we refer to as model-free methods. This has been considered, for instance, for policy-based methods and value-based methods. In particular, it has been shown that $\widetilde{\mathcal{O}}(1/\epsilon)$ environment interactions are needed for policy iteration and $\widetilde{\mathcal{O}}(1/\epsilon)$ for value iteration. Similar progress has been made for first-order (gradient-based) methods.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

For instance, $\mathcal{O}({\tt Poly}(1/\epsilon))$ interaction complexity has been first established, followed by $\widetilde{\mathcal{O}}(1/\epsilon^{5})$, $\widetilde{\mathcal{O}}(1/\epsilon^{2})$, $\widetilde{\mathcal{O}}(1/\epsilon^{3/2})$, and more recently, $\widetilde{\mathcal{O}}(1/\epsilon)$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Why would one consider model-free methods over model-based ones? We can perhaps argue that model-based methods are somewhat expensive, in the sense that a sufficiently large number of interactions need to be collected before we start to improve the policy, with non-trivial computation consumed between consecutive policy improvements. In this sense a reasonably good model-free method should waste no time in collecting too many environment interactions or consume too much computation for each policy improvement, and should ensure incremental yet steady progress towards the optimal policy. Unfortunately some of the aforementioned model-free methods with strong performance guarantees do not enjoy such properties. In essence they operate in a way that the methods behave similarly to their deterministic counterparts, which assume exact model information. This is typically achieved by collecting a large number of interactions (via long trajectories or mini-batches) at each round of policy improvement to ensure that the stochastic update to the policy is close to its deterministic counterpart.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this manuscript we are interested in the convergence of cheap stochastic policy optimization methods. By cheap we mean that they use $\widetilde{\mathcal{O}}$ interactions and computation between consecutive policy improvements. The small number of interactions implies that the update is truly stochastic instead of being a close approximation of deterministic updates, and accompanied with $\widetilde{\mathcal{O}}$ computation, ensures fast policy improvement. We will focus on cheap gradient-based methods. Existing convergence certificates come either with constant probability, or in expectation. It appears quite surprising that no high-probability results with polylogarithmic dependence on the confidence level have been established in the prior literature, despite fruitful development of boosting expectation to high-probability statements in stochastic optimization. It should be noted that the aforementioned convergence in expectation makes the non-trivial assumption on uniform stability throughout policy optimization.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Indeed, the main technical difficulty associated with obtaining convergence for cheap stochastic policy optimization methods (even in expectation) pertains to maintaining stability of the policies throughout policy optimization, as nothing can be said about the stochastic gradient once the policy becomes unstable and the objective (1.1 Stochastic Policy Gradient Converges with High Probability for Linear Quadratic Regulator")) itself blows up to infinity. In view of this, the dependence of gradient noise on the iterate within LQR behaves in a completely non-smooth way compared to problems recently studied in optimization literature with unbounded domains, which depends smoothly on the distance to the optimal solution.^33^ 3 Of course (1.1 Stochastic Policy Gradient Converges with High Probability for Linear Quadratic Regulator")) also has an unbounded domain. This on the other hand is not our main concern within the analysis.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our essential contribution in this manuscript is to provide a framework for convergence analysis that allows us to obtain such high-probability convergence guarantees. Our contributions can be roughly summarized as follows. First, we propose a rather generic framework that allows us to establish high-probability convergence of LQR with cheap stochastic policy gradient methods, provided the gradient construction oracle satisfies some minimalist assumption. In particular, the convergence framework uses no LQR specifics, and applies to generic black-box optimization for objectives satisfying the Polyak-Lojasiewicz (PL) property and local smoothness, and hence can be potentially applied in broader setups. Second, by instantiating the framework with a concrete choice of stepsizes, we establish an $\mathcal{O}(1/\sqrt{T})$ convergence rate of SPG, which is further improved to $\mathcal{O}(1/T)$ by utilizing the PL property.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, we verify that the minimal stochastic gradient oracle assumption can be indeed satisfied by slight modification of an existing gradient estimator, and correspondingly establish its $\widetilde{\mathcal{O}}({\tt Polylog(1/\delta)}/\epsilon)$ interaction complexity with probability at least $1-\delta$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Stochastic Policy Gradient", "weight": 1.0} -->

Going forward, we will focus on the vanilla stochastic policy gradient (SPG) method applied to the LQR problem. At any given iteration $t$, SPG first assumes access to a stochastic oracle that produces an estimate $G_{t}$ of $\nabla f(K_{t})$, and then updates the policy via Throughout the rest of our discussion, we assume that the initial policy $K_{0}$ is stable.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Condition 2.1", "weight": 1.0} -->

Clearly, Condition 2.1 Stochastic Policy Gradient Converges with High Probability for Linear Quadratic Regulator") posits that the estimator $G_{t}$ has small noise and is bounded both in expectation and with high probability. It is perhaps worth noting that we allow the upper bounds of $G_{t}$ (either the moment bound $V_{\Delta}$ or the high-probability bound $M_{\Delta,\delta}$) to depend on the optimality gap. Such a dependence is indeed essential, as the size of the true gradient itself $\nabla f(K_{t})$ would depend on the current optimality gap, and blows up to infinity if $K_{t}$ becomes unstable. For the rest of our discussion in this section, we will discuss the convergence of SPG (2.1 Stochastic Policy Gradient Converges with High Probability for Linear Quadratic Regulator")) assuming the stochastic oracle satisfies Condition 2.1 Stochastic Policy Gradient Converges with High Probability for Linear Quadratic Regulator").

<!-- chunk {"id": "body-0017", "role": "body", "section": "Condition 2.1", "weight": 1.0} -->

We will then discuss the construction of such an oracle in Section 4 Stochastic Policy Gradient Converges with High Probability for Linear Quadratic Regulator"). In particular, the constructed estimate $G_{t}$ will satisfy (2.4 Stochastic Policy Gradient Converges with High Probability for Linear Quadratic Regulator")) with probability $1$. Condition 2.1 Stochastic Policy Gradient Converges with High Probability for Linear Quadratic Regulator") also appears to be quite flexible, in the sense that it does not necessarily require the estimate $G_{t}$ to follow light-tail distributions.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Condition 2.1", "weight": 1.0} -->

We next present two basic properties of the LQR objective (1.1 Stochastic Policy Gradient Converges with High Probability for Linear Quadratic Regulator")), namely it is locally smooth, and satisfies a global PL property. It should be noted that these will be the only LQR-specific properties we utilize within our discussion in Section 3 Stochastic Policy Gradient Converges with High Probability for Linear Quadratic Regulator").

<!-- chunk {"id": "body-0019", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

We start by noting that in view of Condition 2.1 Stochastic Policy Gradient Converges with High Probability for Linear Quadratic Regulator"), to ensure that the stochastic gradient $G_{t}$ remains bounded throughout the optimization process, one needs to in turn control the optimality gap $\Delta(K_{t})$. On the other hand, the optimality gap of the later policies would clearly depend on $G_{t}$. In turn this suggests somewhat an induction approach to the convergence analysis. Nevertheless, it is clear that with our goal of taking only $\widetilde{\mathcal{O}}$ interactions for the construction of $G_{t}$, it would be difficult to maintain such a high-probability certificate if we were to show that $\Delta(K_{t+1})$ remains bounded with high probability simply from the fact that $\Delta(K_{t})$ is bounded with high probability and that we have an approximate descent at iteration $t$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

In principle, $\widetilde{\mathcal{O}}$ interactions for gradient evaluation typically ensure at best approximate descent in expectation, instead of with high probability.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

To proceed, our basic idea is to introduce the following auxiliary sequence $\left\{Y_{t}\right\}$, which in some sense generalizes the observation underlying Lemma 5.4 of.^44^ 4 It is well known that the summation of $T$ independent standard Gaussian random variables is of order $\mathcal{O}(\sqrt{T})$ with high probability. Now suppose in round $t+1$ of summation, the random variable to be summed is Gaussian conditioned on the event that the partial sum of the first $t$ rounds is bounded by $C\sqrt{t}$ for some constant $C$, and $\infty$ otherwise. Lemma 5.4 in shows that the total sum is still of order $\mathcal{O}(\sqrt{T})$ provided $C$ is large enough.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

In essence, since the behavior of $\Delta(K_{t})$ depends on the quality of $\left\{G_{i}\right\}_{i<t}$, we will let $E_{t}$ denote the event of a bounded optimality gap for all iterations up to $t$, such that one can readily control $Y_{t}\coloneqq\Delta(K_{t})\mathbbm{1}_{E_{t}}$. Hence the remaining goal is to show that $\Delta(K_{t})=Y_{t}$ with high probability, i.e., the indicator $\mathbbm{1}_{E_{t}}$ does not really matter in terms of our probabilistic statement.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

To make our above observation precise, let us consider choosing $M,\Delta$ and $\left\{\Delta_{t}\right\}$ such that and accordingly define We make the following immediate observation regarding the auxiliary sequence $\left\{Y_{t}\right\}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "SPG with $O(1/\\sqrt{T})$ Rate", "weight": 1.0} -->

We now proceed to first establish that SPG converges at the rate of $\mathcal{O}(1/\sqrt{T})$ with high probability. To this end, we begin by establishing the following basic recursion on the convergence of $\left\{Y_{t}\right\}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "SPG with $O(1/{T})$ Rate", "weight": 1.0} -->

We now discuss a refinement to our approach in Section 3.1 Rate ‣ 3 Convergence Analysis ‣ (Cheap) Stochastic Policy Gradient Converges with High Probability for Linear Quadratic Regulator"), which leads to an improved $\mathcal{O}(1/T)$ convergence rate for the SPG method. The basic observation we utilize is the fact that the upper bound in (3.11 Rate ‣ 3 Convergence Analysis ‣ (Cheap) Stochastic Policy Gradient Converges with High Probability for Linear Quadratic Regulator")) used in Azuma's inequality indeed depends on the optimality gap $\Delta(K_{t})$, which in view of (2.7 Stochastic Policy Gradient Converges with High Probability for Linear Quadratic Regulator")), also diminishes provided that $\left\{K_{t}\right\}$ converges to the optimal policy.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Construction of Stochastic Oracle", "weight": 1.0} -->

Let us recall the following construction of the two-point estimator first developed for convex optimization and later studied in the context of LQR. Specifically, for a given $\alpha>0$, let us randomly sample $x_{0}\sim\mathcal{D}$, and $U$ uniformly distributed over the unit sphere in $\mathbb{R}^{m\times n}$, and construct where $d=mn$, and $F(K;x)=\textstyle\sum\nolimits_{i\geq 0}x_{i}^{\top}(Q+K^{\top}RK)x_{i}$ where $x_{i}=(A-BK)^{i}x$. As will be seen in the ensuing Proposition 4.1 Stochastic Policy Gradient Converges with High Probability for Linear Quadratic Regulator"), the two-point estimator generalizes the classical one-point estimator for zeroth-order convex optimization with the benefit of reduced variance that can be made independent of $\alpha$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

We now briefly discuss a few more questions of potential interest. First, it is well known that for (1.1 Stochastic Policy Gradient Converges with High Probability for Linear Quadratic Regulator")), with model-based methods a constant number of environment interactions is enough for identifying the exact system parameters. Hence it would be interesting to study whether the reported $\mathcal{O}(1/\epsilon)$ interaction complexity can be further improved. In addition, it is also possible to extend the analysis to average-cost and discounted-cost settings more explicitly by considering detailed constructions of the stochastic gradient oracles satisfying Condition 2.1 Stochastic Policy Gradient Converges with High Probability for Linear Quadratic Regulator").
