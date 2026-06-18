<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Simple and Practical Algorithm for Sparse Fourier Transform

Topics include Sparse fourier transform, Sublinear algorithms, Signal processing, Sketching, Frequency estimation, Gaussian filters, Dolph-Chebyshev filters.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Gives a practical sparse Fourier transform algorithm that estimates the largest Fourier coefficients without running a full FFT, using signal-processing filters and a one-shot sketching-style identification step. The important contribution is making sparse Fourier methods more usable in realistic regimes by combining sublinear sampling and running-time guarantees with experiments showing speedups over FFT for sufficiently sparse spectra.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider the sparse Fourier transform problem: given a complex vector x of length n, and a parameter k, estimate the k largest (in magnitude) coefficients of the Fourier transform of x. The problem is of key interest in several areas, including signal processing, audio/image/video compression, and learning theory. We propose a new algorithm for this problem. The algorithm leverages techniques from digital signal processing, notably Gaussian and Dolph-Chebyshev filters. Unlike the typical approach to this problem, our algorithm is not iterative. That is, instead of estimating “large” coefficients, subtracting them and recursing on the reminder, it identifies and estimates the k largest coefficients in “one shot”, in a manner akin to sketching/streaming algorithms. The resulting algorithm is structurally simpler than its predecessors. As a consequence, we are able to extend considerably the range of sparsity, k, for which the algorithm is faster than FFT, both in theory and practice.
