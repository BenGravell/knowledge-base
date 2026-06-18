<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Safe Feedback Motion Planning: A Contraction Theory and L1-Adaptive Control Based Approach

Topics include Motion planning, Robotics, Safety, Online algorithms, Planning, Control.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Autonomous robots that are capable of operating safely in the presence of imperfect model knowledge or external disturbances are vital in safety-critical applications. In this paper, we present a planner-agnostic framework to design and certify safe tubes around desired trajectories that the robot is always guaranteed to remain inside of. By leveraging recent results in contraction analysis and L_1-adaptive control we synthesize an architecture that induces safe tubes for nonlinear systems with state and time-varying uncertainties. We demonstrate with a few illustrative examples how contraction theory-based L_1-adaptive control can be used in conjunction with traditional motion planning algorithms to obtain provably safe trajectories.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motion planning algorithms generate optimal open-loop trajectories for robots to follow; however, any uncertainty in the system can potentially drive the robot far away from the desired path. For instance, quadrotors experience blade-flapping and induced drag forces that are dependent on the velocity, ground effects that are dependent on the altitude, and external wind effects that are often unaccounted for by the motion planner,. Accurate modeling of these uncertainty effects on system dynamics can be very expensive and time-consuming. A widely accepted approach to account for uncertainty in motion planning is through feedback \[2, Chapter 8\]. In practice, ancillary tracking controllers or model predictive control (MPC) schemes are employed to alleviate this problem. However, the presence of the uncertainties is not explicitly considered in the control design process, and instead the performance is achieved with hand-tuned controller parameters and experimental validation. Without valid safety certificates, the uncertainty might drive the system unstable and far enough away from the desired trajectory, resulting in collisions with obstacles, Fig. 1a.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Robust trajectory tracking controllers using classical Lyapunov stability theory have been designed for helicopters, hovercraft, marine vehicles, and several other autonomous robots, which exhibit nonlinear behavior. These approaches rely on backstepping techniques, sliding-mode control, passivity-based control, or other robust nonlinear control design tools \[6, Chapter 14\]. However, the classical methods do not provide a 'one size fits all' procedure for the constructive design of tracking controllers for a large class of nonlinear systems. Unless the problem has a very specific structure that can be exploited, a control Lyapunov function (CLF) has to be found which can be prohibitively difficult for general nonlinear systems because the feasibility conditions do not appear as linear matrix inequalities (LMI), unlike in case of linear systems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Advances in computational resources and optimization toolboxes available to autonomous robots have led to active developments in the field of robust MPC. The two large classes of methods of interest are min-max MPC and tube-based MPC. Min-max MPC approaches consider the worst-case disturbance that can affect the system making them overly conservative. If the uncertainty is too large or the robot is planning over a long horizon, a min-max MPC based approach may even render the optimization infeasible. Tube-based MPC methods address these issues by employing an ancillary controller to attenuate disturbances and ensure that the robot stays inside of a 'tube' around the desired trajectory. However, with the exception of, these methods assume the existence of a stabilizing ancillary controller and its region of attraction along the desired trajectory. Moreover, the resulting tubes are of fixed width, which may be overly conservative depending on the operating conditions (see Fig. 1b). This issue is partly addressed for feedback linearizable systems in by using sliding-mode boundary layer control to construct tubes of any desired size during the MPC optimization procedure.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Furthermore, unlike classical methods, the MPC-based approaches while applicable to larger class of systems incur a heavy computational load and are not always amenable to real-time applications.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contraction theory-based approaches bridge the gap between classical and optimization-based methods, and provide a constructive control design procedure for nonlinear systems. In, the authors introduce contraction analysis as tool for studying stability of nonlinear systems using differential geometry. In particular, the authors show that the 'contracting' or convergent nature of solutions to nonlinear systems can be derived from the differential dynamics of the system. Since the differential dynamics for nonlinear systems are of linear-time varying (LTV) form, all the results from linear systems theory can be leveraged for nonlinear systems through the contraction analysis framework. In, constructive control design techniques from linear systems theory can be used to find a control contraction metric (CCM), which is analogous to CLFs in the differential framework. This is significantly easier than directly finding the CLFs for nonlinear systems, because the feasibility conditions for CCMs are represented as LMIs. In, a design procedure for synthesizing CCM-based controllers is given, which induces fixed-width tubes in the presence of bounded external disturbances, excluding modeling uncertainties. However, as discussed before, fixed-width tubes might result in infeasibility of the problem and result in more work for the planner to find a more conservative path that produces feasible tubes.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

More recently, in a model reference control architecture in conjunction with CCM-based feedback is proposed for handling uncertainties in the system.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we present an approach for safe feedback motion planning for control-affine nonlinear systems that relies on contraction theory-based solution for exponential stabilizability around trajectories and $\mathcal{L}_{1}$-adaptive control for handling uncertainties and providing guarantees for transient performance and robustness. In $\mathcal{L}_{1}$ control architecture, estimation is decoupled from control, thereby allowing for arbitrarily fast adaptation subject only to hardware limitations,. The $\mathcal{L}_{1}$ control has been successfully implemented on NASA's AirStar 5.5% subscale generic transport aircraft model, Calspan's Learjet, and unmmaned aerial vehicles. In, the authors presented the analysis for the $\mathcal{L}_{1}$-adaptive control architecture with nonlinear time-varying reference systems. However, the stabilizability of the nominal nonlinear model and associated safety certificates were simply assumed.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we present a constructive design of feedback strategy for nonlinear systems using CCMs and $\mathcal{L}_{1}$-adaptive control that provides strong guarantees of transient performance and robustness for a large class of control-affine nonlinear systems. Furthermore, we show how this control architecture induces tubes that can be flexibly changed to ensure safety based on the uncertainty in the system and the environment. In particular, this flexibility is provided by the architecture of the $\mathcal{L}_{1}$-adaptive control by decoupling the control loop from the estimation loop. In this way, the width of the certifiable tubes can be adjusted allowing the safe operation of a robot in tight confines.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The manuscript is organized as follows. The problem statement and the assumptions are provided in Section 2. A brief introduction to contraction theory is provided in Section 3. The proposed controller in presented in Section 4 and the stability analysis of the closed-loop system is provided in Section 5. Finally, in Section 6 the results of numerical experimentation are provided.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

We consider systems for which the evolution of dynamics can be represented as

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Consider a desired control trajectory ${u^{\star}{(t)}} \in {\mathbb{R}}^{m}$ and the induced desired state trajectory ${x^{\star}{(t)}} \in {\mathbb{R}}^{n}$ from any planner based on unperturbed/nominal dynamics

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Together, $({x^{\star}{(t)}},{u^{\star}{(t)}})$ is referred to as the desired state-input trajectory pair. The planner ensures that the desired state-trajectory $x^{\star}{(t)}$ remains in a compact safe set $\mathcal{X} \subset {\mathbb{R}}^{n}$, for all $t \geq 0$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

The goal is to design a control input $u{(t)}$ so that the state $x{(t)}$ of the uncertain system in remains 'close' to the desired trajectory $x^{\star}{(t)}$ while also ensuring ${x{(t)}} \in \mathcal{X}$, for all $t \geq 0$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

Given the positive scalar $\rho$, the desired state trajectory satisfies ${x^{\star}{(t)}} \in \mathcal{X}_{\rho}$, for all $t \geq 0$, where

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 2.2", "weight": 1.0} -->

The desired control/input trajectory satisfies

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 2.2", "weight": 1.0} -->

Note that the bound $\Delta_{u^{\star}}$ is obtained from the planner, which provides the desired state-input trajectory. Next, we place assumptions on the boundedness and continuity properties of the system functions and uncertainties.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 2.3", "weight": 1.0} -->

The known functions ${f{(x)}} \in {\mathbb{R}}^{n}$ and ${B{(x)}} \in {\mathbb{R}}^{n \times m}$ are bounded and continuously differentiable with bounded derivatives, satisfying

<!-- chunk {"id": "body-0020", "role": "body", "section": "Assumption 2.4", "weight": 1.0} -->

The uncertainty $h{(t,x)}$ is bounded and continuously differentiable in both $x$ and $t$ with bounded derivatives, satisfying

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 2.4", "weight": 1.0} -->

for all $x \in {\mathcal{O}{(\rho)}}$ and $t \geq 0$, where the bounds are assumed to be known.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 2.5", "weight": 1.0} -->

The input gain matrix $B{(x)}$ has full column rank. Furthermore, the Moore-Penrose inverse of $B{(x)}$ defined as ${B^{\dagger}{(x)}} = {\left( {B^{\top}{(x)}B{(x)}} \right)^{- 1}B^{\top}{(x)}}$ satisfies the following bounds

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

The nominal/unperturbed dynamics in Eq. 2 admit a CCM $M{(x)}$ for all $x \in \mathcal{X}$ with positive scalars $\lambda$, $\underset{¯}{\alpha}$, and $\overline{\alpha}$, as in Definition 3.2.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

Using Theorem 3.1. ‣ 3 Preliminaries on Contraction Theory ‣ Safe Feedback Motion Planning: A Contraction Theory and ℒ₁-Adaptive Control Based Approach") it is straightforward to conclude that the consequence of this assumption is that any desired state-input trajectory can be tracked by the nominal/unperturbed dynamics in the sense of Definition 3.1. ‣ 3 Preliminaries on Contraction Theory ‣ Safe Feedback Motion Planning: A Contraction Theory and ℒ₁-Adaptive Control Based Approach") with rate $\lambda$ and overshoot $R = {\overline{\alpha}/\underset{¯}{\alpha}}$. Let $\Xi{(p,q)}$ be the set of smooth curves connecting any two points ${p,q} \in \mathcal{X}$. Then using the Riemannian metric $M$, the length of any curve $\gamma \in {\Xi{(p,q)}}$ is given by the following expression

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

where ${\gamma_{s}{(s)}} = {\partial{{\gamma{(s)}}/{\partial s}}}$. By definition, the minimizing geodesic $\overline{\gamma}:{{\lbrack 0,1\rbrack}\rightarrow\mathcal{X}}$ satisfies the following relationship

<!-- chunk {"id": "body-0026", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

where $d{(p,q)}$ refers to the Riemannian distance between the two points $p$ and $q$. Existence of the minimizing geodesic is guaranteed by the Hopf-Rinow theorem. The Riemannian energy between the two points is defined using the Riemannian distance as the following quantity

<!-- chunk {"id": "body-0027", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

Further details on Riemannian geometry may be found. A direct and straightforward consequence of Assumption 3.1 is that

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

The proof for this relationship can be found in Lemma A.3. We will rely on the Riemannian energy's interpretation as a control Lyapunov function for the presented methodology. This interpretation was initially presented.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 3.1", "weight": 1.0} -->

Thus far we have only established the existence of feedback control operators and not constructed any. In fact, as explained in \[15, Sec. VI.A\], any controller may be chosen as long as the following set membership is established

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 3.1", "weight": 1.0} -->

The precise choice of the controller we use will be presented later in the manuscript.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Contraction Theory Based $\\mathcal{L}_{1}$-Adaptive Control", "weight": 1.0} -->

In this section we introduce the structure of the proposed controller for the uncertain nonlinear system in Eq. 1. Consider the following feedback decomposition

<!-- chunk {"id": "body-0032", "role": "body", "section": "Contraction Theory Based $\\mathcal{L}_{1}$-Adaptive Control", "weight": 1.0} -->

where $u_{c}:{{\mathbb{R}}_{\geq 0}\rightarrow{\mathbb{R}}^{m}}$ is the contraction theory based control designed to guarantee UES (Definition 3.1. ‣ 3 Preliminaries on Contraction Theory ‣ Safe Feedback Motion Planning: A Contraction Theory and ℒ₁-Adaptive Control Based Approach")) of the nominal dynamics in Eq. 2, and $u_{a}:{{\mathbb{R}}_{\geq 0}\rightarrow{\mathbb{R}}^{m}}$ is the $\mathcal{L}_{1}$ control signal. The overall architecture of the proposed feedback is illustrated in Fig. 2. We refer to the uncertain system in Eq. 1 with the feedback law Eq. 13 as the $\mathcal{L}_{1}$ closed-loop system.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Contraction theory based control: $u_{c}{(t)}$", "weight": 1.0} -->

As mentioned in Section 3, under Assumption 3.1, Theorem 3.1. ‣ 3 Preliminaries on Contraction Theory ‣ Safe Feedback Motion Planning: A Contraction Theory and ℒ₁-Adaptive Control Based Approach") guarantees the existence of a feedback law which renders the nominal dynamics in Eq. 2 UES. In particular, we propose the following law

<!-- chunk {"id": "body-0034", "role": "body", "section": "Contraction theory based control: $u_{c}{(t)}$", "weight": 1.0} -->

where, for the the feedback term, we use the law constructed in \[18, Sec. 5.1\],

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 4.1", "weight": 1.0} -->

As explained by the authors in \[18, Sec. 5.1\], the solution to the quadratic program in (25 ‣ 4 Contraction Theory Based ℒ₁-Adaptive Control ‣ Safe Feedback Motion Planning: A Contraction Theory and ℒ₁-Adaptive Control Based Approach")) can be obtained analytically given the minimizing geodesic $\overline{\gamma}{( \cdot,t)}$. Alternatively, one may use the differential controller proposed, albeit at the expense of an increase in the control effort.

<!-- chunk {"id": "body-0036", "role": "body", "section": "$\\mathcal{L}_{1}$-adaptive control: $u_{a}{(t)}$", "weight": 1.0} -->

The computation of the signal $u_{a}{(t)}$ depends on three components illustrated in Fig. 2, namely, the state-predictor, the adaptation law, and a low-pass filter. Similar to, we define the state-predictor as

<!-- chunk {"id": "body-0037", "role": "body", "section": "$\\mathcal{L}_{1}$-adaptive control: $u_{a}{(t)}$", "weight": 1.0} -->

The uncertainty estimate $\hat{\sigma}{(t)}$ in Eq. 26 ‣ 4 Contraction Theory Based ℒ₁-Adaptive Control ‣ Safe Feedback Motion Planning: A Contraction Theory and ℒ₁-Adaptive Control Based Approach") is governed by the following adaptation law

<!-- chunk {"id": "body-0038", "role": "body", "section": "$\\mathcal{L}_{1}$-adaptive control: $u_{a}{(t)}$", "weight": 1.0} -->

where $\Gamma > 0$ is the adaptation rate, $\mathcal{H} = \left. \{{y \in {\mathbb{R}}^{m}} \middle| {\left. \parallel y\parallel \right. \leq \Delta_{h}}\} \right.$ is the set to which the uncertainty estimate is restricted to remain in with $\Delta_{h}$ defined in Assumption 2.4. Furthermore, ${\mathbb{S}}^{n} \ni P \succ 0$, is the solution to the Lyapunov equation ${{A_{m}^{\top}P} + {PA_{m}}} = {- Q}$, for some ${\mathbb{S}}^{n} \ni Q \succ 0$. Moreover, $\operatorname{Proj}_{\mathcal{H}}{( \cdot, \cdot )}$ is the projection operator standard in adaptive control literature,.

<!-- chunk {"id": "body-0039", "role": "body", "section": "$\\mathcal{L}_{1}$-adaptive control: $u_{a}{(t)}$", "weight": 1.0} -->

Finally, the control law $u_{a}{(t)}$ is defined as the following Laplace transform

<!-- chunk {"id": "body-0040", "role": "body", "section": "$\\mathcal{L}_{1}$-adaptive control: $u_{a}{(t)}$", "weight": 1.0} -->

where $C{(s)}$ is a low-pass filter with bandwidth $\omega$ and satisfies ${C{}} = {\mathbb{I}}_{m}$. Note that there is an abuse of notation when we denote both the geodesic interval parameter and the Laplace variable by $s$. The delineation between the two is clear from the context.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Filter bandwidth and adaptation rate", "weight": 1.0} -->

The design of the $\mathcal{L}_{1}$-adaptive controller involves the design of a strictly proper and stable low-pass filter $C{(s)}$ with ${C{}} = {\mathbb{I}}_{m}$. Let the bandwidth of this filter be $\omega$. In the manuscript, for the sake of simplicity, we choose ${C{(s)}} = {\frac{\omega}{s + \omega}{\mathbb{I}}_{m}}$. As we will see in Section 5, the bandwidth $\omega$ of the low-pass filter $C{(s)}$ in Eq. 28 ‣ 4 Contraction Theory Based ℒ₁-Adaptive Control ‣ Safe Feedback Motion Planning: A Contraction Theory and ℒ₁-Adaptive Control Based Approach") and the adaptation rate $\Gamma$ in Eq. 27 ‣ 4 Contraction Theory Based ℒ₁-Adaptive Control ‣ Safe Feedback Motion Planning: A Contraction Theory and ℒ₁-Adaptive Control Based Approach") are design parameters which can be thought of as 'tuning-knobs'. However, these entities need to satisfy a few conditions mentioned below.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Filter bandwidth and adaptation rate", "weight": 1.0} -->

The reasoning behind these conditions will be made clear in the subsequent section.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Filter bandwidth and adaptation rate", "weight": 1.0} -->

Suppose that Assumption 3.1 holds. Then, for arbitrarily chosen positive scalars $\epsilon$ and $\rho_{a}$, define

<!-- chunk {"id": "body-0044", "role": "body", "section": "Filter bandwidth and adaptation rate", "weight": 1.0} -->

Furthermore, suppose that Assumptions 2.1-2.5 hold. Define

<!-- chunk {"id": "body-0045", "role": "body", "section": "Filter bandwidth and adaptation rate", "weight": 1.0} -->

Then, the bandwidth $\omega$ of the low-pass filter $C{(s)}$ and the adaptation rate need to verify the following conditions

<!-- chunk {"id": "body-0046", "role": "body", "section": "Filter bandwidth and adaptation rate", "weight": 1.0} -->

where $\Delta_{\theta}$ is another known positive scalar defined in Eq. 21.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Remark 4.2", "weight": 1.0} -->

Based on the definition of $\rho_{r}$ in Eq. 30 and the bounds on the Riemannian energy $\mathcal{E}{({x^{\star}{(t)}},{x{(t)}})}$ in Eq. 12, the inequality $\rho_{r}^{2} > {{\mathcal{E}{(x_{0}^{\star},x_{0})}}/\underset{¯}{\alpha}}$ holds. Furthermore, since $\zeta_{1}{(\omega)}$, $\zeta_{2}{(\omega)}$, and $\zeta_{3}{(\omega)}$, all converge to zero as $\omega$ increases, the bandwidth conditions in (32a)-(32b) can always be satisfied by choosing a large enough $\omega$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Performance Analysis", "weight": 1.0} -->

In this section we analyze the performance of the uncertain system in Eq. 1 with the $\mathcal{L}_{1}$ control feedback $u{(t)}$ defined in Eq. 13.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Performance Analysis", "weight": 1.0} -->

where $k_{c}$ is defined in Eq. 25 ‣ 4 Contraction Theory Based ℒ₁-Adaptive Control ‣ Safe Feedback Motion Planning: A Contraction Theory and ℒ₁-Adaptive Control Based Approach") using $x_{r}$ in place of $x$. The main feature of the reference system is that it defines the the best achievable performance, given the perfect knowledge of uncertainty, i.e. it reflects that the cancellation of the uncertainty $h{(t,{x_{r}{(t)}})}$ can happen only within the bandwidth of the low-pass filter.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Performance Analysis", "weight": 1.0} -->

The analysis consists of two parts: we first derive bounds between the desired trajectory and the reference system $\|{{x^{\star}{(t)}} - {x_{r}{(t)}}}\|$. Then we derive the bounds between the states of the reference system and the actual system $\left. \parallel{{x_{r}{(t)}} - {x{(t)}}}\parallel \right.$. Recall that we refer to the actual system as the $\mathcal{L}_{1}$ closed loop system, which is given by Eq. 1 with the control law in Eq. 13. Finally, the triangle inequality produces the desired bound on $\left. \parallel{{x^{\star}{(t)}} - {x{(t)}}}\parallel \right.$. In this way, the reference system behaves as an 'anchor system' for the analysis. These bounds are illustrated in Fig. 3.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Performance Analysis", "weight": 1.0} -->

Furthermore, we provide the justification of treating the bandwidth $\omega$ of $C{(s)}$ and the adaptation rate $\Gamma$ as tuning-knobs. Indeed, the upcoming analysis will show that we can ensure that ${x{(t)}} \in {\Omega{(\rho,{x^{\star}{(t)}})}}$ (see Eq. 4) for all $t \geq 0$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Performance Analysis", "weight": 1.0} -->

We begin with the bound between the reference system state and desired state trajectory. This corresponds to the green tube in Fig. 3. The proofs for all the claims in this section are provided in Appendix B.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Discussion", "weight": 1.5} -->

A few critical comments are in order for the performance analysis. The main result in Theorem 5.1 provides uniform ultimate bounds. Let us first discuss the implication of the uniform bound $\rho$ in Eq. 37. As per the definition in Eq. 30, $\rho = {\rho_{r} + \rho_{a}}$. It is evident from the definition that $\rho$ is lower bounded by the initial condition difference $\left. \parallel{x_{0}^{\star} - x_{0}}\parallel \right.$ and the positive scalars $\underset{¯}{\alpha}$ and $\overline{\alpha}$ which are associated with the CCM $M{(x)}$ of the nominal dynamics.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Discussion", "weight": 1.5} -->

Furthermore, as per the proof of Lemma 5.2, since $\rho_{a} \propto {1/\sqrt{\Gamma}}$, the adaptation rate $\Gamma$ can be increased to the maximum value allowable by the computation hardware to guarantee the smallest $\rho_{a}$, and thus, the smallest uniform bound $\rho$. However, the fact remains that the uniform bound $\rho$ guaranteed by the $\mathcal{L}_{1}$-controller for the tracking remains lower bounded by $\left. \parallel{x_{0}^{\star} - x_{0}}\parallel \right.$. The only way this bound can be further reduced is if the underlying planner which provides the desired state-input pair $({x^{\star}{(t)}},{u^{\star}{(t)}})$ can minimize $\left. \parallel{x_{0}^{\star} - x_{0}}\parallel \right.$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Discussion", "weight": 1.5} -->

Theorem 5.1 also provides the (uniform) ultimate bound via $\delta{(\omega,T)}$ defined in Eq. 39. As already mentioned, $\rho_{a} \propto {1/\sqrt{\Gamma}}$. Furthermore, from the definition of $\zeta_{1}{(\omega)}$ in Eq. 31a, it is evident that by choosing a large enough $\omega$, there will always exist a known $0 < T < \infty$ such that ${\delta{(\omega,t)}} \leq \overline{\rho}$, for all $t \geq T$, for any chosen $\overline{\delta} > 0$. Therefore, we can always arbitrarily shrink the tube $\mathcal{O}{(\overline{\delta})}$ by choosing appropriate bandwidth $\omega$ and rate of adaptation $\Gamma$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Discussion", "weight": 1.5} -->

This feature of the CCM-based $\mathcal{L}_{1}$-controller is very advantageous, since, for example, this capability will allow the safe navigation of a robot through tight and cluttered environments. This improved performance, however, comes at the cost of reduced robustness. There exists a trade-off between performance and robustness that should be taken into consideration. As aforementioned, performance (radius of tubes around $x^{\star}{(t)}$) depends on $\Gamma$ and $\omega$. The rate of adaptation $\Gamma$ is obviously limited by the available computational hardware. More importantly, the role of the low-pass filter $C{(s)}$ in the $\mathcal{L}_{1}$-control architecture (Fig. 2) is to decouple the control loop from the estimation loop.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Discussion", "weight": 1.5} -->

Thus, increasing the bandwidth $\omega$ of $C{(s)}$ in order to get a tighter tube will lead to the $u_{a}{(t)}$ component of the $\mathcal{L}_{1}$-input to behave as a high-gain signal, thus possibly sacrificing desired robustness levels. Therefore, this trade-off must always be taken into account during the planning phase.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

We provide two illustrative examples. In the first example, we consider the non-feedback linearizable system from and synthesize the controller to ensure safe regulation around the equilibrium point. We also show the effect of uniform ultimate bounds discussed in the previous section, if the system were to start far away from the equilibrium. In the second example, we consider the system from and ensure safety in a motion planning context during trajectory tracking. In particular we show how altering the tube parameters affects the choice in the filter bandwidth and adaptation rate.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Non-feedback Linearizable Systems", "weight": 1.0} -->

Consider the system with the structure defined in Eq. 1 and the system functions given by

<!-- chunk {"id": "body-0060", "role": "body", "section": "Non-feedback Linearizable Systems", "weight": 1.0} -->

where the state ${x{(t)}} = {\lbrack{x_{1}{(t)}x_{2}{(t)}x_{3}{(t)}}\rbrack}^{\top}$. The dual metric ${W{(x)}} = {M{(x)}^{- 1}}$ satisfying the conditions in Eqs. 8a, 8b and 8c was found using the sum-of-squares programming toolbox SumOfSquares.jl, optimization software JuMP, and the optimization solver, as

<!-- chunk {"id": "body-0061", "role": "body", "section": "Non-feedback Linearizable Systems", "weight": 1.0} -->

The metric satisfies a convergence rate $\lambda = 1.0$ and is uniformly bounded in the set $\mathcal{X} = \left. \{{y \in {\mathbb{R}}^{3}} \middle| {\left. \parallel y\parallel \right._{\infty} \leq 0.1}\} \right.$ with $\overline{\alpha} = 5.88$ and $\underset{¯}{\alpha} = 3.85$. Now, suppose that the system is experiencing sinusoidal disturbances of the form: ${h{(t)}} = {0.1{\sin{({2t})}}}$. We chose the initial condition of the system as $x_{0} = {{\lbrack{1 - 1\ 1}\rbrack}^{\top} \times 10^{- 2}}$ and the desired state as $x^{\star} = {\lbrack 0\ 0\ 0\rbrack}^{\top}$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Non-feedback Linearizable Systems", "weight": 1.0} -->

Incidentally, the desired state is also the equilibrium point of the system which means that the desired control is ${u^{\star}{(t)}} \equiv 0$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Non-feedback Linearizable Systems", "weight": 1.0} -->

A pure CCM-based feedback strategy produces the oscillatory behavior, seen in Fig. 4a. A CCM-based $\mathcal{L}_{1}$-adaptive controller is designed in Fig. 4b for tube widths $\epsilon = 0.01$ and $\rho_{a} = 0.01$. The filter bandwidth and adaptation rate required to achieve this level of performance were chosen as $\omega = 50$ and $\Gamma = {5 \times 10^{6}}$ respectively by satisfying the conditions in Eq. 32. Notice that the bounds are far more conservative than the actual behavior of the system. In fact, the error in tracking is uniformly bounded as $\left. \parallel x\parallel \right._{\mathcal{L}_{\infty}} < 0.02$. Additionally, notice that the uniform ultimate bounds of the reference system tube from Eq. 36 and the actual system tube from Eq. 39 shrink with time and are essentially 'forgetting' the initial conditions of the system.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Safe Tubes for Motion Planning", "weight": 1.0} -->

Consider the system with the structure defined in Eq. 1 and the system functions given by

<!-- chunk {"id": "body-0065", "role": "body", "section": "Safe Tubes for Motion Planning", "weight": 1.0} -->

where the state ${x{(t)}} = {\lbrack{x_{1}{(t)}x_{2}{(t)}}\rbrack}^{\top}$. Since this particular system is feedback linearizable, it admits a constant (or flat) dual metric for all $x \in {\mathbb{R}}^{2}$.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Safe Tubes for Motion Planning", "weight": 1.0} -->

Similar to, we chose the initial condition of the system as $x_{0} = {\lbrack{3.4 - 2.4}\rbrack}^{\top}$ and the target state as as $x^{\star} = {\lbrack 0\ 0\rbrack}^{\top}$. The desired state and control trajectory pair was computed using the iterative LQR solver provided by with the parameters $Q = {0.5{\mathbb{I}}_{2}}$ and $R = 1.0$. Suppose the system is affected by uncertainties of the form: ${h{(t,x)}} = {{- {2{\sin{({2t})}}}} - {0.1\left. \parallel{x{(t)}}\parallel \right.}}$, consisting of both time and state dependent terms.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Safe Tubes for Motion Planning", "weight": 1.0} -->

Depending on the desired level of tracking performance or closeness to obstacles in the environment, the user will pick the tube parameters $\epsilon$ and $\rho_{a}$ as defined in Eq. 30. In Fig. 5, we illustrate the trade-offs between choosing a tighter $\rho_{a}$ (Fig. 5a) versus a tighter $\epsilon$ (Fig. 5c) for this system.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Safe Tubes for Motion Planning", "weight": 1.0} -->

In Fig. 6b, we observe the performance and robustness benefits of using CCM-based $\mathcal{L}_{1}$-adaptive control. Not only does the system track the desired trajectory closely, but also avoids colliding with obstacles (unlike in Fig. 6a) through an appropriate choice of tube parameters.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

We present a control methodology to enable safe and guaranteed feedback motion planning. The presented work relies on differential geometric contraction theory and $\mathcal{L}_{1}$-adaptive control. The proposed controller enables the apriori computation of uniform and ultimate-bounds which act as safety-certificates. These safety certificates induce 'tubes' which can be taken into account by any planner of choice. In this way, the safety of the system/robot is always guaranteed in the presence of model and environmental uncertainties. Furthermore, by using the control law's filter bandwidth and rate of adaptation as tuning knobs, the width of the safety tubes can be adjusted. Future research will deal with the incorporation of learning into the proposed control framework. This will lead to improved performance since the underlying planner will have access to improved model knowledge. More importantly, the controller proposed in this work will keep the learning process safe because of the apriori specified and guaranteed bounds during the transient phase. Further investigations will be undertaken to extend this framework to enable safe planning and control using a reduced-order model to enable fast planning.
