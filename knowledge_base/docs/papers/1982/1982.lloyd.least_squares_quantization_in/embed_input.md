<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Least Squares Quantization in PCM

Topics include Lloyd's algorithm, Vector quantization, Scalar quantization, k-means, Pulse-code modulation, Least squares, Signal processing.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Lloyd derives necessary optimality conditions for finite-level least-squares quantizers in pulse-code modulation and gives numerical quantizers for common distributions. The work is one of the classic sources for Lloyd's algorithm, closely tied to k-means and vector quantization through alternating assignment and centroid updates.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

It has long been realized that in pulse-code modulation (PCM), with a given ensemble of signals to handle, the quantum values should be spaced more closely in the voltage regions where the signal amplitude is more likely to fall. It has been shown by Panter and Dite that, in the limit as the number of quanta becomes infinite, the asymptotic fractional density of quanta per unit voltage should vary as the one-third power of the probability density per unit voltage of signal amplitudes. In this paper the corresponding result for any finite number of quanta is derived; that is, necessary conditions are found that the quanta and associated quantization intervals of an optimum finite quantization scheme must satisfy. The optimization criterion used is that the average quantization noise power be a minimum. It is shown that the result obtained here goes over into the Panter and Dite result as the number of quanta become large. The optimum quantization schemes for 2^b quanta, b=1,2,...,7, are given numerically for Gaussian and for Laplacian distribution of signal amplitudes.
