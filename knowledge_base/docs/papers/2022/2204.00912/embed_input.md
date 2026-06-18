<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Escaping High-order Saddles in Policy Optimization for Linear Quadratic Gaussian (LQG) Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

First order policy optimization has been widely used in reinforcement learning. It guarantees to find the optimal policy for the state-feedback linear quadratic regulator (LQR). However, the performance of policy optimization remains unclear for the linear quadratic Gaussian (LQG) control where the LQG cost has spurious suboptimal stationary points. In this paper, we introduce a novel perturbed policy gradient (PGD) method to escape a large class of bad stationary points (including high-order saddles). In particular, based on the specific structure of LQG, we introduce a novel reparameterization procedure which converts the iterate from a high-order saddle to a strict saddle, from which standard random perturbations in PGD can escape efficiently. We further characterize the high-order saddles that can be escaped by our algorithm.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we revisit the linear quadratic Gaussian (LQG) control, one of the most fundamental problems in control theory, from a modern optimization view. In brief, we focus on a continuous-time linear time-invariant (LTI) system

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

where ${{x{(t)}} \in {\mathbb{R}}^{n}},{{{u{(t)}} \in {\mathbb{R}}^{m}},{{y{(t)}} \in {\mathbb{R}}^{p}}}$ are the state, control input, and measurement (output) vector at time $t$, respectively, and $w{(t)}$, $v{(t)}$ are white Gaussian noises with intensity matrices $W \succeq 0$ and $V \succ 0$, respectively. The goal is to design a controller (i.e., policy) based on partial measurements $y{(t)}$ to minimize a quadratic cost

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A special case is the linear quadratic regulator (LQR), where we have direct access to the state $x$ (i.e., ${{y{(t)}} = {x{(t)}}},{{{v{(t)}} = 0},{{\forall t} \in {\mathbb{R}}}}$ in 1 Control")). It is known that the optimal policy for the LQR is in the form of static state feedback ${u{(t)}} = {Kx{(t)}}$, where $K \in {\mathbb{R}}^{m \times n}$ is a constant matrix that can be obtained by solving a Riccati equation. On the other hand, when the state is not directly observed, the policy that minimizes 2 Control") is a dynamical controller of the form

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

where the optimal parameters $\mathsf{K}^{\ast}:={(A_{\mathsf{K}}^{\ast},B_{\mathsf{K}}^{\ast},C_{\mathsf{K}}^{\ast})}$ can be obtained by solving two Riccati equations (see Section II-A Control")). Algorithms for solving Riccati equations are well-studied, including iterative algorithms, algebraic solution methods, and semidefinite optimization. All these methods are model-based and explicitly rely on the system model 1 Control"). Recently, policy gradient methods have achieved impressive results for many challenging problems. These methods directly optimize the quadratic cost 2 Control") as a function of the policy class $\mathsf{K} = {(A_{\mathsf{K}},B_{\mathsf{K}},C_{\mathsf{K}})}$ via gradient descent or its variants. They can be further made model-free, bypassing an explicit estimation of the model 1 Control").

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The flexibility of model-free control has stimulated a growing interest in investigating foundations of policy gradient methods for classical control problems.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

While it is guaranteed to obtain the optimal controller for LQR or LQG via classical model-based methods, such optimality guarantee is more difficult when using policy gradient methods since the cost 2 Control") is typically nonconvex in the policy space. For LQR, recent work has shown that although the LQR cost is nonconvex, it is gradient dominant and coersive, and has a unique stationary point under very mild conditions, rendering the convergence of policy gradient methods to the globally optimal controller. On the other hand, the LQG cost is neither gradient dominant nor coersive, and there may exist spurious saddle points, making it challenging for policy gradient to find the optimal controller.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Saddle points do not always destroy the performance of policy gradient methods. Suitable perturbed policy gradient methods are able to escape strict saddle points whose Hessian has at least one strictly negative eigenvalue. However, it is shown in \[20, Theorem 4.2\] that the Hessian of the LQG cost at a saddle point can even degenerate to zero. We denote the saddle point whose Hessian does not give escaping directions as a *high-order saddle point*. Perturbed policy gradient methods may thus get stuck and take an exponential number of iterations to escape high-order saddle points.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

All the (strict or high-order) saddle points of LQG discussed in are due to a loss of controllability and/or observability for the controller $(A_{\mathsf{K}},B_{\mathsf{K}},C_{\mathsf{K}})$ in 3 Control") (i.e., non-minimal controllers). Indeed, any stationary point corresponds to a full-order minimal controller cannot be saddle and it is instead globally optimal. Further, many intrigue landscape properties of LQG are brought by a classical notion of similarity transformations that induces a symmetry structure. In this paper, we raise a natural question of whether this induced symmetry structure allows us to reveal more information about high-order saddles of LQG such that suitable perturbed policy gradient methods can escape those points. We provide a positive answer to this question.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In particular, we first show that any stationary point after model reduction remains to be stationary. This gives a classification of the stationary points: all bad (suboptimal or saddle) stationary points after model reduction become lower-order and form new stationary points with the same LQG cost.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We then reveal an intriguing transfer function $\mathbf{G}{(s)}$ at any stationary point $(A_{\mathsf{K}},B_{\mathsf{K}},C_{\mathsf{K}})$: 1) if $(A_{\mathsf{K}},B_{\mathsf{K}},C_{\mathsf{K}})$ is globally optimal, the function $\mathbf{G}{(s)}$ is identically zero, ${\forall s} \in {\mathbb{C}}$; 2) if $\mathbf{G}{(s)}$ is not identically zero, we can perturb $(A_{\mathsf{K}},B_{\mathsf{K}},C_{\mathsf{K}})$ to get a new stationary point with the same LQG cost, which is a strict saddle with probability one. Standard perturbed policy gradient (PGD) methods can thus escape this new strict saddle.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We emphasize that our PGD method include perturbations on two parts: 1) a novel structural perturbation on the stationary point $(A_{\mathsf{K}},B_{\mathsf{K}},C_{\mathsf{K}})$; 2) a standard random perturbation on gradients. This combination enables escaping a large class of bad stationary points (including high-order saddles) in LQG.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Review of LQG control", "weight": 1.0} -->

The classical LQG control problem is defined as

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A Review of LQG control", "weight": 1.0} -->

where $J{(u)}$ is defined in 2 Control") with $Q \succeq 0$ and $R \succ 0$. In 4 Control"), the input $u{(t)}$ depends on all past observation $y{(\tau)}$ with $\tau < t$. We make the following standard assumption.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

$(A,B)$ and $(A,W^{1/2})$ are controllable, and $(C,A)$ and $(Q^{1/2},A)$ are observable.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The optimal solution to 4 Control") is a dynamical controller in the form of 3 Control"), in which ${\xi{(t)}} \in {\mathbb{R}}^{q}$ is the controller internal state, and $A_{\mathsf{K}} \in {\mathbb{R}}^{q \times q}$, $B_{\mathsf{K}} \in {\mathbb{R}}^{q \times p}$, $C_{\mathsf{K}} \in {\mathbb{R}}^{m \times q}$ specify the dynamics of the controller. While $q$ can be any positive number, one does not have to use $q > n$ and the optimal controller has $q = n$, given by algebraic Riccati equations (AREs) \[3, Thm. 14.7\]. Precisely, let $P,S$ be the unique positive semidefinite solutions to the following AREs

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Then, the parameters of an optimal controller to 4 Control") are

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

where $L = {PC^{\mathsf{T}}V^{- 1}}$, $M = {R^{- 1}B^{\mathsf{T}}S}$. The optimal solution $(A_{\mathsf{K}}^{\star},B_{\mathsf{K}}^{\star},C_{\mathsf{K}}^{\star})$ is not unique in the state-space domain. Any similarity transformation leads to another equivalent optimal controller (they correspond to the same transfer function in the frequency domain).

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-B Problem Statement", "weight": 1.0} -->

In this paper, we embrace the spirit of and view the LQG problem 4 Control") from a modern optimization perspective. We consider the policy class $(A_{\mathsf{K}},B_{\mathsf{K}},C_{\mathsf{K}})$ in 3 Control"), and the closed-loop matrix becomes

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B Problem Statement", "weight": 1.0} -->

The set of internally stabilizing policies \[3, Chapter 13\] is

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-B Problem Statement", "weight": 1.0} -->

Let ${J_{q}{(\mathsf{K})}}:{\mathcal{C}_{q}\rightarrow{\mathbb{R}}}$ denote the corresponding LQG cost 2 Control") for each stabilizing policy in $\mathcal{C}_{q}$. It is known \[20, Lemmas 2.3 & 2.4\] that this function $J_{q}{(\mathsf{K})}$ is real analytic on $\mathcal{C}_{q}$ and admits efficient computation.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Stationary Points and Their Hessians", "weight": 1.0} -->

The LQG problem 4 Control") has an inherent symmetry structure induced by the notion of similarity transformation. Let ${GL}_{q}$ denote the set of $q \times q$ invertible matrices. Given $q \geq 1$ such that $\mathcal{C}_{q} \neq \varnothing$, the following map $\mathcal{T}_{q}:{{{GL}_{q} \times \mathcal{C}_{q}}\rightarrow\mathcal{C}_{q}}$ represents similarity transformations

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A Classification of stationary points", "weight": 1.0} -->

The symmetry via similarity transformations brings rich and complicated landscape properties of 4 Control"). Here, we show that the underlying symmetry also allows a classification of stationary points of LQG 4 Control"). The lemma below gives an explicit relationship among the gradients of $J_{q}{(\mathsf{K})}$ at $\mathsf{K}$ and $\mathcal{T}_{q}(T,\mathsf{K})$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 1 (Non-minimal globally optimal controllers)", "weight": 1.0} -->

Note that a controller in the form of 13 Control") might still be globally optimal to 4 Control"); See Example 2 Control") below. This happens when the solutions $(A_{\mathsf{K}}^{\star},B_{\mathsf{K}}^{\star},C_{\mathsf{K}}^{\star})$ 6 Control") from the Riccati equations 5 Control") are not minimal, i.e. $(A_{\mathsf{K}}^{\star},B_{\mathsf{K}}^{\star})$ is not controllable or $(C_{\mathsf{K}}^{\star},A_{\mathsf{K}}^{\star})$ is not observable or both.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 1 (Non-minimal globally optimal controllers)", "weight": 1.0} -->

We conjecture that a random LQG instance should have $(A_{\mathsf{K}}^{\star},B_{\mathsf{K}}^{\star},C_{\mathsf{K}}^{\star})$ in 6 Control") being minimal with probability one. An exact characterization is left for future work. $\square$

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-B Hessian of stationary points", "weight": 1.0} -->

Once a policy gradient method reaches a stationary point, if the stationary point corresponds to a minimal controller, it has found a globally optimal solution to 4 Control"). If the stationary point does not correspond to a minimal controller, we can bring it into the form of (13 Control")), for which we have the following characterization of its hessian.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 2 (Sufficiency of ${\\mathbf{G}{(s)}} \\equiv 0$ for global optimality and its interpretation)", "weight": 1.0} -->

Theorem 2 Control") holds with $q = n$, so ${{\mathbf{G}{(s)}} \equiv 0},{{\forall s} \in {\mathbb{C}}}$ is also true when $\mathsf{K}$ comes from the Riccati equations. In this case, we expect that $\mathbf{G}{(s)}$ in 15 Control") should have a nice control-theoretic interpretation. It is interesting to further investigate whether ${{\mathbf{G}{(s)}} \equiv 0},{{\forall s} \in {\mathbb{C}}}$ is sufficient (or some other suitable conditions are needed) to certify the global optimality of $\overset{\sim}{\mathsf{K}}$. $\square$

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 2 (Sufficiency of ${\\mathbf{G}{(s)}} \\equiv 0$ for global optimality and its interpretation)", "weight": 1.0} -->

We conclude this section by presenting three explicit LQG examples to illustrate Theorem 2 Control").

<!-- chunk {"id": "body-0030", "role": "body", "section": "Example 1", "weight": 1.0} -->

We first consider the famous Doyle's LQG example, which has system matrices

<!-- chunk {"id": "body-0031", "role": "body", "section": "Example 1", "weight": 1.0} -->

The globally optimal LQG controller from 6 Control") is

<!-- chunk {"id": "body-0032", "role": "body", "section": "Example 1", "weight": 1.0} -->

We further compute the matrices in 16 Control") (their values can be found in the appendix), and we have

<!-- chunk {"id": "body-0033", "role": "body", "section": "Example 1", "weight": 1.0} -->

This result that $\mathbf{G}{(s)}$ being identically zero is expected from Theorem 2 Control") since $\mathsf{K}^{\star}$ is globally optimal. $\square$

<!-- chunk {"id": "body-0034", "role": "body", "section": "Example 1", "weight": 1.0} -->

We then consider \[20, Example 7\] for which the globally optimal LQG controller is non-minimal in $\mathcal{C}_{n}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Example 2", "weight": 1.0} -->

Consider an LQG instance with matrices

<!-- chunk {"id": "body-0036", "role": "body", "section": "Example 2", "weight": 1.0} -->

The globally optimal controller from 6 Control") is given by

<!-- chunk {"id": "body-0037", "role": "body", "section": "Example 2", "weight": 1.0} -->

Four zero eigenvalues are expected, due to the symmetry by similarity transformations, and the other zero is caused by the unobservablility of $(C_{\mathsf{K}}^{\ast},A_{\mathsf{K}}^{\ast})$. Consider two reduced-order controllers

<!-- chunk {"id": "body-0038", "role": "body", "section": "Example 2", "weight": 1.0} -->

both of which are globally optimal. Thus, the following two full-order controllers

<!-- chunk {"id": "body-0039", "role": "body", "section": "Example 2", "weight": 1.0} -->

are globally optimal as well. From Theorem 2 Control"), we expect ${\mathbf{G}{(s)}} \equiv 0$ for both ${\overset{\sim}{\mathsf{K}}}_{1}$ and ${\overset{\sim}{\mathsf{K}}}_{2}$. For both of them, we can compute (details are in Appendix D) that

<!-- chunk {"id": "body-0040", "role": "body", "section": "Example 2", "weight": 1.0} -->

Finally, we consider an LQG problem with a high-order saddle point. This high-order saddle point is predicted in Theorem 2 Control") and \[20, Theorem 4.2\].

<!-- chunk {"id": "body-0041", "role": "body", "section": "Example 3", "weight": 1.0} -->

Consider an LQG instance with an open-loop stable system, in which the problem data are

<!-- chunk {"id": "body-0042", "role": "body", "section": "Example 3", "weight": 1.0} -->

with weight matrices ${{W = Q = I_{2}},{V = R = 1}}.$ Since this example is open-loop stable, \[20, Theorem 4.2\] guarantees that $\overset{\sim}{\mathsf{K}} = \begin{bmatrix}
\end{bmatrix} \in \mathcal{C}_{2}$ with any stable $\Lambda \in {\mathbb{R}}^{2 \times 2}$ is a stationary point. At this controller, we can compute that the transfer function in 15 Control") is

<!-- chunk {"id": "body-0043", "role": "body", "section": "Example 3", "weight": 1.0} -->

The zero set $\mathcal{Z} = {\{ 0.5\}}$ contains a single value. For any stable $\Lambda$ with ${{eig}{({- \Lambda})}} \nsubseteq \mathcal{Z}$, the Hessian is indefinite by Theorem 2 Control"). For instance, with $\Lambda = {- {{diag}{(0.5,0.1)}}}$, the Hessian is indefinite with eigenvalues ${\lambda_{1} = 0.0561},{{\lambda_{2} = {- 0.0561}},{{\lambda_{i} = 0},{i = {3,\ldots,8}}}}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Example 3", "weight": 1.0} -->

However, we can check that if $\Lambda = {- {0.5I_{2}}}$, (i.e. ${A_{\mathsf{K}} = {- {0.5I_{2}}}},{{B_{\mathsf{K}} = 0},{C_{\mathsf{K}} = 0}}$), its Hessian is degenerated to zero, implying that it is a high-order saddle. Our proposed perturbed gradient descent algorithm in the next section can escape this type of high-order saddles efficiently. ∎

<!-- chunk {"id": "body-0045", "role": "body", "section": "Perturbed policy gradient method", "weight": 1.0} -->

Inspired by Theorems 1 Control") and 2 Control"), we introduce a novel perturbed policy gradient method that combines a structural perturbation on $\Lambda$ in 14 Control") with a standard perturbation on gradients. Numerical results confirm that our perturbed policy gradient method can escape high-order saddles more efficiently, than either vanilla policy gradient or standard perturbed policy gradient.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-A Algorithm setup", "weight": 1.0} -->

Recent work has established that variations of gradient descent can escape strict saddle-points -- points at which the minimum eigenvalue of the Hessian is strictly negative. For example, stochastic gradient descent, gradient descent with appropriate random perturbation or with cubic regularization sub-oracle are proven to escape strict saddles and visit an approximate local minimum in polynomial time with high probability.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-A Algorithm setup", "weight": 1.0} -->

Our method combines the standard perturbed gradient descent \[22, Algorithm 2\] with an additional oracle of random structural perturbation on $\Lambda$. Our perturbed policy gradient descent is listed in Algorithm 1 Control"). We note that Algorithm 1 Control") is a *prototype* algorithm in the sense that some quantities (e.g., order-reduction, gradient and Hessian Lipschitz constants) of the LQG problem require more investigations. Convergence conditions and further quantitative analysis of our algorithm are also left for future work.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-A Algorithm setup", "weight": 1.0} -->

The high-level ideas are described below.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-A Algorithm setup", "weight": 1.0} -->

When the gradient of a controller $\mathsf{K}_{t}$ is close to zero, we check whether it is minimal, i.e., the smallest Hankel singular value of the controllability/observability matrix is bounded away from zero (for the connection with Hankel singular values and controllability/observability, please refer \[3, Chapter 7\]).

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-A Algorithm setup", "weight": 1.0} -->

If $\mathsf{K}_{t}$ is controllable and observable (i.e., minimal), it is close to be globally optimal by Theorem 1 Control"). We terminate the algorithm.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-A Algorithm setup", "weight": 1.0} -->

If $\mathsf{K}_{t}$ is non-minimal, we perform a minimal realization (e.g., Kalman decomposition or balance realization) to get a controller in the form of 13 Control").

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-A Algorithm setup", "weight": 1.0} -->

We then choose a symmetric and stable $\Lambda$ randomly. From Theorem 2 Control"), we expect that the resulting controller is close to a strict saddle point.

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-A Algorithm setup", "weight": 1.0} -->

We apply a random perturbation on the gradients. The random perturbation is i.i.d. Gaussian variables, with small magnitudes, added to each entry of $A_{\mathsf{K}},B_{\mathsf{K}},C_{\mathsf{K}}$ such that the controller is still stabilizing. We run a few gradient descent iterations afterwards. We expect that these gradient descent iterations will escape from the strict saddle point.

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-A Algorithm setup", "weight": 1.0} -->

We terminate the algorithm when the algorithm reaches the predefined number of steps $T$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-A Algorithm setup", "weight": 1.0} -->

Algorithm 1 Control") can escape a large class of (but not all) high-order saddles at which $\mathbf{G}{(s)}$ in 15 Control") is not identically zero. When Algorithm 1 Control") terminates, it is likely to produce an approximately global minimum or return a point at which the transfer function $\mathbf{G}{(s)}$ in 15 Control") is close to zero. In the later case, the point may not be globally optimal, and this is related to the sufficiency of ${\mathbf{G}{(s)}} \equiv 0$ for global optimality in Remark 2≡0 for global optimality and its interpretation). ‣ III-B Hessian of stationary points ‣ III Stationary Points and Their Hessians ‣ Escaping High-order Saddles in Policy Optimization for Linear Quadratic Gaussian (LQG) Control").

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-A Algorithm setup", "weight": 1.0} -->

0: 1) Loss J (K) with its gradient. 2) Thresholds gth, ι. 3) Constant T, τ, step size η. 4) Function λHan, min (K) that returns the minimum singular value of the Hankel matrix of K. 5) Function reduce_order (K) that finds the approximate order of K.
1: Set t = 0, tperturb = −τ − 1 and initialize a stabilizing controller K0.

<!-- chunk {"id": "body-0057", "role": "body", "section": "IV-A Algorithm setup", "weight": 1.0} -->

3: if ∥∇J (Kt)∥ ≤ gth and λHan, min (Kt) ≥ ι then
5: else if ∥∇J (Kt)∥ ≤ gth and λHan, min (Kt) ≤ ι and t − tperturb &gt; τ then
6: ${{\hat{\mathsf{K}}}_{t},q_{t}}\leftarrow{\text{reduce\_order}{(\mathsf{K}_{t})}}$ where qt is the order after model reduction;
7: Λt ← λ In − qt with λ &lt; 0 randomly selected;
8: $\mathsf{K}_{t}\leftarrow{{diag}{({\hat{\mathsf{K}}}_{t},\Lambda_{t})}}$ as in 14 (Theorem 2);
9: Kt ← Kt + ξt with ξt uniformly sampled from 𝔹Kt (r);
Algorithm 1 Perturbed policy gradient

<!-- chunk {"id": "body-0058", "role": "body", "section": "IV-B Numerical results", "weight": 1.0} -->

Standard perturbed policy gradient (with no perturbation on dynamics $\Lambda$, i.e., no Lines 6 Control")-8 Control") in Algorithm 1 Control"));

<!-- chunk {"id": "body-0059", "role": "body", "section": "IV-B Numerical results", "weight": 1.0} -->

Perturb the dynamics $\Lambda$ but with no perturbation on gradients (i.e., no Line 9 Control") in Algorithm 1 Control").).

<!-- chunk {"id": "body-0060", "role": "body", "section": "IV-B Numerical results", "weight": 1.0} -->

The globally optimal controller from 6 Control") for the LQG instance in Example 3 Control") is

<!-- chunk {"id": "body-0061", "role": "body", "section": "IV-B Numerical results", "weight": 1.0} -->

To illustrate the performance of different algorithms, we initialize the controller at

<!-- chunk {"id": "body-0062", "role": "body", "section": "IV-B Numerical results", "weight": 1.0} -->

As discussed in Example 3 Control"), this initial point is close to a high-order saddle ${{A_{\mathsf{K}} = {- {0.5I_{2}}}},{{B_{\mathsf{K}} = 0},{C_{\mathsf{K}} = 0}}}.$ We add a perturbation to the first iteration and run gradient descent with the fixed step size. The perturbations are different, as discussed at the beginning of this section.

<!-- chunk {"id": "body-0063", "role": "body", "section": "IV-B Numerical results", "weight": 1.0} -->

The results are shown in Figure 1 Control"): the left sub-figure shows the suboptimality gap, and the right one shows the norm of graidents at each iteration. Our Algorithm 1 Control") implements both perturbations: 1) identifying an one-dimensional $\Lambda$ as in the standard form (14 Control")) and change it randomly, and 2) randomly perturb all variables with a small quantity $0.01$. As shown in Figure 1 Control"), our Algorithm 1 Control") can escape this high-order saddle faster than the other three algorithms, including standard PGD in (in which no perturbation on $\Lambda$ was applied).

<!-- chunk {"id": "body-0064", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We have proposed a novel PGD algorithm (cf. Algorithm 1 Control")) to escape high-order saddles of LQG. Our PGD algorithm combines the inherent structure of LQG control with standard perturbation on gradients. We have shown the structure of all stationary points after model reduction (cf. Theorem 1 Control")). We have also introduced a reparameterization procedure with an intriguing transfer function $\mathbf{G}{(s)}$ at any stationary point (cf. Theorem 2 Control")). If ${\mathbf{G}{(s)}} ≢ 0$, we can certify that the high-order saddle can be made as a strict saddle by the reparameterization. Numerical simulations confirmed that Algorithm 1 Control") combining the reparameterization with random perturbation on gradients can accelerate the speed of escaping high-order saddles. Ongoing and future directions include quantitative analysis of Algorithm 1 Control").

<!-- chunk {"id": "body-0065", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We are also interested in the sufficiency of ${\mathbf{G}{(s)}} \equiv 0$ (or other conditions are needed) for global optimality of LQG (see Remark 2≡0 for global optimality and its interpretation). ‣ III-B Hessian of stationary points ‣ III Stationary Points and Their Hessians ‣ Escaping High-order Saddles in Policy Optimization for Linear Quadratic Gaussian (LQG) Control")).
