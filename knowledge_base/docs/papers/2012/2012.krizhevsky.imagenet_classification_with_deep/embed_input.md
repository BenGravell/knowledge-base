<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

ImageNet Classification with Deep Convolutional Neural Networks

Topics include AlexNet, Convolutional neural network, ImageNet, Deep learning, Graphics processing unit training, Dropout, ReLU activations, Computer vision.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces the deep convolutional network later known as AlexNet and demonstrates a large jump in ImageNet classification accuracy using GPUs, ReLUs, dropout, data augmentation, and a large labeled dataset. The paper's historical importance is that it made deep supervised representation learning the dominant computer-vision recipe, while its architectural details became the baseline vocabulary for later CNNs.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We trained a large, deep convolutional neural network to classify the 1.3 million high-resolution images in the LSVRC-2010 ImageNet training set into the 1000 different classes. On the test data, we achieved top-1 and top-5 error rates of 39.7\% and 18.9\% which is considerably better than the previous state-of-the-art results. The neural network, which has 60 million parameters and 500,000 neurons, consists of five convolutional layers, some of which are followed by max-pooling layers, and two globally connected layers with a final 1000-way softmax. To make training faster, we used non-saturating neurons and a very efficient GPU implementation of convolutional nets. To reduce overfitting in the globally connected layers we employed a new regularization method that proved to be very effective.
