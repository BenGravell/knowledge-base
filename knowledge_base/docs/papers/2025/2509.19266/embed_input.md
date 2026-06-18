<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Policy Gradient Bounds in Multitask LQR

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We analyze the performance of policy gradient in multitask linear quadratic regulation (LQR), where the system and cost parameters differ across tasks. The main goal of multitask LQR is to find a controller with satisfactory performance on every task. Prior analyses on relevant contexts fail to capture closed-loop task similarities, resulting in conservative performance guarantees. To account for such similarities, we propose bisimulation-based measures of task heterogeneity. Our measures employ new bisimulation functions to bound the cost gradient distance between a pair of tasks in closed loop with a common stabilizing controller. Employing these measures, we derive suboptimality bounds for both the multitask optimal controller and the asymptotic policy gradient controller with respect to each of the tasks. We further provide conditions under which the policy gradient iterates remain stabilizing for every system. For multiple random sets of certain tasks, we observe that our bisimulation-based measures improve upon baseline measures of task heterogeneity dramatically.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Designing a control policy that performs effectively on tasks with heterogeneous dynamics and objectives is a central problem in multitask reinforcement learning.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

over a parameter class containing $K_{\star}$. A popular method for approximating $J_{\text{avg}}{(K_{\star})}$ is provided by policy gradient, with applications ranging from autonomous driving to robotic control. Despite the empirical success of policy gradient, its theoretical guarantees remain relatively unexplored.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we analyze the performance of vanilla policy gradient in multitask linear quadratic regulation (LQR) with respect to each task. Our setting involves LQR tasks with heterogeneous system and cost parameters. In this setting, closed-loop stability may not necessarily be preserved for every system across policy gradient iterations. Our analysis relies on closed-loop measures of task heterogeneity, inspired by classical bisimulation functions. Bisimulation functions, as introduced, are Lyapunov-like functions that provide a principled method for characterizing the output distance of stable systems with vector states.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We define a novel notion of bisimulation functions tailored to Lyapunov matrix systems, and provide a systematic design of them via linear matrix inequalities.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Employing these functions, we introduce bisimulation-based measures that bound the cost gradient discrepancy between two LQR tasks under a common stabilizing controller. Our result establishes the first closed-loop measure of task heterogeneity for this purpose.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Employing these measures, we provide suboptimality bounds for the multitask optimal controller $K_{\star}$ and the asymptotic policy gradient controller with respect to each task. These bounds depend on the average bisimulation-based measure between the task of interest and the others, evaluated at the respective controller.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We identify conditions such that the policy gradient iterates remain stabilizing for all systems.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We apply multitask policy gradient LQR across two sets of tasks: one with inverted pendula and another with unicycles. We observe that our bisimulation-based measures can be informative of the multitask policy gradient controller's performance in cases where previous measures from are vacuous. For multiple random sets of these tasks, our measures dramatically improve upon baselines, effectively mitigating their conservatism. Complete proofs of our results are given in Appendix A. The related work is summarized below.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Policy Gradient Methods. Recent work has studied variants of our setting with different policy gradient methods. The authors of consider the special case where the cost parameters are the same for all tasks. A related line of work focuses on meta-learning LQR, which includes additional fine-tuning to each task-specific cost and presents meta-LQR design with heterogeneous systems and objectives. Closest to our setting is the work, which proposes an asynchronous policy gradient approach for multitask LQR under diverse system and cost parameters.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The analyses in both and provide suboptimality bounds for policy gradient methods based on a measure of the heterogeneity between different tasks. Their measure bounds the norm of the cost gradient difference between the tasks via the maximum norm distance between the task parameters. The derivation of their measure overlooks potential closed-loop task similarities, thus often leading to overly conservative suboptimality bounds. In contrast, our bisimulation-based measures provide a principled *closed-loop* notion of task heterogeneity, resulting in more informative performance bounds.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Bisimulations for Reinforcement Learning and Control. Behavioral similarity has been central in both robust control (e.g., gap metric ) and layered control design (e.g., bisimulation relations and functions ). Approximate bisimulation, in particular, employs Lyapunov-like functions to bound the output distance of two stable systems. Unlike our novel notion of bisimulations, classical bisimulations focus only on behavioral similarity with respect to system dynamics and remain agnostic to task objectives. The same limitation applies to the gap metric.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

In reinforcement learning, approximate bisimulation has been used to capture state similarity in Markov decision processes with respect to immediate rewards and the distribution of next states under a given policy, and has been leveraged for policy transfer across similar states. These measures do not quantify deviations in policy gradient descent directions across tasks, where similarity must jointly capture both dynamics and objectives in the cost gradients. Our work addresses this gap by introducing a bisimulation-based measure that bounds the cost gradient discrepancy across LQR tasks under a common stabilizing controller.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

In multitask reinforcement learning, a standard method of approximating the minimum value $J_{\text{avg}}{(K_{\star})}$ is that of policy gradient. In our setting, we apply policy gradient with an initial controller $K_{0} \in \mathcal{K}_{\text{stab}}$^11^1A controller $K_{0} \in \mathcal{K}_{\text{stab}}$ can be efficiently computed.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Our paper aims to analyze the task-specific performance of $K_{\star}$ and $K_{n}$ with respect to that of each $K_{\star}^{(i)}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

as fundamental for bounding the task-specific optimality gaps. Therefore, we say that $g_{ij}{(K)}$ quantifies the *heterogeneity* between tasks $\mathcal{T}^{(i)}$ and $\mathcal{T}^{(j)}$ under any $K \in \mathcal{K}_{\text{stab}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Limitations of Existing Task Heterogeneity Measures", "weight": 1.5} -->

Bounds $b_{Q}$ and $b_{R}$ for the cost parameter deviations are similarly defined.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Limitations of Existing Task Heterogeneity Measures", "weight": 1.5} -->

For the exact expression of $\overline{b}{(K)}$, we refer the reader to \[7, Appendix 6.2\]. The measures $\overline{b}{(K_{\star})}$ and $\overline{b}{(K_{n})}$ are used to bound the performance gaps ${J^{(i)}{(K_{\star})}} - {J^{(i)}{(K_{\star}^{(i)})}}$ and ${J^{(i)}{(K_{n})}} - {J^{(i)}{(K_{\star}^{(i)})}}$, respectively. However, they are often vacuous in practice, even when the actual performance gaps are small, as illustrated in the following example.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Example 1 (Inverted Pendulum)", "weight": 1.0} -->

As shown in Fig. 1. ‣ 2.1 Limitations of Existing Task Heterogeneity Measures ‣ 2 Problem Formulation ‣ Policy Gradient Bounds in Multitask LQR"), the optimality gaps (7 ‣ 2 Problem Formulation ‣ Policy Gradient Bounds in Multitask LQR")) are below $0.15$ at convergence, for a step size of $0.01$, indicating satisfactory performance of the multitask policy gradient controller. This is in contrast to the heterogeneity measure $\overline{b}{(K_{n})}$, which evaluates to $2.3 \times 10^{6}$ at convergence. Its conservatism can be explained by the derivation of $\overline{b}{(K)}$ in terms of parameter deviation bounds. Specifically, despite the dependence of $\overline{b}{(K)}$ on $K$, its construction overlooks potential closed-loop task similarities that could lead to smaller task heterogeneity.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Toward Closed-Loop Task Heterogeneity Measures", "weight": 1.0} -->

Our goal is to develop closed-loop measures of task heterogeneity, suitable for bounding the performance of both the multitask optimal controller and the policy gradient iterates. Exploiting the closed-loop behavior is intended to mitigate the conservatism incurred by the previous use of parameter deviation bounds to analyze the gaps (6 ‣ 2 Problem Formulation ‣ Policy Gradient Bounds in Multitask LQR")) and (7 ‣ 2 Problem Formulation ‣ Policy Gradient Bounds in Multitask LQR")).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Toward Closed-Loop Task Heterogeneity Measures", "weight": 1.0} -->

Toward this end, we next present a novel notion of bisimulation-based measures of task heterogeneity, which bound the gradient gaps. In Section 4, we leverage these measures to bound the optimality gaps (6 ‣ 2 Problem Formulation ‣ Policy Gradient Bounds in Multitask LQR")) and (7 ‣ 2 Problem Formulation ‣ Policy Gradient Bounds in Multitask LQR")).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Bisimulation-Based Task Heterogeneity", "weight": 1.0} -->

In this section, we propose bisimulation-based measures that allow us to bound the discrepancy in cost gradients between tasks, as quantified. Unlike existing measures of task heterogeneity, our measures provide a *closed-loop* notion of heterogeneity between different tasks. In Subsection 3.1, we define bisimulation functions that can be used to bound the gradient discrepancies. In Subsection 3.2, we develop an effective derivation of these functions and formalize our bisimulation-based measures.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Bisimulation Functions for Cost Gradient Discrepancies", "weight": 1.0} -->

We now introduce novel bisimulation functions that allow us to analyze the gradient gaps.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Bisimulation Functions for Cost Gradient Discrepancies", "weight": 1.0} -->

where $\Sigma_{K,t}^{(i)} \in {\mathbb{S}}_{+}^{d_{x}}$ and $E_{K}^{(i)}$ is defined. The dynamics in represent those of system $i$'s covariance under controller $K$. By using \[4, Lemma 1\] and the fact that $K \in \mathcal{K}_{\text{stab}}$, we can deduce that the output $Y_{K,t}^{(i)}$ converges to the cost gradient ${\nabla J^{(i)}}{(K)}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Bisimulation Functions for Cost Gradient Discrepancies", "weight": 1.0} -->

and can focus on bounding the asymptotic output distance of systems $S_{K}^{(i)}$ and $S_{K}^{(j)}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Bisimulation Functions for Cost Gradient Discrepancies", "weight": 1.0} -->

The concept of bisimulation functions, as introduced, provides a principled method for characterizing the output distance between two stable continuous-time systems with vector states. Next, we extend the definition of bisimulation functions to affine matrix systems of the form.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Task Heterogeneity via Bisimulation Function Design", "weight": 1.0} -->

In this subsection, we develop a systematic procedure for designing bisimulation functions between systems $S_{K}^{(i)}$ and $S_{K}^{(j)}$. Then, we leverage these functions to introduce bisimulation-based measures of task heterogeneity.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The conditions in Lemma 2 are the discrete-time analogues of those derived for continuous-time linear systems with vector states. The bisimulation-based task heterogeneity (20. ‣ 3.2 Task Heterogeneity via Bisimulation Function Design ‣ 3 Bisimulation-Based Task Heterogeneity ‣ Policy Gradient Bounds in Multitask LQR")) is the minimum bisimulation bound for the difference in the cost gradient responses of the $i$-th and $j$-th task, under a common $K \in \mathcal{K}_{\text{stab}}$, as. The value of $\lambda_{K}^{({ij})}$ is determined by the stability margin of $A_{K}^{({ij})}$; specifically, the larger the stability margin, the larger $\lambda_{K}^{({ij})}$ becomes (see (17b)).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Moreover, $M_{K}^{({ij})}$ corresponds to the solution of a Lyapunov equation for $A_{K}^{({ij})}$, which dominates a matrix related to $E_{K}^{(i)}$ and $E_{K}^{(j)}$ (see (17a) and (17b)). These matrices are zero when $K$ is equal to $K_{\star}^{(i)}$ and $K_{\star}^{(j)}$, respectively. Note also the dependence of $b_{ij}{(K)}$ on the initial state covariances $\Sigma_{0}^{(i)}$ and $\Sigma_{0}^{(j)}$, which directly affect the cost of the respective LQR tasks.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Subsequently, we demonstrate how the measures $b_{ij}{(K)}$ influence the optimality gaps (6 ‣ 2 Problem Formulation ‣ Policy Gradient Bounds in Multitask LQR")) and (7 ‣ 2 Problem Formulation ‣ Policy Gradient Bounds in Multitask LQR")), while reducing the conservatism of the previous task heterogeneity bounds.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Policy Gradient Bounds in Multitask LQR via Bisimulations", "weight": 1.0} -->

We now analyze the task-specific optimality gaps (6 ‣ 2 Problem Formulation ‣ Policy Gradient Bounds in Multitask LQR")) and (7 ‣ 2 Problem Formulation ‣ Policy Gradient Bounds in Multitask LQR")) based on the bisimulation-based task heterogeneity measures (20. ‣ 3.2 Task Heterogeneity via Bisimulation Function Design ‣ 3 Bisimulation-Based Task Heterogeneity ‣ Policy Gradient Bounds in Multitask LQR")).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Policy Gradient Bounds in Multitask LQR via Bisimulations", "weight": 1.0} -->

Before introducing our main results, we present a few definitions that will be needed for their statement.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Policy Gradient Bounds in Multitask LQR via Bisimulations", "weight": 1.0} -->

where $b_{ij}{(K)}$ are given by (20. ‣ 3.2 Task Heterogeneity via Bisimulation Function Design ‣ 3 Bisimulation-Based Task Heterogeneity ‣ Policy Gradient Bounds in Multitask LQR")). We note that $b_{i}{(K)}$ describes the average bisimulation-based heterogeneity between the task $\mathcal{T}^{(i)}$ and each of the other tasks. We proceed with defining the stabilizing subset $\mathcal{K} \subset {\mathbb{R}}^{d_{u} \times d_{x}}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 2 (Result Interpretation)", "weight": 1.0} -->

The suboptimality bounds in (22. ‣ 4 Policy Gradient Bounds in Multitask LQR via Bisimulations ‣ Policy Gradient Bounds in Multitask LQR")) and are equal up to universal constants and the bisimulation-based measures $b_{i}{(K)}$, which are evaluated at $K_{\star}$ and $K_{\infty}$, respectively. Their similarity is notable as the analysis of Theorem 2. ‣ 4 Policy Gradient Bounds in Multitask LQR via Bisimulations ‣ Policy Gradient Bounds in Multitask LQR") is algorithm-independent and corresponds to the multitask optimal controller, while the analysis of Theorem 3. ‣ 4 Policy Gradient Bounds in Multitask LQR via Bisimulations ‣ Policy Gradient Bounds in Multitask LQR") relies on the policy gradient algorithm defined.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 2 (Result Interpretation)", "weight": 1.0} -->

Beyond the measures $b_{i}{(K)}$, the optimality gaps are bounded in terms of: i) the steady-state covariance of system $i$ under the task-specific optimal controller $K_{\star}^{(i)}$, ii) the initial state covariance $\Sigma_{0}^{(i)}$, and iii) the input cost matrix $R^{(i)}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 2 (Result Interpretation)", "weight": 1.0} -->

In the next section, we observe that our closed-loop measures significantly reduce the conservatism of previous heterogeneity measures and better capture the performance of multitask policy gradient LQR.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Numerical Validation", "weight": 1.0} -->

We next present numerical examples^22^2Code for reproduction can be found at our GitHub repository. on the inverted pendulum and unicycle dynamics applying multitask policy gradient LQR to demonstrate the effectiveness of our bounds. We observe that our bisimulation-based measures are less conservative than the baseline bounds designed based, which bound the cost gradient discrepancies in terms of the task parameter deviation bounds ${b_{A},b_{B},b_{Q}},$ and $b_{R}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Numerical Validation", "weight": 1.0} -->

Inverted Pendulum. We revisit Example 1. ‣ 2.1 Limitations of Existing Task Heterogeneity Measures ‣ 2 Problem Formulation ‣ Policy Gradient Bounds in Multitask LQR") and compare our bisimulation-based measures with baseline task heterogeneity measures ${\overline{b}{(K)}}:={\overline{b}{(K;b_{A},b_{B},b_{Q},b_{R})}}$ obtained.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Numerical Validation", "weight": 1.0} -->

Suboptimality bounds similar to those in (22. ‣ 4 Policy Gradient Bounds in Multitask LQR via Bisimulations ‣ Policy Gradient Bounds in Multitask LQR")) and can be derived in terms of $\overline{b}{(K_{\star})}$ and $\overline{b}{(K_{\infty})}$, respectively (see Subsection 2.1). Recall that $\overline{b}{(K_{\infty})}$ evaluates to $2.3 \times 10^{6}$ in this example, despite the small optimality gaps observed in Fig. 2. In contrast, our bisimulation-based measures depicted in Fig. 2 are below $3$ at convergence, reflecting the favorable task-specific performance of the multitask controller.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Numerical Validation", "weight": 1.0} -->

We repeat the computation of both measures over $100$ collections of inverted-pendulum tasks, which are generated as in Example 1. ‣ 2.1 Limitations of Existing Task Heterogeneity Measures ‣ 2 Problem Formulation ‣ Policy Gradient Bounds in Multitask LQR"). In this case, we observe an average reduction of $99.9998\%$, which suggests a substantial decrease of conservatism with respect to the previous bounds.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Numerical Validation", "weight": 1.0} -->

Unicycle. We consider a collection of $6$ LQR tasks corresponding to the linearized unicycle dynamics.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Numerical Validation", "weight": 1.0} -->

with state $x = {(p_{x},p_{y},\theta)}$ and input $u = {(v,\omega)}$, where $(p_{x},p_{y})$ is the robot's position on the $x,y$-plane, $\theta$ is the orientation angle, $v$ is the forward velocity, and $\omega$ is the yaw rate. We linearize the dynamics at operating points $(v_{0,i},\theta_{0,i})$ and then discretize with step size ${dt} = 0.05$

<!-- chunk {"id": "body-0044", "role": "body", "section": "Numerical Validation", "weight": 1.0} -->

Fig. 3 depicts the results for the multitask unicycle setting. On the left, we observe that the policy gradient controller achieves performance close to the task-specific optima, illustrating a setting favorable for collaborative control design. In the middle, we note that our bisimulation-based measures are below $1$ at convergence, suggesting that the tasks are similar in closed loop with the designed common controller. This indicates the effectiveness of our task heterogeneity measure on capturing collaborative settings where the designed controller can be readily applied across distinct tasks. Further evaluation of our measures is reserved for future work.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Numerical Validation", "weight": 1.0} -->

On the right plot, we compare ${\max_{i}b_{i}}{(K_{n})}$ with the measure $\overline{b}{(K_{n})}$ from prior works, averaged over $75$ random collections of two unicycle tasks. We note that our measure is significantly less conservative, with a reduction of $99.9996\%$ at convergence, leading to non-vacuous task-specific optimality guarantees. In contrast, the previous heterogeneity measure is overly pessimistic and fails to capture the observed task similarities.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Future Work", "weight": 1.5} -->

Moving forward, our bisimulation-based measures could be applied to relax the task heterogeneity assumptions and enhance the performance bounds in related settings (e.g., LQR with domain randomization, meta-learning LQR ). Moreover, we aim to leverage our new task heterogeneity measures to guide the learning of latent shared dynamics among multiple systems, providing a more favorable setting for applying multitask LQR. Another interesting direction is to employ our bisimulation-based measures in the design of policy gradient updates and provide robustness guarantees for multitask LQR design. Our results can also be extended for the analysis of the model-free setting.
