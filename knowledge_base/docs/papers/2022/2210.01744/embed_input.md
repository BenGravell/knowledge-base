Bang-Bang Boosting of RRTs

Topics include Kinodynamic planning, Rapidly-exploring random tree, Bang-bang control, Steering function, Double integrator, Time-optimal control.

Derives a complete, exact bang-bang time-optimal steering method for synchronized double integrators, using it to boost RRT performance via better BVP solving, improved Voronoi bias metrics, and post-hoc trajectory time-optimization.

This paper presents methods for dramatically improving the performance of sampling-based kinodynamic planners. The key component is the first-known complete, exact steering method that produces a time-optimal trajectory between any states for a vector of synchronized double integrators. This method is applied in three ways: 1) to generate RRT edges that quickly solve the two-point boundary-value problems, 2) to produce a (quasi)metric for more accurate Voronoi bias in RRTs, and 3) to iteratively time-optimize a given collision-free trajectory. Experiments are performed for state spaces with up to 2000 dimensions, resulting in improved computed trajectories and orders of magnitude computation time improvements over using ordinary metrics and constant controls.

## INTRODUCTION

Rapidly exploring random trees were originally introduced as an approach to motion planning with differential constraints and dynamics. The idea was to incrementally grow a space-filling tree by applying controls so that two-point boundary-value problems could be avoided if popular methods such as probabilistic roadmaps were applied to these problems. Curiously, RRTs have found more success over the past decades for basic path planning (no differential constraints and dynamics), rather than their intended target, the kinodynamic planning problem.

Although this phenomenon is partly due to larger mainstream interest since the 1990s in basic path planning, it is primarily due to the additional challenges posed by the harder problems. Computational performance depends greatly how well the RRT nearest-neighbor metric approximates the true, optimal cost-to-go function, which is presumably unattainable. Furthermore, efficient steering methods or motion primitives are often needed to enhance performance, rather than applying constant controls as in....

We have proposed, analyzed, and implemented methods that accelerate planning performance and optimize solutions. The key is our new steering method that quickly computes bang-bang time-optimal controls using exact, parabolic solutions. Although the study has been limited to RRTs, we expect it could enhance other sampling-based planning methods that rely on distance metrics or steering, such as probabilistic roadmaps or expansive space trees....

The encouraging results of this paper lead naturally to many new questions and further studies. The implementation focused mainly on $n$-double-integrator dynamics; however, with the vehicle-in-the-tube results from Section V-C, we have easily extended it for acceleration bounds that vary with state. This opens exciting directions of research to adapt the method to many more classes of stabilizable systems....

## PLANNING METHODS

To extend the result to a vector of double integrators, a waiting method is needed so that each double integrator arrives at its goal in its phase plane at the same time. This problem was considered in, but only for the limited case in which their final velocities are zero. It was also considered in, but the gap problem, introduced shortly, was neglected....
