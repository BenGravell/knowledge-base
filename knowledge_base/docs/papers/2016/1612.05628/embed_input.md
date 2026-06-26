<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

An Alternative Softmax Operator for Reinforcement Learning

Topics include Reinforcement learning, Planning, Learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Proposes the mellowmax operator

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A softmax operator applied to a set of values acts somewhat like the maximization function and somewhat like an average. In sequential decision making, softmax is often used in settings where it is necessary to maximize utility but also to hedge against problems that arise from putting all of one's weight behind a single maximum utility decision. The Boltzmann softmax operator is the most commonly used softmax operator in this setting, but we show that this operator is prone to misbehavior. In this work, we study a differentiable softmax operator that, among other properties, is a non-expansion ensuring a convergent behavior in learning and planning. We introduce a variant of SARSA algorithm that, by utilizing the new operator, computes a Boltzmann policy with a state-dependent temperature parameter. We show that the algorithm is convergent and that it performs favorably in practice.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

There is a fundamental tension in decision making between choosing the action that has highest expected utility and avoiding "starving" the other actions. The issue arises in the context of the exploration--exploitation dilemma, non-stationary decision problems, and when interpreting observed decisions.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In reinforcement learning, an approach to addressing the tension is the use of *softmax* operators for value-function optimization, and softmax policies for action selection. Examples include value-based methods such as SARSA or expected SARSA, and policy-search methods such as REINFORCE.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

An ideal softmax operator is a parameterized set of operators that: has parameter settings that allow it to approximate maximization arbitrarily accurately to perform reward-seeking behavior; is a non-expansion for all parameter settings ensuring convergence to a unique fixed point; is differentiable to make it possible to improve via gradient-based optimization; and avoids the starvation of non-maximizing actions.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Let $\text{X} = {x_{1},\ldots,x_{n}}$ be a vector of values. We define the following operators: The first operator, $\max{(\text{X})}$, is known to be a non-expansion. However, it is non-differentiable (Property 3), and ignores non-maximizing selections (Property 4).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The next operator, $\text{mean}{(\text{X})}$, computes the average of its inputs. It is differentiable and, like any operator that takes a fixed convex combination of its inputs, is a non-expansion. However, it does not allow for maximization (Property 1).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The third operator $\text{eps}_{\epsilon}{(\text{X})}$, commonly referred to as epsilon greedy, interpolates between $\max$ and mean. The operator is a non-expansion, because it is a convex combination of two non-expansion operators. But it is non-differentiable (Property 3).

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The Boltzmann operator $\text{boltz}_{\beta}{(\text{X})}$ is differentiable. It also approximates $\max$ as $\beta\rightarrow\infty$, and mean as $\beta\rightarrow 0$. However, it is not a non-expansion (Property 2), and therefore, prone to misbehavior as will be shown in the next section.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the following section, we provide a simple example illustrating why the non-expansion property is important, especially in the context of planning and on-policy learning. We then present a new softmax operator that is similar to the Boltzmann operator yet is a non-expansion. We prove several critical properties of this new operator, introduce a new softmax policy, and present empirical results.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Boltzmann Misbehaves", "weight": 1.0} -->

We first show that $\text{boltz}_{\beta}$ can lead to problematic behavior. To this end, we ran SARSA with Boltzmann softmax policy (Algorithm 1) on the MDP shown in Figure 1. The edges are labeled with a transition probability (unsigned) and a reward number (signed). Also, state $s_{2}$ is a terminal state, so we only consider two action values, namely $\hat{Q}{(s_{1},a)}$ and $\hat{Q}{(s_{2},b)}$. Recall that the Boltzmann softmax policy assigns the following probability to each action: Figure 1: A simple MDP with two states, two actions, and γ = 0.98. The use of a Boltzmann softmax policy is not sound in this simple domain.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Boltzmann Misbehaves", "weight": 1.0} -->

Input: initial Q̂ (s, a) ∀s ∈ 𝒮 ∀a ∈ 𝒜, α, and β for each episode do a∼ Boltzmann with parameter β Take action a, observe r, s′ a′∼ Boltzmann with parameter β Algorithm 1 SARSA with Boltzmann softmax policy In Figure 2, we plot state--action value estimates at the end of each episode of a single run (smoothed by averaging over ten consecutive points). We set $\alpha =.1$ and $\beta = 16.55$. The value estimates are unstable.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Boltzmann Misbehaves", "weight": 1.0} -->

SARSA is known to converge in the tabular setting using $\epsilon$-greedy exploration, under decreasing exploration, and to a region in the function-approximation setting. There are also variants of the SARSA update rule that converge more generally. However, this example is the first, to our knowledge, to show that SARSA fails to converge in the tabular setting with Boltzmann policy. The next section provides background for our analysis of the example.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Boltzmann Has Multiple Fixed Points", "weight": 1.0} -->

Although it has been known for a long time that the Boltzmann operator is not a non-expansion, we are not aware of a published example of an MDP for which two distinct fixed points exist. The MDP presented in Figure 1 is the first example where, as shown in Figure 4, GVI under $\text{boltz}_{\beta}$ has two distinct fixed points. We also show, in Figure 5, a vector field visualizing GVI updates under $\text{boltz}_{\beta = 16.55}$. The updates can move the current estimates farther from the fixed points. The behavior of SARSA (Figure 2) results from the algorithm stochastically bouncing back and forth between the two fixed points. When the learning algorithm performs a sequence of noisy updates, it moves from a fixed point to the other. As we will show later, planning will also progress extremely slowly near the fixed points. The lack of the non-expansion property leads to multiple fixed points and ultimately a misbehavior in learning and planning.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Mellowmax and its Properties", "weight": 1.0} -->

We advocate for an alternative softmax operator defined as follows: which can be viewed as a particular instantiation of the quasi-arithmetic mean. It can also be derived from information theoretical principles as a way of regularizing policies with a cost function defined by KL divergence. Note that the operator has previously been utilized in other areas, such as power engineering.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Mellowmax and its Properties", "weight": 1.0} -->

We show that $\text{mm}_{\omega}$, which we refer to as *mellowmax*, has the desired properties and that it compares quite favorably to $\text{boltz}_{\beta}$ in practice.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Mellowmax is a Non-Expansion", "weight": 1.0} -->

We prove that $\text{mm}_{\omega}$ is a non-expansion (Property 2), and therefore, GVI and SARSA under $\text{mm}_{\omega}$ are guaranteed to converge to a unique fixed point.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Maximization", "weight": 1.0} -->

Mellowmax includes parameter settings that allow for maximization (Property 1) as well as for minimization. In particular, as $\omega$ goes to infinity, $\text{mm}_{\omega}$ acts like $\max$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Maximization", "weight": 1.0} -->

Let $m = {\max{(\text{X})}}$ and let $W = {|\left. \{{x_{i} = m} \middle| {i \in {\{ 1,\ldots,n\}}}\} \right.|}$. Note that $W \geq 1$ is the number of maximum values ("winners") in X. Then: That is, the operator acts more and more like pure maximization as the value of $\omega$ is increased. Conversely, as $\omega$ goes to $- \infty$, the operator approaches the minimum.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Derivatives", "weight": 1.0} -->

We can take the derivative of mellowmax with respect to each one of the arguments $x_{i}$ and for any non-zero $\omega$: Note that the operator is non-decreasing in each component of X.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Averaging", "weight": 1.0} -->

Because of the division by $\omega$ in the definition of $\text{mm}_{\omega}$, the parameter $\omega$ cannot be set to zero. However, we can examine the behavior of $\text{mm}_{\omega}$ as $\omega$ approaches zero and show that the operator computes an average in the limit.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Averaging", "weight": 1.0} -->

Since both the numerator and denominator go to zero as $\omega$ goes to zero, we will use L'Hôpital's rule and the derivative given in the previous section to derive the value in the limit: That is, as $\omega$ gets closer to zero, $\text{mm}_{\omega}{(\text{X})}$ approaches the mean of the values in X.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Maximum Entropy Mellowmax Policy", "weight": 1.0} -->

As described, $\text{mm}_{\omega}$ computes a value for a list of numbers somewhere between its minimum and maximum. However, it is often useful to actually provide a probability distribution over the actions such that a non-zero probability mass is assigned to each action, and the resulting expected value equals the computed value. Such a probability distribution can then be used for action selection in algorithms such as SARSA.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Maximum Entropy Mellowmax Policy", "weight": 1.0} -->

In this section, we address the problem of identifying such a probability distribution as a maximum entropy problem---over all distributions that satisfy the properties above, pick the one that maximizes information entropy. We formally define the maximum entropy mellowmax policy of a state $s$ as: Note that this optimization problem is convex and can be solved reliably using any numerical convex optimization library.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Maximum Entropy Mellowmax Policy", "weight": 1.0} -->

One way of finding the solution, which leads to an interesting policy form, is to use the method of Lagrange multipliers. Here, the Lagrangian is: Taking the partial derivative of the Lagrangian with respect to each $\pi{(\left. a \middle| s \right.)}$ and setting them to zero, we obtain: These $|\mathcal{A}|$ equations, together with the two linear constraints, form ${|\mathcal{A}|} + 2$ equations to constrain the ${|\mathcal{A}|} + 2$ variables ${\pi{(\left. a \middle| s \right.)}{\forall a}} \in \mathcal{A}$ and the two Lagrangian multipliers $\lambda_{1}$ and $\lambda_{2}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Maximum Entropy Mellowmax Policy", "weight": 1.0} -->

Solving this system of equations, the probability of taking an action under the maximum entropy mellowmax policy has the form: where $\beta$ is a value for which: The argument for the existence of a unique root is simple. As $\beta\rightarrow\infty$ the term corresponding to the best action dominates, and so, the function is positive. Conversely, as $\beta\rightarrow{- \infty}$ the term corresponding to the action with lowest utility dominates, and so the function is negative. Finally, by taking the derivative, it is clear that the function is monotonically increasing, allowing us to conclude that there exists only a single root. Therefore, we can find $\beta$ easily using any root-finding algorithm. In particular, we use Brent's method available in the Numpy library of Python.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Maximum Entropy Mellowmax Policy", "weight": 1.0} -->

This policy has the same form as Boltzmann softmax, but with a parameter $\beta$ whose value depends indirectly on $\omega$. This mathematical form arose not from the structure of $\text{mm}_{\omega}$, but from maximizing the entropy. One way to view the use of the mellowmax operator, then, is as a form of Boltzmann policy with a temperature parameter chosen adaptively in each state to ensure that the non-expansion property holds.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Maximum Entropy Mellowmax Policy", "weight": 1.0} -->

\underset{a^{\prime}\in\mathcal{A}}{\sum}\pi_{mm}{(a^{\prime}|s^{\prime})}\hat{Q}{(s^{\prime},a^{\prime})} \right\rbrack}}}$ | | due to the first constraint of the convex optimization problem. Because mellowmax is a non-expansion, SARSA with the maximum entropy mellowmax policy is guaranteed to converge to a unique fixed point. Note also that, similar to other variants of SARSA, the algorithm simply bootstraps using the value of the next state while implementing the new policy.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experiments on MDPs", "weight": 1.0} -->

We observed that in practice computing mellowmax can yield overflow if the exponentiated values are large. In this case, we can safely shift the values by a constant before exponentiating them due to the following equality: A value of $c = {\max_{i}x_{i}}$ usually avoids overflow.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments on MDPs", "weight": 1.0} -->

We repeat the experiment from Figure 5 for mellowmax with $\omega = 16.55$ to get a vector field. The result, presented in Figure 6, show a rapid and steady convergence towards the unique fixed point. As a result, GVI under $\text{mm}_{\omega}$ can terminate significantly faster than GVI under $\text{boltz}_{\beta}$, as illustrated in Figure 7.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiments on MDPs", "weight": 1.0} -->

We present three additional experiments. The first experiment investigates the behavior of GVI with the softmax operators on randomly generated MDPs. The second experiment evaluates the softmax policies when used in SARSA with a tabular representation. The last experiment is a policy gradient experiment where a deep neural network, with a softmax output layer, is used to directly represent the policy.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Random MDPs", "weight": 1.0} -->

The example in Figure 1 was created carefully by hand. It is interesting to know whether such examples are likely to be encountered naturally. To this end, we constructed 200 MDPs as follows: We sampled $|\mathcal{S}|$ from $\{ 2,3,\ldots,10\}$ and $|\mathcal{A}|$ from $\{ 2,3,4,5\}$ uniformly at random. We initialized the transition probabilities by sampling uniformly from $\lbrack 0,.01\rbrack$. We then added to each entry, with probability 0.5, Gaussian noise with mean 1 and variance 0.1. We next added, with probability 0.1, Gaussian noise with mean 100 and variance 1. Finally, we normalized the raw values to ensure that we get a transition matrix. We did a similar process for rewards, with the difference that we divided each entry by the maximum entry and multiplied by 0.5 to ensure that $R_{\max} = 0.5$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Random MDPs", "weight": 1.0} -->

We measured the failure rate of GVI under $\text{boltz}_{\beta}$ and $\text{mm}_{\omega}$ by stopping GVI when it did not terminate in 1000 iterations. We also computed the average number of iterations needed before termination. A summary of results is presented in the table below. Mellowmax outperforms Boltzmann based on the three measures provided below.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Random MDPs", "weight": 1.0} -->

MDPs, no terminate MDPs, $> 1$ fixed points average iterations

<!-- chunk {"id": "body-0036", "role": "body", "section": "Multi-passenger Taxi Domain", "weight": 1.0} -->

We evaluated SARSA on the multi-passenger taxi domain introduced by Dearden et al.. (See Figure 8.)

<!-- chunk {"id": "body-0037", "role": "body", "section": "Multi-passenger Taxi Domain", "weight": 1.0} -->

One challenging aspect of this domain is that it admits many locally optimal policies. Exploration needs to be set carefully to avoid either over-exploring or under-exploring the state space. Note also that Boltzmann softmax performs remarkably well on this domain, outperforming sophisticated Bayesian reinforcement-learning algorithms.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Multi-passenger Taxi Domain", "weight": 1.0} -->

As shown in Figure 9, SARSA with the epsilon-greedy policy performs poorly. In fact, in our experiment, the algorithm rarely was able to deliver all the passengers. However, SARSA with Boltzmann softmax and SARSA with the maximum entropy mellowmax policy achieved significantly higher average reward. Maximum entropy mellowmax policy is no worse than Boltzmann softmax, here, suggesting that the greater stability does not come at the expense of less effective exploration.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Lunar Lander Domain", "weight": 1.0} -->

In this section, we evaluate the use of the maximum entropy mellowmax policy in the context of a policy-gradient algorithm. Specifically, we represent a policy by a neural network (discussed below) that maps from states to probabilities over actions. A common choice for the activation function of the last layer is the Boltzmann softmax policy. In contrast, we can use maximum entropy mellowmax policy, presented in Section 6, by treating the inputs of the activation function as $\hat{Q}$ values.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Lunar Lander Domain", "weight": 1.0} -->

We used the lunar lander domain, from OpenAI Gym as our benchmark. A screenshot of the domain is presented in Figure 10. This domain has a continuous state space with 8 dimensions, namely x-y coordinates, x-y velocities, angle and angular velocities, and leg-touchdown sensors. There are 4 discrete actions to control 3 engines. The reward is +100 for a safe landing in the designated area, and $- 100$ for a crash. There is a small shaping reward for approaching the landing area. Using the engines results in a negative reward. An episode finishes when the spacecraft crashes or lands. Solving the domain is defined as maintaining mean episode return higher than 200 in 100 consecutive episodes.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Lunar Lander Domain", "weight": 1.0} -->

The policy in our experiment is represented by a neural network with a hidden layer comprised of 16 units with RELU activation functions, followed by a second layer with 16 units and softmax activation functions. We used REINFORCE to train the network. A batch episode size of 10 was used, as we had stability issues with smaller episode batch sizes. We used the Adam algorithm with $\alpha = 0.005$ and the other parameters as suggested by the paper. We used Keras and Theano to implement the neural network architecture.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Lunar Lander Domain", "weight": 1.0} -->

For each softmax policy, we present in Figure 11 the learning curves for different values of their free parameter. We further plot average return over all 40000 episodes. Mellowmax outperforms Boltzmann at its peak.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

We proposed the mellowmax operator as an alternative to the Boltzmann softmax operator. We showed that mellowmax has several desirable properties and that it works favorably in practice. Arguably, mellowmax could be used in place of Boltzmann throughout reinforcement-learning research.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

A future direction is to analyze the fixed point of planning, reinforcement-learning, and game-playing algorithms when using the mellowmax operators. In particular, an interesting analysis could be one that bounds the sub-optimality of the fixed points found by GVI.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

An important future work is to expand the scope of our theoretical understanding to the more general function approximation setting, in which the state space or the action space is large and abstraction techniques are used. Note that the importance of non-expansion in the function approximation case is well-established.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

Finally, due to the convexity of mellowmax, it is compelling to use it in a gradient-based algorithm in the context of sequential decision making. IRL is a natural candidate given the popularity of softmax in this setting.
