<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Performance Analysis of Parallel Differential Dynamic Programming on a GPU

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Parallelism can be used to significantly increase the throughput of computationally expensive algorithms. With the widespread adoption of parallel computing platforms such as GPUs, it is natural to consider whether these architectures can benefit robotics researchers interested in solving trajectory optimization problems online. Differential Dynamic Programming (DDP) algorithms have been shown to achieve some of the best timing performance in robotics tasks by making use of optimized dynamics methods and CPU multi-threading. This paper aims to analyze the benefits and tradeoffs of higher degrees of parallelization using a multiple-shooting variant of DDP implemented on a GPU. We describe our implementation strategy and present results demonstrating its performance compared to an equivalent multi-threaded CPU implementation using several benchmark control tasks. Our results suggest that GPU-based solvers can offer increased per-iteration computation time and faster convergence in some cases, but in general tradeoffs exist between convergence behavior and degree of algorithm-level parallelism.
