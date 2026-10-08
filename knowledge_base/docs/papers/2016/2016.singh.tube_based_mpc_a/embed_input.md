<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Tube-Based MPC: A Contraction Theory Approach

Topics include Tube model predictive control, Contraction theory, Nonlinear control, Robust control, Convex optimization, Invariant tubes.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Uses contraction theory and convex optimization to synthesize ancillary feedback for nonlinear continuous-time tube MPC. Quantifies disturbance tubes, guarantees exponential tracking convergence, and exploits nonlinear system geometry to reduce conservatism.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The objective of this paper is to devise a systematic approach to apply the tube MPC framework to non-linear continuous-time systems. In tube MPC, an ancillary feedback controller is designed to keep the actual state within an invariant “tube” around a nominal trajectory computed neglecting disturbances. Our approach is to leverage recent results in contraction theory together with tools from convex optimization to devise ancillary feedback controllers that (a) enjoy quantifiable bounds for the state tube, (b) provide exponential convergence, and (c) fully exploit the nonlinearity of a system, thereby minimizing conservatism. We present a number of methods to design contraction-based ancillary feedback controllers, along with numerical results corroborating our analytical insights.
