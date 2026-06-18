V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning

Topics include Robotics, Large language models, Language models, Self-supervised learning, Supervised learning, Datasets, Accuracy, Planning, Learning, V-JEPA 2.

A major challenge for modern AI is to learn to understand the world and learn to act largely by observation. This paper explores a self-supervised approach that combines internet-scale video data with a small amount of interaction data (robot trajectories), to develop models capable of understanding, predicting, and planning in the physical world. We first pre-train an action-free joint-embedding-predictive architecture, V-JEPA 2, on a video and image dataset comprising over 1 million hours of internet video. V-JEPA 2 achieves strong performance on motion understanding (77.3 top-1 accuracy on Something-Something v2) and state-of-the-art performance on human action anticipation (39.7 recall-at-5 on Epic-Kitchens-100) surpassing previous task-specific models. Additionally, after aligning V-JEPA 2 with a large language model, we demonstrate state-of-the-art performance on multiple video question-answering tasks at the 8 billion parameter scale (e.g., 84.0 on PerceptionTest, 76.9 on TempCompass).

## Introduction

Humans have the ability to adapt and generalize when taking on new tasks and operating in unfamiliar environments. Several cognitive learning theories suggest that humans learn an internal model of the world by integrating low-level sensory inputs to represent and predict future states, and they further posit that this world model shapes our perception at any given moment, playing a crucial role in informing our understanding of reality. Moreover, our ability to predict the effects of our actions on future states of the world is also essential for goal-oriented planning.

In this work, we build upon the self-supervised hypothesis as a means to learn world models that capture background knowledge of the world largely from observation. Specifically, we leverage the joint-embedding predictive architecture (JEPA), which learns by making predictions in a learned representation space.

Our approach, V-JEPA 2, utilizes a stage-wise training procedure, beginning with action-free pre-training on internet-scale video, followed by post-training with a small amount of interaction data (see Figure˜1). In the first stage, we use a mask-denoising feature prediction objective, where the model predicts masked segments of a video in a learned representation space. We train the V-JEPA 2 encoder with up to 1 billion parameters and with more than 1 million hours of video.

To summarize, we show that joint-embedding predictive architectures learning from videos can be used to build a world model that enables *understanding* the physical world, *predicting* future states, and effectively *planning* in new situations; this is achieved by leveraging internet-scale video and a small amount of interaction data.

## Limitations

V-JEPA 2 and the EK100 benchmark have several limitations. First, V-JEPA 2 does not fully solve EK100, there are failure cases where the model either gets the verb, the noun, or both wrong. We study the distribution of these failures in Section˜13.2. Second, we focus here on predicting actions with a 1 second anticipation time. The accuracy of V-JEPA 2 degrades when predicting at longer time horizons, see Section˜13.2. Third, the EK100 benchmark is limited to kitchen environments, with a closed well-defined vocabulary, and we do not know how well V-JEPA 2 generalizes to other environments.
