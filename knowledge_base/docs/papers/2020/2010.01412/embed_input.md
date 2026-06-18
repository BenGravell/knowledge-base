Sharpness-Aware Minimization for Efficiently Improving Generalization

Topics include Gradient descent, Robustness, Datasets, Benchmarks, Generalization, Optimization, Learning, SAM, Sharpness-aware minimization.

In today's heavily overparameterized models, the value of the training loss provides few guarantees on model generalization ability. Indeed, optimizing only the training loss value, as is commonly done, can easily lead to suboptimal model quality. Motivated by prior work connecting the geometry of the loss landscape and generalization, we introduce a novel, effective procedure for instead simultaneously minimizing loss value and loss sharpness. In particular, our procedure, Sharpness-Aware Minimization (SAM), seeks parameters that lie in neighborhoods having uniformly low loss; this formulation results in a min-max optimization problem on which gradient descent can be performed efficiently. We present empirical results showing that SAM improves model generalization across a variety of benchmark datasets (e.g., CIFAR-10, CIFAR-100, ImageNet, finetuning tasks) and models, yielding novel state-of-the-art performance for several. Additionally, we find that SAM natively provides robustness to label noise on par with that provided by state-of-the-art procedures that specifically target learning with noisy labels. We open source our code .

## Introduction

Modern machine learning's success in achieving ever better performance on a wide range of tasks has relied in significant part on ever heavier overparameterization, in conjunction with developing ever more effective training algorithms that are able to find parameters that generalize well. Indeed, many modern neural networks can easily memorize the training data and have the capacity to readily overfit. Such heavy overparameterization is currently required to achieve state-of-the-art results in a variety of domains.

Unfortunately, simply minimizing commonly used loss functions (e.g., cross-entropy) on the training set is typically not sufficient to achieve satisfactory generalization. The training loss landscapes of today's models are commonly complex and non-convex, with a multiplicity of local and global minima, and with different global minima yielding models with different generalization abilities.

The connection between the geometry of the loss landscape---in particular, the flatness of minima---and generalization has been studied extensively from both theoretical and empirical perspectives. While this connection has held the promise of enabling new approaches to model training that yield better generalization, practical efficient algorithms that specifically seek out flatter minima and furthermore effectively improve generalization on a range of state-of-the-art models have thus far been elusive (e.g., see; we include a more detailed discussion of prior work in Section 5).

We present here a new efficient, scalable, and effective approach to improving model generalization ability that directly leverages the geometry of the loss landscape and its connection to generalization, and is powerfully complementary to existing techniques.

## Discussion and Future Work

In this work, we have introduced SAM, a novel algorithm that improves generalization by simultaneously minimizing loss value and loss sharpness; we have demonstrated SAM's efficacy through a rigorous large-scale empirical evaluation. We have surfaced a number of interesting avenues for future work. On the theoretical side, the notion of per-data-point sharpness yielded by $m$-sharpness (in contrast to global sharpness computed over the entire training set, as has typically been studied in the past) suggests an interesting new lens through which to study generalization.
