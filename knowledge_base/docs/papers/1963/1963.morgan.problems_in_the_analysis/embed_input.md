<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Problems in the Analysis of Survey Data, and a Proposal

Topics include Decision trees, AID, Survey data analysis, Regression trees, Interaction detection, Statistical learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces AID (Automatic Interaction Detection), the first regression-tree algorithm, which recursively partitions survey data into binary groups to maximize variance reduction. Though designed for survey analysis, it established the recursive partitioning framework later refined into CART, CHAID, ID3, and all modern decision tree methods.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Most of the problems of analyzing survey data have been reasonably well handled, except those revolving around the existence of interaction effects. Indeed, increased efficiency in handling multivariate analyses even with non-numerical variables, has been achieved largely by assuming additivity. An approach to survey data is proposed which imposes no restrictions on interaction effects, focuses on importance in reducing predictive error, operates sequentially, and is independent of the extent of linearity in the classifications or the order in which the explanatory factors are introduced.
