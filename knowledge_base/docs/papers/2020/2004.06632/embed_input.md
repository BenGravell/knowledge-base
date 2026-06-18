A Survey on Activation Functions and Their Relation with Xavier and He Normal Initialization

Topics include Activation functions, Weight initialization, Xavier initialization, He initialization, ReLU activations, Leaky ReLU, PReLU, Neural networks, Survey.

This short survey connects common activation-function choices with initialization schemes, emphasizing why nonlinear shape, saturation, and variance propagation matter together. It is useful as a bridge between activation-function cataloging and the practical initialization heuristics that make rectifier networks trainable.

In artificial neural network, the activation function and the weight initialization method play important roles in training and performance of a neural network. The question arises is what properties of a function are important/necessary for being a well-performing activation function. Also, the most widely used weight initialization methods - Xavier and He normal initialization have fundamental connection with activation function. This survey discusses the important/necessary properties of activation function and the most widely used activation functions (sigmoid, tanh, ReLU, LReLU and PReLU). This survey also explores the relationship between these activation functions and the two weight initialization methods - Xavier and He normal initialization.

## Introduction

Artificial intelligence has been trying to make intelligent machines for long. Artificial neural networks have played important roles in artificial intelligence to achieve its goal. When an artificial neural network is built to execute a task, it is programmed to perceive a pattern. The main task of an artificial neural network is to learn this pattern from data.

An artificial neural network is composed of large number of interconnected working units known as perceptrons or neurons. A perceptron is composed of four components: input node, weight vector, activation function and output node. The first component of a perceptron is the input node - it receives the input vector. I assume to have an $m$ dimensional input vector $\mathbf{x} = \begin{bmatrix}

## Conclusion

The usage of sigmoidal activation functions is decreasing as the rectifier nonlinearities are being more popular. On one hand, rectifier nonlinearities, especially ReLU, have good performance with He normal initialization in several kinds of networks. On the other hand, the performance of He normal initialization beats the performance of Xavier initialization. Though tanh activation function with Xavier initialization is used but only in cases where the network is not deep. He normal initialization along with rectifier nonlinearities, especially ReLU, get more preference when the network is deep.

The sigmoid function contains an exponential term as it can be seen from the function definition. Exponential functions have high computation cost and as a result of this, the sigmoid function has a high computational cost. Although, the function is computationally expensive, its gradient is not. Its gradient can be calculated using the formula ${f^{\prime}{(x)}} = {f{(x)}{({1 - {f{(x)}}})}}$.

Continuous: A function cannot be differentiable unless it is continuous. Differentiability is a necessary property of activation function. This makes continuity a necessary property for an activation function.

### Leaky ReLU function

The second component is the weight vector which has the same dimension as that of the input vector. Here, the weight vector is $\mathbf{w} = \begin{bmatrix}
\end{bmatrix}$. From the input vector and the weight vector, an inner product is calculated as $\mathbf{x}^{\top}\mathbf{w}$....
