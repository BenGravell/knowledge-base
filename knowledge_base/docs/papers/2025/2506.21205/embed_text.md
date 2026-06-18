## Introduction

Mobile robots have the potential to enhance various aspects of daily life, from optimizing logistics in warehouses to enabling safer and more efficient transportation through autonomous vehicles \[(https://arxiv.org/html/2506.21205v2#bib.bib1), (https://arxiv.org/html/2506.21205v2#bib.bib2), (https://arxiv.org/html/2506.21205v2#bib.bib3)\]. However, for robots to be successfully integrated into real-world settings like urban areas, they must be capable of safely and efficiently manoeuvring through human-populated spaces. Achieving this requires an ability to interpret and anticipate human movement---a task complicated by the inherent unpredictability of human behaviour. Prediction models, such as \[(https://arxiv.org/html/2506.21205v2#bib.bib4)\], provide probabilistic distributions over potential human trajectories. To ensure safe and efficient navigation, these probabilistic predictions must be incorporated into the motion planning process \[(https://arxiv.org/html/2506.21205v2#bib.bib5), (https://arxiv.org/html/2506.21205v2#bib.bib6), (https://arxiv.org/html/2506.21205v2#bib.bib7)\].

A key challenge in planning under uncertainty is finding a safe trajectory despite the stochastic nature of surrounding obstacles. One approach to handle uncertainty in dynamic environments is robust optimization \[(https://arxiv.org/html/2506.21205v2#bib.bib8)\], which enforces safety guarantees by considering worst-case scenarios within bounded uncertainty sets. This method assumes that the probability density of uncertainty is nonzero within a defined region of the ego agent's workspace, ensuring strict safety constraints. However, by accounting for all possible uncertainty realizations, robust optimization often leads to overly cautious behaviour, potentially rendering solutions infeasible in densely populated environments---a phenomenon commonly referred to as the "frozen robot" problem \[(https://arxiv.org/html/2506.21205v2#bib.bib9)\]. To mitigate excessive conservatism, stochastic optimization offers an alternative by employing chance constraints \[(https://arxiv.org/html/2506.21205v2#bib.bib10), (https://arxiv.org/html/2506.21205v2#bib.bib11), (https://arxiv.org/html/2506.21205v2#bib.bib12)\] that probabilistically bound the likelihood of constraint violations within a specified confidence level $\sigma$. This relaxation allows for more flexible decision-making while maintaining a controlled level of risk, enabling robots to navigate complex environments more effectively than purely robust approaches. In this work, we propose a risk-aware Model Predictive Path Integral (MPPI) that uses Monte-Carlo sampling to approximate the chance constraints for a mobile robot navigating among dynamic agents.

## Related Work

In stochastic optimization, constraint violations are regulated using chance constraints, which ensure that the probability of satisfying a given nominal constraint remains within a predefined threshold. Evaluating chance constraints exactly is often infeasible in real-world scenarios, necessitating approximations. Many existing methods address this challenge by introducing simplifying assumptions, such as modelling uncertainty with Gaussian distributions \[(https://arxiv.org/html/2506.21205v2#bib.bib10)\] or restricting the robot's dynamics to linear systems \[(https://arxiv.org/html/2506.21205v2#bib.bib13), (https://arxiv.org/html/2506.21205v2#bib.bib14)\]. While these approximations facilitate tractability, they also limit the flexibility of the approach. Recent research has made significant progress in overcoming these limitations, enabling stochastic optimization to accommodate nonlinear robot dynamics and more general uncertainty distributions \[(https://arxiv.org/html/2506.21205v2#bib.bib12)\] by leveraging scenario optimization \[(https://arxiv.org/html/2506.21205v2#bib.bib15)\]. However, the Collision Probability (CP) in these works is computed per obstacle, which degrades performance when more obstacles influence the plan, i.e., in crowded environments. In addition, empirical evaluations indicate that the actual risk associated with the planned trajectory is significantly lower than the upper bound imposed by the chance constraint formulation \[(https://arxiv.org/html/2506.21205v2#bib.bib10), (https://arxiv.org/html/2506.21205v2#bib.bib11), (https://arxiv.org/html/2506.21205v2#bib.bib12)\]. To address this issue, \[(https://arxiv.org/html/2506.21205v2#bib.bib16)\] introduced a method to quantify the risk of planned trajectories by running multiple probabilistic planners in parallel with varying risk thresholds. This approach provides probabilistic safety guarantees by attaining a closer bound to the specified risk. However, the scalability of this approach is constrained by the number of probabilistic planners that can be executed in parallel. With the advantage of not requiring gradient information, probabilistic safety measures have been successfully employed in sampling-based motion planning frameworks. In \[(https://arxiv.org/html/2506.21205v2#bib.bib17), (https://arxiv.org/html/2506.21205v2#bib.bib18)\], chance constraints are applied to the Rapidly Random Trees (RRT) algorithm such that each node in the tree is statistically safe. \[(https://arxiv.org/html/2506.21205v2#bib.bib19)\] integrates risk measures to estimate the risk of violating a predefined safety specification into a sampling-based trajectory \[(https://arxiv.org/html/2506.21205v2#bib.bib20)\] to plan minimal risk trajectories. Model Predictive Path Integral (MPPI), a gradient-free local motion planner, has the advantage of massive parallelizability to compute finite horizon plans online via sampling \[(https://arxiv.org/html/2506.21205v2#bib.bib21)\]. \[(https://arxiv.org/html/2506.21205v2#bib.bib22)\] integrates the Conditional Value-at-Risk (CVaR) measure into MPPI to generate optimal control actions but only accounts for the uncertainty in the robot's own dynamics.

In this paper, we propose Dynamic Risk-Aware MPPI (DRA-MPPI), a planner approximating joint CPs among several dynamic obstacles by evaluating the probabilistic distributions of dynamic agents' predicted trajectories, which can be non-Gaussian. The approximated probability of collision becomes a chance constraint by assigning a high enough cost to samples that violate the maximum threshold, essentially rejecting them from the final plan. Leveraging Monte Carlo (MC) sampling \[(https://arxiv.org/html/2506.21205v2#bib.bib23)\] enables greater flexibility and computational efficiency, as it effectively handles arbitrary probability distributions and scales well with an increasing number of dynamic agents.

### II-A Contributions

Our main contributions are twofold:

DRA-MPPI: An MPPI-based planner that approximates the CPs of trajectories using MC methods. It handles joint CPs over several dynamic obstacles and manages non-Gaussian predictions with minimal approximations.

A computationally efficient strategy to find the MC approximation of the joint CP for several hundred samples in parallel, achieving real-time performance.

We design a comprehensive cost function for efficient navigation and validate the approach through simulations and real-world experiments with pedestrians. Our method, tested with Gaussian and non-Gaussian models, is compared to a state-of-the-art Scenario-based Model Predictive Control (S-MPC), a risk-aware Frenét planner, and a vanilla MPPI.

## Preliminaries

We consider a controlled robot moving in a 2D plane, $\mathcal{W} \subseteq {\mathbb{R}}^{2}$, with non-linear discrete-time dynamics given by:

where ${\mathbf{x}}_{t} = \left\lbrack {\mathbf{q}}_{t},\psi_{t} \right\rbrack \in {\mathbb{R}}^{n_{x}}$ and ${\mathbf{u}}_{t} \in {\mathbb{R}}^{n_{u}}$ denote the state and control input of the robot at stage $t$ respectively. The state of the robot ${\mathbf{x}}_{t}$ contains its position ${\mathbf{q}}_{t} = {\lbrack x_{t},y_{t}\rbrack} \in {\mathbb{R}}^{2} \subseteq {\mathbb{R}}^{n_{x}}$ and orientation $\psi_{t}$. The robot navigates in an environment occupied by $N_{o}$ dynamic obstacles whose future trajectories must be predicted. This necessitates a dynamic model of the obstacles' motion, enabling the robot to proactively account for the obstacles' behaviour while generating its own trajectory.

### III-A Dynamic Obstacle Model

The motion planner uses a model that probabilistically forecasts the behaviour of surrounding agents. In this setting, we model the positions of $N_{o}$ dynamic obstacles as random variables. Specifically, the uncertain position of obstacle $o$ at time step $t$ as ${\mathbf{δ}}_{t}^{o} = {\lbrack x_{t}^{o},y_{t}^{o}\rbrack} \in \Delta$, where $\Delta$ is the probability space capturing the uncertainty in the perception of these obstacles. This uncertainty is characterized by a probability measure $\mathbb{P}$. To capture the inherent multi-modality in obstacle behaviour, we model the uncertainty in their motion using a Mixture-of-Gaussians (MoG) distribution. This approach provides a flexible and expressive representation of uncertainty by combining multiple continuous probability distributions. Specifically, the probability density function of an obstacle's position at time step $t$ is given by:

where $N_{m}$ is the number of modes of the MoG, $\phi_{i}$ represents the weight associated with each mode such that ${\sum_{i = 1}^{N_{m}}\phi_{i}} = 1$, and $p_{t,i}^{o}{( \cdot )}$ is the probability density function of the $i^{\text{th}}$ mode with mean ${\mathbf{μ}}_{i} \in {\mathbb{R}}^{2}$ and covariance $\mathbf{\Sigma}_{i} \in {\mathbb{R}}^{2 \times 2}$:

As a result, the prediction model outputs a sequence of state distributions over the prediction horizon for each possible mode, enabling the planner to account for the stochastic nature of obstacle motion.

### III-B Probabilistic Collision Avoidance

The problem of planning under uncertainty can be formulated as a chance-constraint collision avoidance problem. Given a cost function $J$, the initial state of the robot ${\mathbf{x}}_{0} = {\mathbf{x}}_{\text{init}}$, and the predicted future states of all obstacles $p_{t,i}^{o}{( \cdot )}$ over a horizon $T$, the objective is to compute optimal control inputs that guide the robot from its initial state to progress along a reference path, while the collision probability with any moving obstacle at each stage $t$ is below an acceptable threshold $\sigma$. The resulting optimization problem is given by:

$\min\limits_{{\mathbf{u}} \in {\mathbb{U}}}\mspace{21mu}$ ${\sum\limits_{t = 0}^{T - 1}{J_{t}{({\mathbf{x}}_{t},{\mathbf{u}}_{t})}}} + {J_{T}{({\mathbf{x}}_{T})}}$ (4a)
s.t. ${{\mathbf{x}}_{0} = {\mathbf{x}}_{\text{init}}},$ (4b)
${{{\mathbf{x}}_{t + 1} = {\mathcal{F}{({\mathbf{x}}_{t},{\mathbf{u}}_{t})}}},{{{\mathbf{x}} \in {\mathbb{X}}},{{\mathbf{u}} \in {\mathbb{U}}}}},$ (4c)
${{{\mathbb{P}}\left\lbrack {{\|{{\mathbf{q}}_{t} - {\mathbf{δ}}_{t}^{o}}\|}_{2} > {r,{\forall o}}} \right\rbrack} \geq {{1 - \sigma},{\forall t}}},$ (4d)

where $J_{t}{({\mathbf{x}}_{t},{\mathbf{u}}_{t})}$ represents the stage cost of the robot, and $J_{T}{({\mathbf{x}}_{T})}$ denotes the terminal cost. States ${\mathbf{x}}_{t}$ and inputs ${\mathbf{u}}_{t}$ are bounded by the state and input constraint sets $\mathbb{X}$ and $\mathbb{U}$, and radius $r$ is the sum of the robot and obstacle radii.

### III-C Model Predictive Path Integral Control (MPPI)

Model Predictive Path Integral control (MPPI) \[(https://arxiv.org/html/2506.21205v2#bib.bib21), (https://arxiv.org/html/2506.21205v2#bib.bib24)\] is a sampling-based optimization method for solving stochastic optimal control problems. We consider a discrete-time dynamical system governed by the state-transition equation:

where $\mathcal{F}$ represents a nonlinear state-transition function that dictates the evolution of the state $\mathbf{x}$ over discrete time steps $t$. The control input ${\mathbf{v}}_{t}$ follows a Gaussian distribution centered at the commanded input ${\mathbf{u}}_{t}$ with covariance $\Sigma$. To generate potential system trajectories, a set of $K$ perturbed control sequences sequences $V_{k}$ is sampled and rolled-out through the model $\mathcal{F}$, producing $K$ corresponding state trajectories ${X_{k},k} \in {\lbrack 0,{K - 1}\rbrack}$, over a planning horizon of length $T$. Given the state trajectories $X_{k}$ and a predefined cost function $\mathcal{C}$ to be minimized, the total state-cost $S_{k}$ for each sampled sequence $V_{k}$ is computed by evaluating $S_{k} = {\mathcal{C}{(X_{k})}}$. An importance-sampling weighting scheme is then employed to approximate the optimal control sequence. The weight $w_{k}$ associated with trajectory $X_{k}$ is computed using an inverse exponential function of the cost $S_{k}$, adjusted by a tuning parameter $\beta$ known as the inverse temperature:

Here, the minimum sampled cost $\rho = {\min_{k}S_{k}}$ is introduced to enhance numerical stability, and $\eta$ is a normalization factor ensuring weights sum to unity. The final control input sequence $U^{\ast}$ is then computed as a weighted sum of the sampled control sequences:

Once the optimal control sequence $U^{\ast}$ is obtained, only the first control input ${\mathbf{u}}_{0}^{\ast}$ is applied to the system. The procedure is then repeated at the next time step, where, at the next iteration, a time-shifted $U^{\ast}$ is used as a warm-start.

### III-D Risk Assessment

To quantify risk in the context of pedestrian-robot interactions, we define a risk metric that assesses the likelihood of collision. Let $\mathcal{Z}$ represent the set of random variables capturing the uncertainty in pedestrian motion in the $x$ and $y$ directions. The risk metric is a function $\zeta:{\mathcal{Z}\mapsto{\mathbb{R}}}$ that maps these random variables to a real value corresponding to the collision probability. The probability of collision with an obstacle $o$, the marginal probability, is then expressed as:

where the integration domain $\mathcal{R}_{t}^{\circ}$ is defined as a circular region, with radius $r$, centered at the planned robot pose ${\mathbf{q}}_{t}$ at stage $t$ along the planning horizon.

When $o > 1$, the probability of colliding with at least one obstacle is given by the joint collision probability \[(https://arxiv.org/html/2506.21205v2#bib.bib25)\]. Since, at each time step $t$, the marginal probabilities can be assumed independent, the joint collision probability can be computed using a multiplicative approach:

## Proposed Approach

To assess the risk associated with the robot's optimal trajectory in MPPI, (https://arxiv.org/html/2506.21205v2#S3.E8 "In III-D Risk Assessment ‣ III Preliminaries ‣ Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations") and (https://arxiv.org/html/2506.21205v2#S3.E9 "In III-D Risk Assessment ‣ III Preliminaries ‣ Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations") must be evaluated for each sample and each time step in the horizon. For example, with $K = 400$ MPPI samples and a horizon $T = 20$, we must compute the collision probability $8000$ times at each controller iteration. Computing these analytically is not feasible if the controller is to run in real-time. In [Section IV-A](https://arxiv.org/html/2506.21205v2#S4.SS1 "IV-A Monte Carlo Approximation ‣ IV Proposed Approach ‣ Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations"), we propose a Monte Carlo approximation to estimate the joint collision probability for many trajectories efficiently and in parallel. The cost function used to evaluate MPPI samples is detailed in [Section IV-B](https://arxiv.org/html/2506.21205v2#S4.SS2 "IV-B Cost Formulation ‣ IV Proposed Approach ‣ Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations"), and an overview of the algorithm is presented in [Section IV-C](https://arxiv.org/html/2506.21205v2#S4.SS3 "IV-C Algorithm ‣ IV Proposed Approach ‣ Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations").

### IV-A Monte Carlo Approximation

We propose an algorithm to compute all $N_{o}$ integral approximations for all $K$ samples efficiently and in parallel, allowing good scalability with the number of dynamic obstacles and samples. The process begins by sampling $N_{mc}$ Monte Carlo coordinates from a rectangular collision region $\mathcal{R}_{t}^{\square}$, which is bounded as follows:

The bounds of this region are determined by the minimum and maximum spatial positions of the robot's states across all rollouts $K$ at time step $t$, extended by the radius $r$:

Here, $x_{k,t}$ and $y_{k,t}$ denote the $x$ and $y$ robot's position for rollout $k$ at timestep $t$. By taking the minimum and maximum values as bounds and extending the area with the integral radius $r$, we cover the whole area where we need to approximate the integrals at time step $t$.\
Depending on the obstacles' trajectory predictions, we get $N_{o} \times N_{m}$ total number of modes for all obstacles. To approximate the integral for all rollouts $K$ we first evaluate the joint collision probability for all MC sample $j$:

where $x_{j},y_{j}$ represents a single MC sample. We then identify which of these sampled coordinates fall within the region $\mathcal{R}_{k,t}^{\circ}$ of each $k$ and compute the CP over the relevant domain:

where $\pir^{2}$ is the area of the collision region and $N_{\mathcal{R}_{k,t}^{\circ}}$ is the number of Monte Carlo samples in the circular region $\mathcal{R}_{k,t}^{\circ}$ acting as a normalization factor. $\mathbb{1}_{\mathcal{R}_{k,t}^{\circ}}$ is an indicator function to consider only MC samples in the circular collision region $\mathcal{R}_{k,t}^{\circ}$. Given that all the coordinates $x_{k,t}$ and $y_{k,t}$ will be fairly close $\forall k$, there will also be significant overlap in the integration regions $\mathcal{R}_{k,t}^{\circ}$. Thus, the computation effort is massively reduced by using our approach of drawing and evaluating the MC samples only once $\forall k$. The Standard Error (SE) of $\hat{\mathcal{P}}$, if $\mathcal{P}^{\text{joint}}$ were Gaussian distributed, would scale with $\sqrt{\Sigma_{\mathcal{P}^{\text{joint}}}}/N_{\mathcal{R}_{k,t}^{\circ}}$. In practice, we do not know a priori the number of samples in the collision region, and $\mathcal{P}^{\text{joint}}$ is non-gaussian but, compared to an analytical solution, we have empirically observed that we misclassify the CP to be below the threshold less than 2% of the times.

### IV-B Cost Formulation

A key component of MPPI is the design of the cost function $S_{k}$. We design our cost function as:

where $\mathcal{C}_{\text{tracking}}$ drives the robot towards its goal and penalizes the lateral deviation from the reference path, $\mathcal{C}_{\text{speed}}$ penalizes differences with reference speed, and $\mathcal{C}_{\text{rotation}}$ penalizes angular velocity. $\mathcal{C}_{\text{risk}}$ is defined as:

with $\omega_{\text{soft}}$ and $\omega_{\text{hard}}$ being tunable weights. The first part, $\omega_{\text{soft}}\hat{\mathcal{P}}{({\mathbf{q}}_{k,t})}$, is a linear penalty on any collision probabilities, incentivising the planner to always choose lower risk. The second part, $\omega_{\text{hard}}\mathbb{1}_{\sigma}{({\hat{\mathcal{P}}{({\mathbf{q}}_{k,t})}})}$ is an indicator function returning $1$ when the CP is above a chosen risk threshold $\sigma$. Every sampled trajectory with a CP above the threshold, assuming that $\omega_{\text{hard}}$ is high enough and that at least a few low-risk trajectories are sampled, will receive close to zero weight in the average in (https://arxiv.org/html/2506.21205v2#S3.E7 "In III-C Model Predictive Path Integral Control (MPPI) ‣ III Preliminaries ‣ Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations"), essentially being rejected. One advantage is that if, for example, the robot starts planning from a state with CP above the threshold, MPPI still returns a solution in which the CP and the number of time steps with CP above the threshold will be minimised.

### IV-C Algorithm

[Algorithm 1](https://arxiv.org/html/2506.21205v2#alg1 "In IV-C Algorithm ‣ IV Proposed Approach ‣ Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations") summarizes the proposed approach. Note that operations over $k$ and $j$ are parallelized, while the ones over $t$, i.e. rolling out the trajectories, are performed sequentially.

As in \[(https://arxiv.org/html/2506.21205v2#bib.bib26)\], $\mathcal{E}_{k}$ are splines fitted to a Halton sequence for improved smoothness, the inverse temperature $\beta$ is updated online, and $U^{\ast}$ is time-shifted to be reused in the next iteration. We also always take one sample to be zero velocity throughout the horizon. This helps MPPI to converge to a braking manoeuvre when all other samples fail \[(https://arxiv.org/html/2506.21205v2#bib.bib27)\].

### Remark 1

A key difference between MPPI and MPC is that MPPI's planned trajectory is not meant to be applied in open loop. When symmetries are present, e.g. when a robot faces an obstacle ahead, MPPI's plan might go straight through the obstacle. This is intuitively clear given the weighted average in (https://arxiv.org/html/2506.21205v2#S3.E7 "In III-C Model Predictive Path Integral Control (MPPI) ‣ III Preliminaries ‣ Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations"). For certain types of systems and cost functions, MPPI can be related to Path Integral Control \[(https://arxiv.org/html/2506.21205v2#bib.bib21)\]. Within the Path Integral control framework, because there is an assumption that the actions of the ego-agent are noisy, attempting to drive straight to the obstacle for a while is the optimal action. The symmetry is proven to break at some point \[(https://arxiv.org/html/2506.21205v2#bib.bib28)\]. For our planner, this means that while we can reject the samples $k$ with collision probability higher than the threshold $\sigma$, we cannot guarantee that the resulting plan doesn't violate the threshold. Again, this is expected as, in MPPI, only the first input of $U^{\ast}$ is applied, and the rest is only used for warm-starting the next iteration.

{{\hat{\mathcal{P}}}_{k,{t + 1}}\leftarrow} &amp; {\text{estimateJointCP}{({\mathbf{x}}_{k,{t + 1}},}} \\
&amp; {\left\lbrack \mathcal{P}_{1}^{\text{joint}},\ldots,\mathcal{P}_{N_{mc}}^{\text{joint}} \right\rbrack)}
16: $S_{k}\leftarrow{\text{getCost}{(X_{k},\left\lbrack {\hat{\mathcal{P}}}_{k,1},\ldots,{\hat{\mathcal{P}}}_{k,T} \right\rbrack)}}$ ⊳ 13
Algorithm 1 Dynamic Risk-Aware MPPI

Figure 1: Snapshots from the simulated environment under Gaussian pedestrian motion at different time instants. Blue circles depict the robot’s plan, whereas the pedestrians’ predicted trajectories are illustrated in distinct coloured circles. The black walls on both sides represent the corridor boundaries.

## Simulation Experiments

This section evaluates the proposed approach in the context of mobile robot navigation in a crowded environment shared with humans. Our algorithm's implementation is built upon previous open-source MPPI solvers \[(https://arxiv.org/html/2506.21205v2#bib.bib26), (https://arxiv.org/html/2506.21205v2#bib.bib27)\]. The proposed approach is developed in Python using PyTorch and integrated with the Robot Operating System (ROS). The laptop running the simulations has an Intel^®^ Core^TM^ i7 CPU@2.6GHz and NVIDIA GeForce RTX 2080.

### V-A Simulation Setup

The experimental evaluation is conducted in a simulated environment featuring a Clearpath Jackal robot navigating a 6-meter-wide corridor alongside multiple pedestrians. The robot has to follow the corridor's centerline while maintaining a reference velocity of $2$m/s. A visualization with Gaussian predictions is given in [Fig. 1](https://arxiv.org/html/2506.21205v2#S4.F1 "In IV-C Algorithm ‣ IV Proposed Approach ‣ Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations"). The simulator runs at $20$Hz, while the controllers run at $5$Hz. Pedestrian dynamics are modelled using the Social Forces \[(https://arxiv.org/html/2506.21205v2#bib.bib29)\], implemented via open-source software \[(https://arxiv.org/html/2506.21205v2#bib.bib30)\]. In this model, pedestrians avoid one another and the robot. Future pedestrian positions are predicted by the robot's motion planner using a constant velocity assumption. The mismatch between the model used for simulation and prediction is to emulate a real-world scenario where the predictions do not always match the ground-truth trajectory. Pedestrians are modelled with a radius of $0.3$m and spawn on both sides of the corridor, and their goal is to reach the opposing side. The robot dynamics are described by a second-order unicycle model \[(https://arxiv.org/html/2506.21205v2#bib.bib31)\]. Simulations are conducted for three scenarios featuring $4$, $8$, and $12$ pedestrians to evaluate the planner's performance under varying crowd density levels.

### V-A1 Pedestrians with Gaussian noise

In this setup, we model the uncertainty in pedestrian motion using a unimodal Gaussian distribution with covariance matrix $\mathbf{\Sigma}_{w} = {0.3^{2}{\mathbf{I}}}$. By 'unimodal', it is meant that we predict a single trajectory for each pedestrian. We define the pedestrians' dynamics as:

where ${\mathbf{v}} \in {\mathbb{R}}^{2}$ is the velocity that follows the social forces model. The additive noise ${\mathbf{δ}}_{w,t}$ introduces stochastic perturbations, capturing the variability in pedestrian motion.

### V-A2 Pedestrians with Mixture of Gaussians

In this setup, pedestrian motion is modelled as a Markov Chain, where transitions govern changes in the movement direction. Specifically, a pedestrian follows a horizontal trajectory with probability $p = 0.975$ at each time step while transitioning to a diagonal trajectory with probability $p = 0.025$. This behaviour is further perturbed by Gaussian noise as before. The pedestrians' dynamics are described by:

where $B$ is a transformation vector that depends on the current state of the Markov Chain and $\mathbf{v}$ is a constant preferred velocity. If the pedestrian is in the horizontal state, $B = \begin{bmatrix}
\end{bmatrix}^{T}$. Conversely, if the pedestrian switches to the diagonal state, $B = \begin{bmatrix}
\end{bmatrix}^{T}$. The uncertainties associated with this motion can be modelled as a Mixture of Gaussians where each state transition in the Markov Chain leads to a separate mode with an associated probability. For a planning horizon of $T = 20$, the pedestrian may switch from horizontal to diagonal movement every 5-time steps, resulting in 4 distinct modes per pedestrian.

## Pedestrians

Table I: Performance comparison of different planning methods under different pedestrian densities. Quantitative results were obtained from over 100 experiments for uni-modal pedestrian predictions.

## Pedestrians

Table II: Performance comparison of different planning methods under different pedestrian densities. Quantitative results are obtained from 100 experiments for multi-modal pedestrian predictions.

### V-B Comparison to Baselines

We compare DRA-MPPI against three baselines. Baselines are selected on the availability of an open-source implementation and their application to navigation in 2-D dynamic environments. We consider the following baselines:

Stochastic Model Predictive Control (SH-MPC) \[(https://arxiv.org/html/2506.21205v2#bib.bib25)\]: This baseline uses a scenario-based MPC and formulates the collision avoidance chance constraints over the entire trajectory as a scenario program.

Vanilla MPPI \[(https://arxiv.org/html/2506.21205v2#bib.bib21)\]: This baseline assumes deterministic pedestrians' behaviour by considering only the mean predicted trajectories and plans around them.

Frenét Planner \[(https://arxiv.org/html/2506.21205v2#bib.bib32)\]: This sampling-based planner generates trajectories in the Frenét coordinate system. The risk metric used is similar to previous work \[(https://arxiv.org/html/2506.21205v2#bib.bib33)\].

All planners have a horizon of $T = 20$ steps, with a discretization step of $0.2$s, resulting in a time horizon of $4.0$s. We set the maximum allowable risk level to $\sigma = 0.05$. DRA-MPPI uses $K = 400$ and $N_{mc} = 20000$ samples. The following metrics are considered for evaluation:

Task Duration: Measures the time required for the robot to reach the end of the corridor.

Velocity: Determines the average velocity maintained throughout the experiment.

Collision Probability: Quantifies each experiment's maximum joint collision probability (CP). The CP we report is computed a posteriori. Given the remark in [section IV-C](https://arxiv.org/html/2506.21205v2#S4.SS3 "IV-C Algorithm ‣ IV Proposed Approach ‣ Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations"), the CP is only reported for the current time step instead of over the planned trajectory.

Success Rate (SR): Evaluates the proportion of experiments in which the robot successfully avoids collisions with pedestrians and reaches its goal.

Figure 2: The visualization illustrates the task duration, defined as the time required to reach the goal, under a uni-modal pedestrian prediction setting. Our method demonstrates a lower variance in task duration and a shorter completion time compared to SH-MPC and the Frenét Planner. While Vanilla MPPI achieves the shortest task duration, this comes at the cost of a higher collision rate, as reported in Table I.

Figure 3: Visualization of maximum collision probability across 100 experiments under uni-modal pedestrian prediction setup. Frenét Planner is discarded from this Fig. for better readability as its CP is much higher than SH-MPC and DRA-MPPI as seen in Table I.

Figure 4: Visualization of the task duration under multi-modal pedestrian prediction setting. Same conclusions as the uni-modal case.

Figure 5: Visualization of maximum collision probability across 100 experiments under multi-modal pedestrian prediction setup.

Figure 6: Four snapshots of a Jackal robot running DRA-MPPI among five pedestrians. In orange is the trajectory planned by our proposed approach, with the top 30 samples colour-graded by their relative cost. In blue are the predicted trajectories of the pedestrians, and the circle size represents three standard deviations from the mean predicted centre of the obstacle. In green is the reference path. The behaviour is best appreciated in the accompanying video.

[Table I](https://arxiv.org/html/2506.21205v2#S5.T1 "In V-A2 Pedestrians with Mixture of Gaussians ‣ V-A Simulation Setup ‣ V Simulation Experiments ‣ Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations") and [Fig. 2](https://arxiv.org/html/2506.21205v2#S5.F2 "In V-B Comparison to Baselines ‣ V Simulation Experiments ‣ Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations") and (https://arxiv.org/html/2506.21205v2#S5.F3 "Fig. 3 ‣ V-B Comparison to Baselines ‣ V Simulation Experiments ‣ Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations") present a quantitative comparison of different planning methods across varying pedestrian densities under uni-modal pedestrian predictions. The results, averaged over $100$ experiments, highlight the trade-offs between task efficiency and safety among the evaluated approaches. Our proposed approach (DRA-MPPI) consistently demonstrates a favourable balance between task duration and safety. While Vanilla MPPI achieves the shortest task duration across all scenarios, it does so at the expense of significantly lower safety due to its lack of risk awareness, particularly as pedestrian density increases. For instance, in the presence of $12$ pedestrians, Vanilla MPPI completes the task in $18.98$s but exhibits the lowest safety rate ($43$%), indicating a high collision frequency. In contrast, DRA-MPPI maintains a competitive task duration ($19.86$s) while achieving a significantly higher safety rate of $98$%, demonstrating its robustness in crowded environments. The Frenét Planner exhibits longer task duration and suffers a notable drop in safety, particularly at higher pedestrian densities ($74\%$ safety at 12 pedestrians). This deterioration arises from the planner's design, which does not explicitly optimize for risk minimization. Instead, it evaluates a set of sampled trajectories based on assigned costs and selects the one with the lowest one. However, in dense environments, the trajectory with the minimum cost may still entail substantial risk, as observed in the experimental results.

### Remark 2

It is important to stress that, in our simulator, the pedestrians move with Social Forces but are predicted by a constant velocity model, i.e. the predictions are not the ground truth behaviour. This may result in the planner thinking its plan is below the risk threshold while, at the next iteration, it may find itself at a starting pose with a higher-than-allowed collision probability.

SH-MPC strives to track the reference path very closely, often finding itself in riskier positions. SH-MPC relaxes the constraints with slack variables when no feasible solution is found in these riskier situations. When infeasible, SH-MPC switches to a fallback policy (braking). This leads to SH-MPC taking longer to complete the task and often exhibiting collision probabilities higher than the threshold at least a few times per experiment, severely impacting the metrics.

Thanks to its cost (https://arxiv.org/html/2506.21205v2#S4.E13 "In IV-B Cost Formulation ‣ IV Proposed Approach ‣ Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations"), DRA-MPPI always minimizes the CP, even when below the threshold. This makes it strive to avoid riskier situations altogether. Moreover, when DRA-MPPI finds itself in a riskier situation, it will try to return to a state with CP below the threshold in the least amount of steps possible. For these reasons, DRA-MPPI demonstrates good task completion times while providing the highest safety. Moreover, DRA-MPPI and Vanilla MPPI exhibit a lower variance in task duration across experiments, indicating better consistency than SH-MPC and Frenét Planner.

[Table II](https://arxiv.org/html/2506.21205v2#S5.T2 "In V-A2 Pedestrians with Mixture of Gaussians ‣ V-A Simulation Setup ‣ V Simulation Experiments ‣ Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations") and [Fig. 4](https://arxiv.org/html/2506.21205v2#S5.F4 "In V-B Comparison to Baselines ‣ V Simulation Experiments ‣ Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations") and (https://arxiv.org/html/2506.21205v2#S5.F5 "Fig. 5 ‣ V-B Comparison to Baselines ‣ V Simulation Experiments ‣ Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations") show that the key observations from the uni-modal case also hold in the multi-modal setting. DRA-MPPI outperforms other methods in balancing task efficiency and safety. It achieves the shortest task duration ($19.67$s) while maintaining the highest safety rate ($99\%$), demonstrating its ability to navigate complex, uncertain environments effectively. In contrast, Vanilla MPPI completes the task in a comparable time ($19.71$s) but at the cost of reduced safety ($78\%$), reflecting its lack of risk-awareness. DRA-MPPI also remains close to the maximum allowable risk while ensuring safety, demonstrating its consistency and robustness in complex pedestrian environments.

### V-C Computation Time

In [Tables I](https://arxiv.org/html/2506.21205v2#S5.T1 "In V-A2 Pedestrians with Mixture of Gaussians ‣ V-A Simulation Setup ‣ V Simulation Experiments ‣ Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations") and [II](https://arxiv.org/html/2506.21205v2#S5.T2 "Table II ‣ V-A2 Pedestrians with Mixture of Gaussians ‣ V-A Simulation Setup ‣ V Simulation Experiments ‣ Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations"), we also report the computation time (runtime) for SH-MPC and our approach. DRA-MPPI takes just below $100$ms to compute the control action in the uni-modal four-agents experiment, while SH-MPC is almost twice as fast. Both methods scale quite gracefully over the number of agents with multi-modal predictions. However, it is important to note that SH-MPC is written in C++, while DRA-MPPI is implemented in PyTorch. Recent work shows a reduction of compute time of up to two orders of magnitude when running MPPI in CUDA vs Pytorch \[(https://arxiv.org/html/2506.21205v2#bib.bib34)\], highlighting the potential for these massively parallelizable approaches.

## Real Robot Experiments

This section demonstrates the DRA-MPPI for a mobile robot driving among pedestrians in an arena, highlighting the real-time capability of the proposed approach.

### VI-A Experimental Setup

The experiment occurs in a large arena where pedestrians walk alongside the robot. The robot and pedestrians' positions are tracked by a motion capture system operating at 20 Hz. Pedestrian positions are filtered through a Kalman filter that also estimates velocities, which the planner uses to produce constant velocity predictions. The pedestrians are assumed to follow an uni-modal Gaussian distribution with a covariance matrix of $\mathbf{\Sigma}_{w} = {0.1^{2}{\mathbf{I}}}$. The robot follows a reference path between two opposite sides of the environment and performs a turn upon reaching each side. The cost function is the same as in (https://arxiv.org/html/2506.21205v2#S4.E13 "In IV-B Cost Formulation ‣ IV Proposed Approach ‣ Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations").

### VI-B Results

In this set of experiments, the pedestrians were instructed to walk naturally from one side to the other while interacting with the robot. The experiment was conducted over a duration of $65$ seconds, with snapshots captured at various time instances, as illustrated in Fig. (https://arxiv.org/html/2506.21205v2#S5.F6 "Fig. 6 ‣ V-B Comparison to Baselines ‣ V Simulation Experiments ‣ Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations"). Throughout the trials, the maximum collision probability observed for the robot was $0.054$, with an average of $0.023$ and a standard deviation of $0.011$. Notably, no collisions were recorded.

## Conclusions

We have presented DRA-MPPI, an MPPI-based planner capable of computing, in parallel, at each time step, the joint collision probability among many dynamic obstacles using potentially non-Gaussian predictions. Thanks to its gradient-free nature, we have shown that DRA-MPPI can reject samples with a collision probability above a desired threshold and directly minimise the collision probability.

In simulated experiments, while the pedestrians were predicted with constant velocity, they moved with Social Forces. DRA-MPPI demonstrated the highest robustness to this mismatch by being the safest method among a Scenario-Based MPC approach, a risk-aware Frenét Planner, and a Vanilla MPPI while maintaining high speed and good task completion times. Similar conclusions were drawn in experiments where the pedestrians could randomly switch directions, predicted by a Gaussian Mixture Model, demonstrating efficient planning with non-Gaussian distributions.

Real-robot experiments showcased DRA-MPPI's ease of transfer to the real world and real-time performance. Although we relied on a motion capture system, the pedestrian's state and the map can be retrieved from onboard sensors \[(https://arxiv.org/html/2506.21205v2#bib.bib35)\].

While already real-time, in future work our PyTorch implementation could be rewritten in CUDA, dramatically improving computation times \[(https://arxiv.org/html/2506.21205v2#bib.bib34)\]. This could also allow for real-time computations of the Monte Carlo approximation of the joint collision probability over the planning horizon, allowing for accurate constraining of the joint collision probability over the entire trajectory.
