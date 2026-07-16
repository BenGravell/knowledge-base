<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Scenario-Based Trajectory Optimization in Uncertain Dynamic Environments

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present an optimization-based method to plan the motion of an autonomous robot under the uncertainties associated with dynamic obstacles, such as humans. Our method bounds the marginal risk of collisions at each point in time by incorporating chance constraints into the planning problem. This problem is not suitable for online optimization outright for arbitrary probability distributions. Hence, we sample from these chance constraints using an uncertainty model, to generate "scenarios", which translate the probabilistic constraints into deterministic ones. In practice, each scenario represents the collision constraint for a dynamic obstacle at the location of the sample. The number of theoretically required scenarios can be very large. Nevertheless, by exploiting the geometry of the workspace, we show how to prune most scenarios before optimization and we demonstrate how the reduced scenarios can still provide probabilistic guarantees on the safety of the motion plan. Since our approach is scenario based, we are able to handle arbitrary uncertainty distributions. We apply our method in a Model Predictive Contouring Control framework and demonstrate its benefits in simulations and experiments with a moving robot platform navigating among pedestrians, running in real-time.
