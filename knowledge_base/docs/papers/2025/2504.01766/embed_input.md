<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning with Imperfect Models: When Multi-step Prediction Mitigates Compounding Error

Topics include Reinforcement learning, Imitation learning, Control, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Compounding error, where small prediction mistakes accumulate over time, presents a major challenge in learning-based control. For example, this issue often limits the performance of model-based reinforcement learning and imitation learning. One common approach to mitigate compounding error is to train multi-step predictors directly, rather than relying on autoregressive rollout of a single-step model. However, it is not well understood when the benefits of multi-step prediction outweigh the added complexity of learning a more complicated model. In this work, we provide a rigorous analysis of this trade-off in the context of linear dynamical systems. We show that when the model class is well-specified and accurately captures the system dynamics, single-step models achieve lower asymptotic prediction error. On the other hand, when the model class is misspecified due to partial observability, direct multi-step predictors can significantly reduce bias and thus outperform single-step approaches.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

These theoretical results are supported by numerical experiments, wherein we also (a) empirically evaluate an intermediate strategy which trains a single-step model using a multi-step loss and (b) evaluate performance of single step and multi-step predictors in a closed loop control setting.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A typical approach to time series forecasting is to fit a one-step ahead prediction model and apply it recursively to obtain predictions over multiple time steps. In doing so, small errors may compound over time, leading to poor long-horizon prediction. This issue hinders the application of such single-step models in e.g., controller design.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

By directly training multi-step models to predict longer horizons, the issue of compounding error can be mitigated. The main drawback of doing so is that the number of parameters for a direct multi-step predictor scales with the prediction horizon, thus potentially requiring more data to achieve a desired prediction performance. While this tradeoff between prediction horizon accuracy and data requirements is broadly known to exist, it is primarily studied from an empirical perspective. We therefore lack principled guidance for exactly when direct multi-step prediction should be preferred over autoregressive rollout of single-step models. Motivated by this challenge, we provide a rigorous comparison of the sample efficiency of learning multi-step predictors with that of learning single-step predictors in the setting of a linear dynamical system.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Multi-step Identification", "weight": 1.0} -->

The goal of system identification is to use data to learn a model that can be used for forecasting or control. To this end, one typically wants to select a model from the hypothesis class that minimizes the simulation error, i.e., the cumulative prediction error over all future time steps. Due to the computational challenge of doing so, it is much more common to instead learn a model which minimizes the single-step prediction error and apply it autoregressively. However, such approaches tend to generalize poorly if the underlying data generating process does not belong to the hypothesis class. This has motivated the application of algorithms such as Data as Demonstrator (DaD) which use approaches from imitation learning to train a predictor to self-correct its prediction error at each step, leading to improved empirical performance.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Multi-step Identification", "weight": 1.0} -->

Direct learning of prediction models for each time-step in the prediction horizon partially bypasses the issue of compounding error, and has proven successful for both model predictive control and value approximation in MDPs. Empirical studies of single-step and multi-step dynamics models learned with various neural network architectures have also been conducted. Namely, Lambert et al. investigate the performance of recursive application of single-step models parameterized by neural networks in a handful of examples and characterize circumstances which may worsen the effects of compounding error. Chandra et al. give a comparison of various deep learning architectures for predicting multiple steps of a time series and show the efficacy of bidirectional and encoder-decoder LSTM networks.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Multi-step Identification", "weight": 1.0} -->

These empirical studies underscore the importance of careful consideration when designing a model for multi-step prediction. Our work studies this question in stylized settings, allowing us to clearly demonstrate the potential drawbacks and benefits of direct multi-step prediction as compared to more traditional single-step approaches.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Learning-Enabled Control", "weight": 1.0} -->

While the issue of compounding error has long been studied in system identification and control, it has resurfaced as a prominent issue in the learning community, exacerbated by the use of neural networks as function approximators. In model-based reinforcement learning, it has been observed that synthesized controllers may exploit compounding errors of the learned model, motivating numerous heuristics for accounting for the model error during policy synthesis. Lambert et al. instead propose learning a direct multi-step predictor parametrized by a low dimensional decision variable which may be optimized online. The issue of a mismatch between the hypothesis class and the underlying data generating process also poses a challenge for behavior cloning. For example, incorrectly assuming that the demonstrator is Markovian can lead to a policy that deviates substantially from the demonstrator. This can be remedied in part by replacing the standard behavior cloning objective with an objective that predicts the expert actions for multiple timesteps to maintain temporal consistency, resulting in so-called *action-chunking* based approaches.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Learning-Enabled Control", "weight": 1.0} -->

We draw inspiration from these studies, and consider instances of linear systems with either Markovian or non-Markovian observations to compare direct multi-step prediction and autoregressive evaluation of single-step predictors.

<!-- chunk {"id": "body-0011", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

We provide the first quantitative comparison of the multi-step prediction error incurred by directly learned multi-step predictors against that incurred by autoregressive evaluation of a single-step predictor. In particular: We provide an asymptotic characterization of the multi-step prediction error for the two methods in the setting of a fully observed dynamical system. Our results show that for stable systems with a small spectral radius, the prediction error of autoregressive evaluation decays significantly faster with increasing data than that of direct multi-step prediction. This benefit diminishes as the spectral radius increases to one.

<!-- chunk {"id": "body-0012", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

We characterize the prediction error for the two methods applied to a partially observed dynamical system which is incorrectly assumed to be fully observed by the hypothesis class, thus addressing the issue of trajectory prediction under misspecification due to an unjustified Markovian assumption. These results demonstrate that multi-step predictors may enjoy significantly lower bias in the face of model misspecification.

<!-- chunk {"id": "body-0013", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

We conduct numerical experiments that compare the aforementioned approaches with an additional standard baseline: fitting a single-step model that minimizes the multi-step prediction error.

<!-- chunk {"id": "body-0014", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

We empirically evaluate the performance of autoregressive rollouts of single step predictors and multi-step predictors in a closed loop control setting.

<!-- chunk {"id": "body-0015", "role": "body", "section": "I-B Contributions", "weight": 1.0} -->

Our results, while limited to stylized settings, capture key properties of real systems---such as partial observability and misspecification---and thus provide useful guidance to practitioners navigating the complex design space of data-driven multi-step predictors.\Notation: $\mathcal{N}{(\mu,\sigma^{2})}$ denotes a normal distribution with mean $\mu$ and variance $\sigma^{2}$, $\rho{(\cdot)}$ denotes the spectral radius of a matrix, $\left. \parallel \cdot \parallel \right.$ denotes the vector Euclidean norm, $\left. \parallel \cdot \parallel{}_{F} \right.$ denotes the matrix Frobenius norm, ${\mathsf{v}\mathsf{e}\mathsf{c}}{(\cdot)}$ denotes the vectorization of a matrix, and $\otimes$ denotes the Kronecker product.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We assume that the dynamics are unknown, and our goal is to learn a predictor that forecasts a horizon $H$ of future observations using past observations. To this end, we suppose that we are given a dataset $\mathcal{D}_{N} = \left\{ {(y_{t},u_{t})} \right\}_{t = 1}^{N}$ collected from a training rollout of which will be used to determine a function ${\hat{f}}_{H}$ belonging to a hypothesis class $\mathcal{F}_{H}$. This function will be used to predict $y_{{t + 1}:{t + H}}$ given $y_{1:t}$ and $u_{1:{{t + H} - 1}}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The quality of the learned function will be measured by the loss where the operator $\overline{\text{E}}$ is defined as and the expectation is taken over an evaluation rollout of system that is independent of the dataset $\mathcal{D}_{N}$. This is equivalent to taking an expectation under the steady state distribution for the system.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

To provide rigorous understanding of situations where multi-step prediction does or does not help, we consider a simplified setting in which the hypothesis class consists of static linear predictors, i.e., a function $f_{H} \in \mathcal{F}_{H}$, is given by for a matrix $G \in S \subseteq {\mathbb{R}}^{{Hd_{\mathsf{y}}} \times {({d_{\mathsf{y}} + {Hd_{\mathsf{u}}}})}}$. Here the subspace $S$ encodes whether we are fitting a multi-step or single-step model: we provide explicit parameterizations for these model-classes in the next subsections. Our restriction to static linear predictors of the form assumes that the observation sequence is Markovian, i.e., that a history of observations is unnecessary to predict the future trajectory.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

In the sequel, we slightly abuse notation and denote the loss incurred by a predictor defined by matrix $\hat{G}$ by ${L{(\hat{G})}}.$ We consider two settings: one where the Markovian assumption is justified ($C = I$ and $D_{v} = 0$), resulting in a well-specified problem, and one where it is not justified ($C \neq I$ and $D_{v} \succ 0$), resulting in a misspecified problem. In these two settings, we compare the $H$ step prediction error incurred by a learned single-step model rolled out for $H$ timesteps to that incurred by a directly learned $H$-step model.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-A Single-step Predictors", "weight": 1.0} -->

The single-step approach first solves Using this model, one can predict $y_{{t + 1}:{t + H}}$ by rolling out $\begin{bmatrix} \end{bmatrix}$ autoregressively: The resulting $H$-step predictor can be composed to form a direct mapping from the data to the predicted trajectory as As past predictions become part of the regressor for future predictions, this approach often suffers from compounding error.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B Multi-step Predictors", "weight": 1.0} -->

The issue of compounding error from autoregressive roll-out of a single-step model motivates direct multi-step approaches which directly minimize the $H$ step prediction error: for $S \subseteq {\mathbb{R}}^{{Hd_{\mathsf{y}}} \times {({d_{\mathsf{y}} + {Hd_{\mathsf{u}}}})}}$. We consider the function class which fits $H$ distinct predictors, one for each step in the prediction horizon. This amounts to setting $S = {\mathbb{R}}^{{Hd_{\mathsf{y}}} \times {({d_{\mathsf{y}} + {Hd_{\mathsf{u}}}})}}$.^11^1One could impose the causality structure, i.e. that $S$ has a triangular structure. We refrain from doing so for simplicity, and due to the fact that future inputs are independent of the past.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-B Multi-step Predictors", "weight": 1.0} -->

There is a tradeoff induced by fitting multi-step predictors rather than single-step predictors. In particular, the single-step predictor is subject to compounding error, while the complexity of the above identification problem increases for longer horizons. We study this tradeoff in the two aforementioned settings: a system with Markovian observations, and a system with non-Markovian observations. Due to the Markovian assumption for the identification problem, these cases serve as instances where the identification problem is well-specified and misspecified, respectively.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-C Intermediate Formulations", "weight": 1.0} -->

Rather than fitting independent predictors for every timestep, one can instead formulate a hypothesis class for multi-step prediction with lower complexity. In particular, one could impose additional structure on $S$, e.g.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-C Intermediate Formulations", "weight": 1.0} -->

This consists of functions which take the form of a single-step predictor that is applied auto-regressively. In contrast to the single-step approach of Section II-A, solving with this choice of $S$ consists of a multi-step loss function for a class of single-step predictors, a common approach to mitigate the compounding error issue without increasing the number of parameters that must be learned. We study the loss of the predictors fit with classes in numerical experiments and leave analytically characterizing the asymptotic prediction error for this predictor to future work.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Well-Specified Setting", "weight": 1.0} -->

In this section, we study the well-specified setting in which the Markovian assumption is valid. In particular, we restrict system to be a fully observed system by assuming that $C = I$ and $D_{v} = 0$ so $y_{t} = x_{t}$ for all $t$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Well-Specified Setting", "weight": 1.0} -->

To compare the single-step and multi-step approaches in this setting, we first observe that either predictor ${\hat{f}}_{H}$ is defined in terms of a linear map $\hat{G}$ applied to the vector $\begin{bmatrix} \end{bmatrix}^{\top}$. Therefore the loss may be written Rolling out the dynamics, we find that Then expanding $x_{{t + 1}:{t + H}}$ in equation, and using the independence of $w_{t:{{t + H} - 1}}$ from $x_{t}$ and $u_{t:{{t + H} - 1}}$, we conclude that where $\Sigma_{z} = {\overline{\text{E}}\begin{bmatrix} \end{bmatrix}\begin{bmatrix} \end{bmatrix}^{\top}}$ is the stationary covariance for the regressor.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Well-Specified Setting", "weight": 1.0} -->

Consequently, the discrepancy between the single-step and multi-step predictors is contained in the term $\left\| {{({\hat{G} - G^{\star}})}\Sigma_{z}^{1/2}} \right\|_{F}^{2}$. We study the behavior of this term asymptotically, where $\hat{G}$, or equivalently ${\hat{G}}_{N}$, is an operator learned on the dataset of size $N$.^22^2We sometimes omit the subscript $N$ on ${\hat{G}}_{N}$ to ease notational burden. In particular, we examine for the single-step and multi-step predictors ${\hat{G}}_{N}^{SS}$ and $G_{N}^{MS}$, respectively, where the expectation is taken over the dataset used to fit ${\hat{G}}_{N}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Well-Specified Setting", "weight": 1.0} -->

The reducible error of the multi-step predictor is characterized by the following proposition.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-A Comparison", "weight": 1.0} -->

We can express the quadratic form defining the reducible portion of the error in Proposition III.1 as the reducible error in Proposition III.2 plus the additional term ${tr}{({\Gamma_{w}{({{({{M_{MS} - M_{SS}} + {{({H - 1})}d_{u}I_{H}}})} \otimes I_{d_{X}}})}\Gamma_{w}^{T}})}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-A Comparison", "weight": 1.0} -->

As a result, we see that a multi-step predictor is less efficient than a single-step predictor, and that the efficiency gap grows linearly with the prediction horizon $H$. This scaling quantitatively captures that the direct multi-step predictor has a number of parameters which scales with $H$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-A Comparison", "weight": 1.0} -->

To better understand the role of system stability in determining this efficiency gap, we consider the special case of a scalar system without inputs. Here the difference between the statistical efficiency of the single-step predictor and the multi-step predictor is characterized by the difference between the matrices from which we conclude that the difference between the two diminishes as $|a|\rightarrow 1$, i.e. as the system approaches marginal stability.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Misspecified Setting", "weight": 1.0} -->

We again consider a single-step predictor and a multi-step predictor applied to the measurement and sequence of future inputs. However, we now examine the general case in which measurements do not provide full state information by reincorporating partial observations, as specified by $C \in {\mathbb{R}}^{d_{\mathsf{y}} \times d_{\mathsf{x}}}$ and ${D_{v}D_{v}^{\top}} \succ 0$, into the dynamics. Due to the Markovian assumption made in fitting the predictor, this represents a misspecified setting. To ease notational burden we restrict attention to the setting without inputs and set $B = 0$, although our analysis can be extended naturally to the $B \neq 0$ case.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Misspecified Setting", "weight": 1.0} -->

In this setting, the loss is given by We rewrite the dynamics in innovations form where $e_{t}$ is standard normal noise that is independent across time, $K$ is the Kalman gain defined as $K = {ASC^{\top}{({{CSC^{\top}} + R})}^{- 1}}$, $S$ is the stabilizing solution to the Riccati equation defined by $A$, $C$, $D_{w}D_{w}^{\top}$ and $D_{v}D_{v}^{\top}$, and $D_{e} = {({{CSC^{\top}} + {D_{v}D_{v}^{\top}}})}^{1/2}$. Then Under these definitions, and exploiting that innovations are independent across time, the error is given by where $\Sigma_{\hat{x}}$ is the stationary covariance of ${\hat{x}}_{t}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Misspecified Setting", "weight": 1.0} -->

When $\hat{G}$, or equivalently ${\hat{G}}_{N}$, is learned on the dataset of size $N$, we can decompose this quantity into an irreducible component, and a component which decays to zero as the amount of data $N\rightarrow\infty$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Misspecified Setting", "weight": 1.0} -->

Denoting the irreducible component by ${B{({\hat{G}}_{N})}} \triangleq {\lim_{N\rightarrow\infty}{{\text{E}L}{({\hat{G}}_{N})}}}$ and the reducible component by ${\varepsilon{({\hat{G}}_{N})}} \triangleq {{L{({\hat{G}}_{N})}} - {B{({\hat{G}}_{N})}}}$, we decompose Unlike the well-specified setting, the irreducible component $B{({\hat{G}}_{N})}$ differs depending on whether we fit a single-step model or direct multi-step model. We therefore focus on comparing these bias terms rather than the rate of convergence, since this captures the fundamental difference between the two models.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Misspecified Setting", "weight": 1.0} -->

See Section A-C (multi-step) and Section A-D (single-step) for characterizations of the rate of decay of the reducible errors $\lim_{N\rightarrow\infty}{N{\text{E}{\lbrack{\varepsilon{({\hat{G}}_{N})}}\rbrack}}}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Misspecified Setting", "weight": 1.0} -->

The irreducible error for the multi-step predictor is characterized in the following proposition.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-A Comparison", "weight": 1.0} -->

In contrast to the well-specified setting, the dominant discrepancy between the two predictors in the presence of misspecification is the bias term. Note that the bias from the multi-step predictor given in Proposition IV.1 is equal to and therefore, the irreducible error for the direct multi-step never exceeds that of its single-step counterpart.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-A Comparison", "weight": 1.0} -->

Due to the dependence of $M$ on powers of $CA\Sigma_{x}C^{\top}\Sigma_{y}^{- 1}$ in the single-step model's bias, the spectral radius of this quantity dictates how the bias scales with the horizon. Lemma A.1 shows that the quantity $CA\Sigma_{x}C^{\top}\Sigma_{y}^{- 1}$ which the estimate ${\hat{G}}_{y}$ converges to satisfies ${\rho{({CA\Sigma_{x}C^{\top}\Sigma_{y}^{- 1}})}} \leq 1$ if $A$ is stable. Despite this, $CA\Sigma_{x}C^{\top}\Sigma_{y}^{- 1}$ can feature a spectral radius much larger than that of $A$, as demonstrated in the following example.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Example IV.1", "weight": 1.0} -->

As a consequence of this fact, the gap in bias between the multi-step error and the single-step error can grow with the horizon for moderate $H$. This is illustrated for the above example in Figure 1.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

To validate the bounds presented in the previous sections, we consider the system defined by with ${B = \begin{bmatrix} \end{bmatrix}^{\top}},{{C = I_{2}},{\Sigma_{v} = 0}}$ in the well-specified setting and, alternatively, ${B = 0},{{C = {\lbrack 1,0\rbrack}},{\Sigma_{v} = 1}}$ in the misspecified setting.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

(a) Infinite-horizon LQR cost, well-specified case (b) Spectral radius of the closed loop system, misspecified case Figure 5: Infinite-horizon LQR performance in the well-specified case (a) and the misspecified case (b). In (b), closed loop spectral radius greater than 1 for the one step predictor implies infinite LQR cost.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Well-specified: Figure 2 illustrates the well-specified setting. Specifically, we estimate $N{\text{E}{\lbrack{L{({\hat{f}}_{H})}}\rbrack}}$ by averaging over $30,000$ datasets $D_{N}$ for $N \in {\{ 1,\ldots,3000\}}$ to demonstrate convergence to the reducible errors given in Proposition III.1 and Proposition III.2. In these figures, we fix $H = 5$ and vary $a$ across $0.5,0.75$, and $0.9$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Misspecified: Figure 3 illustrates the misspecified setting. Specifically, we estimate $\text{E}{\lbrack{L{({\hat{f}}_{H})}}\rbrack}$ by averaging over $1,000$ datasets $D_{N}$ for $N \in {\{ 1,\ldots,3000\}}$ to demonstrate convergence to the irreducible errors given in Proposition IV.1 and Proposition IV.2. In these figures, we fix $H = 5$ and vary $a$ across $0.5,0.75$, and $0.9$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Multi-step loss: In Figure 4, we compare the multi-step predictor with the single-step predictor trained using a single-step loss, and a multi-step loss with $a = 0.9$ and $H = 10$. We see that in the well-specified setting, the rate of decay for the prediction error of the single-step model trained with a multi-step loss matches the rate of decay for the prediction error using a single-step loss. However, in the presence of misspecification, the prediction error converges nearly to the level of the direct multi-step predictor. The function class for the predictor strictly less expressive than the direct multi-step predictor which explains why the direct multi-step loss still incurs less bias. For the single-step model with a multi-step loss, $\hat{G}$ is fit using gradient descent initialized from the single-step predictor fit with a single-step loss, and using a step size ${2e} - 5$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Control Performance: In Figure 5, we consider a closed-loop control setting in which the control inputs are selected using predictions from either single-step or multi-step models, each trained on datasets of size $N$. In particular the control input is selected via model predictive control using a horizon $H = 20$ with stage costs ${c{(y_{t},u_{t})}} = {\left\| y_{t} \right\|^{2} + \left\| u_{t} \right\|^{2}}$ and $y_{t + H}$ constrained to 0. Panel (a) shows the infinite-horizon LQR cost, $\lim_{T\rightarrow\infty}\text{E}\left\lbrack \sum_{t = 1}^{T}y_{t}^{\top}y_{t} + u_{t}^{\top}u_{t} \right\rbrack$ incurred by this controller in the well-specified setting for a system with $a = 0.9$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

averaged over 1,000 datasets. The multi-step predictor uses the same horizon, $H = 5$ as the MPC horizon. In the low-data regime, single-step rollouts result in lower cost than multi-step prediction.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

Panel (b) shows the spectral radius of the resulting closed-loop system in the misspecified setting for the same system ($a = 0.9$, $H = 20$), averaged over 1,000 datasets. A spectral radius greater than 1 for the single-step rollout indicates that the closed-loop system is unstable, and the associated infinite-horizon LQR cost diverges.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we present a novel theoretical comparison of the asymptotic prediction error associated with autoregressive rollouts of single-step predictors and direct multi-step predictors. Our analysis offers insight into when each modeling approach is preferable. Specifically, we show that for well-specified model classes, autoregressive rollouts of single-step predictors achieve lower asymptotic prediction error. However, in the presence of model misspecification due to an incorrect Markovian assumption, multi-step predictors can significantly outperform their single-step counterparts.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusion", "weight": 1.5} -->

These findings provide a foundation for more informed model design in learning-based control and forecasting. Promising directions for future work include: developing a rigorous analysis of intermediate approaches, such as the single-step model trained with a multi-step loss, which we investigate only empirically in this work; and extending our analysis beyond the white-noise input assumption to study how each of these prediction approaches performs in a closed-loop control setting.
