Gradient Descent on Neural Networks Typically Occurs at the Edge of Stability

Topics include Gradient descent, Stability analysis, Neural networks, Optimization, Edge of stability.

We empirically demonstrate that full-batch gradient descent on neural network training objectives typically operates in a regime we call the Edge of Stability. In this regime, the maximum eigenvalue of the training loss Hessian hovers just above the numerical value 2 / (step size), and the training loss behaves non-monotonically over short timescales, yet consistently decreases over long timescales. Since this behavior is inconsistent with several widespread presumptions in the field of optimization, our findings raise questions as to whether these presumptions are relevant to neural network training. We hope that our findings will inspire future efforts aimed at rigorously understanding optimization at the Edge of Stability. Code is available at

## Introduction

Neural networks are almost never trained using (full-batch) gradient descent, even though gradient descent is the conceptual basis for popular optimization algorithms such as SGD. In this paper, we train neural networks using gradient descent, and find two surprises. First, while little is known about the dynamics of neural network training in general, we find that in the special case of gradient descent, there is a simple characterization that holds across a broad range of network architectures and tasks. Second, this characterization is strongly at odds with prevailing beliefs in optimization.

Figure 1: Gradient descent typically occurs at the Edge of Stability. On three architectures, we run gradient descent at a range of step sizes η, and plot both the train loss (top row) and the sharpness (bottom row). For each step size η, observe that the sharpness rises to 2/η (marked by the horizontal dashed line of the appropriate color) and then hovers right at, or just above, this value.

## Conclusion

We have empirically demonstrated that the behavior of gradient descent on neural training objectives is both surprisingly consistent across architectures and tasks, and surprisingly different from that envisioned in the conventional wisdom. Our findings raise a number of questions. Why does progressive sharpening occur? At the Edge of Stability, by what mechanism does gradient descent avoid diverging entirely? Since the conventional wisdom for step size selection is wrong, how should the gradient descent step size be set during deep learning?...

### Related work

We do not know why progressive sharpening occurs, or whether "sharp" solutions differ in any important way from "not sharp" solutions. These are important questions for future work. Note that Mulayoff & Michaeli studied the latter question in the context of deep linear networks.

Architectures. In Appendix J. and Figure 7.1, we fix the task of training a 5k subset of CIFAR-10, and we systematically vary the network architecture. We consider fully-connected networks, as well as convolutional networks with both max-pooling and average pooling. For all of these architectures, we consider tanh, ReLU, and ELU activations, and for fully-connected networks we moreover consider softplus and hardtanh ---- eleven networks in total. We train each network with both cross-entropy and MSE loss....
