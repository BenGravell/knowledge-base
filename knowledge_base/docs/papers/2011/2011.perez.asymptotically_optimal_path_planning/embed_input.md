<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Asymptotically-optimal Path Planning for Manipulation Using Incremental Sampling-based Algorithms

Topics include Rapidly-exploring random tree star, Manipulation planning, Sampling-based planning, Asymptotic optimality, Sparse sampling, Collision checking, Motion planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Adapts asymptotically optimal sampling-based planning to manipulation by combining RRT* with sparse sampling and memoized collision checking. The result quickly finds feasible manipulation paths and then improves them with more computation, giving better initial and final path quality in high-dimensional PR2 planning problems.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A desirable property of path planning for robotic manipulation is the ability to identify solutions in a sufficiently short amount of time to be usable. This is particularly challenging for the manipulation problem due to the need to plan over high-dimensional configuration spaces and to perform computationally expensive collision checking procedures. Consequently, existing planners take steps to achieve desired solution times at the cost of low quality solutions. This paper presents a planning algorithm that overcomes these difficulties by augmenting the asymptotically-optimal RRT* with a sparse sampling procedure. With the addition of a collision checking procedure that leverages memoization, this approach has the benefit that it quickly identifies low-cost feasible trajectories and takes advantage of subsequent computation time to refine the solution towards an optimal one. We evaluate the algorithm through a series of Monte Carlo simulations of seven, twelve, and fourteen degree of freedom manipulation planning problems in a realistic simulation environment. The results indicate that the proposed approach provides significant improvements in the quality of both the initial solution and the final path, while incurring almost no computational overhead compared to the RRT algorithm. We conclude with a demonstration of our algorithm for single-arm and dual-arm planning on Willow Garage's PR2 robot.
