<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Reasoning-Driven Synthetic Data Generation and Evaluation

Topics include Synthetic data, Data generation, Generative models, Data evaluation, Agentic systems.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Simula generates and evaluates synthetic datasets through a seedless, reasoning-driven process. It lets users specify dataset characteristics and allocate generation resources, then assesses both dataset properties and downstream results.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Although many AI applications of interest require specialized multi-modal models, relevant data to train such models is inherently scarce or inaccessible. Filling these gaps with human annotators is prohibitively expensive, error-prone, and time-consuming, leading model builders to increasingly consider synthetic data as a scalable alternative. However, existing synthetic data generation methods often rely on manual prompts, evolutionary algorithms, or extensive seed data from the target distribution - limiting their scalability, explainability, and control. In this paper, we introduce Simula: a novel reasoning-driven framework for data generation and evaluation. It employs a seedless, agentic approach to generate synthetic datasets at scale, allowing users to define desired dataset characteristics through an explainable and controllable process that enables fine-grained resource allocation. We show the efficacy of our approach on a variety of datasets, rigorously testing both intrinsic and downstream properties. Our work offers guidelines for synthetic data mechanism design, provides insights into generating and evaluating synthetic data at scale, and unlocks new opportunities for developing and deploying AI in domains where data scarcity or privacy concerns are paramount.
