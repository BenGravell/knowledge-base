<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Online Policy Optimization in Unknown Nonlinear Systems

Topics include Gradient descent, Regret bounds, Robustness, Online algorithms, Optimization, Control, Called memoryless GAPS, M-GAPS, Nonlinear systems.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study online policy optimization in nonlinear time-varying dynamical systems where the true dynamical models are unknown to the controller. This problem is challenging because, unlike in linear systems, the controller cannot obtain globally accurate estimations of the ground-truth dynamics using local exploration. We propose a meta-framework that combines a general online policy optimization algorithm (textttALG) with a general online estimator of the dynamical system's model parameters (textttEST). We show that if the hypothetical joint dynamics induced by textttALG with known parameters satisfies several desired properties, the joint dynamics under inexact parameters from textttEST will be robust to errors. Importantly, the final policy regret only depends on textttEST's predictions on the visited trajectory, which relaxes a bottleneck on identifying the true parameters globally. To demonstrate our framework, we develop a computationally efficient variant of Gradient-based Adaptive Policy Selection, called Memoryless GAPS (M-GAPS), and use it to instantiate textttALG. Combining M-GAPS with online gradient descent to instantiate textttEST yields (to our knowledge) the first local regret bound for online policy optimization in nonlinear time-varying systems with unknown dynamics.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

This is where the content of your paper goes.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Limit the main text (not counting references and appendices) to 12 PMLR-formatted pages, using this template. Please add any additional appendix to the same file after references - there is no page limit for the appendix.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Include, either in the main text or the appendices, *all* details, proofs and derivations required to substantiate the results.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The contribution, novelty and significance of submissions will be judged primarily based on the main text of 12 pages. Thus, include enough details, and overview of key arguments, to convince the reviewers of the validity of result statements, and to ease parsing of technical material in the appendix.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Use the \\documentclass\[anon,12pt\]{colt2024} option during submission process -- this automatically hides the author names listed under \\coltauthor. Submissions should NOT include author names or other identifying information in the main text or appendix. To the extent possible, you should avoid including directly identifying information in the text. You should still include all relevant references, discussion, and scientific content, even if this might provide significant hints as to the author identity. But you should generally refer to your own prior work in third person. Do not include acknowledgments in the submission. They can be added in the camera-ready version of accepted papers.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Please note that while submissions must be anonymized, and author names are withheld from reviewers, they are known to the area chair overseeing the paper's review. The assigned area chair is allowed to reveal author names to a reviewer during the rebuttal period, upon the reviewer's request, if they deem such information is needed in ensuring a proper review.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Use \\documentclass\[final,12pt\]{colt2024} only during camera-ready submission.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We thank a bunch of people and funding agency.
