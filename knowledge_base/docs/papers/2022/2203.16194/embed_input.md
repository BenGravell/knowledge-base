FlowFormer: A Transformer Architecture for Optical Flow

Topics include Optical flow, FlowFormer, Transformers, Cost volume, Cost memory, Recurrent decoding, Dense matching.

FlowFormer brings transformer machinery directly to the 4D optical-flow cost volume by encoding it into a reusable cost memory and decoding flow with dynamic positional cost queries. It continues the RAFT lineage of iterative dense matching, but replaces much of the hand-shaped recurrent correlation logic with transformer-based cost-volume reasoning.

We introduce optical Flow transFormer, dubbed as FlowFormer, a transformer-based neural network architecture for learning optical flow. FlowFormer tokenizes the 4D cost volume built from an image pair, encodes the cost tokens into a cost memory with alternate-group transformer (AGT) layers in a novel latent space, and decodes the cost memory via a recurrent transformer decoder with dynamic positional cost queries. On the Sintel benchmark, FlowFormer achieves 1.159 and 2.088 average end-point-error (AEPE) on the clean and final pass, a 16.5% and 15.5% error reduction from the best published result (1.388 and 2.47). Besides, FlowFormer also achieves strong generalization performance. Without being trained on Sintel, FlowFormer achieves 1.01 AEPE on the clean pass of Sintel training set, outperforming the best published result (1.29) by 21.7%.

## Introduction

Optical flow targets at estimating per-pixel correspondences between a source image and a target image, in the form of a 2D displacement field. In many downstream video tasks, such as action recognition, video inpainting, video super-resolution, and frame interpolation, optical flow serves as a fundamental component providing dense correspondences as valuable clues for prediction.

A general assumption adopted in optical flow estimation is that the appearance of corresponding locations in the two images induced from optical flows remains unchanged. Traditionally, optical flow is modeled as an optimization problem that maximizes visual similarities between cross-image corresponding locations with regularization terms. With the rapid development of deep learning and emerging training data, this field has been significantly advanced by deep convolutional neural network-based methods. The recent methods compute costs (i.e. visual similarities) between feature pairs, upon which flows are regressed....

## Conclusion

We have proposed FlowFormer, a Transformer-based architecture for optical flow estimation. FlowFormer summarizes the $H \times W \times H \times W$ 4D cost volume built from a pair of images as $H \times W \times K$ tokens of length $D$, and then efficiently and effectively encodes the cost tokens via the alternate-group transformer (AGT). Thanks to such design, the generated cost memory is able to grasp essential information over the cost volume and obtain compact cost features....

The above self-attention operations' parameters are shared across different groups and they are sequentially operated to form the proposed alternate-group attention layer. By stacking the alternate-group transformer layer multiple times, the latent cost tokens can effectively exchange information across source pixels and across latent representations to better encode the 4D cost volume. In this way, our cost volume encoder transforms the $H \times W \times H \times W$ 4D cost volume to $H \times W \times K$ latent tokens of length $D$....

To tackle this challenging problem, we propose a transformer-based cost volume encoder that encodes the whole cost volume into a cost memory. Our cost volume encoder consists of three steps: 1) cost map patchification, 2) cost patch token embedding, and 3) cost memory encoding....
