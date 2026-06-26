<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

MPCritic: A Plug-and-play MPC Architecture for Reinforcement Learning

Topics include Reinforcement learning, Optimal control, Model predictive control, Predictive control, Robustness, Benchmarks, Online algorithms, Optimization, Control, Learning, MPCritic, Constraint satisfaction.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The reinforcement learning (RL) and model predictive control (MPC) communities have developed vast ecosystems of theoretical approaches and computational tools for solving optimal control problems. Given their conceptual similarities but differing strengths, there has been increasing interest in synergizing RL and MPC. However, existing approaches tend to be limited for various reasons, including computational cost of MPC in an RL algorithm and software hurdles towards seamless integration of MPC and RL tools. These challenges often result in the use of "simple" MPC schemes or RL algorithms, neglecting the state-of-the-art in both areas. This paper presents MPCritic, a machine learning-friendly architecture that interfaces seamlessly with MPC tools. MPCritic utilizes the loss landscape defined by a parameterized MPC problem, focusing on "soft" optimization over batched training steps; thereby updating the MPC parameters while avoiding costly minimization and parametric sensitivities. Since the MPC structure is preserved during training, an MPC agent can be readily used for online deployment, where robust constraint satisfaction is paramount.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We demonstrate the versatility of MPCritic, in terms of MPC architectures and RL algorithms that it can accommodate, on classic control benchmarks.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

RL and \\acMPC have emerged as two successful frameworks for solving optimal control problems. Each community has developed a mature theory and set of computational tools for dealing with the well-known intractability of dynamic programming. Given their individual success and roots in dynamic programming, there is growing interest in developing complementary frameworks that can synergize the safe decision-making of \\acMPC with the flexible learning of \\acRL.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

MPC takes an optimization-based approach to control wherein predictions are made online to select actions. This strategy is amenable to theoretical results regarding safe system operation, such as stability and robustness, typically through its interpretable structure and reliance on constrained optimization. Meanwhile, \\acRL is an iterative, sample-based framework in which a control policy is learned through trial and error in an uncertain environment. Broadly, RL schemes consist of theoretical principles, such as policy gradients and $Q$-learning, combined with general-purpose function approximators.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

While sophisticated software tools have been developed to address the implementation intricacies of \\acRL and \\acMPC individually, two significant hurdles arise when combining them: the cost of running and differentiating \\acMPC in an \\acRL algorithm; and interfacing the highly specialized tools of \\acMPC and \\acRL. Resolving these obstacles would open the door for leveraging the theoretical properties of \\acMPC with the scalability of \\acRL. To this end, we propose MPCritic: an architecture that integrates seamlessly with machine learning and \\acMPC tools, allowing for incorporating \\acMPC theory in \\acRL. MPCritic utilizes the interpretable structure of \\acMPC---model, cost, constraints---to define a "critic" network, a common object in \\acRL, while, crucially, avoiding solving the \\acMPC problem during training iterations. Core to MPCritic is a "fictitious" controller that is cheap to evaluate, enabling batched training like any other critic network in \\acRL.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Due to the preserved \\acMPC structure, the \\acMPC can still be solved in real-time, where online control planning and robust constraint satisfaction can be critical.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The modularity of MPCritic allows for a range of configurations wherein individual \\acMPC components, such as dynamic model and cost, are designed to ensure theoretical properties of the online \\acMPC, or possibly learning all components in unison as a more general \\acRL function approximator. Comparing MPCritic to standard \\acMPC and deep \\acRL approaches, two configurations are demonstrated: learning the theoretically-optimal \\acMPC for the \\acLQR offline, extending to the online setting with constraints, and learning a stochastic "actor" parameterized by the fictitious controller embedded within MPCritic for improved performance and constraint satisfaction in a nonlinear environment. Our contributions are as follows: An algorithmic framework for integrating \\acMPC and \\acRL that is agnostic to the \\acRL algorithm, yet capable of seamlessly incorporating \\acMPC theory.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Detailed account of MPCritic software and implementation, utilizing advanced \\acRL and \\acMPC tools.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Case studies demonstrating the theoretical connection, scalability, and flexibility of MPCritic.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Markov decision processes", "weight": 1.0} -->

We consider an *agent* interacting with a dynamic *environment* with state space $\mathcal{S}$ and action space $\mathcal{A}$. For any state $s\in\mathcal{S}$, an action $a\in\mathcal{A}$ is selected by the agent, leading to a new state $s^{\prime}\in\mathcal{S}$. In particular, we write $s^{\prime}\sim p\left(s^{\prime}\middle|s,a\right)$, assuming the state transition density $p$ satisfies the *Markov property*. The desirability of a state-action tuple is characterized by a *reward* function $r:\mathcal{S}\times\mathcal{A}\to\mathbb{R}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Markov decision processes", "weight": 1.0} -->

Writing $r_{t}=r(s_{t},a_{t})$ leads to a trajectory $\{s_{0},a_{0},r_{0},s_{1},\ldots,s_{t},a_{t},r_{t},s_{t+1},\ldots\}$. The utility of a trajectory is characterized by the discounted return of future rewards $\sum_{t=0}^{\infty}\gamma^{t}r(s_{t},a_{t})$, where $\gamma\in$ is a constant. The link between states and actions is known as a *policy* $\pi$, a probability density where $a\sim\pi\left(a\middle|s\right)$. The agent implements and adapts the policy $\pi$, aimed at improving its expected returns.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Markov decision processes", "weight": 1.0} -->

Mathematically, this setup is \\iacMDP and can be framed as | | | maximize | | $\displaystyle J(\pi)=\mathbb{E}_{\pi}\left[\sum_{t=0}^{\infty}\gamma^{t}r(s_{t},a_{t})\right]$ | | \(2\) | | | | over all | | $\displaystyle\text{policies }\pi\colon\mathcal{S}\to\mathcal{P}(\mathcal{A}),$ | | | where $\mathcal{P}(\mathcal{A})$ is the set of probability measures on $\mathcal{A}$ and the expectation is over trajectories generated by $\pi$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Markov decision processes", "weight": 1.0} -->

In tackling 2, it is useful to define the state-action value function, or $Q$-function, for a policy $\pi$: $Q^{\pi}\left(s,a\right)=\mathbb{E}_{\pi}\left[\sum_{t=0}^{\infty}\gamma^{t}r(s_{t},a_{t})\middle|s_{0}=s,a_{0}=a\right]$. Value functions are an essential ingredient for solving the \\acMDP problem in 2. In particular, they lead to the *Bellman optimality equation* Namely, an optimal policy is designed through "greedy" optimization of the optimal value function Obtaining $Q^{\star}$ and $\pi^{\star}$ exactly is generally intractable due to lack of precise knowledge of the transition dynamics and complications surrounding the expectation and maximization operators. Nonetheless, 3 and 4 serve as fundamental inspiration for \\acRL and \\acMPC.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B Reinforcement learning", "weight": 1.0} -->

Although we cannot obtain $Q^{\star}$ and $\pi^{\star}$ directly, if we had some oracle mapping $\pi\to Q^{\pi}$, then an even better policy $\pi^{+}$ could be derived as $\pi^{+}(s)=\operatornamewithlimits{arg\,max}_{a}Q^{\pi}(s,a)$. This is a general recipe: acquire $Q$, maximize it, and repeat.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-B Reinforcement learning", "weight": 1.0} -->

In practice, we consider two parameterized function approximators: $Q_{\phi}$ and $\pi_{\theta}$, where $\phi$ and $\theta$ are sets of trainable parameters. The *critic* $Q_{\phi}$ is trained to satisfy 3; the *actor* $\pi_{\theta}$ is tasked with both exploring the environment and maximizing $Q_{\phi}$. For exploration, $\pi_{\theta}$ has the form where the mean is parameterized by the deterministic policy $\mu_{\theta}$. Moreover, $\mu_{\theta}$ is trained such that The left-hand side is a simple function evaluation, while the right-hand side requires an optimization routine.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-B Reinforcement learning", "weight": 1.0} -->

An iterative sequence then follows Equation (7a) is a target sample of the right-hand side of 3. By collecting a dataset $\mathcal{D}$ of transition tuples $(s,a,r,s^{\prime})$, the critic weights are updated in 7b to minimize the residual based on 3. Finally, the actor is updated in 7c to improve its maximization performance. Collectively, 7 represents the nominal equations comprising the \\acDPG algorithm; these ideas then led to deep \\acRL algorithms such as \\acsTD3 and \\acsSAC.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-C Model predictive control parameterization", "weight": 1.0} -->

MPC takes a different view towards solving \\acpMDP. At each time step, it uses a dynamic model of the environment, cost, and constraints to plan a sequence of actions. The first action is applied to the environment, and the process is repeated; this is a *receding horizon* approach to control.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-C Model predictive control parameterization", "weight": 1.0} -->

$\phi$ encompasses parameters of the dynamic model $f$, stage cost $\ell$, and terminal value function $V$. Equation 8 is a modular structure, meaning individual components may be fixed or modified by different means. For instance, the dynamic model may be derived from system identification. Each element of $\phi$ is designed such that 8 is a tractable approximation of the \\acMDP problem.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-C Model predictive control parameterization", "weight": 1.0} -->

MPC provides an interpretable representation for approximating $Q^{\star}$. Its model-based structure enables safety and robustness properties, making it a desirable parameterization for learning-based control.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A MPC-based architecture via fictitious controller", "weight": 1.0} -->

The proposed architecture, MPCritic, utilizes a so-called "fictitious" controller to take the space of the decision variables $\{u_{1},\ldots,u_{N-1}\}$ in the \\acMPC problem in 8. Over some restricted domain of the state-action space, consider the following $Q$-function parameterization | | $\displaystyle Q_{\phi}(s,a)$ | $\displaystyle=\frac{1}{N}\sum_{t=0}^{N-1}\ell(x_{t},u_{t})+V(x_{N})$ | | \(9\) | where $\phi=\{\ell,V,f,\mu\}$. The controller $\mu$ is fictitious because it never interacts with the environment. Instead, it serves several important functions: Efficiency. Querying $Q_{\phi}$ only requires running the system model forward and accumulating the closed-loop cost.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A MPC-based architecture via fictitious controller", "weight": 1.0} -->

Approximation. $\mu$ is trained to approximate the minimization step that \\acMPC requires.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A MPC-based architecture via fictitious controller", "weight": 1.0} -->

Modularity. $Q_{\phi}$ contains the \\acMPC structure and can be seamlessly integrated with \\acRL tools. Yet, at deployment, $\mu$ is disregarded and the full \\acMPC optimization is performed online.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A MPC-based architecture via fictitious controller", "weight": 1.0} -->

Taken together, $\mu$ enables batched, iterative training in \\iacRL ecosystem, while preserving the exact \\acMPC structure for online control, as shown in Fig. 1.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-A MPC-based architecture via fictitious controller", "weight": 1.0} -->

Equation 9 is not defined over the full state-action space. Therefore, in practice, MPCritic takes the form of where $\rho>0$ is a constant penalty term. The system dynamics and fictitious controller are explicitly accounted for in computing 10; the action constraints are part of the architecture $\mu$. A penalty approach is assumed in 10 for simplicity. However, the proposed setup is general, inviting other approaches such as barrier or augmented Lagrangian methods.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-A MPC-based architecture via fictitious controller", "weight": 1.0} -->

Relation to differentiable MPC. An alternative to MPCritic is to directly differentiate through the \\acMPC solution. This line of work has the benefit of preserving the \\acMPC structure, while modifying it under some supervisory signal, such as reward or an imitation loss. However, embedding the \\acMPC optimization routine into a general \\acRL framework is cumbersome and expensive because the number of \\acMPC solves scales with the number of time steps, update iterations, and batch size. Our approach treats \\acMPC as a loss, allowing for approximate solutions driving batched parameter updates, but preserves the \\acMPC structure for online deployment.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-A MPC-based architecture via fictitious controller", "weight": 1.0} -->

Relation to approximate MPC. The so-called fictitious controller in 10 aims to approximate the minimization process of \\acMPC. This is conceptually similar to approximate \\acMPC. In fact, the proposed approach can be viewed as a combination of approximate \\acMPC and actor-critic methods in \\acRL. Instead of using $\mu$ to decrease online computational demand, we use it to integrate the \\acMPC structure into \\acRL. Consequently, $\mu$ is never trained for high accuracy over the state-action space for a particular \\acMPC configuration $\phi$. Rather, it is part of a dynamic cycle of refinements to $\phi$ and $\theta$, as in actor-critic methods.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B MPCritic learning configurations", "weight": 1.0} -->

Different variants of MPCritic depend on two factors: Role of the fictitious controller and model in MPCritic. $\mu$ in MPCritic may be viewed either as an approximation to the \\acMPC solution, or as any other parameter, trained entirely from the reward signal. The same distinction applies to the dynamic model $f$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-B MPCritic learning configurations", "weight": 1.0} -->

Definition of the policy. MPCritic preserves the online \\acMPC agent for control simply by removing $\mu$. Alternatively, MPCritic may be used solely as a critic network, leaving the opportunity to train a separate actor network for control.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B MPCritic learning configurations", "weight": 1.0} -->

Thus, there are two extreme versions of MPCritic. The one presented so far trains $\mu$ to minimize the loss defined by the \\acMPC objective, acquires $f$ from system identification, and deploys an online \\acMPC policy derived from MPCritic. The other extreme trains $\mu$ and $f$ entirely from reward, like arbitrary parameters in a critic network, while training a separate actor network for control. That is, MPCritic can, in principle, learn a control-oriented model directly from reward, rather than a system identification method. The first view is useful when a predefined \\acMPC structure is known to be feasible for online control and possibly benefits from favorable theoretical properties, but requires tuning. The second view does not invoke \\iacMPC agent and, therefore, does not require an NLP solver, meaning more complex structures may be used in MPCritic to guide the learning of an easy-to-evaluate actor network; this could be viewed as an adaptive, reward-driven view of approximate \\acMPC.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-B MPCritic learning configurations", "weight": 1.0} -->

These different configurations are summarized in Algorithms 1 and 2. $\theta$ and $\phi$ refer to actor and critic parameters, respectively. Additionally, in light of these different flavors of MPCritic, we define $\psi$ to be parameters inside MPCritic that are trained under some auxiliary objective. Under one view of MPCritic, we have $\psi=\{\psi^{(\mu)},\psi^{(f)}\}$ for the parameters of $\mu$ and $f$ trained in an approximate \\acMPC fashion and system identification, respectively. We may also have $\psi=\emptyset$, meaning we write $\phi^{(\mu)},\phi^{(f)}$ because $\mu$ and $f$ are part of the set of critic parameters $\phi$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-B MPCritic learning configurations", "weight": 1.0} -->

1: Initialize $\theta,\phi,{\color[rgb]{10,92,174}\psi}$ 2: for each environment step do 3: $a\sim\pi\left(a\middle|s\right)\lx@algorithmic@hfill\triangleright\ \text{Optional: See \lx@cref{creftype~refnum}{alg:mpcritic}}$ 5: for each update step do 6: $\phi\leftarrow\phi-\alpha\nabla\mathcal{L}_{\text{critic}}\lx@algorithmic@hfill\triangleright\ \text{e.g., \lx@cref{creftype~refnum}{eq:dpgalg_critic}}$ 7: $\theta\leftarrow\theta+\alpha\nabla\mathcal{L}_{\text{actor}}\lx@algorithmic@hfill\triangleright\ \text{e.g.,

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-B MPCritic learning configurations", "weight": 1.0} -->

${\color[rgb]{10,92,174}a=\underset{a}{\operatornamewithlimits{arg\,min}}\ Q_{\text{{{MPCritic}}}}(s,a)}\lx@algorithmic@hfill\triangleright\ \text{e.g., \lx@cref{creftype~refnum}{eq:Qmpc}}$ 5: Update $\phi,{\color[rgb]{10,92,174}\psi}\text{ via \lx@cref{creftype~refnum}{alg:RL}}$ Algorithm 2 Optimization-based MPCritic actor

<!-- chunk {"id": "body-0034", "role": "body", "section": "Interfacing deep RL with MPC theory", "weight": 1.0} -->

MPCritic permits theoretical properties through its \\acMPC structure. We outline how MPCritic can leverage general \\acMPC formulations within \\iacRL ecosystem, touching on the theoretical and implementation aspects at play.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-A Robustness and stability", "weight": 1.0} -->

MPCritic preserves the \\acMPC structure, which makes it amenable to existing theory. We point to several such avenues that future work should more rigorously investigate. The importance of a terminal value function for stability and constraint satisfaction is well-established. It is straightforward to incorporate quadratic functions, or Lyapunov neural networks, as a terminal cost in the design of MPCritic, as is done here. As such, one may invoke \\acLQR or certainty equivalence arguments to construct a stable-by-design architecture. Robustness is another important aspect of \\acMPC safety. Although MPCritic is trained on the system of interest, robustness is still important for improved constraint satisfaction, especially in the early stages of training, or if training is halted. Any robust \\acMPC or stochastic \\acMPC method is, in principle, compatible with the MPCritic framework.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-B Deep RL implementation", "weight": 1.0} -->

MPCritic is implemented in NeuroMANCER, a differentiable programming library for solving optimal control problems. Because NeuroMANCER is based on PyTorch, MPCritic interfaces nicely with \\acRL packages for training its components. We use CleanRL since its single-file implementations of \\acRL algorithms facilitate transparency. For deployment of MPCritic, we use do-mpc, a Python toolbox for \\acMPC built around CasADi. Finally, L4CasADi serves as a bridge between PyTorch and CasADi, making it a convenient tool for deploying \\iacMPC agent with the learned MPCritic models. Importantly, MPCritic is not restricted to any particular \\acMPC implementation, solver, or \\acRL library. These toolboxes encapsulate general \\acMPC formulations, designed to function as any critic network under the MPCritic framework.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Case studies", "weight": 1.0} -->

To demonstrate the theoretical properties of MPCritic, we investigate the convergence of its learned solutions to the analytical \\acLQR solutions. We then test its computational efficiency for increasingly high-dimensional systems as compared to differentiable \\acMPC. Afterwards, the proposed learning-based control framework is evaluated on two control tasks. In the first, we evaluate Algorithm 2 and the learned fictitious controller, comparing to a standard deep RL agent. The second demonstrates the flexibility of MPCritic as a function approximator in Algorithm 1, learning a stochastic decision-making actor in a nonlinear environment with constraints. All experiments were run on an Apple M3 Pro 11 Core laptop. Codes are available at

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-A Offline validation & scalability of MPCritic", "weight": 1.0} -->

We first study MPCritic in the context of \\acLQR. Consider an open-loop unstable linear system $s^{\prime}=As+Bu$, with quadratic reward $r(s,a)=-s^{\top}Ms-a^{\top}Ra$ (see unstable Laplacian dynamics in). We assume $M$ and $R$ are known, but the parameters of the model $A,B$, terminal cost $P$, and gain $K$ are uncertain. Updating as in Algorithm 1, MPCritic aims to learn the true, optimal parameters for the system model $A^{\star},B^{\star}$, terminal cost $P^{\star}$ (from the discrete algebraic Riccati equation), and the corresponding optimal gain $K^{\star}$, using $\mu(x)=-Kx$. Updates repeatedly follow 7b for $\phi=P$, 7c for $\psi^{(\mu)}=K$, and for $\psi^{(f)}=\{A,B\}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-A Offline validation & scalability of MPCritic", "weight": 1.0} -->

All uncertain parameters are initialized following $\psi^{(f)},\psi^{(\mu)},\phi,\sim\mathcal{N}$ and learned from $10^{5}$ transitions $(s,a,r,s^{\prime})$ following $s,a\sim\mathcal{U}(-1,1)$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-A Offline validation & scalability of MPCritic", "weight": 1.0} -->

The true, optimal parameters are approximately recovered within MPCritic in this learning scheme for systems of equal and increasing state and action dimension, $n$ and $m$, respectively. This is shown in Fig. 2 in terms of the \\acRMSE of the learned closed-loop dynamics $A-BK$ for all systems with each batched update. On average, \\acRMSE diminishes to less than $5{\times}10^{-4}$ within $10^{5}$ steps for all system sizes, and although not depicted, that of the model and fictitious controller individually diminish to less than $4{\times}10^{-4}$. Obtaining an accurate representation for the closed-loop dynamics improves 10 as a $Q$-function approximator, which is further refined by 7b. Accordingly, $P$ is learned such that 9 best approximates $Q^{\star}$, resulting in an \\acRMSE with respect to $P^{\star}$ less than $2{\times}10^{-2}$ for all systems with the error increasing with system size.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-A Offline validation & scalability of MPCritic", "weight": 1.0} -->

This example demonstrates the ability of MPCritic to (approximately) learn the theoretically-optimal \\acMPC components in a batched learning scheme, while preserving the \\acMPC structure.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-A Offline validation & scalability of MPCritic", "weight": 1.0} -->

Additionally, a key benefit of MPCritic is the computational efficiency of batch processing brought forth by parameterizing the \\acMPC optimization through the fictitious controller $\mu$. To demonstrate this point, Table I reports the average time to evaluate $\mu$, or solve an MPC policy $\pi^{\text{MPC}}$ (forward) and differentiate their outputs (backward). For simplicity, the MPC policy is of constrained linear quadratic formulation with horizon $N=1$ and, accordingly, the fictitious controller is defined by a ReLU \\acDNN for its piecewise affine structure with $2$ hidden layers of $100$ nodes. Table I reports significantly less computation time for the "soft" optimization performed by $\mu$ in comparison with the exact optimization of $\pi^{\text{MPC}}$. Critically, the backward computation times for $\mu$ are less sensitive to the system size, requiring less than $1$ millisecond in all cases, as compared to $\pi^{\text{MPC}}$ that can take hours to solve and differentiate.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-A Offline validation & scalability of MPCritic", "weight": 1.0} -->

\\AcRL algorithms typically require rapid evaluation of both forward and backward operations, potentially online, quickly making the exact optimization of $\pi^{\text{MPC}}$ and subsequent differentiation impractical for larger systems. Rather, cheap evaluation and differentiation, as well as favorable scaling, all while retaining the desired structure of \\acMPC through $\mu$, lessen the constraints of computational cost on the user's choice of \\acRL algorithm.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-B Learning \\\\acMPC online with MPCritic", "weight": 1.0} -->

We now explore the application of MPCritic for learning \\acMPC via online interaction and compare it to a traditional deep \\acRL agent, both utilizing the TD3 algorithm. Consider the previous \\acLQR environment with $n=m=4$, initial state $s_{0}\sim\mathcal{U}(-1,1)$, and, now, the goal of maximizing cumulative rewards over an episode of $50$ time steps.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-B Learning \\\\acMPC online with MPCritic", "weight": 1.0} -->

All of $\ell$,$V$,$f$, and $\mu$ are learned via Algorithm 2, with auxiliary objectives 10 and 11 for $\mu$ and $f$, respectively; $\mu$ being the previously defined ReLU \\acDNN. The \\acRL agent acts though a ReLU \\acDNN policy of the same model class as $\mu$, but is trained to maximize the critic, a neural network with 1 hidden layer of 256 nodes.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-B Learning \\\\acMPC online with MPCritic", "weight": 1.0} -->

Learning for $5{\times}10^{5}$ steps, cumulative reward and constraint violation statistics for both agents during the final $10$ episodes are reported in Table II. Notably, the \\acMPC agent generally obtains greater rewards with significantly less variance. Furthermore, while not shown, the \\acMPC agent achieves equal performance, on average, as the final \\acRL agent in less than $10^{3}$ update steps. This difference in sample efficiency can be attributed, in part, to the auxiliary system identification objective. While the deep \\acRL agent relies on rewards and bootstrapping to learn the $Q$-function, provides an additional complementary signal for improving MPCritic.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-B Learning \\\\acMPC online with MPCritic", "weight": 1.0} -->

Table II also shows the learned \\acMPC agent, in the worst of cases, is less apt to violate $\mathchoice{\left\|{{{{s_{t}}}}}\right\|}{\|{{{{s_{t}}}}}\|}{\|{{{{s_{t}}}}}\|}{\|{{{{s_{t}}}}}\|}_{\infty}\leq 1$ compared to the deep \\acRL agent. Although one can attempt to promote this behavior in the \\acRL agent by modifying its reward signal, doing so does not readily provide guarantees. Rather, MPCritic provides a straightforward pathway to incorporate state constraints through its architecture.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-B Learning \\\\acMPC online with MPCritic", "weight": 1.0} -->

The learned behavior of each policy is shown in Fig. 3, including that of the learned fictitious controller $\mu$ for further comparison. With rewards penalizing non-zero actions more than states, the RL agent is largely concerned with avoiding large actions rather than driving the state to the origin. The \\acMPC agent designs coordinated action sequences towards the origin, traversing the boundary of the state and/or action constraints for portions of the sequence. In contrast, without a "planning" mechanism or modified reward, the deep \\acRL agent is willing to leave the closed unit ball to maximize the reward, but this is sure to incur future costs for the unstable system. Notably, the \\acRL agent's policy and $\mu$ are of the same model class, yet $\mu$ is learned to approximate the exact \\acMPC optimization rather than maximize a \\acDNN critic.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-B Learning \\\\acMPC online with MPCritic", "weight": 1.0} -->

Consequently, $\mu$ is informed by the constraints without modifying the reward signal, unlike the \\acRL agent, due to their presence in 10. This property, along with the relative efficiency of $\mu$, raises interesting questions about how $\mu$ can be leveraged more broadly within \\acRL schemes.

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-C Maximum entropy policies with MPCritic", "weight": 1.0} -->

This example illustrates the generality of MPCritic as an inductive bias in \\acRL. We use MPCritic as a function approximator in maximum entropy \\acRL. Here, the goal is to learn a stochastic actor that maximizes its reward, while doing so as randomly as possible. This randomness induces the exploration useful towards system identification.

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-C Maximum entropy policies with MPCritic", "weight": 1.0} -->

Consider a stochastic actor $\pi_{\theta}$ as in 5 and critic $Q_{\phi}$, both given by a \\acDNN. MPCritic is constructed with \\iacDNN dynamic model that is learned online through system identification, a fixed stage cost, a penalty term for state constraints, and $Q_{\phi}$ as terminal value function. In this example, we use neural networks that would be intractable to train using typical NLP solvers. Instead, the fictitious controller, aimed at minimizing the \\acMPC objective in 8, parameterizes the mean of $\pi_{\theta}$. One can simply run actor-critic update steps on $\pi_{\theta}$ and $Q_{\phi}$, while periodically applying updates to $f$ and $\mu$ as in lines 9 and 10 of Algorithm 1. In this way, the policy $\pi_{\theta}$ learns from the structure of MPCritic, and MPCritic adapts with $Q_{\phi}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-C Maximum entropy policies with MPCritic", "weight": 1.0} -->

We demonstrate this learning scheme with \\iacSAC agent, an off-policy maximum entropy deep \\acRL algorithm. The environment is modeled with \\iacCSTR, a common benchmark in process control, and a Gaussian-shaped reward (see for further details of this environment). The goal is to control the concentration $c_{B}$ to a desired level $c_{B}^{\text{goal}}$, comprising the reward $r(s,a)=\exp{\left(-\nicefrac{{\left(c_{B}^{\text{goal}}-c_{B}\right)^{2}}}{{2\sigma^{2}}}\right)}$ with $\sigma^{2}=0.0025$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-C Maximum entropy policies with MPCritic", "weight": 1.0} -->

This reward structure is used for the stage cost with $\sigma^{2}=0.25$; all other models involved---for $\pi_{\theta}$, $Q_{\phi}$, $f_{\psi}$---are two-layer ReLU networks with $256$ nodes per layer; note $\mu_{\psi}=\mu_{\theta}$, which parameterizes the mean of $\pi_{\theta}$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-C Maximum entropy policies with MPCritic", "weight": 1.0} -->

Because MPCritic is a plug-and-play architecture, we can embed it directly in a default \\acSAC agent. Fig. 4 shows three reward curves, each over $10$ seeds. The vanilla \\acSAC agent takes over $1000$ episodes to start improving, only reaching a modest level of reward. We note that this is not a critique of \\acSAC; fine-tuning its hyperparameters can indeed lead to improved results. Rather, we stress that MPCritic provides a useful inductive bias to jump start and enhance the learning process, indicated by the "unconstrained" reward curve. Importantly, MPCritic also incorporates constraints. The intermediate reward curve in Fig. 4 indicates that \\acSAC$+{\texttt{MPCritic}}$ is able to learn a high-performing policy under the Gaussian reward, but that is fundamentally limited by the constraints in its representation. Trajectories from both MPCritic agents are shown in Fig. 5, along with the robust \\acMPC policy given.

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-C Maximum entropy policies with MPCritic", "weight": 1.0} -->

The unconstrained MPCritic agent represents a near-optimal solution to the setpoint $c_{B}^{\text{goal}}$; MPCritic with constraints also achieves its goal, taking longer, but staying within the shaded region. Meanwhile, the \\acMPC agent may achieve robust constraint satisfaction, but it contains no goal-directed feedback to improve its response when a better course of action may exist.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Conclusions", "weight": 1.0} -->

MPCritic is an algorithmic framework capable of seamlessly utilizing advanced tools from both \\acMPC and \\acRL. While we have demonstrated the scalability and versatility of MPCritic across different configurations, there are many fruitful paths for future work. These range from formalizing theoretical properties of MPCritic and its applications with more sophisticated \\acMPC agents to establishing its utility as a general inductive bias in \\acRL for complex environments.
