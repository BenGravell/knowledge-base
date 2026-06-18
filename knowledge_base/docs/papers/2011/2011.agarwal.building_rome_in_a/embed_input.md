<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Building Rome in a Day

Topics include Structure from motion, City-scale reconstruction, Internet photo collections, Distributed computing, Image matching, Bundle adjustment, Multi-view stereo.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Describes a distributed image-matching and reconstruction pipeline for city-scale unordered photo collections. It showed that Internet photo sets with more than one hundred thousand images could be reconstructed in under a day when matching, SfM, and bundle adjustment were structured for parallel execution.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a system that can reconstruct 3D geometry from large, unorganized collections of photographs such as those found by searching for a given city (e.g., Rome) on Internet photo-sharing sites. Our system is built on a set of new, distributed computer vision algorithms for image matching and 3D reconstruction, designed to maximize parallelism at each stage of the pipeline and to scale gracefully with both the size of the problem and the amount of available computation. Our experimental results demonstrate that it is now possible to reconstruct city-scale image collections with more than a hundred thousand images in less than a day.
