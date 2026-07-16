<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Model Predictive Contouring Control for Collision Avoidance in Unstructured Dynamic Environments

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents a method for local motion planning in unstructured environments with static and moving obstacles, such as humans. Given a reference path and speed, our optimization-based receding-horizon approach computes a local trajectory that minimizes the tracking error while avoiding obstacles. We build on nonlinear model-predictive contouring control (MPCC) and extend it to incorporate a static map by computing, online, a set of convex regions in free space. We model moving obstacles as ellipsoids and provide a correct bound to approximate the collision region, given by the Minkowsky sum of an ellipse and a circle. Our framework is agnostic to the robot model. We present experimental results with a mobile robot navigating in indoor environments populated with humans. Our method is executed fully onboard without the need of external support and can be applied to other robot morphologies such as autonomous cars.
