Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks

Topics include Object detection, Region proposal networks, Convolutional neural network, Two-stage detectors, Fast R-CNN, PASCAL VOC, COCO, Computer vision.

Introduces Region Proposal Networks as a learned, convolutional replacement for external proposal methods, letting proposals and Fast R-CNN detection share the same feature backbone. This made two-stage object detection substantially faster while improving accuracy, and became the reference architecture behind many later detection and instance-segmentation systems.

State-of-the-art object detection networks depend on region proposal algorithms to hypothesize object locations. Advances like SPPnet and Fast R-CNN have reduced the running time of these detection networks, exposing region proposal computation as a bottleneck. In this work, we introduce a Region Proposal Network (RPN) that shares full-image convolutional features with the detection network, thus enabling nearly cost-free region proposals. An RPN is a fully convolutional network that simultaneously predicts object bounds and objectness scores at each position. The RPN is trained end-to-end to generate high-quality region proposals, which are used by Fast R-CNN for detection. We further merge RPN and Fast R-CNN into a single network by sharing their convolutional features - using the recently popular terminology of neural networks with 'attention' mechanisms, the RPN component tells the unified network where to look. For the very deep VGG-16 model, our detection system has a frame rate of 5fps (including all steps) on a GPU, while achieving state-of-the-art object detection accuracy on PASCAL VOC 2007, 2012, and MS COCO datasets with only 300 proposals per image....

## Introduction

Recent advances in object detection are driven by the success of region proposal methods (*e.g*., ) and region-based convolutional neural networks (R-CNNs). Although region-based CNNs were computationally expensive as originally developed in, their cost has been drastically reduced thanks to sharing convolutions across proposals. The latest incarnation, Fast R-CNN, achieves near real-time rates using very deep networks, *when ignoring the time spent on region proposals*. Now, proposals are the test-time computational bottleneck in state-of-the-art detection systems.

Region proposal methods typically rely on inexpensive features and economical inference schemes. Selective Search, one of the most popular methods, greedily merges superpixels based on engineered low-level features. Yet when compared to efficient detection networks, Selective Search is an order of magnitude slower, at 2 seconds per image in a CPU implementation. EdgeBoxes currently provides the best tradeoff between proposal quality and speed, at 0.2 seconds per image. Nevertheless, the region proposal step still consumes as much running time as the detection network.

## Conclusion

We have presented RPNs for efficient and accurate region proposal generation. By sharing convolutional features with the down-stream detection network, the region proposal step is nearly cost-free. Our method enables a unified, deep-learning-based object detection system to run at near real-time frame rates. The learned RPN also improves region proposal quality and thus the overall object detection accuracy.

The anchor boxes that cross image boundaries need to be handled with care. During training, we ignore all cross-boundary anchors so they do not contribute to the loss. For a typical $1000 \times 600$ image, there will be roughly 20000 ($\approx {60 \times 40 \times 9}$) anchors in total. With the cross-boundary anchors ignored, there are about 6000 anchors per image for training. If the boundary-crossing outliers are not ignored in training, they introduce large, difficult to correct error terms in the objective, and training does not converge. During testing, however, we still apply the fully convolutional RPN to the entire image....

where $x$, $y$, $w$, and $h$ denote the box's center coordinates and its width and height....
