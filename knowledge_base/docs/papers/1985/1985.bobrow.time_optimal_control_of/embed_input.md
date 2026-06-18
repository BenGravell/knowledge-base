Time-Optimal Control of Robotic Manipulators along Specified Paths

Topics include Time-optimal control, Path parameterization, Manipulator trajectory planning, Bang-bang control, Torque constraints.

Seminal paper establishing the time-optimal path parameterization (TOPP) problem: given a specified geometric path and actuator torque limits, finds the minimum-time traversal by solving for bang-bang optimal torques in the velocity-position phase plane.

The minimum-time manipulator control problem is solved for the case when the path is specified and the actuator torque limitations are known. The optimal open-loop torques are found, and a method is given for implementing these torques with a conventional linear feedback control system. The algorithm allows bounds on the torques that may be arbitrary functions of the joint angles and angular velocities. This method is valid for any path and orientation of the end-effector that is specified. The algorithm can be used for any manipulator that has rigid links, known dynamic equations of motion, and joint angles that can be determined at a given position on the path.
