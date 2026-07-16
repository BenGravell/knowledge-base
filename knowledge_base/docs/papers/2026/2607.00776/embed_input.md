<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

From Prediction Uncertainty to Conformalized Distance Fields for Safe Motion Planning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Safe motion planning in dynamic environments requires reasoning about the uncertainty in predicted obstacle motion without sacrificing real-time performance. Existing conformal approaches conformalize a scalar score that aggregates per-obstacle prediction errors, losing spatial coherence and scaling poorly with scene density. We instead conformalize the entire predicted distance field at once. This functional conformal prediction (FCP) framework yields a distribution-free, field-level lower bound, from which safety follows uniformly: any trajectory satisfying the resulting constraint is certified safe, independent of how the control space is sampled. The key enabler is that the residual distance field is empirically low-rank and approximately time-invariant, which makes the bound decomposable in coefficient space. An envelope is fitted offline via functional PCA and a Gaussian-mixture inductive conformal procedure, then refined online by a lightweight adaptive functional conformal (AFCP) update on a low-dimensional vector. This keeps the per-step cost largely insensitive to obstacle count and retains long-run field coverage under distribution shift. We embed the envelope as a tightened safety constraint in a sampling-based model predictive controller, FCP-MPC.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

On the ETH-UCY pedestrian benchmarks and a dense 3D quadrotor task with up to 280 dynamic obstacles, FCP-MPC attains a favorable balance of safety, feasibility, and efficiency, reaching goals where pointwise and egocentric conformal baselines become too conservative or too expensive, while keeping per-step computation far below online uncertainty-reasoning baselines.
