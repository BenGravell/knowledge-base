<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Distributionally Robust Data-Driven Predictive Control for Stochastic LTI Systems

Topics include Predictive control, Robustness, Probabilistic models, Offline algorithms, Control, Wasserstein distances, SPC.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a distributionally robust data-driven predictive control framework for stochastic linear time-invariant systems with unknown dynamics and disturbance distributions. We use an offline trajectory to fit the subspace predictive control (SPC) predictor via least squares and construct an empirical distribution of the prediction residuals as a proxy for the unknown disturbance distribution. We then center a Wasserstein ambiguity set around this estimate and minimize the worst-case expected cost while enforcing probabilistic output constraint satisfaction over all distributions in the set. The resulting problem admits a tractable reformulation with an equivalent direct data-driven form, eliminating the need for explicit predictor identification. Using finite-sample concentration results, we provide a data-driven Wasserstein radius such that, with high probability, the true expected cost is bounded above by the tractable objective and output constraints are satisfied with respect to the true disturbance distribution. Numerical simulations validate the framework against existing methods under various disturbance conditions and cost functions.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The increasing availability of data from dynamical systems has driven growing interest in Data-Driven Predictive Control (DDPC) methods. Historically, data has been used to identify a system model, which is then used to design a predictive control law. These approaches are called indirect DDPC methods, and despite their success across a wide range of industrial applications, they require an accurate mathematical model of the system, which can be difficult and costly to obtain in practice. Recently, direct DDPC methods have attracted significant interest, where model identification is bypassed entirely and data is used directly to predict future trajectories and compute control actions.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A large body of direct DDPC methods has been developed building on Willems' fundamental lemma, which establishes that under a persistence of excitation condition, the entire behavior of a deterministic LTI system can be parametrized via a Hankel matrix of offline data through a coefficient vector. Following this,a direct DDPC framework known as Data-Enabled Predictive Control (DeePC) was proposed in with an equivalence to Model Predictive Control (MPC) for deterministic LTI systems. However, when the system is subject to stochastic disturbances, the Hankel-based parametrization is no longer exact and predictions can deviate significantly from the true system behavior.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address this, regularization techniques have been proposed. In, $\ell_{1}$ regularization is proposed to enforce consistency with the underlying system. Several equivalence results between direct DDPC and Subspace Predictive Control (SPC) have guided the design of regularization terms. SPC constructs a multi-step predictor by fitting a parametric model to offline trajectory data via least squares. Since the identification process reduces the effect of noise compared to using raw data, direct DDPC methods that establish an equivalence with SPC become less sensitive to noise. In, a connection with the SPC predictor is established and a corresponding regularization is introduced, and derives an analogous equivalence with the causal SPC predictor.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Another line of work provides formal guarantees for direct DDPC under explicit disturbance assumptions, including bounded noise and stochastic formulations, the latter requiring exact knowledge of the disturbance distribution. A distributionally robust formulation for nonlinear systems is proposed, which does not require this knowledge though it requires multiple offline trajectories with identical initial conditions and inputs.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we propose a distributionally robust direct DDPC formulation for LTI systems subject to stochastic disturbances with unknown probability distributions, obtained via an equivalent SPC formulation. The main contributions are as follows. (i) We propose a distributionally robust SPC formulation with a Wasserstein ambiguity set over future disturbance distributions, constructed around an empirical distribution derived from the prediction residuals of an SPC predictor estimated via least squares from an offline trajectory. The formulation minimizes the worst-case expected value of a function of the actual system output while enforcing probabilistic output constraint satisfaction for all distributions in the ambiguity set. (ii) We derive a tractable reformulation and show that it admits an equivalent direct DDPC form. (iii) Using finite-sample concentration results, we provide a data-driven choice of the ambiguity set radius that guarantees the true disturbance distribution is contained within the ambiguity set with high probability. This in turn yields a probabilistic upper bound on the expected cost and a constraint satisfaction guarantee, both holding with high probability.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We aim to develop a receding horizon predictive controller, where at each time step $k$, given the most recent input-output measurements of length $T_{p}$, an optimization problem is solved over the future input sequence $u_{f}:=u_{[k,\,k+T_{f}-1]}$ with prediction horizon $T_{f}$ minimizing a cost function in terms of the inputs $u_{f}$ and future outputs $y_{f}:=y_{[k,\,k+T_{f}-1]}$. The first element of the optimal input sequence is applied to the system, and the past window is updated at the next step. To express $y_{f}$ in terms of $u_{p}$, $y_{p}$, $u_{f}$, and the disturbances, we make the following assumption.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

​​The pair $(A,C)$ is observable and $T_{p}\!\geq\!n$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Under Assumption 1, the future output $y_{f}$ admits the multi-step predictor representation where $m_{f}=\begin{bmatrix}u_{p}^{\top}&y_{p}^{\top}&u_{f}^{\top}\end{bmatrix}^{\top}$. The exact expressions for $K$ and $\xi_{f}$ are obtained by eliminating the initial state via the observability of $(A,C)$ and are omitted for brevity. The matrix $K$ is the unknown multi-step predictor, which is a function of the system matrices $(A,B,C,D)$. The term $\xi_{f}\in\mathbb{R}^{pT_{f}}$ is the multi-step disturbance, which is a function of the past disturbances $(w_{p},v_{p})$ and future disturbances $(w_{f},v_{f})$, where these vectors are defined analogously to.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Distributionally Robust Formulation", "weight": 1.0} -->

Since $y_{f}$ is uncertain under stochastic disturbances, we consider the expected cost $\mathbb{E}_{\mathbb{P}_{y_{f}|m_{f}}}\!\left[f_{1}(u_{f})+f_{2}(y_{f})\right]$ as our objective where $f_{1}$ and $f_{2}$ are the input and output cost functions, respectively. However, since both $K$ and $\mathbb{P}_{y_{f}|m_{f}}$ are unknown, $\mathbb{P}_{y_{f}|m_{f}}$ is inaccessible and this objective cannot be minimized directly. Moreover, any finite-sample estimate of $\mathbb{P}_{y_{f}|m_{f}}$ constructed from offline data will inevitably carry estimation error.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Distributionally Robust Formulation", "weight": 1.0} -->

To robustify against this uncertainty, we adopt a distributionally robust formulation in which we construct an ambiguity set $\mathcal{P}$ of candidate distributions centered around a data-driven empirical estimate of $\mathbb{P}_{y_{f}|m_{f}}$, and minimize the worst-case expected cost over $\mathcal{P}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Distributionally Robust Formulation", "weight": 1.0} -->

We consider output constraints of the form $h(y_{f})\leq 0$. Since $y_{f}$ is stochastic, this constraint cannot be enforced deterministically. Instead, we require it to hold in a probabilistic sense via the Conditional Value-at-Risk (CVaR), defined below, which serves as an upper bound on the Value-at-Risk and therefore guarantees satisfaction of the corresponding chance constraint. We require $\mathrm{CVaR}_{1-\beta}^{Q}\!\left(h(y_{f})\right)\leq 0$ to hold for all $Q\in\mathcal{P}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Ambiguity Set Construction", "weight": 1.0} -->

The construction of $\mathcal{P}$ proceeds in two stages. First, we use offline data to compute an empirical estimate of the distribution $\mathbb{P}_{y_{f}|m_{f}}$. Second, we define a neighborhood of distributions around this estimate to account for estimation errors. Define the offline regressor matrix where $N=T-L+1$ and $L=T_{p}+T_{f}$. The SPC predictor is estimated by least squares: where $M^{\dagger}$ is the Moore-Penrose pseudoinverse of $M$. Using this estimate, we generate a set of approximate residuals $\hat{\xi}_{f}^{(i)}$ using offline data as where $e_{i}\in\mathbb{R}^{N}$ is the $i$-th standard basis vector.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Ambiguity Set Construction", "weight": 1.0} -->

For a given $m_{f}$, we form predictions of $y_{f}$ by shifting the SPC prediction $\hat{K}m_{f}$ with the approximate residual samples The resulting empirical distribution serves as our prediction distribution for $y_{f}$ given $m_{f}$, around which we construct the ambiguity set $\mathcal{P}$. For the finite-sample analysis in Section 3.2, we define where $\bar{\xi}_{f}^{(i)}=\left(Y_{f}-KM\right)e_{i}$. This is unknown since $K$ is unknown, but serves as an intermediate reference in the finite-sample analysis. We construct $\mathcal{P}$ as a Wasserstein ball centered at $\hat{\mathbb{P}}{y_{f}\mid m_{f}}$, as the Wasserstein metric enables a tractable reformulation of the optimization problem.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The equivalence in Theorem 2 relies. The causal SPC predictor equivalence of can also be used, where the empirical distribution is constructed from the causal predictor residuals and an equivalent direct DDPC form is obtained through that equivalence result.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Finite-Sample Guarantee", "weight": 1.0} -->

We now establish finite-sample probabilistic guarantees for the proposed formulation by characterizing a radius $\varepsilon(\alpha,m_{f})$ such that $\mathbb{P}_{y_{f}|m_{f}}\in\mathcal{B}_{\varepsilon(\alpha,m_{f})}(\hat{\mathbb{P}}_{y_{f}|m_{f}})$ with probability at least $1-\alpha$, which guarantees the cost bound and CVaR constraint satisfaction of Theorem 1 with the same probability. To this end, Let $\mathbb{P}$ denote the joint measure of the initial state and noise sequences governing the offline data-generating process. We rely on the following assumption bounding the mismatch between estimated predictor $\hat{K}$ and the true predictor $K$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

For a given confidence level $\alpha\in$, let $\gamma(\alpha)>0$ be such that We refer to and references therein for conditions under which this holds.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

We will use the triangular inequality to find a bound on the Wasserstein distance between the true probability distribution $\mathbb{P}_{y_{f}|m_{f}}$ and our empirical distribution $\hat{\mathbb{P}}_{y_{f}|m_{f}}$ as The following two lemmas bound each term respectively.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 2", "weight": 1.0} -->

The radius $\varepsilon(\alpha,m_{f})$ in may be overly conservative in practice. We therefore assign separate tuning parameters $\varepsilon_{\mathrm{obj}}=\varepsilon_{1}\Psi_{N}^{1/r}+\varepsilon_{2}$ and a fixed scalar $\varepsilon_{\mathrm{con}}$ to the cost and constraint terms, respectively, and treat both as offline tuning parameters in Section 4.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Numerical Example", "weight": 1.0} -->

We illustrate the proposed method through simulation on an example system taken, which takes the form The distribution of the innovation term $e(t)$ varies across experiments and is specified for each simulation scenario. The system is subject to box constraints on both inputs and outputs $y(t)\in$, $u(t)\in$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Numerical Example", "weight": 1.0} -->

We compare the proposed formulation against two existing methods implemented in a receding horizon fashion. The first is SPC, in which the output is predicted using $\hat{K}m_{f}$ with $\hat{K}$ estimated as. The second is Reg-DeePC (Eq. 23 in ), which augments DeePC with an $\ell_{1}$ regularization term $\lambda_{g}\|g\|_{1}$, with weight selected via grid search and fixed across all experiments. We implement the proposed method in its direct DDPC form, referred to as DR-DDPC^11^1Code available at For all methods, output constraints, including the CVaR constraints, are enforced softly by augmenting the cost with a weighted sum of squared violations.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Numerical Example", "weight": 1.0} -->

The offline data $\{u_{k}^{d},y_{k}^{d}\}_{k=1}^{T}$ is generated from a single trajectory of length $T=200$, where the system is excited by a random control law $u(t)\sim\mathcal{N}(0,I_{m})$. The Hankel matrices are constructed with a past horizon $T_{p}=5$ and a prediction horizon $T_{f}=10$, yielding $N=T-T_{p}-T_{f}+1=186$ residual samples. Results are reported over 50 Monte Carlo simulations, regenerating offline data, disturbance realizations, and initial conditions in each iteration, with the same 50 realizations shared across all methods.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Numerical Example", "weight": 1.0} -->

For the distributionally robust formulations, we use Wasserstein ambiguity sets with an $\ell_{2}$-norm ($r=2$) and, following Remark 2, set $\varepsilon_{1}=\varepsilon_{2}=10^{-3}$ for the objective term. For computational efficiency, the full set of $N$ residuals is used in the cost term, while only $20$ residuals are used in the constraint term. Both $\varepsilon_{\mathrm{con}}$ and $\beta$ are swept in the first experiment and fixed to $\varepsilon_{\mathrm{con}}=10^{-4}$ and $\beta=0.2$ in the remaining experiments.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Numerical Example", "weight": 1.0} -->

The control objective is to track a reference output over the prediction horizon $T_{f}$. We initially consider a standard quadratic cost where $y_{r}$ is the stacked reference output over the prediction horizon, and $\mathbf{R}=I_{T_{f}}\otimes R$, $\mathbf{Q}=I_{T_{f}}\otimes Q$, with $R=0.05I_{m}$ and $Q=I_{p}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Numerical Example", "weight": 1.0} -->

To evaluate closed-loop performance, we use the cumulative average cost over the total simulation duration $T_{\text{run}}=50$ We first test the constraint satisfaction performance with respect to changing $\varepsilon_{\mathrm{con}}$ and $\beta$ values. To obtain an informative evaluation of constraint handling, we set $y_{r,k}=0$ and impose the output constraint $y_{k}\in$, while keeping the input constraint $u_{k}\in$. The innovation terms $e(t)$ are sampled from a zero-mean Gaussian distribution with covariance $\Sigma_{e}=0.012\mathbf{I}_{p}$ which corresponds to offline output data $\{y_{k}^{d}\}_{k=1}^{T}$ with Signal to Noise Ratio (SNR) of around 10dB.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Numerical Example", "weight": 1.0} -->

We consider $\varepsilon_{\mathrm{con}}$ values in $\{10^{-5},10^{-4},10^{-3},10^{-2},10^{-1},1\}$ and $\beta$ values in $\{0.1,0.2,0.5,0.7,0.9\}$. The corresponding average constraint violations and the cost performances of the DR-DDPC method over 50 Monte Carlo simulations are given in Figure 1. The results show that the empirical violation rate remains within the prescribed risk level $\beta$ for all scenarios. A clear trade-off is observed regarding the ambiguity radius $\varepsilon_{\mathrm{con}}$, where larger values yield stricter constraint satisfaction but result in higher performance costs. Conversely, increasing $\beta$ allows for lower costs at the expense of more frequent violations.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Numerical Example", "weight": 1.0} -->

For comparison, the average violation rates for SPC and Reg-DeePC are $20.96\%$ and $17.80\%$ with average performance costs of $0.2615$ and $0.3276$, respectively.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Numerical Example", "weight": 1.0} -->

(a) Mean Violation Rate (%) (b) Mean Performance Cost Figure 1: Parameter sweep results for εcon vs β using the DR-DDPC controller.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Numerical Example", "weight": 1.0} -->

Next, we compare tracking performance across varying noise levels using a sinusoidal reference $y_{r,k}=\sin\!\left(\frac{2\pi k}{T_{\text{run}}}\right)$. Under zero-mean Gaussian innovations (Table 1), Reg-DeePC is outperformed by the others, while SPC and DR-DDPC perform nearly identically. This is expected as, for quadratic costs, the DR-DDPC objective reduces to the cost of the mean scenario, which coincides with the nominal SPC prediction in expectation when residuals have zero mean. When the innovation mean is shifted to $0.05$ (Table 1), a performance gap emerges between SPC and DR-DDPC, with DR-DDPC outperforming SPC, as it can account for the bias in the predictor residuals.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Numerical Example", "weight": 1.0} -->

Finally, we repeat the zero-mean Gaussian experiments while varying the tracking cost function $f_{2}(y_{f})$ to evaluate performance in cases where the scenario spread, rather than just the mean, influences the cost. We test an $\ell_{1}$ cost $f_{2}(y_{f})=\|y_{f}-y_{r}\|_{1}$, and an asymmetric linear cost $f_{2}(y_{f})=2\|(y_{f}-y_{r})_{+}\|_{1}+\|(y_{f}-y_{r})_{-}\|_{1}$ where $(\cdot)_{+}$ and $(\cdot)_{-}$ denote the positive and negative parts to penalize overshooting more heavily. In each case $J_{\text{test}}$ is modified by replacing the quadratic output term in with the respective cost.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Numerical Example", "weight": 1.0} -->

As shown in Figure 2, a performance gap between DR-DDPC and SPC emerges in both cases, confirming that the advantage of DR-DDPC grows when the cost is sensitive to the full scenario distribution rather than just its mean.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we proposed a distributionally robust data-driven predictive control framework for stochastic LTI systems with unknown dynamics and disturbance distributions. We presented two equivalent formulations, one based on the SPC predictor and one in direct data-driven form, and established finite-sample guarantees on the expected cost and output constraint satisfaction under the true disturbance distribution. Numerical simulations validated the framework against existing methods, showing that DR-DDPC and SPC perform similarly under zero-mean Gaussian innovation terms with quadratic cost, while DR-DDPC outperforms SPC under nonzero-mean innovations and non-quadratic cost functions. Future work includes establishing stability and recursive feasibility guarantees for the closed-loop system.
