<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Real-Time Iteration Scheme with Quasi-Newton Jacobian Updates for Nonlinear Model Predictive Control

Topics include Nonlinear model predictive control, Real-time iteration, Quasi-Newton methods, Jacobian updates, Implicit integration, Structure-exploiting optimization, Sequential quadratic programming, Embedded optimization, Low-rank updates.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

This paper modifies RTI NMPC by replacing repeated exact Jacobian work with block-structured quasi-Newton updates tailored to the optimal-control sparsity pattern. The result targets stiff or implicitly defined dynamics, showing how low-rank updates and an implementation for implicit integrators can reduce online computation without abandoning the RTI structure.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Nonlinear model predictive control (NMPC) requires the solution of a dynamic optimization problem at each sampling instant under strict timing constraints, involving nonlinear dynamics that can often be stiff or implicitly defined. The real-time iteration (RTI) scheme has been shown to allow real-world embedded applications of NMPC. The present paper proposes an extension of the standard RTI algorithm with a block-structured quasi-Newton method to obtain low-rank Jacobian updates that preserve the block structure of the optimal control problem. In addition, a particular structure-exploiting implementation is presented for implicit integration schemes such that no Jacobian evaluation is needed neither any matrix factorization. Based on a proof of concept implementation in C code, the computational performance of the algorithm is illustrated for multiple NMPC case studies.
