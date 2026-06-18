Optimal Sampling-Based Motion Planning under Differential Constraints: The Drift Case with Linear Affine Dynamics

Topics include Motion planning, Sampling-based methods, Planning, Control, Sampling, Constraints.

In this paper we provide a thorough, rigorous theoretical framework to assess optimality guarantees of sampling-based algorithms for drift control systems: systems that, loosely speaking, can not stop instantaneously due to momentum. We exploit this framework to design and analyze a sampling-based algorithm (the Differential Fast Marching Tree algorithm) that is asymptotically optimal, that is, it is guaranteed to converge, as the number of samples increases, to an optimal solution. In addition, our approach allows us to provide concrete bounds on the rate of this convergence. The focus of this paper is on mixed time/control energy cost functions and on linear affine dynamical systems, which encompass a range of models of interest to applications (e.g., double-integrators) and represent a necessary step to design, via successive linearization, sampling-based and provably-correct algorithms for non-linear drift control systems. Our analysis relies on an original perturbation analysis for two-point boundary value problems, which could be of independent interest.

## Introduction

A key problem in robotics is how to compute an obstacle-free and dynamically-feasible trajectory that a robot can execute. The problem, in the simplest setting where the robot does not have kinematic/dynamical (in short, differential) constraints on its motion and the problem becomes one of finding an obstacle-free "geometric" path, is reasonably well-understood and sound algorithms exist for most practical scenarios. However, robotic systems *do* have differential constraints (e.g., momentum), which most often cannot be neglected....

Broadly speaking, the DMP problem can be divided into two categories: (i) DMP for driftless systems, and (ii) DMP for drift systems. Intuitively, systems with drift constraints are systems where from some states it is impossible to stop instantaneously (this is typically due to momentum). More rigorously, a system $\overset{˙}{\mathbf{x}} = {f{(\mathbf{x},\mathbf{u})}}$ is a drift system if for some state $\mathbf{x}$ there does not exist any admissible control $\mathbf{u}$ such that ${f{(\mathbf{x},\mathbf{u})}} = 0$....

In this paper we have provided a thorough and rigorous theoretical framework to assess optimality guarantees of sampling-based algorithms for linear affine systems with a mixed time/energy cost function. In particular, we leveraged the study of small-cost perturbations to show that optimum-approximating waypoints may be found among randomly sampled state sets with high probability. We applied this analysis to design and theoretically validate an asymptotically optimal algorithm, DFMT^∗^, for the LQDMP problem.

Although this work is nominally limited to linear affine drift systems, it not only provides a good model for many real systems, but is a crucial first step towards modelling nonlinear systems as well. Indeed, since DFMT^∗^ can be applied to a nonlinear system by linearizing the dynamics, an important next step will be to assess the theoretical guarantees of DFMT^∗^ applied to such a linearized approximation....

Then integrating the system dynamics yields

### III-B Small-Time Characterization of the Spectrum of the Controllability Gramian

### Lemma IV.5 (Lemma IV.4, )

To date, the state of the art for one-shot solutions to the DMP problem (both for driftless and drift systems) is represented by sampling-based techniques, whereby an explicit construction of the configuration...
