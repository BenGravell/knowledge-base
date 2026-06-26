## Introduction

End-to-end multi-modal planning has emerged as a powerful approach in autonomous driving. Unlike traditional uni-modal planners that predict a single trajectory, multi-modal approaches generate multiple candidates, enabling greater adaptability during inference. This adaptability supports a wide range of applications, including responding to language instructions, accommodating different driving styles, and navigating complex driving environments.

The typical problem of end-to-end multi-modal planning involves evaluating multiple trajectory proposals through scoring given raw sensor data, without access to ground-truth perception. The planner selects the trajectory with the highest likelihood as the decision.

Current trajectory scoring methods generally fall into two categories: scoring a large static vocabulary, and scoring a small set of dynamically generated proposals. Both approaches face challenges in generalization. Fixed trajectory vocabularies offer limited flexibility, as they cannot adapt to situations where dynamic proposals are needed. Meanwhile, methods that rely on a small number of dynamic proposals often fail to generalize to unseen trajectories, since the scorer is only exposed to a narrow subset during training. Ideally, a robust scorer should generalize across diverse trajectory distributions---whether static or dynamic---to handle the full complexity of real-world scenarios.

To address these limitations, we propose GTRS (Generalized Trajectory Scoring) for end-to-end multi-modal planning. GTRS is built on a key insight: an effective trajectory scorer must be trained on both coarse and fine-grained trajectory distributions to develop robust generalization capabilities. Our approach contains three complementary techniques, each leading to a dedicated sub-network as shown in Fig. 1: Diffusion-based Trajectory Generation (DP): A diffusion policy (DP) produces diverse trajectory candidates with BEV features as the condition. DP provides the fine-grained details crucial for safety-critical situations that coarse, fixed vocabularies cannot capture. (Sec. 2.1) Trajectory Vocabulary Generalization (GTRS-Dense): We train on a super-dense vocabulary of trajectory samples (16,384 trajectories) covering a wide range of driving scenarios. To maximize generalization of fixed trajectory vocabularies, we propose a trajectory dropout training strategy. The idea is to deliberately create a mismatch between training and inference vocabularies---training the model to effectively generalize to unseen trajectory distributions during inference. (Sec. 2.2) Sensor Augmentation with Refinement (GTRS-Aug): To handle unexpected trajectory events and data distribution shifts in the form of viewpoint changes, we introduce a data augmentation strategy by applying rotation perturbations to sensor inputs, dramatically improving robustness to out-of-domain environments. Further, a refinement training mechanism enables the model to distinguish between subtly different trajectory options. (Sec. 2.3) GTRS demonstrates strong trajectory scoring abilities even under sub-optimal sensor conditions, as evaluated on the Navhard benchmark. Our contributions are as follows: We propose GTRS, a generalizable end-to-end multi-modal planning framework that combines diffusion-based trajectory generation with vocabulary scoring. With super-dense vocabularies, sensor augmentations, and refinement strategies, GTRS enables effective scoring across both dynamic and static candidates.

GTRS demonstrates superior planning performance and generalization to out-of-domain data on the Navhard benchmark. With model ensembling, our sensor-based GTRS---the winning entry of the Navsim v2 Challenge---approaches the performance of the state-of-the-art planner PDM-Closed, which operates on ground-truth perception and is unaffected by degraded sensor inputs.

Figure 1: The Three Pillars of GTRS.

## The Three Pillars of GTRS

### Trajectory Generator

To obtain high-quality dynamic trajectory proposals during inference, diffusion models have become a popular practice in autonomous driving for its ability to generate multi-modal trajectory candidates. We adopt a Diffusion Policy-based trajectory generator following to produce multiple trajectory proposals. This sub-network is composed of an image backbone to extract image features, a BEV encoder where BEV queries attend to image features through a Transformer Encoder, and a Diffusion Transformer that generates $N$ trajectory proposals $\mathcal{V}_{dp}$ conditioned on the BEV features.

During training, we follow Transfuser and include a BEV segmentation head to provide supervision on the BEV features. For the Diffusion Transformer, we apply first-order differentiation to the ground-truth trajectory waypoints to normalize the input and use the DDPM scheduling strategy for denoising ground-truth trajectories.

### Scorer with Vocabulary Generalization

While diffusion-based trajectory generators provide fine-grained trajectory proposals, they remain limited in their ability to capture the full breadth of possible driving scenarios. To achieve robust generalization, we introduce a novel vocabulary generalization technique that trains the model to effectively evaluate diverse trajectory distributions, even those not seen during training.

We propose the Generalized Vocabulary Scorer GTRS-Dense, which builds upon Hydra-MDP but introduces critical innovations in trajectory evaluation. The architecture consists of an image backbone, a trajectory tokenizer that encodes candidates into feature representations, and a Transformer Decoder that models complex interactions between trajectory and image tokens.

Our key innovation is twofold: First, we deliberately train on a super-dense trajectory vocabulary ($\mathcal{V}_{XL}$ with 16,384 distinct trajectories) that comprehensively covers the trajectory space, while inferencing on a smaller vocabulary ($\mathcal{V}_{L}$ with 8,192 trajectories)---forcing the model to develop generalizable representations. Second, we apply vocabulary dropout to $\mathcal{V}_{XL}$ during training, randomly removing half of the trajectories in each batch. This serves multiple purposes: it aligns the number of trajectory tokens during training and inference, it creates intentional distribution shifts that improve robustness, and it acts as an effective regularizer against overfitting to specific trajectory patterns.

This vocabulary generalization technique enables our model to effectively score both static trajectory vocabularies and dynamically generated proposals without requiring dedicated training on both types---a capability previous approaches have struggled to achieve.

Table 1: Roadmap to Generalized Trajectory Scoring. Random denotes that we randomly select a trajectory from 𝒱dp during inference. V2-99 is pretrained from DD3D, EVA-ViT-L is initialized from StreamPETR, and ViT-L is from Depth Anything.

Figure 2: The Inference Pipeline of GTRS.

### Sensor-augmented Scorer with Refinement

To further enhance model robustness across diverse and out-of-domain environments, we develop a systematic sensor augmentation strategy, along with a refinement training mechanism. This approach focuses on two critical challenges: handling perceptual distribution shifts in sensor data and distinguishing between subtly different trajectory options in safety-critical scenarios.

First, we introduce structured sensor perturbations by applying controlled 2D horizontal view rotations to the input images. Rather than random augmentation, these perturbations specifically target the model's ability to maintain consistent trajectory evaluation under varying viewing conditions. To maintain label consistency, we apply corresponding transformations to the ground-truths used for training.

Second, we develop a refinement training mechanism focused on fine-grained trajectory discrimination. As a training-only module, it incorporates an additional Transformer Decoder that progressively refines trajectory scores for the top-k most promising candidates, enabling the model to capture subtle differences between similar trajectories. The refinement process is guided by a self-distillation framework where an exponential moving average (EMA) copy of the model provides soft supervision signals: where ${\overset{\sim}{y}}_{i}^{m}$ represents the refined target score, ${\hat{y}}_{i}^{m}$ is the ground-truth score, and $s_{i,{teacher}}^{m}$ is the teacher model's prediction. The clipping parameter $\delta_{m}$ ensures the refined targets remain within a reasonable range of the ground truth.

Together, these strategies enable GTRS-Aug to perform robustly in challenging out-of-domain settings without domain-specific adaptation.

## Inference-time Integration

After training the sub-networks described above, we combine the trajectory generator and one of the trajectory scorers (*i.e*. GTRS-Dense, GTRS-Aug) during inference, as illustrated in Fig. 2. The dynamic proposals generated by the generator $\mathcal{V}_{dp}$ are appended to the inference vocabulary $\mathcal{V}_{L}$, and the combined set $\mathcal{V}_{dp} \cup \mathcal{V}_{L}$ is tokenized and scored by the scorer.

This sequential integration of dynamic proposals at inference time, rather than during training, is a deliberate design choice that leverages the strengths of both approaches. By training solely on a diverse static vocabulary, the scorer develops robust generalization abilities across a wide range of trajectory patterns. Then, at inference time, the diffusion-based generator provides fine-grained, context-aware trajectories specifically tailored to the current scene. Meanwhile, it avoids the computational overhead and potential instability of integrating diffusion sampling into the training loop, while still benefiting from the precision of dynamically generated trajectories during deployment.

Table 2: Performance on the Navhard Benchmark. Backbone settings follow Tab. 1. GTRS-E-Lite ensembles GTRS-Dense and GTRS-Aug with EVA-ViT-L. The challenge-winning entry GTRS-E ensembles all six models from GTRS-Dense and GTRS-Aug.

## Experiments

### Dataset and metrics

The Navsim dataset is designed for evaluating end-to-end driving systems, addressing prior limitations in benchmarking. The Navsim v2 Challenge introduces a new split, Navhard, which features difficult real-world scenarios alongside their synthetic continuations generated using 3DGS. Nevertheless, we observe that the synthetic data exhibits sub-optimal quality, which often contains artifacts such as distortion and blurring and may impair the performance of sensor-based planners. The Navsim v2 challenge evaluates end-to-end models based on the extended PDM Score (EPDMS), an extension of the PDM Score by aggregating multiple rule-based metrics ^11^1 Finally, it uses a two-stage scoring pipeline to aggregate the metrics on real-world data (Stage 1) and synthetic data (Stage 2).

### Implementation Details

We train all models on the Navtrain split with 24 NVIDIA A100 GPUs, while the Navhard split and other synthetic sensor data are not used for training. Training is conducted for 20 epochs with a total batch size of 528 by default, while the training lasts 50 epochs for the trajectory generator. The learning rate and weight decay are $2 \times 10^{- 4}$ and 0.0. We concatenate the frontal view with center-cropped front-left and front-right views to form the input image. For the trajectory generator DP, we formulate a similar input image from the back-view, back-right view, and back-left view for BEV construction. Finally, we use 100 denoising steps with the DDPM scheduler and generate 100 proposals in $\mathcal{V}_{dp}$.

### Roadmap to Generalized Trajectory Scoring

Trajectory Vocabulary Generalization. We evaluate GTRS-Dense with various inference vocabularies (Tab. 4.3). Notably, though it is trained only on the super-dense static vocabulary $\mathcal{V}_{XL}$, the scorer generalizes well to unseen dynamic proposals in $\mathcal{V}_{dp}$ (EPDMS: 36.7), demonstrating strong zero-shot generalization by outperforming the generator with random selection substantially (+ 11.1 EPDMS). When combining $\mathcal{V}_{dp}$ with $\mathcal{V}_{XL}$, performance improves by +1.1 EPDMS over $\mathcal{V}_{XL}$, confirming the complementary benefit of dynamic proposals at inference. Interestingly, $\mathcal{V}_{dp} \cup \mathcal{V}_{L}$ outperforms $\mathcal{V}_{dp} \cup \mathcal{V}_{XL}$, likely because the reduced vocabulary complexity leads to better generalization in out-of-domain synthetic data. Finally, applying dropout to $\mathcal{V}_{XL}$ during training yields the best performance (EPDMS: 43.4), showing that vocabulary dropout enhances generalization significantly.

Sensor Augmentation with Refinement. Finally, we evaluate GTRS-Aug, which incorporates sensor augmentation and refinement training. This model achieves the same top-level performance (EPDMS: 43.4) as the best GTRS-Dense variant, surpassing the baseline scorer by a large margin (+2.8 EPDMS). This confirms that augmentations and refinement training greatly improve trajectory scoring.

### Main Results

As shown in Tab. 2, our GTRS variants achieve significant improvements over the LTF baseline. By scaling the image backbone to ViT-L and EVA-ViT-L, our best single model achieves 45.3 EPDMS on the Navhard Benchmark. Further, GTRS-E-Lite, an ensemble of GTRS-Dense with GTRS-Aug during scoring, achieves 46.6 EPDMS. Our challenge-winning entry GTRS-E, an ensemble of all six variants, reaches 49.4 EPDMS, approaching the performance of PDM-Closed ---a privileged planner that relies on ground-truth perception---despite ours using challenging synthetic sensor input. This demonstrates the exceptional generalization capabilities of our approach across both trajectory distributions and perceptual domains.
