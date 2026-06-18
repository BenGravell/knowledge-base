Quality and Diversity Optimization: A Unifying Modular Framework

Topics include Optimization.

The optimization of functions to find the best solution according to one or several objectives has a central role in many engineering and research fields. Recently, a new family of optimization algorithms, named Quality-Diversity optimization, has been introduced, and contrasts with classic algorithms. Instead of searching for a single solution, Quality-Diversity algorithms are searching for a large collection of both diverse and high-performing solutions. The role of this collection is to cover the range of possible solution types as much as possible, and to contain the best solution for each type. The contribution of this paper is threefold. Firstly, we present a unifying framework of Quality-Diversity optimization algorithms that covers the two main algorithms of this family (Multi-dimensional Archive of Phenotypic Elites and the Novelty Search with Local Competition), and that highlights the large variety of variants that can be investigated within this family. Secondly, we propose algorithms with a new selection mechanism for Quality-Diversity algorithms that outperforms all the algorithms tested in this paper.

## Introduction

Searching for high-quality solutions within a typically high-dimensional search space is an important part of engineering and research. Intensive work has been done in recent decades to produce automated procedures to generate these solutions, which are commonly called "Optimization Algorithms". The applications of such algorithms are numerous and range from modeling purposes to product design. More recently, optimization algorithms have become the core of most machine learning techniques.

After a brief description of the origins of QD-algorithms in the next section, *we unify these algorithms into a single modular framework*, which opens new directions to create QD-algorithms that combine the advantages of existing methods (see section III). Moreover, we introduce a *new QD-algorithm based on this framework that outperforms the existing approaches by using a new selective pressure, named the "curiosity score"*. We also introduce a *new archive management approach for unstructured archives*, like the novelty archive.

## Conclusion and Discussion

In this paper, we presented three new contributions. First, we introduced a new framework that unifies QD-algorithms, showing for example that MAP-Elites and the Novelty Search with Local Competition are two different configurations of the same algorithm. Second, we suggested a new archive management procedure that copes with the erosion issues observed with the previous approaches using unstructured archives (like BR-evolution).

In addition to these three contributions, we presented the results of an experimental comparison between a large number of QD-algorithms, including MAP-Elites and NSLC. One of the main results that can be outlined from these experiments is that selection operators considering the collection instead of a population showed better performance on all scenarios. We can hypothesize that this results from the inherent diversity of solutions contained in the collection.
