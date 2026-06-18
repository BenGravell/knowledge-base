<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Time-Correlated Model Predictive Path Integral: Smooth Action Generation for Sampling-Based Control

Topics include Model predictive path integral control, Trajectory optimization, Sampling-based control, Action smoothing, Time correlation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces temporally correlated noise sampling in MPPI to generate smoother action sequences, improving trajectory quality for sampling-based model predictive control of underactuated systems.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we introduce time-correlated model predictive path integral (TC-MPPI), a novel approach to mitigate action noise in sampling-based control methods. Unlike conventional smoothing techniques that rely on post-processing or additional state variables, TC-MPPI directly incorporates temporal correlation of actions into stochastic optimal control, effectively enforcing quadratic costs on action derivatives. This reformulation enables us to generate smooth action sequences without extra modifications, using a time-correlated and conditional Gaussian sampling distribution. We demonstrate the effectiveness of our approach through simulations on various robotic platforms, including a pendulum, cart-pole, 2D bicopter, 3D quadcopter, and autonomous vehicle. Simulation videos are available at
