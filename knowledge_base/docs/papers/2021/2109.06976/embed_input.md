GRiD: GPU-Accelerated Rigid Body Dynamics with Analytical Gradients

We introduce GRiD: a GPU-accelerated library for computing rigid body dynamics with analytical gradients. GRiD was designed to accelerate the nonlinear trajectory optimization subproblem used in state-of-the-art robotic planning, control, and machine learning, which requires tens to hundreds of naturally parallel computations of rigid body dynamics and their gradients at each iteration. GRiD leverages URDF parsing and code generation to deliver optimized dynamics kernels that not only expose GPU-friendly computational patterns, but also take advantage of both fine-grained parallelism within each computation and coarse-grained parallelism between computations. Through this approach, when performing multiple computations of rigid body dynamics algorithms, GRiD provides as much as a 7.2x speedup over a state-of-the-art, multi-threaded CPU implementation, and maintains as much as a 2.5x speedup when accounting for I/O overhead. We release GRiD as an open-source library for use by the wider robotics community.

## Introduction

Efficient implementations of rigid body dynamics and their gradients have become key computational kernels for robotics applications. Originally required mostly for the nonlinear trajectory optimization sub-problems of model-based planning and control systems for high degrees-of-freedom robots, these computational kernels are also growing in importance for machine learning (ML) techniques.

Despite being highly accurate and optimized, existing implementations of spatial-algebra-based approaches to rigid body dynamics do not take advantage of opportunities for parallelism present in the algorithm, limiting their performance. This is critical because there is natural parallelism in many bottleneck computations involving rigid body dynamics in robotics. For example, the gradient of forward dynamics accounts for $30$% to $90$% of typical nonlinear model-predictive control (MPC) implementations, and is naturally parallel across the discrete points in the trajectory.

We would also like to add support for differentiating through model parameters, as well as for contact, and hope to integrate these accelerated dynamics implementations into existing robotics software frameworks. This would increase both GRiD's ease-of-use and applicability to more robotics researchers.

Finally, building out increased support for more trajectory optimization, MPC, and ML algorithms running entirely on the GPU would further increase the performance benefits from integrating GRiD into these approaches.

### IV-C Code Optimization Approach

The open-source GRiD library can be found at In this section we describe its design, features and code optimization approach.

We used a high-performance workstation with a $3.8$GHz eight-core Intel Core i7-10700K CPU and a $1.44$GHz NVIDIA GeForce RTX 3080 GPU running Ubuntu 20.04 and CUDA 11.4.^44^4For clean timing measurements on the CPU, we disabled TurboBoost and fixed the clock frequency to the maximum. Code was compiled with Clang 12 and g++9.4, and time was measured with the Linux system call clock_gettime, using CLOCK_MONOTONIC as the source. We compare timing results across three robot models: the 7 degrees-of-freedom (dof) Kuka LBR IIWA-14 manipulator, the 12 dof HyQ quadruped, and the 30 dof Atlas humanoid....
