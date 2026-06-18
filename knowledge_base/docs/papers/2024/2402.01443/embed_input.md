FRENETIX: A High-Performance and Modular Motion Planning Framework for Autonomous Driving

Topics include Motion planning, Frenet frame, Autonomous driving, Modular, High performance, CommonRoad.

Introduces FRENETIX, a high-performance and modular motion planning framework for autonomous driving built around Frenet-frame trajectory sampling. Features a Python/C++ implementation with CommonRoad compatibility, achieving real-time performance through parallelized sampling and efficient trajectory evaluation.

Our research introduces a modular motion planning framework for autonomous vehicles using a sampling-based trajectory planning algorithm. This approach effectively tackles the challenges of solution space construction and optimization in path planning. The algorithm is applicable to both real vehicles and simulations, offering a robust solution for complex autonomous navigation. Our method employs a multi-objective optimization strategy for efficient navigation in static and highly dynamic environments, focusing on optimizing trajectory comfort, safety, and path precision. The algorithm is used to analyze the algorithm performance and success rate in 1750 virtual complex urban and highway scenarios. Our results demonstrate fast calculation times (8ms for 800 trajectories), a high success rate in complex scenarios (88%), and easy adaptability with different modules presented. The most noticeable difference exhibited was the fast trajectory sampling, feasibility check, and cost evaluation step across various trajectory counts. We demonstrate the integration and execution of the framework on real vehicles by evaluating deviations from the controller using a test track.

## Introduction

With its promise of revolutionizing transportation, autonomous driving technology faces significant real-world challenges brought to light through various collision reports and practical experiences. Among these challenges are the complexities of urban navigation, the unpredictability of traffic and pedestrian behavior, and the necessity for rapid, informed decision-making in ever-changing environments. These factors underscore the importance of high-performance and adaptable trajectory planning algorithms in autonomous vehicles (AVs) (Fig. 1).

We present a publicly available sampling-based trajectory planner for AVs called FRENETIX, employing a multi-objective optimization strategy for efficient navigation in complex environments, focusing on optimizing trajectory comfort, safety, and path precision. Unlike anything available before, we offer an out-of-the-box method integrated into the simulation environment with a wide variety of scenarios.

We provide a modular approach to improve adaptability and scalability, allowing for easy integration and optimal functionality of each component within the system, catering to a wide range of scenarios.

## Discussion

The results from our study indicate that the FRENETIX algorithm presented is effective in rapidly finding a safe and reliable trajectory in dynamic environments. The algorithm's modular structure allows for quickly adapting and integrating new features and modules. However, it is essential to note that specific settings and parameters influence the algorithm's performance, which is consistent with expectations for an analytical algorithm. During our research, collisions and other issues were mainly attributed to the lack of features for specific scenarios or inadequate parameter tuning.

## Conclusion & Outlook

In this paper, we introduced FRENETIX, a high-performance and modular sampling-based trajectory planner algorithm for autonomous driving applications We propose a composition of multiple steps and methods to create a trajectory planner that runs computationally efficiently. Therefore, FRENETIX is characterized by its robustness, adaptability, and ability to effectively handle complex scenarios. The modular approach and presented cost functions allow different prioritizations of the driving behavior by adapting the cost weights.
