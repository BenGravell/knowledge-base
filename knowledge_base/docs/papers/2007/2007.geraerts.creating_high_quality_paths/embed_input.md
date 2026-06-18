<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Creating High-quality Paths for Motion Planning

Topics include Motion planning, Path optimization, Path shortcutting, Post-processing.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Presents path-quality improvement techniques applied as post-processing steps to paths produced by sampling-based planners. One of the clearest early treatments of path shortcutting.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Many algorithms have been proposed that create a path for a robot in an environment with obstacles. Most methods are aimed at finding a solution. However, for many applications, the path must be of a good quality as well. That is, a path should be short and should keep some amount of minimum clearance to the obstacles. Traveling along such a path reduces the chances of collisions due to the difficulty of measuring and controlling the precise position of the robot. This paper reports a new technique, called Partial shortcut, which decreases the path length. While current methods have difficulties in removing all redundant motions, the technique efficiently removes these motions by interpolating one degree of freedom at a time. Two algorithms are also studied that increase the clearance along paths. The first one is fast but can only deal with rigid, translating bodies. The second algorithm is slower but can handle a broader range of robots, including three-dimensional free-flying and articulated robots, which may reside in arbitrary high-dimensional configuration spaces. A big advantage of these algorithms is that clearance along paths can now be increased efficiently without using complex data structures and algorithms. Finally, we combine the two criteria and show that high-quality paths can be obtained for a broad range of robots.
