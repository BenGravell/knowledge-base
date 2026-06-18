<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Fast Parallel Matrix Inversion Algorithms

Topics include Parallel algorithms, Matrix inversion, Linear systems, Determinants, Characteristic polynomial, Arithmetic complexity, NC algorithms.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Csanky gives polylogarithmic-time parallel algorithms for matrix inversion, linear-system solution, determinants, and characteristic polynomials using a polynomial number of processors. The paper is a landmark in parallel complexity because it places basic linear-algebra primitives within efficient parallel computation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, an investigation of the parallel arithmetic complexity of matrix inversion, solving systems of linear equations, computing determinants and computing the characteristic polynomial of a matrix is reported. The parallel arithmetic complexity of solving equations has been an open question for several years. The gap between the complexity of the best algorithms (2n + 0, where n is the number of unknowns/ equations) and the only proved lower bound (2 log n (All logarithms in this paper are of base two.)) was huge. The first breakthrough came when Csanky reported that the parallel arithmetic complexity of all these four problems has the same growth rate and exhibited an algorithm that computes these problems in 2n - O(log2n) steps. It will be shown in the sequel that the parallel arithmetic complexity of all these four problems is upper bounded by O(log2n) and the algorithms that establish this bound use a number of processors polynomial in n. This disproves I. Munro's conjecture.
