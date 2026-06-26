<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Tutorial on Solution Properties of State Space Models of Dynamical Systems

Topics include Matrix exponential, Neumann series.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The starting point of analysis of state space models is investigating existence, uniqueness and solution properties such as the semigroup property, and various formulas for the solutions. Several concepts such as the state transition matrix, the matrix exponential, the variations of constants formula (the Cauchy formula), the Peano-Baker series, and the Picard iteration are used to characterize solutions. In this note, a tutorial treatment is given where all of these concepts are shown to be various manifestations of a single abstract method, namely solving equations using an operator Neumann series involving the Volterra operator of forward integration. The matrix exponential, the Peano-Baker series, the Picard iteration, and the Cauchy formula can be "discovered" naturally from this Neumann series. The convergence of the series and iterations is a consequence of the key property of asymptotic nilpotence of the Volterra operator. This property is an asymptotic version of the nilpotence property of a strictly-lower-triangular matrix.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

State space models are the starting point in analysis of dynamical systems. They come in various forms of generality as follows The state at each time ${x{(t)}} \in {\mathbb{R}}^{n}$ is an $n$-vector, while the input ${u{(t)}} \in {\mathbb{R}}^{q}$ is also a vector at each $t$, with typically a different dimension than the state. For control problems, for example, the signal $u$ is the control input, and most interesting problems have the dimension of $u$ being much less than that of $x$ (controlling many states with a single or few inputs). If the signal $u$ is a disturbance or a noise signal, it typically has dimensions comparable to those of the state $x$.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The first column in represents systems without an external input, and we generally want to understand their responses $\left\{ {x{(t)}} \right\}$ due to various boundary conditions $x{(\overline{t})}$ specified at some time $\overline{t}$. In the second column, the signal $u$ is regarded as an external signal, and we typically want to establish response properties for a whole class of inputs $u$ rather than a single, fixed input.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The systems in the first row are generally nonlinear, and without making more restrictive assumptions on the structure of the vector field $A$, one can only deduce rather basic properties of existence and uniqueness of solutions. An important special instance of (a) is the time-invariant case where $A$ is constant in $t$. The second row consists of linear time-varying systems. We will be able to say more about them, but in general these are capable of very rich behavior, and again without additional restrictive assumptions, only basic properties can be established. The third row represents linear time-invariant systems, and much more can be said about properties of those systems. Those statements will generally involve linear-algebraic properties of the matrices $A$ and $B$. As a side note, when the state dimension becomes very large or infinite, the distinctions between the three categories of systems listed above can become quite blurry and in some cases cease to be relevant.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

This tutorial is motivated by and organized around a pedagogical principle that it is better to discover results starting from basic, generally applicable principles than to simply be told what the answer is, and then just verify it. I will try to illustrate what I mean by this using the most concrete case of linear time-invariant systems. The traditional treatment to derive formulas for the solution of a linear time-invariant state space system proceeds as follows. First, the homogenous problem with ${w{(t)}} = 0$ is addressed. The solution of this problem is given in terms of the matrix exponential. Given any square matrix $A$, the exponential function is defined by the series formula It is not difficult to show that this series is absolutely convergent for any matrix $A$ and time $t$. Note also that $e^{0} = I$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

By differentiating this series element by element, it then follows that the derivative of this matrix-valued function is the matrix-valued function It is then an easy verification that the solution of (with $w = 0$) is given by | | ${x{(t)}} = {{e^{At}\overline{x}},\text{since}}$ | ${{\overset{˙}{x}{(t)}} = {\frac{d}{dt}e^{At}\overline{x}} = {Ae^{At}\overline{x}} = {Ax{(t)}}},$ | | \(3\) | | | and | ${{x{}} = \left.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

{e^{At}\overline{x}} \right|_{t = 0} = {e^{0}\overline{x}} = {I\overline{x}} = \overline{x}}.$ | | | The solution of with a non-zero forcing function $w$ is given by the "variations-of-constants" formula^11^1This is also known as the Cauchy formula.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The fact that this formula gives $x{(t)}$ that satisfies the differential equation can be directly verified by differentiation.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The development described above, while quick and expedient, is unsatisfactory. Although it might be easy to guess the definition of the matrix exponential, and the solution as a generalization of the well known scalar case, it is difficult to see how this might generalize to the linear time-varying or the nonlinear cases. Again, from a pedagogical point of view, being told what the answer to a problem is, and your role is simply to verify that it is indeed the answer is not helpful in gaining insight into how more general situations might be addressed. For example, if you have not seen the formula before, it probably seems to "come out of thin air". It is easy to verify, but where did it come from? What would a similar formula be in the time-varying case, or if the state $x$ is a matrix rather than a vector?

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

A more satisfactory development is to see the answer emerge naturally from basic, familiar principles that are applicable to a large variety of problem settings. At the expense of a little bit of abstraction, we can have a better, more contextual understanding of the subject. This is the approach we will follow in this paper which is organized around the following central idea. The differential equations are rewritten as integral equations, which can then be thought of as equations in an abstract function space involving the Volterra operator of forward integration. This operator has very special properties which we investigate. The various series expressions and iterative algorithms for solutions follow from Neumann series involving this operator. In particular, the matrix exponential, the Peano-Baker series, the variations-of-constants formula, and the Picard iteration are all specific manifestations of this abstract Neumann series. They all emerge naturally from applying the Neumann series without having to guess the answer. Furthermore, the convergence properties of all these series and iterations follow from an asymptotic nilpotence property of the Volterra operator. This gives a unified view of all the various results in this area.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

This presentation is organized as follows.: Introduces the basic properties of flow maps, and their special forms when the dynamics are time-invariant or linear respectively. These properties follow from the basic assumptions of existence and uniqueness.: Recasts the solution of state-space models in the linear case as a linear algebra problem in function space. The Volterra (forward) integration operator is introduced as analogous to strictly lower-triangular matrices. Such matrices are nilpotent, and the Volterra operator is shown to be "asymptotically nilpotent". Convergence of series and iterations with the Voiterra operator then follow from this latter property. The kernel representation of linear operators is introduced here as the main tool to understand these properties.: Shows how the matrix exponential and the Peano-Baker series are special instances of the Neuman series.: Considers systems with inputs in the linear case. The well-known "variations-of-constants" (Cauchy) formula is derived in three different ways, one of which is again as a consequence of the Neumann series. Readers not interested in systems with inputs can skip this section.: Considers general non-linear systems.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

The Neumann series here becomes the Picard iteration. The proof of convergence follow from fixed point theorems. The standard contraction mapping theorem is used to show local existence and uniqueness. A tighter fixed point theorem that uses the asymptotic nilpotence of the Volterra operator is used to show global existence and uniqueness.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Basic Properties", "weight": 1.0} -->

We consider first systems without inputs (systems (a), (c) and (e) in ). We will give various conditions for existence and uniqueness of solutions later on in Section 6. For now however, we will make the following standing assumption.

<!-- chunk {"id": "body-0015", "role": "body", "section": "The Flow Map", "weight": 1.0} -->

Consider now any of the systems (a), (c) and (e), and assume well-posedness over $\lbrack 0,T)$ for some $T$. The existence and uniqueness of solutions assumption implies that for each ${t,\overline{t}} \in {\lbrack 0,T)}$ there is a well-defined mapping $\Phi_{t,\overline{t}}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n}}$ such that We don't know this mapping explicitly. This mapping is simply the statement that $x{(t)}$ is the solution of the differential equation at time $t$ given the initial condition $x{(\overline{t})}$ at time $\overline{t}$. Since solutions exist and are unique by assumption, this is a well defined mapping.

<!-- chunk {"id": "body-0016", "role": "body", "section": "The Flow Map", "weight": 1.0} -->

More precisely, $\Phi:=\left\{ {{\Phi_{t,\overline{t}},t,\overline{t}} \in {\lbrack 0,\infty)}} \right\}$ is a two-parameter family of mappings on ${\mathbb{R}}^{n}$. We refer to $\Phi$ as the flow map of the dynamical system.

<!-- chunk {"id": "body-0017", "role": "body", "section": "The Flow Map", "weight": 1.0} -->

The flow map's dependence on the parameters has properties that follow immediately from its definition. First, at any $t \in {\lbrack 0,T)}$ where $I$ is the identity map. This follows since $\Phi_{t,t}$ maps an initial condition at $t$ to the solution at $t$, i.e. it maps each vector to itself. Second, consider three time instants ${t_{1},t_{2},t_{3}} \in {\lbrack 0,T)}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "The Flow Map", "weight": 1.0} -->

If we solve the equation from $t_{1}$ to $t_{3}$ starting from $x{(t_{1})}$, then the solution $x{(t_{3})}$ must be the same as what is obtained by solving the equation from $t_{1}$ to $t_{2}$ and then again from $t_{2}$ to $t_{3}$, with the latter starting from $x{(t_{2})}$ as an initial condition (see Figure 1(a) ‣ Figure 1 ‣ 2.1 The Flow Map ‣ 2 Basic Properties ‣ A Tutorial on Solution Properties of State Space Models of Dynamical Systems") for an illustration). In other words where the symbol $\circ$ denotes function composition. Since this has to hold for all possible initial conditions, we have equality of the mappings for all ${t_{1},t_{2},t_{3}} \in {\lbrack 0,T)}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "The Flow Map", "weight": 1.0} -->

This property is called the semigroup property, although this name is better suited for the time-invariant case which we discuss next.

<!-- chunk {"id": "body-0020", "role": "body", "section": "The Flow Map", "weight": 1.0} -->

(a) The semigroup property Φt3, t1 = Φt3, t2 ∘ Φt2, t1 is equivalent to saying that finding the solution at time t3 given an initial condition at time t1 is equivalent to solving in two steps. First, find the solution x (t2) at some intermediate time t2 from the initial condition at t1, then find the solution at time t3 from x (t2) regarded as an initial condition at t2. The answer should be the same as the going directly from t1 to t3.

<!-- chunk {"id": "body-0021", "role": "body", "section": "The Flow Map", "weight": 1.0} -->

(b) The time invariance property implies that the solution x (t) given an initial condition $x{(\overline{t})}$ is the same as solving a time-shifted problem (depicted in green), i.e. solving for $x_{s}{({t - \overline{t}})}$ from an initial condition ${x_{s}{}} = {x{(\overline{t})}}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Time Invariance", "weight": 1.0} -->

The concept of time invariance requires existence and uniqueness of solutions over semi-infinite time intervals. Without loss of generality, we will therefore assume well-posedness of the following system over the entire half line $\lbrack 0,\infty)$ where the vector field $A$ is constant in time. The "dynamics" of this system (i.e. the relation between $\overset{˙}{x}$ and $x$ at each time) are independent of $t$. Suppose that $x{(.)}$ is the solution from the initial condition ${x{}} = \overline{x}$. Define the left-shift of $x$ by where $\overline{t}$ is some fixed number. Note that the initial condition for $x_{s}{}$ is $x{(\overline{t})}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Time Invariance", "weight": 1.0} -->

Now if we solve the equation from the initial condition ${x_{s}{}} = {x{(\overline{t})}}$, the solution will simply be the portion of the original trajectory over $\lbrack\overline{t},\infty)$, which is the same as $x_{s}$ over $\lbrack 0,\infty)$ Thus the shifted function $x_{s}$ satisfies the differential equation with its initial condition as the vector $x{(\overline{t})}$. Figure 1(b) ‣ Figure 1 ‣ 2.1 The Flow Map ‣ 2 Basic Properties ‣ A Tutorial on Solution Properties of State Space Models of Dynamical Systems") illustrates this property, which is called time invariance (or more precisely time-shift equivariance), for which we give a formal definition.

<!-- chunk {"id": "body-0024", "role": "body", "section": "The State Transition Matrix", "weight": 1.0} -->

In the case of linear systems, the flow map $\Phi_{t_{2},t_{1}}$ can be shown to be a linear mapping on ${\mathbb{R}}^{n}$, and is therefore represented by a matrix-valued function $\Phi{(t_{2},t_{1})}$ of two parameteres, which is naturally called the state transition matrix. The fact that the flow map is linear is easy to show without actually "solving" the equation as follows.

<!-- chunk {"id": "body-0025", "role": "body", "section": "The State Transition Matrix", "weight": 1.0} -->

Consider a linear time-varying system with no input, and two solutions corresponding to two initial conditions We can immediately verify that the solution due to a linear combination ${x{(\overline{t})}} = {{\alpha{\overline{x}}_{1}} + {\beta{\overline{x}}_{2}}}$ of the initial conditions is the same linear combination ${x{(t)}} = {{\alphax_{1}{(t)}} + {\betax_{2}{(t)}}}$ of the individual solutions. Indeed Thus ${x{(t)}} = {{\alphax_{1}{(t)}} + {\betax_{2}{(t)}}}$ satisfies the differential equation as well as the initial condition. Note that the only property used above is the linearity of differentiation and the linearity of the right hand side of the differential equation.

<!-- chunk {"id": "body-0026", "role": "body", "section": "The State Transition Matrix", "weight": 1.0} -->

Recall that the flow map $\Phi_{t,\overline{t}}$ maps initial conditions at $\overline{t}$ to solutions at $t$. Since we have established that this map is linear, and on ${\mathbb{R}}^{n}$ general linear maps are represented by matrices, then there must exist a matrix-valued function of time $\Phi{(t,\overline{t})}$ such that This matrix-valued function of two time parameters $\Phi{(.,.)}$ is naturally called the state transition matrix. It inherits properties of the flow map when specialized to linear maps. For example, $\Phi_{t,t}$ is the identity mapping for any $t$, and since this linear map is represented by the matrix $\Phi{(t,t)}$, this must be the identity matrix. The semigroup property is also inherited, and in this case composition of maps becomes matrix multiplication. We now state these properties formally.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Linear Algebra Problem in Function Space", "weight": 1.0} -->

The key to the solution formulas for the system is a slight abstraction where we think of the system as a linear algebra problem but in function space. From this point of view, it is at first just as easy to do the time-varying case, which is a system of the form This equation is equivalent to an integral equation which we obtain by Integrating both sides of To express this equation as a linear algebra problem, fix a time horizon $\lbrack 0,T\rbrack$, and define the Volterra integration operator, which we denote by the symbol $\mathcal{V}$ This operator is well-defined on the function space $\mathsf{L}_{n}^{1}{\lbrack 0,T\rbrack}$. Define also the operator of point-wise (in time) multiplication by $A{(.)}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Linear Algebra Problem in Function Space", "weight": 1.0} -->

Finally define the operator ${\mathfrak{h}}:{{\mathbb{R}}^{n}\rightarrow{\mathsf{L}_{n}^{1}{\lbrack 0,T\rbrack}}}$, which takes vectors $\overline{x} \in {\mathbb{R}}^{n}$ to constant functions of time by where ${\mathfrak{h}}{(.)}$ is the unit step (Heaviside) function Note the slight abuse of notation where we use the same symbol to denote a function ${\mathfrak{h}}{(.)}$ of time, as well as this operator.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Linear Algebra Problem in Function Space", "weight": 1.0} -->

With the above definitions, the integral equation can now be written as the abstract equation where $\mathcal{V}\mathcal{A}$ is the composition of the action of the operator $\mathcal{A}$ (first) with the operator $\mathcal{V}$ (second). Since $w$ and $\overline{x}$ are usually given, we rewrite this equation so as to solve for $x$ in terms of the given quantities by The right hand side $({{\mathcal{V}w} + {{\mathfrak{h}}\overline{x}}})$ and $x$ are functions over $\lbrack 0,T\rbrack$, and $\left({I - {\mathcal{V}\mathcal{A}}} \right)$ is a linear operator on such functions. If this operator is invertible, then the solution is Thus we need to understand the operator $\left({I - {\mathcal{V}\mathcal{A}}} \right)^{- 1}$ and its properties.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Linear Algebra Problem in Function Space", "weight": 1.0} -->

The key is the familiar Neumann series The Neumann series has an interpretation as an iterative algorithm generally known as a fixed point iteration. Denote the right hand side of by $g$. The solution in terms of the Neumann series is then This infinite series can be rewritten as the iterative algorithm Thus $x_{k}$ is the $k$'th partial sum of the series. If this series converges, then the limit $x:={\lim_{k\rightarrow\infty}x_{k}} = {\lim_{k\rightarrow\infty}x_{k + 1}}$ satisfies and thus the limit of the iteration is indeed a solution of the original problem. We will study the convergence properties of this iteration, which also is applicable to nonlinear problems under certain conditions. For now, we consider only linear problems.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Linear Algebra Problem in Function Space", "weight": 1.0} -->

It turns out that the Volterra integration operator $\mathcal{V}$ has a special property that guarantees the convergence of the Neumann series under very mild conditions. In addition, this formula will lead naturally to the matrix exponential when $A$ is constant, and to the so-called Peano-Baker series in the time-varying case. First, we need to establish some important properties of $\mathcal{V}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Linear Algebra Problem in Function Space", "weight": 1.0} -->

The Volterra integration operator $\mathcal{V}$ is analogous to a strictly lower triangular matrix with entries of $1$ below the diagonal. This analogy is important to understand properties of this operator, and it is best done using the so-called kernel representation of linear operators which we now describe.

<!-- chunk {"id": "body-0033", "role": "body", "section": "The Kernel Representation of Linear Operators", "weight": 1.0} -->

Let $A$ be an $n \times n$ matrix with the $ij$'th entry denoted by $A_{ij}$. A matrix represents a linear operator on vectors by the matrix vector product $v = {Au}$ Now let $\mathsf{I} = {(a,b)} \subseteq {\mathbb{R}}$ be any interval, and let $A{(.,.)}$ be a real-valued function^22^2In the case when $u$ and $v$ are vector-valued functions, then $A{(.,.)}$ would be a matrix-valued function. We suppress this distinction in our notation, which is equally applicable to either situation. of two variables from that interval $A:{{\mathsf{I} \times \mathsf{I}}\rightarrow{\mathbb{R}}}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "The Kernel Representation of Linear Operators", "weight": 1.0} -->

Such a function defines a linear operator on single-variable functions over $\mathsf{I}$ in an analogous manner to by where the integration variable $\xi$ plays the same role as the column index $j$ over which the summation in is performed. The operation in is a linear operator $A:{u\mapsto v}$, and note the slight abuse of notation where we use the same symbol $A$ to denote the operator, as well as the function $A{(.,.)}$ of two variables. The function $A{(.,.)}$ is called the kernel function of the operator $A$, and the formula is called the kernel representation^33^3The reader should be careful not to confuse this with the null space of the operator, which is sometimes referred to as the kernel of the operator. The two concepts are unrelated. of $A$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "The Kernel Representation of Linear Operators", "weight": 1.0} -->

The operation is depicted in Figure 2. The one-variable functions $u{(\xi)}$ and $v{(x)}$ are analogous to "column vectors", while the two-variable kernel function $A{(x,\xi)}$ is analogous to a matrix, i.e. a two-dimensional array. For each $x$, the value of $v{(x)}$ is given by the operation of multiply-then-integrate of the corresponding "row" of $A{(x,\xi)}$ with the function $u{(\xi)}$ in an analogous manner to matrix-vector multiplication.

<!-- chunk {"id": "body-0036", "role": "body", "section": "The Kernel Representation of Linear Operators", "weight": 1.0} -->

Given two operators $A$ and $B$ in terms of their respective kernel functions, it is easy to see that the operator sum $C:={A + B}$ has as its kernel function ${C{(x,\xi)}} = {{A{(x,\xi)}} + {B{(x,\xi)}}}$ Therefore, under addition, kernel functions behave just like matrix-matrix addition which is element-by-element.

<!-- chunk {"id": "body-0037", "role": "body", "section": "The Kernel Representation of Linear Operators", "weight": 1.0} -->

Another intuitive property of kernel representations is that they can be composed in a manner similar to matrix-matrix multiplication. Let $A:{u\mapsto v}$ and $B:{v\mapsto w}$ be two operators with kernel representations Define a third operator as the composition ${C:={BA}}:{u\mapsto w}$, and calculate its kernel representation from those of $A$ and $B$ as follows Thus the kernel of the composition $C = {BA}$ is obtained from the formula Figure 3: A graphical depiction of the composition of two operators C = B A as the integral operation on their respective kernels. This operation is akin to matrix-matrix multiplication as shown above. The value of the kernel C at a point $(\overline{x},\overline{r})$ is obtained from integrating the “row” $B{(\overline{x},.)}$ against the “column” $A{(.,\overline{r})}$. which looks like matrix-matrix multiplication except for integration instead of summation.

<!-- chunk {"id": "body-0038", "role": "body", "section": "The Kernel Representation of Linear Operators", "weight": 1.0} -->

Each "row" $B{(x,.)}$ of the kernel of $B$ is integrated against each "column" $A{(.,r)}$ of the kernel of $A$. The composition operation is depicted graphically in Figure 3. The reader should compare this visually with the usual matrix-matrix multiplication.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Lower-Triangular Operators", "weight": 1.0} -->

Just like certain matrix structures encode symmetries or properties of the linear operations they represent, the structure of a kernel encodes properties of the operators they represent. Figure 4(a) ‣ Figure 4 ‣ Lower-Triangular Operators ‣ 3.1 The Kernel Representation of Linear Operators ‣ 3 A Linear Algebra Problem in Function Space ‣ A Tutorial on Solution Properties of State Space Models of Dynamical Systems") illustrates the structure of kernel functions of what can be termed "lower-triangular" operators. Such operators arise when modeling time-varying causal systems.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Lower-Triangular Operators", "weight": 1.0} -->

The kernel is restricted to be zero in the "upper triangular part" of the $(\tau,t)$ plane If $u$ and $y$ are temporal signals over the entire real line, then the lower-triangular property of the kernel implies that the integral has the following limits When $t$ and $\tau$ are interpreted as time, then is the description of a general time-varying system mapping $u$ to $y$ that has the causality property, i.e. for any given time $t$, current and past values of the output $\left\{ {{{y{(\tau)}};\tau} \leq t} \right\}$ do not depend on future values of the input $\left\{ {{{u{(\tau)}};\tau} > t} \right\}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Lower-Triangular Operators", "weight": 1.0} -->

An alternative way of imposing the lower-triangular condition is by using the unit-step (Heaviside) function $\mathfrak{h}$ as follows. Given any kernel function $A{(x,\xi)}$, observe that the product $A{(x,\xi)}{\mathfrak{h}}\left({x - \xi} \right)$ becomes a lower triangular kernel since ${{\mathfrak{h}}\left({x - \xi} \right)} = 0$ when $\xi > x$. The above holds regardless of the original upper and lower integration limits $\overline{\xi}$ and $\underset{¯}{\xi}$ respectively.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Lower-Triangular Operators", "weight": 1.0} -->

(a) A lower-triangular kernel is such that A (t, τ) = 0 for τ ≥ t. If it operates on time signals, a lower-triangular kernel is a causal system, i.e. past values of the output do not depend on future values of the input.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Lower-Triangular Operators", "weight": 1.0} -->

(b) The kernel function of the Volterra (forward) integration operator 𝒱 has value one over the lower-triangular region τ < t and zero everywhere else. It is analogous to a strictly lower-triangular matrix with ones on all subdiagonals.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Lower-Triangular Operators", "weight": 1.0} -->

Operators with a lower triangular kernel are sometimes called Volterra operators if the kernel function is bounded. For Volterra operators acting on function spaces $L^{p}{(\mathsf{I})}$ where $\mathsf{I}$ is compact, these operators have the important property that the Neumann series converges even if the operator norm is greater than one. We first investigate a particular Volterra operator, which is the forward-integration operator defined.

<!-- chunk {"id": "body-0045", "role": "body", "section": "The Volterra Integration Operator $\\mathcal{V}$", "weight": 1.0} -->

The integration operator has a kernel representation in terms of the unit step function as follows were we used the notation $\mathcal{V}{(t,\tau)}$ for the kernel function of the operator $\mathcal{V}$. This operator is analogous to a strictly lower-triangular matrix where all the entries below the diagonal are $1$. This is illustrated in Figure 4(b) ‣ Figure 4 ‣ Lower-Triangular Operators ‣ 3.1 The Kernel Representation of Linear Operators ‣ 3 A Linear Algebra Problem in Function Space ‣ A Tutorial on Solution Properties of State Space Models of Dynamical Systems").

<!-- chunk {"id": "body-0046", "role": "body", "section": "The Volterra Integration Operator $\\mathcal{V}$", "weight": 1.0} -->

A strictly lower-triangular matrix is nilpotent, i.e. the first $k$ subdiagonals of the $k + 1$ power of the matrix is zero, and thus it becomes zero after raising to a sufficiently large power. Although the operator $\mathcal{V}$ is not nilpotent, it does becomes "smaller" as it is composed with itself repeatedly, so it can be thought of as asymptotically nilpotent. More precisely, the composition formula for operator kernels implies that Repeated applications of this calculation show that^44^4As can be verified by induction.

<!-- chunk {"id": "body-0047", "role": "body", "section": "The Volterra Integration Operator $\\mathcal{V}$", "weight": 1.0} -->

Note that for each $(t,\tau)$, the kernel of $\mathcal{V}^{k}$ limits to zero as $k\rightarrow\infty$ since the factorial in the denominator grows faster than any power of $k$. This is the operator counterpart of a strictly lower triangular matrix being nilpotent, and we call this property asymptotic nilpotence. Asymptotic nilpotence implies that the Neumann series expression converges in the operator norm (on $\mathsf{L}^{p}{\lbrack 0,T\rbrack}$) ($p \in {\lbrack 1,\infty\rbrack}$) as outlined in Appendix A.

<!-- chunk {"id": "body-0048", "role": "body", "section": "The Volterra Integration Operator $\\mathcal{V}$", "weight": 1.0} -->

The expression gives a useful formula for repeated integration of any function. Define the $k$'th antiderivative of any function $g$ by and note the consistency of this notation with that for the $k$'th derivative of a function. Applying the expression for the kernel of $\mathcal{V}^{k}$ we see that This formula is known as the Cauchy formula for repeated integration. One interesting application of this formula is to define "fractional integrals" where the non-negative integer $k$ is replaced by a non-negative real number. The term ${({t - \tau})}^{({k - 1})}$ would still make sense, and the term ${({k - 1})}!$ is replaced by the Gamma function $\Gamma{({k - 1})}$. We will not need the concept of fractional integration in this note.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Formulas for the State Transition Matrix", "weight": 1.0} -->

In this section, we consider linear time-varying systems without input of the form and calculate the Neumann series expression for the response due to initial conditions only. For notational simplicity, we assume temporarily that the initial condition is given at $t = 0$, and write $\Phi{(t)}$ for $\Phi{(t,0)}$. By Lemma 4 the solution to is given in terms of the state transition matrix, which is the solution to the matrix differential equation Just like the vector case, this equation can be written as an integral equation where $I$ is the identity matrix, and the function ${{\left({{\mathfrak{h}}I} \right){(t)}} = I},$ for $t \in {\lbrack 0,T\rbrack}$. The abstract formula for the solution again follows from the Neumann series Our goal is to express this series in terms of the system parameter $A{(.)}$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Formulas for the State Transition Matrix", "weight": 1.0} -->

This is done for the time-invariant case first, where the Neumann series will yield the exponential function, and then generalized to the time-varying case, which will yield the less explicit Peano-Baker series.

<!-- chunk {"id": "body-0051", "role": "body", "section": "The Time-invariant Case: The Exponential Function", "weight": 1.0} -->

In the time-invariant case, $A{(t)}$ is constant in $t$ (so we just denote it by $A$). The action of the operator $\mathcal{V}\mathcal{A}$ on any function $g$ is Thus in the time-invariant case, the operators $\mathcal{V}$ and $\mathcal{A}$ commute (${\mathcal{V}\mathcal{A}} = {\mathcal{A}\mathcal{V}}$), and this makes the calculation of the Neumann series particularly easy Now compute the kernel representation of the operator $\left({I - {\mathcal{V}\mathcal{A}}} \right)^{- 1}$. Using, and noting that the operator $\mathcal{A}^{k}$ is simply multiplication by the matrix $A^{k}$, we see that Applying this to the solution formula This is exactly the solution as postulated in earlier.

<!-- chunk {"id": "body-0052", "role": "body", "section": "The Time-invariant Case: The Exponential Function", "weight": 1.0} -->

However, in this case, the matrix exponential $e^{At}$ emerges naturally (without guessing) from the details of the Neumann series for the time-invariant setting.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Time-varying Systems: The Peano-Baker Series", "weight": 1.0} -->

For this calculation and for the subsequent one with non-zero input, it will be useful to switch notation, and derive the expressions for the state transition matrix for a general initial time $\tau$ In this setting, the Volterra integration operator is the forward integration operator starting at time $\tau$ In the general time-varying case, the operators $\mathcal{A}$ and $\mathcal{V}$ are no longer necessarily commutative, and the Neumann series cannot be rearranged into the simpler form. For notational simplicity, relabel the composition where the last expression is for the kernel function of the operator $\mathcal{V}_{A}$. Note that the independent variables in this kernel function are $(t,\tau_{1})$, while $\tau$ should be regarded as a parameter specifying the initial condition time (and therefore a fixed number when applying the operator $\mathcal{V}_{A}$). This notational switching will turn out to significantly simplify subsequent notation.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Time-varying Systems: The Peano-Baker Series", "weight": 1.0} -->

Expressions for the kernels of powers $\mathcal{V}_{A}^{k}$ can get notationally messy as they will involve multivariable integrals. The notation will be significantly simplified by the introduction of the multivariable Heaviside function This is just convenient and compact notation for the product of several scalar Heaviside functions, which can be used as an alternative definition This function allows for encoding integration limits in the following manner Finally observe that the multivariable Heaviside function obeys the following "concatenation" property which will simplify later manipulations We now return to the calculation of the kernel functions of the operators $\mathcal{V}_{A}^{k}$. In the new notation, the kernel calculated in becomes ${\mathcal{V}_{A}{(t,\tau_{1})}} = {A{(\tau_{1})}{\mathfrak{h}}_{t,\tau_{1},\tau}}$, where $\tau$ is a fixed number denoting the initial condition time.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Time-varying Systems: The Peano-Baker Series", "weight": 1.0} -->

Calculations of subsequent powers give Note the use of the concatenation property to simplify the final expression. Repeated applications of this calculation show that Now we turn to the evaluation of the series for the state transition matrix. The $k$'th element of that series, which we denote by $\Phi_{k}$ is calculated by where the propery of $\mathfrak{h}$ gives the integration limits in the last equation.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Time-varying Systems: The Peano-Baker Series", "weight": 1.0} -->

We finally conclude that the state transition matrix $\Phi{(t,\tau)}$ of the system is given by the Peano-Baker series where each $\Phi_{k}$ is given. Note that the expression also implies that the series terms have the following recursion relationship with ${\Phi_{0}{(t,\tau)}} = I$. The convergence of the Peano-Baker series is a consequence of the "asymptotic nilpotence" of the Volterra integration operator. Appendix A details this argument.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Time-varying Systems: The Peano-Baker Series", "weight": 1.0} -->

In general, the Peano-Baker series terms do not yield tractable expressions except in special cases. One such case is when the time-varying family of matrices $\left\{ {{{A{(t)}},t} \in {\lbrack 0,T\rbrack}} \right\}$ mutually commute. In this case, the series can be used to express $\Phi$ in terms of a matrix exponential.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Systems with Inputs", "weight": 1.0} -->

We will show that the solution to the linear time-varying system with input is given by the so-called variations of constants formula where $x{(\overline{t})}$ is an initial condition, and $\Phi$ is the state transition matrix of the homogenous problem (i.e. the problem with ${w{(t)}} = 0$). This formula is states that the solution is the sum of $\Phi{(t,\overline{t})}x{(\overline{t})}$, which is the response due to the initial condition (also called the zero-input response), and the response due to input (also called the input-to-state response), which is a linear operation on $\left\{ {{{u{(\tau)}},\tau} \in {\lbrack\overline{t},t\rbrack}} \right\}$, the input function restricted to the time interval $\lbrack\overline{t},t\rbrack$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Systems with Inputs", "weight": 1.0} -->

The formula can be directly verified by differentiation. First recall the Leibniz integral rule, which is the fundamental theorem of calculus when the integral limits depend on the differentiation variable (see Exercise 3 for a proof). In this specific case it states that for any function $f$ of two variables If $f$ is matrix-valued, this formula applies entry by entry. Now differentiating While the formula is relatively easy to verify, it is not clear where it comes from or how one can discover it from first principles. In the following we present three different methods of arriving at this formula from basic principles. Each method gives additional insight into the problem. First, we consider the response of the system for a special input which is a Dirac delta function.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Systems with Inputs", "weight": 1.0} -->

Consider an input of the form ${w{(t)}} = {\overline{w}\delta{({t - \tau})}}$, a delta function in the direction of the vector $\overline{w}$ applied at time $\tau$ To see what happens around the time $\tau$, integrate the equation over $\lbrack{\tau - \epsilon},{\tau + \epsilon}\rbrack$ Provided that the function $A{(t)}x{(t)}$ is bounded, the last integral term becomes zero when taking the limit $\epsilon\rightarrow 0$, and we conclude that Thus the effect of a delta function at time $\tau$ in the input is to make the state "jump" from $x{(\tau^{-})}$ just before $\tau$ to $x{(\tau^{+})}$ just after $\tau$, with the jump magnitude and direction equal to the vector $\overline{w}$.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Systems with Inputs", "weight": 1.0} -->

This is illustrated in Figure 5(a) ‣ Figure 5 ‣ 5 Systems with Inputs ‣ A Tutorial on Solution Properties of State Space Models of Dynamical Systems").

<!-- chunk {"id": "body-0062", "role": "body", "section": "Systems with Inputs", "weight": 1.0} -->

(a) The input $\overline{w}\delta{({t - \tau})}$ is an impulse at time τ with strength given by the vector $\overline{w}$. This input causes the state to “jump” from x (τ−):= limt ↗ τ to x (τ+):= limt ↘ τ. The magnitude and direction of the jump is given by the vector $\overline{w}$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Systems with Inputs", "weight": 1.0} -->

(b) When the input is an impulse $\overline{w}\delta{({t - \tau})}$ at time τ ∈ (0, T), with zero initial conditions x = 0, the state becomes non-zero at τ, and evolves as if ${x{(\tau)}} = \overline{w}$ is an initial condition. The entire solution is then ${x{(t)}} = {\Phi{(t,\tau)}\overline{w}{\mathfrak{h}}{({t - \tau})}}$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Systems with Inputs", "weight": 1.0} -->

For example, consider the system starting from zero initial conditions ${x{}} = 0$, and the impulse is applied at some time $\tau \in {(0,T)}$. The response is ${x{(t)}} = 0$ for $t \in {\lbrack 0,\tau)}$. Around $t = \tau$ the state jumps to ${x{(\tau^{+})}} = \overline{w}$. Since the input is then zero over the remainder of the time interval $(\tau,T\rbrack$, the state evolves according to $\Phi{(t,\tau)}\overline{w}$ since ${x{(\tau^{+})}} = \overline{w}$ is the initial condition at $t = \tau$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Systems with Inputs", "weight": 1.0} -->

The full evolution over the entire interval $\lbrack 0,T\rbrack$ can then be written as Figure 5(b) ‣ Figure 5 ‣ 5 Systems with Inputs ‣ A Tutorial on Solution Properties of State Space Models of Dynamical Systems") illustrates this example which we will use next in a superposition argument.

<!-- chunk {"id": "body-0066", "role": "body", "section": "The Variations of Constants Formula via Superposition", "weight": 1.0} -->

The system has an input $w$ that is persistently (in time) acting on it. If the signal $w$ can be written as a linear combination of "simpler" inputs, for which the solution is already known, then again by linearity we can write the response as a linear combination of the individual responses. Consider writing any signal as a integral involving the delta function This integral can be though of as "weighted sum" of a parametrized family of delta functions with the function $w{(\tau)}$ acting as the "weighting function". The calculation already gives us the response to each $\delta_{\tau}{(t)}w{(\tau)}$. We label that response as $x_{\tau}$ Note that this formula should be read so that it is a relation between functions of $t$, with $\tau$ as a parameter.

<!-- chunk {"id": "body-0067", "role": "body", "section": "The Variations of Constants Formula via Superposition", "weight": 1.0} -->

The response to the "combined" signal is then the integral of all of those individual responses This is precisely the input-to-state response portion of the variations of constants formula.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Linearity of the Input-to-State Response", "weight": 1.0} -->

We have already seen in Section 2.3 that the zero-input response is a linear mapping from initial conditions to the response at any time. It is similarly easy to show that with zero initial conditions, the input-to-state response must be linear. Consider two inputs acting on the same system with zero initial conditions Adding both sides of the equations as an arbitrary linear combination shows that Thus the response to a linear combination of the two inputs is the same linear combination of their respective responses (when initial conditions are zero).

<!-- chunk {"id": "body-0069", "role": "body", "section": "Linearity of the Input-to-State Response", "weight": 1.0} -->

Recall the kernel representation of linear operators, by which any linear mapping of functions on an interval $\lbrack 0,T\rbrack$ to other functions on $\lbrack 0,T\rbrack$ can be written in the form where the kernel function $G{(.,.)}$ may contain generalized functions. The first form is general, while the second is for the case when the operator is causal. This is the case for the system solved forward in time, as the response $x$ cannot anticipate future values of the input $w$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Linearity of the Input-to-State Response", "weight": 1.0} -->

Given that the response is of the form, we now can determine what the original differential equation implies about the kernel function $G{(.,.)}$ where the last equation follows from applying the Leibniz integral rule. To see what $G{(t,t)}$ should be, note that the kernel representation implies that Thus we can determine $G{(t,t)}$ by applying a delta function input at time $t$ with initial conditions ${x{(t^{-})}} = 0$ and then ${G{(t,t)}} = {x{(t^{+})}}$ is the value of the immediate state response. The formula implies that ${x{(t^{+})}} = \overline{w}$, and since $\overline{w} = {G{(t,t)}\overline{w}}$ for all possible vectors $\overline{w}$, then $G{(t,t)}$ must be the identity matrix.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Linearity of the Input-to-State Response", "weight": 1.0} -->

Applying this to we see that Since this formula has to hold for all possible input functions $w$, we finally conclude that This is precisely the differential equation for the state transition matrix found earlier. We therefore conclude that ${G{(t,\tau)}} = {\Phi{(t,\tau)}}$, and the linear operation can now be rewritten as Again, this is the input-to-state portion of the variations of constants formula.

<!-- chunk {"id": "body-0072", "role": "body", "section": "The Variations of Constants Formula via the Neumann Series", "weight": 1.0} -->

In calculating the initial-condition response for general time-varying system, we used the Neumann series to arrive at the Peano-Baker series. More precisely, we used the kernel representation for each term $\mathcal{V}_{A}^{k}$ in the Neumann series, and then applied it to constant functions to give each term of the Peano-Baker series. For the input-to-state response, we return to the kernel representation of $\mathcal{V}_{A}^{k}$, but apply it to non-constant functions of the form $\mathcal{V}w$.

<!-- chunk {"id": "body-0073", "role": "body", "section": "The Variations of Constants Formula via the Neumann Series", "weight": 1.0} -->

Recall the abstract formula for the solution, and consider only the input-to-state response (i.e. $\overline{x} = 0$), (recall that $\mathcal{V}_{A}:={\mathcal{V}\mathcal{A}}$). Each term in this series can be calculated using the kernel function of $\mathcal{V}_{A}^{k}$ as given. For notational consistency, we now denote the initial time with $\overline{t}$, i.e. the input is applied over $\lbrack\overline{t},T\rbrack$ The last equality follows from the expression for the $k$'th term of the state transition matrix.

<!-- chunk {"id": "body-0074", "role": "body", "section": "The Variations of Constants Formula via the Neumann Series", "weight": 1.0} -->

The total response is then given by the sum over all $k$ of the terms where the last equation follows from the series expression for the state transition matrix. This is precisely the input-to-state term in the variations of constants formula.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Nonlinear Equations: The Picard Iteration", "weight": 1.0} -->

We now consider more general systems^55^5With very minor modifications, everything in this section applies equally to the more general time varying case ${\overset{˙}{x}{(t)}} = {F\left({x{(t)}},t \right)}$. of the form where we set the initial time to $t = 0$ for notational simplicity. In such a general setting, we will not be able to say much about solutions other than existence and uniqueness for certain classes of vector fields $A$. This existence and uniqueness result is sometimes referred to as the Picard-Lindelöf Theorem, the heart of which is the so-called Picard iteration, which is the nonlinear version of the Neumann series discussed earlier. The convergence of this iteration can be shown using the (Banach) fixed point theorem. The key to this argument is a $C{\lbrack 0,T\rbrack}$ norm bound between successive iterates, which is accomplished by similar arguments used for bounds on the action of the Volterra operator.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Nonlinear Equations: The Picard Iteration", "weight": 1.0} -->

The differential equation can be equivalently viewed as an integral equation by integrating both sides to get where the "Heaviside operator" maps vectors to functions ${{\left({{\mathfrak{h}}\overline{x}} \right){(t)}}:=\overline{x}},{t \in {\lbrack\overline{t},T\rbrack}}$, $\mathcal{V}$ is the familiar integration (Volterra) operator, and $\mathcal{A}$ is the nonlinear point-wise operator Unlike the linear case, we cannot write a Neumann series of the form because the operator $\mathcal{A}$ does not distribute over additions. On the other hand, we can still make sense of the iteration | | $x_{k + 1}$ | ${= {{{\mathfrak{h}}\overline{x}} + {\mathcal{V}\mathcal{A}{(x_{k})}}}}.$ | | | This is the Picard iteration in the general nonlinear case.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Nonlinear Equations: The Picard Iteration", "weight": 1.0} -->

If this iteration converges, then $\lim_{k\rightarrow\infty}x_{k + 1} = \lim_{k\rightarrow\infty}x_{k} =:x$, and this limit $x$ satisfies the original equation.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Nonlinear Equations: The Picard Iteration", "weight": 1.0} -->

The convergence of the Picard iteration is dependent on properties of the function $A$. It converges for some, but not others. We will first give conditions and a proof of convergence over some interval $\lbrack 0,\epsilon)$ near the initial condition. This will follow from a classic argument using the so-called Banach fixed point theorem. We will then use a refinement of this technique to show global convergence over all time intervals provided that the nonlinear function $A$ has a linear bound (the so-called Lipschitz bound). We then close with some examples demonstrating the lack of uniqueness or global existence when those conditions do not hold.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Local Convergence and Existence", "weight": 1.0} -->

A common method to show convergence of iterations is the contraction mapping theorem (also called the Banach fixed point theorem ), whose proof is in Appendix C.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Global Convergence and Existence", "weight": 1.0} -->

The previous argument implied that unique solutions can only be guaranteed to exists on proper subintervals of $\lbrack 0,{\min\left\{ {1/\overline{l}},T \right\}}\rbrack$. This seems rather unsatisfactory as the interval can become arbitrarily small as $\overline{l}$ becomes large. In fact, the argument we just presented is unnecessarily conservative. To appreciate this, consider the linear case, where $M$ becomes the mapping $\mathcal{V}_{A}$ from Section 4, and the Picard iteration is just the Neumann series. Demanding that $\mathcal{V}_{A}$ be a contraction mapping is equivalent to demanding that its induced norm $\left\| \mathcal{V}_{A} \right\| < 1$.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Global Convergence and Existence", "weight": 1.0} -->

However, because of the causality property of the Volterra operator, we were earlier able to show that $\mathcal{V}_{A}^{k}$ converges to zero in a way that insures the absolute summability of the Neumann series even if $\left\| \mathcal{V}_{A} \right\| < 1$ did not hold. They key condition was not $\left\| \mathcal{V}_{A} \right\| < 1$, but rather that $\left\| \mathcal{V}_{A}^{k} \right\|$ be a summable (in $k$) sequence. This leads us to state a better version of the fixed point theorem.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Example 10", "weight": 1.0} -->

Consider the scalar nonlinear system This scalar differential equation is solvable by "separation of variables" and direct integration This equation has a solution for small initial times, but it has the interesting feature of "finite escape time" as $t$ approaches ${1/x}{}$. That is the solution asymptotes to infinity as $t\rightarrow{{1/x}{}}$. The larger the initial condition, the shorter is the time interval over which the solution is possible. The right hand side of is not globally Lipschitz, and therefore Theorem 9 does not apply. There is however a notion of locally Lipschitz systems for which only local existence can be guaranteed, with the time interval of existence being dependent on the initial condition. This is the situation with this example.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Example 11", "weight": 1.0} -->

In this example, solutions need not be unique. This usually happens when the vector field $F$ has infinite derivatives. Consider the scalar system Clearly ${x{(t)}} = 0$, $t \geq 0$ is a solution, but there are others. By separation of variables again Thus we have found two different solutions from the same initial conditions. Note that these solutions are valid for all $t \in {\lbrack 0,\infty)}$. Therefore, the non-uniqueness phenomenon is a separate one from the finite-escape-time phenomenon.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Modeling Implications of Existence and Uniqueness", "weight": 1.0} -->

Both of the examples above highlight an important issue in mathematical modeling of physical systems. We generally believe that given enough information about a physical system, we can construct a mathematical model (e.g. a differential equation) that predicts the future behavior of the system given a fully accurate (infinite precision) description of initial conditions^99^9The discussion here is unrelated to the phenomenon of "chaos", which involves sensitive dependence on initial conditions. There are many chaotic systems with solutions that are guaranteed to exists from all initial conditions and are unique.. All models however are approximate, and no one believes that their mathematical model of any physical phenomena is fully accurate in all regimes^1010^10Those who do not realize that, are usually writing science fiction, contemplating Schrödinger's cat, or some other similar speculation.. If we have finite-escape-time, this means that quantities (e.g. velocities, pressures, etc.) are becoming so large that the mathematical model is no longer fully valid. If we have differential equations that are not locally Lipschitz (such as Example 11 above), this means that derivatives (usually forces in mechanical models) become arbitrarily sensitive to small changes in the state.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Modeling Implications of Existence and Uniqueness", "weight": 1.0} -->

This is again a regime where the mathematical model breaks down, and no longer accurately represents the physical world.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Modeling Implications of Existence and Uniqueness", "weight": 1.0} -->

The theme of the above remarks is that non-uniquness or lack of existence of solutions is not a mathematical difficulty, but rather a mathematical modeling difficulty. One can come up with equations and mathematical constructs that do all kinds of fantastical things. The question is whether these are good mathematical models of the physical world. It seems like a natural minimal requirement that a mathematical model should posses the property of existence and uniqueness of solutions.
