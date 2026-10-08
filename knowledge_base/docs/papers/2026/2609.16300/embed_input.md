<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Policy Gradient over History-Dependent Policy Classes for LQR with Domain Randomization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Domain Randomization (DR) has been widely used to overcome the sim-to-real gap by training a controller on a distribution of simulated environments via reinforcement learning. While DR can achieve robust performance simply using controllers synthesized via policy gradient (PG) methods, the optimization landscape is not well understood, even in the case of linear quadratic regulator (LQR) objectives. To this end, we first study PG of domain randomized LQR over history-dependent policy classes, such as finite impulse response controllers, as they can extend the possibilities of simultaneous stabilization. Second, to find such a stabilizing controller, we propose a curriculum learning based algorithm which gradually expands the memory of the controller. Finally, we show that PG with the proposed algorithm converges globally to the minimizer of a sample average approximation of the DR objective under suitable bounds on the heterogeneity of environments. Empirical results support our findings and highlight promising directions for future work, including nonlinear domain-randomized control.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Domain randomization (DR) searches for a feedback control policy belonging to a policy class that minimizes a control objective on average over system parameters from a distribution. It is widely used in robot learning because the randomization introduces some robustness to the simulator parameters, thereby enabling sim-to-real transfer in various robotics applications such as manipulation and locomotion. At the same time, the DR policy can be trained by applying standard algorithms from deep reinforcement learning that update policy parameters using policy gradient (PG) methods. Such approaches are parallelizable and can be efficiently accelerated using GPUs.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite the utility of DR, it is not well understood how the choice of control objective, randomization distribution, and policy parameterization impact the efficacy of the resulting policy, and the convergence of policy search algorithms. present the first analysis of policy gradient for linear quadratic regulator (LQR) with domain randomization over the class of static controllers. However, even in simple examples, the static controller class is insufficient to find a common controller that stabilizes all the systems under the distribution, a property known as simultaneous stabilization. In this paper, we therefore extend the controller class to the history-dependent policies and study policy gradient for domain randomized LQR over this richer class. We highlight the analytical challenges arising from the history dependence of the controller and establish global convergence by introducing a reparameterized representation of the LQR objective.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Robust Control", "weight": 1.0} -->

The DR problem has previously been proposed in the robust control literature. It has also been known as stochastic robust control or average robust control, where the idea is to be robust against average-case uncertainty. In contrast, approaches like $\mathcal{H}_{\infty}$ control and $\mu$-synthesis provide robustness for the worst case. The scenario approach accounts for the worst case but reduces conservatism, drawing samples to provide probabilistic guarantees. Improvements in hardware efficiency have enabled the renewed use of gradient-based policy optimization in DR methods, making them practical even for complex nonlinear systems, where worst-case approaches might not scale well.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Dual and Adaptive Control", "weight": 1.0} -->

In this paper, we focus on history-dependent policy classes. If we allow arbitrary policies, then the DR problem becomes similar to the dual/adaptive control problem. Solving the dual control problem when the policy class consists of arbitrary history-dependent policies is generally intractable, motivating heuristic approaches based on certainty equivalent synthesis. Alternatively, we could consider reducing the complexity of the history-dependent policy class, which is the approach we follow in this paper. We focus on the class of linear, stationary, finite impulse response (FIR) policies.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Domain Randomization", "weight": 1.0} -->

DR was first used with neural network policies optimized via reinforcement learning in a simulator, who coined the name "Domain Randomization". It has since become the standard approach to encourage robustness in robotic policies trained with reinforcement learning in simulation. The sampling distribution may be a design variable in the synthesis problem, or come from a learning procedure, e.g. as the posterior distribution of a Bayesian identification procedure. Recent work has explored generalization of DR in discrete Markov Decision Processes and for continuous control. Convergence analysis of policy gradient methods for the LQR problem with domain randomization with static policy classes was presented. In this work, we extend the convergence analysis of to history-dependent FIR policies in an LQR setting. The use of history dependent policies parametrized by Recurrent Neural Networks such that the resulting policy is "adaptive" rather than just robust was introduced.

<!-- chunk {"id": "body-0008", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

We study the DR problem when the control objective is the LQR objective, and the policy class is the set of FIR linear policies of some order. In this setting: We show that policy gradient converges globally under a bounded heterogeneity assumption among systems over the distribution.

<!-- chunk {"id": "body-0009", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

We provide a curriculum learning approach that gradually expands the memory of the policy during the optimization procedure until satisfactory performance is achieved.

<!-- chunk {"id": "body-0010", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

We present illustrative examples indicating the benefits of FIR policies over static policies for simultaneous stabilization. We further compare the performance of FIR policies with other parameterizations of dynamic policy and show that FIR policies are not only more amenable to optimization, but also outperform other dynamic policies.

<!-- chunk {"id": "body-0011", "role": "body", "section": "I-B Contribution", "weight": 1.0} -->

Our work establishes a promising direction to leverage insights from robust control, adaptive control, and simultaneous stabilization to build a theoretical grounding for domain randomization which can inform policy parameterization and optimization procedures used in the practice of reinforcement learning for robotics.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We consider the DR problem in the LQR setting. In particular, suppose we have a fully observable linear time-invariant system of the form with a parameter $\theta\in\mathbb{R}^{d_{\theta}}$, state $x_{t}\in\mathbb{R}^{d_{\mathsf{X}}}$, control input $u_{t}\in\mathbb{R}^{d_{\mathsf{U}}}$, and disturbance $w_{t}\in\mathbb{R}^{d_{\mathsf{X}}}$ where $w_{t}\sim\mathcal{N}(0,W)$ is an i.i.d. Gaussian noise. We assume $W=I$.^11^ 1 Generalization to arbitrary noise covariance $\Sigma_{w}\succ 0$ may be achieved by a change of basis in state space, which transforms $A(\theta),B(\theta)$, and $Q$ accordingly.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

For fixed $\theta$, we define the control objective function as with $Q\succeq I$ and $R=I$. ^22^ 2 R=I can be enforced by a change of basis in input space The superscript $K$ indicates that the expectation is taken under control inputs generated by the feedback control policy $K\in\mathcal{K}$: the policy class we study is made precise in and Assumption III.2. ‣ III Global Convergence of Policy Gradient ‣ Policy Gradient over History-Dependent Policy Classes for LQR with Domain Randomization"). The goal of domain randomization (DR) is to find a controller that minimizes the expectation of the control objective over a distribution of system parameters $\theta$. Let $\Theta$ be a random variable with density $p_{\Theta}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Then, the *domain randomized LQR (DR-LQR) problem* is to solve: where we define $J_{\textnormal{{DR}}}(K)\coloneqq\E_{\Theta\sim p_{\Theta}}[J(K,\Theta)]$ as the *domain randomization (DR) objective*.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

To tackle this problem, we consider drawing $M$ independent parameter samples, $\theta_{1},\cdots,\theta_{M}\sim p_{\Theta}$, to construct an approximation of the DR objective: where we denote $J^{i}(K)\coloneqq J(K,\theta_{i})$ and each sample follows the dynamics $x_{t+1}=A^{i}x_{t}+B^{i}u_{t}+w_{t}$ with $A^{i}\coloneqq A(\theta_{i}),B^{i}\coloneqq B(\theta_{i})$. We define $J_{\textnormal{{SA}}}(K)$ as the *sample average (SA) objective*. To minimize the SA objective, we apply policy gradient (PG) methods to the control policy. In particular, starting from a controller $K^{}$, we iteratively update the controller as where $\alpha$ is a fixed stepsize.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Our prior work shows that, under a bounded heterogeneity condition, PG converges globally to the minimizer of when the policy class is the set of static feedback controllers, $u_{t}=K_{0}x_{t}$, that is, $\mathcal{K}=\{K_{0}\in\mathbb{R}^{d_{\mathsf{U}}\times d_{\mathsf{X}}}\}$. The limitation of using such a policy class for the DR-LQR problem is illustrated in the following example.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Example II.1", "weight": 1.0} -->

Consider the scalar system There does not exist a static linear feedback controller $u_{t}=kx_{t}$ that stabilizes both systems simultaneously. This can be shown by considering the closed-loop dynamics which is stable if and only if $|a+k|<1$. There does not exist $k$ that satisfies this condition for both systems simultaneously. On the other hand, a policy with one step of memory defined by $u_{t}=K_{0}x_{t}+K_{1}x_{t-1}$ with $K_{0}=0$ and $K_{1}=-0.21$ does simultaneously stabilize both systems.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Example II.1", "weight": 1.0} -->

The above example indicates that controllers with memory may attain a lower cost for the DR-LQR problem than static controllers. In some cases, such as in the above example, static controllers may fail to even achieve a finite cost, while controllers with memory can. Motivated by this, we consider the *Finite Impulse Response (FIR)* parameterization of the feedback controller. The use of other dynamic parameterizations is discussed in Section V-B. A FIR controller of order $H$ is defined as and $\xi_{t}$ is the augmented state containing information of the history length $H$. We define $x_{t}=0$ for $t\leq 0$ for initialization of the buffer. In the augmented state space, the dynamics can be written as and $\mathbb{A}_{K}^{i}\triangleq\mathbb{A}^{i}+\mathbb{B}^{i}K$. In the rest of the paper, we define the original system as the *non-lifted system* and the augmented system as the *lifted system*.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Example II.1", "weight": 1.0} -->

In the lifted system, the *FIR-LQR objective* is written as where we define the state covariance matrix $\Sigma_{K}^{i}$ and the value matrix $P_{K}^{i}$ as the solutions to the following Lyapunov equations: Consequently, \[25, Lemma 1\] tells us that the gradient of is given by We can therefore write the gradient of the SA objective as The goal of this paper is to study the convergence of PG over the class of FIR controllers to the optimal solution of the SA objective. To this end, we show that as long as the sampled systems satisfy a condition on bounded heterogeneity, PG converges to the global optimum starting from an initial stabilizing controller.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Global Convergence of Policy Gradient", "weight": 1.0} -->

Our main result proves the convergence of the PG over the FIR policy classes to the optimal solution of the SA objective. The result requires that the samples are close together, or have a small *heterogeneity gap*. To quantify the admissible gap, we use two scalars determined by the problem data: the model size bound $\tau_{B}\triangleq\max\{1,\sup_{\theta\in\mathcal{S}}\|B(\theta)\|\}$ and the optimal cost bound $\bar{J}_{\star}\triangleq\sup_{\theta\in\mathcal{S}}J(K(\theta),\theta)$, where $K(\theta)$ denotes the optimal FIR gain of system $\theta$ and $\mathcal{S}\subseteq\mathbb{R}^{d_{\theta}}$ is a compact support of $p_{\Theta}$. With these quantities, we assume that $\mathcal{S}$ is small enough that the model error is bounded.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption III.1 (Heterogeneity Assumption)", "weight": 1.0} -->

Since $\bar{\varepsilon}_{\textnormal{{het}}}$ is explicit, it is checkable on the problem data only and nontrivial because it holds whenever the support $\mathcal{S}$ is sufficiently small. Its role is to guarantee that the SA objective satisfies gradient domination, which is the key to global convergence. See Section III-B for further discussion.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption III.1 (Heterogeneity Assumption)", "weight": 1.0} -->

In addition, we impose an assumption on the initial controller.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption III.2 (Initial Stabilization)", "weight": 1.0} -->

The initial iterate $K^{}\in\mathcal{K}$ simultaneously stabilizes the sampled systems, where and its cost is within a factor of $8$ of the optimal Later, we introduce a method to obtain an initial stabilizing controller that ensures that this assumption is satisfied. See Remark III.2. ‣ III Global Convergence of Policy Gradient ‣ Policy Gradient over History-Dependent Policy Classes for LQR with Domain Randomization") for further discussion.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption III.2 (Initial Stabilization)", "weight": 1.0} -->

Now we introduce the main result of the paper. Under the above heterogeneity assumption and initial stabilization, PG under a suitable choice of stepsize converges globally to a minimizer of. Let $K^{\star}\coloneqq\argmin_{K\in\mathcal{K}}J_{SA}(K)$, and $K_{\zeta_{0}}\coloneqq\mathopen{}\left\{K\in\mathcal{K}:J_{\textnormal{{SA}}}(K)\leq\zeta_{0}\right\}\mathclose{}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark III.1 (Heterogeneity Assumption)", "weight": 1.0} -->

As stated in Assumption III.1. ‣ III Global Convergence of Policy Gradient ‣ Policy Gradient over History-Dependent Policy Classes for LQR with Domain Randomization"), we measure open-loop heterogeneity through the A and B matrices. Under this condition, the sampled systems are sufficiently close that a single controller performs well across all of them, which enables global convergence. This heterogeneity requirement might be conservative, as it excludes particular cases in which multiple systems can be simultaneously stabilized despite not being close in the sense of Assumption III.1. ‣ III Global Convergence of Policy Gradient ‣ Policy Gradient over History-Dependent Policy Classes for LQR with Domain Randomization"). We leave relaxing this condition or determining if it is fundamental to future work.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark III.2 (Initial Stabilization)", "weight": 1.0} -->

The above convergence guarantee requires that the PG iteration starts from an initial simultaneously stabilizing controller whose cost is within a factor of $8$ of the optimal solution. Consequently, the initial iterate must simultaneously stabilize all sampled systems (as long as such a simultaneously stabilizing controller exists). In Section IV, we present a scheme to find such an initial stabilizing controller.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark III.3 (Convergence of the DR Objective $J_{\\textnormal{{DR}}}(K)$)", "weight": 1.0} -->

The result ensures convergence to the optimal solution of. However, the original DR objective is. To address this discrepancy, concentration arguments can be applied to demonstrate convergence of the SA objective to its population counterpart as the number of sampled systems becomes sufficiently large. The argument of \[5, Thm. V.1\] is not specific to static policies, and extends to FIR policies.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark III.3 (Convergence of the DR Objective $J_{\\textnormal{{DR}}}(K)$)", "weight": 1.0} -->

Similarly to, the convergence proof consists of three parts: establishing coercivity and smoothness properties of the SA cost, showing that the property known as *gradient domination* holds under small heterogeneity, and combining and to show global convergence. We highlight that the analysis of is *insufficient* to prove these properties in the FIR-LQR setting because the LQR cost needs to be analyzed in the lifted state which has a more intricate landscape because of the history dependence of the controller $K$. In particular, the noise covariance and state penalties are singular in the lifted state space. In Section III-A, we show that the SA objective is coercive and smooth in the sub-level set of the cost. Section III-B establishes gradient domination with the explicit heterogeneity gap bound, and Section III-C combines the two results into global convergence. Full proofs are deferred to the appendix.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-A Coercivity and Smoothness of the Sample Average Objective", "weight": 1.0} -->

We first show that the SA objective is coercive and $L$-smooth. This will in turn be used to ensure convergence of PG in to a fixed point. Note that the LQR cost is known to be coercive and $L$-smooth over any sub-level set from \[26, Lemma 1\]. However, it is not obvious if the same property holds for the lifted LQR objective. To this end, we establish the following lemma.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B Gradient Domination of the Sample Average Objective", "weight": 1.0} -->

Gradient domination of the SA objective only holds when the heterogeneity gap is small. We can formalize this by applying the Lyapunov perturbation arguments developed. This requires that the LQR instances have a nondegenerate process noise, and a non-degenerate state cost. However, the lifted LQR parameterization no longer satisfies this property, as $\lambda_{\min}(\mathbb{W})=\lambda_{\min}(\mathbb{Q})=0$. To address this issue, we derive new expressions for the LQR cost. Consider an arbitrary FIR policy of order $H$ and define We immediately see that there is a uniform lower bound on $\lambda_{\min}(\bar{\mathbb{Q}})$ while the LQR cost remains the same if we replace $\mathbb{Q}$ with $\bar{\mathbb{Q}}$. Additionally, by the controllability of the lifted system, we can lower bound the minimum eigenvalue of $\Sigma_{H}^{i}(K)$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-B Gradient Domination of the Sample Average Objective", "weight": 1.0} -->

Combined with the uniform cost bound in Lemma III.3. ‣ III-A Coercivity and Smoothness of the Sample Average Objective ‣ III Global Convergence of Policy Gradient ‣ Policy Gradient over History-Dependent Policy Classes for LQR with Domain Randomization"), it holds that which is shown in Lemma C.2. ‣ C.2 Coercivity, smoothness, and descent ‣ Appendix C The landscape of a single FIR-LQR cost ‣ Policy Gradient over History-Dependent Policy Classes for LQR with Domain Randomization"). With and, we reformulate the FIR-LQR objective.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark III.4 (Limitation of Assumption III.1. ‣ III Global Convergence of Policy Gradient ‣ Policy Gradient over History-Dependent Policy Classes for LQR with Domain Randomization\"))", "weight": 1.0} -->

Since $f_{\textnormal{{het}}}$ proposed in Lemma III.6. ‣ III-B Gradient Domination of the Sample Average Objective ‣ III Global Convergence of Policy Gradient ‣ Policy Gradient over History-Dependent Policy Classes for LQR with Domain Randomization") scales with the FIR order $H$, it does not fully capture the phenomenon observed in Example II.1, which explains that increasing $H$ helps the controller stabilize the multiple systems with larger heterogeneity gap. However, the convergence result is interesting because even in the small heterogeneity gap regime, the optimization landscape induced by FIR policies remains highly nontrivial. Our result shows that policy gradient can still reliably find the optimum despite the nontrivial optimization landscape.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-C Proof of Theorem III.1. ‣ III Global Convergence of Policy Gradient ‣ Policy Gradient over History-Dependent Policy Classes for LQR with Domain Randomization\")", "weight": 1.0} -->

Finally, combining the landscape analysis of the SA objective in Section III-A with gradient domination in Section III-B, we prove Theorem III.1. ‣ III Global Convergence of Policy Gradient ‣ Policy Gradient over History-Dependent Policy Classes for LQR with Domain Randomization").

<!-- chunk {"id": "body-0034", "role": "body", "section": "Curriculum Learning-based Policy Gradient", "weight": 1.0} -->

In Section III, we show that PG converges for any fixed FIR order $H$. The choice of $H$ is a design parameter: smaller $H$ is preferable because it requires less memory and online computation, while larger $H$ can improve simultaneous stabilization, as demonstrated in Example II.1. We propose a curriculum learning-based algorithm that gradually increases $H$ until satisfactory performance is achieved, whenever such performance is achievable with FIR policies. Algorithm 1 consists of two components: discount annealing, which finds an initial stabilizing controller for a given $H$, and FIR order selection, which gradually increases $H$ until a satisfactory policy is found.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-A Discount Annealing", "weight": 1.0} -->

Generally, it is hard to find a controller that simultaneously stabilizes a collection of systems. \[5, Sect. IV\] presents a scheme that consists of successively optimizing discounted versions of the sample average objective in which the stage cost of the LQR problems at time $t$ are multiplied by the discount factor $\gamma^{t}$ or, equivalently, the state and input matrices for each sample are multiplied by $\sqrt{\gamma}$ with $0<\gamma\leq 1$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-A Discount Annealing", "weight": 1.0} -->

Then $\gamma$ is chosen to gradually increase from $0$ to $1$ such that the discounted versions of the problem always satisfy the condition on the initial iterate. shows that such a scheme is sufficient to ensure convergence to the optimal solution of the SA objective in the setting of static policies starting from an arbitrary initial iterate as long as the heterogeneity assumption holds. However, the argument is not specific to static policies, and immediately extends to the setting of FIR policies.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-B FIR Order Selection", "weight": 1.0} -->

Given a collection of systems, the FIR order $H$ required to simultaneously stabilize all the systems is undecidable when $M\geq 3$. However, suggests that if systems are simultaneously stabilizable, there exists a proper controller with sufficiently rich complexity that achieves stabilization. This motivates a curriculum learning strategy in which we run policy gradient while gradually increasing $H$. In this way, we can efficiently find a small enough $H$ that provides satisfactory performance. In Section V, we demonstrate the effectiveness of this strategy that progressively increases $H$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-B FIR Order Selection", "weight": 1.0} -->

1: Input: collection of systems θ1, …, θM, optimization tolerance ϵ, initial cost threshold $C_{\textnormal{{init}}}$, update multiplier Cγ1, Cγ2, update threshold τγ 2: Initialize FIR order H ← 1, K ← 0 3: Find largest γ ∈ (0, 1] s.t. $J_{SA}(K\mid\gamma,H)\leq C_{\textnormal{{init}}}$ 5: Apply PG to find K′ such that JSA(K′ ∣ γ, H) − infK̃JSA(K̃ ∣ γ, H) ≤ ϵ 7: Find a discount factor γ′ ∈ [γ, 1] such that 12: Run initialized at K to find K′ such that JSA(K′) − infK̃JSA(K̃) ≤ ϵ Algorithm 1 Curriculum Learning-Based Policy Gradient

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-C Curriculum Learning-Based Policy Gradient", "weight": 1.0} -->

Algorithm 1 is the pseudocode used in numerical experiments. We first choose the largest $\gamma$ such that $K=0$ can simultaneously stabilize a collection of systems, and such that the discounted sample average FIR-LQR cost given the FIR order $H$ $J_{\textnormal{{SA}}}(K\mid\gamma,H)$ is bounded by $C_{\textnormal{{init}}}$. Then we gradually update $K$ (line 5) and $\gamma$ (line 7) in a dual manner until we reach $\gamma=1$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-C Curriculum Learning-Based Policy Gradient", "weight": 1.0} -->

Note that $C_{\textnormal{{init}}}$, $C_{\gamma_{1}}$ and $C_{\gamma_{2}}$ need to be chosen carefully: $C_{\textnormal{{init}}}$ and $C_{\gamma_{2}}$ ensure the initial cost condition $J_{\textnormal{{SA}}}(K^{})\leq 8J_{\textnormal{{SA}}}(K^{\star})$ is satisfied when $\gamma$ reaches $1$, while $C_{\gamma_{1}}$is used to obtain a finite iteration guarantee. See \[5, Algorithm 1\] for a concrete example. To determine when to update $H$, we introduce the update threshold $\tau_{\gamma}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-C Curriculum Learning-Based Policy Gradient", "weight": 1.0} -->

When a collection of systems is not simultaneously stabilizable under a given $H$, there exists $\gamma_{\star}<1$ such that Therefore in this case, even though it is always possible to find $\gamma^{\prime}$ such that line 7 holds because of local continuity of $J_{\textnormal{{SA}}}(K)$, the update $\Delta_{\gamma}\coloneqq\gamma^{\prime}-\gamma$ becomes incremental as $\gamma$ gets close to $\gamma_{\star}$. Thus if $\Delta_{\gamma}\leq\tau_{\gamma}$ for some threshold, we increase $H$ to enlarge the controller parameterization (line 9), then initialize $\gamma$ again. Additional details are provided in the code repository.^44^ 4 Code available at this GitHub repository

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-A Policy Gradient over FIR Controller classes", "weight": 1.0} -->

We conduct numerical experiments on the discretized and linearized inverted pendulum defined by We suppose that the parameters $dt=0.01$ and $g=10$ are known. The unknown parameters $m$ and $\ell$ are modeled with a uniform distribution over the interval $[0.5,5.0]$. Starting from the FIR order $H=1$, we gradually increase $H$ when the discount factor does not increase sufficiently toward 1. Figure 1 demonstrates the application of Algorithm 1 to $M=10$ systems sampled from the distribution of systems. We plot the convergence of the SA cost $J_{\textnormal{{SA}}}(K)$, the evolution of the controller gains $K$, and the updates of the discount factor $\gamma$, where phase boundaries indicate the updates of the FIR order $H$. As we can observe, the LQR cost starts to decrease substantially once the FIR order reaches $H=5$, and from that point onward it converges to the minimizer of $J_{\textnormal{{SA}}}(K)$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-A Policy Gradient over FIR Controller classes", "weight": 1.0} -->

The plots of the controller gains and discount factor further show that, for smaller FIR orders, the controller gains start to grow rapidly in magnitude as $\gamma$ approaches $1$. This suggests that the sampled systems are difficult to stabilize with a lower order FIR controller. However, as $H$ increases, the controller can depend on longer history, and eventually this additional memory enables simultaneous stabilization, after which PG converges.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-A Policy Gradient over FIR Controller classes", "weight": 1.0} -->

Fig. 1: Convergence of policy gradient over FIR controller classes with domain randomization. A controller initialized at K = 0 converges to the optimal controller via discount annealing and curriculum learning. Phase boundary represents the increase of the FIR order H. The LQR cost starts to converge after H = 5.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-B Alternative Dynamic Parameterization", "weight": 1.0} -->

We next consider an alternative dynamic parameterization. The general dynamic policy can be parameterized as follows where $\bar{\xi}_{t}\in\mathbb{R}^{(H-1)d_{\mathsf{X}}}$. Since the FIR controller class admits the following parameterization, FIR is one realization of.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-B Alternative Dynamic Parameterization", "weight": 1.0} -->

Now we compare the performance of PG over several dynamic controller classes on the following example.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Example V.1", "weight": 1.0} -->

Consider the scalar system (a) An FIR controller converges at H = 5.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Example V.1", "weight": 1.0} -->

(b) A general dynamic controller converges at H = 2, but optimization is unstable.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Example V.1", "weight": 1.0} -->

Fig. 2: Policy gradient on Example V.1 with FIR and general dynamic controllers.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Example V.1", "weight": 1.0} -->

As shown in Figures 2(a) ‣ Figure 2 ‣ V-B Alternative Dynamic Parameterization ‣ V Numerical Experiments ‣ Policy Gradient over History-Dependent Policy Classes for LQR with Domain Randomization") and 2(b) ‣ Figure 2 ‣ V-B Alternative Dynamic Parameterization ‣ V Numerical Experiments ‣ Policy Gradient over History-Dependent Policy Classes for LQR with Domain Randomization"), PG converges in both cases, but the FIR controller attains a lower cost in fewer iterations than the dynamic controller ($5.1$ vs. $21.8$). Although the FIR controller uses longer history ($H=5$) than the dynamic controller ($H=2$), curriculum learning makes optimization stable. This highlights the tradeoff between controller complexity and optimization ease. Although FIR controllers form a strict subclass of dynamic controllers and are therefore less expressive, their smaller number of degrees of freedom makes optimization easier and leads to more efficient optimization. Results for another dynamic parameterization can be found in Appendix F.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Discussion", "weight": 1.5} -->

There are several possibilities for extensions of the results presented in this paper.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Discussion", "weight": 1.5} -->

Nonlinear parameterizations Although adding memory to the controller appears to improve simultaneous stabilizability, there still exist some examples that no linear controller can stabilize, such as Example VI.1. The use of nonlinear parameterization to overcome this problem is a promising direction.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Example VI.1", "weight": 1.0} -->

Consider the scalar system There does not exist a static controller nor a dynamic controller that can stabilize the system.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Example VI.1", "weight": 1.0} -->

Relaxed heterogeneity assumptions: The heterogeneity assumption $\varepsilon_{\textnormal{{het}}}$ is introduced for the optimality analysis of the DR-LQR objective, but the sufficient condition in Lemma III.6. ‣ III-B Gradient Domination of the Sample Average Objective ‣ III Global Convergence of Policy Gradient ‣ Policy Gradient over History-Dependent Policy Classes for LQR with Domain Randomization") suggests that $\varepsilon_{\textnormal{{het}}}$ scales inversely with the FIR order $H$. This appears to conflict with the stabilization perspective, in which more expressive controllers generally increase the possibility of simultaneous stabilization by shaping the closed-loop geometry more favorably. Investigating whether this intuition from simultaneous stabilization can be leveraged in the optimality analysis is an intriguing direction for future work.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our work motivates the use of history-dependent policies for domain randomization by considering collections of systems for which no static linear feedback controller can simultaneously stabilize the collection, whereas a history-dependent policy parameterized by a lower order finite impulse response controller can. Motivated by this fact, we prove the convergence of policy gradient methods over finite impulse response policies applied to minimize the sample average domain randomized linear quadratic control objective. We believe that further study of optimal policy classes for domain randomization serves as a stronger theoretical foundation for reinforcement learning in robotics.
