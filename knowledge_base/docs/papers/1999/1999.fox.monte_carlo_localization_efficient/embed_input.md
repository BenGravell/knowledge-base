<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Monte Carlo Localization: Efficient Position Estimation for Mobile Robots

Topics include Monte Carlo localization, Particle filters, Mobile robotics, Robot localization, Markov localization, Probabilistic robotics.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces Monte Carlo Localization, a particle-filter implementation of Markov localization for mobile robots. It represents uncertain robot poses with samples, concentrates computation where probability mass lies, and reports improved accuracy with much lower memory and computation than grid-based localization.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents a new, highly efficient algorithm for mobile robot localization, called Monte Carlo Localization. Mobile robot localization has been recognized as one of the most important problems in mobile robotics. Our algorithm is a version of Markov localization, a family of probabilistic approaches that have recently been applied with great practical success. However, previous approaches were either computationally extremely cumbersome (such as grid-based approaches that represent the state space by high-resolution 3D grids), or had to resort to extremely coarse-grained resolution. Our approach is computationally efficient while retaining the ability to represent (almost) arbitrary distributions. It applies highly efficient sampling-based methods for approximating probability distributions. This approach places computation exactly where needed. The number of samples is adapted on-line, thereby invoking large sample sets only when needed. Empirical results illustrate that Monte Carlo Localization is an extremely efficient on-line algorithm, characterized by better accuracy and an order of magnitude lower computation and memory requirement when compared to previous approaches. It is also much easier to implement.
