<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

System Identification of the Crazyflie 2.0 Nano Quadrocopter

Topics include System identification, Quadrotor dynamics, Crazyflie, Motor characterization, Inertia estimation, Aerodynamic drag.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Measures the Crazyflie 2.0's inertia, motor command-to-thrust and torque relationships, motor dynamics, and aerodynamic drag through dedicated experiments. These parameters support model-based estimation and control of the nano quadrocopter.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The physical parameters of the Crazyflie 2.0 nano quadrocopter and the experiments that were used to determine them are presented. Firstly, to measure the coefficients of the inertia matrix, the relationship between the moment of inertia and the period of a pendulum was made use of. Secondly, a set of motor parameter mappings between motor input command, produced thrust and torque and the rotor's angular velocities was determined using a force/torque sensor and a laser tachometer. In addition, a transfer function for the motors was identified by applying sinusoidal inputs to the motors. Thirdly, the quadrocopter's drag coefficients that characterize the force acting on the rotating propellers when the quadrocopter is moving in air were determined. For this, air was blown onto the Crazyflie while it was mounted to the force/torque sensor. Finally, the experimental methods for determining the inertia matrix and the motor parameter mappings were verified using appropriate experiments.
