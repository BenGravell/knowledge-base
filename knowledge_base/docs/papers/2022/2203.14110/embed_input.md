<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Correct-By-Construction Design of Adaptive Cruise Control with Control Barrier Functions under Safety and Regulatory Constraints

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The safety-critical nature of adaptive cruise control (ACC) systems calls for systematic design procedures, e.g., based on formal methods or control barrier functions (CBFs), to provide strong guarantees of safety and performance under all driving conditions. However, existing approaches have mostly focused on fully verified solutions under smooth traffic conditions, with the exception of stop-and-go scenarios. Systematic methods for high-performance ACC design under safety and regulatory constraints like traffic signals are still elusive. A challenge for correct-by-construction approaches based on CBFs stems from the need to capture the constraints imposed by traffic signals, which lead to candidate time-varying CBFs (TV-CBFs) with finite jump discontinuities in bounded time intervals.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The goal of adaptive cruise control (ACC) is to ensure that the vehicle under control, i.e., the *ego* vehicle, tracks the velocity of the leading vehicle while maintaining a safe distance. The safe distance is usually calculated by using a constant-time headway policy, the headway time being the time the ego vehicle takes to cover the distance between itself and the leading vehicle. ACC systems have been extensively studied over the last decade. Predictive cruise control uses time sequence information from upcoming traffic signals to optimize fuel efficiency for vehicle planning. Similarly, ecological ACC aims to avoid traffic signal violations and collisions while generating optimal reference velocity signals to minimize fuel consumption. These optimization-based approaches, however, tend to lack strong guarantees that the ego vehicle is safe and obeys regulatory constraints. More recently, the safety-critical nature of ACC systems has called for formally verified or correct-by-construction approaches using methods from theorem proving, algorithmic control synthesis, and control barrier functions (CBFs) to provide strong guarantees of safety and performance.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

State-of-the-art formal verification and correct-by-construction design methods have been successfully applied in the context of highway systems with smooth traffic conditions. Recently, a provably correct ACC design approach has been proposed to safely handle the occurrence of cut-in vehicles while preserving comfort in a model predictive control (MPC) scheme. However, control synthesis methods that can deal with regulatory constraints like non-smooth traffic signals are still elusive. In this paper, we focus on the synthesis of adaptive cruise controllers under safety and regulatory constraints like traffic signals, a class of systems that we call *regulated ACCs*, using control barrier guarantees.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We model a traffic signal as a function of time, e.g., $s:{{\lbrack 0,\infty)}\rightarrow{\{{\mathtt{G}\mathtt{r}\mathtt{e}\mathtt{e}\mathtt{n}},{\mathtt{Y}\mathtt{e}\mathtt{l}\mathtt{l}\mathtt{o}\mathtt{w}},{\mathtt{R}\mathtt{e}\mathtt{d}}\}}}$, that exhibits finite jump discontinuities within bounded time intervals. Capturing the traffic signal constraints in the form of CBFs leads to time-varying CBFs (TV-CBFs) with jump discontinuities, which makes it difficult to apply standard CBF-based design methods. In fact, non-smooth barrier functions (NBFs) have been investigated for time-invariant CBFs. In the time-varying case, multiple CBFs can be combined via a pointwise minimum operator.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, applying this method to traffic light signals, for example, would require that the vehicle stop at the stop line of every traffic signal, be it green or red, which is overly conservative for practical scenarios, as shown with examples in Section II. We propose, instead, to *represent traffic signals with jump discontinuities via piecewise $m$-times continuously differentiable ($\mathcal{C}^{m}$) TV-CBFs and investigate conditions for the existence of switching-based controllers that render the corresponding safe sets forward-invariant*.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present a control synthesis method for piecewise $m$-times continuously differentiable ($\mathcal{C}^{m}$) TV-CBFs with finite jump discontinuities within bounded time intervals. We prove that the super-level set of such a TV-CBF is forward-invariant under a switching-based controller.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Based on the method above, we design a correct-by-construction regulated ACC, which receives the traffic lights' time sequence and guarantees it will obey these signals while keeping safe spacing with leading vehicles and limiting the velocity of the ego vehicle to a maximum value set by the driver.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We organize the paper as follows. We provide an overview of CBF-based methods in Section II. We then introduce the piecewise $\mathcal{C}^{m}$ TV-CBFs in Section III and formulate the regulated ACC design problem in Section IV. In Section V, a piecewise $\mathcal{C}^{m}$ TV-CBF is constructed for the regulated-ACC problem. In Section VI, the controller is synthesized from the CBF constraints via quadratic programming. Simulation results and conclusions are presented in Section VII and Section VIII, respectively.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Time-Varying Control Barrier Functions", "weight": 1.0} -->

The result in Definition 3. ‣ II Preliminaries ‣ Correct-By-Construction Design of Adaptive Cruise Control with Control Barrier Functions Under Safety and Regulatory Constraints") relates to a time-invariant CBFs. A similar result can, however, be stated for time-varying CBFs. We first recall the notion of relative degree of a CBF, since higher-order CBFs are often required to express many constraints in motion planning.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-B Incorporating Traffic Rules Within CBFs", "weight": 1.0} -->

Let the vehicle approach a traffic signal at $p_{i}$ and suppose that $p_{i - 1} < x \leq p_{i}$ holds, as shown in Fig. 1.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-B Incorporating Traffic Rules Within CBFs", "weight": 1.0} -->

The vehicle should not go beyond the stop line at $p_{i}$ when the $i^{th}$ traffic signal is red. When the $i^{th}$ traffic signal is green or yellow, then the vehicle can cross $p_{i}$. Therefore, when the ego vehicle is between $p_{i - 1}$ and $p_{i}$, the safe set can be expressed as

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-B Incorporating Traffic Rules Within CBFs", "weight": 1.0} -->

suggesting the following candidate CBF

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-B Incorporating Traffic Rules Within CBFs", "weight": 1.0} -->

However, leads to a very conservative design, as it requires that the vehicle stop at the stop line of the upcoming traffic signal, be it $\mathtt{R}\mathtt{e}\mathtt{d}$, $\mathtt{G}\mathtt{r}\mathtt{e}\mathtt{e}\mathtt{n}$ or $\mathtt{Y}\mathtt{e}\mathtt{l}\mathtt{l}\mathtt{o}\mathtt{w}$. In the following, we propose a novel method to overcome this issue by directly dealing with piecewise $C^{m}$ TV-CBFs with finite jump discontinuities in bounded time intervals.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Piecewise $\\mathcal{C}^{m}$ Control Barrier Functions", "weight": 1.0} -->

We first introduce the notion of piecewise $C^{m}$ TV-CBF with finite jump discontinuities in any bounded time interval.

<!-- chunk {"id": "body-0016", "role": "body", "section": "III-A Piecewise $\\mathcal{C}^{1}$ TV-CBF for Traffic Signals", "weight": 1.0} -->

‣ III Piecewise 𝒞^𝑚 Control Barrier Functions ‣ Correct-By-Construction Design of Adaptive Cruise Control with Control Barrier Functions Under Safety and Regulatory Constraints"). However, we can modify ${\mathfrak{h}}{(t,\mathbf{x})}$ so that it becomes a valid piecewise $\mathcal{C}^{m}$ TV-CBF such that, at all discontinuities $t_{j}$, ${{\mathfrak{C}}{(t_{j}^{-})}} \subset {{\mathfrak{C}}{(t_{j})}}$ holds as required by Definition 6. ‣ III Piecewise 𝒞^𝑚 Control Barrier Functions ‣ Correct-By-Construction Design of Adaptive Cruise Control with Control Barrier Functions Under Safety and Regulatory Constraints").

<!-- chunk {"id": "body-0017", "role": "body", "section": "III-A Piecewise $\\mathcal{C}^{1}$ TV-CBF for Traffic Signals", "weight": 1.0} -->

The proposed approach can be extended to the case when the timing sequence of the traffic signals is not known. In particular, if we know the minimum time duration of the yellow light of each traffic signal, we can still achieve safety via a more conservative $h_{it}{(t)}$. Similarly, if the next traffic signal is too far, we can assume that $s_{i} = {\mathtt{R}\mathtt{e}\mathtt{d}}$. Based on this scenario, the regulated ACC can be formulated in the following manner.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Regulated Adaptive Cruise Control", "weight": 1.0} -->

We start by presenting the longitudinal model for the ego vehicle.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-A Longitudinal Dynamics of Vehicle", "weight": 1.0} -->

Let the longitudinal position and longitudinal velocity of the ego vehicle and lead vehicle be denoted by $X_{f}$, $X_{l}$, and $V_{f}$, $V_{l}$ respectively. Let $m$ be the mass of the ego vehicle.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-A Longitudinal Dynamics of Vehicle", "weight": 1.0} -->

where the input $u$ is the force applied by the wheels, $c_{0}$, $c_{1}$, and $c_{2}$ are the vehicle parameters, $h > 0$ is constant time headway and $F_{r}$ denotes the sum of all the frictional and aerodynamic forces on the vehicle. The relative distance and the relative velocity of the ego vehicle and lead vehicle are denoted by $X_{r} = {X_{l} - X_{f}}$ and $V_{r} = {V_{l} - V_{f}}$. The difference between the actual relative distance and the required relative distance is called the spacing error $\delta$ and it is given by $\delta = {X_{r} - {hV_{f}} - S_{0}}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-B Problem Formulation", "weight": 1.0} -->

In ACC systems, the ego vehicle can track the velocity of the lead vehicle by keeping a safe distance. In a regulated ACC, the controller is also subject to regulatory constraints like traffic signals. Specifically, the *regulated* ACC will obey the upcoming traffic signals by utilizing the timing information from them.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-B1 Assumptions", "weight": 1.0} -->

The traffic signals can broadcast the position of the stop line and the timing of the traffic lights to the environment. The ego vehicle knows when and for how long the traffic lights will turn green, yellow, and red.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-B1 Assumptions", "weight": 1.0} -->

The velocities of the vehicles on the road are non-negative.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-B1 Assumptions", "weight": 1.0} -->

The maximum acceleration limits of the lead vehicle and the ego vehicle are known.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-B1 Assumptions", "weight": 1.0} -->

The traffic signals follow the communication protocol below.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-B3 Specifications", "weight": 1.0} -->

The specifications are categorized into hard constraints (HCs) and soft constraints (SCs). The regulated ACC must obey the hard constraints at all times. The soft constraints should, instead, be fulfilled as long as the hard constraints are not violated. The constraints of the problem are given below.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-B3 Specifications", "weight": 1.0} -->

HC-I: The ego vehicle must maintain a relative distance $X_{r} \geq {{hV_{f}} + S_{0}}$ or, equivalently, $\delta \geq 0$ must hold ${\forall t} \geq 0$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-B3 Specifications", "weight": 1.0} -->

HC-III: The ego vehicle must stop at the red signal before the stop line.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-B3 Specifications", "weight": 1.0} -->

SC: The ego vehicle should track the velocity of the lead vehicle $V_{l}$ and $\delta$ should go to $0$ as long as the hard constraints HC-I, HC-II and HC-III are not violated.

<!-- chunk {"id": "body-0030", "role": "body", "section": "IV-B3 Specifications", "weight": 1.0} -->

In the following section, we formulate the CBF for the regulated ACC.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Control Barrier Function For Regulated ACC", "weight": 1.0} -->

The CBFs capturing the hard constraints are formulated below.

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-A Hard Constraints", "weight": 1.0} -->

Let us denote the TV-CBF corresponding to the traffic signals' constraints by $h_{3}{(t,\mathbf{x})}$. Following the encoding in the form of a TV-CBF, we obtain

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-A Hard Constraints", "weight": 1.0} -->

The above candidate TV-CBF has relative degree $2$, hence it is a piecewise $\mathcal{C}^{2}$ function. This function is discontinuous at $t = g_{ij}$, ${\forall j} \in {\mathbb{N}}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-A Hard Constraints", "weight": 1.0} -->

By Theorem 2, we conclude that ${C_{3}{(g_{ij}^{-})}} \subset {C_{3}{(g_{ij})}}$, ${\forall j} \in {\mathbb{N}}$. Therefore, $h_{3}{(t,x)}$ is a valid piecewise $\mathcal{C}^{2}$ TV-CBF. Finally, we fulfill the soft constraints via following nominal controller.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-B Soft Constraints", "weight": 1.0} -->

We design a nominal PID controller such that $\delta\rightarrow 0$ and $V_{f}\rightarrow V_{l}$, as shown below.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-B Soft Constraints", "weight": 1.0} -->

After designing the CBFs, we can synthesize the controller.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Controller Design", "weight": 1.0} -->

The set of safe inputs that renders $C_{3}{(t)}$ forward-invariant is given as

<!-- chunk {"id": "body-0038", "role": "body", "section": "Controller Design", "weight": 1.0} -->

(a) HC-I: h1 (x) ≥ 0. The ego vehicle always maintains the safe distance from the lead vehicle.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Controller Design", "weight": 1.0} -->

(b) HC-II: Vf ≤ Vm a x. The speed profile of the lead vehicle and the ego vehicle in K m/h vs. time (s).

<!-- chunk {"id": "body-0040", "role": "body", "section": "VI-A Control Synthesis Using Quadratic Programming", "weight": 1.0} -->

A nominal controller provides $u_{nom}$ to satisfy the soft constraints $V_{f}\rightarrow V_{l}$, $\delta\rightarrow 0$. If $u_{nom} \in {\mathcal{U}_{safe}{(t)}}$ then the input given by the nominal controller satisfies all the hard constraints. When $u_{nom} \notin {\mathcal{U}_{safe}{(t)}}$ then we solve the following QP problem.

<!-- chunk {"id": "body-0041", "role": "body", "section": "VI-A Control Synthesis Using Quadratic Programming", "weight": 1.0} -->

As ${\mathcal{U}_{safe}{(t)}} \neq \varnothing$, the QP problem is always feasible when $u \in \mathcal{U} = {\mathbb{R}}$. In practice, the input force is constrained to $\mathcal{U} = {\lbrack u_{min},u_{max}\rbrack}$, which could make the QP problem infeasible. Therefore, we modify the CBF so that QP problem remains feasible under the input constraints. We also modify the CBF from relative degree $2$ to relative degree $1$ which is more intuitive and easier to implement.

<!-- chunk {"id": "body-0042", "role": "body", "section": "VI-B Input Constraints", "weight": 1.0} -->

The input force is constrained, i.e., $\mathcal{U} = {\lbrack{- {a_{min}m}},{a_{max}m}\rbrack}$ with $a_{min} > 0$, $a_{max} > 0$. Therefore, we obtain ${{- a_{min}} - \frac{F_{r}}{m}} \leq \mu \leq {a_{max} - \frac{F_{r}}{m}}$. Since $F_{r} \geq 0$, the minimum acceleration available is equal to ${- a_{min}} - \frac{Fr}{m}$, where the first term is the braking acceleration provided by the vehicle and $F_{r}/m$ is the extra braking acceleration provided by the aerodynamic and frictional forces.

<!-- chunk {"id": "body-0043", "role": "body", "section": "VI-B Input Constraints", "weight": 1.0} -->

The stopping distance for the ego vehicle following a lead vehicle $V_{l}$ is given by $\frac{{({V_{l} - V_{f}})}^{2}}{2{({a_{min} + {F_{r}/m}})}}$. As a worst case scenario, we assume that all the braking force is provided by the vehicle. Therefore, after ignoring $\frac{F_{r}}{m}$, we can say that $\mu \geq {- a_{min}}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "VI-B Input Constraints", "weight": 1.0} -->

We also modify $h_{3i}{(t,\mathbf{x})}$ to incorporate input constraints. We define a headway from a stop line of the traffic signal. If the current velocity is $V_{f}$, then it will take a time $\gamma = \frac{V_{f}}{a_{min}}$ for the ego vehicle to completely stop by applying its maximum braking effort. In the worst case scenario, $V_{f} = V_{max}$, $\gamma = \frac{V_{max}}{a_{min}}$. Therefore, the new CBF along with the CBF input constraints is given by

<!-- chunk {"id": "body-0045", "role": "body", "section": "VI-B Input Constraints", "weight": 1.0} -->

This modified time-varying CBF has relative degree $1$ and enforces the input constraints.

<!-- chunk {"id": "body-0046", "role": "body", "section": "VI-C Control Synthesis Using QP with Input Constraints", "weight": 1.0} -->

The controller can be synthesised by solving the following QP problem with input constrains.

<!-- chunk {"id": "body-0047", "role": "body", "section": "VI-C Control Synthesis Using QP with Input Constraints", "weight": 1.0} -->

The above controller ensures that the system fulfills the safety and regulatory constraints.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

We validate our approach on a road trip. A road scenario consists of a straight road with $6$ traffic signals, each $1$ Km away from the other. Traffic signals are not synchronized. Each traffic signal has its own timing sequence that is broadcast to the ego vehicle ahead of time. The values of the parameters used are $g = {9.8\frac{m}{s^{2}}}$, $m = {1650Kg}$, $c_{0} = {0.1N}$, $c_{1} = {5\frac{N}{m/s}}$, $c_{2} = {0.25\frac{N}{m/s^{2}}}$, $a_{max} = {0.2\text{g}\frac{m}{s^{2}}}$, $a_{min} = {- {0.4\text{g}\frac{m}{s^{2}}}}$, and $\tau = 6$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

The gains of the nominal controller are $k_{1} = 7.12$, $k_{2} = 3.24$, $k_{3} = 0.4$. The ego vehicle and the lead vehicle are initially at rest and ${X_{r}{}} = S_{0} = 4.5$ holds with $X_{f} = 0$, $X_{l} = 4.5$. The simulation was performed in MATLAB. In Fig. 2b, the lead vehicle is not following any traffic rules. It first speeds up, then maintains its velocity, and then decelerates. The lead vehicle violates the traffic signals and goes beyond the maximum speed limit of $V_{max}$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

The ego vehicle follows the lead vehicle while observing all the hard constraints HC-I (Fig. 2a), HC-II (Fig. 2b) and HC-III (Fig. 2c and Fig. 3). Fig. 2a shows that $\text{HC-I}:{{h_{1}{(x)}} \geq 0}$ is satisfied by the controller. Fig. 2b shows that $\text{HC-II}:{V_{f} \leq V_{max}}$ is always satisfied and the ego vehicle keeps its speed below the maximum speed limit $V_{max}$. From $t = {65s}$ to $154s$, the lead vehicle violates the traffic signals and goes at a velocity higher than $V_{max}$ but the ego vehicle obeys the traffic signals while still keeping the velocity below $V_{max}$. $h_{1}{(x)}$ first increases from $t = {65s}$ to $t = {154s}$, then it decreases as the lead vehicle slows down but it is never negative.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

The wheel force in ${N/m}g$ is shown in Fig. 2d. The input is constrained to the limit specified by the controller, i.e., $u_{min} \leq u \leq u_{max}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

The controller always satisfies HC-III, i.e., the ego vehicle obeys the traffic signals. Fig. 3 shows the trajectory of the ego vehicle with time. The height of the horizontal lines shows the position of the traffic signals, and the solid red horizontal lines show the interval where a traffic signal is red. The duration of green, red, and yellow signals are $25s$, $20s$, and $5s$, respectively. The zoomed plot in the Fig. 3 and the speed profile of the ego vehicle in Fig. 2b show that the ego vehicle preemptively slows down before a red signal and smoothly accelerates when the signal is green, thereby avoiding unnecessary stops by applying comfortable braking force as set by the input constraints.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

The traffic rules are encoded by ${\overline{h}}_{3}{(t,\mathbf{x})}$, that is, the non-negativeness of ${\overline{h}}_{3}{(t,\mathbf{x})}$ means that the ego vehicle obeys the traffic rules. Fig. 2c shows that ${{\overline{h}}_{3}{(t,\mathbf{x})}} \geq 0$ holds. The value of ${\overline{h}}_{3}{(t,\mathbf{x})}$ represents the safe distance from the next red signal.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

Therefore, ${{\overline{h}}_{3}{(0,{\mathbf{x}{(\mathbf{0})}})}} \approx 2000$. When $p_{1}$ is yellow, then ${\overline{h}}_{3}{(t,\mathbf{x})}$ decreases. Later, when the upcoming traffic signal turns green, ${\overline{h}}_{3}{(t,\mathbf{x})}$ increases. When the upcoming traffic signal is yellow, then ${\overline{h}}_{3}{(t,\mathbf{x})}$ starts decreasing smoothly. The ego vehicle always follows the traffic signals and never crosses the stop line when the signal is red. The controller fulfills the soft constraint that $V_{f}\rightarrow V_{l}$ and $\delta = {h_{1}{(x)}}\rightarrow 0$ as long as the hard constraints HC-I, HC-II and HC-III are not violated.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We presented a correct-by-construction adaptive cruise control design method under safety and regulatory constraints with control barrier guarantees. The proposed regulated ACC obeys the traffic signals and speed limits while maintaining safe spacing from the lead vehicle. The rules for traffic signals are described in the form of piecewise $\mathcal{C}^{m}$ time-varying control barrier functions (TV-CBFs). We proved that, for a valid piecewise $\mathcal{C}^{m}$ TV-CBF, there exists a controller that renders the corresponding superlevel set forward-invariant. Given a valid piece-wise $\mathcal{C}^{m}$ TV-CBF, a switching-based controller can be synthesized using quadratic programming. Simulation results validate the efficacy of the proposed method.
