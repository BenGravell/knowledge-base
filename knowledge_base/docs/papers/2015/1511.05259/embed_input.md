Completeness of Randomized Kinodynamic Planners with State-based Steering

Topics include Kinodynamic planning, Probabilistic completeness, State-based steering, Steering function, Interpolation.

Proves probabilistic completeness for state-based (interpolating) kinodynamic planners under verifiable assumptions. Identifies second-order continuity as the key design requirement. Nice explanation of state-based steering and its beneficial properties as compraed with e.g. randomized action-propagation steering. Contains a great Section 2.3 on the differences between categories of steering functions.

Probabilistic completeness is an important property in motion planning. Although it has been established with clear assumptions for geometric planners, the panorama of completeness results for kinodynamic planners is still incomplete, as most existing proofs rely on strong assumptions that are difficult, if not impossible, to verify on practical systems. In this paper, we focus on an important class of kinodynamic planners, namely those that interpolate trajectories in the state space. We provide a proof of probabilistic completeness for such planners under assumptions that can be readily verified from the system's equations of motion and the user-defined interpolation function. Our proof relies crucially on a property of interpolated trajectories, termed second-order continuity (SOC), which we show is tightly related to the ability of a planner to benefit from denser sampling. We analyze the impact of this property in simulations on a low-torque pendulum. Our results show that a simple RRT using a second-order continuous interpolation swiftly finds solution, while it is impossible for the same planner using standard Bezier curves (which are not SOC) to find any solution.

## Introduction

A deterministic motion planner is said to be *complete* if it returns a solution whenever one exists. A *randomized* planner is said to be *probabilistically complete* if the probability of returning a solution, when there is one, tends to one as execution time goes to infinity. Theoretical as they may seem, these two notions are of notable practical interest, as proving completeness requires one to formalize the problem by hypotheses on the robot, the environment, etc....

Probabilistic completeness has been established for systems with *geometric* constraints such as *e.g.* obstacle avoidance. However, proofs for systems with *kinodynamic* constraints have yet to reach the same level of generality. Proofs available in the literature often rely on strong assumptions that are difficult to verify on practical systems (as a matter of fact, none of the previously mentioned works verified their hypotheses on non-trivial systems). In this paper, we establish probabilistic completeness (Section 3) for a large class of kinodynamic planners, namely those that interpolate trajectories in the state space....

## Conclusion

In this paper, we provided the first "operational" proof of probabilistic completeness for a large class of randomized kinodynamic planners, namely those that interpolate state-space trajectories. We observed that an important ingredient for completeness is the "continuity" of the interpolation procedure, which we characterized by the *second-order continuity* (SOC) property....

Figure 2: Single (A) and double (B) pendulums. Under torque bounds, these systems must swing back and forth several times before they can reach for the upright position, as depicted in (B) (lighter images represent earlier times).

### Terminology

We can now state our main theorem:

The most important of these properties is *second-order continuity* (SOC), which states that the interpolation function varies smoothly and locally between states that are close. We evaluate the impact of this property in simulations (Section 4) on a low-torque pendulum. Experiments validate our completeness theorem, and suggest that SOC is an important design guideline for kinodynamic planners that interpolate in the state space.

## Background

### Kinodynamic Constraints
