# Trajectory Optimization Software

## Gradient-based MPC

### iLQR / DDP

- [aligator](https://github.com/Simple-Robotics/aligator) - versatile and efficient framework for constrained trajectory optimization (C++)
- [crocoddyl: ddp.cpp](https://github.com/loco-3d/crocoddyl/blob/master/src/core/solvers/ddp.cpp) - DDP solver in the crocoddyl optimal control library
- [mujoco_mpc: ilqg planner](https://github.com/google-deepmind/mujoco_mpc/tree/main/mjpc/planners/ilqg) - iLQG planner inside MuJoCo MPC
- [nuplan-devkit: ilqr_tracker.py](https://github.com/motional/nuplan-devkit/blob/master/nuplan/planning/simulation/controller/tracker/ilqr_tracker.py) - iLQR tracker in the nuPlan planning framework

### trajax

- [google/trajax](https://github.com/google/trajax/tree/main) - differentiable trajectory optimization using JAX (iLQR, DDP)
- [L4DC 2022 trajax tutorial](https://l4dc.seas.upenn.edu/tutorials/)

### ALTRO (Augmented Lagrangian Trajectory Optimizer)

- [TrajectoryOptimization.jl](https://rexlab.ri.cmu.edu/TrajectoryOptimization.jl/stable/) - Julia trajectory optimization framework (REx Lab, CMU)
- [Altro.jl](https://github.com/RoboticExplorationLab/Altro.jl) - Julia implementation of ALTRO
- [ALTRO (C++)](https://github.com/RoboticExplorationLab/ALTRO) - C++ implementation of ALTRO (REx Lab)
- [altro-cpp (optimusride)](https://github.com/optimusride/altro-cpp) - alternative C++ port of ALTRO

## Sampling-Based MPC

### MuJoCo MPC

- [google-deepmind/mujoco_mpc](https://github.com/google-deepmind/mujoco_mpc) - real-time behaviour synthesis with MuJoCo using Predictive Sampling, MPPI, and related methods
- [[2212.00541] Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo](https://arxiv.org/abs/2212.00541)

### judo

- [bdaiinstitute/judo](https://github.com/bdaiinstitute/judo) - user-friendly Python package for sampling-based MPC (MPPI, CEM, Predictive Sampling) with MuJoCo backend
- [RAI Institute: judo workshop page](https://rai-inst.com/resources/workshop/judo-open-source-package-for-sampling-based-model-predictive-control/)
- [RAI Institute: Combining Sampling and Learning for Dynamic Whole-Body Manipulation](https://rai-inst.com/resources/blog/combining-sampling-and-learning-for-dynamic-whole-body-manipulation/)

### hydrax

- [vincekurtz/hydrax](https://github.com/vincekurtz/hydrax) - sampling-based MPC on GPU with JAX and MuJoCo MJX
