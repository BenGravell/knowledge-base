Path Planning in 1000+ Dimensions Using a Task-space Voronoi Bias

Topics include High-dimensional planning, Task-space bias, Motion planning, Sampling-based planning, Robotics, Voronoi bias.

Uses a task-space Voronoi bias to guide sampling-based planning in systems with thousands of configuration dimensions. The paper shows that carefully chosen low-dimensional task structure can make otherwise intractable high-dimensional planning problems approachable.

The reduction of the kinematics and/or dynamics of a high-DOF robotic manipulator to a low-dimension task space has proven to be an invaluable tool for designing feedback controllers. When obstacles or other kinodynamic constraints complicate the feedback design process, motion planning techniques can often still find feasible paths, but these techniques are typically implemented in the high-dimensional configuration (or state) space. Here we argue that providing a Voronoi bias in the task space can dramatically improve the performance of randomized motion planners, while still avoiding non-trivial constraints in the configuration (or state) space. We demonstrate the potential of task-space search by planning collision-free trajectories for a 1500 link arm through obstacles to reach a desired end-effector position.
