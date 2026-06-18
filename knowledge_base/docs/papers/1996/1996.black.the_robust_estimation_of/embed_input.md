<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Robust Estimation of Multiple Motions: Parametric and Piecewise-Smooth Flow Fields

Topics include Optical flow, Robust estimation, Multiple motion, Parametric motion, Piecewise-smooth flow, Motion discontinuities, Outlier rejection.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Black and Anandan recast optical flow estimation around robust penalties so that brightness and smoothness violations can be treated as outliers rather than fatal model failures. The work is especially important for motion boundaries, transparency, specularities, and layered or multiple-motion scenes where single-motion assumptions break down.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Most approaches for estimating optical flow assume that, within a finite image region, only a single motion is present. This single motion assumption is violated in common situations involving transparency, depth discontinuities, independently moving objects, shadows, and specular reflections. To robustly estimate optical flow, the single motion assumption must be relaxed. This paper presents a framework based on robust estimation that addresses violations of the brightness constancy and spatial smoothness assumptions caused by multiple motions. We show how the robust estimation framework can be applied to standard formulations of the optical flow problem thus reducing their sensitivity to violations of their underlying assumptions. The approach has been applied to three standard techniques for recovering optical flow: area-based regression, correlation, and regularization with motion discontinuities. This paper focuses on the recovery of multiple parametric motion models within a region, as well as the recovery of piecewise-smooth flow fields, and provides examples with natural and synthetic image sequences.
