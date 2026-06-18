<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Is Inverse Reinforcement Learning Harder than Standard Reinforcement Learning? A Theoretical Perspective

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Inverse Reinforcement Learning (IRL) - the problem of learning reward functions from demonstrations of an expert policy - plays a critical role in developing intelligent systems. While widely used in applications, theoretical understandings of IRL present unique challenges and remain less developed compared with standard RL. For example, it remains open how to do IRL efficiently in standard offline settings with pre-collected data, where states are obtained from a behavior policy (which could be the expert policy itself), and actions are sampled from the expert policy. This paper provides the first line of results for efficient IRL in vanilla offline and online settings using polynomial samples and runtime. Our algorithms and analyses seamlessly adapt the pessimism principle commonly used in offline RL, and achieve IRL guarantees in stronger metrics than considered in existing work. We provide lower bounds showing that our sample complexities are nearly optimal. As an application, we also show that the learned rewards can transfer to another target MDP with suitable guarantees when the target MDP satisfies certain similarity assumptions with the original (source) MDP.
