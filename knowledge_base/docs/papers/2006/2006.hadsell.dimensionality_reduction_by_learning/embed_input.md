<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Dimensionality Reduction by Learning an Invariant Mapping

Topics include Metric learning, Contrastive loss, Siamese networks, Dimensionality reduction, Invariant mapping, Representation learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces DrLIM and the contrastive-loss training setup for learning invariant embeddings from neighborhood relationships. It is an important ancestor of Siamese metric learning and modern contrastive representation learning.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Dimensionality reduction involves mapping a set of high dimensional input points onto a low dimensional manifold so that similar points in input space are mapped to nearby points on the manifold. Most existing techniques for solving the problem suffer from two drawbacks. First, most of them depend on a meaningful and computable distance metric in input space. Second, they do not compute a function that can accurately map new input samples whose relationship to the training data is unknown. We present a method - called Dimensionality Reduction by Learning an Invariant Mapping (DrLIM) - for learning a globally coherent non-linear function that maps the data evenly to the output manifold. The learning relies solely on neighborhood relationships and does not require any distance measure in the input space. The method can learn mappings that are invariant to certain transformations of the inputs, as is demonstrated with a number of experiments. Comparisons are made to other techniques, in particular LLE.
