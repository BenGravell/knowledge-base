<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Fast and Resolution Independent Line Integral Convolution

Topics include Line integral convolution, Fast line integral convolution, Flow visualization, Vector field visualization, Resolution independence, Streamline integration, Texture synthesis, Scientific visualization, Computer graphics, Animation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Makes LIC much more practical by separating streamline computation from convolution, reusing long streamline segments, and supporting arbitrary output resolution. The result is an order-of-magnitude speedup over the original algorithm plus cleaner support for zooming and animated LIC textures.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Line Integral Convolution (LIC) is a powerful technique for generating striking images and animations from vector data. Introduced in 1993, the method has rapidly found many application areas, ranging from computer arts to scientific visualization. Based upon locally filtering an input texture along a curved stream line segment in a vector field, it is able to depict directional information at high spatial resolutions. We present a new method for computing LIC images. It employs simple box filter kernels only and minimizes the total number of stream lines to be computed. Thereby it reduces computational costs by an order of magnitude compared to the original algorithm. Our method utilizes fast, error-controlled numerical integrators. Decoupling the characteristic lengths in vector field grid, input texture and output image, it allows computation of filtered images at arbitrary resolution. This feature is of significance in computer animation as well as in scientific visualization, where it can be used to explore vector data by smoothly enlarging structure of details. We also present methods for improved texture animation, again employing box filter kernels only. To obtain an optimal motion effect, spatial decay of correlation between intensities of distant pixels in the output image has to be controlled.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This is achieved by blending different phase-shifted box filter animations and by adaptively rescaling the contrast of the output frames.
