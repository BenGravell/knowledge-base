<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A General Framework for Object Detection

Topics include Object detection, Computer vision, Wavelet features, Support vector machine, Face detection, Pedestrian detection.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces a trainable object detection framework using wavelet feature representations and SVM classification, demonstrated on faces and pedestrians. An influential precursor to the HOG-SVM and cascade detector pipelines that established the learn-from-examples paradigm for visual object detection.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents a general trainable framework for object detection in static images of cluttered scenes. The detection technique we develop is based on a wavelet representation of an object class derived from a statistical analysis of the class instances. By learning an object class in terms of a subset of an overcomplete dictionary of wavelet basis functions, we derive a compact representation of an object class which is used as an input to a support vector machine classifier. This representation overcomes both the problem of in-class variability and provides a low false detection rate in unconstrained environments. We demonstrate the capabilities of the technique in two domains whose inherent information content differs significantly. The first system is face detection and the second is the domain of people which, in contrast to faces, vary greatly in color, texture, and patterns. Unlike previous approaches, this system learns from examples and does not rely on any a priori (hand-crafted) models or motion-based segmentation. The paper also presents a motion-based extension to enhance the performance of the detection algorithm over video sequences. The results presented here suggest that this architecture may well be quite general.
