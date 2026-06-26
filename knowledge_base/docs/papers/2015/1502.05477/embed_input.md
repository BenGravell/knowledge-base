<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Trust Region Policy Optimization

Topics include Reinforcement learning, Policy optimization, Trust region methods, Continuous control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces TRPO, which guarantees monotonic policy improvement by constraining each update to a KL-divergence trust region. Enables stable training on complex continuous control tasks without manual learning rate tuning.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We describe an iterative procedure for optimizing policies, with guaranteed monotonic improvement. By making several approximations to the theoretically-justified procedure, we develop a practical algorithm, called Trust Region Policy Optimization (TRPO). This algorithm is similar to natural policy gradient methods and is effective for optimizing large nonlinear policies such as neural networks. Our experiments demonstrate its robust performance on a wide variety of tasks: learning simulated robotic swimming, hopping, and walking gaits; and playing Atari games using images of the screen as input. Despite its approximations that deviate from the theory, TRPO tends to give monotonic improvement, with little tuning of hyperparameters.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Most algorithms for policy optimization can be classified into three broad categories: policy iteration methods, which alternate between estimating the value function under the current policy and improving the policy; policy gradient methods, which use an estimator of the gradient of the expected return (total reward) obtained from sample trajectories (and which, as we later discuss, have a close connection to policy iteration); and derivative-free optimization methods, such as the cross-entropy method (CEM) and covariance matrix adaptation (CMA), which treat the return as a black box function to be optimized in terms of the policy parameters.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

General derivative-free stochastic optimization methods such as CEM and CMA are preferred on many problems, because they achieve good results while being simple to understand and implement. For example, while Tetris is a classic benchmark problem for approximate dynamic programming (ADP) methods, stochastic optimization methods are difficult to beat on this task. For continuous control problems, methods like CMA have been successful at learning control policies for challenging tasks like locomotion when provided with hand-engineered policy classes with low-dimensional parameterizations. The inability of ADP and gradient-based methods to consistently beat gradient-free random search is unsatisfying, since gradient-based optimization algorithms enjoy much better sample complexity guarantees than gradient-free methods. Continuous gradient-based optimization has been very successful at learning function approximators for supervised learning tasks with huge numbers of parameters, and extending their success to reinforcement learning would allow for efficient training of complex and powerful policies.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this article, we first prove that minimizing a certain surrogate objective function guarantees policy improvement with non-trivial step sizes. Then we make a series of approximations to the theoretically-justified algorithm, yielding a practical algorithm, which we call trust region policy optimization (TRPO). We describe two variants of this algorithm: first, the single-path method, which can be applied in the model-free setting; second, the vine method, which requires the system to be restored to particular states, which is typically only possible in simulation. These algorithms are scalable and can optimize nonlinear policies with tens of thousands of parameters, which have previously posed a major challenge for model-free policy search. In our experiments, we show that the same TRPO methods can learn complex policies for swimming, hopping, and walking, as well as playing Atari games directly from raw images.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Monotonic Improvement Guarantee for General Stochastic Policies", "weight": 1.0} -->

Equation 6, which applies to conservative policy iteration, implies that a policy update that improves the right-hand side is guaranteed to improve the true performance $\eta$. Our principal theoretical result is that the policy improvement bound in Equation 6 can be extended to general stochastic policies, rather than just mixture polices, by replacing $\alpha$ with a distance measure between $\pi$ and $\overset{\sim}{\pi}$, and changing the constant $\epsilon$ appropriately. Since mixture policies are rarely used in practice, this result is crucial for extending the improvement guarantee to practical problems. The particular distance measure we use is the total variation divergence, which is defined by ${D_{TV}{({p \parallel q})}} = {\frac{1}{2}{\sum_{i}{|{p_{i} - q_{i}}|}}}$ for discrete probability distributions $p,q$.^11^1Our result is straightforward to extend to continuous states and actions by replacing the sums with integrals.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Optimization of Parameterized Policies", "weight": 1.0} -->

In the previous section, we considered the policy optimization problem independently of the parameterization of $\pi$ and under the assumption that the policy can be evaluated at all states. We now describe how to derive a practical algorithm from these theoretical foundations, under finite sample counts and arbitrary parameterizations.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Optimization of Parameterized Policies", "weight": 1.0} -->

The preceding section showed that ${\eta{(\theta)}} \geq {{L_{\theta_{old}}{(\theta)}} - {CD_{KL}^{\max}{(\theta_{old},\theta)}}}$, with equality at $\theta = \theta_{old}$. Thus, by performing the following maximization, we are guaranteed to improve the true objective $\eta$: In practice, if we used the penalty coefficient $C$ recommended by the theory above, the step sizes would be very small. One way to take larger steps in a robust way is to use a constraint on the KL divergence between the new policy and the old policy, i.e., a trust region constraint: This problem imposes a constraint that the KL divergence is bounded at every point in the state space. While it is motivated by the theory, this problem is impractical to solve due to the large number of constraints.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Optimization of Parameterized Policies", "weight": 1.0} -->

Instead, we can use a heuristic approximation which considers the average KL divergence: We therefore propose solving the following optimization problem to generate a policy update: Similar policy updates have been proposed in prior work, and we compare our approach to prior methods in Section 7 and in the experiments in Section 8. Our experiments also show that this type of constrained update has similar empirical performance to the maximum KL divergence constraint in Equation.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Sample-Based Estimation of the Objective and Constraint", "weight": 1.0} -->

The previous section proposed a constrained optimization problem on the policy parameters (Equation ), which optimizes an estimate of the expected total reward $\eta$ subject to a constraint on the change in the policy at each update. This section describes how the objective and constraint functions can be approximated using Monte Carlo simulation.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Sample-Based Estimation of the Objective and Constraint", "weight": 1.0} -->

We seek to solve the following optimization problem, obtained by expanding $L_{\theta_{old}}$ in Equation: We first replace $\sum_{s}{\rho_{\theta_{old}}{(s)}\lbrack\ldots\rbrack}$ in the objective by the expectation $\frac{1}{1 - \gamma}{\mathbb{E}}_{s \sim \rho_{\theta_{old}}}\lbrack\ldots\rbrack$. Next, we replace the advantage values $A_{\theta_{old}}$ by the $Q$-values $Q_{\theta_{old}}$ in Equation, which only changes the objective by a constant. Last, we replace the sum over the actions by an importance sampling estimator.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Sample-Based Estimation of the Objective and Constraint", "weight": 1.0} -->

Using $q$ to denote the sampling distribution, the contribution of a single $s_{n}$ to the loss function is Our optimization problem in Equation 13 is exactly equivalent to the following one, written in terms of expectations: All that remains is to replace the expectations by sample averages and replace the $Q$ value by an empirical estimate. The following sections describe two different schemes for performing this estimation.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Sample-Based Estimation of the Objective and Constraint", "weight": 1.0} -->

The first sampling scheme, which we call single path, is the one that is typically used for policy gradient estimation, and is based on sampling individual trajectories. The second scheme, which we call vine, involves constructing a rollout set and then performing multiple actions from each state in the rollout set. This method has mostly been explored in the context of policy iteration methods.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Single Path", "weight": 1.0} -->

In this estimation procedure, we collect a sequence of states by sampling $s_{0} \sim \rho_{0}$ and then simulating the policy $\pi_{\theta_{old}}$ for some number of timesteps to generate a trajectory $s_{0},a_{0},s_{1},a_{1},\ldots,s_{T - 1},a_{T - 1},s_{T}$. Hence, ${q{(\left. a \middle| s \right.)}} = {\pi_{\theta_{old}}{(\left. a \middle| s \right.)}}$. $Q_{\theta_{old}}{(s,a)}$ is computed at each state-action pair $(s_{t},a_{t})$ by taking the discounted sum of future rewards along the trajectory.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Vine", "weight": 1.0} -->

In this estimation procedure, we first sample $s_{0} \sim \rho_{0}$ and simulate the policy $\pi_{\theta_{i}}$ to generate a number of trajectories. We then choose a subset of $N$ states along these trajectories, denoted $s_{1},s_{2},\ldots,s_{N}$, which we call the "rollout set". For each state $s_{n}$ in the rollout set, we sample $K$ actions according to $a_{n,k} \sim q{( \cdot |s_{n})}$. Any choice of $q{( \cdot |s_{n})}$ with a support that includes the support of $\pi_{\theta_{i}}{( \cdot |s_{n})}$ will produce a consistent estimator.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Vine", "weight": 1.0} -->

In practice, we found that $q{( \cdot |s_{n})} = \pi_{\theta_{i}}{( \cdot |s_{n})}$ works well on continuous problems, such as robotic locomotion, while the uniform distribution works well on discrete tasks, such as the Atari games, where it can sometimes achieve better exploration.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Vine", "weight": 1.0} -->

For each action $a_{n,k}$ sampled at each state $s_{n}$, we estimate ${\hat{Q}}_{\theta_{i}}{(s_{n},a_{n,k})}$ by performing a rollout (i.e., a short trajectory) starting with state $s_{n}$ and action $a_{n,k}$. We can greatly reduce the variance of the $Q$-value differences between rollouts by using the same random number sequence for the noise in each of the $K$ rollouts, i.e., common random numbers. See for additional discussion on Monte Carlo estimation of $Q$-values and for a discussion of common random numbers in reinforcement learning.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Vine", "weight": 1.0} -->

In small, finite action spaces, we can generate a rollout for every possible action from a given state. The contribution to $L_{\theta_{old}}$ from a single state $s_{n}$ is as follows: where the action space is $\mathcal{A} = \left\{ a_{1},a_{2},\ldots,a_{K} \right\}$. In large or continuous state spaces, we can construct an estimator of the surrogate objective using importance sampling. The self-normalized estimator (Owen, Chapter 9) of $L_{\theta_{old}}$ obtained at a single state $s_{n}$ is assuming that we performed $K$ actions $a_{n,1},a_{n,2},\ldots,a_{n,K}$ from state $s_{n}$. This self-normalized estimator removes the need to use a baseline for the $Q$-values (note that the gradient is unchanged by adding a constant to the $Q$-values).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Vine", "weight": 1.0} -->

Averaging over $s_{n} \sim {\rho{(\pi)}}$, we obtain an estimator for $L_{\theta_{old}}$, as well as its gradient.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Vine", "weight": 1.0} -->

The vine and single path methods are illustrated in Figure 1. We use the term vine, since the trajectories used for sampling can be likened to the stems of vines, which branch at various points (the rollout set) into several short offshoots (the rollout trajectories).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Vine", "weight": 1.0} -->

The benefit of the vine method over the single path method that is our local estimate of the objective has much lower variance given the same number of $Q$-value samples in the surrogate objective. That is, the vine method gives much better estimates of the advantage values. The downside of the vine method is that we must perform far more calls to the simulator for each of these advantage estimates. Furthermore, the vine method requires us to generate multiple trajectories from each state in the rollout set, which limits this algorithm to settings where the system can be reset to an arbitrary state. In contrast, the single path algorithm requires no state resets and can be directly implemented on a physical system.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Practical Algorithm", "weight": 1.0} -->

Here we present two practical policy optimization algorithm based on the ideas above, which use either the single path or vine sampling scheme from the preceding section. The algorithms repeatedly perform the following steps: Use the single path or vine procedures to collect a set of state-action pairs along with Monte Carlo estimates of their $Q$-values.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Practical Algorithm", "weight": 1.0} -->

By averaging over samples, construct the estimated objective and constraint in Equation 14.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Practical Algorithm", "weight": 1.0} -->

Approximately solve this constrained optimization problem to update the policy's parameter vector $\theta$. We use the conjugate gradient algorithm followed by a line search, which is altogether only slightly more expensive than computing the gradient itself. See Appendix C for details.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Practical Algorithm", "weight": 1.0} -->

a_{n} \middle| s_{n} \right.)}\frac{\partial}{\partial\theta_{j}}{\log\pi_{\theta}}{(\left. a_{n} \middle| s_{n} \right.)}}}$. The analytic estimator integrates over the action at each state $s_{n}$, and does not depend on the action $a_{n}$ that was sampled. As described in Appendix C, this analytic estimator has computational benefits in the large-scale setting, since it removes the need to store a dense Hessian or all policy gradients from a batch of trajectories. The rate of improvement in the policy is similar to the empirical FIM, as shown in the experiments.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Practical Algorithm", "weight": 1.0} -->

Let us briefly summarize the relationship between the theory from Section 3 and the practical algorithm we have described: The theory justifies optimizing a surrogate objective with a penalty on KL divergence. However, the large penalty coefficient $C$ leads to prohibitively small steps, so we would like to decrease this coefficient. Empirically, it is hard to robustly choose the penalty coefficient, so we use a hard constraint instead of a penalty, with parameter $\delta$ (the bound on KL divergence).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Practical Algorithm", "weight": 1.0} -->

The constraint on $D_{KL}^{\max}{(\theta_{old},\theta)}$ is hard for numerical optimization and estimation, so instead we constrain ${\overline{D}}_{KL}{(\theta_{old},\theta)}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Practical Algorithm", "weight": 1.0} -->

Our theory ignores estimation error for the advantage function. Kakade & Langford consider this error in their derivation, and the same arguments would hold in the setting of this paper, but we omit them for simplicity.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Connections with Prior Work", "weight": 1.0} -->

As mentioned in Section 4, our derivation results in a policy update that is related to several prior methods, providing a unifying perspective on a number of policy update schemes. The natural policy gradient can be obtained as a special case of the update in Equation by using a linear approximation to $L$ and a quadratic approximation to the ${\overline{D}}_{KL}$ constraint, resulting in the following problem: The update is $\left. \theta_{new} = \theta_{old} + \frac{1}{\lambda}A{(\theta_{old})}^{- 1}\nabla_{\theta}L{(\theta)} \middle|_{\theta = \theta_{old}} \right.$, where the stepsize $\frac{1}{\lambda}$ is typically treated as an algorithm parameter. This differs from our approach, which enforces the constraint at each update. Though this difference might seem subtle, our experiments demonstrate that it significantly improves the algorithm's performance on larger problems.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Connections with Prior Work", "weight": 1.0} -->

We can also obtain the standard policy gradient update by using an $\ell_{2}$ constraint or penalty: The policy iteration update can also be obtained by solving the unconstrained problem ${\operatorname{maximize}\limits_{\pi}L_{\pi_{old}}}{(\pi)}$, using $L$ as defined in Equation 3.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Connections with Prior Work", "weight": 1.0} -->

Several other methods employ an update similar to Equation. Relative entropy policy search (REPS) constrains the state-action marginals $p{(s,a)}$, while TRPO constrains the conditionals $p{(\left. a \middle| s \right.)}$. Unlike REPS, our approach does not require a costly nonlinear optimization in the inner loop. Levine and Abbeel also use a KL divergence constraint, but its purpose is to encourage the policy not to stray from regions where the estimated dynamics model is valid, while we do not attempt to estimate the system dynamics explicitly. Pirotta et al. also build on and generalize Kakade and Langford's results, and they derive different algorithms from the ones here.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

We designed our experiments to investigate the following questions: What are the performance characteristics of the single path and vine sampling procedures?

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments", "weight": 1.0} -->

TRPO is related to prior methods (e.g. natural policy gradient) but makes several changes, most notably by using a fixed KL divergence rather than a fixed penalty coefficient. How does this affect the performance of the algorithm?

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiments", "weight": 1.0} -->

Can TRPO be used to solve challenging large-scale problems? How does TRPO compare with other methods when applied to large-scale problems, with regard to final performance, computation time, and sample complexity?

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiments", "weight": 1.0} -->

To answer and, we compare the performance of the single path and vine variants of TRPO, several ablated variants, and a number of prior policy optimization algorithms. With regard to, we show that both the single path and vine algorithm can obtain high-quality locomotion controllers from scratch, which is considered to be a hard problem. We also show that these algorithms produce competitive results when learning policies for playing Atari games from images using convolutional neural networks with tens of thousands of parameters.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Simulated Robotic Locomotion", "weight": 1.0} -->

We conducted the robotic locomotion experiments using the MuJoCo simulator. The three simulated robots are shown in Figure 2. The states of the robots are their generalized positions and velocities, and the controls are joint torques. Underactuation, high dimensionality, and non-smooth dynamics due to contacts make these tasks very challenging. The following models are included in our evaluation: Swimmer. $10$-dimensional state space, linear reward for forward progress and a quadratic penalty on joint effort to produce the reward ${r{(x,u)}} = {v_{x} - {10^{- 5}{\| u\|}^{2}}}$. The swimmer can propel itself forward by making an undulating motion.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Simulated Robotic Locomotion", "weight": 1.0} -->

Hopper. $12$-dimensional state space, same reward as the swimmer, with a bonus of $+ 1$ for being in a non-terminal state. We ended the episodes when the hopper fell over, which was defined by thresholds on the torso height and angle.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Simulated Robotic Locomotion", "weight": 1.0} -->

Walker. $18$-dimensional state space. For the walker, we added a penalty for strong impacts of the feet against the ground to encourage a smooth walk rather than a hopping gait.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Simulated Robotic Locomotion", "weight": 1.0} -->

We used $\delta = 0.01$ for all experiments. See Table 2 in the Appendix for more details on the experimental setup and parameters used. We used neural networks to represent the policy, with the architecture shown in Figure 3, and further details provided in Appendix D. To establish a standard baseline, we also included the classic cart-pole balancing problem, based on the formulation from Barto et al., using a linear policy with six parameters that is easy to optimize with derivative-free black-box optimization methods.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Simulated Robotic Locomotion", "weight": 1.0} -->

The following algorithms were considered in the comparison: single path TRPO; vine TRPO; cross-entropy method (CEM), a gradient-free method; covariance matrix adaption (CMA), another gradient-free method; natural gradient, the classic natural policy gradient algorithm, which differs from single path by the use of a fixed penalty coefficient (Lagrange multiplier) instead of the KL divergence constraint; empirical FIM, identical to single path, except that the FIM is estimated using the covariance matrix of the gradients rather than the analytic estimate; max KL, which was only tractable on the cart-pole problem, and uses the maximum KL divergence in Equation, rather than the average divergence, allowing us to evaluate the quality of this approximation. The parameters used in the experiments are provided in Appendix E. For the natural gradient method, we swept through the possible values of the stepsize in factors of three, and took the best value according to the final performance.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Simulated Robotic Locomotion", "weight": 1.0} -->

Learning curves showing the total reward averaged across five runs of each algorithm are shown in Figure 4. Single path and vine TRPO solved all of the problems, yielding the best solutions. Natural gradient performed well on the two easier problems, but was unable to generate hopping and walking gaits that made forward progress. These results provide empirical evidence that constraining the KL divergence is a more robust way to choose step sizes and make fast, consistent progress, compared to using a fixed penalty. CEM and CMA are derivative-free algorithms, hence their sample complexity scales unfavorably with the number of parameters, and they performed poorly on the larger problems. The max KL method learned somewhat more slowly than our final method, due to the more restrictive form of the constraint, but overall the result suggests that the average KL divergence constraint has a similar effect as the theorecally justified maximum KL divergence. Videos of the policies learned by TRPO may be viewed on the project website: Note that TRPO learned all of the gaits with general-purpose policies and simple reward functions, using minimal prior knowledge.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Simulated Robotic Locomotion", "weight": 1.0} -->

This is in contrast with most prior methods for learning locomotion, which typically rely on hand-architected policy classes that explicitly encode notions of balance and stepping.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Simulated Robotic Locomotion", "weight": 1.0} -->

TRPO - single path Table 1: Performance comparison for vision-based RL algorithms on the Atari domain. Our algorithms (bottom rows) were run once on each task, with the same architecture and parameters. Performance varies substantially from run to run (with different random initializations of the policy), but we could not obtain error statistics due to time constraints.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Playing Games from Images", "weight": 1.0} -->

To evaluate TRPO on a partially observed task with complex observations, we trained policies for playing Atari games, using raw images as input. The games require learning a variety of behaviors, such as dodging bullets and hitting balls with paddles. Aside from the high dimensionality, challenging elements of these games include delayed rewards (no immediate penalty is incurred when a life is lost in Breakout or Space Invaders); complex sequences of behavior (Q\*bert requires a character to hop on $21$ different platforms); and non-stationary image statistics (Enduro involves a changing and flickering background).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Playing Games from Images", "weight": 1.0} -->

We tested our algorithms on the same seven games reported on in and, which are made available through the Arcade Learning Environment The images were preprocessed following the protocol in Mnih et al, and the policy was represented by the convolutional neural network shown in Figure 3, with two convolutional layers with $16$ channels and stride $2$, followed by one fully-connected layer with $20$ units, yielding 33,500 parameters.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Playing Games from Images", "weight": 1.0} -->

The results of the vine and single path algorithms are summarized in Table 1, which also includes an expert human performance and two recent methods: deep $Q$-learning, and a combination of Monte-Carlo Tree Search with supervised training, called UCC-I. The 500 iterations of our algorithm took about 30 hours (with slight variation between games) on a 16-core computer. While our method only outperformed the prior methods on some of the games, it consistently achieved reasonable scores. Unlike the prior methods, our approach was not designed specifically for this task. The ability to apply the same policy search method to methods as diverse as robotic locomotion and image-based game playing demonstrates the generality of TRPO.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Discussion", "weight": 1.5} -->

We proposed and analyzed trust region methods for optimizing stochastic control policies. We proved monotonic improvement for an algorithm that repeatedly optimizes a local approximation to the expected return of the policy with a KL divergence penalty, and we showed that an approximation to this method that incorporates a KL divergence constraint achieves good empirical results on a range of challenging policy learning tasks, outperforming prior methods. Our analysis also provides a perspective that unifies policy gradient and policy iteration methods, and shows them to be special limiting cases of an algorithm that optimizes a certain objective subject to a trust region constraint.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Discussion", "weight": 1.5} -->

In the domain of robotic locomotion, we successfully learned controllers for swimming, walking and hopping in a physics simulator, using general purpose neural networks and minimally informative rewards. To our knowledge, no prior work has learned controllers from scratch for all of these tasks, using a generic policy search method and non-engineered, general-purpose policy representations. In the game-playing domain, we learned convolutional neural network policies that used raw images as inputs. This requires optimizing extremely high-dimensional policies, and only two prior methods report successful results on this task.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Discussion", "weight": 1.5} -->

Since the method we proposed is scalable and has strong theoretical foundations, we hope that it will serve as a jumping-off point for future work on training large, rich function approximators for a range of challenging problems. At the intersection of the two experimental domains we explored, there is the possibility of learning robotic control policies that use vision and raw sensory data as input, providing a unified scheme for training robotic controllers that perform both perception and control. The use of more sophisticated policies, including recurrent policies with hidden state, could further make it possible to roll state estimation and control into the same policy in the partially-observed setting. By combining our method with model learning, it would also be possible to substantially reduce its sample complexity, making it applicable to real-world settings where samples are expensive.
