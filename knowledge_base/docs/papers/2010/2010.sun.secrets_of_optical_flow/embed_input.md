<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Secrets of Optical Flow Estimation and Their Principles

Topics include Optical flow, Variational methods, Classic+NL, Middlebury benchmark, Median filtering, Non-local regularization, Implementation analysis.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Sun, Roth, and Black dissect modern variational optical flow and show that careful implementation choices matter as much as the nominal objective. The paper is remembered for explaining why median filtering during warping helps, then turning that heuristic into a non-local regularization term that leads to the Classic+NL model.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The most accurate methods on the Middlebury flow dataset make different choices about how to model the objective function, how to approximate this model to make it computationally tractable, and how to optimize it. Since most published methods change all of these properties at once, it can be difficult to know which choices are most important. To address this, we define a baseline algorithm that is "classical", in that it is a direct descendant of the original HS formulation, and then systematically vary the model and method using different techniques from the art. The results are surprising. We find that only a small number of key choices produce statistically significant improvements and that they can be combined into a very simple method that achieves accuracies near the state of the art. More importantly, our analysis reveals what makes current flow methods work so well.
