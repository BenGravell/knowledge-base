<!-- arxiv-full-text:v1 {"arxiv_id": "2401.16025", "source": "arxiv-html"} -->

## Introduction

Deep Reinforcement Learning (DRL) has achieved great success in recent years, notably in games, foundation model fine-tuning, and robotic control. Policy gradient (PG) methods, as a major paradigm in RL, have been widely adopted by the academic community. One main practical challenge of PG methods is to reduce the variance of the gradients while keeping the bias low. In this context, a widely used technique is to add a baseline when sampling an estimate of the action-value function. Another challenge of PG methods is to estimate the proper step size for the policy update. Given that the training data strongly depends on the current policy, a large step size may result in a collapse of policy performance, whereas a small one may impair the sample efficiency of the algorithm.

Figure 2: (Left) The only difference between SPO and PPO is the policy loss, where ${\color[rgb]\definecolor[named]{pgfstrokecolor}{rgb}\pgfsys@color@gray@stroke\pgfsys@color@gray@fillr_{t}(\theta)}=\pi_{\theta}(a_{t}|s_{t})/\pi_{\theta_{\mathrm{old}}}(a_{t}|s_{t})$ and ${\color[rgb]{1,.5,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,.5,0}\epsilon}$ is the probability ratio hyperparameter, making it simple and straightforward to implement SPO based on high-quality PPO implementations. (Right) The optimization behavior of PPO and SPO is visualized, where each scatter point represents the probability ratio of a single data point for a specific training epoch, with its color corresponding to its advantage, and the red line representing the probability ratio bound.

To address these challenges, Schulman et al. proved that optimizing a certain surrogate objective guarantees policy improvement with non-trivial step sizes. Subsequently, the TRPO algorithm was derived through a series of approximations, which impose a trust region constraint during the policy iterations, leading to monotonic policy improvement in theory. However, given the complexity of second-order optimization, TRPO is highly inefficient and can be hard to extend to large-scale RL environments. Proximal Policy Optimization (PPO) is designed to enforce comparable constraints on the difference between successive policies during the training process, while only using first-order optimization. By clipping the current data that exceeds the probability ratio limit to a constant, PPO attempts to remove the high incentive for pushing the current policy away from the old one. It has been demonstrated that PPO can be effectively extended to large-scale complex control tasks.

Despite its success, the optimization behavior of PPO remains insufficiently understood. Although PPO aims to constrain the probability ratio deviations between successive policies, it often fails to keep these ratios within bounds. In some tasks, the ratios can even escalate to values as high as $40$. Furthermore, studies have revealed that PPO's performance is highly dependent on "code-level optimizations". The implementation of PPO includes numerous code-level details that critically influence its effectiveness.

In this paper, we propose a new model-free RL algorithm named Simple Policy Optimization (SPO) designed to more effectively bound probability ratios through a novel objective function. The key differences in optimization behavior between PPO and SPO are illustrated in Figure 2. Our main contributions are summarized as follows: We theoretically prove that optimizing a tighter performance lower bound using Total Variation (TV) divergence constrained space results in more consistent policy improvement.

To overcome PPO's limitation in constraining probability ratios, we propose a new objective function, leading to the development of the proposed SPO algorithm.

Experiments benchmark various policy gradient algorithms across different environments, showing that SPO can achieve competitive performance with a simple implementation, improved sample efficiency, and easier training of deeper policy networks.

## Related Work

Since TRPO theoretically demonstrated monotonic policy improvement, numerous studies have explored how to enforce trust region constraints efficiently, which are essential for ensuring robust policy improvement. For instance, the widely-used PPO algorithm was the first to introduce the heuristic clipping technique, effectively avoiding the computationally expensive second-order optimization. This heuristic clipping technique has been widely used in various reinforcement learning algorithms.

However, empirical evidence from a wide range of studies demonstrates that ratio clipping fails to enforce trust region constraints effectively. To prevent aggressive policy updates, previous works have focused on designing adaptive learning rates based on TV divergence or KL divergence, which have been shown to effectively enhance the stability of PPO. On the other hand, code-level optimizations are crucial for the robust performance of PPO. High-quality implementations of PPO involve numerous code details, making it challenging to accurately assess the core factors that truly affect the algorithm's performance.

In this work, we argue that heuristic clipping technique cannot enforce trust region constraints (see Figure 2). During PPO's iterations, ratio clipping zeros the gradients of certain data points, which can lead to a lack of corrective gradients to prevent the policy from escaping the trust region, thus undermining the monotonic improvement guarantee. As a result, PPO requires additional code-level tuning, such as adaptive learning rates or early stopping strategies, to artificially prevent performance collapse. We reveal this inherent flaw of ratio clipping and propose promising alternatives.

## Background

### Reinforcement Learning

Online reinforcement learning is a mathematical framework for sequential decision-making, which is generally defined by the Markov Decision Process (MDP) $\mathcal{M}=(\mathcal{S},\mathcal{A},r,\mathcal{P},\rho_{0},\gamma)$, where $\mathcal{S}$ and $\mathcal{A}$ represent the state space and action space, $r:\mathcal{S}\times\mathcal{A}\mapsto\mathbb{R}$ is the reward function, $\mathcal{P}:\mathcal{S}\times\mathcal{A}\times\mathcal{S}\mapsto$ is the probability distribution of the state transition function, $\rho_{0}:\mathcal{S}\mapsto$ is the initial state distribution, while $\gamma\in$ is the discount factor.

Suppose that an agent interacts with the environment following policy $\pi$, i.e., $a_{t}\sim\pi(\cdot|s_{t})$ and obtains a trajectory $\tau=\left(s_{0},a_{0},r_{0},\dots,s_{t},a_{t},r_{t},\dots\right)$, where $r_{t}=r(s_{t},a_{t})$. The goal of RL is to learn a policy that maximizes the objective $\eta(\pi)=\mathbb{E}_{\tau\sim\pi}\left[\sum_{t=0}^{\infty}\gamma^{t}r_{t}\right]$, where the notation $\mathbb{E}_{\tau\sim\pi}$ represents the expected return of the trajectory $\tau$ generated by the agent following policy $\pi$, i.e., $s_{0}\sim\rho_{0}(\cdot),a_{t}\sim\pi(\cdot|s_{t}),r_{t}=r(s_{t},a_{t}),s_{t+1}\sim\mathcal{P}(\cdot|s_{t},a_{t})$. The action-value function and value function are defined as Given $Q_{\pi}$ and $V_{\pi}$, the advantage function can be expressed as $A_{\pi}(s_{t},a_{t})=Q_{\pi}(s_{t},a_{t})-V_{\pi}(s_{t})$.

### Trust Region Policy Optimization

Classic policy gradient methods cannot reuse data and are highly sensitive to the hyperparameters. To address these issues, in Trust Region Policy Optimization (TRPO), Schulman et al. derived a lower bound for policy improvement. Before that, Kakade & Langford first proved the following policy performance difference theorem.

### Theorem 3.1

Let $\mathbb{P}(s_{t}=s|\pi)$ represents the probability of the $t$-th state equals to $s$ in trajectories generated by the agent following policy $\pi$, and $\rho_{\pi}(s)=(1-\gamma)\sum_{t=0}^{\infty}\gamma^{t}\mathbb{P}(s_{t}=s|\pi)$ represents the normalized discounted visitation distribution. Given any two policies, $\pi$ and $\tilde{\pi}$, their performance difference can be measured by where $\eta(\pi)=\mathbb{E}_{\tau\sim\pi}\left[\sum_{t=0}^{\infty}\gamma^{t}r_{t}\right]$.

The key insight is that the new policy $\tilde{\pi}$ will improve (or at least remain constant) as long as it has a nonnegative expected advantage at every state $s$. Then, the following performance improvement lower bound is given:

### Theorem 3.2

Given any two policies, $\pi$ and $\tilde{\pi}$, the following bound holds: where $\xi=\max_{s}\left|\mathbb{E}_{a\sim\tilde{\pi}(\cdot|s)}\left[A_{\pi}(s,a)\right]\right|$, $D_{\mathrm{TV}}$ is the Total Variation (TV) divergence.

Using importance sampling on action $a\sim{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\tilde{\pi}(\cdot|s)}$ and according to the Pinsker's inequality, we have At this point, the subscripts of the expectation in are replaced from $s\sim{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\rho_{\tilde{\pi}}(\cdot)}$ and $a\sim{\color[rgb]{1,0,0}\definecolor[named]{pgfstrokecolor}{rgb}{1,0,0}\tilde{\pi}(\cdot|s)}$ to $s\sim{\color[rgb]{0,120,255}\definecolor[named]{pgfstrokecolor}{rgb}{0,120,255}\rho_{\pi}(\cdot)}$ and $a\sim{\color[rgb]{0,120,255}\definecolor[named]{pgfstrokecolor}{rgb}{0,120,255}\pi(\cdot|s)}$, which means that we can now reuse the current data. In TRPO, the lower bound in is indirectly optimized by solving the following optimization problem: This problem includes a constraint where $\delta$ is a hyperparameter that limits the KL divergence between successive policies, with $\hat{A}(s_{t},a_{t})$ being the estimate of the advantage function, and the objective is called "surrogate objective".

### Proximal Policy Optimization

Due to the necessity of solving a constrained optimization problem in each update, TRPO is highly inefficient and can be challenging to apply to large-scale reinforcement learning tasks.

Schulman et al. proposed a new objective called "clipped surrogate objective", in which the algorithm is named Proximal Policy Optimization (PPO). PPO retains similar constraints of TRPO but is much easier to implement and involves only first-order optimization.

The "clipped surrogate objective", also called PPO-Clip, adopts a ratio clipping function. Denote $\hat{A}_{t}=\hat{A}(s_{t},a_{t})$, the objective of PPO-Clip can be expressed as with $\pi_{\theta_{\mathrm{old}}}$ and $\pi_{\theta}$ being the old policy and the current policy. The gradient of PPO-Clip, given the training data $(s_{t},a_{t})$, can be expressed as In other words, PPO-Clip aims to remove the high incentive for pushing the current policy away from the old one. PPO-Clip has gained wide adoption in the academic community due to its simplicity and performance.

## Methodology

PPO attempts to limit the differences between successive policies through ratio clipping. However, Wang et al. proved the following theorem:

### Theorem 4.1

For discrete action space tasks where $\left|\mathcal{A}\right|\geq 3$ or continuous action space tasks where the output of the policy $\pi_{\theta}$ follows a multivariate Gaussian distribution. Let $\Theta=\left\{\theta|1-\epsilon\leq r_{t}(\theta)\leq 1+\epsilon\right\}$, we have $\sup_{\theta\in\Theta}D_{\mathrm{KL}}(\pi_{\theta_{\mathrm{old}}}\|\pi_{\theta})[s_{t}]=+\infty$ for both discrete and continuous action space tasks.

Theorem 4.1 demonstrates that $D_{\mathrm{KL}}(\pi_{\theta_{\mathrm{old}}}\|\pi_{\theta})[s_{t}]$ is not necessarily bounded even if the probability ratio $r_{t}(\theta)$ is bounded. However, this theorem considers only an extreme case involving a single data point, which is less typical than the batch processing used in training data. On a broader scale, the heuristic clipping technique employed by PPO aims to bound the TV divergence for sufficient batch sizes. This relationship is formalized as Then, the performance improvement lower bound can be rewritten as This explains why PPO attempts to limit the probability ratio $\left|\tilde{\pi}(a|s)/\pi(a|s)-1\right|\leq\epsilon$, as this enforces a TV divergence trust region in expectation.

Finally, we also found that PPO, which aims to bound the TV divergence, can offer a larger solution space compared to methods that incorporate a looser KL divergence as a constraint (e.g., in TRPO). To illustrate this, we present the following proposition:

### Proposition 4.2

Given the old policy $\pi$, define the solution spaces under the TV and KL divergence constraints as follows: where $\delta_{\mathrm{KL}}>0$ is a predefined threshold. Let $\delta_{\mathrm{TV}}\geq\sqrt{\frac{1}{2}\delta_{\mathrm{KL}}}$, we establish that $\Omega_{\mathrm{KL}}\subset\Omega_{\mathrm{TV}}$.

### Proof

For any given $\delta_{\mathrm{KL}}$ and $\tilde{\pi}\in\Omega_{\mathrm{KL}}$, using Pinsker's inequality, we have $D_{\mathrm{TV}}(\pi\|\tilde{\pi})[s]\leq\sqrt{\frac{1}{2}D_{\mathrm{KL}}(\pi\|\tilde{\pi})[s]}\leq\sqrt{\frac{1}{2}\delta_{\mathrm{KL}}}\leq\delta_{\mathrm{TV}}$, therefore $\tilde{\pi}\in\Omega_{\mathrm{KL}}\Longrightarrow\tilde{\pi}\in\Omega_{\mathrm{TV}}$, which means $\Omega_{\mathrm{KL}}\subset\Omega_{\mathrm{TV}}$, concluding the proof. ∎ 1: Initialize: Policy and value networks πθ, Vϕ, hyperparameter ϵ, value loss and policy entropy coefficients c1, c2 2: Output: Optimal policy network πθ* 3: while not converged do 5: Collect data 𝒟 = {(st,, rt)}t = 1N using the current policy network πθ 6: # The networks before updating 8: # Estimate the advantage Â(st, at) based on Vϕold 9: Use GAE technique to estimate the advantage Â(st, at) 10: # Estimate the return R̂t 12: for each training epoch do 13: # Compute policy loss ℒp (This is the only difference between SPO and PPO) 14: $\mathcal{L}_{p}\leftarrow-\frac{1}{N}\sum_{t=1}^{N}\left\{\frac{\pi_{\theta}(a_{t}|s_{t})}{\pi_{\theta_{\mathrm{old}}}(a_{t}|s_{t})}\cdot\hat{A}(s_{t},a_{t})-\frac{\lvert\hat{A}(s_{t},a_{t})\rvert}{2\epsilon}\cdot\left[\frac{\pi_{\theta}(a_{t}|s_{t})}{\pi_{\theta_{\mathrm{old}}}(a_{t}|s_{t})}-1\right]^{2}\right\}$ 15: # Compute policy entropy ℒe and value loss ℒv 16: $\mathcal{L}_{e}\leftarrow\frac{1}{N}\sum_{t=1}^{N}\mathcal{H}(\pi_{\theta}(\cdot|s_{t})),\enspace\mathcal{L}_{v}\leftarrow\frac{1}{2N}\sum_{t=1}^{N}[V_{\phi}(s_{t})-\hat{R}_{t}]^{2}$ 17: # Compute total loss ℒ 19: # Update parameters θ and ϕ through backpropagation, λθ and λϕ is the step sizes Algorithm 1 Simple Policy Optimization (SPO) Additionally, the optimal solution to the lower bound in the TV divergence solution space, $\Omega_{\mathrm{TV}}$, is expected to be superior. We now present the following theorem:

### Theorem 4.3

Given the old policy $\pi$, and $\Omega_{\mathrm{TV}},\Omega_{\mathrm{KL}}$ presented in Proposition 4.2, let be the lower bounds of performance improvement with TV divergence and KL divergence. Let $\delta_{\mathrm{TV}}\geq\sqrt{\frac{1}{2}\delta_{\mathrm{KL}}}$, denote then $\mathcal{L}_{\pi}^{\mathrm{TV}}(\tilde{\pi}_{\mathrm{TV}}^{*})\geq\mathcal{L}_{\pi}^{\mathrm{KL}}(\tilde{\pi}_{\mathrm{KL}}^{*})$.

### Proof

Since $\Omega_{\mathrm{KL}}\subset\Omega_{\mathrm{TV}}$, we have thus $\mathcal{L}_{\pi}^{\mathrm{TV}}(\tilde{\pi}_{\mathrm{TV}}^{*})\geq\mathcal{L}_{\pi}^{\mathrm{KL}}(\tilde{\pi}_{\mathrm{KL}}^{*})$, concluding the proof. ∎ Based on the Proposition 4.2 and Theorem 4.3, we have the following conclusion: As a result, to optimize the lower bound, we aim to solve the following constrained optimization problem: where $r_{t}(\theta)=\pi_{\theta}(a_{t}|s_{t})/\pi_{\theta_{\mathrm{old}}}(a_{t}|s_{t})$ and $\hat{A}_{t}=\hat{A}(s_{t},a_{t})$.

PPO attempts to satisfy the constraints of through ratio clipping, but this does not prevent excessive ratio deviations (demonstrated in Figure 2). The underlying reason is that ratio clipping causes certain data points to stop contributing to the gradients. Over multiple iterations, this can lead to uncontrollable updates, as the absence of corrective gradients prevents the policy from recovering. To overcome this issue with ratio clipping, we propose the following objective: The details of the objective will be discussed in the following section, and the pseudo-code is shown in Algorithm 1.

## Theoretical Results

In this section, we provide some theoretical insights of the differences between PPO and SPO, demonstrating that SPO can be more effective in constraining probability ratios.

### Objective Class

Simplify the notation by using $r$ and $A$ to represent the probability ratio and the advantage value. Based on the previous analysis, our goal is to find an objective function $f(r,A,\epsilon)$ such that while optimizing the surrogate objective $rA$, the probability ratio is constrained by $\lvert r-1\rvert\leq\epsilon$.

According to, for any given $A\neq 0$ and $\epsilon>0$, we can write down the following desired optimization problem: The objective is linear, so the optimal solution is $r^{*}=1+\mathrm{sign}(A)\cdot\epsilon$, where $\mathrm{sign}(\cdot)$ is the sign function. Motivated by this, we present the following definition:

### Definition 5.1 ($\epsilon$-aligned)

For any given $A\neq 0$ and $\epsilon>0$, we say that the function $f(r,A,\epsilon)$ is $\epsilon$-aligned, if it is differentiable and convex with respect to $r$, and attains its maximum value at $r=1+\mathrm{sign}(A)\cdot\epsilon$.

The objective of PPO in and SPO in can be expressed as It can be obtained that $f_{\mathrm{ppo}}$ is not $\epsilon$-aligned, as $f_{\mathrm{ppo}}$ zeros the gradients under some special cases according to. For $f_{\mathrm{spo}}$, we have the following theorem:

### Theorem 5.2

$f_{\mathrm{spo}}$ is $\epsilon$-aligned.

### Proof

Obviously, $f_{\mathrm{spo}}$ is differentiable and convex with respect to $r$ since $f_{\mathrm{spo}}$ is a quadratic polynomial of $r$. For any given $A\neq 0$ and $\epsilon>0$, let $\partial f_{\mathrm{spo}}(r,A,\epsilon)/\partial r=0$, then thus $r=1+\mathrm{sign}(A)\cdot\epsilon$ is the optimal solution for $f_{\mathrm{spo}}$. ∎ Note that $f_{\mathrm{spo}}$ is not the only objective function that satisfies the definition. It can be proved that there is a simple objective function $f_{\mathrm{simple}}=-(r-1-\mathrm{sign}(A)\cdot\epsilon)^{2}$, which is also $\epsilon$-aligned. We will discuss the differences between these two in Section 6.3.

### Analysis of New Objective

We show that the optimization process of SPO can more effectively bound the probability ratio, as can be seen from Figure 3. The largest circular area in the figure represents the boundary on the probability ratio. The green circles represent data points with non-zero gradients during the training process, while the gray circles represent data points with zero gradients.

Figure 3: In PPO, certain data points exhibit zero gradients, while in SPO, all data points generate non-zero gradients that guide towards the constraint boundary.

During the training process of PPO, certain data points that exceed the probability ratio bound cease to provide gradients. In contrast, all data points in SPO contribute gradients that guide the optimization towards the constraint boundary. As training progresses, PPO will accumulate more gray circles that no longer provide gradients and may be influenced by the harmful gradients from green circles. This phenomenon could potentially push the gray circles further away from the constraint boundary. In contrast, the gradient directions of all data points in SPO point towards the constraint boundary. This indicates that SPO imposes stronger constraints on the probability ratio.

## Experiments

We report results on the Atari 2600 and MuJoCo benchmarks. In all our experiments, we utilize the RL library Gymnasium, which serves as a central abstraction to ensure broad interoperability between benchmark environments and training algorithms.

### Comparing Algorithms

Our implementation of SPO is compared against PPO-Clip, PPO-Penalty, SPU, PPO-RB, TR-PPO, TR-PPO-RB, and RPO in MuJoCo benchmark. We compute the algorithm's performance across ten separate runs with different random seeds. In addition, we emphasize that in all comparative experiments involving the same settings for SPO and PPO, the only modification in SPO is replacing the PPO's objective , no further code-level tuning is applied to SPO, highlighting its simplicity and efficiency.

Due to the absence of human score baselines in MuJoCo, we normalize the algorithms' performance across all environments using the training data of PPO-Clip, specifically, where $\max$ and $\min$ represent the maximum and minimum validation returns of PPO-Clip during training, respectively.

Figure 4: Aggregate metrics on MuJoCo-v4 with 95% CIs based on 6 environments. We collected the returns of each algorithm over the last 1% training steps across ten random seeds. In this context, higher median, IQM and mean scores and lower optimality gap are better.

Figure 5: Training performance of PPO and SPO with different policy network layers in MuJoCo benchmark. The mean and standard deviation are shown across 5 random seeds.

Table 1: Average return of PPO and SPO in the last 10% training steps across 5 separate runs with different random seeds, with their maximum ratio deviation during the entire training process.

As suggested in Agarwal et al., we employ stratified bootstrap confidence intervals to assess the confidence intervals of the algorithm and evaluate the composite metrics of SPO against other baselines, as illustrated in Figure 4. It can be observed that SPO achieved the best performance across nearly all statistical metrics, which fully demonstrates the strong potential of SPO. For the Atari 2600 benchmark, the main results are presented in Appendix A and C.

### Scaling Policy Network

To investigate how scaling policy network size impacts the sample efficiency of both PPO and SPO in MuJoCo, the number of policy network layers was increased without altering the hyperparameters or other settings. The standard deviation of the algorithm's performance was computed and visualized across five separate runs with different random seeds. The results, shown in Figure 5, 9 and Table 1, where the ratio deviation indicates the largest value of average ratio deviation in a batch during the entire training process, i.e., $\frac{1}{\left|\mathcal{D}\right|}\sum_{(s_{t},a_{t})\sim\mathcal{D}}\left|r_{t}(\theta)-1\right|$.

Figure 6: Training performance of SPO using ResNet-18 as the encoder compared to the PPO and SPO using default CNN (shown with the reference line). The mean and standard deviation are shown across 3 random seeds, and the red dashed line represents ϵ = 0.2.

It can be observed that as the network deepens, the performance of PPO collapses in most environments, with uncontrollable probability ratio deviations. In contrast, the performance of SPO outperforms that of shallow networks in almost all environments and constrains the probability ratio deviation effectively. Furthermore, the statistical metrics of SPO generally outperform PPO's and demonstrate relative robustness to variations in network depth and mini-batch size.

We also trained the ResNet-18^11^1Since Bhatt et al. demonstrated that batch normalization is harmful to RL training, we removed batch normalization. as the encoder on the Atari 2600 benchmark, the results are shown in Figure 6. As the network's capacity increases, the performance of SPO is significantly improved. Moreover, SPO can still maintain a good probability ratio constraint, thereby benefiting from the theoretical lower bound. In contrast, it is challenging to train large neural networks with PPO because the probability ratio cannot be controlled during training, even employing a smaller $\epsilon=0.1$.

Figure 7: The optimization behavior of fppo, fspo, and fsimple.

### Constraining Ratio Deviation

To further investigate the optimization behavior of different objective functions that satisfy the $\epsilon$-aligned definition, we visualize the optimization process of $f_{\mathrm{ppo}}$, $f_{\mathrm{spo}}$, and $f_{\mathrm{simple}}$ presented in Section 5.1, on the same batch of advantage values initialized from a standard Gaussian distribution, as shown in Figure 7.

We can observe that while PPO achieves the best performance in optimizing the surrogate objective, it also leads to uncontrollable ratio deviations. In contrast, the two objectives that satisfy the $\epsilon$-aligned definition effectively constrain the ratio deviations during the optimization process.

Furthermore, we also observe that $f_{\mathrm{spo}}$ achieves better optimization of the surrogate objective compared to $f_{\mathrm{simple}}$, while $f_{\mathrm{simple}}$ converges more quickly to the probability ratio boundary. This aligns with our expectations, as the optimization objective of $f_{\mathrm{simple}}$ only depends on the sign of the advantage values. As a result, $f_{\mathrm{simple}}$ pushes each data point equally toward the constraint boundary, which results in the magnitude of the advantage values being less effectively utilized compared to $f_{\mathrm{spo}}$, which makes it difficult to efficiently optimize the surrogate objective.

## Conclusion

In this paper, we introduce Simple Policy Optimization (SPO), a novel unconstrained first-order algorithm that effectively combines the strengths of Trust Region Policy Optimization (TRPO) and Proximal Policy Optimization (PPO). SPO maintains optimization within the trust region, benefiting from TRPO's theoretical guarantees while preserving the efficiency of PPO. Our experimental results demonstrate that SPO achieves competitive performance across various benchmarks with a simple implementation. Moreover, SPO simplifies the training of deep policy networks, addressing a key challenge faced by existing algorithms. These findings indicate that SPO is a promising approach for advancing model-free reinforcement learning. In future work, SPO holds potential for impactful applications in areas such as language models, robotic control, and financial modeling. With further research and refinement, we believe SPO will drive innovation and breakthroughs across these fields.
