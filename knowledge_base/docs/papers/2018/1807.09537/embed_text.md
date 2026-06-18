## Introduction

Formal verification, the process of algorithmically generating correctness certificates for a design, and falsification, the process of algorithmically finding trajectories and inputs that lead to a violation of specifications are important steps before a safety-critical control system can be deployed (fainekos2012verification annpureddy2011s sankaranarayanan2012falsification, ). An alternative to these approaches, when a control design is not available but a plant model and specifications are available, is to synthesize a controller that, by construction, guarantees that the specifications are satisfied by the closed-loop system (ozay2017guest, ). The key insight of this paper is to combine ideas from falsification and control synthesis to evaluate control designs for safety.

Consider the problem of evaluating a control design for an autonomous vehicle for safety. What would be a meaningful specification to run a falsification engine against in this case? The hard safety constraint -- "do not crash!" -- is easy to specify but can be trivially falsified. For instance, if a lead car, with very low speed, cuts in front of the autonomous car traveling with a relatively high speed, a crash is unavoidable. To get "interesting" corner cases, one might constrain the distance at which the lead car cuts in or the speed the lead car is traveling at when it cuts in. But can we systematically generate such constraints/assumptions? If a falsifying trajectory is found, can we say anything about existence of a controller that would be able to steer the vehicle to safety, or is safety simply an impossible task in this situation?

Motivated by these questions, in this paper we propose to use controlled invariant sets (blanchini1999survey, ) to generate interesting corner cases for falsification. By an interesting corner case, we mean initial conditions from which ensuring safety is hard but not necessarily impossible. We restrict our attention to piecewise affine control systems subject to external disturbances (e.g., behavior of the other cars on the road, road profile) and safety constraints given as unions of polyhedra. We propose a scheme to sample initial conditions from the boundary of the invariant set. We also consider the problem of searching for falsifying disturbances (in addition to initial conditions). To this effect, we compute the winning set of a dual game, where control inputs are treated as disturbances and disturbances are treated as control, and where the goal is to reach the unsafe set. The dual strategy obtained by solving the dual game can be used to generate falsifying inputs when the state is within the winning set of the dual game. Greedy heuristics that aim to push the states to the dual game winning set are also proposed.

As an additional advantage, in case a control design is found unsafe using the proposed method, we can supervise this unsafe controller with the controlled invariant set in order to guarantee safety while still using the unsafe controller, which may have favorable performance related properties (nilsson2016correct, ). This supervision idea is similar to the simplex architecture (bak2011sandboxing seto1998dynamic, ), where a performance controller is used together with a simpler controller that has a certified safety envelope and that overwrites the performance controller only when its actions risk safety.

We demonstrate the proposed approach using two autonomous driving functions: adaptive cruise control and lane keeping. Adaptive cruise control aims to regulate the longitudinal dynamics of a vehicle either to a desired speed or a desired headway to a lead vehicle. Lane keeping controls the lateral dynamics of a vehicle to track the center line of the lane. We present safety specifications for both functions. We then apply the proposed approach to a set of controllers, including Comma AI software, an open source autonomous driving package, to reveal potential corner cases leading to specification violation.

## Main Ingredients

Our goal in this paper is to search for interesting corner cases for falsification of closed-loop control systems. By interesting corner case, we mean a pair of initial condition and external (disturbance) input signal that leads to a trajectory violating a given safety specification, together with a certificate that it is possible to satisfy the specification for this initial condition and external input; therefore violation is indeed avoidable. We summarize the proposed framework in Figures 1 and 2 before detailing the different components.

Figure 1. Main workflow. Given a system model and a safety specification we synthesize a controlled invariant set contained inside the safe set and a winning set for the dual game. Based on these two objects we extract “interesting” initial conditions and disturbance strategies that are used to evaluate the safety of arbitrary (black-box) controllers.

Figure 2. In the evaluation phase, a (known) system model is controlled by a (black-box) controller. We discuss two settings, i.e., falsification (left) and supervision (right), for analyzing and enforcing safety of the closed-loop system respectively. In falsification, the outputs of the framework in Figure 1 are used to guide exploration of initial conditions (x0(i)) and disturbances (d) that lead to safety violations. As a by-product, a supervisor architecture that enforces invariance by rejecting potentially unsafe inputs (u) can be added around a controller that is found unsafe in the falsification step.

### Controlled Invariant Sets

Invariance properties are the most basic safety properties where the goal is to avoid an unsafe set at all times, and has been widely studied in the literature (blanchini1999survey, ). The maximal (robust) controlled invariant set is the set of all states inside the safe set from which there exists a controller that can guarantee remaining safe for all future times (under all possible realizations of uncertainty and disturbances).

Formally, we define a controlled invariant set for a continuous-time system using a tangent cone. Let $S$ be a set in ${\mathbb{R}}^{n}$; a vector $y \in {\mathbb{R}}^{n}$ is called a feasible direction of set $S$ at $x \in S$ if there exists $\varepsilon > 0$ such that ${x + {\deltay}} \in S$ for all $\delta \leq \varepsilon$. The tangent cone of a set $S$ at $x$ is then defined to be ${T_{S}{(x)}}:={\text{closure}{({\{ y\mid{y\text{~is feasible direction of~}S\text{~at~}x}\}})}}$. Consider a dynamical system described by the following differential equation

where $x \in X$ is the state, $u \in U$ is the control, and $d \in D$ is the disturbance. Here, $X$, $U$, and $D$ represent the set of possible states, controls, and disturbances, respectively. Set $S_{inv} \subseteq X$ is called controlled invariant under the dynamics in Eq. if (blanchini1999survey, )

where $\partial S_{inv}$ represents the boundary of set $S_{inv}$. Set invariance can be defined similarly for discrete-time control systems of the form

A set $S_{inv}$ is controlled invariant under dynamics in Eq. if

For simple linear system dynamics subject to additive disturbance or polytopic uncertainty, it is possible to approximate the maximal invariant set to an arbitrary precision (DeSantis:2004et rungger2017computing, ). In this paper, we used polytopic invariant sets, as is done in (smith2016interdependence nilsson2016correct pn_thesis2017, ). It is also possible to compute controlled invariant sets represented via barrier functions using sum-of-squares optimization (prajna2004safety, ) or approximate them via abstraction-based techniques (roy2011pessoa, ). Invariant set computation can be seen as a safety game between the control input $u$ and the disturbance $d$, where the maximal controlled invariant set corresponds to the winning set (i.e., the set of all the initial states from which $u$ can enforce safety irrespective of the values of $d$) in the game for the control input.

### Supervision

The controlled invariant set can be used to supervise a legacy controller to avoid violation of the safety constraint (nilsson2016correct, ), even when a controller for which a safety violation is found in the falsification step is used. The idea is to provide a recursive guarantee on safety by enforcing the trajectory to stay within a controlled invariant set $S_{inv}$ contained by the safe set. The supervisor is a set-valued map $\mathcal{P}$ that maps the current state $x_{c}$ to a set of control inputs ${\mathcal{P}{(x_{c})}} \subseteq U$. Under any control $u \in {\mathcal{P}{(x_{c})}}$, the next state stays within set $S_{inv}$ under all disturbance. The supervisor overrides the legacy controller in a minimally intrusive way. That is, the supervisor is active and provides a control input in set $\mathcal{P}{(x_{c})}$, whenever the legacy controller gives a control input outside $\mathcal{P}{(x_{c})}$ at state $x_{c}$. As shown in Fig. 2, when the legacy controller's input $u$ is in $\mathcal{P}{(x_{c})}$, we have the supervisor output $\overline{u} = u$.

To be specific, the set $\mathcal{P}{(x_{c})}$ can be constructed in the following way. Let ${x{({t + 1})}} = {F\left( {x{(t)}},{u{(t)}},{d{(t)}} \right)}$ be the discrete-time dynamics. We define the set

Given the current state $x_{c}$, set $\mathcal{P}{(x_{c})}$ is obtained by fixing the $x$ component of the points in $\mathcal{P}$ to be $x_{c}$, i.e., ${\mathcal{P}{(x_{c})}}:={\{{{(x,u)} \in \mathcal{P}}\mid{x = x_{c}}\}}$. In particular, under the assumption that $S_{inv}$ is a polyhedron (or a union of polyhedra, resp.), $F$ is linear in $x$, $u$, $d$, and $D$ is a polyhedron, then $\mathcal{P}$ can also be represented as a polyhedron (or a union of polyhedra, resp.).

### Sampling of the Boundary

We sample the boundary of the controlled invariant set to obtain potentially interesting initial conditions. As mentioned before, the focus in this paper is on controlled invariant sets that can be represented as a finite union of polyhedra. Figure 3 illustrates the boundary sampling scheme of a polyhedron-union set. The gray shaded area is the union of the polyhedra. We assume the union set is contained within a hyper-rectangular domain, and sample along the first $n - 1$ dimensions of the domain. These samples corresponds to the red dots in the figure. Then the red dots are projected onto the boundary of the invariant set, which are marked by the blue circles in the figure. In particular, this projection can be done by the following procedure.

We first project each red dot $y$ onto the boundary of each polyhedron $P = {\{{x \in {\mathbb{R}}^{n}}\mid{{Ax} \leq b}\}}$ in the collection. To be specific, we fix the first $n - 1$ coordinates of points $x$ inside polyhedron $P$ to be the same as the red dot $y$. This gives 1 dimensional polyhedron

We then compute the vertex representation of the set $P_{y}$ using MPT3 (herceg2013multi, ).

The vertices of $P_{y}$ are admitted if they are not in the interior of other polyhedra.

### Remark 1

The proposed sampling scheme can be extended to the case where the controlled invariant set is represented as the union of convex sets in form of $C = {\{{x \in {\mathbb{R}}^{n}}\mid{{{f_{j}{(x)}} \leq 0},{j = {1,\ldots,m}}}\}}$. Similar to step 1) in the above procedure, set $C_{y}$ is created as

Set $C_{y}$ is a 1-D interval whose bounds can be computed by solving 1-D convex optimization problems $\min{\{{{x_{n} \mid x} \in C_{y}}\}}$ and $\min{\{{{- {x_{n} \mid x}} \in C_{y}}\}}$. Also note that a union of convex sets is not necessarily convex and may contain holes. Our proposed approach is able to sample the boundary of the holes as well.

Figure 3. Sampling the boundary of a union of polyhedra.

For other types of sets, there is a brief survey in (ghosh2013nearly, ) on the existing approaches to sample the surface of nonconvex polyhedra. Other methods for generating (asymptotically) uniform samples on a polytope's boundary include the shake-and-bake method (smith1984pointsuniform boender1991shakeandbake, ), and sweep plane method (Leydold98asweep-plane, ), and these can be used as alternatives to the approach described above.

### Computing the Falsifying Inputs

### Dual Game

A falsifying scenario consists of two parts: an initial condition and a disturbance input profile. In this part, we show how to compute a falsifying input profile, through solving the so called dual game, given that the initial condition is outside the maximal invariant set. Theoretically, if the initial state is already outside the maximal invariant set, there exists a disturbance input profile that steers the trajectory outside the safe set. However, if the disturbance profile is not selected carefully, it does not necessarily lead to falsification.

Figure 4. Illustration: objective of the dual game

We first define some terminology. Let the system dynamics be given by Eq., and let $S_{\text{safe}}$ be the safe set we want to stay inside for all time. The invariance game aims at finding the largest controlled invariant set $S_{\text{inv}} \subseteq S_{\text{safe}}$. Figure 4 shows the objective of its dual game: we want to find set $S_{\text{dual}}$, and a dual strategy $g:{S_{\text{dual}}\rightarrow D}$, under which the states starting from $S_{\text{dual}}$ is steered into unsafe set $S_{\text{unsafe}}:={(S_{\text{safe}})}^{C}$ in finite time, as long as $u \in U$.

We solve the dual game by computing the backwards reachable set of unsafe set $S_{\text{unsafe}}$. For linear discrete-time dynamics, assuming that unsafe set $S_{\text{unsafe}}$ is a polytope, the backwards reachable set can be computed as a collection of polytopes using the same approach in (nilsson2016correct, ). The only difference is that we are now "controlling" the disturbance $d$ and trying to be robust to the real control action $u \in U$. To be specific, let the dynamics be

where $x \in X$, $u \in U$, $d \in D$ are polytopes. We first compute a sequence of polytopes, starting with $P_{0} = S_{unsafe}$, as follows:

We then project each polytope $P_{i}$ onto $X$ space to obtain $\{{\overline{P}}_{i}\}$, and the winning set of the dual game is given by $\bigcup_{i}{\overline{P}}_{i}$. To determine the dual game strategy $g$ at the current state $x$, we locate $x$ in one of the projected polytopes ${\overline{P}}_{i}$, and the dual strategy can be generated by picking $g{(x)}$ such that ${(x,{g{(x)}})} \in P_{i}$.

When $S_{unsafe}$ is nonconvex but can be expressed as a union of polytopes, we compute the backwards reachable set for each polytope and take the union of the obtained backwards reachable sets. This gives a conservative, yet sound, winning set for the dual game. Note that, when the invariant set or the winning set for the dual game is computed via such a conservative approach, there will be a gap between $S_{\text{inv}}$ and $S_{\text{dual}}$ in Fig. 4, corresponding to a set of initial conditions for which concluding whether they are "interesting" or not is not possible with the computed sets.

### Ellipsoid Method

Note that the dual strategy $g$ is defined on $S_{\text{dual}}$ and is not applicable everywhere on $S_{\text{safe}}$. Thus we need a *complementary strategy* $g^{c}$ to generate falsifying inputs for states $x \in {S_{\text{safe}} \smallsetminus S_{\text{dual}}}$. Next, we propose some heuristics for computing a complementary strategy. Assume that the safe set is given as a union of polyhedra $S_{\text{safe}} = {\cup_{i}S_{\text{safe},i}}$ and $C_{\text{safe}}$ denotes the convex-hull of $S_{\text{safe}}$. It is shown in (john2014extremum, ) that, for any compact set $C$, there exists a unique minimum volume ellipsoid (called *LJ-ellipsoid* of $C$) covering it. Denote the LJ-ellipsoid of $C_{\text{safe}}$ with $E_{\text{safe}}$, which is defined as

where the positive definite matrix $Q$ parametrizing the ellipsoid can be computed using (rimon1992efficient, ). Define the *level* of $x \in X$ as

It is reasonable to assume that points lying on the higher levels are closer to the unsafe set; hence, driving the system to higher levels would force it either to the unsafe set $S_{\text{unsafe}}$ or to the winning set of the dual game $S_{\text{dual}}$. With this intuition, complementary strategy $g^{c}:{{S_{\text{safe}} \smallsetminus S_{\text{dual}}}\rightarrow D}$ is defined such that it steers the system to the highest possible level set at each step:

where we assume that control input $u$ is known.^11^1When the invariant set is unbounded, LJ-ellipsoid does not exist. In this case $g^{c}$ can be computed by computing inputs that steer the state closer to $S_{\text{dual}}$ by directly minimizing the distance to $S_{\text{dual}}$ though the corresponding optimization problem can be more complex. Alternatively, if the rays corresponding to unbounded directions are known, an ellipsoid that is significantly elongated along those directions can be chosen by bounding those rays at a large enough level.

Falsifying inputs are computed using $g$ if the current state $x \in S_{\text{dual}}$, and $g^{c}$ is used otherwise (see Fig. 2). Additionally, we develop some simple input-generation heuristics tailored for the ACC and LK functions of autonomous driving. These tailored heuristics will be presented on the fly in Section 4.

## System model and specifications

For the case studies we consider two autonomous driving subsystems: adaptive cruise control and lane keeping. An adaptive cruise controller (ACC) controls the speed of the vehicle to follow a desired speed if there is no car in front, and to follow the lead vehicle within some safe following distance (headway) if there is a relatively slower lead vehicle in front. A lane keeping (LK) controller controls the steering of the vehicle to avoid lane departures. Therefore, adaptive cruise control controls the longitudinal dynamics and lane keeping control deals with the lateral dynamics. In the rest of this section, we provide dynamical models used in our examples and formalize safety specifications for both systems.

### Longitudinal and Lateral Dynamics

We use the following model from (nilsson2016correct, ) to describe the longitudinal dynamics of the vehicle:

The system states consist of the following car velocity $v$, lead car velocity $v_{L}$, and the headway $h$ (i.e., the relative distance between the lead and following car). Control input $F_{w}$ represents the net force acting on the mass of the following car. The lead car acceleration $a_{L}$ can be viewed as a disturbance to the system. Finally, constants $m$, $f_{0}$, $f_{1}$ and $f_{2}$ are parameters of the model. The values of these parameters and the bounds of the variables can be found in Table 1. In particular, the domain the dynamics are defined on is $X_{ACC}:={{\lbrack v^{\min},v^{\max}\rbrack} \times {\lbrack h^{\min},\infty)} \times {\lbrack v_{L}^{\min},v_{L}^{\max}\rbrack}}$.

car+cargo mass

friction/drag term

friction/drag term

friction/drag term

minimal car velocity

maximal car velocity

desired car velocity

minimal force, comfort

maximal force, comfort

minimal force, physical

minimal force, physical

minimal time headway

Table 1. Parameter values for the ACC model

The lateral dynamics are described by

where the states are: lateral deviation from the center of the lane ($y$), the lateral velocity ($\nu$), the yaw-angle deviation in road-fixed coordinates ($\Delta\Psi$), and the yaw rate ($r$), respectively. The input $\delta_{f}$ is the steering angle of the front wheels, which is limited to lie within $\theta_{s}^{\min}$ and $\theta_{s}^{\max}$; and $r_{d}$ is the desired yaw rate, which we interpret as a time-varying external disturbance and computed from road curvature by $r_{d} = {v/R_{0}}$ where $R_{0}$ is the (signed) radius of the road curvature and $v$ is the vehicle's longitudinal velocity. Other parameters include $m$, the total mass of the vehicle, and $a$, $b$, $C_{\alphaf}$, and $C_{\alphar}$, which are vehicle geometry and tire parameters. All values can be found in Table 2. Accordingly, the domain the dynamics are defined on is $X_{LK}:={{\lbrack{- y^{\max}},y^{\max}\rbrack} \times {\lbrack{- \nu^{\max}},\nu^{\max}\rbrack} \times {\lbrack{- {\Delta\Psi^{\max}}},{\Delta\Psi^{\max}}\rbrack} \times {\lbrack{- r^{\max}},r^{\max}\rbrack}}$.

car+cargo mass

car moment of inertia

vehicle geometry parameter

vehicle geometry parameter

maximum lateral deviation

maximum lateral velocity

maximum yaw-angle deviation

maximum yaw rate

minimum steering angle

maximum steering angle

Table 2. Parameter values for the LK model

### Formal Specifications for ACC and LK

For ACC, we focus on the safety aspect of requirement in this work. The (safety part of) ISO Standard requirements for Adaptive Cruise Control Systems (isoACCstandard, ) state:

the control input should stay within specified bounds all the times.

whenever the lead car is close in the sense that the headway $h < {v^{des}\omega^{des}}$, the time headway $\omega$ needs to satisfy $\omega \geq \omega^{\min}$ at all times.

We extract the safety part of the above ISO requirement and express it formally in logic. Define sets

Set $M$ is the set of states where the lead car is close, set $S$ is the safe set of states, and set $S_{U}$ contains the allowable control inputs. Adding the speed limits encoded by the domain $X_{ACC}$, the overall specification can be expressed as

To check safety in the presence of a close enough lead car, we assume the states are in $M$ and consider the following safety specification, denoted by $\varphi_{ACC}$:

In the later falsification experiments, we will consider violations of different aspects of the specification $\varphi_{ACC}$, that is,

These three safety specifications correspond to small time headway, small distance headway, and crash, respectively. Note that specification $\varphi_{ACC}^{2}$ implies $\varphi_{ACC}^{3}$ as $h^{\min} > 0$. Here we distinguish specification $\varphi_{ACC}^{3}$ from $\varphi_{ACC}^{2}$ because violating $\varphi_{ACC}^{3}$ is considered to be more severe.

For LK, as mandated by the width of roads in the United States (approx. $3.8$m) and typical car widths (approx. $2$m), the specification states that the car must stay within $y^{\max}$ meters of the center of the lane, i.e. ${|{y{(t)}}|} \leq y^{\max}$. We also require the other states to remain in the domain $X_{LK}$ as larger values of these states are either physically less meaningful (e.g., can correspond to the vehicle navigating in the reverse direction) or violate passenger comfort requirements. Moreover, the lateral dynamics model we use is valid for relatively smaller ranges of yaw rate, yaw angle and lateral velocity. With these requirements, the overall specification for LK, denoted by $\varphi_{LK}$, is formally stated as:

Note that state $y$ being out of bound should be considered to be a significant safety violation, while the other three states in $x_{LK}$ being out of bounds leads to a less comfortable ride. Therefore, we will independently count the violations of the specification below in the falsification experiments:

## Case studies

In this section, we evaluate the proposed approach on case studies with different controllers for adaptive cruise control and lane keeping.

In what follows, both the wheel force $F_{w}$ and the steering angle $\delta_{f}$ are bounded quantities. Thus, for controllers that cannot handle such input constraints, we use a saturation function before feeding their output to the system. The saturation function $sat$ is defined as follows:

In addition to sampling at the boundary of the invariant set, we also sample in the interior of the invariant set to generate less "trickier" initial conditions. These interior points are obtained by shifting (for ACC) or scaling (for LK) the boundary samples.

### Adaptive Cruise Control Results

We computed a controlled invariant set $S_{ACC}$ for the longitudinal dynamics in, and sampled the boundary of this set with the proposed approach to find falsifying initial conditions. The disturbance profile is computed by (i) solving the dual game, (ii) a simple heuristic that corresponds to the lead car doing a maximum braking, or (iii) the lead car trying to achieve $v^{des}$. We explored the following three classes of controllers for meeting the ACC requirement.

For the first controller, we performed feedback linearization followed by pole placement with a hybrid proportional (P) controller, defined as:

where $k_{P}$ is the proportional gain, the $\min$ part takes care of the two different ACC modes and $F_{w} = {sat_{F_{w,c}^{\min}}^{F_{w,c}^{\max}}{(u)}}$ given the input saturations.

We also consider hybrid proportional-integral (PI) controllers with the following dynamics:

where $e{(t)}$ is the error state and $k_{I}$ is the integral coefficient. Similarly, the control input $u$ needs to be saturated to obtain practical $F_{w}$.

We also designed an MPC controller with a linearized discrete-time model with a sampling period of $0.1$s using the following formulation:

where $v_{0}$, $h_{0}$, $v_{L,0}$ are the initial conditions and $T$ is the length of the prediction horizon. Since the objective contains term $\min{(v^{des},{{h{(t)}}/\omega^{des}})}$, the MPC is hybrid in its nature. To simplify the computation load, we replace the target velocity throughout the predicting horizon by $\min{(v^{des},{{h{}}/\omega^{des}})}$, so that the MPC problem can be solved by a QP solver.

Tables 4-7 summarize the falsification rates for the samples both from the interior and the boundary of the controlled invariant set $S_{ACC}$, with disturbance $a_{L}$ profile generated by multiple methods. It should be noted that the same controlled invariant set $S_{ACC}$ is used to generate initial states to investigate the three different aspects of the safety specification in Eq.. This is because set $S_{ACC}$ is synthesized against the overall safety specification in Eq.. Overall, the MPC controller seems better than the naively designed P controller in terms of safety.

Another key observation is that the falsification rates of the test cases with interior initial conditions can be higher or lower than those on the boundary of set $S_{ACC}$, depending on how the disturbance (i.e., $a_{L}$) profile is generated. In particular, the test cases with interior initial conditions have higher falsification rate than the boundary cases in Table 4-6, and usually have lower falsification rate in Table 7. The key difference between Table 4-6 and Table 7 is that the leading car is usually decelerating (or maintaining speed constant) in the test cases from Table 4-6, while it is accelerating under the test cases from Table 7. In what follows we briefly discuss how this difference affects the falsification rates by the interior initial conditions and by the boundary ones.

When the lead car is decelerating, the dynamics tend to have a "steady state" outside the controlled invariant set $S_{ACC}$. This is true because the lead car's deceleration shortens the headway $h$ and hence pushes the state towards the boundary of $S_{ACC}$. In this case, the falsifications are due to the long term behavior of the dynamics as a trajectory may eventually leave $S_{ACC}$ Since such undesired behaviors occur in a longer term, starting from the interior of set $S_{ACC}$ may not prevent ultimate falsification.

Moreover, the trajectories initiating from the interior tend to move to the "trickier" parts of the boundary, where safe actions are limited, which increases the falsification rate. We next explain why this is so. First note that a point in the interior of $S_{ACC}$ usually has larger relative headway $h$ and larger lead car velocity $v$. Consequently, the target velocity defined by $\min{(v^{des},{h/\omega^{des}})}$ has a higher chance to be equal to $v^{des}$ when starting from the interior. The controller hence accelerates to achieve $v^{des}$ and maintains the velocity there. Now since the lead car velocity $v_{L}$ is low (due to deceleration or small initial value), such acceleration will eventually lead to small headway $h$, which will change the target velocity from $v^{des}$ to $h/\omega^{des}$. At that moment, however, the following car velocity may be already relatively high. This hence leads to a harder scenario and increases the chance of falsification, which explains the result in Table 4-6.

On the contrary, when lead car's steady state speed is $v^{des}$, i.e. it is mostly accelerating, the dynamics tend to have a "steady state" inside the set $S_{ACC}$. This is true because the lead car's acceleration enlarges headway $h$ and pushes the state towards inside of $S_{ACC}$. In this case, the falsifications are mainly due to the transient state of the dynamics because the state will eventually converge to that steady state inside $S_{ACC}$. By our conjecture, the initial conditions on the boundary of $S_{ACC}$ have higher chances for capturing the falsifications due to transient state. This explains why the falsification rate in Table 7 agrees with our conjecture.

To summarize, initial conditions on the boundary help identify safety violations in the transient behavior, whereas input generation techniques tend to capture safety violations due to persistent disturbances (i.e., "steady state").

### Lane Keeping Results

Let us denote the state vector ${\lbrack y,\nu,{\Delta\Psi},r\rbrack}^{\top}$ in Eq. as $x_{LK}$. We computed a controlled invariant set $S_{LK}$ for the lane keeping model in, sampled the boundary of this set with the proposed approach to find falsifying initial conditions, and use various input generation methods to generate road profiles. We explored three classes of controllers for meeting the lane keeping requirement:

A proportional (P) state feedback controller, defined as

Several P controllers are designed by placing the poles in different locations. The control input $\delta_{f}$ is obtained by saturating $u$ to account for the practical limit of the actuator, i.e., $\delta_{f} = {sat_{\theta_{s}^{\min}}^{\theta_{s}^{\max}}{(u)}}$.

A proportional-integral (PI) controller, defined as

where ${\overset{\sim}{x}}_{LK}$ expands $x_{LK}$ to include an error state $e$:

Several PI controllers are designed by choosing different pole locations. Similarly, the control input $\delta_{f}$ is obtained by saturating $u$ accordingly.

An MPC controller with the following formulation:

Since the input saturation is accounted for by the constraints in the MPC formulation, control input $\delta_{f} = u$. where $x_{0}$ is the initial condition, and $Q = {\text{diag}{({\lbrack 1\ 0\ 0\ 0\rbrack})}}$.

Table 8 summarizes the falsification rates for the above three controllers. The initial conditions are generated by sampling the interior and the boundary of set $S_{LK}$, and the disturbance profiles are generated using ellipsoid method plus dual game and using a heuristic described as follows:

where $\tau$ is the sampling time of the discrete-time system.

Overall, our MPC design seems safer than the PI design, which is safer than the P controller. Note that none of these designs are tuned properly, the goal is just to demonstrate how controlled invariant sets can be used to evaluate different designs.

Figure 5. The output of a diff utility showing the modification in Comma AI. Left: Comma AI*, right: Comma AI.

Proportional controller (P gain)

State feedback (poles)

State feedback w/ integral action (poles)

Table 3. Controllers used in our tests

Table 4. ACC falsification rates (FR), with no input generation, for specifications in Eqs. and.

Table 5. ACC falsification rates (FR), with dual game, for specifications in Eqs. and.

Table 6. ACC falsification rates (FR), with max braking, for specifications in Eqs. and.

Table 7. ACC falsification rates (FR), with lead car converging to vdes, for specifications in Eqs. and.

Ellipsoid method + dual game

Table 8. LK falsification rates (FR), with input generation, for specifications in Eqs. and.

Heuristic (max brake)

Ellipsoid method + dual game

aLead = K(vLead -v_des)

Table 9. ACC falsification rates (FR): Comma AI, for specifications in Eqs. and.

Comma AI* (without modification)

Ellipsoid method + dual game

Table 10. LK falsification rates (FR): Comma AI &amp; Comma AI* (without modification), for specifications in Eqs. and.

### Comma AI

Our framework is flexible enough to evaluate any type of controller as long as their inputs and outputs match the inputs and outputs of the system models used. We can also directly use the source code of a controller after developing a proper interface. In this section, we demonstrate our framework on an open source real-world autonomous driving package developed by Comma AI, a start-up working on self-driving car technologies (see [https://comma.ai/](https://comma.ai/)). However, since we are just using a simplified model for the vehicle dynamics, the interface might not accurately reflect the performance of the software on an actual car. This can be improved by improving the models and interfaces, but the goal in this section is to simply show the applicability of the framework on realistic control software rather than accurately mimicking the performance.

We describe how we interfaced the Comma AI code (commit 5524dc8^22^2After we settled on a version of Comma AI to use for this project, newer versions of the Comma AI code have changed the lane-keeping module from using a PI to an MPC-based controller. Testing this new controller within our framework is the subject of future work. at [https://github.com/commaai](https://github.com/commaai)) with our ACC and LK framework. The Comma AI code is written in Python. We call the Python code directly from within Matlab by developing appropriate wrappers for input/output matching as described next.

The ACC module of Comma AI outputs two values: gas and brake commands, each normalized to $\lbrack 0,1\rbrack$. We scale these gas and brake commands by the physical gas and brake limits of average mid-sized sedans, $F_{w,p}^{\max}$ and $F_{w,p}^{\min}$, respectively. We then clip the scaled gas and brake commands to the comfort bounds $\lbrack 0,F_{w}^{\text{max}}\rbrack$ and $\lbrack F_{w}^{\text{max}},0\rbrack$, respectively. The sum of the scaled gas and brake commands is used as the control input to our system.

The LK module of Comma AI requires extra interfacing with our simulations. Firstly, Comma AI outputs a control between $u \in {\lbrack{- 1},1\rbrack}$, and we assume that these bounds map linearly onto the range of steering angles $\lbrack\theta_{s}^{\min},\theta_{s}^{\max}\rbrack$. Secondly, Comma AI takes as input the road profile, at $dR_{c}$ discretization, for the upcoming 50 m, which is measured along the tangent line of the current car configuration. To provide this at time step $T$,

We compute a sequence of future road curvature disturbances ${r_{d}^{1:n}{(T)}} \doteq {{\{ d_{t}\}}_{t = 1}^{n}{(T)}}$, where $n \geq 50$ using one of the input generation methods. To be consistent with prior road profiles, we fix ${r_{d}^{1:{n - 1}}{(T)}} = {r_{d}^{2:n}{({T - 1})}}$ and only compute $r_{d}^{n}{(T)}$ from scratch. In principle, we can compute $r_{d}^{1:n}{(T)}$ entirely from scratch; this setting can be interpreted as driving with Comma AI vision sensor failure/noise, leading to inconsistent roads from prior time steps. However, by ensuring that we provide consistent roads, we give Comma AI the advantage here by assuming that the vision data is exact.

Assuming that the $r_{d}^{1:n}{(T)}$ trajectory was obtained from measurements taken at a rate of $dT_{c}$ of the vehicle traveling at $v_{N}$ m/s on the center line, we can estimate the center line in road-fixed coordinates, $R_{d}^{1:n}{(T)}$, by approximating that the road traces out arcs of angle $r_{d}^{i}dT_{c}$ at every time step $i$. That is,

Since $R_{d}$ is relative to a road-fixed coordinate system, we rotate and translate $R_{d}$ into the car frame by rotating each waypoint by $- {\Delta\Psi}$ and translating by $- y$ (denoted $R_{d}^{\prime}{(T)}$).

We evaluate $R_{d}^{\prime}{(T)}$ values at a discretization of 1 m along the tangent line using linear interpolation.

Additionally, we modified one of the vehicle model equations in the original Comma AI code (see Figure 5). We will refer to the original Comma AI code as Comma AI\*, and to our modified code as Comma AI, which performs better with our interface.

Figures 7 and 8 show a trajectory generated by Comma AI and Comma AI\*, respectively, that leaves the lane boundaries, overlaid by the trajectory generated by Comma AI and Comma AI\* when they are used as the legacy controller when the invariant set based supervisor is active.

We see that for ACC, Comma AI manages to stay out of crashes for all initial conditions and input generation method; however, it violates time and distance headways many times, as Table 9 suggests. These violations are undesirable since the passengers might feel uncomfortable when Comma AI follows the lead car too closely. Furthermore, the Comma AI code itself sets a soft constraint for the desired distance headway being greater than 4m, which is frequently violated.

The LK statistics in the left half of Tables 10 indicate that while Comma AI stays within the lane boundaries for the most part when starting from nonzero initial conditions, in the process of stabilization, it tends to violate comfort bounds. Falsification is more likely starting from initial conditions in the boundary than in the interior. Comma AI\* (see the right half of Table 10) drives slightly better on straight roads but performs much worse with input generation compared to Comma AI, which is consistent with the decent performance of Comma AI\* on simple roads. The ellipsoid + dual game method of input generation seems to falsify Comma AI and Comma AI\* more than the heuristic method; in fact, a straight road tends to falsify Comma AI and Comma AI\* more than the heuristic method. This happens because the heuristic method tends to smooth out the natural overshoot that Comma AI and Comma AI\* exhibit in their responses.

Figure 6. Un/supervised ACC trajectories using Comma AI

Figure 7. Un/supervised LK trajectories using Comma AI

Figure 8. Un/supervised LK trajectories using Comma AI*

### S-TaLiRo Results

For comparison and benchmarking purposes, we use S-TaLiRo, a falsification tool that is proposed in (annpureddy2011s, ), to find falsifying initial conditions and disturbance trajectories. Although S-TaLiRo and our approach are somewhat complementary, we try to demonstrate some of the differences. First, note that S-TaLiRo does not provide any information about whether a falsifying initial condition disturbance pair is "interesting", so it is not known if the violation is due to poor performance of the controller or it is unavoidable. To demonstrate to what extent S-TaLiRo can find "interesting" falsifying trajectories, we use the ACC example. We restrict the initial conditions that S-TaLiRo can choose by upper-bounding the headway $h \leq {200m}$. Let, $X_{0}:={{\lbrack v^{\min},v^{\max}\rbrack} \times {\lbrack h^{\min},200\rbrack} \times {\lbrack v_{L}^{\min},v_{L}^{\max}\rbrack}}$. Then, the specification used in S-TaLiRo for falsification is

In addition, we impose bounds on the external inputs, i.e., ${a_{L}{(t)}} \in {\lbrack a_{L}^{\min},a_{L}^{\max}\rbrack}$ for all $t$; and the domain of the dynamics is accounted for by the simulation model. Note that by the assumptions on the initial conditions and $v_{L}$ in (4.4), we avoid some of the trivially unsafe falsifications. To falsify $P$ and $PI$ controllers and Comma AI, we limit the number of samples S-TaLiRo can try to find a falsifying trajectory to $100$; this acts as a timeout condition. We then run S-TaLiRo for $100$ times with the default option of simulated annealing, a random search method. Table 11 summarizes the results, showing not all falsifying trajectories found by S-TaLiRo are "interesting". Furthermore, S-TaLiRo sometimes fails to falsify $P$ and $PI$ controllers before our timeout condition, whereas Table 5 shows that the dual game approach always finds inputs that lead to falsification.

We also provide S-TaLiRo with initial conditions sampled from the invariant set boundary, therefore forcing it to find "interesting" initial conditions. These results are reported in the last column of Table 11. Although S-TaLiRo finds fewer falsifying trajectories for some controllers in this case, all of the falsifying trajectories found are "interesting" by definition. Comparing the last column in Table 11 with that in Tables 5 and 9, we see that our input generation does better for most controllers except for Comma AI, for which S-TaLiRo has a slightly higher falsification rate.

Finally, we give S-TaLiRo $111$ initial conditions from the winning set of the dual game. S-TaLiRo takes 43secs to falsify all the points whereas dual game takes 170secs. This is partly due to the fact that the inputs selected by dual game input generation are arbitrary (within the winning inputs) but not necessarily aggressive, which can be mitigated by including an objective function in input generation phase. It is also worth mentioning that for these initial conditions, our approach is guaranteed to find a falsifying trajectory however S-TaLiRo does not have such a guarantee due to its random nature.

Table 11. ACC falsification with S-TaLiRo. The Falsified column shows the fraction of times S-TaLiRo finds a falsifying trajectory/initial condition pair for the specification (4.4) before timing out. The invariant set column shows the fraction of times a falsifying pair with an “interesting” initial condition is found among all runs. The last column shows the falsification rate when S-TaLiRo is given initial conditions sampled from the boundary of the invariant set.

## Conclusions and Discussion

This paper proposed a simple idea on how to use controlled invariant sets and solutions from a dual game to generate interesting corner cases that can be used for falsification of safety specifications. We illustrated the effectiveness of this idea with an extensive case study on two autonomous driving functions, namely adaptive cruise control and lane keeping, with various types of controllers, including an open source autonomous driving package Comma AI. Our simulations show that we can identify corner cases with synthesis techniques and also supervise existing controllers to avoid failure in such corner cases.

The proposed approach should not be considered as an alternative to falsification techniques, as it is limited to safety specifications and to cases where approximating the maximal invariant set is possible. Therefore, it requires some knowledge of the system dynamics although it is agnostic to the controller. Whereas, advanced falsification engines (annpureddy2011s, ) can handle rich specifications given in signal temporal logic, and even black-box system models. On the other hand, we believe our approach can be used to seed falsification engines by applying it to the safety part of a specification, a direction for future research.
