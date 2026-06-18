<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Robust Model Predictive Control Using Tubes

Topics include Tube model predictive control, Robust model predictive control, Uncertain systems, Piecewise affine control, Stability, Constrained control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces a tube-based robust MPC formulation that computes a nominal tube and associated piecewise-affine feedback law to keep uncertain trajectories inside it. The approach reduces worst-case complexity growth with horizon length while preserving robust constraint satisfaction and asymptotic stability.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A form of feedback model predictive control (MPC) that overcomes disadvantages of conventional MPC but which has manageable computational complexity is presented. The optimal control problem, solved on-line, yields a ‘tube’ and an associated piecewise affine control law that maintains the controlled trajectories in the tube despite uncertainty; computational complexity is linear (rather than exponential) in horizon length. Asymptotic stability of the controlled system is established.
