Controlgym: Large-Scale Control Environments for Benchmarking Reinforcement Learning Algorithms

Topics include Reinforcement learning, Stability analysis, Robustness, Benchmarks, Scalability, Control, Learning, Controlgym, Partial differential equation, L4DC.

We introduce controlgym, a library of thirty-six industrial control settings, and ten infinite-dimensional partial differential equation (PDE)-based control problems. Integrated within the OpenAI Gym/Gymnasium (Gym) framework, controlgym allows direct applications of standard reinforcement learning (RL) algorithms like stable-baselines3. Our control environments complement those in Gym with continuous, unbounded action and observation spaces, motivated by real-world control applications. Moreover, the PDE control environments uniquely allow the users to extend the state dimensionality of the system to infinity while preserving the intrinsic dynamics. This feature is crucial for evaluating the scalability of RL algorithms for control. This project serves the learning for dynamics & control (L4DC) community, aiming to explore key questions: the convergence of RL algorithms in learning control policies; the stability and robustness issues of learning-based controllers; and the scalability of RL algorithms to high- and potentially infinite-dimensional systems. We open-source the controlgym project at

## Introduction

The intersection of machine learning (ML), reinforcement learning (RL), and control theory has garnered significant attention in recent years, giving rise to the learning for dynamics & control (L4DC) research community (Recht Vamvoudakis et al. Brunke et al. Hu et al., ). L4DC has the naturally driven mission to unlock the power of learning-based methods for control and establish a rigorous theoretical foundation. This mission could only be fulfilled with joint forces and close collaboration between theorists and practitioners from ML, control theory, and optimization.

To address these requirements, we introduce controlgym, a lightweight and versatile Python library that offers a spectrum of environments spanning from linear systems to chaotic, large-scale systems governed by partial differential equations (PDEs). Specifically, controlgym features thirty-six linear industrial control environments, encompassing sectors like aerospace, cyber-physical systems, ground and underwater vehicles, and power systems. Additionally, controlgym includes ten large-scale control environments governed by fundamental PDEs in fluid dynamics and physics.

Leveraging its strengths, controlgym is a testbed for exploring three essential aspects of applying RL to continuous control. First, it aims to probe whether RL algorithms can consistently converge in learning control policies. Second, it examines the stability and robustness of the policy and training process, motivated by real-world safety-critical applications. Lastly, it assesses the scalability of RL algorithms in high-dimensional and potentially infinite-dimensional systems.

## Conclusion

We have presented controlgym, a library designed to support the research efforts of L4DC. The controlgym project facilitates a deeper investigation into the performance of RL algorithms, particularly focusing on their convergence, the stability and robustness of RL-based controllers, and the scalability of RL algorithms to systems with high and infinite state dimensionality.

The research of XZ, WM, and TB were supported in part by the US Army Research Laboratory (ARL) Cooperative Agreement W911NF-17-2-0181, in part by the Army Research Office (ARO) MURI Grant AG285, and in part by the ARO Grant W911NF-24-1-0085. SM and MB were supported solely by MERL.
