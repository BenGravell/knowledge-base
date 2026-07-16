<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

An Introduction to Compressive Sampling

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Conventional approaches to sampling signals or images follow Shannon's theorem: the sampling rate must be at least twice the maximum frequency present in the signal (Nyquist rate). In the field of data conversion, standard analog-to-digital converter (ADC) technology implements the usual quantized Shannon representation - the signal is uniformly sampled at or above the Nyquist rate. This article surveys the theory of compressive sampling, also known as compressed sensing or CS, a novel sensing/sampling paradigm that goes against the common wisdom in data acquisition. CS theory asserts that one can recover certain signals and images from far fewer samples or measurements than traditional methods use.
