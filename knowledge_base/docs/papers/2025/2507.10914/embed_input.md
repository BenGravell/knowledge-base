Fast Non-Episodic Adaptive Tuning of Robot Controllers with Online Policy Optimization

Topics include Reinforcement learning, Robotics, Aerial robotics, Online algorithms, Optimization, Control, Learning.

We study online algorithms to tune the parameters of a robot controller in a setting where the dynamics, policy class, and optimality objective are all time-varying. The system follows a single trajectory without episodes or state resets, and the time-varying information is not known in advance. Focusing on nonlinear geometric quadrotor controllers as a test case, we propose a practical implementation of a single-trajectory model-based online policy optimization algorithm, M-GAPS,along with reparameterizations of the quadrotor state space and policy class to improve the optimization landscape. In hardware experiments,we compare to model-based and model-free baselines that impose artificial episodes. We show that M-GAPS finds near-optimal parameters more quickly, especially when the episode length is not favorable. We also show that M-GAPS rapidly adapts to heavy unmodeled wind and payload disturbances, and achieves similar strong improvement on a 1:6-scale Ackermann-steered car.

## Introduction

We study the problem of optimizing a parameterized non-linear robot control policy in an online setting. A deployed robot may face unpredictable changes in both environment and task, and must adapt to them immediately. Therefore, we consider a protocol where the dynamics, policy class, and cost functions are all time-varying and revealed online: the optimization algorithm has no knowledge of how they will vary in the future. The algorithm is evaluated on a single trajectory without episodes or state resets. As a case study, we focus on nonlinear trajectory tracking control for quadrotors.

Policy optimization has been widely studied in the control and machine learning communities from varying perspectives.

Can be applied to general nonlinear dynamics and costs.

Contributions. We conduct real-hardware experiments comparing three algorithms that extend the online gradient descent principle to online policy optimization: a model-free episodic method OPRF, a model-based episodic method DiffTune, and a model-based non-episodic method M-GAPS. We propose reparameterizations of the quadrotor state space and policy class to improve the optimization landscape for all methods. We study three scenarios: 1) initialization with suboptimal parameters, 2) a strong time-varying wind, and 3) a heavy unmodeled payload. In setting 1, we find that M-GAPS performs best overall.

## Conclusion

We experimentally evaluated algorithms that apply the principle of online gradient descent to the online policy optimization problem for nonlinear robot controllers. For tuning a geometric quadrotor controller for aggressive flight from a suboptimal initialization, the non-episodic model-based M-GAPS performed best, finding a near-optimal policy in about $15\ \sec$. The model-based episodic DiffTune performed nearly as well when its episode length was ideal, but degraded with other episode lengths. The model-free episodic OPRF further lagged the model-based methods.

## Limitations

The contractiveness required for the local regret guarantee of M-GAPS can be difficult to verify, and does not rule out the possibility of bad local minima. Similar to other applications of gradient-based nonconvex optimization, one must do empirical validation (like this work) before deploying M-GAPS in complex real-world robotic systems.
