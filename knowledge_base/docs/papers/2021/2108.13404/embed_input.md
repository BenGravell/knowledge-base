SINDy with Control: A Tutorial

Topics include SINDy, System identification, Control, Nonlinear dynamics, Data-driven methods.

Tutorial demonstrating how to extend SINDy to systems with exogenous control inputs (SINDy-C), covering library selection, ensemble methods for robustness, and applications to controlled nonlinear dynamical systems.

Many dynamical systems of interest are nonlinear, with examples in turbulence, epidemiology, neuroscience, and finance, making them difficult to control using linear approaches. Model predictive control (MPC) is a powerful model-based optimization technique that enables the control of such nonlinear systems with constraints. However, modern systems often lack computationally tractable models, motivating the use of system identification techniques to learn accurate and efficient models for real-time control. In this tutorial article, we review emerging data-driven methods for model discovery and how they are used for nonlinear MPC. In particular, we focus on the sparse identification of nonlinear dynamics (SINDy) algorithm and show how it may be used with MPC on an infectious disease control example. We compare the performance against MPC based on a linear dynamic mode decomposition (DMD) model. Code is provided to run the tutorial examples and may be modified to extend this data-driven control framework to arbitrary nonlinear systems.

## INTRODUCTION

Modern systems of interest in turbulence, epidemiology, neuroscience, and finance are high-dimensional and nonlinear, and exhibit multiscale phenomena in both space and time. Controlling these nonlinear systems remains an important challenge, as traditional linear control approaches are often insufficient. There are several control approaches for nonlinear systems, including model predictive control and reinforcement learning....

Model predictive control (MPC) is a particularly compelling approach that enables control of strongly nonlinear systems with constraints. However, MPC relies on efficient models that accurately represent the dynamics of the system, and these models have remained elusive for many disciplines that lack known governing equations. Generally, MPC also suffers from the curse of dimensionality, requiring large computational effort and limiting the applicability to low-dimensional problems, often based on locally linear models....

In this tutorial, we explored the use of data-driven model discovery techniques to identify computationally tractable and accurate models of nonlinear systems for model-based control. In particular, we demonstrated how SINDy with control can be combined with MPC for infectious disease control. We have included example codes throughout to help clarify these concepts. Our goal in providing open-source code for this tutorial is to encourage the reader to test the assumptions, explore modifications, and adapt these algorithms to their own nonlinear control problems.

We have made certain assumptions to simplify the SINDy modeling and control procedure. We encourage users to implement their own modeling assumptions: changing the numerical differentiation method (assuming we can not measure the derivatives), changing the library functions, the sparse regression algorithm, or investigating different values for the sparsity-promoting hyperparameter $\lambda$ (e.g. using information criteria such as AIC or BIC ). We also encourage the user to investigate different forcing functions and the amount of training data needed to identify models....

subject to the discrete-time dynamics and constraints. The cost function $J$ penalizes deviations of the predicted state $\hat{\mathbf{x}}$ from the reference trajectory $\mathbf{r}$, the control expenditure $\mathbf{u}$, and the rate of change of the control...
