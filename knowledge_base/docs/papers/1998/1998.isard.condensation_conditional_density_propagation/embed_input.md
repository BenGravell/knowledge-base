CONDENSATION - Conditional Density Propagation for Visual Tracking

Topics include Particle filters, Visual tracking, Conditional density propagation, Factored sampling, Bayesian filtering, Computer vision, Multimodal tracking.

Introduces the CONDENSATION algorithm, using factored sampling to propagate a set-based approximation of a multimodal posterior for visual tracking. It is an early and influential particle-filter formulation for computer vision, designed to track agile curves through clutter where Kalman filters are too Gaussian.

The problem of tracking curves in dense visual clutter is challenging. Kalman filtering is inadequate because it is based on Gaussian densities which, being unimo dal, cannot represent simultaneous alternative hypotheses. The Condensation algorithm uses 'factored sampling', previously applied to the interpretation of static images, in which the probability distribution of possible interpretations is represented by a randomly generated set. Condensation uses learned dynamical models, together with visual observations, to propagate the random set over time. The result is highly robust tracking of agile motion. Notwithstanding the use of stochastic methods, the algorithm runs in near real-time.
