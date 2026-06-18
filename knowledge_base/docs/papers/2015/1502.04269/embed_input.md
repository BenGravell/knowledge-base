<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Supersparse Linear Integer Models for Optimized Medical Scoring Systems

Topics include Classification, Accuracy, Scalability, SLIM, Coprime integers.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Scoring systems are linear classification models that only require users to add, subtract and multiply a few small numbers in order to make a prediction. These models are in widespread use by the medical community, but are difficult to learn from data because they need to be accurate and sparse, have coprime integer coefficients, and satisfy multiple operational constraints. We present a new method for creating data-driven scoring systems called a Supersparse Linear Integer Model (SLIM). SLIM scoring systems are built by solving an integer program that directly encodes measures of accuracy (the 0-1 loss) and sparsity (the l_0-seminorm) while restricting coefficients to coprime integers. SLIM can seamlessly incorporate a wide range of operational constraints related to accuracy and sparsity, and can produce highly tailored models without parameter tuning. We provide bounds on the testing and training accuracy of SLIM scoring systems, and present a new data reduction technique that can improve scalability by eliminating a portion of the training data beforehand. Our paper includes results from a collaboration with the Massachusetts General Hospital Sleep Laboratory, where SLIM was used to create a highly tailored scoring system for sleep apnea screening
