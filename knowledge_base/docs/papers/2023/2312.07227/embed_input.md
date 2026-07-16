<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Scalarizing Multi-Objective Robot Planning Problems Using Weighted Maximization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

When designing a motion planner for autonomous robots there are usually multiple objectives to be considered. However, a cost function that yields the desired trade-off between objectives is not easily obtainable. A common technique across many applications is to use a weighted sum of relevant objective functions and then carefully adapt the weights. However, this approach may not find all relevant trade-offs even in simple planning problems. Thus, we study an alternative method based on a weighted maximum of objectives. Such a cost function is more expressive than the weighted sum, and we show how it can be deployed in both continuous- and discrete-space motion planning problems. We propose a novel path planning algorithm for the proposed cost function and establish its correctness, and present heuristic adaptations that yield a practical runtime. In extensive simulation experiments, we demonstrate that the proposed cost function and algorithm are able to find a wider range of trade-offs between objectives (i.e., Pareto-optimal solutions) for various planning problems, showcasing its advantages in practice.
