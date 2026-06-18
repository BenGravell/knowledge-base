<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

On the Separation Theorem of Stochastic Control

Topics include Stochastic control, Separation theorem, Certainty equivalence, Kalman filter, Linear quadratic Gaussian control, Optimal control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Proves the separation theorem for linear-Gaussian stochastic control: the optimal policy decomposes into a Kalman filter for state estimation and an LQR feedback law computed as if the state were known. Establishes the theoretical foundation for LQG control and certainty-equivalence principles.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The object of this paper is to show that the combined problem of optimal control and filtering, for a stochastic linear dynamic system observed via a noisy linear channel, can be reduced to two independent problems of control and filtering, respectively. Under suitable conditions, solutions of the latter problems are shown to exist. This structural property of the optimal system holds whether or not the cost functional is quadratic, and whether or not the optimal feedback control happens to be linear in the system state or its expectation. In general, the optimal control depends parametrically on the intensity of channel noise; the result means, however, that channel noise plays qualitatively the same role as dynamic disturbances in determination of the feedback law. A special result of this type, for the standard, linear stochastic regulator problem, is well known, and has been called the “separation theorem”. For discrete-time systems the general result can be proved by relatively straightforward application of dynamic programming. In this paper attention is confined to continuous systems.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The method is again dynamic programming, with appeal to the Itô-Nisio-Fleming theory of functional stochastic differential equations, Kalman's filter and an existence theorem for parabolic equations due to Ladyjenskaya, Solonnikov and Uraltseva. To apply the foregoing results it is necessary to impose rather stringent conditions on system coefficients. Undoubtedly the separation theorem (Theorem 2.1) is true under weaker hypotheses, more in line with requirements met in practice. In this paper our aim is to clarify some of the principles involved and to indicate the type of result to be expected.
