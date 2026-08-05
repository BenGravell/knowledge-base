<!-- arxiv-full-text:v1 {"arxiv_id": "1706.06643", "source": "arxiv-pdf"} -->

## Notation and Background

We assume that the reader is familiar with the seminal paper by Sutton et al., which shows how the policy gradient theorem can be extended to include function approximation and action-independent baselines. Our paper is intended to be read immediately after reviewing Section 3 of the paper by Sutton et al.. Although here we adopt the episodic setting, the extension of this work to the average reward setting is straightforward. We use the notational standard MDPNv1 and the following additional definitions, where expectations conditioned on θ denote that actions, A t, are sampled from π (S t, ·, θ) unless otherwise specified: State value function: State-action value function: Discounted state distribution: Compatible function approximator:

## The Policy Gradient Theorem With Function Approximation and ActionIndependent Baselines

The policy gradient theorem with function approximation and actionindependent baselines, as presented by Sutton et al., states that for all b: S → R, The action-independent baseline, b, does not add bias because: However, introducing an action-dependent baseline, b: S × A → R, can introduce bias because b (s, a) cannot be pulled out of the sum over actions, and so the derivative of the sum over actions does not necessarily evaluate to zero.

## The Policy Gradient Theorem With Function Approximation and ActionDependent Baselines

We will show how an action-dependent baseline, b: S × A → R, can be incorporated into the policy gradient theorem with function approximation without introducing bias. To do so, we define a different loss function, ˜ L: Intuitively, L is minimized by weights, w, that cause f w (s, a) to approximate the state-action value function, q θ (s, a), while ˜ L is minimized by weights that cause f w (s, a) to approximate the residual error after the baseline is subtracted from the state-action value function. Let In Theorem 1 we show that using an action-dependent baseline does not introduce bias if the compatible function approximator is trained to estimate the residual rather than the state-action value function, i.e., if we use w ⋆ rather than w ⋆: ˜ Theorem 1 (Policy gradient theorem with function approximation and action-dependent baseline). For any action-dependent baseline, b: S × A → R, Proof. By the definition of w ⋆ we have that:

## Discussion

Theorem 1 has interesting ramifications-it suggests several new policy gradient algorithms. First, one might define b ( s, a ) to be an estimate of q θ ( s, a ) constructed from an approximate MDP model, for example, one built from expert knowledge. Alternatively, one might estimate b ( s, a ) from data. In this latter setting, one might parameterize b by a vector, x, and tune x to make b x approximate q θ. This could be done prior to approximating ˜ w ⋆, or could be done simultaneously by viewing ˆ q w,x ( s, a ):= f w ( s, a ) + b x ( s, a ) as a new function approximator with parameter vector ( w ᵀ, x ᵀ ) ᵀ, and searching for weights that make ˆ q w,x approximate q θ.
