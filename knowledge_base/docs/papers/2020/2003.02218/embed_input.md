The Large Learning Rate Phase of Deep Learning: The Catapult Mechanism

Topics include Gradient descent, Neural networks, Deep learning, Online algorithms, Learning.

The choice of initial learning rate can have a profound effect on the performance of deep networks. We present a class of neural networks with solvable training dynamics, and confirm their predictions empirically in practical deep learning settings. The networks exhibit sharply distinct behaviors at small and large learning rates. The two regimes are separated by a phase transition. In the small learning rate phase, training can be understood using the existing theory of infinitely wide neural networks. At large learning rates the model captures qualitatively distinct phenomena, including the convergence of gradient descent dynamics to flatter minima. One key prediction of our model is a narrow range of large, stable learning rates. We find good agreement between our model's predictions and training dynamics in realistic deep learning settings. Furthermore, we find that the optimal performance in such settings is often found in the large learning rate phase. We believe our results shed light on characteristics of models trained at different learning rates.

## Introduction

Deep learning has shown remarkable success across a variety of machine learning tasks. At the same time, our theoretical understanding of deep learning methods remains limited. In particular, the interplay between training dynamics, properties of the learned network, and generalization remains a largely open problem.

In this work we take a step toward addressing these questions. We present a dynamical mechanism that allows deep networks trained using SGD to find flat minima and achieve superior performance. Our theoretical predictions agree well with empirical results in a variety of deep learning settings. In many cases we are able to predict the regime of learning rates where optimal performance is achieved. Figure 1 summarizes our main results. This work builds on several existing results, which we now review.

\begin{overpic}[width=216.81pt,trim=0.0pt 158.5925pt 0.0pt 0.0pt,clip]{figures/fig1.pdf} \put(-1.0,2.0){\small(a)} \end{overpic}
\begin{overpic}[width=216.81pt,trim=0.0pt -5.01874pt 0.0pt 158.5925pt,clip]{figures/fig1.pdf} \put(-1.0,2.0){\small(b)} \end{overpic}
Figure 1: A summary of our main results. (a) A visualization of gradient descent dynamics derived in our theoretical setup. A 2D slice of parameter space is shown, where lighter color indicates higher loss and dots represents points visited during optimization. Initially, the loss grows rapidly while local curvature decreases.

## Discussion

In this work we took a step toward understanding the role of large learning rates in deep learning. We presented a dynamical mechanism that allows deep networks to be trained at larger learning rates than those accessible to their linear counterparts. For MSE loss, linear model training diverges when the learning rate is above the critical value $\eta_{crit} = {2/\lambda_{0}}$, where $\lambda_{0}$ is the curvature at initialization. We showed that deep networks can train for larger learning rates by navigating to an area of the landscape that has sufficiently low curvature.
