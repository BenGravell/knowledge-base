<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

SafeVRU: A Research Platform for the Interaction of Self-Driving Vehicles with Vulnerable Road Users

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents our research platform Safe VRU for the interaction of self-driving vehicles with Vulnerable Road Users (VRUs, i.e., pedestrians and cyclists). The paper details the design (implemented with a modular structure within ROS) of the full stack of vehicle localization, environment perception, motion planning, and control, with emphasis on the environment perception and planning modules. The environment perception detects the VRUs using a stereo camera and predicts their paths with Dynamic Bayesian Networks (DBNs), which can account for switching dynamics. The motion planner is based on model predictive contouring control (MPCC) and takes into account vehicle dynamics, control objectives (e.g., desired speed), and perceived environment (i.e., the predicted VRU paths with behavioral uncertainties) over a certain time horizon. We present simulation and real-world results to illustrate the ability of our vehicle to plan and execute collision-free trajectories in the presence of VRUs.
