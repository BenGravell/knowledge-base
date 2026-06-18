<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Forced Random Dithering: Improved Threshold Matrices for Ordered Dithering

Topics include Ordered dithering, Halftoning, Threshold matrix generation, Blue-noise dithering, Image quantization, Dispersed-dot halftoning, Low-frequency artifact suppression, Digital printing.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Proposes forced random dithering, a method for constructing improved threshold matrices for ordered dithering that suppresses low-frequency artifacts while avoiding excessive random noise. By optimizing micro-dot distributions to closely approximate target intensity levels, the technique achieves output quality competitive with stochastic dithering while retaining the computational predictability of ordered dithering.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper examines the possibilities of improving halftoning techniques using dispersed dots. This corresponds to finding micro-dot distributions that approximate the intensity levels that have to be rendered. A widely used halftoning method is ordered dithering, which uses a threshold matrix to decide if a micro-dot should be set in the output image. A way to generate improved threshold matrices for ordered dithering will be introduced that avoids unwanted low-frequency portions without introducing too much random noise into the rendered image. Since the presented method produces images of high quality it is ideally suited for output generation in high-end image processing systems.
