<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Simple and Model-Free Path Filtering Algorithm for Smoothing and Accuracy

Topics include Path planning, Path smoothing, Path filtering, Moving average, Curvature, Model-free, Post-processing.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

CCMA applies an iterative spatial-curvature-corrected moving average to smooth a path without requiring any kinematic model. Takes advantage of special structure and knowledge that the data series represents a spatial path (instead of an arbitrary sequence).

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Predominantly, complex optimization techniques are used for path reconstruction given noisy measurements. However, optimization techniques often require the selection of suitable models, tedious parameter tuning and typically fail to generalize to higher-level tasks. In this paper, we present a model-free path filtering method based on the popular moving average method, namely the Curvature Corrected Moving Average (CCMA), which convinces by its simplicity and broad applicability. The moving average is characterized by its unique noise suppression property, albeit curves are bent inwards, which adversely affects its accuracy. By utilizing the relation between both curvatures, the original curvature can be inferred based on the curvature of filtered points. Extending the symmetric filtering not only succeeds in minimizing noise but retains the original shape of the path, making it a suitable algorithm for a variety of robotic applications. We demonstrate the practicality of the approach in a real-world convoy scenario: The accumulated estimates of the leader vehicle’s position, originating from an Extended Kalman filter, are smoothed using our novel approach to generate proper inputs for the Model Predictive Controller (MPC). This cascade structure of filtering provides both responsiveness and smoothness.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Furthermore, we successfully applied this method in the off-road convoy scenario for the ELROB 2022, where we won first place. The source code is publicly available.
