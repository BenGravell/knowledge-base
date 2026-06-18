<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Data-Driven Simulation and Control

Topics include Data-driven control, Behavioral systems, Data-driven simulation, Output matching, Linear quadratic tracking, System identification, Direct control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces an early direct data-driven route for LTI simulation and LQ tracking control, using measured trajectories as the computational object instead of first estimating a state-space or transfer-function model. The paper is one of the behavioral precursors to later Hankel/fundamental-lemma control methods.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Classical linear time-invariant system simulation methods are based on a transfer function, impulse response, or input/state/output representation. We present a method for computing the response of a system to a given input and initial conditions directly from a trajectory of the system, without explicitly identifying the system from the data. Similar to the classical approach for simulation, the classical approach for control is model-based: first a model representation is derived from given data of the plant and then a control law is synthesised using the model and the control specifications. We present an approach for computing a linear quadratic tracking control signal that circumvents the identification step. The results are derived assuming exact data and the simulated response or control input is constructed off-line.
