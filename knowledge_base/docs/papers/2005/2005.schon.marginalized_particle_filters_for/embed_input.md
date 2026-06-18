<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Marginalized Particle Filters for Mixed Linear/nonlinear State-space Models

Topics include Particle filters, Marginalized particle filters, Rao-blackwellization, State-space models, Kalman filter, Integrated navigation, Nonlinear filtering.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Derives marginalized particle filters for mixed linear/nonlinear state-space models, where linear conditional substructures are handled by Kalman filters attached to particles. The paper gives general model details, discusses important signal-processing cases, and demonstrates high-dimensional aircraft navigation with particles over only the nonlinear states.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The particle filter offers a general numerical tool to approximate the posterior density function for the state in nonlinear and non-Gaussian filtering problems. While the particle filter is fairly easy to implement and tune, its main drawback is that it is quite computer intensive, with the computational complexity increasing quickly with the state dimension. One remedy to this problem is to marginalize out the states appearing linearly in the dynamics. The result is that one Kalman filter is associated with each particle. The main contribution in this paper is the derivation of the details for the marginalized particle filter for a general nonlinear state-space model. Several important special cases occurring in typical signal processing applications will also be discussed. The marginalized particle filter is applied to an integrated navigation system for aircraft. It is demonstrated that the complete high-dimensional system can be based on a particle filter using marginalization for all but three states. Excellent performance on real flight data is reported.
