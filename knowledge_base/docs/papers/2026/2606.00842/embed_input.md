A Framework for Motion Planning with Temporal Logic Precedence Specifications via Augmented Graphs of Convex Sets

Topics include Graphs of convex sets, Temporal logic planning, Specifications, Motion planning, Convex optimization, Mixed-integer programming, Planning.

Extends graph-of-convex-sets planning to handle temporal-logic precedence requirements through an augmented graph construction. The paper is notable for keeping logic sequencing close to the convex-optimization planning representation rather than treating it as a separate symbolic layer.

We present a framework for planning trajectories that avoid obstacles and satisfy logical precedence constraints expressed with a fragment of signal temporal logic (STL). Our approach models environments containing obstacles, keys, and doors, where collecting a key unlocks its associated door and potentially opens shorter paths to a goal. Based on an exact convex partitioning of the free space that encodes connectivity among convex free space, key, and door regions, we construct an augmented graph of convex sets (GCS) whose layered structure exactly encodes the key-door precedence logic. A shortest path in the augmented GCS simultaneously selects an optimal key collection sequence and computes an optimal continuous trajectory, providing an exact solution up to a finite Bezier curve parameterization.
