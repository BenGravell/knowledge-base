<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Adaptive Cost Function for Pointcloud Registration

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper we introduce an adaptive cost function for pointcloud registration. The algorithm automatically estimates the sensor noise, which is important for generalization across different sensors and environments. Through experiments on real and synthetic data, we show significant improvements in accuracy and robustness over state-of-the-art solutions.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The task of aligning sensor data is called registration and is an important field in robotics, with applications such as simultaneous localization and mapping, object tracking and 3D reconstruction. For two point-clouds, registration is equivalent to finding a relative sensor pose transformation. The modelling of sensor noise can make registration more robust and accurate. Our approach adaptively learns the sensor noise model using the measured point-cloud data while performing the registration.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Registration problems are usually solved by finding corresponding points in different point-clouds and from these correspondences estimate a transformation between the point-clouds. Unfortunately, there is no universal solution, which results in only correct correspondences, for the point matching problem. Many popular solutions require sensor-specific tuning of parameters to reduce the influence of incorrect correspondences, such parameters make using the registration algorithm very complex for non-expert users. It is therefore desirable to find solutions which easily port between different sensors and platforms. In practice, many factors such as illumination strength or environment temperature may affect the sensor noise model. Such environment variables are hard to account for beforehand, making precise a priori noise models impractical in many scenarios. A solution to these problems is to estimate the sensor noise model on the fly, directly from measurement data.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Often when point-cloud registration is required, a coarse initial guess of the alignment is already available. Such guesses can come from robot odometry or from the fact that the sensor only can move so far in a certain amount of time. This class of problems is called constrained registration. If no initial guess is available, it is called unconstrained registration. In the case of constrained registration, solutions usually perform iterative refinement of the correspondences and the estimated transform between the point-clouds. For constrained registration, the range of convergence on the accuracy of the initial guess is an important factor.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

An additional issue can be that the sensors discretely sample the environment, further complicating the registration. This is not addressed by our method. In this paper we limit the problem to constrained registration in which the separation of inliers from outliers is the primary source of error. In particular, we assume that the two point clouds that are to be matched contain some common points that are sampled from nearly the same 3D point in the environment and some that are outliers, ie. points in one point cloud that have no corresponding points in the other point cloud. This is the same assumption made by most registration algorithms.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The main contribution of this paper is a method which we call Statistical Inlier Estimation (SIE). SIE can be used to analyze a set of pairwise matched measurements and from that compute a probability for every match to be correct. The basic idea for SIE is to model the distribution of measurements using histograms of residual errors, and from these histograms estimate the distribution of inliers. The residuals are computed using an estimated transformation between the point-clouds. The estimation of the inlier distribution and the transformation are done alternatively and iteratively. Having an estimate of the inlier probability allows us to define a cost function that does soft matching rather than binary. That is, rather than completely removing points classified as outliers from the cost, all closest matched point pairs are included in the cost but with a weight that depends on the inlier probability.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The registration can be performed without any requirement on hand tuned parameters for specific sensors or applications. From a practical perspective, SIE is relatively simple to implement. The same idea has previously been used for fitting surface primitives such as planes and spheres to point-cloud data. In this paper we show that it can be used as a general purpose inlier estimation framework. We extend the framework to allow for arbitrary noise distributions and enable 3D point-to-point inlier estimation as opposed to only point-to-surface. We also adapt the method by which the distribution of inliers is estimated. We show that SIE can be used to extend the standard *ICP* algorithm. By adding an adaptively decreasing regularization to the variance of our estimated noise model we improve convergence. The regularization approximately correspond to the current uncertainty of the estimated parameters in each iteration of the ICP algorithm. We compare ICP registration using SIE to other methods on both simulated and real world data.

<!-- chunk {"id": "body-0009", "role": "body", "section": "RELATED WORKS", "weight": 1.0} -->

By far the most popular solution to the constrained point-cloud registration problem is the Iterative Closest Point *ICP* algorithm. ICP works directly on the point-clouds by alternating between performing point matching using point-to-point nearest neighbour matching and recomputing the relative transform between the two frames such that it minimizes the L2-norm of the matches. If the sensor measurement noise is Gaussian, the L2-norm correspond to the maximum likelihood estimate of the transform.

<!-- chunk {"id": "body-0010", "role": "body", "section": "RELATED WORKS", "weight": 1.0} -->

Using the assumption that points are sampled from continuous surfaces, several refinements have been proposed to remove the discretization noise generated by the point sampling from a surface. In point-to-plane *ICP* is introduced, meaning that the point distances in one cloud are minimized as the projection distance along the normals of the matched points. In the GICP algorithm is introduced. GICP can be seen as plane-to-plane ICP. In, the NICP algorithm was introduced. During data association, NICP accounts for the relative surface orientations of the points and the local curvature, improving the matching and therefore the accuracy and robustness of the estimation. NICP also change the optimization criteria to minimize the total Mahalanobis distance of the found correspondence point pairs and their normals. In the NICP algorithm was extended to use color information to improve the point matching.

<!-- chunk {"id": "body-0011", "role": "body", "section": "RELATED WORKS", "weight": 1.0} -->

In the trimmed *ICP* algorithm is proposed. To cope with outliers, correspondences with residuals outside of some chosen quantile of the residuals for all correspondences are rejected. This can be a good option if the number of outliers is approximately known a priori.

<!-- chunk {"id": "body-0012", "role": "body", "section": "RELATED WORKS", "weight": 1.0} -->

In, the authors propose to use Levenberg-Marquardt algorithm to perform the estimation of the transformation given point correspondences. The Levenberg-Marquardt algorithm is a general-purpose non-linear optimization method, allowing for arbitrary cost-functions to be used.

<!-- chunk {"id": "body-0013", "role": "body", "section": "RELATED WORKS", "weight": 1.0} -->

In a multi-view Levenberg-Marquardt ICP algorithm is introduced. The algorithm estimates the scale of the sensor noise using the median residual. Using the median residual to estimate the approximate size of the sensor noise removes the need for a hand-tuned rejection criteria, but assumes that atleast half of the residuals come from inlier correspondences and has a built-in bias which increases as the number of outliers grow. The median residual value has some similarity to our use of an adaptively decreasing regularization in that the estimated noise often is larger at the start of the ICP optimization than at the end.

<!-- chunk {"id": "body-0014", "role": "body", "section": "RELATED WORKS", "weight": 1.0} -->

In trust region optimization was used to perform non-linear optimization of robust cost-functions for ICP. Similarly to the approximate size of the sensor noise is estimated using the median residual.

<!-- chunk {"id": "body-0015", "role": "body", "section": "RELATED WORKS", "weight": 1.0} -->

In GO-ICP, a branch-and-bound and *ICP* hybrid algorithm, is introduced. The algorithm is proven to find the optimal solution up to a chosen level of accuracy for the point-to-point L2 error metric and a trimmed *ICP*. Unfortunately the increased range of convergence comes at a price of significantly increased computational complexity.

<!-- chunk {"id": "body-0016", "role": "body", "section": "RELATED WORKS", "weight": 1.0} -->

In, the authors propose the usage of L$p$-norms where $p < 2$ in order to better cope with false correspondences. This work is similar to ours in that it does not require complicated tuning for use on a new sensor.

<!-- chunk {"id": "body-0017", "role": "body", "section": "RELATED WORKS", "weight": 1.0} -->

When using a kd-tree (or a set of trees), the nearest neighbour matching of *ICP* has the computational complexity of $\mathcal{O}{({Nlog{(K)}})}$, where $N$ is the number of points being matched and $K$ is the number of points matched against. Another popular alternative for range scans is to use back projection in order to find correspondences. While back projection does not guarantee to find the true nearest neighbour match, the matching step can be done in $\mathcal{O}{(N)}$, providing a significant reduction in computational complexity. The registration component of popular 3D-SLAM systems such and that require 30 frames per second performance use back projection as a matching algorithm. uses an automatically estimated T-distribution for estimation.

<!-- chunk {"id": "body-0018", "role": "body", "section": "RELATED WORKS", "weight": 1.0} -->

Image registration has traditionally been done using keypoints, a subset of the pixels in the image. Common keypoint extractors such as FAST or Harris corners can find a stable subset of points in images quickly. A large body of work has been put into finding distinctive descriptors for visual information, such as SIFT, SURF, BRIEF, ORB and GRIEF. Keypoint extractors and descriptors have also been created for point-cloud data, such as 3D-sift, NARF and SHOT.

<!-- chunk {"id": "body-0019", "role": "body", "section": "RELATED WORKS", "weight": 1.0} -->

In addition to descriptor similarity, geometrical constraints can be used to filter out false correspondences. Probably the most popular technique used for this is the RANSAC algorithm. In and the AICK algorithm was introduced. AICK is an *ICP*-like algorithm which quickly registers two sets of 3D points with associated descriptors. AICK use a weighted distance metric, taking into account both feature similarity of keypoints and geometrical fit. AICK incrementally change the importance of the feature similarity between the keypoints and the geometrical fit as registration is performed. This relaxes the requirement on geometrical fit at the beginning of the registration, gradually increasing the importance of the geometrical fit for both the matching and outlier rejection as the registration improves from iteration.

<!-- chunk {"id": "body-0020", "role": "body", "section": "RELATED WORKS", "weight": 1.0} -->

In a keypoint-based registration technique which uses a scaled Geman-McClure estimator, where the $\lambda$ parameter is sequentially decreased as the registration is improved. This gradually increases the importance of the geometrical fit for determining the influence of a match based on the geometrical fit as the registration improves.

<!-- chunk {"id": "body-0021", "role": "body", "section": "RELATED WORKS", "weight": 1.0} -->

presents a pointcloud registration method which forms histograms over surface orientations. The surface orientation histograms are then directly aligned to register the pointclouds. This technique efficiently takes advantage of the high amount of co-planar surface patches in indoor environments, leading to improved robustness to poor initialization estimates.

<!-- chunk {"id": "body-0022", "role": "body", "section": "RELATED WORKS", "weight": 1.0} -->

The normal distribution transform (NDT) was developed to take sensor noise into account, first in 2D and later extended to 3D. These methods represent one of the point-clouds using normal distributions to which the points in the other point-clouds are aligned. In the technique is modified to perform registration from a set of normal distributions to another set of normal distributions. In 3D-NDT was augmented with matched keypoints. The weight between the matched keypoints and the NDT results was controlled by a weight that changed over iterations based on the fit of the NDT. In 3D-NDT was extended to use color information.

<!-- chunk {"id": "body-0023", "role": "body", "section": "RELATED WORKS", "weight": 1.0} -->

In an algorithm for fitting geometric primitives to point-cloud data was introduced. At the core of the algorithm is an inlier estimation system which is specifically created for Gaussian distributed point-to-surface distances. and SIE share the idea of fitting a noise distribution to a distance-histogram. Compared to, SIE allows for any distribution to be used. The application domain also differs, as well as many of the practical details as to how the distributions are fitted. SIE also allows for multi-dimensional residuals, which does not.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Point-cloud Registration", "weight": 1.0} -->

Point-cloud registration is done by maximum likelihood estimation over the relative positions of the point-clouds. This finds the transformation that minimizes some cost function over a set of residual errors. In this paper we will assume that the sensor measurement noise distribution is Gaussian. Using other distributions require minimal changes, see appendix for details and experiments using non-Gaussian noise.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Point-cloud Registration", "weight": 1.0} -->

The registration problem can therefore be formulated as the computation of ${{\arg\max}_{b,T}P}{(\left. A \middle| {b,T} \right.)}$, where we indicate by $b$ the correspondences from $B$ that are matched to $A$. We can reformulate the optimization problem as

<!-- chunk {"id": "body-0026", "role": "body", "section": "Point-cloud Registration", "weight": 1.0} -->

The Iterative Closest Point, *ICP*, algorithm assumes that $T$ is approximately known beforehand. The maximum likelihood estimate of $b_{i}$ is the closest point to $T \ast a_{i}$. We will refer to the first step of ICP, where nearest neighbour matching between the point-clouds is performed, as the matching step. The second step of the *ICP* algorithm where eq. is minimized by refining the estimate of $T$ given the previously found point-to-point correspondences, will be referred to as the refinement step. Given the correspondences $b$, minimization of eq. for the $T$ variable can be performed using a standard weighted least squares minimization.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Point-cloud Registration", "weight": 1.0} -->

Using the Iteratively Re-weighted Least Squares (IRLS) algorithm, robust cost functions can be used to reduce the influence of outliers by iteratively solving a set weighted least squares minimizations.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Point-cloud Registration", "weight": 1.0} -->

IRLS is performed using eq. where k indicates the iteration of the IRLS and the superscripts indicate the $T$ that the residuals were computed. We will compare various standard choices for $w{(i)}$. Some of these are designed to give lower or even zero weight to residuals that are less likely to be inliers. We will show in the next section how we can approximate $P{(\left. I \middle| r_{i} \right.)}$, the probability that a residual is an inlier given its value. In our method, the cost function is given a weight proportional to $P{(\left. I \middle| r_{i} \right.)}$:

<!-- chunk {"id": "body-0029", "role": "body", "section": "Statistical Inlier Estimation (SIE)", "weight": 1.0} -->

The ability to detect or mitigate the effect of outliers is critical for the accuracy of point-cloud registration. Even a very small fraction of unaccounted for outliers generally results in extremely poor estimations.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Statistical Inlier Estimation (SIE)", "weight": 1.0} -->

SIE builds a histogram over the residual errors, $r_{i}$, and uses that histogram to estimate the parameters of the measurement noise model. The residuals are the differences between the matched point pairs using the current best estimate of the transformation between point clouds. For estimating the measurement noise model, we exploit the insight that, at or near the peak in the histogram, the contribution to the histogram of outliers is small as compared to that of the inliers.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Statistical Inlier Estimation (SIE)", "weight": 1.0} -->

Fitting a parametric noise model to the histogram shape near the peak therefore models the inlier distribution, with negligible effect from the outliers. Since the histogram is the sum of the outliers and the inliers, the ratio of the inlier distribution to the histogram tells us about the outlier versus inlier relative probability. Figure 1 shows the estimated distributions and probabilities of SIE for a registered pointcloud. For the registration, we use this to weight all correspondence pairs in the cost function. This cost function is then minimized to give a new transformation (the weights are held constant during this minimization). We can then iterate this process with new residuals.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-A Adaptive model fitting", "weight": 1.0} -->

The adaptive model fitting step takes as input a set of residuals, in the form of a matrix $R$ with $n$ rows and $m$ columns, $n$ being the number of correspondences and $m$ the number of dimensions for the residuals caused by the correspondences.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-A Adaptive model fitting", "weight": 1.0} -->

For each column $j$ of $R$, we compute a histogram $H_{j}$. Each histogram is then the sum of the distributions of the inliers and the outliers. The distribution of outliers is in general unknown and often of non-parametric form and is as such hard to compute directly from the data or define a priori. The inlier measurement distribution on the other hand can be approximated by some a-priori known parametric function, making it well suited for estimation. In practice, normal (Gaussian) distributions are very popular approximations of sensor noise for a wide variety of sensor types.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-A Adaptive model fitting", "weight": 1.0} -->

In section III we made the assumption that the sensor noise, and therefore the inliers, were distributed according to $\mathcal{G}_{j} = {\alpha_{j} \ast e^{- {0.5{|\frac{x - \mu_{j}}{\sigma_{j}}|}^{2}}}}$. We make the assumption that all residuals within one column of $R$ are independent and identically distributed. In many applications the sensor noise model parameters (here $\{\alpha_{j},\mu_{j},\sigma_{j}\}$) are unknown and impossible to define a priori, due to among other things environmental conditions. Cameras for example are susceptible to environmental conditions such as illumination, unknown camera exposure time or temperature changes. We believe that if the parameters are unknown or at least inaccurately known, the parameters should be estimated from data.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-A Adaptive model fitting", "weight": 1.0} -->

The $\mu_{j}$ value is defined by a clear peak in $H_{j}$, see fig. for example. Assuming that the vast majority of measurements at the peak correspond to inliers, we can draw the conclusion that $\alpha_{j} \approx {H_{j}{(\mu_{j})}}$. Once $\alpha_{j}$ and $\mu_{j}$ are approximately known, we estimate $\sigma_{j}$ by fitting the noise estimate $\mathcal{G}_{j}$ to the histogram $H_{j}$. $\mathcal{G}_{j}$ is fitted by solving eq.(5 ‣ Adaptive Cost Function for Pointcloud Registration")), which corresponds to maximizing the data likelihood under the soft constraint that $G_{j} \leq H_{j}$. As such, we seek a sensor noise model estimate $\mathcal{G}_{j}$ that explain as many measurements as possible without violating probability constraints.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-A Adaptive model fitting", "weight": 1.0} -->

where $k$ is used as a penalty term that push the minimization to choose solutions where ${H_{j}{(i)}} \geq {\mathcal{G}{(i,\alpha_{j},\mu_{j},\sigma_{j})}}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-A Adaptive model fitting", "weight": 1.0} -->

We found that eq.(5 ‣ Adaptive Cost Function for Pointcloud Registration")) can be effectively minimized using bisection, but any other suitable optimization technique would also be fine.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-A Adaptive model fitting", "weight": 1.0} -->

Computing the inlier distribution parameters in the histogram space has the advantage that, other than constructing the histogram, the computational cost is not related to the number of samples but rather the number of bins in the histogram. This keeps the computational complexity of the minimization low even if there are vast quantities of fitting data and a complex inlier distribution.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B Prediction step", "weight": 1.0} -->

Once the inlier noise distributions and the histograms are known, one can compute the inlier probability for a single dimension $j$ of a measurement $i$. We start with the component of the residual distribution that is due to the inliers,

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-B Prediction step", "weight": 1.0} -->

where P(I) is the prior probability of inliers, and $P{(R_{i,j})}$ is given by the histogram.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-B Prediction step", "weight": 1.0} -->

We will throughout implicitly assume that we have normalized $H_{j}$ and $\mathcal{G}_{j}{(R_{i,j})}$ so that ${\sum_{i,j}{H_{j}{(R_{i,j})}}} = 1$, even if in many formulas this normalization factor cancels and need not be computed. For one dimension the inlier probability is the ratio of expected inliers to the ratio of total residuals for a specific bin in the histogram.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-B Prediction step", "weight": 1.0} -->

We know that a single correspondence, a row $i$ of $R$, is either an inlier or outlier. We have computed the probability of it being an inlier given one column of that row. We now have to compute the probability given the evidence from all the columns of the row. The residuals across a row are not independent unless we know whether or not the row is an inlier. We need to find the joint probability across all dimensions $j$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-B Prediction step", "weight": 1.0} -->

And finally we can infer the inlier probability

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-B Prediction step", "weight": 1.0} -->

where $\gamma = {({{{P{(I)}}/P}{(O)}})}^{m - 1}$. This formula is the inlier probability given the $m$ dimensional residual. To avoid degenerate cases leading to division by zero, we truncate the value of $P{(\left. I \middle| R_{i,j} \right.)}$ to some value less then 1 (in this paper we pick 0.99). This means that, regardless of residual value, no correspondence is completely certain to be correct.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-C Regularizer for use in parameter estimation", "weight": 1.0} -->

Many estimation problems, including point-cloud registration, require fitting some model with a set of variable parameters $T$ to a set of measurements. Since the parameters $T$ are unknown/poorly known at the start of the estimation, the residuals in $R$ are affected by systematic bias, we account for this by adding a secondary regularization term $\beta_{j}$ to the estimated noise $\sigma_{j}$ of the system, resulting in Eq.(14 ‣ Adaptive Cost Function for Pointcloud Registration")).

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-C Regularizer for use in parameter estimation", "weight": 1.0} -->

Once the precision of the estimated parameters $T$ improve, the size of $\beta_{j}$ can be reduced. For the point-cloud registration problem we run the registration algorithm until convergence and then reduce $\beta_{j}$ by 50 percent. Once $\beta_{j}$ has been decreased, the optimization can be run again. We continue this until $\beta_{j}\operatorname{<<}\sigma_{j}$, which means the solution has converged.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-C Regularizer for use in parameter estimation", "weight": 1.0} -->

The initial value of $\beta_{j}$ can be set using prior knowledge about the uncertainty of $T$ or approximated as the standard deviation of the initial set of residuals.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-D Noise normalization", "weight": 1.0} -->

It is a well known fact that the measurement noise of many sensor types is correlated to some a priori known factors for the sensor type. For example, the noise of a measurement by structured light RGBD cameras is known to increases approximately as the square of the distance to the sensor. We formalize this by stating that each residual value $R_{i,j}$ is either an outlier or sampled with an individual $\sigma_{i,j} = {\sigma_{j}F{(i,j)}}$. Re-scaling $R_{i,j}$ by the inverse of $F{(i,j)}$ makes the scale of the measurement noise identical for all measurements and the techniques presented in sections IV-A ‣ Adaptive Cost Function for Pointcloud Registration") and IV-B ‣ Adaptive Cost Function for Pointcloud Registration") performs as expected. For a residual computed from the difference between two measurements, the variance of the resulting residual is the sum of the variances of the two measurements.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-E Adaptive parameters", "weight": 1.0} -->

Two parameters are required to compute a histogram: the interval in which the histogram is defined and the number of bins in the histogram. Through iterative updating, these values can be computed adaptively to the data.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-E Adaptive parameters", "weight": 1.0} -->

Given that our choice of $\mathcal{G}_{j}$ is monotonically decreasing with the distance to the mean value $\mu_{j}$, one can safely limit $H_{j}$ to the interval where $\mathcal{G}_{j} > \epsilon$, where epsilon is a suitably small number.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-E Adaptive parameters", "weight": 1.0} -->

If an initial guess of $\mathcal{G}_{j}$ is not available, one can safely initialize $\mathcal{G}_{j}$ to the maximum likelihood estimate assuming that all measurements in $R$ are inliers.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-E Adaptive parameters", "weight": 1.0} -->

As a means of accounting for sample variance, the number of bins in the histogram can preferably be computed linearly to the number of data that falls within the range of the histogram. This keeps the sample variance of the histogram approximately constant regardless of the amount of data in $H_{j}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-E Adaptive parameters", "weight": 1.0} -->

In hopes of further reducing sample variance, the histogram $H_{j}$ is also smoothed by convolution with a zero mean Gaussian kernel, where the standard deviation is proportional to the width of the histogram. If $\sigma$ is expected to be the same for some set of the dimensions, a joint histogram if all the residuals for those dimensions can be used to reduce the sample variance. Similarly, the absolute values of the residuals can be used to reduce the sample variance of the histograms.

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-E Adaptive parameters", "weight": 1.0} -->

In eq.(5 ‣ Adaptive Cost Function for Pointcloud Registration")) we introduced a penalty term $k$, that bias the minimization to choose solutions where ${H_{j}{(i)}} \geq {\mathcal{G}{(i,\alpha_{j},\mu_{j},\sigma_{j})}}$. In the ideal case with no sample variance in $H_{j}$, one would set $k = \infty$. In practice, because of sample variance, we fund that $1 \leq k \leq 10$ provided good results, with $K = 1$ providing more precise estimations and $k = 10$ providing more robustness to outliers and poor initial value of $T$. We therefore run the registration with $k = 10$ until convergence and then adapt the value of $k$ to the data at hand, using the heuristic $k = {P{(\left. I \middle| H_{j} \right.)}^{- 3}}$ where $P{(\left.

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-E Adaptive parameters", "weight": 1.0} -->

I \middle| H_{j} \right.)}$ is the average probability for the residuals inside the interval of $H_{j}$ to be an inlier.

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-E Adaptive parameters", "weight": 1.0} -->

During iterative estimation, such as *ICP* minimization, the parameters for the histogram width, number of bins and value of $k$ can be carried between iterations. This reduces the computational load of SIE.

<!-- chunk {"id": "body-0057", "role": "body", "section": "EXPERIMENTAL SETUP", "weight": 1.0} -->

We compare our method to other cost functions used for point-cloud registration in order to determine both the accuracy and robustness of the registration relative to other popular solutions. Below we list the cost functions used during experimentation, and the motivation behind using them. Many cost functions have names that indicate which norm is used in the minimization problem. The L2-norm is equivalent to assuming that the measurement noise is Gaussian. All tested solutions are minimized using the iteratively re-weighted least squares (IRLS) minimization algorithm.

<!-- chunk {"id": "body-0058", "role": "body", "section": "EXPERIMENTAL SETUP", "weight": 1.0} -->

: The truncated L~2~-norm is a very popular alternative for point-cloud-alignment. The idea is to reject all correspondences with an error greater than some threshold. The threshold value is usually set to some value in the range of three to four $\sigma$. Finding the optimal rejection threshold can be hard if one does not know $\sigma$ for the sensor.

<!-- chunk {"id": "body-0059", "role": "body", "section": "EXPERIMENTAL SETUP", "weight": 1.0} -->

: The use of L~p~-norms, where one artificially set $p$ to a much smaller number than what is actually present in the sensor, is another popular alternative. The idea is that the effect of correspondences with large residuals can be decreased if $p$ is small. A useful property of the algorithm is that knowledge of the sensor noise model is not required, making it a practical solution in many applications where the threshold of the truncated L~2~-norm is not easily tuned. We will evaluate the result of the L~1~-norm and L~0.1~-norm as proposed.

<!-- chunk {"id": "body-0060", "role": "body", "section": "EXPERIMENTAL SETUP", "weight": 1.0} -->

: In and, the T-distribution is proposed as a self-tuning alternative for registration of RGBD images. Estimation of the scale parameter $\sigma$ is performed using the method.

<!-- chunk {"id": "body-0061", "role": "body", "section": "EXPERIMENTAL SETUP", "weight": 1.0} -->

: SIE models both inlier and outlier distributions. It therefore has the ability to adapt to a wide range of applications. A useful property of the algorithm is that an estimate of the sensor noise is not required, making it a practical solution in many applications where the threshold of the truncated L~2~-norm is not easily tuned.

<!-- chunk {"id": "body-0062", "role": "body", "section": "SIMULATION", "weight": 1.0} -->

As a matter of isolating the effects of the SIE based estimation, we define a simulated experiment where the task is to determine the relative poses of two point-clouds, given a set of point-to-point correspondences, some of which are correct and some which are outliers ^11^1We define a function ${F{(k,n,\sigma)}} = {\{ A,B\}}$ that samples a set of test instance point correspondences $A,B$, where $k$ is the number of inlier matches and $n$ is the number of outlier matches.

<!-- chunk {"id": "body-0063", "role": "body", "section": "SIMULATION", "weight": 1.0} -->

The $k$ inliers in $A$ are uniformly sampled in ${\lbrack 0,1\rbrack}^{3}$ and the inliers in $B$ are identical to the inliers in $A$ but with added Gaussian noise, with a standard deviation of 0.01. The $n$ outliers in $A$ are uniformly sampled in ${\lbrack 0,1\rbrack}^{3}$ and each corresponding outlier in $B$ is uniformly sampled around the outlier in $A$ in the interval of ${\lbrack{- 1},1\rbrack}^{3}$. For an initial guess $T_{0}$, the inlier points are transformed by $T_{0}$ and the outlier points are kept as is. This ensures that the outlier points do not beneficially change the estimation of $T$..

<!-- chunk {"id": "body-0064", "role": "body", "section": "SIMULATION", "weight": 1.0} -->

This is equivalent to performing registration using a keypoint matching scheme. If the points in the point-clouds are independently sampled with zero mean Gaussian noise and transformed by some rigid body transform $T$, the maximum likelihood estimate $T_{MLE}$ of $T$ is given the least squares fit of the correct correspondences.

<!-- chunk {"id": "body-0065", "role": "body", "section": "SIMULATION", "weight": 1.0} -->

Our system aims to compute an estimate of $T$, which is as close to $T_{MLE}$ as possible. In this paper, we measure the Accuracy of estimation, robustness to outliers and robustness to initial guess of $T$. Since this data is simulated, we can vary the number of outliers and change the initial guess for the transformation.

<!-- chunk {"id": "body-0066", "role": "body", "section": "SIMULATION", "weight": 1.0} -->

The test error of an estimated transform is defined as the difference between the root-mean-square-error (RMS) of the correct correspondences and the corresponding value for $T_{MLE}$. The advantage of this error metric is that we are directly measuring how much less probable the estimated solution is to be correct, than the best possible solution. We consider a tested transform with an error greater than the measurement noise a complete failure.

<!-- chunk {"id": "body-0067", "role": "body", "section": "SIMULATION", "weight": 1.0} -->

To acquire reliable statistics we sample a set of 100 different test instances on which we apply our test initial guesses. A total score for an initial transformation and a set of outliers is then computed as the mean error for all the non-failure tests. This score is useful to determine the precision of a registration algorithm. Looking at the ratio of failures is a good method for determining the robustness of the estimator used.

<!-- chunk {"id": "body-0068", "role": "body", "section": "VI-A Simulation Results", "weight": 1.0} -->

We test three different cases, an easy case with 1000 inliers and 100 outliers, a medium case with 1000 inliers and 1000 outliers, and a hard case with 1000 inliers and 10000 outliers. To test the range of convergence, two sets of test transformations are created, one where translation on the X-axis in the range of $\lbrack 0,1\rbrack$ is tested and the other where rotation around the X-axis is tested in the range of $\lbrack 0,\pi\rbrack$ radians. From figures 3 ‣ Adaptive Cost Function for Pointcloud Registration") and 3 ‣ Adaptive Cost Function for Pointcloud Registration"), we observe that SIE reliably and significantly outperform the other cost functions with regards to robustness to poor initialization for $T_{0}$, robustness to outliers and precision of estimation.

<!-- chunk {"id": "body-0069", "role": "body", "section": "PRIMESENSE DATA", "weight": 1.0} -->

In, a benchmark for RGBD-image slam and visual odometry was presented. defines two measurement errors: relative-pose-error (RPE) and absolute-trajectory-error (ATE). The translation RPE is used to test visual odometry and registration algorithms, making it suitable for our purposes.

<!-- chunk {"id": "body-0070", "role": "body", "section": "PRIMESENSE DATA", "weight": 1.0} -->

As previously stated, the noise of a measurement $i$ in the primesense cameras increase approximately by the distance to the sensor squared. We therefore try both $\sigma_{i} = z_{i}^{2}$ and $\sigma_{i} = 1$ and scale the residuals accordingly for all tested methods. From experience, we know that the noise of the primesense cameras is in the range of 0.001 to 0.002 m. We set the threshold for the truncated L~2~-norm is set to 0.007 m. For the other algorithms all parameters are kept identical to the simulation experiments, despite there being a difference of an order of magnitude in the size of the noise.

<!-- chunk {"id": "body-0071", "role": "body", "section": "PRIMESENSE DATA", "weight": 1.0} -->

For computational reasons, the registration algorithm is limited to 2000 randomly sampled nearest neighbour matches for all cost functions. We replace the point-to-point distance used in section VI with the point-to-plane distance metric.

<!-- chunk {"id": "body-0072", "role": "body", "section": "PRIMESENSE DATA", "weight": 1.0} -->

From the results in table I, we can clearly see that SIE consistently outperforms the other cost functions, SIE is has the lowest score or shared lowest score in 11 out of 12 tests. SIE does well especially on the hard cases where all the costfunctions have a high error score. It is also clear that knowing the connection between range and measurement noise has a clear positive effect on the estimation for the tested solutions.

<!-- chunk {"id": "body-0073", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

In this paper we introduced a statistical inlier estimation (SIE) system. SIE is used to determine the probability of pairwise matches to be correct without the need hand tuned parameters. This makes using the system simple and flexible. SIE is intrinsically portable and we have tried it in two different scenarios for sensors with vastly different amounts of noise, without changing any parameters. We extend the *ICP* algorithm to utilize the SIE system for outlier rejection and show that the improved *ICP* algorithm outperforms comparable cost functions on the dataset. Similarly, we show on synthetic data that SIE improves both accuracy and robustness when estimating transforms from point-to-point correspondences, especially in the case of many outliers and poor initialization values.

<!-- chunk {"id": "body-0074", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

In the main body of this paper, we made the assumption that the sensor measurement noise was Gaussian. This is not required by the SIE system presented in section IV ‣ Adaptive Cost Function for Pointcloud Registration"). If we simulate a set of inliers similarly to section V, but with Laplacian noise instead of Gaussian, we can investigate if SIE can be used to estimate the parameters of the Laplacian noise. Both the Laplacian and Gaussian distributions are subsets of the Generalized Gaussian Distribution (GGD)

<!-- chunk {"id": "body-0075", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

where $\Gamma$ denotes the gamma function. The Laplacian distribition is the special case of a GGD when $p = 1$ and the Gaussian distribution the special case of a GGD when $p = 2$.

<!-- chunk {"id": "body-0076", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

The equivalent of eq.(2, with Gaussian noise becomes

<!-- chunk {"id": "body-0077", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

which is equivalent to minimizing over the L~p~-norm instead of the L~2~-norm. The minimization using the probabilities from SIE can be performed using the IRLS algorithm where

<!-- chunk {"id": "body-0078", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

where $\delta$ is a very small number which makes sure that division by zero is avoided.

<!-- chunk {"id": "body-0079", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

For the Laplacian distribution, the test error of an estimated transform is defined as the difference between the mean-absolute-error of the correct correspondences and the corresponding value for $T_{MLE}$. Similarly to the RMS error for the Gaussian distribution, the advantage of the mean-absolute-error metric for Laplacian data is that we directly measure the probability of the estimated solution.

<!-- chunk {"id": "body-0080", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

If $p$ is unknown, SIE can be used to find an estimate of $p$. Naturally this will result in reduced precision, as compared to knowing the exact value of $p$ apriori. In figures 5 and 5 we perform experiments using laplacian noise, we observe that using $p = 1$ results in the best estimation, with SIE estimating $p$ outperforming the estimation when $p = 2$ when there are few to moderate amounts of outliers relative to inliers.

<!-- chunk {"id": "body-0081", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

Both the Laplacian distribution and the estimated $p$ norm allow for fat-tail distributions, resulting in the estimated model over-fitting to the outliers if the outliers significantly outnumber the inliers.

<!-- chunk {"id": "body-0082", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

In figures 7 and 7 we observe that $p = 2$ is the best solution when the measurement noise is Gaussian. The second best solution is using SIE to estimate $p$. Assuming that $p = 1$ providing the worst estimates. We draw the conclusion that estimating $p$ is a good alternative when the exact shape of the measurement noise distribution is not precisely known.
