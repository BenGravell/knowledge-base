<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Dynamic Programming Treatment of the Travelling Salesman Problem

Topics include Traveling salesman problem, Dynamic programming, Bellman-Held-Karp algorithm, Combinatorial optimization, Exact algorithms, Approximation methods.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Bellman gives a dynamic programming formulation of the traveling-salesman problem that solves moderate-sized instances by storing optimal partial tours over subsets of cities. The paper is one of the roots of the Bellman-Held-Karp algorithm and clarifies the exponential-but-structured tradeoff that made TSP dynamic programming a benchmark for exact combinatorial optimization.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The well-known travelling salesman problem is the following: "A salesman is required to visit once and only once each of n different cities starting from a base city, and returning to this city. What path minimizes the total distance travelled by the salesman?" The problem has been treated by a number of different people using a variety of techniques; cf. Dantzig, Fulkerson, Johnson, where a combination of ingenuity and linear programming is used, and Miller, Tucker and Zemlin, whose experiments using an all-integer program of Gomory did not produce results in cases with ten cities although some success was achieved in cases of simply four cities. The purpose of this note is to show that this problem can easily be formulated in dynamic programming terms, and resolved computationally for up to 17 cities. For larger numbers, the method presented below, combined with various simple manipulations, may be used to obtain quick approximate solutions. Results of this nature were independently obtained by M. Held and R. M. Karp, who are in the process of publishing some extensions and computational results.
