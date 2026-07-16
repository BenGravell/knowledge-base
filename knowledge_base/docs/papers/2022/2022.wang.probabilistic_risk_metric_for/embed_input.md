<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Probabilistic Risk Metric for Highway Driving Leveraging Multi-Modal Trajectory Predictions

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Road traffic safety has attracted increasing research attention, in particular in the current transition from human-driven vehicles to autonomous vehicles. Surrogate measures of safety are widely used to assess traffic safety but they typically ignore motion uncertainties and are inflexible in dealing with two-dimensional motion. Meanwhile, learning-based lane-change and trajectory prediction models have shown potential to provide accurate prediction results. We therefore propose a prediction-based driving risk metric for two-dimensional motion on multi-lane highways, expressed by the maximum risk value over different time instants within a prediction horizon. At each time instant, the risk of the vehicle is estimated as the sum of weighted risks over each mode in a finite set of lane-change maneuver possibilities. Under each maneuver mode, the risk is calculated as the product of three factors: lane-change maneuver mode probability, collision probability and expected crash severity. The three factors are estimated leveraging two-stage multi-modal trajectory predictions for surrounding vehicles: first a lane-change intention prediction module is invoked to provide lane-change maneuver mode possibilities, and then the mode possibilities are used as partial input for a multi-modal trajectory prediction module.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Working with the empirical trajectory dataset highD and simulated highway scenarios, the proposed two-stage model achieves superior performance compared to a state-of-the-art prediction model. The proposed risk metric is computationally efficient for real-time applications, and effective to identify potential crashes earlier thanks to the employed prediction model.
