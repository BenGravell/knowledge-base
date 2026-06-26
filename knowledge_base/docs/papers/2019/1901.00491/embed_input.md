<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Optimal Control of the Double Integrator with Minimum Total Variation

Topics include Optimal control, Control, Control variable.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the well-known minimum-energy control of the double integrator, along with the simultaneous minimization of the total variation in the control variable. We derive the optimality conditions and obtain the unique optimal solution to the combined problem, where the initial and terminal boundary points are specified. We study the problem from a multi-objective optimal control viewpoint, constructing the Pareto front. We show that the unique asymptotic optimal control function, for the minimization of the total variation alone, is piecewise constant with one switching at the midpoint of the time horizon. For any instance of the boundary conditions of the problem, we prove that the asymptotic optimal total variation is exactly 2/3 of the total variation of the minimum-energy control. We illustrate the results for a particular instance of the problem and include a link to a video which animates the solutions while moving along the Pareto front.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The double integrator is a mathematical model for a point mass, typically idealizing a car in rectilinear motion on a flat and frictionless plane as schematically illustrated in Figure 1. It also constitutes a model for analogous rotational-mechanical and electrical systems. One should recall that a cubic curve between two oriented points, which minimizes its averaged acceleration, or more precisely, the $L^{2}$-norm of its acceleration, serves as a building block for cubic splines. This latter case can be represented as the energy-minimizing double integrator.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Due to its simplicity, optimal control of the double integrator is studied virtually in every course of lectures on optimal control theory. In the teaching of optimal control theory and its applications, although the minimum-energy, minimum-effort and minimum-time control of the double integrator are widely studied, minimization of total variation is not even considered, presumably because a maximum principle for the control minimizing its total variation does not exist.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

\psfrag{u}{u(t)}\psfrag{x10}{x1 = s0}\psfrag{x1}{x1(t):= y(t)}\psfrag{x2}{x2(t):= ẏ(t)}\includegraphics[width=284.52756pt]{car1.eps} Figure 1: A simplified physical model of a car as a point mass.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The double integrator model is so simple that an analytical solution can be worked out easily for the problem of energy minimization. Moreover, for the case of minimum-time control, where the control variable is bound-constrained, the optimal control can simply be shown to be bang--bang with at most one switching, i.e., the control variable switches from one bound to the other, and it does so at most once. The control structure can also be worked out easily in the case of minimum-effort control, where the $L^{1}$-norm of the control function is minimized. In summary, optimal control of the double integrator yields simple but rich-enough examples for illustrations of some key aspects of the theory of optimal control.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Total variation of a function can be broadly described as the total vertical distance traversed by the graph of the function (a precise definition is to be given in Section 3.1). A small total variation in the control function is obviously desirable, as it would make the control system easier to design and implement, resulting, for example, smaller or lighter motors for a robot or a spacecraft.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although there is a lack of theory and results for the pure minimization of total variation, it is often imposed in addition to the minimization of another functional, for instance, energy or duration of time. This is done in the earlier works, where the optimal control problem is discretized directly by assuming piecewise-constant optimal control variables. This discretization simplifies the expression for the total variation in control; however, optimality conditions for the original (continuous-time) problem cannot be derived or verified, because of the discretization itself.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Total variation is widely used as a regularization term in more general optimization problems such as imaging and signal processing (see and the references therein). It has also relatively recently been used as a regularization term for parameter estimation in linear quadratic control. A bound on the total variation in the control is derived for minimum-time linear control problems, although the total variation itself is not incorporated into the minimization problem.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the present article, in addition to the minimization of energy, we consider the minimization of the total variation in the control variable of the double integrator. In other words, we aim to study simultaneous minimization of energy and total variation, giving rise to multi-objective optimization and the study of the set of all trade-off/compromise solutions called the Pareto front. Optimal control problems which involve total variation have not been studied yet from the viewpoint of multi-objective optimal control.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we use a tutorial approach. First, in Section 2, we introduce the double integrator model as well as the problem of energy minimization as an optimal control problem. This is a standard problem in optimal control; so, we derive the optimal solution without going into details.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Section 3, we define the total variation of a function and state the energy and total variation minimization problem, by appending the total variation in control as a weighted term to the energy functional. Next, we augment the state variable vector, so that the problem can be rewritten and posed as an optimal control problem in standard form. We derive optimality conditions, and discuss the problem as a multi-objective optimal control problem. By means of asymptotic analysis, we derive an optimal solution for the pure total variation minimization problem. These kinds of results on total variation do not exist in the literature.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Section 4, via an example instance of the problem, we illustrate the results given in Section 3. In particular, we provide, via a URL link, a video illustration of the multi-objective solutions on the Pareto front, so that evolution of the solutions as the weight of total variation is varied can be animated and observed.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, in Section 5, we offer concluding remarks and provide various relevant open problems.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Minimum-Energy Control", "weight": 1.0} -->

Consider the car as a point unit mass, moving on a frictionless planar ground in a fixed line of action, as shown in Figure 1. Let the position of the car at time $t$ be given by $y{(t)}$ and the velocity by ${\overset{˙}{y}{(t)}}:={{({{{dy}/d}t})}{(t)}}$. By Newton's second law of motion, ${\overset{¨}{y}{(t)}} = {u{(t)}}$, where $u{(t)}$ is the summation of all the external forces applied on the car, in this case the force simply representing the acceleration and deceleration of the car. This differential equation model is referred to as the double integrator in system theory literature, since $y{(t)}$ can be obtained by integrating $u{(t)}$ twice.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Minimum-Energy Control", "weight": 1.0} -->

Here, the functions $x_{1}$ and $x_{2}$ are referred to as the state variables and $u$ the control variable. As a first step in writing the conditions of optimality for this optimization problem, define the Hamiltonian function $H$ for Problem (Pe) in the usual way as where ${\lambda{(t)}}:={({\lambda_{1}{(t)}},{\lambda_{2}{(t)}})} \in {IR^{2}}$ is the adjoint variable (or costate) vector such that (see) The equations in simply reduce to where ${\overline{\lambda}}_{1}$ and $c$ are real constants.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Minimum-Energy Control", "weight": 1.0} -->

By calculus of variations, or the maximum principle with an unconstrained control variable (see), if $u$ is optimal, then Substituting $u{(t)}$ in into the differential equations and solving these equations by also utilizing the boundary conditions in Problem (Pe), one gets the analytical solution for all $t \in {\lbrack 0,1\rbrack}$, where We note that the position variable $x_{1}{(t)}$ of the car is a cubic polynomial of time. Therefore, the minimum-energy control solution, despite being so simple, constitutes a building block for the problem of finding a cubic spline interpolant passing through a given set of points.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Total variation of a function", "weight": 1.0} -->

The total variation of a function $u:{{\lbrack t_{0},t_{f}\rbrack}\rightarrow{IR}}$ is defined as where the supremum is taken over all partitions of the interval $\lbrack t_{0},t_{f}\rbrack$ (see). Here, $N \in {\{ 1,2,3,\ldots\}}$ is arbitrary as is the choice of the values $t_{1},\cdots,t_{N - 1}$ in $\lbrack t_{0},t_{f}\rbrack$ which, however, must satisfy. The function $u$ is said to be of bounded variation on $\lbrack t_{0},t_{f}\rbrack$, if $\operatorname{TV}{(u)}$ is finite.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Total variation of a function", "weight": 1.0} -->

If $u$ is absolutely continuous on $\lbrack t_{0},t_{f}\rbrack$, in other words, $u \in {W^{1,1}{({\lbrack t_{0},t_{f}\rbrack};{IR})}}$, then where $\overset{˙}{u}:={{{du}/d}t}$. Practically speaking, $\operatorname{TV}{(u)}$ as given in represents the total distance traversed by the projection of the $u{(t)}$ vs. $t$ graph along the vertical $u{(t)}$ axis. Figure 2 illustrates this interpretation with ${u{(t)}} = {\sin t}$ over $\lbrack 0,{{3\pi}/2}\rbrack$, where clearly ${\operatorname{TV}{(u)}} = 3$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Total variation of a function", "weight": 1.0} -->

\psfrag{u}{u(t)}\psfrag{t}{t}\includegraphics[width=284.52756pt]{sint.eps} Figure 2: Graph of u (t) = sin t over [0, 3 π/2], illustrating that TV (u) = 3.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Minimum-Total-Variation Control of the Double Integrator", "weight": 1.0} -->

Recall that in the case when one has Problem (Pe), minimizing only the energy, the solution is as given in --. So, clearly ${\operatorname{TV}{(u)}} = {6{|{{2{({s_{f} - s_{0}})}} - v_{f} - v_{0}}|}}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Minimum-Total-Variation Control of the Double Integrator", "weight": 1.0} -->

We consider optimal control problems where we aim to minimize the total variation in the control variables in addition to the energy functional. where $\alpha > 0$ is referred to as the weight. We assume that $u$ is absolutely continuous on $\lbrack 0,1\rbrack$, in other words, $u \in {W^{1,1}{({\lbrack 0,1\rbrack})}}$. Then we define the new control variable ${v{(t)}}:={\overset{˙}{u}{(t)}}$ for a.e. $t \in {\lbrack 0,1\rbrack}$. Using, Problem (Ptv) can now be reformulated by incorporating the new variable as In this augmented form of the problem, $u$ becomes a new state variable.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Optimality Conditions", "weight": 1.0} -->

The Hamiltonian function for Problem (Paug) is given by where ${\lambda{(t)}} = {({\lambda_{1}{(t)}},{\lambda_{2}{(t)}})} \in {IR^{2}}$ and ${\eta{(t)}} \in {IR}$ are adjoint variables defined by (see) where ${\overline{\lambda}}_{1}$ and $c$ are real constants. Note that, although the expressions in are respectively the same as those, the real constants ${\overline{\lambda}}_{1}$ and $c$ in this case depend on the value of $\alpha$ and so are different in general.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Optimality Conditions", "weight": 1.0} -->

Next we state the maximum principle (see \[15, Theorem 1.5.1\]) for our setting as follows.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Optimality Conditions", "weight": 1.0} -->

Then there exist functions ${\lambda_{1},\lambda_{2},\eta} \in {W^{1,1}{(0,t_{f};{IR})}}$ such that${({\lambda_{1}{(t)}},{\lambda_{2}{(t)}},{\eta{(t)}})} \neq \mathbf{0}$, for every $t \in {\lbrack 0,1\rbrack}$, and, in addition to the state differential equations and other constraints given in Problem (Paug) and the adjoint differential equations in --, the following condition holds: Condition implies that for a.e. $t \in {\lbrack 0,1\rbrack}$. Note that ${|{\eta_{i}{(t)}}|} > \alpha$ is not allowed by the maximum principle, as otherwise one would get ${v{(t)}} = {- \infty}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Optimality Conditions", "weight": 1.0} -->

In view of, when ${- \alpha} < {\eta{(t)}} < \alpha$, a.e. $t \in {\lbrack 0,1\rbrack}$, the original control $u{(t)}$ is (possibly piecewise) constant. What if ${|{\eta{(t)}}|} \equiv \alpha$ over a subinterval of $\lbrack 0,1\rbrack$? If so, then we refer to the optimal control in this subinterval as singular control, which we elaborate further next.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Optimality Conditions", "weight": 1.0} -->

Optimal control. With the incorporation of the singular control, and by the continuity of the adjoint variable $\eta$, can be rewritten as for all $t \in {\lbrack 0,1\rbrack}$. Note that $v{(t)}$ in is piecewise-constant and so $u{(t)}$ is piecewise-linear and continuous in $t$. Then $\eta{(t)}$ is continuous and piecewise-quadratic in $t$. Note in particular that, differentiating both sides of the ODE, using $\overset{˙}{u} = v$ and substituting, one gets The expression in and the boundary conditions in imply that there will be at most two junction points, $0 < t_{1} < t_{2} < 1$, for $\eta{(t)}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Multi-Objective Optimal Control", "weight": 1.0} -->

Problem (Ptv), or equivalently Problem (Paug), concerns a simultaneous minimization of two objectives, which can simply be written as Problem (Pmo) is referred to as a multi-objective, or vector, optimal control problem, with $\mathcal{U}$ representing the feasible, or admissible, set of all control functions satisfying the differential equation constraints and the boundary conditions---see and the references therein. The set of all solutions of is usually infinite, consisting of all trade-off, or Pareto, solutions. Broadly speaking, a Pareto solution is a solution where one cannot improve the value of one objective functional without making the other worse. The set of all Pareto solutions in the $\varphi_{1}\varphi_{2}$-plane (or the value space) is referred to as the Pareto front of Problem (Pmo). An example of a Pareto front is given in Figure 3(a) (see details in Section 4).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Multi-Objective Optimal Control", "weight": 1.0} -->

For solving, a typical approach is to consider a scalarization of the vector objective and so reduce Problem (Pmo) to a single-objective optimal control problem. Note that $\varphi_{1}$ and $\varphi_{2}$ are convex and the constraint set represents linear differential equations and linear boundary conditions. Therefore we can use the weighted-sum scalarization (see): where $\alpha_{1} \in {}$. Since $\alpha_{1} \neq 0$, we can define $\alpha:={{({1 - \alpha_{1}})}/\alpha_{1}}$ and write with $\alpha \in {(0,\infty)}$. We note that Problems (Ps1) and (Ps2) are equivalent and that Problem (Ps2) is in the same form as Problem (Ptv).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Multi-Objective Optimal Control", "weight": 1.0} -->

In this case, the individual functionals in can be calculated using and, in terms of the unknown parameters $t_{1}$, ${\overline{u}}_{1}$ and ${\overline{u}}_{3}$, as follows.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Solution", "weight": 1.0} -->

By using and the initial conditions in Problem (Ptv), and by integrating directly, one can obtain the following expressions for the state variables $x_{1}{(t)}$ and $x_{2}{(t)}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Solution", "weight": 1.0} -->

Finally, writing out the terminal conditions ${x_{1}{}} = 0$ and ${x_{2}{}} = 0$ using and, respectively, using and, and carrying out lengthy manipulations, we obtain the following.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Solution", "weight": 1.0} -->

Once $t_{1}$ is determined as a solution of, the parameters ${\overline{\lambda}}_{1}$, ${\overline{u}}_{1}$ and ${\overline{u}}_{3}$ in --, respectively, can explicitly be found. The following lemma guides us as to which of the signs $\pm$ (in the coefficient of the $t_{1}^{2}$-term) in will yield a solution and that whether the solution will be unique or not.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Lemma 1 states that $t_{1} \in {(0,{1/2})}$, and Lemma 2 ‣ 3.5 Solution ‣ 3 Minimization of Total Variation ‣ Optimal Control of the Double Integrator with Minimum Total Variation") implies which sign in (37 ‣ 3.5 Solution ‣ 3 Minimization of Total Variation ‣ Optimal Control of the Double Integrator with Minimum Total Variation")) needs to be considered in order to find a unique $t_{1}$. By comparing (37 ‣ 3.5 Solution ‣ 3 Minimization of Total Variation ‣ Optimal Control of the Double Integrator with Minimum Total Variation")) and, it is immediate to see that the sign of $({v_{f} + v_{0} + {2{({s_{0} - s_{f}})}}})$ has to be taken into account. The following theorem provides the unique solution to Problem (Ptv), based on this observation. $\square$

<!-- chunk {"id": "body-0035", "role": "body", "section": "Asymptotic Solution (as ${\\mathbf{α}}\\rightarrow\\mathbf{\\infty}$)", "weight": 1.0} -->

As mentioned in the Introduction, it is not possible to write down the necessary conditions of optimality for the minimization of the total variation in the control variable alone. Nevertheless, an analytic solution of Problem (Ptv) can still be obtained by studying the asymptotic behaviour of the solutions when $\alpha\rightarrow\infty$. In this case, Equation becomes ${{{4t_{1}^{3}} - {6t_{1}^{2}}} + 1} = 0$, which has three real roots: 1/2 and ${({1 \pm \sqrt{3}})}/2$. This means that, in $(0,{1/2})$, $t_{1}\rightarrow{1/2}$. Then $t_{2}\rightarrow{1/2}$. Moreover, from Equation, ${\overline{\lambda}}_{1}\rightarrow{\pm \infty}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Asymptotic Solution (as ${\\mathbf{α}}\\rightarrow\\mathbf{\\infty}$)", "weight": 1.0} -->

However, these limit values of $t_{1}$ and ${\overline{\lambda}}_{1}$ make the expression in indeterminate. Therefore, we need to write the asymptotic expressions for the state variables (with $t_{1} = t_{2} = {1/2}$), in order to proceed: Now we can state the result, as $\alpha\rightarrow\infty$, in the following theorem.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Recall that when no minimization of the total variation in control is done, i.e., when only the energy is minimized, the total variation is ${\operatorname{TV}{(u)}} = {6{|{{2{({s_{f} - s_{0}})}} - v_{f} - v_{0}}|}}$. It is interesting to note that the asymptotic minimum total variation in (43 ‣ 3.6 Asymptotic Solution (as 𝜶→∞) ‣ 3 Minimization of Total Variation ‣ Optimal Control of the Double Integrator with Minimum Total Variation")) is exactly $2/3$ of the total variation in minimum-energy control. $\square$

<!-- chunk {"id": "body-0038", "role": "body", "section": "An Example", "weight": 1.0} -->

To demonstrate the results in Theorems 1) ‣ 3.5 Solution ‣ 3 Minimization of Total Variation ‣ Optimal Control of the Double Integrator with Minimum Total Variation") and 2 ‣ 3.6 Asymptotic Solution (as 𝜶→∞) ‣ 3 Minimization of Total Variation ‣ Optimal Control of the Double Integrator with Minimum Total Variation"), as well as illustrate what the Pareto front looks like using the expressions in --, we consider a particular instance when $s_{0} = 0$, $s_{f} = 0$, $v_{0} = 1$ and $v_{f} = 0$. In view of the interpretation of the double integrator dynamics provided in the Introduction, this particular instance means that the car with an initial unit velocity is required to come to rest in the same position where it started the motion.

<!-- chunk {"id": "body-0039", "role": "body", "section": "An Example", "weight": 1.0} -->

The minimum energy solution can be obtained directly, after substituting $s_{0} = 0$, $s_{f} = 0$, $v_{0} = 1$ and $v_{f} = 0$ into --, as for $t \in {\lbrack 0,1\rbrack}$. In this case, clearly, ${\operatorname{TV}{(u)}} = 6$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "An Example", "weight": 1.0} -->

\psfrag{a1}{\smallα = 10−6}\psfrag{a2}{\smallα = 0.05}\psfrag{a3}{\smallα = 0.4}\psfrag{a4}{\hskip 2.84526pt\smallα = 106}\psfrag{f1}{φ1}\psfrag{f2}{φ2}\includegraphics[width=227.62204pt]{Pareto.eps} (a) The Pareto front \psfrag{u}{u(t)}\psfrag{t}{t}\psfrag{a0}{\smallα = 10−6}\psfrag{a5}{\smallα = 106}\includegraphics[width=241.84842pt]{u.eps} (b) The control variable Figure 3: The Pareto front and the control variable for the multi-objective problem, with s0 = 0, sf = 0, v0 = 1 and vf = 0.

<!-- chunk {"id": "body-0041", "role": "body", "section": "An Example", "weight": 1.0} -->

Using a rather "continuous" range of values of $\alpha$, we have generated a movie, by using Matlab. The movie file is called mintotalvar.avi, which can be downloaded via the URL in Reference. An instance of the movie for $\alpha = 0.589$ is shown in Figure 4. For a large number of values of $\alpha$, the movie depicts/animates the Pareto front (using --) and the graphs of the control and state variables (using and --), as well as the graph of the adjoint variable $\eta{(t)}$ divided (or normalized) by $\alpha$ (using ). The graph of ${\eta{(t)}}/\alpha$ in the lower-right corner reconfirms that $u{(t)}$ is constant when ${|{\eta{(t)}}|} < \alpha$ and $u{(t)}$ is linear in $t$ when ${|{\eta{(t)}}|} = \alpha$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "An Example", "weight": 1.0} -->

As expected, reduction in total control variation is obtained as the value of $\alpha$ is increased, with the trade-off that minimum energy is increased. Figure 3(b), and the movie, clearly demonstrate that, as $\alpha$ gets larger, the control variable appears to become closer to a piecewise-constant function, switching from the constant level $- 3$ to the constant level $1$, resulting in ${\operatorname{TV}{(u)}} = 4$. This reconfirms Theorem 2 ‣ 3.6 Asymptotic Solution (as 𝜶→∞) ‣ 3 Minimization of Total Variation ‣ Optimal Control of the Double Integrator with Minimum Total Variation") as well as Remark 2 ‣ 3 Minimization of Total Variation ‣ Optimal Control of the Double Integrator with Minimum Total Variation").

<!-- chunk {"id": "body-0043", "role": "body", "section": "An Example", "weight": 1.0} -->

Finally, with ${\overline{u}}_{1} = {- 3}$ and ${\overline{u}}_{3} = 1$, the asymptotic expressions for the state variables in (40 ‣ 3 Minimization of Total Variation ‣ Optimal Control of the Double Integrator with Minimum Total Variation"))--(41 ‣ 3 Minimization of Total Variation ‣ Optimal Control of the Double Integrator with Minimum Total Variation")) can be rewritten neatly as

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

We have derived the unique solution to the optimal control problem of simultaneous minimization of energy and total variation in control for the double integrator. We obtained analytic expressions for the construction of the Pareto front. We have shown that the unique asymptotic optimal control function, for the minimization of the total variation alone, is piecewise constant with one switching at the midpoint of the time horizon. We computed the two constant levels of the asymptotic control function analytically. Subsequently, we have proved that the asymptotic optimal total variation is exactly $2/3$ of the total variation of the minimum-energy control. These results seem to be the first of their kind in the literature concerning optimal control with minimum total variation, even for a system as simple as the double integrator.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

The minimum-energy control problem which we have also considered is a special case of a general linear quadratic control problem. An approach similar to the one employed in the current paper can be employed for the more general linear quadratic control (or linear quadratic programming) problem where one is additionally concerned with the minimization of total variation, namely the problem The time horizon in Problem (LQPTV) has been set to be $\lbrack 0,1\rbrack$, but, without loss of generality, it can be taken to be any interval $\lbrack t_{0},t_{f}\rbrack$, with $t_{0}$ and $t_{f}$ specified. The state variable vector ${x{(t)}} \in {IR^{n}}$ and the control variable vector ${u{(t)}} \in {IR^{m}}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

The time-varying matrices $A:{{\lbrack 0,1\rbrack}\rightarrow{IR^{n \times n}}}$ and $B:{{\lbrack 0,1\rbrack}\rightarrow{IR^{n \times m}}}$ are continuous, $Q:{{\lbrack 0,1\rbrack}\rightarrow{IR^{n \times n}}}$ is symmetric positive definite and continuous in $t$, and $R:{{\lbrack 0,1\rbrack}\rightarrow{IR^{m \times m}}}$ is positive definite and continuous in $t$. The initial and terminal states are specified as $x_{0}$ and $x_{f}$, respectively.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

Since there are more than just one control variable, i.e., ${u{(t)}} = {({{\overline{u}}_{1}{(t)}},\ldots,{u_{m}{(t)}})} \in {IR^{m}}$, the total variation in can be generalized for this case as It should be noted that the problem we have studied in the current paper fits into the above problem description (LQPTV) with $n = 2$, $m = 1$, $Q = 0$ and $R = 1$, and the appropriate constant system and control matrices $A$ and $B$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

The general linear quadratic problem is a convex problem, so the weighted-sum scalarization can still be used (see ) when it is combined with the minimization of total variation. However, for a generalization to nonconvex problems, a scalarization different from the weighted-sum scalarization needs to be considered. This requires specialized numerical techniques in obtaining a solution---see and the pertaining discussion therein for problems which also have constraints on the state and control variables.
