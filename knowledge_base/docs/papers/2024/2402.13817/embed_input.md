Khronos: A Unified Approach for Spatio-Temporal Metric-Semantic SLAM in Dynamic Environments

Topics include Robotics, Graphs, Real-time systems, Khronos, Spatio-temporal, Metric-semantic simultaneous localization and mapping, SMS.

Perceiving and understanding highly dynamic and changing environments is a crucial capability for robot autonomy. While large strides have been made towards developing dynamic SLAM approaches that estimate the robot pose accurately, a lesser emphasis has been put on the construction of dense spatio-temporal representations of the robot environment. A detailed understanding of the scene and its evolution through time is crucial for long-term robot autonomy and essential to tasks that require long-term reasoning, such as operating effectively in environments shared with humans and other agents and thus are subject to short and long-term dynamics. To address this challenge, this work defines the Spatio-temporal Metric-semantic SLAM (SMS) problem, and presents a framework to factorize and solve it efficiently. We show that the proposed factorization suggests a natural organization of a spatio-temporal perception system, where a fast process tracks short-term dynamics in an active temporal window, while a slower process reasons over long-term changes in the environment using a factor graph formulation.

## Introduction

In order to operate safely and effectively in human-populated environments, a robot needs to have a sufficient understanding of the world around it. Such shared spaces are often highly dynamic, with people, robots, and other entities constantly moving, interacting, and modifying the scene. For a robot to operate in such circumstances, it is not sufficient to build a world model just for a single snapshot in time. Instead, the robot should be also able to reason over the state of the scene at past times, inferring how the scene might have changed across multiple observations.

To this end, we introduce the *Spatio-temporal Metric-semantic SLAM* (SMS) problem, which aims at building a dense metric-semantic model of the world at all times incrementally as the robot navigates the scene. We present a unified framework to tackle the SMS problem. The central idea of our approach is to develop a new factorization of the SMS problem based on spatio-temporal local consistency, which allows for the disentanglement of errors arising from sensing noise, state estimation errors, dynamic objects, and long-term changes in the scene.

We propose a novel factorization of the SMS problem, which provides a unifying lens for existing interpretations focusing on short-term and long-term dynamics.

We present Khronos, the first spatio-temporal metric-semantic perception system, composed of novel algorithms for asynchronous local mapping and deformable global change detection.

## Limitations

Since Khronos utilizes the bounding-box centroid as the position of a fragment for association edges, accurate fragment associations can be sensitive to partial observations and occlusions. Furthermore, the lack of 6D registration between fragments decreases the effectiveness of global estimation and reconciliation. Adoption of modern object pose and shape estimation and registration techniques would increase the robustness and accuracy of fragment association.

Second, we currently only associate fragments geometrically, meaning that fragments that have moved are not associated. Incorporating fragment descriptors would allow reasoning about the history of moving objects in more detail.
