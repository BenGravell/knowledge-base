<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

SafeFlow: Safe Robot Motion Planning with Flow Matching via Control Barrier Functions

Topics include Flow matching, Control barrier functions, Safe motion planning, Trajectory generation, Robot manipulation, Test-time constraints.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Combines flow matching with flow matching barrier functions to enforce trajectory safety at inference time without retraining. Experiments evaluate constrained navigation and seven-degree-of-freedom manipulation in previously unseen environments.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Recent advances in generative modeling have led to promising results in robot motion planning, particularly through diffusion and flow matching (FM)-based models that capture complex, multimodal trajectory distributions. However, these methods are typically trained offline and remain limited when faced with new environments with constraints, often lacking explicit mechanisms to ensure safety during deployment. In this work, safe flow matching (SafeFlow), a motion planning framework, is proposed for trajectory generation that integrates flow matching with safety guarantees. SafeFlow leverages our proposed flow matching barrier functions (FMBF) to ensure the planned trajectories remain within safe regions across the entire planning horizon. Crucially, our approach enables training-free, real-time safety enforcement at test time, eliminating the need for retraining. We evaluate SafeFlow on a diverse set of tasks, including planar robot navigation and 7-DoF manipulation, demonstrating superior safety and planning performance compared to state-of-the-art generative planners. Comprehensive resources are available on the project website:.
