Revisiting Feature Prediction for Learning Visual Representations from Video

Topics include Supervised learning, Unsupervised learning, Datasets, Learning, V-JEPA.

This paper explores feature prediction as a stand-alone objective for unsupervised learning from video and introduces V-JEPA, a collection of vision models trained solely using a feature prediction objective, without the use of pretrained image encoders, text, negative examples, reconstruction, or other sources of supervision. The models are trained on 2 million videos collected from public datasets and are evaluated on downstream image and video tasks. Our results show that learning by predicting video features leads to versatile visual representations that perform well on both motion and appearance-based tasks, without adaption of the model's parameters; e.g., using a frozen backbone. Our largest model, a ViT-H/16 trained only on videos, obtains 81.9% on Kinetics-400, 72.2% on Something-Something-v2, and 77.9% on ImageNet1K.

## Introduction

Humans possess the remarkable ability to map low-level signals originating from the retina into a semantic spatio-temporal understanding of the world; synthesizing notions such as objects and global motion. A long-standing goal of the machine learning community is to identify the principles or objectives that may guide such unsupervised learning in humans (Field Berkes and Wiskott Hinton, ). One related hypothesis is based on the *predictive feature principle*, which posits that representations of temporally adjacent sensory stimuli should be predictive of each other.

Figure 1: V-JEPA models pretrained on video learn versatile visual representations. It performs well on motion-based tasks (Something-Something-v2) and appearance-based tasks (Kinetics 400) without adaptation of the model’s parameters, i.e., using the same frozen backbone for both tasks.

## Conclusion

In this work, we explored the effectiveness of feature prediction as a stand-alone objective for unsupervised learning from video and introduced V-JEPA, a collection of vision models trained solely using a self-supervised feature prediction objective. The V-JEPA models demonstrate the ability to solve various downstream image and video tasks without adaption of the model parameters, and outperform previous video representation learning approaches in frozen evaluation on action recognition, spatio-temporal action detection, and image classification tasks....

We first ablate the effect of computing the prediction loss in representation space. We train a pair of ViT-L/16 models using either a V-JEPA feature prediction loss, or a mean-squared error loss with the normalized pixel values, as in masked autoencoders, and perform a sweep over the learning rate and weight decay schedules for both approaches. All models are pretrained on VideoMix2M for 90K iterations with a batch size of 3072 using multi-block masking....

Figure 3: V-JEPA. Training operates on a video clip of T frames with spatial resolution H × W, flattened into a sequence of L tokens. (Left to right): We first obtain the input of the x-encoder by dropping tokens from the video clip. The x-encoder then processes the masked video sequence, and outputs an embedding vector for each input token....
