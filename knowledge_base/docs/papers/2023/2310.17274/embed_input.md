cuRobo: Parallelized Collision-Free Minimum-Jerk Robot Motion Generation

Topics include Motion planning, Trajectory optimization, Compute unified device architecture, Graphics processing unit, Parallelized, Inverse kinematics, Robot manipulation, Open source, Software.

CUDA-accelerated library for collision-free robot motion generation. Formulates trajectory generation as a global optimization problem solved across thousands of parallel seeds on GPU. Combines L-BFGS with a novel parallel noisy line search and particle-based optimization to produce minimum-jerk, collision-free trajectories within ~50ms. Also includes a parallel geometric planner (~20ms) and a batched IK solver (>7000 queries/s). An earlier version without minimum-jerk optimization was published at ICRA 2023.

This paper explores the problem of collision-free motion generation for manipulators by formulating it as a global motion optimization problem. We develop a parallel optimization technique to solve this problem and demonstrate its effectiveness on massively parallel GPUs. We show that combining simple optimization techniques with many parallel seeds leads to solving difficult motion generation problems within 53ms on average, 62x faster than SOTA trajectory optimization methods. We achieve SOTA performance by combining L-BFGS step direction estimation with a novel parallel noisy line search scheme and a particle-based optimization solver. To further aid trajectory optimization, we develop a parallel geometric planner that is atleast 28x faster than SOTA RRTConnect implementations. We also introduce a collision-free IK solver that can solve over 9000 queries/s. We are releasing our GPU accelerated library CuRobo that contains core components for robot motion generation. Additional details are available at sites.google.com/nvidia.com/curobo.

## Introduction

Safe navigation is fundamental to robotics, requiring robots to have a robust global motion generation system to traverse any environment structure encountered at deployment. Motion generation for high-dimensional systems is extremely challenging as satisfying complex constraints and minimizing cost terms in a very large C-Space is computationally expensive. Manipulators, for instance, can have many articulations, complex link geometries, entire goal regions beyond a single configuration, task constraints, and nontrivial kinematic and torque limitations....

The global optimization literature suggests that finding the true global minimum is usually impractical, but strategies for robustly finding high-performing local minima can be effective. Many strategies follow the simple pattern of selecting many seed candidates and performing a local optimization for each. This sample and optimize process can often realize substantial gains by leveraging distributed computation. However, most motion generation systems today remain sequential and slow, following a CPU-based design. State-of-the-art motion generation solutions take 0.5s to 10s depending on the task's complexity on modern CPUs....

### Limitations & Open Research Problems

There are several open research problems in motion generation that our approach does not solve in it's current form. We hope that our results and framework can be leveraged to solve these problems. We list some key problems below,\
Global Reactive Motion Generation Our approach is currently limited to planning full motions, where the robot starts from a static state....

Figure 12: We compare the compute time for motion generation between cuRobo and Tesseract across three compute platforms. On all of the 2600 motion planning problems, we found cuRobo to take the least time, getting a 60× speedup on average on a desktop pc with NVIDIA RTX 4090 and AMD Ryzen 9 7950x, with a 83× speedup on the 98th percentile.

Our geometric planner as shown in Alg. 5, first performs heuristic planning by checking if we can steer from start to goal configuration directly or through a predefined retract configuration $\theta_{r}$ (lines 1-7)....
