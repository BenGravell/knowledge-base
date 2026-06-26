<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Soft MPCritic: Amortized Model Predictive Value Iteration

Topics include Reinforcement learning, Value iteration, Model predictive control, Predictive control, Robustness, Accuracy, Online algorithms, Planning, Control, Learning, Soft MPCritic, Amortized, Model predictive path integral control.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Reinforcement learning (RL) and model predictive control (MPC) offer complementary strengths, yet combining them at scale remains computationally challenging. We propose soft MPCritic, an RL-MPC framework that learns in (soft) value space while using sample-based planning for both online control and value target generation. soft MPCritic instantiates MPC through model predictive path integral control (MPPI) and trains a terminal Q-function with fitted value iteration, aligning the learned value function with the planner and implicitly extending the effective planning horizon. We introduce an amortized warm-start strategy that recycles planned open-loop action sequences from online observations when computing batched MPPI-based value targets. This makes soft MPCritic computationally practical, while preserving solution quality. soft MPCritic plans in a scenario-based fashion with an ensemble of dynamic models trained for next-step prediction accuracy. Together, these ingredients enable soft MPCritic to learn effectively through robust, short-horizon planning on classic and complex control tasks. These results establish soft MPCritic as a practical and scalable blueprint for synthesizing MPC policies in settings where policy extraction and direct, long-horizon planning may fail.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

RL and MPC are contrasting strategies for designing decision-making agents. MPC accounts for system dynamics and constraints to construct a notion of value to be optimized online in a receding-horizon fashion [rawlingsModelPredictiveControl2017]. Meanwhile, a core design philosophy driving (actor-critic) RL methods is value-based backup followed by policy extraction [lillicrap2016Continuouscontrol, haarnoja2018Softactorcritic]. There are pros and cons to both approaches, as discussed below. Nevertheless, RL and MPC offer complementary benefits, motivating hybrid frameworks that incorporate planning into a flexible learning pipeline [lawrence2025view, reiter2026synthesis].

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

There is a plethora of ways in which dynamic models can be integrated into RL [wang2019benchmarking]. One useful way to divide them is based on alignment: does the RL agent learn from the model or does the model learn from the agent? The so-called dyna framework is a popular instance of the former. Here, simulated experience is used to train a policy using otherwise model-free algorithms. This strategy can be very sample efficient [frauenknecht2024Trustmodel], but has also been shown to be brittle due to its over reliance on simulated experience [jafferjee2020HallucinatingValue, barkley2024StealingThat]. Other lines of work use a model to construct a value target or loss for policy learning [drgona2024LearningConstrained, byravan2020imagined, feinberg2018model]. These approaches provide a rich loss landscape for policy learning; however, it may be difficult to optimize. MPC has also been shown to be a useful structure within RL.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

If the model is sufficiently accurate, then RL can provide MPC with a terminal value function [lawrence2025view], a baseline policy [qu2024RLDrivenMPPI, wang2025ResidualMPPIOnline], or MPC can provide model-based value targets for training a critic network [bhardwaj2020InformationTheoretic]. The other end of the spectrum aims to learn a dynamic model that aligns with the reward or value function [farahmand2017value, hansen2024TDMPC2Scalable]. This can also take the form of differentiable MPC wherein the planner is differentiated and updated to maximize some objective [amos2019DifferentiableMPC, gros2019data]. MPC is viewed as a function approximator whose parameters (including the dynamic model) can be shaped to suit the control objective. In principle, there is significant flexibility in this approach, but it can be hindered by computational and feasibility issues [reiter2026synthesis].

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

MPC-RL framework inspired by soft value iteration [haarnojaReinforcementLearning, levine2018reinforcement]. A dynamic model is used only for short-term predictions within a value-augmented MPC. This MPC serves two functions: control and value function training. To train the terminal value function, the MPC itself provides temporal difference-style targets. This procedure aligns the terminal value function with the MPC, implicitly extending its horizon for online decision-making. We call this framework {\texttt{soft\,MPCritic}}\xspace, representing a parallel work to {\texttt{MPCritic}}\xspace[lawrence2025mpcritic]. {\texttt{MPCritic}}\xspacefollows an actor-critic design, wherein a fictitious controller serves as an approximate MPC solution to streamline the integration of MPC within RL without explicitly solving MPC or computing its sensitivities for RL updates. In contrast, {\texttt{soft\,MPCritic}}\xspacelives entirely in value space.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Specifically, we formalize {\texttt{soft\,MPCritic}}\xspacein the context of soft value iteration wherein a softmax-like operation is used in place of hard maximization as in classical dynamic programming [bertsekas2012dynamic]. This formulation naturally connects MPC, specifically MPPI [williams2016Aggressivedriving, williamsInformationTheoreticMPC2017, honda2025model], to soft value iteration and enables efficient integration of MPC within RL pipeline. {\texttt{soft\,MPCritic}}\xspaceis designed to be algorithmically simple, emphasizing the utility of short-horizon planning and value iteration, while mapping out possible extensions for future work.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

- An RL-MPC algorithm that lives entirely in value space, utilizing a formal connection between path integral control and soft value iteration. - An amortized value iteration approach to efficient MPC integration within RL. Specifically, we disperse the computational burden of MPC via a warm-starting strategy both for online and offline target value generation. - Case studies demonstrating the {\texttt{soft\,MPCritic}}\xspaceon challenging control problems and validating the use of a planner both for online control and target generation.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Markov decision processes", "weight": 1.0} -->

MDP comprising an environment and agent. The environment has states $s \in \state$ that evolve randomly as actions $a \in \action$ are proposed by the agent. We assume these state transitions are Markovian and characterized by a probability density $p$; mathematically, $s' \sim \pp{p}{s'}{s,a}$, where $s' \in \state$denotes a next state.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Markov decision processes", "weight": 1.0} -->

States and actions are scored with a cost function $\ell: \state \times \action \to \reals$. The agent should design actions that account for the cumulative cost of its actions. As a reference, we first examine the so-called free energy of the system. The free energy considers an open-loop prior $\tilde{\beta}$ over actions and the cost of the resulting trajectories. We denote the induced distribution over trajectories by $\tau \sim p^{\tilde{\beta}}$, where $\tau = \{ s_0, a_0, \ldots, s_{H-1}, a_{H-1} \}$. Note $\tau$ depends only on the initial state distribution and sequences of actions, denoted by $\alpha = \{ a_0, \ldots, a_{H-1} \}$, meaning we can write $\tau = \tau(\alpha, s_0)$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Markov decision processes", "weight": 1.0} -->

Taking $J$ to be a real-valued function measuring cumulative cost, the free energy is defined as $$\ensuremath{\mathcal{F}} = - \lambda \log \left(\EE_{\tau \sim p^{\tilde{\beta}}} \left[\exp \left(-\frac{1}{\lambda} J(\tau) \right) \right] \right),$$ where $\lambda > 0$ is a temperature parameter and $s_0 \sim p(s_0)$. Intuitively, free energy is a soft minimum over random trajectories; $\lambda$ influences the sharpness of the soft minimum operator and $\tilde{\beta}$determines the scope and texture of the action space.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Markov decision processes", "weight": 1.0} -->

For any distribution over actions $\beta$, it can be shown (by Jensen's inequality) that $$\ensuremath{\mathcal{F}} \leq -\lambda \mathbb{E}_{\tau \sim p^{\beta}} \left[\log\left(\prod_{t = 0}^{H-1} \frac{\tilde{\beta}(a_t)}{\beta(a_t)} \exp\left(-\frac{1}{\lambda} J(\tau) \right) \right) \right].$$ Given this lower bound, and with a slight abuse of notation, it can be verified that the optimal distribution has density $$\beta^\star (\alpha) = \frac{1}{\eta} \exp\left(-\frac{1}{\lambda} J(\tau) \right) \prod_{t=0}^{H-1}\tilde{\beta}(a_t),$$ where $\eta$ is a normalizing

<!-- chunk {"id": "body-0013", "role": "body", "section": "Markov decision processes", "weight": 1.0} -->

While eq:opt\_pdf gives an elegant solution to the problem, sampling directly from $\beta^\star$ is infeasible. The goal of the agent is to design a near-optimal control distribution over actions that approximately matches the free energy of the system. Next, we outline two methodological frameworks for this problem.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Path integral control approach", "weight": 1.0} -->

MPPI approximately samples from $\beta^\star$ through importance sampling and Monte Carlo estimation [williams2016Aggressivedriving, williamsInformationTheoreticMPC2017, homburgerOptimalitySuboptimality]. To begin, MPPI aims to find optimal control inputs that minimize the KL divergence between the optimal distribution $\beta^\star$ and the design distribution $\beta$. The principal result is that the optimal control inputs can be expressed as an expectation of weighted actions over $\beta$ $$u_t^\star = \frac{1}{\eta} \mathbb{E}_{\alpha \sim \beta(\alpha)} \left[w(\alpha) a_t \right].$$ Assuming, as a standard example, $\tilde{\beta} = \mathcal{N}(0, \Sigma)$ and $\beta = \mathcal{N}(u, \Sigma)$, where $u$ is a commanded control input, actions are sampled through the change of variables $a = u + \epsilon$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Path integral control approach", "weight": 1.0} -->

eq:opt\_pdf is given by $$\eta = \frac{1}{N}\sum_{n=1}^{N} w(\varepsilon^{(n)}).$$ This weighted structure highlights low-cost trajectories and ignores bad ones.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Path integral control approach", "weight": 1.0} -->

Control inputs are then updated iteratively $$u^{(i+1)}_t = u^{(i)}_t + \frac{1}{\eta N} \sum_{n=1}^{N} w (\varepsilon^{(n)}) \epsilon_t^{(n)}.$$ MPPI is implemented in a receding-horizon fashion, meaning the online policy applies $u^{(\cdot)}_0$, the first action computed in eq:u\_iter, and then the MPPIsteps are repeated at the next state.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Soft value function approach", "weight": 1.0} -->

We introduce a state-dependent free energy mirroring The soft value function at state $s$ is defined as \ensuremath{\mathcal{V}}(s) =\\ -\lambda \log \left(\mathbb{E}_{\tau \sim p^{\tilde{\beta}}} \left[\exp\left(- \frac{1}{\lambda} \sum_{t=0}^\infty \gamma^t \ell(s_t, a_t) \right) \middle| s_0 = s \right] \right), where $0 < \gamma < 1$ is a fixed discount factor [haarnojaReinforcementLearning, levine2018reinforcement].

<!-- chunk {"id": "body-0018", "role": "body", "section": "Soft value function approach", "weight": 1.0} -->

$\ensuremath{\mathcal{V}}$ is near identical to $\ensuremath{\mathcal{F}}$ except it evaluates the free energy at a desired state; in that way, $\ensuremath{\mathcal{F}} = \mathbb{E}_{s_0 \sim p(s_0)}\left[\ensuremath{\mathcal{V}} (s_0) \right]$. Value functions enable iterative solution methods that decompose the infinite-horizon objective into recursive subproblems [bertsekas1996neuro, bertsekas2012dynamic]. It is helpful to introduce the soft action-value function or $\ensuremath{\mathcal{Q}}$-function, which follows the same definition as $\ensuremath{\mathcal{V}}$ except it is initialized at state-action pairs.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Soft value function approach", "weight": 1.0} -->

A concise way of expressing $\ensuremath{\mathcal{Q}}$ is in terms of $\ensuremath{\mathcal{V}}$, i.e., $$\ensuremath{\mathcal{Q}} (s,a) = \ell(s,a) + \gamma \mathbb{E}_{s' \sim \pp{p}{s'}{s,a}} \left[\ensuremath{\mathcal{V}}(s') \right].$$ $\ensuremath{\mathcal{Q}}$ enables the agent to design a single action that accounts for long-term cost, captured by the expected free energy across next possible states. Note eq:soft\_bellman can be written with $\ensuremath{\mathcal{Q}}$ on both sides of the equation, leading to a soft Bellman optimality equation.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Soft value function approach", "weight": 1.0} -->

Therefore, one may take $\ensuremath{\mathcal{Q}}$ to be an objective function to be (softly) optimized, for example, using distribution matching technique of the previous section (take $J = \ensuremath{\mathcal{Q}}$).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Soft value function approach", "weight": 1.0} -->

Proceeding along this path, we have $\alpha = a$ and arrive at at the optimal distribution \pp{\pi^\star}{a}{s} &= \frac{1}{\eta} \exp\left(-\frac{1}{\lambda} \ensuremath{\mathcal{Q}} (s,a) \right) \tilde{\beta}(a) \\&\propto \exp\left(-\frac{1}{\lambda} \left(\ensuremath{\mathcal{Q}}(s,a) - \ensuremath{\mathcal{V}}(s) \right) - \norm{a}_{\Sigma^{-1}}^2 \right), as $\ensuremath{\mathcal{V}} (s) = -\lambda \log(\eta)$. Therefore, $\pi^\star$ optimally balances the advantage of each action over the state value $\ensuremath{\mathcal{V}}$and control effort.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Ethos of {\\texttt{MPCritic}}\\xspace", "weight": 1.0} -->

{\texttt{MPCritic}}\xspace[lawrence2025mpcritic] is to enable efficient integration of MPC and RL through principled approximations. {\texttt{MPCritic}}\xspacefollows an actor-critic strategy. The actor, or a subset of its parameters, are trained to approximately represent the solution to MPC problem. This uses the DPC method [drgona2024LearningConstrained] in an iterative, online training context. This (approximate) MPC-enabled actor works in tandem with a critic network to approximate MPC value targets. A full MPCis then used online, where exactness and constraint satisfaction are most important and expensive.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Ethos of {\\texttt{MPCritic}}\\xspace", "weight": 1.0} -->

{\texttt{soft\,MPCritic}}\xspaceis another realization of this goal, rather than an extension of {\texttt{MPCritic}}\xspace. While {\texttt{MPCritic}}\xspaceemphasizes deterministic MPC, classical dynamic programming principles, and applications where constraints are critical, {\texttt{soft\,MPCritic}}\xspaceemphasizes scalability, motivating sample-based MPC and soft value functions. We develop an algorithm that leverages sample-based MPC for both online control and value target generation, as illustrated in fig:concept. This strategy aligns the MPC and its terminal value function, which makes it possible to leverage a dynamic model trained only on one-step transitions. We further show how this setup is computationally efficient by spreading out the MPCtarget computation over the course of training.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Ethos of {\\texttt{MPCritic}}\\xspace", "weight": 1.0} -->

{\texttt{soft\,MPCritic}}\xspaceeffectively combines key approximations of RL and MPPI for autonomous, self-improvement. During online control, the value-space planner updates to initial open-loop actions $\upsilon$ to align with the soft minimum of value function $\ensuremath{\mathcal{Q}}_\phi$. The updated sequence $\upsilon^+$, along with transition $(s,a,\ell,s')$, is stored in the replay buffer to warm-start the planner's value targets $\ensuremath{\mathcal{V}}^{\text{MPPI}}_\phi$. After a value iteration step, the planner is updated with the new $\ensuremath{\mathcal{Q}}_\phi$, and the further-refined solution $\upsilon^+$ is stored for later reuse.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Fitted $\\ensuremath{\\mathcal{Q}}$-iteration via MPPI", "weight": 1.0} -->

$f_\psi$ is trained to minimize the MSE between its prediction and the observed next state; however, other objectives or multi-step targets may be used. We find it beneficial to mitigate uncertainty in $\psi$ by training an ensemble of dynamic models. MPPI therefore considers a branching dynamic model of the form \psi &\sim p(\psi)\\where models $\psi$ are sampled uniformly. Concurrently, $\ensuremath{\mathcal{Q}}_\phi$ is trained to approximately solve the (soft) Bellman equation, namely, $\ensuremath{\mathcal{Q}}_\phi$ should be such that $\ensuremath{\mathcal{V}}^{\text{MPPI}} \approx \ensuremath{\mathcal{V}}$ in the infinite-horizon definition in eq:soft\_value.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Fitted $\\ensuremath{\\mathcal{Q}}$-iteration via MPPI", "weight": 1.0} -->

Fitted $\ensuremath{\mathcal{Q}}$-iteration is an iterative technique for training $\ensuremath{\mathcal{Q}}_\phi$; it was introduced by [riedmiller2005neural] and made tractable in high-dimensional continuous spaces by [lillicrap2016Continuouscontrol]. Here, we use it as an umbrella term, as it is a prevalent idea and this work is compatible with the stabilization techniques introduced since the nominal algorithm of [riedmiller2005neural].

<!-- chunk {"id": "body-0027", "role": "body", "section": "Fitted $\\ensuremath{\\mathcal{Q}}$-iteration via MPPI", "weight": 1.0} -->

We define the objective $$\mathcal{L}_\ensuremath{\mathcal{Q}} = \text{MSE}\left(\ensuremath{\mathcal{Q}}_\phi, \ell + \gamma \ensuremath{\mathcal{V}}^{\text{MPPI}} \right),$$ where the MSE is computed over a batch from the replay buffer $\mathcal{D}$ containing tuples of the form $(s,a,\ell,s',\upsilon)$. $\ell$ is the observed cost at $s,a$ and $\ensuremath{\mathcal{V}}^{\text{MPPI}}$ is the MPPI value in eq:mppi\_value evaluated at $s'$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Fitted $\\ensuremath{\\mathcal{Q}}$-iteration via MPPI", "weight": 1.0} -->

eq:qfun\_obj is only a nominal objective, as variations involving double or target $\ensuremath{\mathcal{Q}}$-networks are possible [lillicrap2016Continuouscontrol, haarnoja2018Softactorcritic]. If $H=0$ in $\ensuremath{\mathcal{V}}^{\text{MPPI}}$, then eq:qfun\_obj will be a soft version of classical fitted $\ensuremath{\mathcal{Q}}$-iteration powered by MPPI, marking a conceptual similarity to SAC [haarnoja2018Softactorcritic]. Taking $H>0$ embeds short-horizon model information into the targets. This same MPPI is used for online control, making $\ensuremath{\mathcal{Q}}$ aligned with the model-based MPPI value estimate and implicitly extending its prediction horizon. The weights $\phi$ are updated iteratively using some form of gradient descent as new data is added to the replay buffer.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Fitted $\\ensuremath{\\mathcal{Q}}$-iteration via MPPI", "weight": 1.0} -->

$\upsilon$ is included in the replay tuples to make the MPPI target computationally efficient.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Amortized {\\texttt{soft\\,MPCritic}}\\xspacealgorithm", "weight": 1.0} -->

Precise control quickly becomes infeasible as $H \rightarrow\infty$, meaning the number of trajectories is coupled with the prediction horizon. {\texttt{soft\,MPCritic}}\xspaceaddresses this by fixing the prediction horizon and caching long-horizon planning with terminal \ensuremath{\mathcal{Q}}-function, i.e., This enables precise control aimed at global optimality with a tractable number of planning trajectories. alg:mppi is a generic instantiation of this, which can be expanded to incorporate covariance and/or temperature annealing [homburgerOptimalitySuboptimality], baseline policies [wang2025ResidualMPPIOnline,qu2024RLDrivenMPPI], non-Gaussian distributions, and other recent advancements in MPPI [honda2025model].

<!-- chunk {"id": "body-0031", "role": "body", "section": "Amortized {\\texttt{soft\\,MPCritic}}\\xspacealgorithm", "weight": 1.0} -->

\ensuremath{\mathcal{Q}}-function can alleviate sampling challenges during online control, it shifts the burden of computation to $\ensuremath{\mathcal{Q}}$-iteration. Furthermore, for alg:mppi to be successful online, $\ensuremath{\mathcal{Q}}_\phi$ should be aligned with the MPPI controller, motivating the use of MPPI for both online control and in RL updates. Considering a fixed number of trajectory samples, the cost of RL scales with the number of value iteration steps though. {\texttt{soft\,MPCritic}}\xspaceaddresses this issue by amortizing target computations at each value iteration step. Recall eq:u\_iter is an iterative update rule. Thus, the MPPI optimization for RL updates need not start from scratch; open-loop controls $\upsilon$ calculated online can be recycled for target computation. This inspires the proposed warm-starting strategy for target computations, exemplified in alg:warmstart RL.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Amortized {\\texttt{soft\\,MPCritic}}\\xspacealgorithm", "weight": 1.0} -->

The benefits of warm-starting targets as in alg:warmstart RL include: 1) fewer trajectory samples needed for RL updates; and 2) targets are iteratively refined as learning proceeds. Regarding the former, online control demands a sizable number of trajectories to acquire near optimal solutions. Hence, when applied to target initialization, only minor refinement is typically necessary. These refinements occur each time a tuple $(s, a, \ell, s', \upsilon)$ is sampled from the replay buffer, meaning $\upsilon$ adapts with the model and terminal value function throughout training.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Amortized {\\texttt{soft\\,MPCritic}}\\xspacealgorithm", "weight": 1.0} -->

\{\{s,a,r,s',\textcolor{warmstart}{\upsilon^+}\}\}$ Empirically, we observe that warm-starting MPPI targets can be highly effective; with only $\approx 10 \%$ of samples used online, significantly reducing the computational cost of the RL algorithm.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Amortized {\\texttt{soft\\,MPCritic}}\\xspacealgorithm", "weight": 1.0} -->

This can be explained through the weighted structure behind eq:u\_iter. Consider two samples $\varepsilon^{(j)}$ and $\varepsilon^{(i)}$, which are relatively small compared to open-loop controls $\upsilon$, giving the ratio of weights \frac{w(\varepsilon^{(j)})}{w(\varepsilon^{(i)})} \approx \\ \exp \bigg(-\frac{1}{\lambda} \Big(J\big(\tau(\upsilon + \varepsilon^{(j)}, s_0)\big) - J\big(\tau(\upsilon + \varepsilon^{(i)}, s_0)\big) \Big) \bigg).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Amortized {\\texttt{soft\\,MPCritic}}\\xspacealgorithm", "weight": 1.0} -->

The weight ratio ensures that even a linear increase in cost $J$ results in an exponential decrease in influence when updating $\upsilon$. The risk of all samples increasing the costthereby degrading $\upsilon$can be mitigated without increasing sample size by annealing the covariance. Furthermore, as part of the latter benefit, any suboptimal updates are naturally corrected in subsequent iterations, as previous target solutions are recycled to warm-start the optimization. Reusing target solutions in subsequent iterations also helps prevent $\upsilon$ from becoming stale as $\ensuremath{\mathcal{Q}}_\phi$ is continually updated. Thus, amortization via warm-started targets yields substantial computational savings without significantly compromising the overall RL algorithm's performance.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Broader scope of {\\texttt{soft\\,MPCritic}}\\xspace", "weight": 1.0} -->

{\texttt{soft\,MPCritic}}\xspacelives in soft value space; however, it could also be adapted to a traditional DP setting. This can be accomplished by targeting the usual Bellman optimality equation. Further, the resulting value function-augmented MPC would directly minimize cost under the system model. Nonetheless, MPPI is useful in the {\texttt{soft\,MPCritic}}\xspaceframework for several reasons. The model is learned online in tandem with the value function, meaning exact minimization may be detrimental to overall stability and performance over the course of training. Additionally, MPPI is agnostic to model and value networks, making it very scalable, a key bottleneck in the RL-MPC interface [reiter2026synthesis]. Therefore, while MPPI is suboptimal relative to a deterministic optimal control problem [homburgerOptimalitySuboptimality], its benefits are worthwhile.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Case studies", "weight": 1.0} -->

{\texttt{soft\,MPCritic}}\xspaceis tested on two case studies. The first demonstrates the benefits of amortizing the \ensuremath{\mathcal{Q}}-iteration process with {\texttt{soft\,MPCritic}}\xspaceon a classical control environment, measuring computational efficiency and reward as a proxy for solution quality. The second ablates {\texttt{soft\,MPCritic}}\xspaceon a challenging robotics environment, establishing the importance of a terminal value function, modeling uncertainty in the dynamics, and planning for control and target computation. The finalized version is benchmarked relative to standard RL algorithms.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Amortization in Learning", "weight": 1.0} -->

{\texttt{soft\,MPCritic}}\xspaceis evaluated in an online learning setting with unknown dynamics, but known goal of balancing a double inverted pendulum. All learnable components of {\texttt{soft\,MPCritic}}\xspace, $\ensuremath{\mathcal{Q}}_\phi$ and $f_\psi$, are parameterized as neural networks. We analyze the effects of warm-starting and using an ensemble of dynamics models in terms of computation and performance.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Amortization in Learning", "weight": 1.0} -->

The grid of plots in fig:dip displays the performance of four learning configurations for {\texttt{soft\,MPCritic}}\xspace, a full factorial design. As seen in the left-hand plots, {\texttt{soft\,MPCritic}}\xspacewith warm-starting quickly maximizes the reward in almost every seed. This is in stark contrast with cold starting MPPI for computing \ensuremath{\mathcal{Q}}-function targets in the right-hand plots. Cold starting these computations generally increases variance in the learning process but, if given enough iterations, can achieve similarly rewarding solutions. However, this comes with additional compute, whereas warm-starting can recycle the online solution and continually refine it. In this way, the open-loop controls $\upsilon$ stored in the replay buffer are iteratively updated to best approximate the optimal sequence for the current $\ensuremath{\mathcal{Q}}_\phi$ and $f_\psi$. Hence, in this example, only a single iteration is necessary to (approximately) maximize performance, roughly matching that of SAC.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Amortization in Learning", "weight": 1.0} -->

While not always a major difference for this simpler system, using a single dynamic model can result in suboptimal solutions when warm or cold starting. This can be attributed to compounding prediction errors over the planning horizon, which manifests in both value function learning and online control to ultimately hinder performance. Rather, planning over an ensemble provides a degree of robustness to parametric uncertainties, meaning MPPI favors low-cost trajectories with high agreement among the ensemble. As seen in fig:dip, this robustness can aid in tightening the range of rewards when warm-starting. This point is revisited in the next case study where the effects become more pronounced in high-dimensional environments, which can be challenging to accurately model.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Amortization in Learning", "weight": 1.0} -->

Performance of warm and cold starting MPPI target computations when utilizing a single or ensemble of dynamic models $f$. Lines represent the median of $10$ seeds, shading percentiles. The horizontal dashed line corresponds to SAC.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Amortization in Learning", "weight": 1.0} -->

Warm-starting can achieve comparable performance to cold starting, but its greatest utility is possibly in amortizing the cost of the overall This effect is measured and tabulated in tab:sps, comparing the environment steps per second relative to cold starting. As the number of MPPI rollouts $N$ used for target computation increase, all approaches experience a degree of slow down. However, recalling fig:dip, cold starting requires $\geq 5$ iterations to achieve comparable performance to $1$ iteration when warm-starting. Requiring additional iterations brings the unfavorable scaling of cold starting to the forefront. Achieving similar performance with cold starting amounts to a $\geq 50\%$slow down in wall time, depending on the desired solution quality. Hence, we only consider warm-starting target computation for all further experiments for its computational efficiency with minimal sacrifice to performance.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Amortization in Learning", "weight": 1.0} -->

Mean and standard deviation of environment steps per second (SPS) during online learning.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Amortization in Learning", "weight": 1.0} -->

1c 4cMPPI target computation iterations (SPS) $N$ $1$ iter. $1$ iter. $5$ iters. $10$ iters.

<!-- chunk {"id": "body-0045", "role": "body", "section": "High-dimensional Control", "weight": 1.0} -->

To distinguish the critical design choices behind {\texttt{soft\,MPCritic}}\xspace, we ablate the approach on a more challenging robotics problem. Here, we consider the Hopper-v5 environment with unknown dynamics but known goal of maximizing velocity while remaining upright. Preserving all hyperparameters from the previous case study, we ablate the MPPI formulation and its usage throughout alg:warmstart RL. In terms of formulation, we gauge the impact of the terminal \ensuremath{\mathcal{Q}}-function and revisit the benefits of modeling parametric uncertainties with an ensemble. Regarding MPPI's usage, we separately compare substituting a parametric representation, i.e., a neural network as is standard in RL, for online decision-making or \ensuremath{\mathcal{Q}}-function target computation.

<!-- chunk {"id": "body-0046", "role": "body", "section": "High-dimensional Control", "weight": 1.0} -->

Ablation of {\texttt{soft\,MPCritic}}\xspacewith Gaussian prior. Left: using only a dynamics model ensemble ($f$ Ensemble), terminal \ensuremath{\mathcal{Q}}-function ($\ensuremath{\mathcal{Q}}$), or both. Right: using MPPI only for control, \ensuremath{\mathcal{Q}}-function targets, or both. Lines represent the median of $10$ seeds, shading percentiles.

<!-- chunk {"id": "body-0047", "role": "body", "section": "High-dimensional Control", "weight": 1.0} -->

Starting with the left panel of fig:hopper, we can begin to distill the essential MPPI ingredients. If the terminal \ensuremath{\mathcal{Q}}-function is removed such that only the dynamics ensemble remains (denoted as no $\ensuremath{\mathcal{Q}}$ / $f$ Ensemble in fig:hopper), performance collapses. This is to be expected as the \ensuremath{\mathcal{Q}}-function implicitly extends the MPPI planning horizon, and without it, planning is confined to a finite horizon ($H=8$ in this case). Without knowing the true dynamics, extending $H$ further to mitigate this effect is not guaranteed to address this issue. That is not to say the value learning underpinning {\texttt{soft\,MPCritic}}\xspaceis not also vulnerable to model mismatch. This is most evident when we remove the dynamics model ensemble from the MPPI formulation (denoted as $\ensuremath{\mathcal{Q}}$ / no $f$ Ensemble in fig:hopper).

<!-- chunk {"id": "body-0048", "role": "body", "section": "High-dimensional Control", "weight": 1.0} -->

Learning and optimizing the terminal \ensuremath{\mathcal{Q}}-function under the predictions of an erroneous model can hinder performance as indicated by the cumulative reward. Incorporating an ensemble targets this very weakness, as the \ensuremath{\mathcal{Q}}-function is learned to reflect uncertainty in the dynamics, and trajectories are planned subject to this uncertainty.

<!-- chunk {"id": "body-0049", "role": "body", "section": "High-dimensional Control", "weight": 1.0} -->

Moving to the right panel of fig:hopper, we examine where in alg:warmstart RL it is crucial to utilize MPPI. We compare to substituting MPPI with a neural network policy $\mu$ with parameters $\theta$ learned such that $\mu_\theta(s) \approx \argmin_a \ensuremath{\mathcal{Q}}_\phi(s,a)$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "High-dimensional Control", "weight": 1.0} -->

Instead of this DDPG-style strategy, we also tested the use of MPPI for optimizing $\ensuremath{\mathcal{Q}}_\phi$ alone, that is, without any planning; the results were similar and the conclusions in this ablations still held true.

<!-- chunk {"id": "body-0051", "role": "body", "section": "High-dimensional Control", "weight": 1.0} -->

To begin, we ask if it is sufficient to only use MPPI for online control (denoted as Control in fig:hopper), effectively replacing line 10 of alg:warmstart RL with $\ensuremath{\mathcal{V}}(s) \leftarrow \ensuremath{\mathcal{Q}}(s,\mu_\theta(s))$. In the early stages of learning, performance is similar to the full MPPI algorithm; both algorithms benefit from online re-planning despite their initially poor \ensuremath{\mathcal{Q}}-function approximators. However, as learning progresses, misalignment between the neural network policy objective and the true form of the optimal policy $\pp{\pi^\star}{a}{s}$ hinders value learning, and thus, performance. If we only use MPPI for target computation in alg:warmstart RL (denoted as Targets in fig:hopper), the misalignment of $\mu_\theta$ also manifests.

<!-- chunk {"id": "body-0052", "role": "body", "section": "High-dimensional Control", "weight": 1.0} -->

Compounding this fact, $\mu_\theta$ does not benefit from re-planning during online control, and the performance of $\mu_\theta$ is largely dependent on its extraction algorithm from $\ensuremath{\mathcal{Q}}_\phi$. Using MPPIfor both tasks ensures alignment between online control and learning, and benefits from online re-planning without requiring additional policy function approximators.

<!-- chunk {"id": "body-0053", "role": "body", "section": "High-dimensional Control", "weight": 1.0} -->

Cumulative reward for {\texttt{soft\,MPCritic}}\xspacewith uniform prior and RL baselines (SAC and DDPG). Lines represent the median of $10$ seeds, shading percentiles. The horizontal dashed lines corresponds to SAC and DDPG after $10^6$ time steps.

<!-- chunk {"id": "body-0054", "role": "body", "section": "High-dimensional Control", "weight": 1.0} -->

Having settled on these algorithmic primitives, we compare the full {\texttt{soft\,MPCritic}}\xspacealgorithm with standard RL baselines, SAC and DDPG. SAC is included due to its shared roots in soft value-iteration. We include DDPG because of its algorithmic simplicity; omitting techniques such as double \ensuremath{\mathcal{Q}}-networks and temperature auto-tuning utilized by SAC but not by alg:warmstart RL. For conceptual alignment, we deploy alg:mppi with a uniform prior such that {\texttt{soft\,MPCritic}}\xspace, like SAC, is optimizing a Gaussian control distribution for maximum entropy control. Results can be seen in fig:methods. Notably, {\texttt{soft\,MPCritic}}\xspaceexceeds the asymptotic performance of both baselines (measured at $10^6$ time steps) within the first $2\times10^5$ time steps.

<!-- chunk {"id": "body-0055", "role": "body", "section": "High-dimensional Control", "weight": 1.0} -->

With all algorithms sharing the same $\ensuremath{\mathcal{Q}}$-iteration frequency and aligned objectives, the primary distinction of the proposed approach apart is the MPPI planning module. As compared to SAC, $H$-step predictions aid in generating quality soft value function targets, accelerating value learning. Furthermore, online re-planning enables the agent to adapt its behavior based on feedback while avoiding parametric policy extraction as a learning bottleneck. With the planner aligned for both value estimation and control, {\texttt{soft\,MPCritic}}\xspaceoffers a streamlined yet high-performance approach to control.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Conclusions", "weight": 1.0} -->

{\texttt{soft\,MPCritic}}\xspaceis an algorithmic framework for learning MPC in value space via RL. In this work, {\texttt{soft\,MPCritic}}\xspacedoes not leverage specialized model learning objectives and many of the stabilization techniques common in deep RL, yet still achieves strong performance. Specifically, {\texttt{soft\,MPCritic}}\xspacelearns a high-quality value function that enables effective short-horizon planning in settings where the same model fails under direct planning—highlighting the benefit of value-space learning over open-loop rollouts. Our results establish {\texttt{soft\,MPCritic}}\xspaceas a principled foundation for future work, including incorporation of advanced model learning objectives, stability guarantees, and broader MPC-enabled RLalgorithm design.
