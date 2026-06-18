<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Internal Feedback in the Cortical Perception-action Loop Enables Fast and Accurate Behavior

Topics include State estimation, Attention mechanisms, Control.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Animals move smoothly and reliably in unpredictable environments. Models of sensorimotor control have assumed that sensory information from the environment leads to actions, which then act back on the environment, creating a single, unidirectional perception-action loop. This loop contains internal delays in sensory and motor pathways, which can lead to unstable control. We show here that these delays can be compensated by internal feedback signals that flow backwards, from motor towards sensory areas. Internal feedback is ubiquitous in neural sensorimotor systems and recent advances in control theory show how internal feedback compensates internal delays. This is accomplished by filtering out self-generated and other predictable changes in early sensory areas so that unpredicted, actionable information can be rapidly transmitted toward action by the fastest components. For example, fast, giant neurons are necessarily less accurate than smaller neurons, but they are crucial for fast and accurate behavior. We use a mathematically tractable control model to show that internal feedback has an indispensable role in achieving state estimation, localization of function - how different parts of cortex control different parts of the body - and attention, all of which are crucial for effective sensorimotor control.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This control model can explain anatomical, physiological and behavioral observations, including motor signals in visual cortex, heterogeneous kinetics of sensory receptors and the presence of giant Betz cells in motor cortex, Meynert cells in visual cortex and giant von Economo cells in the prefrontal cortex of humans as well as internal feedback patterns and unexplained heterogeneity in other neural systems.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Abstract", "weight": 1.5} -->

Animals move smoothly and reliably in unpredictable environments. Models of sensorimotor control have assumed that sensory information from the environment leads to actions, which then act back on the environment, creating a single, unidirectional perception-action loop. This loop contains internal delays in sensory and motor pathways, which can lead to unstable control. We show here that these delays can be compensated by internal feedback signals that flow backwards, from motor towards sensory areas. Internal feedback is ubiquitous in neural sensorimotor systems and recent advances in control theory show how internal feedback compensates internal delays. This is accomplished by filtering out self-generated and other predictable changes in early sensory areas so that unpredicted, actionable information can be rapidly transmitted toward action by the fastest components. For example, fast, giant neurons are necessarily less accurate than smaller neurons, but they are crucial for fast and accurate behavior. We use a mathematically tractable control model to show that internal feedback has an indispensable role in achieving state estimation, localization of function -- how different parts of cortex control different parts of the body -- and attention, all of which are crucial for effective sensorimotor control.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Abstract", "weight": 1.5} -->

This control model can explain anatomical, physiological and behavioral observations, including motor signals in visual cortex, heterogeneous kinetics of sensory receptors and the presence of giant Betz cells in motor cortex, Meynert cells in visual cortex and giant von Economo cells in the prefrontal cortex of humans as well as internal feedback patterns and unexplained heterogeneity in other neural systems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "keywords", "weight": 1.0} -->

internal feedback $|$ sensorimotor control $|$ speed-accuracy trade-off $|$ optimal control

<!-- chunk {"id": "body-0007", "role": "body", "section": "doi", "weight": 1.0} -->

[www.pnas.org/cgi/doi/10.1073/pnas.XXXXXXXXXX](www.pnas.org/cgi/doi/10.1073/pnas.XXXXXXXXXX)

<!-- chunk {"id": "body-0008", "role": "body", "section": "doi", "weight": 1.0} -->

Feedback control is an essential strategy for both engineered and biological systems to achieve reliable movements in unpredictable environments. Optimal and robust control theory, which provide a general mathematical foundation to study feedback systems, have been used successfully to explain behavioral observations by modeling the sensorimotor system as a single control loop called the perception-action cycle. In these models, the sensorimotor system senses the environment, communicates signals from sensors to the brain, computes actions, and then acts on the environment, feeding back to the sensors and forming a single unidirectional loop as shown in Fig. 1.

<!-- chunk {"id": "body-0009", "role": "body", "section": "doi", "weight": 1.0} -->

Consider the canonical model of localized function in the primate visuomotor cortical pathway, depicted in Fig. 2: A visual signal is encoded on the retina, then travels to the lateral geniculate nucleus (LGN) of the thalamus, and on to the primary visual cortex (V1), progressing through successive transformations until it reaches the primary motor cortex (M1), the spinal cord, and ultimately the muscles. The single-loop feedback model also makes implicit assumptions about the interpretation of responses from sensory and motor populations of neurons, which represent sensory signals and action signals, respectively. Although intuitive, this model neglects a well-known and ubiquitous feature of sensorimotor processing: internal feedback, which is the main focus of this paper.

<!-- chunk {"id": "body-0010", "role": "body", "section": "doi", "weight": 1.0} -->

The perception-action control model does not have a direct role for internal feedback connections. Internal feedback includes all signals that do not flow from sensing towards action. We can divide internal feedback into two broad categories: counterdirectional between brain areas and lateral interactions within or between areas. Counterdirectional internal feedback is in the opposite direction of the single-loop model (for instance, from V2 to V1); these signals flow from action toward sensing. Lateral internal feedback consists of recurrent connections within and between areas (for instance, from V2 to V2, or from MT to IT). This distinction emphasizes the importance of where control signals are spatially located.

<!-- chunk {"id": "body-0011", "role": "body", "section": "doi", "weight": 1.0} -->

One reason that the single-loop model has endured is that it offers a set of tools from control theory and a conceptual framework that allows subsystems to be treated in isolation. However, these subsystems are not isolated, and with internal feedback each subsystem has access to both bottom up and top down information. The eye is itself a site of computation and control: as the eye moves and senses different parts of the visual scene, lateral interactions within the retina control spatial and temporal filter properties that can adapt and identify important features under a wide range of illumination and scene dynamics. Retinal ganglion cells project to relay neurons in the LGN, which then project to primary visual cortex, V1, but a much greater number of feedback neurons project back from V1 to LGN.

<!-- chunk {"id": "body-0012", "role": "body", "section": "doi", "weight": 1.0} -->

Projections from motor areas in cortex to visual areas have a wide range of morphology, myelination and synapse kinetics. Given the position of M1 in the final common pathway, one might expect activity in M1 to be driven by current visual stimuli or current movements, but instead autonomous or top-down preparatory activity with internal rotational dynamics dominate the data. Counterintuitively, signals related to movements of the whole body are found in areas typically associated with particular parts of the body, such as the hand area, as well as sensory areas such as primary visual cortex. Indeed, recent analysis of the correlation structure between neurons during a visual discrimination task revealed a task-related global mode in the correlations between cortical neurons associated with the task response rather than the sensory stimulus, strongly supporting the idea that top-down feedback is an important element of sensory processing. Although not typically studied together, all of these sensory and motor signals are generated by internal feedback and are the focus of this study.

<!-- chunk {"id": "body-0013", "role": "body", "section": "doi", "weight": 1.0} -->

Internal feedback has been studied in the context of predictive coding and are invoked in other models. However, these models focus on sensory or motor systems separately and do not account for key constraints on neuronal communication in both space and time to achieve sensorimotor tasks. Achieving fast and accurate computation and communication over large distances is difficult and often impossible because communication may be slow, limited in bandwidth and constrained to spatially localized populations.

<!-- chunk {"id": "body-0014", "role": "body", "section": "doi", "weight": 1.0} -->

Here, we build on the foundations of recent work in distributed control theory and show that internal feedback is a solution to achieving rapid and accurate control given the spatial and temporal constraints on brain components and communication systems. We analyze an idealized class of control models and prove mathematically that internal feedback is both plausible and necessary for achieving optimal performance. Internal feedback serves at least three functions in our model: state estimation, localization of function and focused attention, all of which are crucial for effective sensorimotor control and survival. This theory explains why there are differences in population responses between M1 and V1, why different projections predominately activate AMPA or NMDA glutamate receptors, the functions of giant pyramidal cells in visuomotor control, and both the uses and limitations of localization of function in cortex. There is a general principle behind all of these physiological properties.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Task model and performance", "weight": 1.0} -->

We analyze expected values and theoretical bounds on task performance for models of a simple, well-studied and ethologically relevant tracking task, consisting of reaching for and grasping a moving object. The goal of the task is continuous pursuit, rather than one-time contact between limb and object.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Task model and performance", "weight": 1.0} -->

The complete tracking task requires identification of the object in a cluttered visual scene, prediction of the object's movement, and generation and execution of bimanual limb movement. We make simplifying assumptions that are not essential to our conclusions, but allow us to study internal feedback in an accessible way using familiar linear dynamical systems.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Single-loop feedback control", "weight": 1.0} -->

Consider the task of tracking a moving object with the endpoint of a limb on a plane. The variable to be controlled is the tracking error -- the distance between the hand and the object. We start by assuming that the system controlling the limb can perfectly sense the position of limb and object at every instant, which will be relaxed in later models. The cost is defined as the Euclidean norm of the tracking error over time, with smaller cost indicating better tracking.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Single-loop feedback control", "weight": 1.0} -->

Let $x$, $u$, and $w$ represent the tracking error, the control action on the limb, and the action of the object, respectively. We will refer to $x$ as the state of the system. Let $A$ be a matrix that represents the intrinsic dynamics of $x$ -- including the mechanical coupling between two dimensions of limb movement.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Single-loop feedback control", "weight": 1.0} -->

Let $\alpha$ denote the magnitude of the maximum eigenvalue of $A$, as a proxy for task difficulty. Note that $\alpha < 1$ corresponds to a task in which tracking error $x$ will decrease with no limb action, an easy task.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Single-loop feedback control", "weight": 1.0} -->

The optimal solution to this problem is the linear quadratic regulator (LQR) and the optimal controller is ${\mathbf{K}}{(x{(1:t)})} = - Ax{(t)}$. This controller fits into the single-loop model of sensorimotor control, as there is no internal feedback, and the addition of internal feedback does not provide any additional performance advantage.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Single-loop feedback control", "weight": 1.0} -->

Controllers without internal feedback are optimal for a large but special class of problems, including classical state feedback and full control problems from control theory. Though mathematically elegant, these problems make assumptions that are impractical when applied to biological systems. In subsequent sections, we relax some of the assumptions implicit in this single-loop model and show that small deviations from assumptions relevant to biological systems give rise to the necessity of introducing internal feedback from which advantages accrue.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Single-loop feedback control", "weight": 1.0} -->

Any of the controllers in subsequent sections can be implemented in a variety of ways, though whether or not a particular controller needs internal feedback is generic across all possible implementations. In order to study internal feedback, we choose particular non-unique controller implementations which, when optimized, attain the optimal performance over the relevant class of controllers. We choose implementations for which the optimal solution is relatively transparent and easy to interpret.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Internal feedback facilitates implicit estimation in the presence of sensor delays", "weight": 1.0} -->

Simple modifications to the control problem described above lead to an optimal controller $K$ whose implementation requires internal feedback. One such modification is the introduction of sensor delays, which are ubiquitous in biological systems (for instance, the neuronal conduction time from the eye to motor cortex, on the order of tens or hundreds of milliseconds). Sensor delays can be modeled by introducing a virtual internal state $x_{s}$, which represents the adjusted tracking error from the previous time step.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Internal feedback facilitates implicit estimation in the presence of sensor delays", "weight": 1.0} -->

where the virtual internal state $x_{s}$ contains delayed information about the tracking error. Controller $K$ can be partitioned into two block-matrices, ($K = \begin{bmatrix}
\end{bmatrix}^{\top}$). The resulting system is shown in Fig. 3. Here, the controller does not directly \"perceive\" the tracking error $x$ and only has access to the virtual internal state $x_{s}$. However, the controller can freely take actions that affect both the tracking error and the virtual state. The action on the virtual state, as shown in Fig. 3, is an example of counterdirectional internal feedback with gain $K_{2}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Internal feedback facilitates implicit estimation in the presence of sensor delays", "weight": 1.0} -->

For the delayed sensing problem, the optimal controller has a simple analytical form: $K_{1} = {- A^{2}}$ and $K_{2} = {- A}$ is the internal feedback. If no internal feedback is allowed (i.e. we enforce $K_{2} = 0$), then the optimal controller is $K_{1} = {- {A^{2}/4}}$. We compare the performance of these two controllers in Fig. 4, and see that the controller with internal feedback far outperforms the controller without internal feedback. We also note that as the task becomes more difficult, the controller without internal feedback is unable to stabilize the closed-loop system and tracking breaks down.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Internal feedback facilitates implicit estimation in the presence of sensor delays", "weight": 1.0} -->

For a controller with sensory delays, internal feedback is required for optimal performance. This also applies to controllers with actuator delays. In both cases, internal feedback adjusts delayed signals to compensate for actions taken and information received during the delay; in other words, internal feedback implicitly compensates for the delays.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Intrinsic internal feedback in the Kalman filter", "weight": 1.0} -->

We now consider the case in which sensing is instantaneous, but imperfect.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Intrinsic internal feedback in the Kalman filter", "weight": 1.0} -->

where $y$ is the sensor input. Matrix $B$ represents the effect of action $u$ on tracking error $x$, and matrix $C$ represents how sensor input $y$ is related to tracking error $x$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Intrinsic internal feedback in the Kalman filter", "weight": 1.0} -->

where $\hat{x}$ is an internal estimate of tracking error $x$. This optimal controller uses the Kalman filter, which inherently contains three counterdirectional internal feedback pathways irrespective of delays being present. These pathways are represented by the blue arrows through in Fig. 5, and play a central role in state estimation. The pathway through $A$ estimates state evolution in the absence of noise and actuation; the pathway through $B$ accounts for controller action, and the pathway through $C$ predicts incoming sensory signals based on the internal estimated state.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Sources of internal feedback are preserved in a Kalman filter with delays", "weight": 1.0} -->

We now create a model that combines features from previous sections: sensor delays, actuator delays, and imperfect sensing.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Sources of internal feedback are preserved in a Kalman filter with delays", "weight": 1.0} -->

where $x_{a}$ and $x_{s}$ are virtual internal states corresponding to delayed actuator commands and delayed sensor signals, respectively, and $u_{s}$ represents compensation on virtual internal states. We can use standard control theory to obtain the optimal controller gain $K$ and optimal estimator gain $L$. Due to the block-matrix structure of the system matrices, the optimal gains have the following structure: $K = \begin{bmatrix}
\end{bmatrix}$, and $L = \begin{bmatrix}
\end{bmatrix}^{\top}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Sources of internal feedback are preserved in a Kalman filter with delays", "weight": 1.0} -->

Here, $\delta$ is the delayed difference between the estimated sensor input and true sensor input, discounted by the observer term $L_{2}\delta{(t)}$. The resulting controller, shown in Fig. 6, contains two internal feedback pathways related to delay; one pathway compensates for sensor delays, and the other compensates for actuator delays. The remaining internal feedback is inherent to the Kalman Filter, as described in the previous section and shown in Fig. 5. Overall, the inclusion of sensor delays, actuator delays, and imperfect sensing result in an optimal controller with several internal feedback pathways, each of which serves a specific, interpretable purpose.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Localization of function requires lateral internal feedback", "weight": 1.0} -->

Neuron-to-neuron computation and communication are typically spatially and temporally constrained for signals between areas, compared with signals within a local area. Although lateral feedback within each area may conform to the single-loop model, lateral feedback between areas are unexplained by the single-loop model, and are needed to to achieve good performance.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Localization of function requires lateral internal feedback", "weight": 1.0} -->

Localization of communication naturally leads to the localization of function in cortex; sensory and motor areas are spatially localized (with some cross-talk), as are different motor areas. We start with motor areas and the problem formulation described, and partition tracking errors into two sets $x_{1}$ and $x_{2}$, representing two distinct but possibly coupled subsystems (e.g. two distinct limbs that are mechanically coupled). The overall tracking error is $x = \begin{bmatrix}
\end{bmatrix}^{\top}$. Correspondingly, we partition actuators into two sets $u_{1}$ and $u_{2}$ that act on their respective subsystems, via local controllers; $u = \begin{bmatrix}
\end{bmatrix}^{\top}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Localization of function requires lateral internal feedback", "weight": 1.0} -->

Each local controller senses and controls one subsystem; i.e. local controller 1 senses $x_{1}$ and computes $u_{1}$, and local controller 2 senses $x_{2}$ and computes $u_{2}$. Local controllers may communicate to one another; however, due to localization constraints, the cross-communication is delayed. Thus, local controller 1 cannot directly access $x_{2}$ without some delay, and similarly for local controller 2.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Localization of function requires lateral internal feedback", "weight": 1.0} -->

We first remark that without the constraint of localized communication, the optimal controller for Eq. is $u = {- {Ax}}$. If $A$ is block-diagonal (i.e. $x_{1}$ and $x_{2}$ are uncoupled), then this controller obeys localized communication constraints; in fact, no cross-communication (internal feedback) is required between the two local controllers. However, if the two subsystems are coupled with time delays, then this controller requires rapid, global communication, which violate localized communication constraints. To enforce localized communication, we reformulate the problem by introducing virtual states $x_{1}^{\prime}$ and $x_{2}^{\prime}$, which represent delayed cross-communication between the two local controllers. $x_{1}^{\prime}$ is information sent from local controller 1 to local controller 2, with delay; and similarly for $x_{2}^{\prime}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Localization of function requires lateral internal feedback", "weight": 1.0} -->

We also define $u_{1}^{\prime}$ and $u_{2}^{\prime}$, which model interconnections between virtual states and real tracking errors. For simplicity, we assume unit delay.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Localization of function requires lateral internal feedback", "weight": 1.0} -->

The zeros in the top right and bottom left corners of the $K$ matrix preserve localized communication; they enforce that the two local controllers cannot communicate instantaneously to one another. Asterisks and triangles indicate free values; triangles represent sites of potential cross communication, or lateral internal feedback.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Localization of function requires lateral internal feedback", "weight": 1.0} -->

The resulting local controllers are shown in Fig. 7. Note that the $- A_{12}$ term in the second row and the $- A_{21}$ term in the fourth row of $K$ correspond to lateral internal feedback. Here, these internal feedback signals carry predicted values of the unsensed tracking errors for each controller, after taking control action into account; for instance, internal feedback from local controller 2 to local controller 1 conveys the predicted value of $x_{2}$, after taking control action from controller 2 into account.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Localization of function requires lateral internal feedback", "weight": 1.0} -->

We compare the performance of this controller to the controller without internal feedback in Fig. 8. For the controller without internal feedback, we choose the best possible linear controller; however, the lack of internal feedback results in severe performance degradation. As task difficulty increases, this controller is unable to stabilize the closed-loop system and tracking becomes infeasible. With internal feedback, task performance stays near the centralized optimal (i.e. the case where local controllers can communicate freely without delay).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Localization of function requires lateral internal feedback", "weight": 1.0} -->

The foregoing analysis shows that localization of motor function (i.e. specialization of parts of motor cortex to particular parts of the body) in fact requires cross-communication, or internal feedback, between local controllers. Local circuits in the two hemispheres must also be coordinated -- indeed, they are connected by a massive corpus collosum that crosses the midline. The cross talk between local controllers is supported by the presence of signals relating to the whole body in parts of the motor cortex specialized to particular parts of the body. Internal feedback enables localization of function when subsystems are coupled; in reality, all body movements are mechanically coupled, something which the motor system can conceal through effective localization and coordination.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Speed-accuracy trade-offs necessitate the use of layering and internal feedback for attention", "weight": 1.0} -->

We have shown that state estimation and localization of function require internal feedback to correct for self-generated or predictable movements. We now consider the role of attention in the context of a tracking task. Our model can be considered an implementation by internal feedback of the observation that attention enhances the responses of neurons that selectively respond to an attended stimulus.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Speed-accuracy trade-offs necessitate the use of layering and internal feedback for attention", "weight": 1.0} -->

Up to this point, we have assumed that the controller can directly sense the position of the object (perhaps with some delay). In a real world a scene can have many objects, which makes it more difficult for a sensorimotor system to determine the position of an object in the scene. However, a moving object, once identified, can be discriminated from a static visual scene. This illustrates the distinction between scene-related tasks (such as object identification) and error-related tasks (such as object tracking), which in the visual cortex is accomplished by the ventral and dorsal streams, respectively.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Speed-accuracy trade-offs necessitate the use of layering and internal feedback for attention", "weight": 1.0} -->

This distinction also mirrors the separation between bumps and trails in the mountain-biking task studied, allowing us to build on the control architecture in that task. The main difference is that instead of separating into two control loops, we use layering and internal feedback to supplement the control actions of the main control loop.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Speed-accuracy trade-offs necessitate the use of layering and internal feedback for attention", "weight": 1.0} -->

where $w_{r}$ represents object movement, and $w_{b}$ represents changes in the background scene. Our limb position $p$ is governed by the dynamics

<!-- chunk {"id": "body-0046", "role": "body", "section": "Speed-accuracy trade-offs necessitate the use of layering and internal feedback for attention", "weight": 1.0} -->

where $u{(t)}$ is some limb action. The tracking error $x:={r - p}$ then obeys the dynamics

<!-- chunk {"id": "body-0047", "role": "body", "section": "Speed-accuracy trade-offs necessitate the use of layering and internal feedback for attention", "weight": 1.0} -->

where the task difficulty is implicitly equal to 1.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Speed-accuracy trade-offs necessitate the use of layering and internal feedback for attention", "weight": 1.0} -->

We assume that object movement and background changes are bounded: ${|{w_{r}{(t)}}|} \leq \epsilon_{r}$ and ${|{w_{b}{(t)}}|} \leq \epsilon_{b}$ for all $t$. Additionally, we assume that background changes are much slower than object movement: $\epsilon_{b} \ll \epsilon_{r}$, i.e.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Speed-accuracy trade-offs necessitate the use of layering and internal feedback for attention", "weight": 1.0} -->

Consider a movable sensor that senses some interval of size $\beta$ on the continuous line. Information from the sensor must be communicated to the controller (via axons), but this communication is subject to speed-accuracy trade-offs. Let $R$ be the signaling rate (bits per unit time), let $T$ be the signaling delay, and let $\lambda$ be the resource cost to build and maintain axons. The speed-accuracy trade-off can be formalized as $R = {\lambdaT}$. The signaling rate $R$ is related to the resolution of information sent about the sensed interval.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Speed-accuracy trade-offs necessitate the use of layering and internal feedback for attention", "weight": 1.0} -->

We implement this speed-accuracy trade-off using a static, memoryless quantizer $Q$ with uniform partition, followed by a communication delay, as shown on the top in Fig. 9. This choice of quantizer does not add to the cost, since it recovers the optimal cost over all possible quantizers. The controller can move the sensor around; the interval sensed by the sensor remains constant, but the controller can choose where the interval lies. Assume the initial position of the object is known -- we can select an initial sensor location and $\beta$ appropriately such that $r{(t)}$ always falls within the sensed interval. In this case, the best possible tracking error for any delay $T$ is

<!-- chunk {"id": "body-0051", "role": "body", "section": "Speed-accuracy trade-offs necessitate the use of layering and internal feedback for attention", "weight": 1.0} -->

The first term represents error from delay, object movement, and drift. In the time taken for information to reach the controller, the most adversarial action possible by the object and background would contribute a tracking error of ${({\epsilon_{r} + \epsilon_{b}})}T$; we apply simplification to obtain $\epsilon_{r}T$. The second term represents quantization error. For an interval of size $\beta$ divided into $N$ uniform sub-intervals, the worst-case error is $\frac{\beta}{N}$; we then use the fact that $N = 2^{R} = 2^{\lambdaT}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Speed-accuracy trade-offs necessitate the use of layering and internal feedback for attention", "weight": 1.0} -->

This is achieved by the controller depicted on the top in Fig. 9. The cost, as a function of $T$, is plotted in the left panel Fig. 10 with the label 'No Internal Feedback' (where $T = T_{s}$). Here, the speed-accuracy trade-off is implicit. Very low values of $T$ correspond to very low signaling rates -- the controller does not receive enough information to act accurately, so performance is poor. The opposite problem occurs at very high values of $T$; though the information is high-resolution, the time elapsed between information and action is too long, leading to poor performance. The best performance occurs between these two extremes.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Speed-accuracy trade-offs necessitate the use of layering and internal feedback for attention", "weight": 1.0} -->

We can improve this performance by nearly an order of magnitude by adding an additional communication pathway and the requisite internal feedback. We now have two communication paths from the sensor, each with its own quantizer and delay block. The slower communication path uses quantizer $Q_{s}$ with delay $T_{s}$, while the faster path uses $Q_{f}$ with delay $T_{f}$. To further facilitate speed in the fast path, we allow it to send only a subset of information from the sensor (i.e. only send information about a small part of the sensed scene). Mathematically, let the fast path send information about an interval of size $\beta_{f}$, with $\beta_{f} < \beta$, and let this smaller sub-interval be contained within the sensor interval. This sub-interval is an implementation of attention. The fast path is the main actuation path, while the slower path provides compensatory signals via internal feedback; this is shown on the bottom in Fig. 9. In this case, the best possible cost is

<!-- chunk {"id": "body-0054", "role": "body", "section": "Speed-accuracy trade-offs necessitate the use of layering and internal feedback for attention", "weight": 1.0} -->

The first term represents error from delay and object movement, similar to. The second term represents a combination of quantization error from the fast communication pathway ($\beta_{f}$) and performance error of the slow pathway ($E_{s}$), which informs the fast pathway of where to place the sub-interval. Notice that $E_{s}$ takes the same form as.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Speed-accuracy trade-offs necessitate the use of layering and internal feedback for attention", "weight": 1.0} -->

The cost, as a function of $T_{s}$, is plotted in the left panel of Fig. 10 with the label 'Internal Feedback'. In this plot, we assume $T_{f}$ to be its smallest possible value; one unit of delay. We see that using two quantizers in combination with internal feedback is superior to using one quantizer. We remark that this only holds when the two quantizers are different; if we simply use two quantizers with the same interval, bit rate, and delay, no such performance boost occurs. In general, holding $T_{s}$ constant and decreasing $T_{f}$ improves performance, as shown in the right panel of Fig. 10.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Speed-accuracy trade-offs necessitate the use of layering and internal feedback for attention", "weight": 1.0} -->

Functionally, the inclusion of a faster communication pathway allows action to be taken in a more timely manner than in the single-pathway case. Unlike in the single-pathway case, we are not encumbered by issues of low-resolution information; the slower communication pathway corrects the fast pathway through internal feedback. Here, as in previous examples, the internal feedback carries signals correcting for self-generated and slow, predictable changes. Overall, despite speed-accuracy trade-offs in communication, the system achieves fast and accurate behavior with the help of internal feedback, under reasonable assumptions about the dynamics of the scene and environment.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Discussion", "weight": 1.5} -->

We analyzed a group of basic control models to explore internal feedback in an action-perception loop with time delays and limited communication bandwidth. What emerged was mathematical explanations for previously cryptic features of biological sensorimotor control. We showed how internal feedback is required for state estimation and localization of function, and how it facilitates attention and improved motor performance. This is a first step toward an end-to-end model of sensorimotor processing.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Existing frameworks for internal feedback neglect task performance", "weight": 1.0} -->

There may be other functions for internal feedback in addition to compensating for time delays and limited cortical communication bandwidth. Additional functions that have been suggested are computation through dynamics, deploying recurrent networks, performing Bayesian inference, generating predictive codes, and many others. These frameworks have arisen in parallel with the development of methods for increasingly high-throughput and high-resolution measurements of biological systems, which support the idea that internal feedback and internal dynamics are essential features of cortical computation.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Existing frameworks for internal feedback neglect task performance", "weight": 1.0} -->

These frameworks emphasize prediction but are largely confined to the context of either sensory processing or motor processing separately and do not explicitly model ethological task performance. Our analysis emphasizes motor-based internal feedback signals, which have not been considered in previous frameworks. Recent data showing that motor signals and effects of past and current actions account for substantial cortical activity, previously considered spontaneous, background or noise, are consistent with this view. The ultimate purpose of sensory processing is to support optimal actions for ensuring survival.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Existing frameworks for internal feedback neglect task performance", "weight": 1.0} -->

We propose that internal feedback signals carry information about how actions propagate through the body and its environment, as well as about planned future actions, including how communication limitations affect both plans and actions. Our implementation of control produces performance that is nearly Bayes optimal, illustrating the difference between behavior and implementation introduced earlier. Our emphasis on this motor-centric view of the cortex complements the sensory-centric view that has been explored much more thoroughly to date.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Existing optimal control models neglect physiological limitations", "weight": 1.0} -->

Optimal control theory is a general framework for sensorimotor modeling. Given a mathematical description of a system and some task specification, the optimal controller provably gives the best possible performance. However, these proofs assume that the components are fast and accurate, with communication at the speed of light and control circuits implemented with fast and accurate electronics; with these components, a single sense-compute-actuate loop is generally sufficient to achieve optimal behavior.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Existing optimal control models neglect physiological limitations", "weight": 1.0} -->

To use control theory to model physiological circuitry, a distinction between behavior and implementation must be made. The same behavior (optimal performance) may be achieved through a number of different implementations (underlying circuitry). Although traditional control theory excels as a model of sensorimotor behavior, it does not incorporate the component-level constraints that are prevalent in biology; as a consequence, the implementations of traditional control theory models are not directly relevant to biological control.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Existing optimal control models neglect physiological limitations", "weight": 1.0} -->

Recent advances have extended traditional control theory to allow distributed control and incorporation of component-level constraints. We build on this body of work to describe how constrained components affect the implementation of an optimal distributed biological controller. In particular, we show that internal feedback is a necessary part of any controller whose components exhibit the speed-accuracy trade-offs found in brains.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Existing optimal control models neglect physiological limitations", "weight": 1.0} -->

Fast long-range association fibers in the cortex are metabolically and developmentally expensive, have low bandwidth (compared to counterfactual slower fibers), require constant maintenance and repair and are limited in number. Internal feedback from the motor cortex to earlier sensory areas can regulate the use of these pathways by suppressing self-generated and other predictable signals and using the fast pathways to selectively transmit the unpredicted changes needed by the motor system to make make fast decisions. This virtualizes the behavior of the control system to produce actions that are both fast and accurate despite the internal time delays and limited communication bandwidth.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Biophysical speed-accuracy trade-offs necessitate internal feedback", "weight": 1.0} -->

Biological control systems do not have components that are both fast and accurate. Spiking neurons, though fast relative to other biological signaling mechanisms, are many orders of magnitude slower than electronics and face severe speed-accuracy trade-offs that constrain communication and control. However, by cleverly combining components with different speed-accuracy trade-offs and using internal feedback as demonstrated above, brains are able to perform survival-critical sensorimotor tasks with speed and accuracy.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Biophysical speed-accuracy trade-offs necessitate internal feedback", "weight": 1.0} -->

Neurons have biophysical constraints that lead to speed-accuracy trade-offs; for example, some neurons can rapidly convey a few bits of information, and others can slowly convey many bits of information, but neurons that rapidly convey many bits of information are expensive and correspondingly rare. Speed-accuracy trade-offs include spike averaging versus spike timing and the spatial trade-off between the number of neurons (information rate) and their axonal diameter (conduction speed) in nerve bundles. These trade-offs have consequences for the performance of sensorimotor systems that we can study in our control models.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Biophysical speed-accuracy trade-offs necessitate internal feedback", "weight": 1.0} -->

Brains contain highly diverse populations of neurons; for example, the range of neural conduction speeds in humans spans several orders of magnitude. In sensorimotor systems, these diverse neurons are multiplexed in a task-specific way that approximates the performance of a single-loop system composed of ideal (e.g. fast and accurate) components. The fastest components are used in the feedforward loop, sending information from sensing areas toward motor areas. Internal feedback compensates for accuracy by filtering out slow-changing, predictable, or task-irrelevant stimuli, such that the fewest possible bits need to travel along the fastest possible neurons. From an evolutionary perspective, once a system can achieve fast responses, additional layers of control can be added to achieve more accurate and flexible behavior without sacrificing performance.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Biophysical speed-accuracy trade-offs necessitate internal feedback", "weight": 1.0} -->

The reason why internal feedback is not needed in most engineered control systems is that internal time delays are negligible. But in biological systems, even the fastest neurons used in the feedforward loop give rise to significant time delays. This is why it is essential to include delays in our control-based analyses of the forward loop (Fig. 4).

<!-- chunk {"id": "body-0069", "role": "body", "section": "Fast forward conduction is key to successful sensorimotor task performance", "weight": 1.0} -->

In cortex, the fastest, largest and most striking neurons are the large pyramidal cells: Meynert cells in primary visual cortex carry signals from rapidly moving-object; giant Betz cells in motor cortex that project to the spinal cord are responsible for rapid responses to perturbations from planned movements; and giant Von Economo cells in the prefrontal cortex (anterior cingulate and fronto-insular areas) that project subcortically are involved in the regulation of emotional and cognitive behavior..

<!-- chunk {"id": "body-0070", "role": "body", "section": "Fast forward conduction is key to successful sensorimotor task performance", "weight": 1.0} -->

The visual stream diverges into the dorsal and ventral streams, which are responsible for object motion and object identity, respectively. In natural scenes, object locations may change quickly, but object identities are change relatively slowly; a mouse may move around rapidly, but its status as a prey hunted by a barn owl does not change. Thus, speed is crucial for the dorsal stream, but not the ventral stream.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Fast forward conduction is key to successful sensorimotor task performance", "weight": 1.0} -->

This difference has physiological consequences in our minimal model of attention that could explain differences between cortical projections in the two streams: the giant Meynert Cells that project from V1 to MT (an object motion area in the dorsal stream; see Fig. 1), but there are no equivalently large cells projecting from V1 to inferotemporal cortex (an object identity area in the ventral stream). Reaching tasks could test the predictions of our control model for rapidly and unpredictably moving objects on a fixed background compared with predictably moving objects on nonstationary backgrounds.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Fast forward conduction is key to successful sensorimotor task performance", "weight": 1.0} -->

Neurons in MT respond selectively to the direction of moving objects and provide signals that are used by the oculomotor system for the smooth pursuit of moving objects.There are several visual pathways from the retina to the cortex for tracking moving stimuli. In addition to the cortical pathway that projects from V1 to area MT in Fig. 1, the retina also projects to the pulvinar, another thalamic relay to extrastriate areas of the cortex. These two pathways could implement the optical control model in the bottom panel of Fig. 9, where the fast, direct pathway is from the pulvinar and the delayed, indirect pathway from V1 corresponds to the slower pathway.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Internal feedback facilitates fast feedforward signals in visual cortex", "weight": 1.0} -->

In recent years, large-scale recordings from visual cortex have uncovered non-visual signals that challenge the traditional single-loop view of sensorimotor control. In the traditional view, visuomotor processing consists of a series of successive transformations from stimulus to response, with each cortical area along the way tuned to some aspect of stimulus space. However, although V1 does respond to visual stimuli, the activity of these neurons is dominated by motor-based internal feedback and task/attention-related modulatory internal feedback.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Internal feedback facilitates fast feedforward signals in visual cortex", "weight": 1.0} -->

The number of projections from V1 to V2 is roughly the same as number of neurons, of similar conduction speed, that project from V2 to V1. However, these neurons are very different in morphological and molecular characteristics: The neurons that project feedforward from V1 to V2 primarily activate AMPA receptors, while the feedback neurons that project from V2 to V1 have a strong NMDA receptor component and terminate almost exclusively on excitatory pyramidal neurons. Both of these receptors are activated by glutamate, but AMPA-mediated currents are fast, lasting only a few ms, while NMDA-mediated currents can linger in the postsynaptic neurons for hundreds of ms. This feedback could be relevant for top-down signaling to shape and control perception during actions and could also be important for perceptual learning.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Internal feedback facilitates fast feedforward signals in visual cortex", "weight": 1.0} -->

Pharmacologically blocking NMDA receptors in visual cortex disrupts figure-ground discrimination; that is, a loss in capacity to contextually interpret the visual scene. In the context of our theory and minimal model of attention, internal feedback from V2 informs V1 of predictable elements in future stimuli. Since the visual space cannot be sampled losslessly, these feedback signals could be helping V1 suppress predictable features, making the the unpredictable features more salient.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Internal feedback facilitates localization of function in motor cortex", "weight": 1.0} -->

Primary motor cortex (M1) is dominated by its own past activity rather than static representations. In the context of the state estimation problem we considered in Figure 6, motor cortex is dominated neither by motor representations nor by pattern generation, but by predictions of the consequences of self-action through local internal feedback, which need to be sent throughout the body.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Internal feedback facilitates localization of function in motor cortex", "weight": 1.0} -->

By the same principle, the localization of function within motor cortex that we considered in Figure 8 reconciles the conventional view of homuncular organization, for example, the body-related signals found in putatively hand-related parts of motor cortex, as well as contralateral hand signals. As with motor signals in visual cortex, these broad body movement signals in motor cortex are necessary for identifying predictable consequences of motor signals from other body movements and separating them from unpredictable signals of critical importance for rapidly controlling localized body parts. This provides each body part with the context it needs to compensate for the movement of other body parts.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Learning on internal feedback pathways fine-tunes performance", "weight": 1.0} -->

Internal feedback pathways carry attentional signals that activate slow NMDA receptors, which in turn regulate the strengths of synapses. We have shown that internal feedback pathways are needed for ignoring self-generated and other predictable signals. Early in brain development, activation of NMDA receptors in primary visual cortex before the first visuomotor experience is needed to suppress predictable feedback and the the selection of unpredictable stimuli. Knocking out these NMDA receptors impairs visuomotor skill learning later in life, necessary for compensating for body growth and body weight changes. This form of learning is driven by prediction error. Thus, the same internal feedback system that broadcasts predictions for upcoming actions could drive learning through local prediction error.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Learning on internal feedback pathways fine-tunes performance", "weight": 1.0} -->

Reinforcement learning governed by circuits in the basal ganglia may also benefit from the internal feedback pathways in the cortex. Reinforcement is a scalar signal that does not specify which sensory inputs were responsible for the reward, which in part is why it is a much slower form of learning. Attentional internal feedback in the cortex automatically selects and represents the currently most salient information for motor actions. This information projects to the striatum and makes it easier for the basal ganglia to associate the causally relevant sensory inputs with reward signals.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Learning on internal feedback pathways fine-tunes performance", "weight": 1.0} -->

Attention has been studied primarily in the context of sensory processing. The importance of attentional signals for reducing time delays in making motor decisions adds a new direction for future experimental studies. Attention is linked to conscious awareness and rides atop the global representation of the body throughout the cortex. This makes internal feedback a candidate feature of the nervous system that helps explain the sense of unity that we experience, which would otherwise be difficult to achieve with a balkanized representation of body parts.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Learning on internal feedback pathways fine-tunes performance", "weight": 1.0} -->

Stephen Lisberger helped clarify our discussion on visual pathways to the oculomotor system. J.C.D. and T.J.S. were supported by NSF NCS-FO 1735004. T.J.S. was supported by ONR N00014-16-1-282. J.S.L. was in part supported by NSERC PGSD3-557385-2021. This paper is based on the doctoral research of A.A.S. and J.S.L.
