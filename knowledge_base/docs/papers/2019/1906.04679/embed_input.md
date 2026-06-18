<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Data-Driven Model Predictive Control with Stability and Robustness Guarantees

Topics include Data-driven control, Model predictive control, Behavioral systems, Robust model predictive control, Stability guarantees, Output measurement noise, Terminal constraints.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Gives one of the first closed-loop stability and robustness analyses for a purely data-driven MPC scheme based on behavioral trajectory data. The contribution is especially important because it moves DeePC-style ideas from empirical performance toward certified robust receding-horizon control.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a robust data-driven model predictive control (MPC) scheme to control linear time-invariant (LTI) systems. The scheme uses an implicit model description based on behavioral systems theory and past measured trajectories. In particular, it does not require any prior identification step, but only an initially measured input-output trajectory as well as an upper bound on the order of the unknown system. First, we prove exponential stability of a nominal data-driven MPC scheme with terminal equality constraints in the case of no measurement noise. For bounded additive output measurement noise, we propose a robust modification of the scheme, including a slack variable with regularization in the cost. We prove that the application of this robust MPC scheme in a multi-step fashion leads to practical exponential stability of the closed loop w.r.t. the noise level. The presented results provide the first (theoretical) analysis of closed-loop properties, resulting from a simple, purely data-driven MPC scheme.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

While data-driven methods for system analysis and control have become increasingly popular over the recent years, only few such methods give theoretical guarantees, e.g., stability or constraint satisfaction of system variables. A control method, which is naturally well-suited for achieving these objectives is model predictive control (MPC), which can handle nonlinear system dynamics, hard constraints on input, state and output, and it takes performance criteria into account. It centers around the repeated online solution of an optimization problem over predicted future system trajectories. Thus, for the implementation of MPC, a model of the plant is required, which is usually obtained from first principles or from measured data via system identification. An appealing alternative is to implement an MPC controller directly from measured data, without prior knowledge of an accurate model. In various recent works, learning-based or adaptive MPC schemes have been proposed, which improve an inaccurate initial model using online measurements, while giving guarantees on the resulting closed loop. Similarly, MPC based on Gaussian Processes has received increasing attraction, but proving desirable closed-loop properties remains an open issue.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A different approach, which uses linear combinations of past trajectories to predict future trajectories, has been presented, but also no guarantees, e.g., stability of the closed loop were given. The design of purely data-driven MPC approaches with guarantees on stability and constraint satisfaction thus remains an open problem.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we present a novel data-driven MPC scheme to control linear time-invariant (LTI) systems with stability and robustness guarantees for the closed loop. Our approach relies on a result from behavioral systems theory, which shows that the Hankel matrix consisting of a previously measured input-output trajectory spans the vector space of all trajectories of an LTI system, given that the input component is persistently exciting. Although this result has found various applications in the field of system identification, it has only recently been used to develop data-driven methods for system analysis and control with theoretical guarantees. An exposition of the main result of in the classical state-space control framework and an extension to certain classes of nonlinear systems are provided. Further, the result is employed in to design state- and output-feedback controllers and in to verify dissipation inequalities from measured data, whereas investigates data-driven control without requiring persistently exciting data.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, the recent contributions set up an MPC scheme based, but no guarantees on recursive feasibility or closed-loop stability can be given since neither terminal ingredients are included in the MPC scheme nor sufficient lower bounds on the prediction horizon are derived. In the present paper, we propose a related MPC scheme, which utilizes terminal equality constraints, and we provide a theoretical analysis of various desirable properties of the closed loop. To the best of our knowledge, this is the first analysis regarding recursive feasibility and stability of purely data-driven MPC. The main advantage of the proposed MPC scheme over existing adaptive or learning-based methods such as is that it requires only an initially measured, persistently exciting data trajectory as well as an upper bound on the system order, but no (set-based) model description and no online estimation process. Moreover, since it relies on the data-driven system description, the presented scheme is inherently an output-feedback MPC scheme and does not require online state measurements.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

After stating the required definitions and existing results in Section II, we expand the nominal MPC scheme of by terminal equality constraints in Section III. Under the assumption that the output of the plant can be measured exactly, we prove recursive feasibility, constraint satisfaction, and exponential stability of the scheme. In Section IV, we propose a robust data-driven MPC scheme to account for bounded additive noise in both the initial data for prediction as well as the online measurements. Under suitable assumptions on the system and design parameters, we prove that the closed loop under application of the scheme in a multi-step fashion leads to a practically exponentially stable closed loop. In Section V, we illustrate the advantages of the proposed scheme over the scheme without terminal constraints from by means of a numerical example. The paper is concluded in Section VI.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Nominal data-driven MPC", "weight": 1.0} -->

In this section, we propose a simple, nominal data-driven MPC scheme with terminal equality constraints. The scheme relies on noise-free measurements to predict future trajectories using Theorem 1. ‣ II Preliminaries ‣ Data-Driven Model Predictive Control with Stability and Robustness Guarantees") and is described in Section III-A. Under mild assumptions, we prove recursive feasibility, constraint satisfaction, and exponential stability of the closed loop in Section III-B.

<!-- chunk {"id": "body-0010", "role": "body", "section": "III-A Nominal MPC scheme", "weight": 1.0} -->

Commonly, MPC relies on a model of the plant to predict future trajectories and to optimize over them. Theorem 1. ‣ II Preliminaries ‣ Data-Driven Model Predictive Control with Stability and Robustness Guarantees") provides an appealing alternative to a model since (1. ‣ II Preliminaries ‣ Data-Driven Model Predictive Control with Stability and Robustness Guarantees")) suffices to capture all system trajectories. Thus, to implement a data-driven MPC scheme, one can simply replace the system dynamics constraint by the constraint that the predicted input-output trajectories satisfy (1. ‣ II Preliminaries ‣ Data-Driven Model Predictive Control with Stability and Robustness Guarantees")). To be more precise, the proposed data-driven MPC scheme minimizes, at time $t$, given the last $n$ input-output pairs, the following open-loop cost\

<!-- chunk {"id": "body-0011", "role": "body", "section": "III-A Nominal MPC scheme", "weight": 1.0} -->

As described above, the constraint (2b) replaces the system dynamics compared to classical model-based MPC schemes. Further, (2c) ensures that the internal state of the true trajectory aligns with the internal state of the predicted trajectory at time $t$. Note that the overall length of the trajectory $({\overline{u}{(t)}},{\overline{y}{(t)}})$ is $L + n$ since the past $n$ elements ${\{{{\overline{u}}_{k}{(t)}},{{\overline{y}}_{k}{(t)}}\}}_{k = {- n}}^{- 1}$ are used to specify the initial conditions in (2c). These initial conditions are specified until time step $t - 1$, since the input at time $t$ might already influence the output at time $t$, in case of a feedthrough-element of the plant.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-A Nominal MPC scheme", "weight": 1.0} -->

The open-loop cost depends only on the decision variable $\alpha{(t)}$, since $\overline{u}{(t)}$ and $\overline{y}{(t)}$ are fixed implicitly through the dynamic constraint (2b). Throughout the paper, we consider quadratic stage costs, which penalize the distance w.r.t. a desired equilibrium $(u^{s},y^{s})$, i.e.,

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-A Nominal MPC scheme", "weight": 1.0} -->

where ${Q,R} \succ 0$. In, it was suggested to directly minimize the above open-loop cost subject to constraints on input and output. It is well-known that MPC without terminal constraints requires a sufficiently long prediction horizon to ensure stability and constraint satisfaction. Without such an assumption, the application of MPC can even destabilize an open-loop stable system. There are two main approaches in the literature to guarantee stability: a) providing bounds on the minimal required prediction horizon and b) including terminal ingredients such as terminal cost functions or terminal region constraints. Both approaches are usually based on model knowledge and thus, it is not straightforward to use them in the present, purely data-driven setting.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A Nominal MPC scheme", "weight": 1.0} -->

In this paper, we consider a simple terminal equality constraint, which can be directly included into the data-driven MPC framework, and which guarantees exponential stability of the closed loop. To this end, we propose the following data-driven MPC scheme with a terminal equality constraint.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-A Nominal MPC scheme", "weight": 1.0} -->

The terminal equality constraint (3d) implies that ${\overline{x}}_{L}{(t)}$, which is the internal state predicted $L$ steps ahead corresponding to the predicted input-output trajectory, aligns with the steady-state $x^{s}$ corresponding to $(u^{s},y^{s})$, i.e., ${{\overline{x}}_{L}{(t)}} = x^{s}$ in any minimal realization. While Problem requires that $(u^{s},y^{s})$ is an equilibrium of the unknown system in the sense of Definition 3, this requirement can be dropped when $(u^{s},y^{s})$ is replaced by an artificial equilibrium, which is also optimized online (compare ). The recent paper extends the above MPC scheme to such a setting, thereby leading to a significantly larger region of attraction for the closed loop without requiring knowledge of a reachable equilibrium of the unknown system. As in standard MPC, Problem is solved in a receding horizon fashion, which is summarized in Algorithm 1.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A Nominal MPC scheme", "weight": 1.0} -->

At time t, take the past n measurements u[t − n, t − 1], y[t − n, t − 1] and solve.
Apply the input $u_{t} = {{\overline{u}}_{0}^{\ast}{(t)}}$.
Set t = t + 1 and go back to 1).

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A Nominal MPC scheme", "weight": 1.0} -->

With slight abuse of notation, we will denote the open-loop cost and the optimal open-loop cost of by $J_{L}{(x_{t},{\alpha{(t)}})}$ and $J_{L}^{\ast}{(x_{t})}$, respectively, where $x_{t}$ is the state in some minimal realization, induced by $u_{\lbrack{t - n},{t - 1}\rbrack}$, $y_{\lbrack{t - n},{t - 1}\rbrack}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-B Closed-loop guarantees", "weight": 1.0} -->

Without loss of generality, we assume for the analysis that $u^{s} = 0$, $y^{s} = 0$, and thus $x^{s} = 0$. Further, we define the set of initial states, for which is feasible, by ${\mathbb{X}}_{L} = \left\{ {x \in {\mathbb{R}}^{n}}\mid{{J_{L}^{\ast}{(x)}} < \infty} \right\}$. To prove exponential stability of the proposed scheme, we assume that the optimal value function of is quadratically upper bounded. This is, e.g., satisfied in the present linear-quadratic setting if the constraints are polytopic^11^1While considered model-based linear-quadratic MPC, the result applies similarly to the present data-driven MPC setting since (3b) (together with the initial conditions (3c)) describes the input-output behavior of the system exactly and thus, both settings are equivalent in the nominal case..

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Moreover, we assume that the input $u^{d}$ generating the data used for prediction is sufficiently rich in the following sense.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The input $u^{d}$ of the data trajectory is persistently exciting of order $L + {2n}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Note that we assume persistence of excitation of order $L + {2n}$, although Theorem 1. ‣ II Preliminaries ‣ Data-Driven Model Predictive Control with Stability and Robustness Guarantees") requires only an order of $L + n$. This is due to the fact that the reconstructed trajectories in are of length $L + n$ (compared to length $L$ in Theorem 1. ‣ II Preliminaries ‣ Data-Driven Model Predictive Control with Stability and Robustness Guarantees")), since $n$ components are used to fix the initial conditions. Furthermore, due to the terminal constraints (3d), the prediction horizon needs to be at least as long as the system order $n$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

The prediction horizon satisfies $L \geq n$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

The following result shows that the MPC scheme based on is recursively feasible, ensures constraint satisfaction, and leads to an exponentially stable closed loop.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 1", "weight": 1.0} -->

We would like to emphasize the simplicity of the proposed MPC scheme. Without any prior identification step, a single measured data trajectory can be used directly to set up an MPC scheme for a linear system. Compared to other learning-based MPC approaches such as, which require initial model knowledge as well as an online estimation process, the complexity of is similar to classical MPC schemes, which rely on full model knowledge. To be more precise, the decision variables ${\overline{u}{(t)}},{\overline{y}{(t)}}$ can be replaced by $\alpha{(t)}$ via (3b) (using a condensed formulation) and hence, since ${\alpha{(t)}} \in {\mathbb{R}}^{{N - L - n} + 1}$, Problem contains in total ${N - L - n} + 1$ decision variables.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 1", "weight": 1.0} -->

For $u^{d}$ to be persistently exciting of order $L + {2n}$, it needs to hold that ${{N - L - {2n}} + 1} \geq {m{({L + {2n}})}}$. Assuming equality, Problem hence has ${m{({L + {2n}})}} + n$ free parameters. On the contrary, a condensed model-based MPC optimization problem contains $mL$ decision variables for the input trajectory (assuming that state measurements are available). Thus, the online complexity of the proposed data-driven MPC approach is slightly larger (${2mn} + n$ additional decision variables) than that of model-based MPC, but it does not require an a priori (offline) identification step. It is worth noting that the difference in complexity is independent of the horizon $L$. Moreover, the proposed data-driven MPC is inherently an output-feedback controller since no state measurements are required for its implementation.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Finally, as in model-based MPC, for convex polytopic (or quadratic) constraints ${\mathbb{U}},{\mathbb{Y}}$, is a convex (quadratically constrained) quadratic program which can be solved efficiently.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Robust data-driven MPC", "weight": 1.0} -->

In this section, we propose a multi-step robust data-driven MPC scheme and we prove practical exponential stability of the closed loop in the presence of bounded additive output measurement noise. The scheme includes a slack variable, which is regularized in the cost and compensates noise both in the initial data $(u^{d},y^{d})$ used for prediction and in the online measurement updates $\left( u_{\lbrack{t - n},{t - 1}\rbrack},y_{\lbrack{t - n},{t - 1}\rbrack} \right)$. Section IV-A contains the scheme, which is essentially a robust modification of the nominal scheme of Section III, as well as detailed explanations of the key ingredients. In Sections IV-B and IV-C, we prove two technical Lemmas, which will be required for our main theoretical results.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Robust data-driven MPC", "weight": 1.0} -->

Recursive feasibility of the closed loop is proven in Section IV-D. In Section IV-E, we show that, under suitable assumptions, the closed loop resulting from the application of the multi-step MPC scheme leads to a practically exponentially stable closed loop. Moreover, if the noise bound tends to zero, then the region of attraction of the closed loop approaches the set of all initially feasible points. In this section, we do not consider output constraints, i.e., ${\mathbb{Y}} = {\mathbb{R}}^{p}$. In, we recently extended the results of this section by incorporating tightened output constraints in order to guarantee closed-loop constraint satisfaction despite noisy data.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-A Robust MPC scheme", "weight": 1.0} -->

In practice, the output of the unknown LTI system $G$ is usually not available exactly, but might be subject to measurement noise. This implies that the stacked data-dependent Hankel matrices in (1. ‣ II Preliminaries ‣ Data-Driven Model Predictive Control with Stability and Robustness Guarantees")) do not span the system's trajectory space exactly and thus, the output trajectories cannot be predicted accurately. Moreover, noisy output measurements enter the initial conditions in Problem, which deteriorates the prediction accuracy even further. Therefore, a direct application of the MPC scheme of Section III may lead to feasibility issues or it may render the closed loop unstable. In this section, we tackle the issue of noisy measurements with a robust data-driven MPC scheme with terminal constraints.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-A Robust MPC scheme", "weight": 1.0} -->

We consider output measurements with bounded additive noise in the initially available data ${\overset{\sim}{y}}_{k}^{d} = {y_{k}^{d} + \varepsilon_{k}^{d}}$ as well as in the online measurements ${\overset{\sim}{y}}_{k} = {y_{k} + \varepsilon_{k}}$. We make no assumptions on the nature of the noise, but we require that it is bounded as ${\parallel\varepsilon_{k}^{d}\parallel}_{\infty} \leq \overline{\varepsilon}$ and ${\parallel\varepsilon_{k}\parallel}_{\infty} \leq \overline{\varepsilon}$ for some $\overline{\varepsilon} > 0$. Thus, the present setting includes two types of noise. The data used for the prediction via the Hankel matrices in (1.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-A Robust MPC scheme", "weight": 1.0} -->

‣ II Preliminaries ‣ Data-Driven Model Predictive Control with Stability and Robustness Guarantees")) is perturbed by $\varepsilon^{d}$, which can thus be interpreted as a multiplicative model uncertainty. On the other hand, $\varepsilon$ perturbs the online measurements and hence, the overall control goal is a noisy output-feedback problem.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-A Robust MPC scheme", "weight": 1.0} -->

The key idea to account for noisy measurements is to relax the equality constraint (3b), where the relaxation parameter is penalized appropriately in the cost function. Given a noisy initial input-output trajectory $\left( u_{\lbrack{t - n},{t - 1}\rbrack},{\overset{\sim}{y}}_{\lbrack{t - n},{t - 1}\rbrack} \right)$ of length $n$, and noisy data $(u^{d},{\overset{\sim}{y}}^{d})$, we propose the following robust modification of.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-A Robust MPC scheme", "weight": 1.0} -->

Compared to the nominal MPC problem, the output data trajectory ${\overset{\sim}{y}}^{d}$ as well as the initial output ${\overset{\sim}{y}}_{\lbrack{t - n},{t - 1}\rbrack}$, which is obtained via online measurements, have been replaced by their noisy counterparts.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-A Robust MPC scheme", "weight": 1.0} -->

A slack variable $\sigma$, bounded by (6d), to account for the noisy online measurements ${\overset{\sim}{y}}_{\lbrack{t - n},{t - 1}\rbrack}$ and for the noisy data ${\overset{\sim}{y}}^{d}$ used for prediction, which can be interpreted as a multiplicative model uncertainty,

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-A Robust MPC scheme", "weight": 1.0} -->

Quadratic regularization (i.e., *ridge regularization*) of $\alpha$ and $\sigma$ with weights ${{\lambda_{\alpha}\overline{\varepsilon}},\lambda_{\sigma}} > 0$, i.e., the regularization of $\alpha$ depends on the noise level.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-A Robust MPC scheme", "weight": 1.0} -->

The above $\ell_{2}$-norm regularization for $\alpha{(t)}$ implies that small values of ${\parallel{\alpha{(t)}}\parallel}_{2}^{2}$ are preferred. Since the noisy Hankel matrix $H_{L + n}\left( {\overset{\sim}{y}}^{d} \right)$ is multiplied by $\alpha{(t)}$ in (6a), this implicitly reduces the influence of the noise on the prediction accuracy. Intuitively, for increasing $\lambda_{\alpha}$, the term $\lambda_{\alpha}\overline{\varepsilon}{\parallel{\alpha{(t)}}\parallel}_{2}^{2}$ reduces the "complexity" of the data-driven system description (6a), similar to regularization methods in linear regression, thus allowing for a tradeoff between tracking performance and the avoidance of overfitting.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-A Robust MPC scheme", "weight": 1.0} -->

The term $\lambda_{\sigma}{\parallel{\sigma{(t)}}\parallel}_{2}^{2}$ yields small values for the slack variable $\sigma{(t)}$, thus improving the prediction accuracy. For our theoretical results, $\lambda_{\sigma}$ can be chosen to be zero since $\sigma{(t)}$ is already rendered small by the constraint (6d). However, as we discuss in more detail in Remark 3, the constraint (6d) is non-convex but can be neglected if $\lambda_{\sigma}$ is large enough.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-A Robust MPC scheme", "weight": 1.0} -->

An alternative to the present regularization terms are general quadratic regularization kernels, i.e., costs of the form ${\parallel{\alpha{(t)}}\parallel}_{P_{\alpha}}^{2}$, ${\parallel{\sigma{(t)}}\parallel}_{P_{\sigma}}^{2}$ for suitable matrices ${P_{\alpha},P_{\sigma}} \succ 0$. Further $\ell_{1}$-regularizations of $\alpha$ and $\sigma$ were suggested and the resulting MPC scheme, without terminal equality constraints, was successfully applied to a nonlinear stochastic control problem. However, theoretical guarantees on closed-loop stability were not given.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-A Robust MPC scheme", "weight": 1.0} -->

Throughout this paper, we consider simple quadratic penalty terms since this simplifies the arguments, but we conjecture that our theoretical results remain to hold for general norms ${\parallel{\alpha{(t)}}\parallel}_{p},{\parallel{\sigma{(t)}}\parallel}_{q}$ with arbitrary ${{p,q} = 1},{\ldots,\infty}$. An interesting open question, which is beyond the scope of this paper, is to investigate the impact of particular choices of regularization norms on the practical performance of the presented MPC approach. The choice of norms in the constraint (6d) is independent of the norms in the cost and essentially follows from the $\ell_{\infty}$-noise bound and the proofs of the value function upper bound (Lemma 1) and recursive feasibility (Proposition 1).

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-A Robust MPC scheme", "weight": 1.0} -->

In this section, we study the closed loop resulting from an application of in an $n$-step MPC scheme (compare ). To be more precise, we consider the scenario that, after solving online, the first $n$ computed inputs are applied to the system. Thereafter, the horizon is shifted by $n$ steps, before the whole scheme is repeated (compare Algorithm 2).

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-A Robust MPC scheme", "weight": 1.0} -->

At time t, take the past n measurements u[t − n, t − 1], ${\overset{\sim}{y}}_{\lbrack{t - n},{t - 1}\rbrack}$ and solve.
Apply the input sequence $u_{\lbrack t,{{t + n} - 1}\rbrack} = {{\overline{u}}_{\lbrack 0,{n - 1}\rbrack}^{\ast}{(t)}}$ over the next n time steps.
Set t = t + n and go back to 1).

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-A Robust MPC scheme", "weight": 1.0} -->

As we will see in the remainder of this section, for the considered setting with output measurement noise, the multi-step MPC scheme described in Algorithm 2 has superior theoretical properties compared to its corresponding $1$-step version. This is mainly due to the terminal equality constraints (6c), which complicate the proof of recursive feasibility, similar as in model-based robust MPC with terminal equality constraints and model mismatch. In particular, we show in this section that, for an $n$-step MPC scheme with a terminal equality constraint, practical exponential stability can be proven. On the other hand, we comment on the differences for the corresponding $1$-step MPC scheme in Section IV-D (Remark 4). In particular, for a $1$-step MPC scheme relying, recursive feasibility holds only locally around $(u^{s},y^{s})$ and thus, only local stability can be guaranteed. Nevertheless, as we will see in Section V for a numerical example, the practical performance of the $n$-step scheme is almost indistinguishable from the $1$-step scheme.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Remark 2", "weight": 1.0} -->

In the nominal case of Section III, i.e., for $\overline{\varepsilon} = 0$, (6d) implies $\sigma = 0$. Further, the regularization of $\alpha$ vanishes for $\overline{\varepsilon} = 0$, and the system dynamics (6a) as well as the initial conditions (6b) approach their nominal counterparts. Thus, for $\overline{\varepsilon} = 0$, Problem reduces to the nominal Problem.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Remark 3", "weight": 1.0} -->

If the constraint (6d) is neglected and the input constraint set $\mathbb{U}$ is a convex polytope, then Problem is a strictly convex quadratic program and can be solved efficiently. However, the constraint on the slack variable $\sigma$ in (6d) is non-convex due to the dependence of the right-hand side on ${\parallel{\alpha{(t)}}\parallel}_{1}$, making it difficult to implement in an efficient way. As will become clear later in this section, (6d) is required to prove recursive feasibility and practical exponential stability. It may, however, be replaced by the (convex) constraint ${\parallel{\sigma_{k}{(t)}}\parallel}_{\infty} \leq {c \cdot \overline{\varepsilon}}$ for a sufficiently large constant $c > 0$, retaining the same theoretical guarantees. Generally, a larger choice of $c$ increases the region of attraction, but also the size of the exponentially stable set to which the closed loop converges.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Furthermore, the constraint (6d) can be enforced implicitly by choosing $\lambda_{\sigma}$ large enough. In simulation examples, it was observed that the constraint (6d) is usually satisfied (for suitably large choices of $\lambda_{\sigma}$) without enforcing it explicitly in the optimization problem and thus, it may in most cases be neglected in the online optimization.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Remark 3", "weight": 1.0} -->

As in the previous section, we require that the measured input $u^{d}$ is persistently exciting of order $L + {2n}$ (Assumption 2). Further, to establish a local upper bound on the optimal cost of and to prove recursive feasibility, we require that the horizon $L$ is not shorter than twice the system's order, as captured in the following assumption.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

The prediction horizon satisfies $L \geq {2n}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

In some minimal realization, we denote the state trajectory corresponding to $(u^{d},y^{d})$ by $x^{d}$. According to \[12, Corollary 2\], Assumption 2 implies that the matrix

<!-- chunk {"id": "body-0049", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

For our stability results, we will require that $c_{pe}\overline{\varepsilon}$ is bounded from above by a sufficiently small number. Essentially, this corresponds to a quantitative "persistence-of-excitation-to-noise"-bound. To be more precise, abbreviate in the following $U = {H_{L + n}{(u^{d})}}$ and suppose that

<!-- chunk {"id": "body-0050", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

Thus, if a persistently exciting input $u^{d}$ is multiplied by a constant $c > 1$, then $c_{pe}^{u}$ decreases proportionally to $\frac{1}{c^{2}}$. Further, the constant $\rho$ can typically be chosen larger if the data length $N$ increases. The same arguments can be carried out when assuming a bound of the form for the matrix, but finding a suitable input which generates data achieving such a bound is less obvious. It is well-known for classical definitions of persistence of excitation that larger excitation of the input implies larger excitation of the state. Therefore, we conjecture (and we have observed for various practical simulation examples) that $c_{pe}$ decreases with increasing data horizons $N$ and with multiplications of a persistently exciting input data trajectory $u^{d}$ by a scalar constant greater than one.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

This means that, for a given noise level $\overline{\varepsilon}$, robust stability as guaranteed in the following sections can be obtained by choosing a large enough persistently exciting input $u^{d}$ and/or a sufficiently large data horizon $N$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

For the presented robust data-driven MPC scheme, setpoints ${(u^{s},y^{s})} \neq {}$ change mainly one quantitative constant in Lemma 1. We comment on the main differences in the case ${(u^{s},y^{s})} \neq {}$ in Section IV-D (Remark 5).

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-B Local upper bound of Lyapunov function", "weight": 1.0} -->

In this section, we show that the optimal cost of admits a quadratic upper bound, similar to the nominal case (cf. Assumption 1). It is straightforward to see that such an upper bound can not be quadratic in the state $x$ of some minimal realization: the optimal cost $J_{L}^{\ast}$ depends explicitly on $\alpha^{\ast}{(t)}$ via $\lambda_{\alpha}\overline{\varepsilon}{\parallel{\alpha^{\ast}{(t)}}\parallel}_{2}^{2}$, which in turn depends on the past $n$ inputs and outputs $(u_{\lbrack{t - n},{t - 1}\rbrack},y_{\lbrack{t - n},{t - 1}\rbrack})$ through (6a) and (6b).

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-B Local upper bound of Lyapunov function", "weight": 1.0} -->

Even if the current state is zero, i.e., $x_{t} = 0$, these may in general be arbitrarily large and hence, $\alpha$ and therefore also $J_{L}^{\ast}$ may be arbitrarily large. Thus, $J_{L}^{\ast}$ does not admit an upper bound in the state $x_{t}$ of a minimal realization. To overcome this issue, we consider a different (not minimal) state of the system, defined as

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-B Local upper bound of Lyapunov function", "weight": 1.0} -->

Further, we define the noisy version of $\xi$ as

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-B Local upper bound of Lyapunov function", "weight": 1.0} -->

Note that $\xi$ is the state of a detectable state-space realization and thus, there exists an IOSS Lyapunov function ${W{(\xi)}} = {\parallel\xi\parallel}_{P}^{2}$, similar to the proof of Theorem 2. For some $\gamma > 0$, define $V_{t} ≔ {{J_{L}^{\ast}{({\overset{\sim}{\xi}}_{t})}} + {\gammaW{(\xi_{t})}}}$. The following result shows that, for the state $\xi$, a meaningful quadratic upper bound on $V$ can be proven.

<!-- chunk {"id": "body-0057", "role": "body", "section": "IV-C Prediction error bound", "weight": 1.0} -->

Denote the optimizers of by ${\alpha^{\ast}{(t)}},{\sigma^{\ast}{(t)}},{{\overline{u}}^{\ast}{(t)}},{{\overline{y}}^{\ast}{(t)}}$, and the output trajectory resulting from an open-loop application of ${\overline{u}}^{\ast}{(t)}$ by $\hat{y}$. One of the reasons why it is difficult to analyze the presented MPC scheme is the non-trivial relation between the predicted output ${\overline{y}}^{\ast}{(t)}$ and the "actual" output $\hat{y}$. In the following, we derive a bound on the difference between the two quantities, which will play an important role in proving recursive feasibility and practical stabiliy of the proposed scheme.

<!-- chunk {"id": "body-0058", "role": "body", "section": "IV-C Prediction error bound", "weight": 1.0} -->

For an integer $k$, define constants $\rho_{2,k},\rho_{\infty,k}$ such that

<!-- chunk {"id": "body-0059", "role": "body", "section": "IV-C Prediction error bound", "weight": 1.0} -->

where $\Phi_{\dagger}$ is a left-inverse of the observability matrix $\Phi$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "IV-D Recursive feasibility", "weight": 1.0} -->

The following result shows that, if the proposed robust MPC scheme is feasible at time $t$, then it is also feasible at time $t + n$, assuming that the noise level is sufficiently small.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Remark 4", "weight": 1.0} -->

For a $1$-step MPC scheme, a similar argument to prove recursive feasibility can be applied, given that ${\overline{u}}_{\lbrack{L - {2n}},{L - n - 1}\rbrack}^{\ast}{(t)}$ and ${\overline{y}}_{\lbrack{L - {2n}},{L - n - 1}\rbrack}^{\ast}{(t)}$ (and hence ${\hat{y}}_{\lbrack{{t + L} - {2n}},{{t + L} - n - 1}\rbrack}$) are close to zero. This is required to construct a feasible input which steers the state and the corresponding output to zero, similar to the proof of Proposition 1, and it is, e.g., the case if the initial state $x_{t}$ is close to zero.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Remark 4", "weight": 1.0} -->

That is, the result of Proposition 1 holds locally for a $1$-step MPC scheme, as expected based on model-based MPC with terminal equality constraints under disturbances using inherent robustness properties.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Remark 5", "weight": 1.0} -->

On the other hand, ${\overset{\sim}{c}}_{4}$ changes depending on $\xi^{s}$, since the right-hand side of would need to be proportional to $\parallel\xi_{t} - \xi^{s} \parallel_{2}^{2} + {\parallel\xi^{s}\parallel}_{2}^{2}$. The same phenomenon can be observed in a bound of $\alpha^{\prime}{({t + n})}$ based, which will be used in the stability proof. As will become clear later in this section, such changes in the bound of $\alpha^{\prime}{({t + n})}$ as well as in the constant ${\overset{\sim}{c}}_{4}$ do not affect our qualitative theoretical results, but they may potentially (quantitatively) deterioriate the robustness w.r.t. the noise level $\overline{\varepsilon}$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Remark 5", "weight": 1.0} -->

Intuitively, this can be explained by noting that (6a) corresponds to a multiplicative uncertainty and thus, stabilization of the origin is simpler than stabilization of any other equilibrium. Since equilibria with ${(u^{s},y^{s})} \neq 0$ require a significantly more involved notation, we omit this extension.

<!-- chunk {"id": "body-0065", "role": "body", "section": "IV-E Practical exponential stability", "weight": 1.0} -->

The following is our main stability result. It shows that, under Assumptions 2 and 4, for a low noise amplitude and large persistence of excitation, and for suitable regularization parameters, the application of the scheme as described in Algorithm 2 leads to a practically exponentially stable closed loop.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Remark 6", "weight": 1.0} -->

To apply the proposed data-driven MPC scheme in practice, the following ingredients are required. First of all, the design parameters in the cost, i.e., $Q,R,\lambda_{\alpha},\lambda_{\sigma}$, have to be selected suitably. The proof and discussion of Theorem 3 give a qualitative guideline for choosing the regularization parameters. Further, as in the nominal case (Section III), measured data with a persistently exciting input as well as a (potentially rough) upper bound on the system's order need to be available. Finally, an upper bound on the noise level $\overline{\varepsilon}$ is required.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Remark 6", "weight": 1.0} -->

While these ingredients suffice to apply the proposed scheme, computing bounds as in and is a difficult task in practice. Theorem 3 should be interpreted as a qualitative result which illustrates a) the influence of the regularization parameters on stability and robustness of the presented MPC scheme and b) that large persistence of excitation (compared to the noise level) increases the region of attraction and reduces the tracking error. Further, many of the employed bounds rely on conservative estimates such as ${({a + b})}^{2} \leq {{2a^{2}} + {2b^{2}}}$. In principle, it is possible to improve some of the quantitative estimates at the price of a more involved notation. Nevertheless, such improved estimates may lead to meaningful, non-conservative, verifiable conditions on the noise level $\overline{\varepsilon}$ for closed-loop stability, and are therefore an interesting issue for future research.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Remark 7", "weight": 1.0} -->

In the nominal MPC scheme as well as in its robust modification, the data $(u^{d},y^{d})$ used for prediction is fixed. Alternatively, one may update the data using online measurements, given that the closed loop is persistently exciting. Indeed, we believe that one of the main advantages of the proposed scheme is its ability to cope (locally) with nonlinear components of the unknown system. Nonlinear dynamical systems are in general difficult to identify and thus, the proposed approach may be simpler than a model-based MPC scheme with prior system identification. As illustrated in with an application of a similar MPC scheme to a nonlinear stochastic quadcopter system, the approach is already applicable in practice to time-varying or nonlinear dynamics without updating the data online. Providing theoretical guarantees for the application of the proposed scheme to a nonlinear system is an interesting and relevant problem for future research.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Remark 7", "weight": 1.0} -->

Similar to the nominal MPC scheme, it is easy to see that the only free decision variables of Problem are $\alpha{(t)}$ and $\sigma{(t)}$ with at least ${m{({L + {2n}})}} + n$ and $p{({L + n})}$ free parameters, respectively (cf. Remark 1). On the contrary, to implement a model-based MPC scheme (with state measurements), $mL$ parameters are required. When neglecting the constraint (6d) (cf. Remark 3), the slack variable $\sigma{(t)}$ can be eliminated from by directly penalizing the norm of the model mismatch ${\overline{y}{(t)}} - {H_{L + n}{({\overset{\sim}{y}}^{d})}\alpha{(t)}}$ in the cost. Hence, considering the minimal amount of data required for persistence of excitation, Problem has roughly the same number of decision variables as a model-based MPC problem.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Remark 7", "weight": 1.0} -->

In contrast to the nominal case, however, Theorem 3 implies that larger data horizons $N$ are beneficial for the theoretical properties of the proposed scheme as they typically decrease the constant $c_{pe}$. On the other hand, increasing values for $N$ also lead to an increasing online complexity of since ${\alpha{(t)}} \in {\mathbb{R}}^{{N - L} + 1}$, i.e., the presented MPC approach allows for a tradeoff between computational complexity and desired closed-loop performance by appropriately selecting $N$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Remark 7", "weight": 1.0} -->

On the contrary, the performance of identification-based MPC typically improves if larger amounts of data are employed, whereas the online complexity is independent of $N$. However, while the scheme presented in this paper provides end-to-end guarantees for the closed loop using noisy data of finite length, the derivation of non-conservative estimation bounds on system parameters from such data, which would be required for guarantees in model-based MPC, is difficult in general and an active field of research. An extensive *quantitative* comparison of model-based MPC and the proposed data-driven MPC in theory and for practical examples is an interesting issue for future research.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Example", "weight": 1.0} -->

In this section, we apply the robust data-driven MPC scheme of Section IV to a four tank system, which has been considered. This system is well-known as a real-world example, which is open-loop stable, but can be destabilized by an MPC without terminal constraints if the prediction horizon is too short. Similarly, we show in this section that our proposed scheme is able to track a specified setpoint, whereas a scheme without terminal constraints as suggested in leads to an unstable closed loop, unless it is suitably modified.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Example", "weight": 1.0} -->

We consider a linearized version of the system, which takes the form

<!-- chunk {"id": "body-0074", "role": "body", "section": "Example", "weight": 1.0} -->

For the following application of the robust data-driven MPC scheme, the system matrices are *unknown* and only measured input-output data is available. The control goal is tracking of the setpoint of the linearized system

<!-- chunk {"id": "body-0075", "role": "body", "section": "Example", "weight": 1.0} -->

which is readily shown to satisfy the dynamics. We consider no constraints on the input or the output. In an open-loop experiment, an input-output trajectory of length $N = 400$ is measured, where the input is chosen randomly from the unit interval, i.e., $u_{k}^{d} \in {\lbrack{- 1},1\rbrack}^{2}$, and the output is subject to uniformly distributed additive measurement noise with bound $\overline{\varepsilon} = 0.002$. The online measurements used to update the initial conditions (6b) in the MPC scheme are subject to the same type of noise.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Example", "weight": 1.0} -->

We choose $L = 30$ for the prediction horizon as well as the following design parameters

<!-- chunk {"id": "body-0077", "role": "body", "section": "Example", "weight": 1.0} -->

The closed-loop output resulting from the application of Problem in a $1$-step MPC scheme is displayed in Figure 2. It can be seen that the control goal is fulfilled, with only slight deviations from the desired equilibrium. On the other hand, if the same scheme without terminal constraints is applied to the system, then the closed loop is unstable and diverges with the chosen parameters for both a $1$-step and an $n$-step MPC scheme (cf. again Figure 2). This confirms our initial motivation that rigorous guarantees are indeed desirable for data-driven MPC methods, in particular when they are applied to practical systems. Furthermore, it can also be observed in Figure 2 that an $n$-step version of the proposed MPC scheme with terminal equality constraints yields slightly better tracking accuracy, compared to the $1$-step scheme. We note that, with the above choice of parameters, the non-convex constraint (6d) is automatically satisfied without enforcing it explicitly (cf. Remark 3).

<!-- chunk {"id": "body-0078", "role": "body", "section": "Example", "weight": 1.0} -->

Theorem 3 gives qualitative guidelines for the tuning of the design parameters to guarantee robust stability. In the following, we analyze the influence of various parameters on the closed-loop behavior. Theorem 3 requires that the regularization parameters lie within specific bounds. This is confirmed for the present example, where the MPC scheme achieves desirable closed-loop performance similar to Figure 2 as long as $0.05 \leq {\lambda_{\alpha}\overline{\varepsilon}} \leq 0.5$. If $\lambda_{\alpha}$ is chosen too low, then the closed loop is unstable since the norm of $\alpha^{\ast}{(t)}$ and hence the amplification of the measurement noise in (6a) is too large. On the contrary, if $\lambda_{\alpha}$ is chosen too large, then the asymptotic tracking error increases since the cost term $\lambda_{\alpha}\overline{\varepsilon}{\parallel{\alpha^{\ast}{(t)}}\parallel}_{2}$ dominates over the tracking cost.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Example", "weight": 1.0} -->

Similarly, if $\lambda_{\sigma} < 500$, then the closed loop may be unstable since we did not consider the constraint (6d) and therefore the slack variable is too large, which has a negative impact on the prediction accuracy. An upper bound on $\lambda_{\sigma}$ beyond which the closed-loop behavior is undesirable could not be observed for the present example. Further, if the input weighting $R$ is chosen too low, then the robustness with respect to the noise deteriorates, which can be explained via the bound, which grows with ${1/\lambda_{\min}}{(R)}$. If the input weighting is chosen large enough, then also an MPC scheme without terminal constraints stabilizes the desired equilibrium.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Example", "weight": 1.0} -->

Regarding the knowledge of the system order $n = 4$, it suffices if an upper bound on $n$ is available, i.e., if for instance $n = 10$ is used. If the system order is assumed lower than $n = 4$, then the closed loop can be unstable. The prediction horizon $L$ can be chosen (roughly) between $7 \leq L \leq 70$. The upper bound can be explained by noting that a larger $L$ implies that the constant $c_{pe}$ increases (compare the discussion after ) and therefore, the asymptotic tracking error increases. On the other hand, the lower bound is due to the terminal equality constraints which require local controllability. Moreover, the steady-state tracking error, which can be seen e.g. in Figure 2 (b), may increase or decrease, depending on the particular noise instance, and generally increases with the noise level $\overline{\varepsilon}$. This confirms again the analysis of Section IV, which showed exponential stability of a set which grows with the noise level.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Example", "weight": 1.0} -->

Finally, if the norm of the data input $u^{d}$ increases (i.e., $c_{pe}$ decreases), then the tracking error decreases.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In the present paper, we proposed and analyzed a novel MPC scheme with terminal equality constraints, which uses only past measured data for the prediction, without any prior system identification step. We showed that, for a low noise amplitude, for a large ratio between persistence of excitation and the noise level, and for suitably tuned parameters, the closed loop in an $n$-step MPC scheme is recursively feasible and practically exponentially stable w.r.t. the noise level. To the best of our knowledge, we have provided the first analysis regarding recursive feasibility and stability for a purely data-driven (model-free) MPC scheme. Further, the analysis provides qualitative guidelines to choose the design parameters, and it illustrates the influence of other parameters, such as a persistence of excitation bound, on the region of attraction. While the MPC scheme is simple to implement, its analysis is challenging since we consider two sorts of noise: a) additive output noise and b) in the prediction model, similar to a multiplicative, parametric error in model-based MPC.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In an application to a practical example, we showed that the proposed MPC scheme guarantees stability, whereas an existing data-driven MPC scheme without terminal constraints leads to an unstable closed loop.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Several topics for future research are left open. Extensions of the presented data-driven MPC approach to online optimization over artificial equilibria and robust output constraint satisfaction are provided in the recent works and, respectively. Another extension, which would be highly interesting but also challenging, is the development of data-driven MPC schemes for *nonlinear* systems with meaningful closed-loop guarantees. Finally, many of the bounds employed in our proofs are conservative, and improving them may lead to less conservative, verifiable conditions on the admissible noise level for closed-loop stability.
