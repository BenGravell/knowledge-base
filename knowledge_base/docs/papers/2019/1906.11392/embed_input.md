<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

From Self-tuning Regulators to Reinforcement Learning and Back Again

Topics include Reinforcement learning, Robotics, Vehicles, Safety, Robustness, System identification, Distributed systems, Control, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Machine and reinforcement learning (RL) are increasingly being applied to plan and control the behavior of autonomous systems interacting with the physical world. Examples include self-driving vehicles, distributed sensor networks, and agile robots. However, when machine learning is to be applied in these new settings, the algorithms had better come with the same type of reliability, robustness, and safety bounds that are hallmarks of control theory, or failures could be catastrophic. Thus, as learning algorithms are increasingly and more aggressively deployed in safety critical settings, it is imperative that control theorists join the conversation. The goal of this tutorial paper is to provide a starting point for control theorists wishing to work on learning related problems, by covering recent advances bridging learning and control theory, and by placing these results within an appropriate historical context of system identification and adaptive control.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction & Motivation", "weight": 1.5} -->

With their recent successes in image classification, video game playing, sophisticated robotic simulations, and complex strategy games such as Go, machine and reinforcement learning (RL) are now being applied to plan and control the behavior of autonomous systems that interact with physical environments. Such systems, which include self-driving vehicles and agile robots, must interact with complex environments that are ever changing and difficult to model, strongly motivating the use of data-driven techniques. However, if machine learning is to be applied in these new settings, the resulting algorithms must come with the reliability, robustness, and safety guarantees that typically accompany results in the control theory literature, as failures could be catastrophic. Thus, as RL algorithms are increasingly and more aggressively deployed in safety critical settings, control theorists must be part of the conversation.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction & Motivation", "weight": 1.5} -->

To that end, it is important to recognize that while the applications areas and technical tools are new, the challenges faced -- uncertain and time varying systems and environments, unreliable sensing modalities, the need for robust stability and performance, etc. -- are not, and that many classical results from the system identification and adaptive control literature can be brought to bear on these problems. In the case of discrete time linear systems, adaptive control algorithms further come with strong guarantees of asymptotic consistency, stability, and optimality, and similarly elucidate some of the fundamental challenges that are still being wrestled with today, such as rapidly identifying a system model (exploration) while robustly/optimally controlling it (exploitation).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction & Motivation", "weight": 1.5} -->

Indeed, at a cursory glance, classical self-tuning regulators have the same objective as contemporary RL: an initial control policy and/or model is posited, data is collected, and a refined model/policy is produced, often in an online fashion. However, until recently, there has been relatively little contact between the two research communities. As a result, the tools and analysis objectives are different. One such feature, which will be the focus of this tutorial, is that RL and online learning algorithms are often analyzed in terms of *finite-data* guarantees, and as such, are able to provide *anytime guarantees* on the quality of the current behavior. Such finite-data guarantees are obtained by integrating tools from optimal control, stochastic optimization, and high-dimensional statistics -- whereas the first two tools are familiar to the controls community, the latter is less so. A major theme will be that of uncertainty quantification: indeed the importance of relating uncertainty quantification to control objectives was emphasized already in the 1960-70s. Moreover, the fragility of certainty equivalent control was one of the motivating factors for the development of robust adaptive control methodologies.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction & Motivation", "weight": 1.5} -->

In this tutorial paper and our companion paper, we highlight recent advances that provide non-asymptotic analysis of adaptive algorithms. Our aim is for these papers is for them to serve as a jumping off point for control theorists wanting to work in RL problems. In, we present an overview of tools and results on finite-data guarantees for system identification.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction & Motivation", "weight": 1.5} -->

Section II: provides an extensive literature review of work spanning classical and recent results in system identification, adaptive control, and RL.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction & Motivation", "weight": 1.5} -->

Section III: introduces the fundamental problem and performance metrics considered in RL, and relates them to examples familiar to the controls community.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction & Motivation", "weight": 1.5} -->

Section IV: provides a survey of contemporary results for problems with finite state and action spaces.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction & Motivation", "weight": 1.5} -->

Section V: shows how system estimates and error bounds can be incorporated into model-based self-tuning regulators with finite-time performance guarantees.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction & Motivation", "weight": 1.5} -->

Section VI: presents guarantees for model-free methods, and shows that a complexity gap exists between model-based and model-free methods.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Literature Review", "weight": 1.0} -->

The results we present in this paper draw heavily from three broad areas of control and learning theory: system identification, adaptive control, and approximate dynamic programming (ADP) or, as it has come to be known, reinforcement learning. Each of these areas has a long and rich history and a general literature review is outside the scope of this tutorial. Below we will instead emphasize pointers to good textbooks and survey papers, before giving a more careful account of recent work.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-1 System Identification", "weight": 1.0} -->

The estimation of system behavior from input/output experiments has a well-developed theory dating back to the 1960s, particularly in the case of linear-time-invariant systems. Standard reference texts on the topic include. The success of discrete time series analysis by Box and Jenkins provided an early impetus for the extension of these methods to the controlled system setting. Important connections to information theory were established by Akaike. The rise of robust control in the 1980s further inspired system identification procedures, wherein model errors were optimized under the assumption of adversarial noise processes. Another important step was the development of subspace methods, which became a powerful tool for identification of multi-input multi-output systems.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-2 Adaptive Control", "weight": 1.0} -->

System identification on real systems can be tedious, time consuming, and require skilled personnel. Adaptive control could then offer a simpler path forward. Moreover, adaptation offers an effective way to compensate for time-variations in the system dynamics. An early driving application was aircraft autopilot development in the 1950s. Aerospace applications needed control strategies that automatically compensated for changes in dynamics due to altitude, speed, and flight configuration. Another important early application was ship steering, where adaptation is used to compensate for wave effects. Standard textbooks include.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-2 Adaptive Control", "weight": 1.0} -->

A direct approach to adaptive control expounded by Bellman was to tackle the problem using dynamic programing by augmenting the state to contain the conditional distribution of the unknown parameters. From this it was seen that in such problems, control served the dual purpose of exciting the system to aid in its identification -- hence the term dual control. This approach suffered from the curse of dimensionality, which lead to the development of approximation techniques that ultimately evolved into modern day RL.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-2 Adaptive Control", "weight": 1.0} -->

A more practical approach was self-tuning adaptive control, pioneered by and followed by a long sequence of contributions to adaptive control theory, deriving conditions for convergence, stability, robustness and performance under various assumptions. For example, analysed adaptive algorithms using averaging, and derived an algorithm that gives mean square stability with probability one. On the other hand, conditions that may cause instability were studied, and. Finally, gave conditions for optimal asymptotic rates of convergence. More recent adaptive approaches include the L1 adaptive controller, and model free adaptive control.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-3 Automatic Tuning and Repeated Experiments", "weight": 1.0} -->

There is also an extensive literature on automatic procedures for initialization (tuning) of controllers, without further adaptation after the tuning phase. A successful example is auto-tuning of PID controllers, where a relay provides non-linear feedback during the tuning phase. Another important tuning approach, well established from an engineering perspective, is based on repeated experiments with linear time-invariant controllers. Theoretical bounds on a related approach were obtained by Lai and Robbins. Specifically, they showed that a pseudo-regret of the state variance is lower bounded by $\Omega{({\log{(T)}})}$. Subsequent work by Lai showed that this bound was tight. Recently, Raginsky revisited this problem formulation, and showed that for any persistently exciting controller, the time taken to achieve state variance less than $\epsilon$ is at least $\Omega{({\frac{n^{2}}{\epsilon}{\log{({1/\epsilon})}}})}$ for a system of dimension $n$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-4 Dynamic Programming and Reinforcement Learning", "weight": 1.0} -->

A major part of the literature on dynamic programming is devoted to "tabular MDPs," i.e. systems for which the state and action spaces are discrete and small enough to be stored in memory. The classic texts highlight computationally efficient approximation techniques for solving these problems. They include Monte Carlo methods, temporal-difference (TD) learning (which encompass SARSA and Q-learning ), value and Q-function approximation via Neural Networks, kernel methods, least-squares TD (LSTD), and policy gradient methods such as REINFORCE and Actor-Critic Methods.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-4 Dynamic Programming and Reinforcement Learning", "weight": 1.0} -->

Recent advances in both algorithms and computational power have allowed RL methods to solve incredibly complex tasks in very large discrete spaces that far exceed the tabular setting, including video games, Go, chess, and shogi. This success has renewed an interest in applying traditional model-free RL methods, such as Q-learning and policy optimization, to continuous problems in robotics. Thus far, however, the deployment of systems trained in this way has been limited to simulation environments or highly controlled laboratory settings, as the training process for these systems is both data hungry and highly variable.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-5 System Identification Revisited", "weight": 1.0} -->

With few exceptions (e.g., ), prior to the 2000s, the literature on system identification and adaptive control focused on asymptotic error characterization and consistency guarantees. In contrast, contemporary results in statistical learning seek to characterize *finite time and finite data* rates, leaning heavily on tools from stochastic optimization and concentration of measure. Such finite-time guarantees provide estimates of both system parameters and their uncertainty, allowing for a natural bridge to robust/optimal control. Early such results, characterizing rates for parameter identification, featured conservative bounds which are exponential in the system degree and other relevant quantities. More recent results, focused on state-space parameter identification for LTI systems, have significantly improved upon these bounds. In, the first polynomial time guarantees for identifying a stable linear system were provided -- however, these guarantees are in terms of predictive output performance of the model, and require rather stringent assumptions on the true system. In, it was shown, assuming that the state is directly measurable and the system is driven by white in time Gaussian noise, that solving a least-squares problem using independent data points taken from different trials achieves order optimal rates that are linear in the system dimension.

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-5 System Identification Revisited", "weight": 1.0} -->

This result was generalized to the single trajectory setting for (i) marginally stable systems, (ii) unstable systems, and (iii) partially observed stable systems. We note that analogous results also exist in the fully observed setting for the identification of sparse state-space parameters, where rates are shown to be logarithmic in the ambient dimension, and polynomial in the number of nonzero elements to be estimated.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-6 Automatic Tuning Revisited", "weight": 1.0} -->

There has been renewed interest, motivated in part by the expansion of reinforcement learning to continuous control problems, in the study of automatic tuning as applied to the Linear Quadratic Regulator. More closely akin to iterative learning control, Fietcher showed that the discounted LQR problem is Probably Approximately Correct (PAC) learnable in an episodic setting. In, Dean et al. dramatically improved the generality and sharpness of this result by extending it to the traditional infinite horizon setting, and leveraging contemporary tools from concentration of measure and robust control.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-7 Adaptive Control Revisited", "weight": 1.0} -->

Contemporary results tend to draw on ideas from the bandits literature. A non-asymptotic study of the adaptive LQR problem was initiated by Abbasi-Yadkori and Szepesvari. They use an Optimism in the Face of Uncertainty (OFU) based approach, where they maintain confidence ellipsoids of system parameters and select those parameters that lead to the best closed loop performance. While the OFU method achieves the optimal $O{(T^{1/2})}$ regret, solving the OFU sub-problem is computationally challenging. To address this issue, other exploration methods were studied. Thompson sampling is used to achieve $O{(T^{1/2})}$ regret for scalar systems, and studies a Bayesian setting with a particular Gaussian prior. Both and give tractable algorithms which achieve sub-linear frequentist regret of $O{(T^{2/3})}$ without the Bayesian setting of. Follow up work showed that this rate could be improved to $O{(T^{1/2})}$ by leveraging a novel semi-definite relaxation.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-7 Adaptive Control Revisited", "weight": 1.0} -->

More recently, show that as long as the initial system parameter estimates are sufficiently accurate, certainty equivalent (CE) control achieves $O{(T^{1/2})}$ regret with high probability. Finally, Rantzer shows that for a scalar system with a minimum variance cost criterion, a simple self-tuning regulator scheme achieves $O{({\log{(T)}})}$ expected regret after an initial burn in period, thus matching the lower bound established.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-7 Adaptive Control Revisited", "weight": 1.0} -->

Much of the recent work addressing the sample complexity of the LQR problem was motivated by the desire to understand RL algorithms on a simple baseline. In addition to the model-based approaches described above, model-free methods have also been studied. Model-free methods for the LQR problem were put on solid theoretical footing, where it was shown that controllability and persistence of excitation were sufficient to guarantee convergence to an optimal policy. In, the first finite time analysis for LSTD as applied to the LQR problem is given, in which they show that $O{({n^{3}/\epsilon^{2}})}$ samples are sufficient to estimate the value function up to $\epsilon$-accuracy, for $n$ the state dimension. Subsequently, Fazel et al. also showed that randomized search algorithms similar to policy gradient can learn the optimal controller with a polynomial number of samples in the noiseless case; however an explicit characterization of the dependence of the sample complexity on the parameters of the true system was not given, and the algorithm is dependent on the knowledge of an initially stabilizing controller.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-7 Adaptive Control Revisited", "weight": 1.0} -->

Similarly, Malik et al. study the behavior of random finite differencing for LQR. Finally, shows that there exists a family of systems for which there is a sample complexity gap of at least a factor of state dimension between LSTD/policy gradient methods and simple CE model-based approaches.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Fundamentals", "weight": 1.0} -->

We study the behavior of *Markov Decision Processes (MDP)*. In the finite horizon setting of length $T$, we consider

<!-- chunk {"id": "body-0028", "role": "body", "section": "Fundamentals", "weight": 1.0} -->

With slight abuse of notation, we will use $n_{x}$, $n_{u}$, and $n_{w}$ to denote (i) the dimension of $\mathcal{X}$, $\mathcal{U}$, and $\mathcal{W}$, respectively, when considering continuous state and action spaces, and (ii) the cardinality of $\mathcal{X}$, $\mathcal{U}$, and $\mathcal{W}$, respectively, when considering discrete state and action spaces.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Fundamentals", "weight": 1.0} -->

We consider settings where both the cost functions ${\{ c_{t}\}}_{t = 0}^{T}$ and the dynamics functions ${\{ f_{t}\}}_{t = 0}^{T}$ may not be known. Finally, we assume that the primitive random variables $(x_{0},w_{0:T})$ are defined over a common probability space with known and independent distributions -- the expectation in the cost is taken with respect to these and the policy $\mathbf{π}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-A Dynamic Programming Solutions", "weight": 1.0} -->

When the transition functions $\{ f_{t}\}$ and costs $\{ c_{t}\}$ are known, problem can be solved using dynamic programming. As the dynamics are Markovian, we restrict our search to policies of the form $u_{t} = {\pi_{t}{(x_{t})}}$ without loss of optimality. Define the value function of problem at time $t$ to be

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-A Dynamic Programming Solutions", "weight": 1.0} -->

Iterating through this process yields both an optimal policty ${\mathbf{π}}^{\star}$, and the optimal cost-to-go $V_{0}{(x_{0})}$ that it achieves.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-A Dynamic Programming Solutions", "weight": 1.0} -->

We begin by introducing the discounted cost setting, wherein the cost-functional in optimization is replaced with

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-A Dynamic Programming Solutions", "weight": 1.0} -->

for some $\gamma \in {(0,1\rbrack}$. Note that if $c{(x_{t},u_{t})}$ is bounded almost surely and $\gamma < 1$, then the infinite sum is guaranteed to remain bounded, greatly simplifying analysis.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-A Dynamic Programming Solutions", "weight": 1.0} -->

from which it follows immediately that the optimal value function $V_{\star}$ will satisfy

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-A Dynamic Programming Solutions", "weight": 1.0} -->

and $u_{\star} = {\pi_{\star}{(x)}}$. One can show that under mild technical assumptions, iterative procedures such as policy iteration and value iteration will converge to the optimal policy.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-A Dynamic Programming Solutions", "weight": 1.0} -->

Next, we consider the asymptotic average cost setting, in which case the cost-functional in problem is set to

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-A Dynamic Programming Solutions", "weight": 1.0} -->

Care must be taken to ensure that the limit converges, thus somewhat complicating the analysis -- however, this cost functional is often most appropriate for guaranteeing the stability for stochastic optimal control problems.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Example 1 (Linear Quadratic Regulator)", "weight": 1.0} -->

where the system state $x_{t} \in {\mathbb{R}}^{n_{x}}$, the control input $u_{t} \in {\mathbb{R}}^{n_{u}}$, and the disturbance process $w_{t} \in {\mathbb{R}}^{n_{x}}$ are independently and identically distributed as zero mean Gaussian random variables with a known covariance matrix $\Sigma_{w}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Example 1 (Linear Quadratic Regulator)", "weight": 1.0} -->

For a finite horizon $T$ and known matrices $(A,B)$, this problem can be solved directly via dynamic programming, leading to the optimal control policy

<!-- chunk {"id": "body-0040", "role": "body", "section": "Example 1 (Linear Quadratic Regulator)", "weight": 1.0} -->

where $P_{t} \succeq 0$ satisfies the Discrete Algebraic Riccati (DAR) Recursion initialized at ${P_{T} = Q_{T}}.$ Further, when the triple $(A,B,Q^{1/2})$ is stabilizable and detectable, the closed loop system is stable and hence converges to a stationary distribution, allowing us to consider the asymptotic average cost setting, at which point the optimal control action is a static policy, defined as in (8 ‣ III-A Dynamic Programming Solutions ‣ III Fundamentals ‣ From self-tuning regulators to reinforcement learning and back again")), but with $P_{t}\rightarrow P$, for $P \succeq 0$ a solution of the corresponding DAR Equation.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Example 2 (Tabular MDP)", "weight": 1.0} -->

Consider the setting where the state-space $\mathcal{X}$, the control space $\mathcal{U}$, and the disturbance process space $\mathcal{W}$ have finite cardinalities of $n_{x}$, $n_{u}$, and $n_{w}$, respectively, and further suppose that the underlying dynamics are governed by transition probabilities $P{({x_{t + 1} = \left. x^{\prime} \middle| {x_{t},u_{t}} \right.})}$. We assume that the cardinalities $n_{x}$, $n_{u}$, and $n_{w}$ are such that $\mathcal{X}$, $\mathcal{U}$, and $\mathcal{W}$ can be stored in tabular form in memory and worked with directly.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Example 2 (Tabular MDP)", "weight": 1.0} -->

In the case of average cost, for simplicity, we restrict our attention to communicating and ergodic MDPs. The former correspond to scenario where for any two states, there exists a stationary policy leading from one to the other with positive probability. For the latter, any stationary policy induces an ergodic Markov chain. In the average cost setting, one wishes to minimize $\lim_{T\rightarrow\infty}{\frac{1}{T}V_{T}{(x)}}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Example 2 (Tabular MDP)", "weight": 1.0} -->

More precisely, the objective is to identify as fast as possible a stationary policy $\pi$ with maximal gain function $g^{\pi}$: for any $x \in \mathcal{X}$, ${g^{\pi}{(x)}}:={\lim_{T\rightarrow\infty}{\frac{1}{T}V_{T}^{\pi}{(x)}}}$ where $V_{T}^{\pi}{(x)}$ denotes the average cost under $\pi$ starting in state $x$ over a time horizon $T$. When the MDP is ergodic, this gain does not depend on the initial state. To compute the gain of a policy, we need to introduce the bias function ${h^{\pi}{(x)}}:={{\text{C}\text{-}}{\lim_{T\rightarrow\infty}{{\mathbb{E}}^{\pi}{\lbrack{\left.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Example 2 (Tabular MDP)", "weight": 1.0} -->

The gain and bias functions $g^{\star}{(x)}$ and $h^{\star}{(x)}$ of an optimal policy verify Bellman's equation: for all $x$,

<!-- chunk {"id": "body-0045", "role": "body", "section": "Example 2 (Tabular MDP)", "weight": 1.0} -->

When the transition probabilities and cost function are known, this problem can then be solved via value-iteration, policy-iteration, and linear programming.

<!-- chunk {"id": "body-0046", "role": "body", "section": "III-B Learning to Control MDPs with Unknown Dynamics", "weight": 1.0} -->

Thus far we have considered settings where the dynamics $\{ f_{t}\}$ and costs $\{ c_{t}\}$ are known. Our main interest is understanding what should be done when these models are not known. Our study will focus on the previous two examples, namely LQR and the tabular MDP setting. While much of current work in reinforcement learning focusses on *model-free* methods, we adopt a more control theoretic perspective on the problem and study model-based methods wherein we attempt to approximately learn the system model ${\{ f_{t}\}}_{t = 0}^{T}$, and then subsequently use this approximate model for control design.

<!-- chunk {"id": "body-0047", "role": "body", "section": "III-B Learning to Control MDPs with Unknown Dynamics", "weight": 1.0} -->

Before continuing, we distinguish between episodic and single-trajectory settings. An *episodic task* is akin to traditional *iterative learning control*, wherein a task is repeated over a finite horizon, after which point the episode ends, and the system is reset to begin the next episode. In contrast, a *single-trajectory task* is akin to traditional *adaptive control*, in that no such resets are allowed, and a single evolution of the system under an adaptive policy is studied.

<!-- chunk {"id": "body-0048", "role": "body", "section": "III-B Learning to Control MDPs with Unknown Dynamics", "weight": 1.0} -->

An underlying tension exists between identifying an unknown system and controlling it. Indeed it is well known that without sufficient *exploration* or *excitation*, an incorrect model will be learned, possibly leading to suboptimal and even unstable system behavior; however, this exploration inevitably degrades system performance. Informally, this tension leads to a fundamental tradeoff between how quickly a model can be learned, and how well it can be controlled during this process. Current efforts seek to explicitly address and quantify these tradeoffs through the use of performance metrics such as the Probably Approximately Correct (PAC) and Regret frameworks, which we define next. For episodic tasks, we assume the horizon of each episode to be of length $H$, and consider guarantees on performance as a function of the number of episodes $T$ that have been evaluated. For single trajectory tasks, we consider infinite horizon problems, and the definitions provided are equally applicable to the discounted and asymptotic average cost settings. The definitions that follow are adapted, among others.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Episodic PAC-Bounds", "weight": 1.0} -->

We consider episodic tasks over a horizon $H$, where $H$ may be infinite but the user is allowed to reset the system at a prescribed time $H_{r}$. Let $V_{\star}$ be the optimal cost achievable, and $N_{\epsilon}$ be the number of episodes for which $\mathbf{π}$ is not $\epsilon$-optimal, i.e., the number of episodes for which $V_{\mathbf{π}} > {V_{\star} + \epsilon}$. Then, a policy $\mathbf{π}$ is said to be episodic-$(\epsilon,\delta)$-PAC if, after $T$ episodes, it satisfies^11^1We note that in the discounted setting, we also ask that the bound on $N_{\epsilon}$ depend polynomially on $1/{({1 - \gamma})}$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Episodic PAC-Bounds", "weight": 1.0} -->

We also note that modern definitions of PAC-learning require that the bound on $N_{\epsilon}$ depend polynomially on $\log{({1/\delta})}$ -- this is a reflection of results from contemporary high-dimensional statistics that allow for more refined concentration of measure guarantees. Finally, the polynomial dependence on the horizon $H$ is only enforced for finite horizons $H$ -- in the case of an infinite horizon task, $N_{\epsilon}$ must not depend on the $H$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Episodic PAC-Bounds", "weight": 1.0} -->

These guarantees state that the chosen policy is $\epsilon$-optimal on all but a number of episodes polynomial in the problem parameters, with probability at least $1 - \delta$. Many $(\epsilon,\delta)$ PAC algorithms operate in two phases: the first is solely one of exploration so as to identify an approximate system model, and the second is solely one of exploitation, wherein the approximate system model is used to synthesize a control policy. Therefore, informally one can view PAC guarantees as characterizing the number of episodes needed to identify a model that can be used to synthesize an $\epsilon$-optimal policy.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Example 3 (LQR is episodic PAC-Learnable)", "weight": 1.0} -->

The results in imply that the LQR problem with an asymptotic average cost is episodic PAC-learnable. In particular, it was shown that a simple open-loop exploration process of injecting white in time Gaussian noise over at most ${poly}{(n_{x},n_{u},H_{r},{1/\epsilon},{\log{({1/\delta})}})}$ episodes, followed by a least-squares system identification and uncertainty quantification step, can be used with a robust synthesis method to generate a policy $\mathbf{π}$ which guarantees that

<!-- chunk {"id": "body-0053", "role": "body", "section": "Example 3 (LQR is episodic PAC-Learnable)", "weight": 1.0} -->

when the LQR problem is initialized at $x_{0} = 0$. Hence the resulting algorithm meets the modern definition of being $(\epsilon,\delta)$-PAC-learnable. We revisit this example in Section V.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Single-trajectory PAC-Bounds", "weight": 1.0} -->

We consider single-trajectory tasks over an infinite horizon, and let $V_{\mathbf{π}}{(x_{t})}$ denote the cost-to-go from state $x_{t}$ achieved by a policy $\mathbf{π}$, and $V_{\star}{(x_{t})}$ be the optimal cost-to-go achievable. We further let $N_{\epsilon}$ be the number of time-steps for which $\mathbf{π}$ is not $\epsilon$-optimal in either an absolute or relative sense, i.e., the number of time-steps for which ${V_{\mathbf{π}}{(x_{t})}} > {{V_{\star}{(x_{t})}} + \epsilon}$ or ${V_{\mathbf{π}}{(x_{t})}} > {V_{\star}{(x_{t})}{({1 + \epsilon})}}$, respectively.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Single-trajectory PAC-Bounds", "weight": 1.0} -->

Then, a policy $\mathbf{π}$ is said to be $(\epsilon,\delta)$-PAC if it satisfies^22^2We make the same modifications to this definition for the discounted case and the dependence on $1/\delta$ as in the episodic setting.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Single-trajectory PAC-Bounds", "weight": 1.0} -->

These guarantees should be interpreted as saying that the chosen policy is at worst $\epsilon$-suboptimal on all but ${poly}{(\frac{1}{\epsilon},{\log{({1/\delta})}})}$ time-steps, with probability at least $1 - \delta$. As in the episodic setting, one can view these PAC guarantees as characterizing the number of time-steps needed to identify a model that can be used to synthesize an $\epsilon$-optimal policy.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Limitations of PAC-Bounds", "weight": 1.5} -->

As an algorithm that is $(\epsilon,\delta)$-PAC is only penalized for suboptimal behavior exceeding the $\epsilon$ threshold, there is no guarantee of convergence to an optimal policy. In fact, as pointed out in and illustrated in the LQR example above, many PAC algorithms cease learning once they are able to produce an $\epsilon$-suboptimal strategy.

<!-- chunk {"id": "body-0058", "role": "body", "section": "III-D Regret Bounds", "weight": 1.0} -->

We focus on regret bounds for the single-trajectory setting, as this is the most common type of guarantee found in the literature, but note that analogous episodic definitions exist (cf., ). The regret framework evaluates the quality of an adaptive policy by comparing its running cost to a suitable baseline. Let $b_{T}$ represent the baseline cost at time $T$, and define the regret incurred by a policy ${\mathbf{π}} = {\{\pi_{0},\pi_{1},\ldots\}}$ to be

<!-- chunk {"id": "body-0059", "role": "body", "section": "III-D Regret Bounds", "weight": 1.0} -->

Note that $b_{T}$ is user specified, and is often chosen to be the expected optimal cost achievable by a policy with full knowledge of the system dynamics. The two most common regret guarantees found in the literature are expected regret bounds, and high probability regret bounds. In the expected regret setting, the goal is to show that

<!-- chunk {"id": "body-0060", "role": "body", "section": "III-D Regret Bounds", "weight": 1.0} -->

whereas in the high-probability regret setting, the goal is to show that^33^3As in the PAC setting, modern definitions often require the dependence to be polynomial in $\log{({1/\delta})}$.

<!-- chunk {"id": "body-0061", "role": "body", "section": "III-D Regret Bounds", "weight": 1.0} -->

These bounds therefore quantify the rate of convergence of the cost achieved by the adaptive policy to the baseline cost, providing *any time guarantees* on performance relative to a desirable baseline. From the definition of $R^{\pi}{(T)}$, it is clear that one should strive for an $o{(T)}$ dependence, as this implies that the cost achieved by the adaptive policy converges with at least sub-linear rate to the base cost $b_{T}$. Further, in contrast to the PAC framework, *all sub-optimal behavior* is tallied by the running regret sum, and hence exploration and exploitation must be suitably balanced to achieve favorable bounds.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Example 4 (Regret bounds for LQR)", "weight": 1.0} -->

The study of regret bounds for LQR was initiated. Here we summarize a recent treatment of the problem, as provided. There, the authors study the performance of CE control for LQR, and study a regret measure of the form

<!-- chunk {"id": "body-0063", "role": "body", "section": "Example 4 (Regret bounds for LQR)", "weight": 1.0} -->

with probability at least $1 - \delta$ so long as $\sigma_{\eta,t}^{2} \sim t^{- {1/2}}$ and the initial estimates of the system dynamics $(\hat{A},\hat{B})$ are sufficiently accurate. We revisit this example in Section V.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Limitations of Regret Bounds", "weight": 1.5} -->

As regret only tracks the integral of suboptimal behavior, it does not distinguish between a few severe mistakes and many small ones. In fact, shows that for Tabular MDP problems, an algorithm achieving optimal regret may still make infinitely many mistakes that are maximally suboptimal. Thus regret bounds cannot provide guarantees about transient worst-case deviations from the baseline cost $b_{T}$, which may have implications on guaranteeing the robustness or safety of an algorithm. We comment further on regret for discrete MDPs in the next section.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Optimal control of unknown discrete systems", "weight": 1.0} -->

This section addresses reinforcement learning for stationary MDPs with finite state and control spaces of respective cardinalities $n_{x}$ and $n_{u}$. When the system is in state $x$ and the control input is $u$, the system evolves to state $x^{\prime}$ with probability $p{(\left. x^{\prime} \middle| {x,u} \right.)}$, and the cost $c_{t}{(x,u)}$ induced is independently drawn from a distribution $q{( \cdot |x,u)}$ with expectation $c{(x,u)}$. Costs are bounded, and for any $(x,u)$, the distribution $q{( \cdot |x,u)}$ is absolutely continuous w.r.t. to a measure $\lambda$ (for example, Lebesgue measure).

<!-- chunk {"id": "body-0066", "role": "body", "section": "Optimal control of unknown discrete systems", "weight": 1.0} -->

We consider both average-cost and discounted MDPs (refer to Example 2), and describe methods (i) to derive fundamental performance limits (in terms of regret and sample complexity), and (ii) to devise efficient learning algorithms. The way the learner samples the MDP may significantly differs in the literature, depending on the objective (average or discounted cost), and on whether one wishes to derive fundamental performance limits or performance guarantees of a given algorithm. For example, in the case of average cost, typically, the learner gathers information about the system in an online manner following the system trajectory, a sampling model referred previously to as the single trajectory model. Most sample complexity ananlyses are on the contrary derived under the so-called generative model, where any state-control pair can be sampled in $O{}$ time. Generative models are easier to analyze but hide the difficult issue of navigating the state space to explore various state-control pairs.

<!-- chunk {"id": "body-0067", "role": "body", "section": "IV-A Average-cost MDPs", "weight": 1.0} -->

For average-cost MDPs, we are primarily interested in devising algorithms with minimum regret, defined for a given learning algorithm $\pi$ as

<!-- chunk {"id": "body-0068", "role": "body", "section": "IV-A Average-cost MDPs", "weight": 1.0} -->

where $x_{t}^{\pi}$ and $u_{t}^{\pi}$ are the state and control input under the policy $\pi$ at time-step $t$, and similarly the superscript $\star$ corresponds to an optimal stationary control policy. Next, we discuss the type of regret guarantees we could aim.

<!-- chunk {"id": "body-0069", "role": "body", "section": "IV-A Average-cost MDPs", "weight": 1.0} -->

Expected vs. high-probability regret. We would ideally wish to characterize the complete regret distribution. This is however hard, and most existing results provide guarantees either in expectation or with high probability. In the case of finite state and control spaces, guarantees in high-probability can be easy to derive and not very insightful. Consider for example, a stochastic bandit problem (a stateless MDP) where the goal is to identify the control input with the lowest expected cost. An algorithm exploring each control input at least $\log{({1/\delta})}$ times would yield a regret in $\mathcal{O}{({\log{({1/\delta})}})}$ with probability greater than $1 - \delta$ (this is a direct application of Hoeffding's inequality). This simple observation only holds for a fixed MDP (the gap between the costs of the various inputs cannot depend on $\delta$ nor on the time at which regret is evaluated), and relies on the assumption of bounded costs.

<!-- chunk {"id": "body-0070", "role": "body", "section": "IV-A Average-cost MDPs", "weight": 1.0} -->

Even in the simplistic stochastic bandit problem, analyzing the distribution of the regret remains an open and important challenge, refer to for initial discussions and results.

<!-- chunk {"id": "body-0071", "role": "body", "section": "IV-A Average-cost MDPs", "weight": 1.0} -->

Problem-specific vs. minimax regret guarantees. A regret upper bound is problem-specific if it explicitly depends on the parameters defining the MDP. Such performance guarantees capture and quantify the hardness of learning to control the system. Minimax regret guarantees are far less precise and informative, since they concern the worst system among possibly all systems. An algorithm with good minimax regret upper bound behaves well in the worst case, but does not necessarily learn and adapt to the system it aims at controlling.

<!-- chunk {"id": "body-0072", "role": "body", "section": "IV-A Average-cost MDPs", "weight": 1.0} -->

Guided by the above observations, we focus on the expected regret, and always aim, when this is possible, at deriving problem-specific performance guarantees.

<!-- chunk {"id": "body-0073", "role": "body", "section": "IV-A1 Regret lower bounds", "weight": 1.0} -->

We present here a unified simple method to derive both problem-specific and minimax regret lower bounds. This method has been developed mainly in the bandit optimization literature as a simplified alternative to Lai and Robbins techniques.

<!-- chunk {"id": "body-0074", "role": "body", "section": "IV-A1 Regret lower bounds", "weight": 1.0} -->

Let $\phi = {(p,q)}$ denote the true MDP. Consider a second MDP $\psi = {(p^{\prime},q^{\prime})}$. For a given learning algorithm $\pi$, define by $\mathcal{L}^{\pi}{(T)}$ the log-likelihood ratio of the corresponding observations under $\phi$ and $\psi$.

<!-- chunk {"id": "body-0075", "role": "body", "section": "IV-A1 Regret lower bounds", "weight": 1.0} -->

where $N_{xu}^{\pi}{(T)}$ is the number of times the state-control pair $(x,u)$ is observed, where ${\mathbb{E}}_{\phi}^{\pi}$ is the expectation taken w.r.t. to the distrbution of observations made under $\pi$ for the MDP $\phi$, and where $KL_{\phi|\psi}{(x,u)}$ is the KL divergence between the distributions of the observations made in $(x,u)$ under $\phi$ and $\psi$.

<!-- chunk {"id": "body-0076", "role": "body", "section": "IV-A1 Regret lower bounds", "weight": 1.0} -->

Now the data processing inequality states that for any event $E$ or any $\lbrack 0,1\rbrack$-valued random variable depending on all observations up to time $T$, i.e.,

<!-- chunk {"id": "body-0077", "role": "body", "section": "IV-A1 Regret lower bounds", "weight": 1.0} -->

where $kl{(a,b)}$ is the KL divergence between two Bernoulli distributions of respective means $a$ and $b$. Now combining the above inequality to yields a lower bound on a weighted sum of the expected numbers of times each state-control pair is selected.

<!-- chunk {"id": "body-0078", "role": "body", "section": "IV-A1 Regret lower bounds", "weight": 1.0} -->

where $\mathcal{O}{(x,\phi)}$ denotes the set of optimal control inputs in state $x$ under $\phi$, and $\delta^{\star}{(x,u;\phi)}$ is the sub-optimality gap quantifying the regret obtained by selecting the control $u$ is state $x$. It remains to select the event $E$ or the random variable $Z$ to get a regret lower bound.

<!-- chunk {"id": "body-0079", "role": "body", "section": "IV-A1 Regret lower bounds", "weight": 1.0} -->

To derive problem-specific regret lower bounds, we introduce the notion of uniformly good algorithms. $\pi$ is uniformly good if for any ergodic MDP $\phi$, any initial state and any constant $\alpha > 0$, ${{\mathbb{E}}_{\phi}^{\pi}{\lbrack{R^{\pi}{(T)}}\rbrack}} = {o{(T^{\alpha})}}$. As it will become clear later, uniformly good algorithms exist.

<!-- chunk {"id": "body-0080", "role": "body", "section": "IV-A1 Regret lower bounds", "weight": 1.0} -->

In the change-of-measure argument, $\psi$ is chosen such that ${{\Pi^{\star}{(\phi)}} \cap {\Pi^{\star}{(\psi)}}} = \varnothing$, where $\Pi^{\star}{(\phi)}$ is the set of optimal policies under $\phi$. Now if $\pi$ is uniformly good, $E$ is very likely under $\phi$, and very unlikely under $\psi$.

<!-- chunk {"id": "body-0081", "role": "body", "section": "IV-A2 Efficient Algorithms", "weight": 1.0} -->

A plethora of learning algorithms have been developed for average-cost MDPs. We can categorize these algorithms based on their design principles. A first class of algorithms aim at matching the asymptotic problem-specific regret lower bound derived above. These algorithms rely on estimating the MDP parameters and in each round (or periodically) they solve the optimization problem where the true MDP parameters are replaced by their estimators. The solution is then used to guide and minimize the exploration process. This first class of algorithms is discussed further in §IV-A3.

<!-- chunk {"id": "body-0082", "role": "body", "section": "IV-A2 Efficient Algorithms", "weight": 1.0} -->

The second class of algorithms includes UCRL, UCRL2 and KL-UCRL. These algorithms apply the "optimism in front of uncertainty" principle and exhibit finite-time regret ganrantees. They consists in building confidence upper bounds on the parameters of the MDP, and based on these bounds select control inputs. The regret guarantees are anytime, but use worst-case regret as a performance benchmark.

<!-- chunk {"id": "body-0083", "role": "body", "section": "IV-A3 Structured MDPs", "weight": 1.0} -->

The regret lower bounds derived for tabular MDPs have the major drawback of scaling with the product of the numbers of states and controls, $n_{x}n_{u}$. Hence, with large state and control spaces, it is essential to identify and exploit any possible structure existing in the system dynamics and cost function so as to minimize exploration phases and in turn reduce regret to reasonable values. Modern RL algorithms actually implicitly impose some structural properties either in the model parameters (transition probabilities and cost function, see e.g. ) or directly in the $Q$-function (for discounted RL problems, see e.g.. Despite their successes, we do not have any regret guarantees for these recent algorithms. Recent efforts to develop algorithms with guarantees for structured MDPs include. is the first paper extending the analysis of to the case of structured MDPs. The authors derive a problem-specific regret lower bound, and show that the latter can be obtained by just modifying in Theorem IV.1 the definition of the set of confusing MDPs $\Delta{(\phi)}$.

<!-- chunk {"id": "body-0084", "role": "body", "section": "IV-B Discounted MDPs", "weight": 1.0} -->

Most research efforts, from early work to more recent Deep RL, towards the design of efficient algorithms for discounted MDPs have focussed on model-free approaches, where one directly learns the value or the Q-value function of the MDP. Such an approach leads to simple algorithms that are potentially more robust than model-based algorithms (since they do not rely on modelling assumptions). The performance analysis of these algorithms has been initially mainly centered around the question of their convergence; for example, the analysis of $Q$-learning algorithm with function approximation often calls for new convergence results of stochastic approximation schemes. Researchers have then strived to investigate and optimize their convergence rates. There is no consensus on the metric one should use to characterize the speed of convergence; e.g. the recent Zap Q-learning algorithm minimizes the asymptotic error covariance matrix, while most other analayses focus on the minimax sample complexity. Note that the notion of regret in discounted settings is hard to define and has hence not been studied. Also observe that problem-specific metrics have not been investigated yet, and it hence seems perilous to draw definitive conclusions from existing theoretical results for learning discounted MDPs.

<!-- chunk {"id": "body-0085", "role": "body", "section": "IV-B1 Sample complexity lower bound", "weight": 1.0} -->

For discounted MDPs, the sample complexity is defined as the number of samples one need to gather so as to learn an $\epsilon$-optimal policy with probability at least $1 - \delta$.

<!-- chunk {"id": "body-0086", "role": "body", "section": "IV-B2 The price of model-free approaches", "weight": 1.0} -->

Some model-based algorithms are known to match the minimax sample complexity lower bound. In the online sampling setting, the authors of presents UCRL($\gamma$), an extension of UCRL for discounted costs, and establish a minimax sample complexity upper bound matching the above lower bound. UCRL($\gamma$) consists in deriving upper confidence bounds for the MDP parameters, and in selecting action optimistically (this can lead to important computational issues). In the generative sampling model, algorithms mixing model-based and model-free approaches have been shown to be minimax-sample optimal. This is the case of QVI (Q-value Iteration) initially proposed in and analyzed. QVI estimates the MDP, and from this estimator, applies a classical value iteration method to approximate the $Q$-function and hence the optimal policy. QVI can be also made computationally efficient.

<!-- chunk {"id": "body-0087", "role": "body", "section": "IV-B2 The price of model-free approaches", "weight": 1.0} -->

As for now, there is no pure model-free algorithm achieving the minimax sample complexity limit. Speedy Q-learning has a minimax sample complexity in $\overset{\sim}{\mathcal{O}}{(\frac{n_{x}n_{u}}{\epsilon^{2}{({1 - \gamma})}^{4}})}$ (this is for now the best one can provably do using model-free approaches). However, there is hope to find model-free minimax-sample optimal algorithms. In fact, recently, $Q$-learning with exploration driven by simple upper confidence bounds on the $Q$-values (rather than on the MDP parameters as in UCRL) has been shown to be minimax regret optimal for episodic reinforcement learning tasks. It is likely that model-free algorithms can be made minimax optimal. If this is verified, this would further advocate the use of model-specific rather than minimax performance metrics.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Model-Based Methods for LQR", "weight": 1.0} -->

We combine the techniques described in with robust and optimal control to derive finite-time guarantees for the optimal LQR control of an unknown system. We partition our study according to three initial uncertainty regimes: (i) completely unknown $(A,B)$, (ii) moderate error bounds under which CE control may fail, and (iii) small error bounds under which CE control is stabilizing.

<!-- chunk {"id": "body-0089", "role": "body", "section": "V-A PAC Bounds for Unknown $(A,B)$", "weight": 1.0} -->

Here we assume that the system is completely unknown, and consider the problem of identifying system estimates $(\hat{A},\hat{B})$, bounding the corresponding parameter uncertainties $\epsilon_{A} = {\parallel{\hat{A} - A}\parallel}_{2}$ and $\epsilon_{B} = {\parallel{\hat{B} - B}\parallel}_{2}$, and using these system estimates and uncertainty bounds to compute a controller with provable performance bounds. In what follows, unless otherwise specified, all results are taken.

<!-- chunk {"id": "body-0090", "role": "body", "section": "V-A PAC Bounds for Unknown $(A,B)$", "weight": 1.0} -->

The system identification and uncertainty quantification steps are covered in Theorem IV.3 of, which we summarize here for the convenience of the reader.

<!-- chunk {"id": "body-0091", "role": "body", "section": "V-A PAC Bounds for Unknown $(A,B)$", "weight": 1.0} -->

Consider a linear dynamical system described by

<!-- chunk {"id": "body-0092", "role": "body", "section": "V-A PAC Bounds for Unknown $(A,B)$", "weight": 1.0} -->

Notice that we only use the last time-steps of each trajectory: we do so for analytic simplicity, and return to single trajectory estimators that use all data later in the section. We then have the following guarantees.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Remark V.7", "weight": 1.0} -->

Optimization problem (38 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again")) is infinite-dimensional. However, one can solve a finite-dimensional approximation of the problem over a horizon $T = \Omega{(\log{(1/{(\epsilon_{A} + \epsilon_{B})})}}$ (see Theorem 5.1, ) such that the sub-optimality bounds we prove below still hold up to universal constants.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Remark V.7", "weight": 1.0} -->

We then have the following theorem bounding the sub-optimality of the proposed robust LQR controller.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Example 5", "weight": 1.0} -->

In the left plot of Figure 1 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again"), we show the percentage of stabilizing controllers synthesized using certainty equivalence and the proposed robust LQR controllers over 100 independent trials.. Notice that even after collecting data from 100 trajectories, the CE controller yields unstable behavior in approximately 10% of cases. Given that the state of the underlying dynamical system is only 3-dimensional, one might consider 100 data-points to be a reasonable approximation of an "asymptotic" amount of data, highlighting the need for a more refined analysis of the effects of finite data on stability and performance. Contrast this with the behavior achieved by the robust LQR synthesis method, which explicitly accounts for system uncertainty: after a small number of trials, there is a sharp transition to 100% stability across trials. Further, feasibility of the synthesis problem (38 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again")) provides a certificate of stability and performance, conditioned on the uncertainty bounds being correct.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Example 5", "weight": 1.0} -->

However, robustness does come at a price: as shown in the right plot of Figure 1 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again"), the CE controller outperforms the robust LQR controller when it is stabilizing.

<!-- chunk {"id": "body-0097", "role": "body", "section": "V-B Regret Bounds under Moderate Uncertainty", "weight": 1.0} -->

We have just described an offline procedure for learning a coarse estimate of system dynamics and computing a robustly stabilizing controller. We now consider the task of adaptively refining this model and controller. For this problem, we seek high probability bounds on the regret $R{(T)}$, defined as

<!-- chunk {"id": "body-0098", "role": "body", "section": "V-B Regret Bounds under Moderate Uncertainty", "weight": 1.0} -->

for $J_{\star}$ defined as in the previous section.

<!-- chunk {"id": "body-0099", "role": "body", "section": "V-B Regret Bounds under Moderate Uncertainty", "weight": 1.0} -->

solved with data generated from system (23 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again")) driven by input $u_{t}\overset{\ \text{i.i.d.}}{\sim}{\mathcal{N}{(0,{\sigma_{u}^{2}I_{n_{u}}})}}$. The following result from Simchowitz et al. gives us a high probability bound on the error of the estimator.

<!-- chunk {"id": "body-0100", "role": "body", "section": "V-C Regret Bounds under Small Uncertainty", "weight": 1.0} -->

where the first equality holds for some $\gamma \in {}$ by the mean value form of the Taylor series expansion, and the second equality holds by recognizing that ${{\nabla J}{(K_{\star})}} = 0$ as it must be a stationary point of the cost functional $J$. This intuitive argument is formalized, wherein they explicitly quantify a bound on the error $\epsilon$ such that this approximation is valid.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Example 6", "weight": 1.0} -->

We consider the same dynamics (40 ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again")), but set $Q = {10I}$. In Figure 2 we show a comparison of different adaptive methods on 500 experiments. The median and 90th percentiles are shown for the optimal controller, the certainty equivalence controller, the robust LQR controller, and heuristic implementations of the Thompson Sampling (TS) method proposed in and the Optimism in the Face of Uncertainty (OFU) based method proposed. All methods achieve similar performance, and we note that the latter two methods assume that CE like control is guaranteed to be stabilizing, and further, that the OFU method requires solving a non-convex optimization problem as a subroutine.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Model-free Methods for LQR", "weight": 1.0} -->

We compare and contrast model-free methods from RL to the model-based methods of the previous section. We note that, while there is not a widely accepted technical definition of a model-free method, we informally a method to be model-free if it does not (as an intermediate step) estimate the transition dynamics $(A,B)$. Instead, the model-free methods we encounter either learn an alternative representation (such as a value function), or directly search for the optimal controller.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Approximate Policy Iteration", "weight": 1.0} -->

We start our discussion with a review of an important concept from RL known as the *state-action value function* or *$Q$-function.* Given a policy $\pi$, the (relative) state-action value function^44^4We change the quadratic state matrix in the cost to $S$ here as not to confuse it with the $Q$ function. is defined as

<!-- chunk {"id": "body-0104", "role": "body", "section": "Approximate Policy Iteration", "weight": 1.0} -->

*Policy iteration* (PI) is a classic algorithm from RL that works as follows. Fix a starting policy $\pi_{0}$. Then, iteratively repeat: Compute $Q_{t}$ as the state-value function for policy $\pi_{t}$, Update $\pi_{t + 1}$ as ${\pi_{t + 1}{(x)}} = {{\arg{\min_{u}Q_{t}}}{(x,u)}}$. Step of policy iteration generally requires knowledge of the transition dynamics. Of course, $Q^{\pi}$ for a given policy $\pi$ can be estimated from data. One such method, motivated by the Bellman equation, is based on temporal differences.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Approximate Policy Iteration", "weight": 1.0} -->

Here, $\phi_{t} = {\phi{(x_{t},u_{t})}}$, where ${\phi{(x,u)}} \in {\mathbb{R}}^{K}$ is a column vector of each basis function $\phi_{i}$ evaluated at the pair $(x,u)$. Furthermore, $\psi_{t} = {\phi{(x_{t},{\pi{(x_{t})}})}}$, $c_{t}$ is the instantaneous cost observed for the $t$-th state transition, and ${\hat{\lambda}}_{\pi}$ is an estimate of $\lambda_{\pi}$, the infinite-horizon average cost under the policy $\pi$. This estimator $\hat{w}$ is known as the *least-squares temporal difference* estimator for $Q$-functions (LSTD-Q).

<!-- chunk {"id": "body-0106", "role": "body", "section": "Approximate Policy Iteration", "weight": 1.0} -->

The LSTD-Q estimator is an *off-policy* estimator, meaning that the input $u_{t}$ applied to generate the data does *not* have to follow the policy $\pi$. This is one of the advantages of working with $Q$-functions (as opposed to value functions). We now can state our first model-free algorithm, the least-squares policy iteration (LSPI) algorithm of: Estimate ${\hat{Q}}_{t} \approx Q^{\pi_{t}}$ from data via LSTD-Q, Update $\pi_{t + 1}$ as ${\pi_{t + 1}{(x)}} = {{\arg{\min_{u}{\hat{Q}}_{t}}}{(x,u)}}$.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Derivative-free Search Methods", "weight": 1.0} -->

We now turn to methods which directly search for the optimal policy. Suppose we have a policy class $\Pi = {\{\pi_{\theta}:{\theta \in \Theta}\}}$ with $\Theta \subseteq {\mathbb{R}}^{p}$. We are interested in solving the following optimization problem: ${\min_{\theta \in \Theta}J}{(\theta)}$, where ${J{(\theta)}} = {J{(\pi_{\theta})}}$ is the infinite-horizon average cost performance of the policy $\pi_{\theta}$. In many problem formulations, the function $\theta\mapsto{J{(\theta)}}$ is differentiable on $\Theta$. Therefore, in principle one could run a local search method such as gradient descent: $\theta_{t + 1} = {\theta_{t} - {\eta{\nabla_{\theta}J}{(\theta_{t})}}}$.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Derivative-free Search Methods", "weight": 1.0} -->

However, typically computing ${\nabla_{\theta}J}{(\theta)}$ requires knowledge of the dynamics. To get around this, in many practical situations one can efficiently generate (unbiased estimates) of $J{(\theta)}$ for any $\theta$ via rollouts or simulation. Therefore, we can rely on a rich history of zero-th order optimization. Here, we will focus on two popular zero-th order methods in RL.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Policy Gradients (REINFORCE)", "weight": 1.0} -->

The policy gradient method was popularized, and forms the foundation of many popular algorithms such as TRPO and PPO. The idea is to perturb the action sequence and use these perturbations to estimate gradient information. Let ${J_{\eta}{(\theta)}} = {\lim_{T\rightarrow\infty}{{\mathbb{E}}{\lbrack{\frac{1}{T}{\sum_{t = 1}^{T}c_{t}}}\rbrack}}}$ where $u_{t} = {{\pi_{\theta}{(x_{t})}} + \eta_{t}}$ with $\eta_{t}\overset{\ \text{i.i.d.}}{\sim}{\mathcal{N}{(0,{\sigma^{2}I})}}$. Now under sufficient regularity conditions that allow us to switch the order of differentiation with the limit and the integral,

<!-- chunk {"id": "body-0110", "role": "body", "section": "Random Search", "weight": 1.0} -->

We now consider random finite differences. There are many different variants of finite differences; we present one of the simpler methods. The idea here is to perturb the parameter space. Like for policy gradients, we consider a surrogate function $J_{\xi}{(\theta)}$ defined as ${J_{\xi}{(\theta)}} = {{\mathbb{E}}_{\xi}{\lbrack{J{({\theta + {\sigma\xi}})}}\rbrack}}$, where $\xi \sim {\mathcal{N}{(0,I)}}$.

<!-- chunk {"id": "body-0111", "role": "body", "section": "VI-2 Experimental Evaluation", "weight": 1.0} -->

We compare the previously described model-free methods to the model-based nominal control (Section V-C) as a baseline.

<!-- chunk {"id": "body-0112", "role": "body", "section": "VI-2 Experimental Evaluation", "weight": 1.0} -->

We choose an LQR problem where the $A$ matrix is stable, since the model-free methods we consider require an initial stabilizing controller; using a stable $A$ allows us to start at $K_{0} = 0_{2 \times 3}$. We fix the process noise $\sigma_{w} = 1$. As before, the model-based method learns $(A,B)$ using least-squares, exciting the system with Gaussian noise of variance $\sigma_{u} = 1$.

<!-- chunk {"id": "body-0113", "role": "body", "section": "VI-2 Experimental Evaluation", "weight": 1.0} -->

For policy gradients and derivative-free optimization, we use the projected stochastic gradient descent (SGD) method with a constant step size $\mu$ as the optimization procedure. The details of how we tuned each procedure are described. For policy gradients we considered two different baselines. The *simple baseline* is the one that uses the empirical average cost $\frac{1}{T}{\sum_{t = 1}^{T}c_{t}}$ of the previous iteration as the baseline. The *value function* baseline uses ${b{(x_{t})}} = {x_{t}^{\top}Vx_{t}}$ where $V = {{\mathsf{d}\mathsf{l}\mathsf{y}\mathsf{a}\mathsf{p}}{({A + {BK}},{S + {K^{\top}RK}})}}$. Computing this $V$ requires knowledge of the model $(A,B)$: a practical implementation would need to also estimate $V$, further degrading performance.

<!-- chunk {"id": "body-0114", "role": "body", "section": "VI-3 Separation Results", "weight": 1.0} -->

In the last section we saw that the model-based nominal method substantially outperformed the model-free methods we considered in our experiment. Can we make this rigorous? Here, we outline some results towards this, based. For these results, we consider a finite length $T$ horizon LQR problem with no input penalty: ${\min_{u_{t}}{\mathbb{E}}}{\lbrack{\sum_{t = 1}^{T}{\parallel x_{t}\parallel}^{2}}\rbrack}$. We also only consider dynamics which have the special property that ${{range}{(A)}} \subseteq {{range}{(B)}}$ and $B$ has full column rank. These assumptions imply that the optimal solution is simply to cancel the state: $u_{t} = {- {B^{\dagger}Ax_{t}}}$. It means that the optimal solution on a finite horizon is time-invariant, which is typically not the case.

<!-- chunk {"id": "body-0115", "role": "body", "section": "VI-3 Separation Results", "weight": 1.0} -->

We first consider the risk of the model-based method. The following theorem characterizes the performance of the nominal method as the number of rollouts $N$ tends to infinity. It is an asymptotic version of Theorem V.11 ‣ V-C Regret Bounds under Small Uncertainty ‣ V Model-Based Methods for LQR ‣ From self-tuning regulators to reinforcement learning and back again")

<!-- chunk {"id": "body-0116", "role": "body", "section": "Conclusions", "weight": 1.0} -->

This tutorial paper and our companion paper presented a broad overview of recent progress towards the finite-time analysis for reinforcement learning and self-tuning control methods. We have attempted to provide a summary of representative results in this space that establish connections between the self-tuning control literature and methods recently proposed in reinforcement learning. The former are typically model-based, and are well-studied from a theoretical perspective, although more effort is still needed to better understand their finite-time behavior. The latter mostly adopt a model-free approach; they have had spectacular successes over the last few years, but lack strong theoretical guarantees, although researchers have been trying to validate design choices and algorithms a posteriori. Empirically, there is rich evidence that learning algorithms exploiting prior knowledge about the system (such as a model parameterization) are more sample-efficient, but are also more sensitive to biases introduced by modeling errors. Further, as we showed in Section VI, there exists scenarios where there is a quantitative and provable gap between model-based and model-free methods. A broader assessment of the advantages and drawbacks of modeling choices are however difficult to assess theoretically.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Conclusions", "weight": 1.0} -->

This survey summarized recent progress towards this goal within the limited scope of tabular MDPs and linear optimal control, but we critically need to develop more broadly applicable tools towards the tighter analysis of learning algorithms.
