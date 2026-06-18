Motion Planning for Autonomous Driving: The State of the Art and Future Perspectives

Topics include Survey, Motion planning, Autonomous driving, End-to-end planning, Pipeline planning, Deep learning, Intelligent vehicles.

Surveys both pipeline-based and end-to-end motion planning approaches for autonomous driving, analyzing selection, expansion, and optimization in classical methods alongside deep learning training strategies for end-to-end systems, with experimental comparisons and future challenges.

Intelligent vehicles (IVs) have gained worldwide attention due to their increased convenience, safety advantages, and potential commercial value. Despite predictions of commercial deployment by 2025, implementation remains limited to small-scale validation, with precise tracking controllers and motion planners being essential prerequisites for IVs. This article reviews state-of-the-art motion planning methods for IVs, including pipeline planning and end-to-end planning methods. The study examines the selection, expansion, and optimization operations in a pipeline method, while it investigates training approaches and validation scenarios for driving tasks in end-to-end methods. Experimental platforms are reviewed to assist readers in choosing suitable training and validation strategies. A side-by-side comparison of the methods is provided to highlight their strengths and limitations, aiding system-level design choices. Current challenges and future perspectives are also discussed in this survey.

## Introduction

Intelligent vehicles (IVs) have attracted significant interest from governments, industries, academia, and the public, owing to their potential to transform transportation through advances in artificial intelligence and computer hardware. The deployment of IVs holds great promise for reducing road accidents and alleviating traffic congestion, thereby improving mobility in densely populated urban areas. Despite remarkable contributions by leading experts in the field, IVs remain primarily confined to limited trial programs due to concerns about their reliability and safety....

### I-A Background

Reliability: One critical bottleneck that impedes the development and deployment of IVs is the prohibitively high economic and time costs required to validate their reliability. Constructing an artificial-intelligence-based algorithm that can identify the corner cases in a short time is a key direction for the validation of IVs.

Governance: IV is not only a technical issue, the sound policy is also crucial. Designing a framework that includes safety standards, data privacy regulations, and ethical guidelines is necessary to govern the development and deployment of IVs. This framework will promote accountability and transparency, reduce risks, and ensure that the public interest is defended.

End-to-end stands for the direct mapping from raw sensor data into trajectory points or control signals. Because of its ability to extract task-specific policies, it has achieved great success in a variety of fields. Compared with the pipeline method, there is no external gap between the perception and control modules, and seldom human-customized heuristics are embedded, so the end-to-end method deals with vehicle-environment interactions more efficiently. End-to-end has a higher ceiling, with the potential to achieve expert performance in the autonomous driving field....

In Section LABEL:ppl, pipeline planning methods are reviewed, including global route planning and local behavior/trajectory planning, with a particular focus on the expansion and optimization mechanisms. In Section II, end-to-end planning methods are examined, encompassing imitation learning, reinforcement learning, and parallel learning, while exploring network architecture, generalizability, robustness, and validation & verification methods....
