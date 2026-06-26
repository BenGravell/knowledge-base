<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

PAGE-PG: A Simple and Loopless Variance-Reduced Policy Gradient Method with Probabilistic Gradient Estimation

Topics include Policy gradients, Supervised learning, Probabilistic models, Sample complexity, Control, Learning, Sampling, PAGE-PG.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Despite their success, policy gradient methods suffer from high variance of the gradient estimate, which can result in unsatisfactory sample complexity. Recently, numerous variance-reduced extensions of policy gradient methods with provably better sample complexity and competitive numerical performance have been proposed. After a compact survey on some of the main variance-reduced REINFORCE-type methods, we propose ProbAbilistic Gradient Estimation for Policy Gradient (PAGE-PG), a novel loopless variance-reduced policy gradient method based on a probabilistic switch between two types of updates. Our method is inspired by the PAGE estimator for supervised learning and leverages importance sampling to obtain an unbiased gradient estimator. We show that PAGE-PG enjoys a O( epsilon^(-3) ) average sample complexity to reach an epsilon-stationary solution, which matches the sample complexity of its most competitive counterparts under the same setting. A numerical evaluation confirms the competitive performance of our method on classical control tasks.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Policy gradient methods have proved to be really effective in many challenging deep reinforcement learning (RL) applications. Their success is also due to their versatility as they are applicable to any differentiable policy parametrization, including complex neural networks, and they admit easy extensions to model-free settings and continuous state and action spaces. This class of methods has a long history in the RL literature that dates back to, but only very recent work has characterized their theoretical properties, such as convergence to a globally optimal solution and sample and iteration complexity. Since in RL it is generally not possible to compute the exact gradient, but we rely on sample-based approximations, policy gradient methods are negatively affected by the high-variance of the gradient estimate, which slows down convergence and leads to unsatisfactory sample complexity. To reduce the variance of the gradient estimators, actor-critic methods are deployed, where not only the policy, but also the state-action value function or the advantage function are parameterized. Alternatively, taking inspiration from stochastic optimization, various variance-reduced policy gradient methods have been proposed.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we focus on variance-reduced extensions of REINFORCE-type methods, such as REINFORCE, GPOMDP and their variants with baseline. After reviewing the principal variance-reduced extensions of REINFORCE-type methods, we introduce a novel variance-reduced policy gradient method, PAGE-PG, based on the recently proposed PAGE estimator for supervised learning. We prove that PAGE-PG only takes $\mathcal{O}\left( \epsilon^{- 3} \right)$ trajectories on average to achieve an $\epsilon$-stationary policy, which translates into a near-optimal solution for gradient dominated objectives. This result matches the bounds on total sample complexity of the most competitive variance-reduced REINFORCE-type methods under the same setting. The key feature of our method consists in replacing the double-loop structure typical of variance-reduced methods with a probabilistic switch between two types of updates. According to recent works in supervised learning, loopless variance-reduced methods are easier to tune, analyze and generally lead to superior and more robust practical behavior.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

For policy gradient optimization, similar advantages are discussed, where the authors propose STORM-PG, which, to the best of our knowledge, is the only other loopless variance-reduced policy gradient counterpart to our method. With respect to STORM-PG, our method enjoys a better theoretical rate of convergence. In addition, our experiments show the competitive performance of PAGE-PG on classical control tasks. Finally, we describe the limitations of the considered methods, discuss promising future extensions as well as the importance of incorporating noise annealing and adaptive strategies in the PAGE-PG's update. These might favor exploration in the early stages of training and improve convergence in presence of complex non-concave landscapes.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Main contributions. Our main contributions are summarized below.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose PAGE-PG, a novel loopless variance-reduced extension of REINFORCE-type methods based on a probabilistic update.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that PAGE-PG enjoys a fast rate of convergence and achieves an $\epsilon$-stationary policy within $\mathcal{O}\left( \epsilon^{- 3} \right)$ trajectories on average. We further show that, with gradient dominated objectives, similar results are valid for near-optimal solutions.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

In this section, we describe the problem setting and briefly discuss the necessary background material on REINFORCE-type policy gradient methods.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

Markov Decision Process. The RL paradigm is based on the interaction between an agent and the environment. In the standard setting, the agent observes the state of the environment and, based on that observation, plays an action according to a certain policy. As a consequence, the environment transits to a next state and a reward signal is emitted from the environment back to the agent. This process is repeated over a horizon of length $H > 0$, with $H < \infty$ in the episodic setting and $H\rightarrow\infty$ in the infinite-horizon setting. From a mathematical viewpoint, Markov Decision Processes (MDPs) are a widely utilized mathematical tool to describe RL tasks. In this work we consider discrete-time episodic MDPs $\mathcal{M} = \left\{ \mathcal{S},\mathcal{A},P,r,\gamma,\rho \right\}$, where $\mathcal{S}$ is the state space; $\mathcal{A}$ is the action space; $P$ is a Markovian transition model, where $P{(\left.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

s' \middle| {s,a} \right.)}$ defines the transition density to state $s'$ when taking action $a$ in state $s$; $r:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\lbrack{- R},R\rbrack}}$ is the reward function, where $R > 0$ is a constant; $\gamma \in {}$ is the discount factor; and $\rho$ is the initial state distribution. The agent selects the actions according to a stochastic stationary policy $\pi$, which, given a state $s$, defines a density distribution over the action space $\pi{( \cdot |s)}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

The value function $V^{\pi}:{\mathcal{S}\rightarrow{\mathbb{R}}}$ associated with a policy $\pi$ and initial state $s$ is defined as where the expectation is taken with respect to the trajectory distribution. With an overloaded notation, we denote with $V^{\pi}{(\rho)}$ the expected value under the initial state distribution $\rho$, i.e., The goal of the agent generally is to find the policy $\pi$ that maximizes $V^{\pi}{(\rho)}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

Policy Gradient. Given finite state and action spaces, the policy can be exactly coded with ${|\mathcal{S}|} \times {|\mathcal{A}|}$ parameters in the tabular setting. However, the tabular setting becomes intractable for large state and action spaces. In these scenarios, as well as in infinite countable and continuous spaces, we generally resort to parametric function approximations. In particular, instead of optimizing over the full space of stochastic stationary policies, we restrict our attention to the class of stochastic policies that is described by a finite-dimensional differentiable parametrization $\Pi_{\theta} = \left\{ \pi_{\theta} \middle| {\theta \in {\mathbb{R}}^{d}} \right\}$, such as a deep neural network. The addressed problem therefore becomes We denote with $V^{\ast}$ the optimal value.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

To simplify the notation, we use $V{(\theta)}$ to denote $V^{\pi_{\theta}}{(\rho)}$, $\theta$ to denote $\pi_{\theta}$ and ${R{(\tau)}} = {\sum_{h = 0}^{H - 1}{\gamma^{h}r{(s_{h},a_{h})}}}$ to denote the discounted cumulative reward associated with trajectory $\tau$. Problem can be addressed via gradient ascent, which updates the parameter vector by taking fixed steps of length $\eta > 0$ along the direction of the gradient. The iterations are defined as where the gradient is given by In the model-free setting, we cannot compute the exact gradient as we do not have access to the MDP dynamics.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

Instead, given a certain policy $\theta$, we simulate a finite number $N > 0$ of trajectories, which are then used to approximate Equation via Monte Carlo where each trajectory $\tau_{i} = \left\{ s_{h}^{i},a_{h}^{i} \right\}_{h = 0}^{H - 1}$ is generated according to the trajectory distribution $p{(\cdot |\theta)}$. The estimator in Equation is also known as the REINFORCE estimator. An alternative is given by the GPOMDP estimator where for compactness $Z_{\theta,h} = {\sum_{z = 0}^{h}{{{\nabla_{\theta}\log}\pi_{\theta}}{(\left. a_{z}^{i} \middle| s_{z}^{i} \right.)}}}$. Both REINFORCE and GPOMDP provide unbiased estimates of the gradient, but they are not equivalent in terms of variance.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

Specifically for GPOMDP, by only considering the reward-to-go instead of the full reward, we are removing potentially noisy terms and therefore lowering the variance of our estimate. In addition, since ${{\mathbb{E}}\left\lbrack {{{\nabla_{\theta}\log}\pi_{\theta}}{(\left. a \middle| s \right.)}b{(s)}} \right\rbrack} = 0$ with $b{(s)}$ being a function of the state, e.g. the value function $V^{\pi}{(s)}$, both the REINFORCE and GPOMDP estimators can be used in combination with a baseline.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Setting", "weight": 1.0} -->

The discussed estimators (with or without baseline) are deployed in place of the exact gradient in Equation, leading to the REINFORCE and GPOMDP algorithms. These methods are reminiscent of stochastic gradient ascent that also relies on sample-based estimators of the true gradient.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Variance-Reduced REINFORCE-type Methods", "weight": 1.0} -->

We now briefly review some of the state-of-the-art variance-reduced REINFORCE-type methods to solve Problem. We use $g{(\left. \tau \middle| \theta \right.)}$ and $g^{\omega_{\theta_{2}}}{(\left. \tau \middle| \theta_{1} \right.)}$ to refer to both the REINFORCE and GPOMDP estimators.\Stochastic Varaice-Reduced Policy Gradient (SVRPG), first proposed in and then further analyzed, adapts the stochastic variance-reduced gradient method for finite-sum problems to deal with the RL challenges as discussed above. The method is characterized by a double loop structure, where the outer iterations are called epochs. At the $s$-th epoch, a snapshot of the current iterate $\theta_{0}^{s}$ is taken.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Variance-Reduced REINFORCE-type Methods", "weight": 1.0} -->

Then, $N\operatorname{>>}1$ trajectories $\left\{ \tau_{i} \right\}_{i = 1}^{N}$ are collected based on the current policy and used to compute the gradient estimator $v_{0}^{s} = {\frac{1}{N}{\sum_{i = 1}^{N}{g{(\left. \tau_{i} \middle| \theta_{0}^{s} \right.)}}}}$. For every epoch, $m$ iterations in the inner loop are performed. At the $t$-th iteration of the inner loop with $t = {0,\ldots,{m - 1}}$, the parameter vector is updated by where $\eta > 0$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Variance-Reduced REINFORCE-type Methods", "weight": 1.0} -->

Then $B\operatorname{<<}N$ trajectories $\left\{ \tau_{j} \right\}_{j = 1}^{B}$ are collected according to the current policy $\theta_{t + 1}^{s}$ and an estimate of the gradient at $\theta_{t + 1}^{s}$ is produced After $m$ iterations in the inner loop, the snapshot is refreshed by setting $\theta_{0}^{s + 1} = \theta_{m}^{s}$, and the process is repeated for a fixed number of iterations. See Algorithm 1 in Section A of the Appendix.\Stochastic Recursive Variance-Reduced Policy Gradient (SRVRPG) is inspired from the SARAH method for supervised learning. Differently from SVRPG, SRVRPG incorporates in the update the concept of momentum, which helps convergence by dampening the oscillations typical of first-order methods.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Variance-Reduced REINFORCE-type Methods", "weight": 1.0} -->

In particular, the estimate produced in the inner iterations for all $t = {0,\ldots,{m - 1}}$ is where $\left\{ \tau_{i} \right\}_{i = 1}^{B}$ are generated according to policy $\theta_{t + 1}^{s}$ and $v_{0}^{s}$ is the large batch-size estimate computed at the $s$-th epoch. See Algorithm 2 in Section A of the Appendix.\Stochastic Recursive Momentum Policy Gradient (STORM-PG) blends the key components of STORM, a state-of-the-art variance-reduced gradient estimator for finite-sum problems, with policy gradient algorithms. A major drawback of SVRPG and SRVRPG is the restarting mechanism, namely, the alternation between large and small batches of sampled trajectories which ensures control of the variance. As discussed for the finite-sum scenario, the double-loop structure complicates the theoretical analysis and the tuning procedure.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Variance-Reduced REINFORCE-type Methods", "weight": 1.0} -->

STORM-PG circumvents the issue by deploying an exponential moving averaging mechanism that exponentially discounts the accumulated variance. The method only requires one to collect a large batch of trajectories at the first iteration and then relies on small batch updates. Specifically, STORM-PG starts by collecting $N\operatorname{>>}1$ trajectory samples $\left\{ \tau_{i} \right\}_{i = 1}^{N}$ according to an initial policy $\theta_{0}$. Those samples are deployed to calculate an initial gradient estimate $v_{0} = {\frac{1}{N}{\sum_{i = 1}^{N}{g{(\left. \tau_{i} \middle| \theta_{0} \right.)}}}}$, which is used in place of the gradient to update the parameter vector as in Equation.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Variance-Reduced REINFORCE-type Methods", "weight": 1.0} -->

Then $T$ iterations are performed where at the $t$-th iteration the parameter vector is updated as described in Equation, but replacing the gradient with the following estimate | | $v_{t} = {\frac{1}{B}{\sum\limits_{i = 1}^{B}{g{(\left. \tau_{i} \middle| \theta_{t} \right.)}}}}$ | $+ {(1 - \alpha)}\left\lbrack v_{t - 1} \right.$ | | \(12\) | | | | $\left.

<!-- chunk {"id": "body-0024", "role": "body", "section": "PAGE-PG", "weight": 1.0} -->

PAGE is a novel variance-reduced stochastic gradient estimator for Problem, where $f$ is differentiable but possibly non-convex. Let $\mathcal{B}_{t}$ be a set of randomly selected indices without replacement from $\left\{ 1,\ldots,n \right\}$ and ${|\mathcal{B}_{t}|} = B\operatorname{<<}n$, where the subscript $t$ refers to the iteration. The PAGE estimator is based on a small adjustment to the mini-batch gradient estimator. Specifically, it is initialized to the full gradient $g_{0} = {{\nabla_{\theta}f}{(\theta_{0})}}$ at $\theta_{0}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "PAGE-PG", "weight": 1.0} -->

the parameter vector in a gradient-descent fashion where $\eta > 0$ is a fixed step-size. Therefore, PAGE is based on switching with probability $p_{t}$ between gradient descent and a mini-batch version of SARAH.

<!-- chunk {"id": "body-0026", "role": "body", "section": "PAGE-PG", "weight": 1.0} -->

As suggested by its name, PAGE-PG is designed by blending the key ideas of PAGE with policy gradient methods. As discussed in Section 3, we can not simply use the PAGE estimator for policy gradient in its original formulation but some adjustments are required. In particular, we substitute the exact gradient computations with a stochastic estimate based on a large batch-size $N\operatorname{>>}B$. To deal with the distribution shift, we deploy importance weighting in a similar fashion as the variance-reduced policy gradient methods discussed in Section 3. PAGE-PG works by initially sampling $N$ trajectories with the initial policy $\theta_{0}$ and using those samples to build a solid gradient estimate $v_{0} = {\frac{1}{N}{\sum_{i = 1}^{N}{g{(\left. \tau_{i} \middle| \theta_{0} \right.)}}}}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "PAGE-PG", "weight": 1.0} -->

\tau_{i} \middle| \theta_{t - 1} \right.)}}}}} & {{{\text{prob.}\, 1} - p_{t}},} | | | where $\tau_{i}$ is drawn according to policy $\theta_{t}$ for any $i$. The parameter vector is updated according to Equation, where $v_{t}$ is deployed in place of the gradient. See Algorithm 4 in Section A of the Appendix for a pseudo-code description. As it appears in Equation, the double loop-structure that characterizes SVRPG and SRVRPG is replaced by a probabilistic switching between two estimators.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Theoretical Analysis", "weight": 1.0} -->

\tau_{i} \middle| {\theta_{2},\theta_{1}} \right.)}\gamma^{h}r{(s_{h}^{i},a_{h}^{i})}Z_{\theta_{1},h}}}$. We refer to Section C in the Appendix for the proofs and to Section B in the Appendix for the technical lemmas. After discussing the fundamental assumptions, we focus on studying the sample complexity of PAGE-PG to reach an $\epsilon$-stationary solution. We further show that, when the objective is gradient-dominated, since $\epsilon$-stationarity translates into near-optimality, the derived results are also valid for near-optimal solutions.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Theoretical Analysis", "weight": 1.0} -->

The theoretical analysis of variance-reduced policy gradient methods generally focuses on deriving, under certain assumptions, an upper bound on the number of sampled trajectories that are needed to achieve an $\epsilon$-stationary solution.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Assumption 4.5 (Finite importance weight variance)", "weight": 1.0} -->

The same set of assumptions is considered. By analyzing PAGE-PG in the same setting as its counterparts, we are able to compare them from a theoretical viewpoint.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 4.6", "weight": 1.0} -->

While the non-convex optimization community agrees on the rationality of Assumptions 4.2. ‣ 4.1 Theoretical Analysis ‣ 4 PAGE-PG ‣ PAGE-PG: A Simple and Loopless Variance-Reduced Policy Gradient Method with Probabilistic Gradient Estimation")-4.4. ‣ 4.1 Theoretical Analysis ‣ 4 PAGE-PG ‣ PAGE-PG: A Simple and Loopless Variance-Reduced Policy Gradient Method with Probabilistic Gradient Estimation"), in the authors argue that Assumption 4.5. ‣ 4.1 Theoretical Analysis ‣ 4 PAGE-PG ‣ PAGE-PG: A Simple and Loopless Variance-Reduced Policy Gradient Method with Probabilistic Gradient Estimation") on the boundedness of the importance weight variance is uncheckable and very stringent. In a more limited setting (finite MDPs only) than the one considered in this work, they are able to remove such assumption via the introduction of a gradient-truncation mechanism that provably controls the variance of the importance weights in off-policy sampling. This approach is for now outside the scope of this work, but can be addressed in future work by adopting a trust region policy optimisation perspective.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 4.6", "weight": 1.0} -->

In practice, to ensure that Assumption 4.5. ‣ 4.1 Theoretical Analysis ‣ 4 PAGE-PG ‣ PAGE-PG: A Simple and Loopless Variance-Reduced Policy Gradient Method with Probabilistic Gradient Estimation") is met, one can resort to small step-sizes so that ${p{(\left. \tau \middle| \theta_{b} \right.)}} \approx {p{(\left. \tau \middle| \theta_{a} \right.)}}$ and the weight is bounded. This, however, comes at the cost of slower convergence, as also confirmed by our numerical experiments in Section 5.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 4.6", "weight": 1.0} -->

For completeness, we report the following fundamental proposition, which is used consistently in our proofs.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Numerical Evaluation", "weight": 1.0} -->

In this section we numerically evaluate the performance of the discussed variance-reduced policy gradient methods on two state-of-the-art model-free reinforcement learning tasks from OpenAI Gym. In order to conduct the numerical evaluation of the discussed methods, we implemented them, along with GPOMDP, in a Pytorch-based toolbox. In addition, the toolbox interfaces OpenAI Gym allowing the user to easily train RL agents on different environments with the discussed methods. Finally, Pytorch provides the possibility of speeding up the computation via the deployment of graphical processing units (GPUs). The toolbox is publicly available at

<!-- chunk {"id": "body-0035", "role": "body", "section": "Benchmarks", "weight": 1.0} -->

For the empirical evaluation of the discussed methods we consider the Acrobot and the Cartpole environments from OpenAI Gym.\Acrobot. The Acrobot system comprises two joints and two links, where the joint between the two links is actuated. Initially, the links are hanging downwards, and the goal is to swing the end of the lower link up to a given height. A reward of $- 1$ is emitted every time the goal is not achieved. As soon as the target height is reached or $500$ time-steps are elapsed, the episode ends. The state space is continuous with dimension $6$. The action space is discrete and $3$ possible actions can be selected: apply a positive torque, apply a negative torque, do nothing. To model the policy, we use a neural softmax parametrization. In particular, we deploy a neural network with two hidden layers, width 32 for both layers and Tanh as activation function.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Benchmarks", "weight": 1.0} -->

Cartpole. The Cartpole system is a classical control environment that comprises a pole attached by an un-actuated joint to a cart that moves along a frictionless track. The pendulum starts upright, and the goal is to prevent it from falling over. A reward of $+ 1$ is provided for every time-step that the pole remains within 15 degrees from the upright position. The episode ends when the pole is more than 15 degrees from vertical, or the cart moves more than 2.4 units from its initial position. The state space is continuous with dimension $4$. The action space is discrete with 2 available actions: apply a force of $+ 1$ or $- 1$ to the cart. As for the Acrobot, to model the policy we use a neural softmax parametrization. In particular, we deploy a neural network with two hidden layers, width 32 for both layers and Tanh as activation function. The maximum episode length is set to 200.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Benchmarks", "weight": 1.0} -->

We set $N = 100$, $B = 5$ and $m = 10$ and $\gamma = 0.9999$, while the step-size and the other hyperparameters are tuned for each individual algorithm using grid search. See Section D in the Appendix for more details on the choice of the hyperparameters. For each algorithm, we run the experiment 5 times with random initialization of the environments. The curves (solid-lines) are obtained by taking the mean over the independent runs and the shaded areas represent the $\pm \sigma$ standard deviations.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Benchmarks", "weight": 1.0} -->

The experiments in Figures 1 and 2 show that, given enough episodes, all of the algorithms are able to solve the tasks, achieving near-optimal returns. For the Acrobot environment in Figure 1, the SRVRPG and GPOMDP algorithms take the biggest number of episodes to find an optimal policy, while STORM-PG and SVRPG are the fastest in terms of number of episodes. This might be due to the step-size, which, for certain methods, needs to be set to particularly small values to enforce finite importance weight variance and ensure convergence. For the Cartpole environment in Figure 2, as expected, the GPOMDP algorithm takes the longest to find the optimal policy, followed in order by SVRPG, SRVRPG, STORM-PG and PAGE-PG. Notice that these empirical observations corroborate the theoretical findings on the sample complexity. Finally, our benchmarks demonstrate the competitive performance of PAGE-PG with respect to its counterparts.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Conclusions, Limitations & Future Works", "weight": 1.0} -->

After a brief survey on the main variance reduced policy gradient methods based on REINFORCE-type algorithms, we formulate a novel variance-reduced extension, PAGE-PG, inspired from the PAGE gradient estimator for optimization of non-convex finite-sum problems. To the best of the authors' knowledge, our method is the first variance-reduced policy gradient method that replaces the outer loop with a probabilistic switch. This key feature of PAGE-PG facilitates the theoretical analysis while preserving a fast theoretical rate and a low sample complexity. In addition, our numerical evaluation shows that PAGE-PG has a competitive performance with respect to its counterparts.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Conclusions, Limitations & Future Works", "weight": 1.0} -->

Our benchmarks and theoretical results on the sample complexity confirm that variance-reduced techniques successfully manage to reduce the sample complexity of REINFORCE-type algorithms, speeding up the convergence in terms of number of sampled trajectories. At the same time, it is possible to identify the following limitations:\Unrealistic and uncheckable assumption on importance weight variance. As underlined in Remark 4.6, all the discussed variance-reduced policy gradient methods heavily rely on the stringent and uncheckable assumption that the importance weights have bounded variance for every iteration of the algorithms (Assumption 4.5. ‣ 4.1 Theoretical Analysis ‣ 4 PAGE-PG ‣ PAGE-PG: A Simple and Loopless Variance-Reduced Policy Gradient Method with Probabilistic Gradient Estimation")). To enforce indirectly this assumption, very small values of the step-size are needed, resulting in a dramatic slow-down of the convergence rate. A more efficient alternative could be the deployment of a gradient-truncation strategy, as proposed in for the case of finite MDPs.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Conclusions, Limitations & Future Works", "weight": 1.0} -->

This modification, which corresponds to the solution of a trust-region subproblem, is simple and efficient since it does not involve significant extra computational costs but, at the same time, requires to migrate from vanilla REINFORCE-type methods to trust-region based algorithms such as TRPO and PPO for comparisons.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conclusions, Limitations & Future Works", "weight": 1.0} -->

Extreme sensitivity to hyperparameters. Our benchmarks suggest an extreme sensitivity to the hyperparameters, especially the choice of the step-size. Time-consuming and resource-expensive tuning procedures are required to select a proper configuration of hyperparameters. To alleviate this issue, the update direction should be computed also taking into account second-order information. Second-order methods are notably more robust against the step-size selection than first-order methods, since their update includes information on the local curvature.\Noise annealing strategies. Empirical evidence suggests that, in the presence of complex non-concave landscapes, exploration in the form of noise injection is of critical importance in the early stages of training to prevent convergence to spurious local maximizers. Entropy regularization is often used to improve exploration, since it indirectly injects noise in the training process by favoring the selection of more stochastic policies. Unfortunately, by adding a regularizer to Problem we are effectively changing the optimal policy. An alternative approach would be increasing the batch-size during training. In this perspective, a promising heuristic to further improve the convergence of PAGE-PG could consist in gradually increasing the probability of switching $p_{t}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusions, Limitations & Future Works", "weight": 1.0} -->

Finally, as also pointed out, since the variance of the updates depends on the snapshot policy as well as on the sampled trajectories, it is realistic to imagine that predefined schemes for the probability of switching are not going to perform as well as adaptive ones, which adjust the value of $p_{t}$ based on some measure of the variance.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusions, Limitations & Future Works", "weight": 1.0} -->

We leave for future development the aforementioned extensions, which we believe would counteract the current limitations of the analyzed methods.
