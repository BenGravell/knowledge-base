<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning for Control: An Inverse Optimization Approach

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a learning method to learn the mapping from an input space to an action space, which is particularly suitable when the action is an optimal decision with respect to a certain unknown cost function. We use an inverse optimization approach to retrieve the cost function by introducing a new loss function and a new hypothesis class of mappings. A tractable convex reformulation of the learning problem is also presented. The method is effective for learning input-action mapping in continuous input-action space with input-output constraints, typically present in control systems. The learning approach can be effectively transformed to learn a Model Predictive Control (MPC) behaviour and a case study to mimic an MPC is presented, which is a rather computationally heavy control strategy. Simulation and experimental results show the effectiveness of the proposed approach.
