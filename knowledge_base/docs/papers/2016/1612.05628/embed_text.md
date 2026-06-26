## Introduction

There is a fundamental tension in decision making between choosing the action that has highest expected utility and avoiding "starving" the other actions. The issue arises in the context of the exploration--exploitation dilemma, non-stationary decision problems, and when interpreting observed decisions.

In reinforcement learning, an approach to addressing the tension is the use of *softmax* operators for value-function optimization, and softmax policies for action selection. Examples include value-based methods such as SARSA or expected SARSA, and policy-search methods such as REINFORCE.

An ideal softmax operator is a parameterized set of operators that: has parameter settings that allow it to approximate maximization arbitrarily accurately to perform reward-seeking behavior; is a non-expansion for all parameter settings ensuring convergence to a unique fixed point; is differentiable to make it possible to improve via gradient-based optimization; and avoids the starvation of non-maximizing actions.

Let $\text{X} = {x_{1},\ldots,x_{n}}$ be a vector of values. We define the following operators: The first operator, $\max{(\text{X})}$, is known to be a non-expansion. However, it is non-differentiable (Property 3), and ignores non-maximizing selections (Property 4).

The next operator, $\text{mean}{(\text{X})}$, computes the average of its inputs. It is differentiable and, like any operator that takes a fixed convex combination of its inputs, is a non-expansion. However, it does not allow for maximization (Property 1).

The third operator $\text{eps}_{\epsilon}{(\text{X})}$, commonly referred to as epsilon greedy, interpolates between $\max$ and mean. The operator is a non-expansion, because it is a convex combination of two non-expansion operators. But it is non-differentiable (Property 3).

The Boltzmann operator $\text{boltz}_{\beta}{(\text{X})}$ is differentiable. It also approximates $\max$ as $\beta\rightarrow\infty$, and mean as $\beta\rightarrow 0$. However, it is not a non-expansion (Property 2), and therefore, prone to misbehavior as will be shown in the next section.

In the following section, we provide a simple example illustrating why the non-expansion property is important, especially in the context of planning and on-policy learning. We then present a new softmax operator that is similar to the Boltzmann operator yet is a non-expansion. We prove several critical properties of this new operator, introduce a new softmax policy, and present empirical results.

## Boltzmann Misbehaves

We first show that $\text{boltz}_{\beta}$ can lead to problematic behavior. To this end, we ran SARSA with Boltzmann softmax policy (Algorithm 1) on the MDP shown in Figure 1. The edges are labeled with a transition probability (unsigned) and a reward number (signed). Also, state $s_{2}$ is a terminal state, so we only consider two action values, namely $\hat{Q}{(s_{1},a)}$ and $\hat{Q}{(s_{2},b)}$. Recall that the Boltzmann softmax policy assigns the following probability to each action: Figure 1: A simple MDP with two states, two actions, and γ = 0.98. The use of a Boltzmann softmax policy is not sound in this simple domain.

Input: initial Q̂ (s, a) ∀s ∈ 𝒮 ∀a ∈ 𝒜, α, and β for each episode do a∼ Boltzmann with parameter β Take action a, observe r, s′ a′∼ Boltzmann with parameter β Algorithm 1 SARSA with Boltzmann softmax policy In Figure 2, we plot state--action value estimates at the end of each episode of a single run (smoothed by averaging over ten consecutive points). We set $\alpha =.1$ and $\beta = 16.55$. The value estimates are unstable.

Figure 2: Values estimated by SARSA with Boltzmann softmax. The algorithm never achieves stable values.

SARSA is known to converge in the tabular setting using $\epsilon$-greedy exploration, under decreasing exploration, and to a region in the function-approximation setting. There are also variants of the SARSA update rule that converge more generally. However, this example is the first, to our knowledge, to show that SARSA fails to converge in the tabular setting with Boltzmann policy. The next section provides background for our analysis of the example.

## Background

A Markov decision process, or MDP, is specified by the tuple $\langle\mathcal{S},\mathcal{A},\mathcal{R},\mathcal{P},\gamma\rangle$, where $\mathcal{S}$ is the set of states and $\mathcal{A}$ is the set of actions. The functions $\mathcal{R}:{{\mathcal{S} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$ and $\mathcal{P}:{{\mathcal{S} \times \mathcal{A} \times \mathcal{S}}\rightarrow{\lbrack 0,1\rbrack}}$ denote the reward and transition dynamics of the MDP. Finally, $\gamma \in {\lbrack 0,1)}$, the discount rate, determines the relative importance of immediate reward as opposed to the rewards received in the future.

A typical approach to finding a good policy is to estimate how good it is to be in a particular state---the state value function. The value of a particular state $s$ given a policy $\pi$ and initial action $a$ is written $Q_{\pi}{(s,a)}$. We define the optimal value of a state--action pair ${{Q^{\star}{(s,a)}} = {{\max_{\pi}Q_{\pi}}{(s,a)}}}.$ It is possible to define $Q^{\star}{(s,a)}$ recursively and as a function of the optimal value of the other state--action pairs: Bellman equations, such as the above, are at the core of many reinforcement-learning algorithms such as Value Iteration. The algorithm computes the value of the best policy in an iterative fashion: Regardless of its initial value, $\hat{Q}$ will converge to $Q^{\ast}$.

Littman & Szepesvári generalized this algorithm by replacing the $\max$ operator by any arbitrary operator $\bigotimes$, resulting in the generalized value iteration (GVI) algorithm with the following update rule: Input: initial Q̂ (s, a) ∀s ∈ 𝒮 ∀a ∈ 𝒜 and δ ∈ ℛ+ diff ← max {diff, |Qc o p y − Q̂ (s, a)|} Algorithm 2 GVI algorithm Crucially, convergence of GVI to a unique fixed point follows if operator $\bigotimes$ is a non-expansion with respect to the infinity norm: for any $\hat{Q}$, ${\hat{Q}}'$ and $s$.

Figure 3: max is a non-expansion under the infinity norm.

As mentioned earlier, the $\max$ operator is known to be a non-expansion, as illustrated in Figure 3. mean and $\text{eps}_{\epsilon}$ operators are also non-expansions. Therefore, each of these operators can play the role of $\bigotimes$ in GVI, resulting in convergence to the corresponding unique fixed point. However, the Boltzmann softmax operator, $\text{boltz}_{\beta}$, is not a non-expansion. Note that we can relate GVI to SARSA by observing that SARSA's update is a stochastic implementation of GVI's update. Under a Boltzmann softmax policy $\pi$, the target of the (expected) SARSA update is the following: | | ${\underset{\pi}{\mathbb{E}}\left\lbrack {r + \left. {\gamma\hat{Q}{(s',a')}} \middle| {s,a} \right.} \right\rbrack} =$ | | | | | | ${{\mathcal{R}{(s,a)}} + {\gamma{\sum\limits_{s' \in \mathcal{S}}{\mathcal{P}{(s,a,s')}\underset{\text{boltz}_{\beta}{({\hat{Q}{(s', \cdot)}})}}{\underbrace{\underset{a^{\prime}\in\mathcal{A}}{\sum}{\pi{(\left. a^{\prime} \middle| s^{\prime} \right.)}\hat{Q}{(s^{\prime},a^{\prime})}}}}}}}}.$ | | This matches the GVI update when $\bigotimes = \text{boltz}_{\beta}$.

## Boltzmann Has Multiple Fixed Points

Although it has been known for a long time that the Boltzmann operator is not a non-expansion, we are not aware of a published example of an MDP for which two distinct fixed points exist. The MDP presented in Figure 1 is the first example where, as shown in Figure 4, GVI under $\text{boltz}_{\beta}$ has two distinct fixed points. We also show, in Figure 5, a vector field visualizing GVI updates under $\text{boltz}_{\beta = 16.55}$. The updates can move the current estimates farther from the fixed points. The behavior of SARSA (Figure 2) results from the algorithm stochastically bouncing back and forth between the two fixed points. When the learning algorithm performs a sequence of noisy updates, it moves from a fixed point to the other. As we will show later, planning will also progress extremely slowly near the fixed points. The lack of the non-expansion property leads to multiple fixed points and ultimately a misbehavior in learning and planning.

Figure 4: Fixed points of GVI under boltzβ for varying β. Two distinct fixed points (red and blue) co-exist for a range of β.

Figure 5: A vector field showing GVI updates under boltzβ = 16.55. Fixed points are marked in black. For some points, such as the large blue point, updates can move the current estimates farther from the fixed points. Also, for points that lie in between the two fixed-points, progress is extremely slow.

## Mellowmax and its Properties

We advocate for an alternative softmax operator defined as follows: which can be viewed as a particular instantiation of the quasi-arithmetic mean. It can also be derived from information theoretical principles as a way of regularizing policies with a cost function defined by KL divergence. Note that the operator has previously been utilized in other areas, such as power engineering.

We show that $\text{mm}_{\omega}$, which we refer to as *mellowmax*, has the desired properties and that it compares quite favorably to $\text{boltz}_{\beta}$ in practice.

### Mellowmax is a Non-Expansion

We prove that $\text{mm}_{\omega}$ is a non-expansion (Property 2), and therefore, GVI and SARSA under $\text{mm}_{\omega}$ are guaranteed to converge to a unique fixed point.

Let $\text{X} = {x_{1},\ldots,x_{n}}$ and $\text{Y} = {y_{1},\ldots,y_{n}}$ be two vectors of values. Let $\Delta_{i} = {x_{i} - y_{i}}$ for $i \in {\{ 1,\ldots,n\}}$ be the difference of the $i$th components of the two vectors. Also, let $i^{\ast}$ be the index with the maximum component-wise difference, $i^{\ast} = {\operatorname{argmax}_{i}\Delta_{i}}$. For simplicity, we assume that $i^{\ast}$ is unique and $\omega > 0$. Also, without loss of generality, we assume that ${x_{i^{\ast}} - y_{i^{\ast}}} \geq 0$. It follows that: | | $\left| {{\text{mm}_{\omega}{(\text{X})}} - {\text{mm}_{\omega}{(\text{Y})}}} \right|$ | | | | | $=$ | $\left| {{{\log{({\frac{1}{n}{\sum\limits_{i = 1}^{n}e^{\omegax_{i}}}})}}/\omega} - {{\log{({\frac{1}{n}{\sum\limits_{i = 1}^{n}e^{\omegay_{i}}}})}}/\omega}} \right|$ | | | | | $=$ | $\left| {\log{\frac{\frac{1}{n}{\sum_{i = 1}^{n}e^{\omegax_{i}}}}{\frac{1}{n}{\sum_{i = 1}^{n}e^{\omegay_{i}}}}/\omega}} \right|$ | | | | | $=$ | $\left| {\log{\frac{\sum_{i = 1}^{n}e^{\omega{({y_{i} + \Delta_{i}})}}}{\sum_{i = 1}^{n}e^{\omegay_{i}}}/\omega}} \right|$ | | | | | $\leq$ | $\left| {\log{\frac{\sum_{i = 1}^{n}e^{\omega{({y_{i} + \Delta_{i^{\ast}}})}}}{\sum_{i = 1}^{n}e^{\omegay_{i}}}/\omega}} \right|$ | | allowing us to conclude that mellowmax is a non-expansion under the infinity norm.

### Maximization

Mellowmax includes parameter settings that allow for maximization (Property 1) as well as for minimization. In particular, as $\omega$ goes to infinity, $\text{mm}_{\omega}$ acts like $\max$.

Let $m = {\max{(\text{X})}}$ and let $W = {|\left. \{{x_{i} = m} \middle| {i \in {\{ 1,\ldots,n\}}}\} \right.|}$. Note that $W \geq 1$ is the number of maximum values ("winners") in X. Then: That is, the operator acts more and more like pure maximization as the value of $\omega$ is increased. Conversely, as $\omega$ goes to $- \infty$, the operator approaches the minimum.

### Derivatives

We can take the derivative of mellowmax with respect to each one of the arguments $x_{i}$ and for any non-zero $\omega$: Note that the operator is non-decreasing in each component of X.

Moreover, we can take the derivative of mellowmax with respect to $\omega$. We define ${n_{\omega}{(\text{X})}} = {\log{({\frac{1}{n}{\sum_{i = 1}^{n}e^{\omegax_{i}}}})}}$ and ${d_{\omega}{(\text{X})}} = \omega$. Then: ensuring differentiablity of the operator (Property 3).

### Averaging

Because of the division by $\omega$ in the definition of $\text{mm}_{\omega}$, the parameter $\omega$ cannot be set to zero. However, we can examine the behavior of $\text{mm}_{\omega}$ as $\omega$ approaches zero and show that the operator computes an average in the limit.

Since both the numerator and denominator go to zero as $\omega$ goes to zero, we will use L'Hôpital's rule and the derivative given in the previous section to derive the value in the limit: That is, as $\omega$ gets closer to zero, $\text{mm}_{\omega}{(\text{X})}$ approaches the mean of the values in X.

## Maximum Entropy Mellowmax Policy

As described, $\text{mm}_{\omega}$ computes a value for a list of numbers somewhere between its minimum and maximum. However, it is often useful to actually provide a probability distribution over the actions such that a non-zero probability mass is assigned to each action, and the resulting expected value equals the computed value. Such a probability distribution can then be used for action selection in algorithms such as SARSA.

In this section, we address the problem of identifying such a probability distribution as a maximum entropy problem---over all distributions that satisfy the properties above, pick the one that maximizes information entropy. We formally define the maximum entropy mellowmax policy of a state $s$ as: Note that this optimization problem is convex and can be solved reliably using any numerical convex optimization library.

One way of finding the solution, which leads to an interesting policy form, is to use the method of Lagrange multipliers. Here, the Lagrangian is: Taking the partial derivative of the Lagrangian with respect to each $\pi{(\left. a \middle| s \right.)}$ and setting them to zero, we obtain: These $|\mathcal{A}|$ equations, together with the two linear constraints, form ${|\mathcal{A}|} + 2$ equations to constrain the ${|\mathcal{A}|} + 2$ variables ${\pi{(\left. a \middle| s \right.)}{\forall a}} \in \mathcal{A}$ and the two Lagrangian multipliers $\lambda_{1}$ and $\lambda_{2}$.

Solving this system of equations, the probability of taking an action under the maximum entropy mellowmax policy has the form: where $\beta$ is a value for which: The argument for the existence of a unique root is simple. As $\beta\rightarrow\infty$ the term corresponding to the best action dominates, and so, the function is positive. Conversely, as $\beta\rightarrow{- \infty}$ the term corresponding to the action with lowest utility dominates, and so the function is negative. Finally, by taking the derivative, it is clear that the function is monotonically increasing, allowing us to conclude that there exists only a single root. Therefore, we can find $\beta$ easily using any root-finding algorithm. In particular, we use Brent's method available in the Numpy library of Python.

This policy has the same form as Boltzmann softmax, but with a parameter $\beta$ whose value depends indirectly on $\omega$. This mathematical form arose not from the structure of $\text{mm}_{\omega}$, but from maximizing the entropy. One way to view the use of the mellowmax operator, then, is as a form of Boltzmann policy with a temperature parameter chosen adaptively in each state to ensure that the non-expansion property holds.

Finally, note that the SARSA update under the maximum entropy mellowmax policy could be thought of as a stochastic implementation of the GVI update under the $\text{mm}_{\omega}$ operator: | | ${\underset{\pi_{mm}}{\mathbb{E}}\left\lbrack {r + \left. {\gamma\hat{Q}{(s',a')}} \middle| {s,a} \right.} \right\rbrack} =$ | | | | | | ${\sum\limits_{s' \in \mathcal{S}}{\mathcal{R}{(s,a,s')}}} + {\gamma\mathcal{P}{(s,a,s')}\underset{\text{mm}_{\omega}{(\hat{Q}{(s',.)})}}{\underbrace{\left. \underset{a^{\prime}\in\mathcal{A}}{\sum}\pi_{mm}{(a^{\prime}|s^{\prime})}\hat{Q}{(s^{\prime},a^{\prime})} \right\rbrack}}}$ | | due to the first constraint of the convex optimization problem. Because mellowmax is a non-expansion, SARSA with the maximum entropy mellowmax policy is guaranteed to converge to a unique fixed point. Note also that, similar to other variants of SARSA, the algorithm simply bootstraps using the value of the next state while implementing the new policy.

## Experiments on MDPs

We observed that in practice computing mellowmax can yield overflow if the exponentiated values are large. In this case, we can safely shift the values by a constant before exponentiating them due to the following equality: A value of $c = {\max_{i}x_{i}}$ usually avoids overflow.

We repeat the experiment from Figure 5 for mellowmax with $\omega = 16.55$ to get a vector field. The result, presented in Figure 6, show a rapid and steady convergence towards the unique fixed point. As a result, GVI under $\text{mm}_{\omega}$ can terminate significantly faster than GVI under $\text{boltz}_{\beta}$, as illustrated in Figure 7.

Figure 6: GVI updates under mmω = 16.55. The fixed point is unique, and all updates move quickly toward the fixed point.

Figure 7: Number of iterations before termination of GVI on the example MDP. GVI under mmω outperforms the alternatives.

We present three additional experiments. The first experiment investigates the behavior of GVI with the softmax operators on randomly generated MDPs. The second experiment evaluates the softmax policies when used in SARSA with a tabular representation. The last experiment is a policy gradient experiment where a deep neural network, with a softmax output layer, is used to directly represent the policy.

### Random MDPs

The example in Figure 1 was created carefully by hand. It is interesting to know whether such examples are likely to be encountered naturally. To this end, we constructed 200 MDPs as follows: We sampled $|\mathcal{S}|$ from $\{ 2,3,\ldots,10\}$ and $|\mathcal{A}|$ from $\{ 2,3,4,5\}$ uniformly at random. We initialized the transition probabilities by sampling uniformly from $\lbrack 0,.01\rbrack$. We then added to each entry, with probability 0.5, Gaussian noise with mean 1 and variance 0.1. We next added, with probability 0.1, Gaussian noise with mean 100 and variance 1. Finally, we normalized the raw values to ensure that we get a transition matrix. We did a similar process for rewards, with the difference that we divided each entry by the maximum entry and multiplied by 0.5 to ensure that $R_{\max} = 0.5$.

We measured the failure rate of GVI under $\text{boltz}_{\beta}$ and $\text{mm}_{\omega}$ by stopping GVI when it did not terminate in 1000 iterations. We also computed the average number of iterations needed before termination. A summary of results is presented in the table below. Mellowmax outperforms Boltzmann based on the three measures provided below.

MDPs, no terminate MDPs, $> 1$ fixed points average iterations

### Multi-passenger Taxi Domain

We evaluated SARSA on the multi-passenger taxi domain introduced by Dearden et al.. (See Figure 8.)

Figure 8: Multi-passenger taxi domain. The discount rate γ is 0.99. Reward is +1 for delivering one passenger, +3 for two passengers, and +15 for three passengers. Reward is zero for all the other transitions. Here F, S, and D denote passengers, start state, and destination respectively.

One challenging aspect of this domain is that it admits many locally optimal policies. Exploration needs to be set carefully to avoid either over-exploring or under-exploring the state space. Note also that Boltzmann softmax performs remarkably well on this domain, outperforming sophisticated Bayesian reinforcement-learning algorithms.

Figure 9: Comparison on the multi-passenger taxi domain. Results are shown for different values of ϵ, β, and ω. For each setting, the learning rate is optimized. Results are averaged over 25 independent runs, each consisting of 300000 time steps.

As shown in Figure 9, SARSA with the epsilon-greedy policy performs poorly. In fact, in our experiment, the algorithm rarely was able to deliver all the passengers. However, SARSA with Boltzmann softmax and SARSA with the maximum entropy mellowmax policy achieved significantly higher average reward. Maximum entropy mellowmax policy is no worse than Boltzmann softmax, here, suggesting that the greater stability does not come at the expense of less effective exploration.

### Lunar Lander Domain

In this section, we evaluate the use of the maximum entropy mellowmax policy in the context of a policy-gradient algorithm. Specifically, we represent a policy by a neural network (discussed below) that maps from states to probabilities over actions. A common choice for the activation function of the last layer is the Boltzmann softmax policy. In contrast, we can use maximum entropy mellowmax policy, presented in Section 6, by treating the inputs of the activation function as $\hat{Q}$ values.

We used the lunar lander domain, from OpenAI Gym as our benchmark. A screenshot of the domain is presented in Figure 10. This domain has a continuous state space with 8 dimensions, namely x-y coordinates, x-y velocities, angle and angular velocities, and leg-touchdown sensors. There are 4 discrete actions to control 3 engines. The reward is +100 for a safe landing in the designated area, and $- 100$ for a crash. There is a small shaping reward for approaching the landing area. Using the engines results in a negative reward. An episode finishes when the spacecraft crashes or lands. Solving the domain is defined as maintaining mean episode return higher than 200 in 100 consecutive episodes.

The policy in our experiment is represented by a neural network with a hidden layer comprised of 16 units with RELU activation functions, followed by a second layer with 16 units and softmax activation functions. We used REINFORCE to train the network. A batch episode size of 10 was used, as we had stability issues with smaller episode batch sizes. We used the Adam algorithm with $\alpha = 0.005$ and the other parameters as suggested by the paper. We used Keras and Theano to implement the neural network architecture.

Figure 10: A screenshot of the lunar lander domain.

For each softmax policy, we present in Figure 11 the learning curves for different values of their free parameter. We further plot average return over all 40000 episodes. Mellowmax outperforms Boltzmann at its peak.

Figure 11: Comparison of Boltzmann (top) and maximum entropy mellowmax (middle) in Lunar Lander. Mean return over all episodes (bottom). Results are 400-run averages.

## Related Work

Softmax operators play an important role in sequential decision-making algorithms.

In model-free reinforcement learning, they can help strike a balance between exploration (mean) and exploitation (max). Decision rules based on epsilon-greedy and Boltzmann softmax, while very simple, often perform surprisingly well in practice, even outperforming more advanced exploration techniques that require significant approximation for complex domains. When learning "on policy", exploration steps can and perhaps should become part of the value-estimation process itself. On-policy algorithms like SARSA can be made to converge to optimal behavior in the limit when the exploration rate and the update operator is gradually moved toward $\max$. Our use of softmax in learning updates reflects this point of view and shows that the value-sensitive behavior of Boltzmann exploration can be maintained even as updates are made stable.

Analyses of the behavior of human subjects in choice experiments very frequently use softmax. Sometimes referred to in the literature as logit choice, it forms an important part of the most accurate predictor of human decisions in normal-form games, quantal level-$k$ reasoning (QLk). Softmax-based fixed points play a crucial role in this work. As such, mellowmax could potentially make a good replacement.

Algorithms for inverse reinforcement learning (IRL), the problem of inferring reward functions from observed behavior, frequently use a Boltzmann operator to avoid assigning zero probability to non-optimal actions and hence assessing an observed sequence as impossible. Such methods include Bayesian IRL, natural gradient IRL, and maximum likelihood IRL. Given the recursive nature of value defined in these problems, mellowmax could be a more stable and efficient choice.

In linearly solvable MDPs, an operator similar to mellowmax emerges when using an alternative characterization for cost of action selection in MDPs. Inspired by this work Fox et al. introduced an off-policy G-learning algorithm that uses the operator to perform value-function updates. Instead of performing off-policy updates, we introduced a convergent variant of SARSA with Boltzmann policy and a state-dependent temperature parameter. This is in contrast to Fox et al. where an epsilon greedy behavior policy is used.

## Conclusion and Future Work

We proposed the mellowmax operator as an alternative to the Boltzmann softmax operator. We showed that mellowmax has several desirable properties and that it works favorably in practice. Arguably, mellowmax could be used in place of Boltzmann throughout reinforcement-learning research.

A future direction is to analyze the fixed point of planning, reinforcement-learning, and game-playing algorithms when using the mellowmax operators. In particular, an interesting analysis could be one that bounds the sub-optimality of the fixed points found by GVI.

An important future work is to expand the scope of our theoretical understanding to the more general function approximation setting, in which the state space or the action space is large and abstraction techniques are used. Note that the importance of non-expansion in the function approximation case is well-established.

Finally, due to the convexity of mellowmax, it is compelling to use it in a gradient-based algorithm in the context of sequential decision making. IRL is a natural candidate given the popularity of softmax in this setting.
