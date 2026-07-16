<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Data-driven Soft Robot Control via Adiabatic Spectral Submanifolds

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The mechanical complexity of soft robots creates significant challenges for their model-based control. Specifically, linear data-driven models have struggled to control soft robots on complex, spatially extended paths that explore regions with significant nonlinear behavior. To account for these nonlinearities, we develop here a model-predictive control strategy based on the recent theory of adiabatic spectral submanifolds (aSSMs). This theory is applicable because the internal vibrations of heavily overdamped robots decay at a speed that is much faster than the desired speed of the robot along its intended path. In that case, low-dimensional attracting invariant manifolds (aSSMs) emanate from the path and carry the dominant dynamics of the robot. Aided by this recent theory, we devise an aSSM-based model-predictive control scheme purely from data. We demonstrate the effectiveness of our data-driven model in tracking dynamic trajectories across diverse tasks. We validate on high-fidelity, high-dimensional finite-element models of a soft trunk robot and Cosserat-rod-based elastic soft arms, with additional experiments confirming robust performance even in the presence of experimental noise.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Notably, we find that five- or six-dimensional aSSM-reduced models outperform the tracking performance of other data-driven modeling methods by a factor up to 10 across all closed-loop control tasks.
