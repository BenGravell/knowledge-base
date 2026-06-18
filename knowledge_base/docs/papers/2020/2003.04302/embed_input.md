<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Stochastic Recursive Momentum for Policy Gradient Methods

Topics include Sample complexity, Policy gradients, STORM-PG.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we propose a novel algorithm named STOchastic Recursive Momentum for Policy Gradient (STORM-PG), which operates a SARAH-type stochastic recursive variance-reduced policy gradient in an exponential moving average fashion. STORM-PG enjoys a provably sharp O(1/epsilon^) sample complexity bound for STORM-PG, matching the best-known convergence rate for policy gradient algorithm. In the mean time, STORM-PG avoids the alternations between large batches and small batches which persists in comparable variance-reduced policy gradient methods, allowing considerably simpler parameter tuning. Numerical experiments depicts the superiority of our algorithm over comparative policy gradient algorithms.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reinforcement Learning (RL) is a dynamic learning approach that interacts with the environment and execute actions according to the current state, so that a particular measure of cumulative rewards is maximized. Model-free deep reinforcement learning algorithms have achieved remarkable performance in a range of challenging tasks, including stochastic control, autonomous driving, games, continuous robot control tasks, etc.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Generally, there are two aspects of methods of solving a model-free RL problem: value-based methods such as Q-Learning, SARSA, etc., as well as policy-based methods such as Policy Gradient (PG) algorithm. PG algorithm models the state-to-action transition probabilities as a parameterized family, and the cumulative rewards can be regarded as a function of the parameters. Thus, policy gradient based problem shares a formulation that is analogous to the traditional stochastic optimization problem.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

One critical challenge of reinforcement learning algorithms compared to traditional gradient based algorithms lies on the issue of distribution shift, that is, the data sample distribution encounters distributional changes throughout the learning dynamics. To correct this, (an off-policy version of) Policy Gradient (PG) method and Trust Region Policy Optimization (TRPO) method have been proposed as general off-policy algorithms to optimize policy parameters using gradient based methods.^11^1In reinforcement learning literature, on-policy algorithms make use of samples rolled out by the current policy for only once, and hence suffer from high sample complexities. On the contrary, off-policy algorithms in earlier work enjoy reduced sample complexities since they reuse the past trajectory samples. Nevertheless, they are often brittle and sensitive to hyperparameters and hence suffer from reproducibility issues. PG method directly optimizes the policy parameters via gradient based algorithms, and it dates back to the introduction of REINFORCE and GPOMDP estimators that our algorithm is built upon.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The problem of high sample complexity arises frequently in policy gradient based methods due to a combined effect of high variance incurred during the training phase and distribution shift, limiting the ability of model-free deep reinforcement learning algorithms. Such a combined effect signals the potential need of adopting variance-reduced gradient estimators to accelerate off-policy algorithms. Recently proposed variance-reduced policy gradient methods include SVRPG and SRVRPG theoretically improve the sample efficiency over PG. This is corroborated by empirical findings: we observe that the variance-reduced gradient alternatives SVRPG and SRVRPG accelerate and stabilize the training processes, mainly due to their accommodations with larger stepsizes and reduced variances.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Nevertheless compared to the vanilla PG method, one major drawback of the aforementioned variance-reduced policy gradient methods is their alternations between large and small batches of trajectory samples, spelled as the restarting mechanism, so the variance can be effectively controlled. In this paper, we circumvent such a restarting mechanism by introducing a new algorithm named STOchastic Recursive Momentum Policy Gradient (STORM-PG), which utilizes the idea of a recently proposed variance-reduced gradient method STORM and blends with policy gradient methods. STORM is an online variance-reduced gradient method that adopts an exponential moving averaging mechanism that persistently discount the accumulated variance. In the nonconvex smooth stochastic optimization setting, STORM achieves an $O{(\epsilon^{- 3})}$ queries complexity that ties with online SARAH/SPIDER and matches the lower bound for finding an $\epsilon$-first-order stationary point. As a closely related variant, SARAH/SPIDER based stochastic variance-reduced compositional gradient methods also achieve an $O{(\epsilon^{- 3})}$ complexity under a different set of assumptions (hu2019efficient; zhang2019multi).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our proposed STORM-PG algorithm blends such a state-of-the-art variance-reduced gradient estimator with the PG algorithm. Instead of introducing a restarting mechanism in concurrent variance-reduced policy gradient methods, our STORM-PG algorithm guarantees the variance stability by adopting the exponential moving averaging mechanism featured by STORM. In our experiments, we see that the variance stability of our variance-reduced gradient estimator allows our STORM-PG algorithm to achieve a (perhaps surprisingly) overall mean rewards improvement in reinforcement learning tasks.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

We have designed a novel policy gradient method that enjoys several benign properties, such as using an exponential moving averaging mechanism instead of restarting mechanism to reduce our gradient estimator variance. Theoretically, we prove a state-of-art convergence rate for our proposed STORM-PG algorithm in our setting. Experimentally, our STORM-PG algorithm depicts strikingly desirable performance in many reinforcement learning tasks.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Notational Conventions", "weight": 1.0} -->

Throughout the paper, we treat the parameters $L_{d}$, $C_{\gamma}$, $R$, $M$, $N$, $\Delta$ and $\sigma$ as global constants. Let $h$ denote the index of steps that the agent takes to interact with the environment and $H$ is the maximum length of an episode. Let $\parallel \cdot \parallel$ denote the Euclidean norm of a vector or the operator norm of a matrix induced by Euclidean norm. For fixed $t \geq 0$, let $\mathcal{B}_{t}$ denotes the batch of samples choosen at the $t$'th iteration and $\mathcal{B}_{0:t} = {\{\mathcal{B}_{0},\mathcal{B}_{1},\ldots,\mathcal{B}_{t}\}}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Notational Conventions", "weight": 1.0} -->

$\mathcal{F}_{t}$ is the $\sigma$-algebra generated by $\mathcal{B}_{0:t}$ and ${\mathbb{E}}{\lbrack \cdot \mid \mathcal{F}_{t}\rbrack}$ is the conditional expectation based on samples generated up to the $t$'th iteration. Other notations are explained at their first appearances.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Organization", "weight": 1.0} -->

The rest of our paper is organized as follows. Section 2 introduces the backgrounds and preliminaries of the policy gradient algorithm. Section 3 formally introduces our STORM-PG algorithm design. Section 4 introduces the necessary definitions and assumptions. Section 5 presents the convergence rate analysis, whose corresponding proof is provided in Section 6. Section 7 conducts experimental comparison on continuous control tasks, and Section 8 concludes our results.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Policy Gradient Prelimilaries", "weight": 1.0} -->

In this section we introduce the background of policy gradient and the objective function that our algorithm is based. The basic operation of the PG algorithm is similar to the gradient acsent algorithm with some RL specific gradient estimators. In Section 2.1 we introduce the REINFORCE estimator which is the basis of many follow up PG works. In Section 2.2 we introduce the GPOMDP estimator which further reduces the variance and is the fundation of our algorithm. Finally in Section 2.3 we formulate the probability induced by the policy as a Gaussian distribution, which is a special case adopted in our experiments.

<!-- chunk {"id": "body-0014", "role": "body", "section": "REINFORCE Estimator", "weight": 1.0} -->

We consider the standard reinforcement learning setting of solving a discrete time finite horizon Markov Decision Process (MDP) $\mathcal{M} = {\{\mathcal{S},\mathcal{A},\mathcal{P},\mathcal{R},\gamma,\rho\}}$ which models the behavior of an agent interacting with a given environment.

<!-- chunk {"id": "body-0015", "role": "body", "section": "REINFORCE Estimator", "weight": 1.0} -->

Let $\mathcal{S}$ be the space of states in the environment, $\mathcal{A}$ be the space of actions that the agent can take, $\mathcal{P}:{{\mathcal{S} \times \mathcal{A}}\rightarrow\mathcal{S}}$ be the transition probability from $s \in \mathcal{S}$ to $s^{\prime} \in \mathcal{S}$ given $a \in \mathcal{A}$, $R:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$ be the reward function of taking action $a \in \mathcal{A}$ at state $s \in \mathcal{S}$, $\gamma$ be the discount factor that adds smaller weights to rewards at more distant future, and $\rho$ be the initial state distribution.

<!-- chunk {"id": "body-0016", "role": "body", "section": "REINFORCE Estimator", "weight": 1.0} -->

We mainly focuses on in this paper the policy gradient setting where there is a policy $\pi{({a \mid s})}$ as the probability of taking action $a$ given state $s$ such that ${\sum_{a \in \mathcal{A}}{\pi{({a \mid s})}}} = 1$; The policy $\pi{( \cdot \mid s)}$ models the agent's behavior after experiencing the environment's state $s$. Given finite state and action spaces, the policy $\pi{({a \mid s})}$ can be coded in a ${|\mathcal{S}|} \times {|\mathcal{A}|}$ tabular.

<!-- chunk {"id": "body-0017", "role": "body", "section": "REINFORCE Estimator", "weight": 1.0} -->

However when the state/action space is large or countably infinite, we adopt a probability mass function class $\pi_{\mathbf{ξ}}{({a \mid s})}$, parameterized by ${\mathbf{ξ}} \in {\mathbb{R}}^{d}$, as an approximated class of functions to such a tabular.

<!-- chunk {"id": "body-0018", "role": "body", "section": "REINFORCE Estimator", "weight": 1.0} -->

where the trajectory $\tau:={(s_{0},a_{0},s_{1},a_{1},\ldots,s_{H},a_{H})}$ is the sequence that alters between states and actions, and $H$ is the maximum length (episode) of all trajectories.

<!-- chunk {"id": "body-0019", "role": "body", "section": "REINFORCE Estimator", "weight": 1.0} -->

where the expectation is taken over a parameterized probability distribution $p{( \cdot \mid {\mathbf{ξ}})}$ with parameter $\mathbf{ξ}$, as is defined.

<!-- chunk {"id": "body-0020", "role": "body", "section": "REINFORCE Estimator", "weight": 1.0} -->

where the trajectories $\tau_{i}$ are generated according to the trajectory distribution $p{( \cdot \mid {\mathbf{ξ}})}$. The above estimator in policy gradient is known as the REINFORCE estimator.

<!-- chunk {"id": "body-0021", "role": "body", "section": "GPOMDP Estimator", "weight": 1.0} -->

One of the disadvantage of REINFORCE estimator lies on its excessive variance of trajectories introduced throughout the end of the episode.

<!-- chunk {"id": "body-0022", "role": "body", "section": "GPOMDP Estimator", "weight": 1.0} -->

where $(a_{t},s_{t})$ are action-state pairs along the trajectory $\tau_{i}$. We adopt a variance-reduced version of GPOMDP estimator throughout the end of this paper.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Gaussian Policy", "weight": 1.0} -->

Finally, we introduce the Gaussian policy setting.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Gaussian Policy", "weight": 1.0} -->

where $\sigma^{2}$ is the fixed variance parameter and ${\psi{(s)}}:{\mathcal{S}\rightarrow{\mathbb{R}}^{d}}$ is a bounded feature mapping from the state space $\mathcal{S}$ to ${\mathbb{R}}^{d}$. As the readers will see, the Gaussian policy satisfies all assumptions in Section 4; more detailed discussions can be found in Xu et al., Xu et al. and Papini et al..

<!-- chunk {"id": "body-0025", "role": "body", "section": "STORM-PG Algorithm", "weight": 1.0} -->

and $d_{i}{({\mathbf{ξ}})}$ defined in is an unbiased estimator of the true gradient ${\nabla_{\mathbf{ξ}}L}{({\mathbf{ξ}})}$. The simplest algorithm, stochastic gradient ascent, updates the iterates as

<!-- chunk {"id": "body-0026", "role": "body", "section": "STORM-PG Algorithm", "weight": 1.0} -->

To remedy the distribution shift issue in reinforcement learning tasks, we introduce an importance sampling weight between trajectories generated by $\mathbf{ξ}$ and the ones generated by ${\mathbf{ξ}}^{\prime}$ as

<!-- chunk {"id": "body-0027", "role": "body", "section": "STORM-PG Algorithm", "weight": 1.0} -->

where $\tau_{i,h}$ is a trajectory generated by $p{( \cdot \mid {\mathbf{ξ}}^{\prime})}$ truncated at time $h$. To further reduce the variance introduced by the randomness in $i$, SVRG introduced a variance-reduced estimator estimator of ${\nabla_{\mathbf{ξ}}L}{({\mathbf{ξ}}_{t})}$

<!-- chunk {"id": "body-0028", "role": "body", "section": "STORM-PG Algorithm", "weight": 1.0} -->

where $\overset{\sim}{\mathbf{ξ}}$ is a fixed point calculated once every $q$ steps and $\overset{\sim}{u}$ is a fixed estimation of the gradient at point $\overset{\sim}{\mathbf{ξ}}$. Instead of the aforementioned SVRG-type estimator which was adopted by Xu et al., Papini et al. adopts instead a recursive estimator

<!-- chunk {"id": "body-0029", "role": "body", "section": "STORM-PG Algorithm", "weight": 1.0} -->

to track the gradient ${\nabla_{\mathbf{ξ}}L}{({\mathbf{ξ}}_{t + 1})}$ at each time. In above, $\mathbf{g}_{0}$ is scheduled to be updated once every $q$ iterations as a large-batch estimated gradient.

<!-- chunk {"id": "body-0030", "role": "body", "section": "STORM-PG Estimator", "weight": 1.0} -->

In this paper, we propose to use the STORM estimator as introduced, which is essentially an exponential moving average SARAH estimator

<!-- chunk {"id": "body-0031", "role": "body", "section": "STORM-PG Estimator", "weight": 1.0} -->

When $\alpha = 1$, the STORM-PG estimator reduces to the vanilla stochastic gradient estimator and when $\alpha = 0$, the STORM-PG esimator reduces to the SARAH estimator. As our $\alpha$ is chosen between $$, the estimator is a combination of an variance reduced biased estimator and an unbiased estimator. In addition, can be rewritten as

<!-- chunk {"id": "body-0032", "role": "body", "section": "STORM-PG Estimator", "weight": 1.0} -->

which can be interpreted as an exponentially decaying mechanism via a factor of $({1 - \alpha})$. We can see later in the proof of the convergence rate that the estimation error ${\mathbb{E}}{\|{\mathbf{g}_{t} - {{\nabla L}{({\mathbf{ξ}})}}}\|}^{2}$ can be controlled by a proper choice of $a$ while in SARAH case to control the convergence speed, the batch size $B$ or the learning rate $\eta$ have to be tuned accordingly. This allows us to operate a single-loop algorithm instead of a double-loop algorithm. We only need a large batch to estimate $\mathbf{g}_{0}$ once, and do mini-batch or single batch updates till the end of the algorithm. This estimator hinders the accumulation of estimation error in each round.

<!-- chunk {"id": "body-0033", "role": "body", "section": "STORM-PG Estimator", "weight": 1.0} -->

Output $\overset{\sim}{\mathbf{ξ}}$ chosen uniformly at random from {ξt}t = 0T − 1

<!-- chunk {"id": "body-0034", "role": "body", "section": "Definitions and Assumptions", "weight": 1.0} -->

In this section, we make several definitions and assumptions necessary for analyzing the convergence of the STORM-PG Algorithm.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

In this section, we introduce the lemmas neccessary for proving the convergence results of our STORM-PG Algorithm and finally state our main theorem of convergence. We recall that our goal is to achieve an $\epsilon$-accurate solution of function $L{({\mathbf{ξ}})}$, whose gradient can be estimated unbiasedly by $d_{i}{({\mathbf{ξ}})}$. First of all, given Assumptions 2. ‣ 4 Definitions and Assumptions ‣ Stochastic Recursive Momentum for Policy Gradient Methods") and 3. ‣ 4 Definitions and Assumptions ‣ Stochastic Recursive Momentum for Policy Gradient Methods"), we can derive the boundedness, Liptchizness of $d_{i}{({\mathbf{ξ}})}$ and the smoothness of $L{({\mathbf{ξ}})}$, which are necessary conditions for proving convergence of nonconvex stochastic optimization problems.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Convergence Analysis", "weight": 1.0} -->

Similarily, ${\nabla_{\mathbf{ξ}}d_{i}}{({\mathbf{ξ}})}$ can be written as a linear combination of ${{\nabla_{\mathbf{ξ}}^{2}\log}\pi_{\mathbf{ξ}}}{({a_{h} \mid s_{h}})}$. Using the fact that ${\sum_{h = 0}^{H - 1}{\sum_{t = h}^{H - 1}\gamma^{t}}} \leq {1/{({1 - \gamma})}^{2}}$ and the bound derived in Assumptions 2. ‣ 4 Definitions and Assumptions ‣ Stochastic Recursive Momentum for Policy Gradient Methods") and 3. ‣ 4 Definitions and Assumptions ‣ Stochastic Recursive Momentum for Policy Gradient Methods"), it is direct to see that

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 10", "weight": 1.0} -->

Hence, to control the growth of function value, $\eta$ should be chosen with an order of $\mathcal{O}{(T^{- {1/2}})}$. With infinitely increasing $T$, $\eta$ have to be chosen to be infinitely small. SARAH/SPIDER algorithm uses an restart machenism to remedy for this problem.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Remark 10", "weight": 1.0} -->

For $\alpha$, we only need to control $\alpha \geq {4C_{\gamma}^{2}\eta^{2}}$ so that $\eta$ is no longer related with $T$. This allows us to do continuous training without restarting the iterations.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we design a set of experiments to validate the superiority of our STORM-PG Algorithm. Our implementation is based on the rllab library^22^2 and the initial implementation of Papini et al. ^33^3 We test the performance of our algorithms as well as the baseline algorithms on the Cart-Pole^44^4 environment and the Mountain-Car environment.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experiments", "weight": 1.0} -->

For baseline algorithms, We choose GPOMDP and two variance-reduced policy gradient algorithms SVRPG and SRVRPG.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Comparison of different Algorithms", "weight": 1.0} -->

In SRVRPG and SVRPG, adjustable parameters include the large batch size $S_{0}$, the mini batch size $B$, the inner iteration number $m$ and the learning rate $\eta$. In STORM-PG Algorithm, we have to tune the large batch size $S_{0}$, the momentum factor $a$ and the learning rate $\eta$. Notice that we do not tune the mini batch size $B$ in STORM-PG, and fix it to be the same with the best $B$ tuned on SVRPG, as shown in the theory.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Comparison of different Algorithms", "weight": 1.0} -->

We adaptively choose the learning rate by adam optimizer and learning rate decay. The initial learning rate and decay discount are chosen between $(0.0001,0.1)$ and $(0.5,0.99)$ respectively. The environment related parameters: the discount factor $\gamma$ and the horizon $H$ varies according to tasks. We list the specific choice of $\gamma$, $H$, together with the initial batch size $S_{0}$ and the inner batch size $B$ in the supplementary materials.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Comparison of different Algorithms", "weight": 1.0} -->

We use a Gaussian policy with a neural network with one hidden layer of size 64. For each algorithm in one environment, we choose ten best independent runs to collect the rewards and plot the confidence interval together with the average rewards at each iteration of the training process.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Cart-Pole environment", "weight": 1.0} -->

The Cart-Pole environment describes the interaction of a pendulum pole attached to a cart. By pushing the cart leftward or rightward, a reward of +1 is obtained by keeping the pole upright and the episode ends when the cart or the pole is too far away from a given center.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Cart-Pole environment", "weight": 1.0} -->

Under this environment setting, figure 1 shows the growth of the average return according to the training trajectories.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Cart-Pole environment", "weight": 1.0} -->

From Figure 1, we see that our STORM-PG algorithm ourperforms other variance-reduced policy gradient methods in convergence speed. It reaches the maximum value at approximately 500 trajectories while SRVRPG and SVRPG reaches the maximum value at approximately 1500 trajectories. GPOMDP converges at about 3000 trajectories.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Mountain-Car Environment", "weight": 1.0} -->

We use the Mountain Car environment provided in rllab environments. The task is to push a car to a certain position on a hill. The agent takes continuous actions to move leftward or rightward and gets a reward according to it's current position and height, every step it takes gets a penalty -1 and the episode ends when a target position is reached.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Mountain-Car Environment", "weight": 1.0} -->

From Figure 2, we see that STORM-PG algorithm outperforms other baselines within the first 200 trajectories and reaches a stable zone within 600 trajectories, while for the algorithms it takes at least 1000 trajectories to reach a reasonable result. The two figures 1 and 2 verifies our theory that our STORM-PG algorithm brings significant improvement to the policy gradient training.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Mountain-Car Environment", "weight": 1.0} -->

Specifically, as we have mentioned at the beginning of Section 7, previous variance-reduced policy gradient methods requires carefully tuning of the inner loop iteration number. SVRPG uses adaptive number of iterations while after tuning SRVRPG fixes a very small number of inner loops.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Mountain-Car Environment", "weight": 1.0} -->

On the contrary, we do not tune the mini batch size $B$. In practice, we fix both the initial batch $S_{0}$ and the mini batch $B$. The high stability with respect to hyper-parameters saves lots of efforts during the training process, The tolerance to the choice of parameters allows us to design a highly user friendly while efficient policy gradient algorithm.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Final Remarks", "weight": 1.0} -->

In this paper, we propose a new STORM-PG algorithm that adopts a recently proposed variance-reduced gradient method called STORM. STORM-PG enjoys advantage both theoretically and experimentally. From the final experimental results, our STORM-PG algorithm is significantly better than all other baseline methods, both in aspects of training stability and parameter tuning (the user time of tuning STORM-PG is much shorter). The superiority of STORM-PG in experimental results over SVRPG breaks the curse that stochastic recursive gradient method, namely SARAH, often fails to outperform SVRG in practice even though it has better theoretical convergence rate. Future works include proving the lower bounds of our algorithm and further improvement of the experimental performance on other statistical learning tasks. We hope this work can inspire both reinforcement learning and optimization communities for future explorations.
