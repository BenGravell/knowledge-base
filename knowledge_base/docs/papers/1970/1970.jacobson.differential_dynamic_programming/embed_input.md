<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Differential Dynamic Programming

Topics include Differential dynamic programming, Trajectory optimization, Optimal control, Dynamic programming.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Foundational text introducing Differential Dynamic Programming (DDP), a trajectory optimization method that uses second-order Taylor expansions of the value function within a dynamic programming framework for efficient nonlinear optimal control.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

It is the authors' intention that this book accomplish the following objectives: 1. To illustrate the use of the principle of optimality, locally, in the neighborhood of a nominal trajectory, in the development of new successive approximation algorithms for determining optimal trajectories for a wide variety of dynamic optimization problems, 2. To provide complete details of the derivations of the algorithms, giving rules for their implementation, and including illustrative and computed examples, 3. To indicate the possible advantages over conventional procedures that these algorithms may possess, 4. To report some generalizations of the deterministic algorithms to problems of optimal stochastic control. The book is intended for applied scientists whose projects might involve dynamic optimization either in design or implementation, graduate students in engineering and applied physics, and practicing engineers. The mathematical treatment of the material is not intended to be rigorous; that is, results are not stated in theorem and lemma form. Rather, the reader is encouraged by the use of intuitive reasoning to take part in the derivations of the algorithms and in the interpretation of the theoretical and computational results. Derivations of necessary conditions of optimality via dynamic programming have been reported by S. E.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Dreyfus, who has also indicated the usefulness of the intuitive nature of dynamic programming in stochastic situations. Differential dynamic programming is, however, concerned with the development of actual numerical techniques based on the conceptual framework of dynamic programming; in this sense the present volume appears to be unique. The organization of this book is indicated by the following outline: In Chapter 1 the class of dynamic optimization problems to be considered, is defined. Some of the most important literature references in optimal control theory and related computational procedures are given. The notion of differential dynamic programming is introduced. Chapter 2 is concerned with the development of new algorithms for the solution of optimal control problems whose optimal controls are continuous functions of time. Bang-bang control problems are treated in Chapter 3. In Chapter 4 discrete-time optimal control problems are studied. Chapters 5 and 6 are concerned with the generalization of the algorithms developed in Chapters 2 and 3 to stochastic optimal control problems. In Chapter 7 the significance of differential dynamic programming is stressed, and extensions of the technique are indicated. Appendix A contains a comparison between a differential dynamic programming algorithm and the well-known successive sweep method.
