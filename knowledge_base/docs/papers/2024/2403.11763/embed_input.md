Convex Co-Design of Control Barrier Functions and State Feedback Controllers for Linear Systems with Input Constraints

Topics include Control barrier functions, Safety, Sum-of-squares programming, Semidefinite programming, Input constraints, Linear systems.

Formulates joint CBF and linear feedback-controller synthesis for linear systems as a semidefinite program, including input constraints and mixed-relative-degree safe sets. The useful idea is treating safe-set certificate design and controller design as one convex co-design problem.

We study the problem of co-designing control barrier functions (CBF) and linear state feedback controllers for continuous-time linear systems. We achieve this by means of a single semi-definite optimization program. Our formulation can handle mixed-relative degree problems without requiring an explicit safe controller. Different L-norm based input limitations can be introduced as convex constraints in the proposed program. We demonstrate our results on an omni-directional car numerical example.

## Introduction

Safety is essential for feedback control systems. As a system is steered from an initial set to a target set, safety requires that the trajectory of the system avoids entering an unexpected region, or to remain inside a safe set. On the state space, safety is always formulated by means of constraints imposed on states.

A CBF aims to separate the safe and unsafe regions by its zero super- and sub-level sets; the initial set also belongs to the level set. In addition, there exists a control law, such that the vector field points towards the safe side on its zero sub-level set. This property is also known as *invariance*, characterized by Nagumo's theorem. It is therefore guaranteed that if the system starts from a point inside the zero super-level set, the system can always stay inside. Given a CBF, the controller that guarantees safety can be designed according to the direction requirement of vector field.

Designing a CBF is even more challenging when the relative degree between the function defines safe set and the system dynamics is high or mixed. For relative degree we mean the number of times we need to differentiate a function whose level set encodes the safe set along the system dynamics until the control explicitly shows. High or mixed relative degree is commonly seen in robotics collision avoidance problems, where the safe set is usually defined over positions for the obstacles, but the control signals are imposed on accelerations.

## Conclusion

In this paper we proposed a method to synthesize a control barrier function and a state feedback controller by solving a single convex program. Our approach considers quadratic control barrier functions and affine state feedback controllers. Different types of control input limits can be handled as additional convex constraints to the synthesis program. We demonstrate the efficacy of our approach on an omni-directional car collision avoidance problem. Future work concentrates towards generalizing the obtained results to allow using higher-relative degree polynomials for the CBF and the controller.
