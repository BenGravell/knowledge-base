<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Kinematic Modeling of Wheeled Mobile Robots

Topics include Wheeled mobile robots, Kinematic modeling, Nonholonomic constraints, Mobile robot control, Robot locomotion, Vehicle kinematics.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Muir and Neuman develop kinematic models for wheeled mobile robots, emphasizing how wheel geometry and rolling constraints determine feasible platform motion. The paper is a useful early reference for nonholonomic mobile-robot modeling before later unicycle, car-like, and omnidirectional models became standard textbook forms.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We formulate the kinematic equations of motion of wheeled mobile robots incorporating conventional, omnidirectional, and ball wheels.1 We extend the kinematic modeling of stationary manipulators to accommodate such special characteristics of wheeled mobile robots as multiple closed‐link chains, higher‐pair contact points between a wheel and a surface, and unactuated and unsensed wheel degrees of freedom. We apply the Sheth‐Uicker convention to assign coordinate axes and develop a matrix coordinate transformation algebra to derive the equations of motion. We introduce a wheel Jacobian matrix to relate the motions of each wheel to the motions of the robot. We then combine the individual wheel equations to obtain the composite robot equation of motion. We interpret the properties of the composite robot equation to characterize the mobility of a wheeled mobile robot according to a mobility characterization tree. Similarly, we apply actuation and sensing characterization trees to delineate the robot motions producible by the wheel actuators and discernible by the wheel sensors, respectively. We calculate the sensed forward and actuated inverse solutions and interpret the physical conditions which guarantee their existence.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

To illustrate the development, we formulate and interpret the kinematic equations of motion of Uranus, a wheeled mobile robot being constructed in the CMU Mobile Robot Laboratory.
