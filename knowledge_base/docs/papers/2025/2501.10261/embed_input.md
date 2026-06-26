<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Logarithmic Regret for Nonlinear Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We address the problem of learning to control an unknown nonlinear dynamical system through sequential interactions. Motivated by high-stakes applications in which mistakes can be catastrophic, such as robotics and healthcare, we study situations where it is possible for fast sequential learning to occur. Fast sequential learning is characterized by the ability of the learning agent to incur logarithmic regret relative to a fully-informed baseline. We demonstrate that fast sequential learning is achievable in a diverse class of continuous control problems where the system dynamics depend smoothly on unknown parameters, provided the optimal control policy is persistently exciting. Additionally, we derive a regret bound which grows with the square root of the number of interactions for cases where the optimal policy is not persistently exciting. Our results provide the first regret bounds for controlling nonlinear dynamical systems depending nonlinearly on unknown parameters. We validate the trends our theory predicts in simulation on a simple dynamical system.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Controlling an unknown nonlinear system through repeated sequential interaction is a fundamental problem in controls and reinforcement learning. Recent years have seen considerable impact of this paradigm in application areas ranging from walking robots, mastering games such as go and StarCraft and even fine-tuning large language models. Problems of this form are often analyzed through the lens of Markov Decision Processes (MDP). Indeed, there is a wealth of literature on analyzing interactive sequential decision making in tabular MDPs. Extensions to this framework, typically motivated by studying large state and action spaces together with function approximation, are also abundant in the literature.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, many problems, including certain robotics and healthcare tasks, are more naturally cast through the framework of continuous control. Such problems can be converted to tabular MDPs through discretization of the state and action spaces; however, doing so often results in intractable reinforcement learning problems. Conversely, the continuous control problem can be solved efficiently in special cases, such as the linear quadratic regulator (LQR). Of the above motivating examples, robotic tasks in particular are plagued by costly data-collection. A similar situation arises in healthcare: giving the wrong treatment doses of a medicine repeatedly can have dire consequences. Consequently in these applications one would hope to find *fast learning algorithms* that require as few interactions as possible with the unknown system to meet the desired performance criteria.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the sequel, we measure the performance of an interactive sequential decision-maker by its regret---its performance as compared to the best policy (in a certain class), in hindsight. A fast learning algorithm in such sequential decision making tasks is characterized as one that attains *regret scaling logarithmically in the number of interactions with the unknown environment*. There has been a wealth of literature in characterizing when such rates are achievable in the setting of bandits and analogs for tabular reinforcement learning. However, to date there has been no general characterization of when this is achievable in continuous control for nonlinear systems with nonlinear dependence on the unknown parameters. We thus ask: are there conditions under which such fast learning algorithms exist for continuous control of nonlinear systems with nonlinear parameter dependencies?

<!-- chunk {"id": "body-0006", "role": "body", "section": "Contribution", "weight": 1.0} -->

Our main result answers the question of achievability of logarithmic regret in the affirmative.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Logarithmic Regret in Bandits and RL", "weight": 1.0} -->

The question of whether logarithmic regret is attainable or not is intimately connected with the exploration exploitation trade-off. Beginning with Lai and Robbins in the tabular bandit setting, *gap-dependent* regret bounds have been established showing that logarithmic regret is possible whenever there is a strict separation between the reward of the optimal action and that of a second best, or worse, action. Similar gap sufficient conditions for logarithmic regret also exist in tabular reinforcement learning. In the worst case, or for instance in linear bandits where there is no gap, logarithmic regret is impossible and instead regret scales with the square root of the number of interactions with unknown environment.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Closed-Loop Identifiability and Adaptive Control", "weight": 1.0} -->

Within the system identification community, the exploration-exploitation trade-off is often referred to as the *dual nature of control* and is related to issues of *closed-loop identifiability*. Roughly speaking, closed-loop identifiability issues arise because a fixed control law might not sufficiently excite the system under consideration in the necessary directions in state space (or feature space more generally). Indeed, in the Linear Quadratic Regulator (LQR) setting, Polderman gives an elegant geometric argument showing that the true parameters need to be identified in order to ascertain the optimal control law. It is also interesting to note that, precisely because the minimum variance controller is closed-loop identifiable (in contrast to the more general LQR controller), logarithmic regret can be achieved in this setting. Reiterating the point above: the reason for the impossibility of pure exploitation is precisely a lack of closed-loop identifiability. This insight is leveraged in Simchowitz and Foster and Ziemann and Sandberg to show logarithmic regret is impossible in general in the linear quadratic Gaussian control problem.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Closed-Loop Identifiability and Adaptive Control", "weight": 1.0} -->

However, given some prior information about the system (e.g. if the way the input impacts the state transitions is known), then closed-loop identifiability may hold, making logarithmic regret achievable for LQR. Alternatively, if the policy choice is restricted to a set in which all possible candidate provide closed-loop identifiability of the system parameters, then Lale et al. demonstrate logarithmic regret for the Linear Quadratic Gaussian (LQG).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Closed-Loop Identifiability and Adaptive Control", "weight": 1.0} -->

Closed-loop identifiability issues similarly hinder the achievability of logarithmic regret in the online control of nonlinear systems. In the setting of nonlinear dynamical systems which depend linearly on some unknown parameters, Kakade et al.; Boffi et al. propose algorithms that achieve regret scaling with the square root of the number of interactions. Lale et al. consider linear function approximators for smooth systems, and provide an algorithm achieving regret scaling with the square root of the number of interactions in general, and logarithmic regret if the system is sufficiently smooth. Critically, as with Lale et al., Lale et al. assume that all policies in the policy class provide closed-loop identifiability of the parameters. By contrast, we do not assume a priori access to a policy yielding such identifiability; we show that it suffices that the *unknown* optimal policy yields easy identification and our algorithm then adapts to this property. Moreover, we consider dynamical systems which depend nonlinearly on an unknown parameter, and propose an algorithm that incurs logarithmic regret as long as the optimal policy enables closed-loop identification.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Learning in Dynamical Systems", "weight": 1.0} -->

Our contribution also draws on a recent line of work on learning in dynamical systems beginning with Simchowitz et al.; Faradonbeh et al.. The authors therein show that non-asymptotic parameter recovery from a single trajectory is possible in certain marginally stable, or unstable, linear dynamical systems. Mania et al. leverage the parameter recovery bounds to enable efficient exploration. Non-asymptotic identification of more general nonlinear systems is studied by Sattar and Oymak; Foster et al.; Ziemann and Tu. Treven et al.; Wagenmaker et al.; Lee et al. study control-oriented experiment design in an episodic setting for nonlinear systems.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We study an online learning problem under these dynamics. We consider a learner who has knowledge of the dynamics $f$, but not the parameter $\phi^{*}$. In each episode $n=1,\dots,N$, the learner executes a policy $\pi_{n}$ from the set of policies $\mathopen{}\left\{\pi_{0}\right\}\mathclose{}\cup\Pi$, where $\pi_{0}$ is an initial (possibly randomized) exploration policy, while $\Pi$ is a class of deterministic controllers which take as input a point $x\in\mathbb{R}^{dx}$ and return a control input $u\in\mathbb{R}^{du}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Then, the learner observes a trajectory $(x_{1},u_{1}),\dots(x_{T},u_{T})$ (generated by unrolling with $u_{t}\sim\pi_{n}(x_{t})$); and incurs the cost $J(\pi_{n},\phi^{*})$, where for some cost functions $\{c_{t}\}_{t=1,...,T}$ which are fixed across episodes. The subscript on the expectation denotes that the policy $\pi$ is played, while the superscript denotes that the dynamics are rolled out under $\phi$. The expectation is taken over the noise $w_{t}$ and the policy $\pi_{n}$. We suppose that the policy class $\Pi$ is parametric: $\Pi=\{\pi_{\theta}:\theta\in\mathbb{R}^{d_{\theta}}\}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The learner's objective is to achieve a low sum of costs over episodes. A natural metric is therefore to minimize the regret, defined as We will explore no-regret learners for this setting, for which $\operatorname{Regret}(N)/N\to 0$ as $N\to\infty$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Certainty Equivalent Control", "weight": 1.0} -->

Our learners leverage the principle of certainty equivalence. In particular, the learner uses the data collected from its interactions to pose an estimate $\hat{\phi}$ for the parameter $\phi^{\star}.$ Using this estimate, the learner solves the policy optimization problem, The certainty equivalent policy may then be expressed as a function of the estimated dynamics parameters $\hat{\phi}$ as

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumptions", "weight": 1.0} -->

In order to relate the excess cost achieved by a certainty equivalent controller synthesized under a dynamics estimate $\phi$ to the error in the estimate, $\left\|\phi-\phi^{*}\right\|$, we impose some smoothness assumptions on the dynamics and policy class.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

(Smooth dynamics). The dynamics are four times differentiable with respect to $u$ and $\phi$. Furthermore, for all $(x,u)\in\mathbb{R}^{d_{x}}\times\mathbb{R}^{d_{\Phi}}$, and $i,j\in\{0,1,2,3\}$ such that $1\leq i+j\leq 4$, the derivatives of $f$ satisfy

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

We additionally require that the costs are bounded for policies in the class $\mathopen{}\left\{\pi_{0}\right\}\mathclose{}\cup\Pi$ and all dynamics parameters in a neighborhood of the true parameter. Intuitively, this allows our learning algorithm to occasionally play bad policies without incurring too much excess cost.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

As the task is episodic, the above assumption holds if the stage costs are uniformly bounded for all $x\in\mathbb{R}^{d_{x}}$ and $u\in\mathbb{R}^{d_{u}}$. Alternatively, if the stage costs are smooth, the above condition holds if the states and inputs are bounded with high probability. This is satisfied for $\Pi$ by the smoothness of the dynamics (Assumption 1) and exploitation policy class (Assumption 2). A mild assumption that the initial policy $\pi_{0}$ plays bounded inputs suffices to guarantee the above condition also holds for $\pi_{0}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

We additionally suppose that the certainty equivalent controller parameters, as a function of the estimated dynamics $\phi$, are locally smooth near the true dynamics $\phi^{*}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

It is shown in Proposition 6 of Wagenmaker et al. that this condition holds if the minimizer of $J(\pi_{\theta},\phi_{\star})$ is unique, and $\nabla_{\theta}^{2}J(\pi_{\theta},\phi_{\star})\succ 0$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

In order to bound the parameter recovery error in terms of the prediction error, additional identifiability conditions are needed. Ziemann et al. show that a rather minimal Lojasiewicz condition relating the sharpness of an objective to its manifold of minimizers is sufficient for learning from dependent data. The following definition of a Lojasiewicz policy is taken from Lee et al. and extends the corresponding definition from Ziemann et al. to decision-making. In the setting of Lee et al., the following definition of a Lojasiewicz policy bounds the estimation error $\left\|\phi-\phi^{*}\right\|$ as a function of the prediction error $\operatorname{Err}_{\pi}^{\phi^{*}}(\phi)$ for all dynamics parameters $\phi$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Assumption 5", "weight": 1.0} -->

(Initial Lojasiewicz policy). Fix some positive constant $C_{Loja}$ and $\alpha\in(1/4,1/2]$. The learner has access to a policy $\pi_{0}$ which is $(C_{Loja},\alpha)$-Lojasiewicz (here, we do not require that $\pi_{0}\in\Pi$; furthermore, we allow $\pi_{0}$ to be randomized).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 5", "weight": 1.0} -->

This is satisfied in linear systems with $\alpha=1/2$ if the initial controller $\pi_{0}$ plays Gaussian noise as input, and both the controller noise and process noise have positive definite covariance matrices.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 5", "weight": 1.0} -->

While Assumption 5 ensures that the learner can identify the true dynamics $\phi^{*}$ using only data collected under $\pi_{0}$, the rate of recovery may be slow under only the assumptions listed previously. In order to obtain polylogarithmic regret bounds, we require the assumption that the optimal controller, defined by $\theta^{*}\triangleq\argmin_{\theta}J(\pi_{\theta},\phi_{\star})$, is persistently exciting. Persistence of excitation for a nonlinear dynamical system involves the positive definiteness of the matrix where $Df(x_{t},u_{t},\phi^{*})$ denotes the Jacobian of $f$ with respect to $\phi$ evaluated at $\phi^{*}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Assumption 5", "weight": 1.0} -->

It can be show that $\Sigma^{\pi}$ is a positive scalar multiple of the Fisher Information matrix (when the system evolves according to $\phi^{*}$ and $\pi$) and hence this condition is equivalent to requiring the positive definiteness of the Fisher Information matrix when the system evolves according to $\phi^{*}$ and $\pi$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Assumption 6", "weight": 1.0} -->

(Persistency of excitation for the optimal controller). The optimal policy under the true dynamics $\phi^{*}$, denoted $\pi_{\theta^{*}}\triangleq\pi_{\theta^{*}(\phi^{*})}$, is persistently exciting, i.e. for some $\lambda_{\min}>0$, Note that the above assumption is not satisfied in LQR in general when both the $A^{*}$ and $B^{*}$ matrices are unknown. However, Lee et al. show that a sufficient condition for Assumption 6 to hold in linear systems is that either 1) the $A^{*}$ matrix is known and the optimal controller $K^{*}$ has full row rank or 2) the $B^{*}$ matrix is known.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Assumption 6", "weight": 1.0} -->

Finally, we reiterate that in the event that 6 does not hold, we can obtain slower, but still sublinear regret rates under very general conditions. See Appendix A of the extended manuscript for details.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Fast Learning", "weight": 1.0} -->

Under Assumptions 1, 2, 3, 4, 5, and 6, we give an algorithm (Algorithm 1) based on the aforementioned certainty equivalence principle which achieves polylogarithmic regret in our online nonlinear control setting. Given an initial Lojasiewicz policy $\pi_{0}$, the exploitation policy class $\Pi$, the number of episodes $N$, the number of initial phase episodes $N_{\mathsf{phase\,1}}$ (where $0\leq N_{\mathsf{phase\,1}}\leq N$), and a confidence radius $r_{\Phi}$, the algorithm proceeds in two phases.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Fast Learning", "weight": 1.0} -->

The confidence ball is centered at $\phi_{0}$, which is the solution to a nonlinear least squares problem, With a sufficiently small $r_{\Phi}$, and conditioned on the event $\phi^{*}\in\Phi$, we show that policies synthesized using estimates that fall within this set enjoy a positive definite Fisher Information; equivalently, the prediction error $\operatorname{Err}_{\pi}^{\phi^{*}}(\phi)$ is strongly convex on $\Phi$ for all certainty equivalent controllers $\pi$ synthesized with dynamics estimates $\phi\in\Phi$. This motivates an online convex optimization procedure in the second phase.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Fast Learning", "weight": 1.0} -->

In the second phase, the learner interacts with the system by playing policies synthesized using parameter estimates from $\Phi$. The learner produces successive estimates $\phi_{1},\phi_{2},...$ of the true dynamics $\phi^{*}$ using observations of the prediction error, where the prediction error for a dynamics estimate $\phi$ under the policy $\pi$ is defined as More specifically, the learner uses the certainty equivalent policy $\pi$ corresponding to its current estimate of $\phi^{*}$ to collect a single trajectory $\mathcal{D}=\mathopen{}\left\{(x_{t},u_{t},x_{t+1})\right\}\mathclose{}_{t=1,\dots,T}$. The square loss of a dynamics estimate $\phi$ on the dataset $\mathcal{D}$ is and the learner updates its estimate of $\phi^{*}$ using the gradient $\nabla l_{D}(\phi)$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Fast Learning", "weight": 1.0} -->

1:Exploration policy π0, exploitation policy class Π, number of episodes N, number of initial phase episodes Nphase 1, confidence radius rΦ 2:Play π0 for Nphase 1 episodes to collect the dataset 𝒟0:= {(xt, n, ut, n, xt + 1, n)}t = 1,..., Tn = 1,..., Nphase 1 ⊳ First phase 3:Set ϕ0 via least squares using 𝒟0 5:for i = 0, 1, 2, …, N − Nphase 1 do ⊳ Second phase 7: Play πi + 1 to collect dataset 𝒟i + 1:= {(xt(i + 1), ut(i + 1), xt + 1(i + 1))}t = 1,..., T 9: $\phi_{i+1}\leftarrow\argmin_{\phi\in\Phi}\|\phi-\psi_{i+1}\|$ Algorithm 1 Continuous Refinement In general, the nonlinear least squares problem and policy optimization problem may be computationally challenging.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Fast Learning", "weight": 1.0} -->

The focus of this work is to understand the statistical complexity of the problem rather than the computational complexity. However, it is worth noting that the online stochastic optimization procedure is computationally efficient and therefore the learner may often efficiently execute the second phase of the dynamics estimation procedure online. Additionally, for particular systems and objectives, the policy optimization problem may be efficient. This is the case, for instance, if the optimal solution to the policy optimization problem can be achieved via feedback linearization by choosing the input to cancel out some portion of the dynamics. We consider such an example in Section 4.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Fast Learning", "weight": 1.0} -->

Our main result bounds the regret incurred by Algorithm 1 in terms of $N$ and $N_{\mathsf{phase\,1}}$ under the aforementioned smoothness and identifiability conditions.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Toy Experiment", "weight": 1.0} -->

We provide an simple example to illustrate the fast regret rates attained by Algorithm 1. For more experiments, see section 4.2. Consider the two-dimensional nonlinear system where $x_{t},u_{t},w_{t},\phi^{*}\in\mathbb{R}^{2}$, and with $x_{1}=\begin{bmatrix}0&0\end{bmatrix}^{\top}$. The noise $w_{t}$ has a standard normal distribution. We choose the unknown parameter $\phi^{*}=\begin{bmatrix}0.25&0.25\end{bmatrix}^{\top}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Toy Experiment", "weight": 1.0} -->

In this experiment, we use the horizon $T=10$ and the number of episodes $N=3000$. We will consider the quadratic cost functions The policy class $\Pi$ consists of controllers parameterized by the dynamics estimate $\hat{\phi}$, with It can be shown that the dynamics and policy class satisfy Assumption 6. Our initial policy $\pi_{0}$ plays the controller $\pi_{\phi}$ corresponding to $\phi=\begin{bmatrix}0&0\end{bmatrix}^{\top}$, which can be shown to satisfy Assumption 5. In place of choosing $N_{\mathsf{phase\,1}}$ or $r_{\Phi}$ according to Theorem 1, we heuristically set $N_{\mathsf{phase\,1}}=100$ and $r_{\Phi}=0.2$. We note that the dynamics are not uniformly bounded globally, however they are uniformly bounded with high probability.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Toy Experiment", "weight": 1.0} -->

Under this choice of cost function and policy class, the learner's objective is to keep the system near the origin. Figure 1 illustrates the performance (measured in terms of regret) of Algorithm 1 on the toy dynamical system. The first plot shows that, after the initial $N_{\mathsf{phase\,1}}$-episode initial phase, the excess cost incurred per round begins to decay quickly, leading to the regret growing polylogarithmically with $N$. The second plot is included to better illustrate the regret attained by Algorithm 1; after the initial phase, the average regret appears to grow as a polynomial of the logarithm of the iteration. This toy example highlights the fast regret rates attained by Algorithm 1.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Cartpole Experiment", "weight": 1.0} -->

In this section, we complement our simple numerical example with an implementation of Algorithm 1 on a cartpole system defined by the dynamics: Here, $p$ is the position of the cart, $\theta$ is the angle of the pole from the upright position, $u$ is the control force; the state vector is given by $x=\begin{bmatrix}p&\dot{p}&\theta&\dot{\theta}\end{bmatrix}^{\top}$ and the input is given by $u$. Also, $M$ is the mass of the cart, $m$ is the mass of the pole, $l$ is the length of the pole, $g$ is the acceleration due to gravity, $b_{x}$ is the friction coefficient for the cart, and $b_{\theta}$ is the friction coefficient for the pole. We discretize the system using the Euler approach using a timestep of $dt=0.2$. We also include additive zero mean Gaussian noise with covariance $0.05I_{4}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Cartpole Experiment", "weight": 1.0} -->

The unknown parameters are $\phi^{*}=\begin{bmatrix}M&m&l&b_{x}&b_{\theta}\end{bmatrix}^{\top}=\begin{bmatrix}1&0.1&1&1&1\end{bmatrix}^{\top}$. For every episode, the system starts from the upright position, given by the state $x_{0}=\begin{bmatrix}0&0&0&0\end{bmatrix}^{\top}$. The desired behavior is to keep the pole upright with the cart positioned at the origin for a time horizon of $T=20$ timesteps. This behavior is described by the quadratic cost functions $c_{t}(x,u)=\left\|x\right\|^{2}+0.1u^{2},c_{T+1}(x)=\left\|x\right\|^{2}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Cartpole Experiment", "weight": 1.0} -->

Our exploitation policy class $\Pi$ is given by neural networks with layer sizes $$ and ReLU activation functions. For computational reasons, in place of directly solving for the certainty equivalent policy for each parameter estimate $\phi_{i}$, we simultaneously update a dynamics estimate $\phi_{i}$ and train our control parameters $\theta_{i}$ as follows. At each iteration, we update our estimate of $\phi_{i}$ as in Algorithm 1 to get a new estimate $\phi_{i+1}$; we then use the Adam optimizer to train a new set of control parameters $\theta_{i+1}$ to minimize the cost functions using trajectories sampled with the dynamics $\phi_{i+1}$ (in place of $\phi^{*}$), warm-starting the optimizer with the previous control parameters $\theta_{i}$. The initial exploration policy $\pi_{0}$ is given by bounded random noise scaled to match a predefined energy budget over the time horizon $T$; we choose a budget of $0.1T$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Cartpole Experiment", "weight": 1.0} -->

Finally, to illustrate the performance of our algorithm, we trained a "best-in-class" controller $\pi^{*}$ using trajectories sampled with the true dynamics $\phi^{*}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Cartpole Experiment", "weight": 1.0} -->

In this experiment, we use the horizon $T=20$ and the number of episodes $N=300$. Finally, we note that in place of choosing the number of initial phase episodes $N_{\mathsf{phase\,1}}$, the confidence radius $r_{\Phi}$, and the step sizes $\eta_{i}$ according to Corollary 3.2 and Algorithm 1, we heuristically set $N_{\mathsf{phase\,1}}=1$, $r_{\Phi}=1$, and $\eta_{i}=100/(100+i)$. The cost of each controller was evaluated by sampling $10000$ trajectories and using the average cost; for computational reasons, we chose to only evaluate the cost every $10$ iterations.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have introduced Algorithm 1 for online learning in a broad class of nonlinear dynamical systems. We have also proven a general sufficient condition for polylogarithmic regret under a natural curvature condition --- when the Fisher information matrix at the optimal policy is positive definite (detailed in our Assumption 6) --- and show that polylogarithmic regret is achieved by our Algorithm 1. Finally, we have verified the performance of Algorithm 1 on a toy dynamical system and show that it achieves a fast regret rate in practice. Future work could extend these results to the single-trajectory setting. In particular, it could be interesting to extend the $\log^{2}N$ regret rates of Cassel et al. and Lee et al. in the single-trajectory partially known linear setting to the setting with nonlinear dynamics. Another exciting avenue for future work is to design an online learning algorithm which deploys optimal experiment design techniques to optimally balance exploration and exploitation. Doing so may result in algorithms which automatically determine whether 6 is satisfied. Such an algorithm could achieve logarithmic regret if possible, and otherwise achieve $\sqrt{N}$ regret.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Additionally, it may be possible to show improved dependence on the system-theoretic constants by using this approach.
