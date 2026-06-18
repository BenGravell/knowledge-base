<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Subspace Model Identification Part 1. The Output-Error State-Space Model Identification Class of Algorithms

Topics include System identification, Subspace identification, Multivariable output-error state-space, Output-error models, State-space models, Linear systems, MIMO systems, RQ factorization, Singular value decomposition, Realization theory.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces the MOESP family of subspace system identification algorithms for realizing finite-dimensional linear state-space models from multivariable input-output data. The paper presents elementary and ordinary MOESP schemes organized around RQ factorization, singular value decomposition, and linear least-squares realization steps, establishing a computational template that became a standard alternative to prediction-error and maximum-likelihood identification methods for MIMO systems.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we present two novel algorithms to realize a finite dimensional, linear time-invariant state-space model from input-output data. The algorithms have a number of common features. They are classified as one of the subspace model identification schemes, in that a major part of the identification problem consists of calculating specially structured subspaces of spaces defined by the input-output data. This structure is then exploited in the calculation of a realization. Another common feature is their algorithmic organization: an RQ factorization followed by a singular value decomposition and the solution of an overdetermined set (or sets) of equations. The schemes assume that the underlying system has an output-error structure and that a measurable input sequence is available. The latter characteristic indicates that both schemes are versions of the MIMO Output-Error State Space model identification (MOESP) approach. The first algorithm is denoted in particular as the (elementary MOESP scheme). The subspace approximation step requires, in addition to input-output data, knowledge of a restricted set of Markov parameters. The second algorithm, referred to as the (ordinary MOESP scheme), solely relies on input-output data. A compact implementation is presented of both schemes.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Although we restrict our presentation here to error-free input-output data, a framework is set up in an identification context. The identification aspects of the presented realization schemes are treated in the forthcoming Parts 2 and 3.
