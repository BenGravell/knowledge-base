<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

High Accuracy Optical Flow Estimation Based on a Theory for Warping

Topics include Optical flow, Brox optical flow, Variational methods, Warping, Gradient constancy, Coarse-to-fine estimation, Robust smoothness.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Brox, Bruhn, Papenberg, and Weickert give a high-accuracy variational optical-flow model that combines brightness constancy, gradient constancy, and discontinuity-preserving smoothness. Its main lasting contribution is a principled account of coarse-to-fine warping for large displacements, tying a widely used practical trick to an explicit numerical scheme.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study an energy functional for computing optical flow that combines three assumptions: a brightness constancy assumption, a gradient constancy assumption, and a discontinuity-preserving spatio-temporal smoothness constraint. In order to allow for large displacements, linearisations in the two data terms are strictly avoided. We present a consistent numerical scheme based on two nested fixed point iterations. By proving that this scheme implements a coarse-to-fine warping strategy, we give a theoretical foundation for warping which has been used on a mainly experimental basis so far. Our evaluation demonstrates that the novel method gives significantly smaller angular errors than previous techniques for optical flow estimation. We show that it is fairly insensitive to parameter variations, and we demonstrate its excellent robustness under noise.
