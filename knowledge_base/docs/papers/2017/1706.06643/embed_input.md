<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Policy Gradient Methods for Reinforcement Learning with Function Approximation and Action-Dependent Baselines

Topics include Policy gradients, Reinforcement learning, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We show how an action-dependent baseline can be used by the policy gradient theorem using function approximation, originally presented with action-independent baselines .

<!-- chunk {"id": "body-0003", "role": "body", "section": "The Policy Gradient Theorem With Function Approximation and ActionIndependent Baselines", "weight": 1.0} -->

The policy gradient theorem with function approximation and actionindependent baselines, as presented by Sutton et al., states that for all b: S → R, The action-independent baseline, b, does not add bias because: However, introducing an action-dependent baseline, b: S × A → R, can introduce bias because b (s, a) cannot be pulled out of the sum over actions, and so the derivative of the sum over actions does not necessarily evaluate to zero.

<!-- chunk {"id": "body-0004", "role": "body", "section": "The Policy Gradient Theorem With Function Approximation and ActionDependent Baselines", "weight": 1.0} -->

We will show how an action-dependent baseline, b: S × A → R, can be incorporated into the policy gradient theorem with function approximation without introducing bias. To do so, we define a different loss function, ˜ L: Intuitively, L is minimized by weights, w, that cause f w (s, a) to approximate the state-action value function, q θ (s, a), while ˜ L is minimized by weights that cause f w (s, a) to approximate the residual error after the baseline is subtracted from the state-action value function. Let In Theorem 1 we show that using an action-dependent baseline does not introduce bias if the compatible function approximator is trained to estimate the residual rather than the state-action value function, i.e., if we use w ⋆ rather than w ⋆: ˜ Theorem 1 (Policy gradient theorem with function approximation and action-dependent baseline). For any action-dependent baseline, b: S × A → R, Proof.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Discussion", "weight": 1.5} -->

Theorem 1 has interesting ramifications-it suggests several new policy gradient algorithms. First, one might define b ( s, a ) to be an estimate of q θ ( s, a ) constructed from an approximate MDP model, for example, one built from expert knowledge. Alternatively, one might estimate b ( s, a ) from data. In this latter setting, one might parameterize b by a vector, x, and tune x to make b x approximate q θ. This could be done prior to approximating ˜ w ⋆, or could be done simultaneously by viewing ˆ q w,x ( s, a ):= f w ( s, a ) + b x ( s, a ) as a new function approximator with parameter vector ( w ᵀ, x ᵀ ) ᵀ, and searching for weights that make ˆ q w,x approximate q θ.
