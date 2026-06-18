Dynamic Movement Primitives in Robotics: A Tutorial Survey

Topics include Reinforcement learning, Optimal control, Robotics, Control, Learning.

Biological systems, including human beings, have the innate ability to perform complex tasks in versatile and agile manner. Researchers in sensorimotor control have tried to understand and formally define this innate property. The idea, supported by several experimental findings, that biological systems are able to combine and adapt basic units of motion into complex tasks finally lead to the formulation of the motor primitives theory. In this respect, Dynamic Movement Primitives (DMPs) represent an elegant mathematical formulation of the motor primitives as stable dynamical systems, and are well suited to generate motor commands for artificial systems like robots. In the last decades, DMPs have inspired researchers in different robotic fields including imitation and reinforcement learning, optimal control,physical interaction, and human-robot co-working, resulting a considerable amount of published papers. The goal of this tutorial survey is two-fold. On one side, we present the existing DMPs formulations in rigorous mathematical terms,and discuss advantages and limitations of each approach as well as practical implementation details....

## Introduction

*How biological systems, like humans and animals, execute complex movements in a versatile and creative manner?*

In the past decades, researchers of neurobiology and motor control have made a significant effort trying in to answer this research question and their experimental findings lead to the formulation of the motor or motion primitives theory. The motion primitives theory explains the execution of complex motion with the ability of biological systems of sequencing and adapting units of actions, the so-called motion primitives.

The Austrian Research Foundation (Euregio IPN 86-N30, OLIVER).

Innovation Fund Denmark (Research and innovation project MADE FAST).

Here ${\overset{˙}{C}}_{a} = {\varsigma{({F_{d} - F^{e}})}}$ is the first time-derivative of the admittance coupling term, which changes the velocity and consequently the integrated coupling term, the position output of the DMP. The described approach can be used for Cartesian space motion, where the forces have to be substituted for desired and measured torques. This approach can be implemented in robot tasks involving contact with the environment as well as contact with humans.

Classical DMPs are time invariant, meaning that time scaling $\varsigma\tau$ with $\varsigma > 0$ generate topologically equivalent trajectories. Using a simple modification of the transformation system, namely substituting with

Figure 15: General framework of lifelong/incremental learning approach.

Dynamic Movement Primitives (DMPs) have their roots in the motor control of biological systems and can be seen as a rigorous mathematical formulation of the motion primitives as stable nonlinear dynamical systems. In this respect, DMPs represent one of the first attempts to answer the research question:

*How artificial systems, like (humanoid) robots, can execute complex movements in a versatile and creative manner?*

Beyond their biological motivation, DMPs have a simple and elegant formulation, guarantee convergence to a given target, are sufficiently flexible to create complex behaviors, are capable of reacting to external perturbations in real-time, and can be learned from data using efficient algorithms. These properties explain the "success" of DMPs in robotic applications, where they have established as a prominent tool for learning and generation of motor commands....
