<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Director: A User Interface Designed for Robot Operation with Shared Autonomy

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Operating a high degree of freedom mobile manipulator, such as a humanoid, in a field scenario requires constant situational awareness, capable perception modules, and effective mechanisms for interactive motion planning and control. A well-designed operator interface presents the operator with enough context to quickly carry out a mission and the flexibility to handle unforeseen operating scenarios robustly. By contrast, an unintuitive user interface can increase the risk of catastrophic operator error by overwhelming the user with unnecessary information. With these principles in mind, we present the philosophy and design decisions behind Director - the open-source user interface developed by Team MIT to pilot the Atlas robot in the DARPA Robotics Challenge (DRC). At the heart of Director is an integrated task execution system that specifies sequences of actions needed to achieve a substantive task, such as drilling a wall or climbing a staircase. These task sequences, developed a priori, make online queries to automated perception and planning algorithms with outputs that can be reviewed by the operator and executed by our whole-body controller. Our use of Director at the DRC resulted in efficient high-level task operation while being fully competitive with approaches focusing on teleoperation by highly-trained operators.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We discuss the primary interface elements that comprise the Director and provide analysis of its successful use at the DRC.
