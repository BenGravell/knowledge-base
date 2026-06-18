<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Scenario-based Stochastic MPC for Systems with Uncertain Dynamics

Topics include Optimal control, Model predictive control, Predictive control, Uncertainty, Probabilistic models, Accuracy, Sample complexity, Optimization, Control, Sampling.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Model Predictive Control is an extremely effective control method for systems with input and state constraints. Model Predictive Control performance heavily depends on the accuracy of the open-loop prediction. For systems with uncertainty this in turn depends on the information that is available about the properties of the model and disturbance uncertainties. Here we are interested in situations where such information is only available through realizations of the system trajectories. We propose a general scenario-based optimization framework for stochastic control of a linear system affected by additive disturbance, when the dynamics are only approximately known. The main contribution is in the derivation of an upper bound on the number of scenarios required to provide probabilistic guarantees on the quality of the solution to the deterministic scenario-based finite horizon optimal control problem. We provide a theoretical analysis of the sample complexity of the proposed method and demonstrate its performance on a simple simulation example. Since the proposed approach leverages sampling, it does not rely on the explicit knowledge of the model or disturbance distributions, making it applicable in a wide variety of contexts.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Model Predictive Control (MPC) has been effectively used to control complex dynamical systems in presence of input and state constraints, however, its performance is strongly affected by the accuracy of the prediction model. This aspect is critical when the system is too complex or too expensive to be accurately modelled and identification or learning algorithms are employed to obtain approximate plant dynamics. In the last decades, growing attention has been devoted to stochastic and robust MPC methods that can guarantee stability and constraint satisfaction in the presence of model uncertainties and exogenous disturbances.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Robust MPC (RMPC) classically considers min-max formulations that optimize the control actions with respect to the worst-case model uncertainty or disturbance realizations. These approaches rely on the assumption of bounded uncertainties and on the convexity of the optimization problem with respect to both control variables and uncertainties. The constraints need to be satisfied for all possible values of the uncertainties, an approach that can be conservative if additional information about the uncertainty and its distribution is available (for example, through samples). Furthermore, the computational burden of RMPC methods does not scale favorably with the model and disturbance complexities, sometimes requiring ad hoc simplifications of the constraints.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

When an appropriate probabilistic description of the model uncertainties is available, Stochastic MPC (SMPC) can be used to enforce state and input limitations in the form of chance constraints. Admitting a small level of constraint violation allows one to reduce the conservatism with respect to the RMPC solution, especially in the presence of rare events. Similarly to RMPC, computational tractability typically requires approximations or assumptions on the probability distributions.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

An alternative approach is provided by the class of randomized uncertainty methods. These approaches rely on sampling to obtain a deterministic reformulation of the chance constraint problem, without assumptions on the probability distribution of the uncertainties. A popular method is the so called scenario approach that, in its basic formulation, relies on the convexity of the optimization problem with respect to the decision variables to provide tight a-priori bounds on the number of samples required to guarantee the original chance constraint satisfaction. The idea of applying the scenario approach in a MPC framework has been explored, among others, for known linear time invariant deterministic models affected by additive disturbance, for parametric linear time invariant stochastic dynamics with general dependencies of the system on the parameter realization and for linear parameter varying dynamics. In a robust optimization problem is proposed for which the uncertainty bounds are computed via the scenario approach.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Building on these ideas, we propose a general, but tractable, scenario-based optimization framework for chance constrained stochastic MPC with linear uncertain dynamics. Unlike earlier approaches, the proposed work robustifies, in a probabilistic sense, the stochastic MPC against the model uncertainty related to the model dynamics. For uncertain linear time invariant systems, we provide a probabilistic upper bound on the number of samples required to achieved a prescribed probability of violation, leading to finite sample randomized algorithms to solve the stochastic control problem. Since the proposed approach leverages sampling, it does not rely on the explicit knowledge of the model and disturbance distributions and it does not require any specific assumption on the uncertainties, making it compatible with a wide variety of probabilistic identification algorithms.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rest of the paper is organized as follows. The problem formulation is described in Section II. Section III reviews earlier results in scenario MPC. In Section IV we derive an upper bound on the number of scenarios needed to achieve a prescribed violation probability level for the case of scenario MPC with uncertain dynamics. Section V provides a numerical example. Section VI concludes the paper.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Consider the discrete-time linear time invariant (LTI) system subject to additive disturbances

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

with state $x_{k} \in {\mathbb{R}}^{n}$, control input $u_{k} \in {\mathbb{R}}^{m}$ and disturbance $\eta_{k} \in {\mathbb{R}}^{n}$ distributed according to a (possibly unknown) probability measure ${\mathbb{P}}_{\eta}$ over the (possibly unknown and unbounded) support set $\mathcal{H} \subseteq {\mathbb{R}}^{n}$. We assume that the state is measurable, but that we do not have access to the true system dynamics. This is relevant in many engineering contexts where only an approximate model is available for the control task.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Here we summarize the knowledge we have about the system dynamics by considering an arbitrary parametrization of the system matrices $A = {A{(\vartheta)}}$ and $B = {B{(\vartheta)}}$ and by assuming a parameters distribution $\vartheta \sim {\mathbb{P}}_{\vartheta}$ defined over the (possibly unknown and unbounded) support set $\Theta$. We further assume that the true system dynamics are within this parametrized class, i.e., there exists $\overline{\vartheta} \in \Theta$ such that $\overline{A} = {A{(\overline{\vartheta})}}$ and $\overline{B} = {B{(\overline{\vartheta})}}$. As it will be evident in the next sections, our approach does not require explicit knowledge of the parameter distribution ${\mathbb{P}}_{\vartheta}$ as long as i.i.d. samples from the distribution are available.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

An example where the parameter distribution is not explicitly known is provided in Section V.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Epistemic uncertainty on the system dynamics (i.e. the value of $\vartheta$ for the true system matrices are unknown);

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Stochastic uncertainty due to the presence of the disturbance $\eta_{k}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

The epistemic uncertainty is often treated in the literature by selecting an estimate using regression, then using this estimate in a problem formulation that addresses the stochastic uncertainty. We argue, however, this can be detrimental for performance whenever there is a significant mismatch between the model corresponding to the parameter estimate and the true system dynamics. We aim, instead, for a problem formulation that can provide state and input constraint satisfaction with respect to both the epistemic and the stochastic uncertainty.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Our objective is to design a receding horizon predictive controller that minimizes a given cost function while satisfying probabilistic state and input constraints over a finite horizon $T$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

where ${\overline{x}}_{\tau}$ is the initial condition at time $\tau$,

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

The probabilistic constraint function ${f\left( {\mathbf{x}}_{+},{\mathbf{u}} \right)}:{{\mathbb{R}}^{{({n + m})}T}\rightarrow{\mathbb{R}}}$ can encode constraints that need to be satisfied with probabilities of violation $\varepsilon_{1} \in {\lbrack 0,1\rbrack}$ and $\varepsilon_{2} \in {\lbrack 0,1\rbrack}$. These can be either application specific requirements or design parameters that trade off performance for constraint satisfaction. Unlike robust constraint satisfaction, chance constraints can allow some violations to obtain a larger feasible set and a lower cost. This is a reasonable assumption in many applications where, by specification, limited constraint violations are allowed.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Solving over arbitrary control policies is, in general, an intractable problem. To maintain tractability, one can restrict attention to open-loop policies $u_{\tau},\ldots,u_{{\tau + T} - 1}$ that are trivially causal; this, however, can be too conservative, as it does not allow the input to exploit the information about the future disturbance that will be available when the decision is executed. A popular alternative is to consider causal state-affine policies that can be reformulated as a disturbance-affine policy to maintain computational tractability. Given the assumption of fully measurable state, the disturbance $\eta_{k}$ at each time step can be reconstructed according to

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

The resulting disturbance-affine policy can be written as

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

where ${\mathbf{γ}}_{k} \in {\mathbb{R}}^{m}$ and $\lambda_{k} \in {\mathbb{R}}^{m \times n}$. Note that this class of policies is by construction causal, as it enforces the requirement that the control input at time $\tau + k$ is only affected by the reconstructed disturbances up to time ${\tau + k} - 1$. To obtain a more compact reformulation of the MPC Problem, we can write the system dynamics in matrix form

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Likewise, the input can be parametrized in matrix form as

<!-- chunk {"id": "body-0023", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

The solution of the stochastic FHOC Problem still poses some major challenges. Formulating the chance constraint in a tractable way is only possible under specific assumptions on the disturbance distributions.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 1 (Convexity)", "weight": 1.0} -->

The cost function $\overset{\sim}{J}(\Gamma,\Lambda,\vartheta,{\mathbf{η}})$ and the constraint function $\overset{\sim}{f}(\Gamma,\Lambda,\vartheta,{\mathbf{η}})$ are convex in the optimization variables $\Gamma$ and $\Lambda$ for almost every ${(\vartheta,{\mathbf{η}})} \in {\Theta \times \mathcal{H}^{T}}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 1 (Convexity)", "weight": 1.0} -->

Note that, since $(\Gamma,\Lambda)$ parameterize the state and input trajectories $({\mathbf{x}}_{+},{\mathbf{u}})$ through an affine transformation, it is sufficient to require the cost and constraint function to be convex in $({\mathbf{x}}_{+},{\mathbf{u}})$ to satisfy Assumption 1. ‣ II Problem formulation ‣ Scenario-based Stochastic MPC for systems with uncertain dynamics").

<!-- chunk {"id": "body-0026", "role": "body", "section": "Uncertain Dynamics Scenario-based Stochastic MPC", "weight": 1.0} -->

In presence of uncertainty on the system dynamics, we aim for a problem formulation that can provide state and input constraint satisfaction with respect to both the epistemic and the stochastic uncertainty. In particular, we want to extend the finite sample result of the previous section to the case where the epistemic uncertainty on the system dynamics is described by a probability distribution on the parameters $\vartheta$, as is common for many probabilistic identification algorithms.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-A Scenario program", "weight": 1.0} -->

We can now state the finite sample result that extends Theorem 2 to include the robustness against the model uncertainty.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-B Scenarios construction", "weight": 1.0} -->

We now turn to the question of how to obtain the samples from the joint distribution ${\mathbb{P}}_{\vartheta,\eta}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-B Scenarios construction", "weight": 1.0} -->

If the distributions ${\mathbb{P}}_{\vartheta}$ and ${\mathbb{P}}_{\eta}$ are available, we can directly generate samples from the joint distribution. If not, we can generate samples from historical data.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-B Scenarios construction", "weight": 1.0} -->

When identification or learning algorithms are employed to obtain a probabilistic description of the plant dynamics, historical data are used to produce distributions of models or directly samples from such distributions. An example of a procedure to generate samples of the dynamics based on bootstrapping is given in Section V.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-B Scenarios construction", "weight": 1.0} -->

Having obtained samples of the system dynamics, one can generate the corresponding samples $\mathbf{η}$ using more historical data. To maintain the independency requirement necessary for Theorem 3, we require access to $N$ i.i.d. historical state-input trajectory samples, each of length $T$ (the prediction horizon). We denote these by ${\{{\mathbf{x}}^{i},{\mathbf{u}}^{i}\}}_{i = 1}^{N}$ with ${\mathbf{x}}^{i} = {\{ x_{k}^{i}\}}_{k = 0}^{T}$, ${\mathbf{u}}^{i} = {\{ u_{k}^{i}\}}_{k = 0}^{T - 1}$. With these ingredients one can generate the required scenarios using the following algorithm.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Algorithm 4 (Sequential sampling for Uncertain Dynamics Scenario-based MPC)", "weight": 1.0} -->

Sample $\vartheta^{i} \sim {\mathbb{P}}_{\vartheta}$ from the parameters distribution;

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-C Computational complexity", "weight": 1.0} -->

Following, the number of scenarios $N$ required to satisfy can be explicitly upper bounded by

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-C Computational complexity", "weight": 1.0} -->

We can observe that $\overset{\sim}{N}$ grows logarithmically with $\frac{1}{\beta}$ and linearly in $d$ and in $\frac{1}{\varepsilon_{1}\varepsilon_{2}}$. For the disturbance-affine control policy presented in Section II, the number of optimization variables $d = {{mT} + {mn\frac{{({T - 1})}T}{2}}}$ grows linearly with the state and input dimensions and quadratically with the prediction horizon length $T$. Even though the asymptotic growth is modest, practically applying Theorem 3 would require solving a large program and access to large number of historical system trajectories to generate the samples of $\mathbf{η}$ using Algorithm 4. ‣ IV-B Scenarios construction ‣ IV Uncertain Dynamics Scenario-based Stochastic MPC ‣ Scenario-based Stochastic MPC for systems with uncertain dynamics").

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-C Computational complexity", "weight": 1.0} -->

The number of required scenarios can be decreased by allowing larger probabilities of violations or by reducing the number of optimization variable, e.g. limiting $\Lambda$ to have non zero elements only on the sub-diagonal to achieve linear growth in the prediction horizon length $T$. Nonetheless, empirically good performance can be obtained even for small number of scenarios, well below the minimum number required by the theoretical result of Theorem 3, as seen in the numerical example below.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Numerical example", "weight": 1.0} -->

We assume that we have access to an identification dataset $\mathcal{D}_{Id}$ of size $L_{Id} = 50$ comprising ${\{{\mathbf{x}},{\mathbf{u}},{\mathbf{x}}_{+}\}}^{j}$, ${j = {1,\ldots,L_{Id}}},$ collected by applying a random input sequence $u_{k} \sim {\mathcal{U}{\lbrack{- 0.5};{+ 0.5}\rbrack}}$, $k = {1,\ldots,L_{Id}}$, to the true dynamical system starting from a random initial condition $x_{0} \sim {\mathcal{U}{\lbrack{- 0.5};{+ 0.5}\rbrack}}$. The small size of this dataset can generally represent a poorly designed identification experiment, with either a weakly exciting signal, correlated measurements or low signal-to-noise ratio.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Numerical example", "weight": 1.0} -->

Using this data we generate $N$ samples of $\vartheta^{i}$ using the following bootstrapping algorithm.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Algorithm 5 (Empirical Bootstrap)", "weight": 1.0} -->

Use the Least Squares method to obtain one point estimate of the parameter ${\hat{\vartheta}}_{BS}^{i}$ for each $\mathcal{D}_{BS}^{i}$, $i = {1,\ldots,N}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Algorithm 5 (Empirical Bootstrap)", "weight": 1.0} -->

We also assume availability of a dataset $\mathcal{D}_{Hist}$ comprising $N$ historical trajectory data of length $T$ to obtain samples of the disturbance using Algorithm 4. ‣ IV-B Scenarios construction ‣ IV Uncertain Dynamics Scenario-based Stochastic MPC ‣ Scenario-based Stochastic MPC for systems with uncertain dynamics").

<!-- chunk {"id": "body-0040", "role": "body", "section": "Algorithm 5 (Empirical Bootstrap)", "weight": 1.0} -->

Uncertain Dynamics Scenario MPC (UD-SMPC): it relies on the solution of the deterministic SP, using the bootstrap Algorithm 5. ‣ V Numerical example ‣ Scenario-based Stochastic MPC for systems with uncertain dynamics") to generate samples of the uncertain dynamics from the given dataset $\mathcal{D}_{Id}$;

<!-- chunk {"id": "body-0041", "role": "body", "section": "Algorithm 5 (Empirical Bootstrap)", "weight": 1.0} -->

Least Squares Scenario MPC (LS-SMPC): it relies on the solution of the deterministic SP, considering as the deterministic model the one obtained from the identification dataset $\mathcal{D}_{Id}$ by Least Squares regression;

<!-- chunk {"id": "body-0042", "role": "body", "section": "Algorithm 5 (Empirical Bootstrap)", "weight": 1.0} -->

Ground Truth Scenario MPC (GT-SMPC): it relies on the solution of the deterministic SP, using the ground truth model. This is unrealistic in practice and it is provided only for the sake of comparison as an ideal baseline.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Algorithm 5 (Empirical Bootstrap)", "weight": 1.0} -->

To obtain a simple comparison we will also consider only the constant constraint ${f\left( {\mathbf{x}}_{+},{\mathbf{u}} \right)} = {\max{({\lbrack{0.5 - {\mathbf{x}}_{+}^{}},{- {\mathbf{x}}_{+}^{}}\rbrack}^{\top})}} \leq 0$, i.e. we require the first and the second elements of the state to be greater than $0.5$ and $0$ respectively. Theorem 3 requires SP to be always feasible; we deal with this issue by introducing a slack formulation for the chance constraint satisfaction ${f\left( {\mathbf{x}}_{+},{\mathbf{u}} \right)} \leq \sigma$, with $\sigma$ added as a linear penalty in the cost function with a weight of $10^{5}$, to avoid violating the constraint whenever possible.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-A Open-loop analysis", "weight": 1.0} -->

To show how the inclusion of model uncertainty improves the reliability of the open-loop prediction we compare the three methods by computing the empirical violation probability over $1000$ realizations of the true system $T$-steps trajectory. We repeat this for $400$ Monte Carlo (MC) realizations of $\mathcal{D}_{Id}$ and $\mathcal{D}_{Hist}$. The number of scenarios is determined by setting $\beta = 10^{- 5}$ and $d = 26$, $25$ for the disturbance-affine policy and one for the slack variable $\sigma$. Following, the number of scenarios needed to attain $\varepsilon_{1} = 0.1$ and $\varepsilon_{2} = 0.3$ for UD-SMPC is $1776$, whereas, following the number of scenarios needed to attain $\varepsilon_{1} = 0.1$, for the other two methods is $523$. Figure 1 shows the cumulative distribution of the empirical probability of violation.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-A Open-loop analysis", "weight": 1.0} -->

For approximately $12\%$ of the datasets MC realizations, the LS-SMPC optimal policy results in a probability of violation greater than the specified $\varepsilon_{1} = 0.1$. This issue is related to the neglected model uncertainty and cannot be dealt with by simply increasing the number of scenarios. UD-SMPC robustifies against the epistemic uncertainty by sampling the uncertain dynamics, resulting in lower violation probabilities.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-B Closed-loop analysis", "weight": 1.0} -->

We compare the MPC $10$-steps closed-loop cost and number of violations of the three methods for equal number of scenarios $N = {\{ 2^{6},2^{7},2^{8},2^{9},2^{10},2^{11}\}}$. We repeat this for $400$ MC realizations of $\mathcal{D}_{Id}$ and $\mathcal{D}_{Hist}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-B Closed-loop analysis", "weight": 1.0} -->

the receding horizon nature of MPC, that inherently provides a certain degree of robustness;

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-B Closed-loop analysis", "weight": 1.0} -->

the fact that problem we are trying to solve is not necessarily fully supported, hence our estimates of $N$ are not tight;

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-B Closed-loop analysis", "weight": 1.0} -->

the additional conservatism due to the use of Markov's inequality in the proof of Theorem 3.

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-B Closed-loop analysis", "weight": 1.0} -->

In Figure 4 we can observe that the closed-loop violations decrease with larger number of scenarios. This in turns induces an increase in the closed-loop cost as shown in Figure 2 and Figure 3. By comparing UD-SMPC and LS-SMPC performance, we can see that explicitly considering the uncertainty in the dynamics with UD-SMPC allows us to obtain a more robust controller, leading to fewer closed-loop violations and less outliers in the cost function.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Conclusions and future work", "weight": 1.0} -->

We developed a general scenario-based optimization framework for the solution of chance constrained stochastic MPC with uncertain dynamics. We extended previous work in scenario-based stochastic MPC providing a principled way of dealing with the epistemic uncertainty related to the system dynamics. Unlike stochastic and robust MPC approaches that typically require additional assumptions or over-approximations of the chance constraints, the proposed method allows for arbitrary distributions of the stochastic parameters. Moreover, the explicit distributions of the disturbances and of the model parametric uncertainties are not required, as long as samples are available.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Conclusions and future work", "weight": 1.0} -->

Interesting future work directions include the extension of the proposed approach to an output feedback setup and the adaptation of the proposed scheme to an online learning dual formulation setting, in which at each step there is a trade-off between exploration and exploitation. One of the main aspects that remains to be addressed is the recursive (probabilistic) feasibility through the definition of safe probabilistic terminal sets. This could improve the applicability of the proposed method, making it suitable for a wide range of safety-critical learning-based applications.
