<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Robust Data-Driven Output Feedback Control via Bootstrapped Multiplicative Noise

Topics include Data-driven control, Output feedback control, Robust control, Adaptive control, System identification, Subspace identification, Bootstrap resampling, Uncertainty quantification, Finite-sample uncertainty, Multiplicative noise, Stochastic uncertainty models, Dynamic output feedback, Filter-controller co-design, Structured uncertainty, Non-asymptotic robustness, Stability robustness, Sample complexity, Certainty-equivalent, Learning-based control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Assembles a pipeline for adaptive control that uses a statistical bootstrap to estimate uncertainties in system parameters and a multiplicative-noise device to design a controller that is robust to the size and direction of the estimated uncertainties.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a robust data-driven output feedback control algorithm that explicitly incorporates inherent finite-sample model estimate uncertainties into the control design. The algorithm has three components: a subspace identification nominal model estimator; a bootstrap resampling method that quantifies non-asymptotic variance of the nominal model estimate; and a non-conventional robust control design method comprising a coupled optimal dynamic output feedback filter and controller with multiplicative noise. A key advantage of the proposed approach is that the system identification and robust control design procedures both use stochastic uncertainty representations, so that the actual inherent statistical estimation uncertainty directly aligns with the uncertainty the robust controller is being designed against. Moreover, the control design method accommodates a highly structured uncertainty representation that can capture uncertainty shape more effectively than existing approaches. We show through numerical experiments that the proposed robust data-driven output feedback controller can significantly outperform a certainty equivalent controller on various measures of sample complexity and stability robustness.
