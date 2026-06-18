## Introduction & Motivation

With their recent successes in image classification, video game playing, sophisticated robotic simulations, and complex strategy games such as Go, machine and reinforcement learning (RL) are now being applied to plan and control the behavior of autonomous systems that interact with physical environments. Such systems, which include self-driving vehicles and agile robots, must interact with complex environments that are ever changing and difficult to model, strongly motivating the use of data-driven techniques. However, if machine learning is to be applied in these new settings, the resulting algorithms must come with the reliability, robustness, and safety guarantees that typically accompany results in the control theory literature, as failures could be catastrophic. Thus, as RL algorithms are increasingly and more aggressively deployed in safety critical settings, control theorists must be part of the conversation.

To that end, it is important to recognize that while the applications areas and technical tools are new, the challenges faced -- uncertain and time varying systems and environments, unreliable sensing modalities, the need for robust stability and performance, etc. -- are not, and that many classical results from the system identification and adaptive control literature can be brought to bear on these problems. In the case of discrete time linear systems, adaptive control algorithms further come with strong guarantees of asymptotic consistency, stability, and optimality, and similarly elucidate some of the fundamental challenges that are still being wrestled with today, such as rapidly identifying a system model (exploration) while robustly/optimally controlling it (exploitation).

Indeed, at a cursory glance, classical self-tuning regulators have the same objective as contemporary RL: an initial control policy and/or model is posited, data is collected, and a refined model/policy is produced, often in an online fashion. However, until recently, there has been relatively little contact between the two research communities. As a result, the tools and analysis objectives are different. One such feature, which will be the focus of this tutorial, is that RL and online learning algorithms are often analyzed in terms of *finite-data* guarantees, and as such, are able to provide *anytime guarantees* on the quality of the current behavior. Such finite-data guarantees are obtained by integrating tools from optimal control, stochastic optimization, and high-dimensional statistics -- whereas the first two tools are familiar to the controls community, the latter is less so. A major theme will be that of uncertainty quantification: indeed the importance of relating uncertainty quantification to control objectives was emphasized already in the 1960-70s. Moreover, the fragility of certainty equivalent control was one of the motivating factors for the development of robust adaptive control methodologies.

In this tutorial paper and our companion paper, we highlight recent advances that provide non-asymptotic analysis of adaptive algorithms. Our aim is for these papers is for them to serve as a jumping off point for control theorists wanting to work in RL problems. In, we present an overview of tools and results on finite-data guarantees for system identification. This paper focuses on finite-data guarantees for self-tuning and adaptive control strategies, and is structured as follows:

Section II: provides an extensive literature review of work spanning classical and recent results in system identification, adaptive control, and RL.

Section III: introduces the fundamental problem and performance metrics considered in RL, and relates them to examples familiar to the controls community.

Section IV: provides a survey of contemporary results for problems with finite state and action spaces.

Section V: shows how system estimates and error bounds can be incorporated into model-based self-tuning regulators with finite-time performance guarantees.

Section VI: presents guarantees for model-free methods, and shows that a complexity gap exists between model-based and model-free methods.

## Literature Review

The results we present in this paper draw heavily from three broad areas of control and learning theory: system identification, adaptive control, and approximate dynamic programming (ADP) or, as it has come to be known, reinforcement learning. Each of these areas has a long and rich history and a general literature review is outside the scope of this tutorial. Below we will instead emphasize pointers to good textbooks and survey papers, before giving a more careful account of recent work.

### II-1 System Identification

The estimation of system behavior from input/output experiments has a well-developed theory dating back to the 1960s, particularly in the case of linear-time-invariant systems. Standard reference texts on the topic include. The success of discrete time series analysis by Box and Jenkins provided an early impetus for the extension of these methods to the controlled system setting. Important connections to information theory were established by Akaike. The rise of robust control in the 1980s further inspired system identification procedures, wherein model errors were optimized under the assumption of adversarial noise processes. Another important step was the development of subspace methods, which became a powerful tool for identification of multi-input multi-output systems.

### II-2 Adaptive Control

System identification on real systems can be tedious, time consuming, and require skilled personnel. Adaptive control could then offer a simpler path forward. Moreover, adaptation offers an effective way to compensate for time-variations in the system dynamics. An early driving application was aircraft autopilot development in the 1950s. Aerospace applications needed control strategies that automatically compensated for changes in dynamics due to altitude, speed, and flight configuration. Another important early application was ship steering, where adaptation is used to compensate for wave effects. Standard textbooks include.

A direct approach to adaptive control expounded by Bellman was to tackle the problem using dynamic programing by augmenting the state to contain the conditional distribution of the unknown parameters. From this it was seen that in such problems, control served the dual purpose of exciting the system to aid in its identification -- hence the term dual control. This approach suffered from the curse of dimensionality, which lead to the development of approximation techniques that ultimately evolved into modern day RL.

A more practical approach was self-tuning adaptive control, pioneered by and followed by a long sequence of contributions to adaptive control theory, deriving conditions for convergence, stability, robustness and performance under various assumptions. For example, analysed adaptive algorithms using averaging, and derived an algorithm that gives mean square stability with probability one. On the other hand, conditions that may cause instability were studied in, and. Finally, gave conditions for optimal asymptotic rates of convergence. More recent adaptive approaches include the L1 adaptive controller, and model free adaptive control.

### II-3 Automatic Tuning and Repeated Experiments

There is also an extensive literature on automatic procedures for initialization (tuning) of controllers, without further adaptation after the tuning phase. A successful example is auto-tuning of PID controllers, where a relay provides non-linear feedback during the tuning phase. Another important tuning approach, well established from an engineering perspective, is based on repeated experiments with linear time-invariant controllers. Theoretical bounds on a related approach were obtained by Lai and Robbins. Specifically, they showed that a pseudo-regret of the state variance is lower bounded by $\Omega{({\log{(T)}})}$. Subsequent work by Lai showed that this bound was tight. Recently, Raginsky revisited this problem formulation, and showed that for any persistently exciting controller, the time taken to achieve state variance less than $\epsilon$ is at least $\Omega{({\frac{n^{2}}{\epsilon}{\log{({1/\epsilon})}}})}$ for a system of dimension $n$.

### II-4 Dynamic Programming and Reinforcement Learning

A major part of the literature on dynamic programming is devoted to "tabular MDPs," i.e. systems for which the state and action spaces are discrete and small enough to be stored in memory. The classic texts highlight computationally efficient approximation techniques for solving these problems. They include Monte Carlo methods, temporal-difference (TD) learning (which encompass SARSA and Q-learning ), value and Q-function approximation via Neural Networks, kernel methods, least-squares TD (LSTD), and policy gradient methods such as REINFORCE and Actor-Critic Methods.

Recent advances in both algorithms and computational power have allowed RL methods to solve incredibly complex tasks in very large discrete spaces that far exceed the tabular setting, including video games, Go, chess, and shogi. This success has renewed an interest in applying traditional model-free RL methods, such as Q-learning and policy optimization, to continuous problems in robotics. Thus far, however, the deployment of systems trained in this way has been limited to simulation environments or highly controlled laboratory settings, as the training process for these systems is both data hungry and highly variable.

### II-5 System Identification Revisited

With few exceptions (e.g., ), prior to the 2000s, the literature on system identification and adaptive control focused on asymptotic error characterization and consistency guarantees. In contrast, contemporary results in statistical learning seek to characterize *finite time and finite data* rates, leaning heavily on tools from stochastic optimization and concentration of measure. Such finite-time guarantees provide estimates of both system parameters and their uncertainty, allowing for a natural bridge to robust/optimal control. Early such results, characterizing rates for parameter identification, featured conservative bounds which are exponential in the system degree and other relevant quantities. More recent results, focused on state-space parameter identification for LTI systems, have significantly improved upon these bounds. In, the first polynomial time guarantees for identifying a stable linear system were provided -- however, these guarantees are in terms of predictive output performance of the model, and require rather stringent assumptions on the true system. In, it was shown, assuming that the state is directly measurable and the system is driven by white in time Gaussian noise, that solving a least-squares problem using independent data points taken from different trials achieves order optimal rates that are linear in the system dimension. This result was generalized to the single trajectory setting for (i) marginally stable systems in, (ii) unstable systems in, and (iii) partially observed stable systems in. We note that analogous results also exist in the fully observed setting for the identification of sparse state-space parameters, where rates are shown to be logarithmic in the ambient dimension, and polynomial in the number of nonzero elements to be estimated.

### II-6 Automatic Tuning Revisited

There has been renewed interest, motivated in part by the expansion of reinforcement learning to continuous control problems, in the study of automatic tuning as applied to the Linear Quadratic Regulator. More closely akin to iterative learning control, Fietcher showed that the discounted LQR problem is Probably Approximately Correct (PAC) learnable in an episodic setting. In, Dean et al. dramatically improved the generality and sharpness of this result by extending it to the traditional infinite horizon setting, and leveraging contemporary tools from concentration of measure and robust control.

### II-7 Adaptive Control Revisited

Contemporary results tend to draw on ideas from the bandits literature. A non-asymptotic study of the adaptive LQR problem was initiated by Abbasi-Yadkori and Szepesvari. They use an Optimism in the Face of Uncertainty (OFU) based approach, where they maintain confidence ellipsoids of system parameters and select those parameters that lead to the best closed loop performance. While the OFU method achieves the optimal $O{(T^{1/2})}$ regret, solving the OFU sub-problem is computationally challenging. To address this issue, other exploration methods were studied. Thompson sampling is used to achieve $O{(T^{1/2})}$ regret for scalar systems, and studies a Bayesian setting with a particular Gaussian prior. Both and give tractable algorithms which achieve sub-linear frequentist regret of $O{(T^{2/3})}$ without the Bayesian setting of. Follow up work showed that this rate could be improved to $O{(T^{1/2})}$ by leveraging a novel semi-definite relaxation. More recently, show that as long as the initial system parameter estimates are sufficiently accurate, certainty equivalent (CE) control achieves $O{(T^{1/2})}$ regret with high probability. Finally, Rantzer shows that for a scalar system with a minimum variance cost criterion, a simple self-tuning regulator scheme achieves $O{({\log{(T)}})}$ expected regret after an initial burn in period, thus matching the lower bound established by.

Much of the recent work addressing the sample complexity of the LQR problem was motivated by the desire to understand RL algorithms on a simple baseline. In addition to the model-based approaches described above, model-free methods have also been studied. Model-free methods for the LQR problem were put on solid theoretical footing in, where it was shown that controllability and persistence of excitation were sufficient to guarantee convergence to an optimal policy. In, the first finite time analysis for LSTD as applied to the LQR problem is given, in which they show that $O{({n^{3}/\epsilon^{2}})}$ samples are sufficient to estimate the value function up to $\epsilon$-accuracy, for $n$ the state dimension. Subsequently, Fazel et al. also showed that randomized search algorithms similar to policy gradient can learn the optimal controller with a polynomial number of samples in the noiseless case; however an explicit characterization of the dependence of the sample complexity on the parameters of the true system was not given, and the algorithm is dependent on the knowledge of an initially stabilizing controller. Similarly, Malik et al. study the behavior of random finite differencing for LQR. Finally, shows that there exists a family of systems for which there is a sample complexity gap of at least a factor of state dimension between LSTD/policy gradient methods and simple CE model-based approaches.

## Fundamentals

We study the behavior of *Markov Decision Processes (MDP)*. In the finite horizon setting of length $T$, we consider

for $x_{t} \in \mathcal{X}$ the system state, $u_{t} \in \mathcal{U}$ the control input, $w_{t} \in \mathcal{W}$ the state transition randomness, and ${\mathbf{π}} = {\{\pi_{0},\pi_{1},\ldots,\pi_{T - 1}\}}$ the control policy, with $\pi_{t}:{{\mathcal{X}^{t} \times \mathcal{U}^{t - 1}}\rightarrow\mathcal{U}}$ a possibly random mapping. With slight abuse of notation, we will use $n_{x}$, $n_{u}$, and $n_{w}$ to denote (i) the dimension of $\mathcal{X}$, $\mathcal{U}$, and $\mathcal{W}$, respectively, when considering continuous state and action spaces, and (ii) the cardinality of $\mathcal{X}$, $\mathcal{U}$, and $\mathcal{W}$, respectively, when considering discrete state and action spaces.

We consider settings where both the cost functions ${\{ c_{t}\}}_{t = 0}^{T}$ and the dynamics functions ${\{ f_{t}\}}_{t = 0}^{T}$ may not be known. Finally, we assume that the primitive random variables $(x_{0},w_{0:T})$ are defined over a common probability space with known and independent distributions -- the expectation in the cost is taken with respect to these and the policy $\mathbf{π}$.

### III-A Dynamic Programming Solutions

When the transition functions $\{ f_{t}\}$ and costs $\{ c_{t}\}$ are known, problem can be solved using dynamic programming. As the dynamics are Markovian, we restrict our search to policies of the form $u_{t} = {\pi_{t}{(x_{t})}}$ without loss of optimality. Define the value function of problem at time $t$ to be

Iterating through this process yields both an optimal policty ${\mathbf{π}}^{\star}$, and the optimal cost-to-go $V_{0}{(x_{0})}$ that it achieves.

Moving to the infinite horizon setting, we assume that the cost function and dynamics are static, i.e., that ${c_{t}{(x_{t},u_{t})}} \equiv {c{(x_{t},u_{t})}}$ and $f_{t} \equiv {f{(x_{t},u_{t},w_{t})}}$ for all $t \geq 0$.

We begin by introducing the discounted cost setting, wherein the cost-functional in optimization is replaced with

for some $\gamma \in {(0,1\rbrack}$. Note that if $c{(x_{t},u_{t})}$ is bounded almost surely and $\gamma < 1$, then the infinite sum is guaranteed to remain bounded, greatly simplifying analysis. In this setting, evaluating the performance achieved by a fixed policy $\mathbf{π}$ consists of finding a solution to the following equation:

from which it follows immediately that the optimal value function $V_{\star}$ will satisfy

and $u_{\star} = {\pi_{\star}{(x)}}$. One can show that under mild technical assumptions, iterative procedures such as policy iteration and value iteration will converge to the optimal policy.

Next, we consider the asymptotic average cost setting, in which case the cost-functional in problem is set to

Care must be taken to ensure that the limit converges, thus somewhat complicating the analysis -- however, this cost functional is often most appropriate for guaranteeing the stability for stochastic optimal control problems.

### Example 1 (Linear Quadratic Regulator)

Consider the Linear Quadratic Regulator (LQR), a classical instantiation of MDP from the optimal control literature, for $Q \succeq 0$ and $R \succ 0$:

where the system state $x_{t} \in {\mathbb{R}}^{n_{x}}$, the control input $u_{t} \in {\mathbb{R}}^{n_{u}}$, and the disturbance process $w_{t} \in {\mathbb{R}}^{n_{x}}$ are independently and identically distributed as zero mean Gaussian random variables with a known covariance matrix $\Sigma_{w}$.

For a finite horizon $T$ and known matrices $(A,B)$, this problem can be solved directly via dynamic programming, leading to the optimal control policy

where $P_{t} \succeq 0$ satisfies the Discrete Algebraic Riccati (DAR) Recursion initialized at ${P_{T} = Q_{T}}.$ Further, when the triple $(A,B,Q^{1/2})$ is stabilizable and detectable, the closed loop system is stable and hence converges to a stationary distribution, allowing us to consider the asymptotic average cost setting, at which point the optimal control action is a static policy, defined as in (8 ‣ III-A Dynamic Programming Solutions ‣ III Fundamentals ‣ From self-tuning regulators to reinforcement learning and back again")), but with $P_{t}\rightarrow P$, for $P \succeq 0$ a solution of the corresponding DAR Equation.

### Example 2 (Tabular MDP)

Consider the setting where the state-space $\mathcal{X}$, the control space $\mathcal{U}$, and the disturbance process space $\mathcal{W}$ have finite cardinalities of $n_{x}$, $n_{u}$, and $n_{w}$, respectively, and further suppose that the underlying dynamics are governed by transition probabilities $P{({x_{t + 1} = \left. x^{\prime} \middle| {x_{t},u_{t}} \right.})}$. We assume that the cardinalities $n_{x}$, $n_{u}$, and $n_{w}$ are such that $\mathcal{X}$, $\mathcal{U}$, and $\mathcal{W}$ can be stored in tabular form in memory and worked with directly. These then induce the dynamics functions:

where ${w_{t}{(x_{t},u_{t})}} = x^{\prime}$ with probability $P{({x_{t + 1} = \left. x^{\prime} \middle| {x_{t},u_{t}} \right.})}$.

In the case of average cost, for simplicity, we restrict our attention to communicating and ergodic MDPs. The former correspond to scenario where for any two states, there exists a stationary policy leading from one to the other with positive probability. For the latter, any stationary policy induces an ergodic Markov chain. In the average cost setting, one wishes to minimize $\lim_{T\rightarrow\infty}{\frac{1}{T}V_{T}{(x)}}$. More precisely, the objective is to identify as fast as possible a stationary policy $\pi$ with maximal gain function $g^{\pi}$: for any $x \in \mathcal{X}$, ${g^{\pi}{(x)}}:={\lim_{T\rightarrow\infty}{\frac{1}{T}V_{T}^{\pi}{(x)}}}$ where $V_{T}^{\pi}{(x)}$ denotes the average cost under $\pi$ starting in state $x$ over a time horizon $T$. When the MDP is ergodic, this gain does not depend on the initial state. To compute the gain of a policy, we need to introduce the bias function ${h^{\pi}{(x)}}:={{\text{C}\text{-}}{\lim_{T\rightarrow\infty}{{\mathbb{E}}^{\pi}{\lbrack{\left. {\sum_{t = 1}^{\infty}{({{c{(x_{t},u_{t})}} - {g^{\pi}{(x_{t})}}})}} \middle| x_{0} \right. = x}\rbrack}}}}$ (where ${\text{C}\text{-}}\lim_{T\rightarrow\infty}$ is the Cesaro limit) that quantifies the advantage of starting in state $x$. $g^{\pi}$ and $h^{\pi}$ satisfy for any $x$:

The gain and bias functions $g^{\star}{(x)}$ and $h^{\star}{(x)}$ of an optimal policy verify Bellman's equation: for all $x$,

$h^{\star}$ is defined up to an additive constant.

When the transition probabilities and cost function are known, this problem can then be solved via value-iteration, policy-iteration, and linear programming.

### III-B Learning to Control MDPs with Unknown Dynamics

Thus far we have considered settings where the dynamics $\{ f_{t}\}$ and costs $\{ c_{t}\}$ are known. Our main interest is understanding what should be done when these models are not known. Our study will focus on the previous two examples, namely LQR and the tabular MDP setting. While much of current work in reinforcement learning focusses on *model-free* methods, we adopt a more control theoretic perspective on the problem and study model-based methods wherein we attempt to approximately learn the system model ${\{ f_{t}\}}_{t = 0}^{T}$, and then subsequently use this approximate model for control design.

Before continuing, we distinguish between episodic and single-trajectory settings. An *episodic task* is akin to traditional *iterative learning control*, wherein a task is repeated over a finite horizon, after which point the episode ends, and the system is reset to begin the next episode. In contrast, a *single-trajectory task* is akin to traditional *adaptive control*, in that no such resets are allowed, and a single evolution of the system under an adaptive policy is studied.

An underlying tension exists between identifying an unknown system and controlling it. Indeed it is well known that without sufficient *exploration* or *excitation*, an incorrect model will be learned, possibly leading to suboptimal and even unstable system behavior; however, this exploration inevitably degrades system performance. Informally, this tension leads to a fundamental tradeoff between how quickly a model can be learned, and how well it can be controlled during this process. Current efforts seek to explicitly address and quantify these tradeoffs through the use of performance metrics such as the Probably Approximately Correct (PAC) and Regret frameworks, which we define next. For episodic tasks, we assume the horizon of each episode to be of length $H$, and consider guarantees on performance as a function of the number of episodes $T$ that have been evaluated. For single trajectory tasks, we consider infinite horizon problems, and the definitions provided are equally applicable to the discounted and asymptotic average cost settings. The definitions that follow are adapted from, among others.

### III-C PAC-Bounds

### Episodic PAC-Bounds

We consider episodic tasks over a horizon $H$, where $H$ may be infinite but the user is allowed to reset the system at a prescribed time $H_{r}$. Let $V_{\star}$ be the optimal cost achievable, and $N_{\epsilon}$ be the number of episodes for which $\mathbf{π}$ is not $\epsilon$-optimal, i.e., the number of episodes for which $V_{\mathbf{π}} > {V_{\star} + \epsilon}$. Then, a policy $\mathbf{π}$ is said to be episodic-$(\epsilon,\delta)$-PAC if, after $T$ episodes, it satisfies^11^1We note that in the discounted setting, we also ask that the bound on $N_{\epsilon}$ depend polynomially on $1/{({1 - \gamma})}$. We also note that modern definitions of PAC-learning require that the bound on $N_{\epsilon}$ depend polynomially on $\log{({1/\delta})}$ -- this is a reflection of results from contemporary high-dimensional statistics that allow for more refined concentration of measure guarantees. Finally, the polynomial dependence on the horizon $H$ is only enforced for finite horizons $H$ -- in the case of an infinite horizon task, $N_{\epsilon}$ must not depend on the $H$.

These guarantees state that the chosen policy is $\epsilon$-optimal on all but a number of episodes polynomial in the problem parameters, with probability at least $1 - \delta$. Many $(\epsilon,\delta)$ PAC algorithms operate in two phases: the first is solely one of exploration so as to identify an approximate system model, and the second is solely one of exploitation, wherein the approximate system model is used to synthesize a control policy. Therefore, informally one can view PAC guarantees as characterizing the number of episodes needed to identify a model that can be used to synthesize an $\epsilon$-optimal policy.

### Example 3 (LQR is episodic PAC-Learnable)

The results in imply that the LQR problem with an asymptotic average cost is episodic PAC-learnable. In particular, it was shown that a simple open-loop exploration process of injecting white in time Gaussian noise over at most ${poly}{(n_{x},n_{u},H_{r},{1/\epsilon},{\log{({1/\delta})}})}$ episodes, followed by a least-squares system identification and uncertainty quantification step, can be used with a robust synthesis method to generate a policy $\mathbf{π}$ which guarantees that

when the LQR problem is initialized at $x_{0} = 0$. Hence the resulting algorithm meets the modern definition of being $(\epsilon,\delta)$-PAC-learnable. We revisit this example in Section V.

### Single-trajectory PAC-Bounds

We consider single-trajectory tasks over an infinite horizon, and let $V_{\mathbf{π}}{(x_{t})}$ denote the cost-to-go from state $x_{t}$ achieved by a policy $\mathbf{π}$, and $V_{\star}{(x_{t})}$ be the optimal cost-to-go achievable. We further let $N_{\epsilon}$ be the number of time-steps for which $\mathbf{π}$ is not $\epsilon$-optimal in either an absolute or relative sense, i.e., the number of time-steps for which ${V_{\mathbf{π}}{(x_{t})}} > {{V_{\star}{(x_{t})}} + \epsilon}$ or ${V_{\mathbf{π}}{(x_{t})}} > {V_{\star}{(x_{t})}{({1 + \epsilon})}}$, respectively. Then, a policy $\mathbf{π}$ is said to be $(\epsilon,\delta)$-PAC if it satisfies^22^2We make the same modifications to this definition for the discounted case and the dependence on $1/\delta$ as in the episodic setting.

These guarantees should be interpreted as saying that the chosen policy is at worst $\epsilon$-suboptimal on all but ${poly}{(\frac{1}{\epsilon},{\log{({1/\delta})}})}$ time-steps, with probability at least $1 - \delta$. As in the episodic setting, one can view these PAC guarantees as characterizing the number of time-steps needed to identify a model that can be used to synthesize an $\epsilon$-optimal policy.

### Limitations of PAC-Bounds

As an algorithm that is $(\epsilon,\delta)$-PAC is only penalized for suboptimal behavior exceeding the $\epsilon$ threshold, there is no guarantee of convergence to an optimal policy. In fact, as pointed out in and illustrated in the LQR example above, many PAC algorithms cease learning once they are able to produce an $\epsilon$-suboptimal strategy.

### III-D Regret Bounds

We focus on regret bounds for the single-trajectory setting, as this is the most common type of guarantee found in the literature, but note that analogous episodic definitions exist (cf., ). The regret framework evaluates the quality of an adaptive policy by comparing its running cost to a suitable baseline. Let $b_{T}$ represent the baseline cost at time $T$, and define the regret incurred by a policy ${\mathbf{π}} = {\{\pi_{0},\pi_{1},\ldots\}}$ to be

Note that $b_{T}$ is user specified, and is often chosen to be the expected optimal cost achievable by a policy with full knowledge of the system dynamics. The two most common regret guarantees found in the literature are expected regret bounds, and high probability regret bounds. In the expected regret setting, the goal is to show that

whereas in the high-probability regret setting, the goal is to show that^33^3As in the PAC setting, modern definitions often require the dependence to be polynomial in $\log{({1/\delta})}$.

These bounds therefore quantify the rate of convergence of the cost achieved by the adaptive policy to the baseline cost, providing *any time guarantees* on performance relative to a desirable baseline. From the definition of $R^{\pi}{(T)}$, it is clear that one should strive for an $o{(T)}$ dependence, as this implies that the cost achieved by the adaptive policy converges with at least sub-linear rate to the base cost $b_{T}$. Further, in contrast to the PAC framework, *all sub-optimal behavior* is tallied by the running regret sum, and hence exploration and exploitation must be suitably balanced to achieve favorable bounds.

### Example 4 (Regret bounds for LQR)

The study of regret bounds for LQR was initiated in. Here we summarize a recent treatment of the problem, as provided in. There, the authors study the performance of CE control for LQR, and study a regret measure of the form

with $V_{\star}:={{\min_{u}{\mathbb{E}}}\left\lbrack {{\lim_{T\rightarrow\infty}{T^{- 1}{\sum_{t = 0}^{T}{x_{t}^{\top}Qx_{t}}}}} + {u_{t}^{\top}Ru_{t}}} \right\rbrack}$ the optimal asymptotic average cost achieved by the true optimal LQR controller. They show that the control policy ${u_{t} = {{\hat{K}x_{t}} + \eta_{t}}},$ which has an exploration term $\eta_{t} \sim {\mathcal{N}{(0,{\sigma_{\eta,t}^{2}I})}}$ added to the CE controller, achieves the regret bound

with probability at least $1 - \delta$ so long as $\sigma_{\eta,t}^{2} \sim t^{- {1/2}}$ and the initial estimates of the system dynamics $(\hat{A},\hat{B})$ are sufficiently accurate. We revisit this example in Section V.

### Limitations of Regret Bounds

As regret only tracks the integral of suboptimal behavior, it does not distinguish between a few severe mistakes and many small ones. In fact, shows that for Tabular MDP problems, an algorithm achieving optimal regret may still make infinitely many mistakes that are maximally suboptimal. Thus regret bounds cannot provide guarantees about transient worst-case deviations from the baseline cost $b_{T}$, which may have implications on guaranteeing the robustness or safety of an algorithm. We comment further on regret for discrete MDPs in the next section.

## Optimal control of unknown discrete systems

This section addresses reinforcement learning for stationary MDPs with finite state and control spaces of respective cardinalities $n_{x}$ and $n_{u}$. When the system is in state $x$ and the control input is $u$, the system evolves to state $x^{\prime}$ with probability $p{(\left. x^{\prime} \middle| {x,u} \right.)}$, and the cost $c_{t}{(x,u)}$ induced is independently drawn from a distribution $q{( \cdot |x,u)}$ with expectation $c{(x,u)}$. Costs are bounded, and for any $(x,u)$, the distribution $q{( \cdot |x,u)}$ is absolutely continuous w.r.t. to a measure $\lambda$ (for example, Lebesgue measure).

We consider both average-cost and discounted MDPs (refer to Example 2), and describe methods (i) to derive fundamental performance limits (in terms of regret and sample complexity), and (ii) to devise efficient learning algorithms. The way the learner samples the MDP may significantly differs in the literature, depending on the objective (average or discounted cost), and on whether one wishes to derive fundamental performance limits or performance guarantees of a given algorithm. For example, in the case of average cost, typically, the learner gathers information about the system in an online manner following the system trajectory, a sampling model referred previously to as the single trajectory model. Most sample complexity ananlyses are on the contrary derived under the so-called generative model, where any state-control pair can be sampled in $O{}$ time. Generative models are easier to analyze but hide the difficult issue of navigating the state space to explore various state-control pairs.

### IV-A Average-cost MDPs

For average-cost MDPs, we are primarily interested in devising algorithms with minimum regret, defined for a given learning algorithm $\pi$ as

where $x_{t}^{\pi}$ and $u_{t}^{\pi}$ are the state and control input under the policy $\pi$ at time-step $t$, and similarly the superscript $\star$ corresponds to an optimal stationary control policy. Next, we discuss the type of regret guarantees we could aim at.

Expected vs. high-probability regret. We would ideally wish to characterize the complete regret distribution. This is however hard, and most existing results provide guarantees either in expectation or with high probability. In the case of finite state and control spaces, guarantees in high-probability can be easy to derive and not very insightful. Consider for example, a stochastic bandit problem (a stateless MDP) where the goal is to identify the control input with the lowest expected cost. An algorithm exploring each control input at least $\log{({1/\delta})}$ times would yield a regret in $\mathcal{O}{({\log{({1/\delta})}})}$ with probability greater than $1 - \delta$ (this is a direct application of Hoeffding's inequality). This simple observation only holds for a fixed MDP (the gap between the costs of the various inputs cannot depend on $\delta$ nor on the time at which regret is evaluated), and relies on the assumption of bounded costs. Even in the simplistic stochastic bandit problem, analyzing the distribution of the regret remains an open and important challenge, refer to for initial discussions and results.

Problem-specific vs. minimax regret guarantees. A regret upper bound is problem-specific if it explicitly depends on the parameters defining the MDP. Such performance guarantees capture and quantify the hardness of learning to control the system. Minimax regret guarantees are far less precise and informative, since they concern the worst system among possibly all systems. An algorithm with good minimax regret upper bound behaves well in the worst case, but does not necessarily learn and adapt to the system it aims at controlling.

Guided by the above observations, we focus on the expected regret, and always aim, when this is possible, at deriving problem-specific performance guarantees.

### IV-A1 Regret lower bounds

We present here a unified simple method to derive both problem-specific and minimax regret lower bounds. This method has been developed mainly in the bandit optimization literature as a simplified alternative to Lai and Robbins techniques.

Let $\phi = {(p,q)}$ denote the true MDP. Consider a second MDP $\psi = {(p^{\prime},q^{\prime})}$. For a given learning algorithm $\pi$, define by $\mathcal{L}^{\pi}{(T)}$ the log-likelihood ratio of the corresponding observations under $\phi$ and $\psi$. By a simple extension of the Wald's lemma, we get:

where $N_{xu}^{\pi}{(T)}$ is the number of times the state-control pair $(x,u)$ is observed, where ${\mathbb{E}}_{\phi}^{\pi}$ is the expectation taken w.r.t. to the distrbution of observations made under $\pi$ for the MDP $\phi$, and where $KL_{\phi|\psi}{(x,u)}$ is the KL divergence between the distributions of the observations made in $(x,u)$ under $\phi$ and $\psi$. These observations concern the next state, and the realized reward, and hence:

Now the data processing inequality states that for any event $E$ or any $\lbrack 0,1\rbrack$-valued random variable depending on all observations up to time $T$, i.e., $\mathcal{F}_{T}^{\pi}$-measurable ($\mathcal{F}_{T}^{\pi}$ is the $\sigma$-algebra generated by the observations under $\pi$ up to time $T$):

where $kl{(a,b)}$ is the KL divergence between two Bernoulli distributions of respective means $a$ and $b$. Now combining the above inequality to yields a lower bound on a weighted sum of the expected numbers of times each state-control pair is selected. These numbers are directly related to the regret as one can show that:

where $\mathcal{O}{(x,\phi)}$ denotes the set of optimal control inputs in state $x$ under $\phi$, and $\delta^{\star}{(x,u;\phi)}$ is the sub-optimality gap quantifying the regret obtained by selecting the control $u$ is state $x$. It remains to select the event $E$ or the random variable $Z$ to get a regret lower bound.

To derive problem-specific regret lower bounds, we introduce the notion of uniformly good algorithms. $\pi$ is uniformly good if for any ergodic MDP $\phi$, any initial state and any constant $\alpha > 0$, ${{\mathbb{E}}_{\phi}^{\pi}{\lbrack{R^{\pi}{(T)}}\rbrack}} = {o{(T^{\alpha})}}$. As it will become clear later, uniformly good algorithms exist. Now select the event $E$ as:\
${E = \left\lbrack {{{N_{x}{(T)}} \geq {\rhoT}},{{\sum_{u \notin {\mathcal{O}{(x,\phi)}}}{N_{xu}{(T)}}} \leq \sqrt{T}}} \right\rbrack},$ for some $\rho > 0$ and where $N_{x}{(T)}$ is the number of times $x$ is visited up to time $T$. $\rho$ is chosen such that ${N_{x}{(T)}} \geq {\rhoT}$ is very likely under $\pi$ invoking the ergodicity of the MDP. In the change-of-measure argument, $\psi$ is chosen such that ${{\Pi^{\star}{(\phi)}} \cap {\Pi^{\star}{(\psi)}}} = \varnothing$, where $\Pi^{\star}{(\phi)}$ is the set of optimal policies under $\phi$. Now if $\pi$ is uniformly good, $E$ is very likely under $\phi$, and very unlikely under $\psi$. Formally, we can establish that:

Putting the above ingredients together, we obtain:

### Theorem IV.1

(Theorem 1, ) Let $\phi$ be an ergodic MDP. For any uniformly good algorithm $\pi$ and for any initial state,

where $K{(\phi)}$ is the value of the following optimization problem:

where $\mathcal{F}{(\phi)}$ is the set of $\eta \geq 0$ satisfying

and ${\Delta{(\phi)}} = {\{\psi:{{\phi \ll \psi},{{{\Pi^{\ast}{(\phi)}} \cap {\Pi^{\ast}{(\psi)}}} = \varnothing}}\}}$.

In the above theorem $\psi \ll \phi$ means that the observations under $\psi$ have distributions absolutely continuous w.r.t. those of the observations under $\phi$. By imposing the constraint for all $\psi \in {\Delta{(\phi)}}$, we consider all possible confusing MDP $\psi$. It can be shown that the set of constraints defining $\mathcal{F}{(\phi)}$ can be reduced and decoupled: it is sufficient to consider $\psi$ different than $\phi$ in only one suboptimal state-control pair. In that case, the constraints can be written in the following form: for any $x$ and $u \notin {\mathcal{O}{(x,\phi)}}$, ${\eta{(x,u)}{({\delta^{\star}{(x,u;\phi)}})}^{2}} \geq K$ for some absolute constant $K$. As a consequence, the regret lower bound scales as $n_{x}n_{u}{\log{(T)}}$. The theorem also indicates the optimal exploration rates of the various suboptimal state-control pairs: $\eta{(x,u)}{\log{(T)}}$ represents the expected number of times $(x,u)$ should be observed. Finally, we note that the method used to derive the regret lower bound can also be applied to obtain finite-time regret lower bounds, as in.

For minimax lower bounds, we do not need to restrict the attention to uniformly good algorithms, since for any given algorithm, we are free to pick the MDP for which the algorithm performs the worst. Instead, to identify a $\mathcal{F}_{T}^{\pi}$-measurable $\lbrack 0,1\rbrack$-valued random variable $Z$, such that $kl{({{\mathbb{E}}_{\phi}^{\pi}{\lbrack Z\rbrack}},{{\mathbb{E}}_{\psi}^{\pi}{\lbrack Z\rbrack}})}$ is large, we leverage symmetry arguments. Specifically, The MDP is constructed so as to contain numerous equivalent states and control inputs, and $Z$ is chosen as the proportion of time a particular state-action pair is selected. Refer to for the construction of this MDP, and to for more detailed explanations on how to apply change-of-measure arguments to derive minimax bounds.

### Theorem IV.2

(Theorem 5, ) For any algorithm $\pi$, for all integers ${n_{x},n_{u}} \geq 10$, $D \geq {20{\log_{A}{(n_{x})}}}$, and $T \geq {Dn_{x}n_{u}}$, there is an MDP with $n_{x}$ states, $n_{u}$ control inputs, and diameter $D$ such that for any initial state:

### IV-A2 Efficient Algorithms

A plethora of learning algorithms have been developed for average-cost MDPs. We can categorize these algorithms based on their design principles. A first class of algorithms aim at matching the asymptotic problem-specific regret lower bound derived above. These algorithms rely on estimating the MDP parameters and in each round (or periodically) they solve the optimization problem where the true MDP parameters are replaced by their estimators. The solution is then used to guide and minimize the exploration process. This first class of algorithms is discussed further in §IV-A3.

The second class of algorithms includes UCRL, UCRL2 and KL-UCRL. These algorithms apply the "optimism in front of uncertainty" principle and exhibit finite-time regret ganrantees. They consists in building confidence upper bounds on the parameters of the MDP, and based on these bounds select control inputs. The regret guarantees are anytime, but use worst-case regret as a performance benchmark. For example, UCRL2 with the confidence parameter $\delta$ as an input satisfies:

### Theorem IV.3

(Theorem 2, ) With probability at least $1 - \delta$, for any initial state and all $T \geq 1$, the regret under $\pi =$UCRL2 satisfies:

Anytime regret upper bounds with a logarithmic dependence in the time horizon have been also investigated for UCRL2 and KL-UCRL. For instance, UCRL2 is known to yield a regret in $\mathcal{O}{(D^{2}n_{x}^{2}n_{u}\log{(T/\delta)}}$ with probability at least $1 - {3\delta}$.

The last class of algorithms apply a similar Bayesian approach as that used by the celebrated Thompson sampling algorithm for bandit problems. In, AJ, a posterior sampling algorithm, is proposed and enjoys the following regret guanrantees:

### Theorem IV.4

(Theorem 1, ) With probability at least $1 - \delta$, for any initial state, the regret under $\pi =$AJ with confidence parameter $\delta$ satisfies: for $T \geq Dn_{u}\log{(T/\delta)}^{2}$,

### IV-A3 Structured MDPs

The regret lower bounds derived for tabular MDPs have the major drawback of scaling with the product of the numbers of states and controls, $n_{x}n_{u}$. Hence, with large state and control spaces, it is essential to identify and exploit any possible structure existing in the system dynamics and cost function so as to minimize exploration phases and in turn reduce regret to reasonable values. Modern RL algorithms actually implicitly impose some structural properties either in the model parameters (transition probabilities and cost function, see e.g. ) or directly in the $Q$-function (for discounted RL problems, see e.g.. Despite their successes, we do not have any regret guarantees for these recent algorithms. Recent efforts to develop algorithms with guarantees for structured MDPs include. is the first paper extending the analysis of to the case of structured MDPs. The authors derive a problem-specific regret lower bound, and show that the latter can be obtained by just modifying in Theorem IV.1 the definition of the set of confusing MDPs $\Delta{(\phi)}$. Specifically, if $\Phi$ denotes a set of structured MDPs ($\Phi$ encodes the structure), then ${\Delta{(\phi)}} = {\{{\psi \in \Phi}:{{\phi \ll \psi},{{{\Pi^{\ast}{(\phi)}} \cap {\Pi^{\ast}{(\psi)}}} = \varnothing}}\}}$. The minimal expected regret scales as $K_{\Phi}{(\phi)}{\log{(T)}}$, where $K_{\Phi}{(\phi)}$ is the value of the modified optimization problem. In, DEL, an algorithm extending that proposed in to the case of structured MDPs, is shown to optimally exploit the structure:

### Theorem IV.5

(Theorem 4, ) For any $\phi \in \Phi$, the regret under $\pi =$DEL satisfies:

The semi-infinite LP characterizing the regret lower bound can be simplified for some particular structures. For example in the case where $p$ and $q$ smoothly vary over states and controls (Lipschitz continuous), it can be shown that the regret lower bound does not scale with $n_{x}$ and $n_{u}$. The simplified LP can then be used as in to devise an asymptotically optimal algorithm.

### IV-B Discounted MDPs

Most research efforts, from early work to more recent Deep RL, towards the design of efficient algorithms for discounted MDPs have focussed on model-free approaches, where one directly learns the value or the Q-value function of the MDP. Such an approach leads to simple algorithms that are potentially more robust than model-based algorithms (since they do not rely on modelling assumptions). The performance analysis of these algorithms has been initially mainly centered around the question of their convergence; for example, the analysis of $Q$-learning algorithm with function approximation often calls for new convergence results of stochastic approximation schemes. Researchers have then strived to investigate and optimize their convergence rates. There is no consensus on the metric one should use to characterize the speed of convergence; e.g. the recent Zap Q-learning algorithm minimizes the asymptotic error covariance matrix, while most other analayses focus on the minimax sample complexity. Note that the notion of regret in discounted settings is hard to define and has hence not been studied. Also observe that problem-specific metrics have not been investigated yet, and it hence seems perilous to draw definitive conclusions from existing theoretical results for learning discounted MDPs.

### IV-B1 Sample complexity lower bound

For discounted MDPs, the sample complexity is defined as the number of samples one need to gather so as to learn an $\epsilon$-optimal policy with probability at least $1 - \delta$. Minimax sample complexity lower bounds are known for both the generative and online sampling models:

### Theorem IV.6

(Theorem 1, and Theorem 11, ) In both the generative and online sampling models, for $\epsilon$ and $\delta$ small enough, there exists an MDP such that any learning algorithm must have a sample complexity in $\Omega{({\frac{n_{x}n_{u}}{\epsilon^{2}{({1 - \gamma})}^{3}}{\log{(\frac{n_{x}}{\delta})}}})}$ (where $\gamma$ denotes the discount factor).

### IV-B2 The price of model-free approaches

Some model-based algorithms are known to match the minimax sample complexity lower bound. In the online sampling setting, the authors of presents UCRL($\gamma$), an extension of UCRL for discounted costs, and establish a minimax sample complexity upper bound matching the above lower bound. UCRL($\gamma$) consists in deriving upper confidence bounds for the MDP parameters, and in selecting action optimistically (this can lead to important computational issues). In the generative sampling model, algorithms mixing model-based and model-free approaches have been shown to be minimax-sample optimal. This is the case of QVI (Q-value Iteration) initially proposed in and analyzed in. QVI estimates the MDP, and from this estimator, applies a classical value iteration method to approximate the $Q$-function and hence the optimal policy. QVI can be also made computationally efficient.

As for now, there is no pure model-free algorithm achieving the minimax sample complexity limit. Speedy Q-learning has a minimax sample complexity in $\overset{\sim}{\mathcal{O}}{(\frac{n_{x}n_{u}}{\epsilon^{2}{({1 - \gamma})}^{4}})}$ (this is for now the best one can provably do using model-free approaches). However, there is hope to find model-free minimax-sample optimal algorithms. In fact, recently, $Q$-learning with exploration driven by simple upper confidence bounds on the $Q$-values (rather than on the MDP parameters as in UCRL) has been shown to be minimax regret optimal for episodic reinforcement learning tasks. It is likely that model-free algorithms can be made minimax optimal. If this is verified, this would further advocate the use of model-specific rather than minimax performance metrics.

## Model-Based Methods for LQR

We combine the techniques described in with robust and optimal control to derive finite-time guarantees for the optimal LQR control of an unknown system. We partition our study according to three initial uncertainty regimes: (i) completely unknown $(A,B)$, (ii) moderate error bounds under which CE control may fail, and (iii) small error bounds under which CE control is stabilizing.

### V-A PAC Bounds for Unknown $(A,B)$

Here we assume that the system is completely unknown, and consider the problem of identifying system estimates $(\hat{A},\hat{B})$, bounding the corresponding parameter uncertainties $\epsilon_{A} = {\parallel{\hat{A} - A}\parallel}_{2}$ and $\epsilon_{B} = {\parallel{\hat{B} - B}\parallel}_{2}$, and using these system estimates and uncertainty bounds to compute a controller with provable performance bounds. In what follows, unless otherwise specified, all results are taken from.

The system identification and uncertainty quantification steps are covered in Theorem IV.3 of, which we summarize here for the convenience of the reader.

Consider a linear dynamical system described by

where ${x_{t},w_{t}} \in {\mathbb{R}}^{n_{x}}$, $u_{t} \in {\mathbb{R}}^{n_{u}}$, and $w_{t}\overset{\ \text{i.i.d.}}{\sim}{\mathcal{N}{(0,{\sigma_{w}^{2}I})}}$. To identify the matrices $(A,B)$, we inject excitatory Gaussian noise via $u_{t}\overset{\ \text{i.i.d.}}{\sim}{\mathcal{N}{(0,{\sigma_{u}^{2}I})}}$. We run $N$ experiments over a horizon of $T + 1$ time-steps, and then solve for our estimates $(\hat{A},\hat{B})$ via the least-squares problem:

Notice that we only use the last time-steps of each trajectory: we do so for analytic simplicity, and return to single trajectory estimators that use all data later in the section. We then have the following guarantees.

### Theorem V.1

Consider the least-squares estimator defined by (24 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again")). Fix a failure probability $\delta \in {(0,1\rbrack}$, and assume that $N \geq {24{({n_{x} + n_{u}})}{\log{({54/\delta})}}}$. Then, it holds with probability at least $1 - \delta$, that

where $\lambda_{\min}\left( \Sigma_{x} \right)$ is the minimum eigenvalue of the finite time controllability Gramian ${\Sigma_{x}:={{\sigma_{u}^{2}{\sum_{t = 0}^{T}{A^{t}BB^{\top}{(A^{\top})}^{t}}}} + {\sigma_{w}^{2}{\sum_{t = 0}^{T}{A^{t}{(A^{\top})}^{t}}}}}}.$

We now condition on the high-probability guarantee Theorem V.1 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again"), and assume that we have system estimates $(\hat{A},\hat{B})$ and corresponding uncertainty bounds $(\epsilon_{A},\epsilon_{B})$, allowing us to focus on the controller synthesis step. Our goal is to compute a controller that is robustly stabilizing for any admissible realization of the system parameters, and for which we can bound performance degradation as a function of the uncertainty sizes $(\epsilon_{A},\epsilon_{B})$.

In order to meet these goals, we use the *System Level Synthesis* (SLS) nominal and robust parameterizations of stabilizing controllers. The SLS framework focuses on the *system responses* of a closed-loop system. Consider a LTI causal controller $\mathbf{K}$, and let ${\mathbf{u}} = {{\mathbf{K}}{\mathbf{x}}}$. Then the closed-loop transfer matrices from the process noise $\mathbf{w}$ to the state $\mathbf{x}$ and control action $\mathbf{u}$ satisfy

We then have the following theorem parameterizing the set of stable closed-loop transfer matrices, as described in equation (27 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again")), that are achievable by a stabilizing controller $\mathbf{K}$.

### Theorem V.2 (State-Feedback Parameterization \[115\])

The following are true:

The affine subspace defined by

parameterizes all system responses (27 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again")) from $\mathbf{w}$ to $({\mathbf{x}},{\mathbf{u}})$, achievable by an internally stabilizing state-feedback controller $\mathbf{K}$.

For any transfer matrices $\{\mathbf{\Phi}_{x},\mathbf{\Phi}_{u}\}$ satisfying (28 ‣ V-A PAC Bounds for Unknown (A,B) ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again")), the controller ${\mathbf{K}} = {\mathbf{\Phi}_{u}\mathbf{\Phi}_{x}^{- 1}}$ is internally stabilizing and achieves the desired system response (27 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again")).

We will also make use of the following robust variant of Theorem V.2 ‣ V-A PAC Bounds for Unknown (A,B) ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again").

### Theorem V.3 (Robust Stability \[117\])

Let $\mathbf{\Phi}_{x}$ and $\mathbf{\Phi}_{u}$ be two transfer matrices in $\frac{1}{z}\mathcal{R}\mathcal{H}_{\infty}$ such that

Then the controller $\mathbf{K} = {\mathbf{\Phi}_{u}\mathbf{\Phi}_{x}^{- 1}}$ stabilizes the system described by $(A,B)$ if and only if ${({I + \mathbf{\Delta}})}^{- 1} \in {\mathcal{R}\mathcal{H}_{\infty}}$. Furthermore, the resulting system response is given by

### Corollary V.4

Under the assumptions of Theorem 30 ‣ V-A PAC Bounds for Unknown (A,B) ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again"), if ${\|\mathbf{\Delta}\|} < 1$ for any induced norm $\parallel \cdot \parallel$, then the controller $\mathbf{K} = {\mathbf{\Phi}_{u}\mathbf{\Phi}_{x}^{- 1}}$ stabilizes the system described by $(A,B)$.

We now return to the problem setting where the estimates $(\hat{A},\hat{B})$ of a true system $(A,B)$ satisfy ${{\|\Delta_{A}\|}_{2} \leq \epsilon_{A}},{{\|\Delta_{B}\|}_{2} \leq \epsilon_{B}}$, for $\Delta_{A}:={\hat{A} - A}$ and $\Delta_{B}:={\hat{B} - B}$. We first formuate the LQR problem in terms of the system responses $\{\mathbf{\Phi}_{x},\mathbf{\Phi}_{u}\}$. It follows from Theorem V.2 ‣ V-A PAC Bounds for Unknown (A,B) ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again") and the standard equivalence between infinite horizon LQR and $\mathcal{H}_{2}$ optimal control that, for a disturbance process distributed as $w_{t}\overset{\ \text{i.i.d.}}{\sim}{\mathcal{N}{(0,{\sigma_{w}^{2}I})}}$, the standard LQR problem (7 ‣ III-A Dynamic Programming Solutions ‣ III Fundamentals ‣ From self-tuning regulators to reinforcement learning and back again")) can be equivalently written as

Going forward, we drop the $\sigma_{w}^{2}$ multiplier in the objective function as it does not affect the guarantees that we compute.

We begin with a simple sufficient condition under which any controller $\mathbf{K}$ that stabilizes $(\hat{A},\hat{B})$ also stabilizes the true system $(A,B)$. For a matrix $M$, we let $\Re_{M}$ denote the resolvent, i.e., ${\Re_{M}:={({{zI} - M})}^{- 1}}.$

### Lemma V.5

Let the controller $\mathbf{K}$ stabilize $(\hat{A},\hat{B})$ and $(\mathbf{\Phi}_{x},\mathbf{\Phi}_{u})$ be its corresponding system response (27 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again")) on system $(\hat{A},\hat{B})$. Then if $\mathbf{K}$ stabilizes $(A,B)$, it achieves the following LQR cost $J{(A,B,\mathbf{K})}$ defined as

controller $\mathbf{K}$ stabilizes $(A,B)$ if ${\|\hat{\mathbf{\Delta}}\|}_{\mathcal{H}_{\infty}} < 1$.

We can therefore pose a robust LQR problem as

The resulting robust control problem is one subject to real-parametric uncertainty, a class of problems known to be computationally intractable. To circumvent this issue, we instead find an upper-bound to the cost $J{(A,B,{\mathbf{K}})}$ that is independent of the uncertainties $\Delta_{A}$ and $\Delta_{B}$. First, note that if ${\|\hat{\mathbf{\Delta}}\|}_{\mathcal{H}_{\infty}} < 1$, we can write

This upper bound separates nominal performance, as captured by $J{(\hat{A},\hat{B},{\mathbf{K}})}$, from the effects of the model uncertainty, as captured by ${({1 - {\|\hat{\mathbf{\Delta}}\|}_{\mathcal{H}_{\infty}}})}^{- 1}$. It therefore remains to compute a tractable bound for ${\|\hat{\mathbf{\Delta}}\|}_{\mathcal{H}_{\infty}}$.

### Proposition V.6 (Proposition 3.5, \[62\])

For any $\alpha \in {}$ and $\hat{\mathbf{\Delta}}$ as defined in (33 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again")), we have

Applying Proposition 36 ‣ V-A PAC Bounds for Unknown (A,B) ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again") in conjunction with the bound (35 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again")), we arrive at the following upper bound to the cost function of the robust LQR problem (34 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again")), which is independent of the perturbations $(\Delta_{A},\Delta_{B})$:

The upper bound is only valid when ${H_{\alpha}{(\mathbf{\Phi}_{x},\mathbf{\Phi}_{u})}} < 1$, which guarantees the stability of the closed-loop system. Note that (37 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again")) can be used to upper bound the performance achieved by any robustly stabilizing controller.

We can then pose the robust LQR synthesis problem as the following quasi-convex optimization problem, which can be solved by gridding over $\gamma \in {\lbrack 0,1)}$:

As we constrain $\gamma \in {\lbrack 0,1)}$, any feasible solution $(\mathbf{\Phi}_{x},\mathbf{\Phi}_{u})$ to optimization problem (38 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again")) generates a controller ${\mathbf{K}} = {\mathbf{\Phi}_{u}\mathbf{\Phi}_{x}^{- 1}}$ that stabilizes the true system $(A,B)$.

### Remark V.7

Optimization problem (38 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again")) is infinite-dimensional. However, one can solve a finite-dimensional approximation of the problem over a horizon $T = \Omega{(\log{(1/{(\epsilon_{A} + \epsilon_{B})})}}$ (see Theorem 5.1, ) such that the sub-optimality bounds we prove below still hold up to universal constants.

We then have the following theorem bounding the sub-optimality of the proposed robust LQR controller.

### Theorem V.8

Let $J_{\star}$ denote the minimal LQR cost achievable by any controller for the dynamical system with transition matrices $(A,B)$, and let $K_{\star}$ denote the optimal contoller. Let $(\hat{A},\hat{B})$ be estimates of the transition matrices such that ${\|\Delta_{A}\|}_{2} \leq \epsilon_{A}$, ${\|\Delta_{B}\|}_{2} \leq \epsilon_{B}$. Then, if $\mathbf{K}$ is synthesized via (38 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again")) with $\alpha = {1/2}$, the relative error in the LQR cost is

as long as ${{({\epsilon_{A} + {\epsilon_{B}{\| K_{\star}\|}_{2}}})}{\|\Re_{A + {BK_{\star}}}\|}_{\mathcal{H}_{\infty}}} \leq {1/5}$.

The crux of the proof of Theorem V.8 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again") is to show that for sufficiently small $(\epsilon_{A},\epsilon_{B})$, the optimal LQR controller $K_{\star}$ is robustly stabilizing. We then exploit optimality to upper bound the cost ${({1 - \gamma})}^{- 1}J{(\hat{A},\hat{B},{\mathbf{K}})}$ achieved by our controller with that achieved by the optimal LQR controller ${({1 - \gamma_{LQR}})}^{- 1}J{(\hat{A},\hat{B},K_{\star})}$, from which the result follows almost immediately by repeating the argument with estimated and true systems reversed. Combining Theorems V.8 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again") and V.1 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again"), we see that ${{J{(A,B,{\mathbf{K}})}} - J_{\star}} \leq {O{({\epsilon_{A} + \epsilon_{B}})}} \leq {O{(\sqrt{{{({n + p})}{\log{({1/\delta})}}}/N})}}$. This in turn shows that LQR optimal control of an unknown system is $(\epsilon,\delta)$-episodic PAC learnable, where here we interpret each system identification experiment as an episode.

### Example 5

Figure 1: Left: The percentage of stabilizing controllers synthesized using certainty equivalence and robust LQR over 100 independent trials. Model estimates and uncertainty bounds are computed using independent rollouts with horizon T = 6. Right: Corresponding sub-optimality bounds. CE controllers outperform robust LQR controllers when they are stabilizing.

Consider an LQR problem specified by

In the left plot of Figure 1 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again"), we show the percentage of stabilizing controllers synthesized using certainty equivalence and the proposed robust LQR controllers over 100 independent trials.. Notice that even after collecting data from 100 trajectories, the CE controller yields unstable behavior in approximately 10% of cases. Given that the state of the underlying dynamical system is only 3-dimensional, one might consider 100 data-points to be a reasonable approximation of an "asymptotic" amount of data, highlighting the need for a more refined analysis of the effects of finite data on stability and performance. Contrast this with the behavior achieved by the robust LQR synthesis method, which explicitly accounts for system uncertainty: after a small number of trials, there is a sharp transition to 100% stability across trials. Further, feasibility of the synthesis problem (38 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again")) provides a certificate of stability and performance, conditioned on the uncertainty bounds being correct. However, robustness does come at a price: as shown in the right plot of Figure 1 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again"), the CE controller outperforms the robust LQR controller when it is stabilizing.

### V-B Regret Bounds under Moderate Uncertainty

We have just described an offline procedure for learning a coarse estimate of system dynamics and computing a robustly stabilizing controller. We now consider the task of adaptively refining this model and controller. For this problem, we seek high probability bounds on the regret $R{(T)}$, defined as

for $J_{\star}$ defined as in the previous section.

Consider the single trajectory least-squares estimator:

solved with data generated from system (23 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again")) driven by input $u_{t}\overset{\ \text{i.i.d.}}{\sim}{\mathcal{N}{(0,{\sigma_{u}^{2}I_{n_{u}}})}}$. The following result from Simchowitz et al. gives us a high probability bound on the error of the estimator.

### Theorem V.9 (\[63\])

Suppose that $A$ is stable and that the trajectory length $T$ satisfies:

With probability at least $1 - \delta$, the quantity $\max{\{{\parallel{\hat{A} - A}\parallel},{\parallel{\hat{B} - B}\parallel}\}}$ is bounded above by

Here, the $O{( \cdot )}$ hides specific properties of the controllability gramian.

Suppose we are provided with an initial stabilizing controller $\mathbf{K}$: how should we balance controlling the system (exploitation) with exciting it for system identification purposes (exploration)? We propose studying the simple exploration scheme ${{\mathbf{u}} = {{{\mathbf{K}}{\mathbf{x}}} + {\mathbf{η}}}},$ where $\eta_{t}\overset{\ \text{i.i.d.}}{\sim}{\mathcal{N}{(0,{\sigma_{\eta}^{2}I_{n_{u}}})}}$. Theorem V.9 ‣ V-B Regret Bounds under Moderate Uncertainty ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again") tells us that if we collect data for $T$ time-steps and compute estimates $({\hat{A}{(T)}},{\hat{B}{(T)}})$ using ordinary least squares, then with high probability we have that

when $\sigma_{\eta} \ll \sigma_{w}$. Furthermore, we saw in Theorem V.8 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again") that for a model error size bounded by $\epsilon$, that the sub-optimality incurred by a robust LQR controller $\mathbf{K}$ synthesized using problem (38 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again")) satisfies ${\hat{J} - J_{\star}} \leq {\overset{\sim}{O}{(\epsilon)}}$, where here we use $\hat{J}$ to denote the cost achieved by the controller $\mathbf{K}$. Letting ${\hat{J}}_{T}$ denote the $T$ horizon cost ${\mathbb{E}}{\lbrack{{\sum_{t = 1}^{T}{x_{t}^{\top}Qx_{t}}} + {u_{t}^{\top}Ru_{t}}}\rbrack}$ achieved by the robust LQR controller, we can show using a similar argument that ${{\hat{J}}_{T} - {TJ_{\star}}} \leq {\overset{\sim}{O}{({T\epsilon})}}$. However, we must also consider the performance degradation incurred by injecting the exploratory signal $\mathbf{η}$. As this signal is independent of all others, it is easy to see that it incurs an additional cost of $\overset{\sim}{O}{({T\sigma_{\eta}^{2}})}$. Combining these arguments, we conclude that

where the first term comes from combining the bound ${{\hat{J}}_{T} - {TJ_{\star}}} \leq {\overset{\sim}{O}{({T\epsilon})}}$ with. Setting $\sigma_{\eta}^{2} = {C_{\eta}T^{- {1/3}}}$ optimizes the right-hand side of the bounds, leading to ${{\hat{J}}_{T} - {TJ_{\star}}} \leq {\overset{\sim}{O}{(T^{2/3})}}$.

This reasoning was used in to develop an algorithm that achieves $\overset{\sim}{O}{(T^{2/3})}$ regret, with high probability, as captured by the regret measure. We informally summarize the algorithm and main results below before commenting on the strengths and weaknesses of the method.

1:Input: initial stabilizing controller K0, failure probability δ ∈ (0, 1], base epoch length CT, base exploration variance Cη
4: Collect data {xti,uti}t = 0Ti← evolve system for Ti stps with u = Ki x + ηi, with $\eta_{i,t}\overset{\ \text{i.i.d.}}{\sim}{\mathcal{N}\left( 0,{\sigma_{\eta,i}^{2}I_{n_{u}}} \right)}$
5: (Âi,B̂i,ϵi)← solve OLS problem using collected data and estimate uncertainty ϵi
Algorithm 1 Robust Adaptive LQR (Informal)

### Theorem V.10 (Informal, Theorems 3.2 & 3.3, \[77\])

With the system driven by Algorithm 1, we have with probability at least $1 - \delta$ that the estimates at time $T$ satisfy ${\max{({\parallel{\hat{A} - A}\parallel}_{2},{\parallel{\hat{B} - B}\parallel}_{2})}} \leq {\overset{\sim}{O}{({{({n_{x} + n_{u}})}^{\frac{1}{2}}T^{- \frac{1}{3}}})}}$, and that the regret satisfies ${R{(T)}} \leq {\overset{\sim}{O}{({{({n_{x} + n_{u}})}T^{2/3}})}}$.

Theorem V.10 ‣ V-B Regret Bounds under Moderate Uncertainty ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again") tells us that Algorithm 1 simultaneously leads to consistent estimates of the system matrices $(A,B)$ and near optimal performance, while providing high-probability guarantees on the stability and performance of the system over time. However, as shown in Figure 1 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again"), adding robustness to model uncertainty incurs a loss of performance. One might then ask how sub-optimal the $\overset{\sim}{O}{(T^{2/3})}$ regret bound is. Indeed, from the linear bandits literature, we know that it can be no lower than $\overset{\sim}{O}{(T^{1/2})}$. In the next subsection, we summarize the results of, which state that for sufficiently small uncertainty $\epsilon$, CE control is nearly optimal.

### V-C Regret Bounds under Small Uncertainty

Suppose that we can show that a nominal controller $K = {K{(\hat{A},\hat{B})}}$ computed using model estimates $(\hat{A},\hat{B})$ satisfying error bound, i.e., ${\max{({\parallel{\hat{A} - A}\parallel}_{2},{\parallel{\hat{B} - B}\parallel}_{2})}} \leq \epsilon$, satisfies ${\parallel{K - K_{\star}}\parallel} \leq {O{(\epsilon)}}$. Then, if we were able to take a 2nd order Taylor series expansion of the LQR cost $J{(K)}$ around the optimal controller $K_{\star}$, we would observe that:

where the first equality holds for some $\gamma \in {}$ by the mean value form of the Taylor series expansion, and the second equality holds by recognizing that ${{\nabla J}{(K_{\star})}} = 0$ as it must be a stationary point of the cost functional $J$. This intuitive argument is formalized in, wherein they explicitly quantify a bound on the error $\epsilon$ such that this approximation is valid.

### Theorem V.11 (Informal, Theorem 2, \[79\])

Let $\epsilon > 0$ be such that ${{\parallel{\hat{A} - A}\parallel}_{2},{\parallel{\hat{B} - B}\parallel}_{2}} \leq \epsilon$, and assume that ${Q,R} \succ 0$. Then the cost $\hat{J}$ achieved by applying control input $u_{t} = {K{(\hat{A},\hat{B})}x_{t}}$ satisfies

so long as $\epsilon$ is sufficiently small.

In the interest of space, we do not expand all of the problem dependent constants in bound (45 ‣ V-C Regret Bounds under Small Uncertainty ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again")), nor do we explicitly describe the required bounds on $\epsilon$; these are however available in. It is however worth noting that the bound (45 ‣ V-C Regret Bounds under Small Uncertainty ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again")) is applicable to a much smaller size of model uncertainty than the robust bound (39 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again")) provided in Theorem V.8 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again"). Within this local neighborhood, Theorem V.11 ‣ V-C Regret Bounds under Small Uncertainty ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again") implies that CE control leads to performance satisfying ${\hat{J} - J_{\star}} \leq {O{(\epsilon^{2})}}$, whereas the performance of the robust LQR controller only satisfies ${\hat{J} - J_{\star}} \leq {O{(\epsilon)}}$. Further, integrating this bound into the exploration/exploitation tradeoff, we see that the right hand side is now minimized by setting $\sigma_{\eta}^{2} = {C_{\eta}T^{- {1/2}}}$, leading to the desired ${{\hat{J}}_{T} - {TJ_{\star}}} \leq {\overset{\sim}{O}{(T^{1/2})}}$.

### Example 6

We consider the same dynamics (40 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again")), but set $Q = {10I}$. In Figure 2, from, we show a comparison of different adaptive methods on 500 experiments. The median and 90th percentiles are shown for the optimal controller, the certainty equivalence controller, the robust LQR controller, and heuristic implementations of the Thompson Sampling (TS) method proposed in and the Optimism in the Face of Uncertainty (OFU) based method proposed in. All methods achieve similar performance, and we note that the latter two methods assume that CE like control is guaranteed to be stabilizing, and further, that the OFU method requires solving a non-convex optimization problem as a subroutine.

Figure 2: A comparison of different adaptive methods on 500 experiments. The median and 90th percentiles are shown.

## Model-free Methods for LQR

We compare and contrast model-free methods from RL to the model-based methods of the previous section. We note that, while there is not a widely accepted technical definition of a model-free method, we informally a method to be model-free if it does not (as an intermediate step) estimate the transition dynamics $(A,B)$. Instead, the model-free methods we encounter either learn an alternative representation (such as a value function), or directly search for the optimal controller.

### VI-1 Overview of Model-free methods

### Approximate Policy Iteration

We start our discussion with a review of an important concept from RL known as the *state-action value function* or *$Q$-function.* Given a policy $\pi$, the (relative) state-action value function^44^4We change the quadratic state matrix in the cost to $S$ here as not to confuse it with the $Q$ function. is defined as

where $\lambda_{\pi}$ is the infinite-horizon average cost of the policy $\pi$, achieved via $u_{t} = {\pi{(x_{t})}}$. The Bellman equation associated to is:

*Policy iteration* (PI) is a classic algorithm from RL that works as follows. Fix a starting policy $\pi_{0}$. Then, iteratively repeat: Compute $Q_{t}$ as the state-value function for policy $\pi_{t}$, Update $\pi_{t + 1}$ as ${\pi_{t + 1}{(x)}} = {{\arg{\min_{u}Q_{t}}}{(x,u)}}$. Step of policy iteration generally requires knowledge of the transition dynamics. Of course, $Q^{\pi}$ for a given policy $\pi$ can be estimated from data. One such method, motivated by the Bellman equation, is based on temporal differences. Choose a finite set of basis functions ${\{\phi_{i}\}}_{i = 1}^{K}$, and suppose that $Q^{\pi}$ is well approximated in the span of $\phi_{i}$'s, i.e. $Q^{\pi} \approx {\sum_{i = 1}^{K}{w_{i}\phi_{i}}}$ for weights $w \in {\mathbb{R}}^{K}$. Then given $T$ state transition tuples ${\{{(x_{i},u_{i},x_{i + 1})}\}}_{i = 1}^{T}$, we can estimate the best fit weights $\hat{w}$ as:

Here, $\phi_{t} = {\phi{(x_{t},u_{t})}}$, where ${\phi{(x,u)}} \in {\mathbb{R}}^{K}$ is a column vector of each basis function $\phi_{i}$ evaluated at the pair $(x,u)$. Furthermore, $\psi_{t} = {\phi{(x_{t},{\pi{(x_{t})}})}}$, $c_{t}$ is the instantaneous cost observed for the $t$-th state transition, and ${\hat{\lambda}}_{\pi}$ is an estimate of $\lambda_{\pi}$, the infinite-horizon average cost under the policy $\pi$. This estimator $\hat{w}$ is known as the *least-squares temporal difference* estimator for $Q$-functions (LSTD-Q). The LSTD-Q estimator is an *off-policy* estimator, meaning that the input $u_{t}$ applied to generate the data does *not* have to follow the policy $\pi$. This is one of the advantages of working with $Q$-functions (as opposed to value functions). We now can state our first model-free algorithm, the least-squares policy iteration (LSPI) algorithm of: Estimate ${\hat{Q}}_{t} \approx Q^{\pi_{t}}$ from data via LSTD-Q, Update $\pi_{t + 1}$ as ${\pi_{t + 1}{(x)}} = {{\arg{\min_{u}{\hat{Q}}_{t}}}{(x,u)}}$.

### Derivative-free Search Methods

We now turn to methods which directly search for the optimal policy. Suppose we have a policy class $\Pi = {\{\pi_{\theta}:{\theta \in \Theta}\}}$ with $\Theta \subseteq {\mathbb{R}}^{p}$. We are interested in solving the following optimization problem: ${\min_{\theta \in \Theta}J}{(\theta)}$, where ${J{(\theta)}} = {J{(\pi_{\theta})}}$ is the infinite-horizon average cost performance of the policy $\pi_{\theta}$. In many problem formulations, the function $\theta\mapsto{J{(\theta)}}$ is differentiable on $\Theta$. Therefore, in principle one could run a local search method such as gradient descent: $\theta_{t + 1} = {\theta_{t} - {\eta{\nabla_{\theta}J}{(\theta_{t})}}}$. However, typically computing ${\nabla_{\theta}J}{(\theta)}$ requires knowledge of the dynamics. To get around this, in many practical situations one can efficiently generate (unbiased estimates) of $J{(\theta)}$ for any $\theta$ via rollouts or simulation. Therefore, we can rely on a rich history of zero-th order optimization. Here, we will focus on two popular zero-th order methods in RL.

### Policy Gradients (REINFORCE)

The policy gradient method was popularized by, and forms the foundation of many popular algorithms such as TRPO and PPO. The idea is to perturb the action sequence and use these perturbations to estimate gradient information. Let ${J_{\eta}{(\theta)}} = {\lim_{T\rightarrow\infty}{{\mathbb{E}}{\lbrack{\frac{1}{T}{\sum_{t = 1}^{T}c_{t}}}\rbrack}}}$ where $u_{t} = {{\pi_{\theta}{(x_{t})}} + \eta_{t}}$ with $\eta_{t}\overset{\ \text{i.i.d.}}{\sim}{\mathcal{N}{(0,{\sigma^{2}I})}}$. Now under sufficient regularity conditions that allow us to switch the order of differentiation with the limit and the integral,

We now observe that because the transition dynamics are not a function of $\theta$: ${{{\nabla_{\theta}\log}p}{(\tau_{1:T})}} = {\sum_{t = 1}^{T}{{{\nabla_{\theta}\log}p}{(\left. u_{t} \middle| x_{t} \right.)}}}$. Furthermore, because ${p{(\left. u_{t} \middle| x_{t} \right.)}}\overset{d}{=}{\mathcal{N}{({\pi_{\theta}{(x_{t})}},{\sigma^{2}I})}}$, we have that ${{{\nabla_{\theta}\log}p}{(\left. u_{t} \middle| x_{t} \right.)}} = {\frac{1}{\sigma^{2}}{({D\pi_{\theta}{(x_{t})}})}^{\top}\eta_{t}}$, where ${D\pi_{\theta}{(x_{t})}} \in {\mathbb{R}}^{d \times p}$ is the Jacobian of the map $\theta\mapsto{\pi_{\theta}{(x_{t})}}$. Therefore:

where the second and third equality both follow from iterating expectations and using the fact that ${{\mathbb{E}}{\lbrack\left. \eta_{t} \middle| {x_{1},\eta_{1},\ldots,x_{t}} \right.\rbrack}} = 0$. Here, $b{(\tau_{1:{t - 1}},x_{t})}$ is a *baseline* function which is chosen to reduce variance. Therefore, we can form a gradient estimate of $J_{\eta}{(\theta)}$ by choosing a large $T$, rolling out $T$ steps with $u_{t} = {{\pi_{\theta}{(x_{t})}} + \eta_{t}}$, and then forming $\hat{g} = {\frac{1}{T}{\sum_{t = 1}^{T}{\frac{{c{(\tau_{t:T})}} - {b{(\tau_{1:{t - 1}},x_{t})}}}{\sigma^{2}}{({D\pi_{\theta}{(x_{t})}})}^{\top}\eta_{t}}}}$.

### Random Search

We now consider random finite differences. There are many different variants of finite differences; we present one of the simpler methods. The idea here is to perturb the parameter space. Like for policy gradients, we consider a surrogate function $J_{\xi}{(\theta)}$ defined as ${J_{\xi}{(\theta)}} = {{\mathbb{E}}_{\xi}{\lbrack{J{({\theta + {\sigma\xi}})}}\rbrack}}$, where $\xi \sim {\mathcal{N}{(0,I)}}$. It is a standard fact that the gradient ${\nabla_{\theta}J_{\xi}}{(\theta)}$ is given by:

Hence we can construct a stochastic gradient by first choosing a large $T$, then sampling a random perturbation $\xi$, and finally rolling out a trajectory with $\pi_{\theta + {\sigma\xi}}$ and another with $\pi_{\theta - {\sigma\xi}}$, and using the estimate $\hat{g} = \frac{{\frac{1}{T}{\sum_{t = 1}^{T}c_{t}}} - {\frac{1}{T}{\sum_{t = 1}^{T}c_{t}^{\prime}}}}{2\sigma}$.

### VI-2 Experimental Evaluation

We compare the previously described model-free methods to the model-based nominal control (Section V-C) as a baseline. We consider the following LQR problem:

We choose an LQR problem where the $A$ matrix is stable, since the model-free methods we consider require an initial stabilizing controller; using a stable $A$ allows us to start at $K_{0} = 0_{2 \times 3}$. We fix the process noise $\sigma_{w} = 1$. As before, the model-based method learns $(A,B)$ using least-squares, exciting the system with Gaussian noise of variance $\sigma_{u} = 1$.

Figure 3: The performance of various model-free methods compared with the nominal (Section V-C) controller. The shaded regions represent the lower 10th and upper 90th percentile over 100 trials, and the solid line represents the median performance. Here, PG (simple) is policy gradients with the simple baseline, PG (vf) is policy gradients with the value function baseline, PI is least-squares policy iteration, and DFO is derivative-free optimization.

For policy gradients and derivative-free optimization, we use the projected stochastic gradient descent (SGD) method with a constant step size $\mu$ as the optimization procedure. The details of how we tuned each procedure are described in. For policy gradients we considered two different baselines. The *simple baseline* is the one that uses the empirical average cost $\frac{1}{T}{\sum_{t = 1}^{T}c_{t}}$ of the previous iteration as the baseline. The *value function* baseline uses ${b{(x_{t})}} = {x_{t}^{\top}Vx_{t}}$ where $V = {{\mathsf{d}\mathsf{l}\mathsf{y}\mathsf{a}\mathsf{p}}{({A + {BK}},{S + {K^{\top}RK}})}}$. Computing this $V$ requires knowledge of the model $(A,B)$: a practical implementation would need to also estimate $V$, further degrading performance.

Figure 3 shows that the nominal model-based controller substantially outperforms the model-free methods. We also see that the use of a baseline reduces the variance for policy gradients, the necessity of which is well understood in practice.

### VI-3 Separation Results

In the last section we saw that the model-based nominal method substantially outperformed the model-free methods we considered in our experiment. Can we make this rigorous? Here, we outline some results towards this, based on. For these results, we consider a finite length $T$ horizon LQR problem with no input penalty: ${\min_{u_{t}}{\mathbb{E}}}{\lbrack{\sum_{t = 1}^{T}{\parallel x_{t}\parallel}^{2}}\rbrack}$. We also only consider dynamics which have the special property that ${{range}{(A)}} \subseteq {{range}{(B)}}$ and $B$ has full column rank. These assumptions imply that the optimal solution is simply to cancel the state: $u_{t} = {- {B^{\dagger}Ax_{t}}}$. It means that the optimal solution on a finite horizon is time-invariant, which is typically not the case.

We first consider the risk of the model-based method. The following theorem characterizes the performance of the nominal method as the number of rollouts $N$ tends to infinity. It is an asymptotic version of Theorem V.11 ‣ V-C Regret Bounds under Small Uncertainty ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again")

### Theorem VI.1 (Theorem 2.4, \[86\])

The risk of the model-based nominal controller $\hat{K}$ on the $T$ length LQR problem described above satisfies:

Theorem VI.1 ‣ VI-3 Separation Results ‣ VI Model-free Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again") states that ${{\mathbb{E}}{\lbrack{{J{(\hat{K})}} - J_{\star}}\rbrack}} \approx {O{({{nd}/N})}}$ for large $N$. Next, we study the behavior of the policy gradient algorithm. We consider both a simple baseline ${b{(x_{t})}} = {\parallel x_{t}\parallel}^{2}$ and the value function baseline.

### Theorem VI.2 (Theorem 2.5, \[86\])

The risk of the model-free policy gradient controller $\hat{K}$ on the $T$ length LQR problem described for the *simple baseline* satisfies:

and for the *value function* baseline satisfies:

Above, the $O{( \cdot )}$ and $\Omega{( \cdot )}$ hides the dependence on various properties of $(A,B)$ such as ${\rho{(A)}},{\parallel B\parallel}_{F},{\sigma_{\min}{(B)}}$ as well as the noise variances $\sigma_{w},\sigma_{\eta}$. Comparing with Theorem VI.1 ‣ VI-3 Separation Results ‣ VI Model-free Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again"), Theorem VI.2 ‣ VI-3 Separation Results ‣ VI Model-free Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again") shows that policy gradient has worse sample complexity than the model-based nominal controller: ${{\mathbb{E}}{\lbrack{{J{(\hat{K})}} - J_{\star}}\rbrack}} \approx {\Omega{({{T^{2}n_{u}n_{x}^{3}}/N})}}$ for the simple baseline and ${{\mathbb{E}}{\lbrack{{J{(\hat{K})}} - J_{\star}}\rbrack}} \approx {\Omega{({{Tn_{u}n_{x}^{2}}/N})}}$ for the value function baseline. This result shows that, while more sophisticated baselines help, policy gradient still suffers from worse sample complexity than the nominal method by factors of horizon length $T$ and state dimension $n$.

Finally, we turn to an information-theoretic lower bound which states that the model-based nominal controller is optimal on this family of LQR instances.

### Theorem VI.3 (Theorem 2.6, \[86\])

Consider the family of dynamics ${\mathcal{G}{(\rho,n_{u})}}:={\{{({\rhoUU^{\top}},{\rhoU})}:{{U \in {\mathbb{R}}^{n_{x} \times n_{u}}},{{U^{\top}U} = I}}\}}$. Any algorithm $\mathcal{A}$ which plays feedbacks of the form $u_{t} = {{K_{i}x_{t}} + \eta_{t}}$ with ${\parallel K_{i}\parallel} \leq 1$ and $\eta_{t} \sim {\mathcal{N}{(0,{\sigma_{u}^{2}I})}}$ incurs risk:

if $n_{u} \leq {n_{x}/2}$ and $n_{u}{({n_{x} - n_{u}})}$ is greater than an absolute constant.

This result shows that the $O{({{n_{x}n_{u}}/N})}$ risk incurred by the nominal method is nearly optimal up to constant factors over any algorithm which plays inputs of the form $u_{t} = {{Kx_{t}} + \eta_{t}}$, which includes both the nominal method, the policy gradient methods, and the policy iteration method we described eariler.

## Conclusions

This tutorial paper and our companion paper presented a broad overview of recent progress towards the finite-time analysis for reinforcement learning and self-tuning control methods. We have attempted to provide a summary of representative results in this space that establish connections between the self-tuning control literature and methods recently proposed in reinforcement learning. The former are typically model-based, and are well-studied from a theoretical perspective, although more effort is still needed to better understand their finite-time behavior. The latter mostly adopt a model-free approach; they have had spectacular successes over the last few years, but lack strong theoretical guarantees, although researchers have been trying to validate design choices and algorithms a posteriori. Empirically, there is rich evidence that learning algorithms exploiting prior knowledge about the system (such as a model parameterization) are more sample-efficient, but are also more sensitive to biases introduced by modeling errors. Further, as we showed in Section VI, there exists scenarios where there is a quantitative and provable gap between model-based and model-free methods. A broader assessment of the advantages and drawbacks of modeling choices are however difficult to assess theoretically. This survey summarized recent progress towards this goal within the limited scope of tabular MDPs and linear optimal control, but we critically need to develop more broadly applicable tools towards the tighter analysis of learning algorithms.
