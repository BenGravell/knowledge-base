<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Structure-from-Motion Revisited

Topics include Structure from motion, Incremental structure from motion, COLMAP, Geometric verification, Triangulation, Bundle adjustment, Open source.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Revisits incremental SfM as a complete, robust pipeline, combining geometric verification, careful triangulation, image registration, and bundle-adjustment decisions. The resulting COLMAP system became a reference open-source implementation for reconstructing large unordered photo collections.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Incremental Structure-from-Motion is a prevalent strategy for 3D reconstruction from unordered image collections. While incremental reconstruction systems have tremendously advanced in all regards, robustness, accuracy, completeness, and scalability remain the key problems towards building a truly general-purpose pipeline. We propose a new SfM technique that improves upon the state of the art to make a further step towards this ultimate goal. The full reconstruction pipeline is released to the public as an open-source implementation.
