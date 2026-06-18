<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

DoG Is SGD’s Best Friend: A Parameter-Free Dynamic Step Size Schedule

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a tuning-free dynamic SGD step size formula, which we call Distance over Gradients (DoG). The DoG step sizes depend on simple empirical quantities (distance from the initial point and norms of gradients) and have no “learning rate” parameter. Theoretically, we show that, for stochastic convex optimization, a slight variation of the DoG formula enjoys strong, high-probability parameter-free convergence guarantees and iterate movement bounds. Empirically, we consider a broad range of vision and language transfer learning tasks, and show that DoG’s performance is close to that of SGD with tuned learning rate. We also propose a per-layer variant of DoG that generally outperforms tuned SGD, approaching the performance of tuned Adam. A PyTorch implementation of our algorithms is available at
