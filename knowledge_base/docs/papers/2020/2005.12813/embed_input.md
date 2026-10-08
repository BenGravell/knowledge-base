<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

AlphaPilot: Autonomous Drone Racing

Topics include Autonomous drone racing, Vision-based navigation, Gate detection, State estimation, Time-optimal planning, Quadrotors.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Combines learned gate detections, nonlinear filtering, and near-time-optimal planning into a complete autonomous drone-racing system. Simultaneous observations of multiple gates correct drift and build a global map, enabling flight up to 8 m/s and second place in the 2019 AlphaPilot Challenge.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents a novel system for autonomous, vision-based drone racing combining learned data abstraction, nonlinear filtering, and time-optimal trajectory planning. The system has successfully been deployed at the first autonomous drone racing world championship: the 2019 AlphaPilot Challenge. Contrary to traditional drone racing systems, which only detect the next gate, our approach makes use of any visible gate and takes advantage of multiple, simultaneous gate detections to compensate for drift in the state estimate and build a global map of the gates. The global map and drift-compensated state estimate allow the drone to navigate through the race course even when the gates are not immediately visible and further enable to plan a near time-optimal path through the race course in real time based on approximate drone dynamics. The proposed system has been demonstrated to successfully guide the drone through tight race courses reaching speeds up to 8m/s and ranked second at the 2019 AlphaPilot Challenge.
