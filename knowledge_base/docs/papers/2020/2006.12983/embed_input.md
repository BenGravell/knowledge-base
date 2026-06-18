dm_control: Software and Tasks for Continuous Control

The dm_control software package is a collection of Python libraries and task suites for reinforcement learning agents in an articulated-body simulation. A MuJoCo wrapper provides convenient bindings to functions and data structures. The PyMJCF and Composer libraries enable procedural model manipulation and task authoring. The Control Suite is a fixed set of tasks with standardised structure, intended to serve as performance benchmarks. The Locomotion framework provides high-level abstractions and examples of locomotion tasks. A set of configurable manipulation tasks with a robot arm and snap-together bricks is also included. dm_control is publicly available at

## Introduction

Controlling the physical world is an integral part and arguably a prerequisite of general intelligence. Indeed, the only known example of general-purpose intelligence emerged in primates whose behavioural niche was already contingent on two-handed manipulation for millions of years.

Unlike board games, language and other symbolic domains, physical tasks are fundamentally continuous in state, time and action. Physical dynamics are subject to second-order equations of motion -- the underlying state is composed of positions and velocities. Sensory signals (i.e. observations) carry meaningful physical units and vary over corresponding timescales. These properties, along with their prevalence and importance, make control problems a unique subset of general Markov Decision Processes.

## Software for research

The dm_control package was designed by DeepMind scientists and engineers to facilitate their own continuous control and robotics needs, and is therefore well-suited for research. It is written in Python, exploiting the agile workflow of a dynamic language, while relying on the C-based MuJoCo physics library, a fast and accurate simulator, itself designed to facilitate research.

The ctypes-based MuJoCo wrapper (Sec. 2) provides full access to the simulator, conveniently exposing quantities with named indexing. A Python-based interactive visualiser (Sec. 2.2) allows the user to examine and perturb scene elements with a mouse.

## Conclusion

dm_control is a starting place for the testing and performance comparison of reinforcement learning algorithms for physics-based control. It offers a wide range of pre-designed RL tasks and a rich framework for designing new ones. We are excited to be sharing these tools with the wider community and hope that they will be found useful. We look forward to the diverse research the Control Suite and associated libraries may enable, and to integrating community contributions in future releases.
