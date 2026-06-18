Scalar Spatiotemporal Blue Noise Masks

Topics include Stability analysis, Distributed systems, Monte Carlo methods, White noise.

Blue noise error patterns are well suited to human perception, and when applied to stochastic rendering techniques, blue noise masks (blue noise textures) minimize unwanted low-frequency noise in the final image. Current methods of applying blue noise masks at each frame independently produce white noise frequency spectra temporally. This white noise results in slower integration convergence over time and unstable results when filtered temporally. Unfortunately, achieving temporally stable blue noise distributions is non-trivial since 3D blue noise does not exhibit the desired 2D blue noise properties, and alternative approaches degrade the spatial blue noise qualities. We propose novel blue noise patterns that, when animated, produce values at a pixel that are well distributed over time, converge rapidly for Monte Carlo integration, and are more stable under TAA, while still retaining spatial blue noise properties. To do so, we propose an extension to the well-known void and cluster algorithm that reformulates the underlying energy function to produce spatiotemporal blue noise masks....

## Introduction

Blue Noise Samples
Blue Noise Mask

Figure 2. The left two images show blue noise sample points in 2D and the magnitude of the discrete Fourier transform (DFT). These are in contrast to the two images to the right, which show a blue noise mask and the magnitude of the DFT. In this case, the mask is a 2D image where each pixel stores a single “random value” with blue noise properties. Both samples and masks show attenuated low frequencies but have different uses. Our work focuses on masks.

Generated spatiotemporal blue noise masks and the code to generate them can be found at:

A zip of the supplemental material can be found at:

Both the golden ratio and the low discrepancy sequence by Heitz and Belcour exhibit damaged blue noise frequencies spatially, at the trade-off of better convergence over time. However, both of these low discrepancy noise patterns exhibit strobing patterns along the time dimension, which can be seen as distinct horizontal lines in DFT(XZ). See also Figure 7. For offline rendering, these strobing patterns only occur during convergence, and therefore do not affect the final frame. For real-time applications though, this temporal strobing will lead to a more challenging signal to filter temporally.

Once half of our pixels are ordered, in *Phase III* the state of all the pixels are reversed. Pixels that are on are turned off, and vice versa. Next, we follow a similar process to *Phase II*, and iteratively find the current largest valued cluster pixel that is on and turn that pixel off, assigning to that pixel an order found by counting the number of pixels that were off before this pixel was turned off. When all pixels are turned off, *Phase III* is finished and all pixels will have an ordering.

## Applications and Results

Blue noise error distributions have long been recognized as an appealing alternative to purely random white noise distributions in computer graphics. In real-time and complex stochastic rendering scenarios, sample counts per frame are constrained. As a result, many modern visual effects depend on amortizing sampling expense over space and time to achieve higher quality images at an acceptable performance. If the rendered frames produce a white noise error distribution, the resulting images will contain difficult to filter low-frequency clusters....
