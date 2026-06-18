DiffLoop: Tuning PID Controllers by Differentiating through the Feedback Loop

Topics include Convex optimization, Gradient descent, Optimization, Control, DiffLoop, PID controller, Feedback loop.

Since most industrial control applications use PID controllers, PID tuning and anti-windup measures are significant problems. This paper investigates tuning the feedback gains of a PID controller via back-calculation and automatic differentiation tools. In particular, we episodically use a cost function to generate gradients and perform gradient descent to improve controller performance. We provide a theoretical framework for analyzing this non-convex optimization and establish a relationship between back-calculation and disturbance feedback policies. We include numerical experiments on linear systems with actuator saturation to show the efficacy of this approach.

## Introduction

PID controllers are the most popular form of feedback control in industrial applications. In general, the PID gains need to be tuned to obtain good performance. In addition, potential actuator saturation must be taken into account, since saturation can induce integrator wind-up, resulting in unexpected transients during operation. To address the above issues, PID tuning can be performed using classical control based on a model of the plant devised either from prior knowledge or system identification. Model-free PID tuning has also been explored by performing selective experiments to tune the gains gradually....

We explore using the back-calculation method together with a non-convex optimization approach based on differentiating through the system model, actuator, and the feedback loop to tune the feedback gains. This approach is inspired by recent work on differentiable physics engines/models. In particular, we episodically tune the controller parameters by simulating with the current parameters, evaluating the cost, and performing gradient descent on the cost objective. By propagating the gradients over time for the entire simulation, we capture the controller parameters' long-term dependencies on the system's dynamics....

We outline a PID tuning approach for linear systems with input saturation. This approach differentiates through the model and around the feedback loop to tune the controller parameters. The numerical experiments demonstrate the efficacy of this approach. We also propose a theoretical framework to analyze the convergence properties for this optimization. However, a convergence proof is beyond the scope of this work. We noted that the framework shows the equivalence of the back-calculation method and disturbance feedback policies.

Future work can extend this technique for generating robust controllers for MIMO systems using robust optimization. Further, the automatic differentiation technique could also be used for tuning PID controllers in robotic systems. Output feedback controller optimization also warrants further theoretical study.

### III-B1 Actuator saturation as a disturbance

### III-B Disturbance feedback policies and back-calculation

### III-B3 Optimization for Parameter Tuning

The non-convex optimization problem of interest is posed as an output-feedback controller design with augmented state and...
