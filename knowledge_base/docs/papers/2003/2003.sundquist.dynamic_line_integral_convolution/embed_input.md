<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Dynamic Line Integral Convolution for Visualizing Streamline Evolution

Topics include Line integral convolution, DLIC, Dynamic line integral convolution, Time-dependent vector fields, Streamline evolution, Flow visualization, Vector field visualization, Electromagnetism, Animation coherence, Scientific visualization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces Dynamic Line Integral Convolution (DLIC), which animates a changing vector field by evolving the LIC input texture according to a separate field-line motion field. The method is especially useful when the visual task is to see streamline evolution itself, as in electromagnetic field-line animations, rather than only instantaneous flow direction.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The depiction of time-dependent vector fields is a central problem in scientific visualization. This article describes a technique for generating animations of such fields where the motion of the streamlines to be visualized is given by a second "motion" vector field. Each frame of our animation is a Line Integral Convolution of the original vector field with a time-varying input texture. The texture is evolved according to the associated motion vector field via an automatically adjusted set of random particles. We demonstrate this technique with examples from electromagnetism.
