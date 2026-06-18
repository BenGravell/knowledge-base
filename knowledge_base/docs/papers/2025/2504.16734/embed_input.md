DYNUS: Uncertainty-aware Trajectory Planner in Dynamic Unknown Environments

This paper introduces DYNUS, an uncertainty-aware trajectory planner designed for dynamic unknown environments. Operating in such settings presents many challenges - most notably, because the agent cannot predict the ground-truth future paths of obstacles, a previously planned trajectory can become unsafe at any moment, requiring rapid replanning to avoid collisions. Recently developed planners have used soft-constraint approaches to achieve the necessary fast computation times; however, these methods do not guarantee collision-free paths even with static obstacles. In contrast, hard-constraint methods ensure collision-free safety, but typically have longer computation times. To address these issues, we propose three key contributions. First, the DYNUS Global Planner (DGP) and Temporal Safe Corridor Generation operate in spatio-temporal space and handle both static and dynamic obstacles in the 3D environment. Second, the Safe Planning Framework leverages a combination of exploratory, safe, and contingency trajectories to flexibly re-route when potential future collisions with dynamic obstacles are detected....

## Introduction

Path and trajectory planning for autonomous navigation has been extensively studied. In practical implementations of trajectory planning methods, it is crucial to avoid making overly strict prior assumptions about the environment, as these can limit the generalizability of an approach. This work aims to develop a trajectory planner that utilizes a highly relaxed set of assumptions, which enables it to operate on a wide range of vehicles in a diverse set of environments. The assumptions made by DYNUS are listed in Section II-E. In Section I-A, we demonstrate that DYNUS is capable of operating in a wide range of environments....

### I-A Classification of Environments

## Conclusions

In this paper, we present DYNUS, an uncertainty-aware trajectory planning framework for dynamic, unknown environments. DYNUS navigates across diverse settings, including unknown, confined, cluttered, static, and dynamic spaces. It integrates a spatio-temporal global planner (DGP), a framework for handling dynamic obstacle unpredictability, and a variable elimination-based local optimizer for fast, safe trajectory generation. We validate DYNUS in simulation across forests, office spaces, and caves, and on hardware with UAV, wheeled, and legged robots. Future work will implement larger-scale deployments and further computational improvements.

and we solve the variable-eliminated optimization problem in parallel with different factors $f$ to find the optimal time allocation:

### IV-A Position Trajectory Optimization

## Frontier-based exploration

Environments are classified by three criteria: known vs. unknown, static vs. dynamic, and open vs. confined. Known environments provide agents with prior information, while unknown environments do not. Static environments have fixed obstacles, whereas dynamic environments could include moving ones. The primary difference is predictability: static obstacles do not change position once observed, while dynamic obstacles continuously move, making it a challenging planning environment....

Table I compares the capabilities of numerous UAV trajectory planners under these environmental assumptions. State-of-the-art methods such as FASTER \[\], EGO-Planner \[\], RAPTOR \[\], HDSM \[\], and SUPER \[\] are designed for unknown static environments....
