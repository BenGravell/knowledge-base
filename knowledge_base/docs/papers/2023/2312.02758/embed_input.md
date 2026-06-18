<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Stochastic Data-Driven Predictive Control: Regularization, Estimation, and Constraint Tightening

Topics include Predictive control, Control, Stochastic data-driven predictive control.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Data-driven predictive control methods based on the Willems' fundamental lemma have shown great success in recent years. These approaches use receding horizon predictive control with nonparametric data-driven predictors instead of model-based predictors. This study addresses three problems of applying such algorithms under unbounded stochastic uncertainties: 1) tuning-free regularizer design, 2) initial condition estimation, and 3) reliable constraint satisfaction, by using stochastic prediction error quantification. The regularizer is designed by leveraging the expected output cost. An initial condition estimator is proposed by filtering the measurements with the one-step-ahead stochastic data-driven prediction. A novel constraint-tightening method, using second-order cone constraints, is presented to ensure high-probability chance constraint satisfaction. Numerical results demonstrate that the proposed methods lead to satisfactory control performance in terms of both control cost and constraint satisfaction, with significantly improved initial condition estimation.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Classical model-based control enables simple but powerful control design by considering typically parametric mathematical abstractions of system behaviors, known as models. However, this comes at the cost of additional modeling and identification effort, which constitutes the majority of the budget in model-based control design, in terms of both time and cost. In this regard, the concept of data-driven control provides an appealing alternative that designs the controller directly from data without parametric identification.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we focus on data-driven predictive control (DDPC), the data-driven counterpart to model predictive control (MPC). Similar to MPC, it solves a finite-horizon optimal control problem in a receding horizon fashion, but with nonparametric data-driven predictors instead of model-based predictors. Data-driven predictors for linear systems can be constructed by using the so-called Willems' fundamental lemma, which characterizes all possible system behaviors with finite data.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

While these predictors work well with deterministic data, showing equivalence to model-based design, they become ill-defined with stochastic data. Multiple works have stressed this issue by introducing an inner problem that finds the 'optimal' predictor under some statistical principle, e.g., Fiedler and Lucia; Yin et al.; Breschi et al.. This idea is known as indirect DDPC.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

These stochastic data-driven predictors can be applied to DDPC design similar to the noise-free case. However, they suffer from the following problems with this certainty-equivalent implementation: 1) the control cost does not account for the prediction error, 2) the initial condition measurements suffer from noise which cannot be improved by collecting more data, and 3) the constraint satisfaction is not guaranteed. Aspects of these problems have been analyzed under the robust control framework where a bounded uncertainty set is prescribed. On the other hand, the situation is less clear under the stochastic control framework, where existing works adopt restrictive assumptions, such as noise-free offline data and exact polynomial chaos expansions of stochastic measurements. This paper addresses these problems under general unbounded stochastic uncertainties, utilizing the prediction error quantification provided in Yin et al..

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In particular, three modifications are made to the certainty-equivalent DDPC algorithm. 1) The nominal control cost is replaced by the expected control cost. This introduces an additional uncertainty term that resembles the regularizer used empirically for DDPC problems, but here the weight is specified statistically without tuning. 2) The output initial condition is estimated by Kalman-filtering the output measurements with one-step-ahead predictions from the previous timestep. This significantly reduces the prediction error. 3) Output constraints are formulated as chance constraints and guaranteed by second-order cone (SOC) constraints. The effectiveness of these modifications is tested in a numerical example, where satisfactory control performance in terms of both control cost and constraint satisfaction is observed with significantly improved initial condition estimation.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Consider the observable part of a stable discrete-time linear time-invariant (LTI) dynamical system with disturbance and output noise, given by

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The model parameters $(A,B,C,D,E)$ are unknown, but a matrix of input-disturbance-output trajectory data $Z = \begin{bmatrix}
\end{bmatrix}$ has been collected, where each column

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

is a length-$L$ trajectory of the system, where the superscript $d$ denotes collected offline data. The availability of offline disturbance trajectories retroactively is commonly assumed in DDPC algorithms, e.g., Pan et al., and is practical in many applications. The noise in each column of outputs is assumed to be independent. This assumption holds exactly when the columns are separate trajectories or truncated from a longer trajectory with $t_{i + 1} = {t_{i} + L}$, known as the Page construction. Another common construction of $Z$ is by choosing $t_{i + 1} = {t_{i} + 1}$, forming a block Hankel matrix. The matrix $Z$ is dubbed the signal matrix.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We are interested in designing a receding horizon control algorithm with a predictor derived from the signal matrix $Z$ instead of the model parameters. Such algorithms are known as indirect DDPC. Let $L = {L_{0} + L^{\prime}}$, and $L_{0}$ be no smaller than the observability index of the system. In this paper, we consider the stochastic optimal tracking problem within a horizon of $L^{\prime}$ that minimizes the following expected control cost

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

at time $t$, where ${\hat{u}}_{k}^{t}$ is the designed input at time $({t + k})$, ${\hat{y}}_{k}^{t}$ is a random variable that predicts the noise-free future output $y_{t + k}^{0}$, $r_{t}$ denotes the reference trajectory, and $Q,R$ are the output and the input cost matrices respectively.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Then, the first element in the optimal input sequence is applied to the system, i.e., $u_{t}:={\hat{u}}_{0}^{t}$ and the noisy output $y_{t} = {y_{t}^{0} + v_{t}}$ is measured.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

There are multiple aspects to consider when solving this problem, which will be discussed in the following sections.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

There are uncertainties in both the prediction conditions and the signal matrix. An accurate predictor is desired under these uncertainties.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The expected control cost needs to be formulated as a tractable objective function.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Tractable formulations of the output constraints need to be derived.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Deterministic Prediction", "weight": 1.0} -->

With sufficiently persistently exciting inputs, the range space of $Z$ contains all possible trajectories of the system in the noise-free case, i.e., $v_{t} = \mathbf{0}_{n_{y}}$. The following result derived from the Willems' fundamental lemma provides a deterministic prediction by considering the augmented inputs $\psi_{t}:={\text{col}\left( u_{t},w_{t} \right)}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Stochastic Prediction", "weight": 1.0} -->

Multiple algorithms have been developed to extend the deterministic prediction to the stochastic case.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Stochastic Prediction", "weight": 1.0} -->

where $\lambda$ and $S$ are design parameters.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Stochastic Prediction", "weight": 1.0} -->

See Yin et al. for a comparison between these choices.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Stochastic Prediction", "weight": 1.0} -->

The stochastic predictor can be constructed based on the solution $g^{t}$ with the following lemma.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 5", "weight": 1.0} -->

The singular value condition $\sigma_{L_{\sigma}}\rightarrow\infty$ requires that the columns of $\text{𝑐𝑜𝑙}\left( \Psi,Y_{p} \right)$ activate all directions persistently as $M\rightarrow\infty$. This is satisfied, for example, independent random or repeated full-rank inputs and disturbances.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Stochastic Indirect Data-Driven Predictive Control", "weight": 1.0} -->

Based on the stochastic predictor, the stochastic indirect DDPC algorithm can be proposed. In the following subsections, the stochastic control cost is first formulated as a quadratic objective. Then, the prediction accuracy is improved by filtering the output initial condition estimates with a Kalman filter. Finally, the satisfaction of chance constraints is guaranteed by formulating tightened SOC constraints.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Stochastic Control Cost", "weight": 1.0} -->

The stochastic control cost $J_{t}$ is formulated as a quadratic function in the following lemma.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Initial Condition Estimation", "weight": 1.0} -->

In model-based output-feedback MPC, an estimator has to be designed to estimate the initial state of the predictor, which is not measurable. This is not required in DDPC since the output initial condition ${\overline{\mathbf{y}}}_{\text{ini}}^{t}$ can be directly measured. In fact, in most existing DDPC implementations with stochastic data, the output initial condition ${\overline{\mathbf{y}}}_{\text{ini}}^{t}$ comes from measurements as in the deterministic case, i.e., ${\overline{\mathbf{y}}}_{\text{ini}}^{t}:={(y_{k})}_{k = {t - L_{0}}}^{t - 1}$. Thus, the associated covariance $P_{t} = {\sigma^{2}{\mathbb{I}}}$ is constant.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Initial Condition Estimation", "weight": 1.0} -->

This source of uncertainty can be alleviated by choosing a larger $L_{0}$. On the other hand, in the presence of stochastic uncertainties, a properly designed estimator can estimate the initial state with a diminishing covariance that is much smaller than the noise level in the measurements.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Initial Condition Estimation", "weight": 1.0} -->

Therefore, although not required, it can be beneficial to improve the output initial condition measurements based on output predictions at previous time steps by designing an estimator, especially in cases where the online measurement error is large. In this subsection, a Kalman filter is designed as the estimator. In particular, we replace $y_{k}$ with its Kalman-filtered counterpart for the output initial condition. This reduces the prediction errors by shrinking $P_{t}$ as time progresses.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Initial Condition Estimation", "weight": 1.0} -->

In detail, the same predictor for predictive control design at time $({t - 1})$ is used to filter the output at time $t$ and update ${\overline{\mathbf{y}}}_{\text{ini}}^{t}$. The predictor can be considered as a non-minimal state-space "model" with "state"

<!-- chunk {"id": "body-0030", "role": "body", "section": "Initial Condition Estimation", "weight": 1.0} -->

where $\Lambda^{k}$ denotes the $k$-step upper shift matrix with ones on the $k$-th superdiagonal. The covariances of the "process noise" $e_{0}^{t}$ and the measurement noise $v_{t}$ are $\Sigma_{0}^{t}$ and $\sigma^{2}{\mathbb{I}}_{n_{y}}$, respectively. Then, a Kalman filter for can be designed to estimate the initial condition ${\overline{x}}_{t}$. Let the state estimate and the output part of the state error covariance be ${\overline{x}}_{t,t}$ and $P_{t,t}$, respectively.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Initial Condition Estimation", "weight": 1.0} -->

Algorithm 1 Kalman filter in stochastic indirect DDPC

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 7", "weight": 1.0} -->

Only one-step ahead prediction is required to run the Kalman filter. Here, it is obtained by truncating the same $L^{\prime}$-step ahead predictor used in predictive control for simplicity. One can also similarly construct a one-step ahead data-driven predictor with $L^{\prime} = 1$, specifically for the Kalman filter.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 8", "weight": 1.0} -->

A similar idea was proposed in Alpago et al. for a direct DDPC algorithm. However, no approach is provided to quantify the covariance of the prediction error required in the Kalman filter as there is no well-defined predictor in direct DDPC.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Chance Constraint Satisfaction", "weight": 1.0} -->

As mentioned in Section 2, the output constraints $y_{t} \in \mathcal{Y}_{t}$ cannot be guaranteed robustly under unbounded noise. Instead, high-probability chance constraints are considered, either element-wise as

<!-- chunk {"id": "body-0035", "role": "body", "section": "Chance Constraint Satisfaction", "weight": 1.0} -->

where $p$ is the targeted probability. These chance constraints are typically guaranteed by tightening the nominal constraints to account for prediction uncertainties. However, unlike standard model-based predictors with additive uncertainties, the prediction error covariance of the data-driven predictor depends on the particular inputs and initial conditions via $g^{t}$. So the amount of constraint tightening cannot be calculated offline. Define the augmented linear constraints by ${\overline{\mathcal{Y}}}_{t} = \left\{ \mathbf{y} \middle| {{{\overline{H}}^{t}\mathbf{y}} \leq {\overline{q}}^{t}} \right\}$, where

<!-- chunk {"id": "body-0036", "role": "body", "section": "Chance Constraint Satisfaction", "weight": 1.0} -->

The following lemma guarantees chance constraint satisfaction by constraint tightening.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 10", "weight": 1.0} -->

Let $F_{\chi_{d}^{2}}{( \cdot )}$ and $F_{\mathcal{N}}{( \cdot )}$ be the cumulative distribution function of the $\chi^{2}$-distribution with $d$ degrees of freedom and the unit Gaussian distribution, respectively. The lemma can be tightened if Gaussian uncertainties are considered, i.e., both $v_{t}$ and $\mathbf{w}^{t}$ are Gaussian, by choosing ${F_{\mathcal{N}}{(\mu)}} \geq p$ for and ${F_{\chi_{n_{y}}^{2}}{(\mu^{2})}} \geq p$, respectively. The proof is very similar to that of Lemma 9.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Remark 10", "weight": 1.0} -->

Unfortunately, the tightened constraint is not convex. The following corollary provides a convex surrogate of.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Numerical Example", "weight": 1.0} -->

In this section, we compare the performance of nominal DDPC (N-DDPC), DDPC with initial condition estimation in Algorithm 1 (KF-DDPC), and stochastic DDPC in Algorithm 2 (S-DDPC).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Numerical Example", "weight": 1.0} -->

The following parameters are used in the example: $L_{0} = 4$, $L^{\prime} = 10$, $Q = 20$, $R = 1$, $\sigma^{2} = 0.01$, $p = 0.95$. An offline trajectory of length 500 is collected with unit Gaussian inputs and the signal matrix is constructed with a Hankel structure, which leads to $M = 487$. The statistics of the disturbance are given by ${\overline{\mathbf{w}}}^{t} = \mathbf{0}$ and $\Sigma_{w} = {0.001 \cdot {\mathbb{I}}}$. The elementwise chance constraints are used. The same online noise and disturbance sequences are used to compare the three algorithms. The minimum mean-squared error predictor in Yin et al. is employed as the predictor. No input constraint is considered in this example, i.e., $\mathcal{U}_{t} = {\mathbb{R}}$. Upper and lower output bounds are specified as the output constraints.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Numerical Example", "weight": 1.0} -->

The closed-loop trajectories of the algorithms are presented in Figure 1, alongside the reference trajectory and the output bounds. As observed in Figure 1, KF-DDPC outperforms N-DDPC by introducing the initial condition estimator, although constraint violations are still evident. S-DDPC further enhances KF-DDPC, particularly in terms of constraint satisfaction. To underscore the effectiveness of the Kalman filter, Figure 2 showcases the comparison between the filtered output initial conditions and the measured ones for S-DDPC. The filtered trajectory is notably closer to the true trajectory compared to the measured trajectory.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Numerical Example", "weight": 1.0} -->

The performance is further evaluated quantitatively by 50 Monte Carlo simulations with different noise and disturbance realizations. Figure 3 shows the boxplots of the true total control cost and the total amount of constraint violations, calculated as $\sum_{t}{\max\left( {{H^{t}y_{t}} - q^{t}},0 \right)}$. The results validate our observations from Figure 1 that our proposed algorithm S-DDPC performs much better than the nominal algorithm with almost no constraint violation.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This work discusses several modifications in stochastic data-driven predictive control (DDPC) algorithms. They provide a tuning-free regularizer design in the control cost, improved initial condition estimation, and reliable constraint satisfaction. These are achieved by evaluating the expected cost, designing a Kalman filter, and formulating convex constraint tightening terms, respectively. These modifications pave the way for providing theoretical guarantees for DDPC algorithms under general unbounded stochasticity.
