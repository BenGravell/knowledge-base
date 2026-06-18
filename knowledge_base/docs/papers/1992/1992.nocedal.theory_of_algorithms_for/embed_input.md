Theory of Algorithms for Unconstrained Optimization

Topics include Unconstrained optimization, Nonlinear optimization, Line search, Trust region methods, Quasi-Newton methods, Conjugate gradient, Numerical optimization.

Nocedal surveys the practical theoretical understanding of major algorithms for unconstrained nonlinear optimization, focusing on methods credible enough for numerical software libraries. The article frames convergence theory around implemented behavior, especially line-search, trust-region, conjugate-gradient, and quasi-Newton methods.

A few months ago, while preparing a lecture to an audience that included engineers and numerical analysts, I asked myself the question: from the point of view of a user of nonlinear optimization routines, how interesting and practical is the body of theoretical analysis developed in this field? To make the question a bit more precise, I decided to select the best optimization methods known to date - those methods that deserve to be in a subroutine library - and for each method ask: what do we know about the behaviour of this method, as implemented in practice? To make my task more tractable, I decided to consider only algorithms for unconstrained optimization.
