<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Trajectory Planning for Quadrotor Swarms

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We describe a method for multirobot trajectory planning in known, obstacle-rich environments. We demonstrate our approach on a quadrotor swarm navigating in a warehouse setting. Our method consists of following three stages: 1) roadmap generation that generates sparse roadmaps annotated with possible interrobot collisions; 2) discrete planning that finds valid execution schedules in discrete time and space; 3) continuous refinement that creates smooth trajectories. We account for the downwash effect of quadrotors, allowing safe flight in dense formations. We demonstrate computational efficiency in simulation with up to 200 robots and physical plausibility with an experiment on 32 nano-quadrotors. Our approach can compute safe and smooth trajectories for hundreds of quadrotors in dense environments with obstacles in a few minutes.
