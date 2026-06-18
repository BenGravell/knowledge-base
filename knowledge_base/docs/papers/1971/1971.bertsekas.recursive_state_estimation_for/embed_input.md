<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Recursive State Estimation for a Set-membership Description of Uncertainty

Topics include Set-membership estimation, Recursive estimation, Bounded uncertainty, Ellipsoidal estimation, State estimation, Filtering, Smoothing.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Bertsekas and Rhodes derive recursive estimators for linear systems when disturbances and observation errors are known only to lie in bounded sets. The paper is a foundation for set-membership filtering, showing how feasible state sets or bounding ellipsoids can be propagated in a way analogous to stochastic minimum-variance estimators.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper is concerned with the problem of estimating the state of a linear dynamic system using noise-corrupted observations, when input disturbances and observation errors are unknown except for the fact that they belong to given bounded sets. The cases of both energy constraints and individual instantaneous constraints for the uncertain quantities are considereal. In the former case, the set of possible system states compatible with the observations received is shown to be an ellipsoid, and equations for its center and weighting matrix are given, while in the latter case, equations describing a bounding ellipsoid to the set of possible states are derived. All three problems of filtering, prediction, and smoothing are examined by relating them to standard tracking problems of optimal control theory. The resulting estimators are similar in structure and comparable in simplicity to the corresponding stochastic linear minimum-variance estimators, and it is shown that they provide distinct advantages over existing schemes for recursive estimation with a set-membership description of uncertainty.
