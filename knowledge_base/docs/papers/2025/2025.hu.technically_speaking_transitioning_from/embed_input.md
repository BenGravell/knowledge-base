<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Technically Speaking: Transitioning from Rule-Based to ML-Powered Motion Planning

Topics include Autonomous driving, Motion planning, Machine learning, Reinforcement learning, End-to-end learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Overview of Motional's approach to motion planning: a scene encoder-generator-ranker architecture with joint prediction and planning, closed-loop reinforcement learning training, and data mining for real-world scalability.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The future of autonomous vehicles (AVs) lies in scalability, adaptability, and human-like driving behavior. At Motional, we are pioneering the next evolution of AV technology by transitioning from traditional rule-based planning systems to an end-to-end machine learning (ML) powered motion planning system. This shift allows us to address some of the key limitations of legacy AV architectures and embrace a future where AVs rapidly learn, adapt, and improve with every mile driven. Traditional AV stacks follow a sequential modular pipeline: Sensors -> Perception → Tracking → Prediction → Rule-based Planning. While this approach offers modularity, interpretability and structured debugging, it also introduces significant drawbacks. By embracing an ML-first approach, Motional is building the foundation for the future: a fully end-to-end ML-based AV system. In this blog post, we will introduce our initial steps in this direction - developing an ML-powered Motion Planning system that integrates prediction and planning into a unified framework.
