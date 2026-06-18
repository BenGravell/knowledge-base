<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations

Topics include Model predictive control, Predictive control, Robotics, Safety, Uncertainty, Real-time systems, Control, Monte Carlo methods, Distributionally robust model predictive path integral control, Scenario-based, S-MPC, Mobile robots.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Deploying mobile robots safely among humans requires the motion planner to account for the uncertainty in the other agents' predicted trajectories. This remains challenging in traditional approaches, especially with arbitrarily shaped predictions and real-time constraints. To address these challenges, we propose a Dynamic Risk-Aware Model Predictive Path Integral control (DRA-MPPI), a motion planner that incorporates uncertain future motions modelled with potentially non-Gaussian stochastic predictions. By leveraging MPPI's gradient-free nature, we propose a method that efficiently approximates the joint Collision Probability (CP) among multiple dynamic obstacles for several hundred sampled trajectories in real-time via a Monte Carlo (MC) approach. This enables the rejection of samples exceeding a predefined CP threshold or the integration of CP as a weighted objective within the navigation cost function. Consequently, DRA-MPPI mitigates the freezing robot problem while enhancing safety. Real-world and simulated experiments with multiple dynamic obstacles demonstrate DRA-MPPI's superior performance compared to state-of-the-art approaches, including Scenario-based Model Predictive Control (S-MPC), Frenet planner, and vanilla MPPI.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Mobile robots have the potential to enhance various aspects of daily life, from optimizing logistics in warehouses to enabling safer and more efficient transportation through autonomous vehicles. However, for robots to be successfully integrated into real-world settings like urban areas, they must be capable of safely and efficiently manoeuvring through human-populated spaces. Achieving this requires an ability to interpret and anticipate human movement---a task complicated by the inherent unpredictability of human behaviour. Prediction models, such as, provide probabilistic distributions over potential human trajectories. To ensure safe and efficient navigation, these probabilistic predictions must be incorporated into the motion planning process.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

A key challenge in planning under uncertainty is finding a safe trajectory despite the stochastic nature of surrounding obstacles. One approach to handle uncertainty in dynamic environments is robust optimization, which enforces safety guarantees by considering worst-case scenarios within bounded uncertainty sets. This method assumes that the probability density of uncertainty is nonzero within a defined region of the ego agent's workspace, ensuring strict safety constraints. However, by accounting for all possible uncertainty realizations, robust optimization often leads to overly cautious behaviour, potentially rendering solutions infeasible in densely populated environments---a phenomenon commonly referred to as the "frozen robot" problem. To mitigate excessive conservatism, stochastic optimization offers an alternative by employing chance constraints that probabilistically bound the likelihood of constraint violations within a specified confidence level $\sigma$. This relaxation allows for more flexible decision-making while maintaining a controlled level of risk, enabling robots to navigate complex environments more effectively than purely robust approaches. In this work, we propose a risk-aware Model Predictive Path Integral (MPPI) that uses Monte-Carlo sampling to approximate the chance constraints for a mobile robot navigating among dynamic agents.

<!-- chunk {"id": "body-0005", "role": "body", "section": "II-A Contributions", "weight": 1.0} -->

DRA-MPPI: An MPPI-based planner that approximates the CPs of trajectories using MC methods. It handles joint CPs over several dynamic obstacles and manages non-Gaussian predictions with minimal approximations.

<!-- chunk {"id": "body-0006", "role": "body", "section": "II-A Contributions", "weight": 1.0} -->

A computationally efficient strategy to find the MC approximation of the joint CP for several hundred samples in parallel, achieving real-time performance.

<!-- chunk {"id": "body-0007", "role": "body", "section": "II-A Contributions", "weight": 1.0} -->

We design a comprehensive cost function for efficient navigation and validate the approach through simulations and real-world experiments with pedestrians. Our method, tested with Gaussian and non-Gaussian models, is compared to a state-of-the-art Scenario-based Model Predictive Control (S-MPC), a risk-aware Frenét planner, and a vanilla MPPI.

<!-- chunk {"id": "body-0008", "role": "body", "section": "III-A Dynamic Obstacle Model", "weight": 1.0} -->

The motion planner uses a model that probabilistically forecasts the behaviour of surrounding agents. In this setting, we model the positions of $N_{o}$ dynamic obstacles as random variables. Specifically, the uncertain position of obstacle $o$ at time step $t$ as ${\mathbf{δ}}_{t}^{o} = {\lbrack x_{t}^{o},y_{t}^{o}\rbrack} \in \Delta$, where $\Delta$ is the probability space capturing the uncertainty in the perception of these obstacles. This uncertainty is characterized by a probability measure $\mathbb{P}$. To capture the inherent multi-modality in obstacle behaviour, we model the uncertainty in their motion using a Mixture-of-Gaussians (MoG) distribution. This approach provides a flexible and expressive representation of uncertainty by combining multiple continuous probability distributions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "III-A Dynamic Obstacle Model", "weight": 1.0} -->

As a result, the prediction model outputs a sequence of state distributions over the prediction horizon for each possible mode, enabling the planner to account for the stochastic nature of obstacle motion.

<!-- chunk {"id": "body-0010", "role": "body", "section": "III-B Probabilistic Collision Avoidance", "weight": 1.0} -->

The problem of planning under uncertainty can be formulated as a chance-constraint collision avoidance problem. Given a cost function $J$, the initial state of the robot ${\mathbf{x}}_{0} = {\mathbf{x}}_{\text{init}}$, and the predicted future states of all obstacles $p_{t,i}^{o}{( \cdot )}$ over a horizon $T$, the objective is to compute optimal control inputs that guide the robot from its initial state to progress along a reference path, while the collision probability with any moving obstacle at each stage $t$ is below an acceptable threshold $\sigma$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "III-C Model Predictive Path Integral Control (MPPI)", "weight": 1.0} -->

Model Predictive Path Integral control (MPPI) is a sampling-based optimization method for solving stochastic optimal control problems.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-C Model Predictive Path Integral Control (MPPI)", "weight": 1.0} -->

where $\mathcal{F}$ represents a nonlinear state-transition function that dictates the evolution of the state $\mathbf{x}$ over discrete time steps $t$. The control input ${\mathbf{v}}_{t}$ follows a Gaussian distribution centered at the commanded input ${\mathbf{u}}_{t}$ with covariance $\Sigma$. To generate potential system trajectories, a set of $K$ perturbed control sequences sequences $V_{k}$ is sampled and rolled-out through the model $\mathcal{F}$, producing $K$ corresponding state trajectories ${X_{k},k} \in {\lbrack 0,{K - 1}\rbrack}$, over a planning horizon of length $T$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-C Model Predictive Path Integral Control (MPPI)", "weight": 1.0} -->

Given the state trajectories $X_{k}$ and a predefined cost function $\mathcal{C}$ to be minimized, the total state-cost $S_{k}$ for each sampled sequence $V_{k}$ is computed by evaluating $S_{k} = {\mathcal{C}{(X_{k})}}$. An importance-sampling weighting scheme is then employed to approximate the optimal control sequence.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-C Model Predictive Path Integral Control (MPPI)", "weight": 1.0} -->

Here, the minimum sampled cost $\rho = {\min_{k}S_{k}}$ is introduced to enhance numerical stability, and $\eta$ is a normalization factor ensuring weights sum to unity.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-C Model Predictive Path Integral Control (MPPI)", "weight": 1.0} -->

Once the optimal control sequence $U^{\ast}$ is obtained, only the first control input ${\mathbf{u}}_{0}^{\ast}$ is applied to the system. The procedure is then repeated at the next time step, where, at the next iteration, a time-shifted $U^{\ast}$ is used as a warm-start.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-D Risk Assessment", "weight": 1.0} -->

To quantify risk in the context of pedestrian-robot interactions, we define a risk metric that assesses the likelihood of collision. Let $\mathcal{Z}$ represent the set of random variables capturing the uncertainty in pedestrian motion in the $x$ and $y$ directions. The risk metric is a function $\zeta:{\mathcal{Z}\mapsto{\mathbb{R}}}$ that maps these random variables to a real value corresponding to the collision probability.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-D Risk Assessment", "weight": 1.0} -->

where the integration domain $\mathcal{R}_{t}^{\circ}$ is defined as a circular region, with radius $r$, centered at the planned robot pose ${\mathbf{q}}_{t}$ at stage $t$ along the planning horizon.

<!-- chunk {"id": "body-0018", "role": "body", "section": "III-D Risk Assessment", "weight": 1.0} -->

When $o > 1$, the probability of colliding with at least one obstacle is given by the joint collision probability.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Proposed Approach", "weight": 1.0} -->

To assess the risk associated with the robot's optimal trajectory in MPPI, and must be evaluated for each sample and each time step in the horizon. For example, with $K = 400$ MPPI samples and a horizon $T = 20$, we must compute the collision probability $8000$ times at each controller iteration. Computing these analytically is not feasible if the controller is to run in real-time. In Section IV-A, we propose a Monte Carlo approximation to estimate the joint collision probability for many trajectories efficiently and in parallel. The cost function used to evaluate MPPI samples is detailed in Section IV-B, and an overview of the algorithm is presented in Section IV-C.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-A Monte Carlo Approximation", "weight": 1.0} -->

We propose an algorithm to compute all $N_{o}$ integral approximations for all $K$ samples efficiently and in parallel, allowing good scalability with the number of dynamic obstacles and samples.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-A Monte Carlo Approximation", "weight": 1.0} -->

Here, $x_{k,t}$ and $y_{k,t}$ denote the $x$ and $y$ robot's position for rollout $k$ at timestep $t$. By taking the minimum and maximum values as bounds and extending the area with the integral radius $r$, we cover the whole area where we need to approximate the integrals at time step $t$.\
Depending on the obstacles' trajectory predictions, we get $N_{o} \times N_{m}$ total number of modes for all obstacles.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-A Monte Carlo Approximation", "weight": 1.0} -->

where $\pir^{2}$ is the area of the collision region and $N_{\mathcal{R}_{k,t}^{\circ}}$ is the number of Monte Carlo samples in the circular region $\mathcal{R}_{k,t}^{\circ}$ acting as a normalization factor. $\mathbb{1}_{\mathcal{R}_{k,t}^{\circ}}$ is an indicator function to consider only MC samples in the circular collision region $\mathcal{R}_{k,t}^{\circ}$. Given that all the coordinates $x_{k,t}$ and $y_{k,t}$ will be fairly close $\forall k$, there will also be significant overlap in the integration regions $\mathcal{R}_{k,t}^{\circ}$. Thus, the computation effort is massively reduced by using our approach of drawing and evaluating the MC samples only once $\forall k$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-A Monte Carlo Approximation", "weight": 1.0} -->

The Standard Error (SE) of $\hat{\mathcal{P}}$, if $\mathcal{P}^{\text{joint}}$ were Gaussian distributed, would scale with $\sqrt{\Sigma_{\mathcal{P}^{\text{joint}}}}/N_{\mathcal{R}_{k,t}^{\circ}}$. In practice, we do not know a priori the number of samples in the collision region, and $\mathcal{P}^{\text{joint}}$ is non-gaussian but, compared to an analytical solution, we have empirically observed that we misclassify the CP to be below the threshold less than 2% of the times.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-B Cost Formulation", "weight": 1.0} -->

A key component of MPPI is the design of the cost function $S_{k}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-B Cost Formulation", "weight": 1.0} -->

where $\mathcal{C}_{\text{tracking}}$ drives the robot towards its goal and penalizes the lateral deviation from the reference path, $\mathcal{C}_{\text{speed}}$ penalizes differences with reference speed, and $\mathcal{C}_{\text{rotation}}$ penalizes angular velocity.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-B Cost Formulation", "weight": 1.0} -->

with $\omega_{\text{soft}}$ and $\omega_{\text{hard}}$ being tunable weights. The first part, $\omega_{\text{soft}}\hat{\mathcal{P}}{({\mathbf{q}}_{k,t})}$, is a linear penalty on any collision probabilities, incentivising the planner to always choose lower risk. The second part, $\omega_{\text{hard}}\mathbb{1}_{\sigma}{({\hat{\mathcal{P}}{({\mathbf{q}}_{k,t})}})}$ is an indicator function returning $1$ when the CP is above a chosen risk threshold $\sigma$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-B Cost Formulation", "weight": 1.0} -->

Every sampled trajectory with a CP above the threshold, assuming that $\omega_{\text{hard}}$ is high enough and that at least a few low-risk trajectories are sampled, will receive close to zero weight in the average in ‣ III Preliminaries ‣ Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations"), essentially being rejected. One advantage is that if, for example, the robot starts planning from a state with CP above the threshold, MPPI still returns a solution in which the CP and the number of time steps with CP above the threshold will be minimised.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-C Algorithm", "weight": 1.0} -->

Algorithm 1 summarizes the proposed approach. Note that operations over $k$ and $j$ are parallelized, while the ones over $t$, i.e. rolling out the trajectories, are performed sequentially.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-C Algorithm", "weight": 1.0} -->

As, $\mathcal{E}_{k}$ are splines fitted to a Halton sequence for improved smoothness, the inverse temperature $\beta$ is updated online, and $U^{\ast}$ is time-shifted to be reused in the next iteration. We also always take one sample to be zero velocity throughout the horizon. This helps MPPI to converge to a braking manoeuvre when all other samples fail.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 1", "weight": 1.0} -->

A key difference between MPPI and MPC is that MPPI's planned trajectory is not meant to be applied in open loop. When symmetries are present, e.g. when a robot faces an obstacle ahead, MPPI's plan might go straight through the obstacle. This is intuitively clear given the weighted average in ‣ III Preliminaries ‣ Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations"). For certain types of systems and cost functions, MPPI can be related to Path Integral Control. Within the Path Integral control framework, because there is an assumption that the actions of the ego-agent are noisy, attempting to drive straight to the obstacle for a while is the optimal action. The symmetry is proven to break at some point. For our planner, this means that while we can reject the samples $k$ with collision probability higher than the threshold $\sigma$, we cannot guarantee that the resulting plan doesn't violate the threshold. Again, this is expected as, in MPPI, only the first input of $U^{\ast}$ is applied, and the rest is only used for warm-starting the next iteration.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Simulation Experiments", "weight": 1.0} -->

This section evaluates the proposed approach in the context of mobile robot navigation in a crowded environment shared with humans. Our algorithm's implementation is built upon previous open-source MPPI solvers. The proposed approach is developed in Python using PyTorch and integrated with the Robot Operating System (ROS). The laptop running the simulations has an Intel^®^ Core^TM^ i7 CPU@2.6GHz and NVIDIA GeForce RTX 2080.

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-A Simulation Setup", "weight": 1.0} -->

The experimental evaluation is conducted in a simulated environment featuring a Clearpath Jackal robot navigating a 6-meter-wide corridor alongside multiple pedestrians. The robot has to follow the corridor's centerline while maintaining a reference velocity of $2$m/s. A visualization with Gaussian predictions is given in Fig. 1. The simulator runs at $20$Hz, while the controllers run at $5$Hz. Pedestrian dynamics are modelled using the Social Forces, implemented via open-source software. In this model, pedestrians avoid one another and the robot. Future pedestrian positions are predicted by the robot's motion planner using a constant velocity assumption. The mismatch between the model used for simulation and prediction is to emulate a real-world scenario where the predictions do not always match the ground-truth trajectory. Pedestrians are modelled with a radius of $0.3$m and spawn on both sides of the corridor, and their goal is to reach the opposing side. The robot dynamics are described by a second-order unicycle model. Simulations are conducted for three scenarios featuring $4$, $8$, and $12$ pedestrians to evaluate the planner's performance under varying crowd density levels.

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-A1 Pedestrians with Gaussian noise", "weight": 1.0} -->

In this setup, we model the uncertainty in pedestrian motion using a unimodal Gaussian distribution with covariance matrix $\mathbf{\Sigma}_{w} = {0.3^{2}{\mathbf{I}}}$. By 'unimodal', it is meant that we predict a single trajectory for each pedestrian.

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-A1 Pedestrians with Gaussian noise", "weight": 1.0} -->

where ${\mathbf{v}} \in {\mathbb{R}}^{2}$ is the velocity that follows the social forces model. The additive noise ${\mathbf{δ}}_{w,t}$ introduces stochastic perturbations, capturing the variability in pedestrian motion.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-A2 Pedestrians with Mixture of Gaussians", "weight": 1.0} -->

In this setup, pedestrian motion is modelled as a Markov Chain, where transitions govern changes in the movement direction. Specifically, a pedestrian follows a horizontal trajectory with probability $p = 0.975$ at each time step while transitioning to a diagonal trajectory with probability $p = 0.025$. This behaviour is further perturbed by Gaussian noise as before.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-A2 Pedestrians with Mixture of Gaussians", "weight": 1.0} -->

where $B$ is a transformation vector that depends on the current state of the Markov Chain and $\mathbf{v}$ is a constant preferred velocity. If the pedestrian is in the horizontal state, $B = \begin{bmatrix}
\end{bmatrix}^{T}$. Conversely, if the pedestrian switches to the diagonal state, $B = \begin{bmatrix}
\end{bmatrix}^{T}$. The uncertainties associated with this motion can be modelled as a Mixture of Gaussians where each state transition in the Markov Chain leads to a separate mode with an associated probability. For a planning horizon of $T = 20$, the pedestrian may switch from horizontal to diagonal movement every 5-time steps, resulting in 4 distinct modes per pedestrian.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-B Comparison to Baselines", "weight": 1.0} -->

We compare DRA-MPPI against three baselines. Baselines are selected on the availability of an open-source implementation and their application to navigation in 2-D dynamic environments.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-B Comparison to Baselines", "weight": 1.0} -->

Stochastic Model Predictive Control (SH-MPC): This baseline uses a scenario-based MPC and formulates the collision avoidance chance constraints over the entire trajectory as a scenario program.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-B Comparison to Baselines", "weight": 1.0} -->

Vanilla MPPI: This baseline assumes deterministic pedestrians' behaviour by considering only the mean predicted trajectories and plans around them.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-B Comparison to Baselines", "weight": 1.0} -->

Frenét Planner: This sampling-based planner generates trajectories in the Frenét coordinate system. The risk metric used is similar to previous work.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-B Comparison to Baselines", "weight": 1.0} -->

All planners have a horizon of $T = 20$ steps, with a discretization step of $0.2$s, resulting in a time horizon of $4.0$s. We set the maximum allowable risk level to $\sigma = 0.05$. DRA-MPPI uses $K = 400$ and $N_{mc} = 20000$ samples.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-B Comparison to Baselines", "weight": 1.0} -->

Task Duration: Measures the time required for the robot to reach the end of the corridor.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-B Comparison to Baselines", "weight": 1.0} -->

Velocity: Determines the average velocity maintained throughout the experiment.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-B Comparison to Baselines", "weight": 1.0} -->

Collision Probability: Quantifies each experiment's maximum joint collision probability (CP). The CP we report is computed a posteriori. Given the remark in section IV-C, the CP is only reported for the current time step instead of over the planned trajectory.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-B Comparison to Baselines", "weight": 1.0} -->

Success Rate (SR): Evaluates the proportion of experiments in which the robot successfully avoids collisions with pedestrians and reaches its goal.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-B Comparison to Baselines", "weight": 1.0} -->

Table I and Fig. 2 and present a quantitative comparison of different planning methods across varying pedestrian densities under uni-modal pedestrian predictions. The results, averaged over $100$ experiments, highlight the trade-offs between task efficiency and safety among the evaluated approaches. Our proposed approach (DRA-MPPI) consistently demonstrates a favourable balance between task duration and safety. While Vanilla MPPI achieves the shortest task duration across all scenarios, it does so at the expense of significantly lower safety due to its lack of risk awareness, particularly as pedestrian density increases. For instance, in the presence of $12$ pedestrians, Vanilla MPPI completes the task in $18.98$s but exhibits the lowest safety rate ($43$%), indicating a high collision frequency. In contrast, DRA-MPPI maintains a competitive task duration ($19.86$s) while achieving a significantly higher safety rate of $98$%, demonstrating its robustness in crowded environments. The Frenét Planner exhibits longer task duration and suffers a notable drop in safety, particularly at higher pedestrian densities ($74\%$ safety at 12 pedestrians).

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-B Comparison to Baselines", "weight": 1.0} -->

This deterioration arises from the planner's design, which does not explicitly optimize for risk minimization. Instead, it evaluates a set of sampled trajectories based on assigned costs and selects the one with the lowest one. However, in dense environments, the trajectory with the minimum cost may still entail substantial risk, as observed in the experimental results.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Remark 2", "weight": 1.0} -->

It is important to stress that, in our simulator, the pedestrians move with Social Forces but are predicted by a constant velocity model, i.e. the predictions are not the ground truth behaviour. This may result in the planner thinking its plan is below the risk threshold while, at the next iteration, it may find itself at a starting pose with a higher-than-allowed collision probability.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Remark 2", "weight": 1.0} -->

SH-MPC strives to track the reference path very closely, often finding itself in riskier positions. SH-MPC relaxes the constraints with slack variables when no feasible solution is found in these riskier situations. When infeasible, SH-MPC switches to a fallback policy (braking). This leads to SH-MPC taking longer to complete the task and often exhibiting collision probabilities higher than the threshold at least a few times per experiment, severely impacting the metrics.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Thanks to its cost, DRA-MPPI always minimizes the CP, even when below the threshold. This makes it strive to avoid riskier situations altogether. Moreover, when DRA-MPPI finds itself in a riskier situation, it will try to return to a state with CP below the threshold in the least amount of steps possible. For these reasons, DRA-MPPI demonstrates good task completion times while providing the highest safety. Moreover, DRA-MPPI and Vanilla MPPI exhibit a lower variance in task duration across experiments, indicating better consistency than SH-MPC and Frenét Planner.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Table II and Fig. 4 and show that the key observations from the uni-modal case also hold in the multi-modal setting. DRA-MPPI outperforms other methods in balancing task efficiency and safety. It achieves the shortest task duration ($19.67$s) while maintaining the highest safety rate ($99\%$), demonstrating its ability to navigate complex, uncertain environments effectively. In contrast, Vanilla MPPI completes the task in a comparable time ($19.71$s) but at the cost of reduced safety ($78\%$), reflecting its lack of risk-awareness. DRA-MPPI also remains close to the maximum allowable risk while ensuring safety, demonstrating its consistency and robustness in complex pedestrian environments.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-C Computation Time", "weight": 1.0} -->

In Tables I and II, we also report the computation time (runtime) for SH-MPC and our approach. DRA-MPPI takes just below $100$ms to compute the control action in the uni-modal four-agents experiment, while SH-MPC is almost twice as fast. Both methods scale quite gracefully over the number of agents with multi-modal predictions. However, it is important to note that SH-MPC is written in C++, while DRA-MPPI is implemented in PyTorch. Recent work shows a reduction of compute time of up to two orders of magnitude when running MPPI in CUDA vs Pytorch, highlighting the potential for these massively parallelizable approaches.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Real Robot Experiments", "weight": 1.0} -->

This section demonstrates the DRA-MPPI for a mobile robot driving among pedestrians in an arena, highlighting the real-time capability of the proposed approach.

<!-- chunk {"id": "body-0054", "role": "body", "section": "VI-A Experimental Setup", "weight": 1.0} -->

The experiment occurs in a large arena where pedestrians walk alongside the robot. The robot and pedestrians' positions are tracked by a motion capture system operating at 20 Hz. Pedestrian positions are filtered through a Kalman filter that also estimates velocities, which the planner uses to produce constant velocity predictions. The pedestrians are assumed to follow an uni-modal Gaussian distribution with a covariance matrix of $\mathbf{\Sigma}_{w} = {0.1^{2}{\mathbf{I}}}$. The robot follows a reference path between two opposite sides of the environment and performs a turn upon reaching each side. The cost function is the same as.

<!-- chunk {"id": "body-0055", "role": "body", "section": "VI-B Results", "weight": 1.0} -->

In this set of experiments, the pedestrians were instructed to walk naturally from one side to the other while interacting with the robot. The experiment was conducted over a duration of $65$ seconds, with snapshots captured at various time instances, as illustrated in Fig.. Throughout the trials, the maximum collision probability observed for the robot was $0.054$, with an average of $0.023$ and a standard deviation of $0.011$. Notably, no collisions were recorded.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We have presented DRA-MPPI, an MPPI-based planner capable of computing, in parallel, at each time step, the joint collision probability among many dynamic obstacles using potentially non-Gaussian predictions. Thanks to its gradient-free nature, we have shown that DRA-MPPI can reject samples with a collision probability above a desired threshold and directly minimise the collision probability.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In simulated experiments, while the pedestrians were predicted with constant velocity, they moved with Social Forces. DRA-MPPI demonstrated the highest robustness to this mismatch by being the safest method among a Scenario-Based MPC approach, a risk-aware Frenét Planner, and a Vanilla MPPI while maintaining high speed and good task completion times. Similar conclusions were drawn in experiments where the pedestrians could randomly switch directions, predicted by a Gaussian Mixture Model, demonstrating efficient planning with non-Gaussian distributions.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Real-robot experiments showcased DRA-MPPI's ease of transfer to the real world and real-time performance. Although we relied on a motion capture system, the pedestrian's state and the map can be retrieved from onboard sensors.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conclusions", "weight": 1.0} -->

While already real-time, in future work our PyTorch implementation could be rewritten in CUDA, dramatically improving computation times. This could also allow for real-time computations of the Monte Carlo approximation of the joint collision probability over the planning horizon, allowing for accurate constraining of the joint collision probability over the entire trajectory.
