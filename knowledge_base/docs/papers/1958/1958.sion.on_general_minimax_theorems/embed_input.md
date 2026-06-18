<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On General Minimax Theorems

Topics include Minimax theorem, Game theory, Convexity, Fixed-point theory, Optimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Proves a generalization of von Neumann's minimax theorem to quasi-convex/quasi-concave functions on compact convex sets in topological vector spaces, without requiring the sets to be finite-dimensional. The Sion minimax theorem is a foundational result in game theory and saddle-point optimization.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

von Neumann's minimax theorem can be stated as follows: if M and N are finite dimensional simplices and f is a bilinear function on M x N, then f has a saddle point, i.e.: max_{mu in M} min_{nu in N} f(mu,nu) = min_{nu in N} max_{mu in M} f(mu,nu). There have been several generalizations of this theorem. J. Ville, A. Wald, and others variously extended von Neumann's result to cases where M and N were allowed to be subsets of certain infinite dimensional linear spaces. The functions f they considered, however, were still linear. M. Shiffman seems to have been the first to have considered concave-convex functions in a minimax theorem. H. Kneser, K. Fan, and C. Berge (using induction and the method of separating two disjoint convex sets in Euclidean space by a hyperplane) got minimax theorems for concave-convex functions that are appropriately semi-continuous in one of the two variables.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Although these theorems include the previous results as special cases, they can also be shown to be rather direct consequences of von Neumann's theorem. H. Nikaido, on the other hand, using Brouwer's fixed point theorem, proved the existence of a saddle point for functions satisfying the weaker algebraic condition of being quasi-concave-convex, but the stronger topological condition of being continuous in each variable. Thus, there seem to be essentially two types of argument: one uses some form of separation of disjoint convex sets by a hyperplane and yields the theorem of Kneser-Fan (see 4.2), and the other uses a fixed point theorem and yields Nikaido's result. In this paper, we unify the two streams of thought by proving a minimax theorem for a function that is quasi-concave-convex and appropriately semi-continuous in each variable. The method of proof differs radically from any used previously. The difficulty lies in the fact that we cannot use a fixed point theorem (due to lack of continuity) nor the separation of disjoint convex sets by a hyperplane (due to lack of convexity).

<!-- chunk {"id": "abstract-0005", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The key tool used is a theorem due to Knaster, Kuratowski, Mazurkiewicz based on Sperner's lemma.
