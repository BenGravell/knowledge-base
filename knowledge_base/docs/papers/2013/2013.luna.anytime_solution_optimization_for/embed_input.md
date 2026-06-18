<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Anytime Solution Optimization for Sampling-Based Motion Planning

Topics include Motion planning, Path optimization, Path shortcutting, Anytime planning, Sampling-based planning, Post-processing.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Anytime algorithm that progressively improves path quality after an initial solution is found, combining random shortcutting with path hybridization. Algorithm 1 gives a particularly clear presentation of the shortcutting procedure.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Recent work in sampling-based motion planning has yielded several different approaches for computing good quality paths in high degree of freedom systems: path shortcutting methods that attempt to shorten a single solution path by connecting non-consecutive configurations, a path hybridization technique that combines portions of two or more solutions to form a shorter path, and asymptotically optimal algorithms that converge to the shortest path over time. This paper presents an extensible meta-algorithm that incorporates a traditional sampling-based planning algorithm with offline path shortening techniques to form an anytime algorithm which exhibits competitive solution lengths to the best known methods and optimizers. A series of experiments involving rigid motion and complex manipulation are performed as well as a comparison with asymptotically optimal methods which show the efficacy of the proposed scheme, particularly in high-dimensional spaces.
