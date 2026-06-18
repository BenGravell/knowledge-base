<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Distributionally Robust Control of Constrained Stochastic Systems

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We investigate the control of constrained stochastic linear systems when faced with limited information regarding the disturbance process, i.e., when only the first two moments of the disturbance distribution are known. We consider two types of distributionally robust constraints. In the first case, we require that the constraints hold with a given probability for all disturbance distributions sharing the known moments. These constraints are commonly referred to as distributionally robust chance constraints. In the second case, we impose conditional value-at-risk (CVaR) constraints to bound the expected constraint violation for all disturbance distributions consistent with the given moment information. Such constraints are referred to as distributionally robust CVaR constraints with second-order moment specifications. We propose a method for designing linear controllers for systems with such constraints that is both computationally tractable and practically meaningful for both finite and infinite horizon problems. We prove in the infinite horizon case that our design procedure produces the globally optimal linear output feedback controller for distributionally robust CVaR and chance constrained problems. The proposed methods are illustrated for a wind blade control design case study for which distributionally robust constraints constitute sensible design objectives.
