## Introduction

Model Predictive Control (MPC) methods, along with other optimal control methods, have become commonplace in several domains for robotics, ranging from simple automotives to even high-degree-of-freedom humanoid robots. The space of MPC-based methods includes an information theoretic nonparametric sampling method, Model Predictive Path Integral Control (MPPI). While the performance of MPPI, both in resultant trajectories and computation time, is stellar, it is often only applied to relatively low-dimensional spaces or is abstracted to a lower dimension to make the problem more feasible. We aspire to realize MPPI methods suitable for real-time robust inference for more complex robotic platforms, such as humanoid robots.

The key concept of MPPI involves information maximization over a projected set of rollout trajectories. From a current state estimate and initial action sequence, MPPI will heavily perturb the action sequence, generating a distribution of trajectories which are then rolled out via state dynamics. MPPI then aims to minimize the Kullback--Leibler (KL) Divergence (a measure of the difference between two distributions) between this rollout distribution and an optimal trajectory distribution, identified by a cost function. Functionally, this equates to performing an information maximization expectation to pick a trajectory equal to a weighted sum of the sampled trajectories. The perturbations, however, are generated from Gaussian distributions, which focuses sampling primarily around the mean, which is not often representative of the true optimal distribution. Particularly for constrained high degree-of-freedom non-linear systems, MPPI becomes susceptible to the curse of dimensionality, requiring exponentially more samples to be effective.

Figure 1: A 2D walker climbing previously unseen stairs via SOPPI. Events are sequenced in ascending numerical order.

For similar problems relating to gradient based optimization Stein Variational Gradient Descent (SVGD), or Stein Variational Inference has become increasingly popular, wherein as part of an optimization step, a kernel is used to force particles to spread out. This kernel ensures a more complete representation of a sampled space and prevents mode collapse, often improving particle efficiency. There are several implementations of SVGD within MPC, highlighted , and a few within MPPI.

However, these representations each have their own issues. For strict MPC implementations, the kernel often loses meaning quickly as it must differentiate particles over several sets of dimensions (the horizon, number of rollouts, and state and/or action dimensions). These high dimensions often make kernel distances much more arbitrary, limiting the effectiveness of the repulsive force in SVGD. Additionally, the Stein component of the gradient descent update must be recursively updated through the cost functions and dynamics over the entire horizon, adding significant computation time.

Further, because SVGD requires gradients, the rollout simulation must be differentiable by some method, which leaves it vulnerable to exploding or vanishing gradients, not to mention the increased memory requirement to compute these gradients. There have been attempts to merge SVGD with MPPI as well, however, for the aforementioned reasons, they perform SVGD on simplified systems, velocity-input models, a small subset of particles, or omit most of the kernel terms, which can minimize the benefits of SVGD.

In this paper, we present Stein-Optimized Path-Integral Inference (SOPPI), an algorithm that combines SVGD with MPPI, operating within the action space of the inference model to improve sampling over baseline MPPI. Compared to existing Stein-based methods, SOPPI performs SVGD updates online during rollouts instead of after them, learning a new action distribution at each time-step. This process better preserves a multi-modal distribution than other methods, and alleviates some concerns regarding exploding/vanishing gradients and loss of kernel meaning.

We evaluate the performance of SOPPI and state-of the-art MPPI/MPC algorithms for a planar cart-pole system study the effects of particle counts and sample efficiency between the algorithms. Our findings from these tests suggest that there is a statistically significant improvement at the 95% level in SOPPI's effectiveness over baseline MPPI and other methods, even when operated at lower particle counts. We also study higher degree-of-freedom (DOF) systems: a block pushing task with a 7-DOF robotic arm and a two-dimensional bipedal locomotion task with a 7-link, 6 DOF walking robot. We explore the effect of uncertainty in both: a gaussian noise added to gradients in the pushing task, and imperfect dynamics gradients in the locomotion task, such as due to estimation error or unforeseen changes in the environment (as shown in Figure 1). As a whole, the experiments demonstrate that SOPPI more effectively covers the action space and generates improved control solutions.

Figure 2: Cart-pole action distribution at different points in the cart-pole’s swing for all control algorithms evaluated in Section IV-A. An image of the cart-pole of each state is shown in the top right. Visualization code provided . All distributions are at similar states (not times) and are for the next planned step in the environment. SOPPI maintains multi-modality where needed, whereas other methods do not.

## Related Work

### II-A MPC and MPPI

Model Predictive Control (MPC) represents a collection of controller types that optimize trajectories via an explicit model. One of the most common MPC methods is under direct optimization, for example, a quadratic programming problem over a system's state space. These methods function on both linear and non-linear systems, although linear models are simpler and more consistent.. MPPI, on the other hand, is a sampling-based approach for stochastic trajectory optimization, as introduced by Williams et. al . MPPI algorithms generate several sample trajectories that are evaluated and weighted to minimize the cost function instead.

### II-B MPPI-based Methods

Several versions of MPPI expand upon the original work. In particular, Tube MPPI runs multiple controller layers to create more trajectory guarantees. Constrained Covariance Steering MPPI builds upon this further, adding covariance tracking to Tube MPPI. Robust MPPI introduces additional safeties and disturbance rejection by importance sampling and augmented state spaces. Reinforcement Learning (RL) MPPI methods attempt to improve sample efficiency though reinforcement learning by training an agent to generate trajectories, instead of baseline MPPI's normal distribution sampling. However, these methods suffer from normal RL drawbacks such as training data, time, and constraints. Unscented MPPI implements an Unscented Transform to help manage uncertainty during rollouts, propagating mean and uncertainty throughout sampling. The aforementioned versions provide a reasonable representation of the space of MPPI methods at a high level, noting that these existing methods often assume the action distribution for sampling is Gaussian or unimodal.

### II-C Variational Inference Methods

On the other end of optimization lie gradient descent methods, in particular, stochastic variational inference. This method operates in the probability space, and shifts a distribution towards and optimal one via gradient-based update rules and minimizing KL-divergence, a measure of the difference between two distributions. Stein Variational Gradient Descent (SVGD) applies similar update rules to variational inference, but also adds kernel terms. These terms encourage particles to avoid mode collapse, increasing particle efficiency and assisting in multi-modal distributions.

Uniting SVGD and MPC is Stein MPC, which treats MPC as a Bayesian inference problem (as many other methods do). This combination allows the application of SVGD instead of traditional gradient descent, which assists in complexity and multi-modality in trajectory selection. However, both represented in this work and the Authors' own attempts, kernels across a high dimension, long horizon problem with a large number of samples quickly lose meaning. The high dimensionality asks the kernel to cover too large a solution space, which reduces the overall coverage of the method. Hence, Stein MPC scales less effectively with respect to solution space coverage if the kernel is applied over the entire problem. Figure 2 shows an example of this effect for the cart-pole experiments in Section IV-A. Stein MPC devolves into an unimodal action distribution to cover either the left or right option for the swing-up trajectories, whereas SOPPI can accurately enforce the true bimodality. This difference suggests that SOPPI is helping mitigate the kernel issue that hinders Stein MPC. SVGD and Stein MPC have also been extended for trajectory optimization and belief propagation for multi-robot coordination.

### II-D Differentiable Dynamics

As with most optimization methods, SVGD requires gradient computations to function. With modern automatic differentiation in tools such as PyTorch, this process is quite simple for analytical dynamics. However, more complex systems require significant modeling, which can create lengthy and complicated dynamic functions. For this reason, many simulation tools such as MuJoCo and Gymnasium are commonplace, however, they are often non-differentiable, making them unusable by default with gradient based methods like SVGD. Differentiable simulation is an active field with many aspiring candidates, but several have key limitations including simplified operations and below real-time runtime. Platforms such as Google's Brax and NVIDIA's Warp and Newton are promising, but introduced computational stability issues during the sampling and resetting requirements of our implementations of SOPPI and other baseline algorithms. For these reasons, this paper follows the common approach of utilizing recurrent neural networks to approximate gradients of the dynamics function when required, but hopes to implement these differentiable simulators in the future.

## Methods

### III-A MPPI

In this paper, we build upon the original derivation of MPPI . We consider the stochastic optimal control problem for the general, discrete-time dynamic system operating in a continuous space

where $x_{t},v_{t}$ represent system state and controls at time $t$ and $F$ denotes the system dynamics. Additionally, $v_{t}$ is assumed to be normally distributed $v_{t} \sim {N{(u_{t},\sigma^{2})}}$ where $u_{t}$ represents a targeted input, and $\sigma^{2}$ represents some process noise. We then aim to optimize some control trajectory $U = {(u_{0},u_{1},\ldots,u_{T - 1})}$ of length $T$ via

where $\mathcal{L}{(x_{t},u_{t})}$ and $\phi{(x_{T})}$ represent running and terminal cost functions respectively, defined as

where $R,Q,Q_{T}$ represent weight matrices for action costs, running state costs, and terminal state costs. We can then define $S{(\tau)}$, a cost-to-go function, as dependent on an entirely trajectory such that

where $\tau$ represents a trajectory in the form

To optimize, we first must generate a set of $K$ sample trajectories to minimize KL-Divergence towards some optimal trajectory. This process is done by sampling a zero-mean Gaussian distribution $\varepsilon$ with some variance $\sigma^{2}$, and adding it to some initial guess of a trajectory $u$. These trajectories are rolled out and have their costs computed. Then, the original MPPI derivation yields that for these sample trajectories, each with its own cost-to-go, we can approximate $u^{\ast}$ via an iterative update for $K$ samples

where $w_{k}$ represents a weight for the $k$-th trajectory with cost $S_{k}$, solved as

where $\beta = {\min_{k \in {\mathbb{K}}}{(S_{k})}}$. Note that there are several MPPI variations that apply filtering to the update step as well, which in some cases may improve system performance.

### III-B SVGD

Similar to MPPI, SVGD attempts to optimize some particle set by minimizing KL-Divergence. For a set of particles ${\{\theta^{i}\}}_{i = 1}^{k}$It follows the iterative update rule of

where $\epsilon$ represents a step size, and $\phi^{\ast}{( \cdot )}$ defines the optimal perturbation to reduce KL-divergence via kernel functions, and can be approximated for a set of $K$ particles via

where $k{( \cdot )}$ represents a valid kernel function. The first term is a scaled gradient log-likelihood of the particle's posterior, which drives the particles towards an optimal state. The second term is a repulsive force that prevents mode collapse and allows greater sample coverage. A full derivation can be found , with a high-level explanation .

### III-C SOPPI

Similar to, the SOPPI Algorithm (Algorithm 1) we propose performs SVGD updates to improve the random samples generated for MPPI. Compared to methods like Stein MPC, SOPPI is designed to optimize the noise added to the distribution per time step, not the entire trajectory itself. This choice results in simpler, shorter computations as gradients do not have to propagate through the entire horizon, reducing the issue of exploding or vanishing gradients. This approach also forces the SVGD kernel to measure distance per time-step, instead of over the entire problem. Whereas Stein MPC's kernel function can become arbitrary, SOPPI's does not, representing multi-modality much better, as depicted in Figure 2. By envisioning the SVGD computation as a series of small sub-problems at each timestep, we can ensure that the kernel operation appropriately prevents mode collapse. Thus, this method can improve sampling efficiency from the standard normal distribution sample.

SOPPI uses the same cost structure as normal implementations of MPPI as seen in Equations 1 and 2. Similar to Miura et al., we apply SVGD updates to the trajectories; however, in our case, we apply SVGD updates online.

To start, SOPPI performs a single step of MPPI (i.e., one timestep in the environment) to gain a set of samples. SVGD is then applied to that step's samples to optimize their distribution towards an optimal cost. Specifically, SOPPI uses the same cost as our base MPPI implementation, Equation 3, however, for all but the last time-step, the terminal cost is undefined. So, the cost function reverts to Equation 1, as only one time step is evaluated.

After these updates, we can derive a cost-likelihood function $\mathcal{L}_{s}$ for SOPPI from the MPPI costs to represent our trajectory's distribution, such that

Thus, the gradient of the log likelihood as listed in Equation 6 is simply the negative scaled gradient of our cost function. Additionally, we use a standard radial-basis (RBF) kernel parameterized by $\sigma$ defined as

From these equations, we compute the SVGD update for SOPPI defined in 6, and apply it to the sampled action particles immediately for an online update. Then, we re-compute the rollout with the new actions, continuing the MPPI process as normal. This process is repeated throughout some horizon, after which the weighting defined in equations 4 and 5 are used to select an optimal trajectory. This process effectively creates sequential sub-problems with a lower search dimension than if the entire trajectory were searched at once. The entire algorithm is depicted in Algorithm 1.

Data: K: Number of samples
M: Number of SVGD Updates
Ui n i t: Initial control sequence

while task not completed do
Ssk ← ℒ (xtk + 1,vtk);
${{\hat{\phi}}^{\ast}{(v)}}\leftarrow{\frac{1}{K}{\sum_{j = 1}^{K}\left\lbrack {{- {k{(v^{j},v)}{\nabla_{v_{t}^{k}}S_{s}^{k}}}} + {{\nabla_{v^{j}}k}{(v^{j},v)}}} \right\rbrack}}$;

$w_{k}\leftarrow\frac{\exp{({- {\frac{1}{\lambda}{({S_{k} - \beta})}}})}}{\sum_{j = 1}^{k}{\exp{({- {\frac{1}{\lambda}{({S_{j} - \beta})}}})}}}$;
$u^{\ast}\leftarrow{u + {\sum_{k = 1}^{K}{w_{k}\varepsilon^{k}}}}$;
$U_{init}\leftarrow\begin{bmatrix}

## Experiments

We conducted a series of simulation experiments and, similar to other works, compare SOPPI vs base MPPI, but also compare against SVG-MPPI and stein MPC as they are similar in formulation. We evaluate multiple tasks: a single DOF cart-pole upswing, 7-DOF robot arm box pusher, and a planar 6-DOF bipedal walker. All simulations were conducted through Pytorch and analytical dynamics or the Gymnasium wrap of MuJoCo with a trained recurrent neural network. All tests were performed with a i7-13700K CPU, accelerated by a Nvidia A6000 GPU.

### IV-A Cart Pole

For the cart-pole swing-up task, we used an analytical dynamics model with an upright pole angle of $\theta = 0$, and the starting, downward pole angle as $\theta = \pi$. The cart's lateral ($x$) position starts and ends at $x = 0$. Visualizations of the cart-pole system are depicted in Figure 2.

Figure 3: Cart-Pole response for a horizon (H) of 80 steps (1.6 seconds) and 500 and 1,000 particles (K).

P-value (SOPPI K=500 better than MPPI K=1,000)

P-value (SOPPI K=500 better than Stein MPC K=1,000)

P-value (SOPPI K=500 better than SVG-MPPI K=1,000)

Note: ts, x and ts, θ represent settling times of x and θ, followed by criteria: a meter range for x or percentage of the step range (π) for θ.
† Two out of five trials did not converge;

TABLE I: Cart Inverted Pendulum System Response for a Horizon (H) of 80 steps or 1.6 seconds, and various particle counts (K). Statistically significant (95%) results are bolded.

We performed a range of tests on all four algorithms focusing on varying sample count and horizon timesteps. From these tests, we present results at a horizon of 80 timesteps or 1.6 seconds, and at 500 and 1000 particles to demonstrate differences in particle efficiency between the algorithms. Additionally, for the gradient based algorithms, we present results with a learning rate of $0.05$ over $100$ iterations. All remaining hyper-parameters and costs were identical across tests. Numerical results from these tests can be noted in Table I depicting settling times $t_{s}$ for both $x$ and $\theta$ for multiple criteria (for example, 0.25 m on $x$ or $5\%$ of the $\theta$ range), and Figure 3 depicts visual results. Additionally, Table I contains statistical results from a Welch's t-test, indicating statistical significance between the trials.

From the results in Table I, we note that SOPPI performs statistically better with respect to the cart pole's state mean squared errors at identical particle counts. In conjunction with the visual convergence to steady state in 3, this metric indicates an improved overall error tracking by SOPPI relative to the compared algorithms. Figure 2 provides some insight as to why, highlighting how SOPPI maintains a multi-modal action distribution which either maintains a peak near optimization methods (e.g., a peak near Stein MPC for all but steady state), or splits its distribution across it, avoiding a suboptimal average. The initial and steady state distributions highlight this best. An action to either side to maintain balance is equally valid to swing up or maintain equilibrium, but a 0 action would likely result in a fall.

Similar trends occur in the angle settling times of 5% and 10%, where SOPPI converges to a wide bound much faster than other algorithms. This convergence is also readily apparent in Figure 3. However, SOPPI does not perform as well on the tight 2% angle settling time. We attribute this behavior to the unstable equilibrium of the cart-pole system at the upright position. Due to the instability, the bimodal distribution in the steady state highlighted in Figure 2 promotes a small degree of chattering, hindering convergence to a tighter bound.

For the x position settling time, SOPPI converges faster than all but SVG-MPPI in the 500 particle case, although this faster convergence is only significant compared to MPPI. In the 1,000 particle case, SVG-MPPI actually converges faster on the x position, but at the trade off of losing to SOPPI on angle convergence and the overall x tracking error. We attribute this discrepancy to the single-modal nature of SVG-MPPI. The action distribution as depicted in Figure 2, particularly the second swing, shows a propensity of SVG-MPPI to favor either positive or negative actions more heavily, which equates to heavier swings of the cart-pole. These swings allow the system to reach steady state on x faster, but balance the angle of the pole slower. The wider variation in the x position and larger number of continual swings of the angle for both Stein MPC and SVG-MPPI in Figure 3 support this claim as well.

Lastly, these trends hold when comparing the 500 particle count version of SOPPI vs the other algorithms' 1,000 count versions. Thus, we conclude that in the cart-pole case, SOPPI can increase particle efficiency compared to other algorithms. This claim is further reinforced by the action distributions depicted in Figure 2, wherein the multi-modal nature of SOPPI's generated actions, compared to other algorithms, covers a wider space with each distribution of particles.

### IV-B Arm Pushing Task

To increase the complexity of the system over the cart-pole, we elected to test the algorithm on a simulated planar pushing task on a block with a Franka Panda arm based on Berenson et al.. Since this system is the most stable of those tested, we elected to run trials with noise injected into the gradients as well, to highlight the capabilities of each algorithm to handle uncertainty.

To simplify the dynamics at runtime while maintaining gradients, we trained a recurrent neural network to approximate the next state from a MuJoCo simulation, given a current state and action. In this formulation, states represent the block's pose $\mathbf{x} = \begin{bmatrix}
\end{bmatrix}^{\top} \in {\text{SE}{}}$ and actions $\mathbf{u} = \begin{bmatrix}
\end{bmatrix}^{\top} \in {\mathbb{R}}^{3}$ are represented by $p$ corresponding to the lower edge pushing location of the block, $\phi$ corresponding to the pushing angle, and $\ell$ corresponding to the pushing length as a fraction of the maximum allowed length (0.1 m in this case). In all tests, the arm was tasked with pushing the block from the pose $\lbrack 0.4,0,\frac{\pi}{5}\rbrack$ to $\lbrack 0.8,0,0\rbrack$.

Since this task was inherently more stable than the cart-pole task, we elected for a shorter horizon and higher end sample count, 10 time steps (0.2 seconds) and 1000 samples, for both MPPI and SOPPI. All other hyper-parameters and cost functions were identical between trials for all 4 algorithms. Table II and Figure 5 depict numeric results, and Figure 4 depicts visuals of the state transitions.

Figure 4: Pushing task visualization of the Franka arm pushing a block (white) to a target pose (green). Events are sequenced in ascending numerical order.

Figure 5: Median trial pushing distance error compared between algorithms

Mean End Distance Error (mm)
Standard Deviation of End Distance (mm)

Noisy Stein MPC

Noisy SOPPI (ours)

TABLE II: Steady State Distance Errors for the pushing task

Overall, from Table II we note that the mean steady-state response errors on the pushing direction are slightly better with SOPPI than MPPI and much better with SOPPI than any other method, with or without noise. Errors in the lateral direction and desired angle are quite similar across all systems, with the exception of a larger lateral error in MPPI. From Figure 5, SOPPI reaches steady state slightly faster than MPPI, but compared to other methods, SOPPI and MPPI do not overshoot. Given the reach of the arm, an overshoot is unrecoverable, as the arm physically cannot reach the other side of the block. Hence, SOPPI and MPPI act more cautiously than the other algorithms, especially in the case of added noise. Stein MPC and SVG-MPPI both overshoot significantly with noise added to the gradients, whereas SOPPI has little change in performance. Combined with the cart-pole results, we can empirically note that SOPPI better handles uncertain gradients than some other direct optimization methods. Simulations often simplify dynamics, and thus their gradients, compared to the real-world, so successful performance under uncertainty is quite important for operation on real systems. Experiments for the 2D walker further highlight successful operation under gradient noise.

### IV-C 2D Walker Task

Lastly, we implement the same algorithms on the Walker2D gymnasium environment, which is commonly used in the reinforcement-learning community. However, due to the unstable dynamics of the system's 6 joints, we implement a cost structure similar to, wherein we apply a reference input trajectory around some known gait. Since this system is well studied in the RL community, we trained a Proximal Policy Optimization (PPO) model to generate reference gait, from the Stable Baselines3 package. Additionally, our cost structure was modified from 1 to

where $u_{ref}$ was computed by the PPO model, rolling out from the current state with its own generated actions. To prevent collapsing the distribution on the reference input, we ensure that $Q$ has a much higher magnitude than $R$ so that states weight the cost function more than the inputs. During sampling, we also modified the initial input for the last time step to be the output of the PPO model at the next to last time step's states. So the last line of Algorithm 1 becomes

For gradients, we trained another recurrent neural network to approximate the dynamics of the system for a single step (the duration of gradients required). However, we used MuJoCo simulations for rollouts, as given the chaotic nature of the walker robot, we found MuJoco to be more accurate over a long-horizon. This issue could be reduced with more training and data, but was not required for SOPPI to function. Regardless, there will always be some degree of error in a learned dynamics system, and gradients usually explode or vanish over a long enough horizon, so these issues will exist in some capacity. Managing these simulated gradients is an active field of research, particularly with differentiable simulation. SOPPI is one such approach to apply control in spite of these issues, as evidenced by its performance.

Lastly, we tuned our cost matrix, $Q$ to prioritize maximizing the height of the walker's torso, and added forward kinematic costs which incentivized the robot's feet to be further apart. Both modifications led to more stable, continued steps. We conducted eight trials for each algorithm with all hyper-parameters and cost functions equal. We elected for a 50 time-step horizon and 1,000 samples for each case. The results of these trials are depicted in Table II, with visuals of the system walking depicted in Figure 6. We consider the metric of "walking time" to denote the stable duration, and consider the end of walking time as the last peak of torso height before the torso falls below 1 meter.

Figure 6: Sample 2D walker gait from initial position. Events are sequenced in ascending numerical order.

Mean Walking Time
Median Walking Time

TABLE III: Walker Task Walking Time. Longer times indicate further distance traveled upright

In our experiments, we observe that on average, SOPPI trials were able to walk longer than trials of the other algorithms tested, although not indefinitely. Typically, a trial failed (denoted by the walker falling to the ground) by either a slip or stall in momentum, which we believe to be caused by failure to sample a valid trajectory. Thus, we believe that with the improved sampling of SOPPI, the walker is overall more stable and better able to maintain its upright position.

The Stein MPC and SVG-MPPI algorithms however, are not at all successful. They try to optimize over an entire horizon (x in this case), but given the chaotic nature of the system and accumulated errors on the learned dynamics, cannot optimize successfully. However, in SOPPI's case, the single step optimization improves upon MPPI where the other methods could not, leading to much better results.

A one-tailed Welch's t-test on the walking times of the different algorithms compared to SOPPI yields p-values of 0.023, 0.0016, and 0.0047, for MPPI, Stein MPC, and SVG-MPPI respectively, indicating a significant performance improvements at the 95% level for SOPPI. We do, however, notice a large variance in the results for all algorithms, which we expect is due to the chaotic, unstable nature of the system. Similarly to how neural networks were only used for gradients when needed for stability, we expect that the sampling requirements for perfect stability are higher than conducted in our trials. In addition, many real-world systems have more rigorous reference gaits than our learned one (which contains a "skipping" motion as seen in image 3 of Figure 6). For this reason, we expect that implementing SOPPI on systems designed for the real-world (whether in simulation or not), which have the benefit of tested, stable gaits, would reduce this variance. Instead, especially with any remaining noise, SOPPI would lead to more optimized gaits, similar to the other systems presented in this paper.

### IV-C1 Stairs as an unknown disturbance

Lastly, we tested the algorithms on climbing short stairs, an environment which was not included in any reference trajectory or any trained dynamics. SOPPI was the only algorithm successfully able to perform in this environment, and a sample climbing gait is depicted in Figure 1. These stair climbing results further demonstrate SOPPI's ability to optimize in unstable environments where algorithms cannot.

## Conclusion and Future Works

In this paper, we presented SOPPI, a novel method that interweaves SVGD updates into MPPI, combining the benefits of SVGD's explicit optimization with reduced particles and MPPI's general computational simplicity. We performed a range of experiments including a cart-pole swing up, a block pushing task, and a two dimensional walking task, all demonstrating SOPPI's efficacy compared to MPPI, Stein MPC, and SVG-MPPI. Specifically, the SVGD updates within SOPPI optimized the noise typical in MPPI applications to generate an improved performance, even in some cases where SOPPI operated at lower particle counts. SOPPI was also able to handle environments with noise and instability better than other state of the algorithms, and even an entirely out of distribution environment to climb stairs. With these results, we demonstrated that SOPPI effectively increases the algorithm's performance and/or particle efficiency over other methods, paving the way for future works with higher-dimension systems.

In the future, we intend to expand this algorithm threefold. First, we intend to expand this work to new developments in differentiable simulators, including NVIDIA Warp, Newton and Brax which would simplify our requirements for differentiable dynamics. We also aim to explore further the multi-modal action search, identifying modalities explicitly, rather than implicitly, to further improve sample efficiency. Lastly, we aim to implement this work on more systems, specifically, higher dimensional walkers and real-world systems, such as the Agility Robotics Digit and Unitree G1. In cases such as these, we additionally hope to implement multiple gaits and demonstrate abilities to switch between them, for example, a standing and walking gait, which would hold itself well to real-world applications.
