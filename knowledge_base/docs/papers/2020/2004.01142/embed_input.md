<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Safe Feedback Motion Planning: A Contraction Theory and L1-Adaptive Control Based Approach

Topics include Motion planning, Robotics, Safety, Online algorithms, Planning, Control.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Autonomous robots that are capable of operating safely in the presence of imperfect model knowledge or external disturbances are vital in safety-critical applications. In this paper, we present a planner-agnostic framework to design and certify safe tubes around desired trajectories that the robot is always guaranteed to remain inside of. By leveraging recent results in contraction analysis and L_1-adaptive control we synthesize an architecture that induces safe tubes for nonlinear systems with state and time-varying uncertainties. We demonstrate with a few illustrative examples how contraction theory-based L_1-adaptive control can be used in conjunction with traditional motion planning algorithms to obtain provably safe trajectories.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motion planning algorithms generate optimal open-loop trajectories for robots to follow; however, any uncertainty in the system can potentially drive the robot far away from the desired path. For instance, quadrotors experience bladeflapping and induced drag forces that are dependent on the velocity, ground effects that are dependent on the altitude, and external wind effects that are often unaccounted for by the motion planner,. Accurate modeling of these uncertainty effects on system dynamics can be very expensive and time-consuming. A widely accepted approach to account for uncertainty in motion planning is through feedback [2, Chapter 8]. In practice, ancillary tracking controllers or model predictive control (MPC) schemes are employed to alleviate this problem. However, the presence of the uncertainties is not explicitly considered in the control design process, and instead the performance is achieved with hand-tuned controller parameters and experimental validation. Without valid safety certificates, the uncertainty might drive the system unstable and far enough away from the desired trajectory, resulting in collisions with obstacles, Fig. 1a.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Robust trajectory tracking controllers using classical Lyapunov stability theory have been designed for helicopters, hovercraft, marine vehicles, and several other autonomous robots, which exhibit nonlinear behavior. These approaches rely on backstepping techniques, sliding-mode control, passivity-based control, or other robust nonlinear control design tools [6, Chapter 14]. However, the classical methods do not provide a 'one size fits all' procedure for the constructive design of tracking controllers for a large class of nonlinear systems. Unless the problem has a very specific structure that can be exploited, a control Lyapunov function (CLF) has to be found which can be prohibitively difficult for general nonlinear systems because the feasibility conditions do not appear as linear matrix inequalities (LMI), unlike in case of linear systems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

∗ These authors contributed equally for this work 2 The implementation can be found Figure 1: Although the planned path is collision free (purple), the robot's actual trajectory (dashed-blue) might lead to a collision with the obstacles (gray) in the environment due to model discrepancies or external disturbances. (b) A feedback policy ensures that the robot stays inside of the (orange) tube which is too wide to pass between the obstacles without colliding (c) The safe feedback controller proposed in this paper guarantees that the robot's trajectory never escapes the tube, which itself is also collision-free.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Advances in computational resources and optimization toolboxes available to autonomous robots have led to active developments in the field of robust MPC. The two large classes of methods of interest are min-max MPC and tube-based MPC. Min-max MPC approaches consider the worst-case disturbance that can affect the system making them overly conservative. If the uncertainty is too large or the robot is planning over a long horizon, a minmax MPC based approach may even render the optimization infeasible. Tube-based MPC methods address these issues by employing an ancillary controller to attenuate disturbances and ensure that the robot stays inside of a 'tube' around the desired trajectory. However, with the exception of, these methods assume the existence of a stabilizing ancillary controller and its region of attraction along the desired trajectory. Moreover, the resulting tubes are of fixed width, which may be overly conservative depending on the operating conditions (see Fig. 1b). This issue is partly addressed for feedback linearizable systems in by using sliding-mode boundary layer control to construct tubes of any desired size during the MPC optimization procedure.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Furthermore, unlike classical methods, the MPC-based approaches while applicable to larger class of systems incur a heavy computational load and are not always amenable to real-time applications.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contraction theory-based approaches bridge the gap between classical and optimization-based methods, and provide a constructive control design procedure for nonlinear systems. In, the authors introduce contraction analysis as tool for studying stability of nonlinear systems using differential geometry. In particular, the authors show that the 'contracting' or convergent nature of solutions to nonlinear systems can be derived from the differential dynamics of the system. Since the differential dynamics for nonlinear systems are of linear-time varying (LTV) form, all the results from linear systems theory can be leveraged for nonlinear systems through the contraction analysis framework. In, constructive control design techniques from linear systems theory can be used to find a control contraction metric (CCM), which is analogous to CLFs in the differential framework. This is significantly easier than directly finding the CLFs for nonlinear systems, because the feasibility conditions for CCMs are represented as LMIs. In, a design procedure for synthesizing CCM-based controllers is given, which induces fixed-width tubes in the presence of bounded external disturbances, excluding modeling uncertainties. However, as discussed before, fixed-width tubes might result in infeasibility of the problem and result in more work for the planner to find a more conservative path that produces feasible tubes.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

More recently, in a model reference control architecture in conjunction with CCM-based feedback is proposed for handling uncertainties in the system.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we present an approach for safe feedback motion planning for control-affine nonlinear systems that relies on contraction theory-based solution for exponential stabilizability around trajectories and L 1 -adaptive control for handling uncertainties and providing guarantees for transient performance and robustness. In L 1 control architecture, estimation is decoupled from control, thereby allowing for arbitrarily fast adaptation subject only to hardware limitations,. The L 1 control has been successfully implemented on NASA's AirStar 5.5% subscale generic transport aircraft model, Calspan's Learjet, and unmmaned aerial vehicles. In, the authors presented the analysis for the L 1 -adaptive control architecture with nonlinear time-varying reference systems. However, the stabilizability of the nominal nonlinear model and associated safety certificates were simply assumed. In this paper, we present a constructive design of feedback strategy for nonlinear systems using CCMs and L 1 -adaptive control that pro- vides strong guarantees of transient performance and robustness for a large class of control-affine nonlinear systems. Furthermore, we show how this control architecture induces tubes that can be flexibly changed to ensure safety based on the uncertainty in the system and the environment.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In particular, this flexibility is provided by the architecture of the L 1 -adaptive control by decoupling the control loop from the estimation loop. In this way, the width of the certifiable tubes can be adjusted allowing the safe operation of a robot in tight confines.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The manuscript is organized as follows. The problem statement and the assumptions are provided in Section 2. A brief introduction to contraction theory is provided in Section 3. The proposed controller in presented in Section 4 and the stability analysis of the closed-loop system is provided in Section 5. Finally, in Section 6 the results of numerical experimentation are provided.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

We consider systems for which the evolution of dynamics can be represented as with initial condition x = x 0, where x (t) ∈ R n is the system state and u (t) ∈ R m is the control input. The functions f (x) ∈ R n and B (x) ∈ R n × m are known, and h (t, x) ∈ R m represents the uncertainties. The unperturbed/nominal dynamics (h ≡ 0) are therefore represented as Consider a desired control trajectory u ⋆ (t) ∈ R m and the induced desired state trajectory x ⋆ (t) ∈ R n from any planner based on unperturbed/nominal dynamics Together, (x ⋆ (t), u ⋆ (t)) is referred to as the desired state-input trajectory pair. The planner ensures that the desired state-trajectory x ⋆ (t) remains in a compact safe set X ⊂ R n, for all t ≥ 0.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

The goal is to design a control input u (t) so that the state x (t) of the uncertain system in remains 'close' to the desired trajectory x ⋆ (t) while also ensuring x (t) ∈ X, for all t ≥ 0. In order to rigorously define the notion of 'closeness', we need the following definition: Definition 2.1. Given a positive scalar ρ and the desired state trajectory x ⋆ (t), Ω(ρ, x ⋆ (t)) denotes the ρ -norm ball around x ⋆ (t), i.e.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Clearly Ω(ρ, x ⋆ (t)) induces a tube centered around x ⋆ (t), where the tube is given by with ρ > 0 as the radius.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

The problem under consideration can now be stated as follows: Given the desired trajectory x ⋆ (t) ∈ X and a positive scalar ρ, design a control input u (t) such that the state of the uncertain system satisfies: Note the condition that Ω(ρ, x ⋆ (t)) ⊂ X is dependent on the desired trajectory x ⋆ (t) (given by the planner) and the tube width ρ (chosen by the user). To ensure that this control-independent condition is satisfied, we place the following assumption.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Assumption 2.1. Given the positive scalar ρ, the desired state trajectory satisfies x ⋆ (t) ∈ X ρ, for all t ≥ 0, where Remark 2.1. The implication of Assumption 2.1 is that if the state trajectory satisfies x (t) -x ⋆ (t) ∈ B (ρ) and x ⋆ (t) ∈ X ρ, for all t ≥ 0, then the definition of the Pontryagin set difference implies that x (t) ∈ Ω(ρ, x ⋆ (t)) ⊂ X, for all t ≥ 0.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Assumption 2.2. The desired control/input trajectory satisfies with the upper bound ∆ u ⋆ known.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Note that the bound ∆ u ⋆ is obtained from the planner, which provides the desired state-input trajectory. Next, we place assumptions on the boundedness and continuity properties of the system functions and uncertainties.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Assumption 2.3. The known functions f (x) ∈ R n and B (x) ∈ R n × m are bounded and continuously differentiable with bounded derivatives, satisfying for all x ∈ O (ρ), where b j (x) is the j th column of B (x) and the bounds are assumed to be known.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Assumption 2.4. The uncertainty h (t, x) is bounded and continuously differentiable in both x and t with bounded derivatives, satisfying for all x ∈ O (ρ) and t ≥ 0, where the bounds are assumed to be known.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Assumption 2.5. The input gain matrix B ( x ) has full column rank. Furthermore, the Moore-Penrose inverse of B ( x ) defined as B † ( x ) = ( B ⊤ ( x ) B ( x ) ) -1 B ⊤ ( x ) satisfies the following bounds

<!-- chunk {"id": "body-0023", "role": "body", "section": "Contraction Theory Based L 1 -Adaptive Control", "weight": 1.0} -->

In this section we introduce the structure of the proposed controller for the uncertain nonlinear system in Eq.. Consider the following feedback decomposition where u c: R ≥ 0 → R m is the contraction theory based control designed to guarantee UES (Definition 3.1) of the nominal dynamics in Eq., and u a: R ≥ 0 → R m is the L 1 control signal. The overall architecture of the proposed feedback is illustrated in Fig. 2. We refer to the uncertain system in Eq. with the feedback law Eq. as the L 1 closed-loop system.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Contraction Theory Based L 1 -Adaptive Control", "weight": 1.0} -->

Before we proceed with the description of the individual components of the controller, we introduce the following list of constants that are of importance for the results and analyses presented in this paper: where O (ρ) is defined in Eq.; ∆ u ⋆ is defined in Assumption 2.2; ∆ f, ∆ f x, ∆ B, ∆ B x, ∆ b x, are defined in Assumption 2.3; ∆ h, ∆ h t, ∆ h x are defined in Assumption 2.4; ∆ B † and ∆ B † x are defined in Assumption 2.5; α and α are defined in Assumption 3.1; and F (x) is defined as where W (x) = M (x) -1 is referred to as the dual metric and L (x) ⊤ L (x) = W (x).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Contraction theory based control: u c ( t )", "weight": 1.0} -->

As mentioned in Section 3, under Assumption 3.1, Theorem 3.1 guarantees the existence of a feedback law which renders the nominal dynamics in Eq. UES. In particular, we propose the following law Figure 2: Architecture of CCM-based L 1 -adaptive control where, for the the feedback term, we use the law constructed in [18, Sec. 5.1], which is the solution to the following quadratic program: in which M (·) is the CCM (Definition 3.2), γ (s, t), s ∈, is the minimizing geodesic with γ (1, t) = x k (t) and γ (0, t) = x ⋆ (t). As previously defined, the desired state-input pair satisfies ˙ x ⋆ (t) = ¯ F (x ⋆ (t), u ⋆ (t)) with the nominal dynamics defined in Eq.. Additionally, ˙ x k (t) = ¯ F (x (t), u ⋆ (t) + k).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Contraction theory based control: u c ( t )", "weight": 1.0} -->

Remark 4.1. As explained by the authors in [18, Sec. 5.1], the solution to the quadratic program in can be obtained analytically given the minimizing geodesic γ ( ·, t ). Alternatively, one may use the differential controller proposed, albeit at the expense of an increase in the control effort.

<!-- chunk {"id": "body-0027", "role": "body", "section": "adaptive control: u a ( t )", "weight": 1.0} -->

The computation of the signal u a (t) depends on three components illustrated in Fig. 2, namely, the state-predictor, the adaptation law, and a low-pass filter. Similar to, we define the state-predictor as with ˆ x = x 0, and where ˆ x (t) ∈ R n is the state of the predictor, ˜ x (t) = ˆ x (t) -x (t) is the state prediction error, and A m ∈ R n × n is an arbitrary Hurwitz matrix.

<!-- chunk {"id": "body-0028", "role": "body", "section": "adaptive control: u a ( t )", "weight": 1.0} -->

The uncertainty estimate ˆ σ (t) in Eq. is governed by the following adaptation law where Γ > 0 is the adaptation rate, H = { y ∈ R m | ‖ y ‖ ≤ ∆ h } is the set to which the uncertainty estimate is restricted to remain in with ∆ h defined in Assumption 2.4. Furthermore, S n ∋ P ≻ 0, is the solution to the Lyapunov equation A ⊤ m P + PA m = -Q, for some S n ∋ Q ≻ 0. Moreover, Proj H (·, ·) is the projection operator standard in adaptive control literature,.

<!-- chunk {"id": "body-0029", "role": "body", "section": "adaptive control: u a ( t )", "weight": 1.0} -->

Finally, the control law u a (t) is defined as the following Laplace transform where C (s) is a low-pass filter with bandwidth ω and satisfies C = I m. Note that there is an abuse of notation when we denote both the geodesic interval parameter and the Laplace variable by s. The delineation between the two is clear from the context.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Filter bandwidth and adaptation rate", "weight": 1.0} -->

The design of the L 1 -adaptive controller involves the design of a strictly proper and stable low-pass filter C ( s ) with C = I m. Let the bandwidth of this filter be ω. In the manuscript, for the sake of simplicity, we choose C ( s ) = ω s + ω I m. As we will see in Section 5, the bandwidth ω of the low-pass filter C ( s ) in Eq. and the adaptation rate Γ in Eq. are design parameters which can be thought of as 'tuning-knobs'. However, these entities need to satisfy a few conditions mentioned below. The reasoning behind these conditions will be made clear in the subsequent section.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Filter bandwidth and adaptation rate", "weight": 1.0} -->

Suppose that Assumption 3.1 holds. Then, for arbitrarily chosen positive scalars ϵ and ρ a, define Furthermore, suppose that Assumptions 2.1-2.5 hold. Define where ∆ ˙ x r, ∆ Ψ x, and ∆ ˙ Ψ, are known positive scalars defined in Eqs., and respectively. Then, the bandwidth ω of the low-pass filter C (s) and the adaptation rate need to verify the following conditions where ∆ θ is another known positive scalar defined in Eq..

<!-- chunk {"id": "body-0032", "role": "body", "section": "Filter bandwidth and adaptation rate", "weight": 1.0} -->

Remark 4.2. Based on the definition of ρ r in Eq. and the bounds on the Riemannian energy E ( x ⋆ ( t ), x ( t )) in Eq., the inequality ρ 2 r > E ( x ⋆ 0, x 0 ) /α holds. Furthermore, since ζ 1 ( ω ), ζ 2 ( ω ), and ζ 3 ( ω ), all converge to zero as ω increases, the bandwidth conditions in (32a) -(32b) can always be satisfied by choosing a large enough ω.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Performance Analysis", "weight": 1.0} -->

In this section we analyze the performance of the uncertain system in Eq. with the L 1 control feedback u (t) defined in Eq.. As, to derive the bounds between the desired trajectory x ⋆ (t) and the state x (t) of the uncertain system, we first introduce the following intermediate system, which we refer to as the reference system: where k c is defined in Eq. using x r in place of x. The main feature of the reference system is that it defines the the best achievable performance, given the perfect knowledge of uncertainty, i.e. it reflects that the cancellation of the uncertainty h (t, x r (t)) can happen only within the bandwidth of the low-pass filter.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Performance Analysis", "weight": 1.0} -->

The analysis consists of two parts: we first derive bounds between the desired trajectory and the reference system ‖ x ⋆ ( t ) -x r ( t ) ‖. Then we derive the bounds between the states of the reference system and the actual system ‖ x r ( t ) -x ( t ) ‖. Recall that we refer to the actual system as the L 1 closed loop system, which is given by Eq. with the control law in Eq.. Finally, the triangle inequality produces the desired bound on ‖ x ⋆ ( t ) -x ( t ) ‖. In this way, the reference system behaves as an 'anchor system' for the analysis. These bounds are illustrated in Fig. 3. Furthermore, we provide the justification of treating the bandwidth ω of C ( s ) and the adaptation rate Γ as tuning-knobs. Indeed, the upcoming analysis will show that we can ensure that x ( t ) ∈ Ω( ρ, x ⋆ ( t )) (see Eq. ) for all t ≥ 0.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Performance Analysis", "weight": 1.0} -->

We begin with the bound between the reference system state and desired state trajectory. This corresponds to the green tube in Fig. 3. The proofs for all the claims in this section are provided in Appendix B.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Performance Analysis", "weight": 1.0} -->

Lemma 5.1. Let all the assumptions hold and let ρ r be as defined in Eq.. If the conditions in (32a) -(32b) hold, then for any desired state trajectory x ⋆ (t) the state x r (t) of the reference system in satisfies and is uniformly ultimately bounded as where the ultimate bound is defined as Next, we compute the bounds between the reference system in Eq. and the L 1 closed-loop system (Eq. with Eq.).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Performance Analysis", "weight": 1.0} -->

Lemma 5.2. Suppose that the stated assumptions and the conditions in Eq. hold. Additionally, assume that the trajectory of the L 1 closed-loop system satisfies x (t) ∈ Ω(ρ, x ⋆ (t)), for all t ∈ [0, τ], for some τ > 0, with Ω(ρ, x ⋆ (t)) and ρ defined in Eq. and Eq., respectively. Then, We now use Lemmas 5.1-5.2 to state the main result of the paper.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Performance Analysis", "weight": 1.0} -->

Theorem 5.1. Suppose that the stated assumptions and conditions in Eq. hold. Consider a desired state trajectory x ⋆ (t) as in and the state of the L 1 closed-loop system defined via and. Then we have and is uniformly ultimately bounded as Here, the ultimate bound is defined as where the positive scalars ρ and ρ a are defined, and µ (ω, T) is defined in Lemma 5.1.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Discussion", "weight": 1.5} -->

A few critical comments are in order for the performance analysis. The main result in Theorem 5.1 provides uniform ultimate bounds. Let us first discuss the implication of the uniform bound ρ in Eq.. As per the definition in Eq., ρ = ρ r + ρ a. It is evident from the definition that ρ is lower bounded by the initial condition difference ‖ x ⋆ 0 -x 0 ‖ and the positive scalars α and α which are associated with the CCM M ( x ) of the nominal dynamics. Furthermore, as per the proof of Lemma 5.2, since ρ a ∝ 1 / √ Γ, the adaptation rate Γ can be increased to the maximum value allowable by the computation hardware to guarantee the smallest ρ a, and thus, the smallest uniform bound ρ. However, the fact remains that the uniform bound ρ guaranteed by the L 1 -controller for the tracking remains lower bounded by ‖ x ⋆ 0 -x 0 ‖. The only way this bound can be further reduced is if the underlying planner which provides the desired state-input pair ( x ⋆ ( t ), u ⋆ ( t )) can minimize ‖ x ⋆ 0 -x 0 ‖.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Discussion", "weight": 1.5} -->

Theorem 5.1 also provides the (uniform) ultimate bound via δ ( ω, T ) defined in Eq.. As already mentioned, ρ a ∝ 1 / √ Γ. Furthermore, from the definition of ζ 1 ( ω ) in Eq. (31a), it is evident that by choosing a large enough ω, there will always exist a known 0 < T < ∞ such that δ ( ω, t ) ≤ ¯ ρ, for all t ≥ T, for any chosen ¯ δ > 0. Therefore, we can always arbitrarily shrink the tube O ( ¯ δ ) by choosing appropriate bandwidth ω and rate of adaptation Γ. This feature of the CCM-based L 1 -controller is very advantageous, since, for example, this capability will allow the safe navigation of a robot through tight and cluttered environments. This improved performance, however, comes at the cost of reduced robustness. There exists a trade-off between performance and robustness that should be taken into consideration. As aforementioned, performance (radius of tubes around x ⋆ ( t ) ) depends on Γ and ω. The rate of adaptation Γ is obviously limited by the available computational hardware.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Discussion", "weight": 1.5} -->

More importantly, the role of the low-pass filter C ( s ) in the L 1 -control architecture (Fig. 2) is to decouple the control loop from the estimation loop. Thus, increasing the bandwidth ω of C ( s ) in order to get a tighter tube will lead to the u a ( t ) component of the L 1 -input to behave as a high-gain signal, thus possibly sacrificing desired robustness levels. Therefore, this trade-off must always be taken into account during the planning phase.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

We provide two illustrative examples. In the first example, we consider the non-feedback linearizable system from and synthesize the controller to ensure safe regulation around the equilibrium point. We also show the effect of uniform ultimate bounds discussed in the previous section, if the system were to start far away from the equilibrium. In the second example, we consider the system from and ensure safety in a motion planning context during trajectory tracking. In particular we show how altering the tube parameters affects the choice in the filter bandwidth and adaptation rate.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Non-feedback Linearizable Systems", "weight": 1.0} -->

Consider the system with the structure defined in Eq. and the system functions given by where the state x (t) = [x 1 (t) x 2 (t) x 3 (t)] ⊤. The dual metric W (x) = M (x) -1 satisfying the conditions in Eqs. (8a) to (8c) was found using the sum-of-squares programming toolbox SumOfSquares.jl, optimization software JuMP, and the optimization solver, as The metric satisfies a convergence rate λ = 1. 0 and is uniformly bounded in the set X = { y ∈ R 3 | ‖ y ‖ ∞ ≤ 0. 1 } with α = 5. 88 and α = 3. 85. Now, suppose that the system is experiencing sinusoidal disturbances of the form: h (t) = 0. 1 sin(2 t). We chose the initial condition of the system as x 0 = ⊤ × 10 -2 and the desired state as x ⋆ = ⊤.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Non-feedback Linearizable Systems", "weight": 1.0} -->

Incidentally, the desired state is also the equilibrium point of the system which means that the desired control is u ⋆ (t) ≡ 0. A pure CCM-based feedback strategy produces the oscillatory behavior, seen in Fig. 4a. A CCM-based L 1 -adaptive controller is designed in Fig. 4b for tube widths ϵ = 0. 01 and ρ a = 0. 01. The filter bandwidth and adaptation rate required to achieve this level of performance were chosen as ω = 50 and Γ = 5 × 10 6 respectively by satisfying the conditions in Eq.. Notice that the bounds are far more conservative than the actual behavior of the system. In fact, the error in tracking is uniformly bounded as ‖ x ‖ L ∞ < 0. 02. Additionally, notice that the uniform ultimate bounds of the reference system tube from Eq. and the actual system tube from Eq. shrink with time and are essentially 'forgetting' the initial conditions of the system.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Safe Tubes for Motion Planning", "weight": 1.0} -->

Consider the system with the structure defined in Eq. and the system functions given by where the state x (t) = [x 1 (t) x 2 (t)] ⊤. Since this particular system is feedback linearizable, it admits a constant (or flat) dual metric for all x ∈ R 2. The value of the dual metric and the associated convergence parameter is computed in and provided here for completeness: Figure 4: Comparison of controller performance between (a) pure CCM-based feedback, and a (b) CCM-based L 1 architecture. The green and orange shaded regions signify the induced Ω(ρ r, x ⋆) and Ω(ρ, x ⋆) tubes respectively. The dashed green and orange lines signify the uniform ultimate bounds µ (ω, T) and δ (ω, T) evaluated at every timestep.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Safe Tubes for Motion Planning", "weight": 1.0} -->

Similar to, we chose the initial condition of the system as x 0 = [3. 4 -2. 4] ⊤ and the target state as as x ⋆ = ⊤. The desired state and control trajectory pair was computed using the iterative LQR solver provided by with the parameters Q = 0. 5 I 2 and R = 1. 0. Suppose the system is affected by uncertainties of the form: h ( t, x ) = -2 sin(2 t ) -0. 1 ‖ x ( t ) ‖, consisting of both time and state dependent terms. Depending on the desired level of tracking performance or closeness to obstacles in the environment, the user will pick the tube parameters ϵ and ρ a as defined in Eq.. In Fig. 5, we illustrate the trade-offs between choosing a tighter ρ a (Fig. 5a) versus a tighter ϵ (Fig. 5c) for this system.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Safe Tubes for Motion Planning", "weight": 1.0} -->

In Fig. 6b, we observe the performance and robustness benefits of using CCM-based L 1 -adaptive control. Not only does the system track the desired trajectory closely, but also avoids colliding with obstacles (unlike in Fig. 6a) through an appropriate choice of tube parameters.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

We present a control methodology to enable safe and guaranteed feedback motion planning. The presented work relies on differential geometric contraction theory and L 1 -adaptive control. The proposed controller enables the apriori com- putation of uniform and ultimate-bounds which act as safety-certificates. These safety certificates induce 'tubes' which can be taken into account by any planner of choice. In this way, the safety of the system/robot is always guaranteed in the presence of model and environmental uncertainties. Furthermore, by using the control law's filter bandwidth and rate of adaptation as tuning knobs, the width of the safety tubes can be adjusted. Future research will deal with the incorporation of learning into the proposed control framework. This will lead to improved performance since the underlying planner will have access to improved model knowledge. More importantly, the controller proposed in this work will keep the learning process safe because of the apriori specified and guaranteed bounds during the transient phase. Further investigations will be undertaken to extend this framework to enable safe planning and control using a reduced-order model to enable fast planning.
