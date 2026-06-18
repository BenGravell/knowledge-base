<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Efficient Planning under Uncertainty with Macro-actions

Topics include Partial observability, Robotics, Uncertainty, Online algorithms, Planning, Control, Posterior belief distribution, PBD.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Deciding how to act in partially observable environments remains an active area of research. Identifying good sequences of decisions is particularly challenging when good control performance requires planning multiple steps into the future in domains with many states. Towards addressing this challenge, we present an online, forward-search algorithm called the Posterior Belief Distribution (PBD). PBD leverages a novel method for calculating the posterior distribution over beliefs that result after a sequence of actions is taken, given the set of observation sequences that could be received during this process. This method allows us to efficiently evaluate the expected reward of a sequence of primitive actions, which we refer to as macro-actions. We present a formal analysis of our approach, and examine its performance on two very large simulation experiments: scientific exploration and a target monitoring domain. We also demonstrate our algorithm being used to control a real robotic helicopter in a target monitoring experiment, which suggests that our approach has practical potential for planning in real-world, large partially observable domains where a multi-step lookahead is required to achieve good performance.
