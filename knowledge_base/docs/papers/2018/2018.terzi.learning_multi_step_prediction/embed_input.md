<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning Multi-step Prediction Models for Receding Horizon Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, the derivation of multi-step-ahead prediction models from sampled input-output data of a linear system is considered. Specifically, a dedicated prediction model is built for each future time step of interest. Each model is linearly parametrized in a suitable regressor vector, composed of past output values and past and future input values. In addition to a nominal model, the set of all models consistent with data and prior information is derived as well, making the approach suitable for robust control design within a Model Predictive Control framework. The resulting parameter identification problem is solved through a sequence of convex programs. Convergence of the identified error bounds to their theoretical minimum is demonstrated, under suitable assumptions on the measured data, and features like worst-case accuracy computation are illustrated in a numerical example.
