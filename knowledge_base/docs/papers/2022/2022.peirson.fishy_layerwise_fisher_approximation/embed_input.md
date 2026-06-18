<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Fishy: Layerwise Fisher Approximation for Higher-Order Neural Network Optimization

Topics include Natural gradient descent, Fisher information matrix, Second-order optimization, Neural networks, Fisher information, Regularization, Deep learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces a layer-local approximation to Fisher information for natural-gradient-style neural network training. Fishy avoids an extra full backward pass by sampling locally at layers, making the preconditioner more compatible with model parallelism and existing optimizers such as Shampoo.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce Fishy, a local approximation of the Fisher information matrix at each layer for natural gradient descent training of deep neural networks. The true Fisher approximation for deep networks involves sampling labels from the model's predictive distribution at the output layer and performing a full backward pass - Fishy defines a Bregman exponential family distribution at each layer, performing the sampling locally. Local sampling allows for model parallelism when forming the preconditioner, removing the need for the extra backward pass. We demonstrate our approach through the Shampoo optimizer, replacing its preconditioner gradients with our locally sampled gradients. Our training results on deep autoencoder and image classification models indicate the efficacy of our construction.
