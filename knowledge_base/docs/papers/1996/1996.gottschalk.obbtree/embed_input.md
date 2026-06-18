OBBTree

Topics include Collision detection, Oriented bounding boxes, Bounding volume hierarchies, Separating axis theorem, Computer graphics, Rigid motion, Polygonal models.

Introduces OBBTree, a hierarchical collision-detection structure built from tight oriented bounding boxes and fast separating-axis overlap tests. The method made exact interference detection practical for large rigid polygonal models at interactive rates and became a core reference for bounding-volume hierarchies.

We present a data structure and an algorithm for efficient and exact interference detection amongst complex models undergoing rigid motion. The algorithm is applicable to all general polygonal models. It pre-computes a hierarchical representation of models using tight-fitting oriented bounding b ox trees (OBBTrees). At runtime, the algorithm traverses two such trees and tests for overlaps between oriented bounding boxes based on a separating axis theorem, which takes less than 200 operations in practice. It has been implemented and we compare its performance with other hierarchical data structures. In particular, it can robustly and accurately detect all the contacts between large complex geometries composed of hundreds of thousands of polygons at interactive rates.
