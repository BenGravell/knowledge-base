<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Toward a More Complete, Flexible, and Safer Speed Planning for Autonomous Driving via Convex Optimization

Topics include Speed planning, Autonomous driving, Convex optimization, Constraints, Safety, Comfort, Mobility, Flexibility.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Extends convex-optimization-based speed planning to handle a broader set of constraints (comfort, safety, traffic rules) more completely and flexibly than prior approaches, demonstrated on autonomous driving scenarios.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we present a complete, flexible and safe convex-optimization-based method to solve speed planning problems over a fixed path for autonomous driving in both static and dynamic environments. Our contributions are five fold. First, we summarize the most common constraints raised in various autonomous driving scenarios as the requirements for speed planner developments and metrics to measure the capacity of existing speed planners roughly for autonomous driving. Second, we introduce a more general, flexible and complete speed planning mathematical model including all the summarized constraints compared to the state-of-the-art speed planners, which addresses limitations of existing methods and is able to provide smooth, safety-guaranteed, dynamic-feasible, and time-efficient speed profiles. Third, we emphasize comfort while guaranteeing fundamental motion safety without sacrificing the mobility of cars by treating the comfort box constraint as a semi-hard constraint in optimization via slack variables and penalty functions, which distinguishes our method from existing ones. Fourth, we demonstrate that our problem preserves convexity with the added constraints, thus global optimality of solutions is guaranteed. Fifth, we showcase how our formulation can be used in various autonomous driving scenarios by providing several challenging case studies in both static and dynamic environments.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A range of numerical experiments and challenging realistic speed planning case studies have depicted that the proposed method outperforms existing speed planners for autonomous driving in terms of constraint type covered, optimality, safety, mobility and flexibility.
