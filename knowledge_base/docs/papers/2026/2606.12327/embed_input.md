<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

From the Linear Quadratic Regulator (LQR) to the (Deterministic) Kalman Filter in Two Easy Steps

Topics include Kalman filtering, Linear quadratic regulator, State estimation, Riccati equation, Optimal control, Linear quadratic Gaussian, Tutorial, Homogeneous coordinates.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Gives a tutorial derivation of the deterministic Kalman filter by embedding a trajectory-estimation problem into an enlarged LQR with homogeneous coordinates and nonstandard boundary constraints. The derivation then partitions the resulting Riccati equations to recover the dynamic observer, making the LQR-Kalman connection unusually explicit.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This note is a tutorial on the deterministic version of the Kalman filter (state estimator), which is formulated as finding the state trajectory consistent with the system's equations with the minimal amount of L^ process and measurement uncertainty. As stated, this is an input signal design problem with linear dynamics and an objective that is affine-quadratic in the state and inputs. The first step is to convert this problem to one with a purely quadratic objective by embedding in a larger system using ``homogeneous coordinates''. This converts the problem to a purely quadratic (i.e. an LQR) problem, but with non-standard initial or final state constraints. This latter problem can then be solved using a version of the matrix Differential Riccati Equation (DRE) for the larger LQR problem. The second step is a partitioning of this larger problem, which then yields the optimal dynamic observer and the DRE of the traditional Kalman filter. For comparison, the solution of the traditional LQ-tracking (Servomechanism) problem is also treated using a similar construction.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The Kalman-Bucy filter was originally formulated \[kalman1960new, kalman1961new\] as a stochastic state estimation problem in the presence of uncertainty in the dynamics, measurements and initial states, all of which are characterized probabilistically using their second order statistics. On the other hand, it has long been known that minimum-variance type estimation problems also have equivalent deterministic least-squares versions. Which version (deterministic versus stochastic) of these problems one prefers is often a matter of taste rather than logical necessity. Indeed, as Willems \[willems2002deterministic\] argues "This has been a matter of debate at least since Gauss justified Legendre's least squares as a method of computing the most probable, maximum likelihood, outcome".

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this tutorial note, a motivation for the deterministic Kalman filter is given in line with Willems' arguments \[Willems2004DeterministicLeastSquaresFiltering, willems2002deterministic\]. The derivation given follows more closely that of Sontag \[sontag2013mathematical, Sec. 8.3\], who uses the equivalence with the LQ-tracking problem, combined with a time reversal and a further optimization of the value function over the final state. A more streamlined version of this argument is presented here which disentangles the several steps, namely time reversal, introduction of homogeneous coordinates, and the further optimization of the value function.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The starting point is the traditional Linear Quadratic Regulator (LQR) for a possibly time-varying system over a finite horizon. It is assumed that the reader is familiar with this problem and its solution via a matrix Differential Riccati Equation (DRE). A "dual" problem (unrelated to estimation) is also formulated where the final, rather than initial, state is specified. This leads to a DRE that characterizes the "cost-to-arrive" function rather than the cost-to-go. This dual problem is of interest in its own right and forms the basis for the optimal estimator equations developed later. However, the dual problem as stated is a control problem (or more precisely, an input-design problem) rather than an estimation problem. We call this problem "LQR with final conditions". Its solution can be easily derived from the traditional LQR with initial conditions problem via a time reversal.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The deterministic state-estimation problem as formulated below is an affine-quadratic^11^1As subsequently defined, an "affine-quadratic" cost has quadratic, linear and constant terms. optimal control problem. The first step in the "two easy steps" alluded to in the title is the conversion of affine-quadratic problems to purely quadratic ones (i.e. of the LQR type). This is done by appending to the state an additional scalar state that is enforced to always equal $1$. This technique is akin to the introduction of so-called "homogeneous coordinates" common in optimization, computer graphics and projective geometry. It is of interest in its own right and is described carefully.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The second step is to partition the Differential Riccati Equation (DRE) of the purely quadratic LQR problem, and extract three differential equations from it. One of those is a DRE for the original problem, and the second is a linear system of the same state dimension as the original system. This reveals why controllers for affine-quadratic cost problems contain a dynamical system, while controllers for purely quadratic costs are memoryless. In the LQ-tracking problem, those dynamics are the anti-causal feedforward part of the control, while in the estimation problem, the dynamics are those of the causal observer!

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

There is actually a small third step which appears only in the estimation problem, but it is rather short, so is not emphasized as the other two steps. The estimation problem is solved as if the final state is known. The final state however is unknown, but this solution falls out of the LQR problem with final conditions rather easily given the so-called cost-to-arrive function. It is then very simple to further optimize the cost-to-arrive with respect to the (unknown) final state to yield the Kalman filter equations.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We close this introduction by motivating and formulating the deterministic version of the state estimation problem as advocated by Willems \[Willems2004DeterministicLeastSquaresFiltering\] (see also Hespanha's textbook \[hespanha2018linear, Sec. 24.2\] as well as \[aguiar2003minimum, aguiar2006minimum\]). For simplicity we consider a system model without a control input, since the case with a control input is essentially identical. The uncertain system model is

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We use the notation $w_{\lbrack 0,T\rbrack}:=\left\{ {{{w{(t)}};t} \in {\lbrack 0,T\rbrack}} \right\}$ to refer to the entire signal over the time horizon $\lbrack 0,T\rbrack$ when that is needed for emphasis. We call the system (1 to the (Deterministic) Kalman Filter in Two Easy Steps")) "uncertain" because the only signal that is known is the output $y_{\lbrack 0,T\rbrack}$. All the other signals $w_{\lbrack 0,T\rbrack}$, $v_{\lbrack 0,T\rbrack}$, $x_{\lbrack 0,T\rbrack}$, and the initial state vector $\mathsf{x}_{i} \in {\mathbb{R}}^{n}$ are unknown.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Given an observation $y_{\lbrack 0,T\rbrack}$, there is an infinite number of combinations of the unknown quantities that satisfy the dynamics (1 to the (Deterministic) Kalman Filter in Two Easy Steps")). How should one choose the best from among those?

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

To guide this choice, first note that as mentioned, the uncertainty in the system (1 to the (Deterministic) Kalman Filter in Two Easy Steps")) is "parametrized" by $(w_{\lbrack 0,T\rbrack},v_{\lbrack 0,T\rbrack},x_{\lbrack 0,T\rbrack},\mathsf{x}_{i})$. However, since $\mathsf{x}_{i}$ and $w_{\lbrack 0,T\rbrack}$ together determine $x_{\lbrack 0,T\rbrack}$, we can choose to parameterize the uncertainty with just the triple $(w_{\lbrack 0,T\rbrack},v_{\lbrack 0,T\rbrack},\mathsf{x}_{i})$. Whatever parameterization of the uncertainty we use, the key idea is as follows.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Minimal Uncertainty Principle Given the observation $y_{\lbrack 0,T\rbrack}$, the optimal estimate ${\hat{x}}_{\lbrack 0,T\rbrack}$ of the state trajectory is the signal consistent with the system equations (1 to the (Deterministic) Kalman Filter in Two Easy Steps")), with the minimal "size" of the uncertainty triple $(w_{\lbrack 0,T\rbrack},v_{\lbrack 0,T\rbrack},\mathsf{x}_{i})$. \\endlxSVG@picture

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Note that this principle leaves the notion of uncertainty "size" as a choice. The most mathematically tractable choice made below uses quadratic norms.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

The principle stated above can be thought of as a version of "Occam's razor", which roughly speaking is: among all the possible explanations, choose the one with the fewest assumptions. Here the "assumptions" are the uncertain (unknown) triple $(w_{\lbrack 0,T\rbrack},v_{\lbrack 0,T\rbrack},\mathsf{x}_{i})$, and choosing the smallest size uncertainty is a proxy for "fewest assumptions".

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

As already mentioned, the most mathematically tractable choice of uncertainty size is a quadratic functional of the form

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

The weight matrices $\mathsf{V},\mathsf{W},\mathsf{X}$ are design choices made based on the designer's a priori assumptions about the relative sizes of the various uncertainty components^22^2The initial-state cost can also be generalized to ${\|{\mathsf{x}_{i} - \overline{x}}\|}_{\mathsf{X}}^{2}$ where $\overline{x}$ is a prior mean. We omit this for simplicity of notation.. The standing assumption here is that the uncertain signals $v,w$ belong to $\mathsf{L}^{2}{\lbrack 0,T\rbrack}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

The relations between the weight matrices $\mathsf{V},\mathsf{W},\mathsf{X}$ and the more familiar noise and initial state covariance matrices are described in Section 4.1 to the (Deterministic) Kalman Filter in Two Easy Steps"), where the connections between deterministic and stochastic versions of the Kalman filter are discussed.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

Before stating the problem formally, observe that the output equation (1 to the (Deterministic) Kalman Filter in Two Easy Steps")) can be used to express the $v$ component of the cost $J$ in terms of $x$ and $y$ as follows

<!-- chunk {"id": "body-0021", "role": "body", "section": "Introduction", "weight": 1.5} -->

Now the problem can be stated as follows.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Introduction", "weight": 1.5} -->

As stated, this is an optimal "input design" problem. The solution gives not only the optimal state estimate $\hat{x}$, but also the optimal inputs $\hat{w}$ and $\hat{v}$. It is closely related to the LQ-tracking problem, though there is an important difference in that the initial state is also unknown. It is also different from an LQR problem in that the cost $J$ is not purely quadratic in the state and input, but rather quadratic+linear+constant in the state since

<!-- chunk {"id": "body-0023", "role": "body", "section": "Introduction", "weight": 1.5} -->

We will see that such problems can be converted to ones with purely quadratic cost by introducing "homogeneous state coordinates".

<!-- chunk {"id": "body-0024", "role": "body", "section": "The LQR Problem with Initial or Final Conditions", "weight": 1.0} -->

We consider two versions of the standard LQR problem over a finite time horizon $\lbrack 0,T\rbrack$. One version is where the initial condition is specified. This is the most commonly used version. However, there is a parallel version where the final condition is specified instead. Specifically, we consider the following two problems.

<!-- chunk {"id": "body-0025", "role": "body", "section": "The LQR Problem with Initial or Final Conditions", "weight": 1.0} -->

LQR with initial conditions: This is the standard LQR problem over a finite time horizon with a specified initial condition and a final state penalty

<!-- chunk {"id": "body-0026", "role": "body", "section": "The LQR Problem with Initial or Final Conditions", "weight": 1.0} -->

where ${\|{x{(T)}}\|}_{\mathsf{X}}^{2}:={x^{\ast}{(T)}\mathsf{X}x{(T)}}$ is the final state penalty. As is well known \[kirk1970optimal, sage1977optimum\], the optimal input is obtained from the solution of a matrix Differential Riccati Equation (DRE) with final boundary conditions

<!-- chunk {"id": "body-0027", "role": "body", "section": "The LQR Problem with Initial or Final Conditions", "weight": 1.0} -->

with the quadratic value function

<!-- chunk {"id": "body-0028", "role": "body", "section": "The LQR Problem with Initial or Final Conditions", "weight": 1.0} -->

This is referred to as the "cost-to-go" evaluated at $t = 0$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "The LQR Problem with Initial or Final Conditions", "weight": 1.0} -->

LQR with final conditions: On the other hand, an LQR problem with a final state target $x_{f}$ and an initial state penalty can also be formulated as follows

<!-- chunk {"id": "body-0030", "role": "body", "section": "The LQR Problem with Initial or Final Conditions", "weight": 1.0} -->

where ${\|{x{}}\|}_{\mathsf{X}}^{2}:={x^{\ast}{}\mathsf{X}x{}}$ is the initial-state penalty. The optimal solution to this problem is also obtained from a DRE, but one with initial boundary conditions

<!-- chunk {"id": "body-0031", "role": "body", "section": "The LQR Problem with Initial or Final Conditions", "weight": 1.0} -->

This is sometimes referred to as the "cost-to-arrive" in the Moving Horizon Estimation (MHE) literature \[diehl2014lecture\].

<!-- chunk {"id": "body-0032", "role": "body", "section": "The LQR Problem with Initial or Final Conditions", "weight": 1.0} -->

Note that the main difference between the solutions of the two problems is the final (5 to the (Deterministic) Kalman Filter in Two Easy Steps")) versus initial (7 to the (Deterministic) Kalman Filter in Two Easy Steps")) condition on the DRE. The solution (7 to the (Deterministic) Kalman Filter in Two Easy Steps")) can be derived from the standard minimum principle arguments that lead to a Two Point Boundary Value Problem (TPBVP) with a linear relation between the state and co-state at initial time. Propagating that relation forward in time gives the DRE (7 to the (Deterministic) Kalman Filter in Two Easy Steps")). Alternatively, it can be derived from the ${\mathsf{L}\mathsf{Q}\mathsf{R}}_{\mathsf{i}}$ problem by a simple time reversal as follows. Define the time-reversed signals

<!-- chunk {"id": "body-0033", "role": "body", "section": "The LQR Problem with Initial or Final Conditions", "weight": 1.0} -->

The problem (6 to the (Deterministic) Kalman Filter in Two Easy Steps")) then becomes

<!-- chunk {"id": "body-0034", "role": "body", "section": "The LQR Problem with Initial or Final Conditions", "weight": 1.0} -->

Note that the integral part of the cost is unchanged. Now apply the ${\mathsf{L}\mathsf{Q}\mathsf{R}}_{\mathsf{i}}$ solution (5 to the (Deterministic) Kalman Filter in Two Easy Steps")) to this problem, and define the matrix function ${S{(t)}}:={P{({T - t})}}$ as the time-reversed solution of the DRE (5 to the (Deterministic) Kalman Filter in Two Easy Steps")). This gives the solution (7 to the (Deterministic) Kalman Filter in Two Easy Steps")) after another time reversal to obtain the original $x$ and $u$ signals.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Since these are finite-horizon problems, the only conditions needed for the existence of solutions to the DREs (5 to the (Deterministic) Kalman Filter in Two Easy Steps")) and (7 to the (Deterministic) Kalman Filter in Two Easy Steps")) are ${Q,\mathsf{X}} \geq 0$ and $R > 0$. These conditions also guarantee that ${P{(t)}} \geq 0$, and monotonically non-decreasing backwards in $t$ for (5 to the (Deterministic) Kalman Filter in Two Easy Steps")), and forward in $t$ for (7 to the (Deterministic) Kalman Filter in Two Easy Steps")). Furthermore, if ${P{(t)}} > 0$ is required, then $(Q,A)$ observable guarantees this for all $t \in {\lbrack 0,T\rbrack}$ other than at the boundary condition.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 1", "weight": 1.0} -->

In the LQ-tracking and state estimation problems discussed below, these conditions translate to other conditions on the problem data in each case as will be shown. Note that stabilizability of $(A,B)$ and detectability of $(Q,A)$ are only needed for infinite-horizon problems since stability is an asymptotic concept.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Affine-Quadratic Problems with Initial Conditions", "weight": 1.0} -->

In the case of specified initial conditions, the DRE for the homogenized problem (14 to the (Deterministic) Kalman Filter in Two Easy Steps")) with initial conditions is given by (5 to the (Deterministic) Kalman Filter in Two Easy Steps")). Assuming existence conditions hold (see Remark 2 to the (Deterministic) Kalman Filter in Two Easy Steps") below), label its solution as $\hat{P}$ and partition it conformably with the partitions in (12 to the (Deterministic) Kalman Filter in Two Easy Steps")) as follows

<!-- chunk {"id": "body-0038", "role": "body", "section": "Affine-Quadratic Problems with Initial Conditions", "weight": 1.0} -->

Note that $P$ is an $n \times n$ matrix (the state dimension of the original problem), while the off-diagonal term $p_{1}$ is an $n$-vector, and $p_{0}$ is a scalar. The partitioning of the $\hat{A},\hat{B},\hat{H}$ matrices gives the following set of equations

<!-- chunk {"id": "body-0039", "role": "body", "section": "Affine-Quadratic Problems with Initial Conditions", "weight": 1.0} -->

This gives three equations for the and blocks respectively

<!-- chunk {"id": "body-0040", "role": "body", "section": "Affine-Quadratic Problems with Initial Conditions", "weight": 1.0} -->

Together, these three equations are equivalent to (15 to the (Deterministic) Kalman Filter in Two Easy Steps")).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Affine-Quadratic Problems with Initial Conditions", "weight": 1.0} -->

Equation (16 to the (Deterministic) Kalman Filter in Two Easy Steps")) is a DRE associated with a standard LQR problem with the matrices $(A,B,H,R)$. Equation (17 to the (Deterministic) Kalman Filter in Two Easy Steps")) is a linear system for the vector signal $p_{1}$, driven by the constant or time-varying $n$-vector $h_{1}$, the off-diagonal block of the matrix $\hat{H}$. Note that the "$A$-matrix" of this linear system depends on the solution $P$ of the DRE (16 to the (Deterministic) Kalman Filter in Two Easy Steps")). We will see that in the LQ-tracking problem, the linear system (17 to the (Deterministic) Kalman Filter in Two Easy Steps")) for $p_{1}$ gives the (anti-causal) feedforward part of the control.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Affine-Quadratic Problems with Initial Conditions", "weight": 1.0} -->

The optimal input $u$ is given by the standard formula (5 to the (Deterministic) Kalman Filter in Two Easy Steps")) applied to the problem (14 to the (Deterministic) Kalman Filter in Two Easy Steps"))

<!-- chunk {"id": "body-0043", "role": "body", "section": "Affine-Quadratic Problems with Initial Conditions", "weight": 1.0} -->

Note that it has the form of a state feedback plus an additional term that comes from the linear system (17 to the (Deterministic) Kalman Filter in Two Easy Steps")).

<!-- chunk {"id": "body-0044", "role": "body", "section": "Affine-Quadratic Problems with Initial Conditions", "weight": 1.0} -->

Finally, the $p_{0}$ term in (18 to the (Deterministic) Kalman Filter in Two Easy Steps")) is just the integral of the right hand side which depends on $p_{1}$ (and in turn $P$). This term plays no role in the optimal input, but it does appear in the value function, which is

<!-- chunk {"id": "body-0045", "role": "body", "section": "Affine-Quadratic Problems with Initial Conditions", "weight": 1.0} -->

Note that this is an affine-quadratic function of the initial state $\mathsf{x}_{i}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Remark 2", "weight": 1.0} -->

(Existence conditions) Existence conditions for (16 to the (Deterministic) Kalman Filter in Two Easy Steps")) are $H \geq 0$ and $R > 0$. If those hold, then solutions to (17 to the (Deterministic) Kalman Filter in Two Easy Steps")) and (18 to the (Deterministic) Kalman Filter in Two Easy Steps")) also exist over $\lbrack 0,T\rbrack$ since (17 to the (Deterministic) Kalman Filter in Two Easy Steps")) is a linear system for $p_{1}$, and $p_{0}$ is simply the integral of the right hand side in (18 to the (Deterministic) Kalman Filter in Two Easy Steps")). Thus solutions $\hat{P}$ to (15 to the (Deterministic) Kalman Filter in Two Easy Steps")) exist over $\lbrack 0,T\rbrack$ if $H \geq 0$ and $R > 0$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Affine-Quadratic Problems with Final Conditions", "weight": 1.0} -->

The DRE for the homogenized problem (14 to the (Deterministic) Kalman Filter in Two Easy Steps")) with final conditions is given by (7 to the (Deterministic) Kalman Filter in Two Easy Steps")). Label its solution as $\hat{S}$ and partition it conformably with the partitions in (12 to the (Deterministic) Kalman Filter in Two Easy Steps")) as follows

<!-- chunk {"id": "body-0048", "role": "body", "section": "Affine-Quadratic Problems with Final Conditions", "weight": 1.0} -->

Partitioning this DRE conformably with the partitioning of $\hat{A},\hat{B},\hat{H}$ gives

<!-- chunk {"id": "body-0049", "role": "body", "section": "Affine-Quadratic Problems with Final Conditions", "weight": 1.0} -->

This again leads to three equations for the and blocks respectively

<!-- chunk {"id": "body-0050", "role": "body", "section": "Affine-Quadratic Problems with Final Conditions", "weight": 1.0} -->

In contrast to the ${\mathsf{L}\mathsf{Q}\mathsf{R}}_{\mathsf{i}}$ problem differential equations (16 to the (Deterministic) Kalman Filter in Two Easy Steps"))-(18 to the (Deterministic) Kalman Filter in Two Easy Steps")), these equations can be solved forward in time since initial conditions are given. We will see in the estimation problem that the linear system (22 to the (Deterministic) Kalman Filter in Two Easy Steps")) will produce (after a change of variables) the (causal) observer structure of the Kalman filter.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Affine-Quadratic Problems with Final Conditions", "weight": 1.0} -->

The optimal input for this problem obtained from (7 to the (Deterministic) Kalman Filter in Two Easy Steps")) is given by

<!-- chunk {"id": "body-0052", "role": "body", "section": "Affine-Quadratic Problems with Final Conditions", "weight": 1.0} -->

while the optimal performance is a quadratic form on the (final) homogenized coordinates

<!-- chunk {"id": "body-0053", "role": "body", "section": "Affine-Quadratic Problems with Final Conditions", "weight": 1.0} -->

Note again that this is an affine-quadratic functional on the final state $x_{f}$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Affine-Quadratic Problems with Final Conditions", "weight": 1.0} -->

In the next section we apply the initial-value affine-quadratic problem solution to the well-known LQ-tracking problem. In the following Section 4 to the (Deterministic) Kalman Filter in Two Easy Steps"), we apply the final-value affine-quadratic problem to the state estimation problem.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Remark 3", "weight": 1.0} -->

As in remark 2 to the (Deterministic) Kalman Filter in Two Easy Steps"), the existence conditions for (21 to the (Deterministic) Kalman Filter in Two Easy Steps")) are $H \geq 0$ and $R > 0$. However, when this is applied to the estimation problem in Section 4 to the (Deterministic) Kalman Filter in Two Easy Steps"), we will require ${S{(t)}} > 0$ for $t \in {(0,T\rbrack}$. The additional condition of $(H,A)$ observable guarantees this.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Linear-Quadratic Tracking", "weight": 1.0} -->

The standard Linear-Quadratic tracking (LQ-tracking) problem (also known as the servomechanism problem) involves linear dynamics with a quadratic tracking objective as follows^33^3For simplicity of exposition, a final state cost is not included here.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Linear-Quadratic Tracking", "weight": 1.0} -->

where $Cx$ is considered as an output that should "track" a given reference signal $r$. This problem is of the form (11 to the (Deterministic) Kalman Filter in Two Easy Steps")) since the objective is affine-quadratic

<!-- chunk {"id": "body-0058", "role": "body", "section": "Linear-Quadratic Tracking", "weight": 1.0} -->

In homogeneous coordinates, this becomes the following initial-state LQR problem

<!-- chunk {"id": "body-0059", "role": "body", "section": "Linear-Quadratic Tracking", "weight": 1.0} -->

Note that the state cost above includes the tracking signal $r$, so even if the original LQ-tracking problem is time invariant, its reformulation (27 to the (Deterministic) Kalman Filter in Two Easy Steps")) as an LQR problem has a time-varying state cost (a time-varying $Q$-matrix).

<!-- chunk {"id": "body-0060", "role": "body", "section": "Linear-Quadratic Tracking", "weight": 1.0} -->

Equations (16 to the (Deterministic) Kalman Filter in Two Easy Steps"))-(18 to the (Deterministic) Kalman Filter in Two Easy Steps")) in this case become

<!-- chunk {"id": "body-0061", "role": "body", "section": "Linear-Quadratic Tracking", "weight": 1.0} -->

Note that Equation (28 to the (Deterministic) Kalman Filter in Two Easy Steps")) is a DRE associated with an LQR problem with the matrices $(A,B,{C^{\ast}MC},R)$. It is time invariant if the original LQ-tracking problem is time invariant.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Linear-Quadratic Tracking", "weight": 1.0} -->

Equation (29 to the (Deterministic) Kalman Filter in Two Easy Steps")) is a linear system for the vector signal $p_{1}$, driven by the reference signal $r$, and evolving anti-causally back from the final condition

<!-- chunk {"id": "body-0063", "role": "body", "section": "Linear-Quadratic Tracking", "weight": 1.0} -->

The optimal control $u$ is given by the formula (19 to the (Deterministic) Kalman Filter in Two Easy Steps")) as

<!-- chunk {"id": "body-0064", "role": "body", "section": "Linear-Quadratic Tracking", "weight": 1.0} -->

This is the well-known solution to the LQ-tracking problem (see e.g. \[sage1977optimum, Sec. 5.2\] or \[kirk1970optimal\]).

<!-- chunk {"id": "body-0065", "role": "body", "section": "Remark 4", "weight": 1.0} -->

The conditions $M \geq 0$ and $R > 0$ in (26 to the (Deterministic) Kalman Filter in Two Easy Steps")) guarantee ${C^{\ast}MC} \geq 0$ in (28 to the (Deterministic) Kalman Filter in Two Easy Steps")) and thus the existence of a solution ${P{(t)}} \geq 0$ over $\lbrack 0,T\rbrack$.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Remark 5", "weight": 1.0} -->

Sometimes an equivalent version of the solution is written using the negative of $p_{1}$ in (29 to the (Deterministic) Kalman Filter in Two Easy Steps")). If we define ${f{(t)}}:={- {p_{1}{(t)}}}$, then the differential equation for $f$ is

<!-- chunk {"id": "body-0067", "role": "body", "section": "Remark 5", "weight": 1.0} -->

and the control input can then be written as a function of the difference

<!-- chunk {"id": "body-0068", "role": "body", "section": "Remark 6", "weight": 1.0} -->

The existence conditions for (28 to the (Deterministic) Kalman Filter in Two Easy Steps")) are ${C^{\ast}MC} \geq 0$ and $R > 0$. Those are guaranteed by (26 to the (Deterministic) Kalman Filter in Two Easy Steps")) since $M \geq 0\Rightarrow{C^{\ast}MC} \geq 0$.

<!-- chunk {"id": "body-0069", "role": "body", "section": "State Estimation", "weight": 1.0} -->

As described in the introduction, the state estimation problem is to find the triple $(\hat{x},\hat{w},{\hat{\mathsf{x}}}_{i})$ that minimize the following objective $J$ subject to the dynamic constraints

<!-- chunk {"id": "body-0070", "role": "body", "section": "State Estimation", "weight": 1.0} -->

where now the time horizon is denoted by $\lbrack 0,t\rbrack$, and the running time variable is $\tau$. In homogeneous coordinates, this problem becomes

<!-- chunk {"id": "body-0071", "role": "body", "section": "State Estimation", "weight": 1.0} -->

This problem appears similar to the affine-quadratic problems of Section 2.2 to the (Deterministic) Kalman Filter in Two Easy Steps") with $Bu$ replaced by $\hat{w}$. However, here neither initial ${\hat{x}{}} = {\hat{\mathsf{x}}}_{i}$ nor final $\hat{x}{(t)}$ states are specified. In fact, finding the entire state trajectory (as well as the "optimal" estimate of the process disturbance $\hat{w}$) over $\lbrack 0,t\rbrack$ is the task.

<!-- chunk {"id": "body-0072", "role": "body", "section": "State Estimation", "weight": 1.0} -->

One way to approach this difficulty is to treat the problem (33 to the (Deterministic) Kalman Filter in Two Easy Steps")) as if the final state is known, use the final condition LQR formulation for which we know the optimal cost is given by (25 to the (Deterministic) Kalman Filter in Two Easy Steps")). The next step would be to optimize the optimal cost further with respect to the unknown portion ${\hat{x}{(t)}} = x_{f}$ of the final state. This should yield the answer to (33 to the (Deterministic) Kalman Filter in Two Easy Steps")) since it amounts to optimizing over all consistent state trajectories with unknown final conditions.

<!-- chunk {"id": "body-0073", "role": "body", "section": "State Estimation", "weight": 1.0} -->

This is a problem of the form (14 to the (Deterministic) Kalman Filter in Two Easy Steps")) with a known final state. The optimal solution to such problems is given by Equations (21 to the (Deterministic) Kalman Filter in Two Easy Steps"))-(23 to the (Deterministic) Kalman Filter in Two Easy Steps")), which for this case become

<!-- chunk {"id": "body-0074", "role": "body", "section": "State Estimation", "weight": 1.0} -->

The optimal value of the problem (34 to the (Deterministic) Kalman Filter in Two Easy Steps")) constrained by ${\hat{x}{(t)}} = x_{f}$ is given by (25 to the (Deterministic) Kalman Filter in Two Easy Steps")) as

<!-- chunk {"id": "body-0075", "role": "body", "section": "State Estimation", "weight": 1.0} -->

If we optimize this further with respect to $x_{f}$, we actually obtain the optimal estimate $\hat{x}{(t)}$ at time $t$. The affine-quadratic functional (38 to the (Deterministic) Kalman Filter in Two Easy Steps")) is minimized with respect to $x_{f}$ by

<!-- chunk {"id": "body-0076", "role": "body", "section": "State Estimation", "weight": 1.0} -->

Now one way to obtain the optimal estimate $\hat{x}{(t)}$ is to run Equations (35 to the (Deterministic) Kalman Filter in Two Easy Steps"))-(36 to the (Deterministic) Kalman Filter in Two Easy Steps")) simultaneously forward in time to compute $S{(t)}$ and $s_{1}{(t)}$, and then obtain $\hat{x}{(t)}$ from (39 to the (Deterministic) Kalman Filter in Two Easy Steps")). However, we may want to directly find a differential equation that $\hat{x}$ satisfies and run that instead of the equation for $s_{1}$. Indeed, the differential equation for $\hat{x}$ can be derived from (39 to the (Deterministic) Kalman Filter in Two Easy Steps")) and (35 to the (Deterministic) Kalman Filter in Two Easy Steps"))-(36 to the (Deterministic) Kalman Filter in Two Easy Steps")) as follows

<!-- chunk {"id": "body-0077", "role": "body", "section": "State Estimation", "weight": 1.0} -->

Thus the dynamics of $\hat{x}$ are those of an observer for the system $\overset{˙}{x} = {Ax}$, $y = {Cx}$, with an optimal observer gain $L$ obtained from the solution of the forward DRE (35 to the (Deterministic) Kalman Filter in Two Easy Steps")). Equations (35 to the (Deterministic) Kalman Filter in Two Easy Steps")) and (40 to the (Deterministic) Kalman Filter in Two Easy Steps")) are the "information filter" form of the Kalman filter. This terminology and the relations to the stochastic version of the Kalman filter (in terms of covariance matrices) are detailed in the next section.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Remark 7", "weight": 1.0} -->

Existence conditions for the DRE (35 to the (Deterministic) Kalman Filter in Two Easy Steps")) are $\mathsf{V} \geq 0$ and $\mathsf{W} > 0$. However, the formula (40 to the (Deterministic) Kalman Filter in Two Easy Steps")) for the observer gain $L$ requires $S$ to be invertible. The additional condition that $({C^{\ast}\mathsf{V}C},A)$ is observable guarantees ${S{(t)}} > 0$. This is satisfied by the assumptions in (32 to the (Deterministic) Kalman Filter in Two Easy Steps")) since $\mathsf{V} > 0$ and $(C,A)$ observable implies $({\mathsf{V}^{\frac{1}{2}}C},A)$ observable, which is equivalent to $({C^{\ast}\mathsf{V}C},A)$ observable.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Relations to the Stochastic Kalman Filter", "weight": 1.0} -->

The stochastic version of the Kalman filter problem is formulated for the following dynamics

<!-- chunk {"id": "body-0080", "role": "body", "section": "Relations to the Stochastic Kalman Filter", "weight": 1.0} -->

where $w$ and $v$ are zero-mean, mutually uncorrelated, white noise second-order processes with the following statistics

<!-- chunk {"id": "body-0081", "role": "body", "section": "Relations to the Stochastic Kalman Filter", "weight": 1.0} -->

where $\Sigma_{w}$ and $\Sigma_{v}$ are the instantaneous covariance matrices of $w$ and $v$ respectively, while $\Sigma_{i}$ is the covariance matrix of the (assumed zero-mean) initial state. The objective is to find the estimate $\hat{x}$ which minimizes the variance

<!-- chunk {"id": "body-0082", "role": "body", "section": "Relations to the Stochastic Kalman Filter", "weight": 1.0} -->

of the estimation error $e:={x - \hat{x}}$ at each time $t$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Relations to the Stochastic Kalman Filter", "weight": 1.0} -->

The solution of this problem is given by a DRE for the error covariance matrix $\Sigma_{e}$, together with an observer for the dynamics of $\hat{x}$

<!-- chunk {"id": "body-0084", "role": "body", "section": "Relations to the Stochastic Kalman Filter", "weight": 1.0} -->

For comparison, the equations (35 to the (Deterministic) Kalman Filter in Two Easy Steps")), (40 to the (Deterministic) Kalman Filter in Two Easy Steps")) for $\hat{x}$ from the deterministic problem are

<!-- chunk {"id": "body-0085", "role": "body", "section": "Relations to the Stochastic Kalman Filter", "weight": 1.0} -->

The relation between the two is ${S{(t)}} = {\Sigma_{e}^{- 1}{(t)}}$. Indeed, starting from the DRE (43 to the (Deterministic) Kalman Filter in Two Easy Steps")) for $S$, we can compute the differential equation for $S^{- 1}$ as

<!-- chunk {"id": "body-0086", "role": "body", "section": "Relations to the Stochastic Kalman Filter", "weight": 1.0} -->

This last equation is precisely (41 to the (Deterministic) Kalman Filter in Two Easy Steps")) for $\Sigma_{e}$ if we identify

<!-- chunk {"id": "body-0087", "role": "body", "section": "Relations to the Stochastic Kalman Filter", "weight": 1.0} -->

Note also that the two observer gains $L$ in (42 to the (Deterministic) Kalman Filter in Two Easy Steps")) and (44 to the (Deterministic) Kalman Filter in Two Easy Steps")) are equal as well

<!-- chunk {"id": "body-0088", "role": "body", "section": "Relations to the Stochastic Kalman Filter", "weight": 1.0} -->

The matrix ${S{(t)}} = {\Sigma_{e}^{- 1}{(t)}}$ is sometimes referred to as the "information matrix". See below for further comments on this interpretation. The standard interpretations of $\Sigma_{w}$ and $\Sigma_{v}$ are reversed when considering the weight matrices $\mathsf{W}$ and $\mathsf{V}$ as follows.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Relations to the Stochastic Kalman Filter", "weight": 1.0} -->

When $\Sigma_{w}$ is chosen small, this means lower error in the dynamics $\overset{˙}{x} = {Ax}$, i.e. higher trust in the dynamical model. This is the same as choosing $\mathsf{W} = \Sigma_{w}^{- 1}$ large, which in this case will force $w$ in the cost (2 to the (Deterministic) Kalman Filter in Two Easy Steps")) to be small.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Relations to the Stochastic Kalman Filter", "weight": 1.0} -->

When $\Sigma_{v}$ is chosen small, this means higher trust in the measurements. This is equivalent to choosing $\mathsf{V} = \Sigma_{v}^{- 1}$ large, which will force the term $v$ in the cost (2 to the (Deterministic) Kalman Filter in Two Easy Steps")) to be small.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Relations to the Stochastic Kalman Filter", "weight": 1.0} -->

Lower uncertainty in the initial state means small $\Sigma_{i}$. Again, this corresponds to choosing $\mathsf{X} = \Sigma_{i}^{- 1}$ large to force $\mathsf{x}_{i}$ in (2 to the (Deterministic) Kalman Filter in Two Easy Steps")) to be small.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Interpretations of $\\Sigma_{e}$ and $S$", "weight": 1.0} -->

For reasons described below, we will refer to ${S{(t)}} = {\Sigma_{e}^{- 1}{(t)}}$ as the certainty matrix. Both $S$ and $\Sigma_{e}$ are positive definite matrices, and such matrices have nice geometric interpretations in terms of ellipsoids. We begin with the covariance matrix $\Sigma_{e}$.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Interpretations of $\\Sigma_{e}$ and $S$", "weight": 1.0} -->

For zero-mean Gaussian random vectors, the covariance matrix completely determines the density which is of the following form

<!-- chunk {"id": "body-0094", "role": "body", "section": "Interpretations of $\\Sigma_{e}$ and $S$", "weight": 1.0} -->

One way to visualize this density is through its level sets. The level sets of $\rho{(.)}$ are the same as the level sets of the quadratic functional $e^{\ast}\Sigma_{e}^{\text{-}1}e$ (with different level values). The level sets of this quadratic functional are ellipsoids with principal axes aligned with the eigenvector directions. Let $\left\{ \lambda_{1},\ldots,\lambda_{n} \right\}$ be the eigenvalues of $\Sigma_{e}$ (not $\Sigma_{e}^{\text{-}1}$) arranged in descending order, with $\left\{ v_{1},\ldots,v_{n} \right\}$ the corresponding eigenvectors.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Interpretations of $\\Sigma_{e}$ and $S$", "weight": 1.0} -->

The ellipsoid $\left\{ {{x;{x^{\ast}\Sigma_{e}^{\text{-}1}x}} = 1} \right\}$ has major axis with length $2\sqrt{\lambda_{1}}$ in the direction $v_{1}$, while the minor axis has length $2\sqrt{\lambda_{n}}$ in the direction $v_{n}$. See Figure 2(a) ‣ Figure 2 ‣ Interpretations of Σ_𝑒 and 𝑆 ‣ 4.1 Relations to the Stochastic Kalman Filter ‣ 4 State Estimation ‣ From the Linear Quadratic Regulator (LQR) to the (Deterministic) Kalman Filter in Two Easy Steps") for an illustration in two dimensions.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Interpretations of $\\Sigma_{e}$ and $S$", "weight": 1.0} -->

(a) The level set {e; e* Σe- 1 e=1} for any matrix Σe &gt; 0 is an ellipsoid whose principal axes align with the eigenvectors and eigenvalues of Σe as shown. Here λ1 &gt; λ2 are eigenvalues of Σe (not Σe- 1).

<!-- chunk {"id": "body-0097", "role": "body", "section": "Interpretations of $\\Sigma_{e}$ and $S$", "weight": 1.0} -->

(b) The “certainty functional” (x - x̂)* S (x - x̂) = (x - x̂)* Σ- 1 (x - x̂). Its steepest ascent is in the direction of v2, the eigenvector of Σ with the smallest eigenvalue, which corresponds to the largest eigenvalue of S = Σ- 1. This is the direction of highest certainty, corresponding to the direction of lowest variance in the stochastic interpretation.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Interpretations of $\\Sigma_{e}$ and $S$", "weight": 1.0} -->

(c) Scatter plots of 3 random variables with different densities, normalized to have the same covariance matrix Σ. The black ellipsoids are the level sets {x; x* Σ- 1 x=1}. The blue ellipsoids are scaled to contain 95% of the probability mass for a Gaussian density.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Interpretations of $\\Sigma_{e}$ and $S$", "weight": 1.0} -->

For a Gaussian density, the fraction $p$ of the probability mass is contained in the level-set interior

<!-- chunk {"id": "body-0100", "role": "body", "section": "Interpretations of $\\Sigma_{e}$ and $S$", "weight": 1.0} -->

where $F_{\chi_{n}^{2}}^{- 1}$ is the inverse of the cumulative density (the quantile function) of the $\chi^{2}$ distribution with $n$ degrees of freedom. Figure 2(c) ‣ Figure 2 ‣ Interpretations of Σ_𝑒 and 𝑆 ‣ 4.1 Relations to the Stochastic Kalman Filter ‣ 4 State Estimation ‣ From the Linear Quadratic Regulator (LQR) to the (Deterministic) Kalman Filter in Two Easy Steps") shows the level sets in dimension 2 for three random vectors with different densities. While the formula (45 to the (Deterministic) Kalman Filter in Two Easy Steps")) is exact only for Gaussian densities, it is generally a reasonable approximation for some unimodal densities as seen in the figure. Note how the major axis of the ellipsoid (corresponding to the largest eigenvalue $\lambda_{1}$ of $\Sigma$) is the direction of highest variance, and vice versa for the minor axis.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Interpretations of $\\Sigma_{e}$ and $S$", "weight": 1.0} -->

Thus the eigenvalues/vectors of $\Sigma_{e}$ determine the variance of the estimation error in various directions in state space. The variance of $e$ can be thought of as a proxy for how much uncertainty there is in estimating that direction in state space. For most problems, some directions in state space are easier to estimate than others. The eigenvalues/vectors of $\Sigma_{e}$ quantify this.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Interpretations of $\\Sigma_{e}$ and $S$", "weight": 1.0} -->

In the "information filter" interpretation \[ThrunLiuKollerNgGhahramaniDurrantWhyte2004SEIF\] of the Kalman filter, $\Sigma_{e}^{- 1}{(t)}$ is called the information matrix, and $\Sigma_{e}^{- 1}{(t)}\hat{x}{(t)}$ is called the information vector. Note that the latter is precisely $- s_{1}$ in the linear system (36 to the (Deterministic) Kalman Filter in Two Easy Steps")) since by (39 to the (Deterministic) Kalman Filter in Two Easy Steps")) ${s_{1}{(t)}} = {- {S{(t)}\hat{x}{(t)}}} = {- {\Sigma_{e}^{- 1}{(t)}\hat{x}{(t)}}}$.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Interpretations of $\\Sigma_{e}$ and $S$", "weight": 1.0} -->

The interpretation of $S{(t)}$ as a kind of "information" can also be given without resort to probabilistic arguments. Recall that the optimal estimate $\hat{x}$ was obtained by optimizing (38 to the (Deterministic) Kalman Filter in Two Easy Steps")) at each $t$ with respect to $x_{f}$

<!-- chunk {"id": "body-0104", "role": "body", "section": "Interpretations of $\\Sigma_{e}$ and $S$", "weight": 1.0} -->

Thus the difference between the cost-to-arrive (recall that this quantifies the level of uncertainty (3 to the (Deterministic) Kalman Filter in Two Easy Steps")) in the estimation problem) evaluated at any "guess" $x$ compared to it evaluated at the optimal vector $\hat{x}$ is

<!-- chunk {"id": "body-0105", "role": "body", "section": "Interpretations of $\\Sigma_{e}$ and $S$", "weight": 1.0} -->

With $S > 0$, this is a quadratic, "bowl-shaped" functional of the difference between the optimal estimate $\hat{x}$ and any other vector $x$. For any given direction $({x - \hat{x}})$, the steeper this functional is, the more "certain" the optimal filter is of its estimate in that direction. In particular, the direction of the eigenvector of $S$ of largest eigenvalue is the direction in which the filter is most certain of its estimate, and conversely the eigenvector associated with the smallest eigenvalue is the direction of least certainty. See Figure 2(b) ‣ Figure 2 ‣ Interpretations of Σ_𝑒 and 𝑆 ‣ 4.1 Relations to the Stochastic Kalman Filter ‣ 4 State Estimation ‣ From the Linear Quadratic Regulator (LQR) to the (Deterministic) Kalman Filter in Two Easy Steps") for an illustration.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Interpretations of $\\Sigma_{e}$ and $S$", "weight": 1.0} -->

Thus the matrix $S$ describes how "certain" the optimal filter is of its state estimates in various directions. Here "certainty" in the sense of the curvature of the functional (47 to the (Deterministic) Kalman Filter in Two Easy Steps")) can be thought of as the deterministic counterpart of "information" in the probabilistic setting. Note that the statements about eigenvectors of $\Sigma_{e} = S^{- 1}$ are reversed, e.g. the eigenvector of $\Sigma_{e}$ with largest eigenvalue represents the direction in which the estimate has highest variance, i.e. highest uncertainty. This is precisely the eigenvector of $S$ with lowest eigenvalue. Thus in the deterministic formulation of the Kalman filter, it is perhaps better to refer to $S$ as the "certainty matrix" rather than the "information matrix".

<!-- chunk {"id": "body-0107", "role": "body", "section": "Discussion", "weight": 1.5} -->

It is often stated that controllability and observability are dual notions, or that state-feedback and estimation involve some kind of duality. These notions of duality have been mentioned for decades in papers and textbooks. Recent work \[kim2025arrow\] has revisited these arguments from the point of view that duality usually involves a time reversal.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Discussion", "weight": 1.5} -->

It is not compelling to think of the LQR problem and the Kalman filter as dual problems since their respective structures are quite different. The LQR state-feedback controller is memoryless, while the Kalman filter has dynamics, namely the observer. It is more tempting to think of the LQ-tracking problem and the Kalman filter as duals. However, this does not completely hold. The LQ-tracking problem involves a specified initial state. Its dual through time reversal would be an estimation problem where the final state is known, which is not the case in the Kalman filter. The true dual of the Kalman filter, in the sense of time reversal, would be an LQ-tracking problem where the initial state is unknown. This latter problem however is somewhat fictitious since the solution (31 to the (Deterministic) Kalman Filter in Two Easy Steps")) requires state feedback.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Discussion", "weight": 1.5} -->

There is one conclusion that can be drawn from the similarity (rather than full duality) of the LQ-tracking problem and the Kalman filter on one hand, and their contrast with LQR on the other. Both tracking and estimation problems have dynamics, while the LQR controller is memoryless. Recall from Dynamic Programming that the optimal control for any objective of the form

<!-- chunk {"id": "body-0110", "role": "body", "section": "Discussion", "weight": 1.5} -->

is a memoryless state feedback ${u{(t)}} = {K\left( {x{(t)}},t \right)}$ for some mapping $K{(.,t)}$ from the state space to the set where the control takes its values. However, the objectives in both tracking and estimation are of the form

<!-- chunk {"id": "body-0111", "role": "body", "section": "Discussion", "weight": 1.5} -->

where the minimization is over the signals $x,u$, and $z$ is a fixed known signal ($r$ in the case of tracking, and $y$ in the case of estimation). Such problems are not of the form (48 to the (Deterministic) Kalman Filter in Two Easy Steps")) for which optimal inputs are memoryless state feedback. It is thus the presence of a fixed signal $z$ in the objective (49 to the (Deterministic) Kalman Filter in Two Easy Steps")) ($z$ is not to be optimized over) that results in optimal controllers with dynamics, even when state feedback is available.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Discussion", "weight": 1.5} -->

Finally we point out that the time-reversal argument between ${\mathsf{L}\mathsf{Q}\mathsf{R}}_{\mathsf{i}}$ and ${\mathsf{L}\mathsf{Q}\mathsf{R}}_{\mathsf{f}}$ in Section 1 to the (Deterministic) Kalman Filter in Two Easy Steps") applies just as well to non-linear dynamics and non-quadratic objectives. The time-reversed dynamics would be

<!-- chunk {"id": "body-0113", "role": "body", "section": "Discussion", "weight": 1.5} -->

The corresponding cost-to-go and cost-to-arrive value functions would simply be the time reversals of each other.
