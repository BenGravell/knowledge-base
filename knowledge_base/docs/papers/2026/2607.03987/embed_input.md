<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Fast Asymptotically Optimal Kinodynamic Planning via Vectorization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Sampling-based motion planners have been shown to be effective for systems with complex kinodynamic constraints and high dimensionality. However, these algorithms struggle to achieve real-time performance, leading to recent efforts to parallelize planning. While GPU-accelerated planners have achieved significant speedups, existing approaches require specialized CUDA programming that limits accessibility and portability. We present Parallel Asymptotically Optimal Kinodynamic RRT (PAKR), a massively parallel kinodynamic planner leveraging JAX and the XLA compiler to achieve GPU acceleration through standard Python tooling. By combining our parallel planner with the AO-x meta-algorithm, we achieve asymptotic optimality through fast iterative replanning. We provide a theoretical analysis of probabilistic completeness, analyze the effects of batch size and branching factor on convergence, and demonstrate scalability to complex dynamics using the MuJoCo-XLA simulator. Experiments show competitive runtimes with state-of-the-art GPU planners and superior solution quality.
