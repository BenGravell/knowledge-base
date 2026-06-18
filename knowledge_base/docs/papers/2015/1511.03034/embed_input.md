Learning with a Strong Adversary

The robustness of neural networks to intended perturbations has recently attracted significant attention. In this paper, we propose a new method, learning with a strong adversary, that learns robust classifiers from supervised data. The proposed method takes finding adversarial examples as an intermediate step. A new and simple way of finding adversarial examples is presented and experimentally shown to be efficient. Experimental results demonstrate that resulting learning method greatly improves the robustness of the classification models produced.

## Introduction

Deep Neural Network (DNN) models have recently demonstrated impressive learning results in many visual and speech classification problems. One reason for this success is believed to be the expressive capacity of deep network architectures. Even though classifiers are typically evaluated by their misclassification rate, robustness is also a highly desirable property: intuitively, it is desirable for a classifier to be 'smooth' in the sense that a small perturbation of its input should not change its predictions significantly. An intriguing recent discovery is that DNN models do not typically possess such a robustness property.

The main achievement of this paper is a training method that is able to produce robust classifiers with high classification accuracy in the face of stronger data perturbation. The approach we propose differs from previous approaches in a few ways. First, Goodfellow et al. suggests using an augmented objective that combines the original training objective with an additional objective that is measured after after the training inputs have been perturbed. Alternatively, suggest, as a specialization of the method , to only use the objective defined on the perturbed data.

The remainder of the paper is organized as follows. First, we propose a new method for finding adversarial examples in Section 2. Section 3 is then devoted to developing the main method: a new procedure for learning with a stronger form of adversary. Finally, we provide an experimental evaluation of the proposed method on MNIST and CIFAR-10 in Section 4.

## Conclusion

We investigate the curious phenomenon of 'adversarial perturbation' in a formal min-max problem setting. A generic algorithm is developed based on the proposed min-max formulation, which is more general and allows to replace previous heuristic algorithms with formally derived ones. We also propose a more efficient way in finding adversarial examples for a given network. The experimental results suggests that learning with a strong adversary is promising in the sense that compared to the benchmarks in the literature, it achieves significantly better robustness while maintain high normal accuracy.
