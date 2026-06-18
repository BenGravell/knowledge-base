RMP: A Random Mask Pretrain Framework for Motion Prediction

As the pretraining technique is growing in popularity, little work has been done on pretrained learning-based motion prediction methods in autonomous driving. In this paper, we propose a framework to formalize the pretraining task for trajectory prediction of traffic participants. Within our framework, inspired by the random masked model in natural language processing (NLP) and computer vision (CV), objects' positions at random timesteps are masked and then filled in by the learned neural network (NN). By changing the mask profile, our framework can easily switch among a range of motion-related tasks. We show that our proposed pretraining framework is able to deal with noisy inputs and improves the motion prediction accuracy and miss rate, especially for objects occluded over time by evaluating it on Argoverse and NuScenes datasets.

## Introduction

Accurately predicting the motion of road users is essential in autonomous driving systems. This predictive capability provides the planner with a forward-looking perspective on potential movements, thereby enhancing safety measures. While learning-based motion prediction has become increasingly popular in recent research, the exploration of pretraining and self-supervised learning within this field remains relatively limited.

The technique of random masking has demonstrated its effectiveness in various fields, such as natural language processing (NLP) and computer vision (CV), as evidenced by models like BERT and Masked Autoencoders in conjunction with Vision Transformers (ViT ). Random masking involves concealing a portion of the data (masking), and then tasking the neural network with predicting the hidden elements, thereby creating a nontrivial and beneficial self-supervisory task. This method employs an asymmetric encoder-decoder architecture, which has proven to be particularly powerful regarding training speed with large datasets....

## Conclusion

In this paper, we propose a simple and effective random mask pretraining framework which facilitates the motion prediction task in general and conditional motion prediction. Furthermore, our framework largely improves the prediction accuracy for occlusion scenarios. The self-supervised learning and masked autoencoder can be explored further with state-of-the-art techniques in the field of motion prediction for autonomous driving. Additionally, exploring new auxiliary tasks within the self-supervised learning domain offers exciting possibilities for further advancements....

### IV-A Network

## Problem Formulation

Figure 5: Qualitative results with our random mask pretrain framework.

Figure 1: Random Masking for Motion Data. We treat time-sequential data as one dimension and all agents in the scenario as another, with each cell representing the high-dimensional features of an agent (including position, heading, agent type, agent shape, etc.). Left: Motion prediction is a special case where all future timesteps are masked (shown in blue). Right: We apply random masking to a scenario, hiding patches for random agents and random time steps for pretraining. Ego stands for the ego autonomous vehicle.
