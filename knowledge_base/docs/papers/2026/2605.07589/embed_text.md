## Introduction

The increasing availability of data from dynamical systems has driven growing interest in Data-Driven Predictive Control (DDPC) methods. Historically, data has been used to identify a system model, which is then used to design a predictive control law. These approaches are called indirect DDPC methods, and despite their success across a wide range of industrial applications, they require an accurate mathematical model of the system, which can be difficult and costly to obtain in practice. Recently, direct DDPC methods have attracted significant interest, where model identification is bypassed entirely and data is used directly to predict future trajectories and compute control actions.

A large body of direct DDPC methods has been developed building on Willems' fundamental lemma, which establishes that under a persistence of excitation condition, the entire behavior of a deterministic LTI system can be parametrized via a Hankel matrix of offline data through a coefficient vector. Following this,a direct DDPC framework known as Data-Enabled Predictive Control (DeePC) was proposed in with an equivalence to Model Predictive Control (MPC) for deterministic LTI systems. However, when the system is subject to stochastic disturbances, the Hankel-based parametrization is no longer exact and predictions can deviate significantly from the true system behavior.

To address this, regularization techniques have been proposed. In, $\ell_{1}$ regularization is proposed to enforce consistency with the underlying system. Several equivalence results between direct DDPC and Subspace Predictive Control (SPC) have guided the design of regularization terms. SPC constructs a multi-step predictor by fitting a parametric model to offline trajectory data via least squares. Since the identification process reduces the effect of noise compared to using raw data, direct DDPC methods that establish an equivalence with SPC become less sensitive to noise. In, a connection with the SPC predictor is established and a corresponding regularization is introduced, and derives an analogous equivalence with the causal SPC predictor.

Another line of work provides formal guarantees for direct DDPC under explicit disturbance assumptions, including bounded noise and stochastic formulations, the latter requiring exact knowledge of the disturbance distribution. A distributionally robust formulation for nonlinear systems is proposed , which does not require this knowledge though it requires multiple offline trajectories with identical initial conditions and inputs.

In this work, we propose a distributionally robust direct DDPC formulation for LTI systems subject to stochastic disturbances with unknown probability distributions, obtained via an equivalent SPC formulation. The main contributions are as follows. (i) We propose a distributionally robust SPC formulation with a Wasserstein ambiguity set over future disturbance distributions, constructed around an empirical distribution derived from the prediction residuals of an SPC predictor estimated via least squares from an offline trajectory. The formulation minimizes the worst-case expected value of a function of the actual system output while enforcing probabilistic output constraint satisfaction for all distributions in the ambiguity set. (ii) We derive a tractable reformulation and show that it admits an equivalent direct DDPC form. (iii) Using finite-sample concentration results, we provide a data-driven choice of the ambiguity set radius that guarantees the true disturbance distribution is contained within the ambiguity set with high probability. This in turn yields a probabilistic upper bound on the expected cost and a constraint satisfaction guarantee, both holding with high probability.

### Notation

For a sequence ${\{ z_{k}\}}_{k = 1}^{T}$ with $z_{k} \in {\mathbb{R}}^{\eta}$, we write $z_{\lbrack k,j\rbrack} = \begin{bmatrix}
z_{k}^{\top} & \cdots & z_{j}^{\top}
\end{bmatrix}^{\top}$ and $z:=z_{\lbrack 1,T\rbrack}$. The Hankel matrix of depth $L$ is ${H_{L}{(z)}} = \begin{bmatrix}
z_{\lbrack 1,L\rbrack} & \cdots & z_{\lbrack{{T - L} + 1},T\rbrack}
\end{bmatrix} \in {\mathbb{R}}^{{\etaL} \times {({{T - L} + 1})}}$. We write ${( \cdot )}_{+}:={\max{\{ \cdot,0\}}}$ and $\parallel \cdot \parallel_{r}$ for the $\ell_{r}$-norm.

## Problem Formulation

We consider the stochastic discrete-time LTI system

where $x_{k} \in {\mathbb{R}}^{n}$, $u_{k} \in {\mathbb{R}}^{m}$, $y_{k} \in {\mathbb{R}}^{p}$ are states, inputs, and outputs of the system, respectively. The terms $w_{k} \in {\mathbb{R}}^{n}$ and $v_{k} \in {\mathbb{R}}^{p}$ represent process and measurement noise, drawn from unknown probability distributions ${\mathbb{P}}_{w}$ and ${\mathbb{P}}_{v}$ over support sets $W \subseteq {\mathbb{R}}^{n}$ and $V \subseteq {\mathbb{R}}^{p}$. We assume that $\{ w_{k}\}$ and $\{ v_{k}\}$ are i.i.d. sequences over time. The system matrices $A \in {\mathbb{R}}^{n \times n}$, $B \in {\mathbb{R}}^{n \times m}$, $C \in {\mathbb{R}}^{p \times n}$, $D \in {\mathbb{R}}^{p \times m}$ are unknown.

We aim to develop a receding horizon predictive controller , where at each time step $k$, given the most recent input-output measurements

of length $T_{p}$, an optimization problem is solved over the future input sequence $u_{f}:=u_{\lbrack k,{{k + T_{f}} - 1}\rbrack}$ with prediction horizon $T_{f}$ minimizing a cost function in terms of the inputs $u_{f}$ and future outputs $y_{f}:=y_{\lbrack k,{{k + T_{f}} - 1}\rbrack}$. The first element of the optimal input sequence is applied to the system, and the past window is updated at the next step. To express $y_{f}$ in terms of $u_{p}$, $y_{p}$, $u_{f}$, and the disturbances, we make the following assumption.

### Assumption 1

​​The pair $(A,C)$ is observable and $T_{p} \geq n$.

Under Assumption 1, the future output $y_{f}$ admits the multi-step predictor representation

where $m_{f} = \begin{bmatrix}
u_{p}^{\top} & y_{p}^{\top} & u_{f}^{\top}
\end{bmatrix}^{\top}$. The exact expressions for $K$ and $\xi_{f}$ are obtained by eliminating the initial state via the observability of $(A,C)$ and are omitted for brevity. The matrix $K$ is the unknown multi-step predictor, which is a function of the system matrices $(A,B,C,D)$. The term $\xi_{f} \in {\mathbb{R}}^{pT_{f}}$ is the multi-step disturbance, which is a function of the past disturbances $(w_{p},v_{p})$ and future disturbances $(w_{f},v_{f})$, where these vectors are defined analogously to. The distribution of $\xi_{f}$ is denoted by ${\mathbb{P}}_{\xi_{f}}$ and supported on $\Xi \subseteq {\mathbb{R}}^{pT_{f}}$. We also define ${\mathbb{P}}_{y_{f}|m_{f}}$ as the probability distribution of $y_{f}$ given a fixed $m_{f}$, supported on $\mathcal{Y} \subseteq {\mathbb{R}}^{pT_{f}}$.

Since the system matrices are unknown, we assume the availability of an offline input-output trajectory ${\{ u_{k}^{d},y_{k}^{d}\}}_{k = 1}^{T}$ of length $T$, collected prior to the operation of the controller. Setting $L:={T_{p} + T_{f}}$, the Hankel matrices $H_{L}{(u^{d})}$ and $H_{L}{(y^{d})}$ are partitioned into past and future blocks as

where $U_{p} \in {\mathbb{R}}^{{mT_{p}} \times N}$, $U_{f} \in {\mathbb{R}}^{{mT_{f}} \times N}$ correspond to the first and last $T_{p}$, $T_{f}$ block rows of $H_{L}{(u^{d})}$, $Y_{p}$, $Y_{f}$ are defined analogously, and $N = {{T - L} + 1}$.

### Distributionally Robust Formulation

Since $y_{f}$ is uncertain under stochastic disturbances, we consider the expected cost ${\mathbb{E}}_{{\mathbb{P}}_{y_{f}|m_{f}}}\left\lbrack {{f_{1}{(u_{f})}} + {f_{2}{(y_{f})}}} \right\rbrack$ as our objective where $f_{1}$ and $f_{2}$ are the input and output cost functions, respectively. However, since both $K$ and ${\mathbb{P}}_{y_{f}|m_{f}}$ are unknown, ${\mathbb{P}}_{y_{f}|m_{f}}$ is inaccessible and this objective cannot be minimized directly. Moreover, any finite-sample estimate of ${\mathbb{P}}_{y_{f}|m_{f}}$ constructed from offline data will inevitably carry estimation error. To robustify against this uncertainty, we adopt a distributionally robust formulation in which we construct an ambiguity set $\mathcal{P}$ of candidate distributions centered around a data-driven empirical estimate of ${\mathbb{P}}_{y_{f}|m_{f}}$, and minimize the worst-case expected cost over $\mathcal{P}$.

We consider output constraints of the form ${h{(y_{f})}} \leq 0$. Since $y_{f}$ is stochastic, this constraint cannot be enforced deterministically. Instead, we require it to hold in a probabilistic sense via the Conditional Value-at-Risk (CVaR), defined below, which serves as an upper bound on the Value-at-Risk and therefore guarantees satisfaction of the corresponding chance constraint. We require ${{CVaR}_{1 - \beta}^{Q}\left( {h{(y_{f})}} \right)} \leq 0$ to hold for all $Q \in \mathcal{P}$.

### Definition 1 (Conditional Value-at-Risk)

Let $\omega \in \Omega \subseteq {\mathbb{R}}^{r}$ be a random variable with distribution ${\mathbb{P}}_{\omega}$. For a function $\phi:{{\mathbb{R}}^{r}\rightarrow{\mathbb{R}}}$, the Conditional Value-at-Risk (CVaR) at confidence level ${1 - \beta} \in {}$ is defined as

where ${( \cdot )}_{+}:={\max{\{ \cdot,0\}}}$.

The resulting distributionally robust optimization problem is formulated as

$\min\limits_{u_{f}}$ ${f_{1}{(u_{f})}} + {\sup\limits_{Q \in \mathcal{P}}{{\mathbb{E}}_{Q}\left\lbrack {f_{2}{(y_{f})}} \right\rbrack}}$ (6a)
${{\sup\limits_{Q \in \mathcal{P}}{{CVaR}_{Q}^{1 - \beta}\left( {h{(y_{f})}} \right)}} \leq 0},$ (6c)

where $\mathcal{U} \subseteq {\mathbb{R}}^{mT_{f}}$ is the input constraint set.

### Ambiguity Set Construction

The construction of $\mathcal{P}$ proceeds in two stages. First, we use offline data to compute an empirical estimate of the distribution ${\mathbb{P}}_{y_{f}|m_{f}}$. Second, we define a neighborhood of distributions around this estimate to account for estimation errors. Define the offline regressor matrix

where $N = {{T - L} + 1}$ and $L = {T_{p} + T_{f}}$. The SPC predictor is estimated by least squares:

where $M^{\dagger}$ is the Moore-Penrose pseudoinverse of $M$. Using this estimate, we generate a set of approximate residuals ${\hat{\xi}}_{f}^{(i)}$ using offline data as

where $e_{i} \in {\mathbb{R}}^{N}$ is the $i$-th standard basis vector. For a given $m_{f}$, we form predictions of $y_{f}$ by shifting the SPC prediction $\hat{K}m_{f}$ with the approximate residual samples

The resulting empirical distribution

serves as our prediction distribution for $y_{f}$ given $m_{f}$, around which we construct the ambiguity set $\mathcal{P}$. For the finite-sample analysis in Section 3.2, we define

where ${\overline{\xi}}_{f}^{(i)} = {\left( {Y_{f} - {KM}} \right)e_{i}}$. This is unknown since $K$ is unknown, but serves as an intermediate reference in the finite-sample analysis. We construct $\mathcal{P}$ as a Wasserstein ball centered at ${\hat{\mathbb{P}}y_{f}} \mid m_{f}$, as the Wasserstein metric enables a tractable reformulation of the optimization problem.

### Definition 2

Let $r \in \lbrack 1,\infty\rbrack$ and $\mathcal{M}{(\mathcal{Y})}$ be the set of all probability measures $Q$ supported on $\mathcal{Y} \subseteq {\mathbb{R}}^{pT_{f}}$ with ${{\mathbb{E}}_{Q}{\lbrack{\| y\|}_{r}\rbrack}} < \infty$. The r-Wasserstein metric $d_{W_{r}}:{{{{\mathcal{M}{(\mathcal{Y})}} \times \mathcal{M}}{(\mathcal{Y})}}\rightarrow{\mathbb{R}}_{\geq 0}}$ is defined as

where $\Pi$ ranges over all joint measures on $\mathcal{Y} \times \mathcal{Y}$ with marginals $Q_{1}$ and $Q_{2}$.

The ambiguity set is defined as the Wasserstein ball of radius $\varepsilon > 0$ centered at ${\hat{\mathbb{P}}}_{y_{f} \mid m_{f}}$ for some $r \in \lbrack 1,\infty\rbrack$

Substituting into gives the distributionally robust SPC problem

$\min\limits_{u_{f}}$ ${f_{1}{(u_{f})}} + {\sup\limits_{Q \in {\mathcal{B}_{\varepsilon}{({\hat{\mathbb{P}}}_{y_{f} \mid m_{f}})}}}{{\mathbb{E}}_{Q}\left\lbrack {f_{2}{(y_{f})}} \right\rbrack}}$ (15a)
${{\sup\limits_{Q \in {\mathcal{B}_{\varepsilon}{({\hat{\mathbb{P}}}_{y_{f} \mid m_{f}})}}}{{CVaR}_{Q}^{1 - \beta}\left( {h{(y_{f})}} \right)}} \leq 0}.$ (15c)

## Main Results

### Tractable Reformulation

We now provide a tractable reformulation of.

### Theorem 1

Assume that $f_{2}$ and $h$ are convex and Lipschitz continuous with constants $L_{obj} > 0$ and $L_{con} > 0$ with respect to the $r$-norm, respectively. Then, the optimal value of the distributionally robust SPC problem is upper bounded by the optimal value of

$\min\limits_{u_{f},\tau,s_{i}}\mspace{21mu}{{f_{1}{(u_{f})}} + {\frac{1}{N}{\sum\limits_{i = 1}^{N}{f_{2}\left( {{\hat{K}m_{f}} + {\hat{\xi}}_{f}^{(i)}} \right)}}} + {L_{obj}\varepsilon}}$ (16a)
${{\text{s.t.}\quad u_{f}} \in \mathcal{U}},$ (16b)
${{{- {\tau\beta}} + {L_{con}\varepsilon} + {\frac{1}{N}{\sum\limits_{i = 1}^{N}s_{i}}}} \leq 0},$ (16c)
${{{\tau + {h\left( {{\hat{K}m_{f}} + {\hat{\xi}}_{f}^{(i)}} \right)}} \leq s_{i}},{{\forall i} = {1,\ldots,N}}},$ (16d)
${{s_{i} \geq 0},{{\forall i} = {1,\ldots,N}}}.$ (16e)

where $\hat{K}$ is given . Furthermore, any feasible solution $u_{f}$ to satisfies

### Proof

Proof is given in the Appendix A. ∎

We now show that the tractable SPC problem, which requires knowledge of $\hat{K}$, admits an equivalent reformulation solely in terms of the offline Hankel matrices, without explicit identification of $\hat{K}$.

### Theorem 2

$\min\limits_{g,\tau,s_{i}}\mspace{21mu}$ ${f_{1}{({U_{f}g})}} + {\frac{1}{N}{\sum\limits_{i = 1}^{N}{f_{2}\left( {{Y_{f}g} + {Y_{f}{({I - P})}e_{i}}} \right)}}} + {L_{obj}\varepsilon}$ (18a)
${{{- {\tau\beta}} + {L_{con}\varepsilon} + {\frac{1}{N}{\sum\limits_{i = 1}^{N}s_{i}}}} \leq 0},$ (18f)
${{{\tau + {h\left( {{Y_{f}g} + {Y_{f}{({I - P})}e_{i}}} \right)}} \leq s_{i}},{{\forall i} = {1,\ldots,N}}},$ (18g)
${{s_{i} \geq 0},{{\forall i} = {1,\ldots,N}}},$ (18h)

where $P:={M^{\dagger}M}$ is the orthogonal projector onto the row space of $M$.

### Proof

It was shown in that $\hat{K}m_{f}$ can equivalently be written as $Y_{f}g$ if and only if $g$ satisfies

Furthermore, using $\hat{K} = {Y_{f}M^{\dagger}}$ and $P = {M^{\dagger}M}$, the empirical residuals satisfy

Consequently, the empirical output samples become

where the second equality holds whenever $g$ satisfies the above constraints. Substituting these into and setting $u_{f} = {U_{f}g}$ yields. ∎

### Remark 1

The equivalence in Theorem 2 relies . The causal SPC predictor equivalence of can also be used, where the empirical distribution is constructed from the causal predictor residuals and an equivalent direct DDPC form is obtained through that equivalence result.

### Finite-Sample Guarantee

We now establish finite-sample probabilistic guarantees for the proposed formulation by characterizing a radius $\varepsilon{(\alpha,m_{f})}$ such that ${\mathbb{P}}_{y_{f}|m_{f}} \in {\mathcal{B}_{\varepsilon{(\alpha,m_{f})}}{({\hat{\mathbb{P}}}_{y_{f}|m_{f}})}}$ with probability at least $1 - \alpha$, which guarantees the cost bound and CVaR constraint satisfaction of Theorem 1 with the same probability. To this end, Let $\mathbb{P}$ denote the joint measure of the initial state and noise sequences governing the offline data-generating process. We rely on the following assumption bounding the mismatch between estimated predictor $\hat{K}$ and the true predictor $K$.

### Assumption 2

For a given confidence level $\alpha \in {}$, let ${\gamma{(\alpha)}} > 0$ be such that

We refer to and references therein for conditions under which this holds.

We will use the triangular inequality to find a bound on the Wasserstein distance between the true probability distribution ${\mathbb{P}}_{y_{f}|m_{f}}$ and our empirical distribution ${\hat{\mathbb{P}}}_{y_{f}|m_{f}}$ as

The following two lemmas bound each term respectively.

### Lemma 1

Under Assumptions 1 and 2, let $\alpha \in {}$ specify a risk level. Then,

### Proof

The proof follows from Lemma 5 , adapted to the $r$-Wasserstein distance instead of the $1$-Wasserstein. ∎

We rely on the following result to bound $d_{W_{r}}\left( {\overline{\mathbb{P}}}_{y_{f}|m_{f}},{\mathbb{P}}_{y_{f}|m_{f}} \right)$.

### Lemma 2

Assume that ${{\mathbb{E}}_{{\mathbb{P}}_{y_{f}|m_{f}}}\left\lbrack {\| y_{f}\|}_{r}^{q} \right\rbrack} < \infty$ for some $q > r$. Then, under Assumption 1, there exists a constant $C > 0$ such that

with $d = {pT_{f}}$. Consequently, for all $\kappa > 0$,

### Proof

Proof is given in the Appendix B. ∎

### Theorem 3

Under Assumptions 1 and 2, and the moment condition of Lemma 2, let $\alpha \in {}$ be a risk level and define the ambiguity set radius

where ${\varepsilon_{1}{(\alpha)}}:={\gamma\left( \frac{\alpha}{2} \right)}$ and ${\varepsilon_{2}{(\alpha)}}:=\left( \frac{2\gamma{(N)}}{\alpha} \right)^{1/r}$ where $\gamma{(N)}$ is defined in Lemma 2. Let $g^{\star}$ be a feasible solution of problem with radius $\varepsilon = {\varepsilon{(\alpha,m_{f})}}$, and let $\hat{J}{(g^{\star})}$ denote the objective value of at $g^{\star}$, and define the true expected cost

Then the following probabilistic guarantees hold with respect to $\mathbb{P}$:

### Proof

From Lemmas 1 and 2 and the union bound, it follows that

where $\Psi_{N} = {\frac{1}{N}{\sum_{i = 1}^{N}{\|{{Me_{i}} - m_{f}}\|}_{r}^{r}}}$. This means that with probability at least $1 - \alpha$, the true distribution ${\mathbb{P}}_{y_{f}|m_{f}}$ lies inside the Wasserstein ball $\mathcal{B}_{\varepsilon{(\alpha)}}\left( {\hat{\mathbb{P}}}_{y_{f}|m_{f}} \right)$. The result then follows from Theorem 1. ∎

### Remark 2

The radius $\varepsilon{(\alpha,m_{f})}$ in may be overly conservative in practice. We therefore assign separate tuning parameters $\varepsilon_{obj} = {{\varepsilon_{1}\Psi_{N}^{1/r}} + \varepsilon_{2}}$ and a fixed scalar $\varepsilon_{con}$ to the cost and constraint terms, respectively, and treat both as offline tuning parameters in Section 4.

## Numerical Example

We illustrate the proposed method through simulation on an example system taken , which takes the form

The distribution of the innovation term $e{(t)}$ varies across experiments and is specified for each simulation scenario. The system is subject to box constraints on both inputs and outputs ${y{(t)}} \in {\lbrack{- 2},2\rbrack}$, ${u{(t)}} \in {\lbrack{- 2},2\rbrack}$.

We compare the proposed formulation against two existing methods implemented in a receding horizon fashion. The first is SPC, in which the output is predicted using $\hat{K}m_{f}$ with $\hat{K}$ estimated as . The second is Reg-DeePC (Eq. 23 in ), which augments DeePC with an $\ell_{1}$ regularization term $\lambda_{g}{\| g\|}_{1}$, with weight selected via grid search and fixed across all experiments. We implement the proposed method in its direct DDPC form, referred to as DR-DDPC^11^1Code available at For all methods, output constraints, including the CVaR constraints , are enforced softly by augmenting the cost with a weighted sum of squared violations.

The offline data ${\{ u_{k}^{d},y_{k}^{d}\}}_{k = 1}^{T}$ is generated from a single trajectory of length $T = 200$, where the system is excited by a random control law ${u{(t)}} \sim {\mathcal{N}{(0,I_{m})}}$. The Hankel matrices are constructed with a past horizon $T_{p} = 5$ and a prediction horizon $T_{f} = 10$, yielding $N = {{T - T_{p} - T_{f}} + 1} = 186$ residual samples. Results are reported over 50 Monte Carlo simulations, regenerating offline data, disturbance realizations, and initial conditions in each iteration, with the same 50 realizations shared across all methods. For the distributionally robust formulations, we use Wasserstein ambiguity sets with an $\ell_{2}$-norm ($r = 2$) and, following Remark 2, set $\varepsilon_{1} = \varepsilon_{2} = 10^{- 3}$ for the objective term. For computational efficiency, the full set of $N$ residuals is used in the cost term, while only $20$ residuals are used in the constraint term. Both $\varepsilon_{con}$ and $\beta$ are swept in the first experiment and fixed to $\varepsilon_{con} = 10^{- 4}$ and $\beta = 0.2$ in the remaining experiments.

The control objective is to track a reference output over the prediction horizon $T_{f}$. We initially consider a standard quadratic cost

where $y_{r}$ is the stacked reference output over the prediction horizon, and $\mathbf{R} = {I_{T_{f}} \otimes R}$, $\mathbf{Q} = {I_{T_{f}} \otimes Q}$, with $R = {0.05I_{m}}$ and $Q = I_{p}$.

To evaluate closed-loop performance, we use the cumulative average cost over the total simulation duration $T_{\text{run}} = 50$

We first test the constraint satisfaction performance with respect to changing $\varepsilon_{con}$ and $\beta$ values. To obtain an informative evaluation of constraint handling, we set $y_{r,k} = 0$ and impose the output constraint $y_{k} \in {\lbrack 0,2\rbrack}$, while keeping the input constraint $u_{k} \in {\lbrack{- 2},2\rbrack}$. The innovation terms $e{(t)}$ are sampled from a zero-mean Gaussian distribution with covariance $\Sigma_{e} = {0.012\mathbf{I}_{p}}$ which corresponds to offline output data ${\{ y_{k}^{d}\}}_{k = 1}^{T}$ with Signal to Noise Ratio (SNR) of around 10dB. We consider $\varepsilon_{con}$ values in $\{ 10^{- 5},10^{- 4},10^{- 3},10^{- 2},10^{- 1},1\}$ and $\beta$ values in $\{ 0.1,0.2,0.5,0.7,0.9\}$. The corresponding average constraint violations and the cost performances of the DR-DDPC method over 50 Monte Carlo simulations are given in Figure 1. The results show that the empirical violation rate remains within the prescribed risk level $\beta$ for all scenarios. A clear trade-off is observed regarding the ambiguity radius $\varepsilon_{con}$, where larger values yield stricter constraint satisfaction but result in higher performance costs. Conversely, increasing $\beta$ allows for lower costs at the expense of more frequent violations. For comparison, the average violation rates for SPC and Reg-DeePC are $20.96\%$ and $17.80\%$ with average performance costs of $0.2615$ and $0.3276$, respectively.

(a) Mean Violation Rate (%)

(b) Mean Performance Cost

Figure 1: Parameter sweep results for εcon vs β using the DR-DDPC controller.

Next, we compare tracking performance across varying noise levels using a sinusoidal reference $y_{r,k} = {\sin\left( \frac{2\pik}{T_{\text{run}}} \right)}$. Under zero-mean Gaussian innovations (Table 1), Reg-DeePC is outperformed by the others, while SPC and DR-DDPC perform nearly identically. This is expected as, for quadratic costs, the DR-DDPC objective reduces to the cost of the mean scenario, which coincides with the nominal SPC prediction in expectation when residuals have zero mean. When the innovation mean is shifted to $0.05$ (Table 1), a performance gap emerges between SPC and DR-DDPC, with DR-DDPC outperforming SPC, as it can account for the bias in the predictor residuals.

Finally, we repeat the zero-mean Gaussian experiments while varying the tracking cost function $f_{2}{(y_{f})}$ to evaluate performance in cases where the scenario spread, rather than just the mean, influences the cost . We test an $\ell_{1}$ cost ${f_{2}{(y_{f})}} = {\|{y_{f} - y_{r}}\|}_{1}$, and an asymmetric linear cost ${f_{2}{(y_{f})}} = {{2{\|{({y_{f} - y_{r}})}_{+}\|}_{1}} + {\|{({y_{f} - y_{r}})}_{-}\|}_{1}}$ where ${( \cdot )}_{+}$ and ${( \cdot )}_{-}$ denote the positive and negative parts to penalize overshooting more heavily. In each case $J_{\text{test}}$ is modified by replacing the quadratic output term in with the respective cost. As shown in Figure 2, a performance gap between DR-DDPC and SPC emerges in both cases, confirming that the advantage of DR-DDPC grows when the cost is sensitive to the full scenario distribution rather than just its mean.

Table 1: Mean ± Std of Jtest for three covariance levels of Gaussian innovation terms: zero-mean (top) and mean μ = 0.05 (bottom).

Figure 2: Cost performance Jtest across covariance levels for different cost functions under zero-mean Gaussian innovation terms.

## Conclusion

In this work, we proposed a distributionally robust data-driven predictive control framework for stochastic LTI systems with unknown dynamics and disturbance distributions. We presented two equivalent formulations, one based on the SPC predictor and one in direct data-driven form, and established finite-sample guarantees on the expected cost and output constraint satisfaction under the true disturbance distribution. Numerical simulations validated the framework against existing methods, showing that DR-DDPC and SPC perform similarly under zero-mean Gaussian innovation terms with quadratic cost, while DR-DDPC outperforms SPC under nonzero-mean innovations and non-quadratic cost functions. Future work includes establishing stability and recursive feasibility guarantees for the closed-loop system.
