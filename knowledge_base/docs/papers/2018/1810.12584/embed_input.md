<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning-based Predictive Control for Linear Systems: A Unitary Approach

Topics include Model predictive control, Predictive control, Robustness, Uncertainty, Datasets, Control, Learning, Learning-based model predictive control, Constraint satisfaction, Robust control.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A comprehensive approach addressing identification and control for learningbased Model Predictive Control (MPC) for linear systems is presented. The design technique yields a data-driven MPC law, based on a dataset collected from the working plant. The method is indirect, i.e. it relies on a model learning phase and a model-based control design one, devised in an integrated manner. In the model learning phase, a twofold outcome is achieved: first, different optimal p-steps ahead prediction models are obtained, to be used in the MPC cost function; secondly, a perturbed state-space model is derived, to be used for robust constraint satisfaction. Resorting to Set Membership techniques, a characterization of the bounded model uncertainties is obtained, which is a key feature for a successful application of the robust control algorithm. In the control design phase, a robust MPC law is proposed, able to track piece-wise constant reference signals, with guaranteed recursive feasibility and convergence properties. The controller embeds multistep predictors in the cost function, it ensures robust constraints satisfaction thanks to the learnt uncertainty model, and it can deal with possibly unfeasible reference values. The proposed approach is finally tested in a numerical example.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The idea of combining identification and control for efficient and reliable control systems design, starting from data collected on the plant, has a long standing history, see the survey paper. Indirect approaches are characterized by an initial phase aimed at estimating the model of the plant, while a following one concerns the model-based control synthesis. In this framework different solutions have been proposed, as thoroughly discussed. Specifically, in *dual* algorithms, parameter estimation and control design are posed as a combined problem, in *optimal experiment design* methods, identification procedures suitably tailored for the adopted control synthesis algorithm are developed, while in *robust* algorithms the model is estimated together with uncertainty bounds, to be properly used in the control synthesis. With the cheap availability of large data-sets and the advent of more and more powerful identification and learning techniques, recent years have seen a renaissance of research activity in this area, and in particular on robust methods. From the learning side, new and powerful Set Membership (SM) identification methods, see, have been developed to identify a model for the system with guaranteed prediction error bounds, suitable for robust control design.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

From the control side, MPC algorithms, robust with respect to model disturbances, have been studied from several standpoints, and considering different characterizations of the model and its associated uncertainty, see e.g.. Among the most recent contributions in learning-based control, we recall the dual MPC algorithm described in for systems characterized by probabilistic parametric uncertainty and process noise, and the MPC method developed in guaranteeing both robustness and performance by considering different models of the system. Another recent contribution is reported, where an MPC guaranteeing stability has been developed for nonlinear models estimated with the learning method proposed.\In this paper we present a unitary approach to learning-based robust MPC, where we take a joint perspective on the learning and the control design phases. The system generating the data is linear and time-invariant, with unknown order, subject to process disturbance and measurement noise. In the learning phase, we identify with SM different models, together with their uncertainty bounds.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Specifically, we compute from data $p$-steps-ahead independent prediction models, $p \in {\lbrack 0,\overline{p}\rbrack}$, used to compute the future evolution of the system outputs over the prediction horizon $\overline{p}$ considered in the MPC cost function. The use of different models, as previously suggested, allows one to achieve good prediction accuracy at different steps ahead and to have non-conservative bounds on the process disturbance. In addition to the independent $\overline{p}$ models, we also estimate a perturbed state-space model, together with its disturbance bounds, subsequently used in the MPC design for enforcing state, input and output constraints, as well as the robust stability property according to the well known tube-based approach, see. The robust MPC controller is designed, following the approach proposed, for tracking piece-wise constant reference signals, with guaranteed recursive feasibility and convergence properties. A numerical example is finally reported. Preliminary results on the learning and control synthesis algorithms developed in this paper have been reported, and.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose a novel offline method to learn the uncertainty model to be used in the control design phase, together with a new MPC design to deal with the tracking of (possibly infeasible) piecewise constant reference signals, we derive the full proofs of all the theoretical results concerning learning and control design, and we merge our preliminary work into a unitary and holistic vision of the interplay between learning and control for MPC.\The paper is organized as follows: in Section 2 the problem is stated and the proposed approach is described. In Section 3 the SM identification algorithm is presented, Section 4 describes the robust MPC control scheme design, followed by a numerical example in Section 5 and a concluding discussion in Section 6.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Problem formulation: a unitary approach to learning-based MPC", "weight": 1.0} -->

We consider a discrete-time, linear time-invariant (LTI), single-input/single-output (SISO) system of order $n$ described by the following autoregressive exogenous (ARX) structure ($\cdot^{T}$ is the matrix transpose operator): where $z$ is the output, $v$ an additive process disturbance, $y$ the output measure, and $d$ an additive measurement noise. For a given integer $p \geq 1$, the regressor ${\varphi_{z}^{(p)}{(k)}} \in {\mathbb{R}}^{{{2n} + p} - 1}$ is defined as: here $u$ is the system input. In, ${\overline{\theta}}^{} \in {\mathbb{R}}^{{{2n} + p} - 1}$ is a vector of unknown system parameters. The value of $n$ is not known a priori as well.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Remark 1", "weight": 1.0} -->

a) The problem is formulated in the SISO setting for the sake of clarity and notational simplicity.\b) Our working assumptions are rather common in theoretical contributions concerned with system identification, when an unknown-but-bounded assumption is considered for process and measurement disturbances. They are valid in many practical applications as well: a characterization of the available sensors can be used to compute the worst-case measurement error bound $\overline{d}$, while for process disturbances we just assume boundedness, without necessarily knowing the worst-case value $\overline{v}$. Indeed, the worst-case effect of the signal $v{(k)}$ on the system output will be estimated as part of the uncertainty model in our approach.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Remark 1", "weight": 1.0} -->

In this paper we adopt an indirect approach to learning-based control synthesis, i.e., based on a sequence of model learning and model-based design phases.\The learning phase (Section 3) has a twofold role: Identifying optimal (in the sense specified below) independent $p$-steps ahead prediction models of the type where $\hat{z}{({k + p})}$ is the predicted output at time $k + p$, and the model regressor $\varphi_{y}^{(p)}{(k)}$ is defined as with $o$ being the order of the prediction model. Models are also defined "multi-step" since they directly provide the output prediction $p$ steps ahead, without integrating an underlying simulation model. These models, for all $p \in {\lbrack 1,\overline{p}\rbrack}$, will be used in the MPC cost definition, thanks to their optimal predictive properties, tailored on specific prediction lengths.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Identifying a state-space model of the type where $X$ is the system state, $w$ is the process disturbance, and $A,B_{1},M_{1},C$ are the system matrices. One of the contributions of this paper consists also of a novel approach for obtaining a non-conservative bound $\overline{w}$ on the amplitude of the process disturbance $w{(t)}$ from experimental data. This is fundamental, in a constrained robust design context, to limit the conservativeness of the resulting control approach.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Remark 1", "weight": 1.0} -->

In the control phase (Section 4), we propose a scheme, to be applied to the real system, that asymptotically steers the variable $z{(k)}$ towards the goal $z_{goal}$ and that guarantees the fulfillment of the following input and output constraints, for all $k \geq 0$. where $\mathbb{Z}$ is assumed convex. As already remarked, to this purpose (i) the multi-step prediction models are used for the definition of the cost function and (ii) the perturbed state-space model, with bounds $\overline{d}$ and $\overline{w}$ on $d{(t)}$ and $w{(t)}$, respectively, are used for constraint satisfaction.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Model structure and preliminary considerations", "weight": 1.0} -->

In MPC with horizon $\overline{p}$, at each step $k$ the predictions of variables $z{({k + p})}$, $p = {1,\ldots,\overline{p}}$ are needed. Many contributions on robust MPC in the literature assume that a model of the system in the form is available. A common, but quite conservative, setup is to consider ${d{(k)}} = {0,{\forall k}}$, and $C = I$, i.e. perfectly measurable state, and finally to assume a known bound $\overline{w}$ on the worst-case additive process disturbance, such that ${\|{w{(k)}}\|} \leq {\overline{w},{\forall k}}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Model structure and preliminary considerations", "weight": 1.0} -->

Such a model is then integrated forward in time to predict the state and output values at each future step $k + p$.\However to learn, from experimental data, a model of the form with *good prediction accuracy* at different steps ahead and with *non-conservative bounds* on the process disturbance is a complex task. The parameter identification problem is convex only when a 1-step prediction error method is used, which may return models with poor prediction accuracy over multiple future steps (i.e. poor simulation performance), see e.g.. On the other hand, the use of a cost function that penalizes the multi-step prediction error, or simulation error, yields a nonlinear program (NLP) in the parameters of the 1-step-ahead model, which, besides the possible trapping in local minima, makes it difficult to derive guaranteed disturbance bounds. Additionally, in practical applications the state might not be fully measured, the system order is not known, and measurement noise and process disturbances are present. These features make the identification problem even more challenging.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Model structure and preliminary considerations", "weight": 1.0} -->

To deal with these problems, the approach taken in this paper consists of learning a different (linear-in-the-parameters) multi-step prediction model for each value of $p \in {\lbrack 1,\overline{p}\rbrack}$. Besides, as discussed, directly using models in the MPC cost function, we will employ their corresponding worst-case error bounds to optimally compute the bound $\overline{w}$ in a state-space realization, employed to robustly guarantee stability and constraint satisfaction.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Model structure and preliminary considerations", "weight": 1.0} -->

The choice of a model structure of type is motivated by the fact that, integrating over time a model of type, the future system outputs are indeed affine in the regressor $\varphi_{y}^{(p)}{(k)}$, containing noise-corrupted output measurements: where ${\mathcal{V}^{(p)}{(k)}} = {\lbrack{v{(k)}},\ldots,{v{({{k + p} - 1})}}\rbrack}$ and ${\mathcal{D}^{(p)}{(k)}} = {\lbrack{d{(k)}},\ldots,{d{({{k + p} - 1})}}\rbrack}$ are the sequences of output disturbance and measurement noise, respectively, values from $k$ to ${k + p} - 1$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Model structure and preliminary considerations", "weight": 1.0} -->

The parameter vectors ${\overline{\theta}}^{(p)}$, ${\overline{\theta}}_{v}^{(p)}$ and ${\overline{\theta}}_{d}^{(p)}$ are polynomial functions of the true system parameters ${\overline{\theta}}^{}$ (possibly padded with zeros if the model order $o$ is strictly larger than the true system order $n$), readily obtained by recursion of. In our approach, we will consider instead a distinct parameter vector for each $p$, i.e. ${\hat{\theta}}^{(p)}$. A first advantage in doing so is the possibility to efficiently compute not only a nominal multi-step prediction model for each $p$, but also a *model set* which is tight (i.e. the smallest one compatibly with the available prior information and data), through a Set Membership (SM) identification approach.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Model structure and preliminary considerations", "weight": 1.0} -->

From such a model set, we can thus estimate a tight worst-case prediction error bound $\tau_{p}{({\hat{\theta}}^{(p)})}$ for any given multi-step predictor, i.e.: We term the bound $\tau_{p}{({\hat{\theta}}^{(p)})}$ *global*, since it holds for any regressor value $\varphi_{y}^{(p)}$ within a suitable compact set $\Phi^{(p)}$, introduced in the remainder. A second advantage in using the multi-step models is the possibility to rigorously define, and then efficiently compute, a model optimality criterion and related optimal models, which minimize the worst-case guaranteed prediction error.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Model structure and preliminary considerations", "weight": 1.0} -->

We describe next the considered data-set, followed by the learning approach. An important assumption throughout the paper is the following.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Assumption 2 can be easily satisfied in practice, on the basis of physical considerations on the system at hand and/or by estimating the system order from data.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Available data-set", "weight": 1.0} -->

For a given prediction step $p$, we denote with $\Phi^{(p)}$ the compact set containing all the possible regressor vectors $\varphi_{y}^{(p)}$, i.e., such that for each $p \in {\lbrack 1,\overline{p}\rbrack}$ The set $\Phi^{(p)}$ is not known explicitly in general, as it is a complicated set that depends on the system input and disturbance trajectories and initial conditions of interest. Its compactness is due to the fact that the system is asymptotically stable and its input belongs to a compact set (Assumption 1).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Available data-set", "weight": 1.0} -->

We can express our data-set as: The set ${\overset{\sim}{\mathcal{T}}}_{p}^{N_{p}}$ is countable and contained in its continuous counterpart $\mathcal{T}_{p}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Learning procedure", "weight": 1.0} -->

The proposed estimation procedure consists of the following steps: Define an optimality criterion to evaluate the model estimates and the corresponding optimal (i.e. minimal) error bound.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Learning procedure", "weight": 1.0} -->

Derive a procedure to estimate the optimal error bound.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Learning procedure", "weight": 1.0} -->

Based on the available data and the error bound estimate, build the set of all admissible model parameters (Feasible Parameter Set, FPS).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Learning procedure", "weight": 1.0} -->

Using the information summarized in the FPS, for any given model of the form compute the related guaranteed error bound $\tau_{p}$, see.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Learning procedure", "weight": 1.0} -->

Select a nominal model with minimal guaranteed error bound.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Optimal parameter set and optimal error bound", "weight": 1.0} -->

For any $p \in {\lbrack 1,\overline{p}\rbrack}$, consider a given value of ${\hat{\theta}}^{(p)}$. From and, the error between the true system output and the predicted one is, for all $k \in {\mathbb{Z}}$: Thus, from and we have: The quantity $\epsilon_{p}{(\cdot, \cdot, \cdot, \cdot)}$ accounts for the quality of the estimate ${\hat{\theta}}^{(p)}$, for possible model order mismatch, and for the disturbances $v$ and $d$. In view of Assumption 1, $\epsilon_{p}$ is bounded.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Optimal parameter set and optimal error bound", "weight": 1.0} -->

Moreover,: where ${\overline{\epsilon}}_{p}{({\hat{\theta}}^{(p)})}$ is the global error bound with respect to all possible regressors of interest and all feasible disturbance sequences in the compact set $\Phi^{(p)}$: We can now define the optimal parameter values (i.e. optimal models) as those that minimize the bound ${\overline{\epsilon}}_{p}{({\hat{\theta}}^{(p)})}$. As a technical assumption, we consider parameters within a compact set $\Omega^{(p)} \subset {\mathbb{R}}^{{{2o} + p} - 1}$. $\Omega^{(p)}$ can take into account application-specific prior information on the model parameters or, if no such information is available, it can be chosen as a large-enough set (e.g. by considering box constraints of $\pm 10^{15}$ on each element of the parameter vector).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Optimal parameter set and optimal error bound", "weight": 1.0} -->

This technical assumption allows us to use maximum and minimum operators instead of supremum and infimum.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Estimating the optimal error bound", "weight": 1.0} -->

The optimal models and optimal error bound cannot be computed in practice, since the solution to would imply the availability of an infinite number of data and the solution to an infinite-dimensional optimization program. However, we can compute an estimate ${\underset{¯}{\lambda}}_{p} \approx {\overline{\epsilon}}_{p}^{\ast}$ from the available experimental data, by solving the following linear program (LP): The following result shows that, under the considered working assumptions, the value of ${\underset{¯}{\lambda}}_{p}$ converges to the optimal one, ${\overline{\epsilon}}_{p}^{\ast}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Feasible Parameter Set", "weight": 1.0} -->

We exploit the estimated optimal error bound to construct the tightest set of parameter values consistent with all the prior information, i.e. the FPS $\Theta^{(p)}$: The set $\Theta^{(p)}$ is non-empty by construction, since under Assumption 4 we have (see and) that ${\overline{\Theta}}^{(p)} \subseteq \Theta^{(p)}$. If the FPS is bounded, it results in a polytope with at most $N_{p}$ faces. If it is unbounded, then this indicates that the available measured data are not informative enough to derive a bound on the worst-case model error, and that $N_{p}$ must be increased until a bounded FPS is obtained. This situation usually occurs when very few data points are used (e.g. $N_{p} < {{{2o} + p} - 1}$) or the preliminary experiments are not informative enough.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Error bound computation for a given model", "weight": 1.0} -->

Consider now a given parameter vector ${\hat{\theta}}^{(p)}$ and any ${\varphi_{y}^{(p)}{(k)}} \in \Phi^{(p)}$. From and it follows that In view of Assumption 4, the global worst-case prediction error bound for model ${\hat{\theta}}^{(p)}$ is then: This bound cannot be computed exactly with finite data under the considered assumptions, and its computation would be intractable also if the set $\Phi^{(p)}$ were known precisely. The complexity may be reduced only if additional assumptions are made, e.g. that $\Phi^{(p)}$ is a polytope, which however may result in a high conservativeness.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Selection of nominal multi-step models", "weight": 1.0} -->

The last step in the proposed estimation algorithm is to select a nominal multi-step model for each prediction step $p$. The most common approach is probably based on least-squares estimation: in this case the results of Section 3.3.4 can be applied to obtain an estimate of the resulting global error bound. Since our final goals are to employ the multi-step models in a robust MPC algorithm and estimate bound $\overline{w}$ for the perturbed model in a non-conservative manner, we rather seek the model that minimizes the worst-case error bound for each $p$ value.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Selection of nominal multi-step models", "weight": 1.0} -->

Specifically, considering that the tightest set that contains the optimal parameter values (i.e. with minimum error, see Section 3.3.1) is the FPS $\Theta^{(p)}$, we search within this set for a parameter value that minimizes the resulting bound ${\hat{\tau}}_{p}{({\hat{\theta}}^{(p)})}$: The resulting nominal model reads and the associated error bound estimate is ${\hat{\tau}}_{p}{({\hat{\theta}}^{{(p)} \ast})}$. Note that term ${\hat{\overline{\epsilon}}}_{p}$, see, does not depend on ${\hat{\theta}}^{{(p)} \ast}$ and it converges to the optimal error bound ${\overline{\epsilon}}_{p}^{\ast}$ as $N_{p}$ increases (Theorem 1).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 2", "weight": 1.0} -->

${\hat{\theta}}^{{(p)} \ast}$ in reads This problem can be solved by reformulating it as ${2N_{p}} + 1$ LPs,.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Derivation of the state-space model realization and estimation of the corresponding process disturbance bound", "weight": 1.0} -->

In this section we describe the derivation of the state-space model and of of the bound $\overline{w}$ of the corresponding disturbance $w{(k)}$.\First of all, we define the equations of the state-space model based on the nominal $1$-step ahead predictor, i.e., with $p = 1$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Derivation of the state-space model realization and estimation of the corresponding process disturbance bound", "weight": 1.0} -->

To do so, recalling the structure of $\varphi_{y}^{(p)}$, note that we can partition the parameter vector ${\hat{\theta}}^{(p)}$ of a prediction model as follows: where ${\hat{\theta}}_{AR}^{(p)} \in {\mathbb{R}}^{o}$, ${\hat{\theta}}_{U}^{(p)} \in {\mathbb{R}}^{o - 1}$ and ${\hat{\theta}}_{\overline{U}}^{(p)} \in {\mathbb{R}}^{p}$ are the parameters pertaining to the past $o$ output values, the past $o - 1$ input values, and the current and future inputs, respectively, up to $p - 1$ steps ahead.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Remark 3", "weight": 1.0} -->

The model of order ${2o} - 1$ is considered to be in minimal form Secondly, we need to define the bound $\overline{w}$ on the amplitude of $w{(k)}$. As anticipated, to this aim we will use the computed FPSs $\Theta^{(p)}$. More specifically, the following approach is proposed.\Starting from a noise-corrupted initial state at step $k$ and by iteration of the state-space model (discarding process disturbance), we can compute a $p$-steps ahead prediction ${\hat{z}}^{}{({k + p})}$ of the variable $z{({k + p})}$ as follows: We can write equivalently as This is a multi-step prediction model whose parameter vector ${\hat{\theta}}^{{(p)},1}$, in view of, is composed of polynomial combinations of the entries of the $1$-step ahead prediction model parameter vector ${\hat{\theta}}^{{} \ast}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Remark 3", "weight": 1.0} -->

At this point, we can use the FPSs derived in Section 3.3.3 to estimate the associated worst-case prediction error bounds, ${\hat{\tau}}_{p}{({\hat{\theta}}^{{(p)},1})}$: On the other hand, by initializing the state-space model with the true (i.e. without measurement noise) initial state, and including the presence of process disturbance $w$, we can also write: Then, taking the difference between and, we obtain: which highlights the prediction error due to the process disturbance $w$, and the one due to the measurement noise on the initial condition, ${X_{y}{(k)}} - {X{(k)}}$. Note that the latter is equal to zero for all state components pertaining to the past input values, and it is at most equal to $\overline{d}$ for all components pertaining to the past output values.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Thus, recalling that ${|{w{(k)}}|} \leq \overline{w}$, we have: where $E = \left\lbrack {I_{o}\;0_{{({o - 1})},o}} \right\rbrack^{T}$. The idea proposed here is to compute $\overline{w}$ as the minimum value such that the bounds do not violate the (tight) bounds for all $p \in {\lbrack 1,\overline{p}\rbrack}$: Note that problem always admits a finite feasible solution thanks to the boundedness of ${{{\hat{\tau}}_{p}{({\hat{\theta}}^{{(p)},1})}},{\forall p}} \in {\lbrack 1,\overline{p}\rbrack}$

<!-- chunk {"id": "body-0041", "role": "body", "section": "MPC for tracking with learned models", "weight": 1.0} -->

As anticipated in Section 2, the MPC controller devised in this paper uses, in the cost function optimized at each time instant $k$, the optimal $p$-steps ahead models to predict in the best possible way the future evolution of the output variable, while the perturbed state-space model is used to rigorously define the constraints and ensure recursive feasibility.

<!-- chunk {"id": "body-0042", "role": "body", "section": "State observer and tube-based control approach", "weight": 1.0} -->

Since $z{(k)}$ is measured with some noise, the state $X{(k)}$ of the system cannot be perfectly reconstructed as a suitable collection of the past available outputs and inputs. For this reason, a Luenberger state observer is employed. To design the observer on the basis of the model, it is beneficial to introduce an estimate $\hat{w}{(k)}$ of the disturbance $w$. The term $\hat{w}{(k)}$ will result from a suitable optimization problem introduced later, in Section 4.2. The observer takes then the following form: where $\hat{X}{(k)}$ is the estimated state and the matrix $L$ is chosen such that the closed-loop matrix $({A - {LC}})$ is Schur stable.\Furthermore, for application of a tube-based robust control method inspired, we define the nominal dynamic system related to, where again the disturbance estimate $\hat{w}{(k)}$ is included, i.e.

<!-- chunk {"id": "body-0043", "role": "body", "section": "State observer and tube-based control approach", "weight": 1.0} -->

The input $u{(k)}$, to be applied to system at time instant $k$, is defined as the sum of two components as follows.

<!-- chunk {"id": "body-0044", "role": "body", "section": "State observer and tube-based control approach", "weight": 1.0} -->

The second component (i.e., $K{({{\hat{X}{(k)}} - {\overline{X}{(k)}}})}$) is given by a suitable proportional control law, aiming to reduce the displacement of the state $\overline{X}{(k)}$ of with respect to the state estimate $\hat{X}{(k)}$, available at time $k$. The gain $K$ is defined in such a way that the closed-loop transition matrix $A + {B_{1}K}$ is Schur stable, e.g. by pole-placement or LQR design.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Remark 4", "weight": 1.0} -->

Since the long-term prediction capabilities are commonly more accurate with model with the longest possible prediction horizon, i.e., $p = \overline{p}$, one suitable option for the gain estimate $\hat{\mu}$ is to choose $\hat{\mu} = \mu^{\overline{p}}$, where is the gain of the optimal $\overline{p}$-steps-ahead model.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Remark 4", "weight": 1.0} -->

Last we can define, ${\forall p} \in {\lbrack 1,\overline{p}\rbrack}$, the reference for the $p$-steps ahead model, i.e., The cost function to be minimized at each (sampling) time $k$ is therefore where $\overline{X}{({k + \overline{p} + 1})}$ is obtained by iterating the unperturbed state equation $\overline{p} + 1$ times, i.e., with ${\Gamma = \begin{bmatrix} \end{bmatrix}},{\Gamma_{w} = \begin{bmatrix} \end{bmatrix}}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Remark 4", "weight": 1.0} -->

Then, the weighting matrices are computed such that the following constraints are satisfied: Finally, the scalar $\sigma > 0$ must be chosen sufficiently large to provide converge properties, its quantitative evaluation is discussed in the Appendix.

<!-- chunk {"id": "body-0048", "role": "body", "section": "The optimization problem and main result", "weight": 1.0} -->

The optimization problem, to be solved at each time instant $k \geq 0$, reads If available, the solution to the optimization problem is denoted ${{{\overline{X}{(\left. k \middle| k \right.)}},{\overline{U}{(\left. k \middle| k \right.)}}} = {({\overline{u}{(\left. k \middle| k \right.)}},\ldots,{\overline{u}{({k + \left. \overline{p} \middle| k \right.})}})}},{z_{ref}{(\left. k \middle| k \right.)}}$, and $u{(k)}$ in is applied to the system according to the receding horizon principle. Also, we denote with $\overline{X}{({k + \left. p \middle| k \right.})}$ the future nominal state predictions generated using with input $\overline{U}{(\left.

<!-- chunk {"id": "body-0049", "role": "body", "section": "The optimization problem and main result", "weight": 1.0} -->

k \middle| k \right.)}$. The following result holds.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Simulation example", "weight": 1.0} -->

The proposed approach for learning-based predictive control has been tested on a simulation example. The considered system is of third order, and it corresponds to the discretization of the system with continuous time transfer function characterized by dominant complex poles with natural frequency $\omega_{n} = 4$ and damping factor $\xi = 0.2$, and with unitary gain. Figure 1 shows the open loop step response of the system under analysis. The input and output samples are collected with sampling time $T_{s} = 0.1$, the output $z{(k)}$ is corrupted by an additive disturbance $v{(k)}$ such that ${|{v{(k)}}|} \leq \overline{v} = 0.01$, while the bound on the measurement noise is $\overline{d} = 0.1$. The multistep models and bounds are computed up to $\overline{p} = 20$ steps ahead, while the chosen model order is $o = 4$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Simulation example", "weight": 1.0} -->

The collected dataset is composed overall of 1000 input-output data samples, where the input is a step-wise sequence taking a random value in $\{{- 1},0,1\}$ every $5$ time units.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Simulation example", "weight": 1.0} -->

To clarify the advantage of our approach, in Figure 5 we compare the guaranteed bounds computed by iterating the obtained state-space model as described in this paper with those achieved by considering the uncertainty bound $\overline{w} = {{{\hat{\tau}}_{1}{({\hat{\theta}}^{{} \ast})}} + \overline{d}}$, i.e. the one-step-ahead guaranteed prediction error bound, iterating it over time with the same model matrices, and eventually adding $\overline{d}$. This alternative bound has been proposed in out previous works and. It can be noted that the proposed approach achieves a guaranteed bound on the prediction error that is half the one obtained from the integration of ${{\hat{\tau}}_{1}{({\hat{\theta}}^{{} \ast})}} + \overline{d}$, thus reducing conservativeness significantly.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Simulation example", "weight": 1.0} -->

In the control design phase, the constraint sets ${\mathbb{U}} = {\mathbb{Z}} = {\lbrack{- 10},10\rbrack}$ are considered, while the prediction and control horizon is $\overline{p} = 10$. The Luenberger observer and the auxiliary control law are chosen thanks to optimal control theory and the weighting matrices are tuned according to. The reference to be tracked is piece-wise constant and takes value $\{ 0,5,12\}$, thus including an unfeasible setpoint as well. The trajectories of the closed-loop system are reported in Figure 5, where it is shown that ${{\overline{z}}_{0}{(\left. k \middle| k \right.)}}\rightarrow z_{goal}$ or to its nearest feasible point. As visible from the simulations, the infeasibile reference is handled successfully by the controller as well as the transients with respect to the open loop response of the system.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conclusions", "weight": 1.0} -->

The proposed unitary approach to learning-based MPC for linear systems allows one to design a control law based on a dataset collected from the working plant. The obtained data-driven controller is able to effectively deal with constraints and track desired output references. The method relies on two phases: model learning and model-based control design, that are conceived to limit conservativeness while still robustly guaranteeing constraint satisfaction. To achieve this result, multi-step predictors and the related uncertainty bounds are derived and exploited to compute the state-space model employed in the MPC design. Future directions are concerned with the extension to classes of nonlinear systems, the online (adaptive) computation of the prediction models and disturbance bounds, and the direct use of multi-step predictors also in the constraint tightening scheme.
