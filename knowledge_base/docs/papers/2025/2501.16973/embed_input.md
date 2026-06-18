<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Towards Open-Source and Modular Space Systems with ATMOS

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In the near future, autonomous space systems will compose many of the deployed spacecraft. Their tasks will involve autonomous rendezvous and proximity operations with large structures, such as inspections, assembly, and maintenance of orbiting space stations, as well as human-assistance tasks over shared workspaces. To promote replicable and reliable scientific results for autonomous control of spacecraft, we present the design of a space robotics laboratory based on open-source and modular software and hardware. The simulation software provides a software-in-the-loop architecture that seamlessly transfers simulated results to the hardware. Our results provide an insight into such a system, including comparisons of hardware and software results, as well as control and planning methodologies for controlling free-flying platforms.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The space sector has experienced significant growth in the last decade. Such growth is not only due to the decreased cost of access to space through multiple commercial operators, but also due to the maturation of existing technologies and, consequently, reduced pricing for equipment. In the last twenty to thirty years, a few academic and industrial research facilities have been created to test space systems by replicating motion in microgravity on Earth. These facilities primarily rely on granite tables, resin floors, or other flat-calibrated surfaces such as optic tables.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Some of the first microgravity testing facilities in Tohoku University and Tokyo University used granite tables as calibrated flat surfaces where air-bearings supported robotic equipment mimicking undampened motion in the 2D plane. The National Technical University of Athens proposed a similar test bed, where the platforms carry a microcontroller and an onboard computer that triggers $\text{CO}_{2}$-based thrusters. The facility also provides a vision-based ground truth that relies on fiducial markers for the position of each of the robotic platforms and sub-components. This facility was recently upgraded to more modern avionics, motion capture ground-truth positioning, and robotics communication software through the Robotics Operating System (ROS). Stanford University's Autonomous Systems Laboratory (previously maintained by the Aerospace Robotics Laboratory) free-flyer testbed uses a round platform as a free-flying robotic system for path planning, docking and capturing of space systems, paired with an open-source Python and ROS 2-based simulator. The open-source nature of the software allows other researchers to use the software to test their algorithms either in simulation only or as an intermediary step toward experiments in the facility.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

More recent granite table facilities in Europe are at the Space Research Center in Poland and at DLR Institute of Space Systems. On the latter, a 5 \\acdof platform provides attitude control in 3D and position control in 2D. The large granite surface comprises two granite slabs of $4\ m$$\times$$2.5\ m$, achieving a combined area of $20\ m^{2}$. The flatness of the surface is $20\mu m$ edge-to-edge on each granite slab and $10\mu m$ table-to-table. The platform runs generated C code from Matlab Simulink. The thruster systems are fed by $300\ {bar}$ compressed air bottles, and an external ground-truth system is also available. The granite laboratory at NASA Ames, currently used to test the Astrobee free-flyer, also relies on a granite surface to test the robotic vehicle that is currently operating on the \\acISS. The free-flyer comprises two plenum cavities that provide electric propulsion to the spacecraft.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Onboard, the platform has three ARM-based CPUs that control the platform actuation, provide state estimation from vision-based and inertial odometry, and three payload bays for guest science research. The software stack is open-source with a complete simulation package running in ROS and Gazebo, making it easy for anyone to test their algorithms onboard the Astrobee.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite the considerable precision that can be achieved with granite tables, we identify two drawbacks of this approach: cost and weight. Typically, granite tables are limited to ground-floor installations due to the pressure they apply on the supporting surface. Moreover, large granite slabs are also costly, and aggregating multiple units is also expensive in maintaining the operation, as they need to be calibrated in periodic intervals. An alternative to this solution is to use resin floors. The Space Robotics Laboratory at the Naval Postgraduate School uses a flat floor of approximately $20\ m^{2}$ built with epoxy resin and initially developed to test docking scenarios for two spacecraft that were purpose-built for this facility. This system provides a Pentium III in a PC/104 compatible avionics stack and uses cold-gas thrusters as actuators. Here, localization is done via an indoor GPS system, from which the vehicle position is obtained through triangulation to two fixed transmitters. In, a facility at the University of South California showcases a resin floor capable of operating multiple 3 \\acdof platforms with vision-based docking mechanisms built with commercial off-the-shelf components.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Similar facilities have been proposed by the University of Kentucky Aerospace Deployment Dynamics Laboratory and ATK Robotic Rendezvous and Proximity (RPO) testing facility. With the same operating principles, the facilities at Georgia Institute of Technology and Rensselaer Polytechnic Institute use resin floors and air bearings for a frictionless motion of their platforms, which can provide 5 and 6 \\acdof, respectively. Although the 5 \\acdof system is similar to the one, the 6 \\acdof system augments the 5 \\acdof system with an elevator that can vertically move an attitude-controlled stage. This system can mimic the 6 \\acdof motion at the expense of some imperfection on the Z axis at high speeds. Both platforms use PC/104 computers, using Matlab and Simulink interfaces, while uses a \\acRTAI Linux operating system. The largest resin-based floor system is in the California Institute of Technology. This facility provides a more than $40\ m^{2}$ area with multiple platforms that can provide 3 to 6 \\acdof.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The propulsion method uses compressed air tanks at a $300\ {bar}$, and the onboard computer is an Nvidia Jetson TX2, which contains an integrated GPU for onboard parallel computations. In Europe, multiple facilities have also been created. The European Space Agency Orbital Robotics laboratory provides a similar facility composed mainly of 3 \\acdof platforms using compressed air as a propellant. Two other recent facilities are the ones in the Luleå University of Technology and in the University of Luxembourg. These facilities provide access to 3 Degree-of-Freedom platforms and motion capture systems for ground truth.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Other approaches to recreate microgravity motion have used optic and pressurized tables. In particular, the facility at the Massachusetts Institute of Technology Space Systems Laboratory has been used both to create and to serve as a ground testing facility for the MIT Synchronized Position Hold Engage and Reorient Experimental Satellite (SPHERES), a set of three satellite demonstrators that operated inside the ISS from May 2006 to December 2019. The SPHERES used $\text{CO}_{2}$ as their main propellant. The onboard computer consisted of a Texas Instruments DSP programmed in C. Additionally, a simulator in Matlab and Simulink was available. The optic table provided a $2.7\ m^{2}$ operating surface, which needed to be calibrated regularly to ensure accurate results. The facilities in use similar optic tables. These tables are usually paired with a glass panel to provide a smooth operating surface for air bearings; therefore, their precision depends on the glass panel's properties. The ELISSA facility described provides an operation method that works mostly in an opposite fashion to most of the systems described here.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this case, the air cushion is created by small nozzles distributed on the table surface and a piece of acrylic or glass that is attached to the bottom part of the simulated spacecraft. This allows the operation time of simulated spacecraft to not depend on the available air supply but only on its battery. The NASA Johnson Space Center Precision Air Bearing Floor is capable of simulating human-scale platforms for training astronauts for extravehicular activities in microgravity. The NASA Jet Propulsion Lab GSAT laboratory supports multiple spacecraft analogue systems on their flat floor, composed by individual, calibrated plates of aluminium. Lastly, the LASR laboratory at Texas A&M supports a large flat floor facility with a total of 2000 square feet and simulates satellite dynamics using holonomic wheeled robots instead of air bearings. Multiple other microgravity simulator facilities can be found.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite numerous platforms and laboratory facilities, we found two significant problems related to platform replication, applicability of research results, and benchmarking. First, most software is not open-source or relies on custom-developed low-level hardware, making it hard to replicate the testing conditions. Secondly, platform modularity is often not considered; thus, making adjustments or future-proofing challenging. Due to these reasons, transitioning from ground testing to orbit testing is difficult outside of the proposed facilities. This article proposes an open-source microgravity simulation laboratory to tackle these drawbacks. For this facility, we propose and develop a 3 \\acdof Autonomy Testbed for Multi-purpose Orbital Systems (ATMOS) platform with open hardware and software to facilitate their replication at a low cost. The hardware is based on commercial off-the-shelf components that are widely available. The low-level microcontroller is based on the Pixhawk 6X Mini, while the high-level computer is an Nvidia Jetson Orin NX.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

This combination allows us to: i) run *PX4Space*, a branch of the open-source PX4 we developed for thruster-based systems with \\acSITL capabilities, ii) support multiple payloads with heterogeneous power and communication needs, and iii) be compatible with on-orbit facilities software stacks, such as the Astrobee \\acFSW, aiming at reducing the time-to-orbit of ground experiments. The free-flying platform operates on top of three air bearings with a maximum combined payload of approximately $150\ {}$. The air bearings and thrusters are air operated from three $1.5\ L$ bottles, filled at $300\ {bar}$, and separately regulated to $6\ {bar}$ for the actuation and air bearing systems. The platform contains a total of 8 thrusters actuated via \\acPWM. The facility provides access to low- and high-pressure compressors. The low-pressure compressor can continuously operate three tethered platforms with an uninterrupted air supply. At the same time, the high-pressure compressor is mainly used for fast experimental turnover time by rapidly refilling the compressed air bottles.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

The operational area has an approximate dimension of $15\ m^{2}$ covered by a Qualisys active motion capture system that provides an accurate, sub-millimeter ground-truth position of all tracked rigid bodies.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of the article is divided as follows: in Sec. 2, we introduce the available facilities. Sections 3 and detail the hardware and software of the proposed modular and open-source platform, ATMOS, while Sec. 5 discusses its autonomy capabilities. Ending the manuscript, Sec. 6 provides preliminary results of the proposed hardware and software package along with a small discussion on these. Section 7 concludes the article.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Notation: Matrices are denoted by capital letters. Let $a^{T}$ be the transpose of $a$. The orthogonal basis vectors of a frame $\mathcal{A}$ are denoted $\{ a_{x},a_{y},a_{z}\}$. The inertial reference frame is generally omitted. Sets are defined in blackboard bold, $\mathbb{A}$. The weighted vector norm $\sqrt{x^{T}Ax}$ is denoted $\left\| x \right\|_{A}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Facilities", "weight": 1.0} -->

This chapter provides a detailed overview of the laboratory facilities. These encompass the resin flat floor, the motion capture system, and the compressors for high and low pressures. Figure 1 shows the free-flying platforms available at the facility.

<!-- chunk {"id": "body-0018", "role": "body", "section": "2-A Epoxy Floor", "weight": 1.0} -->

The flat floor depicted in Fig. 1 was developed over one year with multiple resin layers. In between each pour, measurements were collected with a leveling laser, and the higher areas were sanded for more extended periods than the lower areas. In Fig. 2, we show the floor levelness after the first and second pours of epoxy resin. Currently, the flat floor provides a maximum declination of $2\ {{mm}/\text{m}}$. Although a higher precision can be achieved with granite surfaces, the resin floor provided a more cost-efficient installation. We must note that more accurate solutions can be obtained with different types of resins, as also seen, and that our platform has sufficient thrust to compensate for such disturbances.

<!-- chunk {"id": "body-0019", "role": "body", "section": "2-B Motion Capture System", "weight": 1.0} -->

A \\acmocap provided by Qualisys with six cameras is installed above the operating area shown in Fig. 1. These cameras offer sub-millimeter tracking of any rigid body in the workspace at a frequency of $100\ {Hz}$. Since the floor is highly reflective due to the polishing of the surface, the motion capture system operates in active mode, where the cameras passively capture the infrared LEDs on the platform. The infrared LEDs strobe at distinct frequencies and, therefore, are identifiable by the system. The LEDs are connected to a Qualisys Naked Traqr that controls the frequency of each LED. In Fig. 3, we show both the motion capture system cameras and the active tracking unit onboard one of our free-flying platforms.

<!-- chunk {"id": "body-0020", "role": "body", "section": "2-C Pressurized Air Supplies", "weight": 1.0} -->

Low and high-pressure compressors are two critical pieces of equipment that can sustain prolonged test sessions at the laboratory. Our facility has access to an Atlas Copco $10\ {bar}$ compressor capable of simultaneously providing tethered air supply to three of our platforms. The air supply is given through tether cables attached to the pressurized manifold on the platform. Then, the pressurized air is regulated to $6\ {bar}$ to feed the air bearings and the thruster actuation system. An image of the tether attached to a robot is seen Fig. 4. The high-pressure compressor unit consists of a Bauer PE250-MVE $300\ {bar}$ compressor paired with a $50\ L$ reservoir. It also includes a remote filling station for quickly refilling pressurized air bottles used during tests.

<!-- chunk {"id": "body-0021", "role": "body", "section": "2-C Pressurized Air Supplies", "weight": 1.0} -->

As the tether cable induces external disturbances on the platform, it is primarily used during development and testing sessions. When untethered operation is required, the three $1.5\ L$ bottles onboard the platform are used instead. These bottles can be rapidly refueled before each experiment using the high-pressure compressor.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Free-flyers Hardware", "weight": 1.0} -->

A core part of our space robotics laboratory are the ATMOS free-flyers, which simulate the dynamics of a small satellite operating in microgravity. To our knowledge, such platforms are unavailable for off-the-shelf purchase due to each laboratory's different needs. In this section, we detail the hardware needed to build our modular free-flying platforms, proposing a flexible platform that other space robotics facilities can use.

<!-- chunk {"id": "body-0023", "role": "body", "section": "3-A Hardware Overview", "weight": 1.0} -->

The free-flyers developed for the laboratory have the following design goals: i) modularity, allowing for easy module substitution and template designing without significant changes to the platform; ii) cost-efficiency, allowing for an economical replication of these units, and iii) guest science support, providing a facility that external researchers or industry partners can use as a payload bearer to test hardware or software in the laboratory. With these goals in mind, the final design of our platform is shown in Fig. 5.

<!-- chunk {"id": "body-0024", "role": "body", "section": "3-A Hardware Overview", "weight": 1.0} -->

The dimensions of the platform, as well as a schematic overview, are available in Fig. 6. An overview of the platform actuation and inertial parameters is shown in Tab. 1. We compare our platform with the NASA Astrobee robot, a widely used platform for guest science research aboard the \\acISS. The information regarding the Astrobee platform was collected.

<!-- chunk {"id": "body-0025", "role": "body", "section": "3-B Pneumatic Section", "weight": 1.0} -->

The pressurized section provides all sub-components with the necessary capabilities for frictionless motion, propulsion, and pressure regulation. A representation of this section is shown in Fig. 7.

<!-- chunk {"id": "body-0026", "role": "body", "section": "3-B Pneumatic Section", "weight": 1.0} -->

Three bottles provide breathable compressed air at a pressure of $300\ {bar}$ with a combined volume of $4.5\ L$. Two bottle-attached regulators then regulate the high pressure down to $10\ {bar}$. Their description is given in Tab. 2.

<!-- chunk {"id": "body-0027", "role": "body", "section": "3-B Pneumatic Section", "weight": 1.0} -->

The three $50\ {}$ air bearings at the bottom of the platform create an air cushion of $15$ to $20\ {µm}$, thus enabling the frictionless motion of the platform without any contact to the floor. Figure 8 pictures the air bearings, which require an input pressure of $5\ {bar}$ and can hold a load up to $52\ {}$ each. Combining the three bearings on a single platform, a maximum load of approximately $156\ {}$ is achieved.

<!-- chunk {"id": "body-0028", "role": "body", "section": "3-B Pneumatic Section", "weight": 1.0} -->

Compressed air tank (300 bar)
DYE CORE AIR TANK 1.5L 4500PSI

<!-- chunk {"id": "body-0029", "role": "body", "section": "3-B Pneumatic Section", "weight": 1.0} -->

Bottle regulator (to 55 bar)
DYE LT Throttle Regulator 4500PSI

<!-- chunk {"id": "body-0030", "role": "body", "section": "3-B Pneumatic Section", "weight": 1.0} -->

Bottle regulator (to 10 bar)
Polarstar micro MR GEN2 Regulator

<!-- chunk {"id": "body-0031", "role": "body", "section": "3-C Actuation Modules", "weight": 1.0} -->

For our platform, two actuation modules were designed: i) a solenoid valve actuation plate, referred to as a thruster plate, with a total of eight thrusters that mimic the Reaction Control System (RCS) on a spacecraft; and ii) a propeller-based actuation plate that aims at mimicking the actuation dynamics of the free-flyers such as the NASA Astrobee, with a total of four motors capable of bi-directional rotation. These two actuation plates also allow us to have two actuation modalities: the thruster plate only allows for maximum thrust / no thrust with \\acPWM, while the propeller plate allows for selecting any target thrust within the control set.

<!-- chunk {"id": "body-0032", "role": "body", "section": "3-C Actuation Modules", "weight": 1.0} -->

An essential aspect of the platform is the modularity of the actuation modules, making it possible for other system users or laboratories to share their designs and augment the capabilities of ATMOS.

<!-- chunk {"id": "body-0033", "role": "body", "section": "3-C Actuation Modules", "weight": 1.0} -->

The thruster plate has eight solenoid valves divided into four modules, each with a pair of thrusters. The modules are placed in the vertices of a square with $24\ {}$ edges as shown in Fig. 9. This configuration allows the platform to be holonomic in the motion plane, with 3 \\acdof, while providing thruster redundancy for up to two non-collinear thruster failures. The solenoid valves provide a maximum switching frequency of $500\ {Hz}$. The platforms are nominally configured in software to a fixed switching frequency of $10\ {Hz}$ with a controllable duty cycle from $0$ to $100\ {}$. For compactness, we include two solenoids and one $24\ {}$ buck-boost converter into one thruster module, shown in Fig. 10. Compressed air is supplied via the onboard manifold described in Fig. 7 and the blue tubing shown in Fig. 9.

<!-- chunk {"id": "body-0034", "role": "body", "section": "3-C Actuation Modules", "weight": 1.0} -->

The thrusters operate at $6\ {bar}$, drawing air through $4\ {}$ diameter hoses and expelling it via $2\ {}$ nozzles. Experimental measurements show that a single thruster in this system generates $1.7\ N$ of force while consuming $3.5\ {g\ s^{- 1}}$ when open; closely matching the theoretical maximum of $1.76\ N$ for isentropic nozzle flow under these conditions. However, since the thrusters share a common air supply, interactions between them are inevitable. This coupling effect was measured and is illustrated in Fig. 11, where the force output of one thruster is recorded while up to three additional thrusters are simultaneously active. During this measurement, all thrusters ran at the nominal $10\ {Hz}$ frequency whilst switching between $0$ and $100\ \%$ duty cycle. This data was collected at $320$ samples/second using a TAL220 10kg load cell amplified with a NAU7802 analog-to-digital converter.

<!-- chunk {"id": "body-0035", "role": "body", "section": "3-C Actuation Modules", "weight": 1.0} -->

Each additional thruster reduces the output force of the measured thruster by approximately $12.5\ \%$. It should be noted that this is a worst-case scenario, where several thrusters are operating at $100\ \%$. An estimation of the force from the ith thruster can be obtained in closed form with $F_{i} = {1.7u_{i}{({1 - {0.125{\sum_{j \neq i}u_{j}}}})}}$. Given the thruster plate's configuration, no more than four thrusters are expected to operate concurrently, as each thruster can be paired with one in the opposite direction.

<!-- chunk {"id": "body-0036", "role": "body", "section": "3-C Actuation Modules", "weight": 1.0} -->

The three compressed air tanks carry $1.65\ {}$ of compressed air when filled to $300\ {bar}$. With a single thruster consuming $3.5\ {g\ s^{- 1}}$ of air, the robot can thus operate a single thruster continuously open for up to $480\ s$, assuming non-operable below $10\ {bar}$. In practice, however, the thrusters are not expected to operate continuously for extended periods and the actual operational time of the robot will depend on the efficiency of the implemented controller.

<!-- chunk {"id": "body-0037", "role": "body", "section": "3-C Actuation Modules", "weight": 1.0} -->

The propeller plate allows for finer control over the imposed forces on the platform. A preview of the propeller plate is shown in Fig. 12. Each motor is paired with a $3.5$ inch propeller and an electronic speed controller (ESC) capable of field-oriented control (FOC). FOC allows us to accurately track the motor rotation independently of the battery level, as long as there is enough power for the requested velocity. Moreover, FOC allows precise rotation speed control at slow speeds, enabling us to inject disturbances into the motion model accurately or replicate orbital dynamics at scale. Each motor is capable of $1.96\ N$ of thrust in both directions, for a total maximum of $3.92\ N$ of thrust on each axis and $0.67\ $ of torque.

<!-- chunk {"id": "body-0038", "role": "body", "section": "3-D Electronics", "weight": 1.0} -->

On top of the actuation plate sits the avionics layer, composed of high-level and low-level computing units, batteries, and a power monitoring module. An overview of this layer is shown in Fig. 13, and the block diagram with the electrical and signals schematic is shown in Fig. 14.

<!-- chunk {"id": "body-0039", "role": "body", "section": "3-D Electronics", "weight": 1.0} -->

We use a Pixhawk 6X Mini as the low-level computing unit running PX4Space as the firmware. This unit comprises triple-redundant and temperature-compensated inertial measurement units (ICM-45686) and two barometers (ICP20100 and BMP388). An ARM Cortex M7 (STM32H753) microcontroller collects the sensor outputs and interfaces with the high-level computer, a Jetson Orin NX, through $100\ {{M}/s}$ Ethernet. Pixhawk also serves as an interface with the actuators, capable of driving both thruster and propeller plates simultaneously using, e.g., the two PWM output modules or CAN actuator interfaces. Since this unit runs a \\acRTOS, in our case NuttX, it can precisely control the output via CPU interruptions.

<!-- chunk {"id": "body-0040", "role": "body", "section": "3-D Electronics", "weight": 1.0} -->

Lastly, using a separate low-level computing unit provides a safety layer, acting as a failsafe against failures such as stabilization of the platform when the motion capture system odometry estimations are lost, or the high-level controller pushes the system beyond its safety envelope, or the system battery runs low.

<!-- chunk {"id": "body-0041", "role": "body", "section": "3-D Electronics", "weight": 1.0} -->

The high-level computer is an Nvidia Jetson Orin NX with $16\ {G}$ of LPDDR5 RAM, an 8-core ARM Cortex-A78AE with a maximum of $2.2\ {GHz}$ clock, as well as a GPU composed by 1024 Core Ampere, with 32 Tensor Cores. This unit runs Ubuntu 22.04 as the operating system. The ROS 2 Humble is set up on this platform and interfaces via DDS over Ethernet with PX4 running on the low-level computing unit. This unit also interfaces with the \\acmocap over Wi-Fi and passes through the odometry estimations as an external vision system to PX4.

<!-- chunk {"id": "body-0042", "role": "body", "section": "3-D Electronics", "weight": 1.0} -->

Lastly, the system is powered by a 6-cell $9.5\ {A\ h}$ Lithium Polymer battery monitored with a PM02D digital power module.

<!-- chunk {"id": "body-0043", "role": "body", "section": "3-E Payload Hosting", "weight": 1.0} -->

The last layer on the free-flyer is a payload support system. With this architecture, we aim to support other researchers in testing hardware in microgravity conditions and provide a platform for co-development with industry, integrating space-grade hardware into our facilities. Figure 15 shows the BlueRobotics Newton Gripper with custom claw, interfacing over USB and ROS 2 with the high-level computer. Another capability is to host actuated platforms - such as CubeSats - while ATMOS generates a trajectory for the system under testing or compensates for the added mass and inertia of the hosting free-flyer. Communication can be done directly with PX4 on the low-level computing unit or through a ROS node on a high-level computer.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Free-flyers Software", "weight": 1.0} -->

As proposed in this article's introduction, a significant contribution of our facilities is the open-source software stack. In this section, we introduce our software architecture.

<!-- chunk {"id": "body-0045", "role": "body", "section": "4-A Software Architecture", "weight": 1.0} -->

Since multiple computing units are running in real-time and communicating over different protocols, having robust and flexible software solutions is paramount to the efficiency of our facility. In Fig. 16, we shed light on the software architecture in our laboratory facilities.

<!-- chunk {"id": "body-0046", "role": "body", "section": "4-A Software Architecture", "weight": 1.0} -->

The software architecture is supported by mainly two communication protocols: Data Distribution Service (DDS), responsible for the interaction between PX4 and the onboard Nvidia Jetson Orin NX, as well as for the ROS 2 Humble middleware; and FleetMQ^11^1URL: Available on 16th February, 2024., which provides a low-latency link between the platforms and ground control stations, allowing remote operation of the free-flyers.

<!-- chunk {"id": "body-0047", "role": "body", "section": "4-B PX4Space", "weight": 1.0} -->

PX4Space is a customized version of the open-source PX4-Autopilot with adapted modules for the spacecraft. These modules provide control functionality for thruster-actuated vehicles. The link to the source code of PX4Space is available on the first page of this article. Alongside this firmware, we also provide an accompanying QGroundControl interface, providing the user easy access to PX4 vehicle setup and parameters, remote control communication, and a PX4 shell terminal.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Remark 1", "weight": 1.0} -->

As of the submission date for this article, parts of PX4Space have been merged with the PX4-Autopilot codebase. We expect the full codebase to be merged no later than May 2025.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Besides providing interfaces for sensors and actuators, PX4Space also implements the control architecture shown in Fig. 17. The control system comprises three cascaded P and PID controllers. The cascaded loop structure allows PX4Space to be used as a low-level controller of multiple setpoint options and to evaluate different control strategies. The position controller receives a position setpoint $p$ and regulates it through a P-controller, generating an internal velocity setpoint tracked by a PID for the velocity error. An attitude setpoint $\beta = {\{ f,\overline{q}\}}$ is generated, corresponding to a body-frame thrust $f$ and a quaternion attitude setpoint $\overline{q}$. The position controller can modify the attitude setpoint $\overline{q}$ to ensure feasible tracking for non-holonomic vehicles. The attitude controller implements a P-controller, which generates an angular rate setpoint $\gamma = {\{ f,\overline{\omega}\}}$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Lastly, the rate controller generates a wrench setpoint $\delta = {\{ f,\tau\}}$, through a PID to converge the angular velocity to the target.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Remark 1", "weight": 1.0} -->

To actuate each thruster on the platform, the wrench setpoint $\delta$ is processed by the \\acCA module. The \\acCA allows a selection between a normalized allocation ($f_{j} \in {\lbrack 0,1\rbrack}$) or a metric allocation ($f_{j} \in {\lbrack 0,f_{max}\rbrack}$, with $f_{max}$ being the maximum force that each actuator can produce), calculating desired forces for each thruster in Newtons for each thruster $j = {1,\ldots,8}$. It is worth noting that the above setpoints are specific to the implementation of the cascaded loop structure. These setpoints can be generated from any PX4 modules, manual inputs, or external entities such as an onboard computer. In the PX4Space firmware, the modules sc_pos_control, sc_att_control, sc_rate_control and sc_control_allocator implement each of the modules in Fig. 17 in the same order.

<!-- chunk {"id": "body-0052", "role": "body", "section": "4-C Onboard Computer", "weight": 1.0} -->

The OBC, at the center of the diagram in Fig. 16, is at the center of all interactions with the free-flyer. The operating system is Ubuntu 22.04, provided by the Nvidia Jetpack 6.0, and running ROS 2 Humble. This unit hosts ROS 2 interfaces for PX4Space and broadcasts selected internal topics in the firmware to ROS 2. Moreover, it communicates via ROS 2 with the MoCap computer to retrieve vehicle's odometry data (pose and velocities), later fused with the PX4 EKF2 estimator. The OBC also serves as a connection endpoint to ground control stations or any other low-latency routes the user requires.

<!-- chunk {"id": "body-0053", "role": "body", "section": "4-C Onboard Computer", "weight": 1.0} -->

The main task of the OBC is to run all high-level avionics tasks, such as vision-based position estimators, mapping nodes, high-level interface with payloads, or any other task that does not require the strict real-time guarantees of the low-level PX4 system or that cannot be run on its microcontroller. Furthermore, at a later stage, the OBC will allow us to interface with the Astrobee \\acFSW, allowing us to test our contributions locally. Since the OBC runs a generic Linux distribution, we also plan to support other \\acFSW stacks, providing a modular solution for different software needs.

<!-- chunk {"id": "body-0054", "role": "body", "section": "4-D Motion Capture Computer", "weight": 1.0} -->

The motion capture computer, shown at the top of Fig. 16, runs a Qualisys QTM server that interfaces with the MoCap camera network and ROS 2 clients and publishes high-frequency odometry data. The ROS package responsible for the data translation and augmentation with linear and angular velocities is available in This package is executed in a Windows Subsystem for Linux (WSL) environment. At this stage, any ROS 2 node can access odometry messages corresponding to the pose and velocities of the free-flyers.

<!-- chunk {"id": "body-0055", "role": "body", "section": "4-E Simulation", "weight": 1.0} -->

The \\acSITL simulation environment takes advantage of the Portable Operating System Interface (POSIX) compatibility of PX4, where the firmware can be simulated directly on any POSIX-compatible system. This allows easy and accurate simulation of the deployed software, allowing testing with identical software interfaces to the real system. This environment allows interfacing with all low-level control interfaces such as position, attitude, body rate, body force, and torque, as well as direct input allocation. Furthermore, radio-controlled modes such as manual, acro, or stabilized can be simulated as operating a real system in \\acSITL. We currently support Gazebo Garden (and newer versions) for the \\acSITL interface through PX4Space. It should be noted that the platforms are not restricted to devices that use PX4. As an example, we are currently working towards integrating the NASA Astrobee \\acFSW with ATMOS by routing the desired thrusts through PX4Space. Packages for this interfacing and to recreate our laboratory facilities are available in

<!-- chunk {"id": "body-0056", "role": "body", "section": "4-F Ground Control Station", "weight": 1.0} -->

The ground control station (GCS) is a remote operation console for laboratory platforms. Built around Foxglove Studio^22^2URL: Available on 15th of September, 2024., it communicates with each platform over FleetMQ peer-to-peer connection that optimizes the packet routing to the lowest latency path. In the GCS interface, we provide a position of the robotic platform in the MoCap area, feedback from the received thrust commands, vehicle velocity, arming, operation mode, and online status of the free-flyers. Lastly, a low-latency image channel is available, allowing us to remotely operate and navigate the platform. The GCS can be seen in Fig. 19.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Autonomy", "weight": 1.0} -->

In this section, we start by providing an overview of the communication schemes for multi-agent operations at our facility, followed by \\acNMPC schemes for nominal and offset-free tracking, and ending with a proposed planner for multi-agent operations. In particular, we consider direct allocation, body force and torque, and body force and attitude rate setpoints, as demonstrated below.

<!-- chunk {"id": "body-0058", "role": "body", "section": "5-A Autonomy and Multi-Agent Architecture", "weight": 1.0} -->

We first show the laboratory's autonomy architecture, depicted in Fig. 20.

<!-- chunk {"id": "body-0059", "role": "body", "section": "5-A Autonomy and Multi-Agent Architecture", "weight": 1.0} -->

The proposed architecture allows us to run multi-agent operations with different communication schemes, from centralized algorithms to distributed control and planning strategies. Agent communication is done over WiFi with a WiFi 7 capable access point. A centralized planning node is also available on the ground control station, which can provide safe trajectories to each agent. Lastly, onboard ATMOS, setpoint stabilization and trajectory tracking \\acNMPCs are used to track the planner trajectories to complete the assigned tasks. In the next section, we provide an overview of setpoint stabilization \\acNMPC schemes.

<!-- chunk {"id": "body-0060", "role": "body", "section": "5-B Nonlinear Model Predictive Control", "weight": 1.0} -->

Different control strategies can be tested on ATMOS through the offboard control interface of PX4, either via the onboard high-level compute unit or over a remotely connected client. In this section, three control strategies for setpoint regulation are detailed: i) direct control allocation, ii) body wrench setpoints, and iii) body force and angular rate setpoints. The implemented control schemes are open-source and available at

<!-- chunk {"id": "body-0061", "role": "body", "section": "5-B Nonlinear Model Predictive Control", "weight": 1.0} -->

We choose to employ \\iacNMPC strategy which minimizes a cost function $J{(x,u)}$, function of the state $x$ and control input $u$, along a receding horizon of length $N$. The state and control input vectors are constrained to evolve in the polytopes $x \in {\mathbb{X}}$ and $u \in {\mathbb{U}}$, and therefore, state and actuation constraints can be taken into account when calculating each control input. At each sampling time $k$ and over each step $n$ of the prediction horizon $N$, a state prediction $x{({n + \left. 1 \middle| k \right.})}$ is obtained from the previously predicted (or measured) state $x{(\left. n \middle| k \right.)}$, the optimized control input $u{(\left. n \middle| k \right.)}$, and the system dynamics $g{({x{(\left. n \middle| k \right.)}},{u{(\left.

<!-- chunk {"id": "body-0062", "role": "body", "section": "5-B Nonlinear Model Predictive Control", "weight": 1.0} -->

0 \middle| k \right.)}} = {\overset{\sim}{x}{(k)}}$, and an associated optimal cost value $J^{\ast}{({\overset{\sim}{x}{(k)}})}$. Each discrete control input is applied to the system in a Zero Order Hold (ZOH) fashion - a piece-wise constant input between sampling instances, that is, ${u{(t)}} = {u^{\ast}{(k)}{\forall t}} \in {\lbrack{k\Delta t},{{({k + 1})}\Delta t})}$ - abbreviated to $t \in {\lbrack k,{k + 1})}$ in this manuscript.

<!-- chunk {"id": "body-0063", "role": "body", "section": "5-B Nonlinear Model Predictive Control", "weight": 1.0} -->

The \\acNMPC optimization problem is then defined as

<!-- chunk {"id": "body-0064", "role": "body", "section": "5-B Nonlinear Model Predictive Control", "weight": 1.0} -->

where the cost function for setpoint stabilization is given by

<!-- chunk {"id": "body-0065", "role": "body", "section": "5-B Nonlinear Model Predictive Control", "weight": 1.0} -->

where $e$ is the error of the state $x$ with respect to the reference $\overline{x}$. The set ${\mathbb{X}}_{N}$ is a terminal control invariant set under a static state feedback controller, such as ${u_{K}{(t)}} = {Kx{(t)}}$, for a given gain matrix $K$. It is typical to use Linear Quadratic Regulators (LQR) and associated control invariant sets as terminal sets in \\acNMPC.

<!-- chunk {"id": "body-0066", "role": "body", "section": "5-B Nonlinear Model Predictive Control", "weight": 1.0} -->

Depending on the chosen control model - direct control allocation, body force and torque, or body force and angular rate - different models for $g{( \cdot )}$, state $x$ and error $e$ are used, and correspondingly, different state and control constraint sets. Below, we explain the models used in each scenario.

<!-- chunk {"id": "body-0067", "role": "body", "section": "5-B.1 Direct Control Allocation", "weight": 1.0} -->

In direct control allocation, each thruster is modeled in the dynamics through allocation matrices $D$ and $L$. These represent the resulting center-of-mass force and torque applied by each thruster.

<!-- chunk {"id": "body-0068", "role": "body", "section": "5-B.1 Direct Control Allocation", "weight": 1.0} -->

In this case, $g{(x,u)}$ is the discretized (using, for instance, a 4th order Runge Kutta method) version of the model

<!-- chunk {"id": "body-0069", "role": "body", "section": "5-B.1 Direct Control Allocation", "weight": 1.0} -->

where $D \in {\mathbb{R}}^{3 \times 4}$ and $L \in {\mathbb{R}}^{3 \times 4}$ allowing us to use eight thrusters with four decision variables, ${R{(q)}} \in {{\mathbb{S}}{\mathbb{O}}^{3}}$ \[, Eq. 76\] represents the rotation matrix associated with the quaternion $q$, $\Xi{(q)}$ \[, Eq. 54\] represents the skew-symmetric matrix of $q$, $m \in {\mathbb{R}}_{> 0}$ represents the system mass, and $M \in {\mathbb{R}}^{3 \times 3}$ its inertia matrix. Similarly, the constraint set $\mathbb{U}$ represents the minimum and maximum bounds for each thruster, as ${\mathbb{U}} \triangleq \left.

<!-- chunk {"id": "body-0070", "role": "body", "section": "5-B.1 Direct Control Allocation", "weight": 1.0} -->

\{{u_{\lbrack j\rbrack} \in {\mathbb{R}}} \middle| {{{- f_{max}} \leq u_{\lbrack j\rbrack} \leq f_{max}},{j = {1,\ldots,4}}}\} \right.$, and where each $u_{\lbrack j\rbrack}$ corresponds to an aligned thruster pair ($u_{\lbrack j\rbrack} > 0$ actuates one thruster, whereas $u_{\lbrack j\rbrack} < 0$ actuates the opposite one). The error $e$ for this strategy is defined as

<!-- chunk {"id": "body-0071", "role": "body", "section": "5-B.2 Body Force and Torque", "weight": 1.0} -->

In this scenario, the \\acNMPC generates desired body-frame force and torques. The model's continuous-time version of $g{(x,u)}$ is similar to the one considered for control allocation and is defined as

<!-- chunk {"id": "body-0072", "role": "body", "section": "5-B.2 Body Force and Torque", "weight": 1.0} -->

where the control input vector $u$ is defined as $u = {\lbrack f^{T},\tau^{T}\rbrack} \in {\mathbb{U}} \subset {\mathbb{R}}^{6}$ and the state as $x = {\lbrack p,v,q,\omega\rbrack} \in {\mathbb{X}} \subset {{{\mathbb{R}}^{9} \times {\mathbb{S}}}{\mathbb{O}}{}}$, similarly to the Direct Control Allocation model. An important distinction between controlling a body force and torque and the control allocation model is the necessarily more conservative control constraint bounds to avoid saturation. However, in certain scenarios, using a body wrench input may use fewer control variables, leading to a faster control rate. The control constraint set is defined as ${\mathbb{U}} \triangleq \left.

<!-- chunk {"id": "body-0073", "role": "body", "section": "5-B.3 Body Force and Angular Rate", "weight": 1.0} -->

Lastly, we tested offboard control with a body force and desired angular rate. This simpler model considers as control inputs a target force and angular velocity, state as $x = {\lbrack p,v,q\rbrack} \in {\mathbb{X}} \subset {{{\mathbb{R}}^{6} \times {\mathbb{S}}}{\mathbb{O}}{}}$, and $g{(x,u)}$ the discretized version of

<!-- chunk {"id": "body-0074", "role": "body", "section": "5-B.3 Body Force and Angular Rate", "weight": 1.0} -->

The control constraint set is defined as ${\mathbb{U}} \triangleq \left. \{{{f \in {\mathbb{R}}^{3}},{\omega \in {\mathbb{R}}^{3}}} \middle| {{{- f_{max}} \leq f_{\lbrack x,y,z\rbrack} \leq f_{max}},{{- \omega_{max}} \leq \omega_{\lbrack x,y,z\rbrack} \leq \omega_{max}}}\} \right.$ and the setpoint $\gamma = {\lbrack f^{T},\omega^{T}\rbrack}$. Furthermore, note that the attitude dynamics are not considered in this model, resulting in a suboptimal controller when compared to the previous scenario, with the advantage of being faster to solve online. The error $e$ for this control approach is given by

<!-- chunk {"id": "body-0075", "role": "body", "section": "5-C Offset-Free Nonlinear Model Predictive Control", "weight": 1.0} -->

The dynamics for the MPC controller proposed in Sec. 5-B assume that the system is undisturbed. However, often, this is not the case. On microgravity testbeds, uneven surfaces and model imperfections might cause a bias in the system dynamics, inducing steady-state errors on reference tracking tasks. To overcome this limitation, we propose using an offset-free NMPC scheme based on the work. Let us consider the body force and torque model in eq. 5, modified to include the disturbances $d_{v} \in {\mathbb{R}}^{3}$ and $d_{\omega} \in {\mathbb{R}}^{3}$ in the translation and attitude dynamics, obtaining the disturbed model

<!-- chunk {"id": "body-0076", "role": "body", "section": "5-C Offset-Free Nonlinear Model Predictive Control", "weight": 1.0} -->

As the disturbances are unknown, we employ an \\acEKF to estimate ${\hat{d}}_{v}$ and ${\hat{d}}_{\omega}$ using the residual of the expected dynamics with respect to $d_{\omega} = d_{v} = \begin{bmatrix}
\end{bmatrix}^{T}$ and the true dynamics in eq. 8 in the \\acEKF measurement update step, at each sampling time $k$. As the system in eq. 8 is not fully controllable, we linearize the quaternion dynamics with the model in eq. 8c where ${}q$ corresponds to the vector component of the quaternion $q$, defined as $q:=\begin{bmatrix}
\end{bmatrix}^{T}$.

<!-- chunk {"id": "body-0077", "role": "body", "section": "5-C Offset-Free Nonlinear Model Predictive Control", "weight": 1.0} -->

Note that the rotation matrix $R{(q)}$ is still fully defined, as the scalar component of $q$ can be obtained with $q_{w} = \sqrt{1 - {q^{T}q}}$, and the matrix $\overset{\sim}{\Xi}$ corresponds to the three last rows of $\Xi$. At each sampling time, we solve the \\acNMPC in eq. 1 with ${\hat{x}{({i + \left. 1 \middle| k \right.})}} = {g{({\hat{x}{(\left. i \middle| k \right.)}},{u{(\left. i \middle| k \right.)}})}}$ given by the discretization of eq. 8, obtaining $u^{\ast}{(k)}$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "5-C Offset-Free Nonlinear Model Predictive Control", "weight": 1.0} -->

It is worth noting that the wrench model in eq. 8 can be extended to the direct allocation model of eq. 3. Translation disturbances can also be included in eq. 6, but this simplified model does not allow disturbances in the attitude dynamics.

<!-- chunk {"id": "body-0079", "role": "body", "section": "5-D Thruster Force to Pulse-Width Modulation", "weight": 1.0} -->

As each actuator requires a \\acPWM signal as an input, we must convert our desired actuator thrust to a \\acPWM duty cycle. Consider the variable $\lambda \in {\lbrack 0,1\rbrack}$, where $\lambda = 1$ corresponds to a thruster $j$ being open for the entire time duration between sampling times, $\lambda = 0$ being closed for the same duration, and $\lambda \in {}$ the thruster being open a corresponding percentage of time between time sampling times.

<!-- chunk {"id": "body-0080", "role": "body", "section": "5-E Planning Schemes", "weight": 1.0} -->

While MPC provides real-time control by tracking trajectories and rejecting disturbances, high-level planning frameworks play a crucial role in guiding autonomous systems, especially in complex, multi-agent scenarios. To this end, we here present a lightweight, adaptable planning scheme for multi-robot motion planning with Signal Temporal Logic (STL) specifications. The STL planner considers specifications over real-valued signals in both the signal dimension and the time dimension, making it a powerful tool for specifying properties of dynamical systems. Examples include, but are not limited to, fuel consumption, keeping vehicles within certain regions for a given amount of time, avoiding obstacles, and triggering actions at specific time instances. An important aspect of STL is the inherent validation of the proposed plan, in terms of feasibility and correctness.

<!-- chunk {"id": "body-0081", "role": "body", "section": "5-E Planning Schemes", "weight": 1.0} -->

We define a simplified fragment of STL that specifies desired properties of $n$-dimensional, finite, continuous-time signals $\mathbf{x}:{{\mathbb{R}}_{\geq 0}\rightarrow X \subseteq {\mathbb{R}}^{n}}$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Results", "weight": 1.0} -->

(a) ATMOS \acSITL performance with direct control allocation.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Results", "weight": 1.0} -->

(b) ATMOS hardware performance with direct control allocation.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Results", "weight": 1.0} -->

(c) ATMOS \acSITL control inputs with direct control allocation.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Results", "weight": 1.0} -->

(d) ATMOS hardware control inputs with direct control allocation.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Results", "weight": 1.0} -->

(a) ATMOS \acSITL performance with force and torque setpoints.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Results", "weight": 1.0} -->

(b) ATMOS \acSITL force and torque control inputs.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Results", "weight": 1.0} -->

In this section, we show and discuss the results achieved using some of the controllers and planners in Sec. 5, both in \\acSITL and in the real ATMOS platform. For an in-depth analysis of all results, we refer the reader to the video: click here for the video.

<!-- chunk {"id": "body-0089", "role": "body", "section": "6-A Offboard \\\\acNMPC with ATMOS \\\\acSITL", "weight": 1.0} -->

The \\acSITL simulation follows the implementation described in Fig. 18. First, we test the direct control allocation method using the model in eq. 3. We set a sequence of multiple setpoints, spaced in time by $20\ s$, and with translations of $1\ m$ in the $x$ and $y$ axis, as well as of $45\ {^\circ}$ around the $z$ axis. The results are shown in Figs. 21(c) and 21(a) ‣ 6 Results ‣ Towards Open-Source and Modular Space Systems with ATMOS"). In Fig. 21(c), we observe the normalized thrust set on each thruster $i = {1,\ldots,8}$. We can observe in Fig. 21(a) that the simulated platform can converge to the required setpoints with minimal overshoot and no steady-state error. This is expected as no external disturbances are considered in this case, and the actuation model is to the lowest level of control possible for the platform.

<!-- chunk {"id": "body-0090", "role": "body", "section": "6-A Offboard \\\\acNMPC with ATMOS \\\\acSITL", "weight": 1.0} -->

Then, considering the same setpoints but the body force and torque model in eq. 5, we collected the results in Fig. 22. Note that in this scenario, the \\acNMPC generates forces and torques that are then translated to thruster inputs. To conveniently observe this, we included in Fig. 22(b) the \\acNMPC forces $f_{x},f_{y}$ and torque $\tau_{z}$, as well as normalized inputs to each thruster (noting that a value of $1.0$ equals maximum thrust $\overline{f}$). To avoid saturation, we limited the maximum forces to $f_{max} = {1.5\ }$ on each axis. We may also observe that for half the maximum force available per axis, the resulting input to some thrusters is considerably larger than half of the maximum thrust, particularly when translation and attitude changes are required.

<!-- chunk {"id": "body-0091", "role": "body", "section": "6-A Offboard \\\\acNMPC with ATMOS \\\\acSITL", "weight": 1.0} -->

As the maximum force per axis is smaller than in the direct allocation case, we expect the translation to have a slower transient than in the direct allocation scenario, as can be seen when comparing Fig. 21(a) to Fig. 22(a). Lastly, the planning section will demonstrate the results of control with rate setpoints.

<!-- chunk {"id": "body-0092", "role": "body", "section": "6-A Offboard \\\\acNMPC with ATMOS \\\\acSITL", "weight": 1.0} -->

(a) ATMOS hardware performance with wrench setpoints.

<!-- chunk {"id": "body-0093", "role": "body", "section": "6-A Offboard \\\\acNMPC with ATMOS \\\\acSITL", "weight": 1.0} -->

(c) ATMOS hardware control inputs with wrench setpoints.

<!-- chunk {"id": "body-0094", "role": "body", "section": "6-A Offboard \\\\acNMPC with ATMOS \\\\acSITL", "weight": 1.0} -->

(d) ATMOS hardware offset-free NMPC control inputs with wrench setpoints.

<!-- chunk {"id": "body-0095", "role": "body", "section": "6-B Offboard \\\\acNMPC with ATMOS Hardware", "weight": 1.0} -->

After performing simulations on the \\acSITL simulator, we implemented the methods on the ATMOS platform. The experimental setup is very similar to the simulated one, with the addition of \\acmocap for ground-truth.

<!-- chunk {"id": "body-0096", "role": "body", "section": "6-B Offboard \\\\acNMPC with ATMOS Hardware", "weight": 1.0} -->

In Fig. 21(b) and Fig. 21(d), we present the hardware results of direct control allocation with ATMOS. In this scenario, we use the discretized version of the model in eq. 3. The platform can track the desired references, but it is also possible to observe a steady-state error among some of the setpoints. The magnitude of the error is approximately $10\ {}$ in position and $5\ {^\circ}$ in attitude. We identify three sources for such error: i) floor unevenness, ii) inertial parameters mismatch, and iii) actuation model mismatch. Considering the first source, we can infer that an uneven floor will induce a constant residual force on the platform. Since such force is not in the model, it cannot be compensated in the current \\acNMPC framework. These forces would cause the platform the have a steady-state error with a constant input value that is reciprocal to the disturbance effect. Possible solutions to mitigate this source of error are using offset-free \\acNMPC schemes, similar to adding integral action to the controller.

<!-- chunk {"id": "body-0097", "role": "body", "section": "6-B Offboard \\\\acNMPC with ATMOS Hardware", "weight": 1.0} -->

Regarding the second source of error, we note that during operation, both the mass of the platform and inertia change as the platform loses mass due to using the onboard propellant. Although this might change the transient behavior of the platform and cause overshooting or undershooting, it would not be sufficient to cause steady-state errors. Lastly, the actuation model considered for the \\acNMPC scheme is rather simplistic and does not consider losses in efficiency when triggering more than a single thruster at each sampling time. Such an event will yield a lower input than expected, causing the system to move or rotate slower than the predicted model. The effect would be similar to a wrong inertial parameter estimate. It is worth noting that despite the performance difference discussed previously, moving from a simulated environment to a real platform provided similar results, with relatively accurate transient behavior. In particular, the performance on the $x$-axis was largely unaffected (as these setpoints were placed in flatter floor areas), including during transient response.

<!-- chunk {"id": "body-0098", "role": "body", "section": "6-B Offboard \\\\acNMPC with ATMOS Hardware", "weight": 1.0} -->

To overcome the effect of external disturbances, we tested the Offset-free \\acNMPC scheme shown in Sec. 5-C using the model in eq. 8. This control scheme is compared against the nominal \\acNMPC with the model in eq. 5. The results can be seen in Sec. 6-A. Comparing the two columns, it is possible to observe the effect of the offset-free compensation, particularly on position $p_{y}$ and attitude $\psi$. Through the inclusion of the \\acEKF estimator, the external disturbances $d_{v}$ and $d_{\omega}$ are estimated online and the \\acNMPC scheme counteracts its effect, resulting in a zero steady-state error. In the generated control signals, we can observe that in Fig. 23(d) there exists a large steady-state input, particularly in the $60\ s$-$70\ s$ interval, to allow the system to compensate the estimated external disturbance.

<!-- chunk {"id": "body-0099", "role": "body", "section": "6-C Planning", "weight": 1.0} -->

We present the tracking results of a Bézier trajectory, satisfying a high-level specification using the Bézier trajectory parametrization and spatially robust STL planner from Sec. 5-E with the rate controller in eq. 6.

<!-- chunk {"id": "body-0100", "role": "body", "section": "6-C.1 Single-Agent Scenario", "weight": 1.0} -->

The STL specification we consider is $\phi = {{\diamondsuit_{\lbrack 0,60\rbrack}{({p^{1} \in B})}} \land {\diamondsuit_{\lbrack 0,60\rbrack}{({p^{1} \in D})}} \land {\square_{I}{\lbrack 0,60\rbrack}{({p^{1} \notin {Obs}})}}}$, specifying that the robot should visit regions $B$ and $D$ at any time in the horizon and should avoid the obstacle for all time in the time horizon, $t \in {\lbrack t_{0},t_{f}\rbrack}$. The results are presented in Fig. 24, showing the $p_{x}^{1}$ and $p_{y}^{1}$ positions in the plane and over time as well as the planned and executed spatial robustness $\rho_{\phi}$.

<!-- chunk {"id": "body-0101", "role": "body", "section": "6-C.1 Single-Agent Scenario", "weight": 1.0} -->

Note that the goal of the planner is to maximize $\rho_{\phi}$ which entails maximizing the lower bound of the presented robustness value over time. As the size of the regions of interest ($B$ and $D$) is limited (with a maximal distance to violating of $0.25\ m$) the obtained spatial robustness of $\rho_{\phi} = {0.25\ m}$ also ensures a clearing distance of $0.25\ m$ to the obstacle as it is part of the STL specification. If we would increase the size of the regions, the planner would consider an increased clearing distance whenever possible.

<!-- chunk {"id": "body-0102", "role": "body", "section": "6-C.2 Multi-Agent Scenario", "weight": 1.0} -->

Consider now two robots, $R^{1}$ and $R^{2}$ with a specification over a horizon of $t_{0} = 0$ to $t_{f} = 90$.

<!-- chunk {"id": "body-0103", "role": "body", "section": "6-C.2 Multi-Agent Scenario", "weight": 1.0} -->

$A$, $B$, $C$, and again $A$ in order while always avoiding the obstacle.

<!-- chunk {"id": "body-0104", "role": "body", "section": "6-C.2 Multi-Agent Scenario", "weight": 1.0} -->

$D$, $A$, $B$, and again $D$ in order while always avoiding the obstacle.

<!-- chunk {"id": "body-0105", "role": "body", "section": "6-C.2 Multi-Agent Scenario", "weight": 1.0} -->

The global STL specification is then $\phi = {\phi^{1} \land \phi^{2}}$. We additionally specify collision avoidance in the planner layer with implementation details. The results are presented in Fig. 25 with a planned robustness value of $\rho_{\phi} = {0.25\ m}$. Notice here that it is more apparent that the tracking of the Bézier curves lags behind the planned trajectories. While we penalize accelerations in the planner, we are not able to explicitly constrain them. The spatial robustness in the motion plan ensures that these tracking errors can be accommodated for w.r.t. the satisfaction of the STL specification.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Discussion and Conclusions", "weight": 1.5} -->

An overview of existing space robotics research facilities and the different strategies used to achieve frictionless motion has been presented, as well as platform limitations. Based on these works, we created the KTH Space Robotics Laboratory with its modular free-flying ATMOS platforms and multiple support systems.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Discussion and Conclusions", "weight": 1.5} -->

As a significant component of our contribution is the open-source availability of both the hardware and the software of this facility, it is important to qualitatively assess its potential impact on the community. To this end, we are maintaining an open repository of laboratories using ATMOS or PX4Space, available in Due to the flexibility of PX4Space, adapting the software to other free-flyers requires only parameter adjustments regarding thruster placement and inertial parameters. It is also possible to adjust PX4Space to propeller-based actuation using the control and metric allocation modules developed in our software stack. An example of such a platform is available. With the available documentation on PX4Space, step-by-step guide on building ATMOS, and openly available SITL simulator, we look forward to seeing the next users of our contribution.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Discussion and Conclusions", "weight": 1.5} -->

From the results in Sec. 6, we may conclude that our goal of seamless transfer of experiments from simulation to hardware was achieved. Further improvements to the simulator will include adding floor unevenness disturbance using the measurements from Fig. 2(b) and thruster efficiency loss models, reducing the disparity of hardware experiments through higher fidelity simulation.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Discussion and Conclusions", "weight": 1.5} -->

To complete these systems, some trade-offs had to be made. To achieve a large operational area at a reduced cost, the precision of granite tables was exchanged with the lower cost per area solution of using a self-leveling epoxy floor. These leveling issues are also present in other state-of-the-art facilities. On the other hand, the proposed offset-free MPC aids in overcoming such issues for setpoint stabilization. Regarding tracking performance, we expect that using estimators for dynamic residuals can improve the platform performance. Another compromise was made in the 3\\acdof of ATMOS, versus other platforms capable of 5 and 6 \\acdof. With ATMOS, the priority was on providing a modular, low-cost platform based on commercial off-the-shelf parts. This leads to an easy-to-replicate platform, but more importantly, it is easily adaptable to different needs. Users may extend the platform with spherical air bearings to provide 5\\acdof, install gimbaled systems for testing small satellites, and integrate flight-certified hardware, among many other possible use cases.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Discussion and Conclusions", "weight": 1.5} -->

Future work will involve finalizing the integration of the NASA Astrobee \\acFSW in ATMOS, integrating floor disturbance plugins and thruster efficiency loss models, and implementing collaborative load transportation strategies and fault-tolerant control schemes. We also aim to finalize the integration of our software with PX4-Autopilot to allow easier access to the software and improved long-term support.
