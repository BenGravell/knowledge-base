<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Approaches for Heuristically Biasing RRT Growth

Topics include Rapidly-exploring random tree, Heuristic search, Sampling-based planning, Cost maps, Exploration exploitation, Non-uniform sampling.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Biases RRT growth with heuristic path-quality estimates so sampling favors lower-cost regions while retaining exploration. The experiments show improved solution cost in binary and continuous cost spaces, and expose the tradeoff between greedier guidance and computational effort.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents several modifications to the basic rapidly-exploring random tree (RRT) search algorithm. The fundamental idea is to utilize a heuristic quality function to guide the search. Results from a relevant simulation experiment illustrate the benefit and drawbacks of the developed algorithms. The paper concludes with several promising directions for future research.
