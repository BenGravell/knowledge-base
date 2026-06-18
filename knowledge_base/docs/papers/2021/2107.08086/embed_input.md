An Information-state Based Approach to the Optimal Output Feedback Control of Nonlinear Systems

Topics include Optimal control, Trajectory optimization, Uncertainty, Online algorithms, Generalization, Optimization, Control, ARMA, Nonlinear systems, Linear quadratic regulator.

This paper develops a data-based approach to the closed-loop output feedback control of nonlinear dynamical systems with a partial nonlinear observation model. We propose an information state based approach to rigorously transform the partially observed problem into a fully observed problem where the information state consists of the past several observations and control inputs. We further show the equivalence of the transformed and the initial partially observed optimal control problems and provide the conditions to solve for the deterministic optimal solution. We develop a data based generalization of the iterative Linear Quadratic Regulator (iLQR) to partially observed systems using a local linear time varying model of the information state dynamics approximated by an Autoregressive moving average (ARMA) model, that is generated using only the input-output data. This open-loop trajectory optimization solution is then used to design a local feedback control law, and the composite law then provides an optimum solution to the partially observed feedback design problem....

## Introduction

The optimal stochastic control of a nonlinear dynamical system is computationally intractable for complex high-order systems due to the 'curse of dimensionality' associated with solving dynamic programming. The problem becomes more challenging when the model of the system is unknown and even more formidable when only some of the states are available for measurement, i.e., under partial state observation. However, in practice, most problems tend to be partially observed and subject to noise. In this work, we propose a data-based approach for learning to optimally control complex partially observed stochastic nonlinear dynamical systems....

Figure 1: Note the high dimensional, complex, and partially observed nature of the robotic control problems considered in this paper.

## Conclusions

The paper presented a decoupled data-based approach to control complex robotic systems with partial state observations. The paper shows that the exact linear state-space model can be matched by the $q$^th^-order ARMA model generated using the input-output data. The ARMA model then can be used to write an LTV system in the information state which allows designing the optimal nominal trajectory using iLQR and also allows for designing the closed-loop feedback law using only the partially-observed states. Empirical results are also shown for complex robotic systems under motion as well as sensing uncertainty....

### Remark III.1

where the blank part of the matrix is filled so that the complete matrix is symmetric. $H_{i}$ and $R_{i}$ are input-output correlation parameters and output-output correlation parameters defined for sufficiently large number $N$ as:

For the case of noiseless measurements, a simplified LQR design can be used for the closed-loop feedback control with $u_{t} = {{\overline{u}}_{t}^{\ast} - {K_{t}\deltaZ_{t}}}$ where $K_{t}$ is calculated using eqs. 16 Algorithm ‣ Partially-Observed Decoupled Data-based Control (POD2C) for Complex Robotic Systems") and 17 Algorithm ‣ Partially-Observed Decoupled Data-based Control (POD2C) for Complex Robotic Systems") only.

The proposed approach then generalizes the iLQR algorithm to partially observed problems by iteratively generating linear time-varying state-space models, represented in the information state, to obtain the optimized nominal information space trajectory....
