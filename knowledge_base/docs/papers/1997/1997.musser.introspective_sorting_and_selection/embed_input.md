<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Introspective Sorting and Selection Algorithms

Topics include Sorting algorithms, Introsort, Selection algorithms, Quicksort, Heapsort, Generic programming, Worst-case guarantees.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces introspective sorting and selection, hybrid algorithms that begin with fast partitioning methods and switch to worst-case-safe alternatives when recursion depth grows too large. Introsort keeps quicksort-like average performance while guaranteeing O(N log N) sorting time, which helped shape practical standard-library sorting implementations.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Quicksort is the preferred in-place sorting algorithm in many contexts, since its average computing time on uniformly distributed inputs is Θ(N log N), and it is in fact faster than most other sorting algorithms on most inputs. Its drawback is that its worst-case time bound is Θ(N2). Previous attempts to protect against the worst case by improving the way quicksort chooses pivot elements for partitioning have increased the average computing time too much – one might as well use heapsort, which has a Θ(N log N) worst-case time bound, but is on the average 2–5 times slower than quicksort. A similar dilemma exists with selection algorithms (for finding the i-th largest element) based on partitioning. This paper describes a simple solution to this dilemma: limit the depth of partitioning, and for subproblems that exceed the limit switch to another algorithm with a better worst-case bound. Using heapsort as the ‘stopper’ yields a sorting algorithm that is just as fast as quicksort in the average case, but also has an Θ(N log N) worst case time bound.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

For selection, a hybrid of Hoare's FIND algorithm, which is linear on average but quadratic in the worst case, and the Blum–Floyd–Pratt–Rivest–Tarjan algorithm is as fast as Hoare's algorithm in practice, yet has a linear worst-case time bound. Also discussed are issues of implementing the new algorithms as generic algorithms, and accurately measuring their performance in the framework of the C+:+ Standard Template Library.
