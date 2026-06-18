<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Flying Inverted Pendulum

Topics include Aerial robotics, Quadrotor control, Inverted pendulum, Trajectory tracking, Linear feedback control, Flying machine arena, Underactuated systems.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Turns the classic inverted-pendulum benchmark into an aerial robotics experiment by balancing a pendulum on a quadrotor. The paper derives static and circular nominal motions, linearizes around them using a yaw-independent virtual body frame, and validates feedback control in the ETH Flying Machine Arena.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We extend the classic control problem of the inverted pendulum by placing the pendulum on top of a quadrotor aerial vehicle. Both static and dynamic equilibria of the system are investigated to find nominal states of the system at standstill and on circular trajectories. Control laws are designed around these nominal trajectories. A yaw-independent description of quadrotor dynamics is introduced, using a `Virtual Body Frame'. This allows for the time-invariant description of curved trajectories. The balancing performance of the controller is demonstrated in the ETH Zurich Flying Machine Arena testbed. Development potential for the future is highlighted, with a focus on applying learning methodology to increase performance by eliminating systematic errors that were seen in experiments.
