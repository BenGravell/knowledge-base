<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Parameter-Robust MPPI for Safe Online Learning of Unknown Parameters

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Robots deployed in dynamic environments must remain safe even when key physical parameters are uncertain or change over time. We propose Parameter-Robust Model Predictive Path Integral (PRMPPI) control, a framework that integrates online parameter learning with probabilistic safety constraints. PRMPPI maintains a particle-based belief over parameters via Stein Variational Gradient Descent, evaluates safety constraints using Conformal Prediction, and optimizes both a nominal performance-driven and a safety-focused backup trajectory in parallel. This yields a controller that is cautious at first, improves performance as parameters are learned, and ensures safety throughout. Simulation and hardware experiments demonstrate higher success rates, lower tracking error, and more accurate parameter estimates than baselines.
