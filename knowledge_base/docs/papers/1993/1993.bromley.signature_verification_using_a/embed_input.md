<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Signature Verification Using a "Siamese" Time Delay Neural Network

Topics include Siamese networks, Signature verification, Time-delay neural networks, Metric learning, Neural networks, Pattern recognition.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces the Siamese neural-network architecture for signature verification, using two weight-sharing time-delay subnetworks to embed signatures and a joining unit to measure distance. The paper became a foundational example of learned similarity metrics and pairwise neural architectures for verification tasks.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper describes an algorithm for verification of signatures written on a pen-input tablet. The algorithm is based on a novel, artificial neural network, called a "Siamese" neural network. This network consists of two identical sub-networks joined at their outputs. During training the two sub-networks extract features from two signatures, while the joining neuron measures the distance between the two feature vectors. Verification consists of comparing an extracted feature vector with a stored feature vector for the signer. Signatures closer to this stored representation than a chosen threshold are accepted, all other signatures are rejected as forgeries.
