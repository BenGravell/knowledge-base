Judo: A User-Friendly Open-Source Package for Sampling-Based Model Predictive Control

Topics include Model predictive control, Sampling-based control, Model predictive path integral control, MuJoCo, Open source, Software, Real-time control.

Judo is an open-source Python package providing standardized implementations of sampling-based MPC algorithms (MPPI, CEM, Predictive Sampling, etc.), benchmark tasks, and an interactive GUI for controller tuning. It uses MuJoCo as its physics backend for real-time performance, and supports asynchronous execution to ease sim-to-hardware transfer. The focus is on tooling and usability rather than novel algorithmic contributions. One interesting thing is that Judo runs 100% on CPU (by necessity rather than choice, as the authors indicate they are waiting for development of mujoco_warp to stabilize to provide GPU-based sim rollouts). If you get a server grade Threadripper CPU with 64 cores/128 threads you can do amazing things and plan/control in < 2ms.

Recent advancements in parallel simulation and successful robotic applications are spurring a resurgence in sampling-based model predictive control. To build on this progress, however, the robotics community needs common tooling for prototyping, evaluating, and deploying sampling-based controllers. We introduce Judo, a software package designed to address this need. To facilitate rapid prototyping and evaluation, Judo provides robust implementations of common sampling-based MPC algorithms and standardized benchmark tasks. It further emphasizes usability with simple but extensible interfaces for controller and task definitions, asynchronous execution for straightforward simulation-to-hardware transfer, and a highly customizable interactive GUI for tuning controllers interactively. While written in Python, the software leverages MuJoCo as its physics backend to achieve real-time performance, which we validate across both consumer and server-grade hardware. Code at

## Introduction

Recent advances in parallel model-based simulation tools have shown the effectiveness of sampling-based algorithms like predictive sampling, the cross-entropy method (CEM), model predictive path integral control (MPPI), and more for generating rich, dynamic plans for a wide variety of tasks (including contact-rich ones) in real time with limited resources \[\]. Moreover, recent results demonstrate that these strategies can effectively solve real-world tasks, including quadrupedal and bipedal locomotion as well as dexterous, in-hand object reorientation \[\]....

To that end, this work presents `judo`, an open-source library for developing, tuning, and deploying sampling-based MPC algorithms. The aim of `judo` is to provide a user-friendly implementation that is also performant, and enables simple transfer of controllers from simulation to hardware.

## Conclusion

We hope that `judo` can facilitate the prototyping and development of sampling-based MPC algorithms in the wider robotics community. By focusing on a feature-rich and user-friendly interface, `judo` provides a hackable, extensible, and expressive framework for the development of new algorithms and investigation of complex tasks. In the future, we have an exciting roadmap of upcoming features, including integration with learned controllers, examples of hardware usage, and adding many more tasks and optimizers to the core library.

### III-B The GUI

pip install judo-rai # one-line install
judo # runs the browser-based GUI

The `judo` stack is modular, consisting of a "system" node (e.g., the simulator or whatever nodes are required to run a hardware stack), a visualizer node, and a controller node. These nodes all asynchronously communicate with each other, where the interprocess communication is handled by `dora` \[\], a fast robotics-first middleware built on `rust` with a full-featured Python interface.

## Design Principles

Figure 1: The judo interface. The GUI is interactive, allowing users to tune parameters in real time. Dropdown menus allow switching between different tasks and controllers with ease.

3class CartpoleConfig(TaskConfig):
9class Cartpole(Task[CartpoleConfig]):
10 def __init__(self, model_path=XML_PATH):
11 super.__init__(model_path, sim_model_path=XML_PATH)
14 def reward(self, states, sensors, controls, config, system_metadata=None):
15 x, y, vel =...
