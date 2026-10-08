<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Universal Image Quality Index

Topics include Image quality assessment, Full-reference metrics, Perceptual similarity, Correlation, Luminance, Contrast.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces an image quality index that factors distortion into correlation loss, luminance differences, and contrast differences. Experiments show closer agreement with subjective image quality than mean squared error without explicitly modeling the human visual system.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a new universal objective image quality index, which is easy to calculate and applicable to various image processing applications. Instead of using traditional error summation methods, the proposed index is designed by modeling any image distortion as a combination of three factors: loss of correlation, luminance distortion, and contrast distortion. Although the new index is mathematically defined and no human visual system model is explicitly employed, experiments on various image distortion types show that it exhibits surprising consistency with subjective quality measurement. It performs significantly better than the widely used distortion metric mean squared error.
