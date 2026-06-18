<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Tutorial on Fast Fourier Sampling

Topics include Fourier sampling, Sparse frequency sampling, Signal processing, Sublinear algorithms, Randomized algorithms, Frequency estimation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Surveys fast Fourier sampling methods for recovering sparse or compressible frequency structure without computing a full transform. The tutorial frames sparse Fourier ideas as randomized sublinear algorithms for signal processing.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This article describes a computational method, called the Fourier sampling algorithm. The algorithm takes a small number of (correlated) random samples from a signal and processes them efficiently to produce an approximation of the DFT of the signal. The algorithm offers provable guarantees on the number of samples, the running time, and the amount of storage. As we will see, these requirements are exponentially better than the FFT for some cases of interest.
