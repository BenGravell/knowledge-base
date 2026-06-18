Pattern-defeating Quicksort

Topics include Defeating quicksort.

A new solution for the Dutch national flag problem is proposed, requiring no three-way comparisons, which gives quicksort a proper worst-case runtime of O(nk) for inputs with k distinct elements. This is used together with other known and novel techniques to construct a hybrid sort that is never significantly slower than regular quicksort while speeding up drastically for many input distributions.

## Introduction

Arguably the most used hybrid sorting algorithm at the time of writing is introsort. A combination of insertion sort, heapsort and quicksort, it is very fast and can be seen as a truly hybrid algorithm. The algorithm performs introspection and decides when to change strategy using some very simple heuristics. If the recursion depth becomes too deep, it switches to heapsort, and if the partition size becomes too small it switches to insertion sort.

The goal of pattern-defeating quicksort (or pdqsort) is to improve on introsort's heuristics to create a hybrid sorting algorithm with several desirable properties. It maintains quicksort's logarithmic memory usage and fast real-world average case, effectively recognizes and combats worst case behavior (deterministically), and runs in linear time for a few common patterns. It also unavoidably inherits in-place quicksort's instability, so pdqsort can not be used in situations where stability is needed.

## Conclusion and further research

We conclude that the heuristics and techniques presented in this paper have little overhead, and effectively handle various input patterns. Pattern-defeating quicksort is often the best choice of algorithm overall for small to medium input sizes or data type sizes. It and other quicksort variants suffer from datasets that are too large to fit in cache, where is^4^o shines. The latter algorithm however suffers from bad performance on smaller sizes, future research could perhaps combine the best of these two algorithms.

Pattern-defeating quicksort has complexity $O{({n{\log n}})}$.

### Lemma 4

It's important to use a series of moves instead of swaps, as this eliminates a lot of unnecessary shuffling. Another big^66^65-15% from our benchmarks, for sorting small integers. improvement can be made by eliminating bounds checking in the inner insertion sort loop. This can be done for any subsequence that is not leftmost, as there must exist some element before the subsequence you're sorting that acts as a sentinel breaking the loop. Although this change is tiny, for optimal performance this requires an entirely new function as switching behavior based on a condition defeats the purpose of this micro-optimization....

In Section 2 we will explore a quick overview of pattern-defeating quicksort and related work, in Section 3 we propose our new solution for the Dutch...
