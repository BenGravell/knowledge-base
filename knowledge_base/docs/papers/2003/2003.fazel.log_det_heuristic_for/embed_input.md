<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Log-det Heuristic for Matrix Rank Minimization with Applications to Hankel and Euclidean Distance Matrices

Topics include Rank minimization, Log-det heuristic, Semidefinite programming, Low-rank matrices, Hankel matrices, Euclidean distance matrices, Iterative reweighting.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces a log-determinant heuristic for low-rank positive-semidefinite matrix recovery, solved by iteratively minimizing weighted trace objectives. The paper extends the heuristic to general matrices and demonstrates applications in system realization and Euclidean-distance-matrix embedding.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a heuristic for minimizing the rank of a positive semidefinite matrix over a convex set. We use the logarithm of the determinant as a smooth approximation for rank, and locally minimize this function to obtain a sequence of trace minimization problems. We then present a lemma that relates the rank of any general matrix to that of a corresponding positive semidefinite one. Using this, we readily extend the proposed heuristic to handle general matrices. We examine the vector case as a special case, where the heuristic reduces to an iterative l/sub 1/-norm minimization technique. As practical applications of the rank minimization problem and our heuristic, we consider two examples: minimum-order system realization with time-domain constraints, and finding lowest-dimension embedding of points in a Euclidean space from noisy distance data.
