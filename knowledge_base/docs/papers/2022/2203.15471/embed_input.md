<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

State Space Models vs. Multi-step Predictors in Predictive Control: Are State Space Models Complicating Safe Data-driven Designs?

Topics include Optimal control, Predictive control, Safety, Uncertainty, System identification, Control, State space.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper contrasts recursive state space models and direct multi-step predictors for linear predictive control. We provide a tutorial exposition for both model structures to solve the following problems: 1. stochastic optimal control; 2. system identification; 3. stochastic optimal control based on the estimated model. Throughout the paper, we provide detailed discussions of the benefits and limitations of these two model parametrizations for predictive control and highlight the relation to existing works. Additionally, we derive a novel (partially tight) constraint tightening for stochastic predictive control with parametric uncertainty in the multi-step predictor.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Model predictive control (MPC) is an optimization-based control strategy, which is applicable to general MIMO systems and directly accounts for state and input constraints \[. Typically, first a parametric prediction model is identified. In addition to noise and disturbances, the resulting parametric error then needs to be considered to ensure satisfaction of safety critical constraints. In this paper, we study data-driven predictive control problems using two different model parametrizations: state space models and multi-step predictors, i.e., models that skip the sequential state propagation and directly predict $k$-steps into the future.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Contribution", "weight": 1.0} -->

We consider a stochastic optimal control problem for linear systems, as typically arising in MPC, and provide a tutorial-style exposition based on state space models and multi-step predictors, respectively.^11^1Although MPC relies on a receding horizon implementation, we initially focus on the open-loop problem to simplify the exposition. Closed-loop implementations with corresponding caveats are discussed in Section IV-D. First, we reformulate this problem as equivalent quadratic programs (QPs) for both parametrizations (Sec. II). Then, we use a maximum likelihood estimate (MLE) for the system identification (Sec. III). Finally, we study the stochastic optimal control problem with uncertain parameter estimates and derive a novel data-driven stochastic MPC formulation (Sec. IV). Therein, we demonstrate that multi-step predictors allow for a simpler (partially tight) reformulation to account for the parametric uncertainty. On the other hand, accounting for parametric uncertainty in state space models typically requires a sequential propagation, which can result in significant conservatism.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Contribution", "weight": 1.0} -->

Throughout the paper, we provide extensive discussions on the advantages and limitations of the two parametrizations (Sec. II-D, III-C, IV-D), and the relation to existing work (Sec. IV-C).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Stochastic predictive control", "weight": 1.0} -->

We first state the control problem (Sec. II-A) and convert it into a deterministic QP (Sec. II-B). Then, we introduce the multi-step predictors, derive an equivalent QP (Sec. II-C), and provide a discussion (Sec. II-D).

<!-- chunk {"id": "body-0007", "role": "body", "section": "II-A Problem setup", "weight": 1.0} -->

We consider a linear discrete-time system of the form

<!-- chunk {"id": "body-0008", "role": "body", "section": "II-A Problem setup", "weight": 1.0} -->

with ${Q,R} \succ 0$, $H_{x,j} \in {\mathbb{R}}^{n}$, $j \in {\mathbb{I}}_{\lbrack 1,r\rbrack}$, and probability $p \in {}$ for the chance constraints (2b). We consider the stochastic and open-loop control problem to allow for a simple system identification using MLE (Sec. III) and an easier comparison between the two model parametrizations, respectively. Generalizations of this problem setup (e.g., receding horizon, robust, input-output models) are discussed in Sections III-C, IV-C, IV-D. In order to introduce the problem, we assume that the model parameters are known. The problem of system identification and predictive control with probabilistic bounds on the model parameters is treated in Sections III and IV, respectively.

<!-- chunk {"id": "body-0009", "role": "body", "section": "II-C Multi-step predictors", "weight": 1.0} -->

where the matrices $G_{u},G_{0},G_{w}$ directly map to the future state sequence, instead of sequentially applying the one-step prediction of the state space model. The rows in correspond to different horizon steps $k \in {\mathbb{I}}_{\lbrack 1,N\rbrack}$ with

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-C Multi-step predictors", "weight": 1.0} -->

This model corresponds to a compressed/condensed version of the recursive application of the state space model, as is often used for the numerical solution of the QP (cf. \[1, Chap. 7, Sec. 8.8.4\]). This model structure is prevalent in MPC schemes based on FIR models or subspace predictive control (SPC), and is recently employed in many (robust) predictive control approaches (cf. discussion Section IV-C).

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-D Discussion", "weight": 1.0} -->

First, note that both optimization problems are exact solutions to the stochastic optimal control problem.

<!-- chunk {"id": "body-0012", "role": "body", "section": "System Identification", "weight": 1.0} -->

In the following, we assume that the model parameters are unknown and need to be identified. To this end, we apply some probing input signal $u_{\lbrack 0,{T - 1}\rbrack}$ over a time period $T \in {\mathbb{I}}_{\geq 1}$ to the system and obtain noisy state measurements ${\overset{\sim}{x}}_{k} = {x_{k} + \epsilon_{k}}$, $k \in {\mathbb{I}}_{\lbrack 0,T\rbrack}$ with i.i.d. noise $\epsilon_{k} \sim {\mathcal{N}{(0,\Sigma_{\epsilon})}}$. Generalizations to noisy output measurements are discussed in Section IV-D). We assume that the matrices characterizing the variance of the disturbances, i.e., $\Sigma_{w},\Sigma_{\epsilon},E,G_{w}$, are known.

<!-- chunk {"id": "body-0013", "role": "body", "section": "System Identification", "weight": 1.0} -->

First, we focus on the identification of a multi-step predictor (Sec. III-A). Then, we consider the special case of state space models (Sec. III-B) and contrast the results (Sec. III-C).

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A Multi-step predictors", "weight": 1.0} -->

As noted early, subspace identification computes the matrices $G_{u}$, $G_{0}$ as intermediate quantities and hence there is no need to identify a state space model. The direct identification of the multi-step predictor (II-C) can be written as a linear regression problem with the parameters $\theta_{k}:={{vec}\left( {\lbrack G_{0,k},G_{u,k}\rbrack} \right)} \in {\mathbb{R}}^{n^{2} + {nkm}}$. The following lemma provides an MLE to identify each predictor $\theta_{k}$ individually.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-B State space model", "weight": 1.0} -->

The following corollary shows that we can use a simple least-squares estimate for state space models if we assume noise-free state measurements.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-C Discussion", "weight": 1.0} -->

We formulated the identification problem as an MLE with a weighted least-squares estimate, resulting in a (high-probability) bound on the parameter error. However, the presented bounds and estimates can only be applied if the correlation in the disturbances is known. In general, a joint identification of the parameters and this covariance matrix is needed, which results in a nonlinear problem (cf. \[41, Sec. 5\]), which can be solved using expectation-maximisation.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Scalability, conditioning, prior", "weight": 1.0} -->

A crucial difference between the two parametrizations is the number of required parameters. In particular, for the state space model we have $\theta \in {\mathbb{R}}^{n^{2} + {nm}}$ and the parameters often directly relate to physical quantities (e.g., damping constant). This allows for a meaningful integration of priors on the parameters, which can reduce the sample complexity.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Scalability, conditioning, prior", "weight": 1.0} -->

On the other hand, directly identifying a multi-step predictor requires $\theta_{k} \in {\mathbb{R}}^{{nmk} + n^{2}}$, i.e., the number of parameters scales linearly with the horizon $k$. This issue can be relaxed by considering truncated FIR models (cf., \[15, App. A\]) or structured parametrizations using OBF. Multi-step predictors allow to naturally impose general open-loop stability priors, e.g., in terms of over-shoot constants and decay rates (without specifying a Lyapunov function).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Scalability, conditioning, prior", "weight": 1.0} -->

Hence, in case of unstable/marginally-stable systems or physical priors on model parameters, identifying a state space model has benefits. On the other hand, the direct identification of multi-step predictors allows to encode priors in terms of open-loop stability. For long horizons, multi-step predictors can provide better accuracy (cf., \[27, Thm. 1\]) at the cost of an increased complexity.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Impact of noise or disturbances on identification", "weight": 1.0} -->

The state space identification problem becomes simpler if we assume noise-free state measurements (cf. Cor. 1). On the other hand, the identification of multi-step predictors (Lemma 2) for long horizons ($k \gg 1$) simplifies if only measurement noise is present. For comparison, early MPC approaches based on impulse responses, e.g. dynamic matrix control, are restricted to "disturbances on the output". OBFs, a structured parametrization of, also allow for a simple identification under measurement noise. The identification of multi-step predictors is also related to the (implicit) data-driven models based on Hankel matrices, which typically also consider noisy output measurements without disturbances. A corresponding MLE with an ellipsoidal confidence bound was recently derived, which is also applicable to unbiased impulse response estimation \[22, Sec. 6\]. In particular, this approach also considers only output measurement noise without disturbances, the MLE is nonlinear including non-diagonal weights to account for cross correlation, which require prior knowledge of $G_{0,k}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Impact of noise or disturbances on identification", "weight": 1.0} -->

In \[29, Sec. 3.4\], a multi-step predictor subject to both noisy measurements and disturbances is identified using simple a least-squares estimate or the MLE, however, without deriving corresponding error bounds.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Impact of noise or disturbances on identification", "weight": 1.0} -->

We note that by using non-overlapping data-segments (structured in a page matrix), the cross correlation in Lemma 2 can be removed. For the special case of state space models, this corresponds to skipping every second measurement. In both parametrizations, the resulting uncorrelated residuals allow for a simple least-squares estimate.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Robust identification methods", "weight": 1.0} -->

The challenge inherent in MLE with correlated disturbances can also be avoided by considering robust identification methods. In particular, given a compact bound on the disturbances, set-membership estimation can be used to identify the non-falsified set that contains the true parameters, which is frequently used in robust adaptive MPC formulations. In particular, the approaches in \[12, Sec. 5.4\] and are applicable to both noisy measurements and disturbances; \[12, Cor. 3\] provides convergence results for fixed complexity estimates; and multi-step predictors (II-C) are explicitly considered. Note that most of the discussion in this paper regarding predictive control based on multi-step predictors equally applies to such a robust setup.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Input experiment design", "weight": 1.0} -->

The derived estimation bounds are such that collecting more (informative) data reduces the parametric uncertainty. A related problem is choosing the probing input signal $u_{\lbrack 0,{T - 1}\rbrack}$, which is studied in dual control or optimal experiment design. Given, e.g., Corollary 1, a natural approach is to ensure a lower bound on the persistence of excitation, i.e., ${\sum_{k = 0}^{T - 1}{\Phi_{k}^{\top}{\overset{\sim}{\Sigma}}_{w}^{- 1}\Phi_{k}}} \succeq {\beta I}$, given a rough model description. This issue is, e.g., addressed, which introduce conservatism due to convex relaxations, and only obtain approximations or require more complex robust propagation methods \[12, Sec 3.4\].

<!-- chunk {"id": "body-0025", "role": "body", "section": "Input experiment design", "weight": 1.0} -->

On the other hand, if the problem is addressed for multi-step predictors with only measurement noise, the variance can be deterministically predicted, which is, e.g., exploited.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Data-driven predictive control with parametric uncertainty", "weight": 1.0} -->

In the following, we revisit the stochastic optimal control problem (Sec. II) given the uncertain parameter estimates (Sec. III). To this end, we use the concept of robustness in probability, i.e., we consider ${\overset{\sim}{\theta}}_{k} \in \Theta_{\delta,k}$, $\delta > p$ (Lemma 2) robustly and enforce the chance constraints (2b) with a larger probability $\overset{\sim}{p} = {p/\delta} \in {(p,1)}$ (cf. \[44, Lemma V.3\]). We first focus on the state space model (Sec. IV-A) and then the multi-step predictors (Sec. IV-B). Finally, we discuss related work (Sec. IV-C) and contrast the results (Sec. IV-D).

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-A State space model", "weight": 1.0} -->

The predicted states are Gaussian $x_{k} \sim {\mathcal{N}{({\overline{x}}_{k},\Sigma_{x,k})}}$ (Sec. II), however, ${\overline{x}}_{k}$ and $\Sigma_{x,k}$ depend on the uncertain parameters $\theta_{1} = {{vec}\left( {\lbrack A,B\rbrack} \right)}$. Conceptually, we can solve Problem (II-A) using the following problem

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-A State space model", "weight": 1.0} -->

We briefly mention standard approaches from the MPC literature to compute a feasible (but suboptimal) solution to (IV-A). By ignoring the time-invariance of $\theta$, an upper bound for $\Sigma_{x,k}$ can be computed offline(!) using semi-definite programs (SDP), compare, e.g., \[40, Lemma 4.1, Thm. 4.2\],. Determining the reachable set for the mean ${\overline{x}}_{k}$ is addressed in tube-based MPC formulations for multiplicative/parametric uncertainty, \[7, Sec. 5.5\]. These approaches use a fixed parametrization (polytopes/ellipses) and provide sufficient conditions for an over-approximation of the reachable set. The size of this "tube/funnel" depends on the nominal input $u_{\lbrack 0,{N - 1}\rbrack}$ and is computed by adding linear/conic constraints over the prediction horizon.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-B Multi-step predictors", "weight": 1.0} -->

The following lemma shows how to enforce the chance constraints (2b) despite the parametric uncertainty.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-C Existing approaches using multi-step predictor bounds", "weight": 1.0} -->

In the following, we detail some approaches from the literature that, similar to Lemma 3, directly exploit parametric error bounds on the multi-step predictor.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Impulse response models", "weight": 1.0} -->

Early MPC implementations, especially in process control, are focused on impulse/step response models. Corresponding robust designs for FIR models with parametric uncertainty have also been derived using $\min - \max$ problems. By additionally considering set-membership estimation to identify the parametric error, a robust data-driven/adaptive MPC for FIR models is derived. For a more general parametrization with OBFs, and assuming only output measurement noise, robust/chance constraints under parametric uncertainty can also be enforced without conservatism. Notably, the parameter dimension with OBF can be significantly smaller, which reduces the computational complexity of the vertex enumeration.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Data-driven/enabled predictive control", "weight": 1.0} -->

The direct identification of multi-step predictors (II-C) has already been proposed in SPC. More recently, a variation of this approach known as data-driven/enabled predictive control has received significant attention. The basic idea is to specify an implicit model by stacking the measured data in a Hankel matrix, which is directly used within the optimization problem, instead of the usual sequential model identification and predictive control. In, it is shown that this implicit model also allows for simple reformulations of the $\min - \max$/distributionally-robust problem, similar to Lemma 3. In a related result, provide an MLE with simple bounds on the prediction. Notably, most of these results focus on measurement noise instead of disturbances, compare the discussion in Section III-C on system identification. When comparing data-driven/enabled predictive control approaches with standard model-based MPC, we note that the difference is not only attributable to the fact that a direct data-driven design is used (cf. for a detailed discussion on potential benefits); but also due to the fact that multi-step predictors are (implicitly) specified.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Set-membership estimation", "weight": 1.0} -->

In, set-membership estimation is used for multi-step predictors of the form (II-C). These approaches consider polytopic bounded noise and disturbances, resulting in polytopic sets ${\overset{\sim}{\theta}}_{k} \in \Theta_{\delta,k}$. Prediction bounds can then be directly obtained with linear inequality constraints (cf. ), which are guaranteed to be less conservative than corresponding bounds from a state space model \[27, Thm. 1\]. In contrast to Problem, the resulting MPC approaches over-approximate the prediction error with a constant bound to allow for simpler robust MPC methods and ensure recursive feasibility.

<!-- chunk {"id": "body-0034", "role": "body", "section": "System level synthesis (SLS)", "weight": 1.0} -->

SLS is a method to jointly optimize over feedback policies by parametrizing the problem using the (closed-loop) multi-step predictors $G_{u}$,$G_{0}$, $G_{w}$, which are called system responses, compare also the Input-Output Parametrization (IOP). In, multi-step predictors are directly identified and a simple constraint tightening, similar to Lemma 3, is obtained. In, the authors consider parametric errors in the state space formulation and then (partially) over-approximate it with a parametric uncertainty on the multi-step predictors to allow for a similarly simple robustification. Specifically, similar to Lemma 3, the constraint tightening in \[30, Equ. \] is proportional to a weighted norm of $\begin{bmatrix}

<!-- chunk {"id": "body-0035", "role": "body", "section": "Complexity and conservatism", "weight": 1.0} -->

For both model parametrizations, the considered derivation (Sec. IV-A/IV-B) introduces conservatism: a) separately bounding the variance and mean (which allows for a pre-computation of the variance related terms); b) using ${{Prob}\left\lbrack {{\overset{\sim}{\theta}}_{k} \in \Theta_{\delta,k}} \right\rbrack} \geq \delta$ (Lemma 2) instead of directly working with the distribution $\theta_{k} \in {\mathcal{N}{({\hat{\theta}}_{k},\Sigma_{\theta,k})}}$. Apart from this simplification, the derivation in Lemma 3 is tight. Another major benefit of Problem is its simplicity, i.e.,

<!-- chunk {"id": "body-0036", "role": "body", "section": "Complexity and conservatism", "weight": 1.0} -->

The probability level is increased with $\overset{\sim}{p} > p$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Complexity and conservatism", "weight": 1.0} -->

Regarding the computational complexity, the additional vector-norm in the constraint tightening results in second-order cone constraints. In case of polytopic parameter sets $\Theta_{\delta,k}$, a similar derivation results in a linearly constrained QP.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Complexity and conservatism", "weight": 1.0} -->

Considering the state space problem (IV-A), standard tube-based approaches to robustly account for parametric uncertainty (cf. ) also result in a QP subject to linear or second-order-cone constraints, depending if the set $\Theta$ is a polytope or ellipsoid. Notably, these approaches retain the sparsity structure. Tube-based methods require an additional offline step to design a suitable polytope/ellipsoid for the tube parametrization. Considering specifically the polytopic setting, a more complex polytope may reduce the conservatism but significantly increases the computational complexity (cf. \[7, Tab. 5.2\]), thus resulting in a non-trivial offline tuning problem. In addition, there exist degrees of freedom in the tube propagation that require a trade-off between conservatism and computational complexity (cf. \[11, Tab. 1\]). The sequential nature of the tube-propagation with its fixed parametrization can result in significant conservatism, which is difficult to quantify a-priori.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Complexity and conservatism", "weight": 1.0} -->

Less conservative/tight reachability bounds for state space models with parametric uncertainty require more sophisticated robust control tools, e.g., integral quadratic constraints. However, exploiting such tools in MPC is part of ongoing research.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Receding horizon implementation", "weight": 1.0} -->

One of the core principles of MPC is generating feedback by repeatedly solving open-loop optimization problems. Thus, recursive feasibility is of paramount importance, which can be ensured with well-established methods for state space formulations. For the following discussion on recursive feasibility, we restrict ourselves to the robust setting, as the unbounded disturbances in stochastic MPC require extra care. A crucial feature of the sequential disturbance propagation in tube-based MPC (cf. ) is the fact that recursive feasibility directly holds, assuming a proper parametrization and terminal set constraint. On the other hand, directly utilizing the multi-step predictor bounds (cf. Lemma 3), does in general not ensure recursive feasibility. This issue can be addressed using: shrinking/adaptive horizons or a multi-rate/multi-step implementations; intersecting different over-approximations of the reachable set; considering FIR/OBF models (cf. also Volterra series ).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Receding horizon implementation", "weight": 1.0} -->

This issue arises partially due to incompatible models, e.g., ${{\hat{G}}_{0,k}{\hat{G}}_{0,k}} \neq {\hat{G}}_{0,{2k}}$, and has similarities to the known problems associated with move-blocking MPC. Due to the different closed-loop implementation, it is not a-priori clear if the reduced open-loop conservatism of multi-step predictors (Sec. IV-B) results in improved closed-loop performance.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Input-output (IO) models", "weight": 1.0} -->

Hence, a noisy state measurement ${\overset{\sim}{x}}_{k} = {x_{k} + \epsilon_{k}}$ is directly available with the correlated(!) noise $\epsilon_{k} = {(\eta_{\lbrack{k - \nu},{k - 1}\rbrack},0_{{m\nu} \times 1})}$. The correlation requires a modification of the MLE (Sec. III), cf.. The MLE can also be directly applied to noisy output measurements using a Kalman filter. The fact that the resulting state space model is not necessarily minimal can complicate the offline design required in tube-based state space approaches. On the other hand, a minimal state space representation is not directly relevant for multi-step predictors and most of these approaches consider the IO setting. It is tempting to distinguish "standard" MPC schemes and more recent "data-driven" MPC methods in terms of input-state vs. IO setting.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Input-output (IO) models", "weight": 1.0} -->

However, based on the exposition in this paper, we postulate that a major difference is the model parametrization: sequential state space models vs. (implicit) direct multi-step predictors.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Nonlinear systems", "weight": 1.0} -->

While we focus on linear systems throughout the paper, similar conclusions can be drawn for nonlinear systems, where some of the differences become even more pronounced. Nonlinear multi-step predictors, i.e., $x_{i + k} = {f_{k}{(x_{i},u_{\lbrack i,{{i + k} - 1}\rbrack},w_{\lbrack i,{{i + k} - 1}\rbrack})}}$, can be identified using linearly parametrized models, e.g., Volterra series, or non-parametric approaches, e.g., kernel methods, analogous to nonlinear state-space models.^33^3The direct identification of the impulse response used in (II-C) can also be viewed as a non-parametric problem, especially for $N\rightarrow\infty$. The fact that such models do not require any conservative/complex disturbance propagation is even more critical in the nonlinear case. However, the complexity issues of multi-step predictors for large prediction horizons $N$ are also amplified for nonlinear problems.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Nonlinear systems", "weight": 1.0} -->

Furthermore, the difference in the prior information for state space models and multi-step predictors are more important in the nonlinear setting.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have provided a tutorial-style exposition of data-driven stochastic predictive control using state space models or multi-step predictors. In particular, we have investigated the challenges associated with parametric uncertainty in both model parametrizations. Tube-based methods for state space models need to trade-off computational complexity and conservatism, and require additional offline designs with various free design parameters. On the other hand, we derived simple (partially tight) bounds for multi-step predictors (Lemma 3), which do not suffer from similar conservatism. However, an a-priori comparison of the closed-loop performance in a receding horizon implementation is challenging due to the required modifications with multi-step predictors (e.g., multi-rate implementation). A direct comparison of the computational complexity is also difficult, as even within tube-based approaches the complexity can vary by orders of magnitude (cf. \[11, Tab. 1\]). Nonetheless, tube based approaches retain the sparse structure of the state space formulation and hence result in a reduced computational complexity for long horizons $N$ (cf. \[39, Sec. 3\]).

<!-- chunk {"id": "body-0047", "role": "body", "section": "Conclusion", "weight": 1.5} -->

scalability for long prediction horizons;

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion", "weight": 1.5} -->

different model priors and the prevalence of disturbances or noise in the parameter identification.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Open-issues", "weight": 1.0} -->

Lemma 3 could be improved by directly using $\theta_{k} \sim {\mathcal{N}{({\hat{\theta}}_{k},\Sigma_{\theta,k})}}$. Numerical comparisons regarding computational complexity and closed-loop performance would be beneficial. Given the respective benefits, unifying the parametrizations in a hybrid model structure is a promising research direction (cf., DiRec/DIRMO strategies ).
