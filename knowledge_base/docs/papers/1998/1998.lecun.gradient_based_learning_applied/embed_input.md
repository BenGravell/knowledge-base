<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Gradient-Based Learning Applied to Document Recognition

Topics include Convolutional neural network, LeNet, Document recognition, Handwriting recognition, Gradient-based learning, Graph transformer networks.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

The canonical LeNet paper shows that convolutional neural networks can learn directly from pixel inputs for document recognition, and extends the idea to globally trainable document-processing pipelines via Graph Transformer Networks. It is one of the clearest early demonstrations that learned features can replace hand-engineered recognition pipelines.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Multilayer neural networks trained with the backpropagation algorithm constitute the best example of a successful gradient-based learning technique. Given an appropriate network architecture, gradient-based learning algorithms can be used to synthesize a complex decision surface that can classify high-dimensional patterns such as handwritten characters, with minimal preprocessing. This paper reviews various methods applied to handwritten character recognition and compares them on a standard handwritten digit recognition task. Convolutional neural networks, that are specifically designed to deal with the variability of 2D shapes, are shown to outperform all other techniques. Real-life document recognition systems are composed of multiple modules including field extraction, segmentation, recognition, and language modeling. A new learning paradigm, called Graph Transformer Networks (GTN), allows such multi-module systems to be trained globally using gradient-based methods so as to minimize an overall performance measure. Two systems for on-line handwriting recognition are described. Experiments demonstrate the advantage of global training, and the flexibility of Graph Transformer Networks. A graph transformer network for reading a bank cheque is also described.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

It uses convolutional neural network character recognizers combined with global training techniques to provide record accuracy on business and personal cheques.
