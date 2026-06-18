Guided Expansive Spaces Trees: A Search Strategy for Motion- and Cost-Constrained State Spaces

Topics include Motion planning, Expansive space trees, Kinodynamic planning, Cost-constrained planning, Sampling-based planning, Path optimization.

Extends the EST motion planner with a cost-biased node-selection weighting (Guided EST) so tree expansion favours lower-cost, straighter paths through kinodynamically-constrained spaces, and pairs it with Path Gradient Descent for local path refinement.

Motion planning for systems with constraints on controls or the need for relatively straight paths for real-time actions presents challenges for modern planners. This paper presents an approach which addresses these types of systems by building on existing motion planning approaches. Guided Expansive Spaces Trees are introduced to search for a low cost and relatively straight path in a space with motion constraints. Path Gradient Descent, which builds on the idea of Elastic Strips, finds the locally optimal path for an existing path. These techniques are tested on simulations of rendezvous and docking of the space shuttle to the International Space Station and of a 4-foot fan-controlled blimp in a factory setting.
