## Introduction

Classical model-based control enables simple but powerful control design by considering typically parametric mathematical abstractions of system behaviors, known as models. However, this comes at the cost of additional modeling and identification effort, which constitutes the majority of the budget in model-based control design, in terms of both time and cost. In this regard, the concept of data-driven control provides an appealing alternative that designs the controller directly from data without parametric identification.

In this work, we focus on data-driven predictive control (DDPC), the data-driven counterpart to model predictive control (MPC). Similar to MPC, it solves a finite-horizon optimal control problem in a receding horizon fashion, but with nonparametric data-driven predictors instead of model-based predictors. Data-driven predictors for linear systems can be constructed by using the so-called Willems' fundamental lemma, which characterizes all possible system behaviors with finite data.

While these predictors work well with deterministic data, showing equivalence to model-based design, they become ill-defined with stochastic data. Multiple works have stressed this issue by introducing an inner problem that finds the 'optimal' predictor under some statistical principle, e.g., Fiedler and Lucia; Yin et al.; Breschi et al.. This idea is known as indirect DDPC.

These stochastic data-driven predictors can be applied to DDPC design similar to the noise-free case. However, they suffer from the following problems with this certainty-equivalent implementation: 1) the control cost does not account for the prediction error, 2) the initial condition measurements suffer from noise which cannot be improved by collecting more data, and 3) the constraint satisfaction is not guaranteed. Aspects of these problems have been analyzed under the robust control framework where a bounded uncertainty set is prescribed. On the other hand, the situation is less clear under the stochastic control framework, where existing works adopt restrictive assumptions, such as noise-free offline data and exact polynomial chaos expansions of stochastic measurements. This paper addresses these problems under general unbounded stochastic uncertainties, utilizing the prediction error quantification provided in Yin et al..

In particular, three modifications are made to the certainty-equivalent DDPC algorithm. 1) The nominal control cost is replaced by the expected control cost. This introduces an additional uncertainty term that resembles the regularizer used empirically for DDPC problems, but here the weight is specified statistically without tuning. 2) The output initial condition is estimated by Kalman-filtering the output measurements with one-step-ahead predictions from the previous timestep. This significantly reduces the prediction error. 3) Output constraints are formulated as chance constraints and guaranteed by second-order cone (SOC) constraints. The effectiveness of these modifications is tested in a numerical example, where satisfactory control performance in terms of both control cost and constraint satisfaction is observed with significantly improved initial condition estimation.

Notation. The expected value, standard deviation, and covariance are denoted by ${\mathbb{E}}{\lbrack \cdot \rbrack}$, $\text{std}{( \cdot )}$, and $\text{cov}{( \cdot )}$, respectively. The symbol $\text{Pr}{( \cdot )}$ indicates the probability of a random event. For a sequence of matrices $X_{1},\ldots,X_{n}$, we denote the row-wise and diagonal-wise concatenation by $\text{col}\left( X_{1},\ldots,X_{n} \right)$ and $\text{blkdiag}\left( X_{1},\ldots,X_{n} \right)$, respectively. $\text{diag}{( \cdot )}$ denotes the vector of diagonal elements of a square matrix. Given a signal $x:{{\mathbb{Z}}\rightarrow{\mathbb{R}}^{n}}$, its trajectory from $k$ to ${k + N} - 1$ is indicated by ${(x_{i})}_{i = k}^{{k + N} - 1} = {\text{col}{(x_{k},\ldots,x_{{k + N} - 1})}}$. For a vector $x$, $\left. \parallel x\parallel \right._{P}$ denotes the weighted $l_{2}$-norm ${({x^{\top}Px})}^{\frac{1}{2}}$. The rank and trace of a matrix are indicated by $\text{rank}{( \cdot )}$ and $\text{tr}{( \cdot )}$, respectively.

## Problem Formulation

Consider the observable part of a stable discrete-time linear time-invariant (LTI) dynamical system with disturbance and output noise, given by where $x_{t} \in {\mathbb{R}}^{n_{x}}$, $u_{t} \in {\mathbb{R}}^{n_{u}}$, $y_{t} \in {\mathbb{R}}^{n_{y}}$, $w_{t} \in {\mathbb{R}}^{n_{w}}$, $v_{t} \in {\mathbb{R}}^{n_{y}}$ are the states, inputs, outputs, disturbance, and output noise, respectively. The noise-free output is denoted by $y_{t}^{0}$. In this paper, the noise $v_{t}$ is considered to be zero-mean i.i.d. with covariance ${\text{cov}\left(v_{t} \right)} = {\sigma^{2}{\mathbb{I}}_{n_{y}}}$.

The model parameters $(A,B,C,D,E)$ are unknown, but a matrix of input-disturbance-output trajectory data $Z = \begin{bmatrix} \end{bmatrix}$ has been collected, where each column is a length-$L$ trajectory of the system, where the superscript $d$ denotes collected offline data. The availability of offline disturbance trajectories retroactively is commonly assumed in DDPC algorithms, e.g., Pan et al., and is practical in many applications. The noise in each column of outputs is assumed to be independent. This assumption holds exactly when the columns are separate trajectories or truncated from a longer trajectory with $t_{i + 1} = {t_{i} + L}$, known as the Page construction. Another common construction of $Z$ is by choosing $t_{i + 1} = {t_{i} + 1}$, forming a block Hankel matrix. The matrix $Z$ is dubbed the signal matrix.

We are interested in designing a receding horizon control algorithm with a predictor derived from the signal matrix $Z$ instead of the model parameters. Such algorithms are known as indirect DDPC. Let $L = {L_{0} + L'}$, and $L_{0}$ be no smaller than the observability index of the system. In this paper, we consider the stochastic optimal tracking problem within a horizon of $L'$ that minimizes the following expected control cost at time $t$, where ${\hat{u}}_{k}^{t}$ is the designed input at time $({t + k})$, ${\hat{y}}_{k}^{t}$ is a random variable that predicts the noise-free future output $y_{t + k}^{0}$, $r_{t}$ denotes the reference trajectory, and $Q,R$ are the output and the input cost matrices respectively.

It is also desired to constrain the outputs within a polytopic set $\mathcal{Y}_{t}:=\left\{ y_{t} \middle| {{H^{t}y_{t}} \leq q^{t}} \right\}$ at time $t$, where $H^{t}:=\left\lbrack {h_{1}^{t}\ldots h_{n_{c}}^{t}} \right\rbrack^{\top} \in {\mathbb{R}}^{n_{c} \times n_{y}}$ and $q^{t}:={\text{col}\left(q_{1}^{t},\ldots,q_{n_{c}}^{t} \right)} \in {\mathbb{R}}^{n_{c}}$. However, due to the existence of unbounded noise, the output constraints can only be satisfied with high probability as chance constraints, which will be detailed in later sections. The input is constrained to be in the set $\mathcal{U}^{t}$ at time $t$, i.e., Then, the first element in the optimal input sequence is applied to the system, i.e., $u_{t}:={\hat{u}}_{0}^{t}$ and the noisy output $y_{t} = {y_{t}^{0} + v_{t}}$ is measured.

There are multiple aspects to consider when solving this problem, which will be discussed in the following sections.

There are uncertainties in both the prediction conditions and the signal matrix. An accurate predictor is desired under these uncertainties.

The expected control cost needs to be formulated as a tractable objective function.

Tractable formulations of the output constraints need to be derived.

## Stochastic Data-Driven Predictor

### Deterministic Prediction

With sufficiently persistently exciting inputs, the range space of $Z$ contains all possible trajectories of the system in the noise-free case, i.e., $v_{t} = \mathbf{0}_{n_{y}}$. The following result derived from the Willems' fundamental lemma provides a deterministic prediction by considering the augmented inputs $\psi_{t}:={\text{col}\left( u_{t},w_{t} \right)}$.

### Proposition 1

where $U \in {\mathbb{R}}^{{n_{u}L} \times M}$, $W \in {\mathbb{R}}^{{n_{w}L} \times M}$, $Y_{p} \in {\mathbb{R}}^{{n_{y}L_{0}} \times M}$, $Y_{f} \in {\mathbb{R}}^{{n_{y}L'} \times M}$, and $\Psi \in {\mathbb{R}}^{{{({n_{u} + n_{w}})}L} \times M}$. If $v_{t} = \mathbf{0}_{n_{y}}$ and ${\text{𝑟𝑎𝑛𝑘}{(Z)}} = {{{({n_{u} + n_{w}})}L} + n_{x}}$, we have where ${\hat{\mathbf{u}}}^{t}:={({\hat{u}}_{k}^{t})}_{k = 0}^{L' - 1}$ denotes the input sequence within the control horizon, $\mathbf{u}_{\text{𝑖𝑛𝑖}}^{t}:={(u_{k})}_{k = {t - L_{0}}}^{t - 1}$, $\mathbf{y}_{\text{𝑖𝑛𝑖}}^{t}:={(y_{k})}_{k = {t - L_{0}}}^{t - 1}$ denote the immediate past input and output sequences of length $L_{0}$, and $\mathbf{w}^{t}:={(w_{k})}_{k = {t - L_{0}}}^{{t + L'} - 1}$ denotes the immediate past and future disturbance sequence of length $L$. The output sequence ${\hat{\mathbf{y}}}^{t}:={({\hat{y}}_{k}^{t})}_{k = 0}^{L' - 1}$ provides a deterministic output prediction within the control horizon.

Indirect DDPC with deterministic predictor is known as subspace predictive control.

### Stochastic Prediction

In this work, two sources of uncertainties are considered. 1) Noise in output measurements. This induces noise in the output part of the signal matrix $Y_{p}$, $Y_{f}$, and the past output sequence $\mathbf{y}_{\text{ini}}^{t}$ with ${{\mathbb{E}}\left\lbrack \mathbf{y}_{\text{ini}}^{t} \right\rbrack} = {\overline{\mathbf{y}}}_{\text{ini}}^{t}$, ${\text{cov}\left( \mathbf{y}_{\text{ini}}^{t} \right)} = P_{t}$. 2) Uncertainties in the online disturbance sequence $\mathbf{w}^{t}$ with ${{\mathbb{E}}\left\lbrack \mathbf{w}^{t} \right\rbrack} = {\overline{\mathbf{w}}}^{t}$, ${\text{cov}\left( \mathbf{w}^{t} \right)} = \Sigma_{w}$. Statistics ${\overline{\mathbf{w}}}^{t}$ and $\Sigma_{w}$ can come from online measurements and predictions or prior knowledge.

Multiple algorithms have been developed to extend the deterministic prediction to the stochastic case. Such algorithms typically involve solving the following quadratic program: where $\lambda$ and $S$ are design parameters. Different choices of $\lambda$ and $S$ have been proposed: Subspace predictor: $S = {\mathbb{I}}_{n_{y}L_{0}}$, $\lambda\rightarrow 0^{+}$.

Wasserstein distance minimization: $S = {\mathbb{I}}_{n_{y}L_{0}}$, $\lambda = {n_{y}L_{0}\sigma^{2}}$.

Signal matrix model: $S = {\mathbb{I}}_{n_{y}L_{0}}$, Minimum mean-squared error: $S = {{\overline{\Gamma}}^{\top}\overline{\Gamma}}$, $\lambda = {{n_{y}L'\sigma^{2}} + {\text{tr}(S)\sigma^{2}}}$, where $\overline{\Gamma}$ is the last $n_{y}L_{0}$ columns of $Y_{f}\text{col}\left(\Psi,Y_{p} \right)^{\dagger}$.

See Yin et al. for a comparison between these choices. The quadratic program admits the following closed-form solution: and $F:={{\lambda{\mathbb{I}}_{M}} + {Y_{p}^{\top}SY_{p}}}$.

The stochastic predictor can be constructed based on the solution $g^{t}$ with the following lemma.

### Lemma 2

The stochastic output sequence within the control horizon is given by is the autonomous transformation matrix from $\mathbf{y}_{\text{𝑖𝑛𝑖}}^{t}$ to ${\hat{\mathbf{y}}}^{t}$.

This comes directly from the proof of Theorem 1 in Yin et al. by considering the augmented inputs $\psi_{t}$. $\square$ Unfortunately, $\Gamma$ cannot be obtained exactly since $A$ and $C$ are unknown. However, this transformation matrix can also be estimated using a data-driven approach. Note that the true output prediction is given by ${\hat{\mathbf{y}}}_{0}^{t} = {\Gamma{\overline{\mathbf{y}}}_{\text{ini}}^{t}}$ if ${\text{col}\left(\mathbf{u}_{\text{ini}}^{t},{\hat{\mathbf{u}}}^{t},\mathbf{w}^{t} \right)} = \mathbf{0}$ and $P_{t} = \mathbf{0}$. Using the certainty equivalence principle, an estimate ${\hat{\Gamma}}_{Z}$ can be found by replacing ${\hat{\mathbf{y}}}_{0}^{t}$ with ${\overline{\mathbf{y}}}^{t}$. Then we have In what follows, it is assumed that $\Gamma = {\hat{\Gamma}}_{Z}$. This estimate is correct in the noise-free case and consistent under mild conditions as shown in the following propositions.

### Proposition 3

If $v_{t} = \mathbf{0}_{n_{y}}$, we have ${\hat{\Gamma}}_{Z} = \Gamma$.

If $v_{t} = \mathbf{0}_{n_{y}}$, we have $\sigma^{2} = 0$. All designs of $\lambda$ and $S$ are equivalent to the subspace predictor, under which case $R_{4}$ is the last $n_{y}L_{0}$ columns of $\text{col}\left( \Psi,Y_{p} \right)^{\dagger}$ and thus ${Y_{p}R_{4}} = {\mathbb{I}}_{n_{y}L_{0}}$. Then Lemma 2 in Yin et al. directly leads to ${\hat{\Gamma}}_{Z} = \Gamma$. $\square$

### Proposition 4

Let the singular values of $\text{𝑐𝑜𝑙}\left( \Psi,Y_{p} \right)$ be $\sigma_{1},\ldots,\sigma_{L_{\sigma}}$ in descending order, where $L_{\sigma}:={{{({n_{u} + n_{w}})}L} + {n_{y}L_{0}}}$. Then as $M\rightarrow\infty$, ${\hat{\Gamma}}_{Z}\rightarrow\Gamma$ w.p. 1, if $\sigma_{L_{\sigma}}\rightarrow\infty$.

Let ${\text{col}\left( \Psi,Y_{p} \right)}:={\Omega SV^{\top}}$ be the singular value decomposition, where ${\Omega,S} \in {\mathbb{R}}^{L_{\sigma} \times L_{\sigma}}$ and $V \in {\mathbb{R}}^{M \times L_{\sigma}}$. Then, $g_{\text{pinv}}^{t} = {VS^{- 1}\Omega^{\top}\omega^{t}}$, where $\omega^{t}:={\text{col}\left( \mathbf{u}_{\text{ini}}^{t},\mathbf{u}^{t},{\overline{\mathbf{w}}}^{t},{\overline{\mathbf{y}}}_{\text{ini}}^{t} \right)}$, and $\left. \parallel g_{\text{pinv}}^{t}\parallel \right._{2}^{2} \leq {\left. \parallel V\parallel \right._{2}^{2}\left. \parallel S^{- 1}\parallel \right._{2}^{2}\left. \parallel\Omega\parallel \right._{2}^{2}\left. \parallel\omega^{t}\parallel \right._{2}^{2}} = \left. \left. \parallel\omega^{t}\parallel \right._{2}^{2}/\sigma_{L_{\sigma}}^{2} \right.$. Note that $g_{\text{pinv}}^{t}$ is also the least-norm solution to the linear system ${\text{col}\left( \Psi,Y_{p} \right)g} = \omega^{t}$, so we have $\left. \parallel g^{t}\parallel \right._{2}^{2} \leq \left. \parallel g_{\text{pinv}}^{t}\parallel \right._{2}^{2}$. Therefore, if $\sigma_{L_{\sigma}}\rightarrow\infty$, $\left. \parallel g^{t}\parallel \right._{2}^{2}\rightarrow 0$ and $\Sigma^{t}\rightarrow\mathbf{0}$ since $P_{t} = \mathbf{0}$. This directly leads to the convergence of ${\hat{\Gamma}}_{Z}$ to $\Gamma$. $\square$

### Remark 5

The singular value condition $\sigma_{L_{\sigma}}\rightarrow\infty$ requires that the columns of $\text{𝑐𝑜𝑙}\left( \Psi,Y_{p} \right)$ activate all directions persistently as $M\rightarrow\infty$. This is satisfied , for example, independent random or repeated full-rank inputs and disturbances.

## Stochastic Indirect Data-Driven Predictive Control

Based on the stochastic predictor, the stochastic indirect DDPC algorithm can be proposed. In the following subsections, the stochastic control cost is first formulated as a quadratic objective. Then, the prediction accuracy is improved by filtering the output initial condition estimates with a Kalman filter. Finally, the satisfaction of chance constraints is guaranteed by formulating tightened SOC constraints.

### Stochastic Control Cost

The stochastic control cost $J_{t}$ is formulated as a quadratic function in the following lemma.

### Lemma 6

The expected control cost is given by where $\overline{R}:={{\mathbb{I}}_{L'} \otimes R}$, $\overline{Q}:={{\mathbb{I}}_{L'} \otimes Q}$, $\mathbf{r}^{t}:={(r_{t + k})}_{k = 0}^{L' - 1}$ and $T:={\sigma^{2}\left({{\Gamma\Gamma^{\top}} + {\mathbb{I}}_{n_{y}L'}} \right)}$. The cost is quadratic with respect to the optimization variable ${\hat{\mathbf{u}}}^{t}$.

The expected output cost is calculated as: where $\mathbf{e}^{t}$: ${{\mathbb{E}}\left\lbrack \mathbf{e}^{t} \right\rbrack} = \mathbf{0}$, ${\text{cov}\left(\mathbf{e}^{t} \right)} = \Sigma^{t}$ is the prediction error. The second to last equality is due to the cyclic property of the trace function. This cost is quadratic with respect to ${\hat{\mathbf{u}}}^{t}$ since both $g^{t}$ and ${\overline{\mathbf{y}}}^{t}$ are linear with respect to ${\hat{\mathbf{u}}}^{t}$. $\square$ The stochastic control cost adds a $\left. \parallel g^{t}\parallel \right._{2}^{2}$-regularization term to the nominal cost. Such regularization is required in direct DDPC for well-definedness and is proposed to enhance robustness in indirect DDPC. However, it was unclear how to tune the weighting factor for the regularizer other than trial and error. By considering the regularizer as the uncertainty term in the expected output cost, the weighting factor can be reliably selected as ${tr}\left({\overline{Q}T} \right)$, which depends on the output cost matrix and the noise level.

### Initial Condition Estimation

In model-based output-feedback MPC, an estimator has to be designed to estimate the initial state of the predictor, which is not measurable. This is not required in DDPC since the output initial condition ${\overline{\mathbf{y}}}_{\text{ini}}^{t}$ can be directly measured. In fact, in most existing DDPC implementations with stochastic data, the output initial condition ${\overline{\mathbf{y}}}_{\text{ini}}^{t}$ comes from measurements as in the deterministic case, i.e., ${\overline{\mathbf{y}}}_{\text{ini}}^{t}:={(y_{k})}_{k = {t - L_{0}}}^{t - 1}$. Thus, the associated covariance $P_{t} = {\sigma^{2}{\mathbb{I}}}$ is constant . This source of uncertainty can be alleviated by choosing a larger $L_{0}$. On the other hand, in the presence of stochastic uncertainties, a properly designed estimator can estimate the initial state with a diminishing covariance that is much smaller than the noise level in the measurements.

Therefore, although not required, it can be beneficial to improve the output initial condition measurements based on output predictions at previous time steps by designing an estimator, especially in cases where the online measurement error is large. In this subsection, a Kalman filter is designed as the estimator. In particular, we replace $y_{k}$ with its Kalman-filtered counterpart for the output initial condition. This reduces the prediction errors by shrinking $P_{t}$ as time progresses.

In detail, the same predictor for predictive control design at time $({t - 1})$ is used to filter the output at time $t$ and update ${\overline{\mathbf{y}}}_{\text{ini}}^{t}$. The predictor can be considered as a non-minimal state-space "model" with "state" Let ${\overline{y}}_{i}^{t}$ and $e_{i}^{t}$ denote the $({i + 1})$-th block element of ${\overline{\mathbf{y}}}^{t}$ and $\mathbf{e}^{t}$, respectively, and $\Sigma_{i}^{t}$ be the covariance of $e_{i}^{t}$, i.e., the $({i + 1})$-th $n_{y} \times n_{y}$ block on the diagonal of $\Sigma^{t}$. The data-driven "model" is then given by where $\Lambda^{k}$ denotes the $k$-step upper shift matrix with ones on the $k$-th superdiagonal. The covariances of the "process noise" $e_{0}^{t}$ and the measurement noise $v_{t}$ are $\Sigma_{0}^{t}$ and $\sigma^{2}{\mathbb{I}}_{n_{y}}$, respectively. Then, a Kalman filter for can be designed to estimate the initial condition ${\overline{x}}_{t}$. Let the state estimate and the output part of the state error covariance be ${\overline{x}}_{t,t}$ and $P_{t,t}$, respectively. Then, the initial conditions for the DDPC problem can be set as ${\text{col}\left(\mathbf{u}_{\text{ini}}^{t},{\overline{\mathbf{y}}}_{\text{ini}}^{t} \right)}:={\overline{x}}_{t,t}$ and $P_{t}:=P_{t,t}$. The Kalman filtering algorithm is summarized in Algorithm 1. ${:={{\overline{\Lambda}{\overline{x}}_{t,t}} + {\text{col}\left(\mathbf{0},{\hat{u}}_{0}^{t},\mathbf{0},{\overline{y}}_{0}^{t} \right)}}},$ ${:={{\overline{x}}_{t,{t + 1}} + {\text{col}\left(\mathbf{0},{K_{t + 1}\left({y_{t} - {\overline{y}}_{0}^{t}} \right)} \right)}}},$ Algorithm 1 Kalman filter in stochastic indirect DDPC

### Remark 7

Only one-step ahead prediction is required to run the Kalman filter. Here, it is obtained by truncating the same $L'$-step ahead predictor used in predictive control for simplicity. One can also similarly construct a one-step ahead data-driven predictor with $L' = 1$, specifically for the Kalman filter.

### Remark 8

A similar idea was proposed in Alpago et al. for a direct DDPC algorithm. However, no approach is provided to quantify the covariance of the prediction error required in the Kalman filter as there is no well-defined predictor in direct DDPC.

### Chance Constraint Satisfaction

As mentioned in Section 2, the output constraints $y_{t} \in \mathcal{Y}_{t}$ cannot be guaranteed robustly under unbounded noise. Instead, high-probability chance constraints are considered, either element-wise as where $p$ is the targeted probability. These chance constraints are typically guaranteed by tightening the nominal constraints to account for prediction uncertainties. However, unlike standard model-based predictors with additive uncertainties, the prediction error covariance of the data-driven predictor depends on the particular inputs and initial conditions via $g^{t}$. So the amount of constraint tightening cannot be calculated offline. Define the augmented linear constraints by ${\overline{\mathcal{Y}}}_{t} = \left\{ \mathbf{y} \middle| {{{\overline{H}}^{t}\mathbf{y}} \leq {\overline{q}}^{t}} \right\}$, where The following lemma guarantees chance constraint satisfaction by constraint tightening.

### Lemma 9

guarantees the satisfaction of the chance constraints if $\mu \geq \sqrt{\frac{1}{1 - p} - 1}$ and if $\mu \geq \sqrt{\frac{n_{y}}{1 - p}}$.

Applying the one-sided Chebyshev's inequality, we have where ${\text{std}\left({{\overline{h}}_{i}^{t}{\hat{\mathbf{y}}}^{t}} \right)} = \sqrt{{\overline{h}}_{i}^{t}\Sigma^{t}{\overline{h}}_{i}^{t\top}}$. From, we have Equations and lead to for $\mu \geq \sqrt{\frac{1}{1 - p} - 1}$.

From the multi-dimensional Chebyshev's inequality, the ellipsoidal set is a confidence region of prediction error $\mathbf{e}^{t}$ with at least probability $p$. Then, the chance constraint is satisfied if where $\ominus$ denotes the Pontryagin difference. For polytope ${\overline{\mathcal{Y}}}_{t}$ and ellipsoid $\mathcal{E}_{t}$, we have where ${\eta_{\mathcal{E}_{t}}\left({\overline{h}}_{i} \right)}:=\sqrt{\frac{n_{y}}{1 - p}{\overline{h}}_{i}^{\top}\Sigma^{t}{\overline{h}}_{i}}$ is the support function of $\mathcal{E}_{t}$. Aggregating the constraints for all $i$ leads to for $\mu \geq \sqrt{\frac{n_{y}}{1 - p}}$. $\square$

### Remark 10

Let $F_{\chi_{d}^{2}}{( \cdot )}$ and $F_{\mathcal{N}}{( \cdot )}$ be the cumulative distribution function of the $\chi^{2}$-distribution with $d$ degrees of freedom and the unit Gaussian distribution, respectively. The lemma can be tightened if Gaussian uncertainties are considered, i.e., both $v_{t}$ and $\mathbf{w}^{t}$ are Gaussian, by choosing ${F_{\mathcal{N}}{(\mu)}} \geq p$ for and ${F_{\chi_{n_{y}}^{2}}{(\mu^{2})}} \geq p$ , respectively. The proof is very similar to that of Lemma 9.

Unfortunately, the tightened constraint is not convex. The following corollary provides a convex surrogate of.

### Corollary 11

The SOC constraint guarantees the satisfaction of.

Since $\sqrt{\sum_{i}a_{i}} \leq {\sum_{i}\sqrt{a_{i}}}$, we have The proposed stochastic indirect DDPC algorithm is summarized in Algorithm 2.

1:Select a data-driven predictor and calculate predictor parameters from and. 2:Initialize the Kalman filter from Algorithm 1. 4: ${\text{col}\left(\mathbf{u}_{\text{ini}}^{t},\mathbf{y}_{\text{ini}}^{t} \right)}\leftarrow{\overline{x}}_{t,t}$, Pt ← Pt, t 5: ${\hat{\mathbf{u}}}^{t}\leftarrow{{\text{arg}\underset{{\hat{\mathbf{u}}}^{t}}{\text{min}}}\quad{}\quad{\text{s.t.~}},{},{},{}}$. 6: Apply ut = û0t to the system and measure yt. 7: Run the Kalman filter from Algorithm 1. Algorithm 2 Stochastic indirect DDPC

## Numerical Example

In this section, we compare the performance of nominal DDPC (N-DDPC), DDPC with initial condition estimation in Algorithm 1 (KF-DDPC), and stochastic DDPC in Algorithm 2 (S-DDPC). Consider the following fourth-order dynamics: The following parameters are used in the example: $L_{0} = 4$, $L' = 10$, $Q = 20$, $R = 1$, $\sigma^{2} = 0.01$, $p = 0.95$. An offline trajectory of length 500 is collected with unit Gaussian inputs and the signal matrix is constructed with a Hankel structure, which leads to $M = 487$. The statistics of the disturbance are given by ${\overline{\mathbf{w}}}^{t} = \mathbf{0}$ and $\Sigma_{w} = {0.001 \cdot {\mathbb{I}}}$. The elementwise chance constraints are used. The same online noise and disturbance sequences are used to compare the three algorithms. The minimum mean-squared error predictor in Yin et al. is employed as the predictor. No input constraint is considered in this example, i.e., $\mathcal{U}_{t} = {\mathbb{R}}$. Upper and lower output bounds are specified as the output constraints.

The closed-loop trajectories of the algorithms are presented in Figure 1, alongside the reference trajectory and the output bounds. As observed in Figure 1, KF-DDPC outperforms N-DDPC by introducing the initial condition estimator, although constraint violations are still evident. S-DDPC further enhances KF-DDPC, particularly in terms of constraint satisfaction. To underscore the effectiveness of the Kalman filter, Figure 2 showcases the comparison between the filtered output initial conditions and the measured ones for S-DDPC. The filtered trajectory is notably closer to the true trajectory compared to the measured trajectory.

Figure 1: Closed-loop trajectories of DDPC algorithms.

Figure 2: Comparison of filtered and measured output trajectories.

The performance is further evaluated quantitatively by 50 Monte Carlo simulations with different noise and disturbance realizations. Figure 3 shows the boxplots of the true total control cost and the total amount of constraint violations, calculated as $\sum_{t}{\max\left( {{H^{t}y_{t}} - q^{t}},0 \right)}$. The results validate our observations from Figure 1 that our proposed algorithm S-DDPC performs much better than the nominal algorithm with almost no constraint violation.

Figure 3: Boxplots of (a) the true total control cost and (b) the total amount of constraint violations.

## Conclusion

This work discusses several modifications in stochastic data-driven predictive control (DDPC) algorithms. They provide a tuning-free regularizer design in the control cost, improved initial condition estimation, and reliable constraint satisfaction. These are achieved by evaluating the expected cost, designing a Kalman filter, and formulating convex constraint tightening terms, respectively. These modifications pave the way for providing theoretical guarantees for DDPC algorithms under general unbounded stochasticity.
