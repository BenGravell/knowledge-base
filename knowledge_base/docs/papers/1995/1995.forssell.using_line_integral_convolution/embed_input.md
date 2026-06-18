<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Using Line Integral Convolution for Flow Visualization: Curvilinear Grids, Variable-Speed Animation, and Unsteady Flows

Topics include Line integral convolution, Flow visualization, Curvilinear grids, Parametric surfaces, Variable-speed animation, Unsteady flows, Computational fluid dynamics, Texture mapping, Scientific visualization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Generalizes LIC beyond regular Cartesian grids to curvilinear surfaces used in CFD, while also adding variable-speed animation and a route toward unsteady-flow visualization. This paper is the main bridge from the original planar LIC algorithm to practical flow visualization over simulation surfaces and interactive texture-mapped displays.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Line Integral Convolution (LIC), introduced by Cabral and Leedom in SIGGRAPH '93, is a powerful technique for imaging and animating vector fields. We extend the LIC technique in 3 ways: The existing algorithm is limited to vector fields over a regular Cartesian grid. We extend the algorithm and the animation techniques possible with it to vector fields over curvilinear surfaces, such as those found in computational fluid dynamics simulations. We introduce a technique to visualize vector magnitude as well as vector direction, e.e., variable-speed flow animation. We show how to modify LIC to visualize unsteady (time dependent) flows. Our implementation utilizes texture-mapping hardware to run in real time, which allows our algorithms to be included in interactive applications.
