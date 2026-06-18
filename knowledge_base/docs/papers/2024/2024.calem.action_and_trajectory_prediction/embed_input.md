<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Action and Trajectory Prediction for Autonomous Driving

Topics include Action prediction, Trajectory prediction, Trajectory forecasting, Autonomous driving, Reinforcement learning, Diversity, Discovery, Deep learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

PhD thesis covering action and trajectory prediction methods for autonomous driving.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This PhD thesis, in the applicative context of autonomous driving, focuses on the exploration of diversity promoting mechanisms in generative models, which generate a probabilistic distribution of future trajectories given past trajectories. As trajectory forecasting datasets only provide one ground truth trajectory for a given past trajectory and scene spatial layout, many existing methods focus on the accuracy of the best predicted trajectory with respect to the ground truth trajectory. We aim to expand these methods by improving the intrinsic diversity of the predicted distribution, through the creation of a diversity-aware sampling mechanism that replaces traditional sequential sampling from generative models such as variational autoencoders (VAEs). We provide a way to generate samples according to the diversity exhibited in the training dataset, not only centered around the majority mode. The improvement of diversity, validated on nuScenes through a comprehensive set of metrics, is interesting with regard to the safety and smoothness of the planning operation, subsequent to trajectory forecasting. Furthering the diversity aspect in rare but safety-critical scenarios, we ask ourselves the question of expressing the diversity of events that are possible but yet unrepresented in the training dataset.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This line of questioning raises the exploration of a much more challenging aspect: discovery. In order to generate a distribution that contains modes not present in the training dataset, we must carefully grow the training distribution according to an external admissibility function. The delicate balance between allowing the decoder of a generative model to generate from unknown latent codes and the necessity of generating admissible samples is explored in the second part of this thesis, with interesting results on a toy dataset.
