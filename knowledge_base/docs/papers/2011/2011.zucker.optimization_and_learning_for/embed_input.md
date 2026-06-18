<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Optimization and Learning for Rough Terrain Legged Locomotion

Topics include Legged locomotion, Rough terrain, Footstep planning, Inverse optimal control, Trajectory optimization, Anytime planning, LittleDog, Robot learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Proposes a hierarchical optimization framework for quadruped locomotion over rough terrain, combining anytime footstep planning with dynamic body motion optimization. It uses inverse optimal control to reduce hand-tuning of costs and real-time replanning with reflexes and feedback to robustly guide the LittleDog robot across varied terrain.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents a novel approach to legged locomotion over rough terrain rooted in optimization. The approach relies on a hierarchy of fast, anytime algorithms to plan a set of footholds and the dynamic body motions required to execute them. Components within the planning framework coordinate to exchange plans, cost-to-go estimates, and certificates that ensure the output of an abstract high-level planner can be realized by lower layers of the hierarchy. The burden of careful engineering of cost functions is mitigated by a simple inverse optimal control technique, and robustness is achieved by real-time re-planning of the full trajectory, augmented by reflexes and feedback control. We demonstrate the approach guiding the LittleDog quadruped robot over various rough terrains.
