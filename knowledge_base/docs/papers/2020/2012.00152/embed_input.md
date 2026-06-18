Every Model Learned by Gradient Descent Is Approximately a Kernel Machine

Topics include Gradient descent, Deep learning, Learning.

Deep learning's successes are often attributed to its ability to automatically discover new representations of the data, rather than relying on handcrafted features like other learning methods. We show, however, that deep networks learned by the standard gradient descent algorithm are in fact mathematically approximately equivalent to kernel machines, a learning method that simply memorizes the data and uses it directly for prediction via a similarity function (the kernel). This greatly enhances the interpretability of deep network weights, by elucidating that they are effectively a superposition of the training examples. The network architecture incorporates knowledge of the target function into the kernel. This improved understanding should lead to better learning algorithms.

## Introduction

Despite its many successes, deep learning remains poorly understood. In contrast, kernel machines are based on a well-developed mathematical theory, but their empirical performance generally lags behind that of deep networks. The standard algorithm for learning deep networks, and many other models, is gradient descent. Here we show that every model learned by this method, regardless of architecture, is approximately equivalent to a kernel machine with a particular type of kernel. This kernel measures the similarity of the model at two data points in the neighborhood of the path taken by the model parameters during learning.

## Discussion

A notable disadvantage of deep networks is their lack of interpretability. Knowing that they are effectively path kernel machines greatly ameliorates this. In particular, the weights of a deep network have a straightforward interpretation as a superposition of the training examples in gradient space, where each example is represented by the corresponding gradient of the model. Fig. 2 illustrates this. One well-studied approach to interpreting the output of deep networks involves looking for training instances that are close to the query in Euclidean or some other simple space.

Experimentally, deep networks and kernel machines often perform more similarly than would be expected based on their mathematical formulation. Even when they generalize well, deep networks often appear to memorize and replay whole training instances. The fact that deep networks are in fact kernel machines helps explain both of these observations. It also sheds light on the surprising brittleness of deep models, whose performance can degrade rapidly as the query point moves away from the nearest training instance, since this is what is expected of kernel estimators in high-dimensional spaces.

The results in this paper suggest a number of research directions. For example, viewing gradient descent as a method for learning path kernel machines may provide new paths for improving it. Conversely, gradient descent is not necessarily the only way to form superpositions of examples that are useful for prediction. The key question is how to optimize the tradeoff between accurately capturing the target function and minimizing the computational cost of storing and matching the examples in the superposition.
