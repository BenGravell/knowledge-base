<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

iSAM: Incremental Smoothing and Mapping

Topics include Simultaneous localization and mapping, Incremental smoothing, Factor graphs, Sparse matrices, Robot mapping, State estimation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces iSAM, an incremental smoothing approach for SLAM that updates a sparse factorization as new measurements arrive. It shifted practical SLAM toward factor-graph smoothing methods that preserve accuracy while avoiding full batch recomputation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we present incremental smoothing and mapping (iSAM), which is a novel approach to the simultaneous localization and mapping problem that is based on fast incremental matrix factorization. iSAM provides an efficient and exact solution by updating a QR factorization of the naturally sparse smoothing information matrix, thereby recalculating only those matrix entries that actually change. iSAM is efficient even for robot trajectories with many loops as it avoids unnecessary fill-in in the factor matrix by periodic variable reordering. Also, to enable data association in real time, we provide efficient algorithms to access the estimation uncertainties of interest based on the factored information matrix. We systematically evaluate the different components of iSAM as well as the overall algorithm using various simulated and real-world datasets for both landmark and pose-only settings.
