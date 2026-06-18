<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Control Barrier Functions: Theory and Applications

Topics include Robotics, Control barrier functions, Safety, Optimization, Control.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper provides an introduction and overview of recent work on control barrier functions and their use to verify and enforce safety properties in the context of (optimization based) safety-critical controllers. We survey the main technical results and discuss applications to several domains including robotic systems.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

It is easy to agree that any engineered system should be designed to be *safe*. In fact, the term *safety-critical* system is many times used to distinguish those systems for which safety is a major design consideration. But what exactly is *safety*? How do we define it and how can we design systems to achieve it? The notion of safety was first introduced in 1977 in the context of program correctness by Leslie Lamport and formalized, see also. Intuitively, safety requires that "bad" things do not happen while liveness requires that "good" things eventually happen, e.g., asymptotic stability can be seen as an example of a liveness property in the sense that an asymptotically stable equilibrium point is eventually reached. Dually, invariance can be seen as an example of a safety property in the sense that any trajectory starting inside an invariant set will never reach the complement of the set, describing the locus where bad things happen. Based on the identification of liveness with asymptotic stability and safety with invariance, it can be argued that safety has received much less attention in control theory than liveness.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, the notion of Lyapunov function has played a predominant role in the investigation of liveness properties.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The objective of this paper is to refocus the discussion on safety by introducing control barrier functions that play a role equivalent to Lyapunov functions in the study of liveness properties. There are two main reasons driving a surge in research related to safety and control barrier functions: 1) the recent interest in autonomous systems has brought safety to the forefront of systems' design. In particular, autonomous systems are expected to operate in unknown and unstructured environments which makes it considerably harder to enforce safety properties; 2) the recent introduction of control barrier functions suggests that many control design techniques based on Lyapunov and control Lyapunov functions can be suitably transposed to address safety considerations. Hence, we have both the societal need for safety as well as the tools to raise safety to the same level of maturity than liveness in the design of control systems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "I-A Brief History of Barrier Functions", "weight": 1.0} -->

The study of safety in the context of dynamical systems dates back to the 1940's when Nagumo provided necessary and sufficient conditions for set invariance (see for a more detailed historical account, and for a modern proof).

<!-- chunk {"id": "body-0007", "role": "body", "section": "I-A Brief History of Barrier Functions", "weight": 1.0} -->

In particular, given a dynamical system $\overset{˙}{x} = {f{(x)}}$ with $x \in {\mathbb{R}}^{n}$, assuming that the safe set $\mathcal{C}$ is the superlevel set of a smooth function $h:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$, i.e.,

<!-- chunk {"id": "body-0008", "role": "body", "section": "I-A Brief History of Barrier Functions", "weight": 1.0} -->

These conditions have been independently re-discovered on multiple occasions; in particular, around the 1970s by Bony and Brezis (the proof in follows Brezis).

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-A Brief History of Barrier Functions", "weight": 1.0} -->

In the 2000's we saw another change of perspective brought by the need to verify hybrid systems. Barrier certificates were introduced as a convenient tool to formally prove safety of nonlinear and hybrid systems; these results, again, seemed to independently discover Nagumo's theorem. The choice of the term "barrier" was motivated by its use in the optimization literature where barrier functions are added to cost functions to avoid undesirable regions. In the case of barrier certificates, one considers an unsafe set $\mathcal{C}_{u}$ and a set of initial conditions $\mathcal{C}_{0}$ together with a function $B:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ where ${B{(x)}} \leq 0$ for all $x \in \mathcal{C}_{0}$ and ${B{(x)}} > 0$ for all $x \in \mathcal{C}_{u}$. Then $B$ is a barrier certificate if

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-A Brief History of Barrier Functions", "weight": 1.0} -->

In the notation for $\mathcal{C}$ above, by picking the safe set to be the complement of the unsafe set $\mathcal{C} = \mathcal{C}_{u}^{c}$, with ${B{(x)}} = {- {h{(x)}}}$ the barrier certificate conditions become: ${\overset{˙}{h}{(x)}} \geq 0$ which implies that $\mathcal{C}$ is invariant. Therefore, these conditions reduce to those of Nagumo's theorem on the boundary. Importantly, the necessity of barrier certificates were studied along with their extension to a stochastic setting.

<!-- chunk {"id": "body-0011", "role": "body", "section": "I-A Brief History of Barrier Functions", "weight": 1.0} -->

As a means to extend the safety guarantees beyond the boundary of the set, there have been a variety of approaches that can be best described as "Lyapunov-like." That is, Lyapunov functions yield invariant level sets so, if these level sets are contained in the safe set one can guarantee safety---importantly, these conditions can be applied over the entire set and not just on the boundary. In this case, as developed, one constructs a "barrier Lyapunov function" $B$ much as above but with the additional requirement that it is, for all intents and purposes, positive definite. Then, by enforcing the condition that $\overset{˙}{B} \leq 0$ over the set $\mathcal{C}$, it ensures invariance of this set and thus safety. The major limitation is that, while these conditions ensure safety they also enforce invariance of *every* level set. Thus, they are overly strong and conservative.

<!-- chunk {"id": "body-0012", "role": "body", "section": "I-A Brief History of Barrier Functions", "weight": 1.0} -->

While the above results addressed closed dynamical systems, i.e., systems without inputs, the work on *viability theory* extended them to open dynamical systems, e.g., control systems given by $\overset{˙}{x} = {{f{(x)}} + {g{(x)}u}}$ for $u \in U \subset {\mathbb{R}}^{m}$. This required moving from invariant sets to controlled invariant sets: sets that can be made invariant by suitably designing a controller.

<!-- chunk {"id": "body-0013", "role": "body", "section": "I-A Brief History of Barrier Functions", "weight": 1.0} -->

The notion of a barrier certificate was extended to a "control" version to yield the first definition of a "control barrier function" ---although this definition is different than the one considered in this paper.

<!-- chunk {"id": "body-0014", "role": "body", "section": "I-A Brief History of Barrier Functions", "weight": 1.0} -->

These ideas were built upon so as to explicitly combine barrier functions with control Lyapunov functions ---this was done contemporaneously with the development of the methods presented in this paper which use optimization based controllers to unify Lyapunov and barrier functions. In particular, as further developed, conditions were given on creating "control Lyapunov barrier functions" that jointly guarantee safety and stability. Yet, in these cases the conditions in the end reduce to enforcing ${\overset{˙}{h}{(x,u)}} \geq 0$. However, these conditions are stronger than necessary, and thus motivate the "modern" version of control barrier functions.

<!-- chunk {"id": "body-0015", "role": "body", "section": "I-A Brief History of Barrier Functions", "weight": 1.0} -->

The aforementioned methods all led to the most recent formulation of certificates of safety, termed control barrier functions, as recognition of the historical developments outlined above---these were first introduced, and later refined. In particular, the idea was to extend the barrier function conditions (e.g., those discovered by Nagumo) to the entirety of the safe set.

<!-- chunk {"id": "body-0016", "role": "body", "section": "I-A Brief History of Barrier Functions", "weight": 1.0} -->

for $\alpha$ an (extended) class $\mathcal{K}$ function. Importantly, this condition is necessary and sufficient (for compact sets) and thus is minimally restrictive. Finally, because these conditions are true over the entire set $\mathcal{C}$ they give a way to synthesize safe controllers---in this case, through the use of optimization-based control methods that modify the desired controller again in a minimally invasive fashion. This formulation, therefore, provides a foundational framework for safety-critical control.

<!-- chunk {"id": "body-0017", "role": "body", "section": "I-A Brief History of Barrier Functions", "weight": 1.0} -->

The utility of this new formulation of control barrier functions is evidenced by the application domains it has been applied to since its inception, including: automotive systems, mulit-robot systems, quadrotors and robotic systems including walking robots, to name a few. Additionally, it allows for the unification of safety (via a control barrier function) and stability (via a control Lyapunov function) in the context of an optimization based controller---in fact, it was optimization based controllers using control Lyapunov functions that motivated the development of this new form of barrier function. This formulation of control barrier functions will be the focus of this paper, as motivated by the conceptual connections with control Lyapunov functions together with a recognition of the basic differences between control barrier and Lyapunov functions.

<!-- chunk {"id": "body-0018", "role": "body", "section": "I-B Overview of Paper", "weight": 1.0} -->

Building upon the history of barrier functions, and motivated by the new developments, this paper aims to establish the basic theory of safety-critical control and highlight some important applications.

<!-- chunk {"id": "body-0019", "role": "body", "section": "I-B Overview of Paper", "weight": 1.0} -->

Theory: We begin in Section II by establishing the foundations of control barrier functions. This is motivated from the perspective of stabilization with control Lyapunov functions, leading to the "dual" of stability: safety as enforced by control barrier functions. The properties of these functions are discussed, along with the synthesis of optimization-based controllers. In Section III, the application of CBFs to systems with actuation constraints is considered. Finally, in Section IV, the extension of CBFs to constraints with higher relative degree is considered.

<!-- chunk {"id": "body-0020", "role": "body", "section": "I-B Overview of Paper", "weight": 1.0} -->

Application: The discussion of the application of CBFs begins in Section V with the consideration of robotic systems. In particular, we begin by considering the "stepping stone" problem, wherein a robot must walk safely on a series of stepping stones. This is followed by a brief discussion of the experimental implementation of barriers in the context of automotive safety systems and dynamic robotic systems. Additionally, the application of CBFs in the context of long duration autonomy is formulated and demonstrated experimentally.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Foundations of Control Barrier Functions", "weight": 1.0} -->

In this section, we introduce the fundamentals of control barrier functions. That is, we introduce safety, safety sets, and a means in which to enforce safety in a minimally invasive fashion. To motivate these considerations, we will begin by reviewing control Lyapunov functions (CLFs) and discuss how they can be used to synthesize controllers that enforce stability. This naturally leads to the "dual" for safety: control barrier functions (CBFs). We will formulate optimization based controllers from CBFs and conclude by describing how they can be unified with CLFs.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Foundations of Control Barrier Functions", "weight": 1.0} -->

with $f$ and $g$ locally Lipschitz, $x \in D \subset {\mathbb{R}}^{n}$ and $u \in U \subset {\mathbb{R}}^{m}$ is the set of admissible inputs.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-A Motivation: Control Lyapunov Functions", "weight": 1.0} -->

To motivate safety for systems of this form, and hence control barrier functions, we begin by considering the familiar objective of stabilizing the system. Suppose we have the control objective of (asymptotically) stabilizing the nonlinear control system to a point $x^{\ast} = 0$, i.e., driving ${x{(t)}}\rightarrow 0$. In a nonlinear context, this can be achieved---and, in fact, understood---by equivalently finding a feedback control law that drives a positive definite function, $V:{D \subset {\mathbb{R}}^{n}\rightarrow{\mathbb{R}}_{\geq 0}}$, to zero. That is, if

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-A Motivation: Control Lyapunov Functions", "weight": 1.0} -->

Thus, the process of stabilizing a nonlinear system can be understood as finding an input that creates a one-dimensional stable system given by the Lyapunov function: $\overset{˙}{V} \leq {- {\gamma{(V)}}}$, wherein the comparison lemma (see, e. g., ) implies that the full-order nonlinear system is thus stable under the control law $u = {k{(x)}}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-A Motivation: Control Lyapunov Functions", "weight": 1.0} -->

The above observations motivate the notion of a control Lyapunov function wherein a function $V$ is shown to stabilize the system without the need to explicitly construct the feedback controller $u = {k{(x)}}$. That is, as first observed by Sontag and Artstein, we only need a controller to exist that results in the desired inequality on $\overset{˙}{V}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-A Motivation: Control Lyapunov Functions", "weight": 1.0} -->

where $\gamma$ is again a class $\mathcal{K}$ function.

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-A Motivation: Control Lyapunov Functions", "weight": 1.0} -->

This is an affine constraint in $u$ and thus will allow for the formulation of optimization based controllers. It also elucidates conditions on when $V$ is a CLF; for example, if $U = {\mathbb{R}}^{m}$, it is easy to verify that

<!-- chunk {"id": "body-0028", "role": "body", "section": "II-A Motivation: Control Lyapunov Functions", "weight": 1.0} -->

and thus there are stabilizing controllers. More generally, we have the following central stabilization result for CLFs.

<!-- chunk {"id": "body-0029", "role": "body", "section": "II-B Control Barrier Functions", "weight": 1.0} -->

Unlike stability which involves driving a system to a point (or a set), safety can be framed in the context of enforcing invariance of a set, i.e., not leaving a safe set.

<!-- chunk {"id": "body-0030", "role": "body", "section": "II-B Control Barrier Functions", "weight": 1.0} -->

We refer to $\mathcal{C}$ as the safe set.

<!-- chunk {"id": "body-0031", "role": "body", "section": "II-B Control Barrier Functions", "weight": 1.0} -->

Safety. Let $u = {k{(x)}}$ be a feedback controller such that the resulting dynamical system

<!-- chunk {"id": "body-0032", "role": "body", "section": "II-B Control Barrier Functions", "weight": 1.0} -->

is locally Lipschitz. To formally define safety, due to the locally Lipschitz assumption, for any initial condition $x_{0} \in D$ there exists a maximum interval of existence ${I{(x_{0})}} = {\lbrack 0,\tau_{\max})}$ such that $x{(t)}$ is the unique solution to on $I{(x_{0})}$; in the case when $f_{cl}$ is forward complete, $\tau_{\max} = \infty$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Note that, as discussed in Section I, the first notion of a control barrier function was defined in terms of what are now termed reciprocal barrier functions.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 3", "weight": 1.0} -->

This class of barrier functions can be more suitable for some applications, but typically barrier functions, $h$, are preferable since they are well defined outside of $\mathcal{C}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 4", "weight": 1.0} -->

The idea of extending set invarience conditions, i.e., the condition that $\overset{˙}{h} \geq 0$ for all $x \in {\partial\mathcal{C}}$, to all of $\mathcal{C}$ was first considered in in the form of the following condition: $\overset{˙}{h} \geq {- h}$ for all $x \in \mathcal{C}$. This can be viewed as a very special case of a CBF wherein ${\alpha{(r)}} = r$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 4", "weight": 1.0} -->

That is, as in the case of CLFs, we can quantify the set of all control inputs at a point $x \in D$ that keep the system safe.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 5", "weight": 1.0} -->

The condition that the gradient of $h$ not vanish on the boundary is equivalent to requiring that $0$ is a regular value of $h$. Note that this condition was not explicitly stated, but the proof of this result utilizes Nagumo's theorem which requires this regularity condition.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Remark 6", "weight": 1.0} -->

It is important to stress that this result not only guarantees that the safe set $\mathcal{C}$ is invariant, but makes the set $\mathcal{C}$ asymptotically stable. This has beneficial consequences with regard to practical implementation. While a system will not formally leave the safe set $\mathcal{C}$, noise and modeling errors might force the system to leave this set. As a result of the main CBF theorem, controllers in $K_{cbf}{(x)}$ will drive the system back to the set $\mathcal{C}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "II-C Optimization Based Control", "weight": 1.0} -->

Having established that control barrier functions give (necessary and sufficient) conditions on safety, the question becomes: how does one synthesize controllers? Importantly, we wish to do so in a minimally invasive fashion, i.e., modify an existing controller in a minimal way so as to guarantee safety.

<!-- chunk {"id": "body-0040", "role": "body", "section": "II-C Optimization Based Control", "weight": 1.0} -->

Safety-Critical Control. Suppose we are given a feedback controller $u = {k{(x)}}$ for the control system and we wish to guarantee safety. Yet it may be the case that ${k{(x)}} \notin {K_{cbf}{(x)}}$ for some $x \in D$. To modify this controller in a minimal way so as to guarentee safety, we start by noticing that the conditions on safety given in are affine in $u$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "II-C Optimization Based Control", "weight": 1.0} -->

where here we assumed that $U = {\mathbb{R}}^{m}$. Thus, when there are no input constraints, since we have a single inequality constraint the CBF-QP has a closed-form solution (per the KKT conditions ) given by the min-norm controller; this was first utilized in the context of CLFs.

<!-- chunk {"id": "body-0042", "role": "body", "section": "II-C Optimization Based Control", "weight": 1.0} -->

Unifying with Lyapunov. The QP based formulation of safety-critical controllers suggests a means in which to unify safety and stability. In fact, optimization-based controllers were first utilized in the context of CLFs exactly for the purpose of multi-objective nonlinear control, e.g., combining stability with torque constraints.

<!-- chunk {"id": "body-0043", "role": "body", "section": "II-C Optimization Based Control", "weight": 1.0} -->

where here $H{(x)}$ is any positive definite matrix (pointwise in $x$), and $\delta$ is a relaxation variable that ensures solvability of the QP as penalized by $p > 0$ (i.e., to ensure the QP has a solution one must relax the condition on stability to guarantee safety). In it was established that this controller is Lipschitz continuous.

<!-- chunk {"id": "body-0044", "role": "body", "section": "CBFs for Systems with Actuation constraints", "weight": 1.0} -->

Consider again the nonlinear affine control system and assume there exists an *allowable set* of states $A = {\{{x \in D}:{{\rho{(x)}} \geq 0}\}}$ defined via some *performance function* $\rho:{D\rightarrow{\mathbb{R}}}$. Our objective is to construct a CBF $h:{D\rightarrow{\mathbb{R}}}$ such that

<!-- chunk {"id": "body-0045", "role": "body", "section": "CBFs for Systems with Actuation constraints", "weight": 1.0} -->

that is, such that the safe set $\mathcal{C}$, corresponding to the superlevel set of the CBF $h$, is contained within the set of allowed states $A$. Of course, it may be possible to take ${h{(x)}} = {\rho{(x)}}$ if this choice satisfies for an appropriate function $\alpha$, in which case our objective is met.

<!-- chunk {"id": "body-0046", "role": "body", "section": "CBFs for Systems with Actuation constraints", "weight": 1.0} -->

However, in this section, we focus on the case when $A$ cannot be rendered invariant and instead we must find a safe subset that is a strict subset of the allowable set. The inability of $A$ itself to be rendered forward invariant could be due to, *e.g.*, a control set $U$ that restricts the available control actions or due to dynamics with higher relative degree; an alternative approach to accommodate the latter is proposed in Section IV.

<!-- chunk {"id": "body-0047", "role": "body", "section": "CBFs for Systems with Actuation constraints", "weight": 1.0} -->

We assume that a locally Lipschitz *nominal controller* $\beta:{D\rightarrow U}$ (called *nominal evading maneuver* in ) is known. Intuitively, $\beta$ encapsulates a controller that, for some initial conditions, is expected to keep the system within the allowable set, although no guarantees on the ability of $\beta$ to ensure safety are required *a priori*. For example, for an autonomous mobile agent, $\beta$ might be a swerving maneuver or a rapid deceleration maneuver.

<!-- chunk {"id": "body-0048", "role": "body", "section": "CBFs for Systems with Actuation constraints", "weight": 1.0} -->

A barrier function can be computed from $\rho$ and $\beta$ as

<!-- chunk {"id": "body-0049", "role": "body", "section": "CBFs for Systems with Actuation constraints", "weight": 1.0} -->

that is, the barrier $h$ is constructed by assigning to each point $x \in D$ the infimum value of the performance function $\rho$ attained along the trajectory initialized at $x$ when the nominal control strategy $\beta$ is used. Under mild conditions on $\rho$ and $\beta$, $h$ is indeed a CBF.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Exponential Control Barrier Functions", "weight": 1.0} -->

In the previous sections we have seen how control barrier functions (CBFs) can be (i) used to enforce safety-critical constraints for nonlinear (control affine) systems, (ii) combined with control Lyapunov functions to arbitrate between stability and safety, and (iii) used for systems with actuator constraints. While CBFs offer a powerful methodology, there is one critical restriction: the safety-critical constraints have been so far assumed to be of relative-degree one, i.e., the first time-derivative of the CBF has to depend on the control input. However, this is a restrictive assumption that is typically not held for most safety constraints for robotic systems. We therefore need a way to enforce arbitrarily high relative-degree safety constraints. In this section, we introduce a special type of CBFs called Exponential CBFs that enable this functionality.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Exponential Control Barrier Functions", "weight": 1.0} -->

Control barrier functions for high-relative degree safety constraints were initially studied simultaneously. However, the results in only extended to position based safety constraints with relative-degree 2. On the other hand, the results in extended to arbitrary high relative-degree using a backstepping based method. However, backstepping based CBF design for higher relative-degree systems (greater than 2) is challenging and has not been attempted. Building off the work, exponential control barrier functions were first introduced in as a way to easily enforce high relative-degree safety constraints. The rest of this section provides an introduction to exponential CBFs.

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-A High Relative-Degree Safety Constraints", "weight": 1.0} -->

Consider the nonlinear dynamical system in with initial condition $x_{0}$ with the goal to enforce the forward invariance of the safe set $\mathcal{C}$ defined in (II-B). However, unlike in earlier sections, we relax the relative-degree 1 assumption on $h{(x)}$ and assume $h{(x)}$ has arbitrarily high relative-degree $r \geq 1$. This translates to the $r^{\text{th}}$ time-derivative of $h{(x)}$ being,

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-A High Relative-Degree Safety Constraints", "weight": 1.0} -->

We now have everything setup to define exponential control barrier functions.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Remark 8", "weight": 1.0} -->

Note that $K_{\alpha}$ in the above definition needs to satisfy certain specific properties. As we will see, we will require $K_{\alpha}$ to make the closed-loop system matrix stronger than Hurwitz (total negative) and additionally satisfy a condition based on the initial conditions $\eta_{b}{(x_{0})}$. These will be presented in more detail in the subsequent subsection on designing ECBFs.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Remark 9", "weight": 1.0} -->

Note that when the relative-degree $r = 1$, $- {K_{\alpha}\eta_{b}{(x)}}$ in reduces to $- {\alphah{(x)}}$ with $\alpha > 0$. Thus, Definition 2 defines a relative-degree 1 exponential CBF when ${\alpha{({h{(x)}})}} = {\alphah{(x)}}$ (with a small abuse of notation), $\alpha > 0$. In this sense, the above definition is a generalization of the definition of CBFs for higher relative-degree functions $h{(x)}$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Remark 9", "weight": 1.0} -->

Given an ECBF, we can implement a controller that enforces the condition given in Definition 7 by extending the optimization based control methodology presented earlier.

<!-- chunk {"id": "body-0057", "role": "body", "section": "IV-B Designing Exponential Control Barrier Functions", "weight": 1.0} -->

In order to design an exponential CBF, we begin by noting that (IV-A) is in controllable canonical form and if $K_{\alpha} = \begin{bmatrix}
\alpha_{1} & \cdots & \alpha_{r}
\end{bmatrix}$ then the characteristic polynomial of $F - {GK_{\alpha}}$ is ${\lambda^{r} + {\alpha_{r}\lambda^{r - 1}} + \cdots + {\alpha_{2}\lambda} + \alpha_{1}} = 0$, whose roots we will denote by $p_{1},\cdots,p_{r}$. Note that there is a well established relation between the coefficients of a polynomial and its roots.

<!-- chunk {"id": "body-0058", "role": "body", "section": "IV-B Designing Exponential Control Barrier Functions", "weight": 1.0} -->

Note that $\mathcal{C}_{0}$ is identical to $\mathcal{C}$. Our goal is to design $K_{\alpha}$ to ensure $\mathcal{C}$ is forward invariant. We begin with the following result.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Applications: CBFs for Robotic Systems", "weight": 1.0} -->

Having seen the theoretical development of control barrier functions in the earlier sections, we will now present practical uses of CBFs in various robotic application domains. Sections V-A to V-C will introduce CBFs for single-agent robotic systems: we will look at three sufficiently different types of robotic systems, i. e. walking robots, cars, and Segways. Section V-D will introduce CBFs for multi-agent robotic systems.

<!-- chunk {"id": "body-0060", "role": "body", "section": "V-A Dynamic Walking on Stepping Stones", "weight": 1.0} -->

Legged robots are unique in the sense that these systems are able to locomote over discrete terrains - such as a terrain with steeping stones with discrete gaps between the steps (see Fig. 1a). Precisely stepping on the footholds is critical and missing the foothold even by a few centimeters will cause a dramatic fall of the robotic system. In this sense, stepping stones are examples of safety-critical control that have to be strictly enforced. While this is challenging, in the preceding sections we have developed the theory to specifically attack such safety-critical problems. Dynamic walking over stepping stones using CBFs was first demonstrated. Here, we present results on the DURUS bipedal robot reported.

<!-- chunk {"id": "body-0061", "role": "body", "section": "V-A Dynamic Walking on Stepping Stones", "weight": 1.0} -->

Legged systems are modeled as multi-domain hybrid systems with walking consisting of a single-support phase when one (stance) foot is in contact with the ground and an instantaneous double-support phase when the swing foot impacts ground. The single-support phase is modeled as a continuous-time differential equation while the double-support phase is modeled as an instantaneous impact due to the swing foot impacting on the ground. The impact causes an instantaneous jump in the system state. Mathematically, this is represented as the hybrid system

<!-- chunk {"id": "body-0062", "role": "body", "section": "V-A Dynamic Walking on Stepping Stones", "weight": 1.0} -->

with $S$ representing the switching surface that denotes swing foot contact with the ground.

<!-- chunk {"id": "body-0063", "role": "body", "section": "V-A Dynamic Walking on Stepping Stones", "weight": 1.0} -->

For the above system, a hybrid zero dynamics (HZD) based approach (see for details) is used to design a stable periodic orbit---representing walking---by means of an offline nonlinear constrained optimization, in order to find a set of outputs $y:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{m}}$ that are then regulated by constructing a Lyapunov function ${V{(x)}} = {\begin{bmatrix}
\end{bmatrix}P\begin{bmatrix}
\end{bmatrix}^{T}}$ such that driving ${V{(x)}}\rightarrow 0$ results in driving the outputs to zero, resulting in stable walking. This is achieved by the CLF based approach detailed in Section II-A, with the difference for a hybrid system being that rapid exponential stability is sought through a RES-CLF s.t.

<!-- chunk {"id": "body-0064", "role": "body", "section": "V-A Dynamic Walking on Stepping Stones", "weight": 1.0} -->

${\overset{˙}{V}{(x,u)}} \leq {- {\frac{1}{\epsilon}\gamma{({V{(x)}})}}}$, where $0 < \epsilon < 1$. This ensures that the controller contracts faster than the potential expansion that happens at impacts. See for more details.

<!-- chunk {"id": "body-0065", "role": "body", "section": "V-A Dynamic Walking on Stepping Stones", "weight": 1.0} -->

Now, let us look into the problem of how we can guarantee the safety-critical constraint of precisely placing the feet on the stepping stone on each step. In Fig. 1b, the start of the step is shown as the dotted stick-figure with the stance foot at $O$. The goal is to move the swing leg and precisely impact the ground within the solid red foothold at the end of the step. This is a constraint at the step end-time which can not be directly enforced as a barrier. We convert this end-time constraint into a barrier constraint that is enforced point-wise in time. In particular, if the swing foot position, denoted by $F$ in the Fig. 1b, is maintained within the outer circle (with center $O_{1}$ and radius $R_{1}$) and outside the inner circle (with center $O_{2}$ and radius $R_{2}$), then the foot follows the red trajectory and impacts the foothold at the end of step.

<!-- chunk {"id": "body-0066", "role": "body", "section": "V-A Dynamic Walking on Stepping Stones", "weight": 1.0} -->

where $O_{1}F{(x)}$ and $O_{2}F{(x)}$ are the distances between the swing foot $F$ and the centers of the two circles at $O_{1}$ and $O_{2}$ respectively.

<!-- chunk {"id": "body-0067", "role": "body", "section": "V-A Dynamic Walking on Stepping Stones", "weight": 1.0} -->

Fig. 2b illustrates snapshots from simulation of walking over a stepping stone terrain with different step lengths. This method can also be used to walk over a terrain of stepping stones with changing step width or step height.

<!-- chunk {"id": "body-0068", "role": "body", "section": "V-B Automotive Systems: Automatic Cruise Control and Lane Keeping", "weight": 1.0} -->

Our next example is from the automotive domain. Many modern Advanced Driver Assistance Systems (ADAS) provide prime examples of safety-critical constraints. For instance, in Adaptive Cruise Control (ACC) the vehicle's speed is regulated to a user-set speed when there is no vehicle immediately ahead in the lane, yet if a vehicle is detected ahead then a safe following distance is maintained. On the other hand, in Lane Keeping (LK) the vehicle's steering is controlled so as to maintain the vehicle within a lane. Furthermore, two or more ADAS control modules can be simultaneously activated and designing provably correct controllers for simultaneous operation becomes critical; this subsection follows, but see also.

<!-- chunk {"id": "body-0069", "role": "body", "section": "V-B Automotive Systems: Automatic Cruise Control and Lane Keeping", "weight": 1.0} -->

In order to demonstrate adaptive cruise control and lane keeping in an experimental setting, we will consider a Khepera robot modeled as a unicycle model

<!-- chunk {"id": "body-0070", "role": "body", "section": "V-B Automotive Systems: Automatic Cruise Control and Lane Keeping", "weight": 1.0} -->

where ${(p_{x},p_{y})},\psi,v,\omega$ represent the 2D position, orientation, and longitudinal and angular velocities of the robot respectively, with $x \in {\mathbb{R}}^{5}$ the resulting state vector. Further, $u_{l}$ is the longitudinal force and $u_{a}$ is the angular torque and serve as control inputs. The mass and inertia are $m,I_{z}$ respectively and $a$ represents the distance from the center of the wheel-base to the point of interest $(p_{x},p_{y})$. This model can be written as a nonlinear control affine system as given.

<!-- chunk {"id": "body-0071", "role": "body", "section": "V-B Automotive Systems: Automatic Cruise Control and Lane Keeping", "weight": 1.0} -->

As mentioned, adaptive speed regulation comprises of following a user-set speed when there is no vehicle ahead in the lane. This will be formulated as a soft constraint through a CLF. However, when there is a vehicle ahead, the speed needs to be adaptively reduced so as to maintain a fixed time-headway based follow distance.

<!-- chunk {"id": "body-0072", "role": "body", "section": "V-B Automotive Systems: Automatic Cruise Control and Lane Keeping", "weight": 1.0} -->

Here, $D$ is the distance to the vehicle ahead, $\tau$ is minimum time-headway to be maintained, and $v_{f}$ is the velocity of the vehicle (follower)---see for the derivation.

<!-- chunk {"id": "body-0073", "role": "body", "section": "V-B Automotive Systems: Automatic Cruise Control and Lane Keeping", "weight": 1.0} -->

Similarly, the objective of lane keeping is to maintain the vehicle within the lane. We need to enforce a safety-critical constraint of the form $y_{lat} \leq d_{max}$, where $y_{lat}$ is the lateral distance w.r.t. the center of the lane and $d_{max}$ is the distance from the center of the lane to either end of the lane that captures the lane width.

<!-- chunk {"id": "body-0074", "role": "body", "section": "V-B Automotive Systems: Automatic Cruise Control and Lane Keeping", "weight": 1.0} -->

Here, $a_{max}$ is the maximum lateral acceleration and $v_{lat}$ is the lateral velocity of the vehicle. More details about the properties of this CBF are detailed.

<!-- chunk {"id": "body-0075", "role": "body", "section": "V-B Automotive Systems: Automatic Cruise Control and Lane Keeping", "weight": 1.0} -->

Finally, the performance objectives such as driving the longitudinal velocity to a user-defined velocity ($v\rightarrow v_{d}$), creating a smoother path following ($\omega\rightarrow 0$), and following the desired path (${(x,y)}\rightarrow R_{d}$) are specified through output functions that are regulated to zero through CLFs. As earlier, the CLF and CBF conditions are unified into a single controller via (CLF-CBF QP) given in Section II-C. Fig. 3a shows experimental results on the Khepera robot where simultaneous enforcement of lane keeping and adaptive speed regulation safety constraints are enforced. Fig. 3b illustrates the value of the CBFs in experiments and simulation.

<!-- chunk {"id": "body-0076", "role": "body", "section": "V-C Dynamic Balancing on Segways", "weight": 1.0} -->

To demonstrate the application of control barrier functions as "safety filters," we will consider their experimental realization on a Segway type robot, i.e., a two-wheeled inverted pendulum. In particular, this subsection summarizes the results of which provided the first experimental evaluation of CBFs on a robotic system that is not statically stable. To realize these results, a Ninebot Segway was rebuilt, with only the original chassis and motors remaining---all of the electronics were customized to allow for the real-time control of the system via optimization based controllers. The objective is to ensure "safe" operation of the Segway, defined in this case as the robot not tipping over, i.e., always staying upright. Additionally, the goal is to achieve this safety condition even while using a nominal controller for the system (that may not be safe) and thus modifying the controller in a minimally invasive fashion so as to ensure safety.

<!-- chunk {"id": "body-0077", "role": "body", "section": "V-C Dynamic Balancing on Segways", "weight": 1.0} -->

The result will be a safety filter, or an Active Set Invariance Filter (ASIF) of the form illustrated in Fig. 4, where the nominal control input, $u_{des}$, is filtered through a QP of the form (CBF-QP) to ensure safety in the system.

<!-- chunk {"id": "body-0078", "role": "body", "section": "V-C Dynamic Balancing on Segways", "weight": 1.0} -->

The dynamics of the Segway can be written in the standard form given, where in this case the input, $u$, is the voltage input into the motors and $x = {(v,\phi,\overset{˙}{\phi})}^{T}$, where $v$ is the forward velocity of the Segway, $\phi$ is the angle of the pendulum from upright, and $\overset{˙}{\phi}$ is the rate of change of this angle. Correspondingly, there are input bounds on the system of the following form: $u \in {{\lbrack{- 15},15\rbrack}V}$ (this input bounds will play a role in determining the CBF that will be implemented on hardware). The safety constraint for the system is that the pendulum component of the robot stays upright, i.e., that the Segway does not tip over.

<!-- chunk {"id": "body-0079", "role": "body", "section": "V-C Dynamic Balancing on Segways", "weight": 1.0} -->

This can be captured by the condition that the angle of the pendulum, $\phi$, stays within a bounded region, in this case chosen to be $\phi \in {{\lbrack{- \frac{\pi}{12}},\frac{\pi}{12}\rbrack}{rad}}$. Finally, to ensure valid inputs, we also restrict the rate of change of the angle of the pendulum to be $\overset{˙}{\phi} \in {{{\lbrack{- {2\pi}},{2\pi}\rbrack}{rad}}/s}$, and the forward velocity of the Segway to be $v \in {{{\lbrack{- 5},5\rbrack}m}/s}$. Finally, the nominal controller for the system, $u_{des} = {k{(x)}}$, is chosen to be a standard PD controller that tracks a desired signal, i.e., an angle of the pendulum and velocity for the wheels.

<!-- chunk {"id": "body-0080", "role": "body", "section": "V-C Dynamic Balancing on Segways", "weight": 1.0} -->

Since the safety constraint is to keep the Segway upright, i.e.,

<!-- chunk {"id": "body-0081", "role": "body", "section": "V-C Dynamic Balancing on Segways", "weight": 1.0} -->

Yet, while these could be implemented via a CBF-QP to enforce these conditions, they will not enforce all of the additional constraints necessary to guarantee experimental implementation. Therefore, the Hamilton-Jacobi method was utilized to determine the safe set $\mathcal{C}$ resulting by enforcing all the above-mentioned constraints. In particular, a reachability analysis was performed over a 75x75x75 grid of the state space with the edges of the grid at the state constraints given in the previous paragraph. The resulting safe set can be seen in Fig. 5a. A control barrier function can then be synthesized from this set---in this case, polynomial regression was used to create an analytic expression that can be used in the safety filter.

<!-- chunk {"id": "body-0082", "role": "body", "section": "V-C Dynamic Balancing on Segways", "weight": 1.0} -->

The safety filter was implemented on hardware using the general framework indicated in Fig. 4. In particular, the CLF-QP was solved onboard the hardware on a BeagleBone Black with an average computation time of 0.4 ms, with the resulting signal $u_{act}$ passed to the motor controller. To demonstrate the ability of the ASIF to enforce safety, the desired pendulum angle was passed to the system in the form of a sinusoidal signal with an amplitude exceeding the $\frac{\pi}{12}$ angle constraint. Two experiments were then performed, one without and one with the ASIF, i.e., the CLF-QP active. The results can be seen in Fig. 5b, wherein the system remains safe only when the safety filter, implementing the CBF, is active. Finally, to show the potential power of CBFs, a disturbance is added to the system in the form of a kick---the system is able to stay upright, and hence safe, with CBFs while the systems fails without them (illustrated in Fig. 5c).

<!-- chunk {"id": "body-0083", "role": "body", "section": "V-D Long Duration Autonomy", "weight": 1.0} -->

Another robotic application of CBFs involves the long duration autonomy problem for multi-robot systems. This problem considers a team of robots deployed over long time scales which are asked to execute tasks (such as environmental monitoring, search and rescue, or precision agriculture) that require more than a single charge of the battery of the robots. An effective control paradigm to use in this case is the constraint-based control, where survivability constraints, i.e., conditions for the robots to remain operational over long temporal scales, can be enforced by means of CBFs and included in a single constrained optimization problem.

<!-- chunk {"id": "body-0084", "role": "body", "section": "V-D Long Duration Autonomy", "weight": 1.0} -->

where $x_{i} \in {\mathbb{R}}^{n}$ and $u_{i} \in {\mathbb{R}}^{m}$, $i = {1,\ldots,N}$, are the state and the input of robot $i$, respectively, and $f$ and $g$ are locally Lipschitz. As the energy plays an important role in ensuring persistent operation, we augment the state $x_{i}$ by the energy $E_{i}$ stored in robot $i$'s battery obtaining: $\chi_{i} = {\lbrack x_{i}^{T},E_{i}\rbrack}^{T}$. The energy dynamics are given by

<!-- chunk {"id": "body-0085", "role": "body", "section": "V-D Long Duration Autonomy", "weight": 1.0} -->

where $\hat{f}$ and $\hat{g}$ are also assumed to be locally Lipschitz.

<!-- chunk {"id": "body-0086", "role": "body", "section": "V-D Long Duration Autonomy", "weight": 1.0} -->

We assume the robot workspace is endowed with charging stations, interpreted as regions of the state space where robots can charge their batteries. Letting

<!-- chunk {"id": "body-0087", "role": "body", "section": "V-D Long Duration Autonomy", "weight": 1.0} -->

be a static mapping from robot $i$'s state to its position $p_{i} \in {\mathbb{R}}^{d}$, $d = 2$ for ground robots or $d = 3$ for aerial robots, we define

<!-- chunk {"id": "body-0088", "role": "body", "section": "V-D Long Duration Autonomy", "weight": 1.0} -->

as the function that evaluates the energy that robot $i$ requires to reach a charging station starting from position $p_{i}$.

<!-- chunk {"id": "body-0089", "role": "body", "section": "V-D Long Duration Autonomy", "weight": 1.0} -->

We are now ready to encode the survivability constraints mentioned above.

<!-- chunk {"id": "body-0090", "role": "body", "section": "V-D Long Duration Autonomy", "weight": 1.0} -->

i. e. each robot always has enough energy to reach a charging station with a minimum desired amount of energy, $E_{min}$.

<!-- chunk {"id": "body-0091", "role": "body", "section": "V-D Long Duration Autonomy", "weight": 1.0} -->

We can combine these two objectives by defining the logical and of these constraints, $h_{e,i} = {h_{c,i} \land h_{o,i}}$, as

<!-- chunk {"id": "body-0092", "role": "body", "section": "V-D Long Duration Autonomy", "weight": 1.0} -->

and enforcing differential constraints affine in the control variable $u_{i}$, which are analogous to, as shown.

<!-- chunk {"id": "body-0093", "role": "body", "section": "V-D Long Duration Autonomy", "weight": 1.0} -->

Considering the environmental monitoring task, we reformulate the task itself using CBFs which can be then combined with the ones related to survivability introduced above in order to implement persistent environmental monitoring. Consider $N$ robots tasked with monitoring a compact and convex set $\Omega \subset {\mathbb{R}}^{d}$.

<!-- chunk {"id": "body-0094", "role": "body", "section": "V-D Long Duration Autonomy", "weight": 1.0} -->

where $x$ is the ensemble state of the robots, $\{\Omega_{1},\ldots,\Omega_{N}\}$ is the Voronoi tessellation of the set $\Omega$, the value ${{\phi{(q)}} \in {\mathbb{R}}},{{\phi{(q)}} \geq {0{\forall q}} \in \Omega}$, encodes the importance of the point $q$, and where the quality of the sensor coverage associated with the point $q$ decreases quadratically with the distance $\|{{p{(x_{i})}} - q}\|$. The further away the point to monitor is, the worse the coverage is, and the higher the coverage cost $J$ is.

<!-- chunk {"id": "body-0095", "role": "body", "section": "V-D Long Duration Autonomy", "weight": 1.0} -->

Defining the barrier function related to the task as ${h_{t}{(\chi)}} = {- {J{(x)}}}$, where $\chi$ represents the ensemble compound state of the robots, containing $x_{i}$ and $E_{i}$ of each robot, we can express the constraint as

<!-- chunk {"id": "body-0096", "role": "body", "section": "V-D Long Duration Autonomy", "weight": 1.0} -->

As shown, the constraint ensures that the zero superlevel set of the function $h_{t}{(\chi)}$ is asymptotically stable, with the effect of minimizing the coverage cost $J$ defined above.

<!-- chunk {"id": "body-0097", "role": "body", "section": "V-D Long Duration Autonomy", "weight": 1.0} -->

Additionally, safety, specifically intended as collision avoidance, can be guaranteed by ensuring that

<!-- chunk {"id": "body-0098", "role": "body", "section": "V-D Long Duration Autonomy", "weight": 1.0} -->

${{{\forall i},j} \in {\{ 1,\ldots,N\}}},{i \neq j}$, where $\Delta > 0$ is the safety distance to be maintained between any two robots, $i$ and $j$, located at positions $p{(x_{i})}$ and $p{(x_{j})}$. Similarly to what has been done to obtain, we can define

<!-- chunk {"id": "body-0099", "role": "body", "section": "V-D Long Duration Autonomy", "weight": 1.0} -->

which combines energy and safety constraints, in order to formulate a differential constraint analogous to.

<!-- chunk {"id": "body-0100", "role": "body", "section": "V-D Long Duration Autonomy", "weight": 1.0} -->

where $\kappa > 0$ is a weighting factor and the gradients involved in the computation of the Lie derivatives are intended as a particular class of generalized gradients (see ). Note that introducing the relaxation variable $\delta$, as discussed in Section II, allows us to trade the execution of the coverage task for safety and energy, i. e., survivability.

<!-- chunk {"id": "body-0101", "role": "body", "section": "V-D Long Duration Autonomy", "weight": 1.0} -->

The persistent environmental monitoring strategy has been implemented on the Robotarium, where six ground mobile robots have been asked to monitor a given domain over a time horizon that is longer than their (simulated) battery life (see Fig. 6). The robots perform coverage control by minimizing the cost by enforcing the constraint. Additionally, they have to avoid two obstacles moving in the environment (robots circled in red in Fig. 6) and never run out of energy. This is realized by means of the constraint. Six charging stations (blue circles, which turn yellow when the robots are charging) allow the robots to recharge their battery. The charging stations are projected onto the testbed, together with the boundary of the Voronoi tessellation of the domain to cover. The execution of the controller solution of is summarized in Fig. 6.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Conclusions", "weight": 1.0} -->

This paper presented a summary of recent results in safety-critical control based upon a novel form of control barrier functions. The basis theoretic foundations of this formulation were reviewed, all with selected application domains. Due to the recent activity in this domain, and the pressing need for safety in the context of autonomous systems, the authors imagine control barrier functions to become an essential component of modern control system design.
