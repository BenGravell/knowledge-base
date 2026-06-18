Deep Double Descent: Where Bigger Models and More Data Hurt

Topics include Deep learning, Learning.

We show that a variety of modern deep learning tasks exhibit a "double-descent" phenomenon where, as we increase model size, performance first gets worse and then gets better. Moreover, we show that double descent occurs not just as a function of model size, but also as a function of the number of training epochs. We unify the above phenomena by defining a new complexity measure we call the effective model complexity and conjecture a generalized double descent with respect to this measure. Furthermore, our notion of model complexity allows us to identify certain regimes where increasing (even quadrupling) the number of train samples actually hurts test performance.

## Introduction

Figure 1: Left: Train and test error as a function of model size, for of varying width on CIFAR-10 with 15% label noise. Right: Test error, shown for varying train epochs. All models trained using Adam for 4K epochs. The largest model (width 64) corresponds to standard.

The *bias-variance trade-off* is a fundamental concept in classical statistical learning theory (e.g., Hastie et al. ). The idea is that models of higher complexity have lower bias but higher variance. According to this theory, once model complexity passes a certain threshold, models "overfit" with the variance term dominating the test error, and hence from this point onward, increasing model complexity will only *decrease* performance (i.e., increase test error). Hence conventional wisdom in classical statistics is that, once we pass a certain threshold, *"larger models are worse."*

Other notions of model complexity which do not incorporate features and would not suffice to characterize the location of the double-descent peak. Rademacher complexity, for example, is determined by the ability of a model architecture to fit a randomly-labeled train set. But Rademacher complexity and VC dimension are both insufficient to determine the model-wise double descent peak location, since they do not depend on the distribution of labels--- and our experiments show that adding label noise shifts the location of the peak.

Moreover, both Rademacher complexity and VC dimension depend only on the model family and data distribution, and not on the training procedure used to find models. Thus, they are not capable of capturing train-time double-descent effects, such as "epoch-wise" double descent, and the effect of data-augmentation on the peak location.

(b) CIFAR-10. There is a “plateau” in test error around the interpolation point with no label noise, which develops into a peak for added label noise.

We believe Hypothesis 1 ‣ 2 Our results ‣ Deep Double Descent: Where Bigger Models and More Data Hurt") sheds light on the interaction between optimization algorithms, model size, and test performance and helps reconcile some of the competing intuitions about them....
