Regularized Evolution for Image Classifier Architecture Search

Topics include Reinforcement learning, Neural networks, Classifiers, Accuracy, Control, Learning, Tournament selection, Evolutionary algorithms.

The effort devoted to hand-crafting neural network image classifiers has motivated the use of architecture search to discover them automatically. Although evolutionary algorithms have been repeatedly applied to neural network topologies, the image classifiers thus discovered have remained inferior to human-crafted ones. Here, we evolve an image classifier - AmoebaNet-A - that surpasses hand-designs for the first time. To do this, we modify the tournament selection evolutionary algorithm by introducing an age property to favor the younger genotypes. Matching size, AmoebaNet-A has comparable accuracy to current state-of-the-art ImageNet models discovered with more complex architecture-search methods. Scaled to larger size, AmoebaNet-A sets a new state-of-the-art 83.9% / 96.6% top-5 ImageNet accuracy. In a controlled comparison against a well known reinforcement learning algorithm, we give evidence that evolution can obtain results faster with the same hardware, especially at the earlier stages of the search. This is relevant when fewer compute resources are available. Evolution is, thus, a simple method to effectively discover high-quality architectures.

## Introduction

^00^footnotetext: Accepted for publication at AAAI 2019, the Thirty-Third AAAI Conference on Artificial Intelligence.^00^footnotetext: A brief talk from Nov 2018 summarizes this paper at

Until recently, most state-of-the-art image classifier architectures have been manually designed by human experts. To speed up the process, researchers have looked into automated methods. These methods are now collectively known as architecture-search algorithms. A traditional approach is neuro-evolution of topologies. Improved hardware now allows scaling up evolution to produce high-quality image classifiers. Yet, the architectures produced by evolutionary algorithms / genetic programming have not reached the accuracy of those directly designed by human experts. Here we evolve image classifiers that surpass hand-designs.

We presented the first controlled comparison of algorithms for image classifier architecture search in a case study of evolution, RL and random search. We showed that evolution had somewhat faster search speed and stood out in the regime of scarcer resources / early stopping. Evolution also matched RL in final model quality, employing a simpler method.

We evolved AmoebaNet-A (Figure 5), a competitive image classifier. On ImageNet, it is the first evolved model to surpass hand-designs. Matching size, AmoebaNet-A has comparable accuracy to top image-classifiers discovered with other architecture-search methods. At large size, it sets a new state-of-the-art accuracy. We open-sourced code and checkpoint.^55^5

This section complements the Methods section with the details necessary to reproduce our experiments. Possible ops: none (identity); 3x3, 5x5 and 7x7 separable (sep.) convolutions (convs.); 3x3 average (avg.) pool; 3x3 max pool; 3x3 dilated (dil.) sep. conv.; 1x7 then 7x1 conv. Evolved with $P$=$100$, $S$=$25$. CIFAR-10 dataset with 5k withheld examples for validation. Standard ImageNet dataset, 1.2M 331x331 images and 1k classes; 50k examples withheld for validation; standard validation set used for testing. During the search phase, each model trained for 25 epochs; N=3/F=24, 1 GPU....

It is common in tournament selection to keep the population size fixed at the initial value P. This is often accomplished with an additional step within each cycle: discarding (or killing) the worst model in the random S-sample....
