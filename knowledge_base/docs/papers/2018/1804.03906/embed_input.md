Discovering the Elite Hypervolume by Leveraging Interspecies Correlation

Topics include Robotics.

Evolution has produced an astonishing diversity of species, each filling a different niche. Algorithms like MAP-Elites mimic this divergent evolutionary process to find a set of behaviorally diverse but high-performing solutions, called the elites. Our key insight is that species in nature often share a surprisingly large part of their genome, in spite of occupying very different niches; similarly, the elites are likely to be concentrated in a specific "elite hypervolume" whose shape is defined by their common features. In this paper, we first introduce the elite hypervolume concept and propose two metrics to characterize it: the genotypic spread and the genotypic similarity. We then introduce a new variation operator, called "directional variation", that exploits interspecies (or inter-elites) correlations to accelerate the MAP-Elites algorithm. We demonstrate the effectiveness of this operator in three problems (a toy function, a redundant robotic arm, and a hexapod robot).

## Introduction

The astonishing diversity and elegance of life forms has long been an inspiration for creative algorithms that attempt to mimic the evolutionary process. Nevertheless, current evolutionary algorithms primarily view evolution as an optimization process, that is, they aim at performance, not diversity. It is therefore no wonder that most experiments in evolutionary computation do not show an explosion of diverse and surprising designs, but show instead a convergence to a single, rarely surprising "solution".

Figure 1. Illumination/quality diversity algorithms search for the highest-performing solution in each behavioral niche. These solutions are likely to be concentrated in a particular, elite hypervolume because neighboring high-performing solutions often have similar genotypic features.

It is likely that selective biases for illumination algorithms, will complement the variation biases we introduced here, thus, further accelerating illumination. For instance, we could minimize the chances of sampling the regions outside the elite hypervolume by restricting the selection of the second elite which would define the direction of correlation. Such an approach bears similarities to the restricted tournament selection method from multimodal optimization....

One might wonder whether the findings of this work apply for variable-sized genotypes, such as the ones used by the NeuroEvolution of Augmenting Topologies (NEAT) algorithm. While the crossover operator of NEAT is effective in recombining variable-sized neural networks, or compositional pattern producing networks, it resembles a disruptive, mean-centric approach to recombination (e.g., see ), rather than a parent-centric one (e.g., ). Thus, an interesting research direction would be to study how correlations between graphs can be modeled and exploited....

Figure 5. The similarity between elites increases with the number of evaluations in the Schwefel function and arm task, but not in the hexapod task.

## The Elite Hypervolume

In all our experiments, we use the CVT-MAP-Elites algorithm with 10000 niches. We suspect that similar results would be obtained with other quality-diversity algorithms and variants of MAP-Elites because our main assumption is that the elites are located in a specific elite hypervolume (and not evenly spread), which does not depend on the way niches are defined.
