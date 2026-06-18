<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sparse and Low-rank Matrix Decompositions

Topics include Sparse models, Low-rank models, Matrix decomposition, Convex geometry, Identifiability, Semidefinite programming.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Analyzes when a matrix can be decomposed into sparse and low-rank components using convex optimization. The work gives geometric identifiability conditions that later influenced robust PCA and latent-variable graphical model selection.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider the following fundamental problem: given a matrix that is the sum of an unknown sparse matrix and an unknown low-rank matrix, is it possible to exactly recover the two components? Such a capability enables a considerable number of applications, but the goal is both ill-posed and NP-hard in general. In this paper we develop (a) a new uncertainty principle for matrices, and (b) a simple method for exact decomposition based on convex optimization. Our uncertainty principle is a quantification of the notion that a matrix cannot be sparse while having diffuse row/column spaces. It characterizes when the decomposition problem is ill-posed, and forms the basis for our decomposition method and its analysis. We provide deterministic conditions - on the sparse and low-rank components - under which our method guarantees exact recovery.
