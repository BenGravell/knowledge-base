Training Deep Neural Networks via Direct Loss Minimization

Supervised training of deep neural nets typically relies on minimizing cross-entropy. However, in many domains, we are interested in performing well on metrics specific to the application. In this paper we propose a direct loss minimization approach to train deep neural networks, which provably minimizes the application-specific loss function. This is often non-trivial, since these functions are neither smooth nor decomposable and thus are not amenable to optimization with standard gradient-based methods. We demonstrate the effectiveness of our approach in the context of maximizing average precision for ranking problems. Towards this goal, we develop a novel dynamic programming algorithm that can efficiently compute the weight updates. Our approach proves superior to a variety of baselines in the context of action classification and object detection, especially in the presence of label noise.

## Introduction

Standard supervised neural network training involves computing the gradient of the loss function with respect to the parameters of the model, and therefore requires the loss function to be differentiable. Many interesting loss functions are, however, non-differentiable with respect to the output of the network. Notable examples are functions based on discrete outputs, as is common in labeling and ranking problems. In many cases these losses are also non-decomposable, in that they cannot be expressed as simple sums over the output units of the network.

In the context of structured prediction problems, in which the output is multi-dimensional, researchers have developed max-margin training methods that are capable of minimizing an upper bound on non-decomposable loss functions. Standard learning in this paradigm involves changing the parameters such that the model assigns a higher score to the groundtruth output than to any other output. This is typically encoded by a constraint, enforcing that the groundtruth score should be higher than that of a selected, contrastive output....

## Conclusion

In this paper we have proposed a direct loss minimization approach to train deep neural networks. We have demonstrated the effectiveness of our approach in the context of maximizing average precision for ranking problems. This involves minimizing a non-smooth and non-decomposable loss. Towards this goal we have proposed a dynamic programming algorithm that can efficiently compute the weight updates. Our experiments showed that this is beneficial when compared to a large variety of baselines in the context of action classification and object detection, particularly in the presence of noisy labels....

### Lemma 1

Alternatives to optimizing average precision are methods such as RankNet, LambdaRank and LambdaMART. For an overview, we refer the reader to Burges and references therein. Our goal here is simply to show direct loss minimization of AP as an example of our general framework.

Figure 3: Experiments on synthetic data: 3 Average Precision (AP) on the test set as a function of the number of iterations (best view in color). 3 The robustness of pos-AP compared to hinge-AP.

An alternative approach, frequently used in deep neural networks, is to train with a surrogate loss that can be easily optimized, *e.g*., cross-entropy....
