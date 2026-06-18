Fast and Accurate Deep Network Learning by Exponential Linear Units (ELUs)

Topics include Activation functions, Exponential linear units, ReLU alternatives, Vanishing gradients, Bias shift, Neural networks, Classification, Generalization.

ELU introduces a negative saturating branch while preserving identity for positive inputs, aiming to reduce bias shift and improve optimization relative to ReLU-style activations. The experiments argue that ELUs can train faster and generalize better than ReLU and leaky ReLU baselines, including cases where batch normalization does not add further benefit.

We introduce the "exponential linear unit" (ELU) which speeds up learning in deep neural networks and leads to higher classification accuracies. Like rectified linear units (ReLUs), leaky ReLUs (LReLUs) and parametrized ReLUs (PReLUs), ELUs alleviate the vanishing gradient problem via the identity for positive values. However, ELUs have improved learning characteristics compared to the units with other activation functions. In contrast to ReLUs, ELUs have negative values which allows them to push mean unit activations closer to zero like batch normalization but with lower computational complexity. Mean shifts toward zero speed up learning by bringing the normal gradient closer to the unit natural gradient because of a reduced bias shift effect. While LReLUs and PReLUs have negative values, too, they do not ensure a noise-robust deactivation state. ELUs saturate to a negative value with smaller inputs and thereby decrease the forward propagated variation and information. Therefore, ELUs code the degree of presence of particular phenomena in the input, while they do not quantitatively model the degree of their absence....

## Introduction

Currently the most popular activation function for neural networks is the rectified linear unit (ReLU), which was first proposed for restricted Boltzmann machines and then successfully used for neural networks. The ReLU activation function is the identity for positive arguments and zero otherwise. Besides producing sparse codes, the main advantage of ReLUs is that they alleviate the vanishing gradient problem since the derivative of 1 for positive values is not contractive. However ReLUs are non-negative and, therefore, have a mean activation larger than zero.

Units that have a non-zero mean activation act as bias for the next layer. If such units do not cancel each other out, learning causes a bias shift for units in next layer. The more the units are correlated, the higher their bias shift. We will see that Fisher optimal learning, i.e., the natural gradient, would correct for the bias shift by adjusting the weight updates. Thus, less bias shift brings the standard gradient closer to the natural gradient and speeds up learning. We aim at activation functions that push activation means closer to zero to decrease the bias shift effect.

## Conclusion

We have introduced the exponential linear units (ELUs) for faster and more precise learning in deep neural networks. ELUs have negative values, which allows the network to push the mean activations closer to zero. Therefore ELUs decrease the gap between the normal gradient and the unit natural gradient and, thereby speed up learning. We believe that this property is also the reason for the success of activation functions like LReLUs and PReLUs and of batch normalization. In contrast to LReLUs and PReLUs, ELUs have a clear saturation plateau in its negative regime, allowing them to learn a more robust and stable representation....

In contrast to ReLUs, ELUs have negative values which pushes the mean of the activations closer to zero. Mean activations that are closer to zero enable faster learning as they bring the gradient closer to the natural gradient (see Theorem 2") and text thereafter). ELUs saturate to a negative value when the argument gets smaller. Saturation means a small derivative which decreases the variation and the information that is propagated to the next layer. Therefore the representation is both noise-robust and low-complex....

### Theorem 2
