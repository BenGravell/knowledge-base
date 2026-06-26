<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Scaling down Deep Learning with MNIST-1D

Topics include Deep learning, Self-supervised learning, Supervised learning, Benchmarks, Learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Although deep learning models have taken on commercial and political relevance, key aspects of their training and operation remain poorly understood. This has sparked interest in science of deep learning projects, many of which require large amounts of time, money, and electricity. But how much of this research really needs to occur at scale? In this paper, we introduce MNIST-1D: a minimalist, procedurally generated, low-memory, and low-compute alternative to classic deep learning benchmarks. Although the dimensionality of MNIST-1D is only 40 and its default training set size only 4000, MNIST-1D can be used to study inductive biases of different deep architectures, find lottery tickets, observe deep double descent, metalearn an activation function, and demonstrate guillotine regularization in self-supervised learning. All these experiments can be conducted on a GPU or often even on a CPU within minutes, allowing for fast prototyping, educational use cases, and cutting-edge research on a low budget.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The deep learning analogue of Drosophila melanogaster is the MNIST dataset. Drosophila, the fruit fly, has a life cycle that is just a few days long, its nutritional needs are negligible, and it is easier to work with than mammals, especially humans. Like Drosophila, MNIST is easy to use: training a classifier on it takes only a few a minutes whereas training full-size vision and language models can take months of time and millions of dollars.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, despite its historical significance, MNIST has three notable shortcomings. First, it is too simple. Linear classifiers, fully-connected networks, and convolutional models all perform similarly well, obtaining above 90% accuracy (Table 1). This makes it hard to measure the contribution of a CNN's spatial priors or to judge the relative effectiveness of different regularization schemes. Second, it is too large. Each sample in MNIST is a $28\times 28$ image, resulting in 784 input dimensions. Together with its sample size $n=70\,000$, this requires an unnecessarily large amount of computation to perform a hyperparameter search or debug a metalearning loop. Third, it is hard to hack. MNIST is a fixed dataset and it is difficult to increase the sample size or to change the noise distribution. The ideal toy dataset should be procedurally generated to allow researchers to vary its parameters at will.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In order to address these shortcomings, we propose the MNIST-1D dataset (Figure 1). It is a minimalist, low-memory, and low-compute alternative to MNIST, designed for exploratory deep learning research where rapid prototyping and short latency are a priority. MNIST-1D has 40 dimensions, many fewer than MNIST's 784 or CIFAR's 3,072. The sample size can be arbitrarily large, but the frozen default dataset contains 4000 training and 1000 test samples, many fewer than the 70,000 in MNIST and 60,000 in CIFAR-10/100. Although our dataset is procedurally generated, its samples are intuitive enough for a human expert to match or even outperform a CNN.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

MNIST-1D does a much better job than the original MNIST at differentiating between model architectures: a linear classifier can only achieve 32% accuracy (Table 1), while a CNN reaches 94%. Below we show that MNIST-1D can be used to study phenomena ranging from deep double descent to self-supervised learning. Crucially, the experiments we present in this paper take only a few minutes to run on a single GPU (in some cases just a CPU) whereas they would require multiple GPU hours or even GPU days when using MNIST or CIFAR. This makes MNIST-1D valuable as a playground for quick initial experiments and invaluable for researchers without access to powerful GPUs.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

All our experiments are in Jupyter notebooks and are available at with direct links from figure captions. We provide a mnist1d package that can be installed via pip install mnist1d.

<!-- chunk {"id": "body-0008", "role": "body", "section": "The MNIST-1D dataset", "weight": 1.0} -->

Train/test split Gaussian filter width Gaussian noise scale White noise scale Final seq. length Table 2: Default parameters for MNIST-1D generation.

<!-- chunk {"id": "body-0009", "role": "body", "section": "The MNIST-1D dataset", "weight": 1.0} -->

Dimensionality. Our first design choice was to use one-dimensional time series instead of two-dimensional grayscale images or three-dimensional tensors corresponding to colored images. Our rationale was that one-dimensional signals require far less computation to train on but can be designed to have many of the same biases, distortions, and distribution shifts that are of interest to researchers studying fundamental deep learning questions.

<!-- chunk {"id": "body-0010", "role": "body", "section": "The MNIST-1D dataset", "weight": 1.0} -->

Constructing the dataset. We began with ten one-dimensional template patterns which resemble the digits 0--9 when plotted as in Figure 1. Each of these templates consisted of 12 hand-crafted $x$ coordinates. Next we padded the end of each sequence with 36--60 additional zero values, did a random circular shift by up to 48 indices, applied a random scaling, added Gaussian noise, and added a constant linear signal. We used Gaussian smoothing with $\sigma=2$ to induce spatial correlations. Finally, we downsampled the sequences to 40 data points that play the role of pixels in the resulting MNIST-1D (Figure 1). Table 2 gives the values of all the default hyperparameters used in these transformations.

<!-- chunk {"id": "body-0011", "role": "body", "section": "The MNIST-1D dataset", "weight": 1.0} -->

Implementation. Our goal was to make the code as simple, modular, and extensible as possible. The code for generating the dataset occupies two Python files and fits in a total of 150 lines. The get_dataset method has a simple API for changing dataset features such as maximum digit translation, correlated noise scale, shear scale, final sequence length, and more (Table 2). The following code snippet shows how to install the mnist1d package, choose a custom number of samples, and generate a dataset: [⬇](data:text/plain;base64,IyBpbnN0YWxsIHRoZSBwYWNrYWdlIGZyb20gUHlQSQojIHBpcCBpbnN0YWxsIG1uaXN0MWQKCmZyb20gbW5pc3QxZC5kYXRhIGltcG9ydCBtYWtlX2RhdGFzZXQKZnJvbSBtbmlzdDFkLmRhdGEgaW1wb3J0IGdldF9kYXRhc2V0X2FyZ3MKCmFyZ3MgPSBnZXRfZGF0YXNldF9hcmdzKCkgIyBkZWZhdWx0IHBhcmFtcwphcmdzLm51bV9zYW1wbGVzID0gMTBfMDAwCmRhdGEgPSBtYWtlX2RhdGFzZXQoYXJncykKeCwgeSA9IGRhdGFbIngiXSwgZGF0YVsieSJd){download=""} \# install the package from PyPI \# pip install mnist1d from mnist1d.data import make_dataset from mnist1d.data import get_dataset_args args = get_dataset_args \# default params args.num_samples = 10_000 data = make_dataset(args) The frozen dataset with $4000+1000$ samples can be found on GitHub as mnist1d_data.pkl.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Classification", "weight": 1.0} -->

For comparison, we also report the accuracy of a human expert (one of the authors) trained on the training set and evaluated (one-shot) on the test set. His accuracy was 96%. The purpose of this comparison was to show that MNIST-1D is a task that is as intuitive for humans as it is for machine learning models with spatial priors. This suggests that the models are not achieving high performance by exploiting some unintuitive statistical artifacts. Rather, they are using the relative position of various features associated with each 1-D digit. Interestingly, the CNN and the human expert had similar per-digit error rates (Figure S1).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Shuffling sanity check", "weight": 1.0} -->

We also trained the same models on a version of the dataset which was permuted along the spatial dimension. This 'shuffled' version measured each of the models' performances in the absence of local spatial structure. The test accuracy of CNNs and GRUs decreased by about 35 percentage points after shuffling whereas the MLP and logistic models performed about the same (Table 1, Figure 2). This makes sense, as the former two models have spatial and temporal locality priors whereas the latter two do not.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Science of deep learning with MNIST-1D", "weight": 1.0} -->

In this section we show how MNIST-1D can be used to explore empirical science of deep learning topics.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Lottery tickets and spatial inductive biases", "weight": 1.0} -->

Since the original paper was published, many works have sought to explain this phenomenon and then harness it on larger datasets and models. However, very few works have attempted to isolate a minimal working example of this effect so as to investigate it more carefully. We were able to demonstrate the existence of lottery tickets in a MLP classifier trained on MNIST-1D (Figure 4a--b). Lottery ticket subnetworks that we found performed better than random subnetworks with the same level of sparsity. Remarkably, even at high ($>$`<!-- -->`{=html}95%) rates of sparsity, the lottery tickets we found performed better than the original dense network.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Lottery tickets and spatial inductive biases", "weight": 1.0} -->

The asymptotic performance of lottery tickets with 92% sparsity was around 70% (Figure 4c). When we reversed all the 1D patterns in the dataset, effectively preserving the spatial structure but changing the actual locations of all features (analogous to flipping an image upside down), the original lottery tickets continued to perform at around 70% accuracy (Figure 4d). This suggests that the lottery tickets did not overfit to the original dataset; instead, something about their connectivity and initial weights gave them an inherent advantage over random sparse networks. This reproduces the findings of Morcos et al., which showed that lottery tickets can transfer between datasets.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Lottery tickets and spatial inductive biases", "weight": 1.0} -->

Next, we asked whether spatial inductive biases were a factor in the high performance of the lottery tickets we had found. To answer this question, we trained the same tickets on a feature-shuffled version of the MNIST-1D dataset. In other words, we permuted the feature indices in order to remove any spatial structure from the data. Shuffling greatly reduced the performance of the lottery tickets: they performed appreciably worse --- worse, in fact, than the original dense network (Figure 4e). This suggests that part of the lottery tickets' performance can be attributed to a spatial inductive bias in their sparse connectivity structure.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Lottery tickets and spatial inductive biases", "weight": 1.0} -->

Furthermore, on the original (non-shuffled) MNIST-1D, when we froze the sparsity patterns of lottery tickets but initialized them with different random weights, they still continued to outperform the original dense network (Figure 4f). This suggests that not the weight values but rather the sparsity patterns represent the spatial inductive bias of lottery tickets. We verified this hypothesis by measuring how often non-zero weights in a lottery ticket were adjacent to each other in the first layer of the model. The lottery tickets had more adjacent weights than expected by chance (Figure 4g), implying a bias towards local connectivity. See Figure S2 for a visualization of the actual sparsity patterns of several lottery tickets.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Lottery tickets and spatial inductive biases", "weight": 1.0} -->

The original lottery ticket paper, as well as some of the follow-up studies, required a large number of GPUs and multiple days of runtime. By contrast, all the experiments we presented here took around $\sim$`<!-- -->`{=html}30 minutes to complete on a single GPU.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Deep double descent", "weight": 1.0} -->

Despite the above intuition, many aspects of double descent, such as what factors affect its width and location, are not well understood. We argue that MNIST-1D is well suited for exploring these questions. We observed double descent when training a MLP classifier on MNIST-1D, varying the size of the single hidden layer. In the presence of 15% label noise, the test error peaked at the interpolation threshold (training error reaching zero), at around 50 neurons in the hidden layer (Figure 5b). Further increasing the model size led to the test error dropping again. Without label noise, the test error did not peak (Figure 5a). We observed qualitatively similar behavior using the CNN architecture (Figure 5c). The runtime of this experiment was $\sim$`<!-- -->`{=html}60 minutes on a CPU.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Gradient-based metalearning", "weight": 1.0} -->

The goal of metalearning is to learn how to learn. This can be implemented by having two levels of optimization: a fast inner optimization loop which corresponds to a traditional learning objective and a slow outer loop which updates some meta properties of the learning process. One of the simplest examples of metalearning is gradient-based hyperparameter optimization. This concept was proposed in Bengio and then scaled to deep learning models by Maclaurin et al.. The basic idea is to implement a fully differentiable training loop and then backpropagate through the entire process in order to optimize hyperparameters such as the learning rate or the weight decay.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Gradient-based metalearning", "weight": 1.0} -->

We implemented a metalearning optimization for an MLP classifier on MNIST-1D with an explicitly written inner optimization loop using SGD. The gradient-based hyperparameter optimization converges to the optimal learning rate to be 0.62 regardless of whether the initial learning rate is too high or too low (Figure 6). The whole optimization process took only one minute on a CPU.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Metalearning an activation function", "weight": 1.0} -->

The small size of MNIST-1D allows researchers to perform more challenging metalearning optimizations. For example, it permits the metalearning of an activation function --- something that to the best of our knowledge has not been studied before. We parameterized our classifier's activation function with a separate neural network (MLP with layer dimensionalities $1\to 100\to 100\to 1$ using tanh activations, with outputs added to an ELU function such that it could be trained to produce perturbations to the ELU shape) and then learned its weights using meta-gradients. The learned activation function substantially outperformed common nonlinearities such as ReLU, Elu, and Swish (Figure 7), achieving over 5 percentage points higher test accuracy. The resulting activation function had a non-monotonic shape with two local extrema (Figure 7).

<!-- chunk {"id": "body-0024", "role": "body", "section": "Metalearning an activation function", "weight": 1.0} -->

There has been work on optimizing activation functions, but none has used analytical gradients computed via nested optimization. Moreover, some of these prior experiments used multi-day training runs on large clusters of GPUs and TPUs, whereas our entire training took around 1 hour of CPU runtime.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Self-supervised learning", "weight": 1.0} -->

As shown in Table 1, logistic classification accuracy for MNIST-1D in pixel space was low (33%). A powerful approach to self-supervised representation learning in computer vision is to rely on data augmentations: each input image is augmented twice, forming 'positive pairs' which the network is trained to map to close locations in its output space while pushing away representations of other input images. In particular, in SimCLR, each positive pair is repulsed from all other positive pairs in the same mini-batch via the InfoNCE loss function.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Self-supervised learning", "weight": 1.0} -->

We implemented the SimCLR algorithm for MNIST-1D, using a network with three convolutional and two fully-connected layers ('projection head') with output dimensionality $16$. Our data augmentations consisted of regressing out the linear slope, circularly shifting by up to 10 pixels, and then reintroducing a random linear slope. We achieved 82% linear classification accuracy before the projection head in $\sim$`<!-- -->`{=html}1 minute of CPU training (for comparison, training SimCLR on CIFAR-10/100 datasets typically takes $\sim$`<!-- -->`{=html}10 GPU hours). In the output space, digits 0, 3, 6, and 8 appeared as isolated clusters (Figure 8a). Note that here we used both training and test sets of MNIST-1D for the self-supervised training, and the linear classifier was subsequently trained on the training set and evaluated on the test set.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Benchmarking pooling methods", "weight": 1.0} -->

With this in mind, we trained CNN models for MNIST-1D classification with different pooling methods and training set sizes. Note that here we make use of the procedural generation of MNIST-1D that allows one to generate additional samples at will. We found that, while pooling (but not striding!) was very effective in low-data regimes, it did not make much of a difference when more training data was available (Figure 9). We hypothesize that pooling is a poor-man architectural prior which is better than nothing with insufficient data but restricts model expression otherwise.

<!-- chunk {"id": "body-0028", "role": "body", "section": "When to scale", "weight": 1.0} -->

This paper is not an argument against large-scale machine learning research. That research has proven its worth and has come to represent one of the most exciting aspects of the ML research ecosystem. Rather, we wish to *promote* small-scale machine learning research. Neural networks do not have problems with scaling or performance --- but they do have problems with interpretability, reproducibility, and training speed. We see carefully-controlled, small-scale experiments as a great way to address these problems.

<!-- chunk {"id": "body-0029", "role": "body", "section": "When to scale", "weight": 1.0} -->

In fact, small-scale research is complimentary to large-scale research. As in biology, where fruit fly genetics helped guide the Human Genome Project, we believe that small-scale research should always have an eye on how to successfully scale. For example, several of the findings reported in this paper are at the point where they could be investigated at scale. It would be interesting to show that large-scale lottery tickets also learn spatial inductive biases and feature local connectivity. It would also be interesting to try metalearning an activation function on a larger model in order to find an activation that can outperform ReLU and Swish in practical deep learning systems.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Understanding vs. performance", "weight": 1.0} -->

There has been some debate over the relative value of understanding neural nets versus increasing their performance. Some researchers contend that a high-performing algorithm need not be interpretable as long as it saves lives or produces economic value. Others argue that hard-to-interpret deep learning models should not be deployed in sensitive real-world contexts until we understand them better. Both arguments have merit. However, we believe that the process of identifying things we do not understand about large-scale neural networks, reproducing them in toy settings like MNIST-1D, and then performing careful ablation studies to isolate their causal mechanisms is likely to improve both performance and interpretability in the long run.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Reducing environmental impact", "weight": 1.0} -->

There is hope that deep learning will have positive environmental applications. This may be true in the long run, but so far, artificial intelligence has done little to solve environmental problems. Deep learning models do, however, require massive amounts of electricity to train and deploy. Running experiments on smaller datasets --- and waiting to scale until one has a solid grasp of the phenomena involved --- is a good way to reduce the electricity costs and environmental impact of this research.

<!-- chunk {"id": "body-0032", "role": "body", "section": "The scaling down manifesto", "weight": 1.0} -->

We would like to provocatively suggest that in order to explore the limits of how large we can scale neural networks, we may need to explore the limits of how small we can scale them first. Scaling models and datasets down in a way that preserves the nuances of their behaviors will allow researchers to iterate more quickly on fundamental and creative ideas. This fast iteration cycle is the best way to obtain insights on how to incorporate progressively more complex inductive biases into our models. We can then transfer these inductive biases across scales in order to dramatically improve the sample efficiency and generalization of large models. The MNIST-1D dataset is a first step in that direction.
