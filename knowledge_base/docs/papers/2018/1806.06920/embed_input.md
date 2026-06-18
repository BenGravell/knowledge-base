<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Maximum a Posteriori Policy Optimisation

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce a new algorithm for reinforcement learning called Maximum aposteriori Policy Optimisation (MPO) based on coordinate ascent on a relative entropy objective. We show that several existing methods can directly be related to our derivation. We develop two off-policy algorithms and demonstrate that they are competitive with the state-of-the-art in deep reinforcement learning. In particular, for continuous control, our method outperforms existing methods with respect to sample efficiency, premature convergence and robustness to hyperparameter settings while achieving similar or better final performance.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Model free reinforcement learning algorithms can acquire sophisticated behaviours by interacting with the environment while receiving simple rewards. Recent experiments successfully combined these algorithms with powerful deep neural-network approximators while benefiting from the increase of compute capacity.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Unfortunately, the generality and flexibility of these algorithms comes at a price: They can require a large number of samples and -- especially in continuous action spaces -- suffer from high gradient variance. Taken together these issues can lead to unstable learning and/or slow convergence. Nonetheless, recent years have seen significant progress, with improvements to different aspects of learning algorithms including stability, data-efficiency and speed, enabling notable results on a variety of domains, including locomotion, multi-agent behaviour and classical control.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Two types of algorithms currently dominate scalable learning for continuous control problems: First, Trust-Region Policy Optimisation and the derivative family of Proximal Policy Optimisation algorithms. These policy-gradient algorithms are on-policy by design, reducing gradient variance through large batches and limiting the allowed change in parameters. They are robust, applicable to high-dimensional problems, and require moderate parameter tuning, making them a popular first choice. However, as on-policy algorithms, they suffer from poor sample efficiency.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast, off-policy value-gradient algorithms such as the Deep Deterministic Policy Gradient, Stochastic Value Gradient, and the related Normalized Advantage Function formulation rely on experience replay and learned (action-)value functions. These algorithms exhibit much better data efficiency, approaching the regime where experiments with real robots are possible. While also popular, these algorithms can be difficult to tune, especially for high-dimensional domains like general robot manipulation tasks.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we propose a novel off-policy algorithm that benefits from the best properties of both classes. It exhibits the scalability, robustness and hyperparameter insensitivity of on-policy algorithms, while offering the data-efficiency of off-policy, value-based methods.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

To derive our algorithm, we take advantage of the duality between control and estimation by using Expectation Maximisation (EM), a powerful tool from the probabilistic estimation toolbox, in order to solve control problems. This duality can be understood as replacing the question "what are the actions which maximise future rewards?" with the question "assuming future success in maximising rewards, what are the actions most likely to have been taken?". By using this estimation objective we have more control over the policy change in both E and M steps, yielding robust learning. We show below that several algorithms, including TRPO, can be directly related to this perspective. We leverage the fast convergence properties of EM-style coordinate ascent by alternating a non-parametric data-based E-step which re-weights state-action samples, with a supervised, parametric M-step using deep neural networks.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast to typical off-policy value-gradient algorithms, the new algorithm does not require gradient of the Q-function to update the policy. Instead it uses samples from the Q-function to compare different actions in a given state. And subsequently it updates the policy such that better actions in that state will have better probabilities to be chosen.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We evaluate our algorithm on a broad spectrum of continuous control problems including a 56 DoF humanoid body. All experiments used the same optimisation hyperparameters ^11^1With the exception of the number of samples collected between updates.. Our algorithm shows remarkable data efficiency often solving the tasks we consider an order of magnitude faster than the state-of-the-art. A video of some resulting behaviours can be found here youtu.be/he_BPw32PwU.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Markov decision Processes", "weight": 1.0} -->

We consider the problem of finding an optimal policy $\pi$ for a discounted reinforcement learning (RL) problem; formally characterized by a Markov decision process (MDP). The MDP consists of: continuous states $s$, actions $a$, transition probabilities $p{(\left. s_{t + 1} \middle| {s_{t},a_{t}} \right.)}$ -- specifying the probability of transitioning from state $s_{t}$ to $s_{t + 1}$ under action $a_{t}$ --, a reward function ${r{(s,a)}} \in {\mathbb{R}}$ as well as the discounting factor $\gamma \in {\lbrack 0,1)}$. The policy $\pi{(\left.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Markov decision Processes", "weight": 1.0} -->

a \middle| {s,{\mathbf{θ}}} \right.)}$ (with parameters $\mathbf{θ}$) is assumed to specify a probability distribution over action choices given any state and -- together with the transition probabilities -- gives rise to the stationary distribution $\mu_{\pi}{(s)}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Maximum a Posteriori Policy Optimisation", "weight": 1.0} -->

Our approach is motivated by the well established connection between RL and probabilistic inference. This connection casts the reinforcement learning problem as that of inference in a particular probabilistic model. Conventional formulations of RL aim to find a trajectory that maximizes expected reward. In contrast, inference formulations start from a prior distribution over trajectories, condition a desired outcome such as achieving a goal state, and then estimate the posterior distribution over trajectories consistent with this outcome.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Maximum a Posteriori Policy Optimisation", "weight": 1.0} -->

A finite-horizon undiscounted reward formulation can be cast as inference problem by constructing a suitable probabilistic model via a likelihood function ${p{({O = \left. 1 \middle| \tau \right.})}} \propto {\exp{({\left. \sum{}_{t}r_{t} \right./\alpha})}}$, where $\alpha$ is a temperature parameter. Intuitively, $O$ can be interpreted as the event of obtaining maximum reward by choosing an action; or the event of succeeding at the RL task.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Maximum a Posteriori Policy Optimisation", "weight": 1.0} -->

where $p_{\pi}$ is the trajectory distribution induced by policy $\pi{(\left. a \middle| s \right.)}$ as described in section 2.2 and $q{(\tau)}$ is an auxiliary distribution over trajectories that will discussed in more detail below. The lower bound $\mathcal{J}$ is the evidence lower bound (ELBO) which plays an important role in the probabilistic modeling literature. It is worth already noting here that optimizing with respect to $q$ can be seen as a KL regularized RL problem.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Maximum a Posteriori Policy Optimisation", "weight": 1.0} -->

An important motivation for transforming a RL problem into an inference problem is that this allows us draw from the rich toolbox of inference methods: For instance, $\mathcal{J}$ can be optimized with the familiy of expectation maximization (EM) algorithms which alternate between improving $\mathcal{J}$ with respect to $q$ and $\pi$. In this paper we follow classical and more recent works and cast policy search as a particular instance of this family. Our algorithm then combines properties of existing approaches in this family with properties of recent off-policy algorithms for neural networks.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Maximum a Posteriori Policy Optimisation", "weight": 1.0} -->

The algorithm alternates between two phases which we refer to as E and M step in reference to an EM-algorithm. The E-step improves $\mathcal{J}$ with respect to $q$. Existing EM policy search approaches perform this step typically by reweighting trajectories with sample returns or via local trajectory optimization. We show how off-policy deep RL techniques and value-function approximation can be used to make this step both scalable as well as data efficient. The M-step then updates the parametric policy in a supervised learning step using the reweighted state-action samples from the E-step as targets.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Maximum a Posteriori Policy Optimisation", "weight": 1.0} -->

These choices lead to the following desirable properties: (a) low-variance estimates of the expected return via function approximation; (b) low-sample complexity of value function estimate via robust off-policy learning; (c) minimal parametric assumption about the form of the trajectory distribution in the E-step; (d) policy updates via supervised learning in the M step; (e) robust updates via hard trust-region constraints in both the E and the M step.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Policy Improvement", "weight": 1.0} -->

The derivation of our algorithm then starts from the infinite-horizon analogue of the KL-regularized expected reward objective from Equation. In particular, we consider variational distributions $q{(\tau)}$ that factor in the same way as $p_{\pi}$, i.e. ${q{(\tau)}} = {p{(s_{0})}{\prod_{t > 0}{p{(\left. s_{t + 1} \middle| {s_{t},a_{t}} \right.)}q{(\left. a_{t} \middle| s_{t} \right.)}}}}$

<!-- chunk {"id": "body-0020", "role": "body", "section": "Policy Improvement", "weight": 1.0} -->

Note that due to the assumption about the structure of $q{(\tau)}$ the KL over trajectories decomposes into a KL over the individual state-conditional action distributions. This objective has also been considered e.g. by Haarnoja et al.; Schulman et al.. The additional ${\log p}{({\mathbf{θ}})}$ term is a prior over policy parameters and can be motivated by a maximum a-posteriori estimation problem (see appendix for more details).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Policy Improvement", "weight": 1.0} -->

We also define the regularized Q-value function associated with as

<!-- chunk {"id": "body-0022", "role": "body", "section": "Policy Improvement", "weight": 1.0} -->

We observe that optimizing $\mathcal{J}$ with respect to $q$ is equivalent to solving an expected reward RL problem with augmented reward ${\overset{\sim}{r}}_{t} = {r_{t} - {\alpha{\log\frac{q{(\left. a_{t} \middle| s_{t} \right.)}}{\pi{(\left. a_{t} \middle| {s_{t},{\mathbf{θ}}} \right.)}}}}}$. In this view $\pi$ represents a default policy towards which $q$ is regularized -- i.e. the current best policy. The MPO algorithm treats $\pi$ as the primary object of interest. In this case $q$ serves as an auxiliary distribution that allows optimizing $\mathcal{J}$ via alternate coordinate ascent in $q$ and $\pi_{\mathbf{θ}}$, analogous to the expectation-maximization algorithm in the probabilistic modelling literature.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Policy Improvement", "weight": 1.0} -->

In our case, the E-step optimizes $\mathcal{J}$ with respect to $q$ while the M-step optimizes $\mathcal{J}$ with respect to $\pi$. Different optimizations in the E-step and M-step lead to different algorithms. In particular, we note that for the case where $p{({\mathbf{θ}})}$ is an uninformative prior a variant of our algorithm has a monotonic improvement guarantee as show in the Appendix A.

<!-- chunk {"id": "body-0024", "role": "body", "section": "E-Step", "weight": 1.0} -->

In the E-step of iteration $i$ we perform a partial maximization of $\mathcal{J}{(q,{\mathbf{θ}})}$ with respect to $q$ given $\theta = \theta_{i}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "E-Step", "weight": 1.0} -->

Maximizing Equation, thus obtaining $q_{i} = {{\arg{\max\overline{\mathcal{J}}}}{(q,\theta_{i})}}$, does not fully optimize $\mathcal{J}$ since we treat $Q_{\theta_{i}}$ as constant with respect to $q$. An intuitive interpretation $q_{i}$ is that it chooses the soft-optimal action for one step and then resorts to executing policy $\pi$. In the language of the EM algorithm this optimization implements a partial E-step. In practice we also choose $\mu_{q}$ to be the stationary distribution as given through samples from the replay buffer.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Constrained E-step", "weight": 1.0} -->

The reward and the KL terms are on an arbitray relative scale. This can make it difficult to choose $\alpha$. We therefore replace the soft KL regularization with a hard constraint with parameter $\epsilon$, i.e,

<!-- chunk {"id": "body-0027", "role": "body", "section": "Constrained E-step", "weight": 1.0} -->

If we choose to explicitly parameterize $q{(\left. a \middle| s \right.)}$ -- option 1 below -- the resulting optimisation is similar to that performed by the recent TRPO algorithm for continuous control; only in an off-policy setting. Analogously, the unconstrained objective is similar to the objective used by PPO. We note, however, that the KL is reversed when compared to the KL used by TRPO and PPO.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Constrained E-step", "weight": 1.0} -->

To implement we need to choose a form for the variational policy $q{(\left. a \middle| s \right.)}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Constrained E-step", "weight": 1.0} -->

We can use a parametric variational distribution $q{(\left. a \middle| {s,{\mathbf{θ}}^{q}} \right.)}$, with parameters ${\mathbf{θ}}^{q}$, and optimise Equation via the likelihood ratio or action-value gradients. This leads to an algorithm similar to TRPO/PPO and an explicit M-step becomes unnecessary (see. Alg. 3).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Constrained E-step", "weight": 1.0} -->

We can choose a non-parametric representation of $q{(\left. a \middle| s \right.)}$ given by sample based distribution over actions for a state $s$. To achieve generalization in state space we then fit a parametric policy in the M-step. This is possible since in our framework the optimisation of Equation is only the first step of an EM procedure and we thus do not have to commit to a parametric distribution that generalises across the state space at this point.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Constrained E-step", "weight": 1.0} -->

Fitting a parametric policy in the M-step is a supervised learning problem, allowing us to employ various regularization techniques at that point. It also makes it easier to enforce the hard KL constraint.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Non parametric variational distribution", "weight": 1.0} -->

In the non-parametric case we can obtain the optimal sample based $q$ distribution over actions for each state -- the solution to Equation -- in closed form (see the appendix for a full derivation), as,

<!-- chunk {"id": "body-0033", "role": "body", "section": "Non parametric variational distribution", "weight": 1.0} -->

where we can obtain $\eta^{\ast}$ by minimising the following convex dual function,

<!-- chunk {"id": "body-0034", "role": "body", "section": "Non parametric variational distribution", "weight": 1.0} -->

after the optimisation of which we can evaluate $q_{i}{(\left. a \middle| s \right.)}$ on given samples.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Non parametric variational distribution", "weight": 1.0} -->

This optimization problem is similar to the one solved by relative entropy policy search (REPS) with the difference that we optimise only for the conditional variational distribution $q{(\left. a \middle| s \right.)}$ instead of a joint distribution $q{(a,s)}$ -- effectively fixing $\mu_{q}{(s)}$ to the stationary distribution given by previously collected experience -- and we use the Q function of the old policy to evaluate the integral over $a$. While this might seem unimportant it *is crucial* as it allows us to estimate the integral over actions with multiple samples without additional environment interaction. This greatly reduces the variance of the estimate and allows for fully off-policy learning at the cost of performing only a partial optimization of $\mathcal{J}$ as described above.

<!-- chunk {"id": "body-0036", "role": "body", "section": "M-step", "weight": 1.0} -->

Given $q_{i}$ from the E-step we can optimize the lower bound $\mathcal{J}$ with respect to $\mathbf{θ}$ to obtain an updated policy ${\mathbf{θ}}_{i + 1} = {{\arg{\max_{\mathbf{θ}}\mathcal{J}}}{(q_{i},{\mathbf{θ}})}}$. Dropping terms independent of $\mathbf{θ}$ this entails solving for the solution of

<!-- chunk {"id": "body-0037", "role": "body", "section": "M-step", "weight": 1.0} -->

which corresponds to a weighted maximum a-posteriroi estimation (MAP) problem where samples are weighted by the variational distribution from the E-step. Since this is essentially a supervised learning step we can choose any policy representation in combination with any prior for regularisation. In this paper we set $p{({\mathbf{θ}})}$ to a Gaussian prior around the current policy, i.e, ${{p{({\mathbf{θ}})}} \approx {\mathcal{N}\left( {{\mu = {\mathbf{θ}}_{i}},{\Sigma = \frac{F_{{\mathbf{θ}}_{i}}}{\lambda}}} \right)}},$ where ${\mathbf{θ}}_{i}$ are the parameters of the current policy distribution, $F_{{\mathbf{θ}}_{i}}$ is the empirical Fisher information matrix and $\lambda$ is a positive scalar.

<!-- chunk {"id": "body-0038", "role": "body", "section": "M-step", "weight": 1.0} -->

This additional constraint minimises the risk of overfitting the samples, i.e. it helps us to obtain a policy that generalises beyond the state-action samples used for the optimisation. In practice we have found the KL constraint in the M step to greatly increase stability of the algorithm. We also note that in the E-step we are using the reverse, mode-seeking, KL while in the M-step we are using the forward, moment-matching, KL which reduces the tendency of the entropy of the parametric policy to collapse. This is in contrast to other RL algorithms that use M-projection without KL constraint to fit a parametric policy. Using KL constraint in M-step has also been shown effective for stochastic search algorithms.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Policy Evaluation", "weight": 1.0} -->

Our method is directly applicable in an off-policy setting. For this, we have to rely on a stable policy evaluation operator to obtain a parametric representation of the Q-function $Q_{\theta}{(s,a)}$. We make use of the policy evaluation operator from the Retrace algorithm Munos et al., which we found to yield stable policy evaluation in practice^22^2We note that, despite this empirical finding, Retrace may not be guaranteed to be stable with function approximation..

<!-- chunk {"id": "body-0040", "role": "body", "section": "Policy Evaluation", "weight": 1.0} -->

where $Q_{\phi^{\prime}}{(s,a)}$ denotes the output of a target Q-network, with parameters $\phi^{\prime}$, that we copy from the current parameters $\phi$ after each M-step. We truncate the infinite sum after $N$ steps by bootstrapping with $Q_{\phi^{\prime}}$ (rather than considering a $\lambda$ return). Additionally, $b{(\left. a \middle| s \right.)}$ denotes the probabilities of an arbitrary behaviour policy. In our case we use an experience replay buffer and hence $b$ is given by the action probabilities stored in the buffer; which correspond to the action probabilities at the time of action selection.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experiments", "weight": 1.0} -->

For our experiments we evaluate our MPO algorithm across a wide range of tasks. Specifically, we start by looking at the continuous control tasks of the DeepMind Control Suite (Tassa et al., see Figure 1), and then consider the challenging parkour environments recently published in Heess et al.. In both cases we use a Gaussian distribution for the policy whose mean and covariance are parameterized by a neural network (see appendix for details). In addition, we present initial experiments for discrete control using ATARI environments using a categorical policy distribution (whose logits are again parameterized by a neural network) in the appendix.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Evaluation on control suite", "weight": 1.0} -->

The suite of continuous control tasks that we are evaluating against contains 18 tasks, comprising a wide range of domains including well known tasks from the literature. For example, the classical cart-pole and acrobot dynamical systems, 2D and Humanoid walking as well as simple low-dimensional planar reaching and manipulation tasks. This suite of tasks was built in python on top of mujoco and will also be open sourced to the public by the time of publication.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Evaluation on control suite", "weight": 1.0} -->

While we include plots depicting the performance of our algorithm on all tasks below; comparing it against the state-of-the-art algorithms in terms of data-efficiency. We want to start by directing the attention of the reader to a more detailed evaluation on three of the harder tasks from the suite.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Detailed Analysis on Walker-2D, Acrobot, Hopper", "weight": 1.0} -->

We start by looking at the results for the classical Acrobot task (two degrees of freedom, one continuous action dimension) as well as the 2D walker (which has 12 degrees of freedom and thus a 12 dimensional action space and a 21 dimensional state space) and the hopper standing task. The reward in the Acrobot task is the distance of the robots end-effector to an upright position of the underactuated system. For the walker task it is given by the forward velocity, whereas in the hopper the requirement is to stand still.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Detailed Analysis on Walker-2D, Acrobot, Hopper", "weight": 1.0} -->

As a first observation, we can see that MPO gives stable learning on all tasks and, thanks to its fully off-policy implementation, is significantly more sample efficient than the on-policy PPO baseline. Furthermore, we can observe that changing from the non-parametric variational distribution to a parametric distribution^33^3We note that we use a value function baseline ${\mathbb{E}}_{\pi}{\lbrack{Q{(s, \cdot )}}\rbrack}$ in this setup. See appendix for details. (which, as described above, can be related to PPO) results in only a minor asymptotic performance loss but slowed down optimisation and thus hampered sample efficiency; which can be attributed to the fact that the parametric $q$ distribution required a stricter KL constraint. Removing the automatically tuned KL constraint and replacing it with a manually set entropy regulariser then yields an off-policy actor-critic method with Retrace.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Detailed Analysis on Walker-2D, Acrobot, Hopper", "weight": 1.0} -->

This policy gradient method still uses the idea of estimating the integral over actions -- and thus, for a gradient based optimiser, its likelihood ratio derivative -- via multiple action samples (as judged by a Q-Retrace critic). This idea has previously been coined as using the expected policy gradient (EPG) and we hence denote the corresponding algorithm with EPG + Retrace, which no-longer follows the intuitions of the MPO perspective. EPG + Retrace performed well when the correct entropy regularisation scale is used. This, however, required task specific tuning (c.f. Figure 4 where this hyperparameter was set to the one that performed best in average across tasks). Finally using only a single sample to estimate the integral (and hence the likelihood ratio gradient) results in an actor-critic variant with Retrace that is the least performant off-policy algorithm in our comparison.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Complete results on the control suite", "weight": 1.0} -->

The results for MPO (non-parameteric) -- and a comparison to an implementation of state-of-the-art algorithms from the literature in our framework -- on all the environments from the control suite that we tested on are shown in Figure 4. All tasks have rewards that are scaled to be between 0 and 1000. We note that in order to ensure a fair comparison all algorithms ran with exactly the same network configuration, used a single learner (no distributed computation), used the same optimizer and were tuned w.r.t. their hyperparameters for best performance across all tasks. We refer to the appendix for a complete description of the hyperparameters. Our comparison is made in terms of data-efficiency.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Complete results on the control suite", "weight": 1.0} -->

From the plot a few trends are readily apparent: i) We can clearly observe the advantage in terms of data-efficiency that methods relying on a Q-critic obtain over the PPO baseline. This difference is so extreme that in several instances the PPO baseline converges an order of magnitude slower than the off-policy algorithms and we thus indicate the asymptotic performance of each algorithm of PPO and DDPG (which also improved significantly later during training in some instances) with a colored star in the plot; ii) the difference between the MPO results and the (expected) policy gradient (EPG) with entropy regularisation confirm our suspicion from Section 5.1.1: finding a good setting for the entropy regulariser that transfers across environments without additional constraints on the policy distribution is very difficult, leading to instabilities in the learning curves. In contrast to this the MPO results appear to be stable across all environments; iii) Finally, in terms of data-efficiency the methods utilising Retrace obtain a clear advantage over DDPG. The single learner vanilla DDPG implementation learns the lower dimensional environments quickly but suffers in terms of learning speed in environments with sparse rewards (finger, acrobot) and higher dimensional action spaces.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Complete results on the control suite", "weight": 1.0} -->

Overall, MPO is able to solve all environments using surprisingly moderate amounts of data. On average less than 1000 trajectories (or $10^{6}$ samples) are needed to reach the best performance.

<!-- chunk {"id": "body-0050", "role": "body", "section": "High-dimensional continuous control", "weight": 1.0} -->

Next we turn to evaluating our algorithm on two higher-dimensional continuous control problems; humanoid and walker. To make computation time bearable in these more complicated domains we utilize a parallel variant of our algorithm: in this implementation K learners are all independently collecting data from an instance of the environment. Updates are performed at the end of each collected trajectory using distributed synchronous gradient descent on a shared set of policy and Q-function parameters (we refer to the appendix for an algorithm description). The results of this experiment are depicted in Figure 3.

<!-- chunk {"id": "body-0051", "role": "body", "section": "High-dimensional continuous control", "weight": 1.0} -->

For the Humanoid running domain we can observe a similar trend to the experiments from the previous section: MPO quickly finds a stable running policy, outperforming all other algorithms in terms of sample efficiency also in this high-dimensional control problem.

<!-- chunk {"id": "body-0052", "role": "body", "section": "High-dimensional continuous control", "weight": 1.0} -->

The case for the Walker-2D parkour domain (where we compare against a PPO baseline) is even more striking: where standard PPO requires approximately *1M trajectories* to find a good policy MPO finds a solution that is asymptotically no worse than the PPO solution in in about 70k trajectories (or 60M samples), resulting in an order of magnitude improvement. In addition to the walker experiment we have also evaluated MPO on the Parkour domain using a humanoid body (with 22 degrees of freedom) which was learned successfully (not shown in the plot, please see the supplementary video).

<!-- chunk {"id": "body-0053", "role": "body", "section": "Discrete control", "weight": 1.0} -->

As a proof of concept -- showcasing the robustness of our algorithm and its hyperparameters -- we performed an experiment on a subset of the games contained contained in the \"Arcade Learning Environment\" (ALE) where we used *the same hyperparameter* settings for the KL constraints as for the continuous control experiments. The results of this experiment can be found in the Appendix.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have presented a new off-policy reinforcement learning algorithm called Maximum a-posteriori Policy Optimisation (MPO). The algorithm is motivated by the connection between RL and inference and it consists of an alternating optimisation scheme that has a direct relation to several existing algorithms from the literature. Overall, we arrive at a novel, off-policy algorithm that is highly data efficient, robust to hyperparameter choices and applicable to complex control problems. We demonstrated the effectiveness of MPO on a large set of continuous control problems.
