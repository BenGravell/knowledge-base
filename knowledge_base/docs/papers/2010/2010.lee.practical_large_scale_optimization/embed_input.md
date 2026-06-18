Practical Large-Scale Optimization for Max-Norm Regularization

Topics include Max-norm regularization, Matrix factorization, Collaborative filtering, First-order methods, Large-scale optimization, Convex relaxation.

Develops scalable first-order algorithms for optimization problems with max-norm regularization using a Burer-Monteiro style factorization. The work makes max-norm models practical for collaborative filtering, graph cuts, and clustering at large scale.

The max-norm was proposed as a convex matrix regularizer by Srebro et al and was shown to be empirically superior to the trace-norm for collaborative filtering problems. Although the max-norm can be computed in polynomial time, there are currently no practical algorithms for solving large-scale optimization problems that incorporate the max-norm. The present work uses a factorization technique of Burer and Monteiro to devise scalable first-order algorithms for convex programs involving the max-norm. These algorithms are applied to solve huge collaborative filtering, graph cut, and clustering problems. Empirically, the new methods outperform mature techniques from all three areas.
