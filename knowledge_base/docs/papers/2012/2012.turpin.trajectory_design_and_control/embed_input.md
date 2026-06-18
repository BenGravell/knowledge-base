<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Trajectory Design and Control for Aggressive Formation Flight with Quadrotors

Topics include Quadrotor formations, Aggressive flight, Decentralized control, Trajectory planning, Communication delays, Formation tracking, Aerial robotics.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Designs decentralized trajectory planning and control for teams of quadrotors that must maintain specified formation geometry during aggressive 3D motion. The paper is most useful for its treatment of the interaction between fourth-order quadrotor dynamics, nonlinear controllers, local plan sharing, communication delay, and failures, backed by both simulation and multi-robot experiments.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this work we consider the problem of controlling a team of micro-aerial vehicles moving quickly through a three-dimensional environment while maintaining a tight formation. The formation is specified by shape vectors which prescribe the relative separations and bearings between the robots. To maintain the desired shape, each robot plans its trajectory independently based on its local information of other robot plans and estimates of states of other robots in the team. We explore the interaction between nonlinear decentralized controllers, the fourth-order dynamics of the individual robots, time delays in the network, and the effects of communication failures on system performance. Simulations as well as an experimental evaluation of our approach on a team of quadrotors suggests that suitable performance is maintained as the formation motions become increasingly aggressive and as communication degrades.
