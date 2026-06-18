<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Towards Linear-Time Incremental Structure from Motion

Topics include Structure from motion, Incremental structure from motion, VisualSFM, Bundle adjustment, Preconditioned conjugate gradient, Feature matching, Retriangulation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Reworks incremental SfM to scale much closer to linearly by combining preemptive matching, a geometric bundle-adjustment schedule, preconditioned conjugate-gradient solving, and periodic retriangulation. The paper is one of the practical foundations behind large-scale incremental SfM systems such as VisualSFM.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The time complexity of incremental structure from motion (SfM) is often known as O(n4) with respect to the number of cameras. As bundle adjustment (BA) being significantly improved recently by preconditioned conjugate gradient (PCG), it is worth revisiting how fast incremental SfM is. We introduce a novel BA strategy that provides good balance between speed and accuracy. Through algorithm analysis and extensive experiments, we show that incremental SfM requires only O(n) time on many major steps including BA. Our method maintains high accuracy by regularly re-triangulating the feature matches that initially fail to triangulate. We test our algorithm on large photo collections and long video sequences with various settings, and show that our method offers state of the art performance for large-scale reconstructions. The presented algorithm is available as part of VisualSFM at
