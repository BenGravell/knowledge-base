<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Risk-Averse Model Predictive Control for Racing in Adverse Conditions

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Model predictive control (MPC) algorithms can be sensitive to model mismatch when used in challenging nonlinear control tasks. In particular, the performance of MPC for vehicle control at the limits of handling suffers when the underlying model overestimates the vehicle's capabilities. In this work, we propose a risk-averse MPC framework that explicitly accounts for uncertainty over friction limits and tire parameters. Our approach leverages a sample-based approximation of an optimal control problem with a conditional value at risk (CVaR) constraint. This sample-based formulation enables planning with a set of expressive vehicle dynamics models using different tire parameters. Moreover, this formulation enables efficient numerical resolution via sequential quadratic programming and GPU parallelization. Experiments on a Lexus LC 500 show that risk-averse MPC unlocks reliable performance, while a deterministic baseline that plans using a single dynamics model may lose control of the vehicle in adverse road conditions.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Expert racing drivers are able to pilot a vehicle at its performance limits by using all the available friction potential between the tires and the road. They are able to do this reliably lap after lap despite changes in the vehicle's performance and behavior due to tire temperature, tire wear, and especially, weather conditions. However, current approaches to autonomous vehicle control struggle in such settings because they are sensitive to discrepancies between the model used for control and the true system. This sensitivity motivates the design of new algorithms that can robustly leverage the full vehicle capabilities. Designing reliable control algorithms for racing may inform the future design of expert driver assistance systems by unlocking reliable responses for avoiding sudden obstacles, driving in adverse weather, and reacting quickly to challenges on the road.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Research in autonomous racing has boomed in the last decade, see for a survey. State of the art control approaches to racing use model predictive control (MPC) to maximize path progress along a planning horizon while respecting constraints such as track bounds. These works use vehicle dynamics models of varying fidelity such as point mass models, singletrack models with Pacejka and Fiala tire models, and data-driven models. However, vehicle dynamics models have limitations, and although perceiving the environment to predict changes in road conditions and online adaptation can help reduce model mismatch, some factors like black ice may be difficult to observe, while reactive online learning methods may not be fast-enough to avoid leading the vehicle into an unrecoverable state.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

These modeling challenges motivate the design of MPC tools that explicitly account for uncertainty to optimally trade off robustness and performance. Previous uncertainty-aware MPC methods for racing use stochastic MPC and tube MPC. Using a linear model of the vehicle with additive disturbances capturing model mismatch, these methods have demonstrated reliable racing performance. In, using Gaussian process models allowed online adaptation to gradually improve laptime. However, for computational reasons, this method fixes the uncertainty estimates during the optimization, so the MPC is not incentivized to select actions that may reduce uncertainty and lead to faster racing despite uncertainty. Also, these works use a linearization-based uncertainty propagation scheme or model uncertainties with additive disturbances that are randomized at each time, and thus neglect correlations over time. However, uncertain tire friction properties (e.g., due to driving over a wet road) may be highly correlated over time. Treating such sources of uncertain model mismatch as random disturbances may lead to suboptimal racing or to under-estimating the likelihood of spinning out.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

As shown, sample-based uncertainty-aware optimization methods offer a potential avenue for using nonlinear dynamics models and accounting for complicated sources of uncertainties, which may necessary for expert racing.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a risk-constrained racing formulation that explicitly accounts for uncertainty over tire forces. It includes a conditional value at risk (CVaR) constraint for track bounds, nonlinear uncertain dynamics, and a cost to minimize expected lap time.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We reformulate the risk-constrained problem using samples of the tire model parameters. Then, we propose a numerical optimization scheme that leverages the sparsity of the problem and parallelizes computations on a graphics processing unit (GPU), unlocking an uncertainty-aware MPC scheme that reasons over $10$ different dynamics parameters and runs at $20$Hz.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We validate the controller on a Lexus LC 500 and show that the proposed risk-constrained MPC approach unlocks reliable performance, while deterministic MPC may lose control of the vehicle in adverse conditions.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Vehicle Dynamics and Tire Model", "weight": 1.0} -->

We use a single-track vehicle model in curvilinear coordinates, see Figure. We model wheelspeed dynamics to better account for wheel slippage and load transfer dynamics to account for variation in tire normal forces. We define states and control inputs

<!-- chunk {"id": "body-0011", "role": "body", "section": "Vehicle Dynamics and Tire Model", "weight": 1.0} -->

where $r$ is the yaw rate, $v$ is the total velocity, $\beta$ is the sideslip, $\omega_{r}$ is the rear wheelspeed, $\Delta F_{z}$ is the load transferred from the front to rear axle, $e$ and $\Delta\varphi$ are the lateral and angle deviations to the reference trajectory, $s$ is the progress along the reference trajectory, $\delta$ is the steering angle, $\tau_{\text{engine}} \geq 0$ is the engine torque, and ${\tau_{\text{brakes},f},\tau_{\text{brakes},r}} \leq 0$ are the front and rear brake torques, respectively. We model the vehicle dynamics as

<!-- chunk {"id": "body-0012", "role": "body", "section": "Vehicle Dynamics and Tire Model", "weight": 1.0} -->

where $(a,b)$ are the distances from the center of gravity to the front and rear axles, $(I_{z},m)$ are the vehicle inertia and mass, $(r_{\text{w}},I_{\text{w}})$ are the wheel radius and the rear axle inertia, $c > 0$ is a constant, $h_{\text{cg}}$ is the center of gravity height, $\kappa_{\text{ref}}$ is the curvature of the reference path.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Vehicle Dynamics and Tire Model", "weight": 1.0} -->

To model tire forces $(F_{xf},F_{yf},F_{xr},F_{yr})$, we use the isotropic coupled slip brush Fiala model

<!-- chunk {"id": "body-0014", "role": "body", "section": "Vehicle Dynamics and Tire Model", "weight": 1.0} -->

The magnitude of the tire forces $(F_{\text{total},f},F_{\text{total},r})$ are

<!-- chunk {"id": "body-0015", "role": "body", "section": "Vehicle Dynamics and Tire Model", "weight": 1.0} -->

where $(\sigma_{f},\sigma_{r})$ are the total tire slips, and $(\sigma_{\text{slip},f},\sigma_{\text{slip},r})$ are the total slips as the tires begin fully sliding

<!-- chunk {"id": "body-0016", "role": "body", "section": "Vehicle Dynamics and Tire Model", "weight": 1.0} -->

The lateral slip angles $(\alpha_{f},\alpha_{r})$ and longitudinal slip ratios $(\kappa_{f},\kappa_{r})$ are

<!-- chunk {"id": "body-0017", "role": "body", "section": "Vehicle Dynamics and Tire Model", "weight": 1.0} -->

The rear tire model explicitly computes $\kappa_{r}$ since the rear wheelspeed $\omega_{r}$ is in the vehicle state. The front tire model captures coupled lateral-longitudinal tire forces by derating the $F_{\text{max}}$ term according to the friction circle.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Vehicle Dynamics and Tire Model", "weight": 1.0} -->

Many environmental factors can influence tire behavior including road conditions, tire condition, and even tire temperature. With our tire model, the tire forces $(F_{xf},F_{yf},F_{xr},F_{yr})$ depend on the tire-road friction $\mu$ and the tire stiffness $C$ parameters, hereinafter defined

<!-- chunk {"id": "body-0019", "role": "body", "section": "Vehicle Dynamics and Tire Model", "weight": 1.0} -->

In Figure, we represent the front tire lateral forces $F_{yf}$ as a function of the slip angle $\alpha$ for different values of $(\mu_{f},C_{f})$. We observe that tire forces are sensitive to the choice of these parameters. Inaccurate parameter estimation may cause over-estimation of the maximum tire forces. This motivates accounting for uncertainty over these parameters to design a reliable controller.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Minimum-Time Formulation for Racing", "weight": 1.0} -->

Next, we describe the racing formulation used in this work. We reparameterize the state and control input as a function of path progress, add the time variable to the state, and combine the rear braking and engine torques to avoid simultaneous acceleration and braking without the need for a non-convex constraint or cost. We define

<!-- chunk {"id": "body-0021", "role": "body", "section": "Minimum-Time Formulation for Racing", "weight": 1.0} -->

We discretize the dynamics with a constant path progress difference ${\Delta s} = {3\text{m}}$ and a trapezoidal scheme

<!-- chunk {"id": "body-0022", "role": "body", "section": "Minimum-Time Formulation for Racing", "weight": 1.0} -->

where ${(x_{k},u_{k})} \approx {({x{({k\Delta s})}},{u{({k\Delta s})}})}$ correspond to the state and control at $s = {k\Delta s}$ along the path (assuming that $x_{0}$ corresponds to $s = 0$ without loss of generality). Using a trapezoidal scheme for the dynamics constraints allows us to plan with a coarse discretization $\Delta s$ over large distances $N\Delta s$. We found that using explicit integrators instead (e.g., an Euler or high-order Runge Kutta schemes) can cause numerical instability if the minimum time cost dominates (see ). To highlight the dependency on the tire parameters $\theta = {(\mu_{f},\mu_{r},C_{f},C_{r})}$, the dynamics constraint are equivalently written as

<!-- chunk {"id": "body-0023", "role": "body", "section": "Minimum-Time Formulation for Racing", "weight": 1.0} -->

The racing objective consists of minimizing lap time. To improve the robustness and smoothness of the controller, we also penalize state-control deviations to the reference $(x_{\text{ref}},u_{\text{ref}})$ and fast changes in the control inputs. We define the linear and quadratic costs

<!-- chunk {"id": "body-0024", "role": "body", "section": "Minimum-Time Formulation for Racing", "weight": 1.0} -->

where $(Q,R,W)$ are diagonal matrices with small entries compared to the terminal time cost $\ell_{T}$. Constraints account for actuator limits $(u_{\text{min}},u_{\text{max}})$ and ensure that the vehicle remains within the track bounds $(e_{\text{min}},e_{\text{max}})$. To plan over a horizon $N$ from an initial state and control, we formulate the optimal control problem (OCP)

<!-- chunk {"id": "body-0025", "role": "body", "section": "Minimum-Time Formulation for Racing", "weight": 1.0} -->

with the notation ${\lbrack 0,N\rbrack}:={\{ 0,\ldots,N\}}$. The only non-convex term in OCP is the dynamics constraints.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Minimum-Time Formulation for Racing", "weight": 1.0} -->

MPC & linear interpolation: For real-time control, OCP is solved recursively from the current $(x_{\text{init}},u_{\text{init}})$ and the plan $(u_{0},\ldots,u_{N})$ is sent to the vehicle. A low-level controller executes the control $u{(s)}$ at the current $s$ via linear interpolation of the latest plan $(u_{0},\ldots,u_{N})$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Risk-Averse Formulation", "weight": 1.0} -->

Solutions to OCP may be sensitive to the value of the tire parameters $\theta$, and a controller that uses inaccurate values of $\theta$ may result in poor closed-loop performance. Intuitively, low friction values should result in smaller torque values to avoid spinning out or violating track bounds. In this section, we formulate a risk-averse MPC problem that accounts for uncertainty over the parameters $\theta$ distributed according to a probability distribution $p_{\theta}$. First, we reformulate the track bound constraints $e_{\text{min},k} \leq e_{k} \leq e_{\text{max},k}$ in OCP as

<!-- chunk {"id": "body-0028", "role": "body", "section": "Risk-Averse Formulation", "weight": 1.0} -->

To enforce track bound constraints and account for uncertainty over state trajectories due to uncertain tire forces, we constrain the tail probability of ever violating the constraint ${g_{k}{(x_{k})}} \leq 0$ in at any timestep $k$

<!-- chunk {"id": "body-0029", "role": "body", "section": "Risk-Averse Formulation", "weight": 1.0} -->

where $\text{CVaR}_{\alpha}$ is the conditional value at risk at level $\alpha \in {}$ (or average value at risk ), defined as ${\text{CVaR}_{\alpha}{(Z)}} = {{\min_{\xi \in {\mathbb{R}}}{\mathbb{E}}}{\lbrack{\xi + {{\max{(0,{Z - \xi})}}/\alpha}}\rbrack}}$. Using the risk constraint yields many advantages compared to other (e.g., chance-constrained) formulations, see.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Risk-Averse Formulation", "weight": 1.0} -->

The total cost ${\ell_{T}{(x_{N})}} + {\sum_{k = 0}^{N - 1}{\ell{(x_{k},u_{k},u_{k + 1})}}}$ is also a random variable as it depends on the state trajectory, so we minimize its expected (average) value, with the objective of minimizing the average lap time. We formulate the risk-averse optimal control problem (RA-OCP)

<!-- chunk {"id": "body-0031", "role": "body", "section": "Risk-Averse Formulation", "weight": 1.0} -->

RA-OCP encodes the problem of minimizing the average lap time (with additional regularization encoded by the cost term $\ell$) while bounding the tail probability of leaving the track, over the uncertain parameters $\theta \sim p_{\theta}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Sample-based reformulation and numerical resolution", "weight": 1.0} -->

RA-OCP is a challenging problem to solve due to the uncertainty over the parameters $\theta$. Inspired, we compute approximate solutions to RA-OCP by solving a sample-based reformulation instead that depends on $({1 + M})$ samples $\theta^{i}$ of the parameters $\theta$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Sample-based reformulation and numerical resolution", "weight": 1.0} -->

First, we select a nominal value $\overline{\theta}:=\theta^{0}$ for the parameters $\theta$ to parameterize a nominal state and control trajectory ${(\overline{x},\overline{u})}:={(x^{0},u^{0})}$, which will be used to reduce uncertainty growth over the planning horizon via feedback. This trajectory satisfies the nominal dynamics

<!-- chunk {"id": "body-0034", "role": "body", "section": "Sample-based reformulation and numerical resolution", "weight": 1.0} -->

Second, we account for uncertainty over the parameters $\theta$ by parameterizing $M$ state and control trajectories $(x^{i},u^{i})$ around the nominal trajectory $(\overline{x},\overline{u})$. We select $M$ samples $\theta^{i}$ of $\theta$ that define the state trajectories as

<!-- chunk {"id": "body-0035", "role": "body", "section": "Sample-based reformulation and numerical resolution", "weight": 1.0} -->

and the closed-loop control trajectories as

<!-- chunk {"id": "body-0036", "role": "body", "section": "Sample-based reformulation and numerical resolution", "weight": 1.0} -->

where the feedback gains $K_{k}^{i}$ are computed as the solution to a linear-quadratic regulator (LQR) problem \[, Chapter 12\] around $(x_{\text{ref}},u_{\text{ref}})$ using the parameters $\theta^{i}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Sample-based reformulation and numerical resolution", "weight": 1.0} -->

Finally, we introduce the optimization variables

<!-- chunk {"id": "body-0038", "role": "body", "section": "Sample-based reformulation and numerical resolution", "weight": 1.0} -->

where $y$ and $\xi$ are risk variables, the state and control dimensions are ${(n,m)} = {}$, the sample size and horizon are ${(M,N)} = {}$, and formulate the following sample-based approximation to RA-OCP

<!-- chunk {"id": "body-0039", "role": "body", "section": "Remark 1 (On closed-loop uncertainty propagation)", "weight": 1.0} -->

Using a feedback law in the optimization problem RA-OCP to define closed-loop trajectories as in - is a standard approach to prevent uncertainty to grow unbounded over time and make the optimization infeasible. It also allows approximately accounting for closed-loop feedback of the receding horizon MPC scheme. We do not enforce input constraints for the controls $u^{i}$ because solutions are already constrained by the tire friction limits, although one could include closed-loop input constraints in the risk constraint or saturate the controls $u^{i}$ within the dynamics.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Efficient numerical resolution of the sample-based problem: leveraging GPU parallelization and sparsity", "weight": 1.0} -->

Efficiently solving the sample-based reformulation of RA-OCP requires special care due to the large size of the problem. To achieve fast replanning, we leverage two observations. First, the problem is sparse, e.g., the particle $x^{i}$ does not explicitly depend on $x^{i + 1}$. Second, since we parameterize the state trajectory $x^{i}$ for each particle, the cost terms and constraints can be evaluated in parallel over both particles and time on a GPU.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Efficient numerical resolution of the sample-based problem: leveraging GPU parallelization and sparsity", "weight": 1.0} -->

Thus, we decide to solve the sample-based reformulation of RA-OCP via a sequential quadratic programming (SQP) method with a linesearch \[, Chapter 18\]. We evaluate the cost, constraints, and their gradients in Python using Jax, so we can easily evaluate the quadratic programs (QPs) at each SQP step on a GPU and take advantage of the parallel structure of the sample-based reformulation. The problem data is then moved to the CPU and the QPs are solved using OSQP. Even though the QPs involve many variables, they are quickly solved thanks to the sparsity of the QPs that OSQP leverages internally. For receding horizon MPC, we only perform one SQP iteration at each timestep.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 2 (Alternatives and lessons learned)", "weight": 1.0} -->

nominal trajectory $\overline{x}$ could be removed from the optimization variables by defining $\overline{x} = x^{0} = {\frac{1}{M}{\sum_{i = 1}^{M}x^{i}}}$. However, the resulting formulation densely couples the particles $x^{i}$ via the feedback controls in and is thus slow to solve numerically. Parameterizing the nominal trajectory greatly increases the sparsity of the problem.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Remark 2 (Alternatives and lessons learned)", "weight": 1.0} -->

We tried only optimizing over the control inputs $u$ and computing states $x^{i}{(u)}$ for each particle via an explicit integration scheme as, which we found to be numerically sensitive to the choice of initial guess. Parameterizing the particles $x^{i}$ and using an implicit integrator instead improves robustness and enables parallelizing computations over times $k$ and samples $i$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Problem Setup and Trajectory Analysis", "weight": 1.0} -->

We consider an oval racing track shown in Figure. The reference trajectory $(x_{\text{ref}},u_{\text{ref}})$ is the optimal racing line computed offline for nominal parameters $\overline{\theta}$ using the method. In this section, we study trajectories solving OCP and RA-OCP for different values of the parameters $\theta$. For visualization purposes, we use $M = 5$ samples of the parameters, shown in Table I.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Problem Setup and Trajectory Analysis", "weight": 1.0} -->

a\) How different are risk-averse solutions compared to solutions to OCP with nominal tire parameters $\overline{\theta}$? We present trajectories solving OCP and RA-OCP in Figure. The risk-averse solution applies less engine torque and braking forces to account for potentially reduced tire forces and brakes earlier than the solution to OCP. This results in a lower velocity in the turn. We also plot closed-loop trajectories $x^{i}$ satisfying for OCP for the different parameters $\theta^{i}$. The solution to OCP may drive too fast to complete the turn: the vehicle may slide out of the track if the tire friction parameters $\mu_{f}$ and $\mu_{r}$ take lower values. In contrast, solutions to RA-OCP account for different tire parameter values to ensure robust handling of the vehicle in the turn.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Problem Setup and Trajectory Analysis", "weight": 1.0} -->

b\) Does solving OCP with low-friction tire parameters give robust performance?

<!-- chunk {"id": "body-0047", "role": "body", "section": "Problem Setup and Trajectory Analysis", "weight": 1.0} -->

We solve OCP assuming that $\overline{\theta} = \theta^{1}$ (corresponding to low-friction tire parameters $\mu_{f} = \mu_{r} = 0.7$) and present results in Figure. The solution to OCP is now closer to the solution to RA-OCP and yields better performance over different tire parameter values $\theta^{i}$ than if assuming larger-friction tire parameters. However, the performance remains poor for different tire parameter values, e.g., exhibiting large sideslip ($\beta$) values for $\mu_{f} = 0.8$ that may lead to suboptimal closed-loop performance. Overall, these results show that accounting for different tire parameters by solving RA-OCP gives additional robustness compared to only planning with low-friction tire parameters.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Hardware Results", "weight": 1.0} -->

We validate the risk-averse controller on a 2019 Lexus LC 500. State estimates come from an OxTS Inertial Navigation System. The optimization problems are solved on an on-board computer with an Intel Xeon E-2278GE CPU \@3.30GHz and an NVIDIA GeForce RTX 3070 GPU. Further details about the vehicle are.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Hardware Results", "weight": 1.0} -->

We compare the proposed risk-averse MPC approach solving RA-OCP with a nominal MPC solving OCP with the parameters $\theta = \overline{\theta}$. For all experiments, we fix the parameter samples $\theta^{i}$ in OCP and RA-OCP to the values in Table I to cover the parameter space. Keeping these parameter values constant in time also removes randomness in the algorithm. The nominal MPC runs at about $100$Hz. The risk-averse MPC runs at $20$Hz (with mean $22$Hz and standard deviation $1.5$Hz). These update rates are sufficient to reliably control the vehicle.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Hardware Results", "weight": 1.0} -->

a\) Racing in dry conditions: We first validate the controllers in dry conditions and report results in Figure. Nominal MPC (solving OCP with the parameters $\overline{\theta}$) applies larger engine and braking torques and drives slightly faster than risk-averse MPC (solving RA-OCP), with a top speed difference of $1\text{m/s}$. Nominal MPC causes slight yaw rate oscillations while turning due to tire saturation. Overall, nominal MPC slightly outperforms risk-averse MPC in such dry conditions, which is expected behavior given that risk-averse MPC optimizes the expected final time over a wider range of parameters including lower friction values $(\mu_{f},\mu_{r})$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Hardware Results", "weight": 1.0} -->

We also tested nominal MPC planning with low-friction parameters ($\mu_{f} = \mu_{r} = 0.7$). This approach consistently cuts corners in the turns due to model mismatch and is thus unable to race in dry conditions.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Hardware Results", "weight": 1.0} -->

b\) Racing through a patch of water: We test again the controllers on a dry track with a water patch in turn $2$. Such conditions may represent a track that is slowly drying up after rain, resulting in a leftover patch of water. We run the controllers three times each. For repeatability, we alternate between nominal and risk-averse MPC and add water after each individual run.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Hardware Results", "weight": 1.0} -->

Results are reported in Figure. After driving through the wet area when exiting turn $2$, nominal MPC consistently causes a spin out, due to applying engine torques that are too large while oversteering. Indeed, tires are wet and thus cannot apply the planned tire forces, which results in a spin out. In contrast, risk-averse MPC applies slightly smaller engine torques when exiting each turn and is thus consistently able to drive through the wet area and complete the lap. While more robust behavior may be obtained with nominal MPC by reducing the minimum-time cost $\ell_{T}$ compared to the regularizer $\ell$, such a strategy may require additional hyperparameter tuning and lead to suboptimality and slower lap times.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We presented a risk-averse MPC framework for racing and showed that accounting for different tire parameters provides a natural avenue for infusing robustness into MPC. By leveraging a particular sample-based risk-averse formulation, our method accurately accounts for uncertain nonlinear tire dynamics and is amenable to online replanning in MPC. In future work, we plan on investigating improvements to the SQP solver (e.g., by developing specialized methods inspired from to solve RA-OCP entirely on the GPU) to unlock faster replanning and using larger sample sizes, and interfacing with perception to account for state uncertainty and parameters that vary over time and space.
