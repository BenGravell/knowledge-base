<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Robust Nonlinear System Identification Using Neural-network Models

Topics include System identification, Neural networks, Robust identification, RBF networks, H-infinity filtering, Nonlinear systems, Persistency of excitation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Develops robust nonlinear system-identification schemes using feedforward and radial-basis neural-network models under unknown driving noise. The paper adapts H-infinity and cost-to-come identification ideas to neural approximators, with emphasis on avoiding restrictive excitation assumptions.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the problem of identification for nonlinear systems in the presence of unknown driving noise, using both feedforward multilayer neural network and radial basis function network models. Our objective is to resolve the difficulty associated with the persistency of excitation condition inherent to the standard schemes in the neural identification literature. This difficulty is circumvented here by a novel formulation and by using a new class of identification algorithms recently obtained by Didinsky et al. We show how these algorithms can be exploited to successfully identify the nonlinearity in the system using neural-network models. By embedding the original problem in one with noise-perturbed state measurements, we present a class of identifiers (under L1 and L2 cost criteria) which secure a good approximant for the system nonlinearity provided that some global optimization technique is used. In this respect, many available learning algorithms in the current neural-network literature, e.g., the backpropagation scheme and the genetic algorithms-based scheme, with slight modifications, can ensure the identification of the system nonlinearity. Subsequently, we address the same problem under a third, worst case L(infinity) criterion for an RBF modeling.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a neural-network version of an H(infinity)-based identification algorithm from Didinsky et al and show how, along with an appropriate choice of control input to enhance excitation, under both full-state-derivative information (FSDI) and noise-perturbed full-state-information (NPFSI), it leads to satisfaction of a relevant persistency of excitation condition, and thereby to robust identification of the nonlinearity. Results from several simulation studies have been included to demonstrate the effectiveness of these algorithms.
