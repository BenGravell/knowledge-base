Learning Interactive Driving Policies via Data-driven Simulation

Topics include Autonomous driving, Data-driven simulation, Multi-agent interaction, Policy learning, Sim-to-real transfer, Inpainting.

Companion paper to VISTA 2.0 that extends data-driven simulation to multi-agent scenarios by inpainting other vehicles into real-world footage, enabling interactive driving policy learning that transfers directly to a full-scale autonomous vehicle.

Data-driven simulators promise high data-efficiency for driving policy learning. When used for modelling interactions, this data-efficiency becomes a bottleneck: Small underlying datasets often lack interesting and challenging edge cases for learning interactive driving. We address this challenge by proposing a simulation method that uses in-painted ado vehicles for learning robust driving policies. Thus, our approach can be used to learn policies that involve multi-agent interactions and allows for training via state-of-the-art policy learning methods. We evaluate the approach for learning standard interaction scenarios in driving. In extensive experiments, our work demonstrates that the resulting policies can be directly transferred to a full-scale autonomous vehicle without making use of any traditional sim-to-real transfer techniques such as domain randomization.

## Introduction

Intelligent agents can achieve complex continuous control and decision making in the presence of rich multi-agent interactions as well as diverse lighting and environmental conditions. This ability requires learning representations from raw perception to high-level control actions. The interactive multi-agent case is challenging for autonomous navigation. End-to-end policy learning has demonstrated great promise for lane-stable single-agent navigation.

In this paper, we present an end-to-end framework for photorealistic simulation and training of autonomous agents in the presence of both static and dynamic agent interactions. Our training environment is photorealistic and supports high-fidelity rendering of multiple agents such that ego-agent learned control policies can be directly transferred onboard a full-scale autonomous vehicle in the real world, without requiring any degree of domain randomization, augmentation, or fine-tuning.

By simulating arbitrary agent interactions, we do not require massive amounts of expert training data and dense supervisory signals, which are two common limitations of existing imitation learning approaches. Furthermore, by formulating training as a reinforcement learning (RL) problem, we allow the ego agent to autonomously explore the virtual environment and learn to recover from out-of-distribution edge cases and near collisions. We extensively evaluate our method through closed-loop deployment on challenging real-world environments and agents not previously encountered during training.

## Conclusion

In this paper, we present a novel method to learn an end-to-end controller using multi-agent data-driven simulation for autonomous driving. We propose several multi-agent tasks with increasing levels of complexity and conduct extensive empirical analysis within simulation as well as the real-world, where our learned policy is deployed onboard a full-scale autonomous vehicle. By leveraging photorealistic simulation we drastically reduce the amount of data required by our agent to learn a transferable policy.
