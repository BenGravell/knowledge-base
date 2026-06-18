Generalized Trajectory Scoring for End-to-End Multimodal Planning

Topics include Autonomous driving, End-to-end planning, Multimodal planning, Trajectory scoring, Generalization, Benchmarks.

Studies trajectory scoring as the selection layer for end-to-end multimodal driving planners, balancing static trajectory vocabularies and dynamic proposals. The paper is framed as a challenge-winning system contribution that improves generalization when choosing among diverse candidate futures.

End-to-end multi-modal planning is a promising paradigm in autonomous driving, enabling decision-making with diverse trajectory candidates. A key component is a robust trajectory scorer capable of selecting the optimal trajectory from these candidates. While recent trajectory scorers focus on scoring either large sets of static trajectories or small sets of dynamically generated ones, both approaches face significant limitations in generalization. Static vocabularies provide effective coarse discretization but struggle to make fine-grained adaptation, while dynamic proposals offer detailed precision but fail to capture broader trajectory distributions. To overcome these challenges, we propose GTRS (Generalized Trajectory Scoring), a unified framework for end-to-end multi-modal planning that combines coarse and fine-grained trajectory evaluation....

## Introduction

End-to-end multi-modal planning has emerged as a powerful approach in autonomous driving. Unlike traditional uni-modal planners that predict a single trajectory, multi-modal approaches generate multiple candidates, enabling greater adaptability during inference. This adaptability supports a wide range of applications, including responding to language instructions, accommodating different driving styles, and navigating complex driving environments.

The typical problem of end-to-end multi-modal planning involves evaluating multiple trajectory proposals through scoring given raw sensor data, without access to ground-truth perception. The planner selects the trajectory with the highest likelihood as the decision.

### Main Results

As shown in Tab., our GTRS variants achieve significant improvements over the LTF baseline \[\]. By scaling the image backbone to ViT-L \[\] and EVA-ViT-L \[\], our best single model achieves 45.3 EPDMS on the Navhard Benchmark. Further, GTRS-E-Lite, an ensemble of GTRS-Dense with GTRS-Aug during scoring, achieves 46.6 EPDMS. Our challenge-winning entry GTRS-E, an ensemble of all six variants, reaches 49.4 EPDMS, approaching the performance of PDM-Closed \[\]---a privileged planner that relies on ground-truth perception---despite ours using challenging synthetic sensor input....

Table 1: Roadmap to Generalized Trajectory Scoring. Random denotes that we randomly select a trajectory from 𝒱dp during inference. V2-99 is pretrained from DD3D, EVA-ViT-L is initialized from StreamPETR, and ViT-L is from Depth Anything.

To obtain high-quality dynamic trajectory proposals during inference, diffusion models have become a popular practice in autonomous driving for its ability to generate multi-modal trajectory candidates. We adopt a Diffusion Policy-based trajectory generator following \[\] to produce multiple trajectory proposals. This sub-network is composed of an image backbone to extract image features, a BEV encoder where BEV queries attend to image features through a Transformer Encoder \[\], and a Diffusion Transformer that generates $N$ trajectory proposals $\mathcal{V}_{dp}$ conditioned on the BEV features.

Together, these strategies enable GTRS-Aug to perform robustly in challenging out-of-domain settings without domain-specific adaptation.
