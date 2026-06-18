<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

RANGE: Robust Autonomous Navigation in GPS-denied Environments

Topics include Aerial robotics, Global positioning system-denied navigation, Autonomous exploration, Simultaneous localization and mapping, Micro aerial vehicles, Laser rangefinder, State estimation, Field robotics.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Presents a complete quadrotor autonomy stack for GPS-denied environments, including sensing, state estimation, mapping, exploration, and control under tight payload and latency constraints. Its contribution is less a single estimator than an experimentally validated system design showing that small MAVs can autonomously navigate unknown indoor spaces with only onboard range sensing.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper addresses the problem of autonomous navigation of a micro air vehicle (MAV) in GPS-denied environments. We present experimental validation and analysis for our system that enables a quadrotor helicopter, equipped with a laser range finder sensor, to autonomously explore and map unstructured and unknown environments. The key challenge for enabling GPS-denied flight of a MAV is that the system must be able to estimate its position and velocity by sensing unknown environmental structure with sufficient accuracy and low enough latency to stably control the vehicle. Our solution overcomes this challenge in the face of MAV payload limitations imposed on sensing, computational, and communication resources. We first analyze the requirements to achieve fully autonomous quadrotor helicopter flight in GPS-denied areas, highlighting the differences between ground and air robots that make it difficult to use algorithms developed for ground robots. We report on experiments that validate our solutions to key challenges, namely a multilevel sensing and control hierarchy that incorporates a high-speed laser scan-matching algorithm, data fusion filter, high-level simultaneous localization and mapping, and a goal-directed exploration module.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

These experiments illustrate the quadrotor helicopter's ability to accurately and autonomously navigate in a number of large-scale unknown environments, both indoors and in the urban canyon. The system was further validated in the field by our winning entry in the 2009 International Aerial Robotics Competition, which required the quadrotor to autonomously enter a hazardous unknown environment through a window, explore the indoor structure without GPS, and search for a visual target.
