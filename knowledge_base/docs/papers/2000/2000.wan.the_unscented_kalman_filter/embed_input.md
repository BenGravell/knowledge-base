<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Unscented Kalman Filter for Nonlinear Estimation

Topics include Unscented Kalman filter, Nonlinear estimation, Unscented transform, Sigma points, System identification, Neural network training, Dual estimation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Extends the Unscented Kalman Filter beyond state estimation into nonlinear system identification, neural-network training, and dual estimation. The paper popularized the UKF as a practical alternative to EKF linearization by emphasizing sigma-point propagation accuracy at comparable computational order.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper points out the flaws in using the extended Kalman filter (EKE) and introduces an improvement, the unscented Kalman filter (UKF), proposed by Julier and Uhlman. A central and vital operation performed in the Kalman filter is the propagation of a Gaussian random variable (GRV) through the system dynamics. In the EKF the state distribution is approximated by a GRV, which is then propagated analytically through the first-order linearization of the nonlinear system. This can introduce large errors in the true posterior mean and covariance of the transformed GRV, which may lead to sub-optimal performance and sometimes divergence of the filter. The UKF addresses this problem by using a deterministic sampling approach. The state distribution is again approximated by a GRV, but is now represented using a minimal set of carefully chosen sample points. These sample points completely capture the true mean and covariance of the GRV, and when propagated through the true nonlinear system, captures the posterior mean and covariance accurately to the 3rd order (Taylor series expansion) for any nonlinearity. The EKF in contrast, only achieves first-order accuracy.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Remarkably, the computational complexity of the UKF is the same order as that of the EKF. Julier and Uhlman demonstrated the substantial performance gains of the UKF in the context of state-estimation for nonlinear control. Machine learning problems were not considered. We extend the use of the UKF to a broader class of nonlinear estimation problems, including nonlinear system identification, training of neural networks, and dual estimation problems. In this paper, the algorithms are further developed and illustrated with a number of additional examples.
