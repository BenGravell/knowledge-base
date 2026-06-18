Fast and Certifiable Trajectory Optimization

Topics include Semidefinite programming, Nonconvex optimization, Trajectory optimization, Robotics, Vehicles, Real-time systems, Optimization, STROM, PSD.

We propose semidefinite trajectory optimization (STROM), a framework that computes fast and certifiably optimal solutions for nonconvex trajectory optimization problems defined by polynomial objectives and constraints. STROM employs sparse second-order Lasserre's hierarchy to generate semidefinite program (SDP) relaxations of trajectory optimization. Different from existing tools (e.g., YALMIP and SOSTOOLS in Matlab), STROM generates chain-like multiple-block SDPs with only positive semidefinite (PSD) variables. Moreover, STROM does so two orders of magnitude faster. Underpinning STROM is cuADMM, the first ADMM-based SDP solver implemented in CUDA and runs in GPUs (with C/C++ extension). cuADMM builds upon the symmetric Gauss-Seidel ADMM algorithm and leverages GPU parallelization to speedup solving sparse linear systems and projecting onto PSD cones. In five trajectory optimization problems (inverted pendulum, cart-pole, vehicle landing, flying robot, and car back-in), cuADMM computes optimal trajectories (with certified suboptimality below 1%) in minutes (when other solvers take hours or run out of memory) and seconds (when others take minutes).

## Introduction

Trajectory optimization designs dynamical system trajectories by optimizing a performance measure subject to constraints, finding extensive applications in motion planning of robotic, aerospace, and manufacturing systems.

where ${{l_{k},k} = 0},{\ldots,N}$ are the instantaneous and terminal loss functions; $x_{\text{init}}$ is the initial state; $F_{k}$ represents the discretized system dynamics in the form of a differential algebraic equation and §); and $\mathcal{C}_{k}$ imposes constraints on $u_{k - 1}$ and $x_{k}$ (*e.g.,* control limits, obstacle avoidance). Trajectory optimization computes open-loop control; when paired with receding horizon control (*i.e.,* execute only part of the optimal control sequence and repeatedly solve ), leads to closed-loop control with implicit feedback known as *model predictive control* (MPC).

In this paper, we assume $l_{k}$ and $F_{k}$ are polynomial functions and $\mathcal{C}_{k}$ are basic semialgebraic sets (*i.e.,* described by polynomial constraints), in which case problem is an instance of *polynomial optimization* (POP) that is nonconvex and NP-hard in general. We briefly review solution methods for problem.

Contributions. We present STROM (semidefinite trajectory optimization), a fast and certifiable trajectory optimization framework that checks the merits.

Faster sparse moment relaxation. Unlike existing tools in Matlab such as sostools and yalmip that generate sparse second-order SDP relaxations of problem from the dual SOS perspective, we develop a C++ tool to generate SDP relaxations from the *primal moment* perspective. Our POP-SDP conversion reveals the special *chain-like sparsity pattern* in the relaxed multiple-cone SDP. It is two orders of magnitude faster than yalmip and sostools, and on par with the Julia package tssos.

## Conclusion

We presented STROM, a new framework for fast and certifiable trajectory optimization. STROM contains two modules: a C++ package that generates sparse moment relaxations, and a first-order ADMM-based SDP solver cuADMM directly implemented in CUDA. Our C++ package is two orders of magnitude faster than existing Matlab packages, and our cuADMM solves large-scale SDPs far beyond the reach of existing solvers. Moreover, we demonstrated the potential of real-time certifiable trajectory optimization in inverted pendulum using data-driven warmstarts.
