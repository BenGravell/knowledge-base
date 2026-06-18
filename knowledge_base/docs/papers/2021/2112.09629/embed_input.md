Scalar Spatiotemporal Blue Noise Masks

Topics include Stability analysis, Distributed systems, Monte Carlo methods, White noise.

Blue noise error patterns are well suited to human perception, and when applied to stochastic rendering techniques, blue noise masks (blue noise textures) minimize unwanted low-frequency noise in the final image. Current methods of applying blue noise masks at each frame independently produce white noise frequency spectra temporally. This white noise results in slower integration convergence over time and unstable results when filtered temporally. Unfortunately, achieving temporally stable blue noise distributions is non-trivial since 3D blue noise does not exhibit the desired 2D blue noise properties, and alternative approaches degrade the spatial blue noise qualities. We propose novel blue noise patterns that, when animated, produce values at a pixel that are well distributed over time, converge rapidly for Monte Carlo integration, and are more stable under TAA, while still retaining spatial blue noise properties. To do so, we propose an extension to the well-known void and cluster algorithm that reformulates the underlying energy function to produce spatiotemporal blue noise masks.

## Introduction

Blue Noise Samples
Blue Noise Mask

Blue noise error distributions have long been recognized as an appealing alternative to purely random white noise distributions in computer graphics. In real-time and complex stochastic rendering scenarios, sample counts per frame are constrained. As a result, many modern visual effects depend on amortizing sampling expense over space and time to achieve higher quality images at an acceptable performance. If the rendered frames produce a white noise error distribution, the resulting images will contain difficult to filter low-frequency clusters.

In addition to filtering spatially, current real-time techniques often use temporal antialiasing (TAA) to filter these distributions over time. If samples over time were also made to follow a blue noise distribution, TAA could produce similar quality results with a lower alpha blend value, reducing temporal lag, or more accurate results at the same alpha value. Similarly, techniques may seek to integrate over multiple samples per pixel while still maintaining blue noise error properties spatially. Computer displays---and even human perception---can perform some amount of implicit integration over time, especially at high frame rates.

There has been considerable effort to generate good blue noise patterns---made popular in rendering by Mitchell, but also in error diffusion, ordered dithering, and digital halftoning by both Ulichney and Mitsa and Parker. These methods can broadly be divided into two categories: those that generate a discrete set of blue noise distributed sample points, and those that generate continuous values in an image, commonly referred to as blue noise masks. See Fig. 2 for comparison.

What is really desired is a technique where each two-dimensional mask has blue noise properties, and where each pixel has good one-dimensional sampling properties over the time dimension. These masks could then be used by denoising algorithms like TAA and SVGF to produce higher quality, more temporally stable results. To the best of our knowledge, we present the first algorithm for spatiotemporal blue noise mask generation.

Practical analysis of our algorithm's frequency spectrum and convergence speeds in Sections 4.2 and 4.3.
