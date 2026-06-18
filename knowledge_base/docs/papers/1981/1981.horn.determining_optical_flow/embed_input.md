<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Determining Optical Flow

Topics include Optical flow, Horn-Schunck, Variational methods, Brightness constancy, Smoothness regularization, Dense motion estimation, Computer vision.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Horn and Schunck introduce the canonical global variational formulation of optical flow: combine brightness constancy with a smoothness prior to recover a dense velocity field. The paper is foundational because it exposes the aperture problem clearly and turns optical flow into an optimization problem whose data and regularization terms shaped decades of later methods.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Optical flow cannot be computed locally, since only one independent measurement is available from the image sequence at a point, while the flow velocity has two components. A second constraint is needed. A method for finding the optical flow pattern is presented which assumes that the apparent velocity of the brightness pattern varies smoothly almost everywhere in the image. An iterative implementation is shown which successfully computes the optical flow for a number of synthetic image sequences. The algorithm is robust in that it can handle image sequences that are quantized rather coarsely in space and time. It is also insensitive to quantization of brightness levels and additive noise. Examples are included where the assumption of smoothness is violated at singular points or along lines in the image.
