<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

N4SID: Numerical Algorithms for State Space Subspace System Identification

Topics include System identification, Subspace identification, Subspace methods, State-space models, N4SID, Kalman filter, Riccati equation, QR decomposition, Singular value decomposition.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces the N4SID algorithm, which identifies linear state-space models from input-output data using projections of block Hankel matrices, providing a numerically robust approach to subspace system identification.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Recently a great deal of attention has been given to numerical algorithms for subspace state space system identication (N4SID). In this paper, we derive two new N4SID algorithms to identify mixed deterministic-stochastic systems. Both algorithms determine state sequences through the projection of input and output data. These state sequences are shown to be outputs of non-steady state Kalman filter banks. From these it is easy to determine the state space system matrices. The N4SID algorithms are always convergent (non-iterative) and numerically stable since they only make use of QR and Singular Value Decompositions. Both N4SID algorithms are similar, but the second one trades off accuracy for simplicity. These new algorithms are compared with existing subspace algorithms in theory and in practice.
