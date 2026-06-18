<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Fast Efficient Hyperparameter Tuning for Policy Gradient Methods

Topics include HOOF, Hyperparameter optimization, Policy gradients, Reinforcement learning, Sample efficiency, Meta-learning, Importance sampling, Automatic tuning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Presents HOOF, a one-run hyperparameter tuning method for policy-gradient reinforcement learning. The method uses trajectories already collected by the learner to rank candidate policy updates via importance-weighted one-step improvement estimates, reducing the extra sampling burden of grid search or population-based tuning.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The performance of policy gradient methods is sensitive to hyperparameter settings that must be tuned for any new application. Widely used grid search methods for tuning hyperparameters are sample inefficient and computationally expensive. More advanced methods like Population Based Training that learn optimal schedules for hyperparameters instead of fixed settings can yield better results, but are also sample inefficient and computationally expensive. In this paper, we propose Hyperparameter Optimisation on the Fly (HOOF), a gradient-free algorithm that requires no more than one training run to automatically adapt the hyperparameter that affect the policy update directly through the gradient. The main idea is to use existing trajectories sampled by the policy gradient method to optimise a one-step improvement objective, yielding a sample and computationally efficient algorithm that is easy to implement. Our experimental results across multiple domains and algorithms show that using HOOF to learn these hyperparameter schedules leads to faster learning with improved performance.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Policy gradient methods optimise reinforcement learning policies by performing gradient ascent on the policy parameters and have shown considerable success in environments characterised by large or continuous action spaces. However, like other gradient-based optimisation methods, their performance can be sensitive to a number of key hyperparameters.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

For example, the performance of first order policy gradient methods can depend critically on the learning rate, the choice of which in turn often depends on the task, the particular policy gradient method in use, and even the optimiser, e.g., RMSProp and ADAM have narrow ranges for good learning rates which may not be known a priori. Even for second order methods like Natural Policy Gradients (NPG) or Trust Region Policy Optimisation (TRPO), which are more robust to the KL divergence constraint (which can be interpreted as a learning rate), significant performance gains can often be obtained by tuning this parameter.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Similarly, variance reduction techniques such as Generalised Advantage Estimators (GAE), which trade variance for bias in policy gradient estimates, introduce key hyperparameters $(\gamma,\lambda)$ that can also greatly affect performance.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Given such sensitivities, there is a great need for effective methods for tuning policy gradient hyperparameters. Perhaps the most popular hyperparameter optimiser is simply grid search. More sophisticated techniques such as Bayesian optimisation (BO) have also proven effective, and new innovations such as Population Based Training (PBT) and meta-gradients have shown considerable promise. Furthermore, a host of methods have been proposed for hyperparameter optimisation in supervised learning (see Section 4).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, all these methods suffer from a major problem: they require performing many learning runs to identify good hyperparameters. This is particularly problematic in reinforcement learning, where it incurs not just computational costs but sample costs, as new learning runs typically require fresh interactions with the environment. This sample inefficiency is obvious in the case of grid search, BO based methods and PBT. However, even meta-gradients, which reuses samples collected by the underlying policy gradient method to train the meta-learner, requires multiple training runs. This is because the meta-learner introduces its own set of hyperparameters, e.g., meta learning rate and reference $(\gamma,\lambda)$, all of which need tuning to achieve good performance.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Furthermore, grid search and BO based methods typically estimate only the best fixed values of the hyperparameters, which often actually need to change dynamically during learning. This is particularly important in reinforcement learning, where the distribution of visited states, the need for exploration, and the cost of taking suboptimal actions can all vary greatly during a single learning run.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

To make hyperparameter optimisation practical for reinforcement learning methods such as policy gradients, we need radically more efficient methods that can dynamically set key hyperparameters on the fly, not just find the best fixed values, and do so within a single run, using only the data that the baseline method would have gathered anyway, without introducing new hyperparameters that need tuning. This goal may seem ambitious, but in this paper we show that it is actually entirely feasible, using a surprisingly simple method we call Hyperparameter Optimisation on the Fly (HOOF).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main idea is as follows: At each iteration, sample trajectories using the current policy. Next, generate some candidate policies and estimate their value sample efficiently by using an *off-policy* method. Finally, update the policy greedily with respect to the estimated value of the candidates. In practice, HOOF uses the policy gradient method with different hyperparameter (e.g., the learning rate, $\gamma$, and $\lambda$) settings to generate candidate policies and then uses importance sampling (IS) to construct off-policy estimates of the value of each candidate policy.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The viability of such a simple approach is counter-intuitive since off-policy evaluation using IS tends to have high variance that grows rapidly as the behaviour and evaluation policies diverge. However, HOOF is motivated by the insight that in second order methods such as NPG and TRPO, constraints on the magnitude of the update in policy space ensure that the IS estimates remain informative. While this is not the case for first order methods, we show that adding a simple KL constraint, without any of the complications of second order methods, suffices to keep IS estimates informative and enable effective hyperparameter optimisation. We further show that the performance of HOOF is robust to the setting of this KL constraint.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

HOOF is 1) sample efficient, requiring no more than one training run; 2) computationally efficient compared to sequential and parallel search methods; 3) able to learn a dynamic schedule for the hyperparameters that outperforms methods that learn fixed hyperparameter settings; and 4) simple to implement. Being gradient free, HOOF also avoids the limitations of gradient-based methods for learning hyperparameters. While such methods can be more sample efficient than grid search or PBT, they can be sensitive to the choice of their own hyperparameters (see Sections 4 and 5.1) and thus require more than one training run to tune their own hyperparameters.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate HOOF across a range of simulated continuous control tasks using the Mujoco OpenAI Gym environments. First, we apply HOOF to A2C, and show that using it to learn the learning rate can improve performance. We also perform a benchmarking exercise where we use HOOF to learn both the learning rate and the weighting for the entropy term and compare it against a grid search across these two hyperparameters. Next, we show that using HOOF to learn optimal hyperparameter schedules for NPG can outperform TRPO. This suggests that while strictly enforcing the KL constraint enables TRPO to outperform NPG, doing so becomes unnecessary once we can properly adapt NPG's hyperparameters.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Hyperparameter Optimisation on the Fly", "weight": 1.0} -->

The main idea behind HOOF is to automatically adapt the hyperparameters during training by greedily maximising the value of the updated policy, i.e., starting with policy $\pi_{n}$ at iteration $n$, HOOF sets

<!-- chunk {"id": "body-0016", "role": "body", "section": "Hyperparameter Optimisation on the Fly", "weight": 1.0} -->

Given a set of sampled trajectories, $f{(\psi)}$ can be computed for any $\psi$, and thus we can generate different candidate $\pi_{n + 1}$ without requiring any further samples. However, solving the optimisation problem in requires evaluating $J{(\pi_{n + 1})}$ for each such candidate. Any on-policy approach would have prohibitive sample requirements, so HOOF uses weighted importance sampling (WIS) to construct an off-policy estimate of $J{(\pi_{n + 1})}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Hyperparameter Optimisation on the Fly", "weight": 1.0} -->

The success of this approach depends critically on the quality of the WIS estimates, which can suffer from high variance that grows rapidly as the distributions of $\pi_{n + 1}$ and $\pi_{n}$ diverge. Fortunately, for natural gradient methods like NPG, $KL{(\pi_{n + 1}||\pi_{n})}$ is automatically approximately bounded by the update, ensuring reasonable WIS estimates when HOOF directly uses. In the following, we consider the more challenging case of first order methods.

<!-- chunk {"id": "body-0018", "role": "body", "section": "First Order HOOF", "weight": 1.0} -->

Without a KL bound on the policy update, it may seem that WIS will not yield adequate estimates to solve. However, a key insight is that, while the estimated policy value can have high variance, the relative ordering of the policies, which HOOF solves, has much lower variance (See Appendix E for an illustrative example). Nonetheless, HOOF could still fail if $KL{(\pi_{n + 1}||\pi_{n})}$ becomes too large, which can occur in first order methods.

<!-- chunk {"id": "body-0019", "role": "body", "section": "First Order HOOF", "weight": 1.0} -->

While this yields an update that superficially resembles that of natural gradient methods, the KL constraint is applied only during the search for the optimal hyperparameter settings using WIS. The direction of the update is determined solely by a first order gradient update rule, and estimation and inversion of the FIM is not required. From a practical perspective, this constraint is enforced by computing the KL for each candidate policy based on the observed trajectories, and the candidate is rejected if this sample KL is greater than the constraint.

<!-- chunk {"id": "body-0020", "role": "body", "section": "First Order HOOF", "weight": 1.0} -->

If learning the learning rate using HOOF, we can also use the KL constraint to dynamically adjust the search bounds: At each iteration, if none of the candidates violate the KL constraint, we increase the upper bound of the search space by a factor $\nu$, while if a large proportion of the candidates violate the KL constraint, we reduce the upper bound by $\nu$. This makes HOOF even more robust to the initial setting of the search space. Note that this is entirely optional, and is simply a means to reduce the number of number of candidates that would otherwise need to be generated and evaluated to ensure that a good solution of is found.

<!-- chunk {"id": "body-0021", "role": "body", "section": "First Order HOOF", "weight": 1.0} -->

0: Initial policy π0, number of policy iterations N, search space for ψ, KL constraint ϵ if using first order policy gradient method.
2: Sample trajectories τ1: K using πn.
4: Generate candidate hyperparameter {ψz} from the search space.
5: Compute candidate policy πz using ψz in
6: Estimate J (πz) using WIS
7: Compute KL(πz||πn) if using first order policy gradient method,
9: Select ψn, and hence πn + 1, according to or

<!-- chunk {"id": "body-0022", "role": "body", "section": "$({\\mathbf{γ}},{\\mathbf{λ}})$ Conditioned Value Function", "weight": 1.0} -->

If we use HOOF to learn $(\gamma,\lambda)$, $g_{n}$ has to be computed for each setting of $(\gamma,\lambda)$. With neural net value functions, we modify our value function such that its inputs are $(s,\gamma,\lambda)$, similar to Universal Value Function Approximators. Thus we learn a $(\gamma,\lambda)$-conditioned value function that can make value predictions for any candidate $(\gamma,\lambda)$ at the cost of a single forward pass. In Appendix D Conditional Value Functions ‣ Fast Efficient Hyperparameter Tuning for Policy Gradient Methods") we present some experimental results to show that learning a $(\gamma,\lambda)$-conditioned value function is key to the success of HOOF.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Robustness to HOOF Hyperparameters and Computational Costs", "weight": 1.0} -->

HOOF introduces two types of hyperparameters of its own: the search spaces for the various hyperparameters it tunes, and the number of candidate policies generated for evaluation. Since the candidate policies are generated using random search, these hyperparameters express a straight up trade-off between performance and computational cost: A larger search space and larger number of candidates should lead to better solution, but incur higher computational cost. However, just like in random search, the generation and evaluation of the candidate policies can be performed in parallel to reduce wall clock time. Alternatively, Bayesian Optimisation could be used to solve efficiently. Finally, we note that HOOF with random search is always more computationally efficient than grid/random search over the hyperparameters with the same number of candidates, as HOOF saves on the additional computational cost of sampling trajectories for each candidate incurred by grid/random search. HOOF additionally introduces the KL constraint hyperparameter for first order methods. We show experimentally that the performance of HOOF is robust to a wide range of settings for this.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Choice of Optimiser", "weight": 1.0} -->

Throughout this paper we use random search as the optimiser for to show that the simplest methods suffice. However, any gradient-free optimiser could be used instead. For example, grid search, CMA-ES, or Bayesian Optimisation are all viable alternatives.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Choice of Optimiser", "weight": 1.0} -->

Gradient based methods are not viable for two reasons. First, they require that $J{(\pi_{n + 1})}$ be differentiable w.r.t. the hyperparameters, which might be difficult or impossible to compute, e.g. with the TRPO update. Second, they introduce learning rate and initialisation hyperparameters, which require tuning at the expense of sample efficiency.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Experiments", "weight": 1.0} -->

To experimentally validate HOOF, we apply it to four simulated continuous control tasks from MuJoCo OpenAI Gym: HalfCheetah, Hopper, Ant, and Walker. We start with A2C, and show that HOOF performs better than multiple baselines, and is also far more sample efficient. Next, we use NPG as the underlying policy gradient method and apply HOOF to learn $(\delta,\gamma,\lambda)$ and show that it outperforms TRPO.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experiments", "weight": 1.0} -->

We repeat all experiments across 10 random starts. In all figures solid lines represent the median, and shaded regions the quartiles. Similarly all results in tables represent the median. Hyperparameters that are not tuned are held constant across HOOF and baselines to ensure comparability. Details about all hyperparameters can be found in the appendices.

<!-- chunk {"id": "body-0028", "role": "body", "section": "HOOF with A2C", "weight": 1.0} -->

In the A2C framework, a neural net with parameters $\theta$ is commonly used to represent both the policy and the value function, usually with some shared layers.

<!-- chunk {"id": "body-0029", "role": "body", "section": "HOOF with A2C", "weight": 1.0} -->

where we have omitted the dependence on the timestep and other hyperparameters for ease of notation. The performance of A2C is particularly sensitive to the choice of the learning rate $\alpha$, which requires careful tuning.

<!-- chunk {"id": "body-0030", "role": "body", "section": "HOOF with A2C", "weight": 1.0} -->

We learn $\alpha$ using HOOF with the KL constraint $\epsilon = 0.03$ ('HOOF'). We compare this against two baselines: Baseline A2C, i.e., A2C with the initial learning rate set to the OpenAI Baselines default (0.0007), and learning rate being learnt by meta-gradients ('Tuned Meta-Gradient'), where the hyperparameters introduced by meta-gradients were tuned using grid search.

<!-- chunk {"id": "body-0031", "role": "body", "section": "HOOF with A2C", "weight": 1.0} -->

The learning curves in Figure 1 shows that across all environments HOOF learns faster than Baseline A2C, and also outperforms it in HalfCheetah and Walker, demonstrating that learning the learning rate online can yield significant gains.

<!-- chunk {"id": "body-0032", "role": "body", "section": "HOOF with A2C", "weight": 1.0} -->

The update rule for meta-gradients when learning $\alpha$ reduces to $\alpha^{\prime} = {\alpha + {\beta{{\nabla_{\theta^{\prime}}\log}\pi_{\theta^{\prime}}}{(\left. a \middle| s \right.)}{({R - {V_{\theta^{\prime}}{(s)}}})}\frac{f_{\theta}{(\psi)}}{\alpha}}}$, where $\beta$ is the meta learning rate. This leads to two issues: what should the learning rate be initialised to ($\alpha_{0}$), and what should the meta learning rate be set to? Like all gradient based methods, the performance of meta gradients can be sensitive to the choices of these two hyperparamters. When we set $\alpha_{0}$ to the OpenAI baselines default setting and $\beta$ to 0.001 as per Xu et al. A2C fails to learn at all.

<!-- chunk {"id": "body-0033", "role": "body", "section": "HOOF with A2C", "weight": 1.0} -->

Thus, we had to run a grid search over $(\alpha_{0},\beta)$ to find the optimal settings across these hyperparameters. In Figure 1 we plot the best run from this grid search. Despite using 36 times as many samples (due to the grid search), meta-gradients still cannot outperform HOOF, and learns slower in 3 of the 4 tasks. The returns for each of the 36 points on the grid are presented in Appendix B.1 and they show that the performance of meta gradients can be sensitive to these two hyperparamters.

<!-- chunk {"id": "body-0034", "role": "body", "section": "HOOF with A2C", "weight": 1.0} -->

To show that HOOF's performance is robust to $\epsilon$, its own hyperparameter quantifying the KL constraint, we repeated our experiments with different values of $\epsilon$. The results presented in Table 1 show that HOOF's performance is stable across different values of this parameter. This is not surprising -- the sole purpose of the constraint is to ensure that the WIS estimates remain viable.

<!-- chunk {"id": "body-0035", "role": "body", "section": "HOOF with A2C", "weight": 1.0} -->

Max return over subsampled grid of size

<!-- chunk {"id": "body-0036", "role": "body", "section": "HOOF with A2C", "weight": 1.0} -->

Finally, to ascertain the sample efficiency of HOOF relative to grid search, we perform a benchmarking exercise. We used HOOF to learn both the learning rate and the entropy coefficient ($c_{2}$ in ). We split the search bounds for these across a grid with 11x11 points and ran A2C for each setting on the grid. For computational reasons we set the budget for each training run to 1 million timesteps. Given a budget of $n$ training runs, we randomly subsample $n$ points from the grid (without replacement) and note the best return. We repeat this 1000 times to get an estimate of the expected best return of the grid search with a budget of $n$ training runs. The results presented in Table 2 compares the returns of HOOF to that of the expected best return for grid search with different training budgets. The performance of grid search is much worse than that of HOOF with the same budget (i.e., only 1 training run). The results show that grid search can take more than 10 times as many samples to match HOOF's performance.
