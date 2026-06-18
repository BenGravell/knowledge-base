Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network

Topics include Image super-resolution, Video super-resolution, Convolutional networks, Sub-pixel convolution, Pixel shuffle, Real-time inference, Low-resolution feature extraction, ESPCN.

ESPCN moves most computation into low-resolution feature space and performs learned upsampling with a sub-pixel convolution layer, making real-time 1080p super-resolution feasible. The sub-pixel or pixel-shuffle idea became a widely reused upsampling primitive in image and video restoration networks.

Recently, several models based on deep neural networks have achieved great success in terms of both reconstruction accuracy and computational performance for single image super-resolution. In these methods, the low resolution (LR) input image is upscaled to the high resolution (HR) space using a single filter, commonly bicubic interpolation, before reconstruction. This means that the super-resolution (SR) operation is performed in HR space. We demonstrate that this is sub-optimal and adds computational complexity. In this paper, we present the first convolutional neural network (CNN) capable of real-time SR of 1080p videos on a single K2 GPU. To achieve this, we propose a novel CNN architecture where the feature maps are extracted in the LR space. In addition, we introduce an efficient sub-pixel convolution layer which learns an array of upscaling filters to upscale the final LR feature maps into the HR output. By doing so, we effectively replace the handcrafted bicubic filter in the SR pipeline with more complex upscaling filters specifically trained for each feature map, whilst also reducing the computational complexity of the overall SR operation.

## Introduction

The recovery of a high resolution (HR) image or video from its low resolution (LR) counter part is topic of great interest in digital image processing. This task, referred to as super-resolution (SR), finds direct applications in many areas such as HDTV, medical imaging, satellite imaging, face recognition and surveillance. The global SR problem assumes LR data to be a low-pass filtered (blurred), downsampled and noisy version of HR data. It is a highly ill-posed problem, due to the loss of high-frequency information that occurs during the non-invertible low-pass filtering and subsampling operations.

Many methods assume multiple images are available as LR instances of the same scene with different perspectives, i.e. with unique prior affine transformations. These can be categorised as multi-image SR methods and exploit *explicit redundancy* by constraining the ill-posed problem with additional information and attempting to invert the downsampling process. However, these methods usually require computationally complex image registration and fusion stages, the accuracy of which directly impacts the quality of the result. An alternative family of methods are single image super-resolution (SISR) techniques.

## Conclusion

In this paper, we demonstrate that a non-adaptive upscaling at the first layer provides worse results than an adaptive upscaling for SISR and requires more computational complexity. To address the problem, we propose to perform the feature extraction stages in the LR space instead of HR space. To do that we propose a novel sub-pixel convolution layer which is capable of super-resolving LR data into HR space with very little additional computational cost compared to a deconvolution layer at training time.

## Future work

A reasonable assumption when processing video information is that most of a scene's content is shared by neighbouring video frames. Exceptions to this assumption are scene changes and objects sporadically appearing or disappearing from the scene. This creates additional data-implicit redundancy that can be exploited for video super-resolution as has been shown . Spatio-temporal networks are popular as they fully utilise the temporal information from videos for human action recognition.
