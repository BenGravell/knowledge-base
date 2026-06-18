## Introduction

Safety is essential for feedback control systems. As a system is steered from an initial set to a target set, safety requires that the trajectory of the system avoids entering an unexpected region, or to remain inside a safe set. On the state space, safety is always formulated by means of constraints imposed on states. Based on these descriptions, two questions are raised: given a dynamical system $\overset{˙}{x} = {f{(x,u)}}$, a set of initial sets $\mathcal{I}$, and a set of safe states $\mathcal{S}$, (i) verify whether there exists a control input $u{( \cdot )}$, so that the trajectories starting from $\mathcal{I}$ stay inside $\mathcal{S}$; (ii) design such a control law $u{( \cdot )}$ that guarantees safety. The Control Barrier Functions (CBF) approach answers these two questions by using a continuously differentiable function that satisfies certain properties \[(https://arxiv.org/html/2403.11763v1#bib.bib1), (https://arxiv.org/html/2403.11763v1#bib.bib2), (https://arxiv.org/html/2403.11763v1#bib.bib3)\].

A CBF aims to separate the safe and unsafe regions by its zero super- and sub-level sets; the initial set also belongs to the level set. In addition, there exists a control law, such that the vector field points towards the safe side on its zero sub-level set \[(https://arxiv.org/html/2403.11763v1#bib.bib1)\]. This property is also known as *invariance*, characterized by Nagumo's theorem \[(https://arxiv.org/html/2403.11763v1#bib.bib4)\]. It is therefore guaranteed that if the system starts from a point inside the zero super-level set, the system can always stay inside. Given a CBF, the controller that guarantees safety can be designed according to the direction requirement of vector field. However, synthesizing a CBF is not a trivial task even for linear systems. In general, even verifying a CBF is an NP-hard problem \[(https://arxiv.org/html/2403.11763v1#bib.bib5), Proposition 2\].

Designing a CBF is even more challenging when the relative degree between the function defines safe set and the system dynamics is high or mixed \[(https://arxiv.org/html/2403.11763v1#bib.bib6)\]. For relative degree we mean the number of times we need to differentiate a function whose level set encodes the safe set along the system dynamics until the control explicitly shows \[(https://arxiv.org/html/2403.11763v1#bib.bib7), (https://arxiv.org/html/2403.11763v1#bib.bib8)\]. High or mixed relative degree is commonly seen in robotics collision avoidance problems, where the safe set is usually defined over positions for the obstacles, but the control signals are imposed on accelerations.

### I-A Motivating Cases

### Case 1 (Pathological vector field of CBF-QP)

Consider a continuous-time linear system with state matrix $A = \begin{bmatrix}
\end{bmatrix}$ and input matrix $B = \begin{bmatrix}
\end{bmatrix}$. The system is controllable. Let $x = {\lbrack x_{1},x_{2}\rbrack}^{\top} \in {\mathbb{R}}^{2}$ denote the states. The unsafe region is defined by $\mathcal{S}^{c} = \left. \{ x \middle| {{s{(x)}} \leq 0}\} \right.$, where ${s{(x)}} = {{x_{1}^{2} + x_{2}^{2}} - 1}$. Using $s{(x)}$ as a control barrier function in a quadratic programming framework \[(https://arxiv.org/html/2403.11763v1#bib.bib3)\] for controller design, we obtain:

Following \[(https://arxiv.org/html/2403.11763v1#bib.bib9)\], the analytical solution is given by

(a) Values of ∥us(x)∥22 for −1 ≤ x1 ≤ 1, −1 ≤ x2 ≤ 1. The value of ∥us(x)∥22 is limited to 100 for visualization. The controller is only locally smooth, and the Lipschitz constant is large in a local region as the value varies a lot with little state changes. Different selection of a class-𝒦 function does not change the result for x ∈ ∂ℬ, which is the black curve in the figure. Clearly our designed feedback controller ub(x) = 1.4164x1 + 0.59702x2 is globally smooth as it is linear.

(b) Comparison of the two control barrier functions in Case 1. The blue round region is the unsafe set 𝒮c. The yellow open region is the control invariant set ℬ:= {x|b(x) ≥ 0}, and ∂ℬ:= {x|b(x) = 0} is the black curve. Blue arrows represents the vector field Ax + Bub(x), which points inward ℬ on ∂ℬ.

Figure 1: Simulation results for Case 1.

When $g{(x)}$ tends to zero, and ${f{(x)}} < 0$, $u_{s}{(x)}$ tends to infinity. As a consequence, the system cannot be safe at some points, especially points on $\partial\mathcal{S}$ with limited control authority. We also show in Figure [0(a)](https://arxiv.org/html/2403.11763v1#S1.F0.sf1 "0(a) ‣ Figure 1 ‣ Case 1 (Pathological vector field of CBF-QP). ‣ I-A Motivating Cases ‣ I Introduction ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints") that the Lipschitz constant of $u_{s}{(x)}$ is very large. Later on, we will show that, by solving the proposed convex program ([III-A](https://arxiv.org/html/2403.11763v1#S3.E10 "III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) with ${\|{u_{b}{(x)}}\|}_{2}^{2} \leq 8$ for $x$ such that ${b{(x)}} = 0$, we obtain a new control barrier function ${b{(x)}} = {{{{0.88391x_{1}^{2}} - {0.50767x_{1}x_{2}}} + {0.25205x_{2}^{2}}} - 1}$, and a feedback controller ${u_{b}{(x)}} = {{1.4164x_{1}} + {0.59702x_{2}}}$. Comparison of the two control barrier functions is shown in Figure [0(b)](https://arxiv.org/html/2403.11763v1#S1.F0.sf2 "0(b) ‣ Figure 1 ‣ Case 1 (Pathological vector field of CBF-QP). ‣ I-A Motivating Cases ‣ I Introduction ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"). It can be seen that the value of ${\|{u_{s}{(x)}}\|}_{2}^{2}$ is comparably large for small $x_{2}$. Meanwhile, our synthesized controller is constrained by ${\|{u_{b}{(x)}}\|}_{2}^{2} \leq 8$ for $x \in {\partial\mathcal{B}}$.

### Case 2 (Mixed relative degree)

Consider a third-order continuous-time linear system with ${\overset{˙}{x}}_{1} = {x_{2} + x_{3}}$, ${\overset{˙}{x}}_{2} = {x_{1} + u_{1}}$, ${\overset{˙}{x}}_{3} = {x_{1} + u_{2}}$, where $x = {\lbrack x_{1},x_{2},x_{3}\rbrack}^{\top} \in {\mathbb{R}}^{3}$ is the state, $u = {\lbrack u_{1},u_{2}\rbrack}^{\top} \in {\mathbb{R}}^{2}$ is the input. The unsafe region is defined by $\mathcal{S}^{c}:=\left. \{ x \middle| {{s{(x)}} \leq 0}\} \right.$, where ${s{(x)}} = {{x_{1}^{2} + x_{2}^{2}} - 1}$. Let the relative degree be the number of times we need to differentiate $s{(x)}$ along the dynamics until the control input $u$ appears in the resulting expression. For this case, the relative degree between $s{(x)}$ and the system is mixed, as the input $u_{1}$ appears in the first derivative of $s{(x)}$, whereas $u_{2}$ appears in the second derivative. $s{(x)}$ can not be directly used as a CBF using high-relative degree (exponential) CBF techniques \[(https://arxiv.org/html/2403.11763v1#bib.bib7), (https://arxiv.org/html/2403.11763v1#bib.bib8), (https://arxiv.org/html/2403.11763v1#bib.bib10)\]. By solving the convex program ([III-A](https://arxiv.org/html/2403.11763v1#S3.E10 "III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) that we will propose in the sequel, we obtain a control barrier function ${b{(x)}} = {{x_{1}^{2} + x_{2}^{2}} - {0.0129x_{3}^{2}} - 1}$, and a feedback controller ${u_{1}{(x)}} = {{- {2x_{1}}} + {38.9x_{2}}}$, ${u_{2}{(x)}} = {{76.8x_{1}} - {0.5x_{3}}}$, which guarantees safety for the system. Clearly, the relative degree between $b{(x)}$ and the system dynamics is one. We highlight here that the backstepping CBF method \[(https://arxiv.org/html/2403.11763v1#bib.bib11)\] would require a series of explicit pre-synthesized safe controllers which are, however, not needed for our method, which only requires the solution of a convex program.

### I-B Related Work

Dating back to the 1980's, there has been tremendous work on control invariance, especially for linear systems \[(https://arxiv.org/html/2403.11763v1#bib.bib12), (https://arxiv.org/html/2403.11763v1#bib.bib13), (https://arxiv.org/html/2403.11763v1#bib.bib14), (https://arxiv.org/html/2403.11763v1#bib.bib15), (https://arxiv.org/html/2403.11763v1#bib.bib16), (https://arxiv.org/html/2403.11763v1#bib.bib17)\]. For continuous-time linear systems, a half plane divided by an eigenvector is invariant \[(https://arxiv.org/html/2403.11763v1#bib.bib14)\]. For discrete-time systems, an invariant set can be constructed iteratively by state propagation. These methods focus on invariance but not safety. Building upon invariance, different methodologies have been proposed to synthesize control barrier functions.

The first type of methods is reachability-based methods. Given a target set and a safe set, solving an optimal control problem returns a set of states starting from which the dynamical system can stay in the safe set and reach the target set. Such a set is usually the zero super-level set of a value function. Naturally, if only safety is considered over a finite horizon in the optimal control problem, the value function is a finite-time CBF \[(https://arxiv.org/html/2403.11763v1#bib.bib18)\]. More recently, the relationship between the safe value function and a CBF has been established \[(https://arxiv.org/html/2403.11763v1#bib.bib19)\]. Solving this problem directly involves computing the solution of a Hamilton-Jacobi partial differential equation \[(https://arxiv.org/html/2403.11763v1#bib.bib20), (https://arxiv.org/html/2403.11763v1#bib.bib21), (https://arxiv.org/html/2403.11763v1#bib.bib22), (https://arxiv.org/html/2403.11763v1#bib.bib23)\], which is computationally difficult for generic nonlinear systems.

The second type of methods proposed recently involves learning-based approaches. Unlike the optimal control formulation which considers the entire state space, learning-based methods rely on a finite data-set. Supervised learning-based methods have been proposed \[(https://arxiv.org/html/2403.11763v1#bib.bib24), (https://arxiv.org/html/2403.11763v1#bib.bib25)\], where a demonstrator is required to collect data. A neural network with a loss function encoding the conditions that a CBF needs to satisfy is used in \[(https://arxiv.org/html/2403.11763v1#bib.bib26), (https://arxiv.org/html/2403.11763v1#bib.bib27), (https://arxiv.org/html/2403.11763v1#bib.bib28), (https://arxiv.org/html/2403.11763v1#bib.bib29)\]. Learning-based methods show high flexibility for nonlinear and high order systems, and are amenable to applications to high degree-of-freedom robotics. However, rigorous guarantees for safety and network robustness is inherently hard for these black-box methods. At the same time, the data required by the CBF network and the controller network in the training process can be difficult to obtain, as pointed out in \[(https://arxiv.org/html/2403.11763v1#bib.bib30)\].

The third type of methods involves optimization-based approaches, especially using sum-of-squares programming \[(https://arxiv.org/html/2403.11763v1#bib.bib31)\]. Barrier functions are designed for systems with input disturbances using SOS programming in \[(https://arxiv.org/html/2403.11763v1#bib.bib32), (https://arxiv.org/html/2403.11763v1#bib.bib33)\]. When controllers are taken into consideration, alternating between synthesizing a controller and CBFs to solve sequential SOS programs is proposed in \[(https://arxiv.org/html/2403.11763v1#bib.bib34), (https://arxiv.org/html/2403.11763v1#bib.bib6), (https://arxiv.org/html/2403.11763v1#bib.bib35), (https://arxiv.org/html/2403.11763v1#bib.bib36), (https://arxiv.org/html/2403.11763v1#bib.bib37)\]. Convex quadratic CBFs, constructed from a Lyapunov function for a polytopic safe set are considered in \[(https://arxiv.org/html/2403.11763v1#bib.bib38), (https://arxiv.org/html/2403.11763v1#bib.bib39), (https://arxiv.org/html/2403.11763v1#bib.bib40)\]. Newton's method can be leveraged to guarantee local convergence to a feasible CBF \[(https://arxiv.org/html/2403.11763v1#bib.bib5)\]. As a dual to SOS programming, moment problems based on occupation measures have been proposed \[(https://arxiv.org/html/2403.11763v1#bib.bib41), (https://arxiv.org/html/2403.11763v1#bib.bib42)\]. These SOS-based methods transform the algebraic conditions for CBF to polynomial positivity conditions, and cast these conditions using SOS hierarchies. Compared with numerical methods to solve the Hamilton-Jacobi partial differential equations, SOS programming based methods are computationally more efficient provided that the polynomial basis is fixed. Compared with learning-based methods, SOS-based approaches allow for rigorous safety guarantee providing a feasible solution exactly. Our proposed method belongs to the SOS-based methods, whilst providing computational efficiency improvements and feasibility guarantees.

### I-C Contribution

In this paper, we focus on linear systems. Our main contribution is to propose an efficient method to design a control barrier function and an associated affine state feedback controller using sum-of-squares programming. The control barrier function and feedback controller are synthesized in one unified sum-of-squares program, thus overcoming the need for iterative algorithms \[(https://arxiv.org/html/2403.11763v1#bib.bib34), (https://arxiv.org/html/2403.11763v1#bib.bib6), (https://arxiv.org/html/2403.11763v1#bib.bib35), (https://arxiv.org/html/2403.11763v1#bib.bib36), (https://arxiv.org/html/2403.11763v1#bib.bib37)\]. Moreover, our formulation is applicable to high and mixed relative degree cases without using backstepping.

We also extend the existing literature when considering limits in the system inputs. $\mathcal{L}$-1 norm constrained limitation set is considered in \[(https://arxiv.org/html/2403.11763v1#bib.bib34), (https://arxiv.org/html/2403.11763v1#bib.bib5), (https://arxiv.org/html/2403.11763v1#bib.bib36), (https://arxiv.org/html/2403.11763v1#bib.bib39)\]. Specifically, \[(https://arxiv.org/html/2403.11763v1#bib.bib34), (https://arxiv.org/html/2403.11763v1#bib.bib5)\] introduce bilinear constraints in the sum-of-squares programming, \[(https://arxiv.org/html/2403.11763v1#bib.bib36)\] proposes a quantifier exchange to drop the dependency on the control input, and \[(https://arxiv.org/html/2403.11763v1#bib.bib39)\] proposes re-parameterization for linear systems. In our work, $\mathcal{L}$-1, $\mathcal{L}$-2, and $\mathcal{L} - \infty$ norm constrained limitations are all addressed by means of convex constraints. These input constraints can be appended to the CBF and controller synthesis program.

### I-D Organization

Section [II](https://arxiv.org/html/2403.11763v1#S2 "II Preliminaries ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints") provides some background. The convex synthesis program and extensions for linear systems are presented in Section [III](https://arxiv.org/html/2403.11763v1#S3 "III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"). Simulation results are shown in Section [IV](https://arxiv.org/html/2403.11763v1#S4 "IV Simulation Results ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"). Section [V](https://arxiv.org/html/2403.11763v1#S5 "V Conclusion ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints") concludes the paper.

## Preliminaries

### II-A Notation

For a function ${b{(x)}}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$, a set denoted by the corresponding calligraphic letter $\mathcal{B}$ is defined by $\mathcal{B}:{\{{x \in {\mathbb{R}}^{n}}:{{b{(x)}} \geq 0}\}}$. For the set $\mathcal{B}$, $\mathcal{B}^{c}$ denotes the closure of its complement, $\partial\mathcal{B}$ denotes its boundary. For a positive integer $n$, $I_{n}$ denotes the $n \times n$ identity matrix. A positive semi-definite matrix $A$ is denoted by $A \succeq 0$. $A_{ij}$ is the element of $i$-th row and $j$-th column. For a vector $a$, $a_{i}$ denotes the $i$-element. ${Tr}{(A)}$ is the trace of matrix $A$. $\Sigma{\lbrack x\rbrack}$ denotes the set of sum-of-squares polynomials in $x$. A $n \times n$ diagonal matrix is defined by ${diag}{(l_{1},\ldots,l_{n})}$, where ${l_{1},\ldots,l_{n}} \in {\mathbb{R}}$. For $c \in {\mathbb{R}}^{n}$ and $\epsilon > 0$, ${\mathcal{E}{(c,\epsilon)}}:={\{{x \in {\mathbb{R}}^{n}}:{{\|{x - c}\|}_{2}^{2} \leq \epsilon}\}}$.

### II-B Safety and CBF

Consider a continuous-time nonlinear control-affine system

with ${x{(t)}} \in {\mathbb{R}}^{n}$, ${u{(t)}} \in \mathcal{U} \subseteq {\mathbb{R}}^{m}$, ${{f{(x)}}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n}}},$ and ${g{(x)}}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n \times m}}$. Both functions are further assumed to be locally Lipschitz continuous. Our goal is to design a state feedback controller $u{(x)}$ such that the solution $x{(t,x_{0})}$ of the closed-loop system $\overset{˙}{x} = {{f{(x)}} + {g{(x)}u{(x)}}}$ that starts from ${x{}} = x_{0}$, with $x_{0}$ belonging to a set of *initial conditions* $\mathcal{I}$, stays within a *safe set* $\mathcal{S}$ for every $t$ that belongs to the domain of definition of the solution. If such a controller $u{( \cdot )}$ exists, we say the system is *safe*.

By a slight abuse of terminology, for our purposes we introduce the following definition:

### Definition 1 (Forward Invariance)

Consider system $\overset{˙}{x} = {F{(x)}}$, where $F:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n}}$ is a locally Lipschitz continuous vector field. A set $\mathcal{C} = {\{{x \in {\mathbb{R}}^{n}}:{{c{(x)}} \geq 0}\}}$, where $c:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is a continuously differentiable function, is forward invariant for $\overset{˙}{x} = {F{(x)}}$ if

If ${F{(x)}} = {{f{(x)}} + {g{(x)}u{(x)}}}$, we will refer to $\mathcal{C}$ as a control invariant set, to the function $c{( \cdot )}$ as a control barrier function (CBF) and to $u{(x)}$ as a safe controller.

Local Lipschitz continuity of $F$ implies local existence and uniqueness of the solution. The requirement ((https://arxiv.org/html/2403.11763v1#S2.E2 "2 ‣ Definition 1 (Forward Invariance). ‣ II-B Safety and CBF ‣ II Preliminaries ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) guarantees that the solution remains within the set $\mathcal{C}$ throughout its interval of definition.

### II-C Sum-of-Squares Programming

### Definition 2

A polynomial $p{(x)}$ is said to be a sum-of-squares polynomial in $x \in {\mathbb{R}}^{n}$ if there exist $M$ polynomials $p_{i}{(x)}$, ${i = {1,\ldots,M}},$ such that

We also call ((https://arxiv.org/html/2403.11763v1#S2.E3 "3 ‣ Definition 2. ‣ II-C Sum-of-Squares Programming ‣ II Preliminaries ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) a sum-of-squares decomposition for $p{(x)}$. Clearly, if a function $p{(x)}$ has a sum-of-squares decomposition, then it is non-negative for all $x \in {\mathbb{R}}^{n}$. Computing the sum-of-squares decomposition ((https://arxiv.org/html/2403.11763v1#S2.E3 "3 ‣ Definition 2. ‣ II-C Sum-of-Squares Programming ‣ II Preliminaries ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) can be efficient as it is equivalent to a positive semidefinite feasibility program.

### Lemma 1

Consider a polynomial $p{(x)}$ of degree $2d$ in $x \in {\mathbb{R}}^{n}$. Let $z{(x)}$ be a vector of all monomials of degree less than or equal to $d$. Then $p{(x)}$ admits a sum-of-squares decomposition if and only if

In Lemma (https://arxiv.org/html/2403.11763v1#Thmlemma1 "Lemma 1. ‣ II-C Sum-of-Squares Programming ‣ II Preliminaries ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"), $z{(x)}$ is a user-defined monomial basis if $d$ and $n$ are fixed. In the worst case, $z{(x)}$ has $\begin{pmatrix}
\end{pmatrix}$ components, and $Q$ is a $\begin{pmatrix}
\end{pmatrix} \times \begin{pmatrix}
\end{pmatrix}$ square matrix. The necessity of Lemma (https://arxiv.org/html/2403.11763v1#Thmlemma1 "Lemma 1. ‣ II-C Sum-of-Squares Programming ‣ II Preliminaries ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints") is natural from the definition of positive semi-definite matrix, considering the monomial $z{(x)}$ as a vector of new variables $z_{i}$. The sufficiency is shown by factorizing $Q = {L^{\top}L}$. Then ${z{(x)}^{\top}Qz{(x)}} = {{({Lz{(x)}})}^{\top}Lz{(x)}} = {\|{Lz{(x)}}\|}_{2}^{2} \geq 0$.

Given $z{(x)}$, finding $Q$ to decompose $f{(x)}$ as in ((https://arxiv.org/html/2403.11763v1#S2.E4 "4 ‣ Lemma 1. ‣ II-C Sum-of-Squares Programming ‣ II Preliminaries ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) is a semi-definite program, which can be solved efficiently using interior point methods. Selecting the basis $z{(x)}$ depends on the structure of $p{(x)}$ to be decomposed.

### Definition 3

A set $\mathcal{X} \subset {\mathbb{R}}^{n}$ is *semi-algebraic* if it can be represented using polynomial equality and inequality constraints. If there are only equality constraints, the set is *algebraic*.

### Lemma 2 (S-procedure)

Suppose ${t{(x)}} \in {\Sigma{\lbrack x\rbrack}}$, then

Suppose ${l{(x)}} \in {{\mathbb{R}}{\lbrack x\rbrack}}$, then

In general, compared with the Positivstellensatz\[(https://arxiv.org/html/2403.11763v1#bib.bib43)\], the S-procedure only gives a sufficient condition for the emptiness of a semi-algebraic set.

## Convex Design for Linear Systems

In this section, we propose convex synthesis programs to construct a CBF and an affine safe feedback controller. In Section [III-A](https://arxiv.org/html/2403.11763v1#S3.SS1 "III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"), we first consider a *global* design for $\mathcal{B} = {\{{x \in {\mathbb{R}}^{n}}:{{b{(x)}} \geq 0}\}}$ to be control invariant. For this case, we consider the unsafe set $\mathcal{S}^{c}$ to be bounded on a subspace of ${\mathbb{R}}^{n}$. This is commonly for robot collision avoidance problems, where the position space is a subspace of the robot state space. The control invariant set $\mathcal{B}$ is constructed *globally* as its projection to the subspace of $\mathcal{S}^{c}$ is unbounded. For the second case in Section [III-B](https://arxiv.org/html/2403.11763v1#S3.SS2 "III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"), we construct a control invariant set $\mathcal{B}^{c} = {\{{x \in {\mathbb{R}}^{n}}:{{b{(x)}} \leq 0}\}}$ around a bounded initial set. This control invariant set is called *local* as we will show it is bounded on ${\mathbb{R}}^{n}$.

Consider a continuous-time linear system:

where ${x{(t)}} \in {\mathbb{R}}^{n}$, ${u{(t)}} \in \mathcal{U} \subseteq {\mathbb{R}}^{m}$ are the state and control input, and $A \in {\mathbb{R}}^{n \times n}$, $B \in {\mathbb{R}}^{n \times m}$. We assume that the system is stabilizable. Throughout the paper, the CBF $b{(x)}$ and feedback controller $u{(x)}$ are parameterized as follows.

where ${\Omega \in {\mathbb{R}}^{n \times n}},{Y \in {\mathbb{R}}^{m \times n}}$ are matrices to be designed, $c \in {\mathbb{R}}^{n}$ and $d \in {\mathbb{R}}^{m}$ are constant vectors that will be clear in the sequel.

### III-A Global Design

Consider the safe set $\mathcal{S}$ defined by a union of semi-algebraic sets as:

where $x = {\lbrack{\overline{x}}^{\top},{\underset{¯}{x}}^{\top}\rbrack}^{\top}$, with $\overline{x} \in {\mathbb{R}}^{\overline{n}}$, $\underset{¯}{x} \in {\mathbb{R}}^{\underset{¯}{n}}$ and ${\overline{n} + \underset{¯}{n}} = n$. If $\underset{¯}{n} = 0$, the safe set is defined over all the states.

### Assumption 1

$\mathcal{S}$ is a semi-algebraic set, and $\mathcal{S}^{c}$ is bounded on the space ${\mathbb{R}}^{\overline{n}}$.

Let $c = {\lbrack{\overline{c}}^{\top},{\underset{¯}{c}}^{\top}\rbrack}^{\top} \in {\mathbb{R}}^{n}$ be a vector of constants such that rank($\lbrack B,{Ac}\rbrack$) = rank($B$), and consider the following optimization program:

${{0 \prec \overline{\Omega} = {\overline{\Omega}}^{\top} \in {\mathbb{R}}^{\overline{n} \times \overline{n}}},{0 \succ \underset{¯}{\Omega} = {\underset{¯}{\Omega}}^{\top} \in {\mathbb{R}}^{\underset{¯}{n} \times \underset{¯}{n}}}},$

${{0 \prec R = R^{\top} \in {\mathbb{R}}^{\overline{n} \times \overline{n}} \succ 0},{Y \in {\mathbb{R}}^{m \times n}}},$

${{{\sigma_{1}{(\overline{x})}},\ldots,{\sigma_{o}{(\overline{x})}}} \in {\Sigma{\lbrack\overline{x}\rbrack}}},{\epsilon > 0}$

$\Omega = \begin{bmatrix}

${{\Omega A^{\top}} + {Y^{\top}B^{\top}} + {A\Omega} + {BY}} \succeq 0$

I_{\overline{n}} & \overline{\Omega}
\end{bmatrix} \succeq 0$

${{{{1 - {{\overline{x}}_{c}^{\top}R{\overline{x}}_{c}}} + {\sum\limits_{i = 1}^{o}{\sigma_{i}{(\overline{x})}s_{i}{(\overline{x})}}}} - \epsilon} \in {\Sigma{\lbrack\overline{x}\rbrack}}},$

where ${\overline{x}}_{c} = {\overline{x} - \overline{c}}$, ${\underset{¯}{x}}_{c} = {\underset{¯}{x} - \underset{¯}{c}}$, $x_{c} = {x - c}$. Notice that this a convex optimization program, where the objective function is linear, and is subject to semi-define constraints The cost function is to minimize the volume of the set $\{{\overline{x} \in {\mathbb{R}}^{\overline{n}}}:{{{- {{({\overline{x} - \overline{c}})}^{\top}{\overline{\Omega}}^{- 1}{({\overline{x} - \overline{c}})}}} + 1} \geq 0}\}$, thus indirectly maximizing the volume of the projection set of $\mathcal{B}$ on the space ${\mathbb{R}}^{\overline{n}}$. An alternative formulation is ${\max\log}{\det{\overline{\Omega}}^{- 1}}$ \[(https://arxiv.org/html/2403.11763v1#bib.bib44), Section 2.2.4\]. However, this is not supported by SeDuMi, which is the solver we are using to solve the semi-definite program. In the following theorem, we give the main result of the paper, a convex program to synthesize a CBF $b{(x)}$ and a feedback controller $u{(x)}$ under Assumption (https://arxiv.org/html/2403.11763v1#Thmassumption1 "Assumption 1. ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints").

### Theorem 1

Consider Assumption (https://arxiv.org/html/2403.11763v1#Thmassumption1 "Assumption 1. ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"), and let $\mathcal{U} = {\mathbb{R}}^{m}$. Assume that a solution to ([III-A](https://arxiv.org/html/2403.11763v1#S3.E10 "III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) exists and is denoted by $\overline{\Omega},\underset{¯}{\Omega},R,Y,{\{{\sigma_{i}{( \cdot )}}\}}_{i = 1}^{o},\epsilon$. Set ${u{(x)}} = {{Y\Omega^{- 1}{({x - c})}} + d}$ where $d \in {\mathbb{R}}^{m}$ is such that ${{Bd} + {Ac}} = 0$. We then have that

$\mathcal{B}:={\{{x \in {\mathbb{R}}^{n}}:{{{{({x - c})}^{\top}\Omega^{- 1}{({x - c})}} - 1} \geq 0}\}} \subseteq \mathcal{S}$.

$\mathcal{B}$ is a control invariant set for $\overset{˙}{x} = {{Ax} + {Bu{(x)}}}$.

### Proof

We first prove that satisfaction of ([10g](https://arxiv.org/html/2403.11763v1#S3.E10.7 "10g ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")), ([10k](https://arxiv.org/html/2403.11763v1#S3.E10.11 "10k ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) and ([10l](https://arxiv.org/html/2403.11763v1#S3.E10.12 "10l ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) are sufficient for $\mathcal{B} \subseteq \mathcal{S}$. Given that $R \succ 0$ and $\overline{\Omega} \succ 0$, using Schur complement, ([10k](https://arxiv.org/html/2403.11763v1#S3.E10.11 "10k ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) is equivalent to ${R - {\overline{\Omega}}^{- 1}} \succeq 0$. Multiplying the latter condition by ${\overline{x}}_{c}^{\top} = {({\overline{x} - \overline{c}})}^{\top}$ on the left and by ${\overline{x}}_{c}$ on the right, we obtain

Then we have the following relationship

The former set inclusion implies the following relationship for the closures of the associated sets,

The two sets involved are subsets of ${\mathbb{R}}^{\overline{n}}$. Considering them as the base of cylinder sets in ${\mathbb{R}}^{n}$, we obtain

Invoking Lemma (https://arxiv.org/html/2403.11763v1#Thmlemma2 "Lemma 2 (S-procedure). ‣ II-C Sum-of-Squares Programming ‣ II Preliminaries ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints") for polynomial functions $s_{i}{(\overline{x})}$, $i = {1,\ldots,o}$, ([10l](https://arxiv.org/html/2403.11763v1#S3.E10.12 "10l ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) indicates that

which in turn implies

Converting the above relationship in set inclusion form, we have

Combining ((https://arxiv.org/html/2403.11763v1#S3.E11 "11 ‣ Proof. ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) with ((https://arxiv.org/html/2403.11763v1#S3.E14 "14 ‣ Proof. ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) implies

Given that $\underset{¯}{\Omega} \prec 0$, and using the block representation in ([10g](https://arxiv.org/html/2403.11763v1#S3.E10.7 "10g ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")), we have

Using ((https://arxiv.org/html/2403.11763v1#S3.E16 "16 ‣ Proof. ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) into the relationship in ((https://arxiv.org/html/2403.11763v1#S3.E15 "15 ‣ Proof. ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")), and recalling that $\mathcal{B} = {\{{x \in {\mathbb{R}}^{n}}:{{{{({x - c})}^{\top}\Omega^{- 1}{({x - c})}} - 1} \geq 0}\}}$, we obtain

We then prove that $\mathcal{B}$ (the zero super-level set of $b{(x)}$) is a control invariant set. Since $\Omega$ (decomposed as in ([10g](https://arxiv.org/html/2403.11763v1#S3.E10.7 "10g ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"))), is optimal for ([III-A](https://arxiv.org/html/2403.11763v1#S3.E10 "III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")), it will have to satisfy ([10h](https://arxiv.org/html/2403.11763v1#S3.E10.8 "10h ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")). We will show that ([10h](https://arxiv.org/html/2403.11763v1#S3.E10.8 "10h ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) is sufficient for $\mathcal{B}$ to be control invariant, thus establishing the claim. We guarantee control invariance by using an affine state feedback controller as ([8b](https://arxiv.org/html/2403.11763v1#S3.E8.2 "8b ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")), where $K \in {\mathbb{R}}^{m \times n}$. Transforming the coordinate from $x$ to $x_{c} = {x - c}$, and since $d$ is such that ${{Bd} + {Ac}} = 0$, the transformed system dynamics are given by

In the new coordinate ${{b{(x)}}|}_{x = {x_{c} + c}} = {\overset{\sim}{b}{(x_{c})}} = {{x_{c}^{\top}\Omega^{- 1}x_{c}} - 1}$. If ${\overset{˙}{b}{(x)}} \geq 0$ for any $x \in {\mathbb{R}}^{n}$, then $\mathcal{B}$ is invariant. Notice that ${\overset{˙}{b}{(x)}} \geq 0$ is equivalent to

Satisfaction of ((https://arxiv.org/html/2403.11763v1#S3.E18 "18 ‣ Proof. ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) for any $x \in {\mathbb{R}}^{n}$ is equivalent to

Left and right multiplying by $\Omega$ on both sides of ((https://arxiv.org/html/2403.11763v1#S3.E19 "19 ‣ Proof. ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")), we obtain

Substituting $K\Omega$ with a new matrix $Y \in {\mathbb{R}}^{m \times n}$, and noticing that $\Omega$ is invertible, we equivalently obtain ([10h](https://arxiv.org/html/2403.11763v1#S3.E10.8 "10h ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")). The latter is thus a sufficient condition for $\mathcal{B}$ to be invariant.

By the proof of the previous part it follows that ${u{(x)}} = {{K{({x - c})}} + d}$ renders $\mathcal{B}$ invariant. Moreover, $Y = {K\Omega}$, which in turn implies that $K = {Y\Omega^{- 1}}$. Therefore, ${u{(x)}} = {{Y\Omega^{- 1}{({x - c})}} + d}$ guarantees invariance. ∎

Figure 2: Visualization of Case 2 in Section I-A, where the state $\overline{x} = {\lbrack x_{1},x_{2}\rbrack} \in {\mathbb{R}}^{2}$, $\underset{¯}{x} = x_{3} \in {\mathbb{R}}$. The safe set $\mathcal{S}:={\{{x \in {\mathbb{R}}^{3}}:{{s{(\overline{x})}} \geq 0}\}}$ is a cylinder expanded from a set on ℝ2 to ℝ3. The region outside of the blue hyperboloid represents the set ℬ:= {x ∈ ℝ3: b(x) ≥ 0}, which is control invariant from our construction. The safe set $\mathcal{S}:={\{{x \in {\mathbb{R}}^{3}}:{{s{(\overline{x})}} \geq 0}\}}$ is the outside of the inner red cylinder. We can see from the figure that ℬ ⊆ 𝒮.

Figure (https://arxiv.org/html/2403.11763v1#S3.F2 "Figure 2 ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints") visualizes an example of a control invariant set $\mathcal{B}$ and $\mathcal{S}$ on ${\mathbb{R}}^{3}$. To gain an intuitive understanding of Theorem (https://arxiv.org/html/2403.11763v1#Thmtheorem1 "Theorem 1. ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"), we analytically construct a control invariant set for a simple example.

### Example 1

Consider a car moving along a line

where $\overline{x}$ represents the position and $\underset{¯}{x} \in {\mathbb{R}}$ represents the velocity. Let

We follow the construction in Theorem (https://arxiv.org/html/2403.11763v1#Thmtheorem1 "Theorem 1. ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"). The vector $c \in {\mathbb{R}}^{2}$ that satisfies rank($\lbrack{BAc}\rbrack$) = rank($B$) is any vector such that $\underset{¯}{c} = 0$. We also fix $\overline{c} = 0$. Consequently $d = 0$.

Consider the decision variables $\overline{\Omega} \in {\mathbb{R}}_{> 0}$, $\underset{¯}{\Omega} \in {\mathbb{R}}_{< 0}$, $R \in {\mathbb{R}}$, $Y = {\lbrack{Y_{1}Y_{2}}\rbrack} \in {\mathbb{R}}^{1 \times 2}$, ${\sigma{(\overline{x})}} \in {\Sigma{\lbrack\overline{x}\rbrack}}$ and $\varepsilon > 0$. The constraints in ([III-A](https://arxiv.org/html/2403.11763v1#S3.E10 "III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) can be written as follows

${\Omega = \begin{bmatrix}

\end{bmatrix} \succeq 0},$

\end{bmatrix} \succeq 0},$

${{{{1 - {R{\overline{x}}^{2}}} + {\sigma{(\overline{x})}{({{\overline{x}}^{2} - 1})}}} - \epsilon} \in {\Sigma{\lbrack\overline{x}\rbrack}}}.$

Looking at the spectrum of the matrix in ([20f](https://arxiv.org/html/2403.11763v1#S3.E20.6 "20f ‣ Example 1. ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")), we conclude that ([20f](https://arxiv.org/html/2403.11763v1#S3.E20.6 "20f ‣ Example 1. ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) is equivalent to $Y_{2} > 0$ and ${\underset{¯}{\Omega} + Y_{1}} = 0$. Condition ([20i](https://arxiv.org/html/2403.11763v1#S3.E20.9 "20i ‣ Example 1. ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) is equivalently expressed as ${R - {\overline{\Omega}}^{- 1}} \geq 0$. As for $\sigma{(\overline{x})}$, we set it to be an SOS polynomial of degree $0$, hence, ${\sigma{(\overline{x})}} = \overline{\sigma} \geq 0$. Writing the polynomial in ([20j](https://arxiv.org/html/2403.11763v1#S3.E20.10 "20j ‣ Example 1. ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) as

and bearing in mind Lemma (https://arxiv.org/html/2403.11763v1#Thmlemma1 "Lemma 1. ‣ II-C Sum-of-Squares Programming ‣ II Preliminaries ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"), one realizes that condition ([20j](https://arxiv.org/html/2403.11763v1#S3.E20.10 "20j ‣ Example 1. ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) is equivalent to ${\overline{\sigma} - R} \geq 0$ and ${1 - \overline{\sigma} - \epsilon} \geq 0$. In summary, we have the following conditions

We set $Y = {\lbrack{Y_{1}Y_{2}}\rbrack}:={\lbrack{- {\underset{¯}{\Omega}Y_{2}}}\rbrack}$, with $\underset{¯}{\Omega},Y_{2}$ any positive numbers, and $\overline{\Omega} > 1$, $R = \overline{\sigma} = {\overline{\Omega}}^{- 1}$, $\epsilon \leq {1 - \overline{\sigma}}$. Note that setting $\overline{\Omega} > 1$ is necessary for having the constraint ${\overline{\sigma} + \epsilon} \leq 1$ satisfied. To minimize the cost function, we should take $\overline{\Omega}$ as small as possible. We obtain that the function $b{(x)}$ that defines $\mathcal{B}:={\{{x \in {\mathbb{R}}^{n}}:{{b{(x)}} \geq 0}\}}$ is

and the feedback controller is

resulting in the closed-loop dynamics

Figure (https://arxiv.org/html/2403.11763v1#S3.F3 "Figure 3 ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints") shows a sketch of the sets $\mathcal{S}^{c}$, $\mathcal{B}$. We first observe that $\overline{\Omega} > 1$ established above guarantees that $\mathcal{B} \subset \mathcal{S}$. Second, formulating $\mathcal{B}$ in terms of the entire state vector $x$ results in a set $\mathcal{B}$ which differs from the one a designer could expect, namely, $\mathcal{B}:={\{{x \in {\mathbb{R}}^{n}}:{{|\overline{x}|} \geq \overline{b}}\}}$, with $\overline{b} > 1$.

For any feasible choice of the design parameters, the obtained closed-loop matrix has at least one unstable eigenvalue. To have an understanding of the state response, we compute the spectral representation $e^{{({A + {BK}})}t}$ for these values of the design parameters: $\underset{¯}{\Omega} = {- 4}$, $\overline{\Omega} = 2$, $Y_{2} = 4$. Then the spectral representation is given by

Hence, if the system starts from the initial condition $x = \begin{bmatrix}
\end{bmatrix}^{\top} = {\lbrack{20}\rbrack}^{\top}$, which is on the boundary of $\mathcal{B}$, it will evolve as

As a result, both position and velocity diverge exponentially but are certified to stay within $\mathcal{B}$.

The CBF $b{(x)}$ constructed in the previous example is a function of the whole state $x = {\lbrack\overline{x},\underset{¯}{x}\rbrack}^{\top}$. However, given the definition of $\mathcal{S}^{c}$, which only constrains the position variable $\overline{x}$, one could alternatively consider a candidate barrier function ${\overline{b}{(x)}}:={{{({\overline{x} - \overline{c}})}^{\top}{\overline{\Omega}}^{- 1}{({\overline{x} - \overline{c}})}} - 1}$ and the corresponding set $\overline{\mathcal{B}}:={\{{x \in {\mathbb{R}}^{n}}:{{\overline{b}{(x)}} \geq 0}\}}$. We will show below that the set $\overline{\mathcal{B}}$ can not be control invariant using linear feedback $u{(x)}$. Denote the projection matrix

Use ${\overline{x}}_{c}$ instead of $\overline{x} - \overline{c}$, and let ${\overline{x}}_{c} = {\Pi x_{c}}$. We can derive the following identity

and express the invariance condition as

Figure 3: Pictorial illustration for Example 1. The green set $\mathcal{S}^{c}:={\{{x \in {\mathbb{R}}^{2}}:{{{\overline{x}}^{2} - 1} \leq 0}\}}$ is expanded from a segment on ℝ1. The designed control invariant set $\mathcal{B}:={\{ x \in {\mathbb{R}}^{2}:{\overline{\Omega}}^{- 1}{\overline{x}}^{2} - \underset{¯}{\Omega}{\underset{¯}{x}}^{2} - 1 \geq 0}$} has been filled in yellow. Intuitively, with a large velocity, i.e. larger $|\underset{¯}{x}|$, the planar car should stay further away from the obstacle, which can be seen by the gap between ℬ and 𝒮c being larger for larger $|\overline{x}|$.

We partition $A + {BK}$ according to the partition ${\mathbb{R}}^{\overline{n}} \times {\mathbb{R}}^{\underset{¯}{n}}$ to obtain

The invariance condition can be expressed as

which leads to a convex condition by multiplying $\begin{bmatrix}
\end{bmatrix}$ on both sides of the matrices in the inequality. However, the possibility of fulfilling such constraint appears to be related to the possibility of shaping the spectra of ${\overline{A}}_{1} + {\overline{B}\overline{K}}$ and ${\overline{A}}_{2} + {\overline{B}\underset{¯}{K}}$, hence, to the controllability of the pairs $({\overline{A}}_{1},\overline{B})$, $({\overline{A}}_{2},\overline{B})$. Going back to Example (https://arxiv.org/html/2403.11763v1#Thmexample1 "Example 1. ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"), we have ${({\overline{A}}_{1},\overline{B})} = {}$, and ${({\overline{A}}_{2},\overline{B})} = {}$, which shows lack of controllability of both pairs. As a result, the invariance condition above is

which shows that enforcing invariance for the set $\overline{\mathcal{B}}$ via feedback is impossible due to the lack of controllability (the matrix has a positive and a negative eigenvalue).

Figure 4: Exact invariant set for the planar car using $u = {{K_{1}\overline{x}} + {K_{2}\underset{¯}{x}}}$, where ${K_{1} = {Y_{1}{\overline{\Omega}}^{- 1}} = 2},{K_{2} = {Y_{2}{\underset{¯}{\Omega}}^{- 1}} = {- 1}}$. The green vertical lines are the boundary of 𝒮c, the set filled in blue is the exact invariant set.

Figure 5: The union of control invariant set ℬ⋃ℬ′. ℬ is computed by solving our program (III-A) which results in $\overline{\Omega} = 1$. Physical considerations for ℬ′ is obtained from the planar car. The union is also control invariant, and close to the exact invariant set as in Figure 4.

The exact control invariant set for Example (https://arxiv.org/html/2403.11763v1#Thmexample1 "Example 1. ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints") numerically computed by the level-set method toolbox \[(https://arxiv.org/html/2403.11763v1#bib.bib45)\] is shown in Figure (https://arxiv.org/html/2403.11763v1#S3.F4 "Figure 4 ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"). To compute the exact control invariant set, the control feedback $u$ is set in the linear form $u = {Y\Omega^{- 1}x}$, where $Y$ and $\Omega$ have the same numerical values as those chosen in Example (https://arxiv.org/html/2403.11763v1#Thmexample1 "Example 1. ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints") ($\underset{¯}{\Omega} = {- 4}$, $\overline{\Omega} = 2$, $Y_{1} = 4$, $Y_{2} = 4$). In comparison, our computed control invariant set $\mathcal{B}$ determined analytically and depicted in Figure (https://arxiv.org/html/2403.11763v1#S3.F3 "Figure 3 ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints") is conservative when $\overline{\Omega} \neq 1$. This can be alleviated by minimizing ${Tr}{(\overline{\Omega})}$ as in the program ([III-A](https://arxiv.org/html/2403.11763v1#S3.E10 "III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")). Conservative behaviour is also encountered in the first and third quadrants, where the boundary of the exact invariant set coincides with the safe set $\mathcal{S}$. This is natural as the planar car is moving away from the unsafe set $\mathcal{S}^{c}$, which has been filled in green, in these regions. Our method, however, computes a control invariant set $\mathcal{B}$, that is symmetric with respect to the $\overline{x}$-axis. In practice, one can reduce this conservativeness by taking the union of our computed control invariant set $\mathcal{B}$ with other invariant sets, such as $\mathcal{B}^{\prime} = {\{{x \in {\mathbb{R}}^{2}}:{{b^{\prime}{(x)}}:={\underset{¯}{x}\overline{x}} \geq 0}\}}$. The new control invariant set is shown in Figure (https://arxiv.org/html/2403.11763v1#S3.F5 "Figure 5 ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"). The control barrier function corresponds to this union set can be defined by

Such a kind of CBF has been investigated in \[(https://arxiv.org/html/2403.11763v1#bib.bib46)\].

According to Nagumo's Theorem \[(https://arxiv.org/html/2403.11763v1#bib.bib4)\], a compact set is invariant for a vector field if and only if the vector field is within the tangent cone for all points on the boundary of the set. For a compact and closed set $\mathcal{B}$, this is equivalent to having ${\overset{˙}{b}{(x)}} \geq 0$, for any $x$ such that ${b{(x)}} = 0$. However in our proposed convex conditions ([III-A](https://arxiv.org/html/2403.11763v1#S3.E10 "III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")), we enforce a "strengthened" condition that ${\overset{˙}{b}{(x)}} \geq 0$, for any $x \in {\mathbb{R}}^{n}$. Nevertheless, we show in the following proposition that this does not introduce any conservativeness in the case $\overline{n} = n$.

### Proposition 1

Consider the system $()$, constant $c \in {\mathbb{R}}^{n}$ such that ${{rank}{({\lbrack{BAc}\rbrack})}} = {{rank}{(B)}}$ and a quadratic function ${b{(x)}} = {{{({x - c})}^{\top}\Omega^{- 1}{({x - c})}} - 1}$, with $\Omega \succ 0$. If there exists a feedback controller $u = {{K{({x - c})}} + d}$, with $d$ satisfying ${{Bd} + {Ac}} = 0$, such that ${\overset{˙}{b}{(x)}} \geq 0$ for any $x$ such that ${b{(x)}} = 0$, then ${\overset{˙}{b}{(x)}} \geq 0$ for any $x \in {\mathbb{R}}^{n}$.

### Proof

For $x = c$, ${\overset{˙}{b}{(x)}} = {2{({x - c})}^{\top}\Omega^{- 1}{({A + {BK}})}{({x - c})}} = 0$. On the other hand, observe that for any point $x \neq c \in {\mathbb{R}}^{n}$, there exists $y = {{\frac{1}{\lambda}{({x - c})}} + c}$ with $\lambda = {({{({x - c})}^{\top}\Omega^{- 1}{({x - c})}})}^{1/2} > 0$, such that ${b{(y)}} = 0$. The function $\overset{˙}{b}{(x)}$ can be rewritten as

As ${b{(y)}} = 0$, we have ${\overset{˙}{b}{(y)}} \geq 0$ by the proposition's statement that assumes this is the case for $y$ such that ${b{(y)}} = 0$, which implies ${\overset{˙}{b}{(x)}} \geq 0$, as claimed. ∎

As a result of Proposition (https://arxiv.org/html/2403.11763v1#Thmproposition1 "Proposition 1. ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"), the synthesized controller $u{(x)}$ endows robustness as ${\overset{˙}{b}{(x)}} \geq 0$ for any $x$ such that ${b{(x)}} < 0$. If the system starts from an unsafe point $x$, our synthesized CBF guarantees that there exists a controller that forces the state of the system enters the safe region, if the problem is feasible. This property is especially helpful for unexpected perturbations to the system.

### Corollary 1

Assume that the projection of $\mathcal{S}^{c}$ onto ${\mathbb{R}}^{\overline{n}}$ is a polytope on the space ${\mathbb{R}}^{\overline{n}}$ with vertices denoted by ${v_{1},\ldots,v_{o^{\prime}}} \in {\mathbb{R}}^{\overline{n}}$. Constraint ([10l](https://arxiv.org/html/2403.11763v1#S3.E10.12 "10l ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) can be replaced by linear constraints:

### Proof

Constraint ([10l](https://arxiv.org/html/2403.11763v1#S3.E10.12 "10l ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) implies $\mathcal{S}^{c} \subseteq \mathcal{R}:={\{{x \in {\mathbb{R}}^{n}}:{{{- {{({\overline{x} - \overline{c}})}^{\top}R{({\overline{x} - \overline{c}})}}} + 1} \geq 0}\}}$. Denote the projection set of $\mathcal{S}^{c}$ onto ${\mathbb{R}}^{\overline{n}}$ by $\overline{\mathcal{S}^{c}}$, which is a polytope, and the projection set of $\mathcal{R}$ onto ${\mathbb{R}}^{\overline{n}}$ by $\overline{\mathcal{R}}$, which is an ellipsoid. We then have $\mathcal{S}^{c} \subseteq \mathcal{R}$ is equivalent to $\overline{\mathcal{S}^{c}} \subseteq \overline{\mathcal{R}}$, which can be verified by the constraints of all the vertices of $\overline{\mathcal{S}^{c}}$ be within $\overline{\mathcal{R}}$. We conclude the proof. ∎

The number of linear constraints ((https://arxiv.org/html/2403.11763v1#S3.E21 "21 ‣ Corollary 1. ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) depends on $o^{\prime}$. If the polytopic $\mathcal{I}$ has $l$ facets, then the maximum number of vertices is $\left( \begin{array}{l}
{o - \left\lceil {n/2} \right\rceil} \\
\left\lfloor {n/2} \right\rfloor
\end{array} \right) + \left( \begin{array}{l}
{o - \left\lfloor {n/2} \right\rfloor - 1} \\
{\left\lceil {n/2} \right\rceil - 1}
\end{array} \right)$, which could be quite large. For practical purposes, Corollary (https://arxiv.org/html/2403.11763v1#Thmcorollary1 "Corollary 1. ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints") becomes useful if the number of vertices is moderate.

### III-B Local Design

In the previous section, we construct a control invariant set $\mathcal{B}:={\{{x \in {\mathbb{R}}^{n}}:{{b{(x)}} \geq 0}\}}$ globally, it is unbounded on ${\mathbb{R}}^{\overline{n}}$, and naturally unbounded on ${\mathbb{R}}^{n}$. As shown in Example (https://arxiv.org/html/2403.11763v1#Thmexample1 "Example 1. ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"), the closed-loop trajectory diverges using the co-designed linear feedback controller $u{(x)}$. This is undesired in many applications where boundedness of trajectories is a prerequisite. In this section, we consider constructing a bounded control invariant set around a bounded set of initial conditions $\mathcal{I}$, and inside a intersection of half planes, i.e. the safe set $\mathcal{S}$. The new control invariant set will also be parameterized by a quadratic function. To ease notation, we still use ${b{(x)}} = {{x_{c}^{\top}\Omega^{- 1}x_{c}} - 1}$, but the new control invariant set will be derived by a sub-level set of the function, i.e. $\mathcal{B}^{c}:={\{{x \in {\mathbb{R}}^{n}}:{{b{(x)}} \leq 0}\}}$, for boundness. The initial set is defined as an intersection of semi-algebraic sets:

where ${w_{1}{(x)}},\ldots,{w_{l}{(x)}}$ are all polynomial functions.

### Assumption 2

$\mathcal{I}$ is a semi-algebraic set, and $\mathcal{I}$ is bounded on the space ${\mathbb{R}}^{n}$.

The safe set is defined by

where $a_{i} \in {\mathbb{R}}^{n}$, $c \in {\mathbb{R}}^{n}$ is a point in the interior of the safe set. The following theorem proposes a convex condition for ${b{(x)}} = {{{({x - c})}^{\top}\Omega^{- 1}{({x - c})}} - 1}$ to be a CBF for $({()},\mathcal{I},\mathcal{S})$, with $\mathcal{B}^{c} = {\{{x \in {\mathbb{R}}^{n}}:{{b{(x)}} \leq 0}\}}$ a control invariant set. By $b{(x)}$ to be a CBF for $({()},\mathcal{I},\mathcal{S})$ we mean that there exists $u{(x)}$ such that ${\frac{\partial{b{(x)}}}{\partial x}{({{Ax} + {Bu{(x)}}})}} \geq 0$ for all $x \in {\partial\mathcal{B}^{c}}$ and $\mathcal{I} \subseteq \mathcal{B}^{c} \subseteq \mathcal{S}$ (Figure (https://arxiv.org/html/2403.11763v1#S3.F6 "Figure 6 ‣ III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")). We again use $x_{c} = {x - c}$ for notational purpose.

Let $c \in {\mathbb{R}}^{n}$ be a constant vector such that ${{rank}{({\lbrack B,{Ac}\rbrack})}} = {{rank}{(B)}}$ as before, and consider the following optimization program.

${0 \prec \Omega = \Omega^{\top} \in {\mathbb{R}}^{n}},$

${{0 \prec R = R^{\top} \in {\mathbb{R}}^{n \times n}},{Y \in {\mathbb{R}}^{m \times n}}},$

${{{\sigma_{1}{(x)}},\ldots,{\sigma_{l}{(x)}}} \in {\Sigma{\lbrack x\rbrack}}},$

${{{\Omega A^{\top}} + {Y^{\top}B^{\top}} + {A\Omega} + {BY}} \preceq 0},$

\end{bmatrix} \succeq 0},$

${{{{- {x_{c}^{\top}Rx_{c}}} + 1} - {\sum\limits_{i = 1}^{l}{\sigma_{i}{(x)}w_{i}{(x)}}}} \in {\Sigma{\lbrack x\rbrack}}},$

${{{1 - {a_{i}^{\top}\Omega a_{i}}} \geq 0},{i = {1,\ldots,o}}},$

where $x_{c} = {x - c}$. Similarly to program ([III-A](https://arxiv.org/html/2403.11763v1#S3.E10 "III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) for global design, program ([III-B](https://arxiv.org/html/2403.11763v1#S3.E24 "III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) is a convex optimization program, since the cost function is linear, and is subject to semi-definite and linear constraints. In the following theorem, we show how to synthesize a CBF $b{(x)}$ and a feedback safe controller $u{(x)}$ by this convex program under Assumption (https://arxiv.org/html/2403.11763v1#Thmassumption2 "Assumption 2. ‣ III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints").

Figure 6: Geometric illustration of the the locally constructed CBF b(x) on ℝ2. The yellow set represents the initial set ℐ, which is bounded on ℝ2. The blue set represents the safe set 𝒮, which is defined by the intersection of half planes on ℝ2, as in. The magenta set represents the control invariant set ℬc:= {x ∈ ℝ2: b(x) ≤ 0}, which satisfies ℐ ⊆ ℬc ⊆ 𝒮.

### Theorem 2

Consider Assumption (https://arxiv.org/html/2403.11763v1#Thmassumption2 "Assumption 2. ‣ III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"), and let $\mathcal{U} = {\mathbb{R}}^{m}$. Assume that a solution to ([III-B](https://arxiv.org/html/2403.11763v1#S3.E24 "III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) exists and is denoted by $\Omega,R,Y,{\{{\sigma_{i}{( \cdot )}}\}}_{i = 1}^{l}$. Set ${u{(x)}} = {{Y\Omega^{- 1}{({x - c})}} + d}$, where $d \in {\mathbb{R}}^{m}$ is such that ${{Bd} + {Ac}} = 0$. We then have that

$\mathcal{I} \subseteq \mathcal{B}^{c} \subseteq \mathcal{S}$, where $\mathcal{I}$ is as in ((https://arxiv.org/html/2403.11763v1#S3.E22 "22 ‣ III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")), $\mathcal{B}^{c} = {\{{x \in {\mathbb{R}}^{n}}:{{b{(x)}} \leq 0}\}}$, ${b{(x)}} = {{{({x - c})}^{\top}\Omega^{- 1}{({x - c})}} - 1}$ and $\mathcal{S}$ is as in ((https://arxiv.org/html/2403.11763v1#S3.E23 "23 ‣ III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")).

$\mathcal{B}^{c}$ is a control invariant set for $\overset{˙}{x} = {{Ax} + {Bu{(x)}}}$.

### Proof

The proof that ([24e](https://arxiv.org/html/2403.11763v1#S3.E24.5 "24e ‣ III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) is sufficient for $\mathcal{B}^{c}$ to be a control invariant set, and ([24h](https://arxiv.org/html/2403.11763v1#S3.E24.8 "24h ‣ III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) ([24i](https://arxiv.org/html/2403.11763v1#S3.E24.9 "24i ‣ III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) are sufficient for $\mathcal{I} \subseteq \mathcal{B}^{c}$ is similar to the proof of Theorem (https://arxiv.org/html/2403.11763v1#Thmtheorem1 "Theorem 1. ‣ III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"). We only prove that ([24j](https://arxiv.org/html/2403.11763v1#S3.E24.10 "24j ‣ III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) is sufficient and necessary for $\mathcal{B}^{c} \subseteq \mathcal{S}$. Using Farkas' lemma \[(https://arxiv.org/html/2403.11763v1#bib.bib47)\], \[(https://arxiv.org/html/2403.11763v1#bib.bib48), Lemma 6.45\] for affine functions ${{{{a_{i}^{\top}{({x - c})}} + 1},i} = 1},{\ldots,o}$, and convex quadratic function ${{({x - c})}^{\top}\Omega^{- 1}{({x - c})}} - 1$, we have that $\mathcal{B}^{c} \subseteq \mathcal{S}$ if and only if for every $i = {1,\ldots,o}$, there exists $\lambda_{i} \geq \frac{1}{2}$ such that

By Schur complement, ((https://arxiv.org/html/2403.11763v1#S3.E25 "25 ‣ Proof. ‣ III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) holds if and only if $\Omega \succ 0$, which is true by ([24b](https://arxiv.org/html/2403.11763v1#S3.E24.2 "24b ‣ III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")), and if there exists $\lambda_{i} \geq \frac{1}{2}$ such that ${{2\lambda_{i}} - 1 - {\lambda^{2}a_{i}^{\top}\Omega a_{i}}} \geq 0$. The discriminant of the quadratic polynomial on the left hand side of the inequality is $4 - {4a_{i}^{\top}\Omega a_{i}}$. Hence, there exists $\lambda_{i}$ such that ${{2\lambda_{i}} - 1 - {\lambda_{i}^{2}a_{i}^{\top}\Omega a_{i}}} \geq 0$ if and only if ${1 - {a_{i}^{\top}\Omega a_{i}}} \geq 0$. Moreover, if ${1 - {a_{i}^{\top}\Omega a_{i}}} = 0$, then ${\lambda_{i} = 1 \geq \frac{1}{2}},$ and if ${1 - {a_{i}^{\top}\Omega a_{i}}} > 0$, then any $\lambda_{i} \in {\lbrack{1 - \sqrt{1 - {a_{i}^{\top}\Omega a_{i}}}},{1 + \sqrt{1 - {a_{i}^{\top}\Omega a_{i}}}}\rbrack}$ satisfies ${{2\lambda_{i}} - 1 - {\lambda_{i}^{2}a_{i}^{\top}\Omega a_{i}}} \geq 0$. As ${{1 + \sqrt{1 - {a_{i}^{\top}\Omega a_{i}}}} > \frac{1}{2}},$ we have shown that there exists $\lambda_{i} \geq \frac{1}{2}$ such that ${{2\lambda_{i}} - 1 - {\lambda_{i}^{2}a_{i}^{\top}\Omega a_{i}}} \geq 0$ if and only if ${1 - {a_{i}^{\top}\Omega a_{i}}} \geq 0$, which is ([24j](https://arxiv.org/html/2403.11763v1#S3.E24.10 "24j ‣ III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")). Hence, we conclude the proof. ∎

### III-C Input Constraints

In the previous sections for local design we consider the case that $\mathcal{U} = {\mathbb{R}}^{m}$. We now extend the local design result to the case that the control authority is limited. Three different types of input constraints are considered: (i) 2-norm bounds, i.e., $\mathcal{U}_{1} = {\{{u \in {\mathbb{R}}^{m}}:{{\| u\|}_{2}^{2} \leq \zeta}\}}$, where $\zeta > 0$; (ii) $\infty$-norm bounds, i.e., $\mathcal{U}_{2} = {\{{u \in {\mathbb{R}}^{m}}:{{\| u\|}_{\infty} \leq \sqrt{\zeta}}\}}$, where $\zeta > 0$; (iii) polytopic bounds, i.e., $\mathcal{U}_{3} = {\{{u \in {\mathbb{R}}^{m}}:{{Hu} \leq h}\}}$, where $H \in {\mathbb{R}}^{k \times m}$, $h \in {\mathbb{R}}^{k}$.

For $\mathcal{U} = \mathcal{U}_{1}$, consider the following optimization program with decision variables $\Omega,R,Y,{\sigma_{1}{(x)}},\ldots,{\sigma_{l}{(x)}},\mu$:

${\min{Tr}}{(\overline{\Omega})}$

${{{{()} - {()}},{{{- {d^{\top}d}} + \zeta} - \varepsilon}} > \mu > 0},$

\end{bmatrix} \succeq 0},$

and $\varepsilon > 0$ is a small constant. Program ([III-C](https://arxiv.org/html/2403.11763v1#S3.E26 "III-C Input Constraints ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) is a convex program which amends program ([III-B](https://arxiv.org/html/2403.11763v1#S3.E24 "III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) by a new semi-definite constraint ([26e](https://arxiv.org/html/2403.11763v1#S3.E26.5 "26e ‣ III-C Input Constraints ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")).

### Lemma 3

Consider Assumption (https://arxiv.org/html/2403.11763v1#Thmassumption2 "Assumption 2. ‣ III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"), and let $\mathcal{U} = \mathcal{U}_{1}$. Assume that a solution to ([III-C](https://arxiv.org/html/2403.11763v1#S3.E26 "III-C Input Constraints ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) exists and is denoted by $\Omega,R,Y,{\{{\sigma_{i}{( \cdot )}}\}}_{i = 1}^{l},\mu$. Set ${u{(x)}} = {{Y\Omega^{- 1}{({x - c})}} + d}$, where $d \in {\mathbb{R}}^{n}$ is such that ${{Bd} + {Ac}} = 0$. We then have that

$\mathcal{I} \subseteq \mathcal{B}^{c} \subseteq \mathcal{S}$, where $\mathcal{I}$ is as in ((https://arxiv.org/html/2403.11763v1#S3.E22 "22 ‣ III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")), $\mathcal{B}^{c} = {\{{x \in {\mathbb{R}}^{n}}:{{b{(x)}} \leq 0}\}}$, ${b{(x)}} = {{{({x - c})}^{\top}\Omega^{- 1}{({x - c})}} - 1}$ and $\mathcal{S}$ is as in ((https://arxiv.org/html/2403.11763v1#S3.E23 "23 ‣ III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")).

$\mathcal{B}^{c}$ is a control invariant set for $\overset{˙}{x} = {{Ax} + {Bu{(x)}}}$ and ${{u{(x)}} \in \mathcal{U}_{1}},{{\forall x} \in \mathcal{B}^{c}}$.

### Proof

By Theorem (https://arxiv.org/html/2403.11763v1#Thmtheorem2 "Theorem 2. ‣ III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"), we have that if $\Omega,R,Y,{\{{\sigma_{i}{( \cdot )}}\}}_{i = 1}^{o}$ satisfy ([24b](https://arxiv.org/html/2403.11763v1#S3.E24.2 "24b ‣ III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"))-([24j](https://arxiv.org/html/2403.11763v1#S3.E24.10 "24j ‣ III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")), then $\mathcal{B}^{c}$ is a control invariant set, and $\mathcal{I} \subseteq \mathcal{B}^{c} \subseteq \mathcal{S}$, and $u{(x)}$ is a safe controller. We only prove that ([26e](https://arxiv.org/html/2403.11763v1#S3.E26.5 "26e ‣ III-C Input Constraints ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) is sufficient for ${u{(x)}} \in \mathcal{U}_{1}$, for all $x \in \mathcal{B}^{c}$. In condition ([26e](https://arxiv.org/html/2403.11763v1#S3.E26.5 "26e ‣ III-C Input Constraints ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"))$,\Pi \succeq 0$ is equivalent to

By Schur complement, if $\mu > 0$, then the last inequality is equivalent to

Additionally, ${{{- {d^{\top}d}} + \zeta} - \varepsilon - \mu} > 0$, then the latter is equivalent to

The matrix remains positive semidefinite if we left- and right- multiply it by $\Omega^{- 1}$, thus we obtain (recall that $K = {Y\Omega^{- 1}}$)

for any $x$. Writing the product above explicitly, we obtain for any $x \in {\mathbb{R}}^{n}$:

Hence, for any $x$ such that ${b{(x)}} = 0$, we have ${{x_{c}^{\top}\Omega^{- 1}x_{c}} - 1} \leq 0$, then ${u{(x)}^{\top}u{(x)}} \leq {\zeta - \varepsilon} \leq \zeta$. We conclude the proof. ∎

Condition ([26e](https://arxiv.org/html/2403.11763v1#S3.E26.5 "26e ‣ III-C Input Constraints ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) is an LMI of dimension $2{({n + m + 1})}$. The dimension of the constraints is twice the equivalent condition ${\Pi_{11} - {\Pi_{12}I_{n + m + 1}\Pi_{12}^{\top}}} \succeq 0$, which is however not an LMI due to the term $\mu^{2}$. One tractable convex relaxation while maintaining a relatively lower dimension is

Here $\mu$ takes the value of $\frac{{{- {d^{\top}d}} + \zeta} - \varepsilon}{2}$, which is the maximizer of $\mu{({{{- {d^{\top}d}} + \zeta} - \varepsilon - \mu})}$.

The non-negative tolerance $\varepsilon$ is introduced for robustness.

### Proposition 2

Given a CBF $b{(x)}$, system $()$, and a control admissible set $\mathcal{U}_{1}$, for any $x$ such that ${b{(x)}} = 0$, there exists ${\delta{(x)}} > 0$, such that for any $x^{\prime} \in {\mathcal{E}{(x,{\delta{(x)}})}}$, ${u{(x^{\prime})}} = {{Y\Omega^{- 1}{({x^{\prime} - c})}} + d} \in \mathcal{U}_{1}$.

### Proof

Given that $u{(x)}$ is a continuous function, ${\|{u{(x)}}\|}_{2}^{2}$ is also a continuous function. Therefore, for any $x \in {\partial\mathcal{B}^{c}}$, there exists ${\xi{(x)}} > 0$, such that for any $y \in {\mathcal{E}{(x,{\xi{(x)}})}}$, ${{\|{u{(y)}}\|}_{2}^{2} - {\|{u{(x)}}\|}_{2}^{2}} \leq \frac{\varepsilon}{2}$. From Lemma (https://arxiv.org/html/2403.11763v1#Thmlemma3 "Lemma 3. ‣ III-C Input Constraints ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints") we have that ${{\|{u{(x)}}\|}_{2}^{2} \leq {\zeta - \varepsilon}},$ thus ${\|{u{(y)}}\|}_{2}^{2} \leq {\zeta - \frac{\varepsilon}{2}}$. Pick $0 < {\delta{(x)}} \leq \zeta$, we have that for any $x^{\prime} \in {\mathcal{E}{(x,{\delta{(x)}})}}$, ${\|{u{(x^{\prime})}}\|} \leq {\zeta - \frac{\varepsilon}{2}}$. Hence, ${u{(x^{\prime})}} \in \mathcal{U}_{1}$, and we conclude the proof. ∎

We then deal with the case that $\mathcal{U} = \mathcal{U}_{2}$. Consider the following optimization program with decision variables $\Omega,R,Y,{\sigma_{1}{(x)}},\ldots,{\sigma_{l}{(x)}},\mu_{1},\ldots,\mu_{m}$.

${\min{Tr}}{(\overline{\Omega})}$

${{{{()} - {()}},{{{- {d^{\top}d}} + \zeta} - \varepsilon}} > \mu_{i} > 0},$

\end{bmatrix} \succeq 0},{i = {1,\ldots,m}}},$

$O_{i} \in {\mathbb{R}}^{m \times m}$ is an all-zero matrix, with the $i$-th diagonal entry is one, $\varepsilon > 0$ is a small constant. Program ([III-C](https://arxiv.org/html/2403.11763v1#S3.E31 "III-C Input Constraints ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) is a convex program which amends program ([III-B](https://arxiv.org/html/2403.11763v1#S3.E24 "III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) by a new semi-definite constraint ([31e](https://arxiv.org/html/2403.11763v1#S3.E31.5 "31e ‣ III-C Input Constraints ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")).

### Lemma 4

Consider Assumption (https://arxiv.org/html/2403.11763v1#Thmassumption2 "Assumption 2. ‣ III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"), and let $\mathcal{U} = \mathcal{U}_{2}$. Assume that a solution to ([III-C](https://arxiv.org/html/2403.11763v1#S3.E31 "III-C Input Constraints ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) exists and is denoted by $\Omega,R,Y,{\{{\sigma_{i}{( \cdot )}}\}}_{i = 1}^{l},\mu$. Set ${u{(x)}} = {{Y\Omega^{- 1}{({x - c})}} + d}$, where $d \in {\mathbb{R}}^{n}$ is such that ${{Bd} + {Ac}} = 0$. We then have that

$\mathcal{I} \subseteq \mathcal{B}^{c} \subseteq \mathcal{S}$, where $\mathcal{I}$ is as in ((https://arxiv.org/html/2403.11763v1#S3.E22 "22 ‣ III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")), $\mathcal{B}^{c} = {\{{x \in {\mathbb{R}}^{n}}:{{b{(x)}} \leq 0}\}}$, ${b{(x)}} = {{{({x - c})}^{\top}\Omega^{- 1}{({x - c})}} - 1}$ and $\mathcal{S}$ is as in ((https://arxiv.org/html/2403.11763v1#S3.E23 "23 ‣ III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")).

$\mathcal{B}^{c}$ is a control invariant set for $\overset{˙}{x} = {{Ax} + {Bu{(x)}}}$ and ${u{(x)}} \in \mathcal{U}_{2}$, ${\forall x} \in \mathcal{B}^{c}$.

### Proof

Similarly to the proof of Lemma (https://arxiv.org/html/2403.11763v1#Thmlemma3 "Lemma 3. ‣ III-C Input Constraints ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"), we prove that ([31e](https://arxiv.org/html/2403.11763v1#S3.E31.5 "31e ‣ III-C Input Constraints ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) is sufficient for ${{u{(x)}} \in \mathcal{U}_{2}},{{\forall x} \in \mathcal{B}^{c}}$. ([31e](https://arxiv.org/html/2403.11763v1#S3.E31.5 "31e ‣ III-C Input Constraints ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) is equivalent to

Then we have ${{u_{i}{(x)}^{\top}u_{i}{(x)}} \leq {\zeta - \varepsilon} \leq \zeta},{i = {1,\ldots,m}}$, for any $x$ such that ${b{(x)}} = 0$. Therefore, ${\|{u{(x)}}\|}_{\infty} \leq \sqrt{\zeta}$. We conclude the proof. ∎

We then deal with the case that $\mathcal{U} = \mathcal{U}_{3} = {\{{u \in {\mathbb{R}}^{m}}:{{Hu} \leq h}\}}$. Consider the following optimization program

\end{bmatrix} \succeq 0},{i = {1,\ldots,k}}},$

$\varepsilon > 0$ is a small constant. Program ([III-C](https://arxiv.org/html/2403.11763v1#S3.E32 "III-C Input Constraints ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) is a convex program which amends program ([III-B](https://arxiv.org/html/2403.11763v1#S3.E24 "III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) by a new semi-definite constraint ([32e](https://arxiv.org/html/2403.11763v1#S3.E32.5 "32e ‣ III-C Input Constraints ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")).

### Lemma 5

Consider Assumption (https://arxiv.org/html/2403.11763v1#Thmassumption2 "Assumption 2. ‣ III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"), and let $\mathcal{U} = \mathcal{U}_{3}$. Assume that a solution to ([III-C](https://arxiv.org/html/2403.11763v1#S3.E32 "III-C Input Constraints ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) exists and is denoted by $\Omega,R,Y,{\{{\sigma_{i}{( \cdot )}}\}}_{i = 1}^{l},\mu$. Set ${u{(x)}} = {{Y\Omega^{- 1}{({x - c})}} + d}$, where $d \in {\mathbb{R}}^{n}$ is such that ${{Bd} + {Ac}} = 0$. We then have that

$\mathcal{I} \subseteq \mathcal{B}^{c} \subseteq \mathcal{S}$, where $\mathcal{I}$ is as in ((https://arxiv.org/html/2403.11763v1#S3.E22 "22 ‣ III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")), $\mathcal{B}^{c} = {\{{x \in {\mathbb{R}}^{n}}:{{b{(x)}} \leq 0}\}}$, ${b{(x)}} = {{{({x - c})}^{\top}\Omega^{- 1}{({x - c})}} - 1}$ and $\mathcal{S}$ is as in ((https://arxiv.org/html/2403.11763v1#S3.E23 "23 ‣ III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")).

$\mathcal{B}^{c}$ is a control invariant set for $\overset{˙}{x} = {{Ax} + {Bu{(x)}}}$ and ${u{(x)}} \in \mathcal{U}_{3}$, ${\forall x} \in \mathcal{B}^{c}$.

### Proof

Similarly to the proof of Lemma (https://arxiv.org/html/2403.11763v1#Thmlemma3 "Lemma 3. ‣ III-C Input Constraints ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"), and (https://arxiv.org/html/2403.11763v1#Thmlemma4 "Lemma 4. ‣ III-C Input Constraints ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"), we prove that ([32e](https://arxiv.org/html/2403.11763v1#S3.E32.5 "32e ‣ III-C Input Constraints ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) is sufficient for ${{u{(x)}} \in \mathcal{U}_{3}},{{\forall x} \in \mathcal{B}}$. ([32e](https://arxiv.org/html/2403.11763v1#S3.E32.5 "32e ‣ III-C Input Constraints ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")) is equivalent to

The matrix remains positive semidefinite if we left- and right- multiply it by $\Omega^{- 1}$, thus we obtain

Then we have for every $i = {1,\ldots,k}$, ${H_{i}u_{i}{(x)}} \leq {h_{i} - \varepsilon} < h_{i}$ for any $x$ such that ${b{(x)}} = {{{({x - c})}^{\top}\Omega^{- 1}{({x - c})}} - 1} \leq 0$, ${Hu{(x)}} \leq h$. We conclude the proof. ∎

Similar to the design in Lemma (https://arxiv.org/html/2403.11763v1#Thmlemma3 "Lemma 3. ‣ III-C Input Constraints ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"), $\varepsilon$ is also introduced in Lemma (https://arxiv.org/html/2403.11763v1#Thmlemma4 "Lemma 4. ‣ III-C Input Constraints ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints") and (https://arxiv.org/html/2403.11763v1#Thmlemma5 "Lemma 5. ‣ III-C Input Constraints ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"). As a consequence, a robustness property is imposed on the synthesized CBF as in Proposition (https://arxiv.org/html/2403.11763v1#Thmproposition2 "Proposition 2. ‣ III-C Input Constraints ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints").

## Simulation Results

In this section we demonstrate the proposed programs on a linear system with a high relative degree. All the examples are coded using MATLAB R2022a, SOSTOOLS-4.03 \[(https://arxiv.org/html/2403.11763v1#bib.bib49)\], and SeDuMi-1.3.7 \[(https://arxiv.org/html/2403.11763v1#bib.bib50)\].

Figure 7: The collision space 𝒮c is filled by dark blue. Velocity is fixed to be vx = 1, vy = 1. The control invariant set ℬ:= {x: b(x) ≥ 0} is designed by solving the global convex program (III-A), and is filled in yellow.

In this example, we show how to design CBFs for a linear system with a relative degree. Both the global design and the local design will be conducted. Consider an omni-directional vehicle and a collision avoidance problem. The dynamics of the vehicle are

where $\lbrack x,y\rbrack$ represents the position of the vehicle on the 2-D plane, and $\lbrack v_{x},v_{y}\rbrack$ represents the corresponding velocity. The vehicle is controlled by tuning the acceleration denoted by $u = {\lbrack a_{x},a_{y}\rbrack}$ along the two directions. The position corresponds to $\overline{x}$, while the velocity corresponds to $\underset{¯}{x}$ in ([III-A](https://arxiv.org/html/2403.11763v1#S3.E10 "III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")). A polytopic obstacle (with five facets) is placed with $\overline{c} = {\lbrack 0,0\rbrack}^{\top}$ be an inside point. Under this configuration, the safe set is a semi-algebraic set, which can be formulated as

where $a_{i} \in {\mathbb{R}}^{2}$, ${i = {1,\ldots,5}},$ are known vectors. The collision space $\mathcal{S}^{c}$ is then a bounded polytope contains $c = {\lbrack 0,0,0,0\rbrack}^{\top}$. Given that $\mathcal{S}$ is only defined over $\lbrack x,y\rbrack$, we consider to design a CBF

by solving ([III-A](https://arxiv.org/html/2403.11763v1#S3.E10 "III-A Global Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")). We obtain a control barrier function as ${b{(x)}} = {{{{2.4104x^{2}} - {0.67042xy}} + {1.3229y^{2}}} - {859.4863v_{x}^{2}} - {859.4863v_{y}^{2}} - 1}$ and a control gain as $K = \begin{bmatrix}
\end{bmatrix}$. We visualize the control invariant set $\mathcal{B}$ and the obstacle $\mathcal{S}^{c}$ on ${\mathbb{R}}^{2}$ by fixing $v_{x} = 1$, $v_{y} = 1$. The result is shown in Figure (https://arxiv.org/html/2403.11763v1#S4.F7 "Figure 7 ‣ IV Simulation Results ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints").

(a) Blue region is the obstacle 𝒮c, yellow region is ℬc and black region is the initial set ℐ.

(b) Level sets of ∥u(x)∥22. ∥u(x)∥22 ≤ 4 for any x ∈ ℬc, thus showing that the input constraint is not violated.

Figure 8: Convex invariant set ℬc and state feedback controller u(x) designed by solving the local program (III-B). The sets are projected to ℝ2 by setting vx = −0.5, vy = −0.5. The yellow region is ℬc.

Then we consider a local design. The car is starting from the initial set

The acceleration limits are encoded by ${{a_{x}^{2} + a_{y}^{2}} \leq 4}.$ By solving the local design program ([III-B](https://arxiv.org/html/2403.11763v1#S3.E24 "III-B Local Design ‣ III Convex Design for Linear Systems ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints")), we obtain ${b{(x)}} = {{{{{{{{0.66903v_{x}^{2}} - {0.44567v_{x}v_{y}}} + {0.28291v_{x}x}} - {0.80024v_{x}y}} + {1.1024v_{y}^{2}} + {0.23651v_{y}x} + {1.4055v_{y}y} + {1.1198x^{2}}} - {0.58818xy}} + {4.7544y^{2}}} - 1}$ and control gain ${K = \begin{bmatrix}
\end{bmatrix}}.$ The designed control invariant set is $\mathcal{B}^{c}:=\left\{ {\begin{bmatrix}
\end{bmatrix} \in {\mathbb{R}}^{4}}:{{b{(x)}} \leq 0} \right\}$, and level sets of ${\|{u{(x)}}\|}_{2}^{2}$ are visualized in Figure (https://arxiv.org/html/2403.11763v1#S4.F8 "Figure 8 ‣ IV Simulation Results ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints").

## Conclusion

In this paper we proposed a method to synthesize a control barrier function and a state feedback controller by solving a single convex program. Our approach considers quadratic control barrier functions and affine state feedback controllers. Different types of control input limits can be handled as additional convex constraints to the synthesis program. We demonstrate the efficacy of our approach on an omni-directional car collision avoidance problem. Future work concentrates towards generalizing the obtained results to allow using higher-relative degree polynomials for the CBF and the controller. We will also consider how to impose input constraint into the global CBF design program using rational polynomial controllers.
