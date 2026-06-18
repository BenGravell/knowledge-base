<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Convex Co-Design of Control Barrier Functions and State Feedback Controllers for Linear Systems with Input Constraints

Topics include Control barrier functions, Safety, Sum-of-squares programming, Semidefinite programming, Input constraints, Linear systems.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Formulates joint CBF and linear feedback-controller synthesis for linear systems as a semidefinite program, including input constraints and mixed-relative-degree safe sets. The useful idea is treating safe-set certificate design and controller design as one convex co-design problem.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the problem of co-designing control barrier functions (CBF) and linear state feedback controllers for continuous-time linear systems. We achieve this by means of a single semi-definite optimization program. Our formulation can handle mixed-relative degree problems without requiring an explicit safe controller. Different L-norm based input limitations can be introduced as convex constraints in the proposed program. We demonstrate our results on an omni-directional car numerical example.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Safety is essential for feedback control systems. As a system is steered from an initial set to a target set, safety requires that the trajectory of the system avoids entering an unexpected region, or to remain inside a safe set. On the state space, safety is always formulated by means of constraints imposed on states. Based on these descriptions, two questions are raised: given a dynamical system $\overset{˙}{x} = {f{(x,u)}}$, a set of initial sets $\mathcal{I}$, and a set of safe states $\mathcal{S}$, (i) verify whether there exists a control input $u{( \cdot )}$, so that the trajectories starting from $\mathcal{I}$ stay inside $\mathcal{S}$; (ii) design such a control law $u{( \cdot )}$ that guarantees safety. The Control Barrier Functions (CBF) approach answers these two questions by using a continuously differentiable function that satisfies certain properties.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A CBF aims to separate the safe and unsafe regions by its zero super- and sub-level sets; the initial set also belongs to the level set. In addition, there exists a control law, such that the vector field points towards the safe side on its zero sub-level set. This property is also known as *invariance*, characterized by Nagumo's theorem. It is therefore guaranteed that if the system starts from a point inside the zero super-level set, the system can always stay inside. Given a CBF, the controller that guarantees safety can be designed according to the direction requirement of vector field. However, synthesizing a CBF is not a trivial task even for linear systems. In general, even verifying a CBF is an NP-hard problem \[, Proposition 2\].

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Designing a CBF is even more challenging when the relative degree between the function defines safe set and the system dynamics is high or mixed. For relative degree we mean the number of times we need to differentiate a function whose level set encodes the safe set along the system dynamics until the control explicitly shows. High or mixed relative degree is commonly seen in robotics collision avoidance problems, where the safe set is usually defined over positions for the obstacles, but the control signals are imposed on accelerations.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Case 1 (Pathological vector field of CBF-QP)", "weight": 1.0} -->

Following, the analytical solution is given by

<!-- chunk {"id": "body-0008", "role": "body", "section": "Case 1 (Pathological vector field of CBF-QP)", "weight": 1.0} -->

(a) Values of ∥us(x)∥22 for −1 ≤ x1 ≤ 1, −1 ≤ x2 ≤ 1. The value of ∥us(x)∥22 is limited to 100 for visualization. The controller is only locally smooth, and the Lipschitz constant is large in a local region as the value varies a lot with little state changes. Different selection of a class-𝒦 function does not change the result for x ∈ ∂ℬ, which is the black curve in the figure. Clearly our designed feedback controller ub(x) = 1.4164x1 + 0.59702x2 is globally smooth as it is linear.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Case 1 (Pathological vector field of CBF-QP)", "weight": 1.0} -->

(b) Comparison of the two control barrier functions in Case 1. The blue round region is the unsafe set 𝒮c. The yellow open region is the control invariant set ℬ:= {x|b(x) ≥ 0}, and ∂ℬ:= {x|b(x) = 0} is the black curve. Blue arrows represents the vector field Ax + Bub(x), which points inward ℬ on ∂ℬ.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Case 1 (Pathological vector field of CBF-QP)", "weight": 1.0} -->

When $g{(x)}$ tends to zero, and ${f{(x)}} < 0$, $u_{s}{(x)}$ tends to infinity. As a consequence, the system cannot be safe at some points, especially points on $\partial\mathcal{S}$ with limited control authority. We also show in Figure 0(a) ‣ Figure 1 ‣ Case 1 (Pathological vector field of CBF-QP). ‣ I-A Motivating Cases ‣ I Introduction ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints") that the Lipschitz constant of $u_{s}{(x)}$ is very large.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Case 1 (Pathological vector field of CBF-QP)", "weight": 1.0} -->

Later, we will show that, by solving the proposed convex program (III-A) with ${\|{u_{b}{(x)}}\|}_{2}^{2} \leq 8$ for $x$ such that ${b{(x)}} = 0$, we obtain a new control barrier function ${b{(x)}} = {{{{0.88391x_{1}^{2}} - {0.50767x_{1}x_{2}}} + {0.25205x_{2}^{2}}} - 1}$, and a feedback controller ${u_{b}{(x)}} = {{1.4164x_{1}} + {0.59702x_{2}}}$. Comparison of the two control barrier functions is shown in Figure 0(b) ‣ Figure 1 ‣ Case 1 (Pathological vector field of CBF-QP).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Case 1 (Pathological vector field of CBF-QP)", "weight": 1.0} -->

‣ I-A Motivating Cases ‣ I Introduction ‣ Convex Co-Design of Control Barrier Functions and Safe Feedback Controllers Under Input Constraints"). It can be seen that the value of ${\|{u_{s}{(x)}}\|}_{2}^{2}$ is comparably large for small $x_{2}$. Meanwhile, our synthesized controller is constrained by ${\|{u_{b}{(x)}}\|}_{2}^{2} \leq 8$ for $x \in {\partial\mathcal{B}}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Case 2 (Mixed relative degree)", "weight": 1.0} -->

\{ x \middle| {{s{(x)}} \leq 0}\} \right.$, where ${s{(x)}} = {{x_{1}^{2} + x_{2}^{2}} - 1}$. Let the relative degree be the number of times we need to differentiate $s{(x)}$ along the dynamics until the control input $u$ appears in the resulting expression. For this case, the relative degree between $s{(x)}$ and the system is mixed, as the input $u_{1}$ appears in the first derivative of $s{(x)}$, whereas $u_{2}$ appears in the second derivative. $s{(x)}$ can not be directly used as a CBF using high-relative degree (exponential) CBF techniques.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Case 2 (Mixed relative degree)", "weight": 1.0} -->

By solving the convex program (III-A) that we will propose in the sequel, we obtain a control barrier function ${b{(x)}} = {{x_{1}^{2} + x_{2}^{2}} - {0.0129x_{3}^{2}} - 1}$, and a feedback controller ${u_{1}{(x)}} = {{- {2x_{1}}} + {38.9x_{2}}}$, ${u_{2}{(x)}} = {{76.8x_{1}} - {0.5x_{3}}}$, which guarantees safety for the system. Clearly, the relative degree between $b{(x)}$ and the system dynamics is one. We highlight here that the backstepping CBF method would require a series of explicit pre-synthesized safe controllers which are, however, not needed for our method, which only requires the solution of a convex program.

<!-- chunk {"id": "body-0015", "role": "body", "section": "I-B Related Work", "weight": 1.0} -->

Dating back to the 1980's, there has been tremendous work on control invariance, especially for linear systems. For continuous-time linear systems, a half plane divided by an eigenvector is invariant. For discrete-time systems, an invariant set can be constructed iteratively by state propagation. These methods focus on invariance but not safety. Building upon invariance, different methodologies have been proposed to synthesize control barrier functions.

<!-- chunk {"id": "body-0016", "role": "body", "section": "I-B Related Work", "weight": 1.0} -->

The first type of methods is reachability-based methods. Given a target set and a safe set, solving an optimal control problem returns a set of states starting from which the dynamical system can stay in the safe set and reach the target set. Such a set is usually the zero super-level set of a value function. Naturally, if only safety is considered over a finite horizon in the optimal control problem, the value function is a finite-time CBF. More recently, the relationship between the safe value function and a CBF has been established. Solving this problem directly involves computing the solution of a Hamilton-Jacobi partial differential equation, which is computationally difficult for generic nonlinear systems.

<!-- chunk {"id": "body-0017", "role": "body", "section": "I-B Related Work", "weight": 1.0} -->

The second type of methods proposed recently involves learning-based approaches. Unlike the optimal control formulation which considers the entire state space, learning-based methods rely on a finite data-set. Supervised learning-based methods have been proposed, where a demonstrator is required to collect data. A neural network with a loss function encoding the conditions that a CBF needs to satisfy is used. Learning-based methods show high flexibility for nonlinear and high order systems, and are amenable to applications to high degree-of-freedom robotics. However, rigorous guarantees for safety and network robustness is inherently hard for these black-box methods. At the same time, the data required by the CBF network and the controller network in the training process can be difficult to obtain, as pointed out.

<!-- chunk {"id": "body-0018", "role": "body", "section": "I-B Related Work", "weight": 1.0} -->

The third type of methods involves optimization-based approaches, especially using sum-of-squares programming. Barrier functions are designed for systems with input disturbances using SOS programming. When controllers are taken into consideration, alternating between synthesizing a controller and CBFs to solve sequential SOS programs is proposed. Convex quadratic CBFs, constructed from a Lyapunov function for a polytopic safe set are considered. Newton's method can be leveraged to guarantee local convergence to a feasible CBF. As a dual to SOS programming, moment problems based on occupation measures have been proposed. These SOS-based methods transform the algebraic conditions for CBF to polynomial positivity conditions, and cast these conditions using SOS hierarchies. Compared with numerical methods to solve the Hamilton-Jacobi partial differential equations, SOS programming based methods are computationally more efficient provided that the polynomial basis is fixed. Compared with learning-based methods, SOS-based approaches allow for rigorous safety guarantee providing a feasible solution exactly. Our proposed method belongs to the SOS-based methods, whilst providing computational efficiency improvements and feasibility guarantees.

<!-- chunk {"id": "body-0019", "role": "body", "section": "I-C Contribution", "weight": 1.0} -->

In this paper, we focus on linear systems. Our main contribution is to propose an efficient method to design a control barrier function and an associated affine state feedback controller using sum-of-squares programming. The control barrier function and feedback controller are synthesized in one unified sum-of-squares program, thus overcoming the need for iterative algorithms. Moreover, our formulation is applicable to high and mixed relative degree cases without using backstepping.

<!-- chunk {"id": "body-0020", "role": "body", "section": "I-C Contribution", "weight": 1.0} -->

We also extend the existing literature when considering limits in the system inputs. $\mathcal{L}$-1 norm constrained limitation set is considered. Specifically, introduce bilinear constraints in the sum-of-squares programming, proposes a quantifier exchange to drop the dependency on the control input, and proposes re-parameterization for linear systems. In our work, $\mathcal{L}$-1, $\mathcal{L}$-2, and $\mathcal{L} - \infty$ norm constrained limitations are all addressed by means of convex constraints. These input constraints can be appended to the CBF and controller synthesis program.

<!-- chunk {"id": "body-0021", "role": "body", "section": "I-D Organization", "weight": 1.0} -->

Section II provides some background. The convex synthesis program and extensions for linear systems are presented in Section III. Simulation results are shown in Section IV. Section V concludes the paper.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-B Safety and CBF", "weight": 1.0} -->

Consider a continuous-time nonlinear control-affine system

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-B Safety and CBF", "weight": 1.0} -->

Our goal is to design a state feedback controller $u{(x)}$ such that the solution $x{(t,x_{0})}$ of the closed-loop system $\overset{˙}{x} = {{f{(x)}} + {g{(x)}u{(x)}}}$ that starts from ${x{}} = x_{0}$, with $x_{0}$ belonging to a set of *initial conditions* $\mathcal{I}$, stays within a *safe set* $\mathcal{S}$ for every $t$ that belongs to the domain of definition of the solution. If such a controller $u{( \cdot )}$ exists, we say the system is *safe*.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Convex Design for Linear Systems", "weight": 1.0} -->

In this section, we propose convex synthesis programs to construct a CBF and an affine safe feedback controller. In Section III-A, we first consider a *global* design for $\mathcal{B} = {\{{x \in {\mathbb{R}}^{n}}:{{b{(x)}} \geq 0}\}}$ to be control invariant. For this case, we consider the unsafe set $\mathcal{S}^{c}$ to be bounded on a subspace of ${\mathbb{R}}^{n}$. This is commonly for robot collision avoidance problems, where the position space is a subspace of the robot state space. The control invariant set $\mathcal{B}$ is constructed *globally* as its projection to the subspace of $\mathcal{S}^{c}$ is unbounded.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Convex Design for Linear Systems", "weight": 1.0} -->

For the second case in Section III-B, we construct a control invariant set $\mathcal{B}^{c} = {\{{x \in {\mathbb{R}}^{n}}:{{b{(x)}} \leq 0}\}}$ around a bounded initial set. This control invariant set is called *local* as we will show it is bounded on ${\mathbb{R}}^{n}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Convex Design for Linear Systems", "weight": 1.0} -->

where ${x{(t)}} \in {\mathbb{R}}^{n}$, ${u{(t)}} \in \mathcal{U} \subseteq {\mathbb{R}}^{m}$ are the state and control input, and $A \in {\mathbb{R}}^{n \times n}$, $B \in {\mathbb{R}}^{n \times m}$. We assume that the system is stabilizable. Throughout the paper, the CBF $b{(x)}$ and feedback controller $u{(x)}$ are parameterized as follows.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Notice that this a convex optimization program, where the objective function is linear, and is subject to semi-define constraints The cost function is to minimize the volume of the set $\{{\overline{x} \in {\mathbb{R}}^{\overline{n}}}:{{{- {{({\overline{x} - \overline{c}})}^{\top}{\overline{\Omega}}^{- 1}{({\overline{x} - \overline{c}})}}} + 1} \geq 0}\}$, thus indirectly maximizing the volume of the projection set of $\mathcal{B}$ on the space ${\mathbb{R}}^{\overline{n}}$. An alternative formulation is ${\max\log}{\det{\overline{\Omega}}^{- 1}}$ \[, Section 2.2.4\]. However, this is not supported by SeDuMi, which is the solver we are using to solve the semi-definite program.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

In the following theorem, we give the main result of the paper, a convex program to synthesize a CBF $b{(x)}$ and a feedback controller $u{(x)}$ under Assumption.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Example 1", "weight": 1.0} -->

Consider a car moving along a line

<!-- chunk {"id": "body-0030", "role": "body", "section": "Example 1", "weight": 1.0} -->

where $\overline{x}$ represents the position and $\underset{¯}{x} \in {\mathbb{R}}$ represents the velocity. Let

<!-- chunk {"id": "body-0031", "role": "body", "section": "Example 1", "weight": 1.0} -->

We follow the construction in Theorem. The vector $c \in {\mathbb{R}}^{2}$ that satisfies rank($\lbrack{BAc}\rbrack$) = rank($B$) is any vector such that $\underset{¯}{c} = 0$. We also fix $\overline{c} = 0$. Consequently $d = 0$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Example 1", "weight": 1.0} -->

Looking at the spectrum of the matrix in (20f), we conclude that (20f) is equivalent to $Y_{2} > 0$ and ${\underset{¯}{\Omega} + Y_{1}} = 0$. Condition (20i) is equivalently expressed as ${R - {\overline{\Omega}}^{- 1}} \geq 0$. As for $\sigma{(\overline{x})}$, we set it to be an SOS polynomial of degree $0$, hence, ${\sigma{(\overline{x})}} = \overline{\sigma} \geq 0$. Writing the polynomial in (20j) as

<!-- chunk {"id": "body-0033", "role": "body", "section": "Example 1", "weight": 1.0} -->

and bearing in mind Lemma, one realizes that condition (20j) is equivalent to ${\overline{\sigma} - R} \geq 0$ and ${1 - \overline{\sigma} - \epsilon} \geq 0$. In summary, we have the following conditions

<!-- chunk {"id": "body-0034", "role": "body", "section": "Example 1", "weight": 1.0} -->

For any feasible choice of the design parameters, the obtained closed-loop matrix has at least one unstable eigenvalue. To have an understanding of the state response, we compute the spectral representation $e^{{({A + {BK}})}t}$ for these values of the design parameters: $\underset{¯}{\Omega} = {- 4}$, $\overline{\Omega} = 2$, $Y_{2} = 4$. Then the spectral representation is given by

<!-- chunk {"id": "body-0035", "role": "body", "section": "Example 1", "weight": 1.0} -->

Hence, if the system starts from the initial condition $x = \begin{bmatrix}
\end{bmatrix}^{\top} = {\lbrack{20}\rbrack}^{\top}$, which is on the boundary of $\mathcal{B}$, it will evolve as

<!-- chunk {"id": "body-0036", "role": "body", "section": "Example 1", "weight": 1.0} -->

As a result, both position and velocity diverge exponentially but are certified to stay within $\mathcal{B}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Example 1", "weight": 1.0} -->

We will show below that the set $\overline{\mathcal{B}}$ can not be control invariant using linear feedback $u{(x)}$. Denote the projection matrix

<!-- chunk {"id": "body-0038", "role": "body", "section": "Example 1", "weight": 1.0} -->

and express the invariance condition as

<!-- chunk {"id": "body-0039", "role": "body", "section": "Example 1", "weight": 1.0} -->

The invariance condition can be expressed as

<!-- chunk {"id": "body-0040", "role": "body", "section": "Example 1", "weight": 1.0} -->

which leads to a convex condition by multiplying $\begin{bmatrix}
\end{bmatrix}$ on both sides of the matrices in the inequality. However, the possibility of fulfilling such constraint appears to be related to the possibility of shaping the spectra of ${\overline{A}}_{1} + {\overline{B}\overline{K}}$ and ${\overline{A}}_{2} + {\overline{B}\underset{¯}{K}}$, hence, to the controllability of the pairs $({\overline{A}}_{1},\overline{B})$, $({\overline{A}}_{2},\overline{B})$. Going back to Example, we have ${({\overline{A}}_{1},\overline{B})} = {}$, and ${({\overline{A}}_{2},\overline{B})} = {}$, which shows lack of controllability of both pairs.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Example 1", "weight": 1.0} -->

As a result, the invariance condition above is

<!-- chunk {"id": "body-0042", "role": "body", "section": "Example 1", "weight": 1.0} -->

which shows that enforcing invariance for the set $\overline{\mathcal{B}}$ via feedback is impossible due to the lack of controllability (the matrix has a positive and a negative eigenvalue).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Example 1", "weight": 1.0} -->

The exact control invariant set for Example numerically computed by the level-set method toolbox is shown in Figure. To compute the exact control invariant set, the control feedback $u$ is set in the linear form $u = {Y\Omega^{- 1}x}$, where $Y$ and $\Omega$ have the same numerical values as those chosen in Example ($\underset{¯}{\Omega} = {- 4}$, $\overline{\Omega} = 2$, $Y_{1} = 4$, $Y_{2} = 4$). In comparison, our computed control invariant set $\mathcal{B}$ determined analytically and depicted in Figure is conservative when $\overline{\Omega} \neq 1$. This can be alleviated by minimizing ${Tr}{(\overline{\Omega})}$ as in the program (III-A). Conservative behaviour is also encountered in the first and third quadrants, where the boundary of the exact invariant set coincides with the safe set $\mathcal{S}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Example 1", "weight": 1.0} -->

This is natural as the planar car is moving away from the unsafe set $\mathcal{S}^{c}$, which has been filled in green, in these regions. Our method, however, computes a control invariant set $\mathcal{B}$, that is symmetric with respect to the $\overline{x}$-axis. In practice, one can reduce this conservativeness by taking the union of our computed control invariant set $\mathcal{B}$ with other invariant sets, such as $\mathcal{B}^{\prime} = {\{{x \in {\mathbb{R}}^{2}}:{{b^{\prime}{(x)}}:={\underset{¯}{x}\overline{x}} \geq 0}\}}$. The new control invariant set is shown in Figure. The control barrier function corresponds to this union set can be defined by

<!-- chunk {"id": "body-0045", "role": "body", "section": "Example 1", "weight": 1.0} -->

Such a kind of CBF has been investigated.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Example 1", "weight": 1.0} -->

According to Nagumo's Theorem, a compact set is invariant for a vector field if and only if the vector field is within the tangent cone for all points on the boundary of the set. For a compact and closed set $\mathcal{B}$, this is equivalent to having ${\overset{˙}{b}{(x)}} \geq 0$, for any $x$ such that ${b{(x)}} = 0$. However in our proposed convex conditions (III-A), we enforce a "strengthened" condition that ${\overset{˙}{b}{(x)}} \geq 0$, for any $x \in {\mathbb{R}}^{n}$. Nevertheless, we show in the following proposition that this does not introduce any conservativeness in the case $\overline{n} = n$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-B Local Design", "weight": 1.0} -->

In the previous section, we construct a control invariant set $\mathcal{B}:={\{{x \in {\mathbb{R}}^{n}}:{{b{(x)}} \geq 0}\}}$ globally, it is unbounded on ${\mathbb{R}}^{\overline{n}}$, and naturally unbounded on ${\mathbb{R}}^{n}$. As shown in Example, the closed-loop trajectory diverges using the co-designed linear feedback controller $u{(x)}$. This is undesired in many applications where boundedness of trajectories is a prerequisite. In this section, we consider constructing a bounded control invariant set around a bounded set of initial conditions $\mathcal{I}$, and inside a intersection of half planes, i.e. the safe set $\mathcal{S}$. The new control invariant set will also be parameterized by a quadratic function.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

$\mathcal{I}$ is a semi-algebraic set, and $\mathcal{I}$ is bounded on the space ${\mathbb{R}}^{n}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Let $c \in {\mathbb{R}}^{n}$ be a constant vector such that ${{rank}{({\lbrack B,{Ac}\rbrack})}} = {{rank}{(B)}}$ as before, and consider the following optimization program.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

where $x_{c} = {x - c}$. Similarly to program (III-A) for global design, program (III-B) is a convex optimization program, since the cost function is linear, and is subject to semi-definite and linear constraints. In the following theorem, we show how to synthesize a CBF $b{(x)}$ and a feedback safe controller $u{(x)}$ by this convex program under Assumption.

<!-- chunk {"id": "body-0051", "role": "body", "section": "III-C Input Constraints", "weight": 1.0} -->

and $\varepsilon > 0$ is a small constant. Program (III-C) is a convex program which amends program (III-B) by a new semi-definite constraint (26e).

<!-- chunk {"id": "body-0052", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

In this section we demonstrate the proposed programs on a linear system with a high relative degree. All the examples are coded using MATLAB R2022a, SOSTOOLS-4.03, and SeDuMi-1.3.7.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

In this example, we show how to design CBFs for a linear system with a relative degree. Both the global design and the local design will be conducted. Consider an omni-directional vehicle and a collision avoidance problem. The dynamics of the vehicle are

<!-- chunk {"id": "body-0054", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

where $\lbrack x,y\rbrack$ represents the position of the vehicle on the 2-D plane, and $\lbrack v_{x},v_{y}\rbrack$ represents the corresponding velocity. The vehicle is controlled by tuning the acceleration denoted by $u = {\lbrack a_{x},a_{y}\rbrack}$ along the two directions. The position corresponds to $\overline{x}$, while the velocity corresponds to $\underset{¯}{x}$ in (III-A). A polytopic obstacle (with five facets) is placed with $\overline{c} = {\lbrack 0,0\rbrack}^{\top}$ be an inside point. Under this configuration, the safe set is a semi-algebraic set, which can be formulated as

<!-- chunk {"id": "body-0055", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

where $a_{i} \in {\mathbb{R}}^{2}$, ${i = {1,\ldots,5}},$ are known vectors. The collision space $\mathcal{S}^{c}$ is then a bounded polytope contains $c = {\lbrack 0,0,0,0\rbrack}^{\top}$. Given that $\mathcal{S}$ is only defined over $\lbrack x,y\rbrack$, we consider to design a CBF

<!-- chunk {"id": "body-0056", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

(a) Blue region is the obstacle 𝒮c, yellow region is ℬc and black region is the initial set ℐ.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

(b) Level sets of ∥u(x)∥22. ∥u(x)∥22 ≤ 4 for any x ∈ ℬc, thus showing that the input constraint is not violated.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Simulation Results", "weight": 1.0} -->

Then we consider a local design. The car is starting from the initial set

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper we proposed a method to synthesize a control barrier function and a state feedback controller by solving a single convex program. Our approach considers quadratic control barrier functions and affine state feedback controllers. Different types of control input limits can be handled as additional convex constraints to the synthesis program. We demonstrate the efficacy of our approach on an omni-directional car collision avoidance problem. Future work concentrates towards generalizing the obtained results to allow using higher-relative degree polynomials for the CBF and the controller. We will also consider how to impose input constraint into the global CBF design program using rational polynomial controllers.
