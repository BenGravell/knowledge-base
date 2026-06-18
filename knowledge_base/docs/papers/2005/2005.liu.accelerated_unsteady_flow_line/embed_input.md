<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Accelerated Unsteady Flow Line Integral Convolution

Topics include Line integral convolution, AUFLIC, UFLIC, Unsteady flows, Flow visualization, Vector field visualization, Pathline reuse, Animation coherence, Scientific visualization, Computational fluid dynamics.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Accelerates UFLIC by reusing pathlines during value scattering and adding a dynamic seeding controller that decides when to advect, copy, or reuse flow paths. The paper is important as a performance-oriented follow-up that moves coherent unsteady-flow LIC closer to interactive use.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Unsteady flow line integral convolution (UFLIC) is a texture synthesis technique for visualizing unsteady flows with high temporal-spatial coherence. Unfortunately, UFLIC requires considerable time to generate each frame due to the huge amount of pathline integration that is computed for particle value scattering. This paper presents Accelerated UFLIC (AUFLIC) for near interactive (1 frame/second) visualization with 160,000 particles per frame. AUFLIC reuses pathlines in the value scattering process to reduce computationally expensive pathline integration. A flow-driven seeding strategy is employed to distribute seeds such that only a few of them need pathline integration while most seeds are placed along the pathlines advected at earlier times by other seeds upstream and, therefore, the known pathlines can be reused for fast value scattering. To maintain a dense scattering coverage to convey high temporal-spatial coherence while keeping the expense of pathline integration low, a dynamic seeding controller is designed to decide whether to advect, copy, or reuse a pathline. At a negligible memory cost, AUFLIC is 9 times faster than UFLIC with comparable image quality.
