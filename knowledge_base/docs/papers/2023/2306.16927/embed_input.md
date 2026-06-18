End-to-End Autonomous Driving: Challenges and Frontiers

Topics include Autonomous driving, End-to-end planning, Surveys, Perception and planning, Closed-loop evaluation, Foundation models.

Surveys the shift from modular autonomous-driving stacks toward end-to-end systems that jointly optimize perception, prediction, and planning. The paper maps current datasets, closed-loop evaluation issues, and open frontiers, making it a good orientation point for learning-based driving planners.

The autonomous driving community has witnessed a rapid growth in approaches that embrace an end-to-end algorithm framework, utilizing raw sensor input to generate vehicle motion plans, instead of concentrating on individual tasks such as detection and motion prediction. End-to-end systems, in comparison to modular pipelines, benefit from joint feature optimization for perception and planning. This field has flourished due to the availability of large-scale datasets, closed-loop evaluation, and the increasing need for autonomous driving algorithms to perform effectively in challenging scenarios. In this survey, we provide a comprehensive analysis of more than 270 papers, covering the motivation, roadmap, methodology, challenges, and future trends in end-to-end autonomous driving. We delve into several critical challenges, including multi-modality, interpretability, causal confusion, robustness, and world models, amongst others. Additionally, we discuss current advancements in foundation models and visual pre-training, as well as how to incorporate these techniques within the end-to-end driving framework.

## Introduction

Conventional autonomous driving systems adopt a modular design strategy, wherein each functionality, such as perception, prediction, and planning, is individually developed and integrated into onboard vehicles. The planning or control module, responsible for generating steering and acceleration outputs, plays a crucial role in determining the driving experience. The most common approach for planning in modular pipelines involves using sophisticated rule-based designs, which are often ineffective in addressing the vast number of situations that occur on road.

We define end-to-end autonomous driving systems as fully differentiable programs that take raw sensor data as input and produce a plan and/or low-level control actions as output. Fig. (a)-(b) illustrates the difference between the classical and end-to-end formulation. The conventional approach feeds the output of each component, such as bounding boxes and vehicle trajectories, directly into subsequent units (dashed arrows). In contrast, the end-to-end paradigm propagates feature representations across components (gray solid arrow).

## Conclusion and Outlook

In this survey, we provide an overview of fundamental methodologies and summarize various aspects of simulation and benchmarking. We thoroughly analyze the extensive literature to date, and highlight a wide range of critical challenges and promising resolutions.

Outlook: The industry has dedicated considerable effort over the years to develop advanced modular-based systems capable of achieving self-driving on highways. However, these systems face significant challenges when confronted with complex scenarios, e.g., inner-city streets and intersections. Therefore, an increasing number of companies have started exploring end-to-end autonomous driving techniques specifically tailored for these environments.
