Planning-Guided Diffusion Policy Learning for Generalizable Contact-Rich Bimanual Manipulation

Topics include Diffusion policy, Bimanual manipulation, Contact-rich manipulation, Motion planning, Imitation learning, Generalization.

Introduces GLIDE, a planning-guided diffusion-policy approach for contact-rich bimanual manipulation with limited demonstrations. The central contribution is using model-based motion planning to shape diffusion-policy learning so manipulation policies generalize better across object states and task variations.

Contact-rich bimanual manipulation involves precise coordination of two arms to change object states through strategically selected contacts and motions. Due to the inherent complexity of these tasks, acquiring sufficient demonstration data and training policies that generalize to unseen scenarios remain a largely unresolved challenge. Building on recent advances in planning through contacts, we introduce Generalizable Planning-Guided Diffusion Policy Learning (GLIDE), an approach that effectively learns to solve contact-rich bimanual manipulation tasks by leveraging model-based motion planners to generate demonstration data in high-fidelity physics simulation. Through efficient planning in randomized environments, our approach generates large-scale and high-quality synthetic motion trajectories for tasks involving diverse objects and transformations. We then train a task-conditioned diffusion policy via behavior cloning using these demonstrations....

## Introduction

From warehouse logistics to home services, a broad range of essential robotic applications relies on manipulation involving multi-contact interactions between objects and the manipulators. For example, as shown in Fig. LABEL:fig:teaser, the task is to control two robotic arms to manipulate different objects to a specified target pose. These objects are often bulky and heavy, making them not directly graspable by the end-effectors....

To tackle this challenge, recent advances in model-based planning methods utilizing smoothed contact models have begun to demonstrate effectiveness However, such motion planners need complete knowledge of object states and environment geometry, thereby limiting their ability to operate in novel environments where objects exhibit diverse geometries and physical properties. Additionally, their computational overhead prevents them from generating trajectories online, which can be a critical limitation, especially in dynamic environments that require real-time adaptation....

## Conclusion

We presented GLIDE, a planning-guided diffusion policy learning method for generalizable contact-rich bimanual manipulation. Leveraging the recent advances in efficient model-based planning through contact, we generate large-scale, high-quality demonstration trajectories in simulation. We then perform visuomotor imitation learning using a task-conditioned point cloud diffusion policy, and we propose essential design choices in feature extraction, task representation, and action prediction that enable effective policy generalization to unseen scenarios and sim-to-real transfer....

We design the prediction head of the policy network to robustly generate smooth and feasible motion trajectories. Following \[\], our policy predicts an action sequence of $T_{a}$ steps. We use a larger $T_{a} = 20$ at test time to improve performance and train our policy with $T_{a} = 64$. Additionally, prior work like \[\] usually directly predicts the absolute end-effector poses or joint angles as actions. However, we observe that this can result in poor generalization to unseen objects and non-smooth trajectories in the real world....

A collision-free planner using bidirectional RRT \[\] with shortcutting to plan a collision-free trajectory from the current robot joint configuration $q^{a}$ to the next grasp $q_{\text{grasp}}^{a}$.
