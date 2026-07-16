<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Curvature Aware Motion Planning with Closed-Loop Rapidly-exploring Random Trees

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The road's geometry strongly influences the path planner's performance, critical for autonomous navigation in high-speed dynamic scenarios (e.g., highways). Hence, this paper introduces the Curvature-aware Rapidly-exploring Random Trees (CA-CL-RRT), whose planning performance is invariant to the road's geometry. We propose a transformation strategy that allows us to plan on a virtual straightened road and then convert the planned motion to the curved road. It is shown that the proposed approach substantially improves path planning performance on curved roads as compared to prior RRT-based path planners. Moreover, the proposed CA-CL-RRT is combined with a Local Model Predictive Contour Controller (LMPCC) for path tracking while ensuring collision avoidance through constraint satisfaction. We present quantitative and qualitative performance results in two navigation scenarios: dynamic collision avoidance and structured highway driving. The results demonstrate that our proposed navigation framework improves the path quality on curved highway roads and collision avoidance with dynamic obstacles.
