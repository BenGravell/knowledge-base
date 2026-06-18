<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

An Exploratory Technique for Investigating Large Quantities of Categorical Data

Topics include Decision trees, CHAID, Categorical data, Chi-square tests, Survey analysis, Statistical learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces CHAID (Chi-square Automatic Interaction Detection), a multi-way decision tree algorithm for categorical outcomes that uses chi-square tests to select split variables and allows more than two branches per node. CHAID pioneered statistical significance testing as the split criterion, addressing AID's bias toward high-cardinality variables.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The technique set out in the paper, chaid, is an offshoot of aid (Automatic Interaction Detection) designed for a categorized dependent variable. Some important modifications which are relevant to standard aid include: built-in significance testing with the consequence of using the most significant predictor (rather than the most explanatory), multi-way splits (in contrast to binary) and a new type of predictor which is especially useful in handling missing information.
