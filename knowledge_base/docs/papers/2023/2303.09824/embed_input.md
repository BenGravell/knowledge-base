Motion Planning for Autonomous Driving: The State of the Art and Future Perspectives

Topics include Survey, Motion planning, Autonomous driving, End-to-end planning, Pipeline planning, Deep learning, Intelligent vehicles.

Surveys both pipeline-based and end-to-end motion planning approaches for autonomous driving, analyzing selection, expansion, and optimization in classical methods alongside deep learning training strategies for end-to-end systems, with experimental comparisons and future challenges.

Intelligent vehicles (IVs) have gained worldwide attention due to their increased convenience, safety advantages, and potential commercial value. Despite predictions of commercial deployment by 2025, implementation remains limited to small-scale validation, with precise tracking controllers and motion planners being essential prerequisites for IVs. This article reviews state-of-the-art motion planning methods for IVs, including pipeline planning and end-to-end planning methods. The study examines the selection, expansion, and optimization operations in a pipeline method, while it investigates training approaches and validation scenarios for driving tasks in end-to-end methods. Experimental platforms are reviewed to assist readers in choosing suitable training and validation strategies. A side-by-side comparison of the methods is provided to highlight their strengths and limitations, aiding system-level design choices. Current challenges and future perspectives are also discussed in this survey.

## Introduction

Intelligent vehicles (IVs) have attracted significant interest from governments, industries, academia, and the public, owing to their potential to transform transportation through advances in artificial intelligence and computer hardware. The deployment of IVs holds great promise for reducing road accidents and alleviating traffic congestion, thereby improving mobility in densely populated urban areas. Despite remarkable contributions by leading experts in the field, IVs remain primarily confined to limited trial programs due to concerns about their reliability and safety.

## I-A Background

The pipeline planning method, also known as the rule-based planning method, is a well-established category of planners. As depicted in 1a, this method serves as a core component of the pipeline framework and must be integrated with other methods, such as perception, localization, and control, to accomplish autonomous driving tasks. A significant advantage of the pipeline framework is its interpretability, enabling the identification of defective modules when malfunctions or unexpected system behavior occur. In Section-LABEL:ppl, the focus is solely on the planning method within the pipeline framework.

The end-to-end planning method, also known as the learning-based approach, is the sole component in the end-to-end framework and has become a trend in autonomous vehicle research. As illustrated in 1b, the entire driving framework is treated as a single machine learning task that converts raw perception data into control commands. The driving model acquires knowledge through imitation learning, develops driving policies through reinforcement learning, and continuously self-optimizes via parallel learning. Despite its appealing concept, determining the reasons for model misbehavior can be challenging.

## I-B Comparison

In this subsection, we provide a concise overview of the distinctions between pipeline and end-to-end methods, particularly highlighting their respective advantages and disadvantages.
