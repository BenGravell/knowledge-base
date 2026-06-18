On the Convergence of Adam and Beyond

Topics include Convex optimization, Nonconvex optimization, Stochastic optimization, Optimization, Learning.

Several recently proposed stochastic optimization methods that have been successfully used in training deep networks such as RMSProp, Adam, Adadelta, Nadam are based on using gradient updates scaled by square roots of exponential moving averages of squared past gradients. In many applications, e.g. learning with large output spaces, it has been empirically observed that these algorithms fail to converge to an optimal solution (or a critical point in nonconvex settings). We show that one cause for such failures is the exponential moving average used in the algorithms. We provide an explicit example of a simple convex optimization setting where Adam does not converge to the optimal solution, and describe the precise problems with the previous analysis of Adam algorithm. Our analysis suggests that the convergence issues can be fixed by endowing such algorithms with `long-term memory' of past gradients, and propose new variants of the Adam algorithm which not only fix the convergence issues but often also lead to improved empirical performance.

## Introduction

Stochastic gradient descent (Sgd) is the dominant method to train deep networks today. This method iteratively updates the parameters of a model by moving them in the direction of the negative gradient of the loss evaluated on a minibatch. In particular, variants of Sgd that scale coordinates of the gradient by square roots of some form of averaging of the squared coordinates in the past gradients have been particularly successful, because they automatically adjust the learning rate on a per-feature basis.

Although Adagrad works well for sparse settings, its performance has been observed to deteriorate in settings where the loss functions are nonconvex and gradients are dense due to rapid decay of the learning rate in these settings since it uses all the past gradients in the update. This problem is especially exacerbated in high dimensional problems arising in deep learning.

In this paper, we analyze this situation in detail. We rigorously prove that the intuition conveyed in the above paragraph is indeed correct; that limiting the reliance of the update on essentially only the past few gradients can indeed cause significant convergence issues.

We elucidate how the exponential moving average in the RMSprop and Adam algorithms can cause non-convergence by providing an example of simple convex optimization problem where RMSprop and Adam provably do not converge to an optimal solution. Our analysis easily extends to other algorithms using exponential moving averages such as Adadelta and Nadam as well, but we omit this for the sake of clarity.

## Discussion

In this paper, we study exponential moving variants of Adagrad and identify an important flaw in these algorithms which can lead to undesirable convergence behavior. We demonstrate these problems through carefully constructed examples where RMSprop and Adam converge to highly suboptimal solutions. In general, any algorithm that relies on an essentially fixed sized window of past gradients to scale the gradient updates will suffer from this problem.

We proposed fixes to this problem by slightly modifying the algorithms, essentially endowing the algorithms with a long-term memory of past gradients. These fixes retain the good practical performance of the original algorithms, and in some cases actually show improvements.
