## Introduction

Consider the problem of minimizing a *stochastic objective*,

At the heart of many algorithms for reinforcement learning (RL) lies *zeroth-order* estimation of the gradient $\nabla F$. Yet, in domains that deal with structured systems, such as linear control, physical simulation, or robotics, it is possible to obtain *exact* gradients of $f$, which can also be used to construct a *first-order* estimate of $\nabla F$. The availability of both options begs the question: given access to exact gradients of $f$, which estimator should we prefer?

In stochastic optimization, the theoretical benefits of using first-order estimates of $\nabla F$ over zeroth-order ones have mainly been understood through the lens of variance and convergence rates: the first-order estimator often (*not always*) results in much less variance compared to the zeroth-order one, which leads to faster convergence rates to a local minima of general nonconvex smooth objective functions.

However, the landscape of RL objectives that involve long-horizon sequential decision making (e.g. policy optimization) is challenging to analyze, and convergence properties in these landscapes are relatively poorly understood, except for structured settings such as finite-state MDPs or linear control. In particular, physical systems with contact, as we show in Figure 1, can display complex characteristics including nonlinearities, non-smoothness, and discontinuities.

Figure 1: Examples of simple optimization problems on physical systems. Goal is to: A. maximize y position of the ball after dropping. B. maximize distance thrown, with a wall that results in inelastic impact. C. maximize transferred angular momentum to the pivoting bar through collision. Second row: the original objective and the stochastic objective after randomized smoothing.

Nevertheless, lessons from convergence rate analysis tell us that there may be benefits to using the exact gradients even for these complex physical systems. Such ideas have been championed through the term "differentiable simulation", where forward simulation of physics is programmed in a manner that is consistent with automatic differentiation, or computation of analytic derivatives. These methods have shown promising results in decreasing computation time compared to zeroth-order methods.

Existing literature in differentiable simulation mainly focuses on the use of exact gradients for *deterministic* optimization. However, show that using exact gradients for a deterministic objective can lead to suboptimal behavior of certain systems due to their landscapes. In these systems, stochasticity can be used to *regularize* the landscapes with randomized smoothing. We illustrate how the landscapes change upon injecting noise (Figure 1), and list some benefits of considering a *surrogate* stochastic objective.

Stochasticity smooths local minima. As noted in, stochasticity can alleviate some of the high-frequency local minima that deterministic gradients will be stuck on. For instance, the small discontinuity on the right side of Figure 1.B is filtered by Gaussian smoothing.

Stochasticity alleviates flat regions. In systems of Figure 1, the gradients in some of the regions can be completely flat. This stalls progress of gradient descent. The stochastic objective, however, still has non-zero gradient as some samples escape the flat regions and provide an informative direction of improvement.

Stochasticity encodes robustness. In Figure 1.C, following the gradient to increase the transferred momentum causes the ball to miss the pivot and land in a high-cost region. In contrast, the stochastic objective has a local minimum within the safe region, as the samples provide information about missing the pivot.

Thus, our work attempts to compare two versions of gradient estimators in the stochastic setting: the first-order estimator and the zeroth-order one. This setting rules out the case that zeroth-order estimates perform better simply because of stochasticity, and sets equal footing for the two methods.

When $f$ is continuous, these quantities both converge to the same quantity ($\nabla F$) in expectation. We first show that even with continuous $f$, the first-order gradient estimate *can* result in more variance than the zeroth-order one due to the *stiffness* of dynamics or due to compounding of gradients in chaotic systems.

In addition, we show that the assumption of continuous $f$ can be violated in many relevant physical systems that are nearly/strictly *discontinuous* in the underlying landscape. These discontinuities are commonly caused by contact and geometrical constraints. We provide minimal examples to highlight specific challenges in Figure 1. These are not mere pathologies, but abstractions of more complicated examples that are rich with contact, such as robotic manipulation.

We show that the presence of such discontinuities causes the first-order gradient estimator to be biased, while the zeroth-order one still remains unbiased under discontinuities. Furthermore, we show that stiff continuous approximations of discontinuities, even if asymptotically unbiased, can still suffer from what we call *empirical bias* under finite-sample settings. This results in a bias-variance tradeoff between the biased first-order estimator and the *often* high-variance, yet unbiased zeroth-order estimator. Intriguingly, we find that the bias-variance tradeoff in this setting manifests itself not through convergence rates, but through different local minima. This shows that the two estimators may fundamentally operate on different landscapes implicitly.

The presence of discontinuities need not indicate that we need to commit ourselves to uniformly using one of the estimators. Many physical systems are *hybrid* by nature; they consist of smooth regions that are separated by manifolds of non-smoothness or discontinuities. This suggests that we may be able to utilize the first-order estimates far away from these manifolds to obtain benefits of convergence rates, while switching to zeroth-order ones in the vicinity of discontinuities to obtain unbiased estimates.

For this purpose, we further attempt to answer the question: how can we then correctly utilize exact gradients of $f$ for variance reduction when we know the objective is nearly discontinuous? Previous works show that the two estimators can be combined by interpolating based on empirical variance. However, we show that in the presence of near-discontinuities, selecting based on empirical variance alone can lead to highly inaccurate estimates of $\nabla F$, and propose a robustness constraint on the accuracy of the interpolated estimate to remedy this effect.

Contributions. We 1) shed light on some of the inherent problems of RL using differentiable simulators, and answer which gradient estimator can be more useful under different characteristics of underlying systems such as discontinuities, stiffness, and chaos; and 2) present the $\alpha$-order gradient estimator, a robust interpolation strategy between the two gradient estimators that utilizes exact gradients without falling into the identified pitfalls of the previous methods.

We hope both contributions inspire algorithms for policy optimization using differentiable simulators, as well as design guidelines for new and existing simulators.

## Preliminaries

Notation. We denote the expectation of a random vector $\mathbf{z}$ as ${\mathbb{E}}{\lbrack\mathbf{z}\rbrack}$, and its variance as ${\text{Var}{\lbrack\mathbf{z}\rbrack}}:={{\mathbb{E}}{\lbrack{\|{\mathbf{z} - {{\mathbb{E}}{\lbrack\mathbf{z}\rbrack}}}\|}^{2}\rbrack}}$. Expectations are defined in almost-sure sense, so that the law of large numbers holds (see Section A.1 for details).

Setting. We study a discrete-time, finite-horizon, continuous-state control problem with states $\mathbf{x} \in {\mathbb{R}}^{n}$, inputs $\mathbf{u} \in {\mathbb{R}}^{m}$, transition function $\phi:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{m}}\rightarrow{\mathbb{R}}^{n}}$, and horizon $H \in {\mathbb{N}}$. Given a sequence of costs $c_{h}:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{m}}\rightarrow{\mathbb{R}}}$, a family of policies $\pi_{h}:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{d}}\rightarrow{\mathbb{R}}^{m}}$ parameterized by ${\mathbf{θ}} \in {\mathbb{R}}^{d}$, and a sequence of injected noise terms $\mathbf{w}_{1:H} \in {({\mathbb{R}}^{m})}^{H}$, we define the cost-to-go functions

Our aim is to minimize the policy optimization objective

where $\rho$ is a distribution over initial states $\mathbf{x}_{1}$, and $\mathbf{w}_{1},\ldots,\mathbf{w}_{H}$ are independent and identically distributed according to some distribution $p$. In the main text, we make the following assumption on the distributions $\rho$ and $p$:

### Assumption 2.1

We assume that $\rho$ has finite moments, and that $p = {\mathcal{N}{(0,{\sigma^{2}I_{n}})}}$ for some $\sigma > 0$.

Our rationale for Gaussian $p$ is that we view $\mathbf{w}_{1:H}$ as *smoothing* to regularize the optimization landscape. To simplify the main text, we take $\mathbf{x}_{1}$ to be deterministic ($\rho$ is a dirac-delta), with general $\rho$ being addressed in the appendix. Setting $\overline{\mathbf{w}} = \mathbf{w}_{1:H}$, $\overline{p} = {\mathcal{N}{(0,{\sigma^{2}I_{nH}})}}$, and ${f{({\mathbf{θ}},\overline{\mathbf{w}})}} = {V_{1}{(\mathbf{x}_{1},\overline{\mathbf{w}},{\mathbf{θ}})}}$, we can express $F{({\mathbf{θ}})}$ as a *stochastic optimization problem*,

Trajectory optimization. Our parametrization also includes open-loop trajectory optimization. Letting the policy parameters be an open-loop sequence of inputs ${\mathbf{θ}} = {\{{\mathbf{θ}}_{h}\}}_{h = 1}^{H}$ and having no feedback ${\pi{(\mathbf{x}_{h},{\mathbf{θ}})}} = {\mathbf{θ}}_{h}$, we optimize over sequence of inputs to be applied to the system.

One-step optimization. We illustrate some key ideas in the open-loop case where $H = 1$: $\pi:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{m}}$ is the identity function with $\overline{\mathbf{w}} = \mathbf{w} \in {\mathbb{R}}^{m}$, $d = m$ and $c:{{\mathbb{R}}^{m}\rightarrow{\mathbb{R}}}$,

### Gradient Estimators

In order to minimize $F{({\mathbf{θ}})}$, we consider iterative optimization using stochastic estimators of its gradient ${\nabla F}{({\mathbf{θ}})}$. We say a function $\psi:{{\mathbb{R}}^{d_{1}}\rightarrow{\mathbb{R}}^{d_{2}}}$ has *polynomial growth* if there exist constants $a,b$ such that, for all $\mathbf{z} \in {\mathbb{R}}^{d_{1}}$, ${\|{\psi{(\mathbf{z})}}\|} \leq {a{({1 + {\|\mathbf{z}\|}^{b}})}}$. The following assumption ensures these gradients are well-defined.

### Assumption 2.2

We assume that the policy $\pi$ is continuously differentiable everywhere, and the dynamics $\phi$, as well as the cost $c_{h}$ have polynomial growth.

Even when the costs or dynamics are *not* differentiable, the expected cost $F{({\mathbf{θ}})}$ is differentiable due to the smoothing $\overline{\mathbf{w}}$. ${\nabla F}{({\mathbf{θ}})}$ is referred to as the *policy gradient*.

Zeroth-order estimator. The policy gradient can be estimated only using samples of the function values.

### Definition 2.3

Given a single zeroth-order estimate of the policy gradient ${\hat{\nabla}}^{\lbrack 0\rbrack}F_{i}{({\mathbf{θ}})}$, we define the zeroth-order batched gradient (ZoBG) ${\overline{\nabla}}^{\lbrack 0\rbrack}F{({\mathbf{θ}})}$ as the sample mean,

where $\mathbf{x}_{h}^{i}$ is the state at time $h$ of a trajectory induced by the noise $\mathbf{w}_{1:H}^{i}$, $i$ is the index of the sample trajectory, and $D_{\mathbf{θ}}\pi$ is the Jacobian matrix ${\partial{\pi/{\partial{\mathbf{θ}}}}} \in {\mathbb{R}}^{m \times d}$.

The hat notation denotes a per-sample Monte-Carlo estimate, and bar-notation a sample mean. The ZoBG is also referred to as the REINFORCE, score function, or the likelihood-ratio gradient.

Baseline. In practice, a baseline term $b$ is subtracted from $V_{1}{(\mathbf{x}_{1},\mathbf{w}_{1:H}^{i},{\mathbf{θ}})}$ for variance reduction. We use the zero-noise rollout as the baseline $b = {V_{1}{(\mathbf{x}_{1},\mathbf{0}_{1:H},{\mathbf{θ}})}}$:

First-order estimator. In differentiable simulators, the gradients of the dynamics $\phi$ and costs $c_{h}$ are available *almost surely* (i.e., with probability one). Hence, one may compute the exact gradient ${\nabla_{\mathbf{θ}}V_{1}}{(\mathbf{x}_{1},\mathbf{w}_{1:H},{\mathbf{θ}})}$ by automatic differentiation and average them to estimate ${\nabla F}{({\mathbf{θ}})}$.

### Definition 2.4

Given a single first-order gradient estimate ${\hat{\nabla}}^{\lbrack 1\rbrack}F_{i}{({\mathbf{θ}})}$, we define the first-order batched gradient (FoBG) as the sample mean:

The FoBG is also referred to as the reparametrization gradient, or the pathwise derivative. Finally, we define the empirical variance.

### Definition 2.5 (Empirical variance)

For $k \in {\{ 0,1\}}$, we define the empirical variance by

## Pitfalls of First-order Estimates

What are the cases for which we would prefer to use the ZoBG over the FoBG in policy optimization using differentiable simulators? Throughout this section, we analyze the performance of the two estimators through their bias and variance properties, and find pathologies where using the first-order estimator blindly results in worse performance.

### Bias under discontinuities

Under standard regularity conditions, it is well-known that both estimators are unbiased estimators of the true gradient ${\nabla F}{({\mathbf{θ}})}$. However, care must be taken to define these conditions precisely. Fortunately, the ZoBG is still unbiased under mild assumptions.

### Lemma 3.1

Under Assumption 2.1 and Assumption 2.2, the ZoBG is an unbiased estimator of the stochastic objective.

In contrast, the FoBG requires strong continuity conditions in order to satisfy the requirement for unbiasedness. However, under Lipschitz continuity, it is indeed unbiased.

### Lemma 3.2

Under Assumption 2.1 and Assumption 2.2, and if $\phi{( \cdot, \cdot )}$ is locally Lipschitz and $c_{h}{( \cdot, \cdot )}$ is continuously differentiable, then ${\overline{\nabla}}^{\lbrack 1\rbrack}F{({\mathbf{θ}})}$ is defined almost surely, and

The proofs and more rigorous statements of both lemmas are provided in Appendix A. Notice that Lemma 3.1 permits $V_{h}$ to have discontinuities (via discontinuities of $c_{h}$ and $\phi$), whereas Lemma 3.2 does not.

### Bias of FoBG under discontinuities

The FoBG can fail when applied to discontinuous landscapes. We illustrate a simple case of biasedness through a counterexample.

### Example 3.3 (Heaviside)

Consider the Heaviside function,

whose stochastic objective becomes the error function

where ${{erf}{(t;\sigma^{2})}}:={\int_{t}^{\infty}{\frac{1}{\sqrt{2\pi}\sigma}e^{- {x^{2}/\sigma^{2}}}{dx}}}$ is the Gaussian tail integral. Defining the gradient of the Monte-Carlo objective $H{({{\mathbf{θ}} + \mathbf{w}})}$ requires subtlety. It is common in physics to define ${{\nabla_{\mathbf{θ}}H}{({{\mathbf{θ}} + \mathbf{w}})}} = {\delta{({{\mathbf{θ}} + \mathbf{w}})}}$ as a dirac-delta function, where integration is interpreted so that the fundamental theorem of calculus holds. This is *irreconcilable* with using *expectation* to define the integral, which presupposes that the law of large numbers hold. Indeed, since ${{\nabla_{\mathbf{θ}}H}{({{\mathbf{θ}} + \mathbf{w}})}} = 0$ for all ${\mathbf{θ}} \neq {- \mathbf{w}}$, we have ${{\mathbb{E}}_{\mathbf{w}_{i}}\delta{({{\mathbf{θ}} + \mathbf{w}_{i}})}} = 0$. Hence, the FoBG is biased, because the gradient of the stochastic objective at any $\mathbf{θ}$ is non-zero: ${{\nabla_{\mathbf{θ}}\text{erf}}{({- {\mathbf{θ}}};\sigma^{2})}} = {\frac{1}{\sqrt{2\pi}\sigma}{\exp{({- {{{({{\mathbf{θ}} - \mathbf{w}})}/2}\sigma^{2}}})}}} \neq 0$.

It is worth noting that the empirical variance of the FoBG estimator in this example is zero, since all the samples are identically zero. On the other hand, the ZoBG escapes this problem and provides an unbiased estimate, since it always takes finite intervals that include the integral of the delta.

Figure 2: From left: heaviside objective f (θ,w) and stochastic objective F (θ), empirical values of the gradient estimates, and their empirical variance.

### The "Empirical bias" phenomenon

One might argue that *strict* discontinuity is simply an artifact of modeling choice in simulators; indeed, many simulators approximate discontinuous dynamics as a limit of continuous ones with growing Lipschitz constant. In this section, we explain how this can lead to a phenomenon we call *empirical bias*, where the FoBG appears to have low empirical variance, but is still highly inaccurate; i.e. it "looks" biased when a finite number of samples are used. Through this phenomenon, we claim that performance degradation of first-order gradient estimates do not require strict discontinuity, but is also present in continuous, yet *stiff* approximations of discontinuities. ^11^1We say that a continuous function $f$ is stiff at $x$ if the magnitude of the gradient $\|{{\nabla f}{(x)}}\|$ is high.

### Definition 3.4 (Empirical bias)

Let $\mathbf{z}$ be a vector-valued random variable with ${{\mathbb{E}}{\lbrack{\|\mathbf{z}\|}\rbrack}} < \infty$. We say $\mathbf{z}$ has $(\beta,\Delta,S)$-empirical bias if there is a random event $\mathcal{E}$ such that ${\Pr{\lbrack\mathcal{E}\rbrack}} \geq {1 - \beta}$, and $\parallel {\mathbb{E}}{\lbrack\mathbf{z} \mid \mathcal{E}\rbrack} - {\mathbb{E}}{\lbrack\mathbf{z}\rbrack} \parallel \geq \Delta$, but $\parallel \mathbf{z} - {\mathbb{E}}{\lbrack\mathbf{z} \mid \mathcal{E}\rbrack} \parallel \leq S$ almost surely on $\mathcal{E}$.

A paradigmatic example of empirical bias is a random scalar $\mathbf{z}$ which takes the value $0$ with probability $1 - \beta$, and $\frac{1}{\beta}$ with probability $\beta$. Setting $\mathcal{E} = {\{{\mathbf{z} = 0}\}}$, we see ${{\mathbb{E}}{\lbrack\mathbf{z}\rbrack}} = 1$, ${{\mathbb{E}}{\lbrack{\mathbf{z} \mid \mathcal{E}}\rbrack}} = 0$, and so $\mathbf{z}$ satisfies $(\beta,1,0)$-empirical bias. Note that ${\text{Var}{\lbrack\mathbf{z}\rbrack}} = {{1/\beta} - 1}$; in fact, small-$\beta$ empirical bias implies large variance more generally.

### Lemma 3.5

Suppose $\mathbf{z}$ has $(\beta,\Delta,S)$-empirical bias. Then ${\text{Var}{\lbrack\mathbf{z}\rbrack}} \geq \frac{\Delta_{0}^{2}}{\beta}$, where $\Delta_{0}:={\max{\{ 0,{{{({1 - \beta})}\Delta} - {\beta{\|{{\mathbb{E}}{\lbrack\mathbf{z}\rbrack}}\|}}}\}}}$.

Figure 3: Left: More detailed example of ball hitting the wall in Figure 1.B. Left: The green trajectories hit a rectangular wall, displaying discontinuities. Right: the pink trajectories collide with the dome on top, and show continuous but stiff behavior.

Empirical bias naturally arises for discontinuities or stiff continuous approximations. We give two examples of common discontinuities that arise in differentiable simulation, that permit continuous approximations.

### Example 3.6 (Coulomb friction)

The Coulomb model of friction is discontinuous in the relative tangential velocity between two bodies. In many simulators, it is common to consider a continuous approximation instead. We idealize such approximations through a piecewise linear relaxation of the Heaviside that is continuous, parametrized by the width of the middle linear region $\nu$ (which corresponds to *slip tolerance*).

In practice, lower values of $\nu$ lead to more realistic behavior in simulation, but this has adverse effects for empirical bias. Considering ${f_{\nu}{({\mathbf{θ}},\mathbf{w})}} = {{\overline{H}}_{\nu}{({{\mathbf{θ}} + \mathbf{w}})}}$, we have ${F_{\nu}{({\mathbf{θ}})}} = {{\mathbb{E}}_{\mathbf{w}}{\lbrack{{\overline{H}}_{\nu}{({{\mathbf{θ}} + \mathbf{w}})}}\rbrack}}:={{erf}{({{\nu/2} - \theta};\sigma^{2})}}$. In particular, setting $c_{\sigma}:=\frac{1}{\sqrt{2\pi}\sigma}$, then at ${\mathbf{θ}} = {\nu/2}$, ${{\nabla F_{\nu}}{({\mathbf{θ}})}} = c_{\sigma}$, whereas, with probability at least $c_{\sigma}\nu$, ${{\nabla f_{\nu}}{({\mathbf{θ}},\mathbf{w})}} = 0$. Hence, the FoBG has $({c_{\sigma}\nu},c_{\sigma},0)$ empirical bias, and its variance scales with $1/\nu$ as $\nu\rightarrow 0$. The limiting $\nu = 0$ case, corresponding to the Coulomb model, is the Heaviside from Example 3.3. ‣ Bias of FoBG under discontinuities. ‣ 3.1 Bias under discontinuities ‣ 3 Pitfalls of First-order Estimates ‣ Do Differentiable Simulators Give Better Policy Gradients?"), where the limit of high empirical bias, as well as variance, becomes biased in expectation (but, surprisingly, zero variance!). We empirically illustrate this effect in Figure 4. ‣ 3.2 The “Empirical bias” phenomenon ‣ 3 Pitfalls of First-order Estimates ‣ Do Differentiable Simulators Give Better Policy Gradients?"). We also note that more complicated models of friction (e.g. that incorporates the Stribeck effect ) would suffer similar problems.

Figure 4: Top column: illustration of the physical system and the relaxation of Coulomb friction. Bottom column: the values of estimators and their empirical variances depending on number of samples and slip tolerance. Values of FoBG are zero in low-sample regimes due to empirical bias. As ν → 0, the empirical variance of FoBG goes to zero, which shows as empty in the log-scale. Expected variance, however, blows up as it scales with 1/ν.

Figure 5: The variance of the gradient of V1, with running cost ch = ∥xh2 − xg∥2, with respect to input trajectory as spring constant k increases. Mass m and damping coefficient c are fixed.

### Example 3.7

(Geometric Discontinuity). Discontinuity also comes from surface normals. We show this in Figure 3, where balls that collide with a rectangular geometry create discontinuities. It is possible to make a continuous relaxation by considering smoother geometry, depicted by the addition of the dome in Figure 3. While this makes FoBG no longer biased asymptotically, the stiffness of the relaxation results in high empirical bias.

### High variance first-order estimates

Even in the absence of empirical bias, we present other cases in which FoBG suffers simply due to high variance.

Scenario 1: Persistent stiffness. When the dynamics are *stiff* ^22^2We say that a discrete-time dynamical system is stiff if the mapping function $\phi$ is stiff. Note that when $\phi$ contains forces from spring-like components, $\|{\nabla\phi}\|$ scales with the spring constant. Thus, the presence of a stiff spring leads to a stiff system., such as contact models with stiff spring approximations, the high norm of the gradient can contribute to high variance of the FoBG.

### Example 3.8

(Pushing with stiff contact). We demonstrate this phenomenon through a simple 1D pushing example in Figure 5, where the ZoBG has lower variance than the FoBG as stiffness increases, until numerical semi-implicit integration becomes unstable under a fixed timestep.

In practice, lowering the timestep can alleviate the issue at the cost of more computation time. Less stiff formulations of contact dynamics also addresses this problem effectively.

Scenario 2: Chaos. As noted in, even if the gradient of the dynamics is small at every $h$, their compounding product can cause $\|{\nabla_{\mathbf{θ}}V_{1}}\|$ to be large if the system is chaotic. Yet, in expectation, the gradient of the stochastic objective ${\nabla F} = {{\nabla{\mathbb{E}}}{\lbrack V_{1}\rbrack}}$ can be benign and well-behaved.

### Example 3.9

(Chaos of double pendulum). We demonstrate this in Figure 6 for a classic chaotic system of the double pendulum. As the horizon of the trajectory increases, the variance of FoBG becomes higher than that of ZoBG.

Figure 6: Variance of the gradient of the terminal cost ∥qH − qg∥2 with respect to the initial position q1. As horizon grows through a chaotic system, the ZoBG dominates the FoBG.

### Comparison to ZoBG

Compared to the pitfalls of FoBG, the ZoBG variance can be bounded as follows.

### Lemma 3.10

If for all $\mathbf{x}$ and $\overline{\mathbf{w}}$, ${|{V_{1}{(\mathbf{x},\overline{\mathbf{w}},{\mathbf{θ}})}}|} \leq B_{V}$ and ${\|{D_{\mathbf{θ}}\pi{(\mathbf{x},{\mathbf{θ}})}}\|}_{op} \leq B_{\pi}$, then

We refer to Section B.2 for proof. Lemma 3.10 is intended to provide a qualitative understanding of the zeroth-order variance: it scales with the horizon-dimension product $Hn$, but *not* the scale of the derivatives. On the other hand, the variance of FoBG does; when $\frac{Hn}{\sigma^{2}} \gg {\text{Var}{\lbrack{{\hat{\nabla}}^{\lbrack 1\rbrack}F{({\mathbf{θ}})}}\rbrack}} = {\text{Var}{\lbrack{{\nabla_{\mathbf{θ}}V}{(\mathbf{x}_{1},\overline{\mathbf{w}},{\mathbf{θ}})}}\rbrack}}$, the ZoBG has higher variance.

Figure 7: First Column: Ball with wall example. In the third row, the triangle is the initial point, and red/blue/green stars are the optimum achieved by FoBG, ZoBG, and AoBG respectively (blue and green stars overlap). Second column: Iteration vs. Cost plot of different gradients. Right columns: Same plot repeated for the Momentum Transfer example. Standard deviation plotted 10 fold for visualization.

## $\alpha$-order Gradient Estimator

Previous examples give us insight on which landscapes are better fit for first-order estimates of policy gradient, and which are better fit for zeroth-order ones. As shown in Figure 7, even on a single policy optimization objective, it is best to adaptively switch between the first and zeroth-order estimators depending on the local characteristics of the landscape. In this section, we propose a strategy to achieve this adaptively, interpolating between the two estimators to reap the benefits of both approaches simultaneously.

### Definition 4.1

Given $\alpha \in {\lbrack 0,1\rbrack}$, we define the alpha-order batched gradient (AoBG) as:

When interpolating, we use independent trajectories to generate ${\overline{\nabla}}^{\lbrack 1\rbrack}F{({\mathbf{θ}})}$ and ${\overline{\nabla}}^{\lbrack 0\rbrack}F{({\mathbf{θ}})}$ (see Section C.1). We consider strategies for selecting $\alpha$ in a *local fashion*, as a function of the observed sample, as detailed below.

### A robust interpolation protocol

A potential approach might be to select $\alpha$ based on achieving minimum variance, considering empirical variance as an estimate. However, in light of the *empirical bias* phenomenon detailed in Section 3 (or even actual bias in the presence of discontinuities), we see that the empirical variance is unreliable, and can lead to inaccurate estimates for our setting. For this reason, we consider an additional criterion of *uniform accuracy*:

### Definition 4.2 (Accuracy)

$\alpha$ is $(\gamma,\delta)$-accurate if the bound on the *error* of AoBG is satisfied with probability $\delta$:

To remedy the limitations of considering empirical variance in isolation, we propose an interpolation protocol that can satisfy an accuracy guarantee, while still attempting to minimize the variance.

We explain the terms in Eq 4 below in detail.

Objective. Since we interpolate the FoBG and ZoBG using independent samples, ${\alpha^{2}{\hat{\sigma}}_{1}^{2}} + {{({1 - \alpha})}^{2}{\hat{\sigma}}_{0}^{2}}$ is an unbiased estimate of ${N \cdot \text{Var}}{\lbrack{{\overline{\nabla}}^{\lbrack\alpha\rbrack}F{({\mathbf{θ}})}}\rbrack}$. Thus, our objective is to choose $\alpha$ to minimize this variance.

Constraint. Our constraint serves to enforce accuracy. Since the FoBG is potentially biased, we use ZoBG as a surrogate of ${\nabla F}{({\mathbf{θ}})}$. For this purpose, we use $\epsilon > 0$ as a confidence bound on $\|{{{\overline{\nabla}}^{\lbrack 0\rbrack}F{({\mathbf{θ}})}} - {{\nabla F}{({\mathbf{θ}})}}}\|$ from the obtained samples. When $\epsilon$ is a valid confidence bound that holds with probability $\delta$, we prove that our constraint in Eq 4 guarantees accuracy in Eq 3. ‣ 4.1 A robust interpolation protocol ‣ 4 𝛼-order Gradient Estimator ‣ Do Differentiable Simulators Give Better Policy Gradients?").

### Lemma 4.3 (Robustness)

Suppose that ${\epsilon + {\alphaB}} \leq \gamma$ with probability $\delta$. Then, $\alpha$ is $(\gamma,\delta)$-accurate.

### Proof

By repeated applications of the triangle inequality. See Section C.3 for a detailed proof. ∎

Specifying the confidence $\epsilon > 0$. We select $\epsilon > 0$ based on a Bernstein vector concentration bound (Section C.4), which only requires a prior upper bound on the magnitude of the value function $V_{1}{( \cdot )}$ and gradients $D_{\mathbf{θ}}\pi{( \cdot,{\mathbf{θ}})}$.

Asymptotic feasibility. Eq 4 is not feasible if $\epsilon > \gamma$, which would indicate that we simply do not have enough samples to guarantee $(\gamma,\delta)$-accuracy. In this case, we choose to side on conservatism and fully use the ZoBG by setting $\alpha = 0$. Asymptotically, as the number of samples $N\rightarrow\infty$, the confidence interval $\varepsilon\rightarrow 0$, which implies that Eq 4 will always be feasible.

Finally, we note that Eq 4 has a closed form solution, whose proof is provided in Section C.2.

### Lemma 4.4

With $\gamma = \infty$, the optimal $\alpha$ is $\alpha_{\infty}:=\frac{{\hat{\sigma}}_{0}^{2}}{{\hat{\sigma}}_{1}^{2} + {\hat{\sigma}}_{0}^{2}}$. For finite $\gamma \geq \epsilon$, Eq 4 is

We give some qualitative characteristics of the solution:

If we are within constraint and ${\hat{\sigma}}_{0}^{2} \gg {\hat{\sigma}}_{1}^{2}$, as we can expect from benign smooth systems, then $\alpha \approx 1$, and we rely more on the FoBG.

In pathological cases where we are unbiased yet ${\hat{\sigma}}_{1}^{2} \gg {\hat{\sigma}}_{0}^{2}$ (e.g. stiffness and chaos), then $\alpha \approx 0$.

If there is a large difference between the ZoBG and the FoBG such that $B \gg 0$, we expect strict/empirical bias from discontinuities and tend towards using ZoBG.

Figure 8: 1st column: trajectory optimization on pushing example with different contact models. AoBG and FoBG overlaps in soft pushing example. 2nd column: trajectory optimization on friction contact, and policy optimization on the tennis example. 3rd / 4th column: Visualization of policy performance for tennis. Black dots correspond to initial positions and colored dots correspond to final position, while the shaded lines are visualizations of individual closed-loop trajectories across multiple initial conditions.

## Landscape Analysis & Case Studies

### Landscape analysis on examples

Though we have characterized the bias-variance characteristics of different gradients, their convergence properties in landscapes of physical systems remain to be investigated. We visualize the performance of fixed-step gradient descent with the FoBG, ZoBG, and AoBG on examples of Figure 1.

Ball with wall. On the system of Figure 1.B, the FoBG fails to make progress at the region of flatness, while the ZoBG and AoBG successfully find the minima of the landscape (Figure 7). In addition, the interpolation scheme switches to prioritizing ZoBG near discontinuities, while using more information from FoBG far from discontinuities; as a result, the variance of AoBG is lower than that of ZoBG.

Angular momentum transfer. Next, we show results for the momentum transfer system of Figure 1.C in Figure 7. Running gradient descent results in both the ZoBG and AoBG converging to the robust local minima of the solution. However, the bias of FoBG forces it off the cliff and the optimizer is unable to recover. Again, our interpolation scheme smoothly switches to prioritizing the ZoBG near the discontinuity, enabling it to stay within the safe region while maximizing the transferred momentum.

Bias-variance leads to different minima. Through these examples with discontinuities, we claim that the bias-variance characteristics of gradients in these landscapes not only lead to different convergence rates, but convergence to different minima. The same argument holds for *nearly discontinuous* landscapes that display high empirical bias. Both estimators are unbiased in expectation, and the high variance of FoBG should manifest itself in worse convergence rates. Yet, the high *empirical bias* in the finite-sample regime leads to low empirical variance and different minima, leading to performance that is indistinguishable from when the underlying landscape is truly discontinuous.

Combined with the benefits of stochasticity in Section 1, we believe that this might explain why zero-order methods in RL are solving problems for physical systems where deterministic (even *stochastic*) first order methods have struggled.

### Policy optimization case studies

To validate our results on policy optimization problems with differentiable simulators, we compare the performance of different gradients on time-stepping simulations written in torch. For all of our examples, we validate the correctness of the analytic gradients by comparing the values of FoBG and ZoBG on a one-step cost.

To empirically verify the various hypotheses made in this paper, we compare the performance of three gradient estimators: the FoBG and ZoBG, which uniformly utilizes first and zeroth-order gradients, and the AoBG, which utilizes our robust interpolation protocol.

Pushing: Trajectory optimization. We describe performance of gradients on the pushing (Figure 5) environment, where contact is modeled using the *penalty method* (i.e. stiff spring) with additional viscous damping on the velocities of the system. We use horizon of $H = 200$ to find the optimal force sequence of the first block to minimize distance between the second block and the goal position. Our results in Figure 8 show that for soft springs $({k = 10})$, the FoBG outperforms the ZoBG, but stiffer springs $({k = 1000})$ results in the ZoBG outperforming the FoBG. This confirms our hypothesis that the stiffness of contact models has direct correlations with the variance of the estimators, which in turn affects the convergence rate of optimization algorithms that use such estimators.

In addition, we note that the interpolated gradient AoBG is able to automatically choose between the two gradients that performs better by utilizing empirical variance as a statistical measure of performance.

Friction: Trajectory Optimization. We describe performance of gradients on the friction (Figure 4. ‣ 3.2 The “Empirical bias” phenomenon ‣ 3 Pitfalls of First-order Estimates ‣ Do Differentiable Simulators Give Better Policy Gradients?")) environment.

Although the FoBG initially converges faster in this environment, it is unaware of the discontinuity that occurs when it slides off the box. As a result, the performance quickly degrades after few iterations. On the other hand, the AoBG and ZoBG successfully optimize the trajectory, with AoBG showing slightly faster convergence.

Tennis: Policy optimization. Next, we describe the performance of different gradients on a tennis environment (similar to breakout), where the paddle needs to bounce the ball to some desired target location. We use a linear feedback policy with $d = 21$ parameters, and horizon of $H = 200$. In order to correctly obtain analytic gradients, we use continuous event detection with the time of impact formulation. The results of running policy optimization is presented in Figure 8.

While the ZoBG and the AoBG are successful in finding a policy that bounces the balls through different initial conditions, the FoBG suffers from the discontinuities of geometry, and still misses many of the balls. Furthermore, the AoBG still converges slightly faster than the ZoBG by utilizing first-order information.

## Discussion

In this section, we elaborate and discuss on some of the ramifications of our work.

Impact on Computation Time. The convergence rate of gradient descent in stochastic optimization scales directly with the variance of the estimator. For smooth and well-behaved landscapes, FoBG often converges faster since ${\text{Var}{\lbrack{{\overline{\nabla}}^{\lbrack 1\rbrack}F}\rbrack}} < {\text{Var}{\lbrack{{\overline{\nabla}}^{\lbrack 0\rbrack}F}\rbrack}}$. However, when there are discontinuities or near-discontinuities in the landscape, this promise no longer holds since gradient descent using FoBG might not converge due to bias. Indeed, Example 3.6. ‣ 3.2 The “Empirical bias” phenomenon ‣ 3 Pitfalls of First-order Estimates ‣ Do Differentiable Simulators Give Better Policy Gradients?") tells us that bias due to discontinuities can be interpreted as infinite variance. Under this interpretation, the convergence rate of gradient descent is ill-defined.

In practice; however, the computation cost of obtaining the gradient must be taken into consideration as well. Given the same number of samples $N$, the computation of FoBG is more costly than the ZoBG, as FoBG requires automatic differentiation through the computation graph while ZoBG simply requires evaluation. Thus, the benefits of convergence rates using the FoBG must justify the additional cost of computing them.

Implicit time-stepping. In our work, we have mainly addressed two classes of simulation methods for contact. The first uses the penalty method, which approximates contact via stiff springs, and the second uses event detection, which explicitly computes time-of-impact for automatic differentiation.

In addition to the ones covered, we note a third class of simulators that rely on optimization-based implicit time-stepping, which can be made differentiable by sensitivity analysis. These simulators suffer less from stiffness by considering more long-term behavior across each timestep; however, geometrical discontinuities can still remain problematic. We leave detailed empirical study using these simulators to future work.

Analytic Smoothing. Randomized smoothing relies on smoothing out the policy objective via the process of noise injection and sampling. However, one can also resort to *analytic smoothing*, which finds analytically smooth approximation of the underlying dynamics $\phi$. Modifying and smoothing $\phi$ directly also has the effect of smoothing the induced value function, though the resulting landscape will be different from the landscaped induced by appending noise to the policy output.

However, even when $\phi$ can be analytically smoothed, Monte-Carlo sampling is still required for optimization across initial conditions $\rho$. For such settings, the findings of Section 3.2 is still highly relevant, as the performance of FoBG still suffers from the stiffness of the smoothed approximation of $\phi$. However, as many smoothing methods provide access to parameters that control the strength of smoothing, algorithms may be able to take a curriculum-learning approach where dynamics become more realistic, and less smooth, as more iterations are taken for policy search.

## Conclusion

Do differentiable simulators give better policy gradients? We have shown that the answer depends intricately on the underlying characteristics of the physical systems. While Lipschitz continuous systems with reasonably bounded gradients may enjoy fast convergence given by the low variance of first-order estimators, using the gradients of differentiable simulators may *hurt* for problems that involve nearly/strictly discontinuous landscapes, stiff dynamics, or chaotic systems. Moreover, due to the empirical bias phenomenon, bias of first-order estimators in nearly/strictly discontinuous landscapes cannot be diagnosed from empirical variance alone. We believe that many challenging tasks that both RL and differentiable simulators try to address necessarily involve dealing with physical systems with such characteristics, such as those that are rich with contact.

These limitations of using differentiable simulators for planning and control need to be addressed from both the design of simulator and algorithms: from the simulator side, we have shown that certain modeling decisions such as stiffness of contact dynamics can have significant underlying consequences in the performance of policy optimization that uses gradients from these simulators. From the algorithm side, we have shown we can automate the procedure of deciding which one to use online via interpolation.
