<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Building Rome on a Cloudless Day

Topics include Structure from motion, Dense reconstruction, Internet photo collections, City-scale reconstruction, Image clustering, Multi-view stereo, Graphics processing unit acceleration.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Presents a scalable dense reconstruction pipeline for massive unregistered Internet photo collections, emphasizing clustering, stereo, stereo fusion, structure from motion, and commodity parallel hardware. It complements distributed city-scale SfM work by showing that very large photo collections could be processed on a single high-performance PC.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper introduces an approach for dense 3D reconstruction from unregistered Internet-scale photo collections with about 3 million images within the span of a day on a single PC ("cloudless"). Our method advances image clustering, stereo, stereo fusion and structure from motion to achieve high computational performance. We leverage geometric and appearance constraints to obtain a highly parallel implementation on modern graphics processors and multi-core architectures. This leads to two orders of magnitude higher performance on an order of magnitude larger dataset than competing state-of-the-art approaches.
