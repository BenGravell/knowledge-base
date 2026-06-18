Regularized Evolution for Image Classifier Architecture Search

Topics include Reinforcement learning, Neural networks, Classifiers, Accuracy, Control, Learning, Tournament selection, Evolutionary algorithms.

The effort devoted to hand-crafting neural network image classifiers has motivated the use of architecture search to discover them automatically. Although evolutionary algorithms have been repeatedly applied to neural network topologies, the image classifiers thus discovered have remained inferior to human-crafted ones. Here, we evolve an image classifier - AmoebaNet-A - that surpasses hand-designs for the first time. To do this, we modify the tournament selection evolutionary algorithm by introducing an age property to favor the younger genotypes. Matching size, AmoebaNet-A has comparable accuracy to current state-of-the-art ImageNet models discovered with more complex architecture-search methods. Scaled to larger size, AmoebaNet-A sets a new state-of-the-art 83.9% / 96.6% top-5 ImageNet accuracy. In a controlled comparison against a well known reinforcement learning algorithm, we give evidence that evolution can obtain results faster with the same hardware, especially at the earlier stages of the search. This is relevant when fewer compute resources are available. Evolution is, thus, a simple method to effectively discover high-quality architectures.

## Introduction

^00^footnotetext: Accepted for publication at AAAI 2019, the Thirty-Third AAAI Conference on Artificial Intelligence.^00^footnotetext: A brief talk from Nov 2018 summarizes this paper at

Until recently, most state-of-the-art image classifier architectures have been manually designed by human experts. To speed up the process, researchers have looked into automated methods. These methods are now collectively known as architecture-search algorithms. A traditional approach is neuro-evolution of topologies. Improved hardware now allows scaling up evolution to produce high-quality image classifiers. Yet, the architectures produced by evolutionary algorithms / genetic programming have not reached the accuracy of those directly designed by human experts. Here we evolve image classifiers that surpass hand-designs.

To do this, we make two additions to the standard evolutionary process. First, we propose a change to the well-established tournament selection evolutionary algorithm that we refer to as aging evolution or regularized evolution. Whereas in tournament selection, the best genotypes (architectures) are kept, we propose to associate each genotype with an age, and bias the tournament selection to choose the younger genotypes. We will show that this change turns out to make a difference. The connection to regularization will be clarified in the Discussion section.

## Discussion

This section will suggest directions for future work, which we will motivate by speculating about the evolutionary process and by summarizing additional minor results. The details of these minor results have been relegated to the supplements, as they are not necessary to understand or reproduce our main results above.

Scope of results. Some of our findings may be restricted to the search spaces and datasets we used. A natural direction for future work is to extend the controlled comparison to more search spaces, datasets, and tasks, to verify generality, or to more algorithms. Supplement A presents preliminary results, performing evolutionary and RL searches over three search spaces (SP-I: same as in the Results section; SP-II: like SP-I but with more possible ops; SP-III: like SP-II but with more pairwise combinations) and three datasets (gray-scale CIFAR-10, MNIST, and gray-scale ImageNet), at a small-compute scale (on CPU, $F$=$8$, $N$=$1$).
