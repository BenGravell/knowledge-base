<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On Multi-step Prediction Models for Receding Horizon Control

Topics include Model predictive control, Predictive control, Robustness, Control, Multi-Step prediction models.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The derivation of multi-step-ahead prediction models from sampled data of a linear system is considered. A dedicated prediction model is built for each future time step of interest. In addition to a nominal model, the set of all models consistent with data and prior information is derived as well, making the approach suitable for robust control design within a Model Predictive Control framework. The resulting parameter identification problem is solved through a sequence of convex programs, overcoming the non-convexity arising when identifying 1-step prediction models with an output-error criterion. At the same time, the derived models guarantee a worst-case error which is always smaller than the one obtained by iterating models identified with a 1-step prediction error criterion.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

This manuscript contains technical details of recent results developed by the authors on learning-based model predictive control for linear time invariant systems.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Let us consider a single-input, single-output (SISO), open-loop stable, discrete-time, strictly proper linear time invariant (LTI) system with $n$ states, input ${u{(k)}} \in {\mathbb{R}}$ and output ${z{(k)}} \in {\mathbb{R}}$, where $k \in {\mathbb{Z}}$ is the discrete time variable.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The input $u{(k)}$ is measured with negligible noise. $\square$

<!-- chunk {"id": "body-0006", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

(Input bounds) The input $u$ belongs to a compact set: ${{u{(k)}} \in {\mathbb{U}} \subset {\mathbb{R}}},{{\forall k} \in {\mathbb{Z}}}$. $\square$ Let us denote with $p \in {\mathbb{N}}$ a finite number of time steps in the future. We are interested in deriving a prediction model of the future output $z{({k + p})}$, exploiting the input and output measurements collected in the time interval $\lbrack{{k - o} + 1},k\rbrack$, where $o \in {\mathbb{N}}$ is the chosen order of the model, and the future (planned) inputs in the interval $\lbrack k,{{k + p} - 1}\rbrack$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Specifically, at any instant $k$ let us define the regressor ${\varphi_{p}{(k)}} \in {\mathbb{R}}^{{{2o} - 1} + p}$ as: where ^T^ is the matrix transpose operation and Then, we consider the following linear model structure: where $\hat{z}{({k + p})}$ is the predicted output and $\theta_{p} \in {\mathbb{R}}^{{{2o} - 1} + p}$ is the model parameter vector. We refer to models of the form as "multi-step", since for each $p \in {\mathbb{N}}$ the corresponding prediction model provides directly an estimate of $z{({k + p})}$. This is different from the (most common) approach of deriving a one-step-ahead model and then iterating it $p$ times to compute predictions for the subsequent future time-steps.\In addition to the prediction model, we also want to derive guaranteed bounds on its accuracy.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

In particular, we aim for the following *global* guaranteed accuracy bound: The value $\tau_{p}{(\theta_{p})}$ is termed "global" since it holds for any value of the regressor $\varphi_{p}$ within a specified set, as we further detail in the remainder of this paper.\A collection of multi-step models derived for all $p \in {\lbrack 1,\overline{p}\rbrack}$ provides an estimated sequence of future system outputs, up to the prediction horizon $\overline{p} < \infty$, together with an associated sequence of guaranteed uncertainty intervals $\tau_{p}{(\theta_{p})}$. These models can be then embedded in a robust finite-horizon optimal control problem to be solved in a receding-horizon approach, thus realizing a MPC law based on multi-step predictions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Three important reasons to consider multi-step models are: the model identification procedure results in convex optimization problems, as opposed to the nonlinear programs arising when identifying one-step-ahead models with an output-error (i.e. simulation) criterion; the guaranteed bound $\tau_{p}{(\theta_{p})}$ pertaining to a multi-step model is less conservative than the one pertaining to a one-step-ahead model iterated $p$ times; by considering an independent model for each value of $p$, there is no need for trade-offs between model accuracy at high-frequency (i.e. short prediction horizon) vs. low-frequency (i.e. long prediction horizon) that arise when choosing the simulation horizon in the identification of one-step-ahead models with an output-error criterion.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The use of a model structure that is linear in the parameters is justified both by point 1) above and by the observation that, in the case of zero measurement noise, the true output $z{({k + p})}$ is indeed a linear function of the regressor, provided that the following assumption holds.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

(Observability, reachability and model order) The system at hand is completely observable and reachable, and $o \geq n$. $\square$ Under Assumption 3, with straightforward manipulations one can show that the state at time $k$ is in general a linear function of the past $n$ input-output values, and that the output at time $k + p$ is linear in the state and in the planned input values, hence resulting in the model structure. From the practical standpoint, Assumption 3 can be relaxed to account only for the observable and controllable sub-space of the system state. Moreover, this assumption can be satisfied by estimating the system order $n$ (e.g. based on physical considerations) and/or by deriving models with growing order $o$ and by monitoring the magnitude of the corresponding accuracy bounds, as we describe more in detail in section 3.6.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

Assumption 2, combined with the asymptotic stability of the system under study, results in bounded sets where the regressor $\varphi_{p}$ evolves in time. Specifically, for a given horizon $p$ we consider a compact set $\Phi_{p}$ containing the regressor values of interest: $\Phi_{p}$ needs not to be known explicitly and is in general a complicated set that depends on the system input-output trajectories. Rather, we assume that for a given value of $p$ a finite batch of experimental data is available: In, the notation $\overset{\sim}{\cdot}$ indicates specific measured values of a quantity.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

These pairs can be easily built from a given data-set of measured input-output values, collected e.g. in a preliminary experiment on the system.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

We further define the vectors of sampled variables ${{{\overset{\sim}{v}}_{p}{(i)}} \doteq {\lbrack{{\overset{\sim}{\varphi}}_{p}{(i)}^{T}{\overset{\sim}{y}}_{p}{(i)}}\rbrack}^{T}},{i = {1,\ldots,N_{p}}}$ and the corresponding countable set containing them: For any given value of $\varphi_{p} \in \Phi_{p}$, the corresponding measured system output $y_{p}$ is not uniquely determined a priori, rather it belongs to a set ${{\mathbf{Y}}_{p}{(\varphi_{p})}} \subset R$, due to the measurement noise $d$ (both in the regressor and in the corresponding output).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

In view of Assumptions 1 and 3 and of the compactness of $\Phi_{p}$, the set ${\mathbf{Y}}_{p}{(\varphi_{p})}$ is also compact for any $\varphi_{p} \in \Phi_{p}$. We can then define the following continuous counterpart of the set ${\overset{\sim}{\mathcal{V}}}_{p}^{N_{p}}$: Namely, the set $\mathcal{V}_{p}$ contains all possible regressors $\varphi_{p}$ in the compact $\Phi_{p}$ and, for each value of $\varphi_{p}$, all possible output values in the corresponding compact set ${\mathbf{Y}}_{p}{(\varphi_{p})}$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

$\square$ Assumption 4 is equivalent to assuming that ${\lim\limits_{N_{p}\rightarrow\infty}{d_{2}\left(\mathcal{V}_{p},{\overset{\sim}{\mathcal{V}}}_{p}^{N_{p}} \right)}} = 0$, i.e. that by adding more points to the measured data set, the underlying set of all trajectories of interest is densely covered. This is essentially an assumption on the persistence of excitation of the inputs used for the preliminary experiments, together with an assumption of bound-exploring property of the additive disturbance $d$, such that the bound $\overline{d}$ in Assumption 1 is actually tight.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

We are now in position to formulate the problem that we will address in the remainder of this paper:\Problem 1 Under Assumptions 1-4, for a given ${\overline{p} < \infty},{p \in {\mathbb{N}}}$ and any $p = {1,\ldots,\overline{p}}$, use the available data to identify a multi-step model of the form and estimate the associated guaranteed bounds. $\square$\We propose in the next section an approach to solve Problem 1, based on a Set Membership (SM) identification methodology which guarantees convergence of the derived error bounds to suitably defined optimal values.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Learning multi-step prediction models: a set membership approach", "weight": 1.0} -->

For the sake of simplicity, in the following we consider a single value of $p \in {\lbrack 1,\overline{p}\rbrack}$, the extension to any other value is straightforward. The proposed approach consists of the following steps.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Learning multi-step prediction models: a set membership approach", "weight": 1.0} -->

Define an optimality criterion to evaluate the model estimates, corresponding to an optimal (i.e. minimal) error bound.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Learning multi-step prediction models: a set membership approach", "weight": 1.0} -->

Derive a procedure to estimate the optimal error bound.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Learning multi-step prediction models: a set membership approach", "weight": 1.0} -->

Based on the available data and the error bound estimate, build the set of all parameters that are consistent with this information (Feasible Parameter Set, FPS).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Learning multi-step prediction models: a set membership approach", "weight": 1.0} -->

Using the information summarized in the FPS, for any given model of the form compute the related guaranteed error bound $\tau_{p}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Learning multi-step prediction models: a set membership approach", "weight": 1.0} -->

Select a nominal model with minimal guaranteed error bound.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Learning multi-step prediction models: a set membership approach", "weight": 1.0} -->

We describe next each step in detail, followed by a discussion on tuning and extensions of the approach.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Optimal parameters and optimal error bound", "weight": 1.0} -->

Assume that a value of $\theta_{p}$ has been fixed. Then, under the considered working assumptions, ${\forall k} \in {\mathbb{Z}}$: where $\epsilon_{p}{(\theta_{p},{\varphi_{p}{(k)}})}$ is the error between the true system output and the estimated one: The quantity $\epsilon_{p}{(\theta_{p},{\varphi_{p}{(k)}})}$ accounts for the quality of the chosen parameter values, for the model order mismatch ($o > n$, compare Assumption 3) and for the noise in the regressor measurements. Since the underlying system dynamics are time-invariant, $\epsilon_{p}$ depends inherently on the model parameter vector $\theta_{p}$ and on the specific regressor $\varphi_{p}{(k)}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Optimal parameters and optimal error bound", "weight": 1.0} -->

$\epsilon_{p}{(\theta_{p},{\varphi_{p}{(k)}})}$ is bounded because both $y{({k + p})}$ and $\theta_{p}^{T}\varphi_{p}{(k)}$ are, due to the stability of the system and compactness of the set containing the input values. From and Assumption 1 we have: where ${\overline{\epsilon}}_{p}{(\theta_{p})}$ is the global error bound with respect to all possible regressors of interest in the compact $\Phi_{p}$: The quantity ${\overline{\epsilon}}_{p}{(\theta_{p})}$ is the tightest bound on the global (i.e. worst-case) estimation error that a given parameter vector $\theta_{p}$ can produce. We can now define the optimal parameter values (i.e. optimal models) as those that minimize such a bound.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Optimal parameters and optimal error bound", "weight": 1.0} -->

As a technical assumption, we consider all the parameters within a compact set $\Omega \subset {\mathbb{R}}^{{{2o} - 1} + p}$. $\Omega$ can take into account application-specific prior information on the model parameters or, if no such information is available, it can be chosen as a large-enough set (e.g. by considering box constraints of $\pm 10^{15}$ on each element of the parameter vector). This assumption allows us to use maximum and minimum operators instead of supremum and infimum.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Estimating the optimal error bound", "weight": 1.0} -->

The optimal models and optimal error bound cannot be computed in practice, since the solution to would imply the availability of an infinite number of data and the solution to an infinite-dimensional optimization program. However, we can compute an estimate ${\underset{¯}{\lambda}}_{p} \approx {\overline{\epsilon}}_{p}^{0}$ from the available experimental data, by solving the following linear program (LP): The last inequality constraint in is required to enforce a positive estimate of the error bound: without this constraint, the obtained estimate could result to be negative, especially in presence of small amount of data and output disturbance realizations with much smaller magnitude than the considered bound $\overline{d}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Estimating the optimal error bound", "weight": 1.0} -->

The following result shows that, under the considered working assumptions, the estimate converges to the optimal one, ${\overline{\epsilon}}_{p}^{0}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Feasible Parameter Set", "weight": 1.0} -->

We can now exploit the estimated optimal error bound to construct the tightest set of parameter values that are consistent with all the prior information, i.e. the FPS $\Theta_{p}$: The set $\Theta_{p}$ is non-empty by construction, since under Assumption 5 we have (compare and): If the FPS is bounded, it results in a polytope with at most $N_{p}$ faces. If it is unbounded, then this is a sign that the employed measured data are not informative enough to derive a bound on the worst-case model error (as we show next) and that the number of available data $N_{p}$ shall be increased until a bounded FPS is obtained. This situation usually occurs when very few data points are used (e.g. $N_{p} < {{{2o} - 1} + p}$) or the preliminary experiments are not informative enough (e.g. when only steady-state data are used).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Error bound computation for a generic model", "weight": 1.0} -->

Having defined the FPS, we can proceed to derive a bound on the prediction error achieved by any model of the form. Let us consider a generic value of $\theta_{p}$ to derive the prediction model. Then, considering any $\theta_{p}^{0} \in \Theta_{p}^{0}$ and any ${\varphi_{p}{(k)}} \in \Phi_{p}$, using and we have: The tightest bound we can derive on is based on the knowledge that $\theta_{p}^{0} \in \Theta_{p}$ (see) and that ${\overline{\epsilon}}_{p}^{0} \leq {\hat{\overline{\epsilon}}}_{p}$ (Assumption 5): The latter bound is the tightest *local* error bound (i.e. valid for a given value of $\varphi_{p}$) for the model given by the considered parameter value $\theta_{p}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Error bound computation for a generic model", "weight": 1.0} -->

As stated in Problem 1, for the sake of using the model within a robust MPC framework, we want to derive a global bound $\tau_{p}{(\theta_{p})}$ holding ${\forall\varphi_{p}} \in \Phi_{p}$. Considering - leads to: Such a bound cannot be derived exactly with finite data under the considered assumptions, and its computation would be intractable also if the set $\Phi_{p}$ were known precisely (unless some additional assumption is made, e.g. polytopic set $\Phi_{p}$). However, we can approximate it by computing the maximum of over the data-set ${\overset{\sim}{\mathcal{V}}}_{p}^{N_{p}}$: The following result shows convergence of ${\underset{¯}{\tau}}_{p}{(\theta_{p})}$ to $\tau_{p}{(\theta_{p})}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Nominal model selection", "weight": 1.0} -->

The last step in the proposed approach is to select a nominal model. The most common approach is probably least-squares estimation, in which case the results of section (3.4) can be anyway applied to obtain an estimate of the resulting global error bound. Since the final goal is to employ the model in a MPC algorithm, we rather seek the model that minimizes the uncertainty bound.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Nominal model selection", "weight": 1.0} -->

Specifically, considering that the tightest set that contains the optimal parameter values (i.e. with minimum error, see section (3.1)) is the FPS $\Theta_{p}$, we search within this set for the parameter value that minimizes the resulting bound ${\hat{\tau}}_{p}{(\theta_{p})}$: The resulting nominal model is ${\hat{z}{({k + p})}} = {\varphi_{p}{(k)}^{T}\theta_{p}^{\ast}}$, and the associated error bound is: Note that term ${\hat{\overline{\epsilon}}}_{p}$ in does not depend on $\theta_{p}^{\ast}$ and it converges to the optimal error bound ${\overline{\epsilon}}_{p}^{0}$ as $N_{p}$ increases (Theorem 1).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Nominal model selection", "weight": 1.0} -->

Moreover, it can be shown that, under the considered working assumptions, if $\theta_{p}^{0}$ is unique then the difference $|{\theta_{p}^{0} - \theta_{p}^{\ast}}|$ tends to zero, and the associated error bound tends to the minimum value ${\overline{\epsilon}}_{p}^{0}$ as well. Furthermore, for any value of $N_{p}$ it can be shown that ${\hat{\tau}}_{p}{(\theta_{p}^{\ast})}$ corresponds to the radius of information, i.e. the minimum guaranteed error value that can be attained with the given prior information and data. Finally, it also holds that, for each $p > 1$ the bounds ${\hat{\tau}}_{p}{(\theta_{p}^{\ast})}$ computed in our approach are less conservative than the worst-case bounds obtained by iterating any 1-step-ahead prediction model of the form.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Nominal model selection", "weight": 1.0} -->

All these derivations are omitted here for the sake of brevity.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The optimization problem to be solved to compute $\theta_{p}^{\ast}$ takes the form This problem can be solved by reformulating it as ${2N_{p}} + 1$ LPs, as reported in the appendix for completeness.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Learning algorithm, tuning aspects and extensions", "weight": 1.0} -->

In the closing part of this section we report the overall identification algorithm, to be repeated for each prediction step $p = {1\ldots\overline{p}}$: Collect $N_{p}$ measured regressor values and the corresponding measured output instances (see)\Solve the optimization problem and compute ${\hat{\overline{\epsilon}}}_{p} = {\alpha{\underset{¯}{\lambda}}_{p}}$, that is needed to define the FPS \Solve to derive the nominal model $\theta_{p}^{\ast}$ and select a value of $\gamma > 1$ to compute the worst case prediction error estimate ${\hat{\tau}}_{p}{(\theta_{p}^{\ast})}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Learning algorithm, tuning aspects and extensions", "weight": 1.0} -->

The main tuning parameters in the approach are the model order $o$, the disturbance bound $\overline{d}$, and the scalars $\alpha$ and $\gamma$. In practical applications, a good estimate or even exact knowledge of $o$ and $\overline{d}$ is often available from considerations on the plant and the available sensors. If not, an order selection procedure consists, as anticipated in section 2, in monitoring the estimate ${\hat{\overline{\epsilon}}}_{p}$ with increasing values of $o$: typically there is a clear convergence to a constant or slowly decreasing bound when $o \geq n$. We provide an example of this procedure in the next section. Regarding the choice of $\overline{d}$, over- or under-estimating this value leads, respectively, to either a too optimistic estimate of the prediction errors (since part of the model uncertainty is then hidden in the disturbance bound) or to a higher conservativeness (since the prediction error bound is then accounting also in part for the measurement noise).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Learning algorithm, tuning aspects and extensions", "weight": 1.0} -->

In a similar way, too large values of $\alpha$ and $\gamma$ can lead to conservative error bounds, while values too close to 1 might give error bounds that are too tight and could be violated by new, previously unseen data. As a matter of fact, both conditions (over- and under-estimation) can be easily monitored on-line, and the derived tuning parameters $\overline{d},\alpha$ and $\gamma$ suitably adjusted. This feature can be exploited in view of employing the proposed approach in an adaptive framework, which is a planned extension of this work. Other planned extensions that can be developed relatively easily are to consider nonlinear systems, since we can still employ the same model parametrization and the described approach by embedding the effect of nonlinearities in the error term $\epsilon_{p}{(\theta_{p},\varphi_{p})}$ (see ), and the use of other choices of linearly-parametrized models, e.g. truncated series of functional bases, since the same approach and main results would still hold, referred to the specific chosen class of models.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Simulation results", "weight": 1.0} -->

The proposed algorithm has been tested on the benchmark example already considered. In particular, the data are generated according to the continuous-time transfer function: The input-output samples are collected with a sampling time $T_{s} = {0,{2s}}$ according to the output equation ${y{(k)}} = {{z{({kT_{s}})}} + {d{({kT_{s}})}}}$, where $d{(t)}$ is a colored noise obtained by low-pass filtering a randomly generated number, with a first-order filter with time constant of $0.2$s. The disturbance $d{(t)}$ is bounded in the interval ${\lbrack{- 0.2\;0.2}\rbrack},{\forall t}$, and the prediction horizon is $\overline{p} = 10$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Simulation results", "weight": 1.0} -->

The collected dataset is made of 500 input-output data samples. The input is a three level signal taking values randomly each $4$s in the set $\{{- 1},0,1\}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Simulation results", "weight": 1.0} -->

In order to select the order of the model, we solve problem for different orders $o$, as reported in Fig. 1. The trend of the solution is monotonically decreasing, and this can be explained thanks to the noisy regressors that increase in number in vector $\varphi_{p}$ as $o$ grows (see ). The effect of noise contained in them vanishes over time due to compensation of terms, eventually reducing the bound ${{\underset{¯}{\lambda}}_{p}{\forall p}} = {\ldots\overline{p}}$ for growing order $o$ of the model. The final choice has been $o = 3$, consistently with Assumption 3, that matches the order of the system, even though its true dynamics are dominated by the pole in $\overline{s} = {- 1}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We presented an approach to derive multi-step prediction models, and the related uncertainty bounds, for an unknown linear system affected by additive measurement disturbance. Under suitable assumptions, we demonstrated convergence of the bounds to their theoretical minimum based on the available information. The approach requires the solution to linear programs only. The derived models are particularly suited to robust model predictive control design, since they can predict the future trajectory of the system on a finite horizon and the related uncertainty intervals.
