The Scaled Unscented Transformation

Topics include Unscented transform, Scaled unscented transform, Sigma points, Nonlinear estimation, Kalman filtering, Covariance propagation.

Generalizes the unscented transform by scaling sigma points independently of state dimension while preserving second-order mean and covariance accuracy. The paper addresses practical tuning and stability issues in sigma-point filters without requiring Jacobians or Hessians.

This paper describes a generalisation of the unscented transformation (UT) which allows sigma points to be scaled to an arbitrary dimension. The UT is a method for predicting means and covariances in nonlinear systems. A set of samples are deterministically chosen which match the mean and covariance of a (not necessarily Gaussian-distributed) probability distribution. These samples can be scaled by an arbitrary constant. The method guarantees that the mean and covariance second order accuracy in mean and covariance, giving the same performance as a second order truncated filter but without the need to calculate any Jacobians or Hessians. The impacts of scaling issues are illustrated by considering conversions from polar to Cartesian coordinates with large angular uncertainties.
