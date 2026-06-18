<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Spatial Planning: A Configuration Space Approach

Topics include Configuration space, Motion planning, Collision avoidance, Robotics, Polygonal obstacles, Polyhedral obstacles, Spatial planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Lozano-Perez introduces configuration-space planning, representing a robot object's pose as a point and transforming collision constraints into forbidden regions called configuration-space obstacles. The paper is foundational for robot motion planning because it turns geometric collision avoidance into search and arrangement reasoning in the robot's degrees of freedom.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents algorithms for computing constraints on the position of an object due to the presence of other objects. This problem arises in applications that require choosing how to arrange or how to move objects without collisions. The approach presented here is based on characterizing the position and orientation of an object as a single point in a configuration space, in which each coordinate represents a degree of freedom in the position or orientation of the object. The configurations forbidden to this object, due to the presence of other objects, can then be characterized as regions in the configuration space, called configuration space obstacles. The paper presents algorithms for computing these configuration space obstacles when the objects are polygons or polyhedra.
