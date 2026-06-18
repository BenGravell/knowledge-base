The Large Learning Rate Phase of Deep Learning: The Catapult Mechanism

Topics include Gradient descent, Neural networks, Deep learning, Online algorithms, Learning.

The choice of initial learning rate can have a profound effect on the performance of deep networks. We present a class of neural networks with solvable training dynamics, and confirm their predictions empirically in practical deep learning settings. The networks exhibit sharply distinct behaviors at small and large learning rates. The two regimes are separated by a phase transition. In the small learning rate phase, training can be understood using the existing theory of infinitely wide neural networks. At large learning rates the model captures qualitatively distinct phenomena, including the convergence of gradient descent dynamics to flatter minima. One key prediction of our model is a narrow range of large, stable learning rates. We find good agreement between our model's predictions and training dynamics in realistic deep learning settings. Furthermore, we find that the optimal performance in such settings is often found in the large learning rate phase. We believe our results shed light on characteristics of models trained at different learning rates....

## Introduction

Deep learning has shown remarkable success across a variety of machine learning tasks. At the same time, our theoretical understanding of deep learning methods remains limited. In particular, the interplay between training dynamics, properties of the learned network, and generalization remains a largely open problem.

In this work we take a step toward addressing these questions. We present a dynamical mechanism that allows deep networks trained using SGD to find flat minima and achieve superior performance. Our theoretical predictions agree well with empirical results in a variety of deep learning settings. In many cases we are able to predict the regime of learning rates where optimal performance is achieved. Figure 1 summarizes our main results. This work builds on several existing results, which we now review.

### Other open questions

There are several remaining open questions. While the model predicts a maximum learning rate of $4/\lambda_{0}$, for models with ReLU activations we find that the maximum learning rate is consistently higher. This may be due to a separate dynamical curvature-reduction mechanism that relies on ReLU. In addition, we do not explore the degree to which our results extend to softmax classification. While we expect qualitatively similar behavior there, the non-constant Hessian of the softmax cross entropy makes controlled experiments more challenging. Similarly, behavior for other optimizers such as SGD with momentum may differ....

We again take the modified large width limit $n\rightarrow\infty$, allowing the number of steps to scale logarithmically in the width. At initialization, $f_{\alpha}$, ${\overset{\sim}{f}}_{\alpha}$, and $\Theta_{\alpha\beta}$ are all of order $n^{0}$. We now analyze the gradient descent dynamics as a function of the learning rate.

### Lazy phase

We now consider the performance of trained models in the different phases discussed in this work. Keskar et al. observed a correlation between the flatness of a minimum found by SGD and the generalization performance (see Jiang et al. for additional empirical confirmation of this correlation). In this work, we showed that the minima SGD finds are flatter in the catapult phase, as measured by the top kernel eigenvalue. Our measure of flatness differs from that of Keskar et al., but we expect that these measures are correlated.
