<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Animating Flow Fields: Rendering of Oriented Line Integral Convolution

Topics include Flow visualization, Vector field visualization, Line integral convolution, Computer graphics, Animation.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Extends the standard Line Integral Convolution (LIC) visualization technique to encode both flow direction and orientation in a single image, using a sparse input texture and an asymmetric ramp convolution kernel. The resulting Oriented LIC (OLIC) also supports animation of flow fields by reusing precomputed pixel traces.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Line Integral Convolution (LIC) is a common approach for the visualisation of 2D vector fields. It is well suited for visualizing the direction of a flow field, but it gives no information about the orientation of the underlying vectors. We introduce Oriented Line Integral Convolution (OLIC), where direction as well as orientation are encoded within the resulting image. This is achieved by using a sparse input texture and a ramp like (anisotropic) convolution kernel. This method can be used for animations, whereby the computation of so called pixel traces fastens the calculation process. Various OLICs illustrating simple and real world vector fields are shown.
