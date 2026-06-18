Judo: A User-Friendly Open-Source Package for Sampling-Based Model Predictive Control

Topics include Model predictive control, Sampling-based control, Model predictive path integral control, MuJoCo, Open source, Software, Real-time control.

Judo is an open-source Python package providing standardized implementations of sampling-based MPC algorithms (MPPI, CEM, Predictive Sampling, etc.), benchmark tasks, and an interactive GUI for controller tuning. It uses MuJoCo as its physics backend for real-time performance, and supports asynchronous execution to ease sim-to-hardware transfer. The focus is on tooling and usability rather than novel algorithmic contributions. One interesting thing is that Judo runs 100% on CPU (by necessity rather than choice, as the authors indicate they are waiting for development of mujoco_warp to stabilize to provide GPU-based sim rollouts). If you get a server grade Threadripper CPU with 64 cores/128 threads you can do amazing things and plan/control in < 2ms.

Recent advancements in parallel simulation and successful robotic applications are spurring a resurgence in sampling-based model predictive control. To build on this progress, however, the robotics community needs common tooling for prototyping, evaluating, and deploying sampling-based controllers. We introduce Judo, a software package designed to address this need. To facilitate rapid prototyping and evaluation, Judo provides robust implementations of common sampling-based MPC algorithms and standardized benchmark tasks. It further emphasizes usability with simple but extensible interfaces for controller and task definitions, asynchronous execution for straightforward simulation-to-hardware transfer, and a highly customizable interactive GUI for tuning controllers interactively. While written in Python, the software leverages MuJoCo as its physics backend to achieve real-time performance, which we validate across both consumer and server-grade hardware. Code at

## Introduction

Recent advances in parallel model-based simulation tools have shown the effectiveness of sampling-based algorithms like predictive sampling, the cross-entropy method (CEM), model predictive path integral control (MPPI), and more for generating rich, dynamic plans for a wide variety of tasks (including contact-rich ones) in real time with limited resources. Moreover, recent results demonstrate that these strategies can effectively solve real-world tasks, including quadrupedal and bipedal locomotion as well as dexterous, in-hand object reorientation.

To that end, this work presents `judo`, an open-source library for developing, tuning, and deploying sampling-based MPC algorithms. The aim of `judo` is to provide a user-friendly implementation that is also performant, and enables simple transfer of controllers from simulation to hardware.

## Design Principles

The

Maximize Research Velocity. Echoing MJPC, `judo`'s main goal is to accelerate research in sampling-based MPC. To achieve this, `judo` is implemented in Python, offering an effective balance of rapid prototyping and performance suitable for rapid development. Its simple yet extensible interfaces are designed to facilitate extension of (and contribution to) the core codebase. Moreover, an integrated GUI provides real-time visualization and tuning of task and algorithm hyperparameters, significantly shortening the development loop.

## Conclusion

We hope that `judo` can facilitate the prototyping and development of sampling-based MPC algorithms in the wider robotics community. By focusing on a feature-rich and user-friendly interface, `judo` provides a hackable, extensible, and expressive framework for the development of new algorithms and investigation of complex tasks. In the future, we have an exciting roadmap of upcoming features, including integration with learned controllers, examples of hardware usage, and adding many more tasks and optimizers to the core library.
