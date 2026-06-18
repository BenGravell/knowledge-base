Trends in Motion Prediction Toward Deployable and Generalizable Autonomy: A Revisit and Perspectives

Topics include Motion prediction, Autonomous driving, Survey, Taxonomy, Generalization, Deployment.

Surveys the state-of-the-art in motion prediction for autonomous driving with a focus on real-world deployability and generalization, providing a taxonomy of approaches and discussing open challenges for bringing prediction models from research to production.

Motion prediction, recently popularized as world models, refers to the anticipation of future agent states or scene evolution, which is rooted in human cognition, bridging perception and decision-making. It enables intelligent systems, such as robots and self-driving cars, to act safely in dynamic, human-involved environments, and informs broader time-series reasoning challenges. With advances in methods, representations, and datasets, the field has seen rapid progress, reflected in quickly evolving benchmark results. Yet, when state-of-the-art methods are deployed in the real world, they often struggle to generalize to open-world conditions and fall short of deployment standards. This reveals a gap between research benchmarks, which are often idealized or ill-posed, and real-world complexity. To address this gap, this survey revisits the generalization and deployability of motion prediction models, with an emphasis on applications of robotics, autonomous driving, and human motion. We first offer a comprehensive taxonomy of motion prediction methods, covering representations, modeling strategies, application domains, and evaluation protocols.

## Problem Formulation

The

## Introduction to the Autonomy Stack

Input Modalities. As shown in Fig 15, autonomous systems collect the environmental information from sensors, such as multi-view camera images, LiDAR points, or both. Less common modalities also include radar, which is robust to various weather and lighting conditions, and event cameras, which capture changes in the scene at a much higher temporal resolution than traditional cameras. As additional inputs, some methods may rely on offline constructed HD maps as input to the model for additional environment context. In contrast, other methods may create the map online as a perception task using real-time sensor inputs.

Inter-Module Representations. In Figure 6 and Section 2.1.2, we introduced and reviewed five common types of motion prediction representations.

## Conclusion

In this survey, we revisited motion prediction---a cornerstone of intelligent autonomy---from the dual perspectives of deployability and generalizability, two critical yet under-explored dimensions for real-world adoption. While remarkable progress has been made in existing benchmarks, many state-of-the-art approaches still fall short when integrated into deployed systems or faced with open-world variability. This gap underscores the importance of rethinking problem formulations, modeling assumptions, and evaluation protocols to bridge the divide between academic progress and practical utility.

We began with a comprehensive taxonomy (Section 2) of motion prediction methods, spanning representation choices, modeling paradigms, domain-specific applications, and evaluation strategies. This provided foundational clarity to analyze how current practices map---or fail to map---to real-world demands. In Section 3, we focused on deployability, dissecting the role of motion prediction within closed-loop autonomy stacks. We highlighted key issues such as interface mismatches between modules, the neglect of uncertainty propagation, and evaluation schemes that fail to capture full-system performance.
