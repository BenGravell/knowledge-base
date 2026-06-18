cpRRTC: GPU-Parallel RRT-Connect for Constrained Motion Planning

Topics include Motion planning, Robotics, Sampling-based methods, Parallel computing, Planning, Sampling, cpRRTC, Compute unified device architecture.

Motion planning is a fundamental problem in robotics that involves generating feasible trajectories for a robot to follow. Recent advances in parallel computing, particularly through CPU and GPU architectures, have significantly reduced planning times to the order of milliseconds. However, constrained motion planning especially using sampling based methods on GPUs remains underexplored. Prior work such as pRRTC leverages a tracking compiler with a CUDA backend to accelerate forward kinematics and collision checking. While effective in simple settings, their approach struggles with increased complexity in robot models or environments. In this paper, we propose a novel GPU based framework utilizing NVRTC for runtime compilation, enabling efficient handling of high complexity scenarios and supporting constrained motion planning. Experimental results demonstrate that our method achieves superior performance compared to existing approaches.

## Introduction

Many robotic tasks require constrained motion planning, where trajectories must not only avoid collisions but also satisfy task-specific constraints. These requirements significantly increase planning complexity, especially in high-dimensional spaces. Sampling-based approaches like CBiRRT \[\] address this by exploring the configuration space under constraints, but struggle in cluttered environments. To leverage GPU acceleration, cuRobo \[\] adopts an optimization-based approach for generating constrained motions efficiently. However, it lacks the global exploration guarantees provided by sampling-based methods....

During tree extension, pRRTC assigns one thread block to handle each motion, where each thread performs forward kinematics(FK) and collision checking(CC) for one waypoint of the motion. To reduce thread divergence, pRRTC uses a tracing compiler to generate CUDA code for both FK and CC. However, due to CUDA's Single Instruction, Multiple Threads (SIMT) execution model, threads in a block must synchronize, meaning that even if one thread detects a collision early, it must wait for all other threads to complete their computations....

Figure 7: Cumulative distribution of solution times for the Franka arm under line and plane constraint primitives.

For experiments with the Franka, cpRRTC demonstrated a similar performance advantage over cuRobo as observed with the Fetch. Notably, in the line-following task, as the number of obstacles increased, cpRRTC-Parallel maintained a consistently high success rate of approximately 99%, whereas cuRobo's success rate declined sharply to 32%. Moreover, cpRRTC-Parallel achieved a 3.4x speed-up in planning time....

Collision checking across threads is inherently parallel, as each thread evaluates an intermediate configuration independently. However, without communication among threads within a block, computation resources may be wasted---especially when an early collision renders the rest of the evaluation unnecessary. In pRRTC \[\], the authors employed a tracking compiler to generate CUDA code for FK and CC. Due to limitations in the code generation process, it is difficult for FK and CC to leverage shared memory, preventing communication between threads during motion evaluation....

the parallel project function produces a constraint-satisfying motion segment:
