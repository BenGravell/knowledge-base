<!-- arxiv-full-text:v1 {"arxiv_id": "2312.15521", "source": "arxiv-pdf"} -->

## INTRODUCTION

Among optimization-based control schemes, model predictive control (MPC) has recently attracted increasing attention in both industry and academia. This technique enables feedback by repeatedly solving a numerical optimization problem at every time-step, each time taking into account the current (measured or estimated) state of the system as well as process and input constraints. Because of its effectiveness in practical applications, researchers have dedicated significant effort to the task of designing MPC controllers. For example, showed that the introduction of an appropriately selected terminal cost can ensure stability and feasibility of the closedloop. More recently, proposed a design to ensure that the MPC behaves like a linear controller around a specified operating point, with the goal of inheriting the well-known stability and robustness properties of linear controllers. The objective function of an MPC can also be chosen to incentivize learning of an unknown model, as proposed .

MPC design can be viewed as a policy optimization problem. Policy optimization is a well-known problem in reinforcement learning, where the goal is to obtain a control policy that minimizes some performance objective. In common applications, the policy is parameterized by problem parameters, states, or inputs, and gradient-based techniques are used to learn the optimal parameters. In the context of MPC, the design parameters are generally the cost and the constraints of Research supported by the Swiss National Science Foundation under NCCR Automation (grant agreement 51NF40 180545). R. Zuliani and J. Lygeros are with the Automatic Control Laboratory (IfA), ETH Z¨ urich, 8092 Z¨ urich, Switzerland { rzuliani,lygeros } @ethz.ch. E. C. Balta is with Inspire AG, 8005 Z¨ urich, Switzerland & with IfA efe.balta@inspire.ch. the problem. The challenge when considering model predictive control policies is that the MPC policy and resulting closedloop performance are generally not differentiable with respect to the parameters.

Recently, differentiable optimization provided a principled way to overcome the nondifferentiability issue. Specifically, proved that, under certain conditions, the optimizer of a quadratic program (QP) is indeed continuously differentiable with respect to design parameters appearing in the cost and the constraints, and that the gradient can be retrieved by applying the implicit function theorem to the KKT conditions of the QP. Since MPC problems are often formulated as QPs, this approach effectively allows for the differentiation of MPC policies. This discovery led to a plethora of applications of differentiable optimization in the realm of model predictive control. For example, considers the problem of imitation learning, where the tuning parameters are the cost and the model of the linear dynamics of an MPC problem. The idea of utilizing the KKT conditions to obtain derivatives of an optimization problem does not stop with quadratic programs. uses the same technique to compute gradients of a nonlinear optimal control problem, and uses this information to conduct online design of a robust model predictive controller. The goal in this case is to match the performance of a nominal controller. Similarly, introduces a predictive safety filter to ensure the safety of the closed-loop operation.

In a similar fashion, over the course of several papers -, Gros and Zanon used policy gradient methods to optimize the performance of nonlinear economic MPC. The main idea behind these works is to utilize a nonlinear MPC as a function approximator that can encode both the value and the action-value functions of a given problem. Their algorithm can produce MPC schemes that are stabilizing by construction and safe against additive disturbances (only in the case of affine systems). In particular, is the work that we believe is closest to ours, as it uses a linearizationbased procedure to avoid solving a nonconvex problem online. However, the authors focus on infinite horizon problems and do not provide a detailed treatment of the convergence of the optimization algorithm. Additionally, the parameter update is performed online (i.e. as the controller is deployed on the system).

These sophisticated differentiable optimization-based methods rely on the assumption that the optimizer of the MPC problem is continuously differentiable, since the gradient of the optimizer is obtained using the implicit function theorem.

It is well known, however, that this may not be the case, and that the optimizer may not be everywhere differentiable even for simple projection problems. The continuous differentiability assumption can be relaxed thanks to the recently developed concept of conservative Jacobians. Conservative Jacobians are set-valued operators that extend the concept of gradients to almost-everywhere differentiable functions. Similarly to other generalized Jacobians, they obey the chain rule of differentiation and can be used to create firstorder optimization schemes with convergence guarantees. However, unlike e.g. Clarke Jacobians, conservative Jacobians satisfy a nonsmooth implicit function theorem, which is essential in our setting to obtain the sensitivity of the solution maps of the MPC problems.

In this paper, we consider the problem of optimizing the closed-loop trajectory directly by backpropagation. Specifically, we compute the conservative Jacobian of the entire closed-loop trajectory with respect to variations of the design parameters by applying the chain rule to the conservative Jacobians of each MPC problem. We then apply a gradientbased scheme to update the value of the parameter and obtain improved closed-loop performance. This is fundamentally different than optimizing a single MPC step as it accounts for the effect of the receding horizon, where past decisions influece future ones.

The idea of using backpropagation to improve closed-loop performance of MPC first appeared in and. These studies focused on linear dynamics without state constraints and did not provide formal convergence guarantees. Our work makes the following contributions.

- 1) We utilize the backpropagation paradigm to solve a nonconvex closed-loop policy optimization problem where the policy is a parameterized MPC. The MPC utilizes a linearized version of the system dynamics to retain convexity. - 2) We provide conditions under which the closed-loop optimization problem is well posed by extending to the nonsmooth regime, and propose a gradient-based method with convergence guarantees (to a critical point). - 3) We allow the MPC to have cost and constraints that depend on the current state of the system and on the solution of the MPC problem in the previous time-steps, allowing, for example, the application of the real-time iteration. - 4) We propose a simple extension to deal with cases where the MPC scheme loses feasibility and provide conditions under which the closed-loop is guaranteed to converge to a safe operation.

To compute the conservative Jacobian of each optimization problem, we adapt and extend the techniques described in to a control theoretic context. Additionally, we derive problem-specific sufficient conditions under which the nonsmooth implicit function theorem in can be applied. We finally showcase our findings through simulation on a nonlinear problem.

Our algorithm can be applied under the assumption that the initial condition of the system is known (this is the case e.g. for iterative control tasks). The work presented in this paper has been recently extended in to uncertain systems subject to additive noise and with uncertain initial conditions.

The remainder of this paper is structured as follows. Section II describes the system dynamics, the control policy, and the policy optimization problem. Section III presents a short recap of conservative Jacobians, their main calculus rules, and a way to minimize such functions with a firstorder scheme. Section IV demonstrates how the conservative Jacobian of an MPC problem can be computed. Section V showcases our main algorithmic contribution by describing the backpropagation scheme and the main optimization algorithm. In Section VI we provide some useful extensions to our scheme, such as nonlinear dynamics and recovery from infeasibility. In Section VII we showcase our methods in simulation.

Notation: We use N, Z, R to denote the set of natural, integer, and real numbers, respectively. Z [ a,b ] is the set of integers z with a ≤ z ≤ b, for some a ≤ b. If C ⊂ R n is a convex set, we denote with P C the orthogonal projector to the set. Given a matrix A ∈ R n × m, we use r ( A,j ) to denote the j -th row of A (with j ∈ Z [1,n ] ). We use A ≻ 0 ( A ⪰ 0 ) to indicate that the symmetric matrix A is positive definite (positive semi-definite). We use A ∼ B to indicate that A is a function of B. ‖ · ‖ denotes the 2 -norm, and 〈 a, b 〉 = a ⊤ b is the Euclidean inner product.

## PROBLEM FORMULATION

## System dynamics and constraints

We consider a nonlinear time-invariant system where the state dynamics are given for each time-step t ∈ N by with f locally Lipschitz and ¯ x 0 ∈ R n x known. We assume that (¯ x t, ¯ u t) = 0 is an equilibrium. The state ¯ x t ∈ R n x and the input ¯ u t ∈ R n u are subject to polytopic constraints The control input ¯ u t is determined, at each time-step, by a parameterized control policy π: R n x × R n p → R n u The parameter vector p ∈ R n p parameterizes the control policy π at any state ¯ x t (we refer the reader to Subsection II-B for a concrete example of p in the context of MPC). We require p to satisfy the constraint p ∈ P, for some polytopic set P. Below, we restrict attention to MPC control policies.

The goal of this paper is to minimize an objective function involving p and the closed-loop state and input trajectory (¯ x, ¯ u):= (¯ x 0,..., ¯ x T +1, ¯ u 0,..., ¯ u T) for some finite time interval T ∈ N > 0, under the constraints. where C: R (T +2) n x × R (T +1) n u × R n p → R ≥ 0 specifies the performance objective. In, T should be chosen large enough to reach the desired equilibrium condition. Note that problem may be non-convex. In the following, for simplicity, we consider the case for some Q x ∈ R n x × n x with Q x ≻ 0. Our method can easily be extended to more general cost functions as described in Subsection VI-C.

## Model predictive control

In this paper, we restrict attention to MPC policies, where the control input is chosen as the solution of an optimal control problem. Specifically, after measuring the current state ¯ x t, we use the knowledge we possess about the system to optimize the future prediction of the state-input trajectories of the system. The predicted trajectories are denoted by x t:= (x 0 | t,..., x N | t) ∈ R (N +1) n x and u t:= (u 0 | t,..., u N -1 | t) ∈ R Nn u, where N ∈ N > 0, with N ≪ T, is the prediction horizon of the MPC. The initial state is chosen to be equal to the true state of the system, x 0 | t = ¯ x t and, to ensure convexity, we approximate the state dynamics as where A t, B t, and c t are known at runtime and should be chosen to accurately approximate the real dynamics in the vicinity of ¯ x t. We use S t:= (A t, B t, c t) to compactly represent the approximate dynamics at time t.

Each predicted state and input must satisfy the constraints. In addition, we generally impose different constraints on the predicted terminal state x N | t The objective function in the MPC is an approximation of the objective, given by where we added a terminal penalty ‖ x N | t ‖ 2 P and a penalty on the input, with P, R u ≻ 0, to ensure that the problem is strongly convex. The MPC problem that is solved online at each time-step is therefore given as follows.

At each time-step, after measuring ¯ x t and obtaining S t, we solve and choose π (¯ x t, p) = u 0 | t, where u 0 | t is the first entry of the input trajectory. We use MPC(¯ x t, S t, p) to denote the function that maps a parameter p, a nominal system S t, and an initial condition ¯ x t to a control input ¯ u t = u 0 | t, so that Here we treat the terminal cost and the input cost as tunable parameters, by letting p:= (P, R u). However, with the same framework, one can also choose p as any other element appearing in the cost or in the constraints of.

## A projected gradient-based framework

For the time being, we assume that S t ≡ S and drop it from the notation; we deal with the more complex case where S t is determined online in Subsection VI-A. Combining problem with the cost function and the controller, leads to the closed-loop control problem Note that we can remove the input constraints, as they are automatically satisfied if the inputs are obtained from the MPC. As shown in Appendix A, can be compactly rewritten as follows. where ¯ x (p) is the closed-loop state trajectory generated by the dynamics under controller for a given value of p. In the following section, we derive an efficient procedure to obtain generalized gradients of the function C with respect to p.

## CONSERVATIVE JACOBIANS

In the upcoming sections, we repeatedly deal with the problem of minimizing a nonsmooth, nonconvex function. These problems admit a simple solution strategy based on a descent algorithm. However, because of the nonsmoothness, we cannot always guarantee the existence of a gradient. Luckily, we can still devise descent algorithms if the function is almost everywhere differentiable thanks to the concept of conservative Jacobian. This section describes how conservative Jacobians generalize the notion of gradient to functions that are almost everywhere differentiable.

A path is an absolutely continuous function x: → R n which admits a derivative ˙ x for almost every t ∈, and for which x ( t ) -x is the Lebesgue integral of ˙ x between 0 and t for all t ∈.

Definition 1 ([16, Section 2]). A locally Lipschitz function ϕ: R n → R m admits J ϕ: R n ⇒ R m × n as a conservative Jacobian, if J ϕ is nonempty-valued, outer semicontinuous, locally bounded, and for all paths x: → R n and almost all t ∈ A locally Lipschitz function ϕ that admits a conservative Jacobian J ϕ is called path-differentiable.

If ϕ: R n × R p → R n is a function of two arguments p and x, we define J ϕ,x (˜ p, ˜ x ) = { V: [ U V ] ∈ J ϕ (˜ p, ˜ x ) } as the conservative Jacobian of ϕ with respect to x (and similarly for J ϕ,p (˜ p, ˜ x ) ). Note that J ϕ,x (˜ p, ˜ x ) and J ϕ,p (˜ p, ˜ x ) are obtained through the projections of the conservative Jacobian J ϕ onto the ˜ p and ˜ x coordinates.

Conservative Jacobians extend the concept of gradient to nonsmooth almost everywhere differentiable functions. Moreover, the conservative Jacobian J ϕ coincides with the gradient ∇ x ϕ ( x ) almost everywhere [14, Theorem 1]. If ϕ is convex, then the standard subdifferential ∂f is a conservative Jacobian for ϕ.

The most useful property that conservative Jacobians possess is that they admit the chain rule. This immediately implies the following composition rule.

Lemma 1 ([14, Lemma 6]). Given two path-differentiable functions ϕ: R n x → R n p, ψ: R n p → R n u, with conservative Jacobians J ϕ and J ψ, the function ϕ ◦ ψ is path-differentiable with conservative Jacobian J ϕ ◦ ψ ( x ) = J ϕ ( ψ ( x )) J ψ ( x ).

Unfortunately, not every locally Lipschitz function is pathdifferentiable. For this reason, we restrict our attention to definable functions.

Definition 2 ([22, Definitions 1.4 and 1.5]). A collection O = ( O n ) n ∈ N, where each O n contains subsets of R n, is an ominimal structure on ( R, +, · ) if

- 2) the elements of O 1 are precisely the finite unions of points and intervals; - 1) all semialgebraic subsets of R n belong to O n; - 3) O n is a boolean subalgebra of the powerset of R n; - 5) if A ∈ O n +1, then the set containing the elements of A projected onto their first n coordinates belongs to O n.

A subset of R n which belongs to O is said to be definable (in an o-minimal structure). A function ϕ: R n → R p is definable if its graph { ( x, v ): v = ϕ ( x ) } is definable.

Definable functions possess the following useful property.

Lemma 2 ([14, Proposition 2]). All locally Lipschitz definable functions are path-differentiable.

Another crucial property of locally Lipschitz definable functions is that obey a nonsmooth version of the implicit function theorem.

Lemma 3 ([23, Theorem 5]). Let ϕ: R n x × R n p → R n x be a locally Lipschitz definable function and let J ϕ be its conservative Jacobian. Suppose ϕ (˜ x, ˜ p) = 0 for some ˜ x ∈ R n x and ˜ p ∈ R n p. Assume that J ϕ is convex and that for every [U V] ∈ J ϕ (˜ x, ˜ p) the matrix U is invertible. Then there exists a neighborhood N (˜ x) × N (˜ p) of (˜ x, ˜ p) and a path differentiable definable function x: N (˜ p) → N (˜ x) such that for all p ∈ N (˜ p) it holds that ϕ (x (p), p) = 0, and the conservative Jacobian J x of x is given for all p ∈ N (˜ p) by Path-differentiable definable functions can be minimized using simple projected-gradient based scheme as outlined in Algorithm 1.

## Algorithm 1 Minimization of path-differentiable functions

1: while not converged do Where we used P P to denote the projector to the set P. Typically, we stop the algorithm e.g. when ‖ p k -p k -1 ‖ < tol for some positive tolerance tol, or after exceeding a certain number of iterations. The following results demonstrates that, under certain conditions on the step-size { α k } k ∈ N, Algorithm 1 is guaranteed to converge to a critical point of ϕ.

Lemma 4 ([15, Theorem 6.2]). Assume that ϕ is pathdifferentiable and definable, that P is a polytopic set, that the stepsizes { α k } k ∈ N ⊂ R > 0 satisfy and that sup k ‖ x k ‖ < ∞. Then x k as obtained via Algorithm 1 converges to a critical point of ϕ, i.e., a point ˜ x for which 0 ∈ J ϕ (˜ x).

The assumption on the boundedness of the conservative Jacobians is not restrictive in practice and it is generally satisfied under a suitable stepsize choice, or if P is a bounded set. Readers should refer to for more details.

## DIFFERENTIATING THE MPC POLICY

In this section, we rewrite in a more convenient form and then show that, under certain conditions, the map MPC(¯ x t, p ) admits a conservative Jacobian, leading to a descent algorithm .

## Writing the MPC problem as a QP

Problem can be reformulated as a quadratic program in standard form (see e.g. [24, Section III]) where ¯ p:= (¯ x t, p). We denote with n in and n eq the number of inequality and equality constraints, respectively. Note that the parameter p can potentially affect all terms in the cost and in the constraints, whereas the initial condition ¯ x t can only affect the linear part of the cost and the affine term in the constraints.

To simplify the computation of the conservative Jacobian, we operate on the Lagrange dual problem associated to.

In this case, the constraints are parameter-independent, as ¯ p only affects the cost function of the problem. To ensure that the dual problem has a unique solution for every value of ¯ p, we impose the following assumption.

Assumption 1. For all parameter vectors ¯ p in some polytopic set Y, the matrix Q ( p ) in is positive definite, problem is feasible and satisfies the linear independence constraint qualification (LICQ).

Recall that satisfies the LICQ if given an optimizer y (¯ p), the rows of G associated with the active inequality constraints and the rows of F are linearly independent. Note that the LICQ assumption holds if, for example, the constraints on x k | t and u k | t in are simple box constraints for some x min, x max ∈ R n x, x min < x max, and u min, u max ∈ R n u, u min < u max.

The feasibility condition in Assumption 1 can be restrictive in practical scenarios. We propose a simple extension of our method that can deal with losses of feasibility in Subsection VI-D.

Under Assumption 1, we can obtain the Lagrange dual of following the procedure outlined in Appendix B.

Note that in the parameters p and ¯ x t only affect the quadratic part H and the linear part h of the cost, whereas the matrix E in the constraints is parameter-independent.

The primal solution y (¯ p ) can be obtained from the dual solution z (¯ p ) = ( λ (¯ p ), µ (¯ p )) as

## Writing the dual as fixed point condition

To obtain the conservative Jacobian J z of the dual optimizer, we follow the procedure proposed: we write the optimality conditions of as a fixed point equation F (z, ¯ p) = 0, obtain the conservative Jacobian of F with respect to z and ¯ p, and apply the implicit function theorem in Lemma 3. Since is a quadratic program, a necessary and sufficient condition for optimality [25, Theorem 3.67] is where N C is the normal cone mapping of C:= { z ∈ R n z: Ez ≥ 0 }, with n z = n in + n eq [25, Example 3.5]. Leveraging [26, Corollary 27.3], we have that is equivalent to where γ ∈ R > 0 is a positive scalar and P C: R n z → C is the projection operator to the set C. To ensure the existence of the conservative Jacobian of F, we impose the following assumption.

Assumption 2. The maps Q ( p ), q (¯ p ), F ( p ), φ (¯ p ), G ( p ), g (¯ p ) are locally Lipschitz and definable.

Assumption 2 is not restrictive in practice as definable functions include most common functions of interest in the field of optimization and control. For example, all semialgebraic functions, real analytic functions (restricted to a definable domain), and any product, sum, inversion, and composition of definable functions are definable. Moreover, derivatives of definable functions are definable [22, Lemma 6.1], meaning that if F and φ are obtained by linearizing f (which is definable by Assumption 3) using the dynamic linearization technique outlined in Subsection VI-A, the definability assumption is immediately satisfied.

Lemma 5. Under Assumptions 1 and 2, F is locally Lipschitz definable.

Proof. The projector P C is given by where P R ≥ 0: R → R ≥ 0 is the one-dimensional projector to the set of non-negative real numbers The function P R ≥ 0 is locally Lipschitz and piecewise linear, therefore definable. We conclude that P C is locally Lipschitz definable.

Next, the function z ↦→ z -γ ( H (¯ p ) z + h (¯ p )) is linear in z, and therefore both definable and Lipschitz. Moreover, thanks to Assumption 2, we have that both H and h are locally Lipschitz definable in ¯ p since they are constructed as products or sums of locally Lipschitz definable functions (as shown in Appendix B), and these operations preserve both local Lipschitz continuity and definability [27, Corollary 2.9]. Note that Q -1 ( p ) is also locally Lipschitz definable since each of its entries is the ratio of two polynomial functions (i.e. semialgebraic) of the entries of Q. We conclude that ¯ p ↦→ z -γ ( H (¯ p ) z + h (¯ p )) is both locally Lipschitz definable in ¯ p.

We conclude that F is locally Lipschitz definable since it is the composition of locally Lipschitz definable functions.

The conservative Jacobian of the dual variable z can now be readily obtained by applying the implicit function theorem in Lemma 3 to the map F.

Theorem 1. Under Assumptions 1 and 2, the optimizer z (¯ p) of is unique and locally Lipschitz definable for any ¯ p ∈ Y. Its conservative Jacobian J z (¯ p) contains elements of the form -U -1 V, where Proof. See Appendix C.

Remark 1. The proof in Appendix C also establishes that we can always choose J P C of the form justifying our choice of working with the dual problem instead of the primal.

The conservative Jacobian J y (¯ p) of the primal optimizer y (¯ p) can then easily be retrieved from J z (¯ p) using. For simplicity, define Corollary 1. Under Assumptions 1 and 2, the optimizer y (¯ p) of is unique and locally Lipschitz definable for any ¯ p ∈ Y. Its conservative Jacobian J y (¯ p) contains elements of the form Proof. Follows immediately from the fact that composition preserves the local Lipschitz continuity and definability, and by applying the chain rule of differentiation to.

The algorithm below summarizes a procedure for computing the conservative Jacobians J MPC, ¯ x t and J MPC,p.

## Algorithm 2 Computing J MPC (¯ p )

## Input: ¯ p

- 1: Solve and get dual optimizers z = (λ, µ). - 5: return J MPC (¯ p) (extracted from J y (¯ p)).

Notice that J MPC, ¯ x t and J MPC,p are contained in J y, and we can therefore retrieve them by selecting the appropriate entries in J y (¯ x t, p ).

The procedure outlined so far allows for the computation of conservative Jacobians of quadratic programs. Extending this method to more general classes of problems is a promising direction for future research. One way to proceed could be to apply the implicit function theorem to the optimality conditions of the nonlinear problem, as done . In this case, however, it's unclear whether the resulting Jacobian will be conservative.

## CLOSED-LOOP OPTIMIZATION SCHEME

## Backpropagation

Next, we develop a modular mechanism, based on backpropagation, to obtain the conservative Jacobian of the entire closed-loop trajectory ¯ x using the individual conservative Jacobians of each optimization problem.

In machine learning, backpropagation is often used to efficiently construct gradients with respect to design parameters of algorithms involving several successive steps. The idea is to compute the gradients of each step and combine them using the chain rule, eliminating redundant calculations and improving efficiency.

In our case, the closed-loop dynamics can be expressed as a recursive equation where every state ¯ x t +1 depends solely on its predecessor ¯ x t, and the design parameters p. To be able to propagate the conservative Jacobians through the dynamics of the system, we require f to be path-differentiable.

Assumption 3. The function f is locally Lipschitz definable.

Under Assumption 3, we can compute the conservative Jacobian J ¯ x t +1 (p) of the state ¯ x t +1 with respect to the design parameters p recursively as follows: Note that J ¯ x t +1 (p) depends on J ¯ x t (p), and since ¯ x 0 is given, we have J ¯ x 0 (p) = 0. As a result, we can easily construct an algorithm that computes the conservative Jacobian of the closed-loop trajectory ¯ x for a given value of p iteratively. The algorithm, summarized in Algorithm 3, can be implemented online, as the closed-loop is being simulated and the values of ¯ x t are being measured. Note that the simulation needs to span the entire horizon T.

## Algorithm 3 Backpropagation

- 2: Solve and set ¯ u t = MPC(¯ x t, p). - 3: Get next state ¯ x t +1 = f (¯ x t, ¯ u t). - 4: Compute J MPC (¯ x 0, p) using Algorithm 2.

Proposition 1. Under Assumptions 1, 2 and 3, the closedloop trajectory ¯ x is locally Lipschitz definable in p, with conservative Jacobian J ¯ x ( p ) as given by Algorithm 3.

Proof. The closed-loop ¯ x is locally Lipschitz definable since it is given by the composition of locally Lipschitz definable functions. We now prove by induction that Algorithm 3 produces J ¯ x ( p ). First, J ¯ x 0 ( p ) = 0 since ¯ x 0 is fixed a priori. Next, suppose J ¯ x t ( p ) has been computed correctly by the algorithm. The correctness of J ¯ x t +1 ( p ) follows immediately and Lemma 1.

## Optimization algorithm

Once the conservative Jacobian is available, we can utilize it to update the parameter p with a gradient-based scheme. To guarantee convergence, it suffices to meet the conditions of Algorithm 1. We, therefore, choose the following update scheme for any J = J 1 J 2 with where ¯ x k = ¯ x (p k), and α k satisfies the conditions. Algorithm 4 combines all the steps described so far.

## Algorithm 4 Closed-loop optimization scheme

1: while not converged do As long as the map MPC(¯ p) is well-defined, i.e., problem admits a feasible solution throughout the entirety of the execution of Algorithm 4, we have the following.

Theorem 2. Suppose Assumptions 1, 2 and 3 hold, and that is feasible for all ¯ x t and p k as setup in Algorithm 4. Suppose α k satisfies and sup k ‖ p k ‖ < ∞. Then p k converges to a critical point of problem.

Proof. Since J ¯ x (p k) is the conservative Jacobian of ¯ x with respect to the design parameter p thanks to Proposition 1, we have from Lemma 4 that the iterates p k are guaranteed to converge to a critical point ¯ p of the problem Moreover, since the constraints H (p) ≤ 0 are automatically satisfied if MPC(¯ p) is feasible throughout the entire runtime of Algorithm 4, we conclude that the critical point ¯ p of is also a critical point of, which is equivalent to. This concludes the proof.

The condition sup k ‖ p k ‖ < ∞ holds trivially if P is compact. Otherwise, one can augment the cost function with a regularizer that ensures boundedness of the iterates, as discussed in [15, Section 6.1].

Remark 2. Since the horizon of the optimization problem is finite, we do consider the stability of the closed-loop dynamics. Indeed, our method produces MPC schemes that are optimized for a specific finite-horizon task. To obtain a controller that stabilizes, a simple solution would be to use the MPC controller with parameter p ∗ for t ∈ Z [0,T ], and switch to a stabilizing state-feedback controller for t ≥ T (e.g., an LQR). Note that if T is chosen appropriately large, the closed-loop state ¯ x T should be in a neighborhood of the origin, and a simple LQR controller (obtained by linearizing the dynamics at the origin if the system is nonlinear) should suffice.

## EXTENSIONS

## Choosing S t by linearization

The accuracy of the approximate model S t significantly impacts the control performance. To improve precision, we can allow the nominal dynamics to vary at different time-steps within the same MPC problem and construct S t = { A k | t, B k | t, c k | t } N -1 k =0 by linearizing f along the state-input trajectory (x t -1, u t -1) with u N | t -1 = u N -1 | t -1. Alternatively, we can use ¯ x t in place of x 1 | t -1. If the state-input trajectory (x t, u t) predicted by the MPC at time t does not deviate significantly from (¯ x t, u 1 | t -1), then the linearized dynamics are expected to be a good approximation of the true system dynamics.

Since S t now depends on the entire solution y t -1:= (x t -1, u t -1) of the MPC problem at time t -1, and possibly also on ¯ x t, the computation of J ¯ x t +1 (p) in Algorithm 3 needs to be modified: where we used MPC(¯ x t, y t -1, p) instead of MPC(¯ x t, p) to emphasize the dependency on y t -1. The term J y t -1 (p) can be constructed using a simple backpropagation rule where y t -1 = QP(¯ x t -1, y t -2, p). The modified backpropagation algorithm is given in Algorithm 5. Note that we can compute J MPC using Algorithm 2 by setting ¯ p:= (¯ x t, y t -1, p).

Before beginning the simulation of the system, we need to choose the linearization trajectory y -1 for time-step t = 0, either heuristically, or by letting y -1 be part of p, thus allowing the optimization process to select the value of y -1 that yields the best closed-loop performance.

Remark 3. The linearization strategy of this section can be replaced with simpler strategies like choosing a fixed A and B throughout the entire MPC horizon or choosing A k | t ≡ A t = ∂f ( x,u ) ∂x | x = x t, u = u 1 | t -1 and similarly for B and c. This however may negatively impact the performance of the MPC controller, especially when the system dynamics are highly nonlinear. The choice of S t is therefore a trade-off between computational complexity and control performance. In practice, we observed that the linearization technique of this section has an overall satisfactory performance (compare Section VII).

## State-dependent cost and constraints

The closed-loop performance of receding-horizon MPC schemes can be greatly improved by allowing certain elements in the MPC problem to be adapted online based on the state of the system. For example, in the terminal cost and constraints are constructed online as functions of the state ¯ x t. This choice is shown to enlarge the region of attraction of the scheme.

## Algorithm 5 Backpropagation with linearization

- 2: Solve and set ¯ u t = MPC(¯ x t, y t -1, p). - 3: Get next state ¯ x t +1 = f (¯ x t, ¯ u t). - 4: Compute J MPC (¯ x t, y t -1, p) using Algorithm 2.

Our backpropagation framework allows the incorporation of state-dependent elements in the MPC problem by letting H x,N, h x,N, and P be functions of both p and ¯ x t. Since both ¯ x t and p are known at runtime, the MPC problem solved online is a QP in the form which differs from only because Q, F, and G now depend on both ¯ x t and p. As a result, we can perform closedloop optimization using the same algorithmic procedure as in Algorithm 4 without any modification, exception made for the symbolic expression of Q, F, and G which depend on ¯ p = (¯ x t, p) instead of only p.

Remark 4. The same procedure can be applied to the case where H x, H u, h x, h u, Q x and R u depend on ¯ x t. Moreover, one can easily incorporate cost matrices Q x and R u that also depend on y t -1, for example by linearizing the possibly nonlinear cost function C along the trajectory y t -1 and adding sufficient regularization to ensure the positive definiteness of both Q x and R u. We leave such cases for future work and emphasize that our framework is flexible to tune any component of the underlying MPC problem.

## Non-convex cost

Our framework easily extends to scenarios where the quadratic cost in is replaced with more sophisticated costs that can possibly involve other terms in addition to ¯ x. Consider, for example, problem with the cost C (¯ x, y, z, p), where y:= (y 0,..., y T) and z = (z 0,..., z T) are the primaldual optimizers of at all time-steps. Through Algorithm 5 we can include any of the optimization variables in the cost and still manage to efficiently compute the gradient of the objective by storing the conservative Jacobians J y t (p) and J z t (p) and then applying the Leibniz rule The conservative Jacobians J y and J z are already available as a by-product of Algorithm 2.

To ensure that Lemma 5 is still applicable, we only require C to be path-differentiable jointly in its arguments. Under this condition, the results of Theorem 2 still hold. Note that the class of path-differentiable functions is quite large, and comprises a large selection of non-convex functions.

## Dealing with infeasibility

So far, we have not considered the situation where becomes infeasible. This can happen frequently in practice since the gradient-based optimization scheme modifies the behavior of the MPC map without guaranteeing recursive feasibility. There is, however, a simple procedure that can be used to recover from infeasible scenarios. The modification comprises two steps: first we modify to ensure its feasibility, then we change the cost function C to ensure that p minimizes constraint violations.

To ensure that is always feasible, we introduce the slack variables ϵ t and soften the state constraints (the input constraints can always be satisfied) To avoid unnecessary constraint violation, we penalize nonzero values of ϵ t with the penalty function P MPC ϵ (ϵ) = c 1 ‖ ϵ ‖ 2 2 + c 2 ‖ ϵ ‖ 1, with c 1, c 2 > 0. If c 2 is large enough, one can prove that P MPC ϵ is an exact penalty function.

Lemma 6 ([29, Theorem 1]). Problem has the same solution as as long as admits a solution and c 2 > ‖ λ ‖ ∞, where λ are the multipliers associated to the inequality constraints affecting the state .

To ensure that, if possible, p is chosen to have no constraint violations in closed-loop, we introduce a penalty function in the objective of where ϵ:= (ϵ 0,..., ϵ T -1) and P ϵ (ϵ) = c 3 ‖ ϵ ‖ 1 for some c 3 > 0. The introduction of P ϵ should ensure that the solution of satisfies ϵ t = 0 for all t ∈ Z [0,T -1]. If this is the case, the optimizers x t and u t of each MPC problem satisfy the nominal constraints, thus ensuring that ¯ x and ¯ u do too.

With some reformulation, we can equivalently write as where C and ϵ are locally Lipschitz definable functions of p, and ϵ is the function that maps p to the value of ϵ that solves. Since closed-loop constraint satisfaction is equivalent to ϵ (p) = 0, the goal is to obtain a solution of Under certain conditions on P ϵ and on the nature of the minimizers of, we can prove that and are equivalent, in which case P ϵ is an exact penalty function. For this, we need the following definition.

Definition 3. Let p ∗ be such that ϵ (p ∗) = 0. Problem is calm at p ∗ if there exists some ¯ α ≥ 0 and some ϵ > 0 such that for all (p, u) with ‖ p -p ∗ ‖ ≤ ϵ and ϵ (p) = u, we have Calmness is a rather weak regularity condition that is verified in many situations. In finite dimensions, it holds for a dense subset of the perturbations [30, Proposition 2.1]. For calm minimizers of, we have the following.

Proposition 2 ([30, Theorem 2.1]). The set of local minima p ∗ of for which is calm at p ∗ coincide with the local minima of provided that the penalty parameter c 3 is chosen at least as large as the calmness modulus.

Generally, it may be challenging to obtain an accurate estimate of the calmness module. Nevertheless, for practical purposes, a large enough value of c 3 typically produces the desired effect ϵ = 0.

With this in mind, we can use Algorithm 4 replacing C with C + P ϵ and the MPC problem . If c 2 and c 3 are sufficiently large, and under the calmness assumption of Proposition 2, we can guarantee convergence to a local minimizer of the problem with constraints. Combining Lemma 6 and Proposition 2 yields the following.

Theorem 3. Let Assumptions 1, 2 and 3 hold, and let p ∗ be the optimal parameter obtained with Algorithm 3 applied to. If is calm at p ∗ and c 2 and c 3 are sufficiently large, then the MPC controller given in (without constraint relaxation) is recursively feasible for the dynamics, and the closedloop constraints are satisfied for all t ∈ Z [0,T ].

## SIMULATION EXAMPLE

All simulations are done in CasADi with the active set solver DAQP on a laptop with 32 GB of RAM and an Intel(R) Core (TM) processor i7-1165G7 @ 2.80GHz. The code is available and open source 1. Average computation times for each BP-MPC iterations (including the simulation of T time-steps and the computation of the conservative Jacobians) are 499.130 ms and 205.486 ms for the examples in Subsections VII-A and VII-B, respectively.

## Input-constrained example

We begin by deploying our optimization scheme to solve problem for the continuous time pendulum on cart system of where x and ˙ x are the position and velocity of the cart, respectively, and φ and ˙ φ are the angular position and velocity of the pendulum, respectively. The goal is to steer the system to the upright equilibrium position ¯ x = starting from ¯ x 0 = (0, 0, -π, 0) (i.e., pendulum down). For the time being, we only consider the input constraints ¯ u (t) ∈ and postpone state constraints to Subsection VII-B. We discretize the nonlinear ODE using Runge-Kutta 4 with a sampling time of 0. 015 seconds. The closed-loop objective is to minimize with Q x = diag. The MPC utilizes the same input constraints and state cost matrix Q x, and an input and terminal cost parameterized as We set p = (p 0,..., p 10), initialized with p 0 = 0 and P equal to the solution of the discrete-time Algebraic Riccati equation (computed on the linearized dynamics at the origin). Note that this choice of P and R ensures that P ≻ 0, and R ≻ 0 for all p. We use the linearization strategy of Subsection VI-A to obtain linear dynamics. We choose a short horizon of N = 11. In Algorithm 4 we set which fullfills the assumptions in Theorem 2 for any η ∈ (0. 5, 1] and ρ > 0. Through manual tuning, we chose ρ = 5 · 10 -4 and η = 0. 51.

Figure 1 shows the evolution of the relative difference between the closed-loop cost attained by applying Algorithm 4 and the globally optimal cost for problem for different numbers of iterations. Here the global optimum is obtained by solving directly using the nonlinear solver IPOPT. Note that this coincides with the solution of a nonlinear MPC problem with no terminal cost and a control horizon greater than or equal to 170 time steps, after which the system reaches the origin. The suboptimality is negligible (less than 0. 01% ) after only a few iterations. The figure additionally shows that our method achieves a lower cost compared to an MPC with R u = 10 -6 and a fixed terminal cost derived from solving the Discrete Time Algebraic Riccati Equation (DARE), where A and B are chosen as the linearized dynamics at the origin.

Figure 2 shows the closed-loop trajectories of the horizontal and angular position, and of the input under different control policies. We note that the trajectory obtained after 10000 iterations of Algorithm 4 effectively coincides with the optimal one, whereas the one obtained by using p 0 in differs For this simulation example, the linearization procedure of Subsection VI-A is crucial. Using a fixed linear model, obtained by linearizing the dynamics at the origin, results in an MPC controller that is not able to stabilize the system given the same horizon N = 11. This highlights the importance of choosing a sufficiently accurate linear prediction model for the MPC problem. In our experience, the linearization procedure outlined in Subsection VI-A suffices in most cases.

1 At the link substantially.

In Figure 3, we compare the performance of our scheme against a nonlinear MPC controller with different control horizons. The NMPC is implemented using the SQP method offered by Acados with the solver HPIPM. At every time-step, we warm-start the next NMPC using the solution obtained in the previous time-step. At the initial time-step, the warm start trajectory is obtained by solving the NMPC problem with horizon T (similar results can be obtained with shorter horizons). The initial warm starting, which we decided to add to make the comparison with our method more fair, is crucial to ensure fast convergence of the solver and to avoid numerical failures. As the horizon N grows, the suboptimality of the nonlinear controller decreases; however, it never reaches the performance of our controller, which utilizes a fixed horizon N = 11. Coincidentally, the worstcase computation time needed to solve the nonlinear MPC problem grows significantly.

Tuning the nonlinear MPC can significantly improve its performance. This is showcased in Figure 4, where we added the terminal cost x ⊤ N | t Px N | t (with P chosen as the solution of the Algebraic Riccati Equation for the linearized dynamics at the origin) to the nonlinear MPC. In this case, the NMPC is able to outperform our scheme for horizons N ≥ 25. For N = 25, however, the NMPC requires about 10 times more computation time in the worst-case scenario compared to the worst-case scenario of our scheme. If the horizon of the NMPC is chosen equal to ours (i.e., N = 11 ), then our scheme attains a cost that is 10 5 smaller compared to the NMPC.

One might argue that BP-MPC is unnecessary when the system dynamics are known and noise-free. The optimal performance can more efficiently be obtained by solving a nonlinear trajectory optimization problem with a horizon larger than 170 and applying the optimal input u t\_opt t open loop. This choice, however, is very fragile against process noise. Figure 5 shows the closed-loop cost of our scheme (applied in receding horizon) and that of u t\_opt t (applied in open loop), assuming that the dynamics are affected by a stochastic additive noise sampled uniformly from the set { 0 }× [0, w max ] × [0, w max ] ×{ 0 }, for different values of w max. Our scheme compensates for the noise, maintaining good performance.

Figure 6 shows the percentage suboptimality (i.e., the ratio between the closed-loop cost attained by the controller, and the best achievable cost) of our controller (blue line) for 1000 different initial conditions sampled from the set ¯ x 0 +[ ω 1, ω 2, 0, 0], with ω 1, ω 2 sampled uniformly from the interval [ -0. 02, 0. 02]. We can see that the tuned MPC (with horizon 11 ) performs well for about 90% of all samples, but achieves a much larger cost in about 10% of the cases. In addition, our scheme outperforms a nonlinear MPC with horizon N = 19 (with terminal cost set to the solution of the DARE), and outperforms a NMPC with N = 20 in about 90% of the cases. Note however that a NMPC with horizon N = 21 performs strictly better than our tuned controller. This indicates that the optimized MPC may not generalize well to unseen initial conditions. The question of how to robustify the tuning algorithm is a promising direction for future work.

Fig. 1. Suboptimality between closed-loop cost and optimal cost.

Fig. 2. Comparison of closed-loop state and input trajectories.

## Input and state-constrained example

In this section we consider the same dynamics, discretized using RK4 with a sampling time of 0. 05, but this time with initial condition x = ( -3, 0, 0, 0) (i.e., pendulum up, cart at -3 meters from the origin). In this case, the goal is to steer the system to the origin while mainting the pendulum close to the upright position as not to exceed the constraints ˙ x ( t ) ∈ [ -0. 6, 0. 6], φ ( t ) ∈ [ -0. 1, 0. 1] and ˙ φ ( t ) ∈ [ -0. 6, 0. 6]. The input constraints are u ( t ) ∈ [ -0. 9, 0. 9]. We choose the MPC horizon as N = 6, with T = 120, and closed-loop cost Q x = diag(1, 0. 01, 1, 0. 1), R u = 0. 01. Moreover, we use the same choice of p as in Subsection VII-A with the same initialization.

Fig. 3. Comparison of the relative suboptimality and the worst-case computation times (dashed lines) of a nonlinear MPC with different horizon lengths, and our scheme with fixed horizon N = 11 (solid lines).

Fig. 4. Comparison of the relative suboptimality and the worst-case computation times of a nonlinear MPC with terminal cost and different horizon lengths (dashed lines), and our scheme with fixed horizon N = 11 (solid lines).

Fig. 5. Closed-loop median performance (over 1000 random noise samples) of nonlinear trajectory optimization (feedforward) and BP-MPC (receding horizon) with different noise magnitudes.

This new control task is very challenging from a safety perspective, as the controller needs to reduce the aggressiveness of the control action to avoid violating the tight constraints. This is similar to the problem of controlling the position of a segway without falling. We therefore utilize the softconstrained MPC described in with penalty parameters c 1 = 15 and c 2 = 15, and apply the optimization scheme with the objective function , with P ϵ ( ϵ ) = 60 1 ⊤ ϵ + 40 ϵ ⊤ ϵ (where ϵ:= ( ϵ 1, ϵ 2,..., ϵ T ) contains the slack variables of all the optimization problems, each of which spans N timesteps, and 1 is the vector of all ones). The results can be seen in Figure 7, where the constraints are satisfied and ϵ = 0. The effect of a penalty on the constraint violation induces the optimization algorithm to favor values of p that maintain small constraint violations. This does not happen if c 3 = c 4 = 0, as evidenced by Figure 7 (note that in this case we still penalize the slacks within each MPC problem, i.e., c 1 = c 2 = 15 ). The closed-loop cost and constraint violations of the BP-MPC and the MPC with fixed terminal cost (equal to the solution of the DARE) are summarized in Table I.

Fig. 6. Relative suboptimality of the tuned MPC scheme (with horizon 11 ) and nonlinear MPC schemes with variable horizon for a set of 1000 initial conditions.

Fig. 7. Comparison of closed-loop state trajectories x ( t ), ˙ x ( t ), and ˙ φ ( t ) under different control policies.

TABLE I. Comparison of closed-loop cost and constraint violation.

| | Closed-loop cost | Constraint violation |

## Comparison with

For completeness, we compare our method with on the example presented in Subsection VII-A. When using the method , we use the same cost parameterization we used with our method, but employ a fully nonlinear MPC. Using open source code 2, we test both a quasi-Newton and a gradient-based update. However, despite some manual tuning of the stepsizes, both methods fail to achieve a performance comparable to the one of our method (the best observed cost is 37404.04, compared to 17147.9 of our method).

The situation changes if we consider the example in Subsection VII-B. To make the comparison fair, we use a fixed linear prediction model for both methods (obtained by linearizing the dynamics at the origin). In this case, the method of converges rapidly to the optimal performance (same as our method) in a smaller number of iterations than our method. This is due to the fundamental difference in the two update schemes: is using a quasi-Newton scheme and it is performing one update every time-step within each iteration, requiring 1 iteration to converge (hence 120 parameter updates are necessary to reach optimal performance); our scheme, on the other hand, uses a gradient-based scheme and only updates once per iteration, requiring 3 iterations in total.

This comparison empirically suggests that, in scenarios where the dynamics are highly nonlinear (e.g., the example of Subsection VII-A), our method can outperform the method of, achieving optimal performance despite using a simpler MPC architecture. However, in scenarios where the dynamics are linear or mildly nonlinear (e.g., the example of Subsection VII-B), the method of can achieve similar performance with fewer iterations, thanks to the quasi-Newton update scheme and the possibility of updating the parameters at each time-step of every iteration. It is important to note that, additionally, our method has convergence guarantees.

## CONCLUSION

We proposed a backpropagation algorithm to optimally design an MPC scheme to maximize closed-loop performance. The cost and the constraints in the MPC can depend on the current state of the system, as well as on past solutions of previous MPC problems. We employed conservative Jacobians to compute the sensitivity of the closed-loop trajectory with respect to variations of the design parameter. Leveraging a non-smooth version of the implicit function theorem, we derived sufficient conditions under which the gradientbased optimization procedure converges to a critical point of the problem. Further, we extended our framework to cases where the MPC problem becomes infeasible, using nonsmooth penalty functions and derived conditions under which the closed-loop is guaranteed to converge to a safe solution.

Current work focuses on deploying our optimization scheme on more realistic real-life examples and extending it to scenarios where the system dynamics are only partially known and / or affected by stochastic noise.

Future work will also investigate the use of more advanced optimization techniques, such as second-order or accelerated methods, to improve the convergence rate of the optimization procedure and to obtain better convergence guarantees (e.g. to a local or global minimizer).
