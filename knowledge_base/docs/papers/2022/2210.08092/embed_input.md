<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Probably Approximately Correct Nonlinear Model Predictive Control (PAC-NMPC)

Topics include Model predictive control, Predictive control, Nonlinear model predictive control, Stochastic model predictive control, Vehicles, Safety, Uncertainty, Real-time systems, Online algorithms, Sampling-based methods, Sample complexity, Control, Sampling, Probably approximately correct, PAC-NMPC, SNMPC, Uncrewed aerial vehicle.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Approaches for stochastic nonlinear model predictive control (SNMPC) typically make restrictive assumptions about the system dynamics and rely on approximations to characterize the evolution of the underlying uncertainty distributions. For this reason, they are often unable to capture more complex distributions (e.g., non-Gaussian or multi-modal) and cannot provide accurate guarantees of performance. In this paper, we present a sampling-based SNMPC approach that leverages recently derived sample complexity bounds to certify the performance of a feedback policy without making assumptions about the system dynamics or underlying uncertainty distributions. By parallelizing our approach, we are able to demonstrate real-time receding-horizon SNMPC with statistical safety guarantees in simulation and on hardware using a 1/10th scale rally car and a 24-inch wingspan fixed-wing unmanned aerial vehicle (UAV).

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Nonlinear model predictive control (NMPC) has proven to be a powerful approach for controlling high-dimensional, complex robotic systems (e.g., ). Nevertheless, although these methods can handle large state spaces, nonlinear dynamics, and system constraints, their performance can be adversely affected by the presence of uncertainty even in the context of real-time replanning. A number of approaches have been proposed to compensate for this marginal robustness, the simplest of which is to generate a feedback policy to track the current receding-horizon plan (e.g., ). These approaches, however, do not account for uncertainty or closed-loop performance during the planning process. To address this, approaches such as robust NMPC (RNMPC) and stochastic NMPC (SNMPC) attempt to reason about the response of the policy to disturbances during planning. This is usually accomplished by making simplifying assumptions about the dynamics and disturbances. For instance, in RNMPC, disturbance sets may be approximated by ellipsoids, or robustness guarantees may require the existence of a control contraction metric (CCM); in SNMPC, uncertainty distributions are often approximated via Gaussians or sampling.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we present a sampling-based SNMPC algorithm capable of controlling stochastic dynamical systems without applying limiting assumptions to the structure of the stochastic dynamics or underlying uncertainty distributions. In addition, our approach leverages recently derived sample complexity bounds to provide a probabilistic guarantee on system performance. Our algorithm builds on Probably Approximately Correct Robust Policy Search (PROPS) to directly optimize an upper confidence bound on the expected cost and the probability of constraint violation for a receding-horizon feedback policy. Not only does this approach encourage robust policy generation, but the minimized bounds themselves provide a statistical guarantee for each planning interval. To achieve real-time performance, we use a graphics processing unit (GPU) to parallelize our algorithm. We then evaluate our approach in simulation and on hardware using a 1/10^th^ scale rally car and a 24-inch wingspan fixed-wing UAV.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A novel algorithm, PAC-NMPC, for receding horizon SNMPC with probabilistic performance guarantees.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A real-time implementation via GPU acceleration.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Demonstration of our algorithm on complex underactuated systems via simulation and hardware experiments.

<!-- chunk {"id": "body-0008", "role": "body", "section": "III-A Iterative Stochastic Policy Optimization", "weight": 1.0} -->

Consider the stochastic dynamics given by $p{(\left. \mathbf{x}_{t + 1} \middle| {\mathbf{x}_{t},\mathbf{u}_{t}} \right.)}$ defined by a vector of state values $\mathbf{x}_{t} \in {\mathbb{R}}^{N_{x}}$, a vector of control inputs $\mathbf{u}_{t} \in {\mathbb{R}}^{N_{u}}$, and probability density $p$. Iterative Stochastic Policy Optimization (ISPO) formulates the search for a control policy $\mathbf{u}_{t} = {{\mathbf{π}}_{t}{(\mathbf{x}_{t},{\mathbf{ξ}})}}$ as a stochastic optimization problem, where $\mathbf{ξ}$ is a set of policy parameters. Specifically, ISPO introduces a surrogate distribution $p{(\left.

<!-- chunk {"id": "body-0009", "role": "body", "section": "III-A Iterative Stochastic Policy Optimization", "weight": 1.0} -->

{\mathbf{ξ}} \middle| {\mathbf{ν}} \right.)}$ where policy parameters $\mathbf{ξ}$ are dependent on distribution hyper-parameters $\mathbf{ν}$. This induces a joint distribution

<!-- chunk {"id": "body-0010", "role": "body", "section": "III-B PAC Bounds for Stochastic Policy Search", "weight": 1.0} -->

Instead of directly minimizing an empirical approximation of the expected cost, it can be beneficial to minimize *an upper confidence bound* on the expected cost. Not only does such an approach encourage robust policies, but it also can provide guarantees on future performance. In this paper, we directly optimize the PAC bounds derived. While these bounds are derived in and discussed, we review them here since they are fundamental to our approach.

<!-- chunk {"id": "body-0011", "role": "body", "section": "III-B PAC Bounds for Stochastic Policy Search", "weight": 1.0} -->

To compute the distance between the distributions, the Renyi divergence, $D_{2}$, is used. $d{({\mathbf{ν}})}$ is given as

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-B PAC Bounds for Stochastic Policy Search", "weight": 1.0} -->

The concentration-of-measure term $\Phi_{\alpha}{(\delta)}$ is given as

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-B PAC Bounds for Stochastic Policy Search", "weight": 1.0} -->

It tightens the bound as the number of samples increases and as the bound confidence, $1 - \delta$, decreases.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-B PAC Bounds for Stochastic Policy Search", "weight": 1.0} -->

To combine costs and constraints, we optimize a weighted sum of $\mathcal{J}_{\alpha}^{+}{({\mathbf{ν}})}$ and $\mathcal{C}_{\alpha}^{+}{({\mathbf{ν}})}$, where $\gamma > 0$ is a heuristically selected weighting coefficient. We solve

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-B PAC Bounds for Stochastic Policy Search", "weight": 1.0} -->

using a GPU implementation of L-BFGS-B. When optimizing the bounds, we used self-normalized importance weights to compute $\ell_{ij}$ in Eq. 5") and analytical gradients, as described.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Approach", "weight": 1.0} -->

To formulate a receding-horizon NMPC algorithm that leverages the PAC bounds, we first address the stochastic trajectory optimization problem. We then extend this approach to enable real-time feedback motion planning.

<!-- chunk {"id": "body-0017", "role": "body", "section": "IV-A PAC Stochastic Trajectory Optimization", "weight": 1.0} -->

2 for t = 0, …, NT do // Stochastic Rollout
Return τ = {x0,u0,x1,u1,…,uNT,xNT + 1}

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-A PAC Stochastic Trajectory Optimization", "weight": 1.0} -->

For each optimization iteration, $M$ trajectories are sampled from the joint distribution (Eq. 1")) and evaluated using the augmented cost in Eq. 9"). Sampling from the joint distribution is achieved by first sampling policy parameters from the surrogate distribution and then using these policy parameters to sample from the stochastic dynamics as shown in Alg. 3"). The augmented costs of the samples are used to find a new set of policy parameters that minimize the weighted sum of the cost and constraint bounds (Alg. 2")). This process iterates until a termination condition (e.g. maximum time, convergence metric, etc.) is reached. The optimization not only returns the optimized policy parameters, but also the optimized bounds themselves.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-A PAC Stochastic Trajectory Optimization", "weight": 1.0} -->

An analytical formulation for the surrogate distribution is necessary to compute the robust estimates (Eq. 4")) and Renyi divergences (Eq. 7")). By contrast, the only requirement on the stochastic dynamics is to permit sampling. This property allows our algorithm to generalize to a large class of complex (potentially "black-box") stochastic dynamics models. In practice, the cost and constraint functions can also be stochastic (e.g. $J_{ij},c_{ij} \sim p{( \cdot, \cdot |{\mathbf{τ}}_{ij})}$).

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-B PAC Feedback Motion Planning", "weight": 1.0} -->

While the ability to compute PAC open-loop policies is valuable, ideally, we would like to compute closed-loop policies of the form ${\mathbf{π}}_{t}{(\mathbf{x}_{t},{\mathbf{ξ}})}$. A closed-loop policy should enable us to generate tighter state-space trajectory distributions and improve the ability of our policies to satisfy control objectives. However, designing feedback policies is not straightforward and can be very system specific.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-B PAC Feedback Motion Planning", "weight": 1.0} -->

$\mathbf{x}_{t}^{d} \in {\mathbb{R}}^{N_{x}}$ is a nominal state trajectory and $\mathbf{u}_{t}^{d} \in {\mathbb{R}}^{N_{u}}$ is a nominal input trajectory. All of the elements of these sequences are parameters of the feedback policy. Assuming the surrogate distribution is a mulitvariate Gaussian with a diagonal covariance matrix, in this case, ${\mathbf{ξ}} \in {\mathbb{R}}^{2{({{N_{x}N_{u}} + N_{x} + N_{u}})}N_{T}}$. Given the size of the decision space, this parameterization of the policy is unlikely to be computationally tractable.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-B PAC Feedback Motion Planning", "weight": 1.0} -->

3 for k = 0, …, NT do // Nominal Rollout
4 xt + 1d = xtd + f (xtd,utd) Δ t;
8 for t = 0, …, NT do // Feedback Rollout
Return τ = {x0,u0,x1,u1,…,uNT,xNT + 1}
Algorithm 4 τ ∼ p(⋅|ξ,x0) with Feedback

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-B PAC Feedback Motion Planning", "weight": 1.0} -->

To overcome this challenge, we instead use a local closed-loop policy of the form

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-B PAC Feedback Motion Planning", "weight": 1.0} -->

where $\mathbf{u}_{t}^{d} = {\mathbf{ζ}}_{t}$. To sample from this feedback policy, we must first compute the nominal trajectory, ${\mathbf{τ}}^{d}$. However, ${\mathbf{τ}}^{d}$ itself is dependent on $\mathbf{ξ}$; for this reason, we employ a two-stage sampling process. In the first stage, we sample from the trajectory distribution $p{(\left. {\mathbf{τ}}^{d} \middle| {\mathbf{ξ}} \right.)}$ using the deterministic dynamics model (Eq. 11")) and the surrogate distribution $p{(\left. {\mathbf{ξ}} \middle| {\mathbf{ν}} \right.)}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-B PAC Feedback Motion Planning", "weight": 1.0} -->

For each sample trajectory ${\mathbf{τ}}^{d}$, we the compute the time-varying gains $\mathbf{K}_{t}{({\mathbf{τ}}^{d})}$. In the second stage, we sample from the closed-loop stochastic dynamics using the feedback policy (Eq. 10")). This approach, summarized in Alg. 4"), certifies the feedback policy by allowing our sampled costs and constraints to capture the impact of our local feedback policy on our stochastic dynamics model.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-B PAC Feedback Motion Planning", "weight": 1.0} -->

We use the finite horizon, discrete, time-varying linear quadratic regulator (TVLQR) to compute the feedback gains $\mathbf{K}_{t}{({\mathbf{τ}}^{d})}$. For each sampled nominal trajectory, the gains are computed by integrating the finite horizon discrete-time Riccati equations backward in time using the nominal dynamics linearized about ${\mathbf{τ}}^{d}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-C PAC-NMPC", "weight": 1.0} -->

Finally, we propose a receding-horizon NMPC approach based on our PAC feedback motion planning algorithm (Alg. 5")). At each planning interval, with a period of $H$, the trajectory distribution and corresponding feedback policy is optimized given the current state, $\mathbf{x}_{\mathbf{0}}$, and the prior hyper-parameters, ${\hat{\mathbf{ν}}}_{0}^{\ast}$. Then, the trajectory and feedback gains are trimmed by $\frac{H}{\Deltat}$ to account for time passed since the beginning of the planning interval and executed by the controller. The trim operation is given as ${Trim{({\mathbf{κ}})}} = \left\{ \mathbf{K}_{\frac{H}{\Deltat}},\ldots,\mathbf{K}_{N_{T}} \right\}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-C PAC-NMPC", "weight": 1.0} -->

Hyper-parameters determining the first $\frac{H}{\Deltat}$ time steps of the control trajectory represent control signals that the system is executing during the optimization and are not modified during the optimization. To execute the policy, we use the maximum likelihood estimate of the policy parameters, which is simply the mean, $\mathbf{μ}$, of the multivariate Gaussian $p{(\left. {\mathbf{ξ}} \middle| {\mathbf{ν}} \right.)}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-C PAC-NMPC", "weight": 1.0} -->

Given that optimal trajectory distributions are expected to be similar between subsequent planning intervals, we use the optimal hyper-parameters from the last planning interval to initialize the prior policy distribution for the next. This initialization is extremely important since it allows the prior to start near an optimal solution, thus reducing the required number of iterations for convergence. After trimming, we apply the feedback policy to generate a modified policy parameter distribution with a mean feasible for the current initial state. Then, we extend the mean with zeros and the variance with its final value. We threshold the prior variance with ${\mathbf{η}}_{min}$ to prevent it from starting too small, which would inhibit exploration (Alg. 6")).

<!-- chunk {"id": "body-0030", "role": "body", "section": "V-A Trajectory Optimization Experiments", "weight": 1.0} -->

We simulate a stochastic bicycle model with acceleration and steering rate inputs. We denote $\mathbf{x}_{t} = {\lbrack x_{0},x_{1},x_{2},x_{3},x_{4}\rbrack}^{T}$ as the state vector, $\mathbf{u}_{t} = {\lbrack u_{0},u_{1}\rbrack}^{T}$ as the control vector, $l = 0.33$ as the wheel base, and $\mathbf{\Gamma} = {diag{(\lbrack 0.001,0.001,0.1,0.2,0.001\rbrack)}}$ as the covariance.

<!-- chunk {"id": "body-0031", "role": "body", "section": "V-A Trajectory Optimization Experiments", "weight": 1.0} -->

A 20 timestep trajectory with ${\Deltat} = 0.1$ sec is optimized, with an initial state of $\mathbf{x}_{\mathbf{I}} = \lbrack 0.0,0.0,0.0,1.0,0.0\rbrack^{T}$ and a goal state of $\mathbf{x}_{\mathbf{G}} = \lbrack 3.0,0.0,0.0,1.0,0.0\rbrack^{T}$. The steering angle is constrained to ${({- 0.4},0.4)}rad$, the steering rate to ${({- 1.0},1.0)}\frac{rad}{sec}$, and the acceleration to ${({- 1.0},1.0)}\frac{m}{s^{2}}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-A Trajectory Optimization Experiments", "weight": 1.0} -->

We apply a quadratic cost on the final state of the trajectory: ${J{({\mathbf{τ}})}} = {\mathbf{x}_{N_{T} + 1}^{T}\mathbf{Q}_{f}\mathbf{x}_{N_{T} + 1}}$ where $\mathbf{Q}_{\mathbf{f}} = {diag{(\lbrack 2.0,2.0,0.0,0.0,0.0\rbrack)}}$. An obstacle constraint is applied with circular obstacles at $(1.0,0.75)$ and $\left( 2.0,{- 0.75} \right)$. The initial prior distribution has a mean of all zeros and a variance of all ones. Parameters were as follows: $L = 5$, $M = 1024$, $\delta = 0.05$, $\gamma = 10$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-A Trajectory Optimization Experiments", "weight": 1.0} -->

Simulations were run on a laptop with an Intel Core i9-9880H CPU and a Nvidia GeForce RTX 2070 GPU.

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-A Trajectory Optimization Experiments", "weight": 1.0} -->

To highlight the necessity of properly considering stochasticity to generate accurate guarantees, we compared performance while optimizing the PAC bounds with and without considering stochastic dynamics (replace line 3 of Alg. 3") and line 9 of Alg. 4") with $\mathbf{x}_{t + 1} = {\mathbf{x}_{t} + {f{(\mathbf{x}_{t},\mathbf{u}_{t})}\Deltat}}$). Optimizing without stochastic dynamics caused $\hat{\mathcal{J}}{({\hat{\mathbf{ν}}}^{\ast})}$ and $\hat{\mathcal{C}}{({\hat{\mathbf{ν}}}^{\ast})}$ to be larger than the bounds, indicating that the guarantees were not accurate (Fig. 2")a,b). We also performed an ablation study in which we compared performance with and without feedback.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-A Trajectory Optimization Experiments", "weight": 1.0} -->

On average, each iteration took 15.9 ms without feedback and 18.5 ms with feedback. Feedback enabled the optimizer to reduce the bounds to lower values (Fig. 2")e-h) and resulted in a tighter distribution in state-space (Fig 3")).

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-A Trajectory Optimization Experiments", "weight": 1.0} -->

We compare against optimizing an empirical approximation of the expected costs/constraints, regulated by the $\mathcal{K}\mathcal{L}$-divergence to prior policies, to demonstrate that optimizing the PAC bounds encourages more robust polices. We also compare against RA-MPPI, a state-of-the-art risk-aware sampling based NMPC method. We used the following parameters: $\Sigma_{\epsilon} = 0.01$, $M = 1024$, $N = 300$, $\eta = 0$, $\alpha = 0.3$, $A = 10$, $B = 1$, $C_{u} = 0.5$ for the cost, and $C_{u} = 0.05$ for the constraint. Our approach converged to the lowest estimated expected cost and probability of collision (Fig 4")).

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-B NMPC Experiment", "weight": 1.0} -->

The system follows a receding horizon state generated on a looping path. The path runs along a set of circular obstacles. We optimize a 12 timestep trajectory with ${\Deltat} = 0.1$ second at a replanning period of $H = 0.2$ sec. We apply a quadratic cost on the final state of the trajectory: ${J{({\mathbf{τ}})}} = {\mathbf{x}_{N_{T} + 1}^{T}\mathbf{Q}_{f}\mathbf{x}_{N_{T} + 1}}$ where $\mathbf{Q}_{\mathbf{f}} = {diag{(\lbrack 1.0,1.0,0.1,0.1,0.0\rbrack)}}$. Parameters were as follows: $L = 5$, $M = 1024$, $\delta = 0.05$, $\gamma = 10$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-B NMPC Experiment", "weight": 1.0} -->

To allow for a higher control rate, the executed control trajectory is interpolated from 10 Hz to 50 Hz with the assumption that our PAC bounds will still hold. We perform an ablation study in which we compare performance with and without feedback, as well as optimizing the PAC bounds with and without stochastic dynamics.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-B NMPC Experiment", "weight": 1.0} -->

PAC-NMPC was successfully able to control the system in real time and followed the path while avoiding nearby obstacles. In Figure 5"), we show the route taken by the system during five loops of the path.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-B NMPC Experiment", "weight": 1.0} -->

During each planning interval of $H = 0.2$ sec, the controller achieved an average of 54 iterations of PAC stochastic trajectory optimization (approximately 3.7ms per iteration). The controller consistently produced PAC bounds $\leq$ 5% probability of collision, which accurately bounded the Monte Carlo estimates when optimizing with stochastic dynamics. The bound was exceeded only once out of 482 planning intervals. Thus, the estimates were bounded accurately in around 99.8% of planning intervals, well within the 95% confidence bound (Fig 6")d).

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-B NMPC Experiment", "weight": 1.0} -->

We demonstrate a quantitative difference in the observance of the PAC Bounds in Figure 6"). When optimizing the bounds with the nominal dynamics, the probability of collision estimates were only bounded in 93.9% of planning intervals (Fig 6")b). This decrease in bound accuracy is even more apparent when running the controller without feedback to compensate for unmodeled noise, resulting in only 64.7% of planning intervals having bounded probability of collision estimates (Fig 6")a).

<!-- chunk {"id": "body-0042", "role": "body", "section": "VI-A1 Hardware", "weight": 1.0} -->

To evaluate our method on physical hardware, we ran PAC-NMPC on a 1/10th-scale Traxxas Rally Car platform. The algorithm runs on a Nvidia Jetson Orin mounted on the bottom platform. The control interface is a variable electronic speed controller (VESC), which executes commands and provides servo state information. The position and orientation is tracked with an OptiTrack system.

<!-- chunk {"id": "body-0043", "role": "body", "section": "VI-A2 Setup", "weight": 1.0} -->

The route, virtual obstacle placements, and TVLQR costs are identical to those in the simulation experiments. We optimize a 12 timestep trajectory with ${\Deltat} = 0.1$ sec at a replanning period of $H = 0.2$ sec. We apply a quadratic cost to the final state of the trajectory: ${J{({\mathbf{τ}})}} = {\mathbf{x}_{N_{T} + 1}\mathbf{Q}_{f}\mathbf{x}_{N_{T} + 1}}$ where $\mathbf{Q}_{\mathbf{f}} = {diag{(\lbrack 1.0,1.0,0.4,0.1,0.0\rbrack)}}$. Parameters were $L = 2$, $M = 1024$, $\delta = 0.05$, $\gamma = 10$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "VI-A2 Setup", "weight": 1.0} -->

We model the rally car dynamics as a stochastic bicycle model where noise is modeled as a 3 component Gaussian Mixture Model. This mixture model was fit from 2500 samples of data collected with the car (Fig. 7")). We perform the same ablation study as done in the simulation experiments.

<!-- chunk {"id": "body-0045", "role": "body", "section": "VI-A3 Results", "weight": 1.0} -->

PAC-NMPC ran onboard the rally car in real-time and followed the path while avoiding nearby obstacles. In Figure 8"), we display the path taken by the car with collisions annotated by arrows. During each planning interval of $H = 0.2$ sec, the controller achieved an average of 10 iterations of trajectory distribution optimization with approximately 20ms per iteration.

<!-- chunk {"id": "body-0046", "role": "body", "section": "VI-A3 Results", "weight": 1.0} -->

The controller consistently produced PAC bounds $\leq$`<!-- -->`{=html}10% probability of collision, which accurately bounded the Monte Carlo estimates of the probability of collision at all planning intervals (Fig. 9")d). In this context, Monte Carlo estimates refer to sampled trajectories using the simulated stochastic dynamics model. When optimizing with stochastic dynamics and without feedback, the car collided with virtual obstacles twice, likely due to unmodeled dynamics not captured in the Gaussian mixture model (Fig. 9")c). When optimizing the bound with nominal dynamics, the car collided with virtual obstacles, with and without feedback (Fig. 9")a,b).

<!-- chunk {"id": "body-0047", "role": "body", "section": "VI-B1 Hardware", "weight": 1.0} -->

To demonstrate that our approach can extend to more complex, high-dimensional systems, we use PAC-NMPC to control a 24" wingspan Edge 540 fixed-wing UAV. It has a controllable propeller, rudder, elevator, and kinematically linked ailerons. The position and orientation are tracked with an OptiTrack system.

<!-- chunk {"id": "body-0048", "role": "body", "section": "VI-B2 Setup", "weight": 1.0} -->

We utilize a quaternion formulation of the fixed-wing described in with RK2 integration. This system has a 17-dimensional state space and a 4-dimensional control space.

<!-- chunk {"id": "body-0049", "role": "body", "section": "VI-B2 Setup", "weight": 1.0} -->

The control signal is the rate of change of the control surface deflections and of the propeller speed: $\mathbf{u} = \left\lbrack u_{a},u_{e},u_{r},u_{p} \right\rbrack$. We place noise represented by a 3 component Gaussian Mixture Model over the body frame accelerations, which was fit from 2000 samples of data collected with the fixed-wing (Fig. 10")). We optimize a 12 timestep trajectory with ${\Deltat} = 0.1$ sec at a replanning period of $H = 0.2$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "VI-B2 Setup", "weight": 1.0} -->

We use feedback and use stochastic dynamics to optimize the PAC bounds.

<!-- chunk {"id": "body-0051", "role": "body", "section": "VI-B2 Setup", "weight": 1.0} -->

To enable real-time performance, we set the number of prior policies, $L$, to one and compute the linearized dynamics for the feedback policy using finite difference on the mean trajectory of the prior. The controller was run on a desktop computer with an AMD Ryzen 7 5800x and a NVIDIA GeForce RTX 3080.

<!-- chunk {"id": "body-0052", "role": "body", "section": "VI-B3 Results", "weight": 1.0} -->

PAC-NMPC was successfully able to control the fixed-wing in real-time, following a square path while avoiding nearby obstacles. In Figure 11"), we display the route taken by the system during five loops of the path. During each planning interval of $H = 0.2$ sec, the controller achieved an average of 22 iterations of trajectory distribution optimization with around 8.5 ms per iteration. The controller consistently produced PAC bounds of around 10% probability of collision, which accurately bounded the Monte Carlo estimates (Fig. 12")).

<!-- chunk {"id": "body-0053", "role": "body", "section": "Discussion", "weight": 1.5} -->

In this work, we presented a novel SNMPC method capable of propagating uncertainty through arbitrary nonlinear dynamic systems and of providing statistical guarantees on expected cost and constraint violations. We demonstrated real time performance both in simulation and on-board physical hardware. Further, we show that the algorithm is capable of scaling to more complex systems, like fixed-wing UAVs. Since this algorithm can be used with "black-box" sampling of dynamics (assuming they are continuously differentiable), costs, constraints, and noise, future work can investigate its use with learned dynamics and perception-informed costs. Future work could also explore the extension of this approach to more complex control trajectory distributions.
