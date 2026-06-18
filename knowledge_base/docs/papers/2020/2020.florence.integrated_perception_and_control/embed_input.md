<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Integrated Perception and Control at High Speed: Evaluating Collision Avoidance Maneuvers without Maps

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a method for robust high-speed quadrotor flight through unknown cluttered environments using integrated perception and control. Motivated by experiments in which the difficulty of accurate state estimation was a primary limitation on speed, our method forgoes maintaining a map in favor of using only instantaneous depth information in the local frame. This provides robustness in the presence of significant state estimate uncertainty. Additionally, we present approximation methods augmented with spatial partitioning data structures that enable low-latency, real-time reactive control. The probabilistic formulation provides a natural way to integrate reactive obstacle avoidance with arbitrary navigation objectives. We validate the method using a simulated quadrotor race through a forest at high speeds in the presence of increasing state estimate noise. We pair our method with a motion primitive library and compare with a global path-generation and pathfollowing approach.
