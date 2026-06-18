<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Computer Algorithm for Reconstructing a Scene from Two Projections

Topics include Structure from motion, Epipolar geometry, Two-view geometry, Relative pose, Scene reconstruction, Binocular vision, Motion perception.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces the algebraic two-view reconstruction method that became known as the eight-point algorithm, showing how point correspondences across two projections can recover relative camera geometry and scene structure. The paper is a foundation of epipolar geometry and later structure-from-motion pipelines.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A simple algorithm for computing the three-dimensional structure of a scene from a correlated pair of perspective projections is described here, when the spatial relationship between the two projections is unknown. This problem is relevant not only to photographic surveying but also to binocular vision, where the non-visual information available to the observer about the orientation and focal length of each eye is much less accurate than the optical information supplied by the retinal images themselves. The problem also arises in monocular perception of motion, where the two projections represent views which are separated in time as well as space. As Marr and Poggio have noted, the fusing of two images to produce a three-dimensional percept involves two distinct processes: the establishment of a 1:1 correspondence between image points in the two views - the 'correspondence problem' - and the use of the associated disparities for determining the distances of visible elements in the scene. I shall assume that the correspondence problem has been solved; the problem of reconstructing the scene then reduces to that of finding the relative orientation of the two viewpoints.
