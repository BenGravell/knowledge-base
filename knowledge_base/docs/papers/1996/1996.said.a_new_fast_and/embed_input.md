<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A New, Fast, and Efficient Image Codec Based on Set Partitioning in Hierarchical Trees

Topics include SPIHT, Set partitioning, Hierarchical trees, Wavelet transform, Image compression, Embedded coding, Bitplane coding, Zerotrees, Arithmetic coding, Progressive transmission.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Said and Pearlman reformulate zerotree wavelet coding around set partitioning and spatial-orientation trees, yielding SPIHT, a faster and stronger embedded image codec than EZW. The paper is important because it separates the core ordering idea from implementation details, producing a simple progressive bitstream with excellent rate-distortion performance and low complexity.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Embedded zerotree wavelet (EZW) coding, introduced by J. M. Shapiro, is a very effective and computationally simple technique for image compression. Here we offer an alternative explanation of the principles of its operation, so that the reasons for its excellent performance can be better understood. These principles are partial ordering by magnitude with a set partitioning sorting algorithm, ordered bit plane transmission, and exploitation of self-similarity across different scales of an image wavelet transform. Moreover, we present a new and different implementation based on set partitioning in hierarchical trees (SPIHT), which provides even better performance than our previously reported extension of EZW that surpassed the performance of the original EZW. The image coding results, calculated from actual file sizes and images reconstructed by the decoding algorithm, are either comparable to or surpass previous results obtained through much more sophisticated and computationally complex methods. In addition, the new coding and decoding procedures are extremely fast, and they can be made even faster, with only small loss in performance, by omitting entropy coding of the bit stream by the arithmetic code.
