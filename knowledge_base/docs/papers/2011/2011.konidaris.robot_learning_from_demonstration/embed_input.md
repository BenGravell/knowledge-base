<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Robot Learning from Demonstration by Constructing Skill Trees

Topics include Learning from demonstration, Skill trees, Robot learning, Hierarchical reinforcement learning, Skill segmentation, Policy learning, Manipulation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces CST, an online method that segments demonstrations into reusable skills and merges multiple demonstrated chains into a skill tree. The key idea is to attach goals and abstractions to each skill, allowing demonstrated behavior to be refined by policy learning rather than copied as a fixed trajectory.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We describe CST, an online algorithm for constructing skill trees from demonstration trajectories. CST segments a demonstration trajectory into a chain of component skills, where each skill has a goal and is assigned a suitable abstraction from an abstraction library. These properties permit skills to be improved efficiently using a policy learning algorithm. Chains from multiple demonstration trajectories are merged into a skill tree. We show that CST can be used to acquire skills from human demonstration in a dynamic continuous domain, and from both expert demonstration and learned control sequences on the uBot-5 mobile manipulator.
