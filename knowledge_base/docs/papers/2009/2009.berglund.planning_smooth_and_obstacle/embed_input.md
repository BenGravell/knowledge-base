<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Planning Smooth and Obstacle-Avoiding B-Spline Paths for Autonomous Mining Vehicles

Topics include Path planning, B-splines, Curvature variation, Obstacle avoidance, Mining vehicles.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Plans obstacle-avoiding quartic B-spline paths by minimizing curvature variation and enforcing safety margins. Mining-vehicle case studies relate geometric smoothness to faster travel and reduced vehicle wear.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper we study the problem of computing smooth planar paths in the presence of obstacles where we have an a priori knowledge about the environment. We investigate how the smoothness of a path and the total travel time required by the path are related for paths used by a four-wheel four-gear articulated vehicle. A path is considered smooth if the variation of its curvature, i.e., the integral of the square of the derivative of curvature along the path, is minimal. Paths are defined by quartic B-splines and obstacles are represented by polygonal chains. Quartic B-splines have a continuous derivative of curvature. Obstacle-avoidance is achieved by means of the envelope of the B-splines. We present a study of eight cases based on real-world application data from the Swedish mining company Luossavaara-Kiirunavaara AB (LKAB). The results indicate that a minimum curvature variation B-spline path-planning algorithm we have developed yields paths that are substantially better than the ones used by LKAB today. Our simulations shows that the new paths are up to 39% faster to travel along than the paths currently in use. They even decrease the wear on the vehicle.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Preliminary results from the production at LKAB show an overall 5-10% decrease in the total time. The total time includes both travel on the path and ore loading and unloading.
