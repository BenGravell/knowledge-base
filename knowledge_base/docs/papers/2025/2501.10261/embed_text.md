## Introduction

Controlling an unknown nonlinear system through repeated sequential interaction is a fundamental problem in controls and reinforcement learning. Recent years have seen considerable impact of this paradigm in application areas ranging from walking robots, mastering games such as go and StarCraft and even fine-tuning large language models. Problems of this form are often analyzed through the lens of Markov Decision Processes (MDP). Indeed, there is a wealth of literature on analyzing interactive sequential decision making in tabular MDPs. Extensions to this framework, typically motivated by studying large state and action spaces together with function approximation, are also abundant in the literature.

However, many problems, including certain robotics and healthcare tasks, are more naturally cast through the framework of continuous control. Such problems can be converted to tabular MDPs through discretization of the state and action spaces; however, doing so often results in intractable reinforcement learning problems. Conversely, the continuous control problem can be solved efficiently in special cases, such as the linear quadratic regulator (LQR). Of the above motivating examples, robotic tasks in particular are plagued by costly data-collection. A similar situation arises in healthcare: giving the wrong treatment doses of a medicine repeatedly can have dire consequences. Consequently in these applications one would hope to find *fast learning algorithms* that require as few interactions as possible with the unknown system to meet the desired performance criteria.

In the sequel, we measure the performance of an interactive sequential decision-maker by its regret---its performance as compared to the best policy (in a certain class), in hindsight. A fast learning algorithm in such sequential decision making tasks is characterized as one that attains *regret scaling logarithmically in the number of interactions with the unknown environment*. There has been a wealth of literature in characterizing when such rates are achievable in the setting of bandits and analogs for tabular reinforcement learning. However, to date there has been no general characterization of when this is achievable in continuous control for nonlinear systems with nonlinear dependence on the unknown parameters. We thus ask: are there conditions under which such fast learning algorithms exist for continuous control of nonlinear systems with nonlinear parameter dependencies?

### Contribution

Our main result answers the question of achievability of logarithmic regret in the affirmative.

### Theorem 1.1 (Informal version of the main result)

If the optimal policy solving a given continuous control task is identifiable from an experiment running the optimal policy, polylogarithmic regret is attained by our Algorithm 1.

The crux of our contribution is thus to establish a natural condition for logarithmic regret in nonlinear control problems and to provide a novel algorithm leveraging this condition which achieves logarithmic regret. To the best of our knowledge, this is the first algorithm achieving (poly-)logarithmic regret in general nonlinear control problems.

The intuition behind our result is as follows. If the data collected by running the optimal policy is sufficiently informative about the unknown parameters, then it is unnecessary to inject exploratory noise to perform online control. In particular, a policy which is near optimal will enjoy similarly informative data collection, allowing the learner to gradually approach the optimal policy by playing certainty equivalent controllers synthesized with estimates of the dynamics parameters. We formalize this intuition with a persistence of excitation condition, asking that the Fisher information matrix of the optimal policy is positive definite.

Finally, for completeness, we also provide an algorithm attaining sublinear regret in the absence of our identifiability condition. This result can be found in Appendix A along with all proofs.

### Related Work

### Logarithmic Regret in Bandits and RL

The question of whether logarithmic regret is attainable or not is intimately connected with the exploration exploitation trade-off. Beginning with Lai and Robbins in the tabular bandit setting, *gap-dependent* regret bounds have been established showing that logarithmic regret is possible whenever there is a strict separation between the reward of the optimal action and that of a second best, or worse, action. Similar gap sufficient conditions for logarithmic regret also exist in tabular reinforcement learning. In the worst case, or for instance in linear bandits where there is no gap, logarithmic regret is impossible and instead regret scales with the square root of the number of interactions with unknown environment.

### Closed-Loop Identifiability and Adaptive Control

Within the system identification community, the exploration-exploitation trade-off is often referred to as the *dual nature of control* and is related to issues of *closed-loop identifiability*. Roughly speaking, closed-loop identifiability issues arise because a fixed control law might not sufficiently excite the system under consideration in the necessary directions in state space (or feature space more generally). Indeed, in the Linear Quadratic Regulator (LQR) setting, Polderman gives an elegant geometric argument showing that the true parameters need to be identified in order to ascertain the optimal control law. It is also interesting to note that, precisely because the minimum variance controller is closed-loop identifiable (in contrast to the more general LQR controller), logarithmic regret can be achieved in this setting. Reiterating the point above: the reason for the impossibility of pure exploitation is precisely a lack of closed-loop identifiability. This insight is leveraged in Simchowitz and Foster and Ziemann and Sandberg to show logarithmic regret is impossible in general in the linear quadratic Gaussian control problem. However, given some prior information about the system (e.g. if the way the input impacts the state transitions is known), then closed-loop identifiability may hold, making logarithmic regret achievable for LQR. Alternatively, if the policy choice is restricted to a set in which all possible candidate provide closed-loop identifiability of the system parameters, then Lale et al. demonstrate logarithmic regret for the Linear Quadratic Gaussian (LQG).

Closed-loop identifiability issues similarly hinder the achievability of logarithmic regret in the online control of nonlinear systems. In the setting of nonlinear dynamical systems which depend linearly on some unknown parameters, Kakade et al.; Boffi et al. propose algorithms that achieve regret scaling with the square root of the number of interactions. Lale et al. consider linear function approximators for smooth systems, and provide an algorithm achieving regret scaling with the square root of the number of interactions in general, and logarithmic regret if the system is sufficiently smooth. Critically, as with Lale et al., Lale et al. assume that all policies in the policy class provide closed-loop identifiability of the parameters. By contrast, we do not assume a priori access to a policy yielding such identifiability; we show that it suffices that the *unknown* optimal policy yields easy identification and our algorithm then adapts to this property. Moreover, we consider dynamical systems which depend nonlinearly on an unknown parameter, and propose an algorithm that incurs logarithmic regret as long as the optimal policy enables closed-loop identification.

### Learning in Dynamical Systems

Our contribution also draws on a recent line of work on learning in dynamical systems beginning with Simchowitz et al.; Faradonbeh et al.. The authors therein show that non-asymptotic parameter recovery from a single trajectory is possible in certain marginally stable, or unstable, linear dynamical systems. Mania et al. leverage the parameter recovery bounds to enable efficient exploration. Non-asymptotic identification of more general nonlinear systems is studied by Sattar and Oymak; Foster et al.; Ziemann and Tu. Treven et al.; Wagenmaker et al.; Lee et al. study control-oriented experiment design in an episodic setting for nonlinear systems.

### Notation

The Jacobian of a vector-valued function $g:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{m}}$ is denoted $Dg$, and follows the convention for any $x \in {\mathbb{R}}^{n}$, the rows of $Dg{(x)}$ are the transposed gradients of $g_{i}{(x)}$. The $p^{th}$ order derivative of $g$ is denoted by $D^{(p)}g$. Note that for $p \geq 2$, $D^{(p)}g{(x)}$ is a tensor for any $x \in {\mathbb{R}}^{n}$. The operator norm of such a tensor is denoted by $\left\| {D^{(p)}g{(x)}} \right\|_{op}$. For a function $f:{\mathsf{X}\rightarrow{\mathbb{R}}^{d_{y}}}$, we define $\left\| f \right\|_{\infty}{}{\sup_{x \in \mathsf{X}}\left\| {f{(x)}} \right\|}$. A Euclidean norm ball of radius $r$ centered at $x$ is denoted $\mathcal{B}{(x,r)}$.

## Problem Formulation

We consider a nonlinear dynamical system given by the dynamics

where the state $x_{t} \in {\mathbb{R}}^{d_{x}}$; the input $u_{t} \in {\mathbb{R}}^{d_{u}}$; and the additive noise $w_{t} \in {\mathbb{R}}^{d_{x}}$, with $w_{t}\overset{i.i.d.}{\sim}N{(0,{\sigma^{2}I})}$. Let $x_{1} \in {\mathbb{R}}^{d_{x}}$ be arbitrary. Here, $f$ is the dynamics function and depends on a parameter $\phi^{\ast} \in {\mathbb{R}}^{d_{\Phi}}$. We assume that there exists some positive $B$ such that $\left\| \phi^{\ast} \right\| \leq B$ and $\left\| {f{( \cdot, \cdot,\phi)}} \right\|_{\infty} \leq B$ for all $\phi \in {\mathbb{R}}^{d_{\Phi}}$ satisfying $\left\| \phi \right\| \leq B$.

We study an online learning problem under these dynamics. We consider a learner who has knowledge of the dynamics $f$, but not the parameter $\phi^{\ast}$. In each episode $n = {1,\ldots,N}$, the learner executes a policy $\pi_{n}$ from the set of policies ${\left\{ \pi_{0} \right\}} \cup \Pi$, where $\pi_{0}$ is an initial (possibly randomized) exploration policy, while $\Pi$ is a class of deterministic controllers which take as input a point $x \in {\mathbb{R}}^{dx}$ and return a control input $u \in {\mathbb{R}}^{du}$. Then, the learner observes a trajectory ${(x_{1},u_{1})},{\ldots{(x_{T},u_{T})}}$ (generated by unrolling with $u_{t} \sim {\pi_{n}{(x_{t})}}$); and incurs the cost $J{(\pi_{n},\phi^{\ast})}$, where

for some cost functions ${\{ c_{t}\}}_{t = {1,\ldots,T}}$ which are fixed across episodes. The subscript on the expectation denotes that the policy $\pi$ is played, while the superscript denotes that the dynamics are rolled out under $\phi$. The expectation is taken over the noise $w_{t}$ and the policy $\pi_{n}$. We suppose that the policy class $\Pi$ is parametric: $\Pi = {\{\pi_{\theta}:{\theta \in {\mathbb{R}}^{d_{\theta}}}\}}$.

The learner's objective is to achieve a low sum of costs over episodes. A natural metric is therefore to minimize the regret, defined as

We will explore no-regret learners for this setting, for which ${{{Regret}{(N)}}/N}\rightarrow 0$ as $N\rightarrow\infty$.

### Certainty Equivalent Control

Our learners leverage the principle of certainty equivalence. In particular, the learner uses the data collected from its interactions to pose an estimate $\hat{\phi}$ for the parameter $\phi^{\star}.$ Using this estimate, the learner solves the policy optimization problem,

The certainty equivalent policy may then be expressed as a function of the estimated dynamics parameters $\hat{\phi}$ as

### Assumptions

In order to relate the excess cost achieved by a certainty equivalent controller synthesized under a dynamics estimate $\phi$ to the error in the estimate, $\left\| {\phi - \phi^{\ast}} \right\|$, we impose some smoothness assumptions on the dynamics and policy class.

### Assumption 1

(Smooth dynamics). The dynamics are four times differentiable with respect to $u$ and $\phi$. Furthermore, for all ${(x,u)} \in {{\mathbb{R}}^{d_{x}} \times {\mathbb{R}}^{d_{\Phi}}}$, and ${i,j} \in {\{ 0,1,2,3\}}$ such that $1 \leq {i + j} \leq 4$, the derivatives of $f$ satisfy

### Assumption 2

(Smooth exploitation policy class). For all policies $\pi \in \Pi$ and $x \in \mathcal{X}$, the function $\pi_{\theta}{(x)}$ is four-times differentiable in $\theta$. Furthermore $\left\| {D_{\theta}^{(i)}\pi_{\theta}{(x)}} \right\|_{op} \leq L_{\theta}$ for all $i = {1,\ldots,4}$, all $\theta \in {\mathbb{R}}^{d_{\theta}}$, and all $x \in \mathcal{X}$.

We additionally require that the costs are bounded for policies in the class ${\left\{ \pi_{0} \right\}} \cup \Pi$ and all dynamics parameters in a neighborhood of the true parameter. Intuitively, this allows our learning algorithm to occasionally play bad policies without incurring too much excess cost.

### Assumption 3

(Bounded costs). There exists ${r_{cost}{(\phi^{\ast})}} > 0$ such that for all $\phi \in {\mathcal{B}{(\phi^{\ast},{r_{cost}{(\phi^{\ast})}})}}$, and all $\pi \in {\left\{ \pi_{0} \right\}} \cup \Pi$, we have ${{\mathbb{E}}_{\pi}^{\phi}\left\lbrack \left( {{c_{t + 1}{(x_{t + 1})}} + {\sum_{t = 1}^{T}{c_{t}{(x_{t},u_{t})}}}} \right)^{2} \right\rbrack} \leq L_{cost}$.

As the task is episodic, the above assumption holds if the stage costs are uniformly bounded for all $x \in {\mathbb{R}}^{d_{x}}$ and $u \in {\mathbb{R}}^{d_{u}}$. Alternatively, if the stage costs are smooth, the above condition holds if the states and inputs are bounded with high probability. This is satisfied for $\Pi$ by the smoothness of the dynamics (Assumption 1) and exploitation policy class (Assumption 2). A mild assumption that the initial policy $\pi_{0}$ plays bounded inputs suffices to guarantee the above condition also holds for $\pi_{0}$.

We additionally suppose that the certainty equivalent controller parameters, as a function of the estimated dynamics $\phi$, are locally smooth near the true dynamics $\phi^{\ast}$.

### Assumption 4

There exists some $r_{CE} > 0$ such that for all $\phi \in {\mathcal{B}{(\phi^{\ast},r_{CE})}}$,

${{{\nabla_{\theta}J}{(\pi_{\theta},\phi)}}\mid}_{\theta = {\theta^{\ast}{(\phi)}}} = 0$,

$\theta^{\ast}{(\phi)}$ is three times differentiable and $\left\| {D_{\Phi}^{(i)}\theta^{\ast}{(\phi)}} \right\|_{op} \leq L_{CE}$ for some $L_{CE} > 0$ and $i \in {\{ 1,2,3\}}$.

It is shown in Proposition 6 of Wagenmaker et al. that this condition holds if the minimizer of $J{(\pi_{\theta},\phi_{\star})}$ is unique, and ${{\nabla_{\theta}^{2}J}{(\pi_{\theta},\phi_{\star})}} \succ 0$.

In order to bound the parameter recovery error in terms of the prediction error, additional identifiability conditions are needed. Ziemann et al. show that a rather minimal Lojasiewicz condition relating the sharpness of an objective to its manifold of minimizers is sufficient for learning from dependent data. The following definition of a Lojasiewicz policy is taken from Lee et al. and extends the corresponding definition from Ziemann et al. to decision-making. In the setting of Lee et al., the following definition of a Lojasiewicz policy bounds the estimation error $\left\| {\phi - \phi^{\ast}} \right\|$ as a function of the prediction error ${Err}_{\pi}^{\phi^{\ast}}{(\phi)}$ for all dynamics parameters $\phi$.

### Definition 2.1

For positive numbers $C$ and $\alpha$, say that a policy $\pi \in \Pi$ is $(C,\alpha)$-Lojasiewicz if

Next, to ensure parameter recovery is possible for the learner, we make the following assumption regarding identifiability.

### Assumption 5

(Initial Lojasiewicz policy). Fix some positive constant $C_{Loja}$ and $\alpha \in {({1/4},{1/2}\rbrack}$. The learner has access to a policy $\pi_{0}$ which is $(C_{Loja},\alpha)$-Lojasiewicz (here, we do not require that $\pi_{0} \in \Pi$; furthermore, we allow $\pi_{0}$ to be randomized).

This is satisfied in linear systems with $\alpha = {1/2}$ if the initial controller $\pi_{0}$ plays Gaussian noise as input, and both the controller noise and process noise have positive definite covariance matrices.

While Assumption 5 ensures that the learner can identify the true dynamics $\phi^{\ast}$ using only data collected under $\pi_{0}$, the rate of recovery may be slow under only the assumptions listed previously. In order to obtain polylogarithmic regret bounds, we require the assumption that the optimal controller, defined by $\theta^{\ast}{}{}_{\theta}J{(\pi_{\theta},\phi_{\star})}$, is persistently exciting. Persistence of excitation for a nonlinear dynamical system involves the positive definiteness of the matrix

where $Df{(x_{t},u_{t},\phi^{\ast})}$ denotes the Jacobian of $f$ with respect to $\phi$ evaluated at $\phi^{\ast}$. It can be show that $\Sigma^{\pi}$ is a positive scalar multiple of the Fisher Information matrix (when the system evolves according to $\phi^{\ast}$ and $\pi$) and hence this condition is equivalent to requiring the positive definiteness of the Fisher Information matrix when the system evolves according to $\phi^{\ast}$ and $\pi$.

### Assumption 6

(Persistency of excitation for the optimal controller). The optimal policy under the true dynamics $\phi^{\ast}$, denoted $\pi_{\theta^{\ast}}{}\pi_{\theta^{\ast}{(\phi^{\ast})}}$, is persistently exciting, i.e. for some $\lambda_{\min} > 0$,

Note that the above assumption is not satisfied in LQR in general when both the $A^{\ast}$ and $B^{\ast}$ matrices are unknown. However, Lee et al. show that a sufficient condition for Assumption 6 to hold in linear systems is that either 1) the $A^{\ast}$ matrix is known and the optimal controller $K^{\ast}$ has full row rank or 2) the $B^{\ast}$ matrix is known.

Finally, we reiterate that in the event that 6 does not hold, we can obtain slower, but still sublinear regret rates under very general conditions. See Appendix A of the extended manuscript for details.

## Fast Learning

Under Assumptions 1, 2, 3, 4, 5, and 6, we give an algorithm (Algorithm 1) based on the aforementioned certainty equivalence principle which achieves polylogarithmic regret in our online nonlinear control setting. Given an initial Lojasiewicz policy $\pi_{0}$, the exploitation policy class $\Pi$, the number of episodes $N$, the number of initial phase episodes $N_{{\mathsf{p}\mathsf{h}\mathsf{a}\mathsf{s}\mathsf{e}}\, 1}$ (where $0 \leq N_{{\mathsf{p}\mathsf{h}\mathsf{a}\mathsf{s}\mathsf{e}}\, 1} \leq N$), and a confidence radius $r_{\Phi}$, the algorithm proceeds in two phases.

In the first phase, the learner collects a dataset ${\{{(x_{t}^{k},u_{t}^{k},x_{t + 1}^{k})}\}}_{t = {1,\ldots,T}}^{k = {1,\ldots,N_{{\mathsf{p}\mathsf{h}\mathsf{a}\mathsf{s}\mathsf{e}}\, 1}}}$ using $\pi_{0}$, and finds an confidence ball $\Phi$ with a radius of $r_{\Phi}$ which contains the true dynamics $\phi^{\ast}$ with high probability. The confidence ball is centered at $\phi_{0}$, which is the solution to a nonlinear least squares problem,

With a sufficiently small $r_{\Phi}$, and conditioned on the event $\phi^{\ast} \in \Phi$, we show that policies synthesized using estimates that fall within this set enjoy a positive definite Fisher Information; equivalently, the prediction error ${Err}_{\pi}^{\phi^{\ast}}{(\phi)}$ is strongly convex on $\Phi$ for all certainty equivalent controllers $\pi$ synthesized with dynamics estimates $\phi \in \Phi$. This motivates an online convex optimization procedure in the second phase.

In the second phase, the learner interacts with the system by playing policies synthesized using parameter estimates from $\Phi$. The learner produces successive estimates $\phi_{1},\phi_{2},\ldots$ of the true dynamics $\phi^{\ast}$ using observations of the prediction error, where the prediction error for a dynamics estimate $\phi$ under the policy $\pi$ is defined as

More specifically, the learner uses the certainty equivalent policy $\pi$ corresponding to its current estimate of $\phi^{\ast}$ to collect a single trajectory $\mathcal{D} = {\left\{ {(x_{t},u_{t},x_{t + 1})} \right\}}_{t = {1,\ldots,T}}$. The square loss of a dynamics estimate $\phi$ on the dataset $\mathcal{D}$ is

and the learner updates its estimate of $\phi^{\ast}$ using the gradient ${\nabla l_{D}}{(\phi)}$.

1:Exploration policy π0, exploitation policy class Π, number of episodes N, number of initial phase episodes Nphase 1, confidence radius rΦ
2:Play π0 for Nphase 1 episodes to collect the dataset 𝒟0:= {(xt, n,ut, n,xt + 1, n)}t = 1, …, Tn = 1, …, Nphase 1 ⊳ First phase
3:Set ϕ0 via least squares using 𝒟0
5:for i = 0, 1, 2, …, N − Nphase 1 do ⊳ Second phase
7: Play πi + 1 to collect dataset 𝒟i + 1:= {(xt(i+1),ut(i+1),xt + 1(i+1))}t = 1, …, T
Algorithm 1 Continuous Refinement

In general, the nonlinear least squares problem and policy optimization problem may be computationally challenging. The focus of this work is to understand the statistical complexity of the problem rather than the computational complexity. However, it is worth noting that the online stochastic optimization procedure is computationally efficient and therefore the learner may often efficiently execute the second phase of the dynamics estimation procedure online. Additionally, for particular systems and objectives, the policy optimization problem may be efficient. This is the case, for instance, if the optimal solution to the policy optimization problem can be achieved via feedback linearization by choosing the input to cancel out some portion of the dynamics. We consider such an example in Section 4.

Our main result bounds the regret incurred by Algorithm 1 in terms of $N$ and $N_{{\mathsf{p}\mathsf{h}\mathsf{a}\mathsf{s}\mathsf{e}}\, 1}$ under the aforementioned smoothness and identifiability conditions.

### Theorem 3.1

Consider applying Algorithm 1 to the system with initial policy $\pi_{0}$ satisfying Assumption 5, policy class $\Pi$ satisfying Assumption 2, number of iterations $N$, number of initial phase episodes $N_{{\mathsf{p}\mathsf{h}\mathsf{a}\mathsf{s}\mathsf{e}}\, 1}$ and confidence radius $r_{\Phi}$. Additionally suppose that the dynamics satisfy Assumption 1 and that the costs satisfy Assumption 3. Furthermore, suppose that the dynamics, objective, and policy class satisfy Assumption 4. Finally, suppose that the true optimal controller, $\pi_{\theta^{\ast}}$, satisfies Assumption 6. Then,

as long as the following both hold:

$r_{\Phi} \leq {\mathsf{p}\mathsf{o}\mathsf{l}\mathsf{y}}{\left( r_{CE},r_{cost},T^{- 1},d_{x}^{- 1},\sigma_{w}^{- 1},L_{f}^{- 1},L_{\theta}^{- 1},L_{CE}^{- 1},\lambda_{\min} \right)}$,

$N_{{\mathsf{p}\mathsf{h}\mathsf{a}\mathsf{s}\mathsf{e}}\, 1} \geq {{\mathsf{p}\mathsf{o}\mathsf{l}\mathsf{y}}_{\alpha}{({\log N},T,d_{x},d_{\Phi},\sigma_{w},C_{Loja},L_{f},r_{\Phi}^{- 1},\lambda_{\min}^{- 1},{\log B})}}$.

Theorem 3.1 states that if $r_{\Phi}$ is chosen small enough and the number of initial phase episodes $N_{{\mathsf{p}\mathsf{h}\mathsf{a}\mathsf{s}\mathsf{e}}\, 1}$ exceeds some burn-in which is polylogarithmic in $N$ and polynomial in $r_{\Phi}^{- 1}$ all other relevant system parameters, then the regret incurred by Algorithm 1 grows at most linearly with $\log N$ and $N_{{\mathsf{p}\mathsf{h}\mathsf{a}\mathsf{s}\mathsf{e}}\, 1}$. Plugging in specific choices for $r_{\Phi}$ and $N_{{\mathsf{p}\mathsf{h}\mathsf{a}\mathsf{s}\mathsf{e}}\, 1}$ yields the desired polylogarithmic regret bound for Algorithm 1.

### Corollary 3.2

Suppose we apply Algorithm 1 in the setting of Theorem 3.1 with the parameters:

$r_{\Phi} = {\mathsf{p}\mathsf{o}\mathsf{l}\mathsf{y}}{\left( r_{CE},r_{cost},T^{- 1},d_{x}^{- 1},\sigma_{w}^{- 1},L_{f}^{- 1},L_{\theta}^{- 1},L_{CE}^{- 1},\lambda_{\min} \right)}$,

$N_{{\mathsf{p}\mathsf{h}\mathsf{a}\mathsf{s}\mathsf{e}}\, 1} = {\mathsf{p}\mathsf{o}\mathsf{l}\mathsf{y}}_{\alpha}{\left( \log N,T,d_{x},d_{\Phi},\sigma_{w},C_{Loja},L_{f},r_{\Phi}^{- 1},\lambda_{\min}^{- 1},\log B \right)}$.

Then, Algorithm 1 achives regret depending polylogarithmically on the number of episodes $N$, i.e.,

The full proof of Theorem 3.1 may be found in Appendix B; we provide a brief sketch below.

### Proof 3.3 (Proof Sketch)

For $N_{{\mathsf{p}\mathsf{h}\mathsf{a}\mathsf{s}\mathsf{e}}\ \mathsf{1}}$ satisfying the given bound, the system identification results of Ziemann and Tu; Lee et al. ensure that the confidence set $\Phi$ is constructed such that $\phi_{\star} \in \Phi$ with probability at least $1 - {1/N}$. The regret is decomposed into three parts: that of the initial exploration phase, that of the second phase under the failure event where $\phi_{\star} \notin \Phi$, and that of the second phase under the success event, where $\phi_{\star} \in \Phi$. Using the bound on the episode costs, the regret incurred from the first phase is bounded by $L_{cost}N_{{\mathsf{p}\mathsf{h}\mathsf{a}\mathsf{s}\mathsf{e}}\ \mathsf{1}}$ and the regret incurred during the second phase under the failure event $\phi_{\star} \notin \Phi$ is bounded by $L_{cost}{(N - N_{{\mathsf{p}\mathsf{h}\mathsf{a}\mathsf{s}\mathsf{e}}\ 1})}{\mathbb{P}}{\left\lbrack \phi_{\star} \notin \Phi \right\rbrack} \leq L_{cost}$. The condition on the radius of the confidence set ensures that the prediction error is strongly convex when the learner plays a certainty equivalent controller synthesized using any system estimate $\phi \in \Phi$. This in turn allows us to leverage the analysis of stochastic gradient descent to obtain a bound on the regret incurred during the second phase. Summing the contributions of the three components leads to the regret bound in Theorem 3.1.

Before proceeding, we note that while the regret of Algorithm 1 depends polylogarithmically on the number of episodes $N$, it depends polynomially (superlinearly, even) on the episode length $T$. Intuitively, one might expect a sublinear dependence on $T$ since increasing $T$ increases the number of interactions the learner has with the system. The polynomial dependence on $T$ arises because we consider an episodic setting without mixing assumptions within episodes. Indeed, under such mixing assumptions, growing length of the episode does reduce the identification error. Therefore, by imposing stronger assumptions which lead to mixing, such as stability of the initial and optimal policies, one can likely achieve a sublinear dependence on $T$. We leave formalizing this to future work.

## Numerical Validation

### Toy Experiment

We provide an simple example to illustrate the fast regret rates attained by Algorithm 1. For more experiments, see section 4.2. Consider the two-dimensional nonlinear system

where ${x_{t},u_{t},w_{t},\phi^{\ast}} \in {\mathbb{R}}^{2}$, and with $x_{1} = \begin{bmatrix}
\end{bmatrix}^{\top}$. The noise $w_{t}$ has a standard normal distribution. We choose the unknown parameter $\phi^{\ast} = \begin{bmatrix}
\end{bmatrix}^{\top}$.

In this experiment, we use the horizon $T = 10$ and the number of episodes $N = 3000$. We will consider the quadratic cost functions

The policy class $\Pi$ consists of controllers parameterized by the dynamics estimate $\hat{\phi}$, with

It can be shown that the dynamics and policy class satisfy Assumption 6. Our initial policy $\pi_{0}$ plays the controller $\pi_{\phi}$ corresponding to $\phi = \begin{bmatrix}
\end{bmatrix}^{\top}$, which can be shown to satisfy Assumption 5. In place of choosing $N_{{\mathsf{p}\mathsf{h}\mathsf{a}\mathsf{s}\mathsf{e}}\, 1}$ or $r_{\Phi}$ according to Theorem 1, we heuristically set $N_{{\mathsf{p}\mathsf{h}\mathsf{a}\mathsf{s}\mathsf{e}}\, 1} = 100$ and $r_{\Phi} = 0.2$. We note that the dynamics are not uniformly bounded globally, however they are uniformly bounded with high probability.

Under this choice of cost function and policy class, the learner's objective is to keep the system near the origin. Figure 1 illustrates the performance (measured in terms of regret) of Algorithm 1 on the toy dynamical system. The first plot shows that, after the initial $N_{{\mathsf{p}\mathsf{h}\mathsf{a}\mathsf{s}\mathsf{e}}\, 1}$-episode initial phase, the excess cost incurred per round begins to decay quickly, leading to the regret growing polylogarithmically with $N$. The second plot is included to better illustrate the regret attained by Algorithm 1; after the initial phase, the average regret appears to grow as a polynomial of the logarithm of the iteration. This toy example highlights the fast regret rates attained by Algorithm 1.

Figure 1: Average regret incurred by Algorithm 1 on the toy dynamical system, versus iterations and log (iterations), respectively. The mean over 30 runs is shown, with the standard error shaded.

### Cartpole Experiment

In this section, we complement our simple numerical example with an implementation of Algorithm 1 on a cartpole system defined by the dynamics:

Here, $p$ is the position of the cart, $\theta$ is the angle of the pole from the upright position, $u$ is the control force; the state vector is given by $x = \begin{bmatrix}
p & \overset{˙}{p} & \theta & \overset{˙}{\theta}
\end{bmatrix}^{\top}$ and the input is given by $u$. Also, $M$ is the mass of the cart, $m$ is the mass of the pole, $l$ is the length of the pole, $g$ is the acceleration due to gravity, $b_{x}$ is the friction coefficient for the cart, and $b_{\theta}$ is the friction coefficient for the pole. We discretize the system using the Euler approach using a timestep of ${dt} = 0.2$. We also include additive zero mean Gaussian noise with covariance $0.05I_{4}$. The unknown parameters are $\phi^{\ast} = \begin{bmatrix}
\end{bmatrix}^{\top} = \begin{bmatrix}
\end{bmatrix}^{\top}$. For every episode, the system starts from the upright position, given by the state $x_{0} = \begin{bmatrix}
\end{bmatrix}^{\top}$. The desired behavior is to keep the pole upright with the cart positioned at the origin for a time horizon of $T = 20$ timesteps. This behavior is described by the quadratic cost functions ${{c_{t}{(x,u)}} = {\left\| x \right\|^{2} + {0.1u^{2}}}},{{c_{T + 1}{(x)}} = \left\| x \right\|^{2}}$.

Our exploitation policy class $\Pi$ is given by neural networks with layer sizes $$ and ReLU activation functions. For computational reasons, in place of directly solving for the certainty equivalent policy for each parameter estimate $\phi_{i}$, we simultaneously update a dynamics estimate $\phi_{i}$ and train our control parameters $\theta_{i}$ as follows. At each iteration, we update our estimate of $\phi_{i}$ as in Algorithm 1 to get a new estimate $\phi_{i + 1}$; we then use the Adam optimizer to train a new set of control parameters $\theta_{i + 1}$ to minimize the cost functions using trajectories sampled with the dynamics $\phi_{i + 1}$ (in place of $\phi^{\ast}$), warm-starting the optimizer with the previous control parameters $\theta_{i}$. The initial exploration policy $\pi_{0}$ is given by bounded random noise scaled to match a predefined energy budget over the time horizon $T$; we choose a budget of $0.1T$. Finally, to illustrate the performance of our algorithm, we trained a "best-in-class" controller $\pi^{\ast}$ using trajectories sampled with the true dynamics $\phi^{\ast}$.

In this experiment, we use the horizon $T = 20$ and the number of episodes $N = 300$. Finally, we note that in place of choosing the number of initial phase episodes $N_{{\mathsf{p}\mathsf{h}\mathsf{a}\mathsf{s}\mathsf{e}}\, 1}$, the confidence radius $r_{\Phi}$, and the step sizes $\eta_{i}$ according to Corollary 3.2 and Algorithm 1, we heuristically set $N_{{\mathsf{p}\mathsf{h}\mathsf{a}\mathsf{s}\mathsf{e}}\, 1} = 1$, $r_{\Phi} = 1$, and $\eta_{i} = {100/{({100 + i})}}$. The cost of each controller was evaluated by sampling $10000$ trajectories and using the average cost; for computational reasons, we chose to only evaluate the cost every $10$ iterations.

Figure 2: The first plot shows average cost incurred by Algorithm 1 on the cartpole system -, versus iterations. The mean over 30 runs is shown in blue, with standard error shaded. The cost of a ”best-in-class” controller is shown with the dashed black line. The second and third plots show average regret versus iterations and the logarithm of iterations, respectively.

Figure 2 illustrates the cost incurred by Algorithm 1 on the cartpole system. The first plot shows that the cost of the controllers chosen by Algorithm 1 converges to the cost of $\pi^{\ast}$ quickly, which in turn leads to sublinear regret as demonstrated in the second plot. We note that unlike the example in Section 4.1, the plot of regret versus logarithm of iteration does not show the same linear growth. This is due to two main reasons: first, we observed higher variance in estimating the costs of our cartpole controllers via sampling, leading to higher estimation error in both the average performance of Algorithm 1 as well as the optimal cost; second, due to the nonconvexity of optimizing neural network weights, our policy optimization steps were inexact, introducing additional discrepancies with our theory. However, the overall trend of fast convergence to the optimal control cost using a greedy algorithm is clear, and supports the behavior predicted by our theory. This cartpole experiment verifies that Algorithm 1 works on simple physical systems in practice.

## Conclusion

We have introduced Algorithm 1 for online learning in a broad class of nonlinear dynamical systems. We have also proven a general sufficient condition for polylogarithmic regret under a natural curvature condition --- when the Fisher information matrix at the optimal policy is positive definite (detailed in our Assumption 6) --- and show that polylogarithmic regret is achieved by our Algorithm 1. Finally, we have verified the performance of Algorithm 1 on a toy dynamical system and show that it achieves a fast regret rate in practice. Future work could extend these results to the single-trajectory setting. In particular, it could be interesting to extend the $\log^{2}N$ regret rates of Cassel et al. and Lee et al. in the single-trajectory partially known linear setting to the setting with nonlinear dynamics. Another exciting avenue for future work is to design an online learning algorithm which deploys optimal experiment design techniques to optimally balance exploration and exploitation. Doing so may result in algorithms which automatically determine whether 6 is satisfied. Such an algorithm could achieve logarithmic regret if possible, and otherwise achieve $\sqrt{N}$ regret. Additionally, it may be possible to show improved dependence on the system-theoretic constants by using this approach.
