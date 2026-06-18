Reducing the Transformer Architecture to a Minimum

Topics include Neural networks, Transformers, Attention mechanisms, Computer vision, Classification, Benchmarks, Online algorithms, Natural language processing, NLP, CV, Multi-layer perceptron, MLP.

Transformers are a widespread and successful model architecture, particularly in Natural Language Processing (NLP) and Computer Vision (CV). The essential innovation of this architecture is the Attention Mechanism, which solves the problem of extracting relevant context information from long sequences in NLP and realistic scenes in CV. A classical neural network component, a Multi-Layer Perceptron (MLP), complements the attention mechanism. Its necessity is frequently justified by its capability of modeling nonlinear relationships. However, the attention mechanism itself is nonlinear through its internal use of similarity measures. A possible hypothesis is that this nonlinearity is sufficient for modeling typical application problems. As the MLPs usually contain the most trainable parameters of the whole model, their omission would substantially reduce the parameter set size. Further components can also be reorganized to reduce the number of parameters. Under some conditions, query and key matrices can be collapsed into a single matrix of the same size....

## INTRODUCTION

Recently, *Large Language Models* (LLMs) have shown impressive performance in producing complex text answers to given questions. Their outstanding feature is the massive size of parameter sets (up to billions). The rapidly growing parameter number has limited the possibility of developing such models (as well as objectively investigating their properties) to companies and institutions capable of making considerable investments in computing the model's parameters.

This is why it is of great interest to attempt to find more efficient configurations with fewer parameters without performance loss. A computing model with an excellent success record is based on the transformer architecture \[Vaswani et al., 2017\]. Their success is due to an excellent ability to capture contextual information. Initially developed for language processing, transformers have also been successfully used in Computer Vision (CV). The analogy to language processing is the following: the semantics of individual words are determined by other words in the word sequence....

Limitations to image processing suggest further extension. The proper domain of transformers is NLP. An obstacle to its investigation is the size of benchmark problems, so most published investigations consist of observing the performance of fine-tuning pre-trained models. To use pre-trained parameter sets, these fine-tuned models must be identical or almost identical to the pre-trained models. This makes the testing of different architectures difficult. A possibility is to use a large model used for pre-training as a *teacher* and a medium-sized model as *student*, mimicking its performance....

These will be important focuses soon.

Table 1: Results of 16 experiments on the two datasets MNIST and CIFAR-10 with 6 or 12 consecutive transformer encoders and 1 or 4 attention heads per encoder layer either with the default MLP inside each encoder layer or skipping it entirely. The loss and accuracy for the training and validation sets are reported after each model is trained for exactly 500 epochs.

Moreover, it is impossible to equivalently concatenate the value/projection matrices $W_{sh}^{VO}$ to a unique product because of varying index $h$ along various paths through the heads.

The following observations can be made:
