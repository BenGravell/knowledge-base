<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the Identification of Variances and Adaptive Kalman Filtering

Topics include Adaptive Kalman filter, Noise covariance estimation, Kalman filtering, Innovation analysis, Recursive estimation, System identification, State estimation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Mehra studies adaptive Kalman filtering when the process and measurement noise covariance matrices are unknown. The paper gives innovation-correlation tests for filter optimality, methods for estimating noise covariances under identifiability conditions, and an alternative iterative route to the steady-state optimal gain.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A Kalman filter requires an exact knowledge of the process noise covariance matrix Q and the measurement noise covariance matrix R. Here we consider the case in which the true values of Q and R are unknown. The system is assumed to be constant, and the random inputs are stationary. First, a correlation test is given which checks whether a particular Kalman filter is working optimally or not. If the filter is suboptimal, a technique is given to obtain asymptotically normal, unbiased, and consistent estimates of Q and R. This technique works only for the case in which the form of Q is known and the number of unknown elements in Q is less than n \times r where n is the dimension of the state vector and r is the dimension of the measurement vector. For other cases, the optimal steady-state gain K op is obtained directly by an iterative procedure without identifying Q. As a corollary, it is shown that the steady-state optimal Kalman filter gain K op depends only on n \times r linear functionals of Q. The results are first derived for discrete systems. They are then extended to continuous systems. A numerical example is given to show the usefulness of the approach.
