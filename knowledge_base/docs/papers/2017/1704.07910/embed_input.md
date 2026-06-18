Adaptive Cost Function for Pointcloud Registration

In this paper we introduce an adaptive cost function for pointcloud registration. The algorithm automatically estimates the sensor noise, which is important for generalization across different sensors and environments. Through experiments on real and synthetic data, we show significant improvements in accuracy and robustness over state-of-the-art solutions.

## INTRODUCTION

Figure 1: Left: Two point-clouds registered using our method. Right: Resulting histogram of residuals error (inliers and outliers), noise estimate (inliers) and probability of inliers as function of residual error. The non-overlapping outlier regions of the point-clouds appear at the tail end of the histogram of residuals.

The task of aligning sensor data is called registration and is an important field in robotics, with applications such as simultaneous localization and mapping, object tracking and 3D reconstruction. For two point-clouds, registration is equivalent to finding a relative sensor pose transformation. The modelling of sensor noise can make registration more robust and accurate. Our approach adaptively learns the sensor noise model using the measured point-cloud data while performing the registration.

Figure 4: Mean errors of non-failure cases for compared solutions with different number of outliers and different numbers of initial transformation estimates. The measurements are sampled with Laplacian noise. If the failure rate is greater than 0.5, no mean error is displayed. The accuracy of estimation vary by orders of magnitudes between the compared solutions, the mean error is therefore drawn on a logarithmic axis. The top row contain experiments of initial transformation translated along the x-axis by 0 to 1 units....

Figure 6: Mean errors of non-failure cases for compared solutions with different number of outliers and different numbers of initial transformation estimates. The measurements are sampled with Gaussian noise. If the failure rate is greater than 0.5, no mean error is displayed. The accuracy of estimation vary by orders of magnitudes between the compared solutions, the mean error is therefore drawn on a logarithmic axis. The top row contain experiments of initial transformation translated along the x-axis by 0 to 1 units....

where $\gamma = {({{{P{(I)}}/P}{(O)}})}^{m - 1}$. This formula is the inlier probability given the $m$ dimensional residual. To avoid degenerate cases leading to division by zero, we truncate the value of $P{(\left. I \middle| R_{i,j} \right.)}$ to some value less then 1 (in this paper we pick 0.99). This means that, regardless of residual value, no correspondence is completely certain to be correct.
