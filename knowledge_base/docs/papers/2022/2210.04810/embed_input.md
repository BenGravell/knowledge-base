<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Towards a Theoretical Foundation of Policy Optimization for Learning Control Policies

Topics include Reinforcement learning, Stability analysis, Robustness, Sample complexity, Optimization, Control, Learning, Linear quadratic regulator, Linear quadratic Gaussian, Control theory.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Gradient-based methods have been widely used for system design and optimization in diverse application domains. Recently, there has been a renewed interest in studying theoretical properties of these methods in the context of control and reinforcement learning. This article surveys some of the recent developments on policy optimization, a gradient-based iterative approach for feedback control synthesis, popularized by successes of reinforcement learning. We take an interdisciplinary perspective in our exposition that connects control theory, reinforcement learning, and large-scale optimization. We review a number of recently-developed theoretical results on the optimization landscape, global convergence, and sample complexity of gradient-based methods for various continuous control problems such as the linear quadratic regulator (LQR), H_infinity control, risk-sensitive control, linear quadratic Gaussian (LQG) control, and output feedback synthesis. In conjunction with these optimization results, we also discuss how direct policy optimization handles stability and robustness concerns in learning-based control, two main desiderata in control engineering. We conclude the survey by pointing out several challenges and opportunities at the intersection of learning and control.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reinforcement learning (RL) has recently shown an impressive performance on a wide range of applications, from playing Atari and mastering the game of Go, to complex robotic manipulations. Key to RL success is the algorithmic framework of policy optimization (PO), where the policy, mapping observations to actions, is parameterized and directly optimized upon to improve system-level performance. Mastering Go using PO (combined with techniques such as efficient tree-search) is particularly encouraging,^11^1Go is considered a challenging game to master, partially as the number of its legal board positions is significantly larger than the number of atoms in the observable universe. as the main idea behind the latter is rather straightforward -- when learning has been formalized as minimizing a certain cost as a function of the policy, devise an iterative procedure on the policy to improve the objective.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

For example, in the policy gradient (PG) variant of PO, when learning is represented as minimizing a (differentiable) cost $J{(K)}$ over the policy $K$, the policy is improved upon via a gradient update of the form $K^{n + 1} = {K^{n} - {\alpha{\nabla J}{(K^{n})}}}$, for some step size $\alpha$ (also referred to as the learning rate) and data-driven evaluation of the cost gradient $\nabla J$ at each iterate $n$. In fact, PO provides an umbrella formalism for not only policy gradient (PG) methods, but also actor-critic, trust-region, proximal PO methods.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

More generally, PO provides a streamlined approach to learning-based system design. For example, PO gives a general-purpose paradigm for addressing complex nonlinear dynamics with user-specified cost functions: for tasks involving nonlinear dynamics and complex design objectives, one can parameterize the policy as a neural network to be "trained" using gradient-based methods to obtain a reasonable solution. The PO perspective can also be adopted for other insufficiently parameterized decision problems such as end-to-end perception-based control. In this setting, it might be desired to synthesize a policy directly on images. As such, one can envision parameterizing a mapping from pixels (observation) to actions (decisions) as a neural network, and learn the corresponding policy using the PO formalism. Lastly, we mention the use of scalable gradient-based algorithms to efficiently train nonlinear policies on many parameters, making PO suitable for high-dimensional tasks. Computational flexibility and conceptual accessibility of PO have made it a main workhorse for modern RL.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In yet another decision theoretic science, PO has a long history in control theory; in fact, it has been popular among control practitioners when the system model is poorly understood or parameterized. Nevertheless, despite its generality and flexibility, PO formulation of control synthesis is typically nonconvex and as such, challenging for obtaining strong performance certificates, rendering it unpopular amongst system theorists. Since the 1980's, convex reformulations or relaxations of control problems have become popular due to the development of convex programming and related global convergence theory. It has been realized that many problems in optimal and robust control can be reformulated as convex programs, namely, semidefinite programs (SDP), or relaxed via sum-of-squares (SOS), expressed in terms of "certificates," e.g., matrix inequalities that represent Lyapunov or dissipativity conditions. However, these formulations have limitations when there is deviation from the canonical synthesis problems, e.g., when there are constraints on the structure of the desired control/policy. When convex reformulations are not available, PO assumes an important role as the main viable option.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Examples of such scenarios include static output feedback problem, structured $\mathcal{H}_{\infty}$ synthesis, and distributed control, all of significant importance in applications. The PO framework is more flexible, as evidenced by the recent advances in deep RL. PO is also more scalable for high-dimensional problems as it does not generally introduce extra variables in the optimization problems and enjoys a broader range of optimization methods as compared with the SDP or SOS formulations. However, as pointed out previously, nonconvexity of the PO formulation, even on relatively simple linear control problems, have made deriving theoretical guarantees for direct policy optimization challenging, preventing the acceptance of PO as a mainstream control design tool.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this survey, our aim is to revisit these issues from a modern optimization perspective, and provide a unified perspective on the recently-developed global convergence/complexity theory for PO in the context of control synthesis. Recent theoretical results on PO for particular classes of control synthesis problems, some of which are discussed in this survey, are not only exciting, but also lead to a new research thrust at the interface of control theory and machine learning. This survey includes control synthesis related to linear quadratic regulator theory, stabilization, linear robust/risk-sensitive control, Markov jump linear quadratic control, Lur'e system control, output feedback control, and dynamic filtering. Surprisingly, some of these strong global convergence results for PO have been obtained in the absence of convexity in the design objective and/or the underlying feasible set.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

These global convergence guarantees have a number of implications for learning and control. Firstly, these results facilitate examining other classes of synthesis problems in the same general framework. As it will be pointed out in this survey, there is an elegant geometry at play between certificates and controllers in the synthesis process, with immediate algorithmic implications. Secondly, the theoretical developments in PO have created a renewed interest in the control community to examine synthesis of dynamic systems from a complementary perspective, that in our view, is more integrated with learning in general, and RL in particular. This will complement and strengthen the existing connections between RL and control. Lastly, the geometric analysis of PO-inspired algorithms may shed light on issues in state-of-the-art policy-based RL, critical for deriving guarantees for any subsequent RL-based synthesis procedure for dynamic systems.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

This survey is organized to reflect our perspective -- and our excitement -- on how PO (and in particular PG) methods provide a streamlined approach for system synthesis, and build a bridge between control and learning. First, we provide the PO formulations for various control problems in §2. Then we delve into the PO convergence theory on the classic linear quadratic regulator (LQR) problem in §3. As it turns out, a key ingredient for analyzing LQR PO hinges on coerciveness of the cost function and its gradient dominance property (see §3.2). These properties can then be utilized to devise gradient updates ensuring stabilizing feedback policies at each iteration, and convergence to the globally optimal policy. In §3.3 we highlight some of the challenges in extending the LQR PO theory to other classes of problems, including the role of coerciveness, gradient dominance, smoothness, and the landscape of the optimization problem. The PO perspective is then extended to more elaborate synthesis problems such as linear robust/risk-sensitive control, dynamic games, and nonsmooth $\mathcal{H}_{\infty}$ state-feedback synthesis in §4.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Through these extensions, we highlight how variations on the general theme set by the LQR PO theory can be adopted to address lack of coerciveness or nonsmoothness of the objective in these problems while ensuring the convergence of the iterates to solutions of interest. This is then followed by examining PO for control synthesis with partial observations, and in particular, PO theory for linear quadratic Gaussian and output feedback in §5. Our discussion in §5 underscores the importance of the underlying geometry of the policy landscape in developing any PO-based algorithms. Fundamental connections between PO theory and convex parameterization in control are discussed in §6. In particular, it is shown how the geometry of policies and certificates are intertwined through appropriately constructed maps between nonconvex PO formulation of the synthesis problems and the (convex) semidefinite programming parameterizations. This provides a unified approach for analyzing PO in various control problems studied on a case-by-case basis so far.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

In §7, we present current challenges and our outlook for a comprehensive PO theory for synthesizing dynamical systems that ensures stability, robustness, safety, and optimality; and underscore the challenges in addressing synthesis problems in the face of partial observations, nonlinearities, and for multiagent settings. §7 also examines further connections between PO theory and machine learning, and highlights the possibility of integrating model-based and model-free methods to achieve the best of both worlds, illustrating how the main theme of this survey fits within the big picture of learning-based control.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Policy Optimization for Linear Control: Formulation", "weight": 1.0} -->

Control design can generally be formulated as a policy optimization problem of the form,

<!-- chunk {"id": "body-0014", "role": "body", "section": "Policy Optimization for Linear Control: Formulation", "weight": 1.0} -->

where the decision variable $K$ is determined by the controller parameterization (e.g., linear mapping, polynomials, kernels, neural networks, etc.), the cost function $J{(K)}$ is some task-dependent control performance measure (e.g., tracking errors, closed-loop $\mathcal{H}_{2}$ or $\mathcal{H}_{\infty}$ norm, etc.), and the feasible set $\mathcal{K}$ represents the class of controllers of interest, for example, ensuring closed loop stability/robustness requirements. Such a PO formulation is general, and enables flexible policy parameterizations. For example, consider a modern deep RL setting where one wants to design a policy maximizing some task-dependent reward function for a complicated nonlinear system $x_{t + 1} = {f{(x_{t},u_{t},w_{t})}}$ with $(x_{t},u_{t},w_{t})$ being the state, action, and disturbance triplet.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Policy Optimization for Linear Control: Formulation", "weight": 1.0} -->

PO has served as the main workhorse for addressing such tasks. Specifically, one just needs to parameterize the policy $K$ as a (deep) neural network and then apply iterative PO algorithms such as trust-region policy optimization (TRPO) and proximal policy optimization (PPO) to learn the optimal weights.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Policy Optimization for Linear Control: Formulation", "weight": 1.0} -->

The focus of this survey article is the recently-developed (global) convergence, complexity, and landscape theory of PO on classic control tasks including LQR, risk-sensitive/robust control, and output feedback control. In this section, we formulate these linear control problems as PO via properly selecting $(K,J,\mathcal{K})$ in Equation 1.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Policy Optimization for Linear Control: Formulation", "weight": 1.0} -->

Case I: Linear quadratic regulator (LQR). There are several ways to formulate the LQR problem. For simplicity, we start by considering a discrete-time linear time-invariant (LTI) system $x_{t + 1} = {{Ax_{t}} + {Bu_{t}}}$, where $x_{t}$ is the state and $u_{t}$ is the control action. The design objective is to choose the control actions $\{ u_{t}\}$ to minimize a quadratic cost function $J:={{\mathbb{E}}_{x_{0} \sim \mathcal{D}}{\sum_{t = 0}^{\infty}\left( {{x_{t}^{\mathsf{T}}Qx_{t}} + {u_{t}^{\mathsf{T}}Ru_{t}}} \right)}}$ with $Q \succeq 0$ and $R \succ 0$ being pre-selected cost weighting matrices.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Policy Optimization for Linear Control: Formulation", "weight": 1.0} -->

In this setting, the only randomness stems from the initial condition $x_{0}$, which is sampled from a certain distribution $\mathcal{D}$ with a full rank covariance matrix. It is well known that under some standard stabilizability and detectability assumptions the optimal cost is finite and can be achieved by a linear state-feedback controller of the form $u_{t} = {- {Kx_{t}}}$. Therefore, we can formulate the LQR problem as a special case of the PO problem as in Equation 1. Specifically, the decision variable $K$ is simply the feedback gain matrix.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Policy Optimization for Linear Control: Formulation", "weight": 1.0} -->

The above cost $J{(K)}$ is only well defined when the closed-loop system matrix $({A - {BK}})$ is Schur stable, i.e., when the spectral radius satisfies ${\rho{({A - {BK}})}} < 1$. Therefore, one can define the feasible set $\mathcal{K}$ as,

<!-- chunk {"id": "body-0020", "role": "body", "section": "Policy Optimization for Linear Control: Formulation", "weight": 1.0} -->

Now we can see that the LQR problem is a special case of the PO problem in Equation 1. There are several other slightly different ways to formulate the LQR problem. In an alternative formulation, we can add stochastic process noise and consider the LTI system,

<!-- chunk {"id": "body-0021", "role": "body", "section": "Policy Optimization for Linear Control: Formulation", "weight": 1.0} -->

where the disturbance $\{ w_{t}\}$ is a zero-mean i.i.d. process with a full rank covariance matrix $W$. The design objective is then to choose $\{ u_{t}\}$ to minimize the time-average cost

<!-- chunk {"id": "body-0022", "role": "body", "section": "Policy Optimization for Linear Control: Formulation", "weight": 1.0} -->

where $Q \succeq 0$ and $R \succ 0$ are pre-selected weighting matrices. Again, it suffices to parameterize the policy as $u_{t} = {- {Kx_{t}}}$. For a fixed policy $K$, the cost in Equation 5 can be computed as ${J{(K)}} = {\operatorname{Tr}{({P_{K}W})}}$, where $P_{K}$ is the solution for Equation 2. Again, the cost is well defined only for $K$ satisfying ${\rho{({A - {BK}})}} < 1$. This setting leads to almost the same PO formulation as before. Similarly, discounted LQR can be formulated as PO.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Policy Optimization for Linear Control: Formulation", "weight": 1.0} -->

Case II: Linear risk-sensitive/robust control. One can enforce risk-sensitivity and robustness via the formulation of linear exponential quadratic Gaussian (LEQG) or $\mathcal{H}_{\infty}$ control, respectively. For linear risk-sensitive control, we still consider the LTI system as in Equation 4 with $w_{t} \sim {\mathcal{N}{(0,W)}}$ being an i.i.d. Gaussian noise, and the design objective is to choose control actions $\{ u_{t}\}$ to minimize an exponentiated quadratic cost,

<!-- chunk {"id": "body-0024", "role": "body", "section": "Policy Optimization for Linear Control: Formulation", "weight": 1.0} -->

where $\beta$ is the parameter quantifying the intensity of risk-sensitivity, and the expectation is taken over the distribution for $x_{0}$ and $w_{t}$ for all $t \geq 0$. One typically chooses $\beta > 0$ to make the control "risk-averse." As $\beta\rightarrow 0$, the objective in Equation 6 reduces to the LQR cost. The above LEQG problem is also a special case of the PO problem as in Equation 1. It is known that the optimal cost can be achieved by a linear state-feedback controller. Again, one can just parameterize the controller as $u_{t} = {- {Kx_{t}}}$, where the gain matrix $K$ is the decision variable.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Policy Optimization for Linear Control: Formulation", "weight": 1.0} -->

Notice that in this case $J$ is well defined only when $K$ is in the following feasible set,

<!-- chunk {"id": "body-0026", "role": "body", "section": "Policy Optimization for Linear Control: Formulation", "weight": 1.0} -->

Importantly, the LEQG problem can be viewed as a special case of the more general mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design problem studied in robust control. In this survey article, we will cover two important robust control settings, namely the mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design and the $\mathcal{H}_{\infty}$ state-feedback synthesis.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Policy Optimization for Linear Control: Formulation", "weight": 1.0} -->

It is standard to assume ${E^{\mathsf{T}}{\lbrack{CE}\rbrack}} = {\lbrack{0R}\rbrack}$ for some $R \succ 0$. The mixed design objective is to synthesize a linear state-feedback controller that minimizes an upper bound on the $\mathcal{H}_{2}$ cost and satisfies an additional $\mathcal{H}_{\infty}$-robustness requirement on the channel from $w_{t}$ to $z_{t}$. The $\mathcal{H}_{\infty}$ constraint is posed explicitly and is powerful in guaranteeing robust stability in the presence of any small gain type of uncertainty, including being time-varying, dynamic, or nonlinear. For the mixed design problem, the robustness constraint is directly enforced on $K$, and hence the feasible set $\mathcal{K}$ is modified as,

<!-- chunk {"id": "body-0028", "role": "body", "section": "Policy Optimization for Linear Control: Formulation", "weight": 1.0} -->

where $\gamma$ quantifies the robustness level. The smaller $\gamma$ is, the more robust the system is in the $\mathcal{H}_{\infty}$ sense (since it can tolerate the small gain uncertainty at the level $\frac{1}{\gamma}$ by the Small Gain Theorem). There exist several objective functions that upper-bound the $\mathcal{H}_{2}$ cost, and a common one is ${J{(K)}} = {\operatorname{Tr}{({P_{K}DD^{\mathsf{T}}})}}$, where $P_{K}$ is the solution to the above Riccati equation with $Q = {C^{\mathsf{T}}C}$, $\gamma = {1/\sqrt{\beta}}$, $W = {DD^{\mathsf{T}}}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Policy Optimization for Linear Control: Formulation", "weight": 1.0} -->

Notice that the mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control aims at improving the average $\mathcal{H}_{2}$ performance while "maintaining" a certain level of robustness by keeping the closed-loop $\mathcal{H}_{\infty}$ norm to be smaller than a pre-specified number. In contrast, the $\mathcal{H}_{\infty}$ state-feedback synthesis aims at "improving" the system robustness and the worst-case performance via achieving the smallest closed-loop $\mathcal{H}_{\infty}$ norm. For simplicity, consider the LTI system $x_{t + 1} = {{Ax_{t}} + {Bu_{t}} + w_{t}}$ initialized at $x_{0} = 0$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Policy Optimization for Linear Control: Formulation", "weight": 1.0} -->

The reason is that the above cost actually satisfies

<!-- chunk {"id": "body-0031", "role": "body", "section": "Policy Optimization for Linear Control: Formulation", "weight": 1.0} -->

The above cost is well defined only for $K$ satisfying ${\rho{({A - {BK}})}} < 1$. Therefore, minimizing the $\mathcal{H}_{\infty}$ cost function defined by Equation 10 over $\mathcal{K}$ given by Equation 3 leads to a policy that minimizes the quadratic cost under the worst-case $\ell_{2}$ disturbance.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Policy Optimization for Linear Control: Formulation", "weight": 1.0} -->

Case III: Linear quadratic Gaussian (LQG) and output feedback control.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Policy Optimization for Linear Control: Formulation", "weight": 1.0} -->

Here, $w_{t}$ and $v_{t}$ are zero-mean white Gaussian noises with covariance matrices $W \succeq 0$ and $V \succ 0$. At step $t$, one can only observe $y_{t}$, and the state $x_{t}$ is not directly measured. The design objective is to choose actions $\{ u_{t}\}$ to minimize the time-averaged cost defined in Equation 5 given such partial observation information. Again, $Q \succeq 0$ and $R \succ 0$ are pre-selected weighting matrices. It is assumed that the pairs $(A,B)$ and $(A,W^{1/2})$ are controllable, and $(C,A)$ and $(Q^{1/2},A)$ are observable. This problem can also be formulated as a special case of the PO formulation given by Equation 1. Under our assumptions, it suffices to consider (full-order) dynamic controllers of the form,

<!-- chunk {"id": "body-0034", "role": "body", "section": "Policy Optimization for Linear Control: Formulation", "weight": 1.0} -->

where $\xi_{t}$ is the internal state of the controller and has the same dimension as $x_{t}$. For convenience, we encode the dynamic controller as,

<!-- chunk {"id": "body-0035", "role": "body", "section": "Policy Optimization for Linear Control: Formulation", "weight": 1.0} -->

The cost function $J{(K)}$ is well defined when the closed-loop system is stable, and hence, the feasible set should be specified as,

<!-- chunk {"id": "body-0036", "role": "body", "section": "Policy Optimization for Linear Control: Formulation", "weight": 1.0} -->

For any $K \in \mathcal{K}$, the cost $J{(K)}$ can be represented as,

<!-- chunk {"id": "body-0037", "role": "body", "section": "Policy Optimization for Linear Control: Formulation", "weight": 1.0} -->

where $X_{K}$ and $Y_{K}$ are the unique PSD solutions to the following Lyapunov equations,

<!-- chunk {"id": "body-0038", "role": "body", "section": "Policy Optimization for Linear Control: Formulation", "weight": 1.0} -->

Thereby, the LQG design problem can be formulated as a special case of PO. It is possible to use other control parameterizations and enforce more structures on $K$. This will lead to PO formulations for general output feedback control. Such formulations are particularly useful for decentralized control.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Policy Optimization for Linear Control: Formulation", "weight": 1.0} -->

For all three cases, the PO formulation is nonconvex in the policy space. This is in contrast to convex reformulations of these problems. Next, we will review the recently-developed PO theory for Cases I, II, and III in Sections 3, 4, and 5, respectively.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Case I: Global Convergence and Complexity of PO for LQR", "weight": 1.0} -->

LQR provides arguably the most fundamental optimal control formulation. A main challenge for the PO formulation of LQR is that the stability constraints are nonconvex in the policy space. The global convergence and complexity of PO methods on LQR have not been established until very recently. We review such results in this section.

<!-- chunk {"id": "body-0041", "role": "body", "section": "PO Theory for LQR", "weight": 1.0} -->

There are multiple ways to show the global convergence/complexity of the gradient descent method on the LQR problem. In this section, we review one proof which is based on Theorem 1. Interestingly, the LQR cost is coercive, real analytic, and gradient dominant so that Theorem 1 can be directly applied, though the problem is nonconvex in the parameter $K$. Recall that the LQR cost can be computed as ${J{(K)}} = {\operatorname{Tr}{({P_{K}\Sigma_{0}})}}$, where $\Sigma_{0} = {{\mathbb{E}}x_{0}x_{0}^{\mathsf{T}}}$ and $P_{K}$ satisfies ${{{({A - {BK}})}^{\mathsf{T}}P_{K}{({A - {BK}})}} + Q + {K^{\mathsf{T}}RK}} = P_{K}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "PO Theory for LQR", "weight": 1.0} -->

For simplicity, we assume here that $Q \succ 0$, following ^44^4The results can be generalized to the cases where $Q \succeq 0$ and even $Q$ being indefinite.. The following result holds.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Technical Challenges for Settings Beyond LQR", "weight": 1.0} -->

The global convergence of PO for LQR heavily relies on several important properties of the cost function and feasible set. We summarize the importance of these properties as follows.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Technical Challenges for Settings Beyond LQR", "weight": 1.0} -->

Coerciveness of cost. A key factor to the results for LQR is the coerciveness of the objective, as stated in Lemma 1. Coerciveness ensures that as long as the cost function value decreases, the controller $K^{n}$ remains stabilizing, i.e., feasible. Furthermore, coerciveness ensures that the sublevel sets of the cost function are compact, which, together with the real analytical property of the cost, implies that the gradient of the cost is globally Lipschitz over any finite level set, i.e., the cost is globally smooth over its sublevel sets. This smoothness property serves as one of the pillars in nonconvex optimization analysis, in determining the stepsize that sufficiently decreases the cost, see e.g.,. The coercive property makes the cost function a valid barrier function that explicitly regularizes the iterates to be feasible along the iterations. However, the cost is not necessarily coercive for other control problems, and only decreasing the cost value thus may no longer ensure the feasibility of the iterates.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Technical Challenges for Settings Beyond LQR", "weight": 1.0} -->

Gradient dominance (PL property) of cost. Convergence to the global minimum of policy gradient methods for LQR, especially with linear convergence rate, relies heavily on the benign landscape property of gradient dominance (cf. Lemma 1). Together with the smoothness of the objective, the gradient dominance property (of degree $2$, see Definition 1. ‣ 3.1 Background: Optimization and Complexity ‣ 3 Case I: Global Convergence and Complexity of PO for LQR ‣ Towards a Theoretical Foundation of Policy Optimization for Learning Control Policies")) naturally leads to global convergence rate that can be linear. This benign property is a blessing for certain control problems (see §6), and does not necessarily hold in general.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Technical Challenges for Settings Beyond LQR", "weight": 1.0} -->

Smoothness of cost. Sometimes the cost may not be differentiable over the entire feasible set. For example, for optimal $\mathcal{H}_{\infty}$ control, the cost function can be non-differentiable at stationary points. The lack of smoothness causes difficulty for such PO problems.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Technical Challenges for Settings Beyond LQR", "weight": 1.0} -->

Connectivity of feasible set. Another key to the success of PO for LQR, as a local search approach, is that the feasible set, though nonconvex in general, is connected. This is important since local search algorithms typically cannot jump between connected components, and a single connected component has to include the global optimum. Unfortunately, such connectivity is lost when extending PO to partially observable control systems, imposing additional challenges in establishing global convergence.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Technical Challenges for Settings Beyond LQR", "weight": 1.0} -->

Next, we study several control problems where some (if not all) of these desired properties are lacking, and more careful and advanced analyses are needed in order to obtain global convergence guarantees for PO methods.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Case II: PO for Risk-Sensitive & Robust Control", "weight": 1.0} -->

In this section, we review the global convergence results of PO methods on the mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control problem and the state-feedback $\mathcal{H}_{\infty}$ optimal control problem. For the mixed design problem, the main issue is the lack of coerciveness, i.e., the cost function close to the boundary of the feasible set may not approach infinity. For the $\mathcal{H}_{\infty}$ synthesis problem, the main difficulty is the lack of smoothness, i.e., the cost function may be non-differentiable over some important points in the feasible set. We will discuss how to modify PO algorithms to mitigate these issues and achieve global convergence provably. It is worth emphasizing that the idea of applying RL methods to solve $\mathcal{H}_{\infty}$ control is not new. This section mainly focuses on the recently-developed global convergence theory for PO methods on such robust control tasks.

<!-- chunk {"id": "body-0050", "role": "body", "section": "PO for Mixed $\\mathcal{H}_{2}/\\mathcal{H}_{\\infty}$ Design: Implicit Regularization", "weight": 1.0} -->

Recall the formulation of linear risk-sensitive and mixed design problems in Case II in §2. For simplicity, we use one common objective of the problem, and restate it as follows

<!-- chunk {"id": "body-0051", "role": "body", "section": "PO for Mixed $\\mathcal{H}_{2}/\\mathcal{H}_{\\infty}$ Design: Implicit Regularization", "weight": 1.0} -->

The above cost function $J{(K)}$ is known to be differentiable over the feasible set. One may wonder whether the analysis for the LQR case can be tailored to establish the global convergence of the gradient descent method on the above mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design problem. However, the following lemma reveals the less desired landscape properties of the cost function.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Algorithms", "weight": 1.0} -->

For ease of exposition, we introduce the following notation

<!-- chunk {"id": "body-0053", "role": "body", "section": "Algorithms", "weight": 1.0} -->

where $\eta > 0$ is the stepsize. The updates resemble the policy optimization updates for LQR as discussed in §3.2, but with $P_{K}$ therein replaced by ${\overset{\sim}{P}}_{K}$. The natural PG update is related to the gradient over a Riemannian manifold; while the Gauss-Newton update can be viewed as a special case of the quasi-Newton update.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Global Convergence Guarantees", "weight": 1.0} -->

The natural PG and Gauss-Newton updates in Equations 28-29 enjoy the implicit regularization property formalized as below.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Model-Free Implementations: Connections to Dynamic Games and Adversarial RL", "weight": 1.0} -->

There is a fundamental connection between mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control and linear quadratic dynamic games. This connection will not only allow us to implement the PO algorithms using model-free adversarial RL techniques, but also enable the development of PO methods for solving these dynamic games.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Model-Free Implementations: Connections to Dynamic Games and Adversarial RL", "weight": 1.0} -->

As LQR can be viewed as the benchmark for single-agent RL in continuous space, linear quadratic (LQ) dynamic games serve as the benchmark for studying multi-agent RL. Indeed, zero-sum LQ games have been investigated as a fundamental settings in multi-agent RL. Specifically, consider a zero-sum dynamic game with linear dynamics $x_{t + 1} = {{Ax_{t}} + {Bu_{t}} + {Dw_{t}}}$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Model-Free Implementations: Connections to Dynamic Games and Adversarial RL", "weight": 1.0} -->

It is known that the Nash equilibrium (NE), the solution concept for the problem, can be achieved with state-feedback policy classes, i.e., there exists a pair $(K^{\ast},L^{\ast})$, such that the NE satisfies $u_{t}^{\ast} = {- {K^{\ast}x_{t}}}$ and $v_{t}^{\ast} = {- {L^{\ast}x_{t}}}$. Hence, one can parameterize the controllers using matrices $(K,L)$, and solve for ${\min_{K}{\max_{L}\mathcal{C}}}{(K,L)}$, where $\mathcal{C}$ is the accumulated cost under this pair $(K,L)$. This leads to a multi-agent PO problem.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Model-Free Implementations: Connections to Dynamic Games and Adversarial RL", "weight": 1.0} -->

Intriguingly, the NE to the game is provided by the solution to a specific mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control problem. With this connection, the natural PG and Gauss-Newton methods in Equation 28 and Equation 29 can be equivalently transformed into provably convergent double-loop PO algorithms for the above LQ game. Related algorithmic developments have been documented. The game formulation for mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control is powerful in that these double-loop variants of the natural PG and Gauss-Newton methods can be implemented in a model-free manner. See for detailed discussions on model-free implementations and related sample complexity results.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Model-Free Implementations: Connections to Dynamic Games and Adversarial RL", "weight": 1.0} -->

An important issue in RL is the simulation-to-real gap. One common remedy is to use robust adversarial RL (RARL) algorithms which jointly learn a *protagonist* and an *adversary*, where the former learns to robustly perform the control tasks under the disturbances created by the latter. Policy-based RARL methods can be viewed as model-free variants of multi-agent PO methods for dynamic games. Therefore, the PO theory for mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control can also be applied to study the properties of RARL algorithms in the LQ setting. See for more details about this connection and results.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Model-Free Implementations: Connections to Dynamic Games and Adversarial RL", "weight": 1.0} -->

Indefinite LQR. The inner-loop subroutine in both zero-sum dynamic games and RARL reduces to a generalized LQR problem whose state cost matrix $Q$ is not positive semi-definite. The formulation of indefinite LQR is similar to that in §2, except that the $Q$ and $R$ matrices are symmetric but indefinite. Then the cost may not be coercive, and the descent of the cost does not ensure the stability of the iterates. Nevertheless, global convergence of policy optimization methods can be established; see.

<!-- chunk {"id": "body-0061", "role": "body", "section": "PO for $\\mathcal{H}_{\\infty}$ State-Feedback Synthesis: Nonsmoothness and Convergence", "weight": 1.0} -->

In this section, we consider the state-feedback $\mathcal{H}_{\infty}$ optimal control problem. Classical convex approaches for this task requires reparameterizing the problem into a higher-dimensional convex domain. In contrast, we view this problem as a benchmark of PO for robust control. We will discuss how to provably find the optimal $\mathcal{H}_{\infty}$ controller in the policy space directly. Recall that for the PO formulation of $\mathcal{H}_{\infty}$ state-feedback synthesis, the cost function $J{(K)}$ is given by Equation 10, and the feasible set $\mathcal{K}$ is specified by Equation 3. A main technical challenge here is that this $\mathcal{H}_{\infty}$ cost can be non-differentiable at some important feasible points, e.g., the optimal points. From Equation 10, we can see that this cost function is subject to two sources of nonsmoothness.

<!-- chunk {"id": "body-0062", "role": "body", "section": "PO for $\\mathcal{H}_{\\infty}$ State-Feedback Synthesis: Nonsmoothness and Convergence", "weight": 1.0} -->

Namely, the largest eigenvalue for a fixed frequency $\omega$ is nonsmooth, and the optimization step over $\omega \in {\lbrack 0,{2\pi}\rbrack}$ is also nonsmooth. We also know that the feasible set from Equation 3 is nonconvex. Hence, the resultant PO problem for $\mathcal{H}_{\infty}$ state-feedback synthesis is nonconvex nonsmooth. There has been a large family of nonsmooth $\mathcal{H}_{\infty}$ policy search algorithms developed based on the concept of Clarke subdifferential. However, the global convergence theory of PO methods on the $\mathcal{H}_{\infty}$ state-feedback synthesis has not been established until very recently. Next, we review such global convergence results.

<!-- chunk {"id": "body-0063", "role": "body", "section": "PO for $\\mathcal{H}_{\\infty}$ State-Feedback Synthesis: Nonsmoothness and Convergence", "weight": 1.0} -->

First, we introduce a few concepts related to subdifferential of nonconvex functions. A function $J:{\mathcal{K}\rightarrow{\mathbb{R}}}$ is locally Lipschitz if for any bounded $S \subset \mathcal{K}$, there exists a constant $L > 0$ such that ${|{{J{(K)}} - {J{(K^{\prime})}}}|} \leq {L{\parallel{K - K^{\prime}}\parallel}_{F}}$ for all ${K,K^{\prime}} \in S$. Based on Rademacher's theorem, a locally Lipschitz function is differentiable almost everywhere, and the Clarke subdifferential is well defined for all feasible points.

<!-- chunk {"id": "body-0064", "role": "body", "section": "PO for $\\mathcal{H}_{\\infty}$ State-Feedback Synthesis: Nonsmoothness and Convergence", "weight": 1.0} -->

We define the Clarke subdifferential as ${\partial_{C}{J{(K)}}}:={\operatorname{conv}{\{{{\lim_{i\rightarrow\infty}{{\nabla J}{(K_{i})}}}:{{K_{i}\rightarrow K},{K_{i} \in {\operatorname{dom}{({\nabla J})}} \subset \mathcal{K}}}}\}}}$, where $\operatorname{conv}$ denotes the convex hull. For any given direction $V$ (which has the same dimension as $K$), the generalized Clarke directional derivative of $J$ is defined as

<!-- chunk {"id": "body-0065", "role": "body", "section": "PO for $\\mathcal{H}_{\\infty}$ State-Feedback Synthesis: Nonsmoothness and Convergence", "weight": 1.0} -->

In contrast, the (ordinary) directional derivative is defined as follows (when existing)

<!-- chunk {"id": "body-0066", "role": "body", "section": "PO for $\\mathcal{H}_{\\infty}$ State-Feedback Synthesis: Nonsmoothness and Convergence", "weight": 1.0} -->

In general, the Clarke directional derivative can be different from the (ordinary) directional derivative which may not even exist for some feasible points. The objective function $J{(K)}$ is subdifferentially regular if for every $K \in \mathcal{K}$, the ordinary directional derivative always exists and coincides with the generalized one for every direction, i.e., ${J^{\prime}{(K,V)}} = {J^{\circ}{(K,V)}}$. The following result holds for the $\mathcal{H}_{\infty}$ objective function.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Case III: PO with Partial Observations", "weight": 1.0} -->

In this section, we examine the more challenging case of control with partial observation. When the system's state is not directly measured, there is an intricate balance between the achievable control performance and the class of controllers used in PO. Depending on the policy parameterization, the optimization landscape can become quite different. We will first survey several recent results on the optimization landscape of PO for LQG, and then point out some of the subtle aspects for more general output feedback and structured synthesis problems.

<!-- chunk {"id": "body-0068", "role": "body", "section": "PO for Linear Quadratic Gaussian Control: Optimization Landscape", "weight": 1.0} -->

In order to characterize the performance of PO algorithms such as PG methods for LQG, it is necessary to understand the landscape of the associated PO formulation in Equation 1, with the cost function given in Equation 15 and the feasible set given in Equation 14. Following standard setup in the literature, we assume that the pairs $(A,B)$ and $(A,W^{1/2})$ are controllable, and $(C,A)$ and $(Q^{1/2},A)$ are observable. It has been shown that with these assumptions, the set of stabilizing controllers $\mathcal{K}$ is non-empty, open, unbounded, and can be nonconvex. Moreover, the cost function $J{(K)}$ is real analytic on the underlying set $\mathcal{K}$.

<!-- chunk {"id": "body-0069", "role": "body", "section": "PO for Linear Quadratic Gaussian Control: Optimization Landscape", "weight": 1.0} -->

However, beyond these properties, until recently little was known about the geometric and analytical properties of the PO formulation of LQG. We will mainly summarize results on the optimization landscape of LQG, especially with respect to the connectivity of the stabilizing set $\mathcal{K}$ and the structure of the stationary points. Several related extensions can be found. Before introducing the results, we discuss a special structure for LQG with state-space dynamical controller parameterization in Equation 11. It is known that the optimal feedback controller is unique in the frequency domain \[73, Theorem 14.7\]. However, in time domain, this controller is not unique: consider the similarity transformation for the state-space form of the controller and note that the two controller parameterizations,

<!-- chunk {"id": "body-0070", "role": "body", "section": "PO for Linear Quadratic Gaussian Control: Optimization Landscape", "weight": 1.0} -->

where $T$ is an invertible matrix, have identical input-output behavior regardless of the choice of $T$. Thus the cost is invariant with respect to this similarity transformation. Besides this invariance, when a controller $K$ is non-minimal, i.e., $(A_{K},B_{K})$ is not controllable or $(A_{K},C_{K})$ is not observable, one can use model reduction to remove the uncontrollable/unobservable modes while keeping the cost the same. We will now summarize the main results. First, we have the following theorem on the connectivity of $\mathcal{K}$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Output Feedback and Structured Control", "weight": 1.0} -->

We now shift our attention to another class of synthesis problems with partial observations, namely, output feedback and structured control. First, we like to point out that policy synthesis on partially available data (not necessary the underlying state) is of great interest in applications, particularly for large scale systems. For example, in decentralized control, stabilizing feedback with a particular sparsity pattern is desired; in the output feedback case, one aims to design a stabilizing policy that can be factored with its right multiplicand as the observation map. These problems can conveniently be formalized in form of Equation 1, where $\mathcal{K}$ becomes a subset of stabilizing (static or dynamic) feedback policies: for both output feedback and structured synthesis, $\mathcal{K}$ is a linearly constrained subset of stabilizing feedback gains. The PO perspective adopted in this survey then immediately offers an algorithm for these problems, namely, a projected first order update^88^8The projection is used to enforce sparsity/structure patterns. The projection does not involve stability/robustness concerns..

<!-- chunk {"id": "body-0072", "role": "body", "section": "Output Feedback and Structured Control", "weight": 1.0} -->

A natural question is whether such an intuitive generalization has any theoretical guarantees of convergence; the short answer, however, is negative. We now summarize some of our current understanding of why this is the case, intermingled with some more encouraging results.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Output Feedback and Structured Control", "weight": 1.0} -->

A major obstacle in guaranteeing convergence to the global optimum is due to the geometry of the corresponding set $\mathcal{K}$---and not only its non-convexity inherited from the set of stablizing controllers. Rather, due to the intricate geometry of this set, its intersection with linear subspaces can result in disconnected sets; an analogous phenomena in the case of LQG was examined in the previous section. This is a known fact from classic control in the context of output feedback and the method of root locus, where the (scalar) feedback gain can undergo intervals of being stabilizing or not; an example is shown in Figure 4(a).

<!-- chunk {"id": "body-0074", "role": "body", "section": "Output Feedback and Structured Control", "weight": 1.0} -->

However, it is surprising that the number of such connected components even for SISO (single-input single-output) systems was not explicitly characterized until recently. A policy optimization perspective on control synthesis only makes this observation more compelling.

<!-- chunk {"id": "body-0075", "role": "body", "section": "The Role of Convex Parameterization", "weight": 1.0} -->

There is a large body of literature on the reparameterization of various control problems to represent them as convex problems. In this section, we discuss the connections between such convex approaches and PO, showing LMI formulations for control design lead to desired landsacpe properties for PO.

<!-- chunk {"id": "body-0076", "role": "body", "section": "The Role of Convex Parameterization", "weight": 1.0} -->

We have seen successful application of PO to a range of control problems in the previous sections, in many cases achieving the *globally optimal* policy. A natural question is whether there is a unified approach to determining when stationary points for PO are global minima. In this section, we revisit the gradient dominance property given in Definition 1. ‣ 3.1 Background: Optimization and Complexity ‣ 3 Case I: Global Convergence and Complexity of PO for LQR ‣ Towards a Theoretical Foundation of Policy Optimization for Learning Control Policies"), and provide a unified framework to show some related inequality holds for a large family of PO problems, despite the nonconvexity of the cost $J{(K)}$ as a function of $K$. This viewpoint gives insights into the "mysterious" emergence of gradient dominance (or the PL property) in various control problems that are nonconvex in $K$, providing a general tool to determine when stationary points for nonconvex PO problems are actually global minimum.

<!-- chunk {"id": "body-0077", "role": "body", "section": "The Role of Convex Parameterization", "weight": 1.0} -->

Intuitively, the gradient dominance property implies that $J{(K)}$ is close to the optimal value for any $K$ with small gradient norm, from which one can directly conclude nice optimization landscape/convergence properties^99^9Convergence rates will depend on the values of the degree $p$, see for more properties. In particular $p = 1$ gives a sublinear convergence rate, and $p = 2$ gives a linear rate.. Our goal in this section is to show how to use the existence of convex parameterizations, together with important additional assumptions on the *map* between the variables in the nonconvex and convex problems, to conclude such a desired property or some closely-related variant for the nonconvex $J{(K)}$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "The Role of Convex Parameterization", "weight": 1.0} -->

We begin by considering an abstract description of the following pair of problems

<!-- chunk {"id": "body-0079", "role": "body", "section": "The Role of Convex Parameterization", "weight": 1.0} -->

where $\mathcal{K}$ describes the set of desired controllers (typically, stablizing set), and $\mathcal{S}$ captures the appropriate constraint sets (typically LMIs), which are determined for each problem case; see examples below. The following key assumption on the pair of problems in Equation 33 and Equation 34 is critical for Theorem 10.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The feasible set $\mathcal{S}$ is a convex set, and the function $f{(L,P,Z)}$ is convex, bounded, and differentiable over $\mathcal{S}$. Any feasible point ${(L,P,Z)} \in \mathcal{S}$ is assumed to satisfy $P \succ 0$. In addition, assume for all $K \in \mathcal{K}$, we can express $J{(K)}$ as follows^1010^10Note that this assumption needs to hold for all feasible points in the two domains, not only at the optima.,

<!-- chunk {"id": "body-0081", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Recall that $J^{\prime}{(K,V)}$ denotes the directional derivative of $J{(K)}$ along the direction $V$. When $J$ is differentiable, it holds that ${J^{\prime}{(K,V)}} = {{trace}{({V^{\mathsf{T}}{\nabla J}{(K)}})}}$. We have the following result (modified from to also allow non-differentiable points).

<!-- chunk {"id": "body-0082", "role": "body", "section": "Challenges and Outlook", "weight": 1.0} -->

In this article, we have revisited the theoretical foundation of PO for control, and surveyed a number of results that highlight properties of PO algorithms on benchmark control problems. Our survey has been inspired by recent success and wide range of applications of RL. PO provides a bridge between control and RL, and can give new insights into the design trade-offs between assumptions and data, as well as model-based and model-free synthesis. Theoretical development in PO for control can help create a renewed interest in the controls community to examine synthesis of dynamic systems from this perspective, that in our view, is more integrated with machine learning. We close our discussion with an outlook on challenges and open questions in bridging the gap between PO theory and real-world control applications. As an exhaustive list is impossible, we discuss a few challenges and open questions that naturally reflect our perspectives.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Challenges and Outlook", "weight": 1.0} -->

Further connections between optimization and control theory. From our discussion, it is evident that the development of PO theory requires further connections between modern optimization theory (that focuses on convergence and complexity of iterative algorithms) with control theory (that rigorously addresses the notions of optimality, stability, robustness, and safety for closed-loop dynamical systems). For example, it is natural to ask whether leveraging results in nonconvex optimization on the complexity of escaping saddle points, can give similar guarantees for PO with control-theoretic constraints.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Challenges and Outlook", "weight": 1.0} -->

Regularization for stability, robustness, and safety. In this article, we have covered only $\mathcal{H}_{\infty}$ robustness constraints. There is an extensive system theoretic literature on how to enforce other types of robustness and safety guarantees for control design. For example, more general robustness constraints can be formulated via passivity, dissipativity, or integral quadratic constraints. In addition, safety can also be induced by modifying the cost function. It is important to investigate how to provably pose similar robust/safety guarantees for direct policy search via either explicit regularization (on the cost/constraints) or implicit regularization (via algorithm selection).

<!-- chunk {"id": "body-0085", "role": "body", "section": "Challenges and Outlook", "weight": 1.0} -->

Nonlinear systems, deep RL, and perception-based control. We have focused on reviewing the PO theory centered around linear systems. It is our hope that the insights from such study can be used to guide the algorithmic/theoretical developments of PO methods for nonlinear control. Conceptually, nonlinear control design can still be formulated as ${\min_{K \in \mathcal{K}}J}{(K)}$, and convergence to stationary points can still be established given coerciveness. However, how to characterize the feasible set $\mathcal{K}$ in the nonlinear control setting is unclear in the first place. Quite often the stability/robustness constraints hold only locally for nonlinear systems. It is crucial to investigate how to define and characterize feasible policies for nonlinear control problems. An important class of PO problems arise in deep RL for end-to-end perception-based control. The theoretical properties of PO methods on such problems remain largely unknown. In this case, the geometry of the feasible set can become even more complicated due to the presence of the perception modality.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Challenges and Outlook", "weight": 1.0} -->

Multi-agent systems and decentralized control. Decentralized control of multi-agent systems has a long history in control theory and also connects to the partially observable setting since each single agent cannot observe the full system state. PO theory for such control tasks requires further investigation. There has been some recent progress. For example, showed that there can be exponential number of connected component for the feasible set; then established the global convergence and sample complexity under the quadratic invariance condition. It would be interesting to explore other conditions as well as algorithm design principles that admit global convergence of PO methods for decentralized control. It is especially imperative to develop PO methods that scale with a large number of agents. PO has also been studied under the multi-agent game-theoretic settings, including the general-sum LQ dynamic games, with negative non-convergence results, and in LQ mean-field games, where the number of agents is very large and approximated by infinity. It would be interesting to further explore the PO theory in other dynamic game settings with control implications.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Challenges and Outlook", "weight": 1.0} -->

Integration of model-based and model-free methods. Model-based and model-free methods are both important for control design. One one hand, there is a recent trend that examines the LQR problem as a benchmark for learning-based control, starting from the work, and it has been shown that model-based methods can be more sample-efficient in this case from an asymptotic viewpoint. On the other hand, model-free methods can be more flexible for complex tasks such as perception-based control. As such, it is an important future direction to investigate how to integrate model-free and model-based methods to achieve the best of both worlds, especially for controlling systems which are only partially understood or parameterized. It is also expected that such an integrated approach will lead to developments in new settings that further connect learning and control theory, e.g. online control with regret guarantees.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Challenges and Outlook", "weight": 1.0} -->

New PO formulations from ML. Many new tasks arising in machine learning for control can also be formulated as PO. For example, imitation learning for control can be formulated as PO with control-theoretic constraints. Similarly, transfer learning for linear control can be studied as PO if we modify the cost function properly. In the context of control, PO conveniently provides a general paradigm for formulating imitation learning and transfer learning tasks. It will be interesting to investigate the convergence theory of gradient-based algorithms for such problems.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Challenges and Outlook", "weight": 1.0} -->

Thanks to the coerciveness and gradient dominance properties, PO for LQR leads to a nonconvex problem which can still be solved using the gradient method provably.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Challenges and Outlook", "weight": 1.0} -->

In the state-feedback setting, advanced PO methods can be guaranteed to achieve global convergence on linear risk-sensitive/robust control tasks.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Challenges and Outlook", "weight": 1.0} -->

In the partial observation setting, optimization landscape provides important clues for performance of PO methods.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Challenges and Outlook", "weight": 1.0} -->

There are fundamental connections between the convex formulations of optimal/robust control tasks and the PO landscape.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Challenges and Outlook", "weight": 1.0} -->

Many new results on complexity of escaping saddles and finding stationary points for unconstrained optimization may be extended to PO.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Challenges and Outlook", "weight": 1.0} -->

Advanced regularization techniques are needed for robustness and safety in general.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Challenges and Outlook", "weight": 1.0} -->

PO theory for nonlinear or perception-based control remains largely open.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Challenges and Outlook", "weight": 1.0} -->

Scalability is an important issue for PO in multi-agent decentralized control.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Challenges and Outlook", "weight": 1.0} -->

More study is needed to integrate model-based and model-free methods.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Challenges and Outlook", "weight": 1.0} -->

There are new PO problems in ML for control (e.g., imitation/transfer learning).

<!-- chunk {"id": "body-0099", "role": "body", "section": "DISCLOSURE STATEMENT", "weight": 1.0} -->

The authors are not aware of any affiliations, memberships, funding, or financial holdings that might be perceived as affecting the objectivity of this review.
