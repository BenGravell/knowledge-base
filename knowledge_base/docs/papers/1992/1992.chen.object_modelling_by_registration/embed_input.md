<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Object Modelling by Registration of Multiple Range Images

Topics include Iterative closest point, Point cloud registration, Range image registration, Multi-view registration, 3D reconstruction, Object modelling, Point-to-plane registration, Surface modelling, Computer vision.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Presents an early range-image registration method for building complete 3D object models from overlapping scans. Its surface-distance objective is one of the roots of point-to-plane ICP, emphasizing registration directly against range geometry rather than relying on sparse features or known sensor poses.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study the problem of creating a complete model of a physical object. Although this may be possible using intensity images, we here use images which directly provide access to three dimensional information. The first problem that we need to solve is to find the transformation between the different views. Previous approaches either assume this transformation to be known (which is extremely difficult for a complete model), or compute it with feature matching (which is not accurate enough for integration). In this paper, we propose a new approach which works on range data directly and registers successive views with enough overlapping area to get an accurate transformation between views. This is performed by minimizing a functional which does not require point-to-point matches. We give the details of the registration method and modelling procedure and illustrate them on real range images of complex objects.
