<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

MuJoCo: A Physics Engine for Model-based Control

Topics include MuJoCo, Physics engines, Model-based control, Contact dynamics, Inverse dynamics, Optimal control, Robot simulation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces MuJoCo as a physics engine designed around model-based control needs rather than only graphics or offline simulation. The paper's distinctive contributions are efficient generalized-coordinate dynamics, velocity-stepping contact handling, well-defined inverse dynamics with contacts and constraints, XML model compilation, and parallelizable dynamics evaluations for sampling and finite-difference control algorithms.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We describe a new physics engine tailored to model-based control. Multi-joint dynamics are represented in generalized coordinates and computed via recursive algorithms. Contact responses are computed via efficient new algorithms we have developed, based on the modern velocity-stepping approach which avoids the difficulties with spring-dampers. Models are specified using either a high-level C++ API or an intuitive XML file format. A built-in compiler transforms the user model into an optimized data structure used for runtime computation. The engine can compute both forward and inverse dynamics. The latter are well-defined even in the presence of contacts and equality constraints. The model can include tendon wrapping as well as actuator activation states (e.g. pneumatic cylinders or muscles). To facilitate optimal control applications and in particular sampling and finite differencing, the dynamics can be evaluated for different states and controls in parallel. Around 400,000 dynamics evaluations per second are possible on a 12-core machine, for a 3D homanoid with 18 dofs and 6 active contacts. We have already used the engine in a number of control applications. It will soon be made publicly available.
