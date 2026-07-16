<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Stein Particle Filtering

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a new particle filtering algorithm for nonlinear systems in the discrete-time setting. Our algorithm is based on the Stein variational gradient descent (SVGD) framework, which is a general approach to sample from a target distribution. We merge the standard two-step paradigm in particle filtering into one step so that SVGD can be used. A distinguishing feature of the proposed algorithm is that, unlike most particle filtering methods, all the particles at any time step are equally weighted and thus no update on the weights is needed. We further extended our algorithm to allow for updating previous particles within a sliding window. This strategy may improve the reliability of the algorithm with respect to unexpected disturbance in the dynamics or outlier-measurements. The efficacy of the proposed algorithms is illustrated through several numerical examples in comparison with a standard particle filtering method.
