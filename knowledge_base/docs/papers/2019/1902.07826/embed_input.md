<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Certainty Equivalence Is Efficient for Linear Quadratic Control

Topics include Control, Linear quadratic regulator, Linear quadratic, Linear quadratic Gaussian, Fully observed, Riccati equation.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the performance of the certainty equivalent controller on Linear Quadratic (LQ) control problems with unknown transition dynamics. We show that for both the fully and partially observed settings, the sub-optimality gap between the cost incurred by playing the certainty equivalent controller on the true system and the cost incurred by using the optimal LQ controller enjoys a fast statistical rate, scaling as the square of the parameter error. To the best of our knowledge, our result is the first sub-optimality guarantee in the partially observed Linear Quadratic Gaussian (LQG) setting. Furthermore, in the fully observed Linear Quadratic Regulator (LQR), our result improves upon recent work by Dean et al., who present an algorithm achieving a sub-optimality gap linear in the parameter error. A key part of our analysis relies on perturbation bounds for discrete Riccati equations. We provide two new perturbation bounds, one that expands on an existing result from Konstantinov et al., and another based on a new elementary proof strategy.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

One of the most straightforward methods for controlling a dynamical system with unknown transitions is based on the *certainty equivalence principle*: a model of the system is fit by observing its time evolution, and a control policy is then designed by treating the fitted model as the truth. Despite the simplicity of this method, it is challenging to guarantee its efficiency because small modeling errors may propagate to large, undesirable behaviors on long time horizons. As a result, most work on controlling systems with unknown dynamics has explicitly incorporated robustness against model uncertainty.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we show that for the standard baseline of controlling an unknown linear dynamical system with a quadratic objective function known as Linear Quadratic (LQ) control, certainty equivalent control synthesis achieves *better* cost than prior methods that account for model uncertainty. Our results hold for both the fully observed Linear Quadratic Regulator (LQR) and the partially observed Linear Quadratic Gaussian (LQG) setting. For offline control, where one collects some data and then designs a fixed control policy to be run on an infinite time horizon, we show that the gap between the performance of the certainty equivalent controller and the optimal control policy scales *quadratically* with the error in the model parameters for both LQR and LQG. To the best of our knowledge, we provide the first sub-optimality guarantee for LQG. Moreover, in the LQR setting our work improves upon the recent result of Dean et al., who present an algorithm that achieves a sub-optimality gap linear in the parameter error.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the case of online LQR control, where one adaptively improves the control policy as new data comes, our offline result implies that a simple, polynomial time algorithm using $\varepsilon$-greedy exploration suffices for nearly optimal $\overset{\sim}{\mathcal{O}}{(\sqrt{T})}$ regret.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper is structured as follows. In Section 2 we present backround concepts and discuss our main result for LQR; we compare it to prior guarantees and discuss its consequences. Our results rely on a study of the sensitivity to parameter perturbations of the Bellman equation of LQR, known as the discrete algebraic Riccati equation. In Section 2.3, we assume the existence of a sensitivity guarantee, and use the guarantee to prove a meta theorem which quantifies the performance of the certainty equivalent controller. Then, in Section 3 we extend our main result for LQR to the more general case of LQG. Section 4 contains two explicit and interpretable upper bounds on the sensitivity of the Riccati solution: one based on a proof strategy proposed by Konstantinov et al. and one based on a direct approach that is of independent interest. We conclude and discuss future directions in Section 6.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Main Results for the Linear Quadratic Regulator", "weight": 1.0} -->

An instance of the linear quadratic regulator (LQR) is defined by four matrices: two matrices $A_{\star} \in {\mathbb{R}}^{n \times n}$ and $B_{\star} \in {\mathbb{R}}^{n \times d}$ that define the linear dynamics and two positive semidefinite matrices $Q \in {\mathbb{R}}^{n \times n}$ and $R \in {\mathbb{R}}^{d \times d}$ that define the cost function. Given these matrices, the goal of LQR is to solve the optimization problem

<!-- chunk {"id": "body-0008", "role": "body", "section": "Main Results for the Linear Quadratic Regulator", "weight": 1.0} -->

and can be computed efficiently \[4, see e.g.\]. In the sequel we use the notation ${\mathsf{d}\mathsf{a}\mathsf{r}\mathsf{e}}{(A_{\star},B_{\star},Q,R)}$ to denote the unique positive semidefinite solution of. Problem considers an average cost over an infinite horizon. The optimal controller for the finite horizon variant is also static and linear, but time-varying. The LQR solution in this case can be computed efficiently via dynamic programming.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Main Results for the Linear Quadratic Regulator", "weight": 1.0} -->

In this work we are interested in the control of a linear dynamical system with unknown transition parameters $(A_{\star},B_{\star})$ based on estimates $(\hat{A},\hat{B})$. The cost matrices $Q$ and $R$ are assumed known. We analyze the *certainty equivalence approach*: use the estimates $(\hat{A},\hat{B})$ to solve the optimization problem while disregarding the modeling error, and use the resulting controller on the true system $(A_{\star},B_{\star})$. We interchangeably refer to the resulting policy as the *certainty equivalent controller* or, following Dean et al., the *nominal controller*. We denote by $\hat{P}$ the solution to the Riccati equation associated with the parameters $(\hat{A},\hat{B})$ and let $\hat{K}$ be the corresponding controller.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Main Results for the Linear Quadratic Regulator", "weight": 1.0} -->

Let $\varepsilon \geq 0$ such that ${\parallel{A_{\star} - \hat{A}}\parallel} \leq \varepsilon$ and ${\parallel{B_{\star} - \hat{B}}\parallel} \leq \varepsilon$. (Here and throughout this work we use $\parallel \cdot \parallel$ to denote the Euclidean norm for vectors as well as the spectral (operator) norm for matrices.) Dean et al. introduced a robust controller that achieves ${\hat{J} - J_{\star}} \leq {C_{1}{(A_{\star},B_{\star},Q,R)}\varepsilon}$ for some complexity term $C_{1}{(A_{\star},B_{\star},Q,R)}$ that depends on the problem parameters.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Main Results for the Linear Quadratic Regulator", "weight": 1.0} -->

We show that the nominal controller $\mathbf{u}_{t} = {\hat{K}\mathbf{x}_{t}}$ achieves ${\hat{J} - J_{\star}} \leq {C_{2}{(A_{\star},B_{\star},Q,R)}\varepsilon^{2}}$. Both results require $\varepsilon$ to be sufficiently small (as a function of the problem parameters) and it is important to note that $\varepsilon$ must be much smaller for the nominal controller to be guaranteed to stabilize the system than for the robust controller proposed by Dean et al.. However, our result shows that once the estimation error $\varepsilon$ is small enough, the nominal controller performs better: the sub-optimality gap scales as $\mathcal{O}{(\varepsilon^{2})}$ versus $\mathcal{O}{(\varepsilon)}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Main Results for the Linear Quadratic Regulator", "weight": 1.0} -->

Both the more stringent requirement on $\varepsilon$ and better performance of nominal control compared to robust control, when the estimation error is sufficiently small, were observed empirically by Dean et al..

<!-- chunk {"id": "body-0013", "role": "body", "section": "Main Results for the Linear Quadratic Regulator", "weight": 1.0} -->

Before we can formally state our result we need to introduce a few more concepts and assumptions. It is common to assume that the cost matrices $Q$ and $R$ are positive definite. Under an additional observability assumption, this condition can be relaxed to $Q$ being positive semidefinite.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The cost matrices $Q$ and $R$ are positive definite. Since scaling both $Q$ and $R$ does not change the optimal controller $K_{\star}$, we can assume without loss of generality that ${\underset{¯}{\sigma}{(R)}} \geq 1$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

A square matrix $M$ is *stable* if its spectral radius $\rho{(M)}$ is (strictly) smaller than one. Recall that the spectral radius is defined as ${\rho{(M)}} = {\max{\{{{|\lambda|}:{\lambda\text{~is an eigenvalue of~}M}}\}}}$. A linear dynamical system $(A,B)$ in feedback with $K$ is fully described by the *closed loop matrix* $A + {BK}$. More precisely, in this case $\mathbf{x}_{t + 1} = {{{({A + {BK}})}\mathbf{x}_{t}} + \mathbf{w}_{t}}$. For a static linear controller $\mathbf{u}_{t} = {K\mathbf{x}_{t}}$ to achieve finite LQR cost it is necessary and sufficient that the closed loop matrix is stable.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

In order to quantify the growth or decay of powers of a square matrix $M$, we define

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

In other words, $\tau{(M,\rho)}$ is the smallest value such that ${\parallel M^{k}\parallel} \leq {\tau{(M,\rho)}\rho^{k}}$ for all $k \geq 0$. We note that $\tau{(M,\rho)}$ might be infinite, depending on the value of $\rho$, and it is always greater or equal than one. If $\rho$ is larger than $\rho{(M)}$, we are guaranteed to have a finite $\tau{(M,\rho)}$ (this is a consequence of Gelfand's formula). In particular, if $M$ is a stable matrix, we can choose $\rho < 1$ such that $\tau{(M,\rho)}$ is finite.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Also, we note that $\tau{(M,\rho)}$ is a decreasing function of $\rho$; if $\rho \geq {\parallel M\parallel}$, we have ${\tau{(M,\rho)}} = 1$. At a high level, the quantity $\tau{(M,\rho)}$ measures the degree of transient response of the linear system $\mathbf{x}_{t + 1} = {{M\mathbf{x}_{t}} + \mathbf{w}_{t}}$. In particular, when $M$ is stable, $\tau{(M,\rho)}$ can be upper bounded by the $\mathcal{H}_{\infty}$-norm of the system defined by $M$, which is the $\ell_{2}$ to $\ell_{2}$ operator norm of the system and a fundamental quantity in robust control \see [38, for more details\].

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Throughout this work we use the quantities $\Gamma_{\star}:={1 + {\max{\{{\parallel A_{\star}\parallel},{\parallel B_{\star}\parallel},{\parallel P_{\star}\parallel},{\parallel K_{\star}\parallel}\}}}}$ and $L_{\star}:={A_{\star} + {B_{\star}K_{\star}}}$. We use $\Gamma_{\star}$ as a uniform upper bound on the spectral norms of the relevant matrices for the sake of algebraic simplicity. We are ready to state our meta theorem.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

We assume the unknown system $(A_{\star},B_{\star})$ is $(\ell,\nu)$-controllable, with $\nu > 0$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Assumption 2 was used in a different context by Cohen et al.. For any controllable system and any $\ell \geq n$ there exists $\nu > 0$ such that the system is $(\ell,\nu)$-controllable. Therefore, $(\ell,\nu)$-controllability is really not much stronger of an assumption than controllability. As $\ell$ grows minimum singular value $\underset{¯}{\sigma}{(\mathcal{C}_{\ell})}$ also grows and therefore a larger $\nu$ can be chosen so that the system is still $(\ell,\nu)$ controllable.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Note that controllability is not necessary for LQR to have a well-defined solution: the weaker requirement is that of *stabilizability*, in which there exists a feedback matrix $K$ so that $A_{\star} + {B_{\star}K}$ is stable. The result of Dean et al. only requires stabilizability. While our upper bound on $\parallel{\hat{P} - P_{\star}}\parallel$ requires controllability, the result of Konstantinov et al. only requires stabilizability. However, our upper bound on $\parallel{\hat{P} - P_{\star}}\parallel$ is sharper for some classes of systems (see Section 4). Together with Theorem 1, our perturbation result, presented in Section 4, yields the following guarantee.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Case: $A_{\\star}$ is contractive, i.e. ${\\parallel A_{\\star}\\parallel} < 1$", "weight": 1.0} -->

In this case, we can choose $\rho = {\parallel A_{\star}\parallel}$ and $\varepsilon$ small enough so that $\varepsilon \leq {1 - {\parallel A_{\star}\parallel}}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Case: $B_{\\star}$ has rank $n$", "weight": 1.0} -->

In this case, we can choose $\ell = 1$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Comparison to Theorem 4.1 of Dean et al", "weight": 1.0} -->

We see that the dependence on the parameters $\Gamma_{\star}$ and $\tau{(L_{\star},\gamma)}$ is significantly milder compared to Equation 5. Furthermore, this upper bound is valid for larger $\varepsilon$ than the upper bound given in Theorem 2. Comparing these upper bound suggests that there is a price to pay for obtaining a fast rate, and that in regimes of moderate uncertainty (moderate size of $\varepsilon$), being robust to model uncertainty is important. This observation is supported by the empirical results of Dean et al..

<!-- chunk {"id": "body-0026", "role": "body", "section": "Comparison to Theorem 4.1 of Dean et al", "weight": 1.0} -->

A similar trade-off between slow and fast rates arises in the setting of first-order convex stochastic optimization. The convergence rate $\mathcal{O}{({1/\sqrt{T}})}$ of the stochastic gradient descent method can be improved to $\mathcal{O}{({1/T})}$ under a strong convexity assumption. However, the performance of stochastic gradient descent, which can achieve a $\mathcal{O}{({1/T})}$ rate, is sensitive to poorly estimated problem parameters. Similarly, in the case of LQR, the nominal controller achieves a fast rate, but it is much more sensitive to estimation error than the robust controller of Dean et al..

<!-- chunk {"id": "body-0027", "role": "body", "section": "End-to-end guarantees", "weight": 1.0} -->

Theorem 2 can be combined with finite sample learning guarantees (e.g. ) to obtain an end-to-end guarantee similar to Proposition 1.2 of Dean et al.. In general, estimating the transition parameters from $N$ samples yields an estimation error that scales as $\mathcal{O}{({1/\sqrt{N}})}$. Therefore, Theorem 2 implies that ${\hat{J} - J_{\star}} \leq {\mathcal{O}{({1/N})}}$ instead of the ${\hat{J} - J_{\star}} \leq {\mathcal{O}{({1/\sqrt{N}})}}$ rate from Proposition 1.2 of Dean et al.. This is similar to the case of linear regression, where $\mathcal{O}{({1/\sqrt{N}})}$ estimation error for the parameters translates to a $\mathcal{O}{({1/N})}$ *fast rate* for prediction error.

<!-- chunk {"id": "body-0028", "role": "body", "section": "End-to-end guarantees", "weight": 1.0} -->

Furthermore, Simchowitz et al. and Sarkar and Rakhlin showed that faster estimation rates are possible for some linear dynamical systems. Theorem 2 translates such rates into control suboptimality guarantees in a transparent way.

<!-- chunk {"id": "body-0029", "role": "body", "section": "End-to-end guarantees", "weight": 1.0} -->

Our result explains the behavior observed in Figure 4 of Dean et al.. The authors propose two procedures for synthesizing robust controllers for LQR with unknown transitions: one which guarantees robustness of the performance gap $\hat{J} - J_{\star}$, and one which only guarantees the stability of the closed loop system. Dean et al. observed that the latter performs better in the small estimation error regime, which happens because the robustness constraint of the synthesis procedure becomes inactive when the estimation error is small enough. Then, the second robust synthesis procedure effectively outputs the certainty equivalent controller, which we now know to achieve a fast rate.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Nearly optimal $\\overset{\\sim}{\\mathcal{O}}{(\\sqrt{T})}$ regret in the adaptive setting", "weight": 1.0} -->

Abbasi-Yadkori and Szepesvári study the performance of optimism in the face of uncertainty (OFU) and show that it has $\overset{\sim}{\mathcal{O}}{(\sqrt{T})}$ regret, which is nearly optimal for this problem formulation. However, the OFU algorithm requires repeated solutions to a non-convex optimization problem for which no known efficient algorithm exists.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Nearly optimal $\\overset{\\sim}{\\mathcal{O}}{(\\sqrt{T})}$ regret in the adaptive setting", "weight": 1.0} -->

To deal with the computational issues of OFU, Dean et al. propose to analyze the behavior of $\varepsilon$-greedy exploration using the suboptimality gap results of Dean et al.. In the context of continuous control, $\varepsilon$-greedy exploration refers to the application of the control law $\mathbf{u}_{t} = {{\pi{(\mathbf{x}_{t},\mathbf{x}_{t - 1},\ldots,\mathbf{x}_{0})}} + \eta_{t}}$ with $\eta_{t} \sim {\mathcal{N}{(0,{\sigma_{\eta,t}^{2}I_{d}})}}$, where $\pi$ is the policy, updated in epochs, and $\sigma_{\eta,t}^{2}$ is the variance of the exploration noise.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Nearly optimal $\\overset{\\sim}{\\mathcal{O}}{(\\sqrt{T})}$ regret in the adaptive setting", "weight": 1.0} -->

Here, the optimal variance of the exploration noise scales as $\sigma_{\eta,t}^{2} \sim t^{- {1/2}}$, yielding $\overset{\sim}{\mathcal{O}}{(\sqrt{T})}$ regret. We note that the observation that certainty equivalence coupled with $\varepsilon$-greedy exploration achieves $\overset{\sim}{\mathcal{O}}{(\sqrt{T})}$ regret was first made by Faradonbeh et al..

<!-- chunk {"id": "body-0033", "role": "body", "section": "Main Results for the Linear Quadratic Gaussian Problem", "weight": 1.0} -->

Now we consider partially observable systems.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Main Results for the Linear Quadratic Gaussian Problem", "weight": 1.0} -->

In, only the output process $\mathbf{y}_{t}$ is observed. The LQG problem is defined as^11^1Note that many texts define the LQG cost in terms of $\mathbf{x}_{t}^{\mathsf{T}}Q\mathbf{x}_{t}$ instead of $\mathbf{y}_{t}^{\mathsf{T}}Q\mathbf{y}_{t}$. We choose the latter because we do not want the cost to be tied to a particular (unknown) state representation.:

<!-- chunk {"id": "body-0035", "role": "body", "section": "Main Results for the Linear Quadratic Gaussian Problem", "weight": 1.0} -->

There is an inherent ambiguity in the dynamics (9a)-(9b) which makes LQG more delicate than LQR. In particular, for any invertible $T$, the LQG problem with parameters $(A_{\star},B_{\star},C_{\star},Q,R)$ is equivalent to the LQG problem with parameters $({TA_{\star}T^{- 1}},{TB_{\star}},{C_{\star}T^{- 1}},Q,R)$ and appropriately rescaled noise processes.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Main Results for the Linear Quadratic Gaussian Problem", "weight": 1.0} -->

Recent work has shown how to obtain this style of estimates with guarantees from input/output data. As in Section 2, we assume that the cost matrices $(Q,R)$ are known.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Main Results for the Linear Quadratic Gaussian Problem", "weight": 1.0} -->

Similarly to Theorem 1 for LQR, we state a meta theorem for LQG. Unlike Theorem 1, however, we need a stronger type of Riccati perturbation guarantee which also allows for perturbation of the $Q$ matrix. Specifically, we suppose there exists $\gamma_{0}$ such that for any $\gamma \leq \gamma_{0}$ and $(\hat{A},\hat{B},\hat{Q})$ with ${\max{\{{\parallel{\hat{A} - A}\parallel},{\parallel{\hat{B} - B}\parallel},{\parallel{\hat{Q} - Q}\parallel}\}}} \leq \gamma$ the solutions $P$ and $\hat{P}$ of the Riccati equations with parameters $(A,B,Q,R)$ and $(\hat{A},\hat{B},\hat{Q},R)$ satisfy

<!-- chunk {"id": "body-0038", "role": "body", "section": "Main Results for the Linear Quadratic Gaussian Problem", "weight": 1.0} -->

for an increasing function $f$ with ${f{(\gamma)}} \geq \gamma$. The constant $\gamma_{0}$ and function $f$ are allowed to depend on the parameters $(A,B,Q,R)$. In Section 4, we present a perturbation bound (Proposition 2) that satisfies these properties. Similarly to Section 2, let $\Gamma_{\star}:={1 + {\max{\{{\parallel A_{\star}\parallel},{\parallel B_{\star}\parallel},{\parallel C_{\star}\parallel},{\parallel K_{\star}\parallel},{\parallel L_{\star}\parallel},{\parallel P_{\star}\parallel}\}}}}$. The following theorem is our main result for LQG.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Riccati Perturbation Theory", "weight": 1.0} -->

As discussed in Sections 2 and 3, a key piece of our analysis is bounding the solutions to discrete Riccati equations as we perturb the problem parameters. Specifically, we are interested in quantities $b,L$ such that ${\parallel{\hat{P} - P_{\star}}\parallel} \leq {L\varepsilon}$ if $\varepsilon < b$, where $\varepsilon$ represents a bound on the perturbation. We note that it is not possible to find universal values $b,L$. Consider the systems ${(A_{\star},B_{\star})} = {(1,\varepsilon)}$ and ${(\hat{A},\hat{B})} = {}$; the latter system is not stabilizable and hence $\hat{P}$ does not even exist. Therefore, $b$ and $L$ must depend on the system parameters.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Riccati Perturbation Theory", "weight": 1.0} -->

While there is a long line of work analyzing perturbations of Riccati equations, we are not aware of any result that offers explicit and easily interpretable $b$ and $L$ for a fixed $(A_{\star},B_{\star},Q,R)$; see Konstantinov et al. for an overview of this literature. In this section, we present two new results for Riccati perturbation which offer interpretable bounds. The first one expands upon the operator-theoretic proof of Konstantinov et al.; its proof can be found in Section 4.1. In this result we assume the cost matrix $Q$ can also be perturbed, which is needed for our LQG guarantee. In order to be consistent we denote the true cost matrix by $Q_{\star}$ and the estimated one by $\hat{Q}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Though a naïve Taylor expansion suggests that the fast rates we derive here must be achievable, precisely computing such rates has been open since the 80s. All of the pieces we used here have existed in the literature for some time, and perhaps it has just required a bit of time to align contemporary rate-analyses in learning theory with earlier operator theoretic work in optimal control. There remain many possible extensions to this work. The robust control approach of Dean et al. applies to many different objective functions besides quadratic costs, such as $\mathcal{H}_{\infty}$ and $\mathcal{L}_{1}$ control. It would be interesting to know whether fast rates for control are possible for other objective functions. Finally, determining the optimal minimax rate for both LQR and LQG would allow us to understand the tradeoffs between nominal and robust control at a more fine grained level.
