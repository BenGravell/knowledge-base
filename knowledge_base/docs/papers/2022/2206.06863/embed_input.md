<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

How Are Policy Gradient Methods Affected by the Limits of Control?

Topics include Policy gradients, Control, Curse of dimensionality, Gradient method.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study stochastic policy gradient methods from the perspective of control-theoretic limitations. Our main result is that ill-conditioned linear systems in the sense of Doyle inevitably lead to noisy gradient estimates. We also give an example of a class of stable systems in which policy gradient methods suffer from the curse of dimensionality. Our results apply to both state feedback and partially observed systems.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reinforcement learning (RL) methods have shown great empirical success in controlling complex dynamical systems Silver et al.. While these methods are promising, we have only begun to understand performance guarantees and fundamental limitations in continuous state and action problems. Providing such guarantees and understanding such limitations is crucial to deploying these methods in safety-critical systems. In this paper, we focus on a particular class of such methods; namely, we seek to understand fundamental limitations for policy gradient methods.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Policy gradient methods are a relatively simple class of algorithms that have been recently analyzed in the context of the linear quadratic regulator (LQR), Fazel et al.; Tu and Recht. The motivation for studying policy gradients in the context of LQR stems from that it serves as an analytically tractable benchmark for RL in continuous state and action spaces. For instance, by direct arguments on can show that control-theoretic parameters affect the hardness of both offline and online learning in LQR Tsiamis and Pappas; Ziemann and Sandberg; Tsiamis et al.. Here, we extend this line of work and show that the popular policy gradient methods degrade similarly for systems with poor controllability and observability. To be precise, we show that ill-conditioned systems lead to arbitrarily noisy stochastic gradients.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The learning task is to minimize subject to the dynamics without access to the model parameter $S = {(A,B)}$. In equation, $\mathbf{E}_{K,S}$ denotes expectation under the control law $K$ with dynamics $S$.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

In this work, we relate the efficiency of stochastic policy gradient methods to certain control-theoretic parameters. Namely, we analyze algorithms of the form for some learning rate $\alpha \in {\mathbb{R}}_{+}$, and where at each iteration ${{} \ast {\lbrack{{\nabla_{K}J}{(K;S)}}\rbrack}}{\bigwedge{0.5ex{\lbrack{1pt}\rbrack}{\nabla_{K}J}{(K;S)}}}$ is estimated using data from the system. Such algorithms have been shown to converge for LQR by Fazel et al..

<!-- chunk {"id": "body-0007", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The purpose of this work is to demonstrate that any estimate ${{} \ast {\lbrack{{\nabla_{K}J}{(K;S)}}\rbrack}}{\bigwedge{0.5ex{\lbrack{1pt}\rbrack}{\nabla_{K}J}{(K;S)}}}$ from an (arbitrarily) ill-conditioned system is (arbitrarily) noisy.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

To make this statement rigorous we need to model the statistical information available to the learner. Here, we model this as follows: the learner is given access to $N \in {\mathbb{N}}$ experiments ${{(x_{0,n},\ldots,x_{T,n})},n} \in {\lbrack N\rbrack}$ of length $T \in {\mathbb{N}}$ and a total input budget of $\betaNT$ with $\beta \in {\mathbb{R}}_{+}$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

More precisely, the learner is allowed to freely choose $u_{t,n}$ as a function of past observations $(x_{0,n},\ldots,x_{t,n})$ and past trajectories ${{(x_{0,m},\ldots,x_{T,m})},m} < n$ and possible auxiliary randomization, while being constrained to a total budget This formulation allows both open- and closed-loop experiments but normalizes the average input energy to $\beta$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Contribution", "weight": 1.0} -->

We show that policy gradient methods are very much affected by the limits of control. Our main result ( Theorem 1) demonstrates that state feedback systems operating near marginal stability suffer from noisy gradients. This happens for instance if the system has poorly controllable unstable modes. We also provide an analogue of this result for partially observed systems (Theorem 2), which we use to show that systems with bad (small) Markov parameters also lead to noisy gradients. Compared to previous literature on this topic Tu and Recht; Venkataraman and Seiler; Preiss et al., our results provide a more fine-grained theoretical understanding of when and why gradient methods applied to dynamical systems fail.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Policy Gradients", "weight": 1.0} -->

We begin by recalling a standard characterization of the LQR cost for a linear controller $K$. A version of the following lemma can also be found in for instance Fazel et al..

<!-- chunk {"id": "body-0012", "role": "body", "section": "Policy Gradient Estimation Lower Bounds", "weight": 1.0} -->

Let us begin our study of stochastic gradient methods by the observation that ${\nabla_{K}J}{(K;S)}$ diverges if $K$ does not stabilize the system. Consider for instance the following two systems If ${|a|} > 1$ there exists no linear feedback controller which stabilizes both $S_{1}$ and $S_{2}$ of equation. Hence, any policy gradient which is finite for the first system will be infinite for the second system and vice versa. Combining this observation with the two point method (Lemma 7 ‣ Information-Theoretic Lower Bounds ‣ Appendix A Auxilliary Lemmas ‣ How are policy gradient methods affected by the limits of control?")) leads to the following conclusion.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Local Minimax Complexities", "weight": 1.0} -->

In order to understand what properties of a particular system makes learning to control hard, we need to consider local complexity measures. Here, we investigate the $(d,\varepsilon)$-local minimax complexity of estimating gradients. We define this as for some metric $d$ on the set of stabilizable systems $\mathcal{S}$ and where the infimum is taken over all measurable functions of the data ${{(x_{0,n},u_{0,n},\ldots,u_{{T - 1},n},x_{T,n})},n} \in {\lbrack N\rbrack}$. This captures a more instance-specific notion of how hard it is to estimate gradients. Roughly, this complexity measure corresponds to requiring algorithms to performing well not just on a nominal system $S$, but also on small $\varepsilon$-perturbations of that system.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Local Minimax Complexities", "weight": 1.0} -->

Note further that the definition still leaves open the question at which $K$ to measure the complexity of estimating gradients. By equation and Proposition 1 we know that ${\nabla_{K}J}{(K)}$ can be arbitrarily large when evaluated far from a stationary point. As this rather reflects poor initialization than fundamental control-theoretic hardness, we instead seek to lower bound ${\mathfrak{M}}_{d}{(\varepsilon;S,K)}$ near $K_{\star}{(S)}$. Arguably, any successful policy gradient algorithm should eventually find itself near $K_{\star}{(S)}$. Thus, we provide lower bounds on the gradient estimation error in the vicinity of the stationary point $K_{\star}{(S)}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Constructing Hard Instances", "weight": 1.0} -->

To simplify the evaluation of the local minimax complexity, we mainly consider the construction below. Fix a nominal instance $S_{1} = {(A,B)}$ of system with optimal control law $K_{\star} = {K_{\star}{(S_{1})}}$; then the perturbation is tractable to evaluate. Here, $A' = {A - {\DeltaK_{\star}}}$ and $B' = {B + \Delta}$ for some $\Delta \in {\mathbb{R}}^{d_{x} \times d_{u}}$. This perturbation is convenient since ${A' + {B'K_{\star}}} = {A + {BK_{\star}}}$ for any $\Delta$ and has previously been used in Simchowitz and Foster; Ziemann and Sandberg.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Constructing Hard Instances", "weight": 1.0} -->

In particular, the system quantities $P_{K_{\star},S}$ and $\Gamma_{K_{\star},S}$ are invariant as we vary $\Delta$. Combining this observation with the optimality of $K_{\star} = {K_{\star}{(S_{1})}}$ for system $S_{1}$, yields the following simple expression for the gradient of system.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Multivariate Systems", "weight": 1.0} -->

If we assume that $K$ has a left nullspace, the bound in Theorem 1 becomes tractable to evaluate since we are free to select $\Delta$ such that ${\DeltaK} = 0$, which simplifies some calculations. Intuitively, the these instances are hard to distinguish between because controllers with left nullspaces lead to identifiability issues regarding the $B$-matrix Ziemann and Sandberg.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Policy Gradients and the Curse of Dimensionality", "weight": 1.0} -->

Let us now show that variance of policy gradient estimates can suffer from exponential complexity in the dimension. The proof of this fact relies on a construction due to Tsiamis et al.. Namely, we consider a system consisting of two decoupled subsystems $S_{1} = {(A,B)}$ of the form: with $\rho \in {}$, $Q = I_{d_{x}}$ and $R = I_{2}$. We also define the subsystem with $Q_{0} = I_{d_{x} - 1}$ and $R_{0} = 1$ and where $A_{0} \in {\mathbb{R}}^{{({d_{x} - 1})} \times {({d_{x} - 1})}}$ and $B_{0} \in {\mathbb{R}}^{d_{x} - 1}$. Note that $A_{0}$ is a stable matrix since ${|\rho|} < 1$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Policy Gradients and the Curse of Dimensionality", "weight": 1.0} -->

In the notation of Theorem 1, we let $\Delta = \begin{bmatrix} \end{bmatrix}$, so that $S_{2}$ consists of two weakly coupled subsystems, with coupling induced by $\Delta_{1}$ (recall $S_{2} = {(A',B')} = {({A - {\DeltaK}},{B + \Delta})}$).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Policy Gradients and the Curse of Dimensionality", "weight": 1.0} -->

Denote further by $P_{0, \star}$ the solution to the Lyapunov equation for the subsystem with $K_{0} = K_{\star,0}$. Note also that $P_{0, \star}$ satisfies the discrete algebraic Riccati equation for the tuple $(A_{0},B_{0},Q_{0},R_{0})$. With these preliminaries established, we now recall the following two lemmas.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Extension to Partially Observed Systems", "weight": 1.0} -->

We now demonstrate that our lower bound approach extends to partially observed systems of the form in which $A$ and $B$ are as in system, $C \in {\mathbb{R}}^{d_{y} \times d_{x}}$ and both $w_{t}$ and $v_{t}$ are i.i.d. normal with mean zero and covariance $\Sigma_{W},\Sigma_{V}$. We denote partially observed systems of the form by $G = {(A,B,C)}$. For system one typically seeks to learn dynamic controllers of the form (see e.g. Tang et al.) parametrized by the linear system $K_{\mathsf{d}\mathsf{y}\mathsf{n}} = {(A_{\mathsf{d}\mathsf{y}\mathsf{n}},B_{\mathsf{d}\mathsf{y}\mathsf{n}},K)}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Extension to Partially Observed Systems", "weight": 1.0} -->

The objective, as before is to minimize the cost but this time subject to process and controller dynamics -.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Fully Observed Reformulation", "weight": 1.0} -->

To establish a hardness result, it suffices to focus on the difficulty of estimating gradients with respect to the output matrix of the controller, $K$. We will exploit this by reducing the system - when evaluated near the optimum of $J_{S}$ to a fully observed system. Namely, at the optimum $K_{{\mathsf{d}\mathsf{y}\mathsf{n}}, \star} = {{{argmin}J_{S}}{(K_{\mathsf{d}\mathsf{y}\mathsf{n}})}}$ the dynamics of $\xi_{t}$ in equation are given by the Kalman filter $\xi_{t} = {\hat{x}}_{t}$, allowing us to write which has the same input-output behavior as system and where the sequence of innovations $\{\nu_{t}\}$ is independent.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Fully Observed Reformulation", "weight": 1.0} -->

More precisely, the covariance $\Sigma_{t}$ of $\nu_{t}$ is given by where $F_{t|{t - 1}}$ satisfies the filter Riccati recursion (see e.g. Söderström) and the filter gain $L_{t}$ is given by We now consider the cost $J{(K_{\mathsf{d}\mathsf{y}\mathsf{n}})}$ evaluated at the optimal filter and with variable $K$. With some abuse of notation, we denote this quantity $J{(K;G)}$ where $u_{t}$ is given by $u_{t} = {K{\hat{x}}_{t}}$, and ${\hat{x}}_{t}$ is defined by the Kalman filter. We shall call the quantity $J{(K;G)}$ the restricted cost function, and note that it has almost the exact same form as the fully observed cost.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Fully Observed Reformulation", "weight": 1.0} -->

With these preliminaries established, the following lemma is straightforward to verify using Lemmas 1 and 2 (and justifies the abuse of notation $J{(K;G)}$).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Recovering Theorem 1", "weight": 1.0} -->

In the partially observed setting, we keep the exploration budget constraint but the observation model is necessarily different. Namely, we assume that the learner instead has access to input-output data of the form ${{(y_{0,n},u_{0,n},\ldots,u_{{T - 1},n},y_{T,n})},n} \in {\lbrack N\rbrack}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Recovering Theorem 1", "weight": 1.0} -->

In the partially observed setting, we thus define the analogous local minimax complexity as where the infimum is taken over all measurable functions of the data ${{(y_{0,n},u_{0,n},\ldots,u_{{T - 1},n},y_{T,n})},n} \in {\lbrack N\rbrack}$, ${\nabla_{K}J}{(K;G)}$ is given by equation and $d$ again is a metric on system parameters $G = {(A,B,C)}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Recovering Theorem 1", "weight": 1.0} -->

Equipped with the definition and Lemma 6 the proof of the following result follows similarly to that of Theorem 1.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Bad Markov Parameters Imply Noisy Gradients", "weight": 1.0} -->

Consider the almost scalar system $g_{1} = {(a,B,c)}$ given by defined consinstently with system, but specifically ${a,b,c} \in {\mathbb{R}}$ and $Q = \Sigma_{V} = \Sigma_{W} = 1$ and $R = I_{2}$. Note that the maximum singular values of the first Markov parameter of $g_{1}$ is equal to the product $m = {cb}$ and that this is $m$ is invariant under similarity transformation. We consider the two systems $g_{1} = {(a,B,c)}$ and $g_{2} = {(a,{B{(\Delta)}},c)}$ and where ${B{(\Delta)}} = \begin{bmatrix} \end{bmatrix}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Bad Markov Parameters Imply Noisy Gradients", "weight": 1.0} -->

Observe that the optimal policy to system is of the form $K_{\star} = \begin{bmatrix} \end{bmatrix}$ and that the gramians $P_{K_{\star},\nu,g_{1}}$ and $\Gamma_{K_{\star},g_{1}}$ are scalar and equal to $P_{K_{\star},\nu,g_{1}} = P_{k_{\star},\nu,g_{1}}$ and $\Gamma_{K_{\star},g_{1}} = \Gamma_{k_{\star},g_{1}}$ respectively. In other words, the second input has no effect on the system, but as well shall see, $g_{2}$ is very sensitive to perturbations $\Delta$ whenever the largest singular value of the Markov parameter $m = {|{cb}|}$ is small.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Bad Markov Parameters Imply Noisy Gradients", "weight": 1.0} -->

The large and small $c$ asymptotics of $\Sigma_{k_{\star},\nu,g_{1}}$ are proportional to $1/c^{2}$ The factor $|{a + {bk_{\star}}}|$ tends to 0 no faster than $1/b^{2}$ and tends to $\min{(1,{|a|})}$ as $b\rightarrow 0$ (and $|a|$ is invariant under similarity transform).

<!-- chunk {"id": "body-0032", "role": "body", "section": "Bad Markov Parameters Imply Noisy Gradients", "weight": 1.0} -->

Combining these observations, we see that as the system invariant ${|m|} = {|{cb}|}$ tends to zero, gradients become arbitrarily noisy; the lower bound tends to infinity. In other words, we have established that Thus, we obtain an RL analogue to the well-known fact that reparametrization cannot help controlling a partially observed system as any gain in observability is offset by a proportional loss in controllability and vice versa.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this work we showed that estimating policy gradients can become arbitrarily hard due to known control-theoretic fundamental limitations Doyle by leveraging the classic two point method due to Le Cam LeCam. For instance, we showed with system that a partially observed system with small Markov parameters necessarily has noisy policy gradients and that this holds independently of the parametrization. Our bounds also show that learning controllers that are close to marginal stability can be hard. This is similar to what has already been observed for adaptive LQR/LQG in Ziemann and Sandberg. Leveraging results from Tsiamis et al. we further show that estimating policy gradients can suffer from exponential complexity in the system dimension. From a broader perspective, these results work toward elucidating when learning to control is feasible.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Discussion", "weight": 1.5} -->

Acknowledgements: Ingvar Ziemann and Henrik Sandberg are supported by the Swedish Research Council and the Swedish Foundation for Strategic Research through the CLAS project (grant -0046). Nikolai Matni is supported in part by NSF awards CPS-2038873 and CAREER award ECCS-2045834, and a Google Research Scholar award.
