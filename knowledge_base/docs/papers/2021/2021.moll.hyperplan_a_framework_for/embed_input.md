<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Hyperplan: A Framework for Motion Planning Algorithm Selection and Parameter Optimization

Topics include Robotics, Motion planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Formulates motion-planning algorithm selection and parameter tuning as a hyperparameter optimization problem over planners, planner parameters, robots, and problem classes. HyperPlan contributes loss-function designs for planning speed and path quality, and its Fetch and Baxter experiments show that optimized planner configurations can outperform defaults and often generalize beyond the exact scenes used for tuning.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Over the years, many motion planning algorithms have been proposed. It is often unclear which algorithm might be best suited for a particular class of problems. The problem is compounded by the fact that algorithm performance can be highly dependent on parameter settings. This paper shows that hyperparameter optimization is an effective tool in both algorithm selection and parameter tuning over a given set of motion planning problems. We present different loss functions for optimization that capture different notions of optimality. The approach is evaluated on a broad range of scenes using two different manipulators, a Fetch and a Baxter. We show that optimized planning algorithm performance significantly improves upon baseline performance and generalizes broadly in the sense that performance improvements carry over to problems that are very different from the ones considered during optimization.
