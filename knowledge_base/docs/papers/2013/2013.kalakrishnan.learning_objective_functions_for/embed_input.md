<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning Objective Functions for Manipulation

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present an approach to learning objective functions for robotic manipulation based on inverse reinforcement learning. Our path integral inverse reinforcement learning algorithm can deal with high-dimensional continuous state-action spaces, and only requires local optimality of demonstrated trajectories. We use L 1 regularization in order to achieve feature selection, and propose an efficient algorithm to minimize the resulting convex objective function. We demonstrate our approach by applying it to two core problems in robotic manipulation. First, we learn a cost function for redundancy resolution in inverse kinematics. Second, we use our method to learn a cost function over trajectories, which is then used in optimization-based motion planning for grasping and manipulation tasks. Experimental results show that our method outperforms previous algorithms in high-dimensional settings.
