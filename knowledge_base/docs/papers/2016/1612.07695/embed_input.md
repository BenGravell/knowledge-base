MultiNet: Real-time Joint Semantic Reasoning for Autonomous Driving

While most approaches to semantic reasoning have focused on improving performance, in this paper we argue that computational times are very important in order to enable real time applications such as autonomous driving. Towards this goal, we present an approach to joint classification, detection and semantic segmentation via a unified architecture where the encoder is shared amongst the three tasks. Our approach is very simple, can be trained end-to-end and performs extremely well in the challenging KITTI dataset, outperforming the state-of-the-art in the road segmentation task. Our approach is also very efficient, taking less than 100 ms to perform all tasks.

## Introduction

Current advances in the field of computer vision have made clear that visual perception is going to play a key role in the development of self-driving cars. This is mostly due to the deep learning revolution which begun with the introduction of AlexNet in 2012. Since then, the accuracy of new approaches has been increasing at a vertiginous rate. Causes of this are the existence of more data, increased computation power and algorithmic developments. The current trend is to create deeper networks with as many layers as possible.

While performance is already extremely high, when dealing with real-world applications, running times becomes important. New hardware accelerators as well as compression, reduced precision and distillation methods have been exploited to speed up current networks.

In this paper we take an alternative approach and design a network architecture that can very efficiently perform classification, detection and semantic segmentation simultaneously. This is done by incorporating all three task into a unified encoder-decoder architecture. We name our approach MultiNet.

We demonstrate the effectiveness of our approach in the challenging KITTI benchmark and show state-of-the-art performance in road segmentation. Importantly, our ROI-align implementation can significantly improve detection performance without requiring an explicit proposal generation network. This gives our decoder a significant speed advantage compared to Faster-RCNN. Our approach is able to benefit from sharing computations, allowing us to perform inference in less than 45 ms for all tasks.

## Conclusion

In this paper we have developed a unified deep architecture which is able to jointly reason about classification, detection and semantic segmentation. Our approach is very simple, can be trained end-to-end and performs extremely well in the challenging KITTI dataset, outperforming the state-of-the-art in the road segmentation task. Our approach is also very efficient, taking $42.48\ \frac{ms}{}$ to perform all tasks. In the future we plan to exploit compression methods in order to further reduce the computational bottleneck and energy consumption of MutiNet.
