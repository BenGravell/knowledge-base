Complexity of Ten Decision Problems in Continuous Time Dynamical Systems

Topics include Dynamical systems, Computational complexity, NP-hardness, Lyapunov stability, Polynomial vector fields, Control theory, Trigonometric dynamics.

Catalogs ten natural decision problems for continuous-time dynamical systems and proves that even low-degree polynomial or trigonometric systems make them NP-hard or pseudo-polynomially intractable unless P=NP. The paper is valuable as a warning label for control workflows: tasks such as stability, attractivity, boundedness, invariance, collision avoidance, and stabilizing-controller existence can be computationally hard before any numerical approximation issues appear.

We show that for continuous time dynamical systems described by polynomial differential equations of modest degree (typically equal to three), the following decision problems which arise in numerous areas of systems and control theory cannot have a polynomial time (or even pseudo-polynomial time) algorithm unless P=NP: local attractivity of an equilibrium point, stability of an equilibrium point in the sense of Lyapunov, boundedness of trajectories, convergence of all trajectories in a ball to a given equilibrium point, existence of a quadratic Lyapunov function, invariance of a ball, invariance of a quartic semialgebraic set under linear dynamics, local collision avoidance, and existence of a stabilizing control law. We also extend our earlier NP-hardness proof of testing local asymptotic stability for polynomial vector fields to the case of trigonometric differential equations of degree four.

## Introduction

Polynomial and trigonometric differential equations appear ubiquitously in a variety of application domains including robotics, economics, mathematical biology, and chemical engineering, among others. The equations of motion for most robotic systems for example can be described by the familiar *manipulator equations* which give rise to systems of differential equations that are a mixture of polynomial and trigonometric terms in the state variables....

While mature computational tools exist for the numerical solution of such differential equations, in most of the application domains described above, one is *not* typically interested in *particular* solutions of the system. Rather, *qualitative properties* of the differential equations are of central importance. For example, one may be interested in the safety of a robot performing a certain dynamic task, or in determining if the population of certain species diminishes below a critical threshold....

Under the assumption P$\neq$NP, we have shown the impossibility of polynomial time (or even pseudo-polynomial time) algorithms for ten decision problems that ubiquitously arise in control theory and the study of continuous time dynamical systems. Although our hardness results are valid even for very restricted classes of systems (e.g. gradient systems), it is of course still possible that these decision problems admit polynomial time algorithms for other special (and possibly important) *subclasses* of polynomial or trigonometric vector fields.

Aside from extending the results of Theorem IV.1 to other classes of vector fields (such as trigonometric ones), the obvious class of questions that our work leaves open is to investigate the *decidability* of the decision problems studied in Theorem IV.1, or their NP-hardness for polynomial vector fields of degree one or two. Although for linear systems some of these questions become easy, we expect that our hardness results can be strengthened to the case when the degree is $2$....

Given a quartic trigonometric form $t_{h}{(z)}$, we construct the following continuous time dynamical system:

### Lemma III.2

\(a\) The proofs of parts (a) and (b) of the theorem are based on a reduction from the polynomial nonnegativity problem: given a (homogeneous) polynomial $p:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$, decide whether ${{p{(x)}} \geq...
