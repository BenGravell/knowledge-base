<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

High-Dimensional Continuous Control Using Generalized Advantage Estimation

Topics include Policy gradients, Reinforcement learning, Robotics, Neural networks, Online algorithms, Optimization, Control, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Policy gradient methods are an appealing approach in reinforcement learning because they directly optimize the cumulative reward and can straightforwardly be used with nonlinear function approximators such as neural networks. The two main challenges are the large number of samples typically required, and the difficulty of obtaining stable and steady improvement despite the nonstationarity of the incoming data. We address the first challenge by using value functions to substantially reduce the variance of policy gradient estimates at the cost of some bias, with an exponentially-weighted estimator of the advantage function that is analogous to TD(lambda). We address the second challenge by using trust region optimization procedure for both the policy and the value function, which are represented by neural networks. Our approach yields strong empirical results on highly challenging 3D locomotion tasks, learning running gaits for bipedal and quadrupedal simulated robots, and learning a policy for getting the biped to stand up from starting out lying on the ground. In contrast to a body of prior work that uses hand-crafted policy representations, our neural network policies map directly from raw kinematics to joint torques.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Our algorithm is fully model-free, and the amount of simulated experience required for the learning tasks on 3D bipeds corresponds to 1-2 weeks of real time.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The typical problem formulation in reinforcement learning is to maximize the expected total reward of a policy. A key source of difficulty is the long time delay between actions and their positive or negative effect on rewards; this issue is called the credit assignment problem in the reinforcement learning literature, and the distal reward problem in the behavioral literature. Value functions offer an elegant solution to the credit assignment problem---they allow us to estimate the goodness of an action before the delayed reward arrives. Reinforcement learning algorithms make use of value functions in a variety of different ways; this paper considers algorithms that optimize a parameterized policy and use value functions to help estimate how the policy should be improved.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

When using a parameterized stochastic policy, it is possible to obtain an unbiased estimate of the gradient of the expected total returns; these noisy gradient estimates can be used in a stochastic gradient ascent algorithm. Unfortunately, the variance of the gradient estimator scales unfavorably with the time horizon, since the effect of an action is confounded with the effects of past and future actions. Another class of policy gradient algorithms, called actor-critic methods, use a value function rather than the empirical returns, obtaining an estimator with lower variance at the cost of introducing bias. But while high variance necessitates using more samples, bias is more pernicious---even with an unlimited number of samples, bias can cause the algorithm to fail to converge, or to converge to a poor solution that is not even a local optimum.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose a family of policy gradient estimators that significantly reduce variance while maintaining a tolerable level of bias. We call this estimation scheme, parameterized by $\gamma \in {\lbrack 0,1\rbrack}$ and $\lambda \in {\lbrack 0,1\rbrack}$, the generalized advantage estimator (GAE). Related methods have been proposed in the context of online actor-critic methods. We provide a more general analysis, which is applicable in both the online and batch settings, and discuss an interpretation of our method as an instance of reward shaping, where the approximate value function is used to shape the reward.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We present experimental results on a number of highly challenging 3D locomotion tasks, where we show that our approach can learn complex gaits using high-dimensional, general purpose neural network function approximators for both the policy and the value function, each with over $10^{4}$ parameters. The policies perform torque-level control of simulated 3D robots with up to 33 state dimensions and 10 actuators.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The contributions of this paper are summarized as follows: We provide justification and intuition for an effective variance reduction scheme for policy gradients, which we call generalized advantage estimation (GAE). While the formula has been proposed in prior work, our analysis is novel and enables GAE to be applied with a more general set of algorithms, including the batch trust-region algorithm we use for our experiments.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose the use of a trust region optimization method for the value function, which we find is a robust and efficient way to train neural network value functions with thousands of parameters.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

By combining and above, we obtain an algorithm that empirically is effective at learning neural network policies for challenging control tasks. The results extend the state of the art in using reinforcement learning for high-dimensional continuous control. Videos are available at

<!-- chunk {"id": "body-0011", "role": "body", "section": "Advantage function estimation", "weight": 1.0} -->

This section will be concerned with producing an accurate estimate ${\hat{A}}_{t}$ of the discounted advantage function $A^{\pi,\gamma}{(s_{t},a_{t})}$, which will then be used to construct a policy gradient estimator of the following form: where $n$ indexes over a batch of episodes.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Advantage function estimation", "weight": 1.0} -->

Let $V$ be an approximate value function. Define $\delta_{t}^{V} = {{r_{t} + {\gammaV{(s_{t + 1})}}} - {V{(s_{t})}}}$, i.e., the TD residual of $V$ with discount $\gamma$. Note that $\delta_{t}^{V}$ can be considered as an estimate of the advantage of the action $a_{t}$. In fact, if we have the correct value function $V = V^{\pi,\gamma}$, then it is a $\gamma$-just advantage estimator, and in fact, an unbiased estimator of $A^{\pi,\gamma}$: However, this estimator is only $\gamma$-just for $V = V^{\pi,\gamma}$, otherwise it will yield biased policy gradient estimates.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Advantage function estimation", "weight": 1.0} -->

Next, let us consider taking the sum of $k$ of these $\delta$ terms, which we will denote by ${\hat{A}}_{t}^{(k)}$ These equations result from a telescoping sum, and we see that ${\hat{A}}_{t}^{(k)}$ involves a $k$-step estimate of the returns, minus a baseline term $- {V{(s_{t})}}$. Analogously to the case of $\delta_{t}^{V} = {\hat{A}}_{t}^{}$, we can consider ${\hat{A}}_{t}^{(k)}$ to be an estimator of the advantage function, which is only $\gamma$-just when $V = V^{\pi,\gamma}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Advantage function estimation", "weight": 1.0} -->

However, note that the bias generally becomes smaller as $k\rightarrow\infty$, since the term $\gamma^{k}V{(s_{t + k})}$ becomes more heavily discounted, and the term $- {V{(s_{t})}}$ does not affect the bias. Taking $k\rightarrow\infty$, we get which is simply the empirical returns minus the value function baseline.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Advantage function estimation", "weight": 1.0} -->

The generalized advantage estimator ${GAE}{(\gamma,\lambda)}$ is defined as the exponentially-weighted average of these $k$-step estimators: From Equation 16, we see that the advantage estimator has a remarkably simple formula involving a discounted sum of Bellman residual terms. Section 4 discusses an interpretation of this formula as the returns in an MDP with a modified reward function. The construction we used above is closely analogous to the one used to define TD($\lambda$), however TD($\lambda$) is an estimator of the value function, whereas here we are estimating the advantage function.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Advantage function estimation", "weight": 1.0} -->

There are two notable special cases of this formula, obtained by setting $\lambda = 0$ and $\lambda = 1$. ${GAE}{(\gamma,1)}$ is $\gamma$-just regardless of the accuracy of $V$, but it has high variance due to the sum of terms. ${GAE}{(\gamma,0)}$ is $\gamma$-just for $V = V^{\pi,\gamma}$ and otherwise induces bias, but it typically has much lower variance. The generalized advantage estimator for $0 < \lambda < 1$ makes a compromise between bias and variance, controlled by parameter $\lambda$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Advantage function estimation", "weight": 1.0} -->

We've described an advantage estimator with two separate parameters $\gamma$ and $\lambda$, both of which contribute to the bias-variance tradeoff when using an approximate value function. However, they serve different purposes and work best with different ranges of values. $\gamma$ most importantly determines the scale of the value function $V^{\pi,\gamma}$, which does not depend on $\lambda$. Taking $\gamma < 1$ introduces bias into the policy gradient estimate, regardless of the value function's accuracy. On the other hand, $\lambda < 1$ introduces bias only when the value function is inaccurate. Empirically, we find that the best value of $\lambda$ is much lower than the best value of $\gamma$, likely because $\lambda$ introduces far less bias than $\gamma$ for a reasonably accurate value function.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Advantage function estimation", "weight": 1.0} -->

Using the generalized advantage estimator, we can construct a biased estimator of $g^{\gamma}$, the discounted policy gradient from Equation 6: where equality holds when $\lambda = 1$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Interpretation as Reward Shaping", "weight": 1.0} -->

In this section, we discuss how one can interpret $\lambda$ as an extra discount factor applied after performing a reward shaping transformation on the MDP. We also introduce the notion of a response function to help understand the bias introduced by $\gamma$ and $\lambda$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Interpretation as Reward Shaping", "weight": 1.0} -->

Reward shaping refers to the following transformation of the reward function of an MDP: let $\Phi:{\mathcal{S}\rightarrow{\mathbb{R}}}$ be an arbitrary scalar-valued function on state space, and define the transformed reward function $\overset{\sim}{r}$ by which in turn defines a transformed MDP. This transformation leaves the discounted advantage function $A^{\pi,\gamma}$ unchanged for any policy $\pi$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Interpretation as Reward Shaping", "weight": 1.0} -->

To see this, consider the discounted sum of rewards of a trajectory starting with state $s_{t}$: Letting ${\overset{\sim}{Q}}^{\pi,\gamma},{\overset{\sim}{V}}^{\pi,\gamma},{\overset{\sim}{A}}^{\pi,\gamma}$ be the value and advantage functions of the transformed MDP, one obtains from the definitions of these quantities that Note that if $\Phi$ happens to be the state-value function $V^{\pi,\gamma}$ from the original MDP, then the transformed MDP has the interesting property that ${\overset{\sim}{V}}^{\pi,\gamma}{(s)}$ is zero at every state.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Interpretation as Reward Shaping", "weight": 1.0} -->

Note that showed that the reward shaping transformation leaves the policy gradient and optimal policy unchanged when our objective is to maximize the discounted sum of rewards $\sum_{t = 0}^{\infty}{\gamma^{t}r{(s_{t},a_{t},s_{t + 1})}}$. In contrast, this paper is concerned with maximizing the undiscounted sum of rewards, where the discount $\gamma$ is used as a variance-reduction parameter.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Interpretation as Reward Shaping", "weight": 1.0} -->

Having reviewed the idea of reward shaping, let us consider how we could use it to get a policy gradient estimate. The most natural approach is to construct policy gradient estimators that use discounted sums of shaped rewards $\overset{\sim}{r}$. However, Equation 21 shows that we obtain the discounted sum of the original MDP's rewards $r$ minus a baseline term. Next, let's consider using a "steeper" discount $\gamma\lambda$, where $0 \leq \lambda \leq 1$. It's easy to see that the shaped reward $\overset{\sim}{r}$ equals the Bellman residual term $\delta^{V}$, introduced in Section 3, where we set $\Phi = V$. Letting $\Phi = V$, we see that Hence, by considering the $\gamma\lambda$-discounted sum of shaped rewards, we exactly obtain the generalized advantage estimators from Section 3. As shown previously, $\lambda = 1$ gives an unbiased estimate of $g^{\gamma}$, whereas $\lambda < 1$ gives a biased estimate.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Interpretation as Reward Shaping", "weight": 1.0} -->

To further analyze the effect of this shaping transformation and parameters $\gamma$ and $\lambda$, it will be useful to introduce the notion of a response function $\chi$, which we define as follows: Note that ${A^{\pi,\gamma}{(s,a)}} = {\sum_{l = 0}^{\infty}{\gamma^{l}\chi{(l;s,a)}}}$, hence the response function decomposes the advantage function across timesteps. The response function lets us quantify the temporal credit assignment problem: long range dependencies between actions and rewards correspond to nonzero values of the response function for $l \gg 0$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Interpretation as Reward Shaping", "weight": 1.0} -->

Next, let us revisit the discount factor $\gamma$ and the approximation we are making by using $A^{\pi,\gamma}$ rather than $A^{\pi,1}$. The discounted policy gradient estimator from Equation 6 has a sum of terms of the form Using a discount $\gamma < 1$ corresponds to dropping the terms with $l \gg {1/{({1 - \gamma})}}$. Thus, the error introduced by this approximation will be small if $\chi$ rapidly decays as $l$ increases, i.e., if the effect of an action on rewards is "forgotten" after $\approx {1/{({1 - \gamma})}}$ timesteps.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Interpretation as Reward Shaping", "weight": 1.0} -->

If the reward function $\overset{\sim}{r}$ were obtained using $\Phi = V^{\pi,\gamma}$, we would have ${{\mathbb{E}}\left\lbrack {\overset{\sim}{r}}_{t + l} \middle| {s_{t},a_{t}} \right\rbrack} = {{\mathbb{E}}\left\lbrack {\overset{\sim}{r}}_{t + l} \middle| s_{t} \right\rbrack} = 0$ for $l > 0$, i.e., the response function would only be nonzero at $l = 0$. Therefore, this shaping transformation would turn temporally extended response into an immediate response. Given that $V^{\pi,\gamma}$ completely reduces the temporal spread of the response function, we can hope that a good approximation $V \approx V^{\pi,\gamma}$ partially reduces it.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Interpretation as Reward Shaping", "weight": 1.0} -->

This observation suggests an interpretation of Equation 16: reshape the rewards using $V$ to shrink the temporal extent of the response function, and then introduce a "steeper" discount $\gamma\lambda$ to cut off the noise arising from long delays, i.e., ignore terms ${{\nabla_{\theta}\log}\pi_{\theta}}{(\left. a_{t} \middle| s_{t} \right.)}\delta_{t + l}^{V}$ where $l \gg {1/{({1 - {\gamma\lambda}})}}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Value Function Estimation", "weight": 1.0} -->

A variety of different methods can be used to estimate the value function (see, e.g., Bertsekas). When using a nonlinear function approximator to represent the value function, the simplest approach is to solve a nonlinear regression problem: where ${\hat{V}}_{t} = {\sum_{l = 0}^{\infty}{\gamma^{l}r_{t + l}}}$ is the discounted sum of rewards, and $n$ indexes over all timesteps in a batch of trajectories.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Value Function Estimation", "weight": 1.0} -->

This is sometimes called the Monte Carlo or TD($1$) approach for estimating the value function.^22^2Another natural choice is to compute target values with an estimator based on the TD($\lambda$) backup, mirroring the expression we use for policy gradient estimation: $\hat{V_{t}^{\lambda}} = {{V_{\phi_{\text{old}}}{(s_{n})}} + {\sum_{l = 0}^{\infty}{{({\gamma\lambda})}^{l}\delta_{t + l}}}}$. While we experimented with this choice, we did not notice a difference in performance from the $\lambda = 1$ estimator in Equation 28.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Value Function Estimation", "weight": 1.0} -->

For the experiments in this work, we used a trust region method to optimize the value function in each iteration of a batch optimization procedure. The trust region helps us to avoid overfitting to the most recent batch of data. To formulate the trust region problem, we first compute $\sigma^{2} = {\frac{1}{N}{\sum_{n = 1}^{N}{\|{{V_{\phi_{\text{old}}}{(s_{n})}} - {\hat{V}}_{n}}\|}^{2}}}$, where $\phi_{\text{old}}$ is the parameter vector before optimization. Then we solve the following constrained optimization problem: This constraint is equivalent to constraining the average KL divergence between the previous value function and the new value function to be smaller than $\epsilon$, where the value function is taken to parameterize a conditional Gaussian distribution with mean $V_{\phi}{(s)}$ and variance $\sigma^{2}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Value Function Estimation", "weight": 1.0} -->

We compute an approximate solution to the trust region problem using the conjugate gradient algorithm. Specifically, we are solving the quadratic program where $g$ is the gradient of the objective, and $H = {\frac{1}{N}{\sum_{n}{j_{n}j_{n}^{T}}}}$, where $j_{n} = {{\nabla_{\phi}V_{\phi}}{(s_{n})}}$. Note that $H$ is the "Gauss-Newton" approximation of the Hessian of the objective, and it is (up to a $\sigma^{2}$ factor) the Fisher information matrix when interpreting the value function as a conditional probability distribution. Using matrix-vector products $v\rightarrow{Hv}$ to implement the conjugate gradient algorithm, we compute a step direction $s \approx {- {H^{- 1}g}}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Value Function Estimation", "weight": 1.0} -->

Then we rescale $s\rightarrow{\alphas}$ such that ${\frac{1}{2}{({\alphas})}^{T}H{({\alphas})}} = \epsilon$ and take $\phi = {\phi_{\text{old}} + {\alphas}}$. This procedure is analogous to the procedure we use for updating the policy, which is described further in Section 6 and based on Schulman et al..

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

We designed a set of experiments to investigate the following questions: What is the empirical effect of varying $\lambda \in {\lbrack 0,1\rbrack}$ and $\gamma \in {\lbrack 0,1\rbrack}$ when optimizing episodic total reward using generalized advantage estimation?

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments", "weight": 1.0} -->

Can generalized advantage estimation, along with trust region algorithms for policy and value function optimization, be used to optimize large neural network policies for challenging control problems?

<!-- chunk {"id": "body-0035", "role": "body", "section": "Policy Optimization Algorithm", "weight": 1.0} -->

While generalized advantage estimation can be used along with a variety of different policy gradient methods, for these experiments, we performed the policy updates using trust region policy optimization (TRPO). TRPO updates the policy by approximately solving the following constrained optimization problem each iteration: As described, we approximately solve this problem by linearizing the objective and quadraticizing the constraint, which yields a step in the direction ${\theta - \theta_{old}} \propto {- {F^{- 1}g}}$, where $F$ is the average Fisher information matrix, and $g$ is a policy gradient estimate. This policy update yields the same step direction as the natural policy gradient and natural actor-critic, however it uses a different stepsize determination scheme and numerical procedure for computing the step.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Policy Optimization Algorithm", "weight": 1.0} -->

Since prior work compared TRPO to a variety of different policy optimization algorithms, we will not repeat these comparisons; rather, we will focus on varying the $\gamma,\lambda$ parameters of policy gradient estimator while keeping the underlying algorithm fixed.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Policy Optimization Algorithm", "weight": 1.0} -->

For completeness, the whole algorithm for iteratively updating policy and value function is given below: Initialize policy parameter θ0 and value function parameter ϕ0. Simulate current policy πθi until N timesteps are obtained. Compute δtV at all timesteps t ∈ {1, 2, …, N}, using V = Vϕi. Compute ${\hat{A}}_{t} = {\sum_{l = 0}^{\infty}{{({\gamma\lambda})}^{l}\delta_{t + l}^{V}}}$ at all timesteps. Compute θi + 1 with TRPO update, Equation 31. Compute ϕi + 1 with Equation 30.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Policy Optimization Algorithm", "weight": 1.0} -->

Note that the policy update $\theta_{i}\rightarrow\theta_{i + 1}$ is performed using the value function $V_{\phi_{i}}$ for advantage estimation, not $V_{\phi_{i + 1}}$. Additional bias would have been introduced if we updated the value function first. To see this, consider the extreme case where we overfit the value function, and the Bellman residual ${r_{t} + {\gammaV{(s_{t + 1})}}} - {V{(s_{t})}}$ becomes zero at all timesteps---the policy gradient estimate would be zero.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Architecture", "weight": 1.0} -->

We used the same neural network architecture for all of the 3D robot tasks, which was a feedforward network with three hidden layers, with $100$, $50$ and $25$ tanh units respectively. The same architecture was used for the policy and value function. The final output layer had linear activation. The value function estimator used the same architecture, but with only one scalar output. For the simpler cart-pole task, we used a linear policy, and a neural network with one 20-unit hidden layer as the value function.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Task details", "weight": 1.0} -->

For the cart-pole balancing task, we collected 20 trajectories per batch, with a maximum length of 1000 timesteps, using the physical parameters from Barto et al..

<!-- chunk {"id": "body-0041", "role": "body", "section": "Task details", "weight": 1.0} -->

The simulated robot tasks were simulated using the MuJoCo physics engine. The humanoid model has 33 state dimensions and 10 actuated degrees of freedom, while the quadruped model has 29 state dimensions and 8 actuated degrees of freedom. The initial state for these tasks consisted of a uniform distribution centered on a reference configuration. We used 50000 timesteps per batch for bipedal locomotion, and 200000 timesteps per batch for quadrupedal locomotion and bipedal standing. Each episode was terminated after $2000$ timesteps if the robot had not reached a terminal state beforehand. The timestep was $0.01$ seconds.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Task details", "weight": 1.0} -->

The reward functions are provided in the table below.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Task details", "weight": 1.0} -->

In the locomotion tasks, the episode is terminated if the center of mass of the actor falls below a predefined height: $8.m$ for the biped, and $2.m$ for the quadruped. The constant offset in the reward function encourages longer episodes; otherwise the quadratic reward terms might lead lead to a policy that ends the episodes as quickly as possible.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

All results are presented in terms of the cost, which is defined as negative reward and is minimized. Videos of the learned policies are available at In plots, "No VF" means that we used a time-dependent baseline that did not depend on the state, rather than an estimate of the state value function. The time-dependent baseline was computed by averaging the return at each timestep over the trajectories in the batch.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Cart-pole", "weight": 1.0} -->

The results are averaged across $21$ experiments with different random seeds. Results are shown in Figure 2, and indicate that the best results are obtained at intermediate values of the parameters: $\gamma \in {\lbrack 0.96,0.99\rbrack}$ and $\lambda \in {\lbrack 0.92,0.99\rbrack}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "3D bipedal locomotion", "weight": 1.0} -->

Each trial took about 2 hours to run on a 16-core machine, where the simulation rollouts were parallelized, as were the function, gradient, and matrix-vector-product evaluations used when optimizing the policy and value function. Here, the results are averaged across $9$ trials with different random seeds. The best performance is again obtained using intermediate values of ${\gamma \in {\lbrack 0.99,0.995\rbrack}},{\lambda \in {\lbrack 0.96,0.99\rbrack}}$. The result after 1000 iterations is a fast, smooth, and stable gait that is effectively completely stable. We can compute how much "real time" was used for this learning process: ${{{{{{{{0.01{{seconds}/{timestep}}} \times 50000}{{timesteps}/{batch}}} \times 1000}{batches}}/3600} \cdot 24}{{seconds}/{day}}} = {5.8{days}}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "3D bipedal locomotion", "weight": 1.0} -->

Hence, it is plausible that this algorithm could be run on a real robot, or multiple real robots learning in parallel, if there were a way to reset the state of the robot and ensure that it doesn't damage itself.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Other 3D robot tasks", "weight": 1.0} -->

The other two motor behaviors considered are quadrupedal locomotion and getting up off the ground for the 3D biped. Again, we performed 5 trials per experimental condition, with different random seeds (and initializations). The experiments took about 4 hours per trial on a 32-core machine. We performed a more limited comparison on these domains (due to the substantial computational resources required to run these experiments), fixing $\gamma = 0.995$ but varying $\lambda = {\{ 0,0.96\}}$, as well as an experimental condition with no value function. For quadrupedal locomotion, the best results are obtained using a value function with $\lambda = 0.96$ Figure 3. For 3D standing, the value function always helped, but the results are roughly the same for $\lambda = 0.96$ and $\lambda = 1$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Discussion", "weight": 1.5} -->

Policy gradient methods provide a way to reduce reinforcement learning to stochastic gradient descent, by providing unbiased gradient estimates. However, so far their success at solving difficult control problems has been limited, largely due to their high sample complexity. We have argued that the key to variance reduction is to obtain good estimates of the advantage function.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Discussion", "weight": 1.5} -->

We have provided an intuitive but informal analysis of the problem of advantage function estimation, and justified the generalized advantage estimator, which has two parameters $\gamma,\lambda$ which adjust the bias-variance tradeoff. We described how to combine this idea with trust region policy optimization and a trust region algorithm that optimizes a value function, both represented by neural networks. Combining these techniques, we are able to learn to solve difficult control tasks that have previously been out of reach for generic reinforcement learning methods.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Discussion", "weight": 1.5} -->

Our main experimental validation of generalized advantage estimation is in the domain of simulated robotic locomotion. As shown in our experiments, choosing an appropriate intermediate value of $\lambda$ in the range $\lbrack 0.9,0.99\rbrack$ usually results in the best performance. A possible topic for future work is how to adjust the estimator parameters $\gamma,\lambda$ in an adaptive or automatic way.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Discussion", "weight": 1.5} -->

One question that merits future investigation is the relationship between value function estimation error and policy gradient estimation error. If this relationship were known, we could choose an error metric for value function fitting that is well-matched to the quantity of interest, which is typically the accuracy of the policy gradient estimation. Some candidates for such an error metric might include the Bellman error or projected Bellman error, as described in Bhatnagar et al..

<!-- chunk {"id": "body-0053", "role": "body", "section": "Discussion", "weight": 1.5} -->

Another enticing possibility is to use a shared function approximation architecture for the policy and the value function, while optimizing the policy using generalized advantage estimation. While formulating this problem in a way that is suitable for numerical optimization and provides convergence guarantees remains an open question, such an approach could allow the value function and policy representations to share useful features of the input, resulting in even faster learning.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Discussion", "weight": 1.5} -->

In concurrent work, researchers have been developing policy gradient methods that involve differentiation with respect to the continuous-valued action. While we found empirically that the one-step return ($\lambda = 0$) leads to excessive bias and poor performance, these papers show that such methods can work when tuned appropriately. However, note that those papers consider control problems with substantially lower-dimensional state and action spaces than the ones considered here. A comparison between both classes of approach would be useful for future work.
