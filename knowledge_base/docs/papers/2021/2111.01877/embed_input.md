<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

AIT* and EIT*: Asymmetric Bidirectional Sampling-based Path Planning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Optimal path planning is the problem of finding a valid sequence of states between a start and goal that optimizes an objective. Informed path planning algorithms order their search with problem-specific knowledge expressed as heuristics and can be orders of magnitude more efficient than uninformed algorithms. Heuristics are most effective when they are both accurate and computationally inexpensive to evaluate, but these are often conflicting characteristics. This makes the selection of appropriate heuristics difficult for many problems. This paper presents two almost-surely asymptotically optimal sampling-based path planning algorithms to address this challenge, Adaptively Informed Trees (AIT*) and Effort Informed Trees (EIT*). These algorithms use an asymmetric bidirectional search in which both searches continuously inform each other. This allows AIT* and EIT* to improve planning performance by simultaneously calculating and exploiting increasingly accurate, problem-specific heuristics. The benefits of AIT* and EIT* relative to other sampling-based algorithms are demonstrated on twelve problems in abstract, robotic, and biomedical domains optimizing path length and obstacle clearance.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The experiments show that AIT* and EIT* outperform other algorithms on problems optimizing obstacle clearance, where a priori cost heuristics are often ineffective, and still perform well on problems minimizing path length, where such heuristics are often effective.
