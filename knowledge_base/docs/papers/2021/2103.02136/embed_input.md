<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Toward a Scalable Upper Bound for a CVaR-LQ Problem

Topics include Optimal control, Control, Conditional value at risk, Dynamic programming.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study a linear-quadratic, optimal control problem on a discrete, finite time horizon with distributional ambiguity, in which the cost is assessed via Conditional Value-at-Risk (CVaR). We take steps toward deriving a scalable dynamic programming approach to upper-bound the optimal value function for this problem. This dynamic program yields a novel, tunable risk-averse control policy, which we compare to existing state-of-the-art methods.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The standard approach to stochastic optimal control is to evaluate a random cumulative cost in expectation. However, this approach is not designed to protect against worst-case circumstances. This limitation motivates robust optimal control and related methods, such as minimax model predictive control and mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Robust methods typically assume bounded disturbances, which excludes certain common noise models, such as Gaussian noise. A technique to alleviate this restriction is to use a *risk-averse* formulation, in which a random cost is assessed via *exponential utility*. Here, the objective takes the form ${\mathcal{J}_{\gamma}{(x,\pi)}}:={\frac{1}{\gamma}{\log\left( {E_{x}^{\pi}{(e^{{\gammaZ}/2})}} \right)}}$, where $Z \geq 0$ is a random cumulative cost, $\pi$ is a control policy, $x$ is an initial condition, and $\gamma > 0$ is a risk-aversion parameter.^11^1One may consider $\gamma < 0$, which corresponds to a *risk-seeking* perspective. We focus on the *risk-averse* perspective here, which assumes that noise leads to harm rather than benefit.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This problem has been studied in increasing levels of generality from the 1970s to the 2010s, e.g., see. As $\gamma$ increases, the criterion $\mathcal{J}_{\gamma}{(x,\pi)}$ represents a more risk-averse perspective, while as $\gamma$ approaches zero, $\mathcal{J}_{\gamma}{(x,\pi)}$ tends to the usual expected cost.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the case of linear dynamics with Gaussian noise and quadratic costs, the problem of optimizing $\mathcal{J}_{\gamma}{(x,\pi)}$ is commonly called LEQR control. For a fixed $\gamma > 0$, a Riccati recursion is used to derive the optimal value functions and the optimal control law, which is linear state-feedback. At each step $t$ of the recursion, it must be the case that the matrix $\Sigma^{- 1} - {\gamma{\overline{P}}_{t + 1}}$ is positive definite, where $\Sigma$ is the covariance of the process noise, and ${\overline{P}}_{t + 1}$ is the matrix obtained from step $t + 1$. If $\gamma$ is chosen too large, then the above condition may be violated, and the controller synthesis procedure breaks down.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The *Conditional Value-at-Risk* (CVaR) functional, which was invented in the early 2000s by the financial engineering community, has potential to alleviate the above issues. The CVaR of $Z$ at level $\alpha \in {(0,1\rbrack}$ represents the expectation of the $\alpha \cdot {100\%}$ largest values of $Z$. The intuitive interpretation of CVaR and its quantitative characterization of risk aversion (in terms of a *fraction* of worst-case outcomes) are two reasons for its popularity in financial engineering (see and the references therein) and its emerging popularity in control (e.g., see ). In addition to financial applications, CVaR may be a useful tool for the design of stormwater systems, which are required to satisfy precise regulatory specifications, and for the operation of robotic systems.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, the optimization of CVaR is computationally expensive in general. Unlike the expectation of a random (cumulative) cost, the CVaR of a random cost, subject to the dynamics of a Markov decision process, does *not* satisfy a dynamic programming (DP) recursion on the state space. One way to resolve this issue and make DP valid is via a suitable state augmentation.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Here, we study a linear-quadratic optimal control problem with *distributional ambiguity*, where the cost is assessed via CVaR. Our first step is to derive an upper bound to the optimal value of this problem. This derivation (Theorem 3.2). ‣ 3 Upper Bound for CVaR-LQ Problem ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem")) and additional analysis (Theorem 4.8. ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem")) motivate the formulation of an interesting dynamic programming algorithm (Theorem 5.15). While the associated value functions are defined on an augmented state space, they are computed in a *scalable* fashion since their parameters come from a Riccati-like recursion. Moreover, our algorithm provides a risk-averse controller, in which a risk-aversion level is parameterized in a novel way through a positive definite matrix.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

While our controller synthesis procedure is more computationally complex than LEQR, it does not involve a condition that is analogous to the positive definiteness of $\Sigma^{- 1} - {\gamma{\overline{P}}_{t + 1}}$ for all $t$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Linear-Quadratic System Model", "weight": 1.0} -->

We make the following assumptions about the ${\mathbb{R}}^{n}$-valued disturbance process $(W_{0},W_{1},\ldots,W_{N - 1})$. $W_{t}$ and $W_{s}$ are independent for all $t \neq s$, and $W_{t}$ is independent of the initial state $X_{0}$ for each $t$. For each $t$, the exact distribution of $W_{t}$ is not known. However, the first and maximal second moment of $W_{t}$ are known, which we specify below.

<!-- chunk {"id": "body-0012", "role": "body", "section": "CVaR-Risk-Averse Optimal Control Problem", "weight": 1.0} -->

Consider a CVaR optimal control problem on a discrete, finite time horizon with distributional ambiguity: subject to the linear dynamics, where $x \in {\mathbb{R}}^{n}$ is an initial condition and $\alpha \in {(0,1\rbrack}$ is a risk-aversion level. The objective $\text{CVaR}_{\alpha,x}^{\pi,\gamma}{(Z)}$ is the CVaR of $Z$ at level $\alpha$, when the system is initialized at $x$ and evolves according to a control policy $\pi \in \Pi$ and a disturbance strategy $\gamma \in \Gamma$. ($\gamma$ provides a distribution for $W_{t}$ for each $t$. $\Pi$ and $\Gamma$ will be defined in this section.) The CVaR of $Z$ represents the expectation of the $\alpha \cdot 100$% largest values of $Z$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "CVaR-Risk-Averse Optimal Control Problem", "weight": 1.0} -->

While the problem does not satisfy a dynamic programming (DP) recursion on ${\mathbb{R}}^{n}$, there is a useful DP recursion on ${\mathbb{R}}^{n} \times {\mathbb{R}}$ (Lemma 4.12. ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem")). A CVaR optimal control problem *without* distributional ambiguity has been solved by defining an augmented state space. Taking inspiration, we use a ${\mathbb{R}}^{n} \times {\mathbb{R}}$-valued, random *augmented state* $(X_{t},S_{t})$. The dynamics of $X_{t}$ are given. $S_{t}$ is a $\mathbb{R}$-valued random variable, whose dynamics are given by $S_{t}$ keeps track of the random cumulative cost up to time $t$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "CVaR-Risk-Averse Optimal Control Problem", "weight": 1.0} -->

The realizations of $(X_{0},S_{0})$ are concentrated at an arbitrary point ${(x,s)} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}}$. We use the *augmented state space* ${\mathbb{R}}^{n} \times {\mathbb{R}}$ to define $\Pi$, the class of history-dependent control policies that summarize the history through $(X_{t},S_{t})$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Probability Space for Random Cumulative Cost", "weight": 1.0} -->

Every $\omega \in \Omega$ takes the form $\omega = {(x_{0},s_{0},u_{0},\ldots,x_{N - 1},s_{N - 1},u_{N - 1},x_{N},s_{N})}$, where ${(x_{t},s_{t})} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}}$ is the value of $(X_{t},S_{t})$ and $u_{t} \in {\mathbb{R}}^{m}$ is the value of $U_{t}$ in the trajectory $\omega$. We have specified implicitly that the coordinates of $\omega$ have causal dependencies via and Definition 2 ‣ 2.3 CVaR-Risk-Averse Optimal Control Problem ‣ 2 A CVaR-Linear-Quadratic Problem ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem").

<!-- chunk {"id": "body-0016", "role": "body", "section": "Probability Space for Random Cumulative Cost", "weight": 1.0} -->

The form of $P_{x,s}^{\pi,\gamma}$ on measurable rectangles is known, and it depends on the dynamics of the augmented state, an initial augmented condition ${(x,s)} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}}$, a control policy $\pi \in \Pi$, and a disturbance strategy $\gamma \in \Gamma$ (Ionescu-Tulcea Theorem). For instance, see \[17, Prop. 7.28\] or \[18, Prop. C.10, Remark C.11\] for details.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Remark 1", "weight": 1.0} -->

where $Y$ is a random variable such that ${E{({|Y|})}} < {+ \infty}$. In, we use an *extended definition* for CVaR to permit a class of policies $\Pi$ that depends on the augmented state space and need not have a particular analytical form (e.g., linear).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Upper Bound for CVaR-LQ Problem", "weight": 1.0} -->

We use the definition of $\text{CVaR}_{\alpha,x}^{\pi,\gamma}{(Z)}$ to re-express $J_{\alpha}^{\ast}{(x)}$. For any $x \in {\mathbb{R}}^{n}$ and $\alpha \in {(0,1\rbrack}$, it holds that In the current section, first we show that there is a policy $\pi \in \Pi$ such that $J_{\alpha,\pi}{(x)}$ is finite (Lemma 1 is finite for some 𝜋) ‣ 3 Upper Bound for CVaR-LQ Problem ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem")), which guarantees that the problem is well-defined. Second, we derive an upper bound to $J_{\alpha}^{\ast}{(x)}$ (Theorem 3.2).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Upper Bound for CVaR-LQ Problem", "weight": 1.0} -->

‣ 3 Upper Bound for CVaR-LQ Problem ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem")): with ${V_{0}^{\ast}{(x,s)}}:={\inf_{\pi \in \Pi}{\sup_{\gamma \in \Gamma}{E_{x,s}^{\pi,\gamma}{({\max{({Z - S_{0}},0)}})}}}}$. Toward the goal of computing $V_{0}^{\ast}$ scalably, we will define a value iteration algorithm with value functions $V_{N},\ldots,V_{1},V_{0}$ (Section 4). We will analyze the algorithm in the setting of deterministic policies and finitely many disturbance values.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Upper Bound for CVaR-LQ Problem", "weight": 1.0} -->

We will show that, under a measurable selection assumption, ${\overline{V}}_{0}^{\ast} \leq {\overline{V}}_{0}$ (Theorem 4.8. ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem")), where ${\overline{V}}_{0}^{\ast}$ and ${\overline{V}}_{0}$ are the versions of $V_{0}^{\ast}$ and $V_{0}$ in the simplified setting, respectively. In Section 5, we will prove that $V_{0} \leq {\hat{V}}_{0}$, where such that $a_{0} \in {\mathbb{R}}$ and $P_{0} > 0$ are obtained via a Riccati-like recursion (Theorem 5.15). We will explain how the proof of Theorem 5.15 provides an algorithm for a novel risk-averse controller.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Upper Bound for CVaR-LQ Problem", "weight": 1.0} -->

Also, the above analysis takes key steps toward deriving a *scalable* upper bound to a CVaR linear-quadratic optimal control problem with distributional ambiguity.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Analysis of a Value Iteration Algorithm", "weight": 1.0} -->

To estimate $V_{0}^{\ast}$. ‣ 3 Upper Bound for CVaR-LQ Problem ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem")) in a scalable fashion, we propose a value iteration algorithm on ${\mathbb{R}}^{n} \times {\mathbb{R}}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Conjecture 4.4", "weight": 1.0} -->

The functions $V_{N - 1},\ldots,V_{1},V_{0}$ are Borel measurable and bounded below by 0.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Conjecture 4.4", "weight": 1.0} -->

We use the Conjecture in the proof of Theorem 5.15, which requires the Lebesgue integrals in Algorithm 1 ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem") to exist. The Conjecture will be proved formally in future work by using properties of convex functions.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Conjecture 4.4", "weight": 1.0} -->

In this work, we will analyze Algorithm 1 ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem") in the setting of finitely many disturbance values and deterministic policies.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Algorithm 2 (Value Iteration in Finite Case)", "weight": 1.0} -->

Let the functions ${\overline{V}}_{N},{\overline{V}}_{N - 1},\ldots,{\overline{V}}_{0}$ be defined recursively as follows. For all ${(x,s)} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}}$ and for $t = {{N - 1},\ldots,1,0}$, The next theorem specifies properties of Algorithm 2 ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem").

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 4.9", "weight": 1.0} -->

Theorem 4.8. ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem") invokes a measurable selection assumption (see also \[18, Th. 3.2.1\]), which motivates future study of measurable selection theorems.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 4.9", "weight": 1.0} -->

To prove Theorem 4.8. ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem"), we present two supporting results.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Scalable Upper Bound", "weight": 1.0} -->

Here, we return to the setting where there may be uncountably many disturbance values. We will derive a scalable upper bound to $V_{0}$ (Alg. 1 ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem")) of the form, ${{\hat{V}}_{0}{(x,s)}}:={a_{0} + {\max{({{x^{T}P_{0}x} - s},0)}}}$ for all ${(x,s)} \in {{\mathbb{R}}^{n} \times {\mathbb{R}}}$, where $a_{0} \in {\mathbb{R}}$ and a positive definite symmetric matrix $P_{0} \in {\mathbb{R}}^{n \times n}$ are obtained through a Riccati-like recursion. The recursion is parameterized by a positive definite symmetric matrix $L$ and provides a risk-averse controller.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Scalable Upper Bound", "weight": 1.0} -->

After the proof of Theorem 5.15, we will describe the controller synthesis procedure.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 5.16 (About $L$, $P_{t}$, $a_{t}$)", "weight": 1.0} -->

$P_{t}$ and $a_{t}$ are parameterized by $L$. In the finite-time case above, $L \in {\mathbb{R}}^{n \times n}$ is only required to be symmetric and positive definite.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 5.18 (Controller Synthesis)", "weight": 1.0} -->

We now identify some interesting similarities and differences between our approach and classical methods.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 5.19 (Relation to LEQR and LQ games)", "weight": 1.0} -->

The Riccati recursion for the LEQR problem in finite time takes the form: for $t = {{N - 1},\ldots,1,0}$, provided that $\gamma > 0$ is chosen so that $\Sigma^{- 1} - {\gamma{\overline{P}}_{t + 1}}$ is positive definite for each $t$. Similarly, the Riccati recursion for a soft-constrained LQ game takes the form \[1, Eq. 3.4a', p. 53\]: for $t = {{N - 1},\ldots,1,0}$, provided that ${\hat{P}}_{t}$ is invertible for each $t$, $R = I_{m}$, and $\lambda$ is a scalar parameter representing a disturbance-attenuation level. The key differences between, (33. ‣ 5 A Scalable Upper Bound ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem")), and (34.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 5.19 (Relation to LEQR and LQ games)", "weight": 1.0} -->

‣ 5 A Scalable Upper Bound ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem")) appear in the terms $\gamma\Sigma$, $\frac{1}{\lambda^{2}}\Sigma$, and ${({P_{t + 1} + L})}^{- 1}$, respectively. Our recursion encodes a risk-aversion level through the matrix ${({P_{t + 1} + L})}^{- 1}$, whereas the classical recursions (33. ‣ 5 A Scalable Upper Bound ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem")) (34. ‣ 5 A Scalable Upper Bound ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem")) encode risk aversion by scaling the covariance $\Sigma$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 5.20 (Relation to minimax MPC)", "weight": 1.0} -->

One may interpret an LEQR controller in a model-predictive-control (MPC) setting as an approximate solution to minimax MPC \[3, p. 99\]. In minimax MPC, a matrix $\mathcal{T} \geq 0$, which depends on a bounded region containing the process noise, appears in the algorithm that provides an optimal control \[3, Eq. 8.29, p. 99\]. Our recursion has a similar structure since it is parameterized by a matrix $L > 0$, and it is plausible that a preferable choice of $L$ depends on the maximal covariance $\Sigma$ (a topic for future investigation). A key distinction between minimax MPC and our approach is the uncertainty model of the process noise. Our approach permits process noise with an unbounded support and a spectrum of possibilities that occur with various probabilities. However, minimax MPC permits process noise that lives in a bounded region with known bounds \[3, p. 42\]. The "better" uncertainty model may be application-dependent.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Numerical Simulation", "weight": 1.0} -->

Fig. 1 provides example trade-off curves comparing LEQR (as $\gamma$ varies) with our proposed approach from Section 5 (as $L$ varies). These results show that for a simple one-state system, our proposed approach (ACVaR) has comparable performance relative to LEQR. This finding is notable given the simplicity of our experiment and that our method avoids the case where $\gamma$ is too large and the LEQR cost becomes infinite. We also simulated the optimal CVaR controller, which is not distributionally robust. This controller assumes exact prior knowledge of the disturbance distribution, which explains its superior performance. However, this optimal CVaR controller is not scalable to higher-dimensional problem instances, since it requires discretizing the augmented state space.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

We took steps toward deriving a scalable upper bound to a distributionally robust, CVaR optimal control problem for linear systems with quadratic costs. CVaR characterizes the (usually abstract) notion of risk as a fraction of worst-case outcomes, which is intuitive and precise. A result from our analysis is a risk-averse controller with intriguing similarities and differences relative to the state-of-the-art.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

Potential areas for future work include studying the infinite-horizon case, characterizing the extent to which the upper bound approximation parameterized by $L$ is tight, and elucidating the connections between the choice of $L$ and the maximal covariance $\Sigma$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

Further numerical experiments, potentially with higher-dimensional or more realistic application-specific examples, are needed to ascertain whether the proposed approach may be a superior alternative to LEQR in certain application domains.
