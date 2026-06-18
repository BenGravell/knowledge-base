Generalized Trajectory Scoring for End-to-End Multimodal Planning

Topics include Autonomous driving, End-to-end planning, Multimodal planning, Trajectory scoring, Generalization, Benchmarks.

Studies trajectory scoring as the selection layer for end-to-end multimodal driving planners, balancing static trajectory vocabularies and dynamic proposals. The paper is framed as a challenge-winning system contribution that improves generalization when choosing among diverse candidate futures.

End-to-end multi-modal planning is a promising paradigm in autonomous driving, enabling decision-making with diverse trajectory candidates. A key component is a robust trajectory scorer capable of selecting the optimal trajectory from these candidates. While recent trajectory scorers focus on scoring either large sets of static trajectories or small sets of dynamically generated ones, both approaches face significant limitations in generalization. Static vocabularies provide effective coarse discretization but struggle to make fine-grained adaptation, while dynamic proposals offer detailed precision but fail to capture broader trajectory distributions. To overcome these challenges, we propose GTRS (Generalized Trajectory Scoring), a unified framework for end-to-end multi-modal planning that combines coarse and fine-grained trajectory evaluation.

## Introduction

End-to-end multi-modal planning has emerged as a powerful approach in autonomous driving. Unlike traditional uni-modal planners that predict a single trajectory, multi-modal approaches generate multiple candidates, enabling greater adaptability during inference. This adaptability supports a wide range of applications, including responding to language instructions, accommodating different driving styles, and navigating complex driving environments.

The typical problem of end-to-end multi-modal planning involves evaluating multiple trajectory proposals through scoring given raw sensor data, without access to ground-truth perception. The planner selects the trajectory with the highest likelihood as the decision.

Current trajectory scoring methods generally fall into two categories: scoring a large static vocabulary, and scoring a small set of dynamically generated proposals. Both approaches face challenges in generalization. Fixed trajectory vocabularies offer limited flexibility, as they cannot adapt to situations where dynamic proposals are needed. Meanwhile, methods that rely on a small number of dynamic proposals often fail to generalize to unseen trajectories, since the scorer is only exposed to a narrow subset during training.

To address these limitations, we propose GTRS (Generalized Trajectory Scoring) for end-to-end multi-modal planning. GTRS is built on a key insight: an effective trajectory scorer must be trained on both coarse and fine-grained trajectory distributions to develop robust generalization capabilities. Our approach contains three complementary techniques, each leading to a dedicated sub-network as shown in Fig.:

Trajectory Vocabulary Generalization (GTRS-Dense): We train on a super-dense vocabulary of trajectory samples (16,384 trajectories) covering a wide range of driving scenarios. To maximize generalization of fixed trajectory vocabularies, we propose a trajectory dropout training strategy. The idea is to deliberately create a mismatch between training and inference vocabularies---training the model to effectively generalize to unseen trajectory distributions during inference. (Sec. 2.2)
