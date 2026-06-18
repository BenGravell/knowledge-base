Learning Interactive Driving Policies via Data-driven Simulation

Topics include Autonomous driving, Data-driven simulation, Multi-agent interaction, Policy learning, Sim-to-real transfer, Inpainting.

Companion paper to VISTA 2.0 that extends data-driven simulation to multi-agent scenarios by inpainting other vehicles into real-world footage, enabling interactive driving policy learning that transfers directly to a full-scale autonomous vehicle.

Data-driven simulators promise high data-efficiency for driving policy learning. When used for modelling interactions, this data-efficiency becomes a bottleneck: Small underlying datasets often lack interesting and challenging edge cases for learning interactive driving. We address this challenge by proposing a simulation method that uses in-painted ado vehicles for learning robust driving policies. Thus, our approach can be used to learn policies that involve multi-agent interactions and allows for training via state-of-the-art policy learning methods. We evaluate the approach for learning standard interaction scenarios in driving. In extensive experiments, our work demonstrates that the resulting policies can be directly transferred to a full-scale autonomous vehicle without making use of any traditional sim-to-real transfer techniques such as domain randomization.

## Introduction

Intelligent agents can achieve complex continuous control and decision making in the presence of rich multi-agent interactions as well as diverse lighting and environmental conditions. This ability requires learning representations from raw perception to high-level control actions. The interactive multi-agent case is challenging for autonomous navigation. End-to-end policy learning has demonstrated great promise for lane-stable single-agent navigation....

End-to-end learning of multi-agent visual control policies will increase the abilities of autonomous agents to reason and make decisions about how to move in interactive environments. End-to-end imitation learning requires capturing expert training data from extensive edge cases, such as recovery from off-orientation positions or near collisions with other agents. This is prohibitively expensive and dangerous for interactive situations. Simulation presents a solution to efficiently training and testing autonomous agents before deploying them in the real-world....

## Conclusion

In this paper, we present a novel method to learn an end-to-end controller using multi-agent data-driven simulation for autonomous driving. We propose several multi-agent tasks with increasing levels of complexity and conduct extensive empirical analysis within simulation as well as the real-world, where our learned policy is deployed onboard a full-scale autonomous vehicle. By leveraging photorealistic simulation we drastically reduce the amount of data required by our agent to learn a transferable policy....

For car following, we can simply adapt the lane reward by changing the center line to the trajectory traced out by the front car. In overtaking, additional to lane reward, we define a pass reward based on comparing the distances traced out by both cars,

### III-A Data-driven Simulation and Learning Environment

Evaluation metric. We follow two types of evaluation protocols: online active test and offline active test. Online test runs end-to-end control policies on physical full-scale autonomous vehicle, while offline test runs policies in the simulator. These tests examine the transferability from our photorealistic simulator to real-world. Active (i.e....
