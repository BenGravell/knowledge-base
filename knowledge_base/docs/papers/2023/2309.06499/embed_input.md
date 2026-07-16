<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Belief Control Barrier Functions for Risk-aware Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Ensuring safety in real-world robotic systems is often challenging due to unmodeled disturbances and noisy sensor measurements. To account for such stochastic uncertainties, many robotic systems leverage probabilistic state estimators such as Kalman filters to obtain a robot's belief, i.e. a probability distribution over possible states. We propose belief control barrier functions (BCBFs) to enable risk-aware control synthesis, leveraging all information provided by state estimators. This allows robots to stay in predefined safety regions with desired confidence under these stochastic uncertainties. BCBFs are general and can be applied to a variety of robotic systems that use extended Kalman filters as state estimator. We demonstrate BCBFs on a quadrotor that is exposed to external disturbances and varying sensing conditions. Our results show improved safety compared to traditional state-based approaches while allowing control frequencies of up to 1kHz.
