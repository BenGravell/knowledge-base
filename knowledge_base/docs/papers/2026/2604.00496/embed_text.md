## Introduction

Quadrotors are widely used in aerial robotics for their simplicity and agility, yet rigid-frame designs limit adaptability in cluttered or dynamic environments. To address this, we propose QuadSoft, a novel platform with tendon-driven flexible arms that can reconfigure in flight through continuous-curvature deformation. Unlike conventional morphing designs that rely on rigid hinges or discrete joints, QuadSoft leverages soft morphology to achieve thrust vectoring while maintaining structural integrity. This capability enables navigation in tight spaces, improved aerodynamic efficiency, and enhanced stability. By combining a continuum mechanics approach with standard flight control, QuadSoft bridges the gap between compliant robotics and the need for versatile, resilient aerial platforms capable of operating in real-world conditions.

Figure 1: QuadSoft prototype during outdoor flight. The four arms are tendon-driven and flexible, actuated by servomotors to enable in-flight morphological adaptation.

### I-A State of the Art

Quadrotors have become central in aerial robotics for their efficiency, stability, and simplicity, yet their rigid-frame architectures inherently limit adaptability in cluttered or dynamic environments \[31, 1, 4, 28 with appendage repurposing for locomotion plasticity enhancement")\]. Soft robotics has shown that flexible, biologically inspired structures can enhance versatility and safety across manipulators and ground robots, with pneumatic, tendon-driven, and smart-material actuators enabling precise shape control and compliance \[12, 17, 32: a review"), 14, 16\]. However, the application of these principles to aerial vehicles remains limited, with only partial solutions addressing flexibility through distributed-parameter modeling and delay-resistant adaptive control.

Existing morphing quadrotors each fall short in different ways. Impact-resilient designs like Morphy prioritize crash recovery over active reconfiguration. Dual-axis tilting-rotor mechanisms achieve 6-DOF control but at the cost of mechanical complexity and additional failure points. Hybrid platforms such as SMORS combine rigid arms with soft components yet offer only partial deformation. Tendon-driven platforms like those presented in and employ discrete hinge-like bending points and typically require hexarotor configurations to compensate for their limited DOF. In these systems, the tendon actuation is primarily intended for surface grasping rather than for improving maneuverability or flight control. Beyond quadrotors, morphing-wing UAVs and inflatable structures like SFAR target aerodynamic performance and safety, respectively, rather than active in-flight morphological reconfiguration.

In contrast, QuadSoft adopts a constant-curvature continuum approach in a standard X-quadrotor, achieving full 6-DOF actuation with four rotors---without rigid tilting joints, extra propulsion units, or specialized flight control hardware. Notably, the design is validated on a standard, unmodified PX4 autopilot, as detailed in the following section.

### I-B Contribution

Building on earlier theoretical work on constant-curvature soft aerial vehicles, this paper focuses on the design, construction, and real-world experimental validation of QuadSoft. The main contributions are:

Continuum Design and Construction: A tendon-driven soft arm based on a constant-curvature approach, enabling smooth in-flight reconfiguration within a standard X-quadrotor configuration---without discrete joints or rigid hinges.

Geometric Mapping: A closed-form mapping from servomotor input to arm curvature is derived and experimentally validated, linking tendon actuation to 6-DOF thrust-vectoring capability.

Outdoor Flight Validation: First outdoor flight tests of a continuum-morphing quadrotor, demonstrating stable hover and morphology-driven translation using a standard, unmodified PX4 autopilot.

Baseline for Control Allocation: Physical stability validated up to 22^∘^ of curvature (within a 35^∘^ design envelope), providing a foundation for future custom mixer development in fully actuated soft UAVs.

### I-C Organization

The remainder of this paper is organized as follows. Section II formulates the central challenge of designing the QuadSoft with tendon-driven soft arms. The geometric mapping from servomotor input to arm curvature and propeller orientation is derived in Section III. Section IV describes the mechanical and electronic implementation of the proposed design. Section V presents the outdoor experimental validation, focusing on hover stability and morphology-induced translation. Finally, Section VI concludes the paper and outlines future research directions.

## Problem Statement

Designing a morphing quadrotor with soft actuated arms introduces a central challenge: enabling in-flight reconfiguration without compromising flight stability. The inherent flexibility of soft structures allows morphological adaptation but also induces deformations and vibrations that can degrade control performance. Furthermore, maintaining a lightweight structure is critical, as additional mass increases the required lift forces, which in turn amplify structural deformations. This challenge is divided into two interconnected subproblems:

Subproblem A --- Mechanical Design: Developing a lightweight, tendon-driven arm mechanism that balances compliance with structural stability to minimize oscillations while allowing sufficient curvature for reconfiguration.

Subproblem B --- Integration and Modeling: Deriving the actuator--curvature--propeller mapping to ensure that morphological changes translate into predictable and controllable motions while preserving baseline stability.

The solution to Subproblem A is detailed in Section IV, while Subproblem B is addressed in Section III and subsequently validated through the outdoor experiments presented in Section V.

## Geometric Mapping of Servomotor to Arm Curvature

The angular position of the propellers with respect to the main body frame can be expressed as a function of the servomotor angle. This relationship arises from the geometric constraints imposed by the tendon-driven arm. Fig. 2 illustrates the relevant variables: $L_{a}$, the fixed arc length determined by the semi-rigid core, and $L_{b}$, the variable length defined by the tendon pulled by the servomotor. Since the total tendon length remains constant (highlighted in purple in Fig. 2), the change in length $\DeltaL_{c}$ caused by a rotation $\alpha$ of the servomotor can be obtained using trigonometry:

where $r$ is the radius of the tendon trajectory, $\alpha$ is the servomotor angle, and $K$ is a proportionality constant that accounts for unmodeled effects.

The arc lengths $L_{a}$ and $L_{b}$ are related to the arm's angular displacement $\beta$:

where $R$ is the nominal radius of the rigid arc, $R - L_{1}$ corresponds to the effective radius when the tendon is pulled, and $\beta$ is the arm curvature angle. Since $\beta$ is identical in both cases,

From this relation, the effective radius $R$ is expressed as a function of $L_{a}$, $L_{b}$, and $L_{1}$:

Finally, the curvature angle $\beta$ is as follows:

Together, these expressions provide a complete geometric mapping from servomotor input $\alpha$ to arm curvature $\beta$, and thus to the propellers' angular orientation relative to the body frame.

Figure 2: Schematic of the QuadSoft’s flexible arm, showing the geometric variables used to calculate the bending angle β as a function of the servo motor’s rotation angle α. The lengths La, Lb, Lc, and L3 represent segments of the arm and its base, while β describes the arm’s curvature due to flexibility.

Experimental measurements further showed that $\beta$ can be well approximated by a cubic interpolation of the form:

where the coefficients $(a_{i},b_{i},c_{i},d_{i})$ are obtained via data fitting for each arm.

Fig. 3(c) illustrates this mapping, showing the experimental $\alpha$--$\beta$ curve along with the operational limits beyond which vehicle lift would be compromised.

Figure 3: Design and actuation of the QuadSoft. (a) Complete QuadSoft platform. (b) Soft arm with semi-rigid carbon fiber insert and air chambers for vibration damping. (c) In the graph, the geometric mapping between the servo input α and the arm curvature β is shown in blue, while the cubic interpolation obtained using Eq.6 is shown as a red dashed line. (d) Photographs of the QuadSoft with arms at different bending angles. (e) Dual-cable tendon mechanism: one cable induces positive curvature, the other negative. This design ensures precise and reliable arm reconfiguration while balancing flexibility and structural stability.

Figure 4: Electrical system diagram of the drone with a PX4 controller. It shows power distribution from a LiPo battery, motor control via ESCs, and servo connections through a distributor and UBEC. A capacitor reduces electrical noise, and the servos adjust tendon angles for morphing. The RC receiver enables remote control.

## Mechanical and Electronic Design

### IV-A Structural Design and Stiffness

The soft arm features a hybrid structure---a flat carbon fiber core embedded in a TPU matrix with internal air cavities---designed for anisotropic stiffness. This planar core provides high compliance for vertical bending while remaining exceptionally stiff in torsion, preventing unwanted yaw-axis twisting. Furthermore, the TPU and air chambers act as a vibration damper, dampening high-frequency motor vibrations to preserve baseline flight stability. The platform's mass distribution is detailed in Table II.

### IV-B Actuation Mechanism

Active reconfiguration relies on two antagonistic nylon tendons connecting a base servomotor to a tip pulley (Fig. 3b). Adjusting tendon tension induces continuous positive or negative bending (Fig. 3e). The arm design has a physical bending limit of 28^∘^, since propeller efficiency decreases beyond 25^∘^. This limit is set by the gap between the arm segments, which prevents exceeding the allowable curvature and avoids propeller-arm collisions. By physically constraining the maximum bending angle, the design also mitigates material fatigue. Moreover, adjusting the segment spacing during manufacturing provides a simple parametric means to tune arm compliance. Arm specifications are listed in Table I.

Elastic modulus (MPa)

Tensile strength (MPa)
Flexural modulus (MPa)

TABLE I: Specifications of the flexible arms and tendons used in the morphing mechanism of the QuadSoft. These properties ensure lightweight construction, mechanical flexibility, and structural integrity for stable flight.

4 × (Motors and propellers)

TABLE II: Mass budget of the proposed soft-Quadrotor, detailing the absolute and relative weight contributions of each component.

### IV-C Electronics Integration

The electronic architecture is deliberately designed to demonstrate that complex soft-morphing can be managed by standard, off-the-shelf avionics. The core of the system is a Pixhawk^®^ V5+ autopilot running an unmodified PX4 flight stack.

Power is supplied by a 12V 3S LiPo battery via a Power Distribution Board (PDB). The Pixhawk simultaneously manages baseline flight stabilization---commanding the brushless motors via standard ESCs---while synchronizing the servomotors responsible for tendon actuation. To prevent voltage drops during high-torque reconfigurations, a dedicated UBEC regulates a consistent 5V supply to the servomotors.

Standard RC telemetry is utilized for wireless manual input and real-time monitoring. Ultimately, this integrated setup (detailed in Fig. 4) ensures reliable propulsion and precise tendon actuation, validating that morphology-driven maneuverability in soft UAVs does not necessitate custom hardware ecosystems.

## Experiments

(b) Position and velocity tracking

Figure 5: Hover stability experiment with flexible arms. (a) 3D trajectory during take-off, hover, and landing (blue: actual, red dashed: setpoint); Background colors denote the flight modes (green: manual, yellow: hold), and the transition between modes is indicated in red. (b) Position (left) and velocity (right) tracking along x, y, z, showing smooth setpoint following across mode transitions.

To evaluate the QuadSoft platform under realistic, unconstrained conditions, we conducted outdoor flight tests subjected to stochastic wind disturbances. Unlike indoor trials that rely on high-precision Motion Capture (MoCap) systems, these outdoor experiments demonstrate the system's operational autonomy using only on-board sensing (IMU/GPS) and a standard, unmodified PX4 control stack. We focused on two critical aspects of soft-rigid hybrid flight:

Baseline Hover Stability: The platform's ability to reject external perturbations and maintain stable setpoints despite the inherent compliance of the soft arms.

Morphology-Induced Translation: The dynamic response of the vehicle when continuous-curvature arm bending is actively used to generate horizontal displacement without altering the vehicle's global pitch/roll attitude.

### V-A Hover Stability

We first evaluated the QuadSoft's ability to maintain stable hovering in a zero-curvature configuration. The sequence consisted of a take-off to 4 m, a 15 s hover in HOLD mode, and a manual landing under outdoor conditions with light wind gusts.

Fig. 5(a) shows the 3D trajectory, demonstrating that the actual path closely follows the setpoints with negligible lateral drift. Fig. 5(b) presents the corresponding position and velocity profiles. The controller maintains near-zero steady-state error during the hover phase and recovers seamlessly after mode transitions.

Crucially, high-speed footage and telemetry confirmed that passive arm deflections at full hovering thrust remained below $1^{\circ}$. This validates the efficacy of the anisotropic structural design (Section IV-A), proving that the requisite flexibility for tendon actuation does not introduce unmodeled aeroelastic oscillations or degrade the baseline stability expected from a rigid quadrotor.

### V-B Morphology-Induced Translation

The core validation of our continuum approach involved generating horizontal displacement purely through tendon-driven arm actuation. Tests were performed in ALTITUDE HOLD mode, isolating horizontal thrust-vectoring from $z$-axis altitude control.

(b) Position and velocity tracking

(c) Arm curvatures and pitch/roll angles

Figure 6: Morphology-induced translation with tendon activation. (a) 3D trajectory (arrows indicate motion direction; purple dot marks tendon activation). (b) Position and velocity tracking showing steady altitude during translation. (c) Arm curvature angles βi and vehicle attitude (ϕ, θ), confirming the link between continuum actuation and horizontal displacement with minimal attitude coupling.

As illustrated in Fig. 6(a) and (b), upon tendon activation, the vehicle achieved smooth $x$--$y$ translation while strictly maintaining its target altitude. A gradual velocity increase coincided precisely with the onset of arm curvature.

Fig. 6(c) presents the transient response during reconfiguration, detailing the measured arm curvatures ($\beta_{i}$) alongside the vehicle's attitude ($\phi$, $\theta$). As the arms actively bend to induce forward motion, the global pitch and roll remain remarkably stable, staying within a $\pm 5^{\circ}$ envelope. The brief excursions up to $10^{\circ}$ correlate with corrective actions against wind gusts rather than actuation-induced instability.

Most importantly, the data demonstrates that during the dynamic transition phase (from $0^{\circ}$ to the validated $22^{\circ}$ curvature), the change in the vehicle's thrust vector is smoothly compensated by the native PX4 rate controllers. This confirms that the structural damping of the soft arms prevents resonance modes, allowing morphology-driven directional motion with minimal attitude deviations. Ultimately, these unconstrained outdoor trials establish a robust physical baseline, proving the viability of tendon-driven continuum morphing for adaptive aerial systems.

## Conclusion

The experimental evaluation of the QuadSoft platform leads to several critical conclusions regarding the viability and control of soft aerial vehicles.

First, the outdoor flight data demonstrates that the inherent vulnerabilities of soft structures---namely, aeroelastic vibrations and uncontrolled deformations---can be successfully mitigated through anisotropic structural design. Because the vehicle maintained stable hovering and its global attitude deviations remained within $\pm 5^{\circ}$ during dynamic reconfiguration, we conclude that the TPU-carbon hybrid arms act as an effective vibration damper.

Second, the successful morphology-induced translation confirms that a constant-curvature continuum approach is a highly effective mechanism for thrust vectoring. By generating forward and lateral displacements while maintaining a near-level pitch and roll, the results establish that tendon-actuated soft arms can practically decouple a vehicle's position from its orientation.

Finally, achieving these stable transitions under stochastic wind disturbances using a standard, unmodified PX4 autopilot leads to a fundamental conclusion: morphological compliance can be seamlessly integrated into existing flight stacks as a physical asset rather than a control disturbance. Ultimately, this work provides a validated physical baseline for fully actuated soft UAVs. Based on these findings, future research will focus on developing custom control allocation matrices (mixers) within the open-source PX4 ecosystem to fully exploit the platform's 6-DOF maneuverability.

Figure 7: Sequence of an outdoor flight demonstrating forward displacement generated by tendon-driven arm actuation under altitude hold. The snapshots illustrate the QuadSoft’s trajectory during morphological reconfiguration, highlighting controlled horizontal motion achieved without affecting altitude.
