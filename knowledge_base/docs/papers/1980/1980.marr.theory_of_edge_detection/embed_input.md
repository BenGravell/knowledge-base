<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Theory of Edge Detection

Topics include Edge detection, Computer vision, Marr-Hildreth, Laplacian of Gaussian, Zero crossings, Primal sketch.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Formulates the classic Marr-Hildreth model of edge detection: smooth at multiple scales, apply the Laplacian of Gaussian, and detect zero crossings. It links computational vision, psychophysics, and a proposed neural implementation of early visual processing.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A theory of edge detection is presented. The analysis proceeds in two parts. Intensity changes, which occur in a natural image over a wide range of scales, are detected separately at different scales. An appropriate filter for this purpose at a given scale is found to be the second derivative of a Gaussian, and it is shown that, provided some simple conditions are satisfied, these primary filters need not be orientation-dependent. Thus, intensity changes at a given scale are best detected by finding the zero values of nabla^2 G(x, y)*I(x, y) for image I, where G(x, y) is a two-dimensional Gaussian distribution and nabla^2 is the Laplacian. The intensity changes thus discovered in each of the channels are then represented by oriented primitives called zero-crossing segments, and evidence is given that this representation is complete. Intensity changes in images arise from surface discontinuities or from reflectance or illumination boundaries, and these all have the property that they are spatially localized. Because of this, the zero-crossing segments from the different channels are not independent, and rules are deduced for combining them into a description of the image.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This description is called the raw primal sketch. The theory explains several basic psychophysical findings, and the operation of forming oriented zero-crossing segments from the output of centre-surround nabla^2 G filters acting on the image forms the basis for a physiological model of simple cells.
