Dream to Control: Learning Behaviors by Latent Imagination

Topics include World models, Deep learning, Reinforcement learning, Latent, Imagination, Complex behaviors.

Build on the predecessor work PlaNet and learns an actor-critic model in place of online planning with the cross entropy method.

Learned world models summarize an agent's experience to facilitate learning complex behaviors. While learning world models from high-dimensional sensory inputs is becoming feasible through deep learning, there are many potential ways for deriving behaviors from them. We present Dreamer, a reinforcement learning agent that solves long-horizon tasks from images purely by latent imagination. We efficiently learn behaviors by propagating analytic gradients of learned state values back through trajectories imagined in the compact state space of a learned world model. On 20 challenging visual control tasks, Dreamer exceeds existing approaches in data-efficiency, computation time, and final performance.

## Introduction

Figure 1: Dreamer learns a world model from past experience and efficiently learns farsighted behaviors in its latent space by backpropagating value estimates back through imagined trajectories.

Intelligent agents can achieve goals in complex environments even though they never encounter the exact same situation twice. This ability requires building representations of the world from past experience that enable generalization to novel situations. World models offer an explicit way to represent an agent's knowledge about the world in a parametric model that can make predictions about the future.

## Conclusion

We present Dreamer, an agent that learns long-horizon behaviors purely by latent imagination. For this, we propose an actor critic method that optimizes a parametric policy by propagating analytic gradients of multi-step values back through learned latent dynamics. Dreamer outperforms previous methods in data-efficiency, computation time, and final performance on a variety of challenging continuous control tasks with image inputs. We further show that Dreamer is applicable to tasks with discrete actions and early episode termination....

### Comparison to actor critic methods

Dreamer learns long-horizon behaviors in the compact latent space of a learned world model by efficiently leveraging the neural network latent dynamics. For this, we propagate stochastic gradients of multi-step returns through neural network predictions of actions, states, rewards, and values using reparameterization. This section describes the main contribution of our paper.

Predicting pixels can require high model capacity. We can also encourage mutual information between model states and observations by instead predicting the states from the images. This replaces the observation model with a state model,

When the sensory inputs are high-dimensional images, latent dynamics models can abstract observations to predict forward in compact state spaces. Compared to predictions in image space, latent states have a small memory footprint that enables imagining thousands of trajectories in parallel. Learning effective latent dynamics models is becoming feasible through advances in deep learning and latent variable models.

Behaviors can be derived from dynamics models in many ways. Often, imagined rewards are maximized with a parametric policy or by online...
