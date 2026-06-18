Going Deeper with Convolutions

Topics include Neural networks, Convolutional networks, Classification, Inception, Convolutional neural network, Network architecture.

We propose a deep convolutional neural network architecture codenamed "Inception", which was responsible for setting the new state of the art for classification and detection in the ImageNet Large-Scale Visual Recognition Challenge 2014. The main hallmark of this architecture is the improved utilization of the computing resources inside the network. This was achieved by a carefully crafted design that allows for increasing the depth and width of the network while keeping the computational budget constant. To optimize quality, the architectural decisions were based on the Hebbian principle and the intuition of multi-scale processing. One particular incarnation used in our submission for ILSVRC 2014 is called GoogLeNet, a 22 layers deep network, the quality of which is assessed in the context of classification and detection.

## Introduction

In the last three years, mainly due to the advances of deep learning, more concretely convolutional networks, the quality of image recognition and object detection has been progressing at a dramatic pace. One encouraging news is that most of this progress is not just the result of more powerful hardware, larger datasets and bigger models, but mainly a consequence of new ideas, algorithms and improved network architectures. No new data sources were used, for example, by the top entries in the ILSVRC 2014 competition besides the classification dataset of the same competition for detection purposes....

Another notable factor is that with the ongoing traction of mobile and embedded computing, the efficiency of our algorithms -- especially their power and memory use -- gains importance. It is noteworthy that the considerations leading to the design of the deep architecture presented in this paper included this factor rather than having a sheer fixation on accuracy numbers....

## Conclusions

Our results seem to yield a solid evidence that approximating the expected optimal sparse structure by readily available dense building blocks is a viable method for improving neural networks for computer vision. The main advantage of this method is a significant quality gain at a modest increase of computational requirements compared to shallower and less wide networks. Also note that our detection work was competitive despite of neither utilizing context nor performing bounding box regression and this fact provides further evidence of the strength of the Inception architecture....

All the convolutions, including those inside the Inception modules, use rectified linear activation. The size of the receptive field in our network is $224 \times 224$ taking RGB color channels with mean subtraction. "${\#3} \times 3$ reduce" and "${\#5} \times 5$ reduce" stands for the number of $1 \times 1$ filters in the reduction layer used before the $3 \times 3$ and $5 \times 5$ convolutions. One can see the number of $1 \times 1$ filters in the projection layer after the built-in max-pooling in the "pool proj" column. All these reduction/projection layers use rectified linear activation as well.

(b) Inception module with dimension reductions

## Training Methodology
