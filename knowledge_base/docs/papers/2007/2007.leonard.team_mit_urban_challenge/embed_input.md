<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Team MIT Urban Challenge Technical Report

Topics include Autonomous driving, DARPA urban challenge, Sensor fusion, Motion planning, Robotic perception.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Describes the MIT Urban Challenge vehicle architecture, integrating inexpensive sensors, locally smooth perception, traffic interpretation, kinodynamic planning, and autonomous control.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This technical report describes Team MIT’s approach to the DARPA Urban Challenge. We have developed a novel strategy for using many inexpensive sensors, mounted on the vehicle periphery, and calibrated with a new cross-modal calibration technique. Lidar, camera, and radar data streams are processed using an innovative, locally smooth state representation that provides robust perception for real-time autonomous control. A resilient planning and control architecture has been developed for driving in traffic, comprised of an innovative combination of well-proven algorithms for mission planning, situational planning, situational interpretation, and trajectory control. These innovations are being incorporated in two new robotic vehicles equipped for autonomous driving in urban environments, with extensive testing on a DARPA site visit course. Experimental results demonstrate all basic navigation and some basic traffic behaviors, including unoccupied autonomous driving, lane following using pure-pursuit control and our local frame perception strategy, obstacle avoidance using kino-dynamic RRT path planning, U-turns, and precedence evaluation amongst other cars at intersections using our situational interpreter. We are working to extend these approaches to advanced navigation and traffic scenarios.
