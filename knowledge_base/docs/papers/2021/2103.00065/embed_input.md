Gradient Descent on Neural Networks Typically Occurs at the Edge of Stability

Topics include Gradient descent, Stability analysis, Neural networks, Optimization, Edge of stability.

We empirically demonstrate that full-batch gradient descent on neural network training objectives typically operates in a regime we call the Edge of Stability. In this regime, the maximum eigenvalue of the training loss Hessian hovers just above the numerical value 2 / (step size), and the training loss behaves non-monotonically over short timescales, yet consistently decreases over long timescales. Since this behavior is inconsistent with several widespread presumptions in the field of optimization, our findings raise questions as to whether these presumptions are relevant to neural network training. We hope that our findings will inspire future efforts aimed at rigorously understanding optimization at the Edge of Stability. Code is available at

## Introduction

Neural networks are almost never trained using (full-batch) gradient descent, even though gradient descent is the conceptual basis for popular optimization algorithms such as SGD. In this paper, we train neural networks using gradient descent, and find two surprises. First, while little is known about the dynamics of neural network training in general, we find that in the special case of gradient descent, there is a simple characterization that holds across a broad range of network architectures and tasks. Second, this characterization is strongly at odds with prevailing beliefs in optimization.

In more detail, as we train neural networks using gradient descent with step size $\eta$, we measure the evolution of the *sharpness* --- the maximum eigenvalue of the training loss Hessian. Empirically, the behavior of the sharpness is consistent across architectures and tasks: so long as the sharpness is less than the value $2/\eta$, it tends to continually rise (§3.1). We call this phenomenon *progressive sharpening*. The significance of the value $2/\eta$ is that gradient descent on quadratic objectives is unstable if the sharpness exceeds this threshold (§2).

## Discussion

We now explain why the behavior of gradient descent at the Edge of Stability contradicts several pieces of conventional wisdom in optimization.

## Conclusion

We have empirically demonstrated that the behavior of gradient descent on neural training objectives is both surprisingly consistent across architectures and tasks, and surprisingly different from that envisioned in the conventional wisdom. Our findings raise a number of questions. Why does progressive sharpening occur? At the Edge of Stability, by what mechanism does gradient descent avoid diverging entirely? Since the conventional wisdom for step size selection is wrong, how should the gradient descent step size be set during deep learning?
