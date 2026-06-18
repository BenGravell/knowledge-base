Discovering the Elite Hypervolume by Leveraging Interspecies Correlation

Topics include Robotics.

Evolution has produced an astonishing diversity of species, each filling a different niche. Algorithms like MAP-Elites mimic this divergent evolutionary process to find a set of behaviorally diverse but high-performing solutions, called the elites. Our key insight is that species in nature often share a surprisingly large part of their genome, in spite of occupying very different niches; similarly, the elites are likely to be concentrated in a specific "elite hypervolume" whose shape is defined by their common features. In this paper, we first introduce the elite hypervolume concept and propose two metrics to characterize it: the genotypic spread and the genotypic similarity. We then introduce a new variation operator, called "directional variation", that exploits interspecies (or inter-elites) correlations to accelerate the MAP-Elites algorithm. We demonstrate the effectiveness of this operator in three problems (a toy function, a redundant robotic arm, and a hexapod robot).

## Introduction

The astonishing diversity and elegance of life forms has long been an inspiration for creative algorithms that attempt to mimic the evolutionary process. Nevertheless, current evolutionary algorithms primarily view evolution as an optimization process, that is, they aim at performance, not diversity. It is therefore no wonder that most experiments in evolutionary computation do not show an explosion of diverse and surprising designs, but show instead a convergence to a single, rarely surprising "solution".

While being effective at generating a diverse set of high-performing solutions, MAP-Elites requires numerous fitness evaluations to do so. For instance, a few million evaluations are typically used when evolving behavioral repertoires for robots. The objective of this paper is to propose an updated MAP-Elites that uses fewer evaluations for similar or better results.

If we translate the concept that "high-performing species have many things in common" to evolutionary computation, we conclude that all the elites of the search space, as found by MAP-Elites, are likely to be concentrated in a sub-part of the genotypic space (Fig. 1). We propose to call this sub-part of the genotypic space the "elite hypervolume". Describing this sub-part would correspond to writing the "recipe" for high-performing solutions. For instance, all the high-speed walking controllers might need to use the same high-frequency oscillator, in spite of very different gait patterns.

## Conclusion and Discussion

In this paper, we demonstrated that when using illumination algorithms in certain tasks (here the Schwefel function and the arm experiment), the set of solutions returned by the algorithms form an elite hypervolume in genotype space. We introduced two metrics, the genotypic spread and the genotypic similarity, to empirically characterize this hypervolume, as well as a variation operator that can exploit correlations between solutions.
