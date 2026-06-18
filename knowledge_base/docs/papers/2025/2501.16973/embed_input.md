Towards Open-Source and Modular Space Systems with ATMOS

In the near future, autonomous space systems will compose many of the deployed spacecraft. Their tasks will involve autonomous rendezvous and proximity operations with large structures, such as inspections, assembly, and maintenance of orbiting space stations, as well as human-assistance tasks over shared workspaces. To promote replicable and reliable scientific results for autonomous control of spacecraft, we present the design of a space robotics laboratory based on open-source and modular software and hardware. The simulation software provides a software-in-the-loop architecture that seamlessly transfers simulated results to the hardware. Our results provide an insight into such a system, including comparisons of hardware and software results, as well as control and planning methodologies for controlling free-flying platforms.

## Introduction

The space sector has experienced significant growth in the last decade \[\]. Such growth is not only due to the decreased cost of access to space through multiple commercial operators \[\], but also due to the maturation of existing technologies and, consequently, reduced pricing for equipment. In the last twenty to thirty years, a few academic and industrial research facilities have been created to test space systems by replicating motion in microgravity on Earth. These facilities primarily rely on granite tables, resin floors, or other flat-calibrated surfaces such as optic tables.

Figure 1: The KTH Space Robotics Laboratory, with three ATMOS free-flyers operating on a flat floor. One free-flyer is equipped with a manipulator payload, while another is connected to a low-pressure tether system.

To complete these systems, some trade-offs had to be made. To achieve a large operational area at a reduced cost, the precision of granite tables was exchanged with the lower cost per area solution of using a self-leveling epoxy floor. These leveling issues are also present in other state-of-the-art facilities. On the other hand, the proposed offset-free MPC aids in overcoming such issues for setpoint stabilization. Regarding tracking performance, we expect that using estimators for dynamic residuals can improve the platform performance....

Future work will involve finalizing the integration of the NASA Astrobee \\acFSW in ATMOS, integrating floor disturbance plugins and thruster efficiency loss models, and implementing collaborative load transportation strategies and fault-tolerant control schemes. We also aim to finalize the integration of our software with PX4-Autopilot to allow easier access to the software and improved long-term support.

Figure 18: \acSITL simulation in Gazebo. The simulated model interacts with the PX4Space \acSITL setup and allows interaction with any of the control interfaces of the real platform, as well as simulating any of the radio-controlled flight modes.

On top of the actuation plate sits the avionics layer, composed of high-level and low-level computing units, batteries, and a power monitoring module. An overview of this layer is shown in Fig. 13, and the block diagram with the electrical and signals schematic is shown in Fig. 14.
