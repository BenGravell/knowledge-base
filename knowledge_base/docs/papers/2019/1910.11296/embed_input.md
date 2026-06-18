Identifying Unknown Instances for Autonomous Driving

In the past few years, we have seen great progress in perception algorithms, particular through the use of deep learning. However, most existing approaches focus on a few categories of interest, which represent only a small fraction of the potential categories that robots need to handle in the real-world. Thus, identifying objects from unknown classes remains a challenging yet crucial task. In this paper, we develop a novel open-set instance segmentation algorithm for point clouds which can segment objects from both known and unknown classes in a holistic way. Our method uses a deep convolutional neural network to project points into a category-agnostic embedding space in which they can be clustered into instances irrespective of their semantics. Experiments on two large-scale self-driving datasets validate the effectiveness of our proposed method.

## Introduction

One relaxing summer weekend, I drove my family on an excursion to the zoo. All of a sudden, I saw a tiny black creature in front of my car. It was too far away for me to tell what it was, but as an experienced driver, I rolled out a series of moves without hesitation: I performed a shoulder check, I signaled, and then I switched lanes. In the end, I still had not figured out what it was until my daughter told me it was a raccoon crossing the street. The ability to recognize an object without knowing its semantics seems innate to us humans....

A common paradigm in robotics perception is to train and deploy a machine-learned model under the closed-set condition; *i.e*., the robot is only trained to identify instances from known classes. In this paper, we argue that this is not enough for a practical perception system, since in real-world applications, robots often have to operate in an open environment interacting with surrounding objects that were not seen during training. Thus, an ideal perception system should be capable of recognizing and localizing objects from both known and unknown classes. This is referred to as the open-set setting.

## Conclusion

We have presented a novel and effective open-set instance segmentation method for point clouds. In particular, we proposed a deep convolutional neural network to encode points into a category-agnostic embedding space in which they can be clustered into instances. As a result, our method is able to perceptually group points into instances, irrespective of whether they belong to a known or unknown class. We validate our method on two large-scale self-driving datasets and achieve state-of-the-art performance in the open-set setting....

Figure 3: Qualitative results of open-set instance segmentation on TOR4D and Rare4D.

### Backbone network

### Datasets

We are not the first to realize the importance of identifying and interacting with unknown instances. In the pioneering work by Saxena et al., the authors proposed to grasp a novel object by identifying good positions to grasp; this could be trained on known instances and then generalized to unknowns. Also, cognitive scientists have studied the underlying mechanism by which the human vision system detects novel objects....
