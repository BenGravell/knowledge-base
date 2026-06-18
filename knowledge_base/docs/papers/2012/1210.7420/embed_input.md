<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Complexity of Ten Decision Problems in Continuous Time Dynamical Systems

Topics include Dynamical systems, Computational complexity, NP-hardness, Lyapunov stability, Polynomial vector fields, Control theory, Trigonometric dynamics.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Catalogs ten natural decision problems for continuous-time dynamical systems and proves that even low-degree polynomial or trigonometric systems make them NP-hard or pseudo-polynomially intractable unless P=NP. The paper is valuable as a warning label for control workflows: tasks such as stability, attractivity, boundedness, invariance, collision avoidance, and stabilizing-controller existence can be computationally hard before any numerical approximation issues appear.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We show that for continuous time dynamical systems described by polynomial differential equations of modest degree (typically equal to three), the following decision problems which arise in numerous areas of systems and control theory cannot have a polynomial time (or even pseudo-polynomial time) algorithm unless P=NP: local attractivity of an equilibrium point, stability of an equilibrium point in the sense of Lyapunov, boundedness of trajectories, convergence of all trajectories in a ball to a given equilibrium point, existence of a quadratic Lyapunov function, invariance of a ball, invariance of a quartic semialgebraic set under linear dynamics, local collision avoidance, and existence of a stabilizing control law. We also extend our earlier NP-hardness proof of testing local asymptotic stability for polynomial vector fields to the case of trigonometric differential equations of degree four.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Polynomial and trigonometric differential equations appear ubiquitously in a variety of application domains including robotics, economics, mathematical biology, and chemical engineering, among others. The equations of motion for most robotic systems for example can be described by the familiar *manipulator equations* which give rise to systems of differential equations that are a mixture of polynomial and trigonometric terms in the state variables. In mathematical biology and economics, polynomial differential equations such as the Lotka-Volterra model and its variants are used to model population dynamics and competition among entities in an economy. The dynamics of many chemical processes are also naturally modeled by polynomial differential equations. Aside from these specific examples, differential equations in numerous application domains are commonly *approximated* as polynomials.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

While mature computational tools exist for the numerical solution of such differential equations, in most of the application domains described above, one is *not* typically interested in *particular* solutions of the system. Rather, *qualitative properties* of the differential equations are of central importance. For example, one may be interested in the safety of a robot performing a certain dynamic task, or in determining if the population of certain species diminishes below a critical threshold. The former example is related to the *stability* of the control system employed by the robot while the latter can be addressed by defining an "acceptable" set of population numbers and asking whether this set is *invariant* (i.e. if the populations start off in this set, will they always remain within the set?). In a similar vein, one can ask if trajectories in a model of epidemic spread remain *bounded*.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The study of such qualitative properties of differential equations has an extensive literature and numerous algorithms have been proposed for addressing these questions computationally. However, for all but the simplest cases (e.g. the case of linear systems), the problems still lack satisfactory (i.e. exact and efficient) algorithms. This observation motivates the study of the fundamental computational complexity of these problems in order to establish theoretical bounds on the efficiency of algorithms that attempt to answer these questions. Such complexity results may play an important role in shaping the search for practical algorithms for these problems by limiting the kinds of algorithms one can possibly hope to obtain. Further, by understanding exactly where the complexity of these problems stems, we can hope to find *approximations* and *relaxations* that are more amenable to efficient solutions while still maintaining practical relevance.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Questions of complexity related to qualitative properties of differential equations have long been of theoretical interest. A natural question one can ask is if the stability of a system of polynomial differential equations can be decided by a Turing machine in finite time. In, Arnold made a well-known conjecture that the contrary is true; i.e. the question is undecidable. To the authors' knowledge, even though some variants of the question have been studied and answered, the question in its original form is so far unresolved. Although the results in this paper do not resolve Arnold's question, they provide lower bounds on the computational complexity of deciding local asymptotic stability and several similar and related problems.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The primary challenge in establishing such complexity results lies in relating the properties of the *continuous* solutions of polynomial and trigonometric differential equations to the *combinatorial* problems for which complexity results have been previously established. Explicitly mapping trajectories of a system (which typically one does not have access to exactly) to objects in combinatorial problems seems to be a hopeless approach. The main idea that allows us to by-pass this apparent challenge is to relate the combinatorial problem to properties of *Lyapunov functions* that prove stability/invariance of differential equations. All the results in this paper exploit this idea in one way or another.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The organization of the paper is as follows. After stating some preliminaries in Section II, we show in Section III that deciding local asymptotic stability for trigonometric polynomials of degree four is strongly NP-hard. While this result is an extension of the results presented in (which proves the corresponding result for cubic polynomial vector fields), the decision problem is of independent interest, particularly in the field of robotics. This is due to the fact that most mechanical systems can be modeled by the *manipulator equations*, which result in vector fields whose degrees are dominated by trigonometric terms.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Invariance of a basic semialgebraic set defined by a quartic polynomial ($d = 1$),

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Inclusion of the unit ball in the region of attraction of an equilibrium point ($d = 3$),

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Stability of an equilibrium point in the sense of Lyapunov ($d = 4$),

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

These notions are all formally defined in Section IV. The input to these problems is an ordered list of coefficients (expressed as rational numbers) defining the polynomial or trigonometric vector field. Establishing NP-hardness of these problems implies that unless P=NP, it is not possible to provide an algorithm that can have a running time bounded by a polynomial in the number of bits required to represent the input. Further, all the NP-hardness results in this paper are in the *strong* sense (as opposed to weakly NP-hard problems like KNAPSACK or SUBSET SUM). This implies that the problems remain NP-hard even when the bit length of the coefficients (i.e. the input) is $O{({log{(n)}})}$ (here, $n$ is the dimension of the state space). Unless P=NP, even pseudo-polynomial time algorithms cannot exist for strongly NP-hard problems; see for more details and definitions.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

In particular, our results suggest that none of the numerous recent techniques for systems analysis based on convex optimization (e.g. in terms of linear programs, linear matrix inequalities, or sum of squares programs) can be exact, unless the size of the formulated optimization problems are exponential in the input.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

We refer the reader interested in computational complexity in systems and control to the outstanding survey papers and references therein.

<!-- chunk {"id": "body-0016", "role": "body", "section": "A few preliminaries on forms", "weight": 1.0} -->

Many of the results in this paper will make use of *homogeneous* polynomials. A multivariate polynomial $p:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is homogeneous (of degree $d$) if it satisfies ${p{({\lambdax})}} = {\lambda^{d}p{(x)}}$ for all $x \in {\mathbb{R}}^{n}$ and all $\lambda \in {\mathbb{R}}$. This condition is equivalent to all monomials of $p$ having the same degree. A homogeneous polynomial is also called a *form*. Observe that products of forms are again forms, and that the components of the gradient of a form are forms of one fewer degree.

<!-- chunk {"id": "body-0017", "role": "body", "section": "A few preliminaries on forms", "weight": 1.0} -->

Here, $p$ is a homogeneous function of degree $d$ and $\nabla p$ denotes its gradient vector. The identity is easily derived by differentiating both sides of the above equation with respect to $\lambda$ and setting $\lambda = 1$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "A few preliminaries on forms", "weight": 1.0} -->

The degree of a polynomial vector field $\overset{˙}{x} = {f{(x)}}$, with $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n}}$, is defined to be the largest degree of the components of $f$. We say that the vector field $f$ is homogeneous if all components of $f$ are forms of the same degree. Finally, a form $p:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is said to be *positive definite* if ${p{(x)}} > 0$ for all nonzero $x$ in ${\mathbb{R}}^{n}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Complexity of deciding local asymptotic stability of trigonometric vector fields", "weight": 1.0} -->

In this section, we prove that deciding local asymptotic stability of trigonometric vector fields of degree four is strongly NP-hard.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Complexity of several qualitative properties of polynomial vector fields", "weight": 1.0} -->

As we remarked earlier, NP-hardness of testing local and global asymptotic stability of polynomial vector fields of degree 3 has already been established in our earlier work,\[1, Chap. 4\]. In this section, we prove that deciding several other important properties of polynomial vector fields is also NP-hard. For many of these properties, our proof of NP-hardness builds on the proof. Whenever a property has to do with an equilibrium point, we take this equilibrium point to be at the origin. In what follows, the norm $||.||$ is always the Euclidean norm, and the notation $B_{r}$ denotes the ball of radius $r$; i.e., $B_{r}: = {\{ x|||x|| \leq r\}}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark IV.1", "weight": 1.0} -->

Arguments similar to the one presented in the proof of (i) above can be given to show NP-hardness of deciding existence of a controller that establishes several other properties, e.g., invariance of the unit ball, inclusion of the unit ball in the region of attraction, etc. In the statement of (h), the fact that the set $\mathcal{S}$ is a polytope is clearly arbitrary. This choice is only made because "obstacles" are most commonly modeled in the literature as polytopes. We also note that a related problem of interest here is that of deciding, given two polytopes, whether all trajectories starting in one avoid the other. This question is the complement of the usual reachability question, for which claims of undecidability have already appeared; see also.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Conclusions and Open problems", "weight": 1.0} -->

Under the assumption P$\neq$NP, we have shown the impossibility of polynomial time (or even pseudo-polynomial time) algorithms for ten decision problems that ubiquitously arise in control theory and the study of continuous time dynamical systems. Although our hardness results are valid even for very restricted classes of systems (e.g. gradient systems), it is of course still possible that these decision problems admit polynomial time algorithms for other special (and possibly important) *subclasses* of polynomial or trigonometric vector fields.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Conclusions and Open problems", "weight": 1.0} -->

Aside from extending the results of Theorem IV.1 to other classes of vector fields (such as trigonometric ones), the obvious class of questions that our work leaves open is to investigate the *decidability* of the decision problems studied in Theorem IV.1, or their NP-hardness for polynomial vector fields of degree one or two. Although for linear systems some of these questions become easy, we expect that our hardness results can be strengthened to the case when the degree is $2$. Quadratic vector fields already demonstrate very complex behaviour; for example, their stability does not imply existence of a polynomial Lyapunov function of any degree. In general, one can reduce the degree of any vector field to two by introducing polynomially many new variables (see ). However, this operation may or may not preserve the property of the vector field which is of interest.
