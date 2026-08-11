<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Anytime RRTs

Topics include Rapidly-exploring random tree, Anytime planning, Sampling-based planning, Path optimization, Cost maps, Multi-robot planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Turns RRT into an anytime planner by repeatedly building trees that reuse information and enforce a user-selected improvement bound. It produces a feasible path quickly, then steadily lowers path cost as more planning time becomes available.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present an anytime algorithm for planning paths through high-dimensional, non-uniform cost search spaces. Our approach works by generating a series of Rapidly-exploring Random Trees (RRTs), where each tree reuses information from previous trees to improve its growth and the quality of its resulting path. We also present a number of modifications to the RRT algorithm that we use to bias the search in favor of less costly solutions. The resulting approach is able to produce an initial solution very quickly, then improve the quality of this solution while deliberation time allows. It is also able to guarantee that subsequent solutions will be better than all previous ones by a user-defined improvement bound. We demonstrate the effectiveness of the algorithm on both single robot and multirobot planning domains.
