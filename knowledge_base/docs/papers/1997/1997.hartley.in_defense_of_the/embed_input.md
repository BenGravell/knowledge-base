In Defense of the Eight-Point Algorithm

Topics include Structure from motion, Epipolar geometry, Fundamental matrix, Eight-point algorithm, Coordinate normalization, Numerical conditioning, Stereo vision.

Shows that the classical eight-point algorithm becomes numerically competitive when image points are translated and scaled before solving for the fundamental matrix. The paper reframes earlier failures as conditioning problems and made normalized coordinate preprocessing standard in two-view geometry.

The fundamental matrix is a basic tool in the analysis of scenes taken with two uncalibrated cameras, and the eight-point algorithm is a frequently cited method for computing the fundamental matrix from a set of eight or more point matches. It has the advantage of simplicity of implementation. The prevailing view is, however, that it is extremely susceptible to noise and hence virtually useless for most purposes. This paper challenges that view, by showing that by preceding the algorithm with a very simple normalization (translation and scaling) of the coordinates of the matched points, results are obtained comparable with the best iterative algorithms. This improved performance is justified by theory and verified by extensive experiments on real images.
