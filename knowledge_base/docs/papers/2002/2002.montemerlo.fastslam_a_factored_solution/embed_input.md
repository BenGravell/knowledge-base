<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

FastSLAM: A Factored Solution to the Simultaneous Localization and Mapping Problem

Topics include Simultaneous localization and mapping, Particle filtering, Rao-blackwellization, Robot localization, Landmark mapping.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Factors the SLAM posterior into a distribution over robot paths and independent landmark estimates conditioned on each path. A particle filter with per-landmark filters then scales observation updates logarithmically with map size and was tested on maps with up to 50,000 landmarks.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The ability to simultaneously localize a robot and accurately map its surroundings is considered by many to be a key prerequisite of truly autonomous robots. However, few approaches to this problem scale up to handle the very large number of landmarks present in real environments. Kalman filter-based algorithms, for example, require time quadratic in the number of landmarks to incorporate each sensor observation. This paper presents FastSLAM, an algorithm that recursively estimates the full posterior distribution over robot pose and landmark locations, yet scales logarithmically with the number of landmarks in the map. This algorithm is based on an exact factorization of the posterior into a product of conditional landmark distributions and a distribution over robot paths. The algorithm has been run successfully on as many as 50,000 landmarks, environments far beyond the reach of previous approaches. Experimental results demonstrate the advantages and limitations of the FastSLAM algorithm on both simulated and real-world data.
