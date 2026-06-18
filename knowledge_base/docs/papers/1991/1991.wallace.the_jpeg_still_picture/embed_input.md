<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The JPEG Still Picture Compression Standard

Topics include Joint photographic experts group, Image compression, Still image coding, Discrete cosine transform, Quantization, Huffman coding, Arithmetic coding, Lossy compression, Lossless compression, Standards.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Wallace explains the still-image JPEG standard at the point when DCT-based baseline JPEG was becoming the common interchange format for photographic images. The paper is useful both as a historical standardization record and as a compact engineering description of the transform, quantization, entropy coding, progressive, lossless, and hierarchical pieces that shaped practical image compression.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

For the past few years, a joint ISO/CCITT committee known as JPEG (Joint Photographic Experts Group) has been working to establish the first international compression standard for continuous-tone still images, both grayscale and color. JPEG's proposed standard aims to be generic, to support a wide variety of applications for continuous-tone images. To meet the differing needs of many applications, the JPEG standard includes two basic compression methods, each with various modes of operation. A DCT-based method is specified for "lossy" compression, and a predictive method for "lossless" compression. JPEG features a simple lossy technique known as the Baseline method, a subset of the other DCT-based modes of operation. The Baseline method has been by far the most widely implemented JPEG method to date, and is sufficient in its own right for a large number of applications. This article provides an overview of the JPEG standard, and focuses in detail on the Baseline method.
