<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Identification for Long-range Predictive Control

Topics include Predictive control, System identification, Adaptive control, Recursive least squares, Multi-step prediction, Industrial process control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Examines why adaptive predictive controllers that combine single-step parameter estimation with multi-step prediction can become unstable without the bandpass filtering often used in practice. The paper introduces a multi-step-ahead identification cost aligned with the controller objective, showing how this estimator naturally produces the frequency-response behavior that earlier applications achieved through ad hoc prefiltering.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The current generation of adaptive predictive controllers uses a standard single-step-ahead estimator with multi-step-ahead predictors. In order to obtain satisfactory results in applications, data are bandpass filtered before being used in the estimator. This paper demonstrates that the use of a standard RLS estimator with no data filtering frequently results in unstable closed loops if the parameters are used in a multi-step-ahead control scheme. A multi-step-ahead cost is introduced for parameter estimation as a dual of the control law. It is shown that the method is superior to the standard scheme. The frequency response properties of this estimator indicate that prefiltering of the data prevalent among the reported successful applications of the predictive controller is a natural outcome of this choice of the cost for the estimator scheme. The paper provides some useful guidelines for the choice of order and time constants of these filters.
