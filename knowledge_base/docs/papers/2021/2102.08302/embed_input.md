<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Robust Multi-rate Predictive Control Using Multi-step Prediction Models Learned from Data

Topics include Predictive control, Stability analysis, Robustness, Uncertainty, Control.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This note extends a recently proposed algorithm for model identification and robust MPC of asymptotically stable, linear time-invariant systems subject to process and measurement disturbances. Independent output predictors for different steps ahead are estimated with Set Membership methods. It is here shown that the corresponding prediction error bounds are the least conservative in the considered model class. Then, a new multi-rate robust MPC algorithm is developed, employing said multi-step predictors to robustly enforce constraints and stability against disturbances and model uncertainty, and to reduce conservativeness. A simulation example illustrates the effectiveness of the approach.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In a recent paper, we presented a unitary approach to model identification and robust Model Predictive Control (MPC) design for linear, asymptotically stable, discrete time systems subject to process and measurement disturbances. A Set Membership (SM) identification approach was used to obtain multi-step prediction models used in the cost function definition, while state and control constraints were tightened by propagating the uncertainty bound of a simulation model, tuned using the knowledge of the multi-step models and the associated error intervals. Being the multi-step predictors linear in their parameters, it was possible to derive tight uncertainty bounds in a tractable way. However, these bounds were not directly exploited to deal robustly with constraints, with a consequent limited advantage in terms of conservativeness reduction in the constraint tightening procedure.\In the present paper, we develop this line of research with two main contributions: first, we prove that the prediction error bounds obtained with the SM approach proposed in are smaller than those of *any* linear simulation model iterated $p$ times. This further motivates the use of such predictors both in the cost function and for constraint tightening.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We do so in our second contribution, since we propose a new robust MPC scheme that explicitly relies on the optimal SM multi-step models, thus dramatically reducing conservativeness. To deal with the particular structure of the multi-step predictors, which prevents the use of a standard robust MPC approach, we adopt a novel multi-rate receding horizon strategy, for which we prove guaranteed constraint satisfaction and convergence properties. Many multirate schemes have been proposed in the literature for predictive control design, see for example, and the references therein, usually to cope with different sampling rates in outputs sampling, state update, and control implementation. On the contrary, here the multirate implementation stems from the particular form of the predictors.\In the last section of the paper, the new approach is compared with that of in a simulation example.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The proofs of the main results are reported in Appendix.\Notation: $I_{n}$ is the identity matrix of dimension $n$, ${\overline{I}}_{n}$ is the matrix with zero entries except for those on the anti-diagonal, which are equal to 1, $0_{m,n}$ is the null matrix of dimensions $m$ and $n$. The Cartesian product between $n$ sets $\text{T}_{1},\ldots,\text{T}_{n}$ is $\prod\limits_{i = 1}^{n}\text{T}_{i}$. For a generic vector $x$, ${\| x\|}^{2} \doteq {x^{T}x}$ and ${\| x\|}_{Q}^{2} \doteq {x^{T}Qx}$ with $Q$ being a given square matrix of suitable dimension.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Problem statement, identification algorithm, and error bounds", "weight": 1.0} -->

The system can be expressed in ARX (autoregressive-exogenous) form as where ${\overline{\theta}}^{} \in {\mathbb{R}}^{2n}$ is the vector of unknown parameters.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

(Model order) The order of the models is $o \geq n$ $\square$ An algorithm to estimate $o$ is described. The SM learning phase also returns an estimate of the bound on the worst-case prediction error: In fact, for each step $p \leq \overline{p}$ one can derive a guaranteed upper bound ${\hat{\tau}}_{p}$ of the difference between the nominal output and its prediction obtained with a generic predictor For the identification of ${\hat{\theta}}^{{(p)} \ast}$ and ${\hat{\tau}}_{p}$ a finite number $N$ of measured data is available, composed of pairs ${{{({\varphi_{y}^{(p)}{(k)}},{y{({k + p})}})},k} = 1},{\ldots,N}$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

We first estimate an error bound ${\hat{\overline{\epsilon}}}_{p} = {\alpha{\underset{¯}{\lambda}}_{p}}$, ${\forall p} = {1,\ldots,\overline{p}}$, through The latter value is inflated by a scalar $\alpha > 1$ to account for the fact that the available dataset is finite. The Feasible Parameter Sets (FPSs) are then defined as For each $p$, $\Theta^{(p)}$ is a convex set and, if the data are informative enough, it is also compact. This property can be checked easily by linear programming; if the set $\Theta^{(p)}$ is not bounded then this is a sign that more informative data should be collected. In the remainder, we consider that $\Theta^{(p)}$ is compact for any $p$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Let us further denote with $\Phi^{(p)} \subseteq {\mathbb{R}}^{{{2o} - 1} + p}$ a compact set containing all possible values of $\varphi_{y}^{(p)}{(k)}$. In practice, this means that we restrict our analysis and results to a set of system trajectories of interest, which contains the available data points. This is a reasonable assumption in practice.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Since ${\overline{\theta}}^{(p)}$ in belongs to $\Theta^{(p)}$, the smallest bound on the error $|{{z{({k + p})}} - {\hat{z}{({k + p})}}}|$ (see) ${\forall p} = {1,\ldots,\overline{p}}$ is: The bound is global, since it holds for any regressor value inside $\Phi^{(p)}$ and for any model compatible with the data, i.e. contained in the set $\Theta^{(p)}$. However it cannot be computed in practice since the set $\Phi^{(p)}$ is not available.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The nominal predictor, for each step $p$, is chosen as the minimizer of this worst case error ${\underset{¯}{\tau}}_{p}{({\hat{\theta}}^{(p)})}$, i.e.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The following theorem is concerned with the optimality (in terms of size of the uncertainty bound) of the multistep prediction models.

<!-- chunk {"id": "body-0013", "role": "body", "section": "MPC design and properties", "weight": 1.0} -->

The multi-step models previously introduced can not be directly used in existing robust MPC schemes. Therefore we propose a new multirate MPC approach where the predicted behavior of the system is optimized by considering a prediction/control horizon of $N_{p}$ "long" steps, with index ${j \in {\mathbb{N}}},$ each one consisting of $\overline{p}$ "short" sampling times with index $k$. Note that the "short" sampling interval is the one assumed for the true system. The optimal control problem is thus solved at every long step $j$ (i.e. every $\overline{p}$ short steps) and the solution provides the values of the control input to be applied at each step $k$ in the interval $\{{j\overline{p}},\ldots,{{{({j + 1})}\overline{p}} - 1}\}$ according to a standard receding horizon formulation.

<!-- chunk {"id": "body-0014", "role": "body", "section": "MPC design and properties", "weight": 1.0} -->

For clarity, we represent the long and short sampling times on a common time-scale in Figure 1. Also, in the remainder we will use the upper-case letters to denote variables defined at a long sampling time.

<!-- chunk {"id": "body-0015", "role": "body", "section": "MPC design and properties", "weight": 1.0} -->

Denote with ${\overline{w}}_{p}$ a value such that ${|{w_{p}{({j\overline{p}})}}|} \leq {\overline{w}}_{p}$, for all $p = {1,\ldots,\overline{p}}$, which accounts for the error stemming from the identification procedure, the process noise, and the measurement disturbance. Given the bound, since the state $X{(j)}$ comprises samples of the measured output $y$ affected by measurement noise $d$, it is possible to obtain ${\overline{w}}_{p}$ as thus directly exploiting the multi-step error bounds previously obtained. The state transition equation, that maps the current state $X{(j)}$ into the $\overline{p}$ steps ahead state $X{({j + 1})}$, is: The following assumption is introduced.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

The pair $(\overline{A},\overline{B})$ is stabilizable. $\square$ Since the model is obtained from input-output data, Assumption 3 is usually satisfied in practice and is thus not restrictive.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

Thanks to the predictors, we write In the control design phase a tube-based robust control approach is used and the input $U{(j)}$ is defined as The input $\overline{U}{(j)}$ will be computed by MPC, while the term $K{({{X{(j)}} - {\overline{X}{(j)}}})}$ aims to reduce the error between the state $\overline{X}{(j)}$ of a suitably defined nominal dynamic system and the actual value of $X{(j)}$, available at time $k = {j\overline{p}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

The gain $K$ is chosen such that $\overline{F} = {\overline{A} + {\overline{B}K}}$ is Schur stable, which is possible thanks to Assumption 3.\The nominal dynamic system is defined based: The $p$ steps ahead nominal output predictor corresponding to is computed as: The difference between the real available data vector $X{(j)}$ and the state of the nominal system is defined as ${E{(j)}} = {{X{(j)}} - {\overline{X}{(j)}}}$. From and, it evolves according to: Let $\mathbb{E}$ be a robust positively invariant (RPI) set for the system. Similarly to, the constraints and the optimization problem will be defined with reference to the nominal model. This will require to define suitable tightened state and input constraints, that allow one to account for the difference between $\overline{X}{(j)}$ and $X{(j)}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Remark 1", "weight": 1.0} -->

In only the last $o$ components of $W{(j)}$ are involved in the computation of $\mathbb{E}$, and they depend on the estimates ${\hat{\tau}}_{p}{({\hat{\theta}}^{{(p)} \ast})}$ of the bounds proved to be optimal in Theorem 1, see. Moreover, since $\overline{A} + {\overline{B}K}$ is Schur stable and evolves over a (possibly long) $\overline{p}$-steps-ahead period, it is prone to have a smaller spectral radius and norm with respect to the one corresponding to a 1-step state space model, e.g. the one considered. Thus, this results in a smaller set $\mathbb{E}$ and less conservative constraint tightening, as also illustrated in the example of Section IV.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 1", "weight": 1.0} -->

$\square$ The MPC controller must guarantee the fulfillment of input and output constraints for all $k \geq 0$: where $\mathbb{U}$ and $\mathbb{Z}$ are suitable convex sets containing the origin in their interior. For ease of notation, let us introduce the higher-dimensional convex sets $\text{U} = {\mathbb{U}}^{\overline{p}}$ and $\text{Z} = {\mathbb{Z}}^{\overline{p}}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Similarly to, it is first necessary to constrain $\overline{X}{(j)}$ at time $j\overline{p}$ to lie in the neighborhood of $X{(j)}$, i.e Finally, to guarantee recursive feasibility, we also need to enforce a terminal constraint of the type where ${\mathbb{X}}_{F}$ is defined as a positively invariant set for the system ${\hat{X}{({j + 1})}} = {{({\overline{A} + {\overline{B}K}})}\hat{X}{(j)}}$ that verifies ${{({\overline{C} + {\overline{D}K}})}{\mathbb{X}}_{F}} \subseteq {\hat{\mathbf{Z}} \ominus {{({\overline{C} + {\overline{D}K}})}{\mathbb{E}}}}$

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

There exists a ball $\mathcal{B}$ in space ${\mathbb{R}}^{\overline{p}}$, centered at the origin and with radius $\varepsilon$, such that The cost function to be minimized at time step $k$ is where $Q = {\text{diag}{(q_{1},\ldots,q_{\overline{p}})}} > 0$, $R = {\text{diag}{(r_{0},\ldots,r_{\overline{p} - 1})}} > 0$, $N_{p}$ is the prediction horizon, and $P$ is the unique positive definite solution to the Riccati equation (see Assumption 3) where $\overline{G} = {({\overline{C} + {\overline{D}K}})}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

Note that $Q$ and $R$ can be chosen freely while in they were selected according to the solution to an LMI problem, so limiting the possible trade-offs between bandwidth and control activity of the closed-loop system.\Now, denoting the vector of decision variables with the optimization problem to be solved at each "long" sampling time $j \geq 0$, reads If problem is feasible, its solution is denoted with ${{{\overline{X}}^{\ast}{(j)}},{{\overline{\mathbf{U}}}^{\ast}{(j)}}} = {\lbrack{{\overline{U}}^{\ast}{(j)}^{T}},\ldots,{{\overline{U}}^{\ast}{({{j + N_{p}} - 1})}^{T}}\rbrack}^{T}$, and the input sequence ${U^{\ast}{(j)}} =

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

Also, we denote with ${\overline{X}}^{\ast}{({j + i})}$ the future nominal state predictions generated using with input ${\overline{\mathbf{U}}}^{\ast}{(j)}$, as well as all the other derived quantities, such as ${\hat{\overline{Z}}}^{\ast}{(j)}$ (see).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Simulation example", "weight": 1.0} -->

Consider the system employed, obtained by discretizing, with sampling time $T_{s} = 0.1$, the continuous-time transfer function A dataset of 1000 pairs $(u,y)$ has been collected by exciting the system with a signal $u$ taking value in $\{{- 1},0,1\}$ randomly each $5$ units of time, and adding the disturbance $v{(k)}$ and $d{(k)}$, with $\overline{v} = 0.01$ and $\overline{d} = 0.1$, respectively, consistently. The multi-step bounds estimates ${\hat{\tau}}_{p}{({\hat{\theta}}^{{(p)} \ast})}$ have been computed according to the algorithm described, with $\overline{p} = 10$ (resulting in a "long" sampling time equal to ${T_{s}\overline{p}} = {1s}$) and model order $o = 4$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Simulation example", "weight": 1.0} -->

In Figure 2 they are plotted and compared with the bounds computed by simply iterating the simulation model (i.e., the $1$-step ahead predictor) and propagating its uncertainty bound accordingly.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Simulation example", "weight": 1.0} -->

In the control design phase, the matrix $K$ has been computed with Linear Quadratic (LQ) control, while the prediction horizon for the MPC controller is $N_{p} = 3$. The weighting matrices are defined as $Q = {100I_{\overline{p}}}$ and $R = {1I_{\overline{p}}}$, while matrix $P$ is obtained thanks to. Both the input $u$ and the output $z$ have been enforced to belong to the set $\lbrack{- 10},10\rbrack$ for each time instant.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Simulation example", "weight": 1.0} -->

The input and output trajectories, comparing the closed-loop with the open-loop response of the system, are plotted in Figures 3 and 4 together with the relevant bounds. The controller, based on the identified model, is able to regulate the real system to zero with a much faster time constant and sensibly damping the oscillations. In Table I we also report, for the same tuning of the LQ problem, the spectral radius and norm of the state transition matrix of the nominal system subject to the auxiliary law $K$, see also Remark 1. Note that the norm of such matrix directly affects the computation of the invariant set $\mathbb{E}$. Moreover, by comparing the effect on the constraint tightening, we note that, while in the tightened output constraints correspond to the interval $\lbrack{- 7.7},7.7\rbrack$ for each prediction step and the input constraints to the interval $\lbrack{- 9.05},9.05\rbrack$, with the new algorithm proposed.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Simulation example", "weight": 1.0} -->

here we obtain the following box-inequalities, to be intended entry-wise, $i = {0,\ldots,{N_{p} - 1}}$: Specifically, define and the constraints\which confirm a conservativeness reduction. ${\rho\left({\overline{A} + {\overline{B}K}} \right)} = 0.2974$ $\left\| {\overline{A} + {\overline{B}K}} \right\| = 0.455$ Table I: Table of comparison of radius and spectral norm of state transition matrix Figure 2: Computed bounds. Dashed line: bound obtained by iterating $\overline{w_{1}}$ with the one-step model, solid line: bounds ${{{\overline{w}}_{p},p} = 1},{\ldots,\overline{p}}$ Figure 3: Input variable.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Simulation example", "weight": 1.0} -->

Dash-dotted line: $\overline{U}{(k)}$, solid line: U (k), dashed lines: tightened constraints (23b), dotted lines: absolute constraints.
