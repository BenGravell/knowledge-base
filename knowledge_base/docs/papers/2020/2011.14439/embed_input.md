Scaling down Deep Learning with MNIST-1D

Topics include Deep learning, Self-supervised learning, Supervised learning, Benchmarks, Learning.

Although deep learning models have taken on commercial and political relevance, key aspects of their training and operation remain poorly understood. This has sparked interest in science of deep learning projects, many of which require large amounts of time, money, and electricity. But how much of this research really needs to occur at scale? In this paper, we introduce MNIST-1D: a minimalist, procedurally generated, low-memory, and low-compute alternative to classic deep learning benchmarks. Although the dimensionality of MNIST-1D is only 40 and its default training set size only 4000, MNIST-1D can be used to study inductive biases of different deep architectures, find lottery tickets, observe deep double descent, metalearn an activation function, and demonstrate guillotine regularization in self-supervised learning. All these experiments can be conducted on a GPU or often even on a CPU within minutes, allowing for fast prototyping, educational use cases, and cutting-edge research on a low budget.

## Introduction

The deep learning analogue of Drosophila melanogaster is the MNIST dataset. Drosophila, the fruit fly, has a life cycle that is just a few days long, its nutritional needs are negligible, and it is easier to work with than mammals, especially humans. Like Drosophila, MNIST is easy to use: training a classifier on it takes only a few a minutes whereas training full-size vision and language models can take months of time and millions of dollars (Sharir et al., ).

Figure 1: Constructing the MNIST-1D dataset. Unlike MNIST, each sample is a one-dimensional sequence. To generate each sample, we begin with a hand-crafted digit template loosely inspired by MNIST shapes. Then we randomly pad, translate, and add noise to produce 1D sequences with 40 points each. [CODE]

### The scaling down manifesto

We would like to provocatively suggest that in order to explore the limits of how large we can scale neural networks, we may need to explore the limits of how small we can scale them first. Scaling models and datasets down in a way that preserves the nuances of their behaviors will allow researchers to iterate more quickly on fundamental and creative ideas. This fast iteration cycle is the best way to obtain insights on how to incorporate progressively more complex inductive biases into our models....

It is not unusual for deep learning models to have many times more parameters than necessary to perfectly fit the training set (Prince, ). This overparameterization helps training but increases computational overhead. One solution is to progressively prune weights from a model during training so that the final network is just a fraction of its original size. Although this approach works, conventional wisdom holds that sparse networks do not train well from scratch. Recent work by Frankle and Carbin challenges this conventional wisdom....

The frozen dataset with $4000 + 1000$ samples can be found on GitHub as mnist1d_data.pkl.

Figure 6: Metalearning the learning rate of SGD optimization of an MLP classifier on MNIST-1D. The outer training converges to the optimal learning rate of 0.62 regardless of whether the initial learning rate is too high or too low. Runtime: ∼1 minute. [CODE]

But in spite of their small size, both test systems have had a major impact on their respective fields....
