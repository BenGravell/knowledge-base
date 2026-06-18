Quality and Diversity Optimization: A Unifying Modular Framework

Topics include Optimization.

The optimization of functions to find the best solution according to one or several objectives has a central role in many engineering and research fields. Recently, a new family of optimization algorithms, named Quality-Diversity optimization, has been introduced, and contrasts with classic algorithms. Instead of searching for a single solution, Quality-Diversity algorithms are searching for a large collection of both diverse and high-performing solutions. The role of this collection is to cover the range of possible solution types as much as possible, and to contain the best solution for each type. The contribution of this paper is threefold. Firstly, we present a unifying framework of Quality-Diversity optimization algorithms that covers the two main algorithms of this family (Multi-dimensional Archive of Phenotypic Elites and the Novelty Search with Local Competition), and that highlights the large variety of variants that can be investigated within this family. Secondly, we propose algorithms with a new selection mechanism for Quality-Diversity algorithms that outperforms all the algorithms tested in this paper....

## Introduction

Searching for high-quality solutions within a typically high-dimensional search space is an important part of engineering and research. Intensive work has been done in recent decades to produce automated procedures to generate these solutions, which are commonly called "Optimization Algorithms". The applications of such algorithms are numerous and range from modeling purposes to product design. More recently, optimization algorithms have become the core of most machine learning techniques....

Inspired by the ability of natural evolution to generate species that are well adapted to their environment, Evolutionary Computation has a long history in the domain of optimization, particularly in stochastic optimization. For example, evolutionary methods have been used to optimize the morphologies and the neural networks of physical robots, and to infer the equations behind collected data. These optimization abilities are also the core of Evolutionary Robotics in which evolutionary algorithms are used to generate neural networks, robot behaviors, or objects.

The source code of the QD-algorithm framework is available at It is based on the Sferes~v2~ framework and implements both the grid-based and archive-based containers and several selection operators, including all those that have been evaluated in this paper. The source code of the experimental setups is available at the same location and can be used by interested readers to investigate and evaluate new QD-algorithms.

The implementation allows researchers to easily implement and evaluate new combinations of operators, while maintaining high execution speed. For this reason, we followed the policy-based design in C++, which allows developers to replace the behavior of the program simply by changing the template declarations of the algorithm. For example, changing from the grid-based container to the archive-based one only requires changing "container::Grid" to "container::Archive" in the template definition of the QD-algorithm object....

### III-B2 Uniform Random Selection

The main purpose of a container is to gather all the solutions found so far into an ordered collection, in which only the best *and* most diverse solutions are kept. One of the main differences between MAP-Elites and NSLC is the way the collection of solutions is formed....
