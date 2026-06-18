VISTA 2.0: An Open, Data-driven Simulator for Multimodal Sensing and Policy Learning for Autonomous Vehicles

Topics include Autonomous driving, Data-driven simulation, Sim-to-real transfer, Multimodal sensing, LiDAR, Event camera, Policy learning.

VISTA 2.0 is an open-source, data-driven simulator from MIT that synthesizes novel viewpoints from real-world data across RGB cameras, 3D LiDAR, and event-based cameras; policies trained in it transfer directly to a full-scale autonomous vehicle without domain randomization.

Simulation has the potential to transform the development of robust algorithms for mobile agents deployed in safety-critical scenarios. However, the poor photorealism and lack of diverse sensor modalities of existing simulation engines remain key hurdles towards realizing this potential. Here, we present VISTA, an open source, data-driven simulator that integrates multiple types of sensors for autonomous vehicles. Using high fidelity, real-world datasets, VISTA represents and simulates RGB cameras, 3D LiDAR, and event-based cameras, enabling the rapid generation of novel viewpoints in simulation and thereby enriching the data available for policy learning with corner cases that are difficult to capture in the physical world. Using VISTA, we demonstrate the ability to train and test perception-to-control policies across each of the sensor types and showcase the power of this approach via deployment on a full scale autonomous vehicle. The policies learned in VISTA exhibit sim-to-real transfer without modification and greater robustness than those trained exclusively on real-world data.

## Introduction

Simulation has emerged as an essential tool for advancing new algorithms in robot perception, learning, and evaluation. For safety-critical domains in particular, such as for autonomous vehicles, experience in simulation is often significantly faster and safer than direct operation in the physical world. Simulation affords the potential to rapidly synthesize novel data for training, including challenging edge cases difficult to capture in the real world. An agent's exposure to edge cases during training is critical to achieving robustness to out-of-distribution events....

Figure 1: VISTA 2.0 is an open-source data-driven simulator for multi-sensor perception of embodied agents. Leveraging data of the real-world, VISTA synthesizes ego-agent viewpoints as their dynamics unroll novel trajectories in the environment. Sensors are efficient and high fidelity for online perception learning, evaluation, and sim-to-real deployment.

## Conclusion

We present VISTA, an open-source simulator that supports multimodal sensor synthesis including 2D RGB cameras, 3D LiDAR, and event-based cameras for mobile agents. The simulator is data-driven and capable of synthesizing high-fidelity sensor measurement sufficient for policy learning and evaluation. We showcase the sim-to-real ability by directly deploying policies learned in VISTA on a full-scale autonomous vehicle for each sensor and demonstrate consistent results between closed-loop evaluation in simulation and real-world test....

Event-based cameras are asynchronous, continuous-time sensors that detect brightness changes of the scene. An event is emitted when brightness change exceeds a certain threshold at a pixel location, and is described as a 4-tuple of pixel coordinate, timestamp, and polarity. The polarity is a binary value that indicates whether brightness change is positive or negative. Conceptually, event camera can be viewed as the derivative of regular RGB camera with additional advantages of much higher operating frequency ($> {10,000}$Hz) and dynamic range....

LiDAR sensors play a central role in modern autonomy pipelines due to their accuracy in measuring geometric depth information and robustness to environmental changes like illumination. Unlike cameras which return structured grid-like images, the LiDAR sensor captures a sparse pointcloud of the environment....
