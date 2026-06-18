<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Building Rome with Convex Optimization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Global bundle adjustment is made easy by depth prediction and convex optimization. We (i) propose a scaled bundle adjustment (SBA) formulation that lifts 2D keypoint measurements to 3D with learned depth, (ii) design an empirically tight convex semidefinite programming (SDP) relaxation that solves SBA to certifiable global optimality, (iii) solve the SDP relaxation at extreme scale with Burer-Monteiro factorization and a CUDA-based trust-region Riemannian optimizer (dubbed XM), (iv) build a structure from motion pipeline with XM as the optimization engine and show that XM-SfM compares favorably with existing pipelines in terms of reconstruction quality while being significantly faster, more scalable, and initialization-free.
