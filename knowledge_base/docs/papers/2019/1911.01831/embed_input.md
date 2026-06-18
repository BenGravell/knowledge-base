<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Quinoa: A Q-function You Infer Normalized over Actions

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present an algorithm for learning an approximate action-value soft Q-function in the relative entropy regularised reinforcement learning setting, for which an optimal improved policy can be recovered in closed form. We use recent advances in normalising flows for parametrising the policy together with a learned value-function; and show how this combination can be used to implicitly represent Q-values of an arbitrary policy in continuous action space. Using simple temporal difference learning on the Q-values then leads to a unified objective for policy and value learning. We show how this approach considerably simplifies standard Actor-Critic off-policy algorithms, removing the need for a policy optimisation step. We perform experiments on a range of established reinforcement learning benchmarks, demonstrating that our approach allows for complex, multimodal policy distributions in continuous action spaces, while keeping the process of sampling from the policy both fast and exact.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Off-policy actor-critic algorithms, in combination with deep neural networks, hold promise for solving problems in continuous control, as they can be used to learn complex non-linear policies in a data-efficient manner. Typically deep actor-critic approaches consist of two steps. First, a neural network is used to fit the Q-values of the current policy. After that, a parametric policy -- often a conditional Gaussian distribution -- is learned by maximising these learned Q-values. These two steps are then iterated to convergence. Ideally, the second policy optimisation step would not be needed. After all, optimising a policy against a learned Q-function just transforms action-preferences into a normalised distribution. This optimisation step cannot produce new information which was not already encoded in the Q-function. It can however introduce sub-optimal behaviour through approximation errors; either due to the choice in the parametric policy distribution or due to numerical fitting errors.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

As a consequence, the idea of learning a Q-function from which an improved policy can be obtained without additional optimisation, has been previously considered by learning normalised advantage functions (NAF) or using compatible function approximation with Gaussian policies. While appealing in theory, these approaches come with the caveat that they put additional constraints on the Q-function, such as being locally quadratic in action space. This limits the expressiveness of the Q-function, making it no longer able to correctly fit any set of Q-values.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we propose an algorithm which learns a soft Q-function globally while providing the optimal policy in closed form. We call this algorithm Quinoa, a *Q-function you Infer Normalised Over Actions* as we can directly perform inference on the optimal policy, which is the soft Q-function normalised over the action dimensions. We find that the key to allowing unrestricted Q-functions that allow for inference of the optimal policy, is to use a richer class of policy parametrisations. In particular, we use normalising flows as they can be universal density function approximators. In the next section, we will explain how we derive our soft Q-function, starting from a relative entropy regularised RL objective, as considered in REPS, TRPO, MPO and SAC.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Quinoa", "weight": 1.0} -->

We would like to find a soft-optimal policy $\pi$, which in every state maximises the soft Q-function $Q_{\pi}^{s}{(a,s)}$. This in turn would locally maximise our objective $J{(\pi)}$ at each state under the assumption that $Q_{\pi}^{s}$ is sufficiently accurate. Solving for $\pi$ comes with one caveat: finding the multiplier $\alpha$ trading the regularisation with the reward is hard, as the magnitude of the reward can differ significantly over the course of the training process.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Quinoa", "weight": 1.0} -->

where the last constraint ensures that $\pi$ is normalised. We solve this constrained optimisation problem using the method of Lagrange multipliers, automatically obtaining an optimal $\alpha$ for a given $\epsilon$. The details of this procedure are given in the Appendix.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Quinoa", "weight": 1.0} -->

Taking into account the constraint that $\pi{(\left. a \middle| s \right.)}$ is a distribution, we obtain that the optimal policy $\pi{(\left. a \middle| s \right.)}$ for a given $Q_{\pi}^{s}{(a,s)}$ is given by

<!-- chunk {"id": "body-0009", "role": "body", "section": "Quinoa", "weight": 1.0} -->

this not only defines an improved policy, but also establishes a relation between the soft action-value $Q_{\pi}^{s}{(a,s)}$ and the policy $\pi$. To act according to $\pi$, we need a way to infer actions from Q-values. There are three main viable approaches. Firstly, we could learn a parametric Q-function and then project the exponentiated Q-values onto a parametric $\pi$. This approach has been considered in Haarnoja et al. and was extended to use rich parametric policies in Haarnoja et al.. Secondly, we could aim to sample from $\pi$ directly, for instance via importance sampling based on samples from $\overset{\sim}{\pi}{(\left. a \middle| s \right.)}$ reweighed with $\exp{({{Q_{\pi}^{s}{(a,s)}}/\alpha})}$. This approach is known to have high-variance and is compute intensive.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Quinoa", "weight": 1.0} -->

Finally, we could parameterise the Q-function, restricting its expressiveness, such that we can obtain $\pi$ in closed form. Using a Gaussian distribution for the policy would recover the NAF setting, but this restricts $Q_{\pi}^{s}{(a,s)}$ to be quadratic in action space. In this paper we follow the third approach yet make use of a rich policy class of normalising flows, allowing the soft action-value function $Q_{\pi}^{s}$ to be a universal function approximator.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Quinoa", "weight": 1.0} -->

To achieve this we first solve Equation 1 for $Q_{\pi}^{s}{(a,s)}$ to find the following equation.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Quinoa", "weight": 1.0} -->

It makes sense to call the first term the soft value function, since taking the expectation of both sides of the equation gives ${\mathbb{E}_{\pi}\left\lbrack {Q_{\pi}^{s}{(a,s)}} \right\rbrack} = {{V_{\pi}^{s}{(s)}} + {\alpha{D_{KL}{\lbrack\pi,\left. \overset{\sim}{\pi} \middle| s \right.\rbrack}}}}$, which corresponds to the definition of the soft value function. Additionally, the second term in Equation 2 can be interpreted as a soft version of the advantage function ${A{(a,s)}} = {\alpha{\log{({{\pi{(\left. a \middle| s \right.)}}/{\overset{\sim}{\pi}{(\left.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Quinoa", "weight": 1.0} -->

a \middle| s \right.)}}})}}}$, where differences in log-likelihoods are interpreted as advantages. Given this sum, a natural way to parameterise $Q$ becomes apparent. We can choose to parameterise $V_{\pi}^{s}{(s)}$ as a deep neural network, and $\pi{(\left. a \middle| s \right.)}$ as a density modelled by a normalising flow. These can be universal density estimators and hence allow $Q_{\pi}^{s}$ to model arbitrary functions. In the following, we chose to use a Real NVP architecture for our policy, as we can both sample and infer the probability density function efficiently^11^1We note that to the best of our knowledge there is no formal proof that Real NVP's are universal density function approximators, nor any counterexamples of why they would not be. Other flows such as Neural Autoregressive Flows could be used when a formal proof is required..

<!-- chunk {"id": "body-0014", "role": "body", "section": "Quinoa", "weight": 1.0} -->

In order to condition the Real NVP on the state $s$, we concatenate $s$ to the input of every neural network inside the Real NVP.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Quinoa", "weight": 1.0} -->

Using this parametrisation, we can fit $Q_{\pi}^{s}{(a,s)}$ directly by minimising the squared temporal difference error

<!-- chunk {"id": "body-0016", "role": "body", "section": "Quinoa", "weight": 1.0} -->

where $\theta$ denote policy parameters, $\phi$ are value function parameters and $\phi^{\prime}$ are the parameters of a target value function, that are periodically copied from $\phi$; and $Q_{\pi}^{s}$, $V^{s}$ are given as in Equation 2. We approximate the expectation over transition and state visitation distribution by samples from a replay buffer. A full algorithm listing of the procedure is given in Algorithms 1 and 2.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Results", "weight": 1.0} -->

We ran experiments across three domains from the DeepMind control suite, the walker, the cheetah and the hopper, as depicted in Figure 1. Our neural networks were initialised such that $Q{(a,s)}$ is identically zero in all states and actions, which means that our initial policy $\pi{(\left. a \middle| s \right.)}$ is exactly uniform. All neural networks have weight normalisation with an initialisation based on the statistics of the first batch. In order to deal with the gradients of the squashing operations in the Real NVP, we clip the gradient norm to $1$. We set the learning rate to $0.001$ and update the target network every $1000$ steps.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Results", "weight": 1.0} -->

As we can see, the performance of Quinoa is similar to the one obtained by SVG for the cheetah and the walker tasks. On the hopper task, the performance is slightly lacking behind.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Results", "weight": 1.0} -->

When analysing the policies obtained, we find that using this richer class of distributions for a policy shows a distinct behaviour which is hard to obtain using a Gaussian policy. First of all, the actions samples from this policy have limited support. As shown in Figure 2, we can observe that in some states the policy has high-skew and non-linearly correlated exploration noise during the training process. Therefore, it is clearly not following a normal distribution.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Results", "weight": 1.0} -->

Moreover, the policy shows some multimodal behaviour during training. This can be explained by the fact that the converged policy for the walker domain has actions in the extremities for most states. The policy depicted has not converged yet, but it has learned that it prefers to take actions in the extremities. In this state however, it does not know which one yet, resulting in a multimodal distribution. The scatter plots also show how some dimensions of the action space have already collapsed, while others remain high in variance in order to keep the entropy large and keep exploring the action space.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we describe a new parametrisation of the soft Q-function, such that the optimal policy can be obtained in closed form. This approach removes the need for a policy optimisation step from the learning process, simplifying standard actor-critic algorithms. We show that our algorithm is able to work across a range of tasks. We have illustrated that the policy is able to have an arbitrary distribution for its exploration noise. Moreover, we have shown that given this additional degree of freedom, the resulting policy does not show a Gaussian behaviour, with long tails and non-linearly correlated noise. We find in some states the actions of the policy are distributed multimodally. In the future, we will work on expanding this approach to harder tasks.
