Trends in Motion Prediction Toward Deployable and Generalizable Autonomy: A Revisit and Perspectives

Topics include Motion prediction, Autonomous driving, Survey, Taxonomy, Generalization, Deployment.

Surveys the state-of-the-art in motion prediction for autonomous driving with a focus on real-world deployability and generalization, providing a taxonomy of approaches and discussing open challenges for bringing prediction models from research to production.

Motion prediction, recently popularized as world models, refers to the anticipation of future agent states or scene evolution, which is rooted in human cognition, bridging perception and decision-making. It enables intelligent systems, such as robots and self-driving cars, to act safely in dynamic, human-involved environments, and informs broader time-series reasoning challenges. With advances in methods, representations, and datasets, the field has seen rapid progress, reflected in quickly evolving benchmark results. Yet, when state-of-the-art methods are deployed in the real world, they often struggle to generalize to open-world conditions and fall short of deployment standards. This reveals a gap between research benchmarks, which are often idealized or ill-posed, and real-world complexity. To address this gap, this survey revisits the generalization and deployability of motion prediction models, with an emphasis on applications of robotics, autonomous driving, and human motion. We first offer a comprehensive taxonomy of motion prediction methods, covering representations, modeling strategies, application domains, and evaluation protocols....

## Introduction

### Background

When intelligent autonomous systems are deployed in real-world environments, they have to coexist and interact with other users of those spaces. This is true for self-driving cars interacting with vehicles and pedestrians on public roads, and for robots collaborating with humans in settings such as manufacturing or home assistance. To understand the surroundings and make efficient and safe decisions, these systems need to observe, reason about, and predict the future motion of other space users and the future evolution of the scene....

Throughout each section and chapter, we provide perspectives and insights, and highlight future challenges. We emphasized that prediction within autonomy stacks requires more than just accuracy---it must feature well-defined interfaces, compatible learning signals, and an awareness of both upstream inputs and downstream requirements. Similarly, generalization should be treated as a primary objective. It is not simply a byproduct of scale, but a property that must be explicitly pursued through deliberate design....

By bringing deployability and generalizability to the forefront, we hope this survey serves as a roadmap for the next phase of motion prediction research---one that moves beyond idealized benchmarks and embraces the full complexity of real-world autonomy and are truly ready for the open-world.

Figure 20: To more accurately reflect real-world performance, a realistic evaluation framework must capture implications from upstream perception, downstream planning, and closed-loop systems.

### Autonomy Tasks Decomposition

(c) Different traffic regulation (e.g. lights/signs)

In light of such complexity, the research community has devoted increasing attention to understanding and modeling the temporal evolution of dynamic objects and scenes. The field has progressed rapidly, transitioning from early physics- and planning-based paradigms to the prevailing wave of learning-based approaches. This evolution has been accompanied by a growing diversity of representational choices---from compact formats such as trajectories, motion primitives, and flows, valued for their efficiency and interpretability, to sensor-level inputs like video and point clouds, enabled by advances in computational resources and the...
