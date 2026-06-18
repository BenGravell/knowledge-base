<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Robust MPC via Min-Max Differential Inequalities

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper is concerned with tube-based model predictive control (MPC) for both linear and nonlinear, input-affine continuous-time dynamic systems that are affected by time-varying disturbances. We derive a min-max differential inequality describing the support function of positive robust forward invariant tubes, which can be used to construct a variety of tube-based model predictive controllers. These constructions are conservative, but computationally tractable and their complexity scales linearly with the length of the prediction horizon. In contrast to many existing tube-based MPC implementations, the proposed framework does not involve discretizing the control policy and, therefore, the conservatism of the predicted tube depends solely on the accuracy of the set parameterization. The proposed approach is then used to construct a robust MPC scheme based on tubes with ellipsoidal cross-sections. This ellipsoidal MPC scheme is based on solving an optimal control problem under linear matrix inequality constraints. We illustrate these results with the numerical case study of a spring-mass-damper system.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Model predictive control (MPC) refers to a class of feedback controllers, which proceed by solving, at each time step, an optimal control problem predicting the future behavior of a dynamic system on a finite, receding time-horizon, using the current state estimate as initial condition. The predicted optimal control trajectory is applied to the actual system until the next measurement becomes available, and the process is then repeated. The implementation of such controllers is based on a certainty-equivalence principle, whereby the future of the system is optimized as if neither external disturbances nor model mismatch were present, despite the fact that such disturbances and mismatch are the reason why feedback is needed in the first place.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main advantage of certainty-equivalence in MPC is that the resulting optimization problems can often be solved efficiently, in real time. This approach works well in many practical applications, and it often exhibits a certain robustness due to its inherent ability to reject disturbances. However, the constraints may become violated when large disturbances occur, since uncertainty is not taken into account in optimizing the predicted state trajectories. In such cases, robust MPC schemes can be used to mitigate these optimistic, certainty-equivalence-based predictions. Nonetheless, a rigorous formulation of robust MPC calls for the solution, at each sampling time, of an optimization problem whose decision variables are the future control policies, that is, functions mapping the state measurements onto the control actions. Such optimization problems are hard to solve in general, and brute-force approximations, e.g. based on scenario trees, can currently only be used for very short time-horizons. Because scenario-tree approaches scale exponentially with the length of the time-horizon, they may even be worse than robust dynamic programming approaches, which scale linearly with the length of the prediction horizon, yet exponentially with the state dimension.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Convex formulations of robust MPC have been derived for certain classes of problems, for instance when the dynamic system is jointly affine in the state, control and uncertainty and the feedback control law is itself affine in the disturbance. There, the number of the (matrix-valued) optimization variables scales quadratically with the length of the prediction horizon. The conservatism introduced by an affine parameterization of the control law is discussed. In this context, we also refer to, where real-time variants of robust MPC based on certain affine feedback laws are analyzed. Other convex formulations can be obtained by reformulating the semi-infinite constraints arising in robust MPC as linear matrix inequalities (LMIs). One such LMI reformulation for bounding the worst-case performance of linear systems under additive bounded uncertainty using constant state-feedback control laws was derived. Another approach was presented, where the future model variations are bounded by a family of polytopes expressed as LMI constraints.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Other state-of-the-art approaches in robust MPC adopt a set-theoretic perspective. These methods find their origins in viability theory or, more specifically, in set-theoretic methods for control. Robust MPC schemes based on these parametric set-propagation methods are also known collectively under the name tube-based MPC. There, the predicted trajectory is replaced by a robust forward invariant tube (RFIT) in the state-space, namely a tube that encloses all possible state trajectories under a given feedback control law, which is independent of the uncertainty realization. Tube-based approaches are typically analyzed under the assumption that exact state measurements are available, or that the equations of a parameterized state estimator, e.g. a linear filter, can be added to the system dynamics so that standard tube-based methods transfer readily.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

A parameterized tube-based MPC formulation for linear discrete-time systems with affine uncertainty has been proposed. This formulation allows for the simultaneous optimization of tubes and control laws that are nonlinear in the state measurements, resulting in a computationally tractable, linear programming (LP) formulation, whose decision variables and constraints scale quadratically with the prediction horizon. A generalization handling more general cost functions is considered, and a way of reducing the online complexity of this approach to linear complexity via offline computations is further presented. Tube-based methods have also been developed for linear systems with multiplicative uncertainty, for example by using polytopic tubes with quadratic cost, which leads to a quadratic programming (QP) formulation. Regarding nonlinear dynamics, a possible tube-based approach involves linearizing the system around a feasible, but suboptimal, trajectory and computing the tube by regarding the linearization errors as additional uncertainty. This idea was used in with polytopic tubes and affine feedback laws. A similar approach was developed by in the case of quadratic cost terms and ellipsoidal tubes.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

A tube-based approach for nonlinear continuous-time systems was proposed, where the feedback control laws are affinely parameterized and computed offline.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper presents a novel numerical approach for addressing tube-based MPC problems. In contrast to existing methods which parameterize the control law, our approach introduces a min-max differential inequality exploiting the properties on the boundary of RFITs. These min-max differential inequalities yield a non-trivial generalization of differential inequalities and provide sufficient conditions for a time-varying convex-set-valued function to be a RFIT for a class of continuous-time nonlinear control systems. We show that these (on the first view) rather abstract concepts can be used to derive practical implementations of tube-based MPC, which i) scale linearly with the length of the prediction horizon, and ii) do not rely on a particular parameterization of the control law. In principle, this approach can achieve arbitrary precision, insofar as the tubes are represented with sufficient accuracy.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rest of the paper is organized as follows. The problem formulation is described in Sect. 2. The main theoretical framework for characterizing RFITs for nonlinear input-affine systems is developed in Sect. 3 and its application to RFITs with ellipsoidal cross-sections is presented in Sect. 4. A practical implementation of tube-based MPC based on these results is discussed in Sect. 5 and illustrated with a numerical case study in Sect. 6. Finally, Sect. 7 concludes the paper.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The class of nonlinear control systems is affine in the control function $u$. Although the reasons for this assumption will become apparent later, it is important to note that it is not as restrictive as it may seem. In engineering practice, many physical systems possess such an affine control structure. Moreover, any nonlinear controlled system may be reformulated into the desired form under a stronger assumption on $u$; for instance, under the assumption that $u$ is at least locally Lipschitz continuous, an integrable control $v$ can be introduced such that $u$ is now regarded as a auxiliary state satisfying the differential equation ${\overset{˙}{u}{(t)}} = {v{(t)}}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The function $f$ is jointly continuous in $x,w$ and locally Lipschitz-continuous in $x$. Moreover, the function $G$ is continuously differentiable.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The derivation builds upon a recent result for computing enclosures of the reachable set of uncertain ODEs.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The following theorem is adapted from \[40, Theorem 3 & Remark 2\] for the class of controlled dynamic systems of interest.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The feedback control law given by Eqs. is not necessarily unique.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Remark 2", "weight": 1.0} -->

It is clear from Eq. in Appendix A, that the construction of the feedback control law relies heavily on the assumption of a control-affine structure for $g$ as well as the absence of uncertain inputs $w$ in the matrix-valued function $G$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Although heavily inspired by set-theoretic methods for the synthesis of model predictive controllers (see for an introduction), Theorem 2 also provides a constructive approach for nonlinear feedback control laws by exploiting properties at the boundaries of RFITs. This approach has not been exploited so far in the robust MPC literature.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Checking the sufficient conditions provided by Theorem 2 for an arbitrary convex set-valued function may prove computationally challenging in general. Nevertheless, the min-max differential inequality can be checked constructively for certain parameterizations of the tube cross-sections, as shown for ellipsoidal tubes next.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Ellipsoidal Robust Forward Invariant Tubes", "weight": 1.0} -->

This section derives computationally tractable conditions for checking whether a particular set-valued function $Y$ is a RFIT for the dynamic system. The focus is on tubes with ellipsoidal cross-sections, given by

<!-- chunk {"id": "body-0020", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

The functions $f$ and $G$ are twice continuously differentiable in all of their arguments.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

The following construction of ellipsoidal tubes is based on Theorem 2 and uses the same ideas as the construction of ellipsoidal bounds for uncertain ODEs based on Theorem 1; see, e.g.,. The control $u$, disturbance $w$ and state $x$ are decomposed into their nominal and perturbed components as

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

for a reference control ${u_{x}{(t)}} \in {\mathcal{E}{(q_{u},Q_{u})}}$. It follows that the perturbed state component $\delta_{x}$ satisfies the ODE

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

A number of remarks are in order. Since the central path $q_{x}$ corresponds to the nominal state, $u_{x}$ can be understood as the control input that would be applied if no uncertainty were affecting the system. Moreover, the decomposition of the right-hand side per is valid with any integrable functions $A$ and $B$ of suitable dimensions, as long as $n$ is chosen in an appropriate manner. For instance, if $A$ and $B$ are constructed through a first-order Taylor expansion, $n$ is given by the remainder function per Taylor's theorem.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

The present tube construction relies on the existence of an inner approximation of $\mathcal{E}{(q_{u},Q_{u})}$ centered at $u_{x}{(t)}$, as given by the following lemma.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Another feedback law can be obtained by extending the the domain of the Gauss map of an ellipsoid from ${{bd}\mathcal{E}}{(q,Q)}$ to ${\mathcal{E}{(q,Q)}} \smallsetminus {\{ q\}}$, and replacing the condition $\xi \in {{{bd}Y}{(t)}}$ with $\xi \neq q_{x}$ in the feedback law.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Depending on the problem at hand, the required nonlinear bounders in Assumptions 5 and 6 may be constructed either symbolically, as proposed, or numerically, e.g. using tools from interval analysis. A difficulty with the latter approach, however, is that operations performed using usual interval arithmetic are Lipschitz continuous, yet typically nonsmooth. This would impair the use of gradient-based methods for solving the optimization problems. Instead of applying interval analysis directly, Lemma 7 in Appendix D presents a way of constructing a smooth nonlinearity bounder for any twice continuously-differentiable function.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Robust Tube-Based MPC Based on Min-Max Differential Inequalities", "weight": 1.0} -->

This section discusses how the developments in Sect. 3 and Sect. 4 can be used in the context of robust MPC.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Robust Tube-Based MPC Based on Min-Max Differential Inequalities", "weight": 1.0} -->

Notice that is not a standard optimal control problem, as it embeds semi-infinite differential inequality constraints. However, discretizing this problem leads to a band-structured optimization problem whose complexity scales linearly with respect to the length of the time horizon.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Robust Tube-Based MPC Based on Min-Max Differential Inequalities", "weight": 1.0} -->

Observe that now yields a standard optimal control problem with linear matrix inequality (LMI) constraints. A solution to this problem provides a RFIT in the form ${Y{(\tau)}} = {\mathcal{E}{({q_{x}{(\tau)}},{Q_{x}{(\tau)}})}}$, from which an explicit feedback control law can be derived by applying Corollary 6.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Robust Tube-Based MPC Based on Min-Max Differential Inequalities", "weight": 1.0} -->

A practical implementation of this tube-based MPC scheme calls for the specification of the performance criterion $\ell$ and the feasibility set $F_{x}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Robust Tube-Based MPC Based on Min-Max Differential Inequalities", "weight": 1.0} -->

Regarding the feasible set, we may consider linear state constraints of the form

<!-- chunk {"id": "body-0032", "role": "body", "section": "Robust Tube-Based MPC Based on Min-Max Differential Inequalities", "weight": 1.0} -->

One of the main issues in robust MPC is ensuring recursive feasibility, namely the ability to find, for every possible initial state, a feasible state at every time along the closed-loop trajectory.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Robust Tube-Based MPC Based on Min-Max Differential Inequalities", "weight": 1.0} -->

where $Y_{ref} \subseteq F_{x}$ is a robust forward invariant set, i.e. a time-invariant RFIT. If $Y_{ref}$ satisfies Definition 1 on any time interval, then the sets $\left. \{{\mu{({t + T},{x{({t + T})}})}} \middle| {{x{({t + T})}} \in {Y{({t + T})}}}\} \right. \in U$ will remain non-empty by construction, and the MPC procedure discussed previously is indeed recursively feasible. This recursive feasibility condition is satisfied, if

<!-- chunk {"id": "body-0034", "role": "body", "section": "Robust Tube-Based MPC Based on Min-Max Differential Inequalities", "weight": 1.0} -->

The following section presents an application of the ellipsoidal approach of tube-based MPC on a numerical case-study.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Numerical Case Study", "weight": 1.0} -->

where $x_{1}$ and $x_{2}$ denote the displacement of the cart with respect to the equilibrium position $\lbrack m\rbrack$ and its velocity $\lbrack{m/s}\rbrack$, respectively; $M$ is the mass of the cart; ${k{(x)}}:={k_{0}{\exp{({- x_{1}})}}}$, the stiffness of the spring; and $h_{d}$, the damping factor. The values of the parameters are $M = {1{kg}}$, $k_{0} = {{0.33N}/m}$ and $h_{d} = {{1.1{Ns}}/m}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Numerical Case Study", "weight": 1.0} -->

The optimization problem in the tube-based MPC controller is based on and involves minimizing the functional

<!-- chunk {"id": "body-0037", "role": "body", "section": "Numerical Case Study", "weight": 1.0} -->

This cost corresponds to the generalized rotational inertia, except for the term $u_{x}{(t)}^{2}$ which can be interpreted as a control regularization. Moreover, a state constraint is enforced, so that ${\mathcal{E}{({q_{x}{(\tau)}},{Q_{x}{(\tau)}})}} \subseteq F_{x}:={\{ x\mid{x_{1} \leq 0.85}\}}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Numerical Case Study", "weight": 1.0} -->

Problem is solved numerically using the optimal control sofware ACADO,^11^1Since ACADO Toolkit does not support LMI constraints, our implementation substitutes the LMI constraints in with equivalent standard (nonlinear) state constraints using Schur complement techniques. using a piecewise constant control discretization on $40$ equidistant intervals. All the nonlinearity bounders are constructed using the technique in Appendix D.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Numerical Case Study", "weight": 1.0} -->

Fig. 1 compares the optimal ellipsoidal RFIT (grey area) with closed-loop trajectories for the nominal system (red line) and a system subject to a random disturbance taking values in $\mathcal{E}{(Q_{w})}$ (green line) for a certainty-equivalent MPC controller. The latter minimizes the tracking objective

<!-- chunk {"id": "body-0040", "role": "body", "section": "Numerical Case Study", "weight": 1.0} -->

and is implemented in ACADO using the same parameter values and state constraint as the robust tube-based MPC controller above. Notice that in the case where no uncertainty is present, the certainty-equivalent MPC controller performs as expected---although it touches the state constraint, it is able to steer the state to a neighbourhood of the origin without violating it. In contrast, when the system is subject to disturbances this controller fails in about $50\%$ of the uncertainty scenarios, after causing a constraint violation.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Numerical Case Study", "weight": 1.0} -->

The results of the tube-based MPC controller are shown in Fig. 2. As expected, the controller steers the nominal state (center of the RFIT) close to the origin at $t = 10$. In order to prevent violation of the path constraint against all the possible uncertainty scenarios, the controller rotates the ellipsoidal cross-sections of the RFIT quite drastically initially. Moreover, solving a conservative approximation of the min-max differential inequality appears to have a small adverse effect on the controller's performance in this simple case study.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conclusions", "weight": 1.0} -->

A novel approach to tube-based robust MPC has been proposed for control-affine nonlinear systems, which relies on a min-max differential inequality formulation in order to provide sufficient conditions for a time-varying convex set-valued function to be a RFIT. Unlike other robust MPC approaches, the procedure based on this differential inequality does not call for any particular parameterization of the feedback control law, while benefiting from having linear complexity with respect to the time horizon. Another benefit of the proposed approach is that a semi-explicit representation of a feedback control law may be obtained as a side-product of the RFIT propagation under mild conditions, namely when the RFIT cross-sections and the control sets are smooth with positive curvature. This property has been exploited to devise a practical implementation involving tubes with ellipsoidal cross-sections. This ellipsoidal tube-based MPC approach was tested for a spring-mass-damper system. In contrast to the certainty-equivalent model predictive controller it guarantees feasibility for all uncertainty scenarios.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusions", "weight": 1.0} -->

This paper is based upon work supported by the Engineering and Physical Sciences Research Council (EPSRC) under Grant EP/J006572/1. Financial support from Marie Curie Career Integration Grant -GA-2011-293953 and from the Centre of Process Systems Engineering (CPSE) of Imperial College is gratefully acknowledged. M.E.V. thanks CONACYT for doctoral scholarship. This research was supported by the EU via ERC-HIGHWIND (259 166), FP7-ITN-TEMPO (607 957), and H2020-ITN-AWESCO (642 682). Rien Quirynen holds a research fellowship by the FWO. Support by Freiburg University in form of a guest professorship of the last author at the Freiburg Institute for Advanced Studies (FRIAS) in 2014 is gratefully acknowledged.
