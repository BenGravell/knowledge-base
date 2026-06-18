Bench2Drive: Towards Multi-Ability Benchmarking of Closed-Loop End-To-End Autonomous Driving

In an era marked by the rapid scaling of foundation models, autonomous driving technologies are approaching a transformative threshold where end-to-end autonomous driving (E2E-AD) emerges due to its potential of scaling up in the data-driven manner. However, existing E2E-AD methods are mostly evaluated under the open-loop log-replay manner with L2 errors and collision rate as metrics (e.g., in nuScenes), which could not fully reflect the driving performance of algorithms as recently acknowledged in the community. For those E2E-AD methods evaluated under the closed-loop protocol, they are tested in fixed routes (e.g., Town05Long and Longest6 in CARLA) with the driving score as metrics, which is known for high variance due to the unsmoothed metric function and large randomness in the long route. Besides, these methods usually collect their own data for training, which makes algorithm-level fair comparison infeasible. To fulfill the paramount need of comprehensive, realistic, and fair testing environments for Full Self-Driving (FSD), we present Bench2Drive, the first benchmark for evaluating E2E-AD systems' multiple abilities in a closed-loop manner.

## Introduction

^††^footnotetext: This work was in part supported by by NSFC and Shanghai Municipal Science and Technology Major Project under Grant 2021SHZDZX0102.

In recent years, the field of autonomous driving has witnessed tremendous growth, fueled by the rapid advancement and scaling of foundation models. These developments have ushered in a new era of end-to-end autonomous driving (E2E-AD) systems, which promise a scalable, data-driven approach to vehicle automation, opposed to traditional module-based perception, prediction, planning pipeline. Such systems are designed to be capable of learning from vast amounts of data, potentially transforming the landscape of vehicle intelligence.

Despite these advancements, the evaluation methodologies for E2E-AD systems remain a critical bottleneck. One popular way is to conduct log-replay with the recorded expert trajectories in dataset like nuScenes, i.e., open-loop evaluation. These models usually predict the future locations of the ego vehicle with the raw sensor information as inputs. As for metrics, the L2 error relative to the recorded trajectories and the ratio of collision happening are used.

To address the aforementioned challenges in evaluating autonomous driving (AD) systems, it is essential to develop a new benchmark that fairly assesses their capabilities in a granular manner. To this end, we introduce Bench2Drive, a new benchmark designed to evaluate E2E-AD systems in a comprehensive, realistic, and fair closed-loop environment. Bench2Drive has an official training dataset collected by state-of-the-art expert model Think2Drive, comprising 2 million fully annotated frames, sourced from 13638 clips.

## Conclusion

In this work, we present Bench2Drive, a new benchmark tailed for closed-loop evaluation of end-to-end autonomous driving methods. We open source a fully-annotated large-scale dataset as the official training set and a multi-ability evaluation toolkit for the granular driving skill assessment. State-of-the-art E2E-AD methods are tested in Bench2Drive with their pros and cons evaluated, which provides insights for the future direction.

Since the rendering of simulation in CARLA has gaps compared to real world, utilizing real world datasets could be complementary as done in the concurrent work - NAVSIM.
