A Unified Perspective on Multiple Shooting in Differential Dynamic Programming

Topics include Differential dynamic programming, Multiple shooting, Trajectory optimization, Optimal control.

Provides a unified theoretical framework for multiple-shooting DDP variants, clarifying relationships between existing methods and deriving conditions under which they share convergence guarantees.

Differential Dynamic Programming (DDP) is an efficient computational tool for solving nonlinear optimal control problems. It was originally designed as a single shooting method and thus is sensitive to the initial guess supplied. This work considers the extension of DDP to multiple shooting (MS), improving its robustness to initial guesses. A novel derivation is proposed that accounts for the defect between shooting segments during the DDP backward pass, while still maintaining quadratic convergence locally. The derivation enables unifying multiple previous MS algorithms, and opens the door to many smaller algorithmic improvements. A penalty method is introduced to strategically control the step size, further improving the convergence performance. An adaptive merit function and a more reliable acceptance condition are employed for globalization. The effects of these improvements are benchmarked for trajectory optimization with a quadrotor, an acrobot, and a manipulator. MS-DDP is also demonstrated for use in Model Predictive Control (MPC) for dynamic jumping with a quadruped robot, showing its benefits over a single shooting approach.

## Introduction

Model Predictive Control (MPC) is a powerful technique for controlling complex systems and has been widely used for many robotic systems, including quadrotors, quadruped robots, and humanoid robots. MPC needs to efficiently and reliably solve a sequence of finite horizon optimal control problems (OCPs) of the form

where $T$ is the prediction horizon, $\mathbf{x}$ the state variable, $\mathbf{u}$ the control variable, $\ell_{c}$ the running cost, $\phi$ the terminal cost, and $\mathbf{f}_{c}$ the dynamics function. The problem is an infinite-dimensional optimization problem, as it is in continuous time, and the dynamics are highly nonlinear for many robotics systems. Therefore, an analytical solution, in general, does not exist, and numerical methods are often employed. One commonly used class of approaches are direct methods....

## Conclusions

This work presents a unified framework for extending DDP to a multiple-shooting OCP solver. The proposed framework provides multiple configurations and several enhancements, allowing for easy comparison with and between previous algorithms. The novel derivation of the defect-aware DDP backward pass enables using second-order dynamics, and is shown to have local quadratic convergence when used with the nonlinear roll-out method. We show that the expected cost change model is important for algorithm convergence, and propose an exact model that further improves the performance of a state-of-the-art solver....

where $0 < \gamma < 1$ is a tuning parameter, $\operatorname{EC}{(\alpha)}$ is the expected cost change, and

where $\mathbf{x}_{0}^{\prime} = {\overline{\mathbf{x}}}_{0}$, $\alpha \in {(0,1\rbrack}$ is the step size, which is used in backtracking line search for global convergence, and $\delta\mathbf{u}_{k}{(\alpha)}$ is the scaled search direction. The main difference between the three roll-out methods is in the state update.

The MS-DDP framework is benchmarked on three problems for numerical analysis. Each problem is associated with moving a robotic system from an initial state to a terminal state. A semi-implicit Euler method is used for integration, with the integration time step 0.02 s. Quadratic cost functions are used for all problems. We use the $L_{2}$-norm to measure the total defect....
