<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Relative Entropy Regularized Policy Iteration

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present an off-policy actor-critic algorithm for Reinforcement Learning (RL) that combines ideas from gradient-free optimization via stochastic search with learned action-value function. The result is a simple procedure consisting of three steps: i) policy evaluation by estimating a parametric action-value function; ii) policy improvement via the estimation of a local non-parametric policy; and iii) generalization by fitting a parametric policy. Each step can be implemented in different ways, giving rise to several algorithm variants. Our algorithm draws on connections to existing literature on black-box optimization and 'RL as an inference' and it can be seen either as an extension of the Maximum a Posteriori Policy Optimisation algorithm (MPO) [Abdolmaleki et al., 2018a], or as an extension of Trust Region Covariance Matrix Adaptation Evolutionary Strategy (CMA-ES) [Abdolmaleki et al., 2017b; Hansen et al., 1997] to a policy iteration scheme.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our comparison on 31 continuous control tasks from parkour suite [Heess et al., 2017], DeepMind control suite [Tassa et al., 2018] and OpenAI Gym [Brockman et al., 2016] with diverse properties, limited amount of compute and a single set of hyperparameters, demonstrate the effectiveness of our method and the state of art results. Videos, summarizing results, can be found at goo.gl/HtvJKR.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reinforcement learning with flexible function approximators such as neural networks, also referred to as "deep RL", holds great promises for continuous control and robotics. Neural networks can express complex dependencies between high-dimensional and multimodal input and output spaces, and learning-based approaches can find solutions that would be difficult to craft by hand. Unfortunately, the generality and flexibility of learning based approaches with neural networks can come at a price: Deep reinforcement learning algorithms can require large amounts of training data; they can suffer from stability problems, especially in high-dimensional continuous action spaces; and they can be sensitive to hyperparameter settings. Even though attempts to control robots or simulated robots with neural networks go back a long time, it has only been recently that algorithms have emerged which are able to scale to challenging problems -- including first successes in the data-restricted domain of physical robots.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Model-free off-policy actor-critic algorithms have several appealing properties. In particular, they make minimal assumptions about the control problem, and can be data-efficient when used in combination with a appropriate data reuse. They can also scale well when implemented appropriately (see e.g. Gu et al. Popov et al., ). Broadly speaking, many off-policy algorithms are implemented by alternating between two steps: i) a policy evaluation step in which an action-value function is learned for the current policy; and ii) a policy improvement step during which the policy is modified given the current action-value function.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we outline a general policy iteration framework and motivate it from both an intuitive perspective as well as a "RL as inference" perspective. In the case when the MDP collapses to a bandit setting our framework can be related to the black-box optimization literature. We propose an algorithm that works reliably across a wide range of tasks and requires minimal hyper-parameter tuning to achieve state of the art results on several benchmark suites. Similarly to Maximum a Posteriori Policy Optimisation algorithm (MPO), it estimates the action-value function $Q^{\pi}{(s,a)}$ for a policy $\pi$ and then uses this Q-function to update the policy. The policy improvement step builds on ideas from the black-box optimization and KL-regularized control literature. It first estimates a local, non-parametric policy that is obtained by reweighting the samples from the current/prior policy, and subsequently fits a new parametric policy via weighted maximum likelihood learning. Trust-region like constraints ensure stability of the procedure. The algorithm simplifies the original formulation of MPO while improving its robustness via decoupled optimization of policy's mean and covariance.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that our algorithm solves standard continuous control benchmark tasks from the DeepMind control suite (including control of a humanoid with 56 action dimensions), from the OpenAI Gym, and also the challenging "Parkour" tasks from Heess et al. all with the same hyperparameter settings and a single actor for data collection.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

In this paper we are focused on actor-critic algorithms for stable and data efficient policy optimization. Actor-critic algorithms decompose the policy optimization problem into two distinct sub-problems as also outlined in Algorithm 1: i) estimating the state-conditional action value (the Q-function, denoted by $Q$) given a policy $\pi$, and, ii) improving $\pi$ given an estimate of $Q$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

We consider the usual discounted reinforcement learning (RL) problem defined by a Markov decision process (MDP). The MDP consists of continuous states $s$, actions $a$, an initial state distribution $p{(s_{0})}$, transition probabilities $p{(\left. s_{t + 1} \middle| {s_{t},a_{t}} \right.)}$ which specify the probability of transitioning from state $s_{t}$ to $s_{t + 1}$ under action $a_{t}$, a reward function ${r{(s,a)}} \in {\mathbb{R}}$ and the discount factor $\gamma \in {\lbrack 0,1)}$. The policy $\pi{(\left. a \middle| {s,{\mathbf{θ}}} \right.)}$ with parameters $\mathbf{θ}$ is a distribution over actions $a$ given a state $s$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

We optimize the objective, where the expectation is taken with respect to the trajectory distribution induced by $\pi$. We define the action-value function associated with $\pi$ as the expected cumulative discounted return when choosing action $a$ in state $s$ and acting subsequently according to policy $\pi$ as ${Q^{\pi}{(s,a)}} = {{\mathbb{E}}_{\pi}{\lbrack{{\left. {\sum_{t = 0}^{\infty}{\gamma^{t}r{(s_{t},a_{t})}}} \middle| s_{0} \right. = s},{a_{0} = a}}\rbrack}}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

The true Q-function of an MDP and policy $\pi^{(k)}$ in iteration $k$ provides the information needed to estimate a new policy $\pi^{({k + 1})}$ that will have a higher expected discounted return than $\pi^{(k)}$; and will thus improve our objective. This is the core idea underlying policy iteration: if for all states we change our policy to pick actions that have higher value with higher probability then the overall objective is guaranteed to improve. For instance, we could attempt to choose ${\pi^{({k + 1})}{(\left. a \middle| s \right.)}} = {\delta{({{a^{\ast}{(s)}} - a})}}$ where ${a^{\ast}{(s)}} = {{\operatorname{argmax}_{a}Q}{(s,a)}}$ as action selection rule -- assuming an accurate $Q^{\pi}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

In this paper we specifically focus on the problem of reliably optimizing $\pi^{({k + 1})}$ given $Q^{\pi^{(k)}}$. In particular, in Section 4 ‣ Relative Entropy Regularized Policy Iteration") we discuss update rules for stochastic policies that explicitly control the change in $\pi$ from one iteration to the next. And we show how to avoid premature convergence when Gaussian policies are used.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Policy Evaluation (Step 1)", "weight": 1.0} -->

Policy Evaluation is concerned with learning an approximate Q-function (policy evaluation). In principle, any off-policy method for learning Q-functions could be used here, as long as it provides sufficiently accurate value estimates. This includes making use of recent advances such as distributional RL or Retrace. To separate the effects of Policy Improvement and better value estimation we focus on simple 1-step temporal difference (TD) learning for most of the paper (showing advantages from better policy evaluation approaches in separate experiments). We fit a parametric Q-function $Q_{\phi}^{\pi}{(s,a)}$ with parameters $\phi$ by minimizing the squared (TD) error where $r_{t} = {r{(s_{t},a_{t})}}$, which we optimize via gradient descent. We let $\phi'$ be the parameters of a target network (the parameters of the last Q-function) that is held constant for $250$ steps (and then copied from the optimized parameters $\phi$).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Policy Evaluation (Step 1)", "weight": 1.0} -->

For brevity of notation we drop the subscript and dependence on parameters $\phi$ in the following section and write $Q^{\pi^{(k)}}{(a,s)}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Policy Improvement (Step 2-3)", "weight": 1.0} -->

The policy improvement step consists of optimizing ${\overline{J}{(s,\pi)}} = {{\mathbb{E}}_{\pi}{\lbrack{Q^{\pi^{(k)}}{(s,a)}}\rbrack}}$ for $s$ drawn from the visitation distribution $\mu_{\pi}{(s)}$. In practice, we replace $\mu_{\pi}{(s)}$ with draws from a replay buffer. As argued intuitively in Section 2, if we improve this expectation in all states and for an accurate $Q$, this will improve our objective $J$ (Equation 1). Below we describe two approaches that perform this optimization. They do not fully optimize $\overline{J}$ to avoid being misled by errors in the approximated Q-function -- while keeping exploration. We find a solution capturing some information about the local value landscape in the shape of the distribution. Maintaining this information is important for exploration and future optimization steps.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Policy Improvement (Step 2-3)", "weight": 1.0} -->

Both approaches employ a two-step procedure: they first construct a non-parametric estimate $q$ s.t. ${\overline{J}{(s,q)}} \geq {\overline{J}{(s,\pi^{(k)})}}$ (Step 2). They then project this non-parametric representation back onto the manifold of parameterized policies by finding which amounts to supervised learning -- or maximum likelihood estimation (MLE) (Step 3). This split of the improvement step into sample based estimation followed by supervised learning allows us to separate the neural network fitting from the RL procedure, enabling regularization in the latter.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Finding action weights (Step 2)", "weight": 1.0} -->

Given a learned approximate Q-function, in each policy optimization step, we first sample K states ${\{ s_{j}\}}_{j = {1\ldotsK}}$ from the replay buffer. Secondly, we sample N actions for each state $s_{j}$ from the last policy distribution, forming the sample based estimate, i.e, ${{\{ a_{i}\}}_{i = {1\ldotsN}} \sim {\pi^{(k)}{(\left. a \middle| s_{j} \right.)}}},$ where i denotes the action index and j denotes the state index in the replay. We then evaluate each state-action pair using the Q-function ($Q^{\pi^{(k)}}$).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Finding action weights (Step 2)", "weight": 1.0} -->

Now, given states, actions, and their corresponding Q-values, i.e. ${\{ s_{j},{\{ a_{i},{Q^{\pi^{(k)}}{(s_{j},a_{i})}}\}}_{i = {1\ldotsN}}\}}_{j = {1\ldotsK}}$ we want to first re-adjust the probabilities for the given actions in each state such that better actions have higher probability. These updated probabilities are expressed via the weights $q_{ij}$, forming the non-parametric, sample based improved policy, i.e, ${{{\forall s_{j}},a_{i}}:{{q{(\left. a_{i} \middle| s_{j} \right.)}} = q_{ij}}}.$ To determine $q_{ij}$, one could assign probabilities manually to the actions based on the ranking of actions w.r.t their Q-values.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Finding action weights (Step 2)", "weight": 1.0} -->

This approach has been used in the black-box and stochastic search communities and can be related to methods such as CMA-ES and the cross-entropy method. In general, we can calculate weights using any rank preserving transformation of the Q-values. If the weights additionally form a proper sample based distribution, satisfying: i) positivity of weights, and ii) normalization ${\sum_{i}q_{ij}} = 1$. We now discuss various valid transformations of the Q-values.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Using ranking to transform Q-values", "weight": 1.0} -->

In particular, one such weighting would be to choose the weight of the $i$-th best action for the $j$-th sampled state to be proportional to $q_{ij} \propto {\ln{(\frac{N + \eta}{i})}}$, where N is the number of action samples per state and $\eta$ is a temperature parameter (if $\eta = 0.5$ this would correspond to an update similar to CMA-ES). Intuitively, we set a fixed pseudo probability for each action based on their rank, such that the expected Q-value under this new sample-based (state dependent) distribution increases.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Using an exponential transformation of the Q-values", "weight": 1.0} -->

Alternatively, we can obtain the weights by optimizing for an optimal assignment of action probabilities directly. If we additionally want to constrain the change of the policy this corresponds to solving the following KL regularized objective: Here, the first constraint forces the weights to stay close to the last policy probabilities, i.e. bounds the average relative entropy, or average KL, since samples $a_{i}$ are drawn from $\pi^{(k)}$. The second constraint ensures that weights are normalized. The solution will be new weights, given through the categorical probabilities $q_{ij} = {q{(\left. a_{i} \middle| s_{j} \right.)}}$, such that the expected Q-value increases while constraining the reduction in entropy (to prevent the weights from collapsing onto one action immediately). This objective has been used in the RL and bandit optimization literature before (see e.g.) and, when combined with Q-learning has some optimality guarantees.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Using an exponential transformation of the Q-values", "weight": 1.0} -->

As it turns out, its solution can be obtained in closed form, and consists of a softmax over Q-values: where ${Z{(j)}} = {\sum_{i}{\exp\left({{Q^{\pi^{(k)}}\left(s_{j},a_{i} \right)}/\eta} \right)}}$. The temperature $\eta$ corresponding to the constraint $\epsilon$ can be found automatically by solving the following convex dual function alongside our policy optimization: We found that, in practice, this optimization can be performed via a few steps of gradient descent on $\eta$ for each batch after the weight calculation. As $\eta$ should be positive, we use a projection operator to project back the $\eta$ to feasible positive space after each gradient step. We use Adam to optimize $\eta$ together with all other parameters. We refer to the appendix in section B for a derivation of this objective from RL as Inference perspective and the dual.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Using an identity transformation", "weight": 1.0} -->

An interesting other possibility is to use an identity transformation. While not respecting the desiderata from above, this would bring our method close to an expected policy gradient algorithm. We discuss this choice in detail in Section A in the appendix.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Using an identity transformation", "weight": 1.0} -->

1:given batch-size (N), Number of actions (K), Q-function Qπ(k)(target-network), old-policy π(k) (target network) and replay-buffer 2:initialize πθ from the parameters of π(k) 4: Sample batch of size N from replay buffer 5: // Step 2: sample based policy (weights) 11: qi j= Compute Weights({Qi j}i = 1 … N), see section 4.1 12: // Step 3: update parametric policy 13: Given the data-set {sj, (ai, qi j)i = 1 … N}j = 1 … K 14: Update the Policy by finding 15: $\pi^{({k + 1})} = {\operatorname{argmax}_{\theta}{\sum_{j}^{K}{\sum_{i}^{N}{q_{ij}{\log\pi_{\mathbf{θ}}}{(\left.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Using an identity transformation", "weight": 1.0} -->

a_{i} \middle| s_{j} \right.)}}}}}$ 16: (subject to additional (KL) regularization), see section 4.2 17:until Fixed number of steps Algorithm 2 KL Regularized Policy Improvement

<!-- chunk {"id": "body-0026", "role": "body", "section": "Fitting an improved policy (Step 3)", "weight": 1.0} -->

So far, for each state, we obtained an improved sample-based distribution over actions. Next, we want to generalize this sample-based solution over state and action space -- which is required when we want to select better actions in unseen situations during control. For this, we solve a weighted supervised learning problem where $\mathbf{θ}$ are the parameters of our function approximator (a neural network) which we initialize from the weights of the previous policy $\pi^{(k)}$. This objective corresponds to minimization of the KL divergence between the sample based distribution $\hat{\pi}$ from Step 2 and the parametric policy $\pi_{\theta}$, as given in Equation (2 ‣ Relative Entropy Regularized Policy Iteration")).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Fitting an improved policy (Step 3)", "weight": 1.0} -->

Unfortunately, sample based maximum likelihood estimation can suffer from overfitting to the samples from Step 2. Additionally, these sample weights themselves can be unreliable due to a poor approximation of $Q^{\pi^{(k)}}$ -- potentially resulting in a large change of the action distribution in the wrong direction when optimizing Equation (3 ‣ 4 Policy Improvement (Step 2-3) ‣ Relative Entropy Regularized Policy Iteration")). One effective regularization that addresses both concerns is to limit the overall change in the parametric policy. This additional regularization has a different effect than enforcing tighter constraints in Step 2, which would still only limit the change in the sample-based distribution. To direcly limit the change in the parametric policy (even in regions of the action space we have not sampled from) we thus employ an additional KL constraint^11^1We note that other commonly used regularization techniques might be worth investigating. and change the objective from Equation (3 ‣ 4 Policy Improvement (Step 2-3) ‣ Relative Entropy Regularized Policy Iteration")) to where $\epsilon_{\pi}$ denotes the allowed expected change over state distribution in KL divergence for the policy.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Fitting an improved policy (Step 3)", "weight": 1.0} -->

To make this objective amenable to gradient based optimization we employ Lagrangian Relaxation, yielding the following primal optimization problem: We solve for $\mathbf{θ}$ by iterating the inner and outer optimization programs independently: We fix the parameters $\mathbf{θ}$ to their current value and optimize for the Lagrangian multipliers (inner minimization) and then we fix the Lagrangian multipliers to their current value and optimize for $\mathbf{θ}$ (outer maximization). In practice we found it effective to simply perform one gradient step each in inner and outer optimization for each sampled batch of data. This lead to good satisfaction of the constraints throughout coordinate gradient decent training.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Fitting an improved Gaussian policy", "weight": 1.0} -->

The method described in the main part of Section 4.2 ‣ 4 Policy Improvement (Step 2-3) ‣ Relative Entropy Regularized Policy Iteration") works for any distribution. However, in particular for continuous action spaces it still can suffer from premature convergence as it is shown in Figure 1 ‣ 4 Policy Improvement (Step 2-3) ‣ Relative Entropy Regularized Policy Iteration")(left). The reason is that, in each policy improvement step we are essentially optimising for the expected reward for state given actions from the last policy. In such a setting, the optimal solution is to give a probability of 1 to the best action (or equal probabilities to equally good actions) based on its Q-value and zero to other actions. This means that the policy will collapse on the best action to optimise the expected reward even though the best action is not the true optimal action. We can postpone this effect by adding a KL constraint, however, in each iteration the policy will lose entropy to cover the best actions it has seen, albeit slowly, depending on the shape of $Q$ and the choice of $\epsilon_{\pi}$. And it therefore still can converge prematurely.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Fitting an improved Gaussian policy", "weight": 1.0} -->

We found that when using Gaussian policies, a simple change can avoid premature convergence in Step 3: we can decouple the objective for the policy mean and covariance matrix which, as intuitively described below, will fix this issue. This technique is also employed in the CMA-ES and TR-CMA-ES algorithms for bandit problems, but we generalize it to non-linear parameterizations. Concretely, we jointly optimize the neural network weights $\theta$ to maximize two objectives: one for updating the mean with the the covariance fixed to the one of the last policy (target network) and one for updating the covariance while fixing the mean to the one from the target network. This yields the following optimization objectives for the updated mean and covariance: Here, $\mu^{k}$ and $\Sigma^{k}$ respectively refer to the mean and covariance of obtained from the previous policy $\pi^{(k)}$ and ${\pi_{\mathbf{θ}}{(\left.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Fitting an improved Gaussian policy", "weight": 1.0} -->

a \middle| s \right.)}} = {\mathcal{N}{(\mu_{\theta},\Sigma_{\theta})}}$. We solve this optimization by performing gradient descent on an objective derived via the same Langrangian relaxation technique as in Section 4.2 ‣ 4 Policy Improvement (Step 2-3) ‣ Relative Entropy Regularized Policy Iteration").

<!-- chunk {"id": "body-0032", "role": "body", "section": "Fitting an improved Gaussian policy", "weight": 1.0} -->

This procedure has two advantages: 1) the gradient w.r.t. the parameters of the covariance is now independent of changes in the mean; hence the only way the policy can increase the likelihood of good samples far away from the mean is by stretching along the value landscape. This gives us the ability to grow and shrink the distribution supervised by samples without introducing any extra entropy term to the objective (see also Figures 1 ‣ 4 Policy Improvement (Step 2-3) ‣ Relative Entropy Regularized Policy Iteration") and 2 for an experiment showing this effect). 2) we can set the KL bound for mean and co-variance separately. The latter is especially useful in high-dimensional action spaces, where we want to avoid problems with ill-conditioning of the covariance matrix but want fast learning, enabled by large changes to the mean. The complete algorithm is listed in Algorithm 2 ‣ 4 Policy Improvement (Step 2-3) ‣ Relative Entropy Regularized Policy Iteration").

<!-- chunk {"id": "body-0033", "role": "body", "section": "Fitting an improved Gaussian policy", "weight": 1.0} -->

Please note that the objective we optimise here still is the weighted maximum likelihood objective from Equation 4 ‣ 4 Policy Improvement (Step 2-3) ‣ Relative Entropy Regularized Policy Iteration"), with the difference that we optimise it in a coordinate ascent fashion - resulting in the decoupled updates with different KL bounds. In general, such a procedure can also be applied for optimising different policy classes. For other distributions, such as mixtures of Gaussians, we can still use the same procedure and optimise for means, covariances and categorical distribution independently, getting the same effect as for the Gaussian case. If the policy is deterministic (as in DDPG) then the exploration variance is fixed and we would simply optimize the mean of a Gaussian. For categorical distributions each component can be optimized independently. However, the application of the coordinate ascent updates will have to be derived on a per distribution basis.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Results", "weight": 1.0} -->

To illustrate core features of our algorithm we first present results on two standard optimization problems. These highlight the benefit of decoupled maximum likelihood for Gaussian policies. We then perform experiments on 24 tasks from the DeepMind control suite, three high dimensional parkour tasks from and four high dimensional tasks from OpenAI gym. Depictions of task sets are in the appendix (Figure 9, 10).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Standard Functions", "weight": 1.0} -->

To isolate the evaluation of our policy improvement procedure from errors in the estimation of $Q^{\pi}$ we performed experiments using two fixed standard functions. We make both functions state and action dependent by first defining an auxiliary variable $y = {a + s}$, that varies linearly with to the action (the functions can thus seen as "ground truth" Q-functions. We consider: i) the sphere function ${Q{(a,s)}} = {- {\sum_{i = 1}^{N}y_{i}^{2}}}$, and ii) the well known Rosenbrock function ${Q{(a,s)}} = {- {\sum_{i = 1}^{n - 1}{\lbrack{{100{({y_{i + 1} - y_{i}^{2}})}^{2}} + {({1 - y_{i}^{2}})}}\rbrack}}}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Standard Functions", "weight": 1.0} -->

The global optimal action for state $s$ for both of these functions is given as $a^{\ast} = {- s}$; in which the optimal Q-value of zero is obtained. Instead of using a replay buffer, we sample 100 states from a uniform state distribution in the interval $\lbrack{- 2};2\rbrack$ for each batch and sample 10 actions from our current policy for calculating weights.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Standard Functions", "weight": 1.0} -->

The results for the dimensional sphere function are depicted in Figure 1 ‣ 4 Policy Improvement (Step 2-3) ‣ Relative Entropy Regularized Policy Iteration"). We plot the learning progress of the Gaussian policy for state $\lbrack 0;0\rbrack$ (every 20 iterations) for both the weighted MLE which also used by MPO and the decoupled optimization approach. The decoupled optimization starts by increasing the variance. Only when the optimum is found the variance start shrinking, and the distribution successfully converges on the optimum. The MLE procedure always shrinks variance, causing premature convergenceeven though we purposefully started with a larger variance for the MLE objective.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Continuous control benchmark tasks", "weight": 1.0} -->

(b) Sweep mean bound (c) Sweep mean bound (d) Sweep cov. bound Figure 3: (a): We evaluate the effect of using a KL bound for the decoupled MLE update in the humanoid-stand task. (b): We fix the KL bound on the covariance and evaluate three different bounds for the mean. The results clearly show that the most conservative bound on the change of the mean(0.001) leads to the best results. (c): Same as (b) but on the parkour-walls task. Here, we see that a loose bound on the mean decreases performance and a too tight bound slows down learning (d): we fix the KL bound on the mean and evaluate different bounds on the covariance (in the cheetah domain). Overall the results emphasize the importance of conservative updates.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experimental setup", "weight": 1.0} -->

Unless noted otherwise we use the decoupled updates proposed in Section 4.2.1 ‣ 4 Policy Improvement (Step 2-3) ‣ Relative Entropy Regularized Policy Iteration") in combination with the exponential transformation. Experiments with ranking based weights are given in the appendix in Section D. The policy is a state-conditional Gaussian parameterized by a feed-forward neural network. We use a single learner process on a GPU and a single actor process on a CPU to gather data from the environment, performing asynchronous learning from a replay buffer. Unlike e.g. in Barth-Maron et al., we do not perform distributed data collection. We use a single fixed set of hyperparameters across all tasks to show the reliability of the proposed algorithm. Details on all network architectures used, and the hyperparameters are given in the appendix in section G. For each task, we repeat the experiments five times and report the mean performance and standard deviation.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Control Suite Tasks", "weight": 1.0} -->

Full results are given in Figure 11 and Figure 12 in the appendix. We here focus on five domains for detailed comparisons: the acrobot (with 2 action dimensions), the swimmer (15 action dimensions), the cheetah (6 action dimensions), the humanoid (22 action dimensions) and the CMU humanoid (56 action dimension), as illustrated in the appendix in Figure 9.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Ablations", "weight": 1.0} -->

We consider four ablations of our algorithm comparing: i) the full algorithm, ii) no KL constraints ii) varying the strength of the KL on the mean, iii) varying the strength of the KL on the covariance. First, we compare the optimization with KL bounds on the mean and the covariance with a variant when there is no KL bound. I.e. fitting is performed via MLE. As depicted in Figure 3(a), without a constraint learning becomes unstable and considerably lower asymptotic performance is achieved. We found that decoupling the policy improvement objective for the mean and covariance can alleviate premature convergence. In Figures 3(c) and Figure 3(d) we compare for two environments different settings for the bounds on the mean while keeping the bound on the covariance fixed to the best value obtained via a grid-search, and vice versa. The results show that bounding both mean and covariance matrix is important to achieve stable performance. This is consistent with existing studies which have previously found that avoiding premature convergence (typically by tuning exploration noise) can be vitally important. In general, we find that constraints are important for reliable learning across tasks.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Parkour tasks", "weight": 1.0} -->

In this section, we consider three Parkour tasks. These tasks require the policy to steer a robotic body through an obstacle course, performing jumps and avoidance maneuvers. A depiction of the environments can be found in the appendix, Figure 10. We use the same setup and hyperparameters as in the previous section. This includes still using only one GPU for learning and one actor for interacting with the environment, a significant reduction in compute compared to the previously used 32-128 actors for solving these tasks. We compare two variants of our method with two variants of SVG and DDPG: a version with TD0 to fit the Q-function, and a version with Retrace.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Parkour tasks", "weight": 1.0} -->

As shown in Figure 5, only our method is able to solve all tasks. In addition, *our algorithm is capable of solving these challenging tasks while running on a single workstation*. Analyzing the results in more detail we can observe that learning the Q-function with TD leads to overall slower learning than when using Retrace, as well as to lower asymptotic performance. This gap increases with task complexity. Among the parkour tasks, *humanoid-3D gaps* is the hardest as it requires controlling a humanoid body to jump across gaps, see Figure 10 in the appendix. *Parkour-2D* is the easiest and only requires the policy to control a walker in a 2D environment. We observed a similar trend for other tasks although the difference is less dramatic on low-dimensional tasks such as the ones in the control suite.

<!-- chunk {"id": "body-0044", "role": "body", "section": "OpenAI Gym", "weight": 1.0} -->

Finally, we consider OpenAI gym tasks to compare our method with soft-actor critic algorithm (SAC) which is an actor-critic algorithm very similar to SVG that optimizes the entropy regularized objective expected reward objective. We use four tasks from OpenAI gym, i.e, Ant, Walker2d, Humanoid run, Humanoid stand-up for evaluating our method against SAC. For policy evaluation we use Retrace. We report the evaluation performance as in every 1000 environment steps and compare to their final performance. To obtain a similar data generation rate to we slowed down the actor such that it generated 1 trajectory each 5 seconds. We used the same hyperparameters for learning as we used for Parkour suite and DeepMind control suite. Our results in figure 6 show that we achieve considerably better asymptotic-performance than the ones reported by SAC in these environments with on-par sample efficiency. With thesame hyper parameters, our method also solves humanoid-stand with final return of 4000000 which is 100-1000 order of magnitude different than the final return of other environments.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We have presented a policy iteration algorithm for high-dimensional continuous control problems. The algorithm alternates between Q-value estimation, local policy improvement and parametric policy fitting; hard constraints control the rate of change of the policy. And a decoupled update for mean and covarinace of a Gaussian policy avoids premature convergence. Our analysis shows that when an approximate Q-function is used, slow updates to the policy can be critical to achieve reliable learning. Our comparison on 31 continuous control tasks with rather diverse properties using a limited amount of compute and a single set of hyperparameters demonstrate the robustness our method while it achieves state of art results.
