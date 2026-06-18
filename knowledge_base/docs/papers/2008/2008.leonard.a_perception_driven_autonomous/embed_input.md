<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Perception-driven Autonomous Urban Vehicle

Topics include Autonomous vehicles, Urban challenge, Perception, Planning, Robotics systems, Field robotics.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Describes an autonomous urban vehicle architecture organized around perception-driven behavior and planning. The paper is most useful as a systems account of how sensing, mapping, prediction, and control were integrated for real-world urban driving.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper describes the architecture and implementation of an autonomous passenger vehicle designed to navigate using locally perceived information in preference to potentially inaccurate or incomplete map data. The vehicle architecture was designed to handle the original DARPA Urban Challenge requirements of perceiving and navigating a road network with segments defined by sparse waypoints. The vehicle implementation includes many heterogeneous sensors with significant communications and computation bandwidth to capture and process high‐resolution, high‐rate sensor data. The output of the comprehensive environmental sensing subsystem is fed into a kinodynamic motion planning algorithm to generate all vehicle motion. The requirements of driving in lanes, three‐point turns, parking, and maneuvering through obstacle fields are all generated with a unified planner. A key aspect of the planner is its use of closed‐loop simulation in a rapidly exploring randomized trees algorithm, which can randomly explore the space while efficiently generating smooth trajectories in a dynamic and uncertain environment. The overall system was realized through the creation of a powerful new suite of software tools for message passing, logging, and visualization. These innovations provide a strong platform for future research in autonomous driving in global positioning system–denied and highly dynamic environments with poor a priori information.
