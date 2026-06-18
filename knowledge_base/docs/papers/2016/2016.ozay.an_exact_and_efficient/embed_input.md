<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

An Exact and Efficient Algorithm for Segmentation of ARX Models

Topics include System identification, ARX models, Dynamic programming, Switched systems, Change detection, Convex relaxation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Shows that ARX model segmentation can be solved exactly in polynomial time with dynamic programming under broad fitting-error conditions. The paper is a useful counterpoint to convex-relaxation approaches because it preserves computational efficiency while improving optimality guarantees and making model-complexity tradeoff sweeps cheap.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider the problem of segmentation of autoregressive models with exogenous inputs (ARX models). This problem, where the goal is to determine the parameters of a sequence of ARX models that can explain a given input/output data within some noise bound, has attracted considerable attention in recent years. Most of the recently proposed approaches are based on convex relaxations. Although efficient, these approaches do not necessarily lead to optimal solutions. In the present paper, by exploiting some early results in dynamic programming, we show that an optimal solution can indeed be obtained in polynomial-time. One salient feature of the proposed approach is that exploration of the model complexity/quality of the fit trade-off space comes with negligible additional computational cost. We discuss several other properties of the proposed approach and compare it with existing approaches on numerical examples, which show that the proposed approach is consistently faster.
