<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Bounded Ratio Reinforcement Learning

Topics include Reinforcement learning, Stability analysis, Robustness, Scalability, Optimization, Learning, BPO, Bounded ratio, Proximal policy optimization, BRRL, CEM, GBPO, Group-relative.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Proximal Policy Optimization (PPO) has become the predominant algorithm for on-policy reinforcement learning due to its scalability and empirical robustness across domains. However, there is a significant disconnect between the underlying foundations of trust region methods and the heuristic clipped objective used in PPO. In this paper, we bridge this gap by introducing the Bounded Ratio Reinforcement Learning (BRRL) framework. We formulate a novel regularized and constrained policy optimization problem and derive its analytical optimal solution. We prove that this solution ensures monotonic performance improvement. To handle parameterized policy classes, we develop a policy optimization algorithm called Bounded Policy Optimization (BPO) that minimizes an advantage-weighted divergence between the policy and the analytic optimal solution from BRRL. We further establish a lower bound on the expected performance of the resulting policy in terms of the BPO loss function. Notably, our framework also provides a new theoretical lens to interpret the success of the PPO loss, and connects trust region policy optimization and the Cross-Entropy Method (CEM). We additionally extend BPO to Group-relative BPO (GBPO) for LLM fine-tuning.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Empirical evaluations of BPO across MuJoCo, Atari, and complex IsaacLab environments (e.g., Humanoid locomotion), and of GBPO for LLM fine-tuning tasks, demonstrate that BPO and GBPO generally match or outperform PPO and GRPO in stability and final performance.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Deep reinforcement learning (DRL) has achieved breakthroughs across diverse domains silver2017mastering; lee2020learning; ouyang2022training; radosavovic2024real. Among DRL methods, Proximal Policy Optimization (PPO) schulman2017proximal remains one of the most widely adopted algorithms. The core design of PPO is motivated by Trust Region Policy Optimization (TRPO, schulman2015trust ), which constrains policy updates within a "trust region" to ensure stable iterations. By utilizing a first-order approximation of the TRPO objective, PPO achieves the scalability necessary for training modern large-scale models. As a result, PPO and its variant GRPO are now widely applied to tasks ranging from robotics to large language model (LLM) fine-tuning miki2022learning; andrychowicz2020learning; shao2024deepseekmath.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite its empirical success, PPO remains largely heuristic: its clipped objective is not directly derived from the trust-region formulation it was intended to approximate. Instead, the design of the PPO objective was primarily driven by experimentation schulman2017proximal; engstrom2020implementation. Furthermore, most existing theoretical analyses of PPO's performance improvement rely on the original TRPO or policy gradient formulation schulman2015trust; liu2019neural; doering2026approximate, none of which fully capture the nuances of the first-order loss used in practice.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Numerous variants have been recently proposed to improve PPO. Some works focus primarily on algorithm design and report empirical performance gains without formal theoretical contributions cobbe2021phasic; ye2020mastering; tan2024beyond; fakoor2020p3o; kobayashi2021proximal. Other works extend PPO to specific domains (e.g., safe RL, non-stationary RL) without modifying the core PPO loss function akgul2025overcoming; milosevic2025central. There are also PPO variants aiming at improving the PPO loss from a theoretical lens xie2024simple; wang2020truly; wang2019trust; qi2026rethinking. However, similar to PPO, they also utilize TRPO theory without introducing novel theoretical frameworks or establishing superior performance guarantees. Consequently, there remains a substantial gap between the theoretical foundations and the practical policy optimization algorithms.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address this gap, we introduce the bounded ratio reinforcement learning (BRRL) framework. Instead of constraining policy updates through KL divergence kullback1951information bounds as in TRPO, BRRL imposes bounded ratio constraints on the policy likelihood ratios. This formulation admits an analytic optimal policy, which reveals a simple structure for policy updates.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We derive the optimal solution of BRRL and prove its monotonic performance improvement guarantees. We also demonstrate that optimizing the PPO loss approximately pushes the policy towards this analytic optimal solution.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We establish a connection between BRRL and the Cross-Entropy Method (CEM).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose Bounded Policy Optimization (BPO), which optimizes an advantage-weighted divergence from the BRRL solution. We also extend BPO to Group-Relative BPO (GBPO), mirroring the extension from PPO to GRPO.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We provide a performance improvement guarantee for the policy attained by BPO in terms of the loss that BPO optimizes.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate strong empirical performance of BPO on MuJoCo, Atari, IsaacLab locomotion tasks, and of GBPO for LLM fine-tuning.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Overall, BRRL provides a principled perspective on PPO-style algorithms, suggesting that their empirical success arises from approximating an analytically optimal bounded-ratio update. By more directly approximating this analytically optimal bounded-ratio update, BPO achieves improved empirical performance (Figure˜1).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Overview of Contributions", "weight": 1.0} -->

In this section, we present an overview of the contributions within this work, as shown in Figure 2.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Overview of Contributions", "weight": 1.0} -->

Bounded ratio RL framework: We consider a policy optimization problem with bounded ratio trust region constraints from an old policy $\pi_{0}$, instead of the KL-divergence constraint of TRPO, as shown in Figure 2 (Middle Left). Specifically, with $L_{\pi_{0}}{(\pi)}$ defined, the problem is expressed as

<!-- chunk {"id": "body-0016", "role": "body", "section": "Overview of Contributions", "weight": 1.0} -->

which also has an implicit normalization constraint ${\sum_{a}{\pi{(\left. a \middle| s \right.)}}} = {1,{\forall s}}$. Notably, this problem has an *analytical* optimal solution $\pi^{\ast}$, which in many cases (as detailed in Remark 4.3). ‣ 4.1 Bounded Ratio RL Framework ‣ 4 Method ‣ Bounded Ratio Reinforcement Learning")) can be derived as

<!-- chunk {"id": "body-0017", "role": "body", "section": "Overview of Contributions", "weight": 1.0} -->

As shown in Figure 2 (Middle Right) and Figure 3 (c), this optimal solution can be explained as: if $Q_{\pi_{0}}{(s,a)}$ is higher than the threshold $\mu_{\pi_{0}}{(s)}$, then take the highest probability within the constraint ${\pi^{\ast}{(\left. a \middle| s \right.)}} = {{({1 + \epsilon})}\pi_{0}{(\left. a \middle| s \right.)}}$; otherwise, let ${\pi^{\ast}{(\left. a \middle| s \right.)}} = {{({1 - \epsilon})}\pi_{0}{(\left. a \middle| s \right.)}}$. Threshold $\mu_{\pi_{0}}{(s)}$ is selected as the median, s.t.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Overview of Contributions", "weight": 1.0} -->

$\pi^{\ast}$ is a normalized probability distribution (${\sum_{a}{\pi^{\ast}{(\left. a \middle| s \right.)}}} = 1$). A formal theorem on the optimal solution for general cases is provided in Theorem 4.1. ‣ 4.1 Bounded Ratio RL Framework ‣ 4 Method ‣ Bounded Ratio Reinforcement Learning"). Note that Theorem 4.1. ‣ 4.1 Bounded Ratio RL Framework ‣ 4 Method ‣ Bounded Ratio Reinforcement Learning") can also be extended to problems with asymmetric bounded ratio constraints ($c_{l} \leq {{{\pi{(\left. a \middle| s \right.)}}/\pi_{0}}{(\left. a \middle| s \right.)}} \leq c_{h}$). This asymmetric solution is used to draw a connection to the cross-entropy method (CEM, rubinstein1999cross ) in Section 4.6.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Overview of Contributions", "weight": 1.0} -->

Monotonic performance guarantee: For the cases where optimal policy $\pi^{\ast}$ from is realizable, it can be shown to have improved performance over $\pi_{0}$

<!-- chunk {"id": "body-0020", "role": "body", "section": "Overview of Contributions", "weight": 1.0} -->

where the second term is non-negative and is positive whenever $\pi_{0}$ induces non-zero median advantage. For a fixed $\pi_{0}$, we denote this constant improvement term as $\epsilonB$. A performance bound for general cases is provided in Theorem 4.2. ‣ 4.1 Bounded Ratio RL Framework ‣ 4 Method ‣ Bounded Ratio Reinforcement Learning"). Though $\pi^{\ast}$ is simple to express and provides improvement guarantees, it may not lie in the admissible policy class $\Pi$ (Figure 2 Middle right). This motivates the design of policy optimization algorithms to minimize divergence between the policy $\pi \in \Pi$ and $\pi^{\ast}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Overview of Contributions", "weight": 1.0} -->

Revisiting the PPO loss function: We observe that the PPO loss function approximately drives the policy towards $\pi^{\ast}$. Specifically, as shown in Figure 3 (a-b), optimizing the PPO objective schulman2017proximal is equivalent to minimizing the expectation of the following loss function evaluated at $\rho = {{{\pi{(\left. a \middle| s \right.)}}/\pi_{0}}{(\left. a \middle| s \right.)}}$

<!-- chunk {"id": "body-0022", "role": "body", "section": "Overview of Contributions", "weight": 1.0} -->

A formal theorem on this equivalence with step-by-step proof is detailed in Section 4.4 and Appendix A.6. At the beginning of the iteration, the ratio always starts from 1, and the PPO loss minimizes an *advantage-weighted absolute error* between the ratio $\rho$ and the target $1 + {\epsilon\text{sign}{(A_{\pi_{0}})}}$, then it applies zero-gradient after reaching the target. Note that this target ratio closely matches the solution, except that PPO uses the mean advantage $A_{\pi_{0}}$, and the BRRL solution is expressed in terms of the median advantage ${\overset{\sim}{A}}_{\pi_{0}}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Overview of Contributions", "weight": 1.0} -->

Bounded Policy Optimization (BPO): Building on the solution, we introduce a natural PPO variant with the loss function $l^{BPO}$ to directly minimize the *advantage weighted total variation* from the optimal solution. For the solution, the loss $l^{BPO}$ evaluated under $\rho = {{{\pi{(\left. a \middle| s \right.)}}/\pi_{0}}{(\left. a \middle| s \right.)}}$ is

<!-- chunk {"id": "body-0024", "role": "body", "section": "Overview of Contributions", "weight": 1.0} -->

The loss is illustrated in Figure 3 (d). Compared with the PPO loss, this loss function $l^{BPO}$ only differs in two ways: a symmetric slope also for ${{\lbrack{\rho - {({1 + {{\epsilon \cdot \text{sign}}{(A_{\pi_{0}})}}})}}\rbrack} \cdot A_{\pi_{0}}} > 0$ and using ${\overset{\sim}{A}}_{\pi_{0}}$ instead of $A_{\pi_{0}}$. In practice, this also requires learning an additional median value function alongside the mean value function, though the median can be approximated by the mean to reduce computational overhead. Notably, with this refined loss function, BPO has both *theoretical performance guarantees* (discussed below) and strong empirical performance, as demonstrated in Section 5. The same loss function can also be adapted for LLM fine-tuning, analogous to how PPO was adapted to GRPO (Section 4.5).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Overview of Contributions", "weight": 1.0} -->

BPO performance guarantees: Assuming the optimal solution in is valid, we can express the stepwise improvement in terms of the achieved loss. Specifically, we show that

<!-- chunk {"id": "body-0026", "role": "body", "section": "Overview of Contributions", "weight": 1.0} -->

where $B$ is defined. Here, $\delta{(\pi,\pi^{\ast})}$ is an error term that is related to $l^{BPO}{(\frac{\pi{(\left. a \middle| s \right.)}}{\pi_{0}{(\left. a \middle| s \right.)}})}$ and reduces to $0$ if we have perfect policy approximation $\pi = \pi^{\ast}$. This theoretical result directly implies that, if our loss function $l^{BPO}$ is sufficiently minimized over states and actions sampled from $\pi_{0}$, and if the policy approximation error is small, we can obtain monotonic performance improvement. The formal result is detailed in Corollary 4.5. ‣ 4.2 Alternative Perspective: Minimizing Divergence from Optimal Policy ‣ 4 Method ‣ Bounded Ratio Reinforcement Learning").

<!-- chunk {"id": "body-0027", "role": "body", "section": "Method", "weight": 1.0} -->

We now proceed to present the aforementioned framework of BRRL and its extensions.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Bounded Ratio RL Framework", "weight": 1.0} -->

Intuitively, for an MDP with finite state and action spaces, Problem is a linear programming problem. Specifically, for a fixed state $s$, the optimization variable $\pi{(\left. a \middle| s \right.)}$ is a finite-dimensional vector. Consequently, the objective function and constraints in Problem are linear in $\pi{(\left. a \middle| s \right.)}$. However, for general state and action spaces, the optimal solution of this linear programming problem is difficult to specify analytically. Nevertheless, an additional *regularizer* allows for the derivation of the general analytical solution.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Bounded Ratio RL Framework", "weight": 1.0} -->

Here the regularizer ${H{(\rho)}} \in {\lbrack{2\epsilon{\log\epsilon}},{2\epsilon{\log{({2\epsilon})}}}\rbrack}$ decreases as $\rho\rightarrow 1$ and increases as $\rho\rightarrow{1 \pm \epsilon}$. Moreover, its gradient becomes unbounded near the boundaries $1 \pm \epsilon$, so $H$ provides log barriers for the original bounded ratio constraints ${1 - \epsilon} < \frac{\pi{(\left. a \middle| s \right.)}}{\pi_{0}{(\left. a \middle| s \right.)}} < {1 + \epsilon}$. The regularizer is weighted by $\lambda$. According to Fermi-Dirac statistics landau1980statistical, Problem has a closed-form solution, detailed in the following theorem.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 4.3 (Optimal solution to unregularized Problem )", "weight": 1.0} -->

Note that by taking $\lambda\rightarrow 0$ in Theorem 4.1. ‣ 4.1 Bounded Ratio RL Framework ‣ 4 Method ‣ Bounded Ratio Reinforcement Learning") and Theorem 4.2. ‣ 4.1 Bounded Ratio RL Framework ‣ 4 Method ‣ Bounded Ratio Reinforcement Learning"), one can obtain the optimal ratio and monotonic guarantees for the unregularized Problem. In many cases, one can simplify the resulting optimal policy as ${\pi^{\ast}{(\left. a \middle| s \right.)}} = {{\lbrack{1 + {\epsilon\text{sign}{({\overset{\sim}{A}}_{\pi_{0}})}}}\rbrack}\pi_{0}{(\left.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 4.3 (Optimal solution to unregularized Problem )", "weight": 1.0} -->

Otherwise, the simplified $\pi^{\ast}$ can never be normalized. One valid case is a uniform density $\pi_{0}{( \cdot |s)}$ with continuous $\mathcal{A}$ and a $Q$-function $Q_{\pi_{0}}{(s,a)}$ which is smooth over $a$. However, there are also counterexamples.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 4.3 (Optimal solution to unregularized Problem )", "weight": 1.0} -->

‣ 4.1 Bounded Ratio RL Framework ‣ 4 Method ‣ Bounded Ratio Reinforcement Learning") still holds for arbitrarily small $\lambda > 0$ and general spaces (see Appendix A.2).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Alternative Perspective: Minimizing Divergence from Optimal Policy", "weight": 1.0} -->

In this section, we consider the policy optimization problem as minimizing the divergence to the optimal solution, instead of directly applying policy gradient methods. Specifically, given the optimal policy obtained from Theorem˜4.1. ‣ 4.1 Bounded Ratio RL Framework ‣ 4 Method ‣ Bounded Ratio Reinforcement Learning"), we can formulate policy optimization as

<!-- chunk {"id": "body-0034", "role": "body", "section": "Alternative Perspective: Minimizing Divergence from Optimal Policy", "weight": 1.0} -->

where $\pi_{\theta}$ is the parameterized policy, $D$ is a divergence function such as the KL-divergence, total variation (TV), etc. Specifically, the TV (without $\frac{1}{2}$ multiplier) for each state can be expressed as

<!-- chunk {"id": "body-0035", "role": "body", "section": "Alternative Perspective: Minimizing Divergence from Optimal Policy", "weight": 1.0} -->

We also consider an advantage-weighted TV (ATV) loss function defined as

<!-- chunk {"id": "body-0036", "role": "body", "section": "Alternative Perspective: Minimizing Divergence from Optimal Policy", "weight": 1.0} -->

Notably, this divergence is directly correlated with the performance improvement of the parameterized policy $\pi_{\theta}$, as detailed in the following Corollary.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Bounded Policy Optimization", "weight": 1.0} -->

In this section, we present the practical implementation of our algorithm. As in PPO, we use a value network $V_{\phi}$ to estimate $A_{\pi_{0}}$. Specifically, we estimate the return value $R_{\phi}{(s,a)}$ using generalized advantage estimation schulman2015high, and use it to update the value function by minimizing

<!-- chunk {"id": "body-0038", "role": "body", "section": "Bounded Policy Optimization", "weight": 1.0} -->

where $sg$ denotes stop gradient. In addition, following Theorem 4.1. ‣ 4.1 Bounded Ratio RL Framework ‣ 4 Method ‣ Bounded Ratio Reinforcement Learning"), we further train a network $\mu_{\psi}$ to minimize the normalization loss

<!-- chunk {"id": "body-0039", "role": "body", "section": "Bounded Policy Optimization", "weight": 1.0} -->

with $g$ defined in Theorem 4.1. ‣ 4.1 Bounded Ratio RL Framework ‣ 4 Method ‣ Bounded Ratio Reinforcement Learning"). For numerical stability, we use the equivalent representation ${g{(x)}} = {{- \frac{x}{2}} + {\text{softplus}{(x)}}}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Bounded Policy Optimization", "weight": 1.0} -->

where ${\hat{A}}_{\pi_{0}}:={sg{({{R_{\phi}{(s,a)}} - {\mu_{\psi}{(s)}}})}}$. Note that ${\hat{J}}^{P}{(\theta)}$ is not exactly $J^{P}$, but the gap can be controlled by minimizing the estimation error of $V_{\phi}$ and $\mu_{\psi}$. Our final bounded policy optimization algorithm follows a PPO-style training procedure, summarized in Algorithm 1.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Bounded Policy Optimization", "weight": 1.0} -->

1: Initialize πθ, Vϕ, μψ, choose a sufficiently small λ
4: Run π0 for N steps, and collect the dataset 𝒟:= {sj, aj, Rj, π0 (aj|sj)}j = 1N.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Bounded Policy Optimization", "weight": 1.0} -->

where ĴP, JV F, JM F are defined in and evaluated from 𝒟.
Algorithm 1 Bounded policy optimization (BPO)

<!-- chunk {"id": "body-0043", "role": "body", "section": "Revisiting the PPO Objective", "weight": 1.0} -->

In this section, we connect our theory and algorithmic framework to PPO schulman2017proximal. In PPO, the following surrogate objective function is introduced

<!-- chunk {"id": "body-0044", "role": "body", "section": "Revisiting the PPO Objective", "weight": 1.0} -->

We observe a strong correlation between the BPO loss function and the PPO loss function. To show this correlation, we first introduce an equivalent form of the PPO loss in the following proposition.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Extension to LLM Fine-Tuning", "weight": 1.0} -->

In the context of LLM fine-tuning, training an additional critic can be computationally expensive. This challenge motivates the design of Group Relative Policy Optimization (GRPO) shao2024deepseekmath, which estimates advantages relative to a group of concurrent samples rather than utilizing an auxiliary value network. Building on this idea, we introduce Group-relative Bounded Policy Optimization (GBPO), an extension of BPO derived from Theorem 4.1. ‣ 4.1 Bounded Ratio RL Framework ‣ 4 Method ‣ Bounded Ratio Reinforcement Learning"). Specifically, for a given prompt $q$, the model generates a group of sampled outcomes $\{ o_{1},o_{2},\ldots,o_{G}\}$. A reward model then assigns a score to each output, denoted by $\mathbf{R} = {\{ r_{1},r_{2},\ldots,r_{G}\}}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Extension to LLM Fine-Tuning", "weight": 1.0} -->

As in standard GRPO, we estimate advantages using z-scores $A_{i}:=\frac{r_{i} - {\text{mean}{(\mathbf{R})}}}{\text{std}{(\mathbf{R})}}$. As noted in Remark 4.3). ‣ 4.1 Bounded Ratio RL Framework ‣ 4 Method ‣ Bounded Ratio Reinforcement Learning"), when the regularization parameter $\lambda$ is small, the implicit baseline $\mu_{\pi_{0}}{(q)}$ converges to the median of the Q-values. We therefore also estimate the median-advantage as ${\overset{\sim}{A}}_{i}:=\frac{r_{i} - {\text{median}{(\mathbf{R})}}}{\text{std}{(\mathbf{R})}}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Extension to LLM Fine-Tuning", "weight": 1.0} -->

where $t$ denotes the token index, and $\mathcal{Q}$ is the question set. In scenarios where a reward is only provided at the end of the sequence, the step-dependent advantages $A_{i,t}$ and ${\overset{\sim}{A}}_{i,t}$ are equal to the sequence-level $A_{i}$ and ${\overset{\sim}{A}}_{i}$, respectively. If per-step scores are available, these advantages can be estimated token-wise following the approach in shao2024deepseekmath.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Asymmetric Ratio Constraints and Cross Entropy Method", "weight": 1.0} -->

In this section, we generalize Theorem 4.1. ‣ 4.1 Bounded Ratio RL Framework ‣ 4 Method ‣ Bounded Ratio Reinforcement Learning") to asymmetric ratio constraints. Similar to, we consider the regularized problem with general ratio boundaries ${{\forall s},a,c_{l}} \leq \frac{\pi{(\left. a \middle| s \right.)}}{\pi_{0}{(\left. a \middle| s \right.)}} \leq c_{h}$, with $c_{l} < 1 < c_{h}$

<!-- chunk {"id": "body-0049", "role": "body", "section": "Asymmetric Ratio Constraints and Cross Entropy Method", "weight": 1.0} -->

Here, the regularizer $H^{\prime}$ still takes its minimum at $\rho = 1$, and provides log barriers for the asymmetric constraints $c_{l} \leq \rho \leq c_{h}$. The optimal solution is detailed in the following Corollary.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we present extensive experiments to validate the proposed BPO algorithm. We first benchmark its performance against PPO across standard MuJoCo and Atari environments (Section 5.1). To assess scalability, we evaluate BPO within NVIDIA IsaacLab mittal2025isaac, a high-throughput simulation platform capable of simulating *thousands of* parallel environments for real-world robotic policy training. Furthermore, we apply our GBPO variant to LLM fine-tuning tasks, and compare it directly against GRPO (Section 5.3). Then, we dive deeper into the analysis of the ratio statistics during training, connecting it to the performance gap between BPO and PPO. Finally, we conduct an ablation study to analyze the sensitivity of training performance to key components, including the loss function, the $\lambda$ parameter, and various loss coefficients. All hyperparameters are detailed in Appendix A.9

<!-- chunk {"id": "body-0051", "role": "body", "section": "Benchmarking with Classical Environments", "weight": 1.0} -->

We compare the performance of BPO and PPO in classical environments. For these experiments, BPO was implemented within the Stable Baselines3 framework, with hyperparameters for all baseline algorithms sourced from RL-Zoo rl-zoo3. As shown in Figure 4, BPO performs competitively with or superior to PPO across a range of classical benchmarks. Specifically, in MuJoCo tasks, BPO achieves clear performance gains in the Ant-v4, Hopper-v4, and Humanoid-v4 environments. Training on Humanoid-v4 exhibits high variance for BPO, characterized by significant performance divergence across random seeds. Both PPO and BPO struggle to achieve peak performance in this environment, primarily due to limited sample efficiency. However, as demonstrated in Section 5.2, both methods successfully solve more complex humanoid tasks when provided with sufficient samples. In Atari benchmarks, BPO generally matches PPO's performance, notably outperforming it in the Asterix environment.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Benchmarking with Classical Environments", "weight": 1.0} -->

We report our benchmarking results against off-policy baselines in MuJoCo and Atari environments in Table 1. While SAC haarnoja2018soft outperforms both PPO and BPO in the Ant-v4 and Humanoid-v4 tasks, it fails to achieve competitive results in Swimmer-v4. In contrast, BPO consistently outperforms PPO in the Ant-v4, Humanoid-v4, and Hopper-v4 environments while remaining competitive in Swimmer-v4. Both BPO and PPO consistently outperform DQN mnih2013playing in Atari benchmarks.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Benchmarking with IsaacLab Environments", "weight": 1.0} -->

In this section, we evaluate the scalability and performance of BPO relative to PPO within the IsaacLab simulation platform. We focus on four challenging locomotion tasks on rough terrain: Go1-rough, Anymal-C-rough, G1-rough, and H1-rough, which require the agents (quadrupeds like Unitree Go1 and Anymal-C or humanoids like Unitree G1 and H1) to maintain stable gaits while tracking target velocities across rough surfaces. Both BPO and PPO were implemented using the RSL-RL framework, utilizing a large-scale parallelization of 4,096 environments per task.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Benchmarking with IsaacLab Environments", "weight": 1.0} -->

The results in Figure 5 demonstrate that BPO is highly effective in complex robotic locomotion tasks. In particular, on G1-rough, BPO significantly outperforms the baseline to reach a higher performance ceiling. For the Go1-rough and H1-rough environment, BPO also slightly exceeds the final performance of PPO. Notably, across all four benchmarks, BPO exhibits enhanced training stability and smoother dynamics compared to the PPO baseline.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Fine-Tuning with GBPO", "weight": 1.0} -->

We further evaluate GBPO against GRPO for large language model fine-tuning (Section 4.5). Specifically, we conduct experiments in the Test-Time Reinforcement Learning (TTRL, zuo2025ttrl ) framework, fine-tuning the Qwen2.5-Math-1.5B model with GBPO and GRPO on the AIME-TTT and AMC-TTT benchmarks, and then compare their reasoning performance. The empirical results, illustrated in Figure 6, reveal that GBPO can maintain performance gains as the number of training epochs and clip ratio increase. Conversely, GRPO exhibits instability under these conditions. These findings highlight GBPO's potential as a more robust and stable alternative for the fine-tuning of large-scale models.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Ratio Statistics Analysis", "weight": 1.0} -->

We analyze the statistics of importance weights (ratio ${{\pi{(\left. a \middle| s \right.)}}/\pi_{0}}{(\left. a \middle| s \right.)}$) during the training process. In MuJoCo environments (using the stable-baselines3 implementation), BPO maintains more stable ratio distributions than PPO, as illustrated in Figure 7. This difference in stability is more obvious in environments where BPO outperforms PPO (e.g., Hopper and Asterix).

<!-- chunk {"id": "body-0057", "role": "body", "section": "Ratio Statistics Analysis", "weight": 1.0} -->

In IsaacLab environments (utilizing RSL-RL), learning rates are dynamically adjusted to maintain a target KL divergence. As shown in Figure 8, the adapted learning rates for PPO are often lower than those for BPO, suggesting more aggressive ratio updates that surpass the target KL divergence more frequently. The scales of the learning rates differ more in tasks where BPO shows a clear performance improvement (e.g., G1-rough). These findings suggest a strong correlation between the stability of ratio distributions and overall algorithmic performance. By effectively enforcing this stability, BPO allows for more stable performance improvement.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

This section presents an ablation study of the impact of the value function, loss function, $\lambda$, and the coefficient of TV loss on the performance of the policy, within the G1-rough environment.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Mean vs median value function. We evaluate the performance of the algorithm by substituting median advantages ${\overset{\sim}{A}}_{\pi_{0}}$ with the mean advantage $A_{\pi_{0}}$. As illustrated in the left panel of Figure 9, this simplification achieves performance comparable to the original BPO. This robustness likely stems from the low practical differences between median and mean values, caused by the specific return distribution and inherent value estimation errors. These results also suggest that this median-to-mean value simplification offers a compelling alternative when the computational overhead of learning the median value is high.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Divergence function ablation. As illustrated in the middle-left panel of Figure 9, the ATV loss yields superior performance in the G1-rough environment. While the standard TV loss facilitates some learning, it fails to match the asymptotic performance of ATV. Conversely, KL divergence proves ineffective and fails to achieve successful policy convergence.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Sensitivity to $\lambda$. We conduct a hyperparameter sweep for $\lambda$ in the G1-rough environment. As shown in the middle-right panel of Figure 9, smaller values of $\lambda$ generally lead to strong performance. Specifically, increasing $\lambda$ from $10^{- 3}$ to $10^{- 2}$ may slightly improve asymptotic performance, but at the cost of a reduced convergence rate. Conversely, excessively large values of $\lambda$ prevent the learning process entirely.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Ablation Study", "weight": 1.0} -->

Impact of TV loss regularization. We study the effect of the TV loss coefficient by incrementally increasing its weight relative to the ATV loss in the G1-rough environment. Although Corollary 4.5. ‣ 4.2 Alternative Perspective: Minimizing Divergence from Optimal Policy ‣ 4 Method ‣ Bounded Ratio Reinforcement Learning") suggests that both terms contribute to performance gains, the results in the right panel of Figure 9 indicate that explicitly adding a TV loss component does not improve performance in practice.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We introduced Bounded Ratio Reinforcement Learning (BRRL), a framework for policy optimization under bounded ratio constraints. We showed that the underlying optimization problem admits an analytic solution. Our main finding is that this optimal solution allows interpreting the PPO loss from a new perspective, connects to the cross-entropy method (CEM), and motivates a *theoretically grounded* variant, Bounded Policy Optimization (BPO). Empirically, BPO is consistently effective across a broad range of tasks, including robotic control and large-model fine-tuning. Despite the extensive evaluation with standard RL benchmarks, extending the experiments towards a broader range of LLM fine-tuning tasks remains a compelling future direction. Other future research directions include enhancing sample efficiency via advanced exploration, extending the framework to constrained MDPs, and adapting the algorithm for fine-tuning generative policies.
