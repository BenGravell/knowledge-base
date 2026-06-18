CARLA: An Open Urban Driving Simulator

Topics include Reinforcement learning, Imitation learning, Autonomous driving, Vehicles, Control, Learning, CARLA, Open source, Driving simulator, Source code.

We introduce CARLA, an open-source simulator for autonomous driving research. CARLA has been developed from the ground up to support development, training, and validation of autonomous urban driving systems. In addition to open-source code and protocols, CARLA provides open digital assets (urban layouts, buildings, vehicles) that were created for this purpose and can be used freely. The simulation platform supports flexible specification of sensor suites and environmental conditions. We use CARLA to study the performance of three approaches to autonomous driving: a classic modular pipeline, an end-to-end model trained via imitation learning, and an end-to-end model trained via reinforcement learning. The approaches are evaluated in controlled scenarios of increasing difficulty, and their performance is examined via metrics provided by CARLA, illustrating the platform's utility for autonomous driving research. The supplementary video can be viewed at

## Introduction

Sensorimotor control in three-dimensional environments remains a major challenge in machine learning and robotics. The development of autonomous ground vehicles is a long-studied instantiation of this problem. Its most difficult form is navigation in densely populated urban environments. This setting is particularly challenging due to complex multi-agent dynamics at traffic intersections; the necessity to track and respond to the motion of tens or hundreds of other actors that may be in view at any given time; prescriptive traffic rules that necessitate recognizing street signs, street lights, and road markings and distinguishing between...

Research in autonomous urban driving is hindered by infrastructure costs and the logistical difficulties of training and testing systems in the physical world. Instrumenting and operating even one robotic car requires significant funds and manpower. And a single vehicle is far from sufficient for collecting the requisite data that cover the multitude of corner cases that must be processed for both training and validation. This is true for classic modular pipelines and even more so for data-hungry deep learning techniques....

## Conclusion

We have presented CARLA, an open simulator for autonomous driving. In addition to open-source code and protocols, CARLA provides digital assets that were created specifically for this purpose and can be reused freely. We leverage CARLA's simulation engine and content to test three approaches to autonomous driving: a classic modular pipeline, a deep network trained end-to-end via imitation learning, and a deep network trained via reinforcement learning. We challenged these systems to navigate urban environments in the presence of other vehicles and pedestrians....

### Imitation learning

## Autonomous Driving

One turn: Destination is one turn away from the starting point; no dynamic objects. Average driving distance to the goal is 400 m in Town 1 and 170 m in Town 2.

An alternative is to train and validate driving strategies in simulation. Simulation can democratize research in autonomous urban driving. It is also necessary for system verification, since some scenarios are too dangerous to be staged in the physical world (e.g., a child running onto the road ahead of the car)....
