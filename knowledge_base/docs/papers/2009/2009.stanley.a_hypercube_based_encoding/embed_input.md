<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Hypercube-Based Encoding for Evolving Large-Scale Neural Networks

Topics include Neuroevolution, Indirect encoding, Neural networks, Evolutionary algorithms, Large-scale networks, HyperNEAT.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces HyperNEAT, an indirect encoding that evolves neural connectivity patterns as functions over geometric coordinates. The approach scales neuroevolution to large structured networks by exploiting regularities such as symmetry and repetition.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Research in neuroevolution—that is, evolving artificial neural networks (ANNs) through evolutionary algorithms—is inspired by the evolution of biological brains, which can contain trillions of connections. Yet while neuroevolution has produced successful results, the scale of natural brains remains far beyond reach. This article presents a method called hypercube-based NeuroEvolution of Augmenting Topologies (HyperNEAT) that aims to narrow this gap. HyperNEAT employs an indirect encoding called connective compositional pattern-producing networks (CPPNs) that can produce connectivity patterns with symmetries and repeating motifs by interpreting spatial patterns generated within a hypercube as connectivity patterns in a lower-dimensional space. This approach can exploit the geometry of the task by mapping its regularities onto the topology of the network, thereby shifting problem difficulty away from dimensionality to the underlying problem structure. Furthermore, connective CPPNs can represent the same connectivity pattern at any resolution, allowing ANNs to scale to new numbers of inputs and outputs without further evolution. HyperNEAT is demonstrated through visual discrimination and food-gathering tasks, including successful visual discrimination networks containing over eight million connections.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The main conclusion is that the ability to explore the space of regular connectivity patterns opens up a new class of complex high-dimensional tasks to neuroevolution.
