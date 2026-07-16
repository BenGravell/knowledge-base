<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

What Probing Reveals about Autonomous Driving: Linking Internal Prediction Errors to Ego Planning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Large-scale datasets and fast simulators have enabled improvements in driving policies that appear safe and robust, yet strong performance in nominal scenarios can still mask flawed reasoning and unsafe heuristics. Summary scores from closed-loop simulators do not give significant insight into the policy, making it difficult to determine whether they truly predict the motion of surrounding vehicles, how the ego vehicle generates future plans, or whether they merely rely on brittle heuristics that happen to succeed in nominal scenarios. To better understand the limits and weaknesses of driving policies, we focus on probing for forms of prediction, i.e., where surrounding vehicles will move next, and planning, i.e., understanding how to generate safe trajectories. We focus on these two capabilities because they reflect behaviors expected of effective driving policies, and use their presence or absence to assess policy quality across data-driven behavior cloning and simulation-driven reinforcement learning policies. To evaluate the presence of these capabilities, we investigate them as a function of scale, asking whether the closed-loop gains from larger datasets and longer simulation training reflect stronger prediction and planning or merely better behavioral heuristics.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We use linear probing and targeted perturbations in both imitation learning and reinforcement learning models to track when these internal signals emerge, plateau, or fail. Despite good closed-loop performance, policies often fail to form timely surrounding-vehicle predictions during near-collision events, revealing a limitation in the predictive signals available for ego planning. Finally, causal intervention shows that correcting mistaken predictions improves ego planning toward safer trajectories.
