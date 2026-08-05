<!-- arxiv-full-text:v1 {"arxiv_id": "2206.06863", "source": "ar5iv"} -->

## Introduction

Reinforcement learning (RL) methods have shown great empirical success in controlling complex dynamical systems Silver et al.. While these methods are promising, we have only begun to understand performance guarantees and fundamental limitations in continuous state and action problems. Providing such guarantees and understanding such limitations is crucial to deploying these methods in safety-critical systems. In this paper, we focus on a particular class of such methods; namely, we seek to understand fundamental limitations for policy gradient methods.

Policy gradient methods are a relatively simple class of algorithms that have been recently analyzed in the context of the linear quadratic regulator (LQR), Fazel et al.; Tu and Recht. The motivation for studying policy gradients in the context of LQR stems from that it serves as an analytically tractable benchmark for RL in continuous state and action spaces. For instance, by direct arguments on can show that control-theoretic parameters affect the hardness of both offline and online learning in LQR Tsiamis and Pappas; Ziemann and Sandberg; Tsiamis et al.. Here, we extend this line of work and show that the popular policy gradient methods degrade similarly for systems with poor controllability and observability. To be precise, we show that ill-conditioned systems lead to arbitrarily noisy stochastic gradients.

### Problem Formulation

We are interested in studying how policy gradient methods applied to the linear system are affected by the fundamental limits of control. Above, ${x_{t} \in {\mathbb{R}}^{d_{x}}},{A \in {\mathbb{R}}^{d_{x} \times d_{x}}}$, $u_{t} \in {\mathbb{R}}^{d_{u}}$ and $w_{t} \in {\mathbb{R}}^{d_{x}}$ is an i.i.d. mean zero sequence of Gaussian noise with covariance matrix $\Sigma_{W} \in {\mathbb{R}}^{d_{x} \times d_{x}}$.

The learning task is to minimize subject to the dynamics without access to the model parameter $S = {(A,B)}$. In equation, $\mathbf{E}_{K,S}$ denotes expectation under the control law $K$ with dynamics $S$.

In this work, we relate the efficiency of stochastic policy gradient methods to certain control-theoretic parameters. Namely, we analyze algorithms of the form for some learning rate $\alpha \in {\mathbb{R}}_{+}$, and where at each iteration ${{} \ast {\lbrack{{\nabla_{K}J}{(K;S)}}\rbrack}}{\bigwedge{0.5ex{\lbrack{1pt}\rbrack}{\nabla_{K}J}{(K;S)}}}$ is estimated using data from the system. Such algorithms have been shown to converge for LQR by Fazel et al.. The purpose of this work is to demonstrate that any estimate ${{} \ast {\lbrack{{\nabla_{K}J}{(K;S)}}\rbrack}}{\bigwedge{0.5ex{\lbrack{1pt}\rbrack}{\nabla_{K}J}{(K;S)}}}$ from an (arbitrarily) ill-conditioned system is (arbitrarily) noisy.

To make this statement rigorous we need to model the statistical information available to the learner. Here, we model this as follows: the learner is given access to $N \in {\mathbb{N}}$ experiments ${{(x_{0,n},\ldots,x_{T,n})},n} \in {\lbrack N\rbrack}$ of length $T \in {\mathbb{N}}$ and a total input budget of $\betaNT$ with $\beta \in {\mathbb{R}}_{+}$. More precisely, the learner is allowed to freely choose $u_{t,n}$ as a function of past observations $(x_{0,n},\ldots,x_{t,n})$ and past trajectories ${{(x_{0,m},\ldots,x_{T,m})},m} < n$ and possible auxiliary randomization, while being constrained to a total budget This formulation allows both open- and closed-loop experiments but normalizes the average input energy to $\beta$.

### Related Work

The first proof that policy gradient methods converge for LQR is given in Fazel et al., which provides nonasymptotic guarantees that are polynomial in relevant problem parameters. Convergence guarantees for more general MDPs and other versions of LQR are given in Zhang et al.; Gravell et al.; Zhang et al.; Yaghmaie et al.. Extensions to partially observed systems are considered in Tang et al.; Mohammadi et al.; Zheng et al.. A popular alternative approach to policy gradients for LQR is based on certainty equivalence Dean et al..

Most closely related to our work are Preiss et al.; Tu and Recht; Venkataraman and Seiler. While we give lower bounds valid for any estimator in this work, Preiss et al. analyzes the variance of a particular gradient estimator known as REINFORCE. Similarly, Tu and Recht provides algorithm specific lower bounds which demonstrate, among other things, that if $R = 0$ and $B$ is invertible, then learning fails as ${\| B\|}\rightarrow 0$. Further, Tu and Recht gives a generic performance lower bound for offline methods which however does not scale with relevant system-theoretic quantities.

Our work also relates to Tsiamis and Pappas; Ziemann and Sandberg; Tsiamis et al., which also study fundamental limits in learning-enabled control. From a broader perspective, the present work fits into a line of work that strives to ascertain the interplay between control-theoretic performance, stability and robustness notions, and learning Bernat et al.; Boffi et al.; Perdomo et al.; Tu et al.; Ziemann et al.. While we are mostly interested in offline methods in this work, analyses of online LQR can be found in the literature, see Abbasi-Yadkori et al.; Simchowitz and Foster; Cassel and Koren; Ziemann and Sandberg and the references therein.

### Contribution

We show that policy gradient methods are very much affected by the limits of control. Our main result ( Theorem 1) demonstrates that state feedback systems operating near marginal stability suffer from noisy gradients. This happens for instance if the system has poorly controllable unstable modes. We also provide an analogue of this result for partially observed systems (Theorem 2), which we use to show that systems with bad (small) Markov parameters also lead to noisy gradients. Compared to previous literature on this topic Tu and Recht; Venkataraman and Seiler; Preiss et al., our results provide a more fine-grained theoretical understanding of when and why gradient methods applied to dynamical systems fail.

### Preliminaries

A matrix $A$ is stable if ${\rho{(A)}} < 1$. A matrix $K$ is stabilizing for the system $S = {(A,B)}$ if $A + {BK}$ is a stable matrix. If $K$ is stabilizing for the system $S = {(A,B)}$, the closed-loop controllability gramian is well-defined. The set of all systems $S$ for which there exists a stabilizing $K$ is denoted by $\mathcal{S} = \mathcal{S}_{d_{x},d_{u}}$, which is an open subset of ${\mathbb{R}}^{{d_{x} \times d_{x}} + {d_{x} \times d_{u}}}$ in norm topology. Further, we define $K_{\star}{(S)}$ as (any element of) ${K_{\star}{(S)}} \in {{{argmin}_{K}J_{S}}{(K)}}$. Moreover, we denote the matrix operator norm (induced ${l^{2}{({\mathbb{R}}^{d})}}\rightarrow{l^{2}{({\mathbb{R}}^{d})}}$) by $\parallel \cdot \parallel_{\mathsf{o}\mathsf{p}}$.

We also require the following information-theoretic quantities. We define the Kullback-Leibler divergence between two probability measures $\mathbf{P}$ and $\mathbf{Q}$ as ${d_{\mathsf{K}\mathsf{L}}{(\mathbf{P},\mathbf{Q})}} \triangleq {\int{\frac{d\mathbf{P}}{d\mathbf{Q}}{d\mathbf{P}}}}$ and the total variation distance as ${d_{\mathsf{T}\mathsf{V}}{(\mathbf{P},\mathbf{Q})}} \triangleq {\int{|{{d\mathbf{P}} - {d\mathbf{Q}}}|}}$. When $\mathbf{P}$ and $\mathbf{Q}$ correspond to induced probability measures from two systems $S_{1}$ and $S_{2}$ we abuse notation and write ${d_{\mathsf{K}\mathsf{L}}{(S_{1},S_{2})}} = {d_{\mathsf{K}\mathsf{L}}{(\mathbf{P},\mathbf{Q})}}$ and ${d_{\mathsf{T}\mathsf{V}}{(S_{1},S_{2})}} = {d_{\mathsf{T}\mathsf{V}}{(\mathbf{P},\mathbf{Q})}}$ for divergences between the corresponding parametric families.

It will be convenient to introduce the shorthand $a_{t} \lesssim b_{t}$ if there exists a universal constant $C$ such that $a_{t} \leq {Cb_{t}}$ for every $t \geq t_{0}$ and some $t_{0} \in {\mathbb{N}}$. If $a_{t} \lesssim b_{t}$ and $b_{t} \lesssim a_{t}$ we write $a_{t} \asymp b_{t}$. For an integer $N$, we also define ${\lbrack N\rbrack} \triangleq {\{ 1,\ldots,N\}}$.

### Policy Gradients

We begin by recalling a standard characterization of the LQR cost for a linear controller $K$. A version of the following lemma can also be found in for instance Fazel et al..

### Lemma 1

If $K$ is stabilizing for $S = {(A,B)}$, the LQR cost can be written as where $P_{K}$ satisfies the Lyapunov equation Lemma 1 allows us to conveniently characterize the policy gradient ${\nabla_{K}J}{(K;S)}$.

### Lemma 2

Let $K$ be stabilizing for $S = {(A,B)}$. The policy gradient ${\nabla J}{(K;S)}$ can be written as where $P_{K}$ satisfies the Lyapunov equation and where $\Gamma_{K,S}$ is given by definition.

Combining Lemmas 1 and 2 we see that we are almost in the same setting as studied in Fazel et al.. The difference is mainly in how information is acquired, since each sample from the system is noisy and conditionally Gaussian. Compared to the noise-free random initial condition setting considered in Fazel et al., this simplifies the analysis of the variance of the gradient estimates since we later rely on the closed form of the KL divergence for Gaussians of different means.

## Policy Gradient Estimation Lower Bounds

Let us begin our study of stochastic gradient methods by the observation that ${\nabla_{K}J}{(K;S)}$ diverges if $K$ does not stabilize the system. Consider for instance the following two systems If ${|a|} > 1$ there exists no linear feedback controller which stabilizes both $S_{1}$ and $S_{2}$ of equation. Hence, any policy gradient which is finite for the first system will be infinite for the second system and vice versa. Combining this observation with the two point method (Lemma 7 ‣ Information-Theoretic Lower Bounds ‣ Appendix A Auxilliary Lemmas ‣ How are policy gradient methods affected by the limits of control?")) leads to the following conclusion.

### Proposition 1

For any $k \in {\mathbb{R}}$ the global minimax complexity of estimating the policy gradient at $k$ is infinite: where the infimum is taken over all measurable functions of the data ${{(x_{0,n},u_{0,n},\ldots,u_{{T - 1},n},x_{T,n})},n} \in {\lbrack N\rbrack}$.

Proposition 1 shows that the global minimax complexity of estimating gradients is infinite. While this shows that estimating gradients can be hard, it does not reveal how this hardness depends on control theoretic parameters.

### Local Minimax Complexities

In order to understand what properties of a particular system makes learning to control hard, we need to consider local complexity measures. Here, we investigate the $(d,\varepsilon)$-local minimax complexity of estimating gradients. We define this as for some metric $d$ on the set of stabilizable systems $\mathcal{S}$ and where the infimum is taken over all measurable functions of the data ${{(x_{0,n},u_{0,n},\ldots,u_{{T - 1},n},x_{T,n})},n} \in {\lbrack N\rbrack}$. This captures a more instance-specific notion of how hard it is to estimate gradients. Roughly, this complexity measure corresponds to requiring algorithms to performing well not just on a nominal system $S$, but also on small $\varepsilon$-perturbations of that system.

Note further that the definition still leaves open the question at which $K$ to measure the complexity of estimating gradients. By equation and Proposition 1 we know that ${\nabla_{K}J}{(K)}$ can be arbitrarily large when evaluated far from a stationary point. As this rather reflects poor initialization than fundamental control-theoretic hardness, we instead seek to lower bound ${\mathfrak{M}}_{d}{(\varepsilon;S,K)}$ near $K_{\star}{(S)}$. Arguably, any successful policy gradient algorithm should eventually find itself near $K_{\star}{(S)}$. Thus, we provide lower bounds on the gradient estimation error in the vicinity of the stationary point $K_{\star}{(S)}$. We denote the associated local complexity by ${{\mathfrak{M}}_{d}{(\varepsilon;S)}} = {{\mathfrak{M}}_{d}{(\varepsilon;S,{K_{\star}{(S)}})}}$.

### Constructing Hard Instances

To simplify the evaluation of the local minimax complexity, we mainly consider the construction below. Fix a nominal instance $S_{1} = {(A,B)}$ of system with optimal control law $K_{\star} = {K_{\star}{(S_{1})}}$; then the perturbation is tractable to evaluate. Here, $A' = {A - {\DeltaK_{\star}}}$ and $B' = {B + \Delta}$ for some $\Delta \in {\mathbb{R}}^{d_{x} \times d_{u}}$. This perturbation is convenient since ${A' + {B'K_{\star}}} = {A + {BK_{\star}}}$ for any $\Delta$ and has previously been used in Simchowitz and Foster; Ziemann and Sandberg. In particular, the system quantities $P_{K_{\star},S}$ and $\Gamma_{K_{\star},S}$ are invariant as we vary $\Delta$. Combining this observation with the optimality of $K_{\star} = {K_{\star}{(S_{1})}}$ for system $S_{1}$, yields the following simple expression for the gradient of system.

### Lemma 3

The policy gradient for $S_{2} = {(A',B')}$ given by system at $K_{\star} = {K_{\star}{(S_{1})}}$ is given by Proof of Lemma 3. By Lemma 2 the policy gradient is given by where we used that ${A + {BK_{\star}}} = {A' + {B'K_{\star}}}$. On the other hand by optimality of $K_{\star}$ to $S_{1}$. The result follows. $\blacksquare$ By combining Lemma 3 with Le Cam's two point method LeCam (provided in the appendix as Lemma 7 ‣ Information-Theoretic Lower Bounds ‣ Appendix A Auxilliary Lemmas ‣ How are policy gradient methods affected by the limits of control?")) we obtain a generic estimation lower bound for policy gradients evaluated in the vicinity of the optimum $K_{\star}$.

### Theorem 1

Consider two systems $S_{1} = {(A,B)}$ and ${S_{2}{(\Delta)}} = {(A',B')}$ with $A' = {A - {\DeltaK_{\star}}}$ and $B' = {B + \Delta}$. Let ${{\mathfrak{M}}_{d}{(\varepsilon;S_{1})}} = {{\mathfrak{M}}_{d}{(\varepsilon;S_{1},{K_{\star}{(S_{1})}})}}$ and $K_{\star} = {K_{\star}{(S_{1})}}$, then In other words, the local complexity of estimating gradients can be lower bounded by the maximum of $\left\| {\Delta^{\top}P_{K_{\star},S_{1}}{({A + {BK}})}\Gamma_{K_{\star},S_{1}}} \right\|_{\mathsf{o}\mathsf{p}}$, optimized over $\Delta$ and subject to this leading to small differences in the output of systems $S_{1}$ and $S_{2}$.

Proof of Theorem 1. Define the loss function ${L{({\mathsf{d}\mathsf{e}\mathsf{c}},S)}} \triangleq \left\| {{{\nabla_{K}J}{(K;S)}} - {\mathsf{d}\mathsf{e}\mathsf{c}}} \right\|_{\mathsf{o}\mathsf{p}}$, where the decision $\mathsf{d}\mathsf{e}\mathsf{c}$ is a placeholder variable for the gradient estimate. For any two systems $S_{1}$ and $S_{2}$ we have that by the triangle inequality. Invoking Lemma 3 we thus see that for the choice $S_{1} = {(A,B)}$ and $S_{2} = {(A',B')}$ with $A' = {A - {\DeltaK_{\star}}}$ and $B' = {B + \Delta}$ we have for any $\Delta \in {\mathbb{R}}^{d_{x} \times d_{u}}$. Combining equation with Lemma 7 ‣ Information-Theoretic Lower Bounds ‣ Appendix A Auxilliary Lemmas ‣ How are policy gradient methods affected by the limits of control?") it follows that where the second inequality is an application of Pinsker's inequality. $\blacksquare$ At this point, we note that the right hand side of inequality is large for systems operating near marginal stability. When ${A + {BK_{\star}}}\rightarrow 1$ both $P_{K_{\star},S}$ and $\Gamma_{K_{\star},S}$ tend to infinity. To better understand the practical implications of this, we now turn to interpreting Theorem 1 by instantiating it for three special cases: scalar systems, over-actuated systems and integrator-like systems.

### Consequences of Theorem 1

### Scalar Systems

The bound in Theorem 1 is agnostic to the experiment used to generate the dataset, which is simply reflected in the quantity $\left({1 - \sqrt{\frac{1}{2}d_{\mathsf{K}\mathsf{L}}{(S_{1},{S_{2}{(\Delta)}})}}} \right)$. Let us interpret Theorem 1 by a simple scalar example. To this end, consider the system with ${a,b} \in {\mathbb{R}}$, which is open-loop unstable ${|a|} > 1$. Let $s_{2}$ be given by the perturbation $s_{2} = {({a - {\Deltak_{\star}}},{b + \Delta})}$ with $\Delta \in {\mathbb{R}}$. The divergence $d_{\mathsf{K}\mathsf{L}}{(s_{1},s_{2})}$ satisfies | | $d_{\mathsf{K}\mathsf{L}}{(s_{1},s_{2})}$ | $= {\sum\limits_{n = 1}^{N}{\sum\limits_{t = 0}^{T - 1}{\mathbf{E}_{s_{1}}\frac{1}{2}{({{k_{\star}\Deltax_{t}} + {\Deltau_{t}}})}^{2}}}}$ | | (Lemma 8) | | \(17\) | | | | $\leq {\Delta^{2}{\sum\limits_{n = 1}^{N}{\sum\limits_{t = 0}^{T - 1}{\mathbf{E}_{s_{1}}\left({u_{t}^{2} + {k_{\star}x_{t}^{2}}} \right)}}}}$ | | | if $\Delta^{2} = \frac{1}{2NT{({\Gamma_{k_{\star},s_{1}} + \beta})}}$. Plugging inequality into inequality, we conclude that with $\varepsilon_{N,T} \asymp \frac{1}{\sqrt{NT{({\beta + \Gamma_{k_{\star},s_{1}}})}}}$. In particular as ${|b|}\rightarrow 0$, one may verify that the right hand side of the expression tends to infinity. In other words, as controllability (of unstable modes) is lost, policy gradients become arbitrarily noisy. This is verified via simulations in the appendix (Figure 1) using both a least squares certainty equivalent approach and a $0$-th order method (see).

### Multivariate Systems

If we assume that $K$ has a left nullspace, the bound in Theorem 1 becomes tractable to evaluate since we are free to select $\Delta$ such that ${\DeltaK} = 0$, which simplifies some calculations. Intuitively, the these instances are hard to distinguish between because controllers with left nullspaces lead to identifiability issues regarding the $B$-matrix Ziemann and Sandberg.

### Corollary 1

For any $\Delta$ such that ${\DeltaK_{\star}} = 0$ and ${\|\Delta\|}_{\mathsf{o}\mathsf{p}} \leq 1$ we have that for any $\varepsilon_{N,T} \gtrsim {1/\sqrt{NT}}$ and where ${d_{\infty}{(S_{1},S_{2})}} = {\max{({\|{A - A'}\|}_{\mathsf{o}\mathsf{p}},{\|{B - B'}\|}_{\mathsf{o}\mathsf{p}})}}$.

Proof of Corollary 1. Fix $\varepsilon > 0$. By Lemma 8 the two systems $S_{1} = {(A,B)}$ and ${S_{2}{(N,T)}} = {(A_{N,T}',B_{N,T}')}$ with $A' = {A - {\frac{\varepsilon}{\sqrt{\betaNT}}\DeltaK_{\star}}} = A$ and $B' = {B + {\frac{\varepsilon}{\sqrt{\betaNT}}\Delta}}$ satisfy ${d_{\mathsf{K}\mathsf{L}}{(S_{1},{S_{2}{(N,T)}})}} = {O{}}$. The result follows by Theorem 1. $\blacksquare$ In other words, the complexity of estimating gradients can be asymptotically lower bounded at the central limit theorem scale $\sqrt{NT}$ by the part of $P_{K_{\star},S_{1}}{({A + {BK_{\star}}})}\Gamma_{K_{\star},S_{1}}$ that cannot be identified by closed loop experiments using $K_{\star}$. It so happens that this complexity measure is very similar to that dictating regret lower bounds in adaptive LQR Ziemann and Sandberg. In the sequel, we exploit this to show that the gradient variance can grow exponentially with the system dimension in the worse case by leveraging certain Riccati calculations due to Tsiamis et al..

### Policy Gradients and the Curse of Dimensionality

Let us now show that variance of policy gradient estimates can suffer from exponential complexity in the dimension. The proof of this fact relies on a construction due to Tsiamis et al.. Namely, we consider a system consisting of two decoupled subsystems $S_{1} = {(A,B)}$ of the form: with $\rho \in {}$, $Q = I_{d_{x}}$ and $R = I_{2}$. We also define the subsystem with $Q_{0} = I_{d_{x} - 1}$ and $R_{0} = 1$ and where $A_{0} \in {\mathbb{R}}^{{({d_{x} - 1})} \times {({d_{x} - 1})}}$ and $B_{0} \in {\mathbb{R}}^{d_{x} - 1}$. Note that $A_{0}$ is a stable matrix since ${|\rho|} < 1$. In the notation of Theorem 1, we let $\Delta = \begin{bmatrix} \end{bmatrix}$, so that $S_{2}$ consists of two weakly coupled subsystems, with coupling induced by $\Delta_{1}$ (recall $S_{2} = {(A',B')} = {({A - {\DeltaK}},{B + \Delta})}$).

Denote further by $P_{0, \star}$ the solution to the Lyapunov equation for the subsystem with $K_{0} = K_{\star,0}$. Note also that $P_{0, \star}$ satisfies the discrete algebraic Riccati equation for the tuple $(A_{0},B_{0},Q_{0},R_{0})$. With these preliminaries established, we now recall the following two lemmas .

### Lemma 4

where the term $o{}$ tends to $0$ as $d_{x}$ tends to infinity.

### Lemma 5 (Riccati matrix can grow exponentially)

For system we have: Combining Corollary 1 with Lemmas 4 and 5 ‣ Policy Gradients and the Curse of Dimensionality ‣ 2.2 Consequences of Theorem 1 ‣ 2 Policy Gradient Estimation Lower Bounds ‣ How are policy gradient methods affected by the limits of control?") we arrive at the following conclusion:

### Proposition 2

For the system $S$ given in equation we have that for $d_{x}$ and $NT$ sufficiently large.

In other words, there are classes of stable systems for which the policy gradient suffers from exponential complexity in the state dimension.

## Extension to Partially Observed Systems

We now demonstrate that our lower bound approach extends to partially observed systems of the form in which $A$ and $B$ are as in system, $C \in {\mathbb{R}}^{d_{y} \times d_{x}}$ and both $w_{t}$ and $v_{t}$ are i.i.d. normal with mean zero and covariance $\Sigma_{W},\Sigma_{V}$. We denote partially observed systems of the form by $G = {(A,B,C)}$. For system one typically seeks to learn dynamic controllers of the form (see e.g. Tang et al.) parametrized by the linear system $K_{\mathsf{d}\mathsf{y}\mathsf{n}} = {(A_{\mathsf{d}\mathsf{y}\mathsf{n}},B_{\mathsf{d}\mathsf{y}\mathsf{n}},K)}$. The objective, as before is to minimize the cost but this time subject to process and controller dynamics -.

### Fully Observed Reformulation

To establish a hardness result, it suffices to focus on the difficulty of estimating gradients with respect to the output matrix of the controller, $K$. We will exploit this by reducing the system - when evaluated near the optimum of $J_{S}$ to a fully observed system. Namely, at the optimum $K_{{\mathsf{d}\mathsf{y}\mathsf{n}}, \star} = {{{argmin}J_{S}}{(K_{\mathsf{d}\mathsf{y}\mathsf{n}})}}$ the dynamics of $\xi_{t}$ in equation are given by the Kalman filter $\xi_{t} = {\hat{x}}_{t}$, allowing us to write which has the same input-output behavior as system and where the sequence of innovations $\{\nu_{t}\}$ is independent. More precisely, the covariance $\Sigma_{t}$ of $\nu_{t}$ is given by where $F_{t|{t - 1}}$ satisfies the filter Riccati recursion (see e.g. Söderström) and the filter gain $L_{t}$ is given by We now consider the cost $J{(K_{\mathsf{d}\mathsf{y}\mathsf{n}})}$ evaluated at the optimal filter and with variable $K$. With some abuse of notation, we denote this quantity $J{(K;G)}$ where $u_{t}$ is given by $u_{t} = {K{\hat{x}}_{t}}$, and ${\hat{x}}_{t}$ is defined by the Kalman filter. We shall call the quantity $J{(K;G)}$ the restricted cost function, and note that it has almost the exact same form as the fully observed cost. With these preliminaries established, the following lemma is straightforward to verify using Lemmas 1 and 2 (and justifies the abuse of notation $J{(K;G)}$).

### Lemma 6

Consider a partially observed system $G = {(A,B,C)}$ of the form. Then the restricted cost function satisfies where $L_{G}$ and $\Sigma_{\nu,G}$ are the steady state quantities corresponding to recursions and respectively and where $P_{K}$ as before is given by the Lyapunov equation. Moreover, the policy gradient is given by In other words, near the optimal controller $K_{{\mathsf{d}\mathsf{y}\mathsf{n}},_{\star}}$ the gradient with respect to the filter gain $K$ has the same form as in the state-feedback setting. However, we stress at this point that neither the realization of the system nor the realization of the controller is unique. To remedy this, we will later verify in a scalar setting that our lower bounds are invariant under similarity transformation (see equation).

### Recovering Theorem 1

In the partially observed setting, we keep the exploration budget constraint but the observation model is necessarily different. Namely, we assume that the learner instead has access to input-output data of the form ${{(y_{0,n},u_{0,n},\ldots,u_{{T - 1},n},y_{T,n})},n} \in {\lbrack N\rbrack}$.

In the partially observed setting, we thus define the analogous local minimax complexity as where the infimum is taken over all measurable functions of the data ${{(y_{0,n},u_{0,n},\ldots,u_{{T - 1},n},y_{T,n})},n} \in {\lbrack N\rbrack}$, ${\nabla_{K}J}{(K;G)}$ is given by equation and $d$ again is a metric on system parameters $G = {(A,B,C)}$.

Equipped with the definition and Lemma 6 the proof of the following result follows similarly to that of Theorem 1.

### Theorem 2

Consider two systems $G_{1} = {(A,B,C)}$ and ${G_{2}{(\Delta)}} = {(A',B',C')}$ with $A' = {A - {\DeltaK_{\star}}}$, $B' = {B + \Delta}$ and $C' = C$. Then the local minimax complexity of estimating gradients is lower bounded as Above $d_{\mathsf{K}\mathsf{L}}{(G_{1},{G_{2}{(\Delta)}})}$ is the divergence between the induced probability measures over input-output data ${{(y_{0,n},u_{0,n},\ldots,u_{{T - 1},n},y_{T,n})},n} \in {\lbrack N\rbrack}$ between models $G_{1}$ and $G_{2}$.

By the data-processing inequality, the lower bound can be brought onto the exact same form as the lower bound. Namely, we observe that^11^1To see this, simply observe that $(y_{0},\ldots,y_{T})$ is a stochastic function of $(x_{0,n},u_{0,n},\ldots,u_{{T - 1},n},x_{T,n})$. where $d_{\mathsf{K}\mathsf{L}}{(S_{1},{S_{2}{(\Delta)}})}$ is a slight overload of notation for the divergence between state-input data ${{(x_{0,n},u_{0,n},\ldots,u_{{T - 1},n},x_{T,n})},n} \in {\lbrack N\rbrack}$ between models $G_{1}$ and $G_{2}$. In other words, all the results of Section 2 apply with $\Gamma_{K_{\star},S_{1}}$ defined by equation exchanged for $\Gamma_{K_{\star},\nu,G_{1}}$ defined in equation and $\Sigma_{w}$ exchanged for $\Sigma_{t}$ given by equation. While this is true for a fixed parametrization $G = {(A,B,C)}$, one may wonder whether the lower-bound relies on fundamental system-theoretic quantities or is simply a consequence of poor parametric choice for computing gradients. In the next example we show that the lower bound captures control-theoretic limitations that are independent of the state-space representation.

### Bad Markov Parameters Imply Noisy Gradients

Consider the almost scalar system $g_{1} = {(a,B,c)}$ given by defined consinstently with system, but specifically ${a,b,c} \in {\mathbb{R}}$ and $Q = \Sigma_{V} = \Sigma_{W} = 1$ and $R = I_{2}$. Note that the maximum singular values of the first Markov parameter of $g_{1}$ is equal to the product $m = {cb}$ and that this is $m$ is invariant under similarity transformation. We consider the two systems $g_{1} = {(a,B,c)}$ and $g_{2} = {(a,{B{(\Delta)}},c)}$ and where ${B{(\Delta)}} = \begin{bmatrix} \end{bmatrix}$. Observe that the optimal policy to system is of the form $K_{\star} = \begin{bmatrix} \end{bmatrix}$ and that the gramians $P_{K_{\star},\nu,g_{1}}$ and $\Gamma_{K_{\star},g_{1}}$ are scalar and equal to $P_{K_{\star},\nu,g_{1}} = P_{k_{\star},\nu,g_{1}}$ and $\Gamma_{K_{\star},g_{1}} = \Gamma_{k_{\star},g_{1}}$ respectively. In other words, the second input has no effect on the system, but as well shall see, $g_{2}$ is very sensitive to perturbations $\Delta$ whenever the largest singular value of the Markov parameter $m = {|{cb}|}$ is small.

If we denote by $d_{\mathsf{K}\mathsf{L}}{(s_{1},s_{2})}$ the KL divergence between scalar input-state trajectories drawn from $g_{1}$ and $g_{2}$, we have by Lemma 8 that | | $d_{\mathsf{K}\mathsf{L}}{(s_{1},s_{2})}$ | $= {\sum\limits_{n = 1}^{N}{\sum\limits_{t = 0}^{T - 1}{\mathbf{E}_{g_{1}}\frac{1}{2}{({\Deltau_{t}})}^{2}}}}$ | (Lemma 8) | | | | | $\leq {\frac{1}{2}\Delta^{2}{\sum\limits_{n = 1}^{N}{\sum\limits_{t = 0}^{T - 1}{\mathbf{E}_{g_{1}}u_{t}^{2}}}}}$ | | | | | $\leq {\frac{1}{2}\Delta^{2}NT\beta}$ | (by) | | | | | $\leq \frac{1}{2}$ | $\left({{\text{~if~}\Delta^{2}} = \frac{1}{NT\beta}} \right).$ | | Invoking Theorem 2 this implies the local minimax lower bound where $\varepsilon_{N,T} \asymp {1/\sqrt{NT}}$. Inequality in itself is an instance specific lower bound for scalar partially observed systems of the form. Further, the inequality implies that if the Markov parameter ${|m|} = {|{cb}|}$ is small, estimating gradients is always hard. Namely, we make the following observations^22^2To verify these claims, observe that the scalar quantities $P_{k_{\star},\nu,g_{1}}$, $k_{\star}$ and $\Sigma_{k_{\star},\nu,g_{1}}$ have closed form solutions.: $P_{k_{\star},\nu,g_{1}}$ tends to infinity at rate $1/b^{2}$ as $b$ tends to $0$. Moreover, $P_{k_{\star},{g1}}$ is always lower-bounded by $1$.

The large and small $c$ asymptotics of $\Sigma_{k_{\star},\nu,g_{1}}$ are proportional to $1/c^{2}$ The factor $|{a + {bk_{\star}}}|$ tends to 0 no faster than $1/b^{2}$ and tends to $\min{(1,{|a|})}$ as $b\rightarrow 0$ (and $|a|$ is invariant under similarity transform).

Combining these observations, we see that as the system invariant ${|m|} = {|{cb}|}$ tends to zero, gradients become arbitrarily noisy; the lower bound tends to infinity. In other words, we have established that Thus, we obtain an RL analogue to the well-known fact that reparametrization cannot help controlling a partially observed system as any gain in observability is offset by a proportional loss in controllability and vice versa.

## Discussion

In this work we showed that estimating policy gradients can become arbitrarily hard due to known control-theoretic fundamental limitations Doyle by leveraging the classic two point method due to Le Cam LeCam. For instance, we showed with system that a partially observed system with small Markov parameters necessarily has noisy policy gradients and that this holds independently of the parametrization. Our bounds also show that learning controllers that are close to marginal stability can be hard. This is similar to what has already been observed for adaptive LQR/LQG in Ziemann and Sandberg. Leveraging results from Tsiamis et al. we further show that estimating policy gradients can suffer from exponential complexity in the system dimension. From a broader perspective, these results work toward elucidating when learning to control is feasible.

Acknowledgements: Ingvar Ziemann and Henrik Sandberg are supported by the Swedish Research Council and the Swedish Foundation for Strategic Research through the CLAS project (grant -0046). Nikolai Matni is supported in part by NSF awards CPS-2038873 and CAREER award ECCS-2045834, and a Google Research Scholar award.
