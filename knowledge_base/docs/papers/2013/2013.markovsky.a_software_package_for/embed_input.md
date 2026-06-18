<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Software Package for System Identification in the Behavioral Setting

Topics include System identification, Behavioral systems, Structured low-rank approximation, Mosaic hankel matrices, Missing data, Multiple experiments, Total least squares, Reproducible software.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Packages behavioral system identification as a structured low-rank approximation problem over mosaic-Hankel matrices, including exact and missing variables and multiple experiments. It is useful context for how behavioral, representation-free control ideas became numerically actionable rather than only conceptual.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

An identification problem with no a priori separation of the variables into inputs and outputs and representation invariant approximation criterion is considered. The model class consists of linear time-invariant systems of bounded complexity and the approximation criterion is the minimum of a weighted 2-norm distance between the given time series and a time series that is consistent with the model. The problem is equivalent to and is solved as a mosaic-Hankel structured low-rank approximation problem. Software implementing the approach is developed and tested on benchmark problems. Additional nonstandard features of the software are specification of exact and missing variables and identification from multiple experiments.
