<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Embedded Deformation for Shape Manipulation

Topics include Shape deformation, Computer graphics, Geometry processing, Mesh editing, Character animation, Nonrigid registration.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces embedded deformation, representing shape edits through a sparse graph of local affine transformations embedded in the object. The method enables intuitive, smooth, and detail-preserving manipulation of meshes and other geometric shapes.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present an algorithm that generates natural and intuitive deformations via direct manipulation for a wide range of shape representations and editing scenarios. Our method builds a space deformation represented by a collection of affine transformations organized in a graph structure. One transformation is associated with each graph node and applies a deformation to the nearby space. Positional constraints are specified on the points of an embedded object. As the user manipulates the constraints, a nonlinear minimization problem is solved to find optimal values for the affine transformations. Feature preservation is encoded directly in the objective function by measuring the deviation of each transformation from a true rotation. This algorithm addresses the problem of "embedded deformation" since it deforms space through direct manipulation of objects embedded within it, while preserving the embedded objects' features. We demonstrate our method by editing meshes, polygon soups, mesh animations, and animated particle systems.
