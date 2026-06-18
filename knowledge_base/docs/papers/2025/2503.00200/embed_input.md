Unified Video Action Model

Topics include Vision-language-action models, Video prediction, Robot learning, Action prediction, Unified models, Robotics.

Proposes a unified video-action model that jointly predicts future video and robot actions, using each signal to improve the other. The paper is relevant for robotics world-model and policy-learning work because it tries to combine generative scene understanding with efficient action prediction in one architecture.

A unified video and action model holds significant promise for robotics, where videos provide rich scene information for action prediction, and actions provide dynamics information for video prediction. However, effectively combining video generation and action prediction remains challenging, and current video generation-based methods struggle to match the performance of direct policy learning in action accuracy and inference speed. To bridge this gap, we introduce the Unified Video Action model (UVA), which jointly optimizes video and action predictions to achieve both high accuracy and efficient action inference. The key lies in learning a joint video-action latent representation and decoupling video-action decoding. The joint latent representation bridges the visual and action domains, effectively modeling the relationship between video and action sequences. Meanwhile, the decoupled decoding, powered by two lightweight diffusion heads, enables high-speed action inference by bypassing video generation during inference. Such a unified framework further enables versatile functionality through masked input training.

## Introduction

A unified video and action model that jointly learns an agent's actions and their effects on visual observations holds great promise for robotics -- videos provide rich environmental context for predicting actions, while actions reveal how interactions drive visual changes, enabling more accurate modeling of real-world dynamics. However, despite its promise, previous approaches have often failed to fully realize this potential. A key challenge lies in the inherent mismatch between the requirements of action and video generation.

To address these limitations, we propose UVA, a Unified Video and Action Model designed to simultaneously model videos and actions -- capturing the underlying interactions between visuals and actions to enhance task understanding, while maintaining high-speed action prediction during inference.

We evaluate UVA on seven publicly available benchmarks to assess its diverse capabilities. UVA outperforms or matches state-of-the-art approaches, demonstrating particularly strong performance in multi-task settings. For instance, UVA outperforms the best baseline by 20% in success rate on PushT Multitask and by 5%. The experiments show that UVA can serve as a general-purpose framework for different robotics tasks without compromising performance compared to methods tailored for specific applications.

## Discussion

We propose a unified video-action model that jointly models and separately decodes video and actions. This design enables us to fully leverage video data as additional supervision, resulting in stronger performance and fast action prediction by skipping video decoding during inference. The framework inherently supports masking training, allowing it to fulfill various robotics functions, including acting as a policy, video model, forward and inverse dynamics model, and a combined policy and planner.

One limitation of our framework is that it does not currently leverage large amounts of actionless video data, which could provide valuable additional supervision. As a result, our method occasionally achieves only comparable performance to the DP-UMI on real-world tasks. We believe that pretraining the model on web-scale video datasets could significantly enhance its generalization capabilities, and we leave this exploration for future work.
