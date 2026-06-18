A Survey on Activation Functions and Their Relation with Xavier and He Normal Initialization

Topics include Activation functions, Weight initialization, Xavier initialization, He initialization, ReLU activations, Leaky ReLU, PReLU, Neural networks, Survey.

This short survey connects common activation-function choices with initialization schemes, emphasizing why nonlinear shape, saturation, and variance propagation matter together. It is useful as a bridge between activation-function cataloging and the practical initialization heuristics that make rectifier networks trainable.

In artificial neural network, the activation function and the weight initialization method play important roles in training and performance of a neural network. The question arises is what properties of a function are important/necessary for being a well-performing activation function. Also, the most widely used weight initialization methods - Xavier and He normal initialization have fundamental connection with activation function. This survey discusses the important/necessary properties of activation function and the most widely used activation functions (sigmoid, tanh, ReLU, LReLU and PReLU). This survey also explores the relationship between these activation functions and the two weight initialization methods - Xavier and He normal initialization.

## Introduction

Artificial intelligence has been trying to make intelligent machines for long. Artificial neural networks have played important roles in artificial intelligence to achieve its goal. When an artificial neural network is built to execute a task, it is programmed to perceive a pattern. The main task of an artificial neural network is to learn this pattern from data.

Since the weight vector gets updated during training, it needs to be assigned initial values before the training starts. Assigning the initial values to the weight vector is known as weight initialization. Once the weight vector is updated, the input is again passed through the network in forward direction to generate the output and calculate the loss. This process continues till the loss reaches a satisfactory minimum value. A network is said to converge when the loss achieves the satisfactory minimum value and this process is called the training of a neural network.

## Discussion

Xavier et al. strongly suggests that the sigmoid activation function easily saturates at very early stage of training. This causes the training to fail. It also suggests tanh activation function as a good alternative for the sigmoid because it does not get saturated easily. The main advantage of tanh function over sigmoid, as they show in the paper, is that its mean value is 0 (more precisely, it is a zero-centered activation function). Xavier et al. paper, as it states in the section 'Theoretical Considerations and a New Normalized Initialization', assumes a linear regime of the network.

To explore the relation between Xavier and rectifier nonlinearities, He et al. paper discusses an experiment where they experiment a 22 layered neural network and a 30 layered neural network. ReLU has been used as activation functions and Xavier initialization has been used as weight initializer in the experiment. The experiment shows that the 22 layered network converges while the 30 layered network fails to converge. Siddharth et al. shows the reason behind this failure as - 'the variance of the inputs to the deeper layers is exponentially smaller than the variance of the inputs to the shallower layer'.
