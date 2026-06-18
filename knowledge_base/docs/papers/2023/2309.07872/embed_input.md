A Unified Perspective on Multiple Shooting in Differential Dynamic Programming

Topics include Differential dynamic programming, Multiple shooting, Trajectory optimization, Optimal control.

Provides a unified theoretical framework for multiple-shooting DDP variants, clarifying relationships between existing methods and deriving conditions under which they share convergence guarantees.

Differential Dynamic Programming (DDP) is an efficient computational tool for solving nonlinear optimal control problems. It was originally designed as a single shooting method and thus is sensitive to the initial guess supplied. This work considers the extension of DDP to multiple shooting (MS), improving its robustness to initial guesses. A novel derivation is proposed that accounts for the defect between shooting segments during the DDP backward pass, while still maintaining quadratic convergence locally. The derivation enables unifying multiple previous MS algorithms, and opens the door to many smaller algorithmic improvements. A penalty method is introduced to strategically control the step size, further improving the convergence performance. An adaptive merit function and a more reliable acceptance condition are employed for globalization. The effects of these improvements are benchmarked for trajectory optimization with a quadrotor, an acrobot, and a manipulator. MS-DDP is also demonstrated for use in Model Predictive Control (MPC) for dynamic jumping with a quadruped robot, showing its benefits over a single shooting approach.

## Introduction

Model Predictive Control (MPC) is a powerful technique for controlling complex systems and has been widely used for many robotic systems, including quadrotors, quadruped robots, and humanoid robots. MPC needs to efficiently and reliably solve a sequence of finite horizon optimal control problems (OCPs) of the form

where $T$ is the prediction horizon, $\mathbf{x}$ the state variable, $\mathbf{u}$ the control variable, $\ell_{c}$ the running cost, $\phi$ the terminal cost, and $\mathbf{f}_{c}$ the dynamics function. The problem is an infinite-dimensional optimization problem, as it is in continuous time, and the dynamics are highly nonlinear for many robotics systems. Therefore, an analytical solution, in general, does not exist, and numerical methods are often employed. One commonly used class of approaches are direct methods.

Differential Dynamic Programming (DDP) is a single shooting method to solve the OCP, and is shown to have a local quadratic convergence rate. It naturally exploits the temporal structure of the transcribed problem by successively solving a sequence of sub-problems, resulting in linear computational cost with horizon length $T$. These sub-problems originate from locally solving Bellman's equation, which additionally gives a local feedback policy without additional computation cost. These properties make DDP exceptionally well suited for MPC with a long prediction horizon.

Multiple shooting (Fig. 2) alleviates the sensitivity problem of single shooting by introducing intermediate state variables (also known as shooting states). The shooting states divide a trajectory into several sub-intervals, known as shooting segments. Numerical integration is performed separately on each segment using the shooting state as an initial condition. Continuity constraints that link the shooting state to a previous segment need to be satisfied at convergence, so that the resulting trajectory is dynamically feasible.

## Discussion on The Unified Perspective

The search direction computation in Section III and the globalization method for step acceptance in Section IV comprise one iteration of the MS-DDP algorithm. A brief summary of the overall MS-DDP framework is given below

Give the nominal trajectory $(\overline{\mathbf{x}},\overline{\mathbf{u}})$, optimization horizon $N$, and number of shooting segments $M$.
