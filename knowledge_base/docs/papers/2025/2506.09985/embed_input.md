V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning

Topics include Robotics, Large language models, Language models, Self-supervised learning, Supervised learning, Datasets, Accuracy, Planning, Learning, V-JEPA 2.

A major challenge for modern AI is to learn to understand the world and learn to act largely by observation. This paper explores a self-supervised approach that combines internet-scale video data with a small amount of interaction data (robot trajectories), to develop models capable of understanding, predicting, and planning in the physical world. We first pre-train an action-free joint-embedding-predictive architecture, V-JEPA 2, on a video and image dataset comprising over 1 million hours of internet video. V-JEPA 2 achieves strong performance on motion understanding (77.3 top-1 accuracy on Something-Something v2) and state-of-the-art performance on human action anticipation (39.7 recall-at-5 on Epic-Kitchens-100) surpassing previous task-specific models. Additionally, after aligning V-JEPA 2 with a large language model, we demonstrate state-of-the-art performance on multiple video question-answering tasks at the 8 billion parameter scale (e.g., 84.0 on PerceptionTest, 76.9 on TempCompass)....

## Introduction

Humans have the ability to adapt and generalize when taking on new tasks and operating in unfamiliar environments. Several cognitive learning theories suggest that humans learn an internal model of the world by integrating low-level sensory inputs to represent and predict future states, and they further posit that this world model shapes our perception at any given moment, playing a crucial role in informing our understanding of reality. Moreover, our ability to predict the effects of our actions on future states of the world is also essential for goal-oriented planning....

Figure 1: V-JEPA 2 Overview. Leveraging 1M hours of internet-scale video and 1M images, we pretrain the V-JEPA 2 video model using a visual mask denoising objective, and leverage this model for downstream tasks such as action classification, object recognition, action anticipation, and Video Question Answering by aligning the model with an LLM backbone....

Second, as mentioned in Section˜4, V-JEPA 2-AC currently relies upon tasks specified as image goals. Although this may be natural for some tasks, there are other situations where language-based goal specification may be preferable. Extending the V-JEPA 2-AC to accept language-based goals, e.g., by having a model that can embed language-based goals into the V-JEPA 2-AC representation space, is another important direction for future work. The results described in Section˜7, aligning V-JEPA 2 with a language model, may serve as a starting point.

Finally, in this work we scaled V-JEPA 2 models up to a modest 1B parameters. The results in Section˜2 demonstrated consistent performance improvements while scaling to this level. Previous work has investigated scaling vision encoders to as large as 20B parameters. Additional work is needed in this direction to develop scalable pre-training recipes that lead to sustained performance improvements with scale.

### Results

### Action-Conditioned World Model Training

Table 4: Action and Object Classification. We report the classification performance of V-JEPA 2 models pretrained on 64 frames at resolution 256 × 256 for all models, except V-JEPA 2 ViT-g384 which was pretrained at resolution 384 × 384, on action and object classification, and compare their performance with state-of-art image and video encoders....
