<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Do Differentiable Simulators Give Better Policy Gradients?

Topics include Policy gradients, Reinforcement learning, Robustness, Planning, Control, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Differentiable simulators promise faster computation time for reinforcement learning by replacing zeroth-order gradient estimates of a stochastic objective with an estimate based on first-order gradients. However, it is yet unclear what factors decide the performance of the two estimators on complex landscapes that involve long-horizon planning and control on physical systems, despite the crucial relevance of this question for the utility of differentiable simulators. We show that characteristics of certain physical systems, such as stiffness or discontinuities, may compromise the efficacy of the first-order estimator, and analyze this phenomenon through the lens of bias and variance. We additionally propose an alpha-order gradient estimator, with alpha , which correctly utilizes exact gradients to combine the efficiency of first-order estimates with the robustness of zero-order methods. We demonstrate the pitfalls of traditional estimators and the advantages of the alpha-order estimator on some numerical examples.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Consider the problem of minimizing a *stochastic objective*, At the heart of many algorithms for reinforcement learning (RL) lies *zeroth-order* estimation of the gradient $\nabla F$. Yet, in domains that deal with structured systems, such as linear control, physical simulation, or robotics, it is possible to obtain *exact* gradients of $f$, which can also be used to construct a *first-order* estimate of $\nabla F$. The availability of both options begs the question: given access to exact gradients of $f$, which estimator should we prefer?

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In stochastic optimization, the theoretical benefits of using first-order estimates of $\nabla F$ over zeroth-order ones have mainly been understood through the lens of variance and convergence rates: the first-order estimator often (*not always*) results in much less variance compared to the zeroth-order one, which leads to faster convergence rates to a local minima of general nonconvex smooth objective functions.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, the landscape of RL objectives that involve long-horizon sequential decision making (e.g. policy optimization) is challenging to analyze, and convergence properties in these landscapes are relatively poorly understood, except for structured settings such as finite-state MDPs or linear control. In particular, physical systems with contact, as we show in Figure 1, can display complex characteristics including nonlinearities, non-smoothness, and discontinuities.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Nevertheless, lessons from convergence rate analysis tell us that there may be benefits to using the exact gradients even for these complex physical systems. Such ideas have been championed through the term "differentiable simulation", where forward simulation of physics is programmed in a manner that is consistent with automatic differentiation, or computation of analytic derivatives. These methods have shown promising results in decreasing computation time compared to zeroth-order methods.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Existing literature in differentiable simulation mainly focuses on the use of exact gradients for *deterministic* optimization. However, show that using exact gradients for a deterministic objective can lead to suboptimal behavior of certain systems due to their landscapes. In these systems, stochasticity can be used to *regularize* the landscapes with randomized smoothing. We illustrate how the landscapes change upon injecting noise (Figure 1), and list some benefits of considering a *surrogate* stochastic objective.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Stochasticity smooths local minima. As noted, stochasticity can alleviate some of the high-frequency local minima that deterministic gradients will be stuck. For instance, the small discontinuity on the right side of Figure 1.B is filtered by Gaussian smoothing.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Stochasticity alleviates flat regions. In systems of Figure 1, the gradients in some of the regions can be completely flat. This stalls progress of gradient descent. The stochastic objective, however, still has non-zero gradient as some samples escape the flat regions and provide an informative direction of improvement.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Stochasticity encodes robustness. In Figure 1.C, following the gradient to increase the transferred momentum causes the ball to miss the pivot and land in a high-cost region. In contrast, the stochastic objective has a local minimum within the safe region, as the samples provide information about missing the pivot.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Thus, our work attempts to compare two versions of gradient estimators in the stochastic setting: the first-order estimator and the zeroth-order one. This setting rules out the case that zeroth-order estimates perform better simply because of stochasticity, and sets equal footing for the two methods.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

When $f$ is continuous, these quantities both converge to the same quantity ($\nabla F$) in expectation. We first show that even with continuous $f$, the first-order gradient estimate *can* result in more variance than the zeroth-order one due to the *stiffness* of dynamics or due to compounding of gradients in chaotic systems.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

In addition, we show that the assumption of continuous $f$ can be violated in many relevant physical systems that are nearly/strictly *discontinuous* in the underlying landscape. These discontinuities are commonly caused by contact and geometrical constraints. We provide minimal examples to highlight specific challenges in Figure 1. These are not mere pathologies, but abstractions of more complicated examples that are rich with contact, such as robotic manipulation.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that the presence of such discontinuities causes the first-order gradient estimator to be biased, while the zeroth-order one still remains unbiased under discontinuities. Furthermore, we show that stiff continuous approximations of discontinuities, even if asymptotically unbiased, can still suffer from what we call *empirical bias* under finite-sample settings. This results in a bias-variance tradeoff between the biased first-order estimator and the *often* high-variance, yet unbiased zeroth-order estimator. Intriguingly, we find that the bias-variance tradeoff in this setting manifests itself not through convergence rates, but through different local minima. This shows that the two estimators may fundamentally operate on different landscapes implicitly.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

The presence of discontinuities need not indicate that we need to commit ourselves to uniformly using one of the estimators. Many physical systems are *hybrid* by nature; they consist of smooth regions that are separated by manifolds of non-smoothness or discontinuities. This suggests that we may be able to utilize the first-order estimates far away from these manifolds to obtain benefits of convergence rates, while switching to zeroth-order ones in the vicinity of discontinuities to obtain unbiased estimates.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

For this purpose, we further attempt to answer the question: how can we then correctly utilize exact gradients of $f$ for variance reduction when we know the objective is nearly discontinuous? Previous works show that the two estimators can be combined by interpolating based on empirical variance. However, we show that in the presence of near-discontinuities, selecting based on empirical variance alone can lead to highly inaccurate estimates of $\nabla F$, and propose a robustness constraint on the accuracy of the interpolated estimate to remedy this effect.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions. We 1) shed light on some of the inherent problems of RL using differentiable simulators, and answer which gradient estimator can be more useful under different characteristics of underlying systems such as discontinuities, stiffness, and chaos; and 2) present the $\alpha$-order gradient estimator, a robust interpolation strategy between the two gradient estimators that utilizes exact gradients without falling into the identified pitfalls of the previous methods.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

We hope both contributions inspire algorithms for policy optimization using differentiable simulators, as well as design guidelines for new and existing simulators.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

Our rationale for Gaussian $p$ is that we view $\mathbf{w}_{1:H}$ as *smoothing* to regularize the optimization landscape. To simplify the main text, we take $\mathbf{x}_{1}$ to be deterministic ($\rho$ is a dirac-delta), with general $\rho$ being addressed in the appendix.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Assumption 2.2", "weight": 1.0} -->

We assume that the policy $\pi$ is continuously differentiable everywhere, and the dynamics $\phi$, as well as the cost $c_{h}$ have polynomial growth.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 2.2", "weight": 1.0} -->

Even when the costs or dynamics are *not* differentiable, the expected cost $F{({\mathbf{θ}})}$ is differentiable due to the smoothing $\overline{\mathbf{w}}$. ${\nabla F}{({\mathbf{θ}})}$ is referred to as the *policy gradient*.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 2.2", "weight": 1.0} -->

Zeroth-order estimator. The policy gradient can be estimated only using samples of the function values.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Pitfalls of First-order Estimates", "weight": 1.0} -->

What are the cases for which we would prefer to use the ZoBG over the FoBG in policy optimization using differentiable simulators? Throughout this section, we analyze the performance of the two estimators through their bias and variance properties, and find pathologies where using the first-order estimator blindly results in worse performance.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Bias under discontinuities", "weight": 1.0} -->

Under standard regularity conditions, it is well-known that both estimators are unbiased estimators of the true gradient ${\nabla F}{({\mathbf{θ}})}$. However, care must be taken to define these conditions precisely. Fortunately, the ZoBG is still unbiased under mild assumptions.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Bias of FoBG under discontinuities", "weight": 1.0} -->

The FoBG can fail when applied to discontinuous landscapes. We illustrate a simple case of biasedness through a counterexample.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Example 3.3 (Heaviside)", "weight": 1.0} -->

It is worth noting that the empirical variance of the FoBG estimator in this example is zero, since all the samples are identically zero. On the other hand, the ZoBG escapes this problem and provides an unbiased estimate, since it always takes finite intervals that include the integral of the delta.

<!-- chunk {"id": "body-0027", "role": "body", "section": "The \"Empirical bias\" phenomenon", "weight": 1.0} -->

One might argue that *strict* discontinuity is simply an artifact of modeling choice in simulators; indeed, many simulators approximate discontinuous dynamics as a limit of continuous ones with growing Lipschitz constant. In this section, we explain how this can lead to a phenomenon we call *empirical bias*, where the FoBG appears to have low empirical variance, but is still highly inaccurate; i.e. it "looks" biased when a finite number of samples are used. Through this phenomenon, we claim that performance degradation of first-order gradient estimates do not require strict discontinuity, but is also present in continuous, yet *stiff* approximations of discontinuities. ^11^1We say that a continuous function $f$ is stiff at $x$ if the magnitude of the gradient $\|{{\nabla f}{(x)}}\|$ is high.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Example 3.6 (Coulomb friction)", "weight": 1.0} -->

The Coulomb model of friction is discontinuous in the relative tangential velocity between two bodies. In many simulators, it is common to consider a continuous approximation instead. We idealize such approximations through a piecewise linear relaxation of the Heaviside that is continuous, parametrized by the width of the middle linear region $\nu$ (which corresponds to *slip tolerance*).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Example 3.6 (Coulomb friction)", "weight": 1.0} -->

In particular, setting $c_{\sigma}:=\frac{1}{\sqrt{2\pi}\sigma}$, then at ${\mathbf{θ}} = {\nu/2}$, ${{\nabla F_{\nu}}{({\mathbf{θ}})}} = c_{\sigma}$, whereas, with probability at least $c_{\sigma}\nu$, ${{\nabla f_{\nu}}{({\mathbf{θ}},\mathbf{w})}} = 0$. Hence, the FoBG has $({c_{\sigma}\nu},c_{\sigma},0)$ empirical bias, and its variance scales with $1/\nu$ as $\nu\rightarrow 0$. The limiting $\nu = 0$ case, corresponding to the Coulomb model, is the Heaviside from Example 3.3. ‣ Bias of FoBG under discontinuities.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Example 3.6 (Coulomb friction)", "weight": 1.0} -->

‣ 3.1 Bias under discontinuities ‣ 3 Pitfalls of First-order Estimates ‣ Do Differentiable Simulators Give Better Policy Gradients?"), where the limit of high empirical bias, as well as variance, becomes biased in expectation (but, surprisingly, zero variance!). We empirically illustrate this effect in Figure 4. ‣ 3.2 The “Empirical bias” phenomenon ‣ 3 Pitfalls of First-order Estimates ‣ Do Differentiable Simulators Give Better Policy Gradients?"). We also note that more complicated models of friction (e.g. that incorporates the Stribeck effect ) would suffer similar problems.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Example 3.7", "weight": 1.0} -->

(Geometric Discontinuity). Discontinuity also comes from surface normals. We show this in Figure 3, where balls that collide with a rectangular geometry create discontinuities. It is possible to make a continuous relaxation by considering smoother geometry, depicted by the addition of the dome in Figure 3. While this makes FoBG no longer biased asymptotically, the stiffness of the relaxation results in high empirical bias.

<!-- chunk {"id": "body-0032", "role": "body", "section": "High variance first-order estimates", "weight": 1.0} -->

Even in the absence of empirical bias, we present other cases in which FoBG suffers simply due to high variance.

<!-- chunk {"id": "body-0033", "role": "body", "section": "High variance first-order estimates", "weight": 1.0} -->

Scenario 1: Persistent stiffness. When the dynamics are *stiff* ^22^2We say that a discrete-time dynamical system is stiff if the mapping function $\phi$ is stiff. Note that when $\phi$ contains forces from spring-like components, $\|{\nabla\phi}\|$ scales with the spring constant. Thus, the presence of a stiff spring leads to a stiff system., such as contact models with stiff spring approximations, the high norm of the gradient can contribute to high variance of the FoBG.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Example 3.8", "weight": 1.0} -->

(Pushing with stiff contact). We demonstrate this phenomenon through a simple 1D pushing example in Figure 5, where the ZoBG has lower variance than the FoBG as stiffness increases, until numerical semi-implicit integration becomes unstable under a fixed timestep.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Example 3.8", "weight": 1.0} -->

In practice, lowering the timestep can alleviate the issue at the cost of more computation time. Less stiff formulations of contact dynamics also addresses this problem effectively.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Example 3.8", "weight": 1.0} -->

Scenario 2: Chaos. As noted, even if the gradient of the dynamics is small at every $h$, their compounding product can cause $\|{\nabla_{\mathbf{θ}}V_{1}}\|$ to be large if the system is chaotic. Yet, in expectation, the gradient of the stochastic objective ${\nabla F} = {{\nabla{\mathbb{E}}}{\lbrack V_{1}\rbrack}}$ can be benign and well-behaved.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Example 3.9", "weight": 1.0} -->

(Chaos of double pendulum). We demonstrate this in Figure 6 for a classic chaotic system of the double pendulum. As the horizon of the trajectory increases, the variance of FoBG becomes higher than that of ZoBG.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Comparison to ZoBG", "weight": 1.0} -->

Compared to the pitfalls of FoBG, the ZoBG variance can be bounded as follows.

<!-- chunk {"id": "body-0039", "role": "body", "section": "$\\alpha$-order Gradient Estimator", "weight": 1.0} -->

Previous examples give us insight on which landscapes are better fit for first-order estimates of policy gradient, and which are better fit for zeroth-order ones. As shown in Figure 7, even on a single policy optimization objective, it is best to adaptively switch between the first and zeroth-order estimators depending on the local characteristics of the landscape. In this section, we propose a strategy to achieve this adaptively, interpolating between the two estimators to reap the benefits of both approaches simultaneously.

<!-- chunk {"id": "body-0040", "role": "body", "section": "A robust interpolation protocol", "weight": 1.0} -->

A potential approach might be to select $\alpha$ based on achieving minimum variance, considering empirical variance as an estimate. However, in light of the *empirical bias* phenomenon detailed in Section 3 (or even actual bias in the presence of discontinuities), we see that the empirical variance is unreliable, and can lead to inaccurate estimates for our setting.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Landscape analysis on examples", "weight": 1.0} -->

Though we have characterized the bias-variance characteristics of different gradients, their convergence properties in landscapes of physical systems remain to be investigated. We visualize the performance of fixed-step gradient descent with the FoBG, ZoBG, and AoBG on examples of Figure 1.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Landscape analysis on examples", "weight": 1.0} -->

Ball with wall. On the system of Figure 1.B, the FoBG fails to make progress at the region of flatness, while the ZoBG and AoBG successfully find the minima of the landscape (Figure 7). In addition, the interpolation scheme switches to prioritizing ZoBG near discontinuities, while using more information from FoBG far from discontinuities; as a result, the variance of AoBG is lower than that of ZoBG.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Landscape analysis on examples", "weight": 1.0} -->

Angular momentum transfer. Next, we show results for the momentum transfer system of Figure 1.C in Figure 7. Running gradient descent results in both the ZoBG and AoBG converging to the robust local minima of the solution. However, the bias of FoBG forces it off the cliff and the optimizer is unable to recover. Again, our interpolation scheme smoothly switches to prioritizing the ZoBG near the discontinuity, enabling it to stay within the safe region while maximizing the transferred momentum.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Landscape analysis on examples", "weight": 1.0} -->

Bias-variance leads to different minima. Through these examples with discontinuities, we claim that the bias-variance characteristics of gradients in these landscapes not only lead to different convergence rates, but convergence to different minima. The same argument holds for *nearly discontinuous* landscapes that display high empirical bias. Both estimators are unbiased in expectation, and the high variance of FoBG should manifest itself in worse convergence rates. Yet, the high *empirical bias* in the finite-sample regime leads to low empirical variance and different minima, leading to performance that is indistinguishable from when the underlying landscape is truly discontinuous.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Landscape analysis on examples", "weight": 1.0} -->

Combined with the benefits of stochasticity in Section 1, we believe that this might explain why zero-order methods in RL are solving problems for physical systems where deterministic (even *stochastic*) first order methods have struggled.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Policy optimization case studies", "weight": 1.0} -->

To validate our results on policy optimization problems with differentiable simulators, we compare the performance of different gradients on time-stepping simulations written in torch. For all of our examples, we validate the correctness of the analytic gradients by comparing the values of FoBG and ZoBG on a one-step cost.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Policy optimization case studies", "weight": 1.0} -->

To empirically verify the various hypotheses made in this paper, we compare the performance of three gradient estimators: the FoBG and ZoBG, which uniformly utilizes first and zeroth-order gradients, and the AoBG, which utilizes our robust interpolation protocol.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Policy optimization case studies", "weight": 1.0} -->

Pushing: Trajectory optimization. We describe performance of gradients on the pushing (Figure 5) environment, where contact is modeled using the *penalty method* (i.e. stiff spring) with additional viscous damping on the velocities of the system. We use horizon of $H = 200$ to find the optimal force sequence of the first block to minimize distance between the second block and the goal position. Our results in Figure 8 show that for soft springs $({k = 10})$, the FoBG outperforms the ZoBG, but stiffer springs $({k = 1000})$ results in the ZoBG outperforming the FoBG. This confirms our hypothesis that the stiffness of contact models has direct correlations with the variance of the estimators, which in turn affects the convergence rate of optimization algorithms that use such estimators.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Policy optimization case studies", "weight": 1.0} -->

In addition, we note that the interpolated gradient AoBG is able to automatically choose between the two gradients that performs better by utilizing empirical variance as a statistical measure of performance.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Policy optimization case studies", "weight": 1.0} -->

Friction: Trajectory Optimization. We describe performance of gradients on the friction (Figure 4. ‣ 3.2 The “Empirical bias” phenomenon ‣ 3 Pitfalls of First-order Estimates ‣ Do Differentiable Simulators Give Better Policy Gradients?")) environment.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Policy optimization case studies", "weight": 1.0} -->

Although the FoBG initially converges faster in this environment, it is unaware of the discontinuity that occurs when it slides off the box. As a result, the performance quickly degrades after few iterations. On the other hand, the AoBG and ZoBG successfully optimize the trajectory, with AoBG showing slightly faster convergence.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Policy optimization case studies", "weight": 1.0} -->

Tennis: Policy optimization. Next, we describe the performance of different gradients on a tennis environment (similar to breakout), where the paddle needs to bounce the ball to some desired target location. We use a linear feedback policy with $d = 21$ parameters, and horizon of $H = 200$. In order to correctly obtain analytic gradients, we use continuous event detection with the time of impact formulation. The results of running policy optimization is presented in Figure 8.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Policy optimization case studies", "weight": 1.0} -->

While the ZoBG and the AoBG are successful in finding a policy that bounces the balls through different initial conditions, the FoBG suffers from the discontinuities of geometry, and still misses many of the balls. Furthermore, the AoBG still converges slightly faster than the ZoBG by utilizing first-order information.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this section, we elaborate and discuss on some of the ramifications of our work.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Discussion", "weight": 1.5} -->

Impact on Computation Time. The convergence rate of gradient descent in stochastic optimization scales directly with the variance of the estimator. For smooth and well-behaved landscapes, FoBG often converges faster since ${\text{Var}{\lbrack{{\overline{\nabla}}^{\lbrack 1\rbrack}F}\rbrack}} < {\text{Var}{\lbrack{{\overline{\nabla}}^{\lbrack 0\rbrack}F}\rbrack}}$. However, when there are discontinuities or near-discontinuities in the landscape, this promise no longer holds since gradient descent using FoBG might not converge due to bias. Indeed, Example 3.6. ‣ 3.2 The “Empirical bias” phenomenon ‣ 3 Pitfalls of First-order Estimates ‣ Do Differentiable Simulators Give Better Policy Gradients?") tells us that bias due to discontinuities can be interpreted as infinite variance. Under this interpretation, the convergence rate of gradient descent is ill-defined.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Discussion", "weight": 1.5} -->

In practice; however, the computation cost of obtaining the gradient must be taken into consideration as well. Given the same number of samples $N$, the computation of FoBG is more costly than the ZoBG, as FoBG requires automatic differentiation through the computation graph while ZoBG simply requires evaluation. Thus, the benefits of convergence rates using the FoBG must justify the additional cost of computing them.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Discussion", "weight": 1.5} -->

Implicit time-stepping. In our work, we have mainly addressed two classes of simulation methods for contact. The first uses the penalty method, which approximates contact via stiff springs, and the second uses event detection, which explicitly computes time-of-impact for automatic differentiation.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Discussion", "weight": 1.5} -->

In addition to the ones covered, we note a third class of simulators that rely on optimization-based implicit time-stepping, which can be made differentiable by sensitivity analysis. These simulators suffer less from stiffness by considering more long-term behavior across each timestep; however, geometrical discontinuities can still remain problematic. We leave detailed empirical study using these simulators to future work.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Discussion", "weight": 1.5} -->

Analytic Smoothing. Randomized smoothing relies on smoothing out the policy objective via the process of noise injection and sampling. However, one can also resort to *analytic smoothing*, which finds analytically smooth approximation of the underlying dynamics $\phi$. Modifying and smoothing $\phi$ directly also has the effect of smoothing the induced value function, though the resulting landscape will be different from the landscaped induced by appending noise to the policy output.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Discussion", "weight": 1.5} -->

However, even when $\phi$ can be analytically smoothed, Monte-Carlo sampling is still required for optimization across initial conditions $\rho$. For such settings, the findings of Section 3.2 is still highly relevant, as the performance of FoBG still suffers from the stiffness of the smoothed approximation of $\phi$. However, as many smoothing methods provide access to parameters that control the strength of smoothing, algorithms may be able to take a curriculum-learning approach where dynamics become more realistic, and less smooth, as more iterations are taken for policy search.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Do differentiable simulators give better policy gradients? We have shown that the answer depends intricately on the underlying characteristics of the physical systems. While Lipschitz continuous systems with reasonably bounded gradients may enjoy fast convergence given by the low variance of first-order estimators, using the gradients of differentiable simulators may *hurt* for problems that involve nearly/strictly discontinuous landscapes, stiff dynamics, or chaotic systems. Moreover, due to the empirical bias phenomenon, bias of first-order estimators in nearly/strictly discontinuous landscapes cannot be diagnosed from empirical variance alone. We believe that many challenging tasks that both RL and differentiable simulators try to address necessarily involve dealing with physical systems with such characteristics, such as those that are rich with contact.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusion", "weight": 1.5} -->

These limitations of using differentiable simulators for planning and control need to be addressed from both the design of simulator and algorithms: from the simulator side, we have shown that certain modeling decisions such as stiffness of contact dynamics can have significant underlying consequences in the performance of policy optimization that uses gradients from these simulators. From the algorithm side, we have shown we can automate the procedure of deciding which one to use online via interpolation.
