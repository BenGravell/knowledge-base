<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The QuadSoft: Design, Construction, and Experimental Validation of a Soft and Actuated Quadrotor

Topics include Robotics, Aerial robotics, Stability analysis, Safety, Control, QuadSoft, Soft robotics.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents QuadSoft, a novel fully actuated quadrotor equipped with continuous-curvature, tendon-driven soft robotic arms. The design combines a semi-rigid central frame with flexible arms, enabling controlled structural reconfiguration during flight without altering the propeller layout. Unlike existing soft aerial platforms that rely on discrete bending joints, QuadSoft utilizes a continuum deformation approach to modulate arm curvature, actively adjusting its thrust vector and aerodynamic characteristics. We characterize the geometric mapping between servomotor input and the resulting constant curvature, validating it experimentally. Outdoor flight tests demonstrate stable take-off, hover, directional maneuvers, and landing, confirming that controlled arm bending can generate horizontal displacement while preserving altitude. Measurements of pitch, roll, and curvature angles show that the platform follows intended actuation patterns with minimal attitude deviations. These results demonstrate that QuadSoft preserves the baseline stability of rigid quadrotors while enabling morphology-driven maneuverability, all under the standard PX4 autopilot without retuning.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Beyond a proof of concept, this work establishes a distinctive outdoor validation of a tendon-driven continuum morphing quadrotor, opening a new research avenue toward adaptive aerial systems that combine the safety and versatility of soft robotics with the performance of conventional UAVs.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Quadrotors are widely used in aerial robotics for their simplicity and agility, yet rigid-frame designs limit adaptability in cluttered or dynamic environments. To address this, we propose QuadSoft, a novel platform with tendon-driven flexible arms that can reconfigure in flight through continuous-curvature deformation. Unlike conventional morphing designs that rely on rigid hinges or discrete joints, QuadSoft leverages soft morphology to achieve thrust vectoring while maintaining structural integrity. This capability enables navigation in tight spaces, improved aerodynamic efficiency, and enhanced stability. By combining a continuum mechanics approach with standard flight control, QuadSoft bridges the gap between compliant robotics and the need for versatile, resilient aerial platforms capable of operating in real-world conditions.

<!-- chunk {"id": "body-0005", "role": "body", "section": "I-A State of the Art", "weight": 1.0} -->

Quadrotors have become central in aerial robotics for their efficiency, stability, and simplicity, yet their rigid-frame architectures inherently limit adaptability in cluttered or dynamic environments \[31, 1, 4, 28 with appendage repurposing for locomotion plasticity enhancement")\]. Soft robotics has shown that flexible, biologically inspired structures can enhance versatility and safety across manipulators and ground robots, with pneumatic, tendon-driven, and smart-material actuators enabling precise shape control and compliance \[12, 17, 32: a review"), 14, 16\]. However, the application of these principles to aerial vehicles remains limited, with only partial solutions addressing flexibility through distributed-parameter modeling and delay-resistant adaptive control.

<!-- chunk {"id": "body-0006", "role": "body", "section": "I-A State of the Art", "weight": 1.0} -->

Existing morphing quadrotors each fall short in different ways. Impact-resilient designs like Morphy prioritize crash recovery over active reconfiguration. Dual-axis tilting-rotor mechanisms achieve 6-DOF control but at the cost of mechanical complexity and additional failure points. Hybrid platforms such as SMORS combine rigid arms with soft components yet offer only partial deformation. Tendon-driven platforms like those presented in and employ discrete hinge-like bending points and typically require hexarotor configurations to compensate for their limited DOF. In these systems, the tendon actuation is primarily intended for surface grasping rather than for improving maneuverability or flight control. Beyond quadrotors, morphing-wing UAVs and inflatable structures like SFAR target aerodynamic performance and safety, respectively, rather than active in-flight morphological reconfiguration.

<!-- chunk {"id": "body-0007", "role": "body", "section": "I-A State of the Art", "weight": 1.0} -->

In contrast, QuadSoft adopts a constant-curvature continuum approach in a standard X-quadrotor, achieving full 6-DOF actuation with four rotors---without rigid tilting joints, extra propulsion units, or specialized flight control hardware. Notably, the design is validated on a standard, unmodified PX4 autopilot, as detailed in the following section.

<!-- chunk {"id": "body-0008", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

Building on earlier theoretical work on constant-curvature soft aerial vehicles, this paper focuses on the design, construction, and real-world experimental validation of QuadSoft.

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

Continuum Design and Construction: A tendon-driven soft arm based on a constant-curvature approach, enabling smooth in-flight reconfiguration within a standard X-quadrotor configuration---without discrete joints or rigid hinges.

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

Geometric Mapping: A closed-form mapping from servomotor input to arm curvature is derived and experimentally validated, linking tendon actuation to 6-DOF thrust-vectoring capability.

<!-- chunk {"id": "body-0011", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

Outdoor Flight Validation: First outdoor flight tests of a continuum-morphing quadrotor, demonstrating stable hover and morphology-driven translation using a standard, unmodified PX4 autopilot.

<!-- chunk {"id": "body-0012", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

Baseline for Control Allocation: Physical stability validated up to 22^∘^ of curvature (within a 35^∘^ design envelope), providing a foundation for future custom mixer development in fully actuated soft UAVs.

<!-- chunk {"id": "body-0013", "role": "body", "section": "I-C Organization", "weight": 1.0} -->

The remainder of this paper is organized as follows. Section II formulates the central challenge of designing the QuadSoft with tendon-driven soft arms. The geometric mapping from servomotor input to arm curvature and propeller orientation is derived in Section III. Section IV describes the mechanical and electronic implementation of the proposed design. Section V presents the outdoor experimental validation, focusing on hover stability and morphology-induced translation. Finally, Section VI concludes the paper and outlines future research directions.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Designing a morphing quadrotor with soft actuated arms introduces a central challenge: enabling in-flight reconfiguration without compromising flight stability. The inherent flexibility of soft structures allows morphological adaptation but also induces deformations and vibrations that can degrade control performance. Furthermore, maintaining a lightweight structure is critical, as additional mass increases the required lift forces, which in turn amplify structural deformations.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Subproblem A --- Mechanical Design: Developing a lightweight, tendon-driven arm mechanism that balances compliance with structural stability to minimize oscillations while allowing sufficient curvature for reconfiguration.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Subproblem B --- Integration and Modeling: Deriving the actuator--curvature--propeller mapping to ensure that morphological changes translate into predictable and controllable motions while preserving baseline stability.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

The solution to Subproblem A is detailed in Section IV, while Subproblem B is addressed in Section III and subsequently validated through the outdoor experiments presented in Section V.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Geometric Mapping of Servomotor to Arm Curvature", "weight": 1.0} -->

The angular position of the propellers with respect to the main body frame can be expressed as a function of the servomotor angle. This relationship arises from the geometric constraints imposed by the tendon-driven arm. Fig. 2 illustrates the relevant variables: $L_{a}$, the fixed arc length determined by the semi-rigid core, and $L_{b}$, the variable length defined by the tendon pulled by the servomotor. Since the total tendon length remains constant (highlighted in purple in Fig.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Geometric Mapping of Servomotor to Arm Curvature", "weight": 1.0} -->

where $r$ is the radius of the tendon trajectory, $\alpha$ is the servomotor angle, and $K$ is a proportionality constant that accounts for unmodeled effects.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Geometric Mapping of Servomotor to Arm Curvature", "weight": 1.0} -->

where $R$ is the nominal radius of the rigid arc, $R - L_{1}$ corresponds to the effective radius when the tendon is pulled, and $\beta$ is the arm curvature angle. Since $\beta$ is identical in both cases,

<!-- chunk {"id": "body-0021", "role": "body", "section": "Geometric Mapping of Servomotor to Arm Curvature", "weight": 1.0} -->

Together, these expressions provide a complete geometric mapping from servomotor input $\alpha$ to arm curvature $\beta$, and thus to the propellers' angular orientation relative to the body frame.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Geometric Mapping of Servomotor to Arm Curvature", "weight": 1.0} -->

where the coefficients $(a_{i},b_{i},c_{i},d_{i})$ are obtained via data fitting for each arm.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Geometric Mapping of Servomotor to Arm Curvature", "weight": 1.0} -->

Fig. 3(c) illustrates this mapping, showing the experimental $\alpha$--$\beta$ curve along with the operational limits beyond which vehicle lift would be compromised.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-A Structural Design and Stiffness", "weight": 1.0} -->

The soft arm features a hybrid structure---a flat carbon fiber core embedded in a TPU matrix with internal air cavities---designed for anisotropic stiffness. This planar core provides high compliance for vertical bending while remaining exceptionally stiff in torsion, preventing unwanted yaw-axis twisting. Furthermore, the TPU and air chambers act as a vibration damper, dampening high-frequency motor vibrations to preserve baseline flight stability. The platform's mass distribution is detailed in Table II.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-B Actuation Mechanism", "weight": 1.0} -->

Active reconfiguration relies on two antagonistic nylon tendons connecting a base servomotor to a tip pulley (Fig. 3b). Adjusting tendon tension induces continuous positive or negative bending (Fig. 3e). The arm design has a physical bending limit of 28^∘^, since propeller efficiency decreases beyond 25^∘^. This limit is set by the gap between the arm segments, which prevents exceeding the allowable curvature and avoids propeller-arm collisions. By physically constraining the maximum bending angle, the design also mitigates material fatigue. Moreover, adjusting the segment spacing during manufacturing provides a simple parametric means to tune arm compliance. Arm specifications are listed in Table I.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-B Actuation Mechanism", "weight": 1.0} -->

Tensile strength (MPa)
Flexural modulus (MPa)

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-C Electronics Integration", "weight": 1.0} -->

The electronic architecture is deliberately designed to demonstrate that complex soft-morphing can be managed by standard, off-the-shelf avionics. The core of the system is a Pixhawk^®^ V5+ autopilot running an unmodified PX4 flight stack.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-C Electronics Integration", "weight": 1.0} -->

Power is supplied by a 12V 3S LiPo battery via a Power Distribution Board (PDB). The Pixhawk simultaneously manages baseline flight stabilization---commanding the brushless motors via standard ESCs---while synchronizing the servomotors responsible for tendon actuation. To prevent voltage drops during high-torque reconfigurations, a dedicated UBEC regulates a consistent 5V supply to the servomotors.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-C Electronics Integration", "weight": 1.0} -->

Standard RC telemetry is utilized for wireless manual input and real-time monitoring. Ultimately, this integrated setup (detailed in Fig. 4) ensures reliable propulsion and precise tendon actuation, validating that morphology-driven maneuverability in soft UAVs does not necessitate custom hardware ecosystems.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experiments", "weight": 1.0} -->

To evaluate the QuadSoft platform under realistic, unconstrained conditions, we conducted outdoor flight tests subjected to stochastic wind disturbances. Unlike indoor trials that rely on high-precision Motion Capture (MoCap) systems, these outdoor experiments demonstrate the system's operational autonomy using only on-board sensing (IMU/GPS) and a standard, unmodified PX4 control stack.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments", "weight": 1.0} -->

Baseline Hover Stability: The platform's ability to reject external perturbations and maintain stable setpoints despite the inherent compliance of the soft arms.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiments", "weight": 1.0} -->

Morphology-Induced Translation: The dynamic response of the vehicle when continuous-curvature arm bending is actively used to generate horizontal displacement without altering the vehicle's global pitch/roll attitude.

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-A Hover Stability", "weight": 1.0} -->

We first evaluated the QuadSoft's ability to maintain stable hovering in a zero-curvature configuration. The sequence consisted of a take-off to 4 m, a 15 s hover in HOLD mode, and a manual landing under outdoor conditions with light wind gusts.

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-A Hover Stability", "weight": 1.0} -->

Fig. 5(a) shows the 3D trajectory, demonstrating that the actual path closely follows the setpoints with negligible lateral drift. Fig. 5(b) presents the corresponding position and velocity profiles. The controller maintains near-zero steady-state error during the hover phase and recovers seamlessly after mode transitions.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-A Hover Stability", "weight": 1.0} -->

Crucially, high-speed footage and telemetry confirmed that passive arm deflections at full hovering thrust remained below $1^{\circ}$. This validates the efficacy of the anisotropic structural design (Section IV-A), proving that the requisite flexibility for tendon actuation does not introduce unmodeled aeroelastic oscillations or degrade the baseline stability expected from a rigid quadrotor.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-B Morphology-Induced Translation", "weight": 1.0} -->

The core validation of our continuum approach involved generating horizontal displacement purely through tendon-driven arm actuation. Tests were performed in ALTITUDE HOLD mode, isolating horizontal thrust-vectoring from $z$-axis altitude control.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-B Morphology-Induced Translation", "weight": 1.0} -->

(c) Arm curvatures and pitch/roll angles

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-B Morphology-Induced Translation", "weight": 1.0} -->

As illustrated in Fig. 6(a) and (b), upon tendon activation, the vehicle achieved smooth $x$--$y$ translation while strictly maintaining its target altitude. A gradual velocity increase coincided precisely with the onset of arm curvature.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-B Morphology-Induced Translation", "weight": 1.0} -->

Fig. 6(c) presents the transient response during reconfiguration, detailing the measured arm curvatures ($\beta_{i}$) alongside the vehicle's attitude ($\phi$, $\theta$). As the arms actively bend to induce forward motion, the global pitch and roll remain remarkably stable, staying within a $\pm 5^{\circ}$ envelope. The brief excursions up to $10^{\circ}$ correlate with corrective actions against wind gusts rather than actuation-induced instability.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-B Morphology-Induced Translation", "weight": 1.0} -->

Most importantly, the data demonstrates that during the dynamic transition phase (from $0^{\circ}$ to the validated $22^{\circ}$ curvature), the change in the vehicle's thrust vector is smoothly compensated by the native PX4 rate controllers. This confirms that the structural damping of the soft arms prevents resonance modes, allowing morphology-driven directional motion with minimal attitude deviations. Ultimately, these unconstrained outdoor trials establish a robust physical baseline, proving the viability of tendon-driven continuum morphing for adaptive aerial systems.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The experimental evaluation of the QuadSoft platform leads to several critical conclusions regarding the viability and control of soft aerial vehicles.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conclusion", "weight": 1.5} -->

First, the outdoor flight data demonstrates that the inherent vulnerabilities of soft structures---namely, aeroelastic vibrations and uncontrolled deformations---can be successfully mitigated through anisotropic structural design. Because the vehicle maintained stable hovering and its global attitude deviations remained within $\pm 5^{\circ}$ during dynamic reconfiguration, we conclude that the TPU-carbon hybrid arms act as an effective vibration damper.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Second, the successful morphology-induced translation confirms that a constant-curvature continuum approach is a highly effective mechanism for thrust vectoring. By generating forward and lateral displacements while maintaining a near-level pitch and roll, the results establish that tendon-actuated soft arms can practically decouple a vehicle's position from its orientation.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Finally, achieving these stable transitions under stochastic wind disturbances using a standard, unmodified PX4 autopilot leads to a fundamental conclusion: morphological compliance can be seamlessly integrated into existing flight stacks as a physical asset rather than a control disturbance. Ultimately, this work provides a validated physical baseline for fully actuated soft UAVs. Based on these findings, future research will focus on developing custom control allocation matrices (mixers) within the open-source PX4 ecosystem to fully exploit the platform's 6-DOF maneuverability.
