Signature Verification Using a "Siamese" Time Delay Neural Network

Topics include Siamese networks, Signature verification, Time-delay neural networks, Metric learning, Neural networks, Pattern recognition.

Introduces the Siamese neural-network architecture for signature verification, using two weight-sharing time-delay subnetworks to embed signatures and a joining unit to measure distance. The paper became a foundational example of learned similarity metrics and pairwise neural architectures for verification tasks.

This paper describes an algorithm for verification of signatures written on a pen-input tablet. The algorithm is based on a novel, artificial neural network, called a "Siamese" neural network. This network consists of two identical sub-networks joined at their outputs. During training the two sub-networks extract features from two signatures, while the joining neuron measures the distance between the two feature vectors. Verification consists of comparing an extracted feature vector with a stored feature vector for the signer. Signatures closer to this stored representation than a chosen threshold are accepted, all other signatures are rejected as forgeries.
