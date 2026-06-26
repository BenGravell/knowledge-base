<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Quaternion Based Camera Pose Estimation from Matched Feature Points

Topics include Robustness, Pose estimation, Graphs, Accuracy, Online algorithms.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a novel solution to the camera pose estimation problem, where rotation and translation of a camera between two views are estimated from matched feature points in the images. The camera pose estimation problem is traditionally solved via algorithms that are based on the essential matrix or the Euclidean homography. With six or more feature points in general positions in the space, essential matrix based algorithms can recover a unique solution. However, such algorithms fail when points are on critical surfaces (e.g., coplanar points) and homography should be used instead. By formulating the problem in quaternions and decoupling the rotation and translation estimation, our proposed algorithm works for all point configurations. Using both simulated and real world images, we compare the estimation accuracy of our algorithm with some of the most commonly used algorithms. Our method is shown to be more robust to noise and outliers. For the benefit of community, we have made the implementation of our algorithm available online and free.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many applications in computer vision and robotics require measurements of the rotation and translation (i.e., pose) changes of an object as it moves through an environment. In photogrammetry, for example, by knowing the pose changes of the camera, 3D model of a scene can be constructed from a set of 2D images. In robotics, pose estimated from images can be used for navigation, or fused with other sensor measurements (e.g., IMU and GPS) to increase the reliability and accuracy. Camera pose estimation has further applications in simultaneous localization and mapping (SLAM), autonomous vehicles, and augmented reality.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Camera pose estimation techniques are often based on image features (e.g., edges, corners, etc., in an image) that can be detected and matched in two or more images. Figure 1 shows an example where feature points are detected and matched as indicated by yellow lines in two images. Many existing methods use the coordinates of feature points on the image to construct the essential/fundamental matrix or the Euclidean homography matrix, from which relative rotation and translation of the camera can be recovered. Although these approach are fast and easy to implement, they are subject to drawbacks: the essential matrix based algorithms fail when feature points are on critical surfaces (e.g., coplanar points), while homography based algorithms only work when points are coplanar.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we present a novel formulation of the camera pose estimation problem using quaternions and present a solution to estimate the pose under this formulation. Our approach, which we refer to as the Quaternion Estimation (QuEst) algorithm, does not use the homography or essential matrices, and decouples the estimation of rotation and translation. Consequently, common problems such as degeneracy for special 3D point configurations are avoided. We present two methods to recover the rotation from seven and six matched feature points. We then show how the unique correct solution can be detected from among the set of recovered solutions. The performance of QuEst is compared with algorithms that are based on the homography or essential matrix in the presence of noise in image point coordinates. The performance is further vetted by using real world image datasets that come with the ground truth camera pose information.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main contributions and benefits of the proposed algorithm can be summarized as follows.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

As illustrated in Table I, unlike the homography or essential matrix based algorithms, QuEst provides an accurate pose estimate for both general point configurations and points that are on critical surfaces, e.g., coplanar points. To initialize the bundle adjustment in SLAM applications, often heuristic methods are used to detect the coplanarity of the points and select the appropriate algorithm correspondingly. QuEst can be used to initialize the bundle adjustment regardless of the feature point configuration in the space.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

By recovering the translation, QuEst simultaneously recovers depths of the feature points. Therefore, a 3D model of the scene can be reconstructed. The recovered translation and depths share a common scale factor, hence, the magnitude of the recovered translation vector goes to zero as the camera translation between two views approaches zero. The translation recovered from the essential matrix always has unit norm, which is not desirable in applications such as visual servoing.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Tests performed using both simulated and real world images show that the pose recovered from QuEst is more accurate and robust to noise and outliers compared to the existing algorithms.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rest of the paper is organized as follows. We briefly review related approaches in Section II, before we formulate the pose estimation problem using quaternions in Section III. We present the QuEst algorithm in Section IV and evaluate its performance under noise in Section V. In Section IV, we further vet the performance of QuEst using the real world image datasets.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Camera Pose Estimation", "weight": 1.0} -->

We introduce the notation and assumptions, followed by formulating the pose estimation problem in quaternions.

<!-- chunk {"id": "body-0012", "role": "body", "section": "III-A Notation and Assumptions", "weight": 1.0} -->

Throughout the paper, we assume that the camera calibration matrix is known; this matrix can be easily found through the existing camera calibration routines.

<!-- chunk {"id": "body-0013", "role": "body", "section": "III-A Notation and Assumptions", "weight": 1.0} -->

Scalars are represented by lower case (e.g., $s$), vectors by lowercase and bold (e.g., $\mathbf{v}$), and matrices by upper case and bold letters (e.g., $\mathbf{M}$). All vectors are column vectors. The Moore-Penrose pseudo inverse of matrix $\mathbf{M}$ is shown by $\mathbf{M}^{\dagger}$. Binomial coefficients are denoted by $\binom{n}{k}:=\frac{n!}{{k!}{{({n - k})}!}}$. By norm of a vector, we imply the $l^{2}$-norm.

<!-- chunk {"id": "body-0014", "role": "body", "section": "III-A Notation and Assumptions", "weight": 1.0} -->

Degree 4 monomials in variables $w,x,y,z$ are single term polynomials $w^{a}x^{b}y^{c}z^{d}$, such that ${a + b + c + d} = 4$, for ${a,b,c,d} \in {\{ 0,1,2,3,4\}}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "III-B Problem Formulation", "weight": 1.0} -->

Consider images of a scene taken by a camera at two views (e.g., Fig. 1). Let $\mathbf{R} \in {\text{SO}{}}$ and $\mathbf{t} \in {\mathbb{R}}^{3}$ respectively represent the relative rotation and translation of the camera frame between the views. Assume that feature points are detected and matched, and their $x$-$y$ coordinates are read from the images. (In practice, the coordinates are in pixels, and should be mapped via the camera calibration matrix to Cartesian coordinates on the image plane.)

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-B Problem Formulation", "weight": 1.0} -->

For each matched feature point the rigid motion constraint must hold, in which ${\mathbf{m},\mathbf{n}} \in {\mathbb{R}}^{3}$ are homogeneous coordinates (i.e., a 1 is appended to the $x$-$y$ coordinates) of the feature point in two images. Scalars $u$ and $v$ represent depths of the 3D point at each view, and as shown in Fig. 2, are the projections of the point onto the $z$-axis of the camera coordinate frame. Point coordinates $\mathbf{m}$ and $\mathbf{n}$ are known from the images, and the unknowns in are $u$, $v$, $\mathbf{R}$, and $\mathbf{t}$, which need to be recovered.

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-B Problem Formulation", "weight": 1.0} -->

We need to point out that in the pose estimation problem, translation and depths of the points can only be recovered up to a scale factor. This can be seen, where any constant multiplied into both hand sides can be absorbed by unknown variables $u,v$, and $\mathbf{t}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Example 1", "weight": 1.0} -->

Consider pictures shown in Fig. 1, where feature points are matched and their coordinates on the image are determined. For the matched feature point with coordinates $({- 0.1},{- 1.5})$ in the left image and $(0.2,{- 1.2})$ in the right image, from we get where scalar $u_{1}$ and $v_{1}$ are the depths of the 3D point at each view. Similarly, for two other matched pairs we can write where subscripts are used to distinguish the depths of the points (scalars $u$ and $v$). Notice that rotation matrix $\mathbf{R}$ and translation vector $\mathbf{t}$ are the same in all equations.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Example 1", "weight": 1.0} -->

Equation uses the matrix representation of rotation, in which $\mathbf{R}$ is a $3 \times 3$ orthonormal matrix. That is, $\mathbf{R}^{\top} = \mathbf{R}^{- 1}$, and ${\det{(\mathbf{R})}} = 1$. Representing the rotation in the matrix form with orthonormality constraints makes the problem very nonlinear and challenging to solve. Instead, we use quaternions, which represent a rotation by four elements ${w,x,y,z} \in {\mathbb{R}}$ such that ${w^{2} + x^{2} + y^{2} + z^{2}} = 1$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Example 1", "weight": 1.0} -->

Although can be formulated directly in quaternions, for simplicity and to avoid introducing the quaternion algebra we only mention what is essential to solve the problem here: if ${w,x,y,z} \in {\mathbb{R}}$ are elements of a rotation quaternion, the associated rotation matrix is given by Quaternions provide a singularity free representation of rotation, and by restricting the first element to nonnegative numbers (i.e., $w \geq 0$), there is a one to one and onto correspondence between rotation matrices and quaternions.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Example 1", "weight": 1.0} -->

To recover the pose, we first eliminate the unknowns $u,v$ and $\mathbf{t}$, and derive a system of equations in terms of the quaternion elements. From solving this system all rotation solution candidates are found. Subsequently, the translation and depths of the points are recovered. By taking for two different feature points and subtracting the equations, $\mathbf{t}$ can be eliminated. Subsequently, $u$ and $v$ can be eliminated from the resulting equations by noting that they form a null vector for the matrix consisting of the point coordinates and their rotations. The following example illustrates this procedure.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Example 2", "weight": 1.0} -->

Consider Example 1. By subtracting and, respectively, and bringing terms to the left hand side we get in which the unknown translation $\mathbf{t}$ has been eliminated. We can represent and in the matrix-vector form which implies that matrix $\mathbf{M} \in {\mathbb{R}}^{6 \times 6}$ has a null vector. Therefore, its determinant must be zero. Calculating determinant of $\mathbf{M}$ with $\mathbf{R}$ given in the parametric form gives Equation consists of all degree 4 monomials in $w,x,y,z$ (i.e., terms such as $w^{4},{w^{3}x},{w^{2}x^{2}},\ldots$), with coefficients that depend on the feature point coordinates.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Example 2", "weight": 1.0} -->

Note that since $\mathbf{M}$ is a $6 \times 6$ matrix, one may expect its determinant to have degree six monomials, however, due to special structure of $\mathbf{M}$, it is always possible to factor out $w^{2} + x^{2} + y^{2} + z^{2}$ from the determinant expression. Since ${w^{2} + x^{2} + y^{2} + z^{2}} = 1$, the degree four polynomial equation follows.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Example 2", "weight": 1.0} -->

What we showed in Example 2 was that three matched feature points generate a polynomial equation of the form. This equation is in terms of degree four monomials in $w,x,y,z$. Note that there are 35 such monomials, and their coefficients are in terms of the feature point coordinates. In practice, we do not need to calculate the determinant of $\mathbf{M}$ to find these coefficients. By replacing the feature point coordinates with symbolic expressions the determinant can be computed symbolically, and explicit formulas for the coefficients can be derived. By substituting the numerical values of point coordinates in these formulas the coefficients are calculated directly. Due to the space limitation we do not give the explicit formulas here.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Example 2", "weight": 1.0} -->

Since any three feature points give a polynomial equation of the form, from $n$ points $\binom{n}{3}$ equations can be generated. These equations can be stacked into a matrix-vector form, where the vector consists of the unknown monomial terms. The following example illustrates this point.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Example 3", "weight": 1.0} -->

Consider $\binom{6}{3} = 20$ polynomial equations of the form, generated from 6 feature points. These polynomial equations can be represented in the matrix-vector form where the coefficient matrix $\mathbf{A} \in {\mathbb{R}}^{20 \times 35}$ depends on the feature point coordinates, and vector $\mathbf{x} \in {\mathbb{R}}^{35}$ consists of all degree 4 monomials. Our goal is to find all $w,x,y,z$, for which is satisfied.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Example 3", "weight": 1.0} -->

The problem of recovering the rotation is henceforth equivalent to solving a system of equations of the form, where the goal is to find all $\mathbf{x}$ for which is satisfied. In, the coefficient matrix $\mathbf{A}$ is known from the feature point coordinates, and vector $\mathbf{x}$ is unknown with entries in degree four monomials of $w,x,y,z$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "The QuEst Algorithm", "weight": 1.0} -->

In what follows we first show how rotation solution candidates can be recovered from 7 and 6 matched feature points. Given a rotation solution candidate, it is then shown how the associated translation vector and depths are recovered. Lastly, we show how the unique solution can be distinguished by discarding the physically infeasible solution candidates. The Matlab implementation of QuEst is accessible at We will not discuss why the pose estimation problem has always more than one mathematically feasible solution (e.g., 2 for general points and 4 for coplanar points) since these results are well-known. Interested readers are referred to for further discussion and mathematical proofs on the number of solutions.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-A Recovering Rotation From 7 Points", "weight": 1.0} -->

Consider the system of equations for 7 matched feature points. Since 7 points generate $\binom{7}{3} = 35$ equations, in this case $\mathbf{A}$ is a $35 \times 35$ matrix. Due to the mathematical multiplicity of solutions however, $\mathbf{A}$ cannot be full rank (otherwise, only one solution exists, which is a contradiction).

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-A Recovering Rotation From 7 Points", "weight": 1.0} -->

Hence, 4 solution candidates are found by calculating the (unit norm) eigenvectors of $\mathbf{B}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "IV-A Recovering Rotation From 7 Points", "weight": 1.0} -->

We should mention that the choice of $\mathbf{x}_{1}$ and $\mathbf{x}_{2}$ are somewhat arbitrary. For example, we could have chosen $\mathbf{x}_{2}$ as $\mathbf{x}_{2}:=\begin{bmatrix} \end{bmatrix}^{\top}$, and derive a similar eigenvalue problem with $\lambda = \frac{y^{3}}{w^{3}}$. We will later use this fact to distinguish the unique solution.

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-B Recovering Rotation From 6 Points", "weight": 1.0} -->

Consider equation for 6 feature points. Since 6 feature points generate $\binom{6}{3} = 20$ equations, in this case $\mathbf{A}$ is a $20 \times 35$ full rank matrix.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-B Recovering Rotation From 6 Points", "weight": 1.0} -->

Equation allows us to construct an eigenvalue problem of the form ${\lambda\mathbf{v}} = {\mathbf{B}\mathbf{v}}$, with $\mathbf{B} \in {\mathbb{R}}^{20 \times 20}$. Indeed, let us choose $\lambda = \frac{x}{w}$, and consider the eigenvalue problem The entries of vector $x\mathbf{v}$ either belong to $\mathbf{x}_{2}$ or $\mathbf{x}_{1}$. For entries that belong to $\mathbf{x}_{2}$, the associated rows of $\mathbf{B}$ are chosen from the corresponding rows of $\overline{\mathbf{B}}$. For entries that belong to $\mathbf{x}_{1}$, rows of $\mathbf{B}$ are chosen as $\lbrack{0\ldots\, 010\ldots\, 0}\rbrack$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-B Recovering Rotation From 6 Points", "weight": 1.0} -->

The following example illustrates this procedure.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Example 4", "weight": 1.0} -->

Suppose entries of $\mathbf{x}_{1}$ and $\mathbf{x}_{2}$ are arranged as and assume that from the feature point coordinates we have derived as From we can construct the eigenvalue problem as where the first two entries of $x\mathbf{v}$ belong to $\mathbf{x}_{1} = {w\mathbf{v}}$, and hence their associated rows in $\mathbf{B}$ consist of zeros except for a single one entry. The third and last entries of $x\mathbf{v}$ belong to $\mathbf{x}_{2}$, and their associated rows come from $\overline{\mathbf{B}}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Example 4", "weight": 1.0} -->

Once the eigenvalue problem is constructed, 20 solution candidates for $\mathbf{v}$ are derived by computing the eigenvectors of $\mathbf{B}$. For each solution candidate, $w,x,y,z$ are found by calculating the third root of the $w^{3},x^{3},y^{3},z^{3}$ entries in $\mathbf{v}$. The recovered solution can be normalized to meet the unit norm constraint ${w^{2} + x^{2} + y^{2} + z^{2}} = 1$. Notice that by choosing $\mathbf{x}_{1}$ or $\lambda$ differently (e.g., $\lambda = \frac{y}{w}$) it is possible to derive different eigenvalue problems of the form.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-C Recovering Translation and Depths", "weight": 1.0} -->

Once quaternion elements $w,x,y,z$ are recovered, the corresponding rotation matrix $\mathbf{R}$ is given. Having $\mathbf{R}$, the rigid motion constraint ${{u\mathbf{R}\mathbf{m}} + \mathbf{t}} = {v\mathbf{n}}$ can now be written for all matched feature points, and stacked into the matrix-vector form where $\mathbf{I} \in {\mathbb{R}}^{3 \times 3}$ is the identity matrix, $k$ is the number feature points, $\mathbf{C} \in {\mathbb{R}}^{{{{3k} \times \, 2}k} + 3}$, and $\mathbf{y} \in {\mathbb{R}}^{{2k} + 3}$. Equation implies that $\mathbf{y}$ is in the null space of $\mathbf{C}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-C Recovering Translation and Depths", "weight": 1.0} -->

Thus, $\mathbf{y}$ can be found by calculating the rightmost singular vector of $\mathbf{C}$ (i.e., eigenvector of $\mathbf{C}^{\top}\mathbf{C}$ corresponding to the zero eigenvalue). Notice that $\mathbf{y}$ consists of the translation vector and feature point depths. Therefore, these parameters are recovered simultaneously and with a common scale factor.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-D The Unique Solution", "weight": 1.0} -->

Before we proceed with finding the unique solution, we need to briefly talk about the critical surfaces. Critical surfaces are special configurations of 3D points in the space for which one cannot distinguish a unique solution. (In this case the problem always has more than one physically realizable solution.) Perhaps the most important and practical example of such surfaces is when all 3D points lie on a plane, i.e., coplanar points. Coplanar points are abundant in aerial images (due to large distance of points from the camera) or images of the man-made environments (due to points lying on walls, floor, etc.). In what follows we will discuss the case of general and coplanar points separately.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-D The Unique Solution", "weight": 1.0} -->

Since feature points that are reflected with respect to the origin of the camera frame produce the same image, to detect the physically infeasible solutions one should check the chirality. Solution with the wrong chirality correspond to points that are behind the camera, and therefore have negative depths. Hence, physically infeasible solution candidates can be detected and discarded after recovering the depths.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-D1 General points", "weight": 1.0} -->

As discussed at the end of Sections IV-A and IV-B, by choosing other values for $\lambda$ (e.g. $\lambda = {\frac{y}{w},\frac{z}{w}}$) similar eigenvalue problems of the form and can be derived. Since the correct solution must satisfy the eigenvalue problem regardless of the chosen $\lambda$, solution candidates that do not satisfy ${\lambdav} = {\mathbf{B}v}$ for all values of $\lambda$ can be discarded. In this case, two mathematically feasible solutions remain, from which the unique solution is determined by checking the chirality.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-D2 Coplanar points", "weight": 1.0} -->

When points are coplanar (or more generally lie on critical surfaces), four mathematically feasible solutions remain after checking ${\lambdav} = {\mathbf{B}v}$ for different values of $\lambda$. Two of these solutions can be discarded by checking the chirality. To determine the solution uniquely further information is required (e.g., a third view or the normal vector to the plane).

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-D2 Coplanar points", "weight": 1.0} -->

Although in theory the methods discussed above can eliminate infeasible solution candidates, in practice pixelization noise and matching imperfections may result in choosing the wrong solution. For instance, in applications where parallax is small (i.e., translation between the views is much smaller than the average distance of the 3D points to the camera), recovering the depths becomes an ill-conditioned problem. Thus, checking the chirality may result in the wrong conclusion. Furthermore, with noise, coplanar points may appear as if they are at general positions and instead of two only one solution is returned. It is therefore recommended to always keep the best four solution candidates, and use the Random Sample Consensus (RANSAC) algorithm to find the unique solution.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Noise and Time Benchmarks", "weight": 1.0} -->

We benchmark our proposed algorithm against some of the most well-known algorithms such as the essential matrix 8-point, 7-point, and 6-point algorithms, and the Euclidean homography algorithm. For the first three algorithms the Stewenius's implementation, and for the latter Hartley's implementation in Matlab are used. We refer to the algorithms presented in this paper for 6 and 7 points respectively as QuEst 6 and QuEst 7.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Noise and Time Benchmarks", "weight": 1.0} -->

Each Monte Carlo simulation consists of eight randomly generated 3D points with uniform distribution inside a rectangular parallelepiped in front of the camera at the initial location. The camera is moved to a second location by a random translation and rotation quaternion, with uniform distribution within a bounded box of ${\mathbb{R}}^{3}$ and on the 3-sphere, respectively. Coordinates of the feature points on the image plane are computed by projecting the 3D points on the image planes. Each algorithm is provided with the minimum number of points it requires to compute the pose.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-A Noise Benchmarks", "weight": 1.0} -->

To evaluate the performance under noise, Gaussian noise with zero mean and standard deviation ranging from 0 to 10 pixels is added to all image coordinates. The noise standard deviation is increased by 0.1 pixel increments, and for each noise increment 100 simulations are generated. As mentioned in Section IV-D, the chirality condition is sensitive to noise, so to avoid choosing the wrong solution, the solution candidate that is closest to the ground truth is chosen as the best pose estimate for each algorithm. The estimation error for rotation is defined by where $\mathbf{q} = {\lbrack{wxyz}\rbrack}^{\top}$ is the rotation estimated from the noisy images, and $\mathbf{q}^{\ast}$ is the ground truth rotation in quaternions. Note that defines a metric on the rotation quaternion space.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-A Noise Benchmarks", "weight": 1.0} -->

Similarly, the estimation error for translation is defined by where $\mathbf{t}_{\mathbf{n}}$ and $\mathbf{t}_{\mathbf{n}}^{\ast}$ are the estimated translation vector and the ground truth, respectively, normalized to have unit norm (because the magnitude of the recovered translation vector can vary depending on the algorithm).

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-A Noise Benchmarks", "weight": 1.0} -->

To analyze the performance when points are on critical surfaces, the previous analysis is repeated for coplanar points, where the points are chosen randomly on a bounded plane with uniform distribution. The mean of the rotation and translation estimation errors for noise standard deviation varying from 0 to 2 is shown in Fig. 4. As can be seen from the figure, homography shows the best noise resilience when the standard deviation is small (approximately 1 to 1.5 pixels). This is because the homography algorithm is specifically designed to recover the pose when points are coplanar. QuEst 6 has the next best estimation accuracy. When points are on critical surfaces matrix $\mathbf{A}_{2}$ in loses rank and becomes rank 27. Hence, multiplication by $\mathbf{A}_{2}^{\dagger}$ will not result, and QuEst 7 fails to recover the pose. On the other hand, $\mathbf{A}_{2}$ used for QuEst 6 in remains full rank due to having smaller dimensions.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-A Noise Benchmarks", "weight": 1.0} -->

Lastly, none of the algorithms that are based on the essential matrix can recover the pose in this case, regardless of the number of points used in the algorithm or the magnitude of noise (see for further explanation).

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-A Noise Benchmarks", "weight": 1.0} -->

In conclusion, QuEst 6 shows the best performance since the pose is estimated correctly regardless of the 3D point configuration, and the estimation is robust to noise and outliers.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-B Time Benchmarks", "weight": 1.0} -->

Table II lists the average execution time of all algorithms in milliseconds, where 1000 Monte Carlo simulations with both coplanar and general points and various noise magnitudes are used to generate the results. All algorithms are implemented as Mex files in Matlab, and tested on the same platform with Intel's 4th Gen i-7 CPU. Algorithms that use homography or essential matrix have smaller execution time since fewer operations are needed to estimate these matrices. QuEst has a larger execution time since the rotation and translation are recovered independently. We should emphasize that although QuEst is not at fast as other algorithms, it is fast enough to be used with RANSAC in real-time applications. Furthermore, since QuEst recovers the pose regardless of the 3D point configuration, no prior effort is required to detect the coplanarity and choose the appropriate algorithm correspondingly.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Real World Performance", "weight": 1.0} -->

To further assess the accuracy and robustness of QuEst, images from four real world datasets are used to estimate the pose and compare the results with the ground truth that is provided by the dataset. Datasets used for the comparison are ICL, KITTI, NAIST, and TUM, where SURF image feature points are extracted and matched between two consecutive keyframes. Each algorithm is provided with the minimum number of points it requires to estimate the pose, where points with the highest matching score are chosen. To test the robustness of the algorithms, RANSAC is not used, and the provided set of matched points can occasionally have outliers.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Real World Performance", "weight": 1.0} -->

The ICL-NUIM dataset consists of computer-generated renderings of 3D scenes. These artificial images are accompanied by exact ground truth information, and their main purpose is to benchmark 3D reconstruction algorithms. The KITTI and TUM datasets were created to evaluate SLAM algorithms. The KITTI dataset consists of outdoor stereo image sequences taken from a moving vehicle. The images are accompanied by LIDAR, IMU and GPS measurements, so full pose information is provided in the left camera frame. The TUM dataset is comprised of indoor images as well as point depth information from a RGB-D camera. The RGB-D camera poses were recorded by using an optical tracking system, with millimeter-level accuracy. The NAIST campus sequences are part of an Augmented Reality benchmark called TrakMark. The ground truth files for these sequences were created by solving a PnP problem from known 3D world point coordinates, acquired using high precision surveying equipment. The images come from a handheld camera, with the operator walking while capturing some sequences and running for others.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Real World Performance", "weight": 1.0} -->

Since the chosen feature points may not be coplanar, the homography algorithm does not return the correct solution in general. The pose estimated by the 6-point and 7-point algorithms has smaller median error compared to the 8-point algorithm. The translation estimated by QuEst 7 has the smallest median error due to the additional point. The rotation estimated by Quest 6 shows the best performance due to having smaller median errors, 0.25 and 0.75 quartiles, and outliers for all datasets.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

By using quaternion representation of rotation, we formulated the camera pose estimation problem and presented the QuEst algorithm to recover the relative pose between two camera views. Unlike the existing homography or essential matrix based methods, QuEst decouples the rotation and translation estimation, and recovers the pose correctly for both cases of general and coplanar points. QuEst can be used to initialize the bundle adjustment algorithm in applications such as SLAM without needing to resort to heuristic methods to detect the coplanarity of the points. Using both simulated and real world images, we demonstrated the estimation accuracy and robustness of QuEst in comparison to the commonly used algorithms. We have made the Matlab implementation of QuEst available online and free. Future work includes the online release of the C++ implementation of QuEst with RANSAC.
