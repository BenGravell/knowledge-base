<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Recursively Generated B-Spline Surfaces on Arbitrary Topological Meshes

Topics include Catmull-Clark subdivision, Subdivision surfaces, B-splines, Computer graphics, Geometric modeling, Meshes.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces Catmull-Clark subdivision, generalizing bicubic B-spline subdivision to arbitrary-topology meshes. This became a core surface representation in computer graphics and animation because it gives smooth limit surfaces from polygonal control meshes.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper describes a method for recursively generating surfaces that approximate points lying on a mesh of arbitrary topology. The method is presented as a generalization of a recursive bicubic B-spline patch subdivision algorithm. For rectangular control-point meshes, the method generates a standard B-spline surface. For non-rectangular meshes, it generates surfaces that are shown to reduce to a standard B-spline surface except at a small number of points, called extraordinary points. Therefore, everywhere except at these points the surface is continuous in tangent and curvature. At the extraordinary points, the pictures of the surface indicate that the surface is at least continuous in tangent, but no proof of continuity is given. A similar algorithm for biquadratic B-splines is also presented.
