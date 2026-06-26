<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Statistical Efficiency of Single- and Multi-step Models for Forecasting and Control

Topics include Accuracy, Control, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Compounding error, where small prediction mistakes accumulate over time, presents a major challenge in learning-based control. A common remedy is to train multi-step predictors directly instead of rolling out single-step models. However, it is unclear when the benefits of multi-step predictors outweigh the difficulty of learning a more complex model. We provide the first quantitative analysis of this trade-off for linear dynamical systems. We study three predictor classes: (i) single step models, (ii) multi-step models, and (iii) single step models trained with multi-step losses. We show that when the model class is well-specified and accurately captures the system dynamics, single-step models achieve the lowest asymptotic prediction error. On the other hand, when the model class is misspecified due to partial observability, direct multi-step predictors can significantly reduce bias and improve accuracy. We provide theoretical and empirical evidence that these trade-offs persist when predictors are used in closed-loop control.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

A typical approach to time series forecasting is to fit a one-step ahead prediction model and apply it recursively to obtain predictions over multiple time steps. In doing so, small errors may compound over time, leading to poor long-horizon prediction. This issue can make the application of such single-step models to long-term planning and controller design challenging.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

By directly training multi-step models to predict over longer horizons, the issue of compounding error can be mitigated. The main drawback of doing so is that the number of parameters for a direct multi-step predictor scales with the prediction horizon, thus potentially requiring more data than a single-step predictor to achieve a desired prediction performance. While this tradeoff between prediction horizon accuracy and data requirements is broadly known to exist, it is primarily studied from an empirical perspective. We therefore lack principled guidance for exactly when direct multi-step prediction should be preferred over autoregressive rollout of single-step models. Motivated by this challenge, we provide a rigorous comparison of the sample efficiency of learning multi-step predictors with that of learning single-step predictors in the setting of a linear dynamical system.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Multi-step Identification", "weight": 1.0} -->

The goal of system identification is to use data to learn a model that can be used for forecasting or control. To this end, one typically wants to select a model from the hypothesis class that minimizes the simulation error, i.e., the cumulative prediction error over all future time steps. Due to the computational challenge of doing so, it is much more common to instead learn a model which minimizes the single-step prediction error and apply it autoregressively. However, such approaches tend to generalize poorly if the underlying data generating process does not belong to the hypothesis class. This has motivated the application of algorithms such as Data as Demonstrator (DaD) which use approaches from imitation learning to train a predictor to self-correct its prediction error at each step, leading to improved empirical performance.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Multi-step Identification", "weight": 1.0} -->

Direct learning of prediction models for each time-step in the prediction horizon partially bypasses the issue of compounding error, and has proven successful for both model predictive control and value approximation in MDPs. Empirical studies of single-step and multi-step dynamics models learned with various neural network architectures have also been conducted. Namely, investigates the performance of recursive application of single-step models parameterized by neural networks in a handful of examples and characterize circumstances which such models may worsen the effects of compounding error. In, the authors give a comparison of various deep learning architectures for predicting multiple steps of a time series and show the efficacy of bidirectional and encoder-decoder LSTM networks.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Multi-step Identification", "weight": 1.0} -->

These empirical studies underscore the importance of careful consideration when designing a model for multi-step prediction. Our work studies this question in stylized settings, allowing us to clearly demonstrate the potential drawbacks and benefits of direct multi-step prediction as compared to more traditional single-step approaches.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Learning-Enabled Control", "weight": 1.0} -->

While the issue of compounding error has long been studied in system identification and control, it has resurfaced as a prominent issue in the learning community, exacerbated by the use of neural networks as function approximators. In model-based reinforcement learning, it has been observed that synthesized controllers may exploit compounding errors of the learned model, motivating numerous heuristics for accounting for the model error during policy synthesis. In, the authors instead propose learning a direct multi-step predictor parametrized by a low dimensional decision variable which may be optimized online.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Learning-Enabled Control", "weight": 1.0} -->

The issue of a mismatch between the hypothesis class and the underlying data generating process also poses a challenge for behavior cloning. For example, incorrectly assuming that the demonstrator is Markovian can lead to a policy that deviates substantially from the demonstrator. This can be remedied in part by replacing the standard behavior cloning objective with an objective that predicts the expert actions for multiple timesteps to maintain temporal consistency, resulting in so-called *action-chunking* based approaches. We draw inspiration from these studies, and consider instances of linear systems with either Markovian or non-Markovian observations to compare direct multi-step prediction and autoregressive evaluation of single-step predictors.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Contributions", "weight": 1.0} -->

Our prior work provided a quantitative comparison of the multi-step prediction error incurred by a directly learned multi-step predictor and autoregressive evaluation of a single-step predictor. Here, we extend this work: (i) considering a third class of predictors, specifically a single-step predictor trained by minimizing a multi-step loss, (ii) analyzing the resulting closed-loop control performance, and (iii) providing complete proofs. In particular: We provide an asymptotic characterization of the multi-step prediction error for the three methods in the setting of a fully observed dynamical system. Our results show that for stable systems with a small spectral radius, the prediction error of autoregressive evaluation for a single-step predictor decays significantly faster with increasing data than that of the other methods.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Contributions", "weight": 1.0} -->

We characterize the prediction error for the three methods applied to a partially observed dynamical system that is incorrectly assumed to be fully observed by the hypothesis class, thus addressing the issue of trajectory prediction under misspecification due to an unjustified Markovian assumption. These results demonstrate that multi-step predictors may enjoy significantly lower bias in the face of model misspecification.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Contributions", "weight": 1.0} -->

We analyze predictor performance in a closed loop control setting. Our results show that, in the case of a fully observed dynamical system (well-specified setting), autoregressive evaluation of a single-step predictor fitted with a single step loss often yields lower control cost than autoregressive evaluation of a single step predictor fitted with a multistep loss.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Contributions", "weight": 1.0} -->

We conduct numerical experiments that exemplify the above results. Code to reproduce these experiments is available.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Contributions", "weight": 1.0} -->

^11^1Code to reproduce experiments: Our results, while limited to stylized settings, capture key properties of real systems---such as partial observability and misspecification---and thus provide useful guidance to practitioners navigating the complex design space of data-driven multi-step predictors.\Notation: $\mathcal{N}(\mu,\sigma^{2})$ denotes a normal distribution with mean $\mu$ and variance $\sigma^{2}$, $\overset{p}{\to}$ denotes convergence in probability, $\rho(\cdot)$ denotes the spectral radius of a matrix, $\left\|\cdot\right\|$ denotes the vector Euclidean norm, $\left\|\cdot\right\|_{F}$ denotes the matrix Frobenius norm, $\left\|\cdot\right\|_{\star}$ denotes the matrix nuclear norm, $\operatorname{\mathsf{vec}}(\cdot)$ denotes the vectorization of a matrix, and $\otimes$ denotes the Kronecker product.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Contributions", "weight": 1.0} -->

For a random sequence $X_{n}$, we use $X_{n}={\cal O}_{p}\mathopen{}\left(a_{n}\right)\mathclose{}$ to denote that the set of values $X_{n}/a_{n}$ is stochastically bounded. We use the notation $X_{a:b}$ to denote the sequence $X_{n}$ for $n=a$ to $n=b$. For functions $f,g$ of $x$, we use the notation $f(x)=o(g(x))$ to denote that $\lim_{x\rightarrow\infty}\frac{f(x)}{g(x)}=0$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We assume that the dynamics are unknown, and our goal is to learn a predictor that forecasts a horizon $H$ of future observations using past observations. To this end, we suppose that we are given a dataset $\mathcal{D}_{N}=\mathopen{}\left\{(y_{t},u_{t})\right\}\mathclose{}_{t=1}^{N}$ collected from a training rollout of which will be used to determine a function $\hat{f}_{H}$ belonging to a hypothesis class $\mathcal{F}_{H}$. This function will be used to predict $y_{t+1:t+H}$ given $y_{1:t}$ and $u_{1:t+H-1}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The quality of the learned function will be measured by the loss where the operator $\bar{\operatorname{\textbf{E}}}$ is defined as and the expectation is taken over an evaluation rollout of system that is independent of the dataset $\mathcal{D}_{N}$. By ergodicity of the process, this is equivalent to taking an expectation under the steady state distribution for the system.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

To provide rigorous understanding of situations where multi-step prediction does or does not help, we consider a simplified setting in which the hypothesis class consists of static linear predictors, i.e., a function $f_{H}\in\mathcal{F}_{H}$ given by for a matrix $G\in S\subseteq\mathbb{R}^{Hd_{\mathsf{y}}\times(d_{\mathsf{y}}+Hd_{\mathsf{u}})}$. Here the subspace $S$ encodes whether we are fitting a multi-step or single-step model: we provide explicit parameterizations for these model-classes in the next subsections. Our restriction to static linear predictors of the form assumes that the observation sequence is Markovian, i.e., that a history of observations is unnecessary to predict the future trajectory.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

In the sequel, we slightly abuse notation and denote the loss incurred by a predictor defined by matrix $\hat{G}$ by $L(\hat{G}).$ We consider two settings: one where the Markovian assumption is justified ($C=I$ and $D_{v}=0$), resulting in a well-specified problem, and one where it is not justified ($C\neq I$ or $D_{v}D_{v}^{\top}\succ 0$), resulting in a misspecified problem. In these two settings, we compare the $H$ step prediction error incurred by a learned single-step model rolled out for $H$ timesteps to that incurred by a directly learned $H$-step model.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Throughout, we use "misspecification" specifically to refer to violations of the Markov assumption induced by partial observability (and observation noise), while "well-specified" refers to the fully observed state setting.

<!-- chunk {"id": "body-0021", "role": "body", "section": "I-A Single-step Predictors", "weight": 1.0} -->

The single-step approach first solves Using this model, one can predict $y_{t+1:t+H}$ by rolling out $\begin{bmatrix}\hat{G}_{y}&\hat{G}_{u}\end{bmatrix}$ autoregressively: The resulting $H$-step predictor can be composed to form a direct mapping from the data to the predicted trajectory as As past predictions become part of the regressor for future predictions, this approach often suffers from compounding error.

<!-- chunk {"id": "body-0022", "role": "body", "section": "I-B Multi-step Predictors", "weight": 1.0} -->

The issue of compounding error from autoregressive roll-out of a single-step model motivates direct multi-step approaches which directly minimize the $H$ step prediction error: for $S\subseteq\mathbb{R}^{Hd_{\mathsf{y}}\times(d_{\mathsf{y}}+Hd_{\mathsf{u}})}$. We consider the function class which fits $H$ distinct predictors, one for each step in the prediction horizon. This amounts to setting $S=\mathbb{R}^{Hd_{\mathsf{y}}\times(d_{\mathsf{y}}+Hd_{\mathsf{u}})}$.^33^3One could impose the causality structure, i.e. that $S$ has a triangular structure. We refrain from doing so for simplicity, and due to the fact that future inputs are independent of the past.

<!-- chunk {"id": "body-0023", "role": "body", "section": "I-B Multi-step Predictors", "weight": 1.0} -->

There is a tradeoff induced by fitting multi-step predictors rather than single-step predictors. In particular, the single-step predictor is subject to compounding error, while the complexity of the above identification problem increases for longer horizons.

<!-- chunk {"id": "body-0024", "role": "body", "section": "I-C Intermediate Formulations", "weight": 1.0} -->

Rather than fitting independent predictors for every timestep, one can instead formulate a hypothesis class for multi-step prediction with lower complexity. In particular, one could impose additional structure on $S$. For example, let This consists of functions which take the form of a single-step predictor that is applied auto-regressively. In contrast to the single-step approach of Section I-A, solving with this choice of $S$ consists of a multi-step loss function for a class of single-step predictors, a common approach to mitigate the compounding error issue without increasing the number of parameters that must be learned.

<!-- chunk {"id": "body-0025", "role": "body", "section": "I-C Intermediate Formulations", "weight": 1.0} -->

We compare single-step, multi-step, and the intermediate predictors described above in the two aforementioned settings: a system with Markovian observations, and a system with non-Markovian observations. Due to the Markovian assumption for the identification problem, these cases serve as instances where the identification problem is well-specified and misspecified, respectively.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Well-Specified Setting", "weight": 1.0} -->

In this section, we study the well-specified setting in which the Markovian assumption is valid. In particular, we restrict system to be a fully observed system by assuming that $C=I$ and $D_{v}=0$ so $y_{t}=x_{t}$ for all $t$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Well-Specified Setting", "weight": 1.0} -->

To compare the three approaches in this setting, we first observe that the predictors $\hat{f}_{H}$ are defined in terms of a linear map $\hat{G}$ applied to the vector $\begin{bmatrix}x_{t}^{\top}&u_{t:t+H-1}^{\top}\end{bmatrix}^{\top}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Well-Specified Setting", "weight": 1.0} -->

Therefore the loss may be written Rolling out the dynamics, we find that Then expanding $x_{t+1:t+H}$ in equation, and using the independence of $w_{t:t+H-1}$ from $x_{t}$ and $u_{t:t+H-1}$, we conclude that where $\Sigma_{z}=\bar{\operatorname{\textbf{E}}}z_{t}z_{t}^{\top}$ is the stationary covariance for the regressor $z_{t}\triangleq\begin{bmatrix}x_{t}\\u_{t:t+H-1}\end{bmatrix}$. ^44^4By the fact that $w_{t},u_{t}$ are i.i.d.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Well-Specified Setting", "weight": 1.0} -->

standard normal and $(A,\begin{bmatrix}B,B_{w}\end{bmatrix})$ is controllable, persistence of excitation holds, i.e. $\Sigma_{z}$ is positive definite. Consequently, the discrepancy between the single-step and multi-step predictors is contained in the term $\left\|(\hat{G}-G^{\star})\Sigma_{z}^{1/2}\right\|_{F}^{2}$. We study the behavior of this term asymptotically, where $\hat{G}$, or equivalently $\hat{G}_{N}$, is an operator learned on the dataset of size $N$.^55^5We sometimes omit the subscript $N$ on $\hat{G}_{N}$ to ease notational burden.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Well-Specified Setting", "weight": 1.0} -->

The reducible error of the multi-step predictor is characterized by the following proposition.

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-A Comparison of Predictor Error", "weight": 1.0} -->

The next proposition compares the asymptotic decay rates given in Propositions II.1. ‣ II Well-Specified Setting ‣ Statistical Efficiency of Single- and Multi-step Models for Forecasting and Control"), II.2. ‣ II Well-Specified Setting ‣ Statistical Efficiency of Single- and Multi-step Models for Forecasting and Control") and II.3.

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-B Numerical Experiments", "weight": 1.0} -->

To validate the error characterizations presented in section II, we consider the fully observed system defined by with $B=\begin{bmatrix}0&1\end{bmatrix}^{\top},C=I_{2},\Sigma_{v}=0$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "II-B Numerical Experiments", "weight": 1.0} -->

In Figure 1, we estimate $N\operatorname{\textbf{E}}[L(\hat{f}_{H})]$ by averaging over $2,500$ datasets $D_{N}$ for $N\in\{1,...,3000\}$ to demonstrate convergence to the reducible errors given in Propositions II.1. ‣ II Well-Specified Setting ‣ Statistical Efficiency of Single- and Multi-step Models for Forecasting and Control"), II.2. ‣ II Well-Specified Setting ‣ Statistical Efficiency of Single- and Multi-step Models for Forecasting and Control") and II.3. In these figures, we fix $H=5$ and vary $a$ across $0.5,0.75$, and $0.9$. For the single-step model with a multi-step loss, $\hat{G}$ is fit using Adam initialized from the single-step predictor fit with a single-step loss, and using a step size $1e-2$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "II-B Numerical Experiments", "weight": 1.0} -->

For each data generating process (choice of parameter $a$) and each predictor, we see that the decay rate of the excess prediction error converges to its predicted value as $N$ increases. Comparing the decay rates across predictor classes, these results exemplify the efficiency gap suggested by Proposition II.4. That is, for each choice of the parameter $a$, the excess prediction error of the single-step predictor has the fastest decay rate, followed by the single-step predictor with a multi-step loss, then the direct multi-step predictor. Comparing the figures left to right, we see that, unlike for the scalar system discussed in Section II-A, the efficiency gap does not diminish with $a$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Misspecified Setting", "weight": 1.0} -->

We again consider a single-step predictor and a multi-step predictor applied to the measurement. However, we now examine the general case in which measurements do not provide full state information by reincorporating partial observations, as specified by $C\in\mathbb{R}^{d_{\mathsf{y}}\times d_{\mathsf{x}}}$ and $D_{v}D_{v}^{\top}\succ 0$, into the dynamics. Due to the Markovian assumption made in fitting the predictor, this represents a misspecified setting. To ease notational burden we restrict attention to the setting without inputs and set $B=0$, although our analysis can be extended naturally to the $B\neq 0$ case.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Misspecified Setting", "weight": 1.0} -->

In this setting, the loss is given by We rewrite the dynamics in innovations form as where $e_{t}$ is standard normal noise that is independent across time, $K$ is the Kalman gain defined as $K=ASC^{\top}(CSC^{\top}+R)^{-1}$, $S$ is the stabilizing solution to the Riccati equation defined by $A$, $C$, $D_{w}D_{w}^{\top}$ and $D_{v}D_{v}^{\top}$, and $D_{e}=(CSC^{\top}+D_{v}D_{v}^{\top})^{1/2}$. Then Under these definitions, and exploiting that innovations are independent across time, the error is given by where $\Sigma_{\hat{x}}$ is the stationary covariance of $\hat{x}_{t}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Misspecified Setting", "weight": 1.0} -->

Let $\Sigma_{y}$ be the stationary covariance of $y_{t}$.^66^6It follows from $D_{v}D_{v}^{\top}\succ 0$ that $\Sigma_{y}$ is positive definite. When $\hat{G}$, or equivalently $\hat{G}_{N}$, is learned on the dataset of size $N$, we can decompose this quantity into an irreducible component, and a component which decays to zero as the amount of data $N\to\infty$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Misspecified Setting", "weight": 1.0} -->

Denoting the irreducible component by $B(\hat{G}_{N})\triangleq\lim_{N\to\infty}\operatorname{\textbf{E}}L(\hat{G}_{N})$ and the reducible component by $\varepsilon(\hat{G}_{N})\triangleq L(\hat{G}_{N})-B(\hat{G}_{N})$, we decompose Unlike the well-specified setting, the irreducible component $B(\hat{G}_{N})$ differs depending on whether we fit a single-step model, direct multi-step model, or single-step model fitted with a multi-step loss. We therefore focus on comparing these bias terms rather than the rate of convergence, since this captures the fundamental difference between the two models.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Misspecified Setting", "weight": 1.0} -->

The irreducible error for the multi-step predictor is characterized in the following proposition.

<!-- chunk {"id": "body-0040", "role": "body", "section": "III-A Comparison", "weight": 1.0} -->

The next proposition compares the asymptotic biases given in Proposition III.1. ‣ III Misspecified Setting ‣ Statistical Efficiency of Single- and Multi-step Models for Forecasting and Control"), Proposition III.2. ‣ III Misspecified Setting ‣ Statistical Efficiency of Single- and Multi-step Models for Forecasting and Control"), and Proposition III.3.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Example III.1", "weight": 1.0} -->

As a consequence of this fact, the gap in bias between the multi-step error and the single-step error can grow with the horizon for moderate $H$. This is illustrated for the above example in Figure 3.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-B Numerical Experiments", "weight": 1.0} -->

To validate the error characterizations presented in section III, we consider the partially observed system defined by In Figure 2, we estimate $\operatorname{\textbf{E}}[L(\hat{f}_{H})]$ by averaging over $2,500$ datasets $D_{N}$ for $N\in\{1,...,3000\}$ to demonstrate convergence to the irreducible errors given in Proposition III.1. ‣ III Misspecified Setting ‣ Statistical Efficiency of Single- and Multi-step Models for Forecasting and Control") and Proposition III.2. ‣ III Misspecified Setting ‣ Statistical Efficiency of Single- and Multi-step Models for Forecasting and Control"). In these figures, we fix $H=5$ and vary $a$ across $0.5,0.75$, and $0.9$. For the single-step model with a multi-step loss, $\hat{G}$ is fit using Adam initialized from the single-step predictor fit with a single-step loss, and using a step size $1e-2$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "III-B Numerical Experiments", "weight": 1.0} -->

For each data generating process (choice of parameter $a$) and each predictor, we see that the prediction error converges to its predicted value as $N$ increases. Comparing prediction error across predictor classes, these results exemplify the bias gap suggested in Proposition III.4. That is, for each choice of the parameter $a$, the multi-step predictor has the lowest asymptotic prediction error, followed by the single-step predictor with a multi-step loss, then the single-step predictor.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Control Performance", "weight": 1.0} -->

We evaluate the predictor classes in a closed-loop control setting in which the control inputs are selected using predictions from a model trained on a dataset of size $N$. In particular, the control input is selected via model predictive control with a planning horizon equal to the predictor's forecast horizon $H$. Given an $H$-step predictor $\hat{G}$, we compute an $H$-step feedback gain $K_{H}(\hat{G})$ such that minimizes the finite horizon quadratic cost At execution time, controls are applied one step at a time according to $u_{t}=K(\hat{G})y_{t}$ where $K(\hat{G})$ is the first $d_{u}$-block row of $K_{H}(\hat{G})$. The infinite-horizon LQR cost incurred by the resulting closed-loop system gives a measure of performance of the predictors.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Control Performance", "weight": 1.0} -->

However, on the event that $K(\hat{G})$ is not stabilizing, $J(K(\hat{G}))$ will be infinite-valued. To account for this, we fix a large upper bound $M\gg 0$ and evaluate performance of predictors according instead to the clipped loss

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-A Well-Specified Setting", "weight": 1.0} -->

In the well-specified setting, we can compare the decay rates of the clipped infinite horizon LQR costs of controllers learned from a single-step predictor with a single step loss and a single step predictor with a multistep loss.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-B Misspecified Setting", "weight": 1.0} -->

In the previous section, we analyzed the infinite-horizon control cost induced by controllers designed using multi-step predictions obtained from (a) a single-step predictor, (b) a single-step predictor trained with a multi-step loss, and (c) a direct multi-step predictor. Under model misspecification, however, irreducible prediction bias may prevent any static state-feedback controller derived from these predictors from stabilizing the true system. In such cases, the infinite-horizon control cost is infinite, even in the limit as the dataset size $N\to\infty$. Consequently, rather than comparing asymptotic control costs, we instead compare predictors through their ability to induce stabilizing controllers. In particular, we identify regimes in which the lower-bias multi-step predictor yields a stabilizing controller, whereas the alternative predictors may fail to do so. We provide numerical examples illustrating this phenomenon and leave theoretical characterization of these regimes to future work.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-B Misspecified Setting", "weight": 1.0} -->

(a) Closed loop spectral radius for system with a = 0.6.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-B Misspecified Setting", "weight": 1.0} -->

(b) Closed loop spectral radius for system with a = 0.75.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-B Misspecified Setting", "weight": 1.0} -->

First, let $K^{\star}$ denote the feedback gain computed from the ground truth multi-step predictor $G^{\star}$. For sufficiently large planning horizon $H$, the associated closed-loop system is stable, i.e. $\rho(A+BK^{\star})<1$. By continuity of the spectral radius, it follows that if a feedback gain $K$ has $\left\|K-K^{\star}\right\|$ sufficiently small, then $K$ yields a stabilizing closed-loop matrix. Since $K(\hat{G})$ is a continuous function of $\hat{G}$, it then follows that for $\left\|\hat{G}-G^{\star}\right\|$ sufficiently small, $\rho\mathopen{}\left(A+BK(\hat{G})\right)\mathclose{}<1$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-B Misspecified Setting", "weight": 1.0} -->

In Proposition III.4, we showed that, in the presence of misspecification, direct multi-step predictors achieve lower asymptotic prediction error than the other predictor types. Thus, they are more likely to lie within this stabilization neighborhood.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-B Misspecified Setting", "weight": 1.0} -->

Second, for stable systems, multi-step prediction errors are dominated by errors in the direction of the modes with the largest magnitude. Since these directions are those which govern stabilization, training predictors with a multi-step loss implicitly emphasizes accurate modeling in the directions which are most relevant for stabilization. Thus, multi-step predictors are better suited for inducing stabilizing controllers.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Nonlinear Systems", "weight": 1.0} -->

In Sections II and III, we provided a rigorous comparison of the prediction error incurred by single- and multi-step predictors. Though these results are restricted to linear systems, we provide empirical evidence that similar phenomena arise for nonlinear dynamics. Consider the system with state $x_{t}=\begin{bmatrix}p_{t}\ q_{t}\end{bmatrix}$, initialized at $x_{0}=\begin{bmatrix}0\ 0\end{bmatrix}$, and evolving as | | $\displaystyle q_{t+1}$ | $\displaystyle=\lambda(q_{t}-p_{t}^{2})+w_{t}^{(q)},$ | | | where $w_{t}^{(p)},w_{t}^{(q)}\overset{iid}{\sim}\mathcal{N}(0,\sigma_{w})$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Nonlinear Systems", "weight": 1.0} -->

We evaluate these predictors in both a well-specified setting ($C=I$, $\sigma_{v}=0$) and a misspecified setting ($C\neq I$, $\sigma_{v}>0$), analogous to Sections II and III.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Nonlinear Systems", "weight": 1.0} -->

In Figure 6, we estimate expected mean-squared prediction error by averaging over $200$ datasets with $N=300$. We fix $\mu=\lambda=0.9$, $\sigma_{w}=0.1$, and vary $H\in$. In the misspecified case, we use $C=\begin{bmatrix}0&1&0&0\end{bmatrix}$ and $\sigma_{v}=0.4$. The intermediate predictor $\hat{G}_{N}^{I}$ is trained using Adam (step size $10^{-2}$), initialized from $\hat{G}_{N}^{SS}$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Nonlinear Systems", "weight": 1.0} -->

The results mirror our linear theory. In the well-specified setting, Figure 6(a) shows that the single-step predictor achieves the lowest error, followed by the single-step predictor trained with a multi-step loss, and then the direct multi-step predictor, consistent with Proposition II.4. In contrast, Figure 6(b) shows the reverse ordering, consistent with Proposition III.4.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Nonlinear Systems", "weight": 1.0} -->

These experiments suggest that the qualitative behavior predicted by our linear analysis may extend to some nonlinear systems. A rigorous treatment of this setting is left for future work.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we present a novel theoretical comparison of the asymptotic prediction error associated with autoregressive rollouts of single-step predictors, direct multi-step predictors, and single-step predictors fitted with multi-step losses. Our analysis offers insight into when each modeling approach is preferable. Specifically, we show that for well-specified model classes, autoregressive rollouts of single-step predictors achieve lower asymptotic prediction error. However, in the presence of model misspecification due to an incorrect Markovian assumption, multi-step predictors can significantly outperform their single-step counterparts.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conclusion", "weight": 1.5} -->

These findings provide a foundation for more informed model design in learning-based control and forecasting. Promising directions for future work include: extending these results to the setting of nonlinear systems and analyzing predictor performance in closed-loop control in frameworks other than the LQR setting studied in this work, e.g. model based reinforcement learning.
