Searching for Activation Functions

Topics include Activation functions, Swish, Neural architecture search, Reinforcement learning, ImageNet, ReLU alternatives, Deep learning.

This paper uses search over activation-function expressions to discover Swish, a smooth self-gated nonlinearity of the form x times a sigmoid. The empirical result is important less because every searched function transfers, and more because a simple ReLU-like smooth gate became a strong activation baseline for deep vision networks.

The choice of activation functions in deep networks has a significant effect on the training dynamics and task performance. Currently, the most successful and widely-used activation function is the Rectified Linear Unit (ReLU). Although various hand-designed alternatives to ReLU have been proposed, none have managed to replace it due to inconsistent gains. In this work, we propose to leverage automatic search techniques to discover new activation functions. Using a combination of exhaustive and reinforcement learning-based search, we discover multiple novel activation functions. We verify the effectiveness of the searches by conducting an empirical evaluation with the best discovered activation function. Our experiments show that the best discovered activation function, f(x) = x * sigmoid(beta x), which we name Swish, tends to work better than ReLU on deeper models across a number of challenging datasets. For example, simply replacing ReLUs with Swish units improves top-1 classification accuracy on ImageNet by 0.9\% for Mobile NASNet-A and 0.6\% for Inception-ResNet-v2.

## Introduction

At the heart of every deep network lies a linear transformation followed by an activation function $f{( \cdot )}$. The activation function plays a major role in the success of training deep neural networks. Currently, the most successful and widely-used activation function is the Rectified Linear Unit (ReLU), defined as ${f{(x)}} = {\max{(x,0)}}$. The use of ReLUs was a breakthrough that enabled the fully supervised training of state-of-the-art deep networks. Deep networks with ReLUs are more easily optimized than networks with sigmoid or tanh units, because gradients are able to flow when the input to the ReLU function is positive.

While numerous activation functions have been proposed to replace ReLU, none have managed to gain the widespread adoption that ReLU enjoys. Many practitioners have favored the simplicity and reliability of ReLU because the performance improvements of the other activation functions tend to be inconsistent across different models and datasets.

The activation functions proposed to replace ReLU were hand-designed to fit properties deemed to be important. However, the use of search techniques to automate the discovery of traditionally human-designed components has recently shown to be extremely effective. For example, Zoph et al. used reinforcement learning-based search to find a replicable convolutional cell that outperforms human-designed architectures on ImageNet.

## Conclusion

In this work, we utilized automatic search techniques to discover novel activation functions that have strong empirical performance. We then empirically validated the best discovered activation function, which we call Swish and is defined as ${f{(x)}} = {{x \cdot \text{sigmoid}}{({\betax})}}$. Our experiments used models and hyperparameters that were designed for ReLU and just replaced the ReLU activation function with Swish; even this simple, suboptimal procedure resulted in Swish consistently outperforming ReLU and other activation functions.
