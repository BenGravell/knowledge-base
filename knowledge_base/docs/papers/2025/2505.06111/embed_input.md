UniVLA: Learning to Act Anywhere with Task-Centric Latent Actions

Topics include Vision-language-action models, Latent actions, Robot learning, Cross-embodiment learning, Video learning, Generalist robots.

Introduces UniVLA, a cross-embodiment vision-language-action policy that derives task-centric latent actions from videos before grounding them in robot-specific controls. The paper is useful for separating transferable task intent from embodiment-specific action spaces in generalist robot learning.

A generalist robot should perform effectively across various environments. However, most existing approaches heavily rely on scaling action-annotated data to enhance their capabilities. Consequently, they are often limited to single physical specification and struggle to learn transferable knowledge across different embodiments and environments. To confront these limitations, we propose UniVLA, a new framework for learning cross-embodiment vision-language-action (VLA) policies. Our key innovation is to derive task-centric action representations from videos with a latent action model. This enables us to exploit extensive data across a wide spectrum of embodiments and perspectives. To mitigate the effect of task-irrelevant dynamics, we incorporate language instructions and establish a latent action model within the DINO feature space. Learned from internet-scale videos, the generalist policy can be deployed to various robots through efficient latent action decoding. We obtain state-of-the-art results across multiple manipulation and navigation benchmarks, as well as real-robot deployments....

## Introduction

Empowered by the emergence of large-scale robotic datasets, robot policies based on vision-language-action models (VLA) have made encouraging strides recently. However, they typically rely on ground-truth action labels for supervision, which limits their scalability in utilizing internet-scale data from diverse environments. Furthermore, the heterogeneity of action and observation spaces across different embodiments (*e.g*., Franka, WidowX, and even human hands) and tasks (*e.g*., manipulation and navigation) poses a significant challenge to effective knowledge transfer....

To address these challenges, we propose UniVLA, a generalist policy learning framework that enables scalable and efficient planning across various embodiments and environments. Much like large language models (LLMs) learn cross-lingual shared knowledge, we aim to construct a unified action space that facilitates knowledge transfer across video data, including various robot demonstrations and egocentric human videos. Our recipe for generalist policy consists of three key stages: 1) Task-centric Latent Action Learning, where we extract task-relevant action representations from massive cross-embodiment videos in an unsupervised manner....

### In-context learning

capability is critical for enhancing the performance ceiling of vision-language-action models. Given our finding that the proposed latent action model can extract transferable motion representations bridging human and robotic manipulations, we propose encoding human demonstration videos into a sequence of compact latent action embeddings, serving as in-context samples (conceptually, the latent action model functions as a video tokenizer). This approach enables zero-shot skill acquisition without additional fine-tuning. We will explore this direction in future work.

MDT \[\] leverages diffusion models to generate flexible action sequences conditioned by multimodal goals.

### Learn from history outputs

Spatial Awareness: Pick up the screwdriver to put it into the cabinet and close the door ("Store the screwdriver").

While recent studies have investigated the viability of learning latent actions from web-scale videos, they suffer from a critical limitation: their naive reconstruction-based objectives often capture task-irrelevant dynamics, such as movements of non-ego agents or unpredictable camera shifts....
