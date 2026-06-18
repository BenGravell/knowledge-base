<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Simple Policy Optimization

Topics include Reinforcement learning, Policy optimization, Proximal policy optimization, Simple policy optimization, SPO.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Proposes a modified policy gradient loss that achieves better performance than PPO while maintaining simplicity.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Model-free reinforcement learning algorithms have seen remarkable progress, but key challenges remain. Trust Region Policy Optimization (TRPO) is known for ensuring monotonic policy improvement through conservative updates within a trust region, backed by strong theoretical guarantees. However, its reliance on complex second-order optimization limits its practical efficiency. Proximal Policy Optimization (PPO) addresses this by simplifying TRPO's approach using ratio clipping, improving efficiency but sacrificing some theoretical robustness. This raises a natural question: Can we combine the strengths of both methods? In this paper, we introduce Simple Policy Optimization (SPO), a novel unconstrained first-order algorithm. By slightly modifying the policy loss used in PPO, SPO can achieve the best of both worlds. Our new objective improves upon ratio clipping, offering stronger theoretical properties and better constraining the probability ratio within the trust region. Empirical results demonstrate that SPO outperforms PPO with a simple implementation, particularly for training large, complex network architectures end-to-end.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Deep Reinforcement Learning (DRL) has achieved great success in recent years, notably in games (Mnih et al. Silver et al. Vinyals et al., ), foundation model fine-tuning (Ouyang et al. Black et al., ), and robotic control (Makoviychuk et al. Rudin et al., ). Policy gradient (PG) methods (Sutton & Barto Lehmann, ), as a major paradigm in RL, have been widely adopted by the academic community. One main practical challenge of PG methods is to reduce the variance of the gradients while keeping the bias low. In this context, a widely used technique is to add a baseline when sampling an estimate of the action-value function. Another challenge of PG methods is to estimate the proper step size for the policy update. Given that the training data strongly depends on the current policy, a large step size may result in a collapse of policy performance, whereas a small one may impair the sample efficiency of the algorithm.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address these challenges, Schulman et al. proved that optimizing a certain surrogate objective guarantees policy improvement with non-trivial step sizes. Subsequently, the TRPO algorithm was derived through a series of approximations, which impose a trust region constraint during the policy iterations, leading to monotonic policy improvement in theory. However, given the complexity of second-order optimization, TRPO is highly inefficient and can be hard to extend to large-scale RL environments. Proximal Policy Optimization (PPO) is designed to enforce comparable constraints on the difference between successive policies during the training process, while only using first-order optimization. By clipping the current data that exceeds the probability ratio limit to a constant, PPO attempts to remove the high incentive for pushing the current policy away from the old one. It has been demonstrated that PPO can be effectively extended to large-scale complex control tasks (Ye et al. Makoviychuk et al., ).

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite its success, the optimization behavior of PPO remains insufficiently understood. Although PPO aims to constrain the probability ratio deviations between successive policies, it often fails to keep these ratios within bounds (Ilyas et al. Engstrom et al. Wang et al., ). In some tasks, the ratios can even escalate to values as high as $40$. Furthermore, studies have revealed that PPO's performance is highly dependent on "code-level optimizations". The implementation of PPO includes numerous code-level details that critically influence its effectiveness.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose a new model-free RL algorithm named Simple Policy Optimization (SPO) designed to more effectively bound probability ratios through a novel objective function. The key differences in optimization behavior between PPO and SPO are illustrated in Figure.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We theoretically prove that optimizing a tighter performance lower bound using Total Variation (TV) divergence constrained space results in more consistent policy improvement.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

To overcome PPO's limitation in constraining probability ratios, we propose a new objective function, leading to the development of the proposed SPO algorithm.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Experiments benchmark various policy gradient algorithms across different environments, showing that SPO can achieve competitive performance with a simple implementation, improved sample efficiency, and easier training of deeper policy networks.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Reinforcement Learning", "weight": 1.0} -->

Online reinforcement learning is a mathematical framework for sequential decision-making, which is generally defined by the Markov Decision Process (MDP) $\mathcal{M} = {(\mathcal{S},\mathcal{A},r,\mathcal{P},\rho_{0},\gamma)}$, where $\mathcal{S}$ and $\mathcal{A}$ represent the state space and action space, $r:{{\mathcal{S} \times \mathcal{A}}\mapsto{\mathbb{R}}}$ is the reward function, $\mathcal{P}:{{\mathcal{S} \times \mathcal{A} \times \mathcal{S}}\mapsto{\lbrack 0,1\rbrack}}$ is the probability distribution of the state transition function, $\rho_{0}:{\mathcal{S}\mapsto{\lbrack 0,1\rbrack}}$ is the initial state distribution, while $\gamma \in {}$ is the discount factor.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Trust Region Policy Optimization", "weight": 1.0} -->

Classic policy gradient methods cannot reuse data and are highly sensitive to the hyperparameters. To address these issues, in Trust Region Policy Optimization (TRPO), Schulman et al. derived a lower bound for policy improvement. Before that, Kakade & Langford first proved the following policy performance difference theorem.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Proximal Policy Optimization", "weight": 1.0} -->

Due to the necessity of solving a constrained optimization problem in each update, TRPO is highly inefficient and can be challenging to apply to large-scale reinforcement learning tasks.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Proximal Policy Optimization", "weight": 1.0} -->

Schulman et al. proposed a new objective called "clipped surrogate objective", in which the algorithm is named Proximal Policy Optimization (PPO). PPO retains similar constraints of TRPO but is much easier to implement and involves only first-order optimization.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Proximal Policy Optimization", "weight": 1.0} -->

The "clipped surrogate objective", also called PPO-Clip, adopts a ratio clipping function. Denote ${\hat{A}}_{t} = {\hat{A}{(s_{t},a_{t})}}$, the objective of PPO-Clip can be expressed as

<!-- chunk {"id": "body-0016", "role": "body", "section": "Proximal Policy Optimization", "weight": 1.0} -->

with $\pi_{\theta_{old}}$ and $\pi_{\theta}$ being the old policy and the current policy. The gradient of PPO-Clip, given the training data $(s_{t},a_{t})$, can be expressed as

<!-- chunk {"id": "body-0017", "role": "body", "section": "Proximal Policy Optimization", "weight": 1.0} -->

In other words, PPO-Clip aims to remove the high incentive for pushing the current policy away from the old one. PPO-Clip has gained wide adoption in the academic community due to its simplicity and performance.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Methodology", "weight": 1.0} -->

PPO attempts to limit the differences between successive policies through ratio clipping. However, Wang et al.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Theoretical Results", "weight": 1.0} -->

In this section, we provide some theoretical insights of the differences between PPO and SPO, demonstrating that SPO can be more effective in constraining probability ratios.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Objective Class", "weight": 1.0} -->

Simplify the notation by using $r$ and $A$ to represent the probability ratio and the advantage value. Based on the previous analysis, our goal is to find an objective function $f{(r,A,\epsilon)}$ such that while optimizing the surrogate objective $rA$, the probability ratio is constrained by ${|{r - 1}|} \leq \epsilon$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Objective Class", "weight": 1.0} -->

The objective is linear, so the optimal solution is $r^{\ast} = {1 + {{{sign}{(A)}} \cdot \epsilon}}$, where ${sign}{( \cdot )}$ is the sign function.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Analysis of New Objective", "weight": 1.0} -->

We show that the optimization process of SPO can more effectively bound the probability ratio, as can be seen from Figure. The largest circular area in the figure represents the boundary on the probability ratio. The green circles represent data points with non-zero gradients during the training process, while the gray circles represent data points with zero gradients.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Analysis of New Objective", "weight": 1.0} -->

During the training process of PPO, certain data points that exceed the probability ratio bound cease to provide gradients. In contrast, all data points in SPO contribute gradients that guide the optimization towards the constraint boundary. As training progresses, PPO will accumulate more gray circles that no longer provide gradients and may be influenced by the harmful gradients from green circles. This phenomenon could potentially push the gray circles further away from the constraint boundary. In contrast, the gradient directions of all data points in SPO point towards the constraint boundary. This indicates that SPO imposes stronger constraints on the probability ratio.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Experiments", "weight": 1.0} -->

We report results on the Atari 2600 (Bellemare et al. Machado et al., ) and MuJoCo benchmarks. In all our experiments, we utilize the RL library Gymnasium, which serves as a central abstraction to ensure broad interoperability between benchmark environments and training algorithms.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Comparing Algorithms", "weight": 1.0} -->

Our implementation of SPO is compared against PPO-Clip, PPO-Penalty, SPU, PPO-RB, TR-PPO, TR-PPO-RB, and RPO in MuJoCo benchmark. We compute the algorithm's performance across ten separate runs with different random seeds. In addition, we emphasize that in all comparative experiments involving the same settings for SPO and PPO, the only modification in SPO is replacing the PPO's objective, no further code-level tuning is applied to SPO, highlighting its simplicity and efficiency.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Comparing Algorithms", "weight": 1.0} -->

Due to the absence of human score baselines in MuJoCo, we normalize the algorithms' performance across all environments using the training data of PPO-Clip, specifically,

<!-- chunk {"id": "body-0027", "role": "body", "section": "Comparing Algorithms", "weight": 1.0} -->

where $\max$ and $\min$ represent the maximum and minimum validation returns of PPO-Clip during training, respectively.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Comparing Algorithms", "weight": 1.0} -->

As suggested in Agarwal et al., we employ stratified bootstrap confidence intervals to assess the confidence intervals of the algorithm and evaluate the composite metrics of SPO against other baselines, as illustrated in Figure. It can be observed that SPO achieved the best performance across nearly all statistical metrics, which fully demonstrates the strong potential of SPO. For the Atari 2600 benchmark, the main results are presented in Appendix A and C.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Scaling Policy Network", "weight": 1.0} -->

To investigate how scaling policy network size impacts the sample efficiency of both PPO and SPO in MuJoCo, the number of policy network layers was increased without altering the hyperparameters or other settings. The standard deviation of the algorithm's performance was computed and visualized across five separate runs with different random seeds. The results, shown in Figure, and Table, where the ratio deviation indicates the largest value of average ratio deviation in a batch during the entire training process, i.e., $\frac{1}{|\mathcal{D}|}{\sum_{{(s_{t},a_{t})} \sim \mathcal{D}}\left| {{r_{t}{(\theta)}} - 1} \right|}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Scaling Policy Network", "weight": 1.0} -->

It can be observed that as the network deepens, the performance of PPO collapses in most environments, with uncontrollable probability ratio deviations. In contrast, the performance of SPO outperforms that of shallow networks in almost all environments and constrains the probability ratio deviation effectively. Furthermore, the statistical metrics of SPO generally outperform PPO's and demonstrate relative robustness to variations in network depth and mini-batch size.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Scaling Policy Network", "weight": 1.0} -->

We also trained the ResNet-18^11^1Since Bhatt et al. demonstrated that batch normalization is harmful to RL training, we removed batch normalization. as the encoder on the Atari 2600 benchmark, the results are shown in Figure. As the network's capacity increases, the performance of SPO is significantly improved. Moreover, SPO can still maintain a good probability ratio constraint, thereby benefiting from the theoretical lower bound. In contrast, it is challenging to train large neural networks with PPO because the probability ratio cannot be controlled during training, even employing a smaller $\epsilon = 0.1$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Constraining Ratio Deviation", "weight": 1.0} -->

To further investigate the optimization behavior of different objective functions that satisfy the $\epsilon$-aligned definition, we visualize the optimization process of $f_{ppo}$, $f_{spo}$, and $f_{simple}$ presented in Section 5.1, on the same batch of advantage values initialized from a standard Gaussian distribution, as shown in Figure.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Constraining Ratio Deviation", "weight": 1.0} -->

We can observe that while PPO achieves the best performance in optimizing the surrogate objective, it also leads to uncontrollable ratio deviations. In contrast, the two objectives that satisfy the $\epsilon$-aligned definition effectively constrain the ratio deviations during the optimization process.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Constraining Ratio Deviation", "weight": 1.0} -->

Furthermore, we also observe that $f_{spo}$ achieves better optimization of the surrogate objective compared to $f_{simple}$, while $f_{simple}$ converges more quickly to the probability ratio boundary. This aligns with our expectations, as the optimization objective of $f_{simple}$ only depends on the sign of the advantage values. As a result, $f_{simple}$ pushes each data point equally toward the constraint boundary, which results in the magnitude of the advantage values being less effectively utilized compared to $f_{spo}$, which makes it difficult to efficiently optimize the surrogate objective.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we introduce Simple Policy Optimization (SPO), a novel unconstrained first-order algorithm that effectively combines the strengths of Trust Region Policy Optimization (TRPO) and Proximal Policy Optimization (PPO). SPO maintains optimization within the trust region, benefiting from TRPO's theoretical guarantees while preserving the efficiency of PPO. Our experimental results demonstrate that SPO achieves competitive performance across various benchmarks with a simple implementation. Moreover, SPO simplifies the training of deep policy networks, addressing a key challenge faced by existing algorithms. These findings indicate that SPO is a promising approach for advancing model-free reinforcement learning. In future work, SPO holds potential for impactful applications in areas such as language models, robotic control, and financial modeling. With further research and refinement, we believe SPO will drive innovation and breakthroughs across these fields.
