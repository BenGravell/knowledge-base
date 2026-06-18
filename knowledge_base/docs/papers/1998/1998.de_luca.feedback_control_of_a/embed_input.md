<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Feedback Control of a Nonholonomic Car-like Robot

Topics include Nonholonomic robots, Car-like robots, Mobile robot control, Feedback control, Path following, Trajectory tracking, Motion planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Surveys and organizes feedback-control techniques for nonholonomic car-like robots, connecting low-level stabilization and tracking with the motion-planning layer that supplies feasible paths or goals. The chapter is a compact reference for how posture regulation, path following, and trajectory tracking differ in wheeled mobile robots.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The subject of this chapter is the control problem for nonholonomic wheeled mobile robots moving on the plane, and in particular the use of feedback techniques for achieving a given motion task. In automatic control, feedback improves system performance by allowing the successful completion of a task even in the presence of external disturbances and/or initial errors. To this end, real-time sensor measurements are used to reconstruct the robot state. Throughout this study, the latter is assumed to be available at every instant, as provided by proprioceptive (e.g., odometry) or exteroceptive (sonar, laser) sensors. We will limit our analysis to the case of a robot workspace free of obstacles. In fact, we implicitly consider the robot controller to be embedded in a hierarchical architecture in which a higher-level planner solves the obstacle avoidance problem and provides a series of motion goals to the lower control layer. In this perspective, the controller deals with the basic issue of converting ideal plans into actual motion execution. Wherever appropriate, we shall highlight the interactions between feedback control and motion planning primitives, such as the generation of open-loop commands and the availability of a feasible smooth path joining the current robot position to the destination.
