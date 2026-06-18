<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

One Model to Drift Them All: Physics-Informed Conditional Diffusion Model for Driving at the Limits

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Enabling autonomous vehicles to reliably operate at the limits of handling— where tire forces are saturated — would improve their safety, particularly in scenarios like emergency obstacle avoidance or adverse weather conditions. However, unlocking this capability is challenging due to the task’s dynamic nature and the high sensitivity to uncertain multimodal properties of the road, vehicle, and their dynamic interactions. Motivated by these challenges, we propose a framework to learn a conditional diffusion model for high-performance vehicle control using an unlabelled multimodal trajectory dataset. We design the diffusion model to capture the distribution of parameters of a physics-informed data-driven dynamics model. By conditioning the generation process on online measurements, we integrate the diffusion model into a real-time model predictive control framework for driving at the limits, and show that it can adapt on the fly to a given vehicle and environment. Extensive experiments on a Toyota Supra and a Lexus LC 500 show that a single diffusion model enables reliable autonomous drifting on both vehicles when operating with different tires in varying road conditions. The model matches the performance of task-specific expert models while outperforming them in generalization to unseen conditions, paving the way towards a general, reliable method for autonomous driving at the limits of handling.
