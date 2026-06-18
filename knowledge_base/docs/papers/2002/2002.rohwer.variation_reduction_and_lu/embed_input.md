<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Variation Reduction and Lu Lu-Smoothing

Topics include Signal filtering, Nonlinear smoothing, LULU smoothing, Total variation, Variation reduction, Variation preservation, Impulsive noise, Shape preservation, Median smoothers.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Develops the variation-preserving view of LULU smoothers, showing that they split a sequence into smoothed signal and residual parts without losing total variation. This gives a mathematical basis for using these nonlinear smoothers to remove impulsive noise while preserving shape features, and clarifies why median smoothers can behave well despite their less direct structure.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In the space of absolutely summable sequences the total variation of a sequence becomes a natural norm, and is a measure of smoothness. This norm is preserved by the so-called LU LU-smoothers, in that the variation of the image plus the variation of the difference is equal to the variation of the original sequence. This surprising property is useful for strategies for the removal of impulsive and other random noise. Strong shape preserving properties of these smoothers are derived in the process of proving this. The results shed light on similar properties of the popular median smoothers, as well as their sometimes enigmatic behaviour.
