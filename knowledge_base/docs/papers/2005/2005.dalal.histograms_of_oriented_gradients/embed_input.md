<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Histograms of Oriented Gradients for Human Detection

Topics include Pedestrian detection, Histogram of oriented gradients, HOG, Object detection, Support vector machine, Computer vision, Feature descriptor.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces HOG (Histograms of Oriented Gradients) descriptors: gradient orientation histograms computed in overlapping, contrast-normalized blocks over a dense grid, fed into a linear SVM. Significantly outperformed prior human detection methods, and the HOG+SVM pipeline dominated rigid object detection until the deep learning era.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the question of feature sets for robust visual object recognition; adopting linear SVM based human detection as a test case. After reviewing existing edge and gradient based descriptors, we show experimentally that grids of histograms of oriented gradient (HOG) descriptors significantly outperform existing feature sets for human detection. We study the influence of each stage of the computation on performance, concluding that fine-scale gradients, fine orientation binning, relatively coarse spatial binning, and high-quality local contrast normalization in overlapping descriptor blocks are all important for good results. The new approach gives near-perfect separation on the original MIT pedestrian database, so we introduce a more challenging dataset containing over 1800 annotated human images with a large range of pose variations and backgrounds.
