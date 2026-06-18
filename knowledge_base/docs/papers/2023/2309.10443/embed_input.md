Rethinking Imitation-Based Planner for Autonomous Driving

Topics include Autonomous driving, Imitation learning, Behavior cloning, End-to-end planning, Closed-loop.

Studies design choices for imitation-based planners on nuPlan and distills the findings into PlanTF, a strong pure-imitation baseline. The paper is useful because it separates benchmark, feature, augmentation, and compounding-error effects that are often bundled together in end-to-end driving claims.

In recent years, imitation-based driving planners have reported considerable success. However, due to the absence of a standardized benchmark, the effectiveness of various designs remains unclear. The newly released nuPlan addresses this issue by offering a large-scale real-world dataset and a standardized closed-loop benchmark for equitable comparisons. Utilizing this platform, we conduct a comprehensive study on two fundamental yet underexplored aspects of imitation-based planners: the essential features for ego planning and the effective data augmentation techniques to reduce compounding errors. Furthermore, we highlight an imitation gap that has been overlooked by current learning systems. Finally, integrating our findings, we propose a strong baseline model-PlanTF. Our results demonstrate that a well-designed, purely imitation-based planner can achieve highly competitive performance compared to state-of-the-art methods involving hand-crafted rules and exhibit superior generalization capabilities in long-tail cases. Our models and benchmarks are publicly available. Project website

## Introduction

Learning-based planners are considered a potentially scalable solution for autonomous driving, supplanting traditional rule-based planners. This has sparked significant research interest in recent years. In particular, imitation-based planners are reported to achieve notable success in simulations and real-world scenarios. Nevertheless, these planners are predominantly trained and evaluated in diverse custom conditions (*e.g*. varying datasets, metrics, and simulation setups) owing to the absence of a standardized benchmark....

Recently, the release of the large-scale nuPlan dataset, alongside a standardized simulation benchmark, has provided a new opportunity for advancing learned motion planners. Enabled by this fresh benchmark, we conduct in-depth investigations on several common and critical yet not fully studied design choices of the learning-based planner, aiming to provide constructive suggestions for future research. This paper concentrates on two overarching and fundamental facets of the imitation-based planner: the requisite ego features for planning and the efficacious techniques of data augmentation.

Table VIII shows the ablation study on different dropout rate the of state6+SDE model.

TABLE VIII: Ablation study on the state dropout rate of the SDE.

TABLE II: Experimental results of the state dropout encoder (SDE) on -random and -hard benchmark. Models with SDE gain significant improvements on CLS while maintaining high performance on OLS.

### Metrics

### III-C The hidden imitation gap

The majority of imitation-based planning models follow the success of prediction models and inherently incorporate the past trajectory of the autonomous vehicle (AV) as an input feature, though imitation learning (IL) has frequently been noted for its tendency to acquire shortcuts from historical observations. Our research reaffirms that the past motion of the AV leads to significant closed-loop performance degradation. The planner achieves enhanced performance by solely utilizing the AV's present state. Surprisingly, it attains better closed-loop performance purely using the AV's current pose (position and heading)....

Imitation learning is also known to have compounding errors. Perturbation-based augmentations are a commonly employed strategy to instruct the planner on recovering from deviations....
