Khronos: A Unified Approach for Spatio-Temporal Metric-Semantic SLAM in Dynamic Environments

Topics include Robotics, Graphs, Real-time systems, Khronos, Spatio-temporal, Metric-semantic simultaneous localization and mapping, SMS.

Perceiving and understanding highly dynamic and changing environments is a crucial capability for robot autonomy. While large strides have been made towards developing dynamic SLAM approaches that estimate the robot pose accurately, a lesser emphasis has been put on the construction of dense spatio-temporal representations of the robot environment. A detailed understanding of the scene and its evolution through time is crucial for long-term robot autonomy and essential to tasks that require long-term reasoning, such as operating effectively in environments shared with humans and other agents and thus are subject to short and long-term dynamics. To address this challenge, this work defines the Spatio-temporal Metric-semantic SLAM (SMS) problem, and presents a framework to factorize and solve it efficiently. We show that the proposed factorization suggests a natural organization of a spatio-temporal perception system, where a fast process tracks short-term dynamics in an active temporal window, while a slower process reasons over long-term changes in the environment using a factor graph formulation....

## Introduction

In order to operate safely and effectively in human-populated environments, a robot needs to have a sufficient understanding of the world around it. Such shared spaces are often highly dynamic, with people, robots, and other entities constantly moving, interacting, and modifying the scene. For a robot to operate in such circumstances, it is not sufficient to build a world model just for a single snapshot in time. Instead, the robot should be also able to reason over the state of the scene at past times, inferring how the scene might have changed across multiple observations....

Metric-semantic simultaneous localization and mapping (SLAM) \[\] allows a robot to construct a semantically annotated geometric representation of a scene in real-time. Geometric information is critical for robots to navigate safely and to manipulate objects, while semantic information provides the understanding for a robot to execute human instructions and to provide humans with models of the environment that are easy to understand....

## Conclusions

In this paper, we defined the SMS problem and presented a novel approach to structure the problem, unifying the tracking of short-term dynamics and the detection of long-term changes in a single formulation We introduced Khronos, a first metric-semantic spatio-temporal perception system capable of solving the SMS problem and generate a dense 4D spatio-temporal map. We demonstrated that Khronos outperforms recent baselines across metrics pertaining to short and long-term dynamics, can interface with different semantic object formulations, and solve the complex SMS problem in real-time with limited compute....

Hence, the edges of the final deformation graph consist of *observed* edges $\mathcal{E}_{obs} = {\mathcal{E}_{XX} \cup \mathcal{E}_{P_{M}P_{M}} \cup \mathcal{E}_{XP_{M}} \cup \mathcal{E}_{XY}}$, and *candidate* edges $\mathcal{E}_{can} = {\mathcal{E}_{YY} \cup \mathcal{E}_{LC}}$, thus $\mathcal{E} = {\mathcal{E}_{obs} \cup \mathcal{E}_{can}}$. An overview of this is shown in Fig.. The estimates of the robot poses, fragment positions, and the background mesh is then obtained by finding a solution $\mathcal{T} = {X \cup P_{M} \cup T_{WY}}$ of the robust pose graph optimization problem:

Since for a single object $O_{i}$, all relevant information is captured in their respective segments ${\overline{Y}}_{i}...
