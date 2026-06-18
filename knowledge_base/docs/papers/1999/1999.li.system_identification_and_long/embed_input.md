<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

System Identification and Long-range Predictive Control of Multi-rate Systems

Topics include System identification, Model predictive control, Multirate systems, Subspace identification, Lifted systems, Process control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Combines lifted-system identification with long-range predictive control for multirate processes where inputs are sampled faster than outputs. The method identifies a lifted state-space model, extracts a fast-rate model, and uses minimum-variance intersample output estimates to improve predictive-control performance.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Discusses system identification and model-based predictive control of multi-rate systems. In particular, the practically useful case of systems with fast manipulative variable sampling and slow output sampling is considered. The lifting method is used to analyze the multi-rate system in a state-space framework. A subspace identification algorithm, is first used to identify the lifted multi-rate system. The single-rate model at the faster sampling rate is then extracted from this estimated system and subsequently used for long-range predictive control. The fast-sampling rate model is used to estimate the outputs at inter-sample instants, using a minimum variance predictor. The estimated output is then used for model-based predictive control at the faster sampling rate. The performance of this controller is compared with the performance of the slow sample-rate scheme, and it is shown that the fast-rate controller has a significantly better performance.
