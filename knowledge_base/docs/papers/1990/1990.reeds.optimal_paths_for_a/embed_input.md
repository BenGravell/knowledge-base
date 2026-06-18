<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Optimal Paths for a Car That Goes Both Forwards and Backwards

Topics include Path generation, Reeds-Shepp, Curvature.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The path taken by a car with a given minimum turning radius has a lower bound on its radius of curvature at each point, but the path has cusps if the car shifts into or out of reverse gear. What is the shortest such path a car can travel between two points if its starting and ending directions are specified? One need consider only paths with at most 2 cusps or reversals. We give a set of paths which is sufficient in the sense that it always contains a shortest path and small in the sense that there are at most 68, but usually many fewer paths in the set for any pair of endpoints and directions. We give these paths by explicit formula. Calculating the length of each of these paths and selecting the (not necessarily unique) path with smallest length yields a simple algorithm for a shortest path in each case. These optimal paths or geodesics may be described as follows: If C is an arc of a circle of the minimal turning radius and S is a line segment, then it is sufficient to consider only certain paths of the form CCSCC where arcs and segments fit smoothly, one or more of the arcs or segments may vanish, and where reversals, or equivalently cusps, between arcs or segments are allowed.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This contrasts with the case when cusps are not allowed, where Dubins has shown that paths of the form CCC and CSC suffice.
