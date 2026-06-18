<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Swing up Control Problem for the Acrobot

Topics include Acrobot, Swing-up control, Underactuated systems, Energy-based control, Nonlinear control, Robotics.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces the Acrobot (a two-link robot arm with one passive joint) as a benchmark for underactuated control and presents an energy-based swing-up strategy that pumps energy to bring the arm from hanging to the inverted position, after which a linear stabilizer takes over. Popularized the Acrobot as a canonical underactuated control problem.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Underactuated mechanical systems are those possessing fewer actuators than degrees of freedom. Examples of such systems abound, including flexible joint and flexible link robots, space robots, mobile robots, and robot models that include actuator dynamics and rigid body dynamics together. Complex internal dynamics, nonholonomic behavior, and lack of feedback linearizability are often exhibited by such systems, making the class a rich one from a control standpoint. In this article the author studies a particular underactuated system known as the Acrobot: a two-degree-of-freedom planar robot with a single actuator. The author considers the so-called swing up control problem using the method of partial feedback linearization. The author gives conditions under which the response of either degree of freedom may be globally decoupled from the response of the other and linearized. This result can be used as a starting point to design swing up control algorithms. Analysis of the resulting zero dynamics as well as analysis of the energy of the system provides an understanding of the swing up algorithms. Simulation results are presented showing the swing up motion resulting from partial feedback linearization designs.
