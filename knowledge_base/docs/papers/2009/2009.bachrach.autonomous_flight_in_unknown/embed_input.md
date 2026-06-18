<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Autonomous Flight in Unknown Indoor Environments

Topics include Autonomous flight, Indoor navigation, MAVs, Simultaneous localization and mapping, Exploration, Robot perception.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Demonstrates autonomous flight through unknown indoor environments using onboard sensing, mapping, planning, and control. The paper is a field-robotics systems contribution showing that small aerial vehicles can operate without prior maps or GPS.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents our solution for enabling a quadrotor helicopter, equipped with a laser rangefinder sensor, to autonomously explore and map unstructured and unknown indoor environments. While these capabilities are already commodities on ground vehicles, air vehicles seeking the same performance face unique challenges. In this paper, we describe the difficulties in achieving fully autonomous helicopter flight, highlighting the differences between ground and helicopter robots that make it difficult to use algorithms that have been developed for ground robots. We then provide an overview of our solution to the key problems, including a multilevel sensing and control hierarchy, a high-speed laser scan-matching algorithm, an EKF for data fusion, a high-level SLAM implementation, and an exploration planner.1 Finally, we show experimental results demonstrating the helicopter's ability to navigate accurately and autonomously in unknown environments.
