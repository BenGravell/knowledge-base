AgiBot World Colosseo: A Large-Scale Manipulation Platform for Scalable and Intelligent Embodied Systems

Topics include Robot manipulation, Datasets, Vision-language-action models, Generalist robot policies, Dexterous manipulation, Scalable robot data.

Introduces AgiBot World Colosseo, a large-scale manipulation dataset and platform, together with the GO-1 generalist policy trained on its trajectories. The paper is primarily a data-scaling and infrastructure contribution for embodied manipulation, with policy results showing how latent action representations can exploit the dataset.

We explore how scalable robot data can address real-world challenges for generalized robotic manipulation. Introducing AgiBot World, a large-scale platform comprising over 1 million trajectories across 217 tasks in five deployment scenarios, we achieve an order-of-magnitude increase in data scale compared to existing datasets. Accelerated by a standardized collection pipeline with human-in-the-loop verification, AgiBot World guarantees high-quality and diverse data distribution. It is extensible from grippers to dexterous hands and visuo-tactile sensors for fine-grained skill acquisition. Building on top of data, we introduce Genie Operator-1 (GO-1), a novel generalist policy that leverages latent action representations to maximize data utilization, demonstrating predictable performance scaling with increased data volume. Policies pre-trained on our dataset achieve an average performance improvement of 30% over those trained on Open X-Embodiment, both in in-domain and out-of-distribution scenarios. GO-1 exhibits exceptional capability in real-world dexterous and long-horizon tasks, achieving over 60% success rate on complex tasks and outperforming prior RDT approach by 32%....

## Introduction

Manipulation is a cornerstone task in robotics, enabling the agent to interact with and adapt to the physical world. While significant progress has been made in general-purpose foundational models for natural language processing \[\] and computer vision \[\], robotics lags behind due to the difficulty of (high-quality) data collection. In the controlled lab setting, simple tasks such as pick-and-place have been well studied. Yet for the open-set real-world setting, tasks spanning from fine-grained object interaction, mobile manipulation to collaborative tasks, remains a formidable challenge \[\]....

Recent efforts, such as Open X-Embodiment (OXE) \[\], have addressed by aggregating and standardizing existing datasets. Despite advancements on large-scale cross-embodiment learning, the resulting policy is constrained within naive, short-horizon tasks and can weakly generalize to out-of-domain scenarios \[\]. DROID \[\] collected expert data through crowd-sourcing from diverse real-life scenes. The absence of data quality assurance (with human feedback) and the reliance on a constrained hardware setup (i.e., featuring fixed, single-arm robots), limit its real-world applicability and broader effectiveness. More recently, Lin et al....

## Conclusion

We introduce AgiBot World, an open-source ecosystem aimed at democratizing access to large-scale, high-quality robot learning datasets. It is complete with toolchains and foundation models to advance embodied general intelligence through community collaboration. Our dataset distinguishes itself through unparalleled scale, diversity, and quality, underpinned by carefully crafted tasks. Policy learning evaluations confirm AgiBot World's value in enhancing performance and generalizability. To further explore its impact, we develop GO-1, a generalist policy utilizing latent actions for web-scale pre-training....

To effectively utilize our high-quality AgiBot World dataset and enhance the policy's generalizability, we propose a hierarchical Vision-Language-Latent-Action (ViLLA) framework with three training stages, as depicted in Fig. 4. Compared to Vision-Language-Action (VLA) model where action is vision-language conditioned, the ViLLA model predicts latent action tokens, conditioned on the generation of subsequent robot control actions.

### III-B Data Collection: Protocol and Quality
