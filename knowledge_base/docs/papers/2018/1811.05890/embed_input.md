<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Data-Enabled Predictive Control: In the Shallows of the DeePC

Topics include Model predictive control, Predictive control, Safety, Real-time systems, Online algorithms, Control, DeePC.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider the problem of optimal trajectory tracking for unknown systems. A novel data-enabled predictive control (DeePC) algorithm is presented that computes optimal and safe control policies using real-time feedback driving the unknown system along a desired trajectory while satisfying system constraints. Using a finite number of data samples from the unknown system, our proposed algorithm uses a behavioural systems theory approach to learn a non-parametric system model used to predict future trajectories. The DeePC algorithm is shown to be equivalent to the classical and widely adopted Model Predictive Control (MPC) algorithm in the case of deterministic linear time-invariant systems. In the case of nonlinear stochastic systems, we propose regularizations to the DeePC algorithm. Simulations are provided to illustrate performance and compare the algorithm with other methods.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

As systems are becoming more complex and data is becoming more readily available, scientists and practitioners are beginning to bypass classical model-based techniques in favour of data-driven methods. Data-driven methods are suitable for applications where first-principle models are not conceivable (e.g., in human-in-the-loop applications), when models are too complex for control design (e.g., in fluid dynamics), and when thorough modelling and parameter identification is too costly (e.g., in robotics). In fact, it is sometimes easier to learn control policies directly from data, rather than learning a model (the quintessential example supporting this claim is PID control ).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A challenging problem in systems control is optimal trajectory tracking, where a control policy is computed based on output feedback that drives a dynamical system along a desired output trajectory while minimizing a stage cost and respecting safety constraints. A special case of the trajectory tracking problem is regulation, in which a control policy drives the system to an equilibrium point. One of the most celebrated and widely used control techniques for trajectory tracking is receding horizon Model Predictive Control (MPC), precisely because it allows one to include safety considerations during control design. Applications in which trajectory tracking is approached via MPC include autonomous driving, autonomous flight, mobile robots, and smart energy systems, among others. The key ingredient for MPC is an accurate parametric state space model of the system (represented by state space matrices), but obtaining such a model is often the most time-consuming and expensive part of control design.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the context of unknown black-box systems, there is no approach which solves the optimal trajectory tracking problem subject to constraints and partial (output) observations. However, some more benign variations of the optimal trajectory tracking problem have been approached using data-driven and learning based methods. We do not attempt to provide a comprehensive survey of the recent, albeit already vast, literature. Rather, we single out a few references that are representative for (and at the forefront of) different approaches in the literature.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We begin with reinforcement learning approaches in which control actions are chosen to maximize a reward. This requires either exploring the system via random control actions, or exploiting the knowledge gained by applying optimal control actions. Reinforcement learning approaches usually require a large number of data samples to perform well, and are often very sensitive to hyper-parameters leading to non-reproducible and highly variable outcomes. Additionally, these approaches do not address all of the challenges present in the optimal trajectory tracking problem; namely, they generally do not take into account safety constraints, and typically assume full state feedback.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Other approaches propose performing sequential system identification (ID) and control. System ID can be used to produce an approximate model as well as provide finite sample guarantees quantifying model uncertainty, thus allowing for robust control design. In this spirit, an end-to-end ID and control pipeline is given in and arrives at a data-driven control solution with guarantees on the sample efficiency, stability, performance, and robustness. The system identification step in these approaches disregards one of the main advantages of a data-driven approach: independence from an underlying parametric representation (e.g., state space representation). In fact, non-parametric learning approaches often outperform parametric approaches (see, e.g., Gaussian processes for regression ). Additionally, they only consider regulation, rely on having full state information, and do not enforce constraint satisfaction.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Beyond reinforcement learning and sequential ID and control, there are many other adaptive control and safe learning approaches. However, they rely on a-priori stabilizing controllers and safe regions, and thus apply only to a small class of problems.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

MPC based on Dynamic Matrix Control has been historically used as a data-driven control technique, in which zero-initial condition step responses are used to predict future trajectories. Although this technique has many limitations, it motivates the use of a non-parametric predictive control model. Other non-parametric predictive models have been proposed. These methods do not solve the problem of optimal trajectory tracking with constraints, but serve as building blocks for our approach.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Here we present a Data-enabled Predictive Control (DeePC) algorithm. Unlike classical MPC and the learning-based control techniques outlined above, the DeePC algorithm does not rely on a parametric system representation. Instead, similar to, we approach the problem from a behavioural systems theory perspective. Rather than attempting to learn a parametric system model, we aim at learning the system's "behaviour" (see Section IV for the precise definition). Our novel predictive control strategy computes optimal controls for unknown systems using real-time output feedback via a receding horizon implementation, allowing one to incorporate input/output constraints to ensure safety. We formally show the equivalence of the DeePC algorithm to the classical MPC algorithm in the special case of deterministic linear time-invariant (LTI) systems. Our approach is much simpler to implement than the learning-based techniques above, as well as model-based approaches which require system identification and state observer design. In contrast to most MPC formulations (where full state measurement is required), the DeePC algorithm only requires output measurements. Additionally, since our approach does not rely on a parametric system model, we are hopeful that it can also be applied beyond deterministic LTI systems.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

To apply the algorithm to such systems, we propose some preliminary though insightful regularizations (e.g., low-rank approximations, and introduction of auxiliary slack variables ), and reason as to why these regularizations improve performance. All of the results are validated with a nonlinear and stochastic aerial robotics case study, in which the DeePC algorithm is shown to outperform sequential ID with MPC.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of the paper is organized as follows: in Section II, we formally define the problem. In Section III we review the basic notion of MPC. In Section IV we introduce behavioural system theory. Section V contains the DeePC algorithm. In Section VI we simulate the DeePC algorithm and compare it with sequential ID and MPC using a quadcopter simulation. We conclude the paper in Section VII.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Consider the discrete-time system given by

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Given a desired reference trajectory $r = {(r_{0},r_{1},\ldots)} \in {({}_{}^{}}^{{\mathbb{Z}}_{\geq 0}}$, input constraint set $\mathcal{U} \subseteq^{m}$, output constraint set $\mathcal{Y} \subseteq^{p}$, we wish to apply control inputs such that the system output tracks the reference trajectory $r$ while satisfying constraints and optimizing a cost function. Tracking of the trivial trajectory $r = {(0,0,\ldots)}$ is simply regulation.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

In the case when the model for the system is *known*, i.e., matrices $A$, $B$, $C$ and $D$ are known, the problem can be approached using MPC (see Section III). This paper focuses on the above trajectory tracking problem in the case when the model for system is *unknown*, but input/output data samples are available.

<!-- chunk {"id": "body-0016", "role": "body", "section": "MPC: A Brief Overview", "weight": 1.0} -->

We outline the well-known receding-horizon model predictive control and estimation algorithm for trajectory tracking when the model of system is known (see, e.g., ).

<!-- chunk {"id": "body-0017", "role": "body", "section": "MPC: A Brief Overview", "weight": 1.0} -->

The norm ${\| u_{k}\|}_{R}$ denotes the quadratic form $u_{k}^{T}Ru_{k}$ (similarly for $\parallel \cdot \parallel_{Q}$), where $R \in^{m \times m}$ is the control cost matrix and $Q \in^{p \times p}$ is the output cost matrix. The estimated state at time $t$ is denoted by $\hat{x}{(t)}$ and the predicted state and output at time $t + k$ are denoted by $x_{k}$ and $y_{k}$, respectively. If the entire state is measured then ${\hat{x}{(t)}} = {x{(t)}}$. When the state measurement is not available, but system is observable, an observer is typically used to estimate the state based on knowledge of the system and the measured output $y$. One may also combine the control and estimation into a single min-max optimization problem.

<!-- chunk {"id": "body-0018", "role": "body", "section": "MPC: A Brief Overview", "weight": 1.0} -->

The classical MPC algorithm involves solving optimization problem (III) in a receding horizon manner.

<!-- chunk {"id": "body-0019", "role": "body", "section": "MPC: A Brief Overview", "weight": 1.0} -->

Input: (A,B,C,D), reference trajectory r, past input/output data (u,y), constraint sets 𝒰 and 𝒴, and performance matrices Q and R

<!-- chunk {"id": "body-0020", "role": "body", "section": "MPC: A Brief Overview", "weight": 1.0} -->

Generate state estimate x̂ (t) using past input/output data.
Solve (III) for u⋆ = (u0⋆,…,uN − 1⋆).
Apply inputs (u (t),…,u (t+s)) = (u0⋆,…,us⋆) for some s ≤ N − 1.
Set t to t + s and update past input/output data.

<!-- chunk {"id": "body-0021", "role": "body", "section": "MPC: A Brief Overview", "weight": 1.0} -->

Note that choosing $s > 0$ reduces the number of computations, and in some cases may improve performance.

<!-- chunk {"id": "body-0022", "role": "body", "section": "MPC: A Brief Overview", "weight": 1.0} -->

Under standard assumptions, it can be shown that the MPC algorithm is recursively feasible and stabilizing. One crucial ingredient for MPC is an accurate model of the system; this is needed both to formulate problem (III) and, in cases where the state is not measured exactly, to generate the initial state estimates $\hat{x}{(t)}$. The need for a model is traditionally addressed through system identification, where observations of the system are collected offline before the online control operation begins and are used to estimate a model of the form that matches the observed data in an appropriate sense. For complex systems, this can be a cumbersome and expensive process. For this reason, we propose a Data-enabled Predictive Control (DeePC) algorithm which learns the behaviour of the system and does not require an explicit model, system identification, or state estimation (see Algorithm 2).

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-A Non-parametric system representation", "weight": 1.0} -->

Behavioural system theory is a natural way of viewing a dynamical system when one is not concerned with a particular system representation, but rather the subspace of the signal space in which trajectories of the system live. This is in contrast with classical system theory, where a particular parametric system representation (such as the state-space model ) is used to describe the input/output behaviour, and properties of the system are derived by studying the chosen system representation. Following, we define a dynamical system and its properties in terms of its behaviour.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-B Parametric system representation", "weight": 1.0} -->

There are several equivalent ways of representing a behavioural system $\mathcal{B} \in \mathcal{L}^{m + p}$, including the classical input/output/state representation denoted by $\mathcal{B}{(A,B,C,D)} = {\{\text{col}{(u,y)} \in {({}_{}^{m + p}}^{{\mathbb{Z}}_{\geq 0}} \mid \exists x \in {({}_{}^{}}^{{\mathbb{Z}}_{\geq 0}}\text{s.t.}\sigma x = Ax + Bu,y = Cx + Du\}}$. The input/output/state representation of smallest order (i.e., smallest state dimension) is called a *minimal representation*, and we denote its order by ${\mathbf{n}}{(\mathcal{B})}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-B Parametric system representation", "weight": 1.0} -->

Another important property of a system $\mathcal{B} \in \mathcal{L}^{m + p}$ is the *lag* defined by the smallest integer $\ell \in {\mathbb{Z}}_{> 0}$ such that the observability matrix ${\mathcal{O}_{\ell}{(A,C)}}:={\text{col}\left( C,{CA},\ldots,{CA^{\ell - 1}} \right)}$ has rank ${\mathbf{n}}{(\mathcal{B})}$. We denote the lag by $\mathbf{\ell}{(\mathcal{B})}$ (see \[38, Section 7.2\] for equivalent input/output/state representation free definitions of lag). The lower triangular Toeplitz matrix consisting of $A,B,C,D$ is denoted by

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-B Parametric system representation", "weight": 1.0} -->

We can now present a uniqueness result.

<!-- chunk {"id": "body-0027", "role": "body", "section": "V-A Data collection", "weight": 1.0} -->

Note that the data ${\text{col}{(u^{\text{d}},y^{\text{d}})}} \in \mathcal{B}_{T}$ can be equivalently thought of as coming from the minimimal input/output/state representation $\mathcal{B}{(A,B,C,D)}$. Next, we partition the input/output data into two parts which we call *past data* and *future data*. More formally, define

<!-- chunk {"id": "body-0028", "role": "body", "section": "V-A Data collection", "weight": 1.0} -->

where $U_{p}$ consists of the first $T_{\text{ini}}$ block rows of $\mathcal{H}_{T_{\text{ini}} + N}{(u^{\text{d}})}$ and $U_{f}$ consists of the last $N$ block rows of $\mathcal{H}_{T_{\text{ini}} + N}{(u^{\text{d}})}$ (similarly for $Y_{p}$ and $Y_{f}$). In the sequel, past data denoted by the subscript $p$ will be used to estimate the initial condition of the underlying state, whereas the future data denoted by the subscript $f$ will be used to predict the future trajectories.

<!-- chunk {"id": "body-0029", "role": "body", "section": "V-B State estimation and trajectory prediction", "weight": 1.0} -->

If $T_{\text{ini}} \geq {\mathbf{\ell}{(\mathcal{B})}}$, then Lemma IV.1 implies that there exists a unique $x_{\text{ini}} \in^{{\mathbf{n}}{(\mathcal{B})}}$ such that the output $y$ is uniquely determined. Intuitively, the trajectory $\text{col}{(u_{\text{ini}},y_{\text{ini}})}$ fixes the underlying initial state $x_{\text{ini}}$ from which the trajectory $\text{col}{(u,y)}$ evolves. Note, however, that does not require the input/output/state representation of the system to be known. The state $x_{\text{ini}}$ is only "fixed" implicitly by $\text{col}{(u_{\text{ini}},y_{\text{ini}})}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "V-B State estimation and trajectory prediction", "weight": 1.0} -->

The sequence of future outputs are then given by $y = {Y_{f}g}$. Furthermore, by Lemma IV.1 the vector $y$ computed contains the unique sequence of outputs corresponding to the inputs $u$. Vice versa, given a desired reference output $y$ an associated feedforward control input can be calculated.

<!-- chunk {"id": "body-0031", "role": "body", "section": "V-C DeePC algorithm", "weight": 1.0} -->

Note here, that $u$ and $y$ are not independent decision variables of the optimization problem. Rather they are described completely by the fixed data matrices $U_{f}$ and $Y_{f}$ and the decision variable $g$. A comparison of the two optimal control problems (III) and (V-C) yields only a single (though key) difference; the model and the state estimate in (III) are replaced completely with input/output data samples in (V-C). We now present the DeePC algorithm.

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-C DeePC algorithm", "weight": 1.0} -->

Input: col (ud,yd) ∈ ℬT, reference trajectory r∈N p, past input/output data col (uini,yini) ∈ ℬTini, constraint sets 𝒰 and 𝒴, and performance matrices Q and R

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-C DeePC algorithm", "weight": 1.0} -->

Solve (V-C) for g⋆.
Compute the optimal input sequence u⋆ = Uf g⋆.
Apply input (u (t),…,u (t+s)) = (u0⋆,…,us⋆) for some s ≤ N − 1.
Set t to t + s and update uini and yini to the Tini most recent input/output measurements.

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-D Equivalence of DeePC and MPC", "weight": 1.0} -->

It can be shown that Algorithm 1 and Algorithm 2 yield equivalent closed-loop trajectories under certain assumptions. We first show the equivalence of the feasible sets of (III) and (V-C).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Beyond deterministic LTI systems", "weight": 1.0} -->

In this section we provide preliminary results which shows the promising extension of the DeePC algorithm beyond deterministic LTI systems. We offer insightful algorithmic extensions by means of salient regularizations, show their utility through a numerical study, and provide plausible reasoning for the regularizations.

<!-- chunk {"id": "body-0036", "role": "body", "section": "VI-A Regularized DeePC Algorithm", "weight": 1.0} -->

Consider now the nonlinear discrete-time system given by

<!-- chunk {"id": "body-0037", "role": "body", "section": "VI-A Regularized DeePC Algorithm", "weight": 1.0} -->

where $\eta{(t)} \in^{p}$ is white measurement noise, and $f:{}_{}^{}{}_{}^{}^{n}$ and $h:{}_{}^{}{}_{}^{}{}_{}^{}^{p}$ are not necessarily linear. One may also consider a system affected by process noise. However, we focus on systems only affected by measurement noise in order to isolate its effect on the DeePC algorithm. To apply the DeePC algorithm to system, we propose three regularizations to the optimal control problem (V-C).

<!-- chunk {"id": "body-0038", "role": "body", "section": "VI-A Regularized DeePC Algorithm", "weight": 1.0} -->

Slack variable: When the output measurements are corrupted by noise, the constraint equation in (V-C) may become inconsistent. Hence, in (VI-A) we include the slack variable $\sigma_{y}$ in the constraint to ensure feasibility of the constraint at all times. We penalize the slack variable with a weighted one-norm penalty function. Choosing $\lambda_{y}$ sufficiently large gives the desired property that $\sigma_{y} \neq 0$ only if the constraint is infeasible (see, e.g., ), that is, only if the data is inconsistent.

<!-- chunk {"id": "body-0039", "role": "body", "section": "VI-A Regularized DeePC Algorithm", "weight": 1.0} -->

One-norm regularization on $g$: The cost includes a one-norm penalty on $g$. We conjecture that this regularization is related to distributionally robust optimization problems, in which similar regularization terms arise.

<!-- chunk {"id": "body-0040", "role": "body", "section": "VI-A Regularized DeePC Algorithm", "weight": 1.0} -->

Low-rank approximation: By performing a low-rank matrix approximation (e.g., via singular value decomposition (SVD) and truncation ), we take into account only the most dominant sub-behaviour (corresponding to the largest singular values), resulting in a data matrix describing the behaviour of the closest deterministic LTI system (where "closest" is measured with the Frobenius norm in the SVD case). In the case of noisy measurements, the SVD filters the noise. In the case of nonlinear dynamics (which can be lifted to infinite-dimensional linear dynamics with a nonlinear output map ), the SVD results in a matrix describing an approximate LTI model, i.e., the most relevant basis functions of the infinite-dimensional lift whose dimension can be chosen by adjusting the SVD cutoff.

<!-- chunk {"id": "body-0041", "role": "body", "section": "VI-A Regularized DeePC Algorithm", "weight": 1.0} -->

Note that after performing the low-rank approximation, the DeePC algorithm does not require that the matrix $\text{col}{({\hat{U}}_{p},{\hat{Y}}_{p},{\hat{U}}_{f},{\hat{Y}}_{f})}$ have a Hankel structure. This is in contrast to subspace ID techniques, in which low-rank approximations must be carefully modified in order to preserve the Hankel structure of the data matrix resulting in higher algorithmic and computational complexity.

<!-- chunk {"id": "body-0042", "role": "body", "section": "VI-B Aerial Robotics Case Study", "weight": 1.0} -->

We illustrate the performance of the regularized DeePC algorithm, i.e., Algorithm 2 with (VI-A), by simulating it on a high-fidelity nonlinear quadcopter model, and compare the performance to system identification (ID) followed by MPC using the identified model. The states of the quadcopter model are given by the 3 spatial coordinates ($x$, $y$, $z$) and their velocities, and the 3 angular coordinates $(\alpha,\beta,\gamma)$ and their velocities, i.e., the state is $(x,y,z,\overset{˙}{x},\overset{˙}{y},\overset{˙}{z},\alpha,\beta,\gamma,\overset{˙}{\alpha},\overset{˙}{\beta},\overset{˙}{\gamma})$. The inputs are given by the thrusts from the 4 rotors, $(u_{1},u_{2},u_{3},u_{4})$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "VI-B Aerial Robotics Case Study", "weight": 1.0} -->

We assume full state measurement to facilitate the comparison to standard MPC. Data was collected from the nonlinear model subject to additive white measurement noise. We collected 214 input/output measurements with a sample time of 0.1 seconds. Drawing the input sequence from a uniformly distributed random variable ensured that the data was persistently exciting. For the model-based MPC, the data was used to identify the system parameters through the least square prediction error method with an assumed state dimension of 12.

<!-- chunk {"id": "body-0044", "role": "body", "section": "VI-B Aerial Robotics Case Study", "weight": 1.0} -->

We simulated the system ID followed by the MPC algorithm and the regularized DeePC algorithm on the nonlinear and stochastic quadcopter model in which the quadcopter was commanded to follow a series of figure-eight trajectories for a duration of 60 seconds. We observe that DeePC performs better than sequential ID and MPC in terms of reference tracking and constraint satisfaction; see Figure 1 for an illustration.

<!-- chunk {"id": "body-0045", "role": "body", "section": "VI-B Aerial Robotics Case Study", "weight": 1.0} -->

Another simulation was performed in which the quadcopter was commanded to perform a simple step trajectory in the $(x,y,z)$ coordinates with the same constraints listed above. The duration of constraint violations and the cost were measured. This was repeated 30 times with different data sets for constructing $\text{col}{(U_{p},Y_{p},U_{f},Y_{f})}$, and different random seeds for the measurement noise. The results are displayed in Figure 2 and show that DeePC consistently outperforms identification-based MPC in terms of cost and constraint satisfaction. While these observations should be made cautiously, an intuitive explanation for the superior performance of DeePC is that (VI-A) simultaneously optimizes for the best system model, state estimation, and control policy, whereas conventional MPC requires fixing a system model and performs these tasks independently.

<!-- chunk {"id": "body-0046", "role": "body", "section": "VI-B Aerial Robotics Case Study", "weight": 1.0} -->

To study the effect of the regularizations on the performance of the DeePC algorithm, we performed a sensitivity analysis on the regularization parameters $\lambda_{y}$ and $\lambda_{g}$. We did not perform any low-rank approximation to the data. The quadcopter was commanded to follow the same step trajectory as in the previous simulation. The duration of constraint violations and cost were measured. This was repeated 8 times with different data sets, and the duration of constraint violations and cost were averaged over these 8 data sets. The results in Figure 3 show that the regularizations improve performance.

<!-- chunk {"id": "body-0047", "role": "body", "section": "VI-B Aerial Robotics Case Study", "weight": 1.0} -->

Our preliminary simulations suggest that one-norm regularization of $\lambda_{g}$ is more effective and robust than a low-rank approximation of the Hankel matrix $\text{col}{(U_{p},Y_{p},U_{f},Y_{f})}$. In fact, the latter appears to be sensitive and needs to be performed on a case by case basis to avoid unstable behaviour. This will be investigated in future work.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We presented a data-enabled algorithm that can be applied to unknown LTI systems and formally showed its equivalence to the classical MPC algorithm. The DeePC algorithm uses a finite data set to learn the behaviour of the unknown system and computes optimal controls using real-time feedback to drive the system along a desired trajectory while respecting system constraints. Furthermore, we simulated a regularized version of the algorithm on stochastic nonlinear quadcopter dynamics illustrating its capabilities beyond deterministic LTI systems. The performance was superior when compared to system ID followed by MPC. Ongoing and future work focuses on the robustness of the DeePC algorithm and its regularization when applied to stochastic and nonlinear dynamics.
