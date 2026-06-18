Dynamic Tube MPC for Nonlinear Systems

Topics include Model predictive control, Predictive control, Robustness, Uncertainty, Computational complexity, Online algorithms, Offline algorithms, Optimization, Control, DTMPC, Robust model predictive control, RMPC, Nonlinear systems, Obstacle avoidance.

Modeling error or external disturbances can severely degrade the performance of Model Predictive Control (MPC) in real-world scenarios. Robust MPC (RMPC) addresses this limitation by optimizing over feedback policies but at the expense of increased computational complexity. Tube MPC is an approximate solution strategy in which a robust controller, designed offline, keeps the system in an invariant tube around a desired nominal trajectory, generated online. Naturally, this decomposition is suboptimal, especially for systems with changing objectives or operating conditions. In addition, many tube MPC approaches are unable to capture state-dependent uncertainty due to the complexity of calculating invariant tubes, resulting in overly-conservative approximations. This work presents the Dynamic Tube MPC (DTMPC) framework for nonlinear systems where both the tube geometry and open-loop trajectory are optimized simultaneously....

## INTRODUCTION

Model predictive control (MPC) has become a core control strategy because of its natural ability to handle constraints and balance competing objectives. Heavy reliance on a model though makes MPC susceptible to modeling error and external disturbances, often leading to poor performance or instability. Robust MPC (RMPC) addresses this limitation (at the expense of additional computational complexity) by optimizing over control policies instead of open-loop control actions. Tube MPC is a tractable alternative that decomposes RMPC into an offline robust controller design and online open-loop MPC problem....

Tube MPC for nonlinear systems has been an active area of research. For example, hierarchical MPC, reachability theory, sliding mode control, sum-of-square optimization, and Control Contraction Metrics have all been recently used in nonlinear tube MPC. These approaches try to maximize robustness by minimizing tube size given control constraints and bounds on uncertainty. However, minimizing tube size typically results in a high-bandwidth controller that responds aggressively to measurement noise or external disturbances....

## CONCLUSIONS

This work presented the Dynamic Tube MPC (DTMPC) algorithm that addresses a number of shortcomings of existing nonlinear tube MPC algorithms. First, the open-loop MPC optimization is augmented with the tube geometry dynamics enabling the trajectory and tube to be optimized simultaneously. Second, DTMPC is able to utilize state-dependent uncertainty to reduce conservativeness and improve optimization feasibility. And third, the tube geometry and error dynamics can be combined to further reduce conservativeness. All three of these properties were made possible by leveraging the simplicity and robustness of boundary layer sliding control....

Many physical systems posses these type of constrains so the above assumption is not overly restrictive.

where again the division is element-wise. Alternatively, Equation 10 can be written as

guarantees, for all realization of the uncertainty, the true constraint is satisfied.

The primary contribution of this work is a tube MPC framework for nonlinear systems that simultaneously optimizes tube geometry and open-loop reference trajectories in the presence of uncertainty....
