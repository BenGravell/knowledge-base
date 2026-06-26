## Introduction

A typical approach to time series forecasting is to fit a one-step ahead prediction model and apply it recursively to obtain predictions over multiple time steps. In doing so, small errors may compound over time, leading to poor long-horizon prediction. This issue can make the application of such single-step models to long-term planning and controller design challenging.

By directly training multi-step models to predict over longer horizons, the issue of compounding error can be mitigated. The main drawback of doing so is that the number of parameters for a direct multi-step predictor scales with the prediction horizon, thus potentially requiring more data than a single-step predictor to achieve a desired prediction performance. While this tradeoff between prediction horizon accuracy and data requirements is broadly known to exist, it is primarily studied from an empirical perspective. We therefore lack principled guidance for exactly when direct multi-step prediction should be preferred over autoregressive rollout of single-step models. Motivated by this challenge, we provide a rigorous comparison of the sample efficiency of learning multi-step predictors with that of learning single-step predictors in the setting of a linear dynamical system.

### A Related Work

### Multi-step Identification

The goal of system identification is to use data to learn a model that can be used for forecasting or control. To this end, one typically wants to select a model from the hypothesis class that minimizes the simulation error, i.e., the cumulative prediction error over all future time steps. Due to the computational challenge of doing so, it is much more common to instead learn a model which minimizes the single-step prediction error and apply it autoregressively. However, such approaches tend to generalize poorly if the underlying data generating process does not belong to the hypothesis class. This has motivated the application of algorithms such as Data as Demonstrator (DaD) which use approaches from imitation learning to train a predictor to self-correct its prediction error at each step, leading to improved empirical performance.

Direct learning of prediction models for each time-step in the prediction horizon partially bypasses the issue of compounding error, and has proven successful for both model predictive control and value approximation in MDPs. Empirical studies of single-step and multi-step dynamics models learned with various neural network architectures have also been conducted. Namely, investigates the performance of recursive application of single-step models parameterized by neural networks in a handful of examples and characterize circumstances which such models may worsen the effects of compounding error. In, the authors give a comparison of various deep learning architectures for predicting multiple steps of a time series and show the efficacy of bidirectional and encoder-decoder LSTM networks.

These empirical studies underscore the importance of careful consideration when designing a model for multi-step prediction. Our work studies this question in stylized settings, allowing us to clearly demonstrate the potential drawbacks and benefits of direct multi-step prediction as compared to more traditional single-step approaches.

### Learning-Enabled Control

While the issue of compounding error has long been studied in system identification and control, it has resurfaced as a prominent issue in the learning community, exacerbated by the use of neural networks as function approximators. In model-based reinforcement learning, it has been observed that synthesized controllers may exploit compounding errors of the learned model, motivating numerous heuristics for accounting for the model error during policy synthesis. In, the authors instead propose learning a direct multi-step predictor parametrized by a low dimensional decision variable which may be optimized online.

The issue of a mismatch between the hypothesis class and the underlying data generating process also poses a challenge for behavior cloning. For example, incorrectly assuming that the demonstrator is Markovian can lead to a policy that deviates substantially from the demonstrator. This can be remedied in part by replacing the standard behavior cloning objective with an objective that predicts the expert actions for multiple timesteps to maintain temporal consistency, resulting in so-called *action-chunking* based approaches. We draw inspiration from these studies, and consider instances of linear systems with either Markovian or non-Markovian observations to compare direct multi-step prediction and autoregressive evaluation of single-step predictors.

### B Contributions

Our prior work provided a quantitative comparison of the multi-step prediction error incurred by a directly learned multi-step predictor and autoregressive evaluation of a single-step predictor. Here, we extend this work: (i) considering a third class of predictors, specifically a single-step predictor trained by minimizing a multi-step loss, (ii) analyzing the resulting closed-loop control performance, and (iii) providing complete proofs. In particular: We provide an asymptotic characterization of the multi-step prediction error for the three methods in the setting of a fully observed dynamical system. Our results show that for stable systems with a small spectral radius, the prediction error of autoregressive evaluation for a single-step predictor decays significantly faster with increasing data than that of the other methods.

We characterize the prediction error for the three methods applied to a partially observed dynamical system that is incorrectly assumed to be fully observed by the hypothesis class, thus addressing the issue of trajectory prediction under misspecification due to an unjustified Markovian assumption. These results demonstrate that multi-step predictors may enjoy significantly lower bias in the face of model misspecification.

We analyze predictor performance in a closed loop control setting. Our results show that, in the case of a fully observed dynamical system (well-specified setting), autoregressive evaluation of a single-step predictor fitted with a single step loss often yields lower control cost than autoregressive evaluation of a single step predictor fitted with a multistep loss.

We conduct numerical experiments that exemplify the above results. Code to reproduce these experiments is available. ^11^1Code to reproduce experiments: Our results, while limited to stylized settings, capture key properties of real systems---such as partial observability and misspecification---and thus provide useful guidance to practitioners navigating the complex design space of data-driven multi-step predictors.\Notation: $\mathcal{N}(\mu,\sigma^{2})$ denotes a normal distribution with mean $\mu$ and variance $\sigma^{2}$, $\overset{p}{\to}$ denotes convergence in probability, $\rho(\cdot)$ denotes the spectral radius of a matrix, $\left\|\cdot\right\|$ denotes the vector Euclidean norm, $\left\|\cdot\right\|_{F}$ denotes the matrix Frobenius norm, $\left\|\cdot\right\|_{\star}$ denotes the matrix nuclear norm, $\operatorname{\mathsf{vec}}(\cdot)$ denotes the vectorization of a matrix, and $\otimes$ denotes the Kronecker product. For a random sequence $X_{n}$, we use $X_{n}={\cal O}_{p}\mathopen{}\left(a_{n}\right)\mathclose{}$ to denote that the set of values $X_{n}/a_{n}$ is stochastically bounded. We use the notation $X_{a:b}$ to denote the sequence $X_{n}$ for $n=a$ to $n=b$. For functions $f,g$ of $x$, we use the notation $f(x)=o(g(x))$ to denote that $\lim_{x\rightarrow\infty}\frac{f(x)}{g(x)}=0$.

## Problem Formulation

Consider the linear time invariant dynamical system | | $\displaystyle x_{t+1}$ | $\displaystyle=Ax_{t}+Bu_{t}+B_{w}w_{t}$ | | $\displaystyle\quad t\in\mathbb{Z}^{+}$ | | \(1\) | | | $\displaystyle y_{t}$ | $\displaystyle=Cx_{t}+D_{v}v_{t},$ | | $\displaystyle\quad t\in\mathbb{Z}^{+}$ | | | with state $x_{t}\in\mathbb{R}^{d_{\mathsf{x}}}$, input $u_{t}\in\mathbb{R}^{d_{\mathsf{u}}}$, observation $y_{t}\in R^{d_{\mathsf{y}}}$, process noise $w_{t}\overset{iid}{\sim}\mathcal{N}(0,I_{d_{x}})$, sensor noise $v_{t}\overset{iid}{\sim}\mathcal{N}(0,I_{d_{y}})$, and initial condition $x_{0}=0$. We assume that $(A,C)$ is observable, that $(A,\begin{bmatrix}B,B_{w}\end{bmatrix})$ is controllable, $\rho(A)<1$^22^2The assumption $\rho(A)<1$ guarantees stationarity and ergodicity of the process $\{x_{t}\}$., and that the control inputs are selected randomly as $u_{t}\overset{iid}{\sim}\mathcal{N}(0,I_{d_{u}})$.

We assume that the dynamics are unknown, and our goal is to learn a predictor that forecasts a horizon $H$ of future observations using past observations. To this end, we suppose that we are given a dataset $\mathcal{D}_{N}=\mathopen{}\left\{(y_{t},u_{t})\right\}\mathclose{}_{t=1}^{N}$ collected from a training rollout of which will be used to determine a function $\hat{f}_{H}$ belonging to a hypothesis class $\mathcal{F}_{H}$. This function will be used to predict $y_{t+1:t+H}$ given $y_{1:t}$ and $u_{1:t+H-1}$.

The quality of the learned function will be measured by the loss where the operator $\bar{\operatorname{\textbf{E}}}$ is defined as and the expectation is taken over an evaluation rollout of system that is independent of the dataset $\mathcal{D}_{N}$. By ergodicity of the process, this is equivalent to taking an expectation under the steady state distribution for the system.

To provide rigorous understanding of situations where multi-step prediction does or does not help, we consider a simplified setting in which the hypothesis class consists of static linear predictors, i.e., a function $f_{H}\in\mathcal{F}_{H}$ given by for a matrix $G\in S\subseteq\mathbb{R}^{Hd_{\mathsf{y}}\times(d_{\mathsf{y}}+Hd_{\mathsf{u}})}$. Here the subspace $S$ encodes whether we are fitting a multi-step or single-step model: we provide explicit parameterizations for these model-classes in the next subsections. Our restriction to static linear predictors of the form assumes that the observation sequence is Markovian, i.e., that a history of observations is unnecessary to predict the future trajectory. In the sequel, we slightly abuse notation and denote the loss incurred by a predictor defined by matrix $\hat{G}$ by $L(\hat{G}).$ We consider two settings: one where the Markovian assumption is justified ($C=I$ and $D_{v}=0$), resulting in a well-specified problem, and one where it is not justified ($C\neq I$ or $D_{v}D_{v}^{\top}\succ 0$), resulting in a misspecified problem. In these two settings, we compare the $H$ step prediction error incurred by a learned single-step model rolled out for $H$ timesteps to that incurred by a directly learned $H$-step model.

Throughout, we use "misspecification" specifically to refer to violations of the Markov assumption induced by partial observability (and observation noise), while "well-specified" refers to the fully observed state setting.

### I-A Single-step Predictors

The single-step approach first solves Using this model, one can predict $y_{t+1:t+H}$ by rolling out $\begin{bmatrix}\hat{G}_{y}&\hat{G}_{u}\end{bmatrix}$ autoregressively: The resulting $H$-step predictor can be composed to form a direct mapping from the data to the predicted trajectory as As past predictions become part of the regressor for future predictions, this approach often suffers from compounding error.

### I-B Multi-step Predictors

The issue of compounding error from autoregressive roll-out of a single-step model motivates direct multi-step approaches which directly minimize the $H$ step prediction error: for $S\subseteq\mathbb{R}^{Hd_{\mathsf{y}}\times(d_{\mathsf{y}}+Hd_{\mathsf{u}})}$. We consider the function class which fits $H$ distinct predictors, one for each step in the prediction horizon. This amounts to setting $S=\mathbb{R}^{Hd_{\mathsf{y}}\times(d_{\mathsf{y}}+Hd_{\mathsf{u}})}$.^33^3One could impose the causality structure, i.e. that $S$ has a triangular structure. We refrain from doing so for simplicity, and due to the fact that future inputs are independent of the past.

There is a tradeoff induced by fitting multi-step predictors rather than single-step predictors. In particular, the single-step predictor is subject to compounding error, while the complexity of the above identification problem increases for longer horizons.

### I-C Intermediate Formulations

Rather than fitting independent predictors for every timestep, one can instead formulate a hypothesis class for multi-step prediction with lower complexity. In particular, one could impose additional structure on $S$. For example, let This consists of functions which take the form of a single-step predictor that is applied auto-regressively. In contrast to the single-step approach of Section I-A, solving with this choice of $S$ consists of a multi-step loss function for a class of single-step predictors, a common approach to mitigate the compounding error issue without increasing the number of parameters that must be learned.

We compare single-step, multi-step, and the intermediate predictors described above in the two aforementioned settings: a system with Markovian observations, and a system with non-Markovian observations. Due to the Markovian assumption for the identification problem, these cases serve as instances where the identification problem is well-specified and misspecified, respectively.

## Well-Specified Setting

In this section, we study the well-specified setting in which the Markovian assumption is valid. In particular, we restrict system to be a fully observed system by assuming that $C=I$ and $D_{v}=0$ so $y_{t}=x_{t}$ for all $t$.

To compare the three approaches in this setting, we first observe that the predictors $\hat{f}_{H}$ are defined in terms of a linear map $\hat{G}$ applied to the vector $\begin{bmatrix}x_{t}^{\top}&u_{t:t+H-1}^{\top}\end{bmatrix}^{\top}$. Therefore the loss may be written Rolling out the dynamics, we find that Then expanding $x_{t+1:t+H}$ in equation, and using the independence of $w_{t:t+H-1}$ from $x_{t}$ and $u_{t:t+H-1}$, we conclude that where $\Sigma_{z}=\bar{\operatorname{\textbf{E}}}z_{t}z_{t}^{\top}$ is the stationary covariance for the regressor $z_{t}\triangleq\begin{bmatrix}x_{t}\\u_{t:t+H-1}\end{bmatrix}$. ^44^4By the fact that $w_{t},u_{t}$ are i.i.d. standard normal and $(A,\begin{bmatrix}B,B_{w}\end{bmatrix})$ is controllable, persistence of excitation holds, i.e. $\Sigma_{z}$ is positive definite. Consequently, the discrepancy between the single-step and multi-step predictors is contained in the term $\left\|(\hat{G}-G^{\star})\Sigma_{z}^{1/2}\right\|_{F}^{2}$. We study the behavior of this term asymptotically, where $\hat{G}$, or equivalently $\hat{G}_{N}$, is an operator learned on the dataset of size $N$.^55^5We sometimes omit the subscript $N$ on $\hat{G}_{N}$ to ease notational burden. In particular, we examine for the predictors $\hat{G}^{SS}_{N}$, $\hat{G}^{MS}_{N}$, and $\hat{G}^{I}_{N}$, where the expectation is taken over the dataset used to fit $\hat{G}_{N}$.

The reducible error of the multi-step predictor is characterized by the following proposition.

### Proposition II.1 (Proposition III.1 of )

The reducible asymptotic error of the multi-step predictor $\hat{G}^{MS}_{N}$ is given by where $M_{MS}\in\mathbb{R}^{H\times H}$ is the matrix with entry $(i,j)$ given by $M_{MS}^{ij}=\operatorname{\mathrm{tr}}(A^{{\left|i-j\right|}})$.

### Proof

By the normal equations for the least-squares estimator, From a combination of Slutsky's theorem, Birkhoff-Khinchin theorem, and Vitali's convergence theorem, Expanding the Frobenius norm results in a double sum over time indices. The evaluation of each term, accounting for temporal dependence, is given in Lemma A.1. Summing over all indices and combining terms yields the characterization stated in the proposition. ∎ The above result shows that the error decays asymptotically at a rate of $1/N$. The scaling is characterized by the trace expression, which represents the asymptotic covariance of the estimation error; importantly, it grows with the horizon $H$ (note the $(M_{MS}+Hd_{u}I_{H})$ term). We will contrast this with the error of the single-step predictor, characterized below.

### Proposition II.2 (Proposition III.2 of )

The asymptotic error of the single-step predictor $\hat{G}^{SS}_{N}$ is given by where $M_{SS}\in\mathbb{R}^{H\times H}$ is the matrix with entry $(i,j)$ given by

### Proof

Manipulating, we can write $\hat{G}_{N}^{SS}-G^{\star}$ as a sum of terms which are linear in $\begin{bmatrix}\hat{G}_{y}\!-\!A\!&\!\!\hat{G}_{u}\!-\!B\end{bmatrix}$ and higher order terms. That is, where $F$ and $\Gamma$ are functions of $A,B,H$ defined in Appendix A-B. Noting that higher order terms vanish in the limit, where $L=\sum_{i=1}^{H}e_{i}\otimes I_{d_{\mathsf{x}}+d_{\mathsf{u}}}\otimes e_{i}\otimes I_{d_{\mathsf{x}}}$ and $e_{i}$ is the $i$th column of $I_{H}$. From Lemma A.2, where $\Sigma_{x,u}$ is the stationary covariance of $\begin{bmatrix}x_{t}^{\top}&u_{t}^{\top}\end{bmatrix}^{\top}$. Expanding the norm and plugging, (II) becomes Simplifying this expression gives the result stated in the proposition. ∎ Again, the error decays at a rate $1/N$. In contrast to the multi-step predictor, the asymptotic scaling of the single-step prediction error has the quantity $M_{SS}+d_{\mathsf{u}}I_{H}$ inside the trace. This means that the multi-step predictor suffers an extra factor of $H$ in the input term. Additionally the matrix $M_{MS}$ for the multi-step case has entries which decay as the distance to the diagonal increases, while $M_{SS}$ has entries which decay as the distance to the upper left element increases. Roughly, this indicates that for very stable systems $M_{SS}$ should become smaller than $M_{MS}$.

Next, we characterize the reducible error of the intermediate predictor. We introduce several quantities in order to cleanly express this characterization. Define the per-timestep loss Let $\theta:=\operatorname{\mathsf{vec}}\!\left(\begin{bmatrix}G_{y}&G_{u}\end{bmatrix}\right).$ Define $J=\bar{\operatorname{\textbf{E}}}\!\left[\nabla_{\theta}^{2}\,m_{t}(A,B)\right],$ and Let $\begin{bmatrix}\hat{G}_{y}^{I}&\hat{G}_{u}^{I}\end{bmatrix}$ be the first block row of the intermediate predictor $\hat{G}_{N}^{I}$. Lemma A.3 shows that the quantities $J$ and $\Sigma$ describe its asymptotic variance. In particular, The matrices $J$ and $\Sigma$ admit closed form expressions in terms of $A,B,B_{w},$ and $H$. Implementations of these closed form expressions as required for the numerical validation in Section II-B can be found in the accompanying codebase. We use these quantities in the following proposition.

### Proposition II.3

The asymptotic error of the single-step predictor fitted with a multi-step loss $\hat{G}^{I}_{N}$ is given by where $L$, $F$, and $\Gamma$ are functions of $A,B,H$ as defined in Appendix A-B.

### Proof

From the structure, we can write $\hat{G}_{N}^{I}-G^{\star}$ as a sum of terms which are linear in $\begin{bmatrix}\hat{G}_{y}^{I}\!-\!A\!&\!\!\hat{G}_{u}^{I}\!-\!B\end{bmatrix}$ and higher order terms which vanish in the limit. That is, Expanding the norm and plugging in gives the result. ∎ Once again, the error decays asymptotically at a rate of $1/N$. This closed form expression does not admit an easy comparison with the single and multi-step decay rates. However, we are still able to show the comparison of the asymptotic variance of the three types of predictor.

### II-A Comparison of Predictor Error

Figure 1: Convergence of N𝐄 [L(f̂H)] to the reducible prediction errors given in Proposition II.1 (multi-step predictor), Proposition II.2 (single-step rollout), and Proposition II.3 (intermediate predictor) for the system defined by Equation 16 with a = 0.5, 0.75, 0.9 (left to right) and horizon H = 5.

The next proposition compares the asymptotic decay rates given in Propositions II.1. ‣ II Well-Specified Setting ‣ Statistical Efficiency of Single- and Multi-step Models for Forecasting and Control"), II.2. ‣ II Well-Specified Setting ‣ Statistical Efficiency of Single- and Multi-step Models for Forecasting and Control") and II.3.

### Proposition II.4

The asymptotic decay rates for the single step, intermediate, and multistep predictors obey the ordering

### Proof

Consider the first inequality. Recall from the proofs of Proposition II.2. ‣ II Well-Specified Setting ‣ Statistical Efficiency of Single- and Multi-step Models for Forecasting and Control") and Proposition II.3 that Notice that $\Sigma_{x,u}^{-1}\otimes B_{w}B_{w}^{\top}$ is the inverse of the Fisher Information in the data $\mathcal{D}_{N}$ about the parameter $\operatorname{\mathsf{vec}}(\begin{bmatrix}A&B\end{bmatrix})$. From the Cramér Rao inequality, $\Sigma_{x,u}^{-1}\otimes B_{w}B_{w}^{\top}\preceq J^{-1}\Sigma J^{-1}$. Thus, the first inequality of the proposition holds.

Consider the second inequality. Let $\beta^{\star}=\operatorname{\mathsf{vec}}(G^{\star})$. Let $\hat{\beta}^{MS}=\operatorname{\mathsf{vec}}(\hat{G}_{N}^{MS})$ be the parameters of the unconstrained multi-step predictor and $\hat{\beta}^{I}=\operatorname{\mathsf{vec}}(\hat{G}_{N}^{I})$ be the parameters of the intermediate predictor. Let $V_{\hat{\beta}^{MS}}$ be the asymptotic variance $\lim_{N\rightarrow\infty}N\operatorname{var}(\hat{\beta}^{MS}-\beta^{\star})$ and similarly $V_{\hat{\beta}^{I}}\triangleq\lim_{N\rightarrow\infty}N\operatorname{var}(\hat{\beta}^{I}-\beta^{\star})$. Let $Q\triangleq\Sigma_{z}\otimes I_{Hd_{\mathsf{x}}}$. Then, From results on constrained least squares regression (see Lemma A.4 and), we have that for some $R\in\mathbb{R}^{Hd_{\mathsf{y}}(d_{\mathsf{y}}+Hd_{\mathsf{u}})\times(H-1)d_{\mathsf{y}}(d_{\mathsf{y}}+Hd_{\mathsf{u}})}$ with full row rank. Since $\operatorname{\mathrm{tr}}(V_{\hat{\beta}^{MS}}^{\frac{1}{2}}R(R^{\top}Q^{-1}R)^{-1}R^{\top}V_{\hat{\beta}^{MS}}^{\frac{1}{2}})\geq 0$, the result holds. ∎ While Propositions II.1. ‣ II Well-Specified Setting ‣ Statistical Efficiency of Single- and Multi-step Models for Forecasting and Control"), II.2. ‣ II Well-Specified Setting ‣ Statistical Efficiency of Single- and Multi-step Models for Forecasting and Control"), and II.3 explicitly characterize the asymptotic decay rates of the reducible errors induced by the three predictor classes, Proposition II.4 provides a direct comparison of these rates. In particular, it shows that for any system of the form with full-state observations, the single-step predictor is statistically more efficient than the intermediate predictor (single-step model trained with a multi-step loss), which in turn is more efficient than the direct multi-step predictor.

This ordering reflects the extent to which each estimator exploits structural properties of the underlying dynamics. The single-step predictor benefits from (i) leveraging the Markovian structure of the true system and (ii) avoiding compounding process noise across multiple prediction steps in the training loss. The intermediate predictor also exploits the Markovian structure but incurs additional variance due to multi-step noise accumulation in the loss. The direct multi-step predictor benefits from neither advantage, and thus its prediction error exhibits the slowest asymptotic decay rate.

In the case of the single-step and direct multi-step predictors, we can characterize and analyze the efficiency gap. Specifically, we can express the quadratic form defining the reducible portion of the error in Proposition II.1. ‣ II Well-Specified Setting ‣ Statistical Efficiency of Single- and Multi-step Models for Forecasting and Control") as the reducible error in Proposition II.2. ‣ II Well-Specified Setting ‣ Statistical Efficiency of Single- and Multi-step Models for Forecasting and Control") plus the additional term $\operatorname{\mathrm{tr}}(\Gamma_{w}((M_{MS}-M_{SS}+(H-1)d_{u}I_{H})\otimes I_{d_{X}})\Gamma_{w}^{T})$. Note that $(M_{MS}-M_{SS})$ is the matrix with entry $(i,j)$ given by $\operatorname{\mathrm{tr}}(\Sigma_{x}^{-1}\sum_{\ell=0}^{\min\mathopen{}\left\{i,j\right\}\mathclose{}-2}A^{\ell}B_{w}B_{w}^{\top}(A^{\ell})^{\top}(A^{{\left|j-i\right|}})^{\top})$. We see that the efficiency gap grows with the prediction horizon $H$. This scaling quantitatively captures that the direct multi-step predictor has a number of parameters which scales with $H$.

To better understand the role of system stability in determining this efficiency gap, we consider the special case of a scalar system without inputs. Here the difference between the statistical efficiency of the single-step predictor and the multi-step predictor is characterized by the difference between the matrices from which we conclude that the difference between the two diminishes as ${\left|a\right|}\to 1$. Since the statistical efficency of the intermediate predictor lies in between that of the single step and multistep predictors by Proposition II.4, we can conclude that the difference between all three predictor classes diminishes as the system approaches marginal stability.

The above statement about the decay in the efficiency gap as the system approaches marginal stability holds for scalar systems, but the picture is more nuanced in general. In particular, if any eigenvalue remains less than 1, we maintain an efficiency gap even as $\rho(A)\rightarrow 1$, as seen in Figure 1.

### II-B Numerical Experiments

To validate the error characterizations presented in section II, we consider the fully observed system defined by with $B=\begin{bmatrix}0&1\end{bmatrix}^{\top},C=I_{2},\Sigma_{v}=0$.

In Figure 1, we estimate $N\operatorname{\textbf{E}}[L(\hat{f}_{H})]$ by averaging over $2,500$ datasets $D_{N}$ for $N\in\{1,...,3000\}$ to demonstrate convergence to the reducible errors given in Propositions II.1. ‣ II Well-Specified Setting ‣ Statistical Efficiency of Single- and Multi-step Models for Forecasting and Control"), II.2. ‣ II Well-Specified Setting ‣ Statistical Efficiency of Single- and Multi-step Models for Forecasting and Control") and II.3. In these figures, we fix $H=5$ and vary $a$ across $0.5,0.75$, and $0.9$. For the single-step model with a multi-step loss, $\hat{G}$ is fit using Adam initialized from the single-step predictor fit with a single-step loss, and using a step size $1e-2$.

For each data generating process (choice of parameter $a$) and each predictor, we see that the decay rate of the excess prediction error converges to its predicted value as $N$ increases. Comparing the decay rates across predictor classes, these results exemplify the efficiency gap suggested by Proposition II.4. That is, for each choice of the parameter $a$, the excess prediction error of the single-step predictor has the fastest decay rate, followed by the single-step predictor with a multi-step loss, then the direct multi-step predictor. Comparing the figures left to right, we see that, unlike for the scalar system discussed in Section II-A, the efficiency gap does not diminish with $a$.

## Misspecified Setting

We again consider a single-step predictor and a multi-step predictor applied to the measurement. However, we now examine the general case in which measurements do not provide full state information by reincorporating partial observations, as specified by $C\in\mathbb{R}^{d_{\mathsf{y}}\times d_{\mathsf{x}}}$ and $D_{v}D_{v}^{\top}\succ 0$, into the dynamics. Due to the Markovian assumption made in fitting the predictor, this represents a misspecified setting. To ease notational burden we restrict attention to the setting without inputs and set $B=0$, although our analysis can be extended naturally to the $B\neq 0$ case.

In this setting, the loss is given by We rewrite the dynamics in innovations form as where $e_{t}$ is standard normal noise that is independent across time, $K$ is the Kalman gain defined as $K=ASC^{\top}(CSC^{\top}+R)^{-1}$, $S$ is the stabilizing solution to the Riccati equation defined by $A$, $C$, $D_{w}D_{w}^{\top}$ and $D_{v}D_{v}^{\top}$, and $D_{e}=(CSC^{\top}+D_{v}D_{v}^{\top})^{1/2}$. Then Under these definitions, and exploiting that innovations are independent across time, the error is given by where $\Sigma_{\hat{x}}$ is the stationary covariance of $\hat{x}_{t}$. Let $\Sigma_{y}$ be the stationary covariance of $y_{t}$.^66^6It follows from $D_{v}D_{v}^{\top}\succ 0$ that $\Sigma_{y}$ is positive definite. When $\hat{G}$, or equivalently $\hat{G}_{N}$, is learned on the dataset of size $N$, we can decompose this quantity into an irreducible component, and a component which decays to zero as the amount of data $N\to\infty$. Denoting the irreducible component by $B(\hat{G}_{N})\triangleq\lim_{N\to\infty}\operatorname{\textbf{E}}L(\hat{G}_{N})$ and the reducible component by $\varepsilon(\hat{G}_{N})\triangleq L(\hat{G}_{N})-B(\hat{G}_{N})$, we decompose Unlike the well-specified setting, the irreducible component $B(\hat{G}_{N})$ differs depending on whether we fit a single-step model, direct multi-step model, or single-step model fitted with a multi-step loss. We therefore focus on comparing these bias terms rather than the rate of convergence, since this captures the fundamental difference between the two models.

Figure 2: Convergence of 𝐄 [L(f̂H)] to the irreducible prediction errors given in Proposition III.1 (multi-step predictor), Proposition III.2 (single-step rollout), and Proposition III.3 (intermediate predictor) for the system defined by Equation 23 with a = 0.5, 0.75, 0.9 (left to right) and horizon H = 5.

The irreducible error for the multi-step predictor is characterized in the following proposition.

### Proposition III.1 (Proposition IV.1 of )

The irreducible error for the multi-step predictor $\hat{G}_{N}^{MS}$ is given by where $\Sigma_{\hat{x}}$ is the stationary covariance of $\hat{x}_{t}$.

### Proof

The least squares identification error is Expanding $y_{t}=C\hat{x}_{t}+D_{e}e_{t}$, this becomes By Slutsky's theorem and the Birkhoff Khinchin Theorem, Plugging this in to $L(\hat{G}_{N}^{MS})$, applying Vitali Convergence, and noting that terms which scale with $\tilde{E}_{MS}$ vanish in the limit, it follows that The above proposition quantifies exactly how the loss of information from partial system observations (through $C\neq I$ or $D_{v}\neq 0$) affects the asymptotic bias induced by the multi-step predictor. It shows that this bias scales with the prediction horizon $H$ as $A^{H}$, suggesting worse prediction performance for systems with larger spectral radius $\rho(A)$.

We can compare this with the irreducible error associated with the single-step predictor, which is characterized as follows.

### Proposition III.2 (Proposition IV.2 of )

The irreducible error for the single-step predictor $\hat{G}_{N}^{SS}$ is given by and $\Sigma_{x}$ is the stationary covariance of $x_{t}$.

### Proof

Since we consider the setting without inputs, we can write where, from the normal equations for the least squares estimator, Expanding $y_{t+1}$ and $y_{t}$, this becomes By Slutsky's theorem and the Birkhoff Khinchin theorem, Plugging this in to $L(\hat{G}_{N}^{SS})$, applying Vitali Convergence, and noting that terms which scale with $\tilde{E}_{SS}$ vanish in the limit, it follows that The above proposition quantifies how the loss of information from partial system observations affects the asymptotic bias induced by the single-step predictor. It shows that this bias scales with the prediction horizon $H$ as $(CA\Sigma_{\hat{x}}C^{\top}\Sigma_{y}^{-1})^{H}$. As in the case of the direct multi-step predictor, this suggests worse prediction performance for systems with larger spectral radius $\rho(A)$. However, unlike the case of the multi-step predictor, this scaling depends on $C,\Sigma_{y},$ and $\Sigma_{\hat{x}}$, meaning that the quality of system observations affects how the bias scales with the horizon. See Example III.1 for a numerical example where this dependence leads to prohibitive compounding error.

In the case of the intermediate predictor, the irreducible error can be written as a solution of a constrained optimization problem.

### Proposition III.3

Let $\hat{G}_{N}^{I}$ be the single-step predictor with a multistep loss defined as in with the additional constraint that $\lVert G_{N}^{I}\rVert_{F}<R$ for some $R\in\mathbb{R}$ for all $N$. The irreducible error solves the optimization problem where $S$ is defined as in and we assume $R$ is chosen large enough that $\operatorname*{argmin}_{G\in S}L(G)\subset\{G\mid\lVert G\rVert_{F}<R\}$.

Note that there is no closed form solution to the optimization problem. Also note that $R$ may be chosen arbitrarily large, so the restriction to the ball $\{G\mid\lVert G\rVert_{F}<R\}$ is practically inconsequential.

### Proof

For $G^{*}\in\operatorname*{argmin}_{G\in S}L(G),$ The final result holds by uniform integrability of $L(\hat{G}_{N}^{I})$ and Vitali's Convergence Theorem. ∎ Though it is impossible to give a closed form solution to the optimization problem in the above problem, this characterization of the bias is useful in the next section where we compare the biases induced by the three classes of predictors.

### III-A Comparison

The next proposition compares the asymptotic biases given in Proposition III.1. ‣ III Misspecified Setting ‣ Statistical Efficiency of Single- and Multi-step Models for Forecasting and Control"), Proposition III.2. ‣ III Misspecified Setting ‣ Statistical Efficiency of Single- and Multi-step Models for Forecasting and Control"), and Proposition III.3.

### Proposition III.4

This ordering follows from the observation that the irreducible errors of the multi-step, intermediate, and single-step predictors can be written as solutions of nested optimization problems. Specifically, the bias from the multi-step predictor given in Proposition III.1. ‣ III Misspecified Setting ‣ Statistical Efficiency of Single- and Multi-step Models for Forecasting and Control") is given by The bias from the intermediate predictor given in Proposition III.3 solves the same problem but with $G$ constrained to the set $S$ defined. The bias from the single step predictor in Proposition III.2. ‣ III Misspecified Setting ‣ Statistical Efficiency of Single- and Multi-step Models for Forecasting and Control") corresponds to an evaluation of the same loss at a fixed point $\tilde{G}\in S$. That is, $B(\hat{G}_{N}^{SS})=L(\tilde{G})$. Since, $\mathbb{R}^{Hd_{\mathsf{y}}\times d_{\mathsf{y}}}\supseteq S\supseteq\{\tilde{G}\}$, the ordering holds.

In the case of the single-step predictor and direct multi-step predictor, we can quantify how the bias scales with the horizon $H$. As discussed earlier, the single step predictor scales with the horizon as $(CA\Sigma_{\hat{x}}C^{\top}\Sigma_{y}^{-1})^{H}$ and the direct multi-step predictor as $A^{H}$. Thus, the scaling is dictated by the spectral radii of these quantities. Lemma B.1 shows that the quantity $CA\Sigma_{\hat{x}}C^{\top}\Sigma_{y}^{-1}$ which the estimate $\hat{G}_{y}$ converges to satisfies $\rho(CA\Sigma_{\hat{x}}C^{\top}\Sigma_{y}^{-1})\leq 1$ if $\rho(A)<1$. Despite this, $CA\Sigma_{\hat{x}}C^{\top}\Sigma_{y}^{-1}$ can feature a spectral radius much larger than that of $A$, as demonstrated in the following example.

### Example III.1

Figure 3: Comparison of the bias from the single and multi-step estimators across different horizons for the system defined in Example III.1.

Consider the system defined by We find that $\rho(CA\Sigma_{\hat{x}}C^{\top}\Sigma_{y}^{-1})=0.99$, though $\rho(A)=0.9$.

As a consequence of this fact, the gap in bias between the multi-step error and the single-step error can grow with the horizon for moderate $H$. This is illustrated for the above example in Figure 3.

### III-B Numerical Experiments

To validate the error characterizations presented in section III, we consider the partially observed system defined by In Figure 2, we estimate $\operatorname{\textbf{E}}[L(\hat{f}_{H})]$ by averaging over $2,500$ datasets $D_{N}$ for $N\in\{1,...,3000\}$ to demonstrate convergence to the irreducible errors given in Proposition III.1. ‣ III Misspecified Setting ‣ Statistical Efficiency of Single- and Multi-step Models for Forecasting and Control") and Proposition III.2. ‣ III Misspecified Setting ‣ Statistical Efficiency of Single- and Multi-step Models for Forecasting and Control"). In these figures, we fix $H=5$ and vary $a$ across $0.5,0.75$, and $0.9$. For the single-step model with a multi-step loss, $\hat{G}$ is fit using Adam initialized from the single-step predictor fit with a single-step loss, and using a step size $1e-2$.

For each data generating process (choice of parameter $a$) and each predictor, we see that the prediction error converges to its predicted value as $N$ increases. Comparing prediction error across predictor classes, these results exemplify the bias gap suggested in Proposition III.4. That is, for each choice of the parameter $a$, the multi-step predictor has the lowest asymptotic prediction error, followed by the single-step predictor with a multi-step loss, then the single-step predictor.

## Control Performance

We evaluate the predictor classes in a closed-loop control setting in which the control inputs are selected using predictions from a model trained on a dataset of size $N$. In particular, the control input is selected via model predictive control with a planning horizon equal to the predictor's forecast horizon $H$. Given an $H$-step predictor $\hat{G}$, we compute an $H$-step feedback gain $K_{H}(\hat{G})$ such that minimizes the finite horizon quadratic cost At execution time, controls are applied one step at a time according to $u_{t}=K(\hat{G})y_{t}$ where $K(\hat{G})$ is the first $d_{u}$-block row of $K_{H}(\hat{G})$. The infinite-horizon LQR cost incurred by the resulting closed-loop system gives a measure of performance of the predictors. However, on the event that $K(\hat{G})$ is not stabilizing, $J(K(\hat{G}))$ will be infinite-valued. To account for this, we fix a large upper bound $M\gg 0$ and evaluate performance of predictors according instead to the clipped loss

### IV-A Well-Specified Setting

In the well-specified setting, we can compare the decay rates of the clipped infinite horizon LQR costs of controllers learned from a single-step predictor with a single step loss and a single step predictor with a multistep loss.

### Proposition IV.1

Assume $H$ is sufficiently large so that $\rho\mathopen{}\left(A+BK(G^{\star})\right)\mathclose{}<1$. There exist constants $c\in\mathbb{R}$ and $\rho\in$ such that

### Proof

Fix $\epsilon>0$ so that $\rho\mathopen{}\left(A+BK(G^{\star})\right)\mathclose{}\leq 1-\epsilon$. There exists $r>0$ such that if $\left\|K(G)-K(G^{\star})\right\|<r$, then $\rho\mathopen{}\left(A+BK\right)\mathclose{}\leq 1-\frac{\epsilon}{2}$. Define the event Then, for any predictor $\hat{G}_{N}$, From Theorem 5.3 of, $\operatorname{\mathbb{P}}\mathopen{}\left(\mathcal{E}(\hat{G}_{N}^{SS})^{C}\right)\mathclose{}\sim o\mathopen{}\left(\frac{1}{N}\right)\mathclose{}$, so for the single step predictor, the complement term vanishes asymptotically. Thus, it suffices to compare the first term for $\hat{G}_{N}=\hat{G}_{N}^{SS},\hat{G}_{N}^{I}$, and $\hat{G}_{N}^{MS}$. On $\mathcal{E}(\hat{G}_{N})$, $\tilde{J}\!\left(K(\hat{G}_{N})\right)$ is smooth, so from Lemma C.1, the expectation above can be written as plus a term which scales as $\rho^{H}$ for $\rho\in$, where $\Sigma_{\hat{G}_{N}}$ is the asymptotic variance and $K^{\star}=\operatorname*{argmin}_{K}J(K)$. By the Cramér Rao Lower Bound, we have that the asymptotic variance of the single step predictor $\hat{G}_{N}^{SS}$ is smaller than that of the intermediate predictor in the p.s.d cone. Since the final result holds. ∎ The above proposition states that the infinite horizon LQR cost associated with a single-step predictor decays faster than that of the intermediate predictor up to a term which decays exponentially in the horizon $H$. Comparison with the multi-step predictor is left for future work.

Figure 4: Infinite-horizon LQR performance in the well-specified case.

In Figure 4, we consider the closed-loop control setting above for system with $a=0.9$ and $H=20$ averaged over $2,500$ datasets $D_{N}$ for $N\in\{1,...,3000\}$. As suggested by Proposition IV.1, the single-step predictor exhibits a faster decay rate than the intermediate predictor. However, though the intermediate predictor achieves a faster prediction error decay rate than the multi-step predictor, as shown in proposition II.4, it exhibits a slower LQR cost decay rate than the multi-step in closed loop.

### IV-B Misspecified Setting

In the previous section, we analyzed the infinite-horizon control cost induced by controllers designed using multi-step predictions obtained from (a) a single-step predictor, (b) a single-step predictor trained with a multi-step loss, and (c) a direct multi-step predictor. Under model misspecification, however, irreducible prediction bias may prevent any static state-feedback controller derived from these predictors from stabilizing the true system. In such cases, the infinite-horizon control cost is infinite, even in the limit as the dataset size $N\to\infty$. Consequently, rather than comparing asymptotic control costs, we instead compare predictors through their ability to induce stabilizing controllers. In particular, we identify regimes in which the lower-bias multi-step predictor yields a stabilizing controller, whereas the alternative predictors may fail to do so. We provide numerical examples illustrating this phenomenon and leave theoretical characterization of these regimes to future work.

(a) Closed loop spectral radius for system with a = 0.6.

(b) Closed loop spectral radius for system with a = 0.75.

Figure 5: Infinite-horizon LQR performance in the misspecified case. Closed loop spectral radius greater than 1 implies infinite LQR cost.

Figure 5 shows the spectral radius of the resulting closed-loop system in the misspecified setting for the system with $H=20$ averaged over 2,500 datasets. A spectral radius greater than 1 for the single-step rollout indicates closed-loop system instability, in which case the associated infinite-horizon LQR cost diverges. Panel (a) corresponds to $a=0.6$, where both the single step and intermediate predictors yield stabilizing controllers but, for small $N$, the single step predictor does not. Panel (b) corresponds to $a=0.75$, where stabilization is achieved only by the multi-step predictor. These results suggest that controllers induced by direct multi-step predictors are more likely to stabilize the true system than those obtained from single-step rollouts. We provide two explanations for this.

First, let $K^{\star}$ denote the feedback gain computed from the ground truth multi-step predictor $G^{\star}$. For sufficiently large planning horizon $H$, the associated closed-loop system is stable, i.e. $\rho(A+BK^{\star})<1$. By continuity of the spectral radius, it follows that if a feedback gain $K$ has $\left\|K-K^{\star}\right\|$ sufficiently small, then $K$ yields a stabilizing closed-loop matrix. Since $K(\hat{G})$ is a continuous function of $\hat{G}$, it then follows that for $\left\|\hat{G}-G^{\star}\right\|$ sufficiently small, $\rho\mathopen{}\left(A+BK(\hat{G})\right)\mathclose{}<1$. In Proposition III.4, we showed that, in the presence of misspecification, direct multi-step predictors achieve lower asymptotic prediction error than the other predictor types. Thus, they are more likely to lie within this stabilization neighborhood.

Second, for stable systems, multi-step prediction errors are dominated by errors in the direction of the modes with the largest magnitude. Since these directions are those which govern stabilization, training predictors with a multi-step loss implicitly emphasizes accurate modeling in the directions which are most relevant for stabilization. Thus, multi-step predictors are better suited for inducing stabilizing controllers.

## Nonlinear Systems

In Sections II and III, we provided a rigorous comparison of the prediction error incurred by single- and multi-step predictors. Though these results are restricted to linear systems, we provide empirical evidence that similar phenomena arise for nonlinear dynamics. Consider the system with state $x_{t}=\begin{bmatrix}p_{t}\ q_{t}\end{bmatrix}$, initialized at $x_{0}=\begin{bmatrix}0\ 0\end{bmatrix}$, and evolving as | | $\displaystyle q_{t+1}$ | $\displaystyle=\lambda(q_{t}-p_{t}^{2})+w_{t}^{(q)},$ | | | where $w_{t}^{(p)},w_{t}^{(q)}\overset{iid}{\sim}\mathcal{N}(0,\sigma_{w})$.

This system admits a finite-dimensional Koopman lifting (e.g.) with observables $\tilde{x}_{t}=\begin{bmatrix}p_{t}\ q_{t}\ p_{t}^{2}\ 1\end{bmatrix}$, for which the dynamics are linear in $\tilde{x}_{t}$ up to noise terms: and, given a dataset $\mathcal{D}_{N}=\{y_{t}\}_{t=1}^{N}$, compute the single-step predictor $\hat{G}_{N}^{SS}$, multi-step predictor $\hat{G}_{N}^{MS}$, and intermediate predictor $\hat{G}_{N}^{I}$ as described in Sections I-A, I-B and I-C.

We evaluate these predictors in both a well-specified setting ($C=I$, $\sigma_{v}=0$) and a misspecified setting ($C\neq I$, $\sigma_{v}>0$), analogous to Sections II and III.

Figure 6: Prediction error versus horizon H for the system.

In Figure 6, we estimate expected mean-squared prediction error by averaging over $200$ datasets with $N=300$. We fix $\mu=\lambda=0.9$, $\sigma_{w}=0.1$, and vary $H\in$. In the misspecified case, we use $C=\begin{bmatrix}0&1&0&0\end{bmatrix}$ and $\sigma_{v}=0.4$. The intermediate predictor $\hat{G}_{N}^{I}$ is trained using Adam (step size $10^{-2}$), initialized from $\hat{G}_{N}^{SS}$.

The results mirror our linear theory. In the well-specified setting, Figure 6(a) shows that the single-step predictor achieves the lowest error, followed by the single-step predictor trained with a multi-step loss, and then the direct multi-step predictor, consistent with Proposition II.4. In contrast, Figure 6(b) shows the reverse ordering, consistent with Proposition III.4.

These experiments suggest that the qualitative behavior predicted by our linear analysis may extend to some nonlinear systems. A rigorous treatment of this setting is left for future work.

## Conclusion

In this work, we present a novel theoretical comparison of the asymptotic prediction error associated with autoregressive rollouts of single-step predictors, direct multi-step predictors, and single-step predictors fitted with multi-step losses. Our analysis offers insight into when each modeling approach is preferable. Specifically, we show that for well-specified model classes, autoregressive rollouts of single-step predictors achieve lower asymptotic prediction error. However, in the presence of model misspecification due to an incorrect Markovian assumption, multi-step predictors can significantly outperform their single-step counterparts.

These findings provide a foundation for more informed model design in learning-based control and forecasting. Promising directions for future work include: extending these results to the setting of nonlinear systems and analyzing predictor performance in closed-loop control in frameworks other than the LQR setting studied in this work, e.g. model based reinforcement learning.
