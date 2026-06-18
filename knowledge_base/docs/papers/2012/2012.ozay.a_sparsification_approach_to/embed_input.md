<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Sparsification Approach to Set Membership Identification of Switched Affine Systems

Topics include Switched affine systems, Set membership identification, Sparse optimization, Hybrid systems, Convex relaxation, Bounded noise, System identification.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Turns set-membership identification of switched affine systems into a sparsification problem, using sparsity in constructed residual or switching sequences to recover models and switching behavior from noisy data. The key result is that, under l-infinity bounded noise for the switch-count formulation, the sparsification problem admits an exact convex optimization solution, connecting hybrid-system identification to sparse recovery tools.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper addresses the problem of robust identification of a class of discrete-time affine hybrid systems, switched affine models, in a set membership framework. Given a finite collection of noisy input/output data and some minimal a priori information about the set of admissible plants, the objective is to identify a suitable set of affine models along with a switching sequence that can explain the available experimental information, while minimizing either the number of switches or subsystems. For the case where it is desired to minimize the number of switches, the key idea of the paper is to reduce this problem to a sparsification form, where the goal is to maximize sparsity of a suitably constructed vector sequence. Our main result shows that in the case of ℓ ∞ bounded noise, this sparsification problem can be exactly solved via convex optimization. In the general case where the noise is only known to belong to a convex set N, the problem is generically NP-hard. However, as we show in the paper, efficient convex relaxations can be obtained by exploiting recent results on sparse signal recovery.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Similarly, we present both a sparsification formulation and a convex relaxation for the (known to be NP hard) case where it is desired to minimize the number of subsystems. These results are illustrated using two non-trivial problems arising in computer vision applications: video-shot and dynamic texture segmentation.
