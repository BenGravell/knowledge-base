Learning with a Strong Adversary

The robustness of neural networks to intended perturbations has recently attracted significant attention. In this paper, we propose a new method, learning with a strong adversary, that learns robust classifiers from supervised data. The proposed method takes finding adversarial examples as an intermediate step. A new and simple way of finding adversarial examples is presented and experimentally shown to be efficient. Experimental results demonstrate that resulting learning method greatly improves the robustness of the classification models produced.

## Introduction

Deep Neural Network (DNN) models have recently demonstrated impressive learning results in many visual and speech classification problems. One reason for this success is believed to be the expressive capacity of deep network architectures. Even though classifiers are typically evaluated by their misclassification rate, robustness is also a highly desirable property: intuitively, it is desirable for a classifier to be 'smooth' in the sense that a small perturbation of its input should not change its predictions significantly. An intriguing recent discovery is that DNN models do not typically possess such a robustness property....

Since the appearance of Szegedy et al., increasing attention has been paid to the curious phenomenon of 'adversarial perturbation' in the deep learning community; see, for example. Goodfellow et al. suggest that one reason for the detrimental effect of adversarial examples lies in the implicit linearity of the classification models in high dimensional spaces. Additional exploration by Tabacof & Valle has demonstrated that, for image classification problems, adversarial images inhabit large "adversarial pockets" in the pixel space....

## Conclusion

We investigate the curious phenomenon of 'adversarial perturbation' in a formal min-max problem setting. A generic algorithm is developed based on the proposed min-max formulation, which is more general and allows to replace previous heuristic algorithms with formally derived ones. We also propose a more efficient way in finding adversarial examples for a given network. The experimental results suggests that learning with a strong adversary is promising in the sense that compared to the benchmarks in the literature, it achieves significantly better robustness while maintain high normal accuracy.

### Computing the perturbation

1. When taking $\ell$ to be the logistic loss, $g$ to be a linear function, and the norm for perturbation to be $\ell_{\infty}$, then the inner max problem has analytical solution, and Equation matches the learning objective in Section 5 of.\
2. Let $\ell$ be the negative log function and $g$ be the probability predicted by the model. Viewing $y_{i}$ as a distribution that has weight 1 on $y_{i}$ and $0$ on other classes, then the classical entropy loss is in fact $D_{KL}{({y_{i} \parallel p})}$ where $p = {g{(x_{i})}}$....
