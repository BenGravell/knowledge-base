<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Parameter Identification for Uncertain Plants Using H∞ Methods

Topics include System identification, H-infinity filtering, Robust control, Uncertain systems, Cost-to-come methods, Parameter estimation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Formulates parameter identification for uncertain nonlinear plants as an H-infinity filtering problem, using cost-to-come ideas and measurement-based observer design. The paper compares a standard prefiltering approach with a new singular-perturbation-based identification scheme, giving robust-control tools for deterministic parameter estimation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We demonstrate the effective use of H∞ filtering and cost-to-come methods for parameter identification in (deterministic) uncertain plants that are linear in the unknown parameters, but nonlinear otherwise. The cost-to-come method is an approach that has been used earlier to solve linear and nonlinear H∞ optimal control and filtering problems. It consists of constructing a cost-to-come function, which assists in the design of an 'optimal' observer scheme. The method is used here in the design of a parameter identification scheme for uncertain plants, where measurements on the state of the system are available, but not on its derivative. Two approaches are adopted, in both of which the parameter estimation problem is formulated as an H∞ filtering problem. One of the approaches uses a more standard prefiltering of the past states, input and disturbance signals. The other approach is a novel design method, which leads to a new class of identification schemes.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

It involves two subproblems: FSDI (full-state-derivative information) problem, where it is assumed that both the state and its derivative are available to the parameter estimator, and NPFSI (noise-perturbed FSI) problem, where the estimator is assumed to measure a noise-perturbed measurement of the state. In the latter problem we use singular perturbation methods to prove asymptotic convergence of the performance of the identifier to that of the unperturbed case, thus providing an asymptotically optimal solution to the FSI (full-state measurement) problem. To illustrate both approaches, several simulation studies on a numerical example are provided.
