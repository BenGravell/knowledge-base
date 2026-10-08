<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Factor Graphs and GTSAM: A Hands-On Introduction

Topics include Factor graphs, GTSAM, Simultaneous localization and mapping, State estimation, Sparse optimization, Structure from motion.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces factor graphs and the GTSAM library through executable examples of inference, robot localization, SLAM, and structure from motion. Explains how sparse graphical structure enables efficient batch and incremental estimation.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This tutorial introduces factor graphs and the GTSAM library through examples from robotics and computer vision. Factor graphs express estimation problems, including simultaneous localization and mapping and structure from motion, as bipartite graphs connecting unknown variables to factors that encode measurements and prior information. GTSAM is a BSD-licensed C++ library developed at Georgia Tech for solving these and other estimation problems. Its MATLAB interface supports prototyping, visualization, and interaction. The library exploits the sparse connections produced by measurements involving only a few variables to reduce computational cost, and offers iterative methods for graphs that are too dense for efficient direct solution.
