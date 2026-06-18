<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Bundle Adjustment — A Modern Synthesis

Topics include Bundle adjustment, Computer vision, Photogrammetry, Structure from motion, Sparse optimization, Robust estimation, Nonlinear least squares.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Synthesizes bundle adjustment for computer vision, covering robust cost functions, sparse Newton methods, gauge freedom, updating strategies, and quality control. The paper became a standard implementation-oriented reference for refining camera and structure estimates in photogrammetry and structure-from-motion pipelines.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper is a survey of the theory and methods of photogrammetric bundle adjustment, aimed at potential implementors in the computer vision community. Bundle adjustment is the problem of refining a visual reconstruction to produce jointly optimal structure and viewing parameter estimates. Topics covered include: the choice of cost function and robustness; numerical optimization including sparse Newton methods, linearly convergent approximations, updating and recursive methods; gauge (datum) invariance; and quality control. The theory is developed for general robust cost functions rather than restricting attention to traditional nonlinear least squares.
