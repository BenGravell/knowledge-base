<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Simple Random Search Provides a Competitive Approach to Reinforcement Learning

Topics include Reinforcement learning, Random search, Evolution strategies, Policy optimization, Continuous control, Baseline, Evaluation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Describes Basic Random Search (BRS) and Augmented Random Search (ARS) and demonstrates that simple random perturbations to the parameters of linear policies with state normalization achieves competitive performance against deep RL on MuJoCo benchmarks. Challenges the necessity of more complicated neural network-backed policy optimization algorithms such as Trust Region Policy Optimization (TRPO), Deep Deterministic Policy Gradient (DDPG), Natural Gradients (NG), Evolution Strategies (ES), Proximal Policy Optimization (PPO), Soft Actor Critic (SAC), Soft Q-Learning (SQL), A2C, and the Cross Entropy Method (CEM).

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A common belief in model-free reinforcement learning is that methods based on random search in the parameter space of policies exhibit significantly worse sample complexity than those that explore the space of actions. We dispel such beliefs by introducing a random search method for training static, linear policies for continuous control problems, matching state-of-the-art sample efficiency on the benchmark MuJoCo locomotion tasks. Our method also finds a nearly optimal controller for a challenging instance of the Linear Quadratic Regulator, a classical problem in control theory, when the dynamics are not known. Computationally, our random search algorithm is at least 15 times more efficient than the fastest competing model-free methods on these benchmarks. We take advantage of this computational efficiency to evaluate the performance of our method over hundreds of random seeds and many different hyperparameter configurations for each benchmark task. Our simulations highlight a high variability in performance in these benchmark tasks, suggesting that commonly used estimations of sample efficiency do not adequately evaluate the performance of RL algorithms.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Model-free reinforcement learning (RL) aims to offer off-the-shelf solutions for controlling dynamical systems without requiring models of the system dynamics. Such methods have successfully produced RL agents that surpass human players in video games and games such as Go. Although these results are impressive, model-free methods have not yet been successfully deployed to control physical systems, outside of research demos. There are several factors prohibiting the adoption of model-free RL methods for controlling physical systems: the methods require too much data to achieve reasonable performance, the ever-increasing assortment of RL methods makes it difficult to choose what is the best method for a specific task, and many candidate algorithms are difficult to implement and deploy.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Unfortunately, the current trend in RL research has put these impediments at odds with each other. In the quest to find methods that are *sample efficient* (i.e. methods that need little data) the general trend has been to develop increasingly complicated methods. This increasing complexity has lead to a reproducibility crisis. Recent studies demonstrate that many RL methods are not robust to changes in hyperparameters, random seeds, or even different implementations of the same algorithm. Algorithms with such fragilities cannot be integrated into mission critical control systems without significant simplification and robustification.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Furthermore, it is common practice to evaluate and compare new RL methods by applying them to video games or simulated continuous control problems and measure their performance over a small number of independent trials (i.e., fewer than ten random seeds). The most popular continuous control benchmarks are the MuJoCo locomotion tasks, with the Humanoid model being considered "one of the most challenging continuous control problems solvable by state-of-the-art RL techniques." In principle, one can use video games and simulated control problems for beta testing new ideas, but simple baselines should be established and thoroughly evaluated before moving towards more complex solutions.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

To this end, we aim to determine *the simplest* model-free RL method that can solve standard benchmarks. Recently, two different directions have been proposed for simplifying RL. Salimans et al. introduced a derivative-free policy optimization method, called Evolution Strategies (ES). The authors showed that, for several RL tasks, their method can easily be parallelized to train policies faster than other methods. While the method proposed by Salimans et al. is simpler than previously proposed methods, it employs several complicated algorithmic elements, which we discuss in Section 3.4. As a second simplification to model-free RL, Rajeswaran et al. have shown that linear policies can be trained via natural policy gradients to obtain competitive performance on the MuJoCo locomotion tasks, showing that complicated neural network policies are not needed to solve these continuous control problems. In this work, we combine ideas from the work of Salimans et al. and Rajeswaran et al. to obtain the simplest model-free RL method yet, a derivative-free optimization algorithm for training linear policies.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate that a simple random search method can match or exceed state-of-the-art sample efficiency on MuJoCo locomotion benchmarks. Moreover, our method is at least $15$ times more computationally efficient than ES, the fastest competing method. Our findings contradict the common belief that policy gradient techniques, which rely on exploration in the action space, are more sample efficient than methods based on finite-differences. In more detail, our contributions are as follows: In Section 3, we present a classical, basic random search algorithm for solving derivative-free optimization problems. For application to continuous control, we augment the basic random search method with three simple features. First, we scale each update step by the standard deviation of the rewards collected for computing that update step. Second, we normalize the system's states by online estimates of their mean and standard deviation. Third, we discard from the computation of the update steps the directions that yield the least improvement of the reward. We refer to this method as *Augmented Random Search*^11^1Our implementation of ARS can be found at (ARS).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Section 4.2, we evaluate the performance of ARS on the benchmark MuJoCo locomotion tasks. Our method can learn static, linear policies that achieve high rewards on all MuJoCo tasks. That is, our control action is a linear map of the current states alone. No neural networks are used, and yet state-of-the-art performance is still uniformly achieved. For example, for the Humanoid model ARS finds linear policies which achieve average rewards of over $11500$, the highest reward reported in the literature.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

To put ARS on equal footing with competing methods, we evaluated its required sample complexity to solve the MuJoCo locomotion tasks over three random seeds, uniformly sampled from an interval. We compare the measured performance of our method with results reported by Haarnoja et al., Rajeswaran et al., Salimans et al., and Schulman et al.. ARS matches or exceeds state-of-the-art sample efficiency on the MuJoCo locomotion tasks.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Section 4.4 we report the time and computational resources required by ARS to train policies for the Humanoid-v1 task. We measure the time required to reach an average reward of $6000$ or more, and our results are reported over a hundred random seeds. On one machine with $48$ CPUs, ARS takes at most $13$ minutes on $25/100$ random seeds, and takes at most $21$ minutes on $50/100$ random seeds. Training policies for the Humanoid-v1 task to reach the same reward threshold takes about a day on modern hardware with the popular Trust Region Policy Optimization (TRPO) method, and takes around $10$ minutes with ES when parallelized over $1440$ CPUs. Therefore, our method is at least $15$ times more computationally efficient than ES, the fastest competing method.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Since our method is more efficient than previous approaches, we are able to explore the variance of our method over many random seeds. RL algorithms exhibit large training variances and hence evaluations over a small number of random seeds do not accurately capture their performance. Henderson et al. and Islam et al. have already discussed the importance of measuring the performance of RL algorithms over many random seeds, and the sensitivity of RL methods to choices of hyperparameters. For a more thorough evaluation of our method, we measured performance of ARS over a hundred random seeds and also evaluated its sensitivity to hyperparameter choices. Though ARS successfully trains policies for the MuJoCo locomotion tasks a large fraction of the time when hyperparameters and random seeds are varied, we note that it still exhibits a large variance, and that we still frequently find that learned policies do not uniformly yield high rewards.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

In order to simplify and streamline the evaluation of RL for continuous control, we argue that it is important to add more baselines that are extensible and reproducible. In Section 4.3 we argue for using the Linear Quadratic Regulator (LQR) with unknown dynamics as such a benchmark. We evaluate the performance of ARS, over a hundred random seeds, on a difficult instance of this problem. Although not as sample efficient as model-based methods, ARS finds nearly optimal solutions for the LQR instance considered.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem setup", "weight": 1.0} -->

Solving problems in reinforcement learning requires finding policies for controlling dynamical systems with the goal of maximizing average reward on given tasks. Such problems can be abstractly formulated as where $\theta \in {\mathbb{R}}^{n}$ parametrizes a policy $\pi_{\theta}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{p}}$. The random variable $\xi$ encodes the randomness of the environment, i.e., random initial states and stochastic transitions. The value $r{(\pi_{\theta},\xi)}$ is the reward achieved by the policy $\pi_{\theta}$ on one trajectory generated from the system. In general one could use stochastic policies $\pi_{\theta}$, but our proposed method uses deterministic policies.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Basic random search", "weight": 1.0} -->

Note that the problem formulation aims to optimize reward by directly optimizing over the policy parameters $\theta$. We consider methods which explore in the parameter space rather than the action space. This choice renders RL training equivalent to derivative-free optimization with noisy function evaluations. One of the simplest and oldest optimization methods for derivative-free optimization is *random search*. Random search chooses a direction uniformly at random on the sphere in parameter space, and then optimizes the function along this direction.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Basic random search", "weight": 1.0} -->

A primitive form of random search simply computes a finite difference approximation along the random direction and then takes a step along this direction without using a line search. Our method ARS, described in Section 3, is based precisely on this simple strategy. For updating the parameters $\theta$ of a policy $\pi_{\theta}$, our method exploits update directions of the form: for two i.i.d. random variables $\xi_{1}$ and $\xi_{2}$, $\nu$ a positive real number, and $\delta$ a zero mean Gaussian vector. It is known that such an update increment is an unbiased estimator of the gradient with respect to $\theta$ of ${\mathbb{E}}_{\delta}{\mathbb{E}}_{\xi}\left\lbrack {r{(\pi_{\theta + {\nu\delta}},\xi)}} \right\rbrack$, a smoothed version of the objective which is close to the original objective when $\nu$ is small.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Basic random search", "weight": 1.0} -->

When the function evaluations are noisy, minibatches can be used to reduce the variance in this gradient estimate. The basic random search (BRS) algorithm is outlined in Algorithm 1. Evolution Strategies is version of this algorithm with several complicated algorithmic enhancements. BRS is called Bandit Gradient Descent by Flaxman et al.. We note the many names for this algorithm, as it is at least 50 years old and has been rediscovered by a variety of different optimization communities.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Basic random search", "weight": 1.0} -->

1:Hyperparameters: step-size α, number of directions sampled per iteration N, standard deviation of the exploration noise ν 3:while ending condition not satisfied do 4: Sample δ1, δ2, …, δN of the same size as θj, with i.i.d. standard normal entries. 5: Collect 2 N rollouts of horizon H and their corresponding rewards using the policies 6: Make the update step: ${\theta_{j + 1} = {\theta_{j} + {\frac{\alpha}{N}{\sum\limits_{k = 1}^{N}{\left\lbrack {{r{(\pi_{j,k, +})}} - {r{(\pi_{j,k, -})}}} \right\rbrack\delta_{k}}}}}}.$ Algorithm 1 Basic Random Search (BRS)

<!-- chunk {"id": "body-0019", "role": "body", "section": "An oracle model for RL", "weight": 1.0} -->

We introduce and oracle model for RL to quantify the information about the system used by many RL methods. An RL algorithm can query the oracle by sending it a proposed policy $\pi_{\theta}$. Then, the oracle samples a random variable $\xi$, independent from the past, and generates a trajectory from the system according to the policy $\pi_{\theta}$ and the randomness $\xi$. Then, the oracle returns to the RL algorithm a sequence of states, actions, and rewards ${\{{(s_{t},a_{t},r_{t})}\}}_{t = 0}^{H - 1}$ which represent a trajectory generated from the system according to the policy $\pi_{\theta}$. One query is called an episode or a rollout. The goal of RL algorithms is to approximately solve problem by making as few calls to the oracle as possible. The number of oracle queries needed for solving problem is called *oracle complexity* or *sample complexity*. Note that both policy gradient methods and finite difference methods can be implemented under this oracle model.

<!-- chunk {"id": "body-0020", "role": "body", "section": "An oracle model for RL", "weight": 1.0} -->

Both approaches access the same information about the system: rollouts from fixed policies, and the associated states and rewards. The question then is whether one approach is making better use of this information than the other?

<!-- chunk {"id": "body-0021", "role": "body", "section": "Our proposed algorithm", "weight": 1.0} -->

We now introduce three augmentations of BRS that build on successful heuristics employed in deep reinforcement learning. Throughout the rest of the paper we use $M$ to denote the parameters of policies because our method uses linear policies, and hence $M$ is a $p \times n$ matrix.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Our proposed algorithm", "weight": 1.0} -->

The first version of our method, ARS V1, is obtained from BRS by scaling its update steps by the standard deviation of the rewards collected at each iteration (see Line 6 of Algorithm 1). We motivate this scaling and offer intuition in Section 3.1. As shown in Section 4.2, ARS V1 can train linear policies, which achieve the reward thresholds previously proposed in the literature, for the Swimmer-v1, Hopper-v1, HalfCheetah-v1, Walker2d-v1, and Ant-v1 tasks.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Our proposed algorithm", "weight": 1.0} -->

However, ARS V1 requires a larger number of episodes for training policies for these tasks, and it cannot train policies for the Humanoid-v1 task. To address these issues, in Algorithm 2 we also propose ARS V2. ARS V2 trains policies which are linear maps of states normalized by a mean and standard deviation computed online. We explain further this procedure in Section 3.2.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Our proposed algorithm", "weight": 1.0} -->

To further enhance the performance of ARS V1 and ARS V2, we introduce a third algorithmic enhancement, shown in Algorithm 2 as ARS V1-t and ARS V2-t. These versions of ARS can drop perturbation directions that yield the least improvement of the reward. We motivate this algorithmic element in Section 3.3.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Our proposed algorithm", "weight": 1.0} -->

1:Hyperparameters: step-size α, number of directions sampled per iteration N, standard deviation of the exploration noise ν, number of top-performing directions to use b (b < N is allowed only for V1-t and V2-t) 3:while ending condition not satisfied do 4: Sample δ1, δ2, …, δN in ℝp × n with i.i.d. standard normal entries.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Our proposed algorithm", "weight": 1.0} -->

(πj, k, −)}, denote by δ(k) the k-th largest direction, and by πj, (k), + and πj, (k), − the corresponding policies.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Our proposed algorithm", "weight": 1.0} -->

7: Make the update step: ${M_{j + 1} = {M_{j} + {\frac{\alpha}{b\sigma_{R}}{\sum\limits_{k = 1}^{b}{\left\lbrack {{r{(\pi_{j,{(k)}, +})}} - {r{(\pi_{j,{(k)}, -})}}} \right\rbrack\delta_{(k)}}}}}},$ where σR is the standard deviation of the 2 b rewards used in the update step. 8: V2: Set μj + 1, Σj + 1 to be the mean and covariance of the 2 N H (j + 1) states encountered from the start of training.222Of course, we implement this in an efficient way that does not require the storage of all the states.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Our proposed algorithm", "weight": 1.0} -->

Also, we only keep track of the diagonal of Σj + 1. Finally, to ensure that the ratio 0/0 is treated as 0, if a diagonal entry of Σj is smaller than 10−8 we make it equal to +∞. Algorithm 2 Augmented Random Search (ARS): four versions V1, V1-t, V2 and V2-t

<!-- chunk {"id": "body-0029", "role": "body", "section": "Scaling by the standard deviation $\\sigma_{R}$", "weight": 1.0} -->

As the training of policies progresses, random search in the parameter space of policies can lead to large variations in the rewards observed across iterations. As a result, it is difficult to choose a fixed step-size $\alpha$ which does not allow harmful changes between large and small steps. Salimans et al. address this issue by transforming the rewards into rankings and then using the adaptive optimization algorithm Adam for computing the update step. Both of these techniques change the direction of the updates, obfuscating the behavior of the algorithm and making it difficult to ascertain the objective Evolution Strategies is actually optimizing.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Scaling by the standard deviation $\\sigma_{R}$", "weight": 1.0} -->

To address the large variations of the differences ${r{(\pi_{M + {\nu\delta}})}} - {r{(\pi_{M - {\nu\delta}})}}$, we scale the update steps by the standard deviation $\sigma_{R}$ of the $2N$ rewards collected at each iteration (see Line 7 of Algorithm 2). To understand the effect of scaling by $\sigma_{R}$, we plot standard deviations $\sigma_{R}$ obtained during training a policy for the Humanoid-v1 model in Figure 1. The standard deviations $\sigma_{R}$ have an increasing trend as training progresses. This behavior occurs because perturbations of the policy weights at high rewards can cause Humanoid-v1 to fall early, yielding large variations in the rewards collected. Therefore, without scaling by $\sigma_{R}$, our method at iteration $300$ would be taking steps which are a thousand times larger than in the beginning of training. The same effect of scaling by $\sigma_{R}$ could probably be obtained by tuning a step-size schedule.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Scaling by the standard deviation $\\sigma_{R}$", "weight": 1.0} -->

However, our goal was to minimize the amount of tuning required, and thus we opted for the scaling by the standard deviation.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Normalization of the states", "weight": 1.0} -->

The normalization of states used by V2 is akin to data whitening used in regression tasks, and intuitively it ensures that policies put equal weight on the different components of the states. To gain intuition for why this might help, suppose that a state coordinate only takes values in the range $\lbrack 90,100\rbrack$ while another state component takes values in the range $\lbrack{- 1},1\rbrack$. Then, small changes in the control gain with respect to the first state coordinate would lead to larger changes in the actions then the same sized changes with respect to the second state component. Hence, whitening allows the isotropic exploration of random search to have equal influence over the various state components.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Normalization of the states", "weight": 1.0} -->

Previous work has also implemented such state normalization for fitting a neural network model for several MuJoCo environments. A similar normalization is used by ES as part of the virtual batch normalization of the neural network policies.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Normalization of the states", "weight": 1.0} -->

In the case of ARS, the state normalization can be seen as a form of non-isotropic exploration in the parameter space of linear policies. In particular, for policy weights $M$ and a perturbation direction $\delta$ we have where $\overset{\sim}{M} = M\operatorname{diag}{(\Sigma)}^{- {1/2}}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Normalization of the states", "weight": 1.0} -->

The main empirical motivation for version 2 of our method comes from the Humanoid-v1 task. We were not able to train a linear policy for this task without the normalization of the states described in Algorithm 2. Moreover, the measured sample complexity of ARS V2 is better on the other MuJoCo locomotion tasks as well, as shown in Section 4.2. On the other hand, we note that ARS V2 is impractical for the Linear Quadratic Regulator problem, discussed in Section 4.3, because the size of the states grows exponentially fast as a function of the trajectory length when the policy does not stabilize the system.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Using top performing directions", "weight": 1.0} -->

In Section 4.2 we show that ARS V2 matches or exceeds state-of-the-art performance on the tasks Swimmer-v1, Hopper-v1, HalfCheetah-v1 and Humanoid-v1. However, for training the Walker2d-v1 and Ant-v1 models, ARS V2 requires two to three times more rollouts than competing methods.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Using top performing directions", "weight": 1.0} -->

To improve the performance of ARS V1 and V2 we propose ARS V1-t and V2-t. In the update steps used by ARS V1 and V2 each perturbation direction $\delta$ is weighted by the difference of the rewards $r{(\pi_{j,k, +})}$ and $r{(\pi_{j,k, -})}$. These two rewards are the obtained from two queries to the oracle described in Section 2, using the policies If ${r{(\pi_{j,k, +})}} > {r{(\pi_{j,k, -})}}$, the update steps of ARS V1 and V2 push the policy weights $M_{j}$ in the direction of $\delta_{k}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Using top performing directions", "weight": 1.0} -->

If ${r{(\pi_{j,k, +})}} < {r{(\pi_{j,k, -})}}$, the update steps of ARS V1 and V2 push the policy weights $M_{j}$ in the direction of $- \delta_{k}$. However, since $r{(\pi_{j,k, +})}$ and $r{(\pi_{j,k, -})}$ are noisy evaluations of the performance of the policies parametrized by $M_{j} + {\nu\delta_{k}}$ and $M_{j} - {\nu\delta_{k}}$, ARS V1 and V2 might push the weights $M_{j}$ in the direction $\delta_{k}$ even when $- \delta_{k}$ is better, or vice versa.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Using top performing directions", "weight": 1.0} -->

Moreover, there can be perturbation directions $\delta_{k}$ such that updating the policy weights $M_{j}$ in either the direction $\delta_{k}$ or $- \delta_{k}$ would lead to sub-optimal performance.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Using top performing directions", "weight": 1.0} -->

For example, the rewards $r{(\pi_{j,k, +})}$ and $r{(\pi_{j,k, -})}$ being both small compared to other observed rewards might suggest that moving $M_{j}$ in either the direction $\delta_{k}$ or $- \delta_{k}$ would decrease the average reward. To address these issues, in ARS V1-t and V2-t we propose to order decreasingly the perturbation directions $\delta_{k}$, according to $\max{\{{r{(\pi_{j,k, +})}},{r{(\pi_{j,k, -})}}\}}$, and then use only the top $b$ directions for updating the policy weights (see Line 7 of Algorithm 2).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Using top performing directions", "weight": 1.0} -->

This algorithmic enhancement intuitively improves the update steps of ARS because with it the update steps are an average over directions that obtained high rewards. However, without theoretical investigation we cannot be certain of the effect of using this algorithmic enhancement (i.e. choosing $b < N$). When $b = N$ versions V1-t and V2-t are equivalent to versions V1 and V2. Therefore, it is certain that after tuning the hyperparameters of ARS V1-t and V2-t, they will not perform any worse than ARS V1 and V2. In Section 4.2 we show that ARS V2-t exceeds or matches state-of-the-art performance on all the MuJoCo locomotion tasks included in the OpenAI gym.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Comparison to Salimans et al", "weight": 1.0} -->

ARS simplifies the Evolution Strategies of Salimans et al. in several ways: ES feeds the gradient estimate into the Adam algorithm.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Comparison to Salimans et al", "weight": 1.0} -->

Instead of using the actual reward values $r{({\theta \pm {\sigma\epsilon_{i}}})}$, ES transforms the rewards into rankings and uses the ranks to compute update steps. The rankings are used to make training more robust. Instead, our method scales the update steps by the standard deviation of the rewards.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Comparison to Salimans et al", "weight": 1.0} -->

ES bins the action space of the Swimmer-v1 and Hopper-v1 to encourage exploration. Our method surpasses ES without such binning.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Comparison to Salimans et al", "weight": 1.0} -->

ES relies on policies parametrized by neural networks with virtual batch normalization, while we show that ARS achieves state-of-the-art performance with linear policies.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Implementation details", "weight": 1.0} -->

We implemented a parallel version of Algorithm 2 using the Python library Ray. To avoid the computational bottleneck of communicating perturbations $\delta$, we created a shared noise table which stores independent standard normal entries. Then, instead of communicating perturbations $\delta$, the workers communicate indices in the shared noise table. This approach has been used in the implementation of ES by Moritz et al. and is similar to the approach proposed by Salimans et al.. Our code sets the random seeds for the random generators of all the workers and for all copies of the OpenAI Gym environments held by the workers. All these random seeds are distinct and are a function of a single integer to which we refer as *the random seed*. Furthermore, we made sure that the states and rewards produced during the evaluation rollouts were not used in any form during training.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Results on the MuJoCo locomotion tasks", "weight": 1.0} -->

We evaluate the performance of ARS on the MuJoCo locomotion tasks included in the OpenAI Gym-v$0.9.3$. The OpenAI Gym provides benchmark reward functions for the different MuJoCo locomotion tasks. We used these default reward functions for evaluating the performance of the linear policies trained with ARS. The reported rewards obtained by a policy were averaged over $100$ independent rollouts.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Results on the MuJoCo locomotion tasks", "weight": 1.0} -->

For the Hopper-v1, Walker2d-v1, Ant-v1, and Humanoid-v1 tasks the default reward functions include a survival bonus, which rewards RL agents with a constant reward at each timestep, as long as a termination condition (i.e., falling over) has not been reached. For example, the environment Humanoid-v1 awards a reward of $5$ at each time steps, as long as the Humanoid model does not fall. Hence, if the Humanoid model stands still for $1000$ timesteps, it will receive a reward of $5000$ minus a small penalty for the actions used to maintain a vertical position. Furthermore, if the Humanoid falls forward at then end of a rollout, it will receive a reward higher than $5000$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Results on the MuJoCo locomotion tasks", "weight": 1.0} -->

It is common practice to report the sample complexity of an RL method by showing the number of episodes required to reach a reward threshold. For example, Gu et al. chose a threshold of $2500$, while Rajeswaran et al. chose a threshold of $5280$. However, given the survival bonus awarded to Humanoid-v1, we do not believe these reward thresholds are meaningful for locomotion. In Table 1 and Section 4.4 we use a reward threshold of $6000$ to evaluate the performance of ARS on the Humanoid-v1 task, the threshold also used by Salimans et al..

<!-- chunk {"id": "body-0050", "role": "body", "section": "Results on the MuJoCo locomotion tasks", "weight": 1.0} -->

The survival bonuses awarded by the OpenAI gym discourage the exploration of policies that cause falling early, which is needed for the discovery of policies that achieve locomotion. These bonuses cause ARS to find policies which make the MuJoCo models stand still for a thousand timesteps; policies which are likely local optima. These bonuses were probably included in the reward functions to help the training of stochastic policies since such policies cause constant movement through stochastic actions. To resolve the local optima problem for training deterministic policies, we subtracted the survival bonus from the rewards outputted by the OpenAI gym during training. For the evaluation of trained policies we used the default reward functions.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Results on the MuJoCo locomotion tasks", "weight": 1.0} -->

We first evaluated the performance of ARS on three random seeds after hyperparameter tuning. Evaluation on three random seeds is widely adopted in the literature and hence we wanted to put ARS on equal footing with competing methods. Then, we evaluated the performance of ARS on $100$ random seeds for a thorough estimation of performance. Finally, we also evaluated the sensitivity of our method to changes of the hyperparameters.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Three random seeds evaluation", "weight": 1.0} -->

We compared the different versions of ARS against the following methods: Trust Region Policy Optimization (TRPO), Deep Deterministic Policy Gradient (DDPG), Natural Gradients (NG), Evolution Strategies (ES), Proximal Policy Optimization (PPO), Soft Actor Critic (SAC), Soft Q-Learning (SQL), A2C, and the Cross Entropy Method (CEM). For the performance of these methods we used values reported by Rajeswaran et al., Salimans et al., Schulman et al., and Haarnoja et al..

<!-- chunk {"id": "body-0053", "role": "body", "section": "Three random seeds evaluation", "weight": 1.0} -->

Rajeswaran et al. and Schulman et al. evaluated the performance of RL algorithms on three random seeds, while Salimans et al. and Haarnoja et al. used six and five random seeds respectively. To all methods on equal footing, for the evaluation of ARS, we sampled three random seeds uniformly from the interval $\lbrack 0,1000)$ and fixed them. For each of the six popular MuJoCo locomotion tasks we chose a grid of hyperparameters^33^3Recall that ARS V1 and V2 take in only three hyperparameters: the step-size $\alpha$, the number of perturbation directions $N$, and scale of the perturbations $\nu$. ARS V1-t and V2-t take in an additional hyperparameter, the number of top directions used $b$ ($b \leq N$)., shown in Appendix A.2, and for each set of hyperarameters we ran ARS V1, V2, V1-t, and V2-t three times, once for each of the three fixed random seeds.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Three random seeds evaluation", "weight": 1.0} -->

Table 1 shows the average number of episodes required by ARS, NG, and TRPO to reach a prescribed reward threshold, using the values reported by Rajeswaran et al. for NG and TRPO. For each version of ARS and each MuJoCo task we chose the hyperparameters which minimize the average number of episodes required to reach the reward threshold. The corresponding training curves of ARS are shown in Figure 2. For all MuJoCo tasks, except Humanoid-v1, we used the same reward thresholds as Rajeswaran et al.. Our choice to increase the reward threshold for Humanoid-v1 is motivated by the presence of the survival bonuses, as discussed in Section 4.1.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Three random seeds evaluation", "weight": 1.0} -->

Average # episodes to reach reward threshold N/A 444N/A means that the method did not reach the reward threshold.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Three random seeds evaluation", "weight": 1.0} -->

UNK555UNK stands for unknown.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Three random seeds evaluation", "weight": 1.0} -->

Table 1 shows that ARS V1 can train policies for all the MuJoCo locomotion tasks except Humanoid-v1, which is successfully solved by ARS V2. Secondly, we note that ARS V2 reaches the prescribed thresholds for the Swimmer-v1, Hopper-v1, and HalfCheetah-v1 tasks faster than NG or TRPO, and matches the performance of NG on the Humanoid-v1 task. On the Walker2d-v1 and Ant-v1 tasks ARS V2 is outperformed by NG. Nonetheless, we note that ARS V2-t surpasses the performance of NG on these two tasks. Although TRPO hits the reward threshold for Walker2d-v1 faster than ARS, we will see that in other metrics ARS surpasses TRPO.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Three random seeds evaluation", "weight": 1.0} -->

Table 2 shows the maximum reward achieved by ARS^66^6We explain our methodology for computing this value for ARS in Appendix A.1., PPO, A2C, CEM, and TRPO after one million timesteps of the simulator have been collected, averaged over the three fixed random seeds. The hyperparameters were chosen based on the same evaluations performed for Table 1 and Figure 2. Schulman et al. did not report performance of PPO, A2C, CEM, and TRPO on the Ant-v1 and Humanoid-v1 tasks of the OpenAI gym. Table 2 shows that ARS surpasses these four methods on the Swimmer-v1, Hopper-v1, and HalfCheetah-v1 tasks. On the Walker2d-v1 task PPO achieves a higher average maximum reward than ARS, while ARS achieves a similar maximum reward to A2C, CEM, and TRPO.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Three random seeds evaluation", "weight": 1.0} -->

Maximum average reward after # timesteps

<!-- chunk {"id": "body-0060", "role": "body", "section": "timesteps", "weight": 1.0} -->

Table 3 shows the maximum reward achieved by ARS, SAC, DDPG, SQL, and TRPO after a prescribed number of simulator timesteps have been collected. The hyperparameters for ARS were chosen based on the same evaluations performed for Table 1 and Figure 2. Table 3 shows that ARS surpasses SAC, DDPG, SQL, and TRPO on the Hopper-v1 and Walker2d-v1 tasks, and that ARS is surpassed by SAC, DDPG, and SQL on the HalfCheetah-v1 taks. However, ARS performs better than TRPO on this task. On the Ant-v1 task, ARS is surpassed by SAC and performs similarly to SQL, but it outperforms DDPG and TRPO. We did not include values for Swimmer-v1 and Humanoid-v1 because Haarnoja et al. did not use the OpenAI versions of these tasks for evaluation. Instead, they evaluated SAC on the rllab version of these tasks.

<!-- chunk {"id": "body-0061", "role": "body", "section": "timesteps", "weight": 1.0} -->

The authors indicated that Humanoid-v1 is more challenging for SAC than the rllab version because of the parametrization of the states used by the OpenAI gym, and that Swimmer-v1 is more challenging because of the reward function used.

<!-- chunk {"id": "body-0062", "role": "body", "section": "timesteps", "weight": 1.0} -->

Maximum average reward after # timesteps

<!-- chunk {"id": "body-0063", "role": "body", "section": "timesteps", "weight": 1.0} -->

Table 4 shows the number of timesteps required by ARS to reach a prescribed reward threshold, averaged over the three fixed random seeds. The hyperparameters were chosen based on the same evaluations performed for Table 1 and Figure 2. We compare ARS to ES and TRPO. For these two methods we show the values reported by Salimans et al., who used six random seeds for evaluation. Salimans et al. do not report sample complexity results for the Ant-v1 and Humanoid-v1 tasks. Table 4 shows that TRPO requires fewer timesteps than ARS to reach the prescribed reward threshold on Walker2d-v1. However, we see that ARS requires fewer timesteps than ES and TRPO on the Swimmer-v1, Hopper-v1, and HalfCheetah-v1 tasks.

<!-- chunk {"id": "body-0064", "role": "body", "section": "A hundred seeds evaluation", "weight": 1.0} -->

Evaluating ARS on three random seeds shows that overall our method is more sample efficient than the NG, ES, DDPG, PPO, SAC, SQL, A2C, CEM, and TRPO methods on the MuJoCo locomotion tasks. However, it is well known that RL algorithms exhibit high training variance.

<!-- chunk {"id": "body-0065", "role": "body", "section": "A hundred seeds evaluation", "weight": 1.0} -->

For a thorough evaluation, we sampled $100$ distinct random seeds uniformly at random from the interval $\lbrack 0,10000)$. Then, using the hyperparameters selected for Table 1 and Figure 2, we ran ARS for each of the six MuJoCo locomotion tasks and the $100$ random seeds. Such a thorough evaluation was feasible only because ARS has a small computational footprint, as discussed in Section 4.4.

<!-- chunk {"id": "body-0066", "role": "body", "section": "A hundred seeds evaluation", "weight": 1.0} -->

The results are shown in Figure 3. Figure 3 shows that $70\%$ of the time ARS trains policies for all the MuJoCo locomotion tasks, with the exception of Walker2d-v1 for which it succeeds only $20\%$ of the time. Moreover, ARS succeeds at training policies a large fraction of the time while using a competitive number of episodes.

<!-- chunk {"id": "body-0067", "role": "body", "section": "A hundred seeds evaluation", "weight": 1.0} -->

Average reward evaluated over 100 random seeds, shown by percentile Figure 3: An evaluation of ARS over 100 random seeds on the MuJoCo locomotion tasks. The dotted lines represent median rewards and the shaded regions represent percentiles. For Swimmer-v1 we used ARS V1. For Hopper-v1, Walker2d-v1, and Ant-v1 we used ARS V2-t. For HalfCheetah-v1 and Humanoid-v1 we used ARS V2.

<!-- chunk {"id": "body-0068", "role": "body", "section": "A hundred seeds evaluation", "weight": 1.0} -->

There are two types of random seeds that are used in Figure 3 and that cause ARS to not reach high rewards. There are random seeds on which ARS eventually finds high reward policies if sufficiently many iterations of ARS are performed, and there are random seeds which lead ARS to discover locally optimal behaviors. For the Humanoid model, ARS found numerous distinct gait, including ones during which the Humanoid hopes only in one leg, walks backwards, or moves in a swirling motion. Such gaits were found by ARS on the random seeds which cause slower training. While multiple gaits for Humanoid models have been previously observed, our evaluation better emphasizes their prevalence. These results further emphasize the importance of evaluating RL algorithms on many random seeds since evaluations on small numbers of seeds cannot correctly capture the ability of algorithms to find good solutions for highly non-convex optimization problems.

<!-- chunk {"id": "body-0069", "role": "body", "section": "A hundred seeds evaluation", "weight": 1.0} -->

Finally, Figure 3 shows that ARS is the least sensitive to the random seed used when applied to the HalfCheetah-v1 problem. While SAC achieved a higher reward than ARS on this task, Haarnoja et al. evaluated the sensitivity of SAC to random seeds only on HalfCheetah-v1.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Sensitivity to hyperparameters", "weight": 1.0} -->

It has been correctly noted in the literature that RL methods should not be sensitive to hyperparameter choices if one hopes to apply them in practice. For example, DDPG is known to be highly sensitive to hyperparameter choices, making it difficult to use in practice. In the evaluations of ARS presented above we used hyperparameters chosen by tuning over the three fixed random seeds. To determine the sensitivity of ARS to the choice of hyperarameters, in Figure 4 we plot the median performance of all the hyperparameters considered for tuning over the three fixed random seeds. Recall that the grids of hyperparameters used for the different MuJoCo tasks are shown in Appendix A.2.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Sensitivity to hyperparameters", "weight": 1.0} -->

Interestingly, the success rates of ARS depicted in Figure 4 are similar to those shown in Figure 3. Figure 4 shows a decrease in median performance only for Ant-v1 and Humanoid-v1. The similarity between Figures 3 and 4 shows that the success of ARS is as influenced by the choice of hyperparameters as it is by the choice of random seeds. To put it another way, ARS is not highly sensitive to the choice of hyperparameters because its success rate when varying hyperarameters is similar to its success rate when performing independent trials with a "good" choice of hyperparameters. Finally, Figure 4 shows that the performance of ARS on the HalfCheetah-v1 task, a problem often used for evaluations of sensitivity, is the least sensitive to the choice of hyperparameter.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Sensitivity to hyperparameters", "weight": 1.0} -->

Evaluation of sensitivity to hyperparameters, shown by percentile Figure 4: An evaluation of the sensitivity of ARS to the choice of hyperparameters. The dotted lines represent median average reward and the shaded regions represent percentiles. We used all the learning curves collected during the hyperparameter tuning performed for the evaluation over the three fixed random seeds. For Swimmer-v1 we used ARS V1, and for the rest of the environments we used ARS V2-t (and implicitly V2 when b = N).

<!-- chunk {"id": "body-0073", "role": "body", "section": "Linear policies are sufficiently expressive for MuJoCo", "weight": 1.0} -->

For our evaluation on $100$ random seeds we discussed how linear policies can produce diverse gaits for the MuJoCo models, showing that linear policies are sufficiently expressive to capture diverse behaviors. Moreover, Table 5 shows that linear policies can achieve high rewards on all the MuJoCo locomotion tasks. In particular, for the Humanoid-v1 and Walker2d-v1 ARS found policies that achieve significantly higher rewards than any other results we encountered in the literature. These results show that linear policies are perfectly adequate for the MuJoCo locomotion tasks, reducing the need for more expressive and more computationally expensive policies.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Linear policies are sufficiently expressive for MuJoCo", "weight": 1.0} -->

Maximum reward achieved Table 5: Maximum average reward achieved by ARS, where we took the maximum over all sets of hyperparameters considered and the three fixed random seeds.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Linear quadratic regulator", "weight": 1.0} -->

While the MuJoCo locomotion tasks considered above are popular benchmarks in the RL literature, they have their shortcomings. The maximal achievable awards are unknown as are the optimal policies, and the current state-of-the-art may indeed be very suboptimal. These methods exhibit high variance making it difficult to distinguish quality of learned policies. And, since it is hard to generate new instances, the community may be overfitting to this small suite of tests.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Linear quadratic regulator", "weight": 1.0} -->

In this section we propose a simpler benchmark which obviates many of these shortcomings: the classical Linear Quadratic Regulator (LQR) with unknown dynamics. In control theory the LQR with known dynamics is a fundamental problem, which is thoroughly understood. In this problem the goal is to control a linear dynamical system while minimizing a quadratic cost. The problem is formalized in Eq.. The states $x_{t}$ lie in ${\mathbb{R}}^{n}$, the actions $u_{t}$ lie in ${\mathbb{R}}^{p}$, and the matrices $A$, $B$, $Q$, and $R$ are have the appropriate dimensions. The noise process $w_{t}$ is i.i.d. Guassian. When the dynamics $(A,B)$ are known, under mild conditions, problem admits an optimal policy of the form $u_{t} = {Kx_{t}}$ for some unique matrix $K$, computed efficiently from the solution of an algebraic Riccati equation.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Linear quadratic regulator", "weight": 1.0} -->

Moreover, the finite horizon version of problem 4 can be efficiently solved via dynamic programming.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Linear quadratic regulator", "weight": 1.0} -->

LQR with unknown dynamics is considerably less well understood and offers a fertile ground for new research. Note that it is still trivial to produce a varied set of instances for LQR, and we can always compare the best achievable cost when the dynamics are known.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Linear quadratic regulator", "weight": 1.0} -->

A natural model-based approach consists of estimating the transition matrices $(A,B)$ from data and then solving for $K$ by plugging the estimates in the Riccati equation. A controller $K$ computed in this fashion is called a *nominal controller*. Though this method may not be ideally robust (see, e.g., Dean et al. ), nominal control provide a useful baseline to which we can compare other methods.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Linear quadratic regulator", "weight": 1.0} -->

Consider the LQR instance defined introduced by Dean et al. as a challenging low-dimensional instance for LQR with unknown dynamics.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Linear quadratic regulator", "weight": 1.0} -->

The matrix $A$ has eigenvalues greater than $1$, and hence the system is unstable without some control. Moreover, if a method fails to recognize that the system is unstable, it may not yield a stable controller. In Figure 5 we compare ARS to nominal control and to a method using Q-functions fitted by temporal differencing (LSPI), analyzed by Tu and Recht.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Linear quadratic regulator", "weight": 1.0} -->

(a) A comparison of how frequently the controllers produced by ARS, the nominal synthesis procedure, and the LSPI method find stabilizing controllers. The frequencies are estimated from 100 trials.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Linear quadratic regulator", "weight": 1.0} -->

(b) A comparison of the relative cost of the controllers produced by ARS, the nominal synthesis procedure, and the LSPI method. The points along the dashed line denote the median cost, and the shaded region covers the 2-nd to 98-th percentile out of 100 trials.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Linear quadratic regulator", "weight": 1.0} -->

While Figure 5(b) shows ARS to require significantly more samples than LSPI to find a stabilizing controller, we note that LSPI requires an initial controller $K_{0}$ which stabilizes a discounted version of problem. ARS does not require a special initialization. However, Figure 5(b) also shows that the nominal control method is orders of magnitude more sample efficient than both LSPI and ARS. Hence there is much room for improvement for pure model-free approaches.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Linear quadratic regulator", "weight": 1.0} -->

We conjecture that the LQR instance would also be particularly challenging for policy gradient methods or other methods that explore in the action space. When the control signal is zero, the linear system described by Eq. has a small spectral radius ($\rho \approx 1.024$) and as a result the states $x_{t}$ would blow up, but slowly. Therefore long trajectories are required for evaluating the performance of a controller. However, the variance of policy gradient methods grows with the length of the trajectories used, even when standard variance reduction techniques are used.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Computational efficiency", "weight": 1.0} -->

The small computational footprint of linear policies and the embarrassingly parallel structure of ARS make our method ideal for training policies in a small amount of time, with few computational resources. In Tables 6 and 7 we show the wall-clock time required by ARS to reach an average reward of $6000$, evaluated over $100$ random seeds. ARS requires a median time of $21$ minutes to reach the prescribed reward threshold, when trained on one m5.24xlarge EC2 instance with $48$ CPUs. The Evolution Strategies method of Salimans et al. took a median time of $10$ minutes when evaluated over $7$ trials. However, the authors do not clarify what $7$ trails means, multiple trials with the same random seed or multiple trials with different random seeds. Moreover, Table 7 shows that ARS trains a policy in at most $10$ minutes on $10$ out of $100$ seeds. Also, Table 6 shows that ARS requires up to $15$ times less CPU time than ES.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Computational efficiency", "weight": 1.0} -->

Finally, we would like to point out that our method could be scaled to more workers. In that case, ARS V2 will have a computational bottleneck in the aggregation of the statistics $\Sigma_{j}$ and $\mu_{j}$ across workers. For successful training of policies, ARS V2 does not require the update of the statistics (see Line 2 of Algorithm 2) to occur at each iteration. For example, in their implementation of ES, Moritz et al. allowed each worker to have its own independent estimate of $\mu_{j}$ and $\Sigma_{j}$. With this choice, the authors used Ray to scale ES to $8192$ cores, reaching a $6000$ reward on Humanoid-v1 in $3.7$ minutes. One could tune an update schedule for the statistics $\Sigma_{j}$ and $\mu_{j}$ in order to reduce the communication time between workers or reduce the sample complexity of ARS. For the sake of simplicity we refrained from tuning such a schedule.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We attempted to find the simplest algorithm for model-free RL that performs well on the continuous control benchmarks used in the RL literature. We demonstrated that with a few algorithmic augmentations, basic random search could be used to train *linear* policies that achieve state-of-the-art sample efficiency on the MuJoCo locomotion tasks. We showed that linear policies match the performance of complex neural network policies and can be found through a simple algorithm. Since the algorithm and policies are simple, we were able to perform extensive sensitivity studies, and observed that our method can find good solutions to highly nonconvex problems a large fraction of the time. Up to the variance of RL algorithms, our method achieves state-of-the-art performance on the MuJoCo locomotion tasks when hyperparameters and random seeds are varied. Our results emphasize the high variance intrinsic to the training of policies for MuJoCo RL tasks. Therefore, it is not clear what is gained by evaluating RL algorithms on only a small numbers of random seeds, as is common in the RL literature. Evaluation on small numbers of random seeds does not capture performance adequately due to high variance.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our results point out some problems with the common methodology used for the evaluation of RL algorithms. Though many RL researchers are concerned about minimizing sample complexity, *it does not make sense to optimize the running time of an algorithm on a single instance.* The running time of an algorithm is only a meaningful notion if either (a) evaluated on a family of instances, or (b) when clearly restricting the class of algorithms.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Common RL practice, however, does not follow either (a) or (b). Instead researchers run algorithm $\mathcal{A}$ on task $\mathcal{T}$ with a given hyperparameter configuration, and plot a "learning curve" showing the algorithm reaches a target reward after collecting $X$ samples. Then the "sample complexity" of the method is reported as the number of samples required to reach a target reward threshold, with the given hyperparameter configuration. However, any number of hyperparameter configurations can be tried. Any number of algorithmic enhancements can be added or discarded and then tested in simulation. For a fair measurement of sample complexity, should we not count the number of rollouts used for every tested hyperparameters?

<!-- chunk {"id": "body-0091", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Let us look what would happen if the field of convex optimization relied exclusively on the same method of evaluation. Suppose we wanted to assess the performance of the stochastic gradient method at optimizing the objective ${G{(x)}} = {{\mathbb{E}}g{(x,\xi)}}$, where $g{( \cdot,\xi)}$ is a one dimensional function, strongly convex and smooth for all random variables $\xi$. Moreover, let us assume that for all $\xi$ the functions $g{( \cdot,\xi)}$ have the same minimizer. At each iteration the algorithm queries an oracle for a stochastic gradient. The oracle samples $\xi$ and returns to the algorithm the derivative $g'{(x,\xi)}$.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Then, according to the current RL methodology for evaluation, we fix a sequence of random variables $\xi$ sampled by the oracle by fixing a random seed and then proceed to tune the step-size of the stochastic gradient method. Since for each step-size the first random variable sampled by the oracle is the same, call it $\xi_{0}$, after $\mathcal{O}{({1/\epsilon})}$ tries we can determine a step-size which ensures reaching an $\epsilon$-close minimizer of $g{( \cdot,\xi)}$ after one iteration of the algorithm. Since all functions $g{( \cdot,\xi)}$ have the same minimizer, the point found after one iteration would be $\epsilon$-close to the minimizer of $G$. Hence, by using $\mathcal{O}{({1/\epsilon})}$ oracle calls behind the scene, we can elicit a step-size which optimizes the objective in one iteration.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Conclusion", "weight": 1.5} -->

However, we would not say that the sample complexity of the algorithm is one because the same algorithm would require more than one sample to optimize new objectives. A better measure of sample complexity would be the total number of samples required for tuning and the final optimization, which is $\mathcal{O}{({1/\epsilon})}$, but this methodology would also not capture the correct sample complexity of the algorithm. Indeed, we know the sample complexity of the stochastic gradient method for the optimization of objectives like $G$ is $\mathcal{O}{({\log{({1/\epsilon})}})}$.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Conclusion", "weight": 1.5} -->

RL tasks are not as simple as the one dimensional convex objective considered above, and RL methods are evaluated on more than one random seed. However, our arguments are just as relevant. Through optimal hyperparameter tuning one can artificially improve the perceived sample efficiency of a method. Indeed, this is what we see in our work. By adding a third algorithmic enhancement to basic random search (i.e., enhancing ARS V2 to V2-t), we are able to improve the sample efficiency of an already highly performing method. Considering that most of the prior work in RL uses algorithms with far more tunable parameters and neural nets whose architectures themselves are hyperparameters, the significance of the reported sample complexities for those methods is not clear. This issue is important because a meaningful sample complexity of an algorithm should inform us on the number of samples required to solve a new, previously unseen task. A simulation task should be thought of as an *instance* of a problem, not the problem itself.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In light of these issues and of our empirical results, we make several suggestions for future work: Simple baselines should be established before moving forward to more complex benchmarks and methods. Simpler algorithms are easier to evaluate empirically and understand theoretically. We propose that LQR is a reasonable baseline as this task is very well-understood when the model is known, instances can be generated with a variety of different levels of difficulty, and little overhead is required for replication.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Conclusion", "weight": 1.5} -->

When games and physics simulators are used for evaluation, separate problem instances should be used for tuning and evaluation of RL methods. Moreover, large numbers of random seeds should be used for statistically significant evaluations. However, since the distribution of problems occurring in games and physics simulators differs from the distribution of problems one hopes to solve, this methodology is not ideal either. In particular, it is difficult to say that one algorithm is better than another when evaluations are performed only in simulation since one of the algorithms might be exploiting particularities of the simulator used.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Rather than trying to develop algorithms which are applicable to many different classes of problems, it might be better to focus on specific problems of interest and find targeted solutions.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Conclusion", "weight": 1.5} -->

More emphasis should be put on the development of model-based methods. For many problems, such methods have been observed to require fewer samples than model-free methods. Moreover, the physics of the systems should inform the parametric classes of models used for different problems. Model-based methods incur many computational challenges themselves, and it is quite possible that tools from deep RL such as improved tree search can provide new paths forward for tasks that require the navigation of complex and uncertain environments.
