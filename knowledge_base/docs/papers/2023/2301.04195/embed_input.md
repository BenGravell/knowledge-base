Orbit: A Unified Simulation Framework for Interactive Robot Learning Environments

Topics include Reinforcement learning, Imitation learning, Motion planning, Robotics, Representation learning, Datasets, Benchmarks, Planning, Learning, Orbit, Modular design.

We present Orbit, a unified and modular framework for robot learning powered by NVIDIA Isaac Sim. It offers a modular design to easily and efficiently create robotic environments with photo-realistic scenes and high-fidelity rigid and deformable body simulation. With Orbit, we provide a suite of benchmark tasks of varying difficulty - from single-stage cabinet opening and cloth folding to multi-stage tasks such as room reorganization. To support working with diverse observations and action spaces, we include fixed-arm and mobile manipulators with different physically-based sensors and motion generators. Orbit allows training reinforcement learning policies and collecting large demonstration datasets from hand-crafted or expert solutions in a matter of minutes by leveraging GPU-based parallelization. In summary, we offer an open-sourced framework that readily comes with 16 robotic platforms, 4 sensor modalities, 10 motion generators, more than 20 benchmark tasks, and wrappers to 4 learning libraries. With this framework, we aim to support various research areas, including representation learning, reinforcement learning, imitation learning, and task and motion planning....

## Introduction

ThreeDWorld supports simulation of rigid bodies and deformable bodies based on whether PhysX 4 or FleX/Obi is enabled respectively. Thus, it is limited in simulating interactions between rigid and deformable bodies.
ManiSkill2 supports a Warp-based Material Point Method (MPM) solver that helps simulate cutting and plastic deformations of soft objects. Currently, this feature is under development for Orbit.

TABLE I: Comparison between different simulation frameworks and Orbit. The check ( ✓) and cross ( X) denote presence or absence of the feature. In Robotic Platforms column, M stands for manipulator. In Scene Authoring column, G stands for game-based designing, M for mesh-scan scenes, and P for procedural-generation.

While our experiments demonstrate the effectiveness of rigid-contact modeling and FEM for soft bodies, quantitatively studying the fidelity of the entire simulator (such as rendering, sensors, and physics) remains an area for future exploration. It is important to note that robotics research, particularly in deformable-body manipulation, has infrequently used sim-to-real due to difficulties in achieving fast and accurate simulation and realistic rendering. We believe that Orbit can help address these challenges and facilitate answering open research questions in these fields.

Further enhancements to the framework include integrating tactile sensors and 6-axis force-torque sensors. Additionally, we plan to add support for loading assets directly in their native formats (such as URDF and OBJ) instead of USDs to make the framework more versatile and user-friendly.

With Orbit, we include GPU-based implementations for differential IK \[\], operational-space control \[\], and joint-level control, which compute commands for several robots efficiently. Additionally, we provide CPU implementation of state-of-the-art model-based planners such as RMP-Flow \[\] for fixed-arm manipulators and OCS2 \[\] for whole-body control of mobile manipulators. To facilitate research in legged robot navigation, such as traversability estimation and path-planning, we also include pre-trained policies for legged locomotion \[\] that track base velocity commands.

### Agent

We create a state machine for a given task to perform sequential planning as a separate node in the agent....
