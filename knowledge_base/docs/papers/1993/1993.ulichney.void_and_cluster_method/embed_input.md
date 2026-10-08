<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Void-and-Cluster Method for Dither Array Generation

Topics include Ordered dithering, Digital halftoning, Blue noise, Dither arrays, Isotropy, Image processing.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces a method for constructing ordered dither arrays by relocating pixels from dense clusters into voids and assigning threshold ranks. The resulting homogeneous, isotropic patterns reduce the periodic artifacts of recursive tessellation while retaining the speed of ordered dithering; the method also supports multilevel output.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Halftoning to two or more levels by means of ordered dither has always been attractive because of its speed and simplicity. However, the so-called recursive tessellation arrays in wide used suffer from strong periodic structure that imparts an unnatural appearance to resulting images. A new method for generating homogeneous ordered dither arrays is presented. A dither array is built by looking for voids and clusters in the intermediate patterns and relaxing them to optimize isotropy. While the method can be used for strikingly high quality artifact-free dithering with relatively small arrays, it is quite general; with different initial conditions the familiar recursive tessellation arrays can be built. This paper presents the algorithm for generating such arrays. Example images are compared with other ordered dither and error diffusion-based techniques.
