Differentiable GPU-Parallelized Task and Motion Planning

Topics include Task and motion planning, Compute unified device architecture, Graphics processing unit, Parallelized, Differentiable optimization, Robot manipulation, Bilevel planning.

Exploits GPU parallelism to simultaneously evaluate thousands of candidate continuous parameter seeds for a given plan skeleton, then applies differentiable gradient-based optimization to each seed in parallel to satisfy the induced continuous constraint satisfaction problem. This combines the discrete search of classical TAMP with massively parallel differentiable optimization, significantly reducing solve times for long-horizon manipulation tasks in highly constrained settings.

Planning long-horizon robot manipulation requires making discrete decisions about which objects to interact with and continuous decisions about how to interact with them. A robot planner must select grasps, placements, and motions that are feasible and safe. This class of problems falls under Task and Motion Planning (TAMP) and poses significant computational challenges in terms of algorithm runtime and solution quality, particularly when the solution space is highly constrained. To address these challenges, we propose a new bilevel TAMP algorithm that leverages GPU parallelism to efficiently explore thousands of candidate continuous solutions simultaneously. Our approach uses GPU parallelism to sample an initial batch of solution seeds for a plan skeleton and to apply differentiable optimization on this batch to satisfy plan constraints and minimize solution cost with respect to soft objectives. We demonstrate that our algorithm can effectively solve highly constrained problems with non-convex constraints in just seconds, substantially outperforming serial TAMP approaches, and validate our approach on multiple real-world robots.

## Introduction

Task and Motion Planning (TAMP) enables robots to plan long-horizon manipulation through integrated reasoning about sequences of discrete action types, such as pick, place, or press, and continuous action parameter values, such as grasps, placements, and trajectories \[\]. TAMP planners have demonstrated remarkable generality in complex tasks including object rearrangement \[\], multi-arm assembly \[\], and cooking a meal \[\]....

A popular family of TAMP algorithms solve problems by first searching over discrete action sequences, also known as plan skeletons, and then searching for continuous action parameter values that satisfy the collective action constraints that govern legal parameter values. Each candidate plan skeleton induces a continuous Constraint Satisfaction Problem (CSP), which TAMP algorithms typically solve using a mixture of compositional sampling and joint optimization techniques, with each having their own trade-offs \[\].

Figure 8: Packing fruit with obstacles. The strawberry is obstructed by four Lego blocks, requiring at least two to be moved for a feasible grasp. cuTAMP autonomously infers this to find a feasible plan skeleton and valid solution.

While cuTAMP supports 6-DOF grasps, we model placement poses with 3-DOF position and yaw (Section VII). In the future, we would like to also model varying placement roll and pitch, accounting for stable orientations on approximately planar surfaces. Our experiments show that cuTAMP’s optimal configuration is sensitive to the number of particles and cost weights λ, though it performs robustly with the default weights across all tested domains....

A 6-DOF grasp sampler that takes the Grasp(red, g) constraint as input and generates grasps G in the object frame (Figure 4a).
A conditional sampler for robot configurations that takes the grasp samples G and constraints Kin(q1, red, g, p0) and CFreeHold(red, g, q1) as input (Figure 4b). The sampler uses the parallelized inverse kinematics solver from cuRobo to solve for 7-DOF joint positions Q1 ∈ ℝNb × 7 conditioned on the target end-effector poses derived from the grasps G.
A conditional trajectory sampler for τ1 that takes the configurations Q1 and the Motion(q0, τ1, q1) and CFreeTraj(τ1) constraints as input (Figure 4c)....

Grasp(red,g), CFreeHold(red,g,q1), Motion(q1,τ2,q2),

#Opt. Plans
