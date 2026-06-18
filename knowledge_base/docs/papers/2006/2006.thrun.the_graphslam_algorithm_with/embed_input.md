<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The GraphSLAM Algorithm with Applications to Large-Scale Mapping of Urban Structures

Topics include Simultaneous localization and mapping, Graph-based simultaneous localization and mapping, Sparse optimization, Variable elimination, Data association, Large-scale mapping, Urban mapping, Robot localization, GraphSLAM.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Formulates full SLAM as a sparse graphical optimization problem over robot poses and map features, then uses variable elimination to reduce and solve the resulting likelihood graph. The paper helped crystallize graph-based SLAM as a unifying alternative to filtering and showed that large urban maps could be handled by exploiting sparsity.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This article presents GraphSLAM, a unifying algorithm for the offline SLAM problem. GraphSLAM is closely related to a recent sequence of research papers on applying optimization techniques to SLAM problems. It transforms the SLAM posterior into a graphical network, representing the log-likelihood of the data. It then reduces this graph using variable elimination techniques, arriving at a lower-dimensional problems that is then solved using conventional optimization techniques. As a result, GraphSLAM can generate maps with 108 or more features. The paper discusses a greedy algorithm for data association, and presents results for SLAM in urban environments with occasional GPS measurements.
