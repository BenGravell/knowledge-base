<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Perception-Based Sampled-Data Optimization of Dynamical Systems

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Motivated by perception-based and sensing-based control problems in autonomous systems, this paper addresses the problem of developing feedback controllers to regulate the inputs and the states of a dynamical system to optimal solutions of an optimization problem when one has no access to exact measurements of the system states. In particular, we consider the case where the states need to be estimated from high-dimensional sensory data received only at some time instants. We develop a sampled-data feedback controller that is based on adaptations of a projected gradient descent method and includes neural networks as integral components to estimate the state of the system from perceptual information. We derive sufficient conditions to guarantee (local) input-to-state stability of the control loop. Moreover, we show that the interconnected system tracks the solution trajectory of the underlying optimization problem up to an error that depends on the approximation errors of the neural network and on the time-variability of the optimization problem; the latter originates from time-varying safety and performance objectives, input constraints, and unknown disturbances.
