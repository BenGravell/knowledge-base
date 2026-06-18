Woulda, Coulda, Shoulda: Counterfactually-Guided Policy Search

Learning policies on data synthesized by models can in principle quench the thirst of reinforcement learning algorithms for large amounts of real experience, which is often costly to acquire. However, simulating plausible experience de novo is a hard problem for many complex environments, often resulting in biases for model-based policy evaluation and search. Instead of de novo synthesis of data, here we assume logged, real experience and model alternative outcomes of this experience under counterfactual actions, actions that were not actually taken. Based on this, we propose the Counterfactually-Guided Policy Search (CF-GPS) algorithm for learning policies in POMDPs from off-policy experience. It leverages structural causal models for counterfactual evaluation of arbitrary policies on individual off-policy episodes. CF-GPS can improve on vanilla model-based RL algorithms by making use of available logged data to de-bias model predictions. In contrast to off-policy algorithms based on Importance Sampling which re-weight data, CF-GPS leverages a model to explicitly consider alternative outcomes, allowing the algorithm to make better use of experience data....

## Introduction

Imagine that a month ago Alice had two job offers from companies $a_{1}$ and $a_{2}$. She decided to join $a_{1}$ because of the larger salary, in spite of an awkward feeling during the job interview. Since then she learned a lot about $a_{1}$ and recently received information about $a_{2}$ from a friend, prodding her now to imagine what would have happened had she joined $a_{2}$. Re-evaluating her decision in hindsight in this way, she concludes that she made a regrettable decision. She could and should have known that $a_{2}$ was a better choice, had she only interpreted the cues during the interview correctly......

In spite of recent success, learning policies with standard, model-free RL algorithms can be notoriously data inefficient. This issue can in principle be addressed by learning policies on data synthesized from a model. However, a mismatch between the model and the true environment, often unavoidable in practice, can cause this approach to fail, resulting in policies that do not generalize to the real environment....

## Discussion

Simulating plausible synthetic experience de novo is a hard problem for many environments, often resulting in biases for model-based RL algorithms. The main takeaway from this work is that we can improve policy learning by evaluating counterfactual actions in concrete, past scenarios. Compared to only considering synthetic scenarios, this procedure mitigates model bias. However, it relies on some crucial assumptions that we want to briefly discuss here. The first assumption is that off-policy experience is available at all. In cases where this is e.g....

Assuming no model mismatch, CF-PE is unbiased.

Assume we have observations ${\hat{x}}_{o} \sim p$. We can simulate from $\mathcal{M}$, under any intervention $I$, i.e. obtain unbiased samples from $\mathcal{M}^{{do}{(I)}}$, by first sampling values $u_{CF}$ for an arbitrary subset $U_{CF} \subset U$ from the posterior $p{(\left. u_{CF} \middle| {\hat{x}}_{o} \right.)}$ and the remaining $U_{Prior}:={U\backslash U_{CF}}$ from the prior $p{(u_{Prior})}$, and then computing $X$ with noise $u = {u_{CF} \cup u_{Prior}}$.

## Off-Policy improvement: Counterfactually-guided policy search

We formulate model-based RL in POMDPs in terms of structural causal models, thereby connecting concepts from reinforcement learning and causal inference.
