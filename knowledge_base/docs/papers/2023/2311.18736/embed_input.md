Controlgym: Large-Scale Control Environments for Benchmarking Reinforcement Learning Algorithms

Topics include Reinforcement learning, Stability analysis, Robustness, Benchmarks, Scalability, Control, Learning, Controlgym, Partial differential equation, L4DC.

We introduce controlgym, a library of thirty-six industrial control settings, and ten infinite-dimensional partial differential equation (PDE)-based control problems. Integrated within the OpenAI Gym/Gymnasium (Gym) framework, controlgym allows direct applications of standard reinforcement learning (RL) algorithms like stable-baselines3. Our control environments complement those in Gym with continuous, unbounded action and observation spaces, motivated by real-world control applications. Moreover, the PDE control environments uniquely allow the users to extend the state dimensionality of the system to infinity while preserving the intrinsic dynamics. This feature is crucial for evaluating the scalability of RL algorithms for control. This project serves the learning for dynamics & control (L4DC) community, aiming to explore key questions: the convergence of RL algorithms in learning control policies; the stability and robustness issues of learning-based controllers; and the scalability of RL algorithms to high- and potentially infinite-dimensional systems. We open-source the controlgym project at

## Introduction

The intersection of machine learning (ML), reinforcement learning (RL), and control theory has garnered significant attention in recent years, giving rise to the learning for dynamics & control (L4DC) research community (Recht Vamvoudakis et al. Brunke et al. Hu et al., ). L4DC has the naturally driven mission to unlock the power of learning-based methods for control and establish a rigorous theoretical foundation. This mission could only be fulfilled with joint forces and close collaboration between theorists and practitioners from ML, control theory, and optimization.

Theorists are keen to validate their algorithms and theories in real-world scenarios but encounter challenges with OpenAI Gym/Gymnasium (Gym) environments (Brockman et al. Towers et al., ). Specifically, most Gym environments feature highly nonlinear dynamics, often involving contacts, and offer very limited parameter customization options, making them ill-suited testbeds for control theory research. Meanwhile, control textbook examples lack the complexity for cutting-edge ML/RL research that prioritizes efficiency and scalability.

We have presented controlgym, a library designed to support the research efforts of L4DC. The controlgym project facilitates a deeper investigation into the performance of RL algorithms, particularly focusing on their convergence, the stability and robustness of RL-based controllers, and the scalability of RL algorithms to systems with high and infinite state dimensionality.

The research of XZ, WM, and TB were supported in part by the US Army Research Laboratory (ARL) Cooperative Agreement W911NF-17-2-0181, in part by the Army Research Office (ARO) MURI Grant AG285, and in part by the ARO Grant W911NF-24-1-0085. SM and MB were supported solely by MERL.

Figure 4: The uncontrolled solution to the wave equation in a domain of length L = 1 with parameter c = 0.1. The initial conditions are u(x, t=0) = sech(10x−5) and ψ(x, t=0) = 0. The figure convention is consistent with that of Figure 3.

Discretization of space and time. To solve the PDEs listed in Table, we first need to discretize space and time in the continuous form (2.1). For a state dimension $n_{s}$ that is even and a sampling time ${\Delta t} \in {\mathbb{R}}^{+}$, both selected by the user, we define a state vector $s_{k} \in {\mathbb{R}}^{n_{s}}$ that contains the values of $u$ at...
