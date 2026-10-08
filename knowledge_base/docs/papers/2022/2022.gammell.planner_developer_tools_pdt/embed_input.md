<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Planner Developer Tools (PDT): Reproducible Experiments and Statistical Analysis for Developing and Testing Motion Planners

Topics include Motion planning, Benchmarking, Reproducibility, Statistical analysis, Sampling-based planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Provides tools and controlled scenarios for reproducible sampling-based planner experiments and statistical evaluation of probabilistic performance.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The success of sampling-based planning algorithms has made their design and evaluation a popular area of research. Evaluating different algorithms is complicated due to their use of quasirandom sampling. Experiments and analysis must be designed to calculate probabilistic performance from a finite number of individual trials. This requires careful experimental design and statistical analysis. Planner Developer Tools (PDT) is a C++ project to make it easier to test, evaluate, and analyze sampling-based planners across problem domains. It provides tools to evaluate Open Motion Planning Library (OMPL) algorithms fairly and also a number of abstract scenarios that isolate specific challenging aspects of the planning problem during algorithm development. It is the result of almost 10 years of development and is available open source to the sampling-based motion planning research community.
