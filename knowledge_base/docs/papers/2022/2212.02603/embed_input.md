<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning to Optimize in Model Predictive Control

Topics include Imitation learning, Model predictive control, Predictive control, Robotics, Sampling-based methods, Control, Learning, Sampling, Machine learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Sampling-based Model Predictive Control (MPC) is a flexible control framework that can reason about non-smooth dynamics and cost functions. Recently, significant work has focused on the use of machine learning to improve the performance of MPC, often through learning or fine-tuning the dynamics or cost function. In contrast, we focus on learning to optimize more effectively. In other words, to improve the update rule within MPC. We show that this can be particularly useful in sampling-based MPC, where we often wish to minimize the number of samples for computational reasons. Unfortunately, the cost of computational efficiency is a reduction in performance; fewer samples results in noisier updates. We show that we can contend with this noise by learning how to update the control distribution more effectively and make better use of the few samples that we have. Our learned controllers are trained via imitation learning to mimic an expert which has access to substantially more samples. We test the efficacy of our approach on multiple simulated robotics tasks in sample-constrained regimes and demonstrate that our approach can outperform a MPC controller with the same number of samples.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Model Predictive Control (MPC) is a powerful, practical tool for solving sequential decision problems on real-world systems. MPC has been successfully used in a variety of tasks including autonomous helicopter aerobatics, aggressive off-road driving, manipulation, and humanoid robot locomotion. Recent work has shown that many popular MPC algorithms can be unified through the generic framework of dynamic mirror descent (DMD), a first-order online learning algorithm. This perspective provides an opportunity to improve performance of existing algorithms by drawing on powerful optimization techniques. Most modern approaches to optimization use fixed update rules tailored to specific classes of problems. Recently, research has explored *learning* to optimize, where the update rule is specified by a function approximator, such as a neural network, that can improve optimization performance with experience.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we leverage the optimization perspective of sampling-based MPC and adopt the learning-to-optimize framework in order to improve the update rule. This is in contrast to most existing learning-based approaches to MPC, which either focus on learning a good dynamics model, introducing a learned cost-shaping term into the objective, coupling MPC with a learned value function, or learning a good warm-start for MPC to refine. Other approaches have focused on performing MPC with a learned latent space of high-dimensional observations, low-level skills, or controls such that sampling because more efficient. Another promising avenue has explored differentiating through optimal controllers or planners to learn components of the optimization pipeline. These methods propose to learn or fine-tune the dynamics and cost functions of the controllers or parameters of differentiable planners end-to-end. Compared with these approaches, we fix the dynamics and cost function and instead focus on improving the optimization process.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

For many practical sampling-based MPC algorithms, the primary challenge is finding a good trade-off between speed and accuracy. Sampling-based MPC algorithms work by using simple policies to sample control sequences, which are used to roll out the dynamics function and compute a sample-based approximation of the gradient of the objective function. This approximate gradient is then used to update the sampling policy. Using complex dynamics and cost functions can make each rollout computationally expensive. To contend with this problem, one could use fewer samples to decrease computation, but this can increase the noise in the sample-based gradient, leading to poor performance.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, our objective is to *learn* how to more effectively update the control distribution with a small number of samples. To this end, we employ imitation learning to train fast, low-sample controllers to imitate an expert which makes use of additional samples. The learned optimizer is better able to integrate information in the sample-constrained regime. Our key contributions are that we: Leverage the gradient-based interpretation of many sampling-based MPC algorithms and show how to improve performance by learning a better update rule.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Propose to use structured sampling techniques to provide more information to the learned update than is contained in the noisy gradient, which enables us to make better use of fewer samples.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Empirically evaluate our proposed approach on multiple simulated robotics tasks, in which the learned optimizer has restricted access to samples.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our experiments show that the learned controller is indeed able to make better use of fewer samples while remaining competitive or outperforming the expert with the same number of samples. This illustrates the utility of the learning-to-optimize framework in the domain of control and indicates the potential to improve the viability of sampling-based MPC controllers on embedded platforms.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Model Predictive Control", "weight": 1.0} -->

We consider the problem of controlling a discrete-time stochastic dynamical system with states $x_{t} \in {\mathbb{R}}^{N}$ and controls $u_{t} \in {\mathbb{R}}^{M}$. The system chooses controls using a policy $\pi_{\theta_{t}}$ with parameters $\theta_{t} \in \Theta$, where $\Theta$ is the set of feasible parameters. After applying the control, the system incurs the instantaneous cost $c{(x_{t},u_{t})}$ and transitions to the next state $x_{t + 1}$ according to the dynamics where $f:{{{\mathbb{R}}^{N} \times {\mathbb{R}}^{M}}\rightarrow{\mathbb{R}}^{N}}$ is a stochastic transition map.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Model Predictive Control", "weight": 1.0} -->

Over a time horizon $H$, we sample a control sequence $U_{t} \triangleq {(u_{t},u_{t + 1},\ldots,u_{{t + H} - 1})}$, which results in a state trajectory $X_{t} \triangleq {(x_{t},x_{t + 1},\cdots,x_{t + H})}$. The total cost incurred is where $c_{term}{(\cdot)}$ is a terminal cost function.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Model Predictive Control", "weight": 1.0} -->

In general, we do not have access to the true dynamics function $f$ and instead approximate it with the model $\hat{f}$, corresponding to the surrogate statistic $\hat{J}{({\mathbf{π}}_{\mathbf{θ}};x_{t})}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Model Predictive Control", "weight": 1.0} -->

This optimization problem can only be approximated in practice due to real-time constraints. One commonly applied heuristic is to bootstrap the previous approximate solution as an initialization for the current problem. This is effective because the optimization problems between two consecutive time steps share all control variables except the first and last. If our solution from the previous problem is ${\mathbf{θ}}_{t - 1}$, then our warm start for the current problem is given by where $\Phi{(\cdot)}$ is called the shift operator. A common choice is ${\overset{\sim}{\mathbf{θ}}}_{t} = {(\theta_{t + 1},\theta_{t + 2},\ldots,\theta_{{t + H} - 1},\overline{\theta})}$, where $\overline{\theta}$ is a new parameter which reflects the expected final action.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-A Model Predictive Control", "weight": 1.0} -->

Recent work by Wagener et al. showed that many common MPC algorithms fall under the framework of an online learning algorithm known as dynamic mirror descent (DMD). Online learning involves interactions between a learner and an environment over $T$ rounds. In our case, the learner is the MPC algorithm, which in round $t$ plays the decision ${\overset{\sim}{\mathbf{θ}}}_{t} \in \mathbf{\Theta}$, the shifted policy parameter sequence, along with side information $u_{t - 1}$, the control applied to the real system. The per-round loss is defined as ${\ell_{t}{(\cdot)}} = {\hat{J}{(\cdot;x_{t})}}$, which is selected by the environment via the state transition.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-B Sampling-Based Model Predictive Control", "weight": 1.0} -->

A popular, practical sampling-based MPC algorithm is Model Predictive Path Integral (MPPI) control, which is a special case of DMD-MPC under certain choices of objective function, control distribution, and Bregman divergence. Specifically, we assume the policies are open loop and choose the exponential utility for the objective: where $\lambda > 0$ is a scaling parameter, also known as the temperature. Since we generally assume that the cost function is non-differentiable with respect to $\mathbf{θ}$, we instead compute the gradients via a likelihood-ratio derivative: We approximate these expectations with Monte Carlo sampling, which results in a convex combination of gradients: with weights $w_{i}$ defined by the softmax operation Because of this estimation, the gradients will be noisy, with noise that scales inversely with number of samples. The more samples we use, the more exact our approximations will be.

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-C Learning to Optimize Framework", "weight": 1.0} -->

Rather than hand design an update rule tailored to a specific subclass of problems, the learning-to-optimize approach aims to learn a sequential update rule from experience. For a set of optimizee parameters $\theta \in \Theta$ and objective function $\ell{(\theta)}$, we find the minimizer $\theta^{\ast} = {{{\arg\min}_{\theta \in \Theta}\ell}{(\theta)}}$ with an iterative algorithm that has the update rule where $m$ is the learned optimizer, which can be of any parameterized function class with parameters $\phi$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-C Learning to Optimize Framework", "weight": 1.0} -->

The majority of approaches to learning-to-optimize differentiate through the optimization process using gradient descent or use reinforcement learning. However, we do not assume that the optimization process is end-to-end differentiable and wish to avoid the high sample complexity that often hinders reinforcement learning. Instead, we opt to use imitation learning to train the optimizer. Chen et al. also make use of imitation learning, in which the experts are common hand-designed optimizers that have access to full gradient information. However, in our case, the learned optimizers only have access to noisier gradients than the expert demonstrator and therefore less information.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-C Learning to Optimize Framework", "weight": 1.0} -->

Another major difference from prior work is that most literature in this area targets optimizing deep neural networks. As such, they must contend with the large parameter space of these models. Andrychowicz et al. proposed to use a coordinate-wise optimizer, in which the parameters of the optimizer are shared across updates for all optimizee parameters. A downside to this approach is that it throws away potentially useful information for improving the learned update. Instead, since we have a moderate number of parameters, we can jointly optimize the entire planning horizon of control distribution parameters in order to capture relationships between time steps.

<!-- chunk {"id": "body-0019", "role": "body", "section": "III-A Design of the Learnable Optimzier", "weight": 1.0} -->

As shown in the previous section, the MPPI update rule in Equation 12 corresponds to performing mirror descent with an approximate gradient computed from $N$ samples. Fewer samples results in a worse approximation and, therefore, a noisier update. One possible avenue for improving performance would be to employ more advanced first-order methods. However, by adopting the learning-to-optimize framework and replacing the update rule with a learned optimizer, we can potentially do better than a manually specified update. A naive approach would be to follow Equation 13 and use the noisy gradient as input to the learned optimizer to produce the updated parameters. However, our objective is to learn how to mitigate the effect of a low number of samples on gradient noise, and the computation of the noisy gradient itself potentially throws away information that may be useful for improving the update. For instance, looking at Equation 12, we are simply computing a weighted sum of the samples. This collapses the information in each trajectory sample and its corresponding cost into a single vector. Therefore, we propose instead to use the individual components which form the gradient directly.

<!-- chunk {"id": "body-0020", "role": "body", "section": "III-A Design of the Learnable Optimzier", "weight": 1.0} -->

From Equation 12, we can see that the update is a function of the current mean ${\overset{\sim}{\mu}}_{t + h}$ and covariance ${\overset{\sim}{\Sigma}}_{t + h}$, sample weights $w_{t}^{({1:N})}$, and control samples $u_{t + h}^{({1:N})}$. The sample weights themselves are actually a function of the total trajectory costs $C_{t}^{({1:N})}$, where $C_{t} = {C{(X_{t},U_{t})}}$. One potential choice would be to make each of these terms an input to the learned update: A limitation of this choice of parameterization is that it assumes independence of the updates between time steps in the rollouts. While this is the case for vanilla MPPI, we could potentially learn a better update by incorporating information across time steps.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A Design of the Learnable Optimzier", "weight": 1.0} -->

However, if we parameterize the optimizer with a fully-connected or recurrent neural network architecture, this would result in a large number of parameters to learn, making optimization difficult. Instead, we alter the way in which we sample from the Gaussian policies to remedy this explosion in the dimensionality.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A Design of the Learnable Optimzier", "weight": 1.0} -->

As proposed by Bhardwaj et al., we make use of low-discrepancy Halton sequences to generate samples from the Gaussian policies. Normal pseudo-random sequences often result in clusters of sampled points, leaving many regions of the parameter space untouched. Low-discrepancy sequences are a deterministic alternative that alleviate this problem by correlating each point.

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A Design of the Learnable Optimzier", "weight": 1.0} -->

A $D$-dimensional Halton sequence $x_{1},x_{2},\ldots,x_{N}$, in which $x_{i} \in {\mathbb{R}}^{D}$ is generated by where $p_{1},\ldots,p_{D}$ are consecutive prime numbers and ${a_{j}{(p_{b})}} \in {\{ 0,1,\ldots,{p_{b} - 1}\}}$ such that the condition $i = {\sum_{j = 1}^{\infty}{a_{j}{(p_{b})}p_{b}^{j - 1}}}$ holds. The Halton sequence is sampled once at the beginning of the rollout and then transformed using the mean and covariance of the Gaussian policy. While this can improve the performance of sampling-based MPC, the main benefit is that it makes all sampled control sequences a deterministic function of the current mean and covariance.

<!-- chunk {"id": "body-0024", "role": "body", "section": "III-A Design of the Learnable Optimzier", "weight": 1.0} -->

Therefore, the sampled control sequences can be excluded from the learned update without loss of information.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-A Design of the Learnable Optimzier", "weight": 1.0} -->

As such, rather than optimizing each time step independently, we leverage the structured nature of these samples to learn an update that optimizes the entire trajectory jointly using only cost information. The resulting update is then where ${\mathbf{μ}}_{t} \triangleq {(\mu_{t},\mu_{t + 1},\ldots,\mu_{{t + H} - 1})}$, $\mathbf{\Sigma}_{t} \triangleq {(\Sigma_{t},\Sigma_{t + 1},\ldots,\Sigma_{{t + H} - 1})}$, and ${\overset{\sim}{\mathbf{μ}}}_{t}$ and ${\overset{\sim}{\mathbf{\Sigma}}}_{t}$ are defined similarly. We can think about the Halton sequence as giving us a sense of what the environment and cost landscape is like around the current state.

<!-- chunk {"id": "body-0026", "role": "body", "section": "III-A Design of the Learnable Optimzier", "weight": 1.0} -->

Since the learned optimizer can potentially make better use of its inputs than the expert, we may be able to more effectively use fewer samples while maintaining similar performance.

<!-- chunk {"id": "body-0027", "role": "body", "section": "III-A Design of the Learnable Optimzier", "weight": 1.0} -->

Finally, we note that Equation 12 is a convex combination of the previous control parameters and the weighted samples. We can actually think about MPC as a form of recurrent network, with the warm-started control distribution as our form of memory about the previous time steps. From this perspective, the step size is acting as a gating term which modulates how much information we preserve about our history. The hidden state update in a gated recurrent unit (GRU) is of the same form, except the multiplicative gating term is also learned. Inspired by this similarity, we use the following update: where $\odot$ is the Hadamard product. Here, $g_{t}^{\mu},g_{t}^{\sigma}$ are the learned gating terms, which are passed through a sigmoid to ensure they are between zero and one. Meanwhile, $h_{t}^{\mu},h_{t}^{\sigma}$ can be interpreted as the updates proposed by the network. In our experiments, this choice of parameterization significantly outperformed a simple fully-connected network.

<!-- chunk {"id": "body-0028", "role": "body", "section": "III-B Imitation Learning for Training the Optimizer", "weight": 1.0} -->

{\{{({\overset{\sim}{\mathbf{θ}}}_{1:T},C_{1:T}^{({1:M})},{\mathbf{θ}}_{1:T}^{expert})}\}}}$ Train optimizer parameters ϕ on 𝒟 Algorithm 1 DAgger Training Loop Unlike prior work in learning-to-optimize, we cannot assume that the optimization process itself is differentiable, as it occurs online via interactions with the environment.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-B Imitation Learning for Training the Optimizer", "weight": 1.0} -->

Even in the simulated case, we do not want to assume that everything has been implemented in a differentiable fashion. We could use reinforcement learning (RL), although it generally has high sample complexity and may be slow to learn. Since we have access to a tuned optimal controller, imitation learning is a promising direction for training the optimizer. Our expert is an MPPI controller with unrestricted access to samples. That is, we provide the controller with as many samples as needed to achieve good performance. The learner is also an MPPI controller, but it has access to fewer samples, and the standard update is replaced with the learned optimizer. In our preliminary experiments, we tried using standard behavioral cloning, in which we collect a dataset of expert demonstrations and train a policy offline via regression. However, this did not work well due to covariate shift between the expert and learner distributions. Instead, we used DAgger to perform imitation learning, which is an interactive algorithm that aims to combat issues of covariate shift. The algorithm queries an expert online for corrective labels on learner visited states. We outline the main loop of DAgger in Algorithm 1.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-B Imitation Learning for Training the Optimizer", "weight": 1.0} -->

Input: State x1, policy ${\mathbf{π}}_{{\overset{\sim}{\mathbf{θ}}}_{1}}$, probability βk Parameters: Rollout length T, expert samples N, learner samples M Output: Shifted parameters ${\overset{\sim}{\mathbf{θ}}}_{1:T}$, sample costs C1: T(1: M), expert decisions θ1: Te x p e r t Sample controls from policy ${\{ U_{t}^{(i)}\}}_{i = 1}^{N} \sim {\mathbf{π}}_{{\overset{\sim}{\mathbf{θ}}}_{t}}$ Sample Xt(i) from dynamics f̂ using Ut(i), xt Compute sample weights with Equation 9 Update ${\overset{\sim}{\mathbf{θ}}}_{t}$ to θte x p e r t using Equation 12 Update

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-B Imitation Learning for Training the Optimizer", "weight": 1.0} -->

${\overset{\sim}{\mathbf{θ}}}_{t}$ to θtl e a r n using Equation 17 Sample ut ∼ πθt or use mean ut ← μt Apply control to system xt + 1 ∼ f (xt, ut) Shift parameters ${\overset{\sim}{\mathbf{θ}}}_{t + 1} = {\Phi{({\mathbf{θ}}_{t})}}$ Algorithm 2 DAgger Rollout Function First, we begin by collecting a bootstrap dataset in which only the expert is run.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-B Imitation Learning for Training the Optimizer", "weight": 1.0} -->

Next, each iteration $k$ of DAgger, we run $R$ rollouts according to Algorithm 2 by sampling some initial state $x_{1}$ from a known initial state distribution $\rho$. During a rollout, at each time step, we apply the controls from the expert with probability $\beta_{k}$ and the learner with probability $1 - \beta_{k}$. The expert is always run in order to provide a corrective target for training the policy at the next iteration. Both the expert and learner controllers use the same trajectory samples, although the learner only receives a subset of them. Generally, the mixing probabilities $\beta_{k}$ are set according to a schedule such that we run the learner more often in later iterations. In our experiments, we set $\beta_{k} = p^{k}$ for some $p \in {}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-B Imitation Learning for Training the Optimizer", "weight": 1.0} -->

After running the rollouts, we collect the warm-started control distribution parameters ${\overset{\sim}{\mathbf{θ}}}_{1:T}$, the trajectory costs $C_{1:T}^{({1:M})}$, and the updated expert control distribution parameters ${\mathbf{θ}}_{1:T}^{expert}$ into a dataset $\mathcal{D}_{i}$. We only collect the $M \leq N$ samples used by the learner. This data is then aggregated into our main dataset $\mathcal{D}$ to train the optimizer.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments", "weight": 1.0} -->

Implementation Details. In all experiments, our MPPI implementation is a modified version of the one developed by Bhardwaj et al.. This implementation uses Halton sequences for generating control sequence samples and smooths the sampled trajectories with 3rd degree B-splines. We use a fixed diagonal covariance for the sampling distribution and do not perform covariance adaptation. All hyperparameters were tuned using a grid search, and the optimal number of samples is what the expert controller has access to during data generation and training. Now, the optimal choice of hyperparameters may be different for a given number of samples. Therefore, for a fair comparison, we tune the MPPI hyperparameters separately for each sample count used in our evaluation. Both MPPI and the neural networks are implemented in PyTorch.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiments", "weight": 1.0} -->

Task Details. We evaluate on simulated tasks: Cartpole: The task is to slide a cart along a rail to swing up the pole attached via an unactuated joint using only actuation from the cart. Both the expert and learner are given access to the true analytical dynamics. The initial position of the cart and pole are randomized at every episode, which lasts 200 time steps. An episode is considered successful if the pole is swung up with a linear and angular velocity near zero.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiments", "weight": 1.0} -->

Franka Reacher: A 7 degree-of-freedom (DOF) Franka Panda robot arm must reach a target goal from a fixed starting pose. The goal is randomly selected at the beginning of each episode. Both the expert and learner use the same kinematic model described in Bhardwaj et al., which is different from the true dynamics of the simulator (Nvidia's Isaac Gym ). Each episode lasts for 500 time steps and is considered successful if the end effector reaches the target position.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiments", "weight": 1.0} -->

Franka Obstacles: This task is identical to Franka Reacher, except now there are two spherical obstacles placed in the environment which the arm must avoid. The obstacle and the goal positions are randomized at the beginning of each episode, which lasts for 600 time steps. An episode is considered successful if the end effector reaches the goal while avoiding collisions.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experiments", "weight": 1.0} -->

Evaluation. We evaluate the performance of the learned optimizer by varying the number of samples, up to the amount used by the expert. For each sample amount, we compare against a standard MPPI implementation with access to the same number of samples as the learned controller over 30 test rollouts. All test rollouts use a fixed set of start states, goals, and obstacle locations. This is achieved by setting the random seed value to a pre-defined test seed. Our primary metric for comparison is success rate, which is defined as the percentage of times the task goal was achieved out of all trials. In the Franka Obstacles task, the placement of obstacles is randomized according to a pre-specified distribution. Therefore, this task allows us to evaluate the generalization capability of the learned optimizer to new environments which are drawn from a similar distribution. Additionally, we report statistics of the end effector test trajectories. Specifically, we compute a relative trajectory length and average jerk as the ratio between the statistics for the learned optimizer and baseline MPPI controller. The trajectory length is averaged over all test runs, while the jerk is averaged over only successful test runs.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experiments", "weight": 1.0} -->

Training Details. Prior work in learning-to-optimize made use of recurrent architectures which can account for the history of the gradients and optimization process. While we could potentially benefit from such an architecture, we found that a simple multi-layer perceptron (MLP) was sufficient to learn powerful optimizers. As such, in all experiments, the learned optimizer is represented with a two-layer MLP using ReLU activation functions. We use 1024, 2048, and 4096 hidden units per layer for the Cartpole, Franka Reacher, and Franka Obstacles tasks, respectively. To prevent overfitting, all networks are regularized with dropout using a dropout probability of 0.1. We use the Adam optimizer with a learning rate of $10^{- 3}$ for Cartpole and Franka Reacher and $10^{- 4}$ for Franka Obstacles. We normalize the total trajectory costs based on the mean and standard deviation of the training dataset. For all tasks, we bootstrapped the dataset with 1024 trajectories, in which only the expert's action was applied to the system.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experiments", "weight": 1.0} -->

We ran DAgger for 20 iterations with 128 rollouts per iteration and a mixing probability schedule $\beta_{k} = 0.8^{k}$. For each iteration, we train the networks on the aggregated dataset for 1000 epochs with a batch size of 8. The best performing network evaluated on a held-out validation set is saved and used in the next iteration of DAgger.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Results", "weight": 1.0} -->

We report the success rate for all tasks in Table I and refer to standard MPPI by MPPI and MPC with the learned optimizer by L2O-MPC. Success rate is computed for each task based on the criteria discussed in Section IV. For Franka Obstacles, not every randomly generated scenario is feasible. Hence, there is an upper-bound of an 80% success rate for both MPPI and L2O-MPC. We can see that the performance of MPPI quickly drops off as the number of control sequence samples is reduced. For Cartpole, the performance of L2O-MPC remains fairly consistent even with a lower number of samples. While the performance drop is more pronounced in the Franka experiments, L2O-MPC still consistently matches or outperforms MPPI at each sample amount. In Franka Reacher, L2O-MPC is able to withstand a $4 \times$ decrease in the number of samples while still achieving an $100\%$ success rate. Similarly, in Franka Obstacles, L2O-MPC only incurs a $4\%$ decrease in performance under an $8 \times$ decrease in number of samples.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Results", "weight": 1.0} -->

This illustrates that L2O-MPC is successfully able to generalize to new environments similar to those on which it was trained.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Samples", "weight": 1.0} -->

Qualitatively, the L2O-MPC trajectories appear to be slightly more jittery than the MPPI expert. In Table II, we provide the average relative jerk between L2O-MPC and MPPI for successful test runs at different sample counts. Indeed, we see that the L2O-MPC trajectories are less smooth than those of MPPI, and this effect is exacerbated at lower sample counts. Additionally, we provide the average relative trajectory length across all test environments. With more samples, L2O-MPC has slightly longer trajectories than MPPI, indicating that it is slower at reaching the goal. However, when given access to fewer samples, L2O-MPC consistently has shorter trajectories, as it more often reaches the goal. Therefore, while L2O-MPC is often jerkier and sometimes slower than the expert with full samples, it succeeds more often in achieving the desired objective in a timely fashion than MPPI given the same number of samples.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We presented a method for improving upon standard sampling-based MPC algorithms by learning a better update rule. This provides a novel way to incorporate learning into model-based control algorithms, which is orthogonal to the standard approaches of learning or fine-tuning the dynamics model and/or cost function. We contend with noisy gradients by learning how to more effectively update the control distribution. By using structured sampling strategies, we are able to provide more information to the learned update and better utilize fewer samples. We show through empirical evaluations that our learned controllers remain competitive or outperform a baseline MPPI controller with access to the same number of samples. This demonstrates the viability of the learning-to-optimize framework in the context of control, opening the door for a variety of techniques to be applied to improving the performance of optimization-based controllers and planners. While we leveraged imitation learning to train the optimizers, this is just one possible option and an interesting direction for future work is to explore using reinforcement learning to see if it can outperform the expert and model-free methods.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Since performance of sampling-based methods relies so heavily on thorough exploration of the sample space, another possible avenue is to learn how to generate better samples in addition to better updates.
