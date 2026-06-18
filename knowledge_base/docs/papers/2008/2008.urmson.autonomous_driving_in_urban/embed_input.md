<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Autonomous Driving in Urban Environments: Boss and the Urban Challenge

Topics include Autonomous driving, Urban driving, DARPA urban challenge, Behavior planning, Sensor fusion, Autonomous vehicles.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Describes Boss, the CMU autonomous vehicle that won the 2007 DARPA Urban Challenge. Presents the full software stack for urban driving including perception, behavior planning, and motion planning components that operate in complex traffic scenarios with other vehicles and pedestrians.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Boss is an autonomous vehicle that uses on-board sensors (global positioning system - lasers, radars, and cameras) to track other vehicles, detect static obstacles, and localize itself relative to a road model. A three-layer planning system combines mission, behavioral, and motion planning to drive in urban environments. The mission planning layer considers which street to take to achieve a mission goal. The behavioral layer determines when to change lanes and precedence at intersections and performs error recovery maneuvers. The motion planning layer selects actions to avoid obstacles while making progress toward local goals. The system was developed from the ground up to address the requirements of the DARPA Urban Challenge using a spiral system development process with a heavy emphasis on regular, regressive system testing. During the National Qualification Event and the 85-km Urban Challenge Final Event, Boss demonstrated some of its capabilities, qualifying first and winning the challenge.
