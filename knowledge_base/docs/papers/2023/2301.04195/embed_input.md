Orbit: A Unified Simulation Framework for Interactive Robot Learning Environments

Topics include Reinforcement learning, Imitation learning, Motion planning, Robotics, Representation learning, Datasets, Benchmarks, Planning, Learning, Orbit, Modular design.

We present Orbit, a unified and modular framework for robot learning powered by NVIDIA Isaac Sim. It offers a modular design to easily and efficiently create robotic environments with photo-realistic scenes and high-fidelity rigid and deformable body simulation. With Orbit, we provide a suite of benchmark tasks of varying difficulty - from single-stage cabinet opening and cloth folding to multi-stage tasks such as room reorganization. To support working with diverse observations and action spaces, we include fixed-arm and mobile manipulators with different physically-based sensors and motion generators. Orbit allows training reinforcement learning policies and collecting large demonstration datasets from hand-crafted or expert solutions in a matter of minutes by leveraging GPU-based parallelization. In summary, we offer an open-sourced framework that readily comes with 16 robotic platforms, 4 sensor modalities, 10 motion generators, more than 20 benchmark tasks, and wrappers to 4 learning libraries. With this framework, we aim to support various research areas, including representation learning, reinforcement learning, imitation learning, and task and motion planning.

## Introduction

ThreeDWorld supports simulation of rigid bodies and deformable bodies based on whether PhysX 4 or FleX/Obi is enabled respectively. Thus, it is limited in simulating interactions between rigid and deformable bodies.
ManiSkill2 supports a Warp-based Material Point Method (MPM) solver that helps simulate cutting and plastic deformations of soft objects. Currently, this feature is under development for Orbit.

Our

Through experiments, we demonstrate the accuracy of the simulator for rigid and soft body simulation. Compared to existing frameworks, we show that Orbit is able to obtain up to $\sim 10$x and $\sim 3$x the throughput for rigid and deformable body manipulation tasks respectively. Additionally, we demonstrate the sim-to-real transfer of a locomotion policy for the quadruped robot, ANYmal.

In the remainder of the paper, we describe the available simulator choices (Sec. II), the framework's design decisions and abstractions (Sec. III), and its highlighted features (Sec. IV). We demonstrate the framework's applicability on different robotics workflows (Sec. V), show sim-to-real experiments for locomotion and manipulation, and evaluate the obtained accuracy and simulation throughput in Sec. V-E.

## Discussion

In this paper, we proposed Orbit: an interactive and intuitive framework to simplify environment designing, enable easy task specifications, and lower the entry barrier into robotics and robot learning. Orbit exploits the latest state-of-the-art simulation capabilities through Isaac Sim and extends them further to incorporate different actuator and sensor noise models into the simulation, and advance sensors, actuators, and motion generators at varying operating frequencies.

By open-sourcing this framework^44^4 Nvidia Isaac Sim is free with an individual license. Orbit is open-sourced on GitHub and available at we aim to reduce the overhead for developing new applications and provide a unified platform for robot learning research. As we continue to enhance and incorporate more features into the framework, we encourage researchers to contribute to transforming it into a comprehensive solution for robotics research.
