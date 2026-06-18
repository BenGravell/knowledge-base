<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Data-Driven Computation of Minimal Robust Control Invariant Set

Topics include Data-driven control, Robust control invariant sets, Robust optimization, System identification, Safety, Autonomous driving.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Computes low-complexity robust control invariant sets directly from data by coupling model-admissibility constraints with robust optimization. The paper is useful for safety-control pipelines where model identification and invariant-set computation should be solved together rather than sequentially.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a data-driven framework to compute an approximation of a minimal robust control invariant set (mRCI) for an uncertain dynamical system where the model of the system is also unknown and should be learned from data. First, the set of admissible models is characterized via a set of linear constraints extracted from the experimental data. Each model in the set of admissible models contains information about the nominal model, as well as the characterization of the model uncertainty, including additive and multiplicative uncertainties. Then an iterative algorithm based on robust optimization is proposed to simultaneously compute a minimal robust control invariant set while selecting an optimal model from the admissible set. The numerical results show that the proposed method greatly reduces the size of the invariant set compared to a benchmark method that sequentially selects a model with least squares and then computes the invariant set.
