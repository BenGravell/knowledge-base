<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Robust Learning-Based Control via Bootstrapped Multiplicative Noise

Topics include Control, Optimal control, Robust control, Adaptive control, Reinforcement learning, Model-based, System identification, Multiplicative noise, Stochastic parameters, Bootstrap, Regret.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Assembles a pipeline for automatically designing controllers from data that perform well throughout the data acquisition and system operation timeline. Uncertainty is quantified with a statistical bootstrap and designed against by using a multiplicative noise framework to achieve robustness. The aim is to achieve both good robustness in the low-data short-term transient as well as good performance in the high-data long-term steady state condition.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Despite decades of research and recent progress in adaptive control and reinforcement learning, there remains a fundamental lack of understanding in designing controllers that provide robustness to inherent non-asymptotic uncertainties arising from models estimated with finite, noisy data. We propose a robust adaptive control algorithm that explicitly incorporates such non-asymptotic uncertainties into the control design. The algorithm has three components: a least-squares nominal model estimator; a bootstrap resampling method that quantifies non-asymptotic variance of the nominal model estimate; and a non-conventional robust control design method using an optimal linear quadratic regulator (LQR) with multiplicative noise. A key advantage of the proposed approach is that the system identification and robust control design procedures both use stochastic uncertainty representations, so that the actual inherent statistical estimation uncertainty directly aligns with the uncertainty the robust controller is being designed against. We show through numerical experiments that the proposed robust adaptive controller can significantly outperform the certainty equivalent controller on both expected regret and measures of regret risk.
