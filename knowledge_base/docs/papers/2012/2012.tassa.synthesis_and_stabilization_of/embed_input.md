<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Synthesis and Stabilization of Complex Behaviors through Online Trajectory Optimization

Topics include Trajectory optimization, Iterative linear quadratic regulator, Differential dynamic programming, iLQR, Nonlinear control, Online optimization, Synthesis, Stabilization, Behaviors.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Refines iLQR with key algorithmic improvements now standard in modern implementations: state Hessian regularization, improved feedforward gain line search, and adaptive regularization scheduling. Clearer presentation than the original Li & Todorov paper.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present an online trajectory optimization method and software platform applicable to complex humanoid robots performing challenging tasks such as getting up from an arbitrary pose on the ground and recovering from large disturbances using dexterous acrobatic maneuvers. The resulting behaviors, illustrated in the attached video, are computed only 7x slower than real time, on a standard PC. The video also shows results on the acrobot problem, planar swimming and one-legged hopping. These simpler problems can already be solved in real time, without pre-computing anything.
