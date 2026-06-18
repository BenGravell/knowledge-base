FlowFormer: A Transformer Architecture for Optical Flow

Topics include Optical flow, FlowFormer, Transformers, Cost volume, Cost memory, Recurrent decoding, Dense matching.

FlowFormer brings transformer machinery directly to the 4D optical-flow cost volume by encoding it into a reusable cost memory and decoding flow with dynamic positional cost queries. It continues the RAFT lineage of iterative dense matching, but replaces much of the hand-shaped recurrent correlation logic with transformer-based cost-volume reasoning.

We introduce optical Flow transFormer, dubbed as FlowFormer, a transformer-based neural network architecture for learning optical flow. FlowFormer tokenizes the 4D cost volume built from an image pair, encodes the cost tokens into a cost memory with alternate-group transformer (AGT) layers in a novel latent space, and decodes the cost memory via a recurrent transformer decoder with dynamic positional cost queries. On the Sintel benchmark, FlowFormer achieves 1.159 and 2.088 average end-point-error (AEPE) on the clean and final pass, a 16.5% and 15.5% error reduction from the best published result (1.388 and 2.47). Besides, FlowFormer also achieves strong generalization performance. Without being trained on Sintel, FlowFormer achieves 1.01 AEPE on the clean pass of Sintel training set, outperforming the best published result (1.29) by 21.7%.

## Introduction

Optical flow targets at estimating per-pixel correspondences between a source image and a target image, in the form of a 2D displacement field. In many downstream video tasks, such as action recognition, video inpainting, video super-resolution, and frame interpolation, optical flow serves as a fundamental component providing dense correspondences as valuable clues for prediction.

A naive strategy to transform the 4D cost volume with transformers is directly tokenizing the 4D cost volume and applying transformers. However, such a strategy needs to use thousands of tokens, which is computationally unbearable. To tackle this challenge, we propose two key designs in our cost encoder. We propose a two-step tokenization: 1) converting each of the 2D cost maps, which records visual similarities between one source pixel and all target pixels, from the 4D cost volume into patches as commonly done in transformer networks, and 2) further projecting cost-map patches of each cost map into $K$ latent cost tokens.

Our contributions can be summarized as fourfold. 1) We propose a novel transformer-based neural network architecture, FlowFormer, for optical flow estimation, which achieves state-of-the-art flow estimation performance. 2) We design a novel cost volume encoder, effectively aggregating cost information into compact latent cost tokens. 3) We propose a recurrent cost decoder that recurrently decodes cost features with dynamic positional cost queries to iteratively refine the estimated optical flows. 4) To the best of our knowledge, we validate for the first time that an ImageNet-pretrained transformer can benefit the estimation of optical flow.

## Conclusion

We have proposed FlowFormer, a Transformer-based architecture for optical flow estimation. FlowFormer summarizes the $H \times W \times H \times W$ 4D cost volume built from a pair of images as $H \times W \times K$ tokens of length $D$, and then efficiently and effectively encodes the cost tokens via the alternate-group transformer (AGT). Thanks to such design, the generated cost memory is able to grasp essential information over the cost volume and obtain compact cost features.
