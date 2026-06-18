<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Image Coding Using Wavelet Transform

Topics include Wavelet transform, Biorthogonal wavelets, Vector quantization, Image compression, Progressive transmission, Rate-distortion theory, Psychovisual modeling, Multiresolution coding.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Antonini, Barlaud, Mathieu, and Daubechies show how biorthogonal wavelet transforms, multiresolution vector quantization, and psychovisual bit allocation can form an effective still-image coder. The paper is an early bridge from wavelet theory to practical progressive image coding, and it helped set up the wavelet-based line of work that eventually led to JPEG 2000.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Image compression is now essential for applications such as transmission and storage in data bases. This paper proposes a new scheme for image compression taking into account psychovisual features both in the space and frequency domains; this new method involves two steps. First, we use a wavelet transform in order to obtain a set of biorthogonal subclasses of images; the original image is decomposed at different scales using a pyramidal algorithm architecture. The decomposition is along the vertical and horizontal directions and maintains constant the number of pixels required to describe the image. Second, according to Shannon's rate distortion theory, the wavelet coefficients are vector quantized using a multiresolution codebook. Furthermore, to encode the wavelet coefficients, we propose a noise shaping bit allocation procedure which assumes that details at high resolution are less visible to the human eye. Finally, in order to allow the receiver to recognize a picture as quickly as possible at minimum cost, we present a progressive transmission scheme. It is shown that the wavelet transform is particularly well adapted to progressive transmission.
