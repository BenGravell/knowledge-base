<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Control Barrier Function Based Quadratic Programs for Safety Critical Systems

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Safety critical systems involve the tight coupling between potentially conflicting control objectives and safety constraints. As a means of creating a formal framework for controlling systems of this form, and with a view toward automotive applications, this paper develops a methodology that allows safety conditions—expressed as control barrier functions—to be unified with performance objectives—expressed as control Lyapunov functions—in the context of real-time optimization-based controllers. Safety conditions are specified in terms of forward invariance of a set, and are verified via two novel generalizations of barrier functions; in each case, the existence of a barrier function satisfying Lyapunov-like conditions implies forward invariance of the set, and the relationship between these two classes of barrier functions is characterized. In addition, each of these formulations yields a notion of control barrier function (CBF), providing inequality constraints in the control input that, when satisfied, again imply forward invariance of the set.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Through these constructions, CBFs can naturally be unified with control Lyapunov functions (CLFs) in the context of a quadratic program (QP); this allows for the achievement of control objectives (represented by CLFs) subject to conditions on the admissible states of the system (represented by CBFs). The mediation of safety and performance through a QP is demonstrated on adaptive cruise control and lane keeping, two automotive control problems that present both safety and performance considerations coupled with actuator bounds.
