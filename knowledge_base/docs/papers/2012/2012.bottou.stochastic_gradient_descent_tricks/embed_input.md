<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Stochastic Gradient Descent Tricks

Topics include Stochastic gradient descent, Large-scale learning, Learning rates, Online learning, Neural network training, Optimization practice, Generalization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Surveys practical SGD design choices for large-scale machine learning, including objective decomposition, stochastic approximations, step-size schedules, averaging, feature scaling, and implementation pitfalls. Its value is not a new convergence theorem but an experienced practitioner's map of why SGD works well on large datasets and how to tune it so that statistical efficiency, computation, and generalization line up.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Chapter 1 strongly advocates the stochastic back-propagation method to train neural networks. This is in fact an instance of a more general technique called stochastic gradient descent (SGD). This chapter provides background material, explains why SGD is a good learning algorithm when the training set is large, and provides useful recommendations.
