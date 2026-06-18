DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset

Topics include Robotics, Safety, Robustness, Datasets, Distributed systems, Generalization, Learning, DROID.

The creation of large, diverse, high-quality robot manipulation datasets is an important stepping stone on the path toward more capable and robust robotic manipulation policies. However, creating such datasets is challenging: collecting robot manipulation data in diverse environments poses logistical and safety challenges and requires substantial investments in hardware and human labour. As a result, even the most general robot manipulation policies today are mostly trained on data collected in a small number of environments with limited scene and task diversity. In this work, we introduce DROID (Distributed Robot Interaction Dataset), a diverse robot manipulation dataset with 76k demonstration trajectories or 350 hours of interaction data, collected across 564 scenes and 84 tasks by 50 data collectors in North America, Asia, and Europe over the course of 12 months. We demonstrate that training with DROID leads to policies with higher performance and improved generalization ability. We open source the full dataset, policy learning code, and a detailed guide for reproducing our robot hardware setup.

## Introduction

^††^footnotetext: Affiliations: ^1^Stanford University; ^2^University of California, Berkeley; ^3^Toyota Research Institute; ^4^Carnegie Mellon University; ^5^University of Texas, Austin; ^6^University of Montreal; ^7^University of Edinburgh; ^8^Princeton University; ^9^University of Washington; ^10^Korea Advanced Institute of Science & Technology (KAIST); ^11^University of California, San Diego; ^12^Google DeepMind; ^13^University of California, Davis; ^14^University of Pennsylvania; ^15^Columbia University; ^16^Yonsei University

## Traj
## Verbs
## Scenes

In this work, we introduced DROID (Distributed Robot Interaction Dataset), a new robot manipulation dataset with a large diversity of scenes, tasks, objects and viewpoints. Our dataset analysis in Section IV showed that DROID has an order of magnitude larger scene diversity than existing large robot manipulation datasets, a wide range of tasks, many interaction objects, and diverse viewpoints. Our policy learning evaluations show that DROID is a valuable data resource for improving policy performance and robustness, even in comparison to existing large robot data sources like the Open X-Embodiment dataset \[\].

We hope that DROID can be a catalyst for research on general-purpose robot manipulation policies that are able to generalize to a broad range of tasks and scenes. In this work, we showed one example for leveraging DROID to boost policy performance, but there are many open questions about how to best make use of such diverse data: how should we combine DROID with existing large-scale robot datasets and how can we train policies that perform tasks in new scenes without *any* in-domain data? Can the diverse interaction data in DROID be used to learn better visual representations for robotic control?...

### Scene diversity

Our dataset is collected by 50 data collectors across various research institutions. A shared data collection protocol helps streamline data collection, particularly for inexperienced data collectors. When designing the collection protocol for DROID, we focused on the following objectives: preventing common data collection mistakes like "camera cannot see robot" or "teleoperator in camera view", encouraging collection of diverse data, allowing data collectors to creatively choose scenes and tasks.
