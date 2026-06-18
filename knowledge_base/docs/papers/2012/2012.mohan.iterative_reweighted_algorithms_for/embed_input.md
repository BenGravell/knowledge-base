<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Iterative Reweighted Algorithms for Matrix Rank Minimization

Topics include Rank minimization, Matrix completion, Iterative reweighting, Nuclear norm, Low-rank recovery, MovieLens, IRLS.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Proposes IRLS-p and related smoothed iterative reweighted least-squares methods for affine rank minimization, aiming to improve on plain nuclear-norm relaxation. The paper combines recovery guarantees for the p=1 case with empirical evidence that nonconvex p<1 variants recover lower-rank matrices more often and run competitively on random matrix-completion tasks and MovieLens data.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The problem of minimizing the rank of a matrix subject to affine constraints has applications in several areas including machine learning, and is known to be NP-hard. A tractable relaxation for this problem is nuclear norm or trace norm minimization, which is guaranteed to find the minimum rank matrix under suitable assumptions. In this paper, we propose a family of Iterative Reweighted Least Squares algorithms IRLS-p, with 0 <= p <= 1, as a computationally efficient way to improve over the performance of nuclear norm minimization. The algorithms can be viewed as locally minimizing certain smooth approximations to the rank function. When p = 1, we give theoretical guarantees similar to those for nuclear norm minimization, that is, recovery of low-rank matrices under certain assumptions on the operator defining the constraints. For p < 1, IRLS-p shows better empirical performance in terms of recovering low-rank matrices than nuclear norm minimization. We provide an efficient implementation for IRLS-p, and also present a related family of algorithms, sIRLS-p.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

These algorithms exhibit competitive run times and improved recovery when compared to existing algorithms for random instances of the matrix completion problem, as well as on the MovieLens movie recommendation data set.
