<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning Multiple Layers of Features from Tiny Images

Topics include Unsupervised learning, Representation learning, Restricted boltzmann machines, Deep belief networks, Image classification, CIFAR-10, CIFAR-100, Distributed training, ZCA whitening.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Studies unsupervised feature learning with restricted Boltzmann machines and deep belief networks on tiny natural images, including whitening and a distributed RBM training algorithm. Introduces the labeled CIFAR-10 and CIFAR-100 datasets and demonstrates improved object classification through unsupervised pretraining.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Groups at MIT and NYU have collected a dataset of millions of tiny colour images from the web. It is, in principle, an excellent dataset for unsupervised training of deep generative models, but previous researchers who have tried this have found it difficult to learn a good set of filters from the images. We show how to train a multi-layer generative model that learns to extract meaningful features which resemble those found in the human visual cortex. Using a novel parallelization algorithm to distribute the work among multiple machines connected on a network, we show how training such a model can be done in reasonable time. A second problematic aspect of the tiny images dataset is that there are no reliable class labels which makes it hard to use for object recognition experiments. We created two sets of reliable labels. The CIFAR-10 set has 6000 examples of each of 10 classes and the CIFAR-100 set has 600 examples of each of 100 non-overlapping classes. Using these labels, we show that object recognition is significantly improved by pre-training a layer of features on a large set of unlabeled tiny images.
