<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Iterative Linear Quadratic Optimization for Nonlinear Control: Differentiable Programming Algorithmic Templates

Topics include Trajectory optimization, iLQR, Differentiable programming, Nonlinear control, Tutorial.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Presents iLQR and its variants as differentiable programming algorithmic templates, enabling systematic derivation, implementation, and differentiation through iLQR solvers using automatic differentiation frameworks.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Iterative optimization algorithms depend on access to information about the objective function. In a differentiable programming framework, this information, such as gradients, can be automatically derived from the computational graph. We explore how nonlinear control algorithms, often employing linear and/or quadratic approximations, can be effectively cast within this framework. Our approach illuminates shared components and differences between gradient descent, Gauss-Newton, Newton, and differential dynamic programming methods in the context of discrete time nonlinear control. Furthermore, we present line-search strategies and regularized variants of these algorithms, along with a comprehensive analysis of their computational complexities. We study the performance of the aforementioned algorithms on various nonlinear control benchmarks, including autonomous car racing simulations using a simplified car model. All implementations are publicly available in a package coded in a differentiable programming language.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Problems of the form have been tackled in various ways, from direct approaches using nonlinear optimization to convex relaxations using semi-definite optimization. Numerous packages exist for such problems such as CasAdi, Pyomo, JumP, IPOPT, or SNOPT, Crocoddyl, acados. A popular approach of the former category proceeds by computing at each iteration the linear quadratic regulator associated with a linear quadratic approximation of the problem around the current candidate solutions. The computed feedback policies are then applied either along the linearized dynamics or along the original dynamics to output a new candidate solution. Such canonical nonlinear control algorithms efficiently incorporate second-order information into the optimization procedure by exploiting the dynamical structure of the problem. This approach lends itself to an integration in a differentiable programming framework to extend this paradigm beyond first-order oracles.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Differentiable programming consists of the implementation of functions in a programming language that enables access to derivatives of these functions by automatic differentiation. Automatic differentiation itself has roots in the control literature, and its use is pervasive in numerous domains, in particular deep learning. Canonical nonlinear control algorithms incorporating second order information can also be integrated in reinforcement learning pipelines, and may then benefit from a differentiable programming viewpoint to isolate their underlying principles. These algorithms have indeed generally be presented through linear algebraic manipulations instantiated separately for each algorithm, which hinder a global perspective.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The motivation of this work is to cast all such algorithms in a common differentiable programming viewpoint to delineate the discrepancies between the different algorithms and identify the common subroutines. We review the implementation of (i) a Gauss-Newton method, a.k.a. Iterative Linear Quadratic Regulator (ILQR), (ii) a Newton method, (iii) a differential dynamic programming approach based on linear approximations of the dynamics and quadratic approximations of the costs, a.k.a. iterative Linear Quadratic Regulator (iLQR), (iv) a differential dynamic programming approach based on quadratic approximations of both dynamics and costs, usually simply called DDP, and consider regularized variants of the aforementioned algorithms with their corresponding line searches. In turn, the differentiable programming viewpoint informs efficient handling of memory by appropriate check-pointing. An extended related work discussion is in Appendix B.\Outline. In Sec. 2 we recall how linear quadratic control problems are solved by dynamic programming and used as a building block for nonlinear control algorithms.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The implementation of classical optimization oracles such as a gradient step, a Gauss-Newton step, or a Newton step is presented in Sec. 3. Sec. 4 details the rationale and implementation of differential dynamic programming approaches. Sec. 5 presents the computational complexities of each oracle in terms of space and time complexities in a differentiable programming framework. All algorithms are tested on several synthetic problems in Sec. 6: swinging-up a fixed pendulum, and autonomous car racing with simple dynamics. Code is available at Appendix A, B, C, D detail notations, related work, proofs and line-search procedures respectively. A summary of all algorithms with detailed pseudocode and computational schemes is given in Appendix E. Alternative implementations using check-pointing and different linear algebra solvers are presented in Appendix F and G respectively. Experimental setups and additional experiments are detailed in Appendix H and I.\Notation. For a sequence of vectors ${x_{1},\ldots,x_{\tau}} \in {\mathbb{R}}^{n_{x}}$, we denote by semicolons their concatenation s.t.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Tensor notations, such as ${\nabla^{2}f}{(x)}{\lbrack y,y, \cdot \rbrack}$, inspired, are detailed in Appendix A.

<!-- chunk {"id": "body-0009", "role": "body", "section": "From Linear Quadratic Control Problem to Nonlinear Control Algorithm", "weight": 1.0} -->

Algorithms for nonlinear control problems revolve around solving linear quadratic control problems by dynamic programming. Therefore, we start by recalling the rationale of dynamic programming and how discrete time control problems with linear dynamics and quadratic costs can be solved by dynamic programming.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Dynamic Programming", "weight": 1.0} -->

The idea of dynamic programming is to decompose dynamical problems such as into a sequence of nested subproblems defined by the *cost-to-go* $c_{t}$, from $x_{t}$ at time $t \in {\{ 0,\ldots,{\tau - 1}\}}$: The cost-to-go from $x_{\tau}$ at time $\tau$ is simply the last cost, namely, ${{c_{\tau}{(x_{\tau})}} = {h_{\tau}{(x_{\tau})}}},$ and the original problem amounts to compute $c_{0}{({\overline{x}}_{0})}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Dynamic Programming", "weight": 1.0} -->

The cost-to-go functions define nested subproblems that are linked for $t \in {\{ 0,\ldots,{\tau - 1}\}}$ by *Bellman's equation* The optimal control at time $t$ from state $x_{t}$ is given by $u_{t} = {\pi_{t}{(x_{t})}}$, where $\pi_{t}$, called a *policy*, is given by Define the procedure that back-propagates ($BP$) the cost-to-go functions as A dynamic programming approach, formally described in Algo. 1, solves problems of the form as follows.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Dynamic Programming", "weight": 1.0} -->

Compute recursively the cost-to-go functions $c_{t}$ for $t = {\tau,{\ldots,0}}$ using Bellman's equation (2.1), i.e., compute from $c_{\tau} = h_{\tau}$, and record at each step the policies $\pi_{t}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Dynamic Programming", "weight": 1.0} -->

Unroll the optimal trajectory that starts from time 0 at ${\overline{x}}_{0}$, follows the dynamics $f_{t}$, and uses at each step the optimal control given by the computed policies, that is, starting from $x_{0}^{\ast} = {\overline{x}}_{0}$, compute The resulting command ${\mathbf{u}}^{\ast} = {(u_{0}^{\ast};\ldots;u_{\tau - 1}^{\ast})}$ and trajectory ${\mathbf{x}}^{\ast} = {(x_{1}^{\ast};\ldots;x_{\tau}^{\ast})}$ are then optimal for problem. In the following, the dynamic programming ($DynProg$) procedure, detailed^22^2For ease of reference and comparisons, all procedures, algorithms, and computational schemes are grouped in Appendix E. in Algo.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Dynamic Programming", "weight": 1.0} -->

1 in Appendix E, is denoted The bottleneck of the approach is the ability to solve Bellman's equation (2.1), i.e., having access to the procedure $BP$ defined above.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Linear Dynamic, Quadratic Cost", "weight": 1.0} -->

In that case, under appropriate conditions on the quadratic functions, Bellman's equation (2.1) can be solved analytically through a linear quadratic back-propagation ($LQBP$) as recalled in Lemma 2.2. Note that the operation $LQBP$ defined in amounts to computing the Schur complement of a block of the Hessian of the quadratic ${x,u}\rightarrow{{q_{t}{(x,u)}} + {c_{t + 1}{({\ell_{t}{(x,u)}})}}}$, namely, the block corresponding to the Hessian w.r.t. the control variables (see, e.g.,). The proofs of Lemma 2.2 and Corollary 2.2 are standard and are given in Appendix C.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Linear Dynamic, Quadratic Cost", "weight": 1.0} -->

For linear functions $\ell_{t}$ and quadratic functions $q_{t},c_{t + 1}$ s.t. ${q_{t}{(x, \cdot)}} + {c_{t + 1}{({\ell_{t}{(x, \cdot)}})}}$ is strongly convex for any $x$, the procedure can be implemented analytically as detailed in Algo. 2. If problem consists of linear dynamics and quadratic costs that are strongly convex w.r.t. the control variable, the procedure $LQBP$ can be applied iteratively in a dynamic programming approach to give the solution of the problem, as formally stated in Corollary 2.2.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Linear Dynamic, Quadratic Cost", "weight": 1.0} -->

{coro} Consider problem such that for all $t \in {\{ 0,\ldots,{\tau - 1}\}}$, $f_{t}$ is linear, $h_{t}$ is convex quadratic with $h_{t}{(x, \cdot)}$ strongly convex for any $x$, and $h_{\tau}$ is convex quadratic. Then, the solution of problem is given by with $DynProg$ and $LQBP$ implemented in Algo. 1 and Algo. 2 respectively.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Nonlinear Control Algorithm Example", "weight": 1.0} -->

Nonlinear control algorithms based on nonlinear optimization use linear or quadratic approximations of the dynamics and the costs at a current candidate sequence of controllers to apply a dynamic programming procedure to the resulting problem. For example, the Iterative Linear Quadratic Regulator (ILQR) algorithm uses linear approximations of the dynamics and quadratic approximations of the costs. Each iteration of the ILQR algorithm is composed of the three steps below illustrated in Fig. 6.\Iterative Linear Quadratic Regulator Iteration.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Nonlinear Control Algorithm Example", "weight": 1.0} -->

The procedure is then repeated on the next sequence of control variables. Ignoring the line-search phase (namely, taking $\gamma = 1$), each iteration can be summarized as computing ${\mathbf{u}}^{next} = {{\mathbf{u}} + {\mathbf{v}}}$ where for $y_{0} = 0$, where $DynProg$ is the dynamic programming procedure implemented in Algo. 1. Note that for convex costs $h_{t}$ such that $h_{t}{(x, \cdot)}$ is strongly convex, the subproblems satisfy the assumptions of Cor. 2.2.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Nonlinear Control Algorithm Example", "weight": 1.0} -->

The iterations of the following nonlinear control algorithms can always be decomposed into the three passes described above for the ILQR algorithm. The algorithms vary by (i) what approximations of the dynamics and the costs are computed in the forward pass, (ii) how the policies are computed in the backward pass, (iii) how the policies are rolled out.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Classical Optimization Oracle", "weight": 1.0} -->

Problem is entirely determined by the choice of the initial state and a sequence of control variables, such that the objective in can be written in terms of the control variables ${\mathbf{u}} = {(u_{0};\ldots;u_{\tau - 1})}$ as The objective can be decomposed into the costs and the control of $\tau$ steps of a sequence of dynamics defined as follows.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Classical Optimization Oracle", "weight": 1.0} -->

The implementation of classical oracles for problem relies on the dynamical structure of the problem encapsulated in the control $f^{\lbrack\tau\rbrack}$ of the discrete time dynamics ${(f_{t})}_{t = 0}^{\tau - 1}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Formulation", "weight": 1.0} -->

Classical optimization algorithms rely on the availability of oracles for the objective. Here, we consider these oracles to compute the minimizer of an approximation of the objective around the current point with an optional regularization term. Formally, at a point ${\mathbf{u}} \in {\mathbb{R}}^{\tau n_{u}}$, given a regularization $\nu \geq 0$, for an objective of the form a *gradient* oracle to use a linear expansion of the objective, and to output, for $\nu > 0$, a *Gauss-Newton* oracle to use a linear quadratic expansion of the objective, and to output a *Newton* oracle to use a quadratic expansion of the objective, and to output where $\ell_{f}^{x}$, $q_{f}^{x}$ are the linear and quadratic expansions of $f$ around $x$ as defined in the notations in Eq..

<!-- chunk {"id": "body-0024", "role": "body", "section": "Formulation", "weight": 1.0} -->

Gauss-Newton and Newton oracles are generally defined without a regularization, i.e., for $\nu = 0$. However, in practice, a regularization may be necessary to ensure that Gauss-Newton and Newton oracles provide a descent direction. Moreover, the reciprocal of the regularization, $1/\nu$, can play the role of a stepsize as detailed in Appendix D. Lemma 3.1 presents how the computation of the above oracles can be decomposed into the dynamical structure of the problem. The proof is detailed in Appendix C.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Formulation", "weight": 1.0} -->

Consider a nonlinear dynamical problem summarized as with $f^{\lbrack\tau\rbrack}$ the control of $\tau$ dynamics ${(f_{t})}_{t = 0}^{\tau - 1}$ as defined in Def. 3.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Formulation", "weight": 1.0} -->

Gradient (10 ‣ 3.1 Formulation ‣ 3 Classical Optimization Oracle ‣ Iterative Linear Quadratic Optimization for Nonlinear Control: Differentiable Programming Algorithmic Templates")), Gauss-Newton (11 ‣ 3.1 Formulation ‣ 3 Classical Optimization Oracle ‣ Iterative Linear Quadratic Optimization for Nonlinear Control: Differentiable Programming Algorithmic Templates")) and Newton oracles for $h \circ g$ amount to solving for ${\mathbf{v}}^{\ast} = {(v_{0}^{\ast};\ldots;v_{\tau - 1}^{\ast})}$ linear quadratic control problems of the form the gradient oracle (10 ‣ 3.1 Formulation ‣ 3 Classical Optimization Oracle ‣ Iterative Linear Quadratic Optimization for Nonlinear Control: Differentiable Programming Algorithmic Templates")), ${q_{\tau}{(y_{\tau})}} = {\ell_{h_{\tau}}^{x_{\tau}}{(y_{\tau})}}$ and, for $0 \leq t \leq {\tau -

<!-- chunk {"id": "body-0027", "role": "body", "section": "Formulation", "weight": 1.0} -->

Second order methods such as Gauss-Newton or Newton methods generally require solving a linear system at a cubic cost in the dimension of the problem. Here, the dimension of the problem in the control variables is $\tau n_{u}$, with $n_{u}$, the dimension of the control variables, usually small (see the numerical examples in Sec. 6), but $\tau$, the number of time steps, potentially large if, e.g., the discretization time step used to define from a continuous time control problem is small while the original time length of the continuous time control problem is large. A cubic cost w.r.t. the number of time steps $\tau$ is then a priori prohibitive.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Formulation", "weight": 1.0} -->

A closer look at the implementation of all the above oracles (10 ‣ 3.1 Formulation ‣ 3 Classical Optimization Oracle ‣ Iterative Linear Quadratic Optimization for Nonlinear Control: Differentiable Programming Algorithmic Templates")), (11 ‣ 3.1 Formulation ‣ 3 Classical Optimization Oracle ‣ Iterative Linear Quadratic Optimization for Nonlinear Control: Differentiable Programming Algorithmic Templates")) shows that they all amount to solving linear quadratic control problems as presented in Lemma 3.1. Hence, they can be solved by a dynamic programming approach detailed in Sec. 3.2 at a cost linear w.r.t. the number of time steps $\tau$. As a consequence, if the dimensions $n_{u},n_{x}$ of the control and state variables are negligible compared to the horizon $\tau$, the computational complexities of Gauss-Newton and Newton oracles, detailed in Sec. 5 are of the same order as the computational complexity of a gradient oracle. This observation was done by Pantoja Dunn and Bertsekas, for a Newton step and Sideris and Bobrow, for a Gauss-Newton step.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Formulation", "weight": 1.0} -->

Wright, also presented how sequential quadratic programming methods can naturally be cast in a similar way. Lemma 3.1 casts all classical optimization oracles in the same formulation, including a gradient oracle.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Formulation", "weight": 1.0} -->

The linear quadratic control problems can be solved by different procedures than dynamic programming such as using Riccati-based or parallel implementations as detailed in Appendix G. We focus on their resolution by dynamic programming to cast all algorithms in a common framework.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Implementation", "weight": 1.0} -->

Given Lemma 3.1, for $f^{\lbrack\tau\rbrack}{({\overline{x}}_{0},{\mathbf{u}})}$ the control of $\tau$ dynamics ${(f_{t})}_{t = 0}^{\tau - 1}$ defined in Def. 3, classical optimization oracles for objectives of the form can be implemented by (i) instantiating the linear quadratic control problem with the chosen approximations, (ii) solving the linear quadratic control problem by dynamic programming as detailed in Sec. 2. Precisely, their implementation can be split into the following three phases.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Implementation", "weight": 1.0} -->

Forward pass: All oracles start by gathering the information necessary for the step in a forward pass that takes the generic form of Algo. 5 and can be summarized as that compute the objective $\mathcal{J}{({\mathbf{u}})}$ associated to the given sequence of controls $\mathbf{u}$ and record approximations ${(m_{f_{t}}^{x_{t},u_{t}})}_{t = 0}^{\tau - 1},{(m_{h_{t}}^{x_{t},u_{t}})}_{t = 0}^{\tau - 1},m_{h_{\tau}}^{x_{\tau}}$ of the dynamics and the costs up to the orders $o_{f}$ and $o_{h}$, The orders of approximation $o_{f},o_{h}$ for each algorithm are summarized in Fig. 1.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Implementation", "weight": 1.0} -->

Backward pass: Once approximations of the dynamics have been computed, a backward pass on the corresponding linear quadratic control problem can be done as in the linear quadratic case presented in Sec. 2. The backward passes of the gradient oracle in Algo. 6, the Gauss-Newton oracle in Algo. 7 and the Newton oracle in Algo. 8 take generally the form Namely, they take as input a regularization $\nu \geq 0$ and some approximations of the dynamics and the costs ${(m_{f_{t}}^{x_{t},u_{t}})}_{t = 0}^{\tau - 1},{(m_{h_{t}}^{x_{t},u_{t}})}_{t = 0}^{\tau - 1},m_{h_{\tau}}^{x_{\tau}}$ computed in a forward pass, and return a set of policies and the final cost-to-go corresponding to the subproblem.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Implementation", "weight": 1.0} -->

Roll-out pass: Given the output of a backward pass defined above, the oracle is computed by rolling out the policies along the linear trajectories defined in the subproblem. Formally, given a sequence of policies ${(\pi_{t})}_{t = 0}^{\tau - 1}$, the oracles are then given as ${\mathbf{v}} = {(v_{0};\ldots;v_{\tau - 1})}$ computed, for $y_{0} = 0$, by Algo. 11 as Here the policies ${(\pi_{t})}_{t = 0}^{\tau - 1}$ are output by one of the backward passes in Algo. 6, Algo. 7 or Algo. 8. For the Gauss-Newton and Newton oracles, an additional procedure checks whether the subproblems are convex at each iteration as explained in more detail in Appendix E.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Implementation", "weight": 1.0} -->

Gradient, Gauss-Newton, and Newton oracles are implemented, respectively, Algo. 12, Algo. 13, Algo. 14. Additional line-searches are presented in Appendix D. The computational schemes of a gradient, a Gauss-Newton and a Newton oracle are illustrated in Fig. 5, Fig. 6 and Fig. 8 respectively.\For a gradient oracle (10 ‣ 3.1 Formulation ‣ 3 Classical Optimization Oracle ‣ Iterative Linear Quadratic Optimization for Nonlinear Control: Differentiable Programming Algorithmic Templates")), the procedure $LQBP$ normally used to solve linear quadratic control problems simplifies to a linear back-propagation, $LBP$, presented in Algo. 3 that implements for linear functions $\ell_{t}^{f},\ell_{t}^{h},c_{t + 1}$. Plugging into the overall dynamic programming procedure, Algo. 3, the linearizations of the dynamics and the costs, we get that the gradient oracle, Algo.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Implementation", "weight": 1.0} -->

6, computes affine cost-to-go functions of the form ${c_{t}{(y_{t})}} = {{j_{t}^{\top}y_{t}} + j_{t}^{0}}$ with Moreover, the policies are independent of the state variables, i.e., ${\pi_{t}{(y_{t})}} = k_{t}$, with The roll-out of these policies is independent of the dynamics and output directly the gradient up to a factor $- \nu^{- 1}$. Note that we naturally retrieve the gradient back-propagation algorithm.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Differential Dynamic Programming Oracle", "weight": 1.0} -->

The original differential dynamic programming algorithm was developed by Jacobson and Mayne, and revisited, e.g., Mayne and Polak Murray and Yakowitz Liao and Shoemaker Tassa et al.,. The reader can verify from the aforementioned citations that our presentation matches the original formulation, e.g., the quadratic case, while offering a larger perspective on the method that incorporates, e.g., linear quadratic approximations. Such approaches have also been called *direct multiple shooting* by Bock and Plitt,.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Rationale", "weight": 1.0} -->

Denoting $h$ the total cost as in and $f^{\lbrack\tau\rbrack}$ the control in $\tau$ dynamics ${(f_{t})}_{t = 0}^{\tau - 1}$, Differential Dynamic Programming (DDP) oracles consist in solving approximately by means of a dynamic programming procedure and using the resulting policies to update the current sequence of controllers. For a consistent presentation with the classical optimization oracles presented in Sec. 3, we consider a regularized formulation of the DDP oracles, that is, for some regularization $\nu \geq 0$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Rationale", "weight": 1.0} -->

The objective in problem can be rewritten as where for a function $f$, $\delta_{f}^{x}$ is the finite difference expression of $f$ around $x$ as defined in the notations in Eq.. In particular, $\delta_{f^{\lbrack\tau\rbrack}}^{{\overline{x}}_{0},{\mathbf{u}}}{(0,{\mathbf{v}})}$ is the trajectory defined by the finite differences of the dynamics given as The dynamic programming approach is then applied on the above dynamics. Namely, the goal is to solve by dynamic programming. Denote then $c_{t}^{\ast}$ the cost-to-go functions associated to problem for $t \in {\{ 0,{\ldots\tau}\}}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Rationale", "weight": 1.0} -->

These cost-to-go functions satisfy the recursive equation starting from $c_{\tau}^{\ast} = \delta_{h_{\tau}}^{x_{\tau}}$ and such that our objective is to compute $c_{0}^{\ast}{}$. Since the dynamics $\delta_{f_{t}}^{x_{t},u_{t}}$ are not linear and the costs $\delta_{h_{t}}^{x_{t},u_{t}}$ are not quadratic, there is no analytical solution for the subproblem. To circumvent this issue, the cost-to-go functions are approximated as ${{c_{t}^{\ast}{(y_{t})}} \approx {c_{t}{(y_{t})}}},$ where $c_{t}$ is computed from approximations of the dynamics and the costs.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Rationale", "weight": 1.0} -->

The approximation is done around the nominal value of the subproblem which is ${\mathbf{v}} = 0$ and corresponds to ${\mathbf{y}} = 0$ and no change of the original objective.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Rationale", "weight": 1.0} -->

A DDP oracle computes then a sequence of policies by iterating in a backward pass, starting from $c_{\tau} = m_{\delta_{h_{\tau}}^{x_{\tau}}}$, Given a set of policies, an approximate solution is given by rolling out the policies along the dynamics defining problem, i.e., by computing $v_{0},\ldots,v_{\tau - 1}$ as The main difference with the classical optimization oracles lies a priori in the computation of the policies in detailed below and in the roll-out pass that uses the finite differences of the dynamics. The constant part of the cost-to-go functions is used for line-searches as detailed in Appendix D.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Detailed Derivation of the Backward Passes", "weight": 1.0} -->

Linear Approximation. If we consider a linear approximation for the composition of the cost-to-go function and the dynamics, we have where we denote simply $\ell_{f} = \ell_{f}^{0}$ the linear expansion of a function $f$ around the origin.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Detailed Derivation of the Backward Passes", "weight": 1.0} -->

Plugging this model into and using linear approximations of the costs, the recursion amounts to computing, starting from $c_{\tau} = \ell_{\delta_{h_{\tau}}^{x_{\tau},u_{\tau}}} = \ell_{h_{\tau}}^{x_{\tau},u_{\tau}}$, where in the last line we used that the cost-to-go functions $c_{t}$ are necessarily affine, s.t. ${c_{t + 1}{(y)}} = {{c_{t + 1}{}} + {\ell_{c_{t + 1}}{(y)}}}$. We retrieve then the same recursion as the one used for a gradient oracle, with the same policies. Since the computed policies are constant, they are not affected by the dynamics along which a roll-out phase is performed. In other words, the oracle returned by using linear approximations in a DDP approach is just a gradient oracle.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Detailed Derivation of the Backward Passes", "weight": 1.0} -->

Linear Quadratic Approximation. If we consider a linear quadratic approximation for the composition of the cost-to-go function and the dynamics, we have where we denote simply $q_{f} = q_{f}^{0}$ the quadratic expansion of a function $f$ around the origin.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Detailed Derivation of the Backward Passes", "weight": 1.0} -->

In that case, the recursion simplifies as and the policies are given by the minimizer of Eq.. The recursion is then the same as the recursion done when computing a Gauss-Newton oracle. Namely, the backward pass in this case is the backward pass of a Gauss-Newton oracle. Though the output policies are the same, the output of the oracle will differ since the roll-out phase does not follow the linearized trajectories in the DDP approach. The computational scheme of a DDP approach with linear quadratic approximations presented in Fig. 7 is then almost the same as the one of a Gauss-Newton oracle presented in Fig. 6, except that in the roll-out phase the linear approximations of the dynamics are replaced by finite differences of the dynamics. This DDP approach amounts to the iterative Linear Quadratic Regulator (iLQR) developed by Tassa et al.,.\Quadratic Approximation.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Detailed Derivation of the Backward Passes", "weight": 1.0} -->

If we consider a quadratic approximation for the composition of the cost-to-go function and the dynamics, we get where ${\nabla^{2}f}{(x,u)}{\lbrack \cdot, \cdot,\lambda\rbrack}$ is defined in (15 ‣ 3.1 Formulation ‣ 3 Classical Optimization Oracle ‣ Iterative Linear Quadratic Optimization for Nonlinear Control: Differentiable Programming Algorithmic Templates")).

<!-- chunk {"id": "body-0048", "role": "body", "section": "Detailed Derivation of the Backward Passes", "weight": 1.0} -->

cost-to-go functions $c_{t}$ are convex quadratics for all $t$. In that case, the recursion simplifies as and the policies are given by the minimizer of Eq.. The overall backward pass is detailed in Algo. 9.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Detailed Derivation of the Backward Passes", "weight": 1.0} -->

Compared to the backward pass of the Newton oracle in Algo. 8, we note that the additional cost derived from the curvatures of the dynamics is not computed the same way. Namely, the Newton oracle computes this additional cost by using back-propagated adjoint variables in Eq. (14 ‣ 3.1 Formulation ‣ 3 Classical Optimization Oracle ‣ Iterative Linear Quadratic Optimization for Nonlinear Control: Differentiable Programming Algorithmic Templates")), while in the DDP approach the additional cost is directly defined through the previously computed cost-to-go function. Fig. 9 illustrates the computational scheme of the implementation of DDP with quadratic approximations and can be compared to the computational scheme of the Newton oracle in Fig. 8.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Detailed Derivation of the Backward Passes", "weight": 1.0} -->

Note that, while we used second order Taylor expansions for the compositions and the costs, the approximate cost-to-go-functions $c_{t}$ are *not* second order Taylor expansion of the true cost-to-go functions $c_{t}^{\ast}$, except for $c_{\tau}$. Indeed, $c_{t}$ is computed as an approximate solution of the Bellman equation. The true Taylor expansion of the cost-to-go function requires the gradient and the Hessian of the cost and the dynamic in Eq. computed at the minimizer of the subproblem. Here, since we only use an approximation of the minimizer, we do not have access to the true gradient and Hessian of the cost-to-go function.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Implementation", "weight": 1.0} -->

The implementation of the DDP oracles follows the same steps as the ones given for classical optimization oracles as detailed below. The implementation of a DDP oracle with linear quadratic approximations is given in Algo. 15 and illustrated in Fig. 7. The implementation of a DDP oracle with quadratic approximations is given in Algo. 16 and illustrated in Fig. 9.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Implementation", "weight": 1.0} -->

Backward pass: As for the classical optimization oracles, the backward pass can generally be written If linear approximations are used, the backward pass is given in Algo. 6, if linear quadratic approximations are used, the backward pass is given in Algo. 7 and if quadratic approximations are used, the backward pass is given in Algo. 9.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Implementation", "weight": 1.0} -->

Roll-out pass: The roll-out phase differs by using finite differences of the original dynamics of problem rather than the linearized dynamics. Formally, given a sequence of policies ${(\pi_{t})}_{t = 0}^{\tau - 1}$, the oracles are then given as ${\mathbf{v}} = {(v_{0};\ldots;v_{\tau - 1})}$ computed, for $y_{0} = 0$, by Algo. 11 as

<!-- chunk {"id": "body-0054", "role": "body", "section": "Computational Complexity", "weight": 1.0} -->

In Figure 1, we present a summary of the different algorithms presented in this manuscript. We added in parentheses the names usually given for these methods. Additional line-search mechanisms are presented in Appendix D. The overall implementations are detailed in Appendix E. We consider then the computational complexities of the algorithms in a differentiable programming framework.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Computational Complexity", "weight": 1.0} -->

Formal Computational Complexity. We present in Table 5 the computational complexities of the algorithms following the implementations described in Sec. 3 and Sec. 4 and detailed in Appendix E. We ignore the additional cost of the line-searches which requires a theoretical analysis of the admissible stepsizes depending on the smoothness properties of the dynamics and the costs. We consider for simplicity that the cost of evaluating a function $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{n}}$ is of the order of $O{({nd})}$, as it is the case if $f$ is linear. For the computational complexities of the core operation of the backward pass, i.e, $LQBP$ in Algo. 2 or $LBP$ in Algo. 3, we simply give the leading computational complexities, which, in the case of $LQBP$, are the matrix multiplications and inversions.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Computational Complexity", "weight": 1.0} -->

The time complexities differ depending on whether linear or quadratic approximations of the costs are used. In the latter case, matrices of size $n_{u} \times n_{u}$ need to be inverted and matrices of size $n_{x} \times n_{x}$ need to be multiplied. However, all oracles have a linear time complexity with respect to the horizon $\tau$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Computational Complexity", "weight": 1.0} -->

We note that the space complexities of the gradient descent and the Gauss-Newton method or the DDP approach with linear quadratic approximations are essentially the same. On the other hand, the space complexity of the Newton oracle is a priori larger.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Computational Complexity", "weight": 1.0} -->

Computational Complexity in a Differentiable Programming Framework. The decomposition of each oracle between forward, backward and roll-out passes has the advantage to clarify the discrepancies between each approach. However, a careful implementation of these oracles only requires storing in memory the function and the inputs given at each time-step. Namely, the forward pass can simply keep in memory $h_{t},f_{t},x_{t},u_{t}$ for $t \in {\{ 0,\ldots,\tau\}}$. The backward pass computes then, on the fly, the information necessary to compute the policies. This amounts to a simple system of check-pointing, a strategy used in differentiable programming to circumvent the memory cost of the reverse-mode of automatic differentiation.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Computational Complexity", "weight": 1.0} -->

Acknowledgments. This work was supported by NSF DMS-1839371, DMS-2134012, CCF-2019844, CIFARLMB, NSF TRIPODS II DMS-2023166 and faculty research awards. The authors deeply thank Alexander Liniger for his help on implementing the bicycle model of a car. The authors also thank Dmitriy Drusvyatskiy, Krishna Pillutla and John Thickstun for fruitful discussions on the paper and the code.
