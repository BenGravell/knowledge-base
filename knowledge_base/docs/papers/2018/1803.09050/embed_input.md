<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning to Reweight Examples for Robust Deep Learning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Deep neural networks have been shown to be very powerful modeling tools for many supervised learning tasks involving complex input patterns. However, they can also easily overfit to training set biases and label noises. In addition to various regularizers, example reweighting algorithms are popular solutions to these problems, but they require careful tuning of additional hyperparameters, such as example mining schedules and regularization hyperparameters. In contrast to past reweighting methods, which typically consist of functions of the cost value of each example, in this work we propose a novel meta-learning algorithm that learns to assign weights to training examples based on their gradient directions. To determine the example weights, our method performs a meta gradient descent step on the current mini-batch example weights (which are initialized from zero) to minimize the loss on a clean unbiased validation set. Our proposed method can be easily implemented on any type of deep network, does not require any additional hyperparameter tuning, and achieves impressive performance on class imbalance and corrupted label problems where only a small amount of clean validation data is available.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Deep neural networks (DNNs) have been widely used for machine learning applications due to their powerful capacity for modeling complex input patterns. Despite their success, it has been shown that DNNs are prone to training set biases, i.e. the training set is drawn from a joint distribution $p{(x,y)}$ that is different from the distribution $p{(x^{v},y^{v})}$ of the evaluation set. This distribution mismatch could have many different forms. Class imbalance in the training set is a very common example. In applications such as object detection in the context of autonomous driving, the vast majority of the training data is composed of standard vehicles but models also need to recognize rarely seen classes such as emergency vehicles or animals with very high accuracy. This will sometime lead to biased training models that do not perform well in practice.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Another popular type of training set bias is label noise. To train a reasonable supervised deep model, we ideally need a large dataset with high-quality labels, which require many passes of expensive human quality assurance (QA). Although coarse labels are cheap and of high availability, the presence of noise will hurt the model performance, e.g. Zhang et al. has shown that a standard CNN can fit any ratio of label flipping noise in the training set and eventually leads to poor generalization performance.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Training set biases and misspecification can sometimes be addressed with dataset resampling, i.e. choosing the correct proportion of labels to train a network, or more generally by assigning a weight to each example and minimizing a weighted training loss. The example weights are typically calculated based on the training loss, as in many classical algorithms such as AdaBoost, hard negative mining, self-paced learning, and other more recent work.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, there exist two contradicting ideas in training loss based approaches. In noisy label problems, we prefer examples with smaller training losses as they are more likely to be clean images; yet in class imbalance problems, algorithms such as hard negative mining prioritize examples with higher training loss since they are more likely to be the minority class. In cases when the training set is both imbalanced and noisy, these existing methods would have the wrong model assumptions. In fact, without a proper definition of an unbiased test set, solving the training set bias problem is inherently ill-defined. As the model cannot distinguish the right from the wrong, stronger regularization can usually work surprisingly well in certain synthetic noise settings. Here we argue that in order to learn general forms of training set biases, it is necessary to have a small unbiased validation to guide training. It is actually not uncommon to construct a dataset with two parts - one relatively small but very accurately labeled, and another massive but coarsely labeled. Coarse labels can come from inexpensive crowdsourcing services or weakly supervised data.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Different from existing training loss based approaches, we follow a meta-learning paradigm and model the most basic assumption instead: the best example weighting should minimize the loss of a set of unbiased clean validation examples that are consistent with the evaluation procedure. Traditionally, validation is performed at the end of training, which can be prohibitively expensive if we treat the example weights as some hyperparameters to optimize; to circumvent this, we perform validation at every training iteration to dynamically determine the example weights of the current batch. Towards this goal, we propose an online reweighting method that leverages an additional small validation set and adaptively assigns importance weights to examples in every iteration. We experiment with both class imbalance and corrupted label problems and find that our approach significantly increases the robustness to training set biases.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Learning to Reweight Examples", "weight": 1.0} -->

In this section, we derive our model from a meta-learning objective towards an online approximation that can fit into any regular supervised training. We give a practical implementation suitable for any deep network type and provide theoretical guarantees under mild conditions that our algorithm has a convergence rate of $O{({1/\epsilon^{2}})}$. Note that this is the same as that of stochastic gradient descent (SGD).

<!-- chunk {"id": "body-0009", "role": "body", "section": "From a meta-learning objective to an online approximation", "weight": 1.0} -->

Let $(x,y)$ be an input-target pair, and $\{{{{(x_{i},y_{i})},1} \leq i \leq N}\}$ be the training set. We assume that there is a small unbiased and clean validation set $\{{{{(x_{i}^{v},y_{i}^{v})},1} \leq i \leq M}\}$, and $M \ll N$. Hereafter, we will use superscript $v$ to denote validation set and subscript $i$ to denote the $i^{th}$ data. We also assume that the training set contains the validation set; otherwise, we can always add this small validation set into the training set and leverage more information during training.

<!-- chunk {"id": "body-0010", "role": "body", "section": "From a meta-learning objective to an online approximation", "weight": 1.0} -->

Let $\Phi{(x,\theta)}$ be our neural network model, and $\theta$ be the model parameters. We consider a loss function $C{(\hat{y},y)}$ to minimize during training, where $\hat{y} = {\Phi{(x,\theta)}}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "From a meta-learning objective to an online approximation", "weight": 1.0} -->

In standard training, we aim to minimize the expected loss for the training set: ${\frac{1}{N}{\sum_{i = 1}^{N}{C{({\hat{y}}_{i},y_{i})}}}} = {\frac{1}{N}{\sum_{i = 1}^{N}{f_{i}{(\theta)}}}}$, where each input example is weighted equally, and $f_{i}{(\theta)}$ stands for the loss function associating with data $x_{i}$. Here we aim to learn a reweighting of the inputs, where we minimize a weighted loss: with $w_{i}$ unknown upon beginning.

<!-- chunk {"id": "body-0012", "role": "body", "section": "From a meta-learning objective to an online approximation", "weight": 1.0} -->

Note that ${\{ w_{i}\}}_{i = 1}^{N}$ can be understood as training hyperparameters, and the optimal selection of $w$ is based on its validation performance: It is necessary that $w_{i} \geq 0$ for all $i$, since minimizing the negative training loss can usually result in unstable behavior.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Online approximation", "weight": 1.0} -->

Calculating the optimal $w_{i}$ requires two nested loops of optimization, and every single loop can be very expensive. The motivation of our approach is to adapt online $w$ through a single optimization loop. For each training iteration, we inspect the descent direction of some training examples locally on the training loss surface and reweight them according to their similarity to the descent direction of the validation loss surface.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Online approximation", "weight": 1.0} -->

For most training of deep neural networks, SGD or its variants are used to optimize such loss functions. At every step $t$ of training, a mini-batch of training examples $\{{{{(x_{i},y_{i})},1} \leq i \leq n}\}$ is sampled, where $n$ is the mini-batch size, $n \ll N$. Then the parameters are adjusted according to the descent direction of the expected loss on the mini-batch. Let's consider vanilla SGD: where $\alpha$ is the step size.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Online approximation", "weight": 1.0} -->

We want to understand what would be the impact of training example $i$ towards the performance of the validation set at training step $t$. Following a similar analysis to Koh & Liang, we consider perturbing the weighting by $\epsilon_{i}$ for each training example in the mini- batch, We can then look for the optimal $\epsilon^{\ast}$ that minimizes the validation loss $f^{v}$ locally at step $t$: Unfortunately, this can still be quite time-consuming. To get a cheap estimate of $w_{i}$ at step $t$, we take a single gradient descent step on a mini-batch of validation samples wrt. $\epsilon_{t}$, and then rectify the output to get a non-negative weighting: where $\eta$ is the descent step size on $\epsilon$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Online approximation", "weight": 1.0} -->

To match the original training step size, in practice, we can consider normalizing the weights of all examples in a training batch so that they sum up to one. In other words, we choose to have a hard constraint within the set ${\{ w:{{\parallel w\parallel}_{1} = 1}\}} \cup {\{ 0\}}$. where $\delta{(\cdot)}$ is to prevent the degenerate case when all $w_{i}$'s in a mini-batch are zeros, i.e. ${\delta{(a)}} = 1$ if $a = 0$, and equals to $0$ otherwise. Without the batch-normalization step, it is possible that the algorithm modifies its effective learning rate of the training progress, and our one-step look ahead may be too conservative in terms of the choice of learning rate. Moreover, with batch normalization, we effectively cancel the meta learning rate parameter $\eta$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Example: learning to reweight examples in a multi-layer perceptron network", "weight": 1.0} -->

In this section, we study how to compute $w_{i,t}$ in a multi-layer perceptron (MLP) network. One of the core steps is to compute the gradients of the validation loss wrt. the local perturbation $\epsilon$, We can consider a multi-layered network where we have parameters for each layer $\theta = {\{\theta_{l}\}}_{l = 1}^{L}$, and at every layer, we first compute $z_{l}$ the pre-activation, a weighted sum of inputs to the layer, and afterwards we apply a non-linear activation function $\sigma$ to obtain ${\overset{\sim}{z}}_{l}$ the post-activation: During backpropagation, let $g_{l}$ be the gradients of loss wrt. $z_{l}$, and the gradients wrt. $\theta_{l}$ is given by ${\overset{\sim}{z}}_{l - 1}g_{l}^{\top}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Example: learning to reweight examples in a multi-layer perceptron network", "weight": 1.0} -->

We can further express the gradients towards $\epsilon$ as a sum of local dot products.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Example: learning to reweight examples in a multi-layer perceptron network", "weight": 1.0} -->

{\frac{1}{m}{\sum\limits_{j = 1}^{m}\frac{\partial{f_{j}^{v}{(\theta)}}}{\partial\theta}}} \right|_{\theta = \theta_{t}}^{\top}\frac{\partial{f_{i}{(\theta)}}}{\partial\theta}} \right|_{\theta = \theta_{t}}} \\ | | | Detailed derivations can be found in Appendix A. Eq. 12 suggests that the meta-gradient on $\epsilon$ is composed of the sum of the products of two terms: $z^{\top}z^{v}$ and $g^{\top}g^{v}$. The first dot product computes the similarity between the training and validation inputs to the layer, while the second computes the similarity between the training and validation gradient directions.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Example: learning to reweight examples in a multi-layer perceptron network", "weight": 1.0} -->

In other words, suppose that a pair of training and validation examples are very similar, and they also provide similar gradient directions, then this training example is helpful and should be up-weighted, and conversely, if they provide opposite gradient directions, this training example is harmful and should be downweighed.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Implementation using automatic differentiation", "weight": 1.0} -->

In an MLP and a CNN, the unnormalized weights can be calculated based on the sum of the correlations of layerwise activation gradients and input activations. In more general networks, we can leverage automatic differentiation techniques to compute the gradient of the validation loss wrt. the example weights of the current batch. As shown in Figure 1, to get the gradients of the example weights, one needs to first unroll the gradient graph of the training batch, and then use backward-on-backward automatic differentiation to take a second order gradient pass (see Step 5 in Figure 1). We list detailed step-by-step pseudo-code in Algorithm 1. This implementation can be generalized to any deep learning architectures and can be very easily implemented using popular deep learning frameworks such as TensorFlow.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Training time", "weight": 1.0} -->

Our automatic reweighting method will introduce a constant factor of overhead. First, it requires two full forward and backward passes of the network on training and validation respectively, and then another backward on backward pass (Step 5 in Figure 1), to get the gradients to the example weights, and finally a backward pass to minimize the reweighted objective. In modern networks, a backward-on-backward pass usually takes about the same time as a forward pass, and therefore compared to regular training, our method needs approximately 3$\times$ training time; it is also possible to reduce the batch size of the validation pass for speedup. We expect that it is worthwhile to spend the extra time to avoid the irritation of choosing early stopping, finetuning schedules, and other hyperparameters.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Analysis: convergence of the reweighted training", "weight": 1.0} -->

Convergence results of SGD based optimization methods are well-known. However it is still meaningful to establish a convergence result about our method since it involves optimization of two-level objectives (Eq. 1, 2) rather than one, and we further make some first-order approximation by introducing Eq. 7. Here, we show theoretically that our method converges to the critical point of the validation loss function under some mild conditions, and we also give its convergence rate. More detailed proofs can be found in the Appendix B, C.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Experiments", "weight": 1.0} -->

To test the effectiveness of our reweighting algorithm, we designed both class imbalance and noisy label settings, and a combination of both, on standard MNIST and CIFAR benchmarks for image classification using deep CNNs.

<!-- chunk {"id": "body-0025", "role": "body", "section": "MNIST data imbalance experiments", "weight": 1.0} -->

We use the standard MNIST handwritten digit classification dataset and subsample the dataset to generate a class imbalance binary classification task. We select a total of 5,000 images of size 28$\times$`<!-- -->`{=html}28 on class 4 and 9, where 9 dominates the training data distribution. We train a standard LeNet on this task and we compare our method with a suite of commonly used tricks for class imbalance: 1) Proportion weights each example by the inverse frequency 2) Resample samples a class-balanced mini-batch for each iteration 3) Hard Mining selects the highest loss examples from the majority class and 4) Random is a random example weight baseline that assigns weights based on a rectified Gaussian distribution: To make sure that our method does not have the privilege of training on more data, we split the balanced validation set of 10 images directly from the training set. The network is trained with SGD with a learning rate of 1e-3 and mini-batch size of 100 for a total of 8,000 steps.

<!-- chunk {"id": "body-0026", "role": "body", "section": "CIFAR noisy label experiments", "weight": 1.0} -->

Reweighting algorithm can also be useful on datasets where the labels are noisy. We study two settings of label noise here: UniformFlip: All label classes can uniformly flip to any other label classes, which is the most studied in the literature.

<!-- chunk {"id": "body-0027", "role": "body", "section": "CIFAR noisy label experiments", "weight": 1.0} -->

BackgroundFlip: All label classes can flip to a single background class. This noise setting is very realistic. For instance, human annotators may not have recognized all the positive instances, while the rest remain in the background class. This is also a combination of label imbalance and label noise since the background class usually dominates the label distribution.

<!-- chunk {"id": "body-0028", "role": "body", "section": "CIFAR noisy label experiments", "weight": 1.0} -->

We compare our method with prior work on the noisy label problem.

<!-- chunk {"id": "body-0029", "role": "body", "section": "CIFAR noisy label experiments", "weight": 1.0} -->

Reed, proposed by Reed et al., is a bootstrapping technique where the training target is a convex combination of the model prediction and the label.

<!-- chunk {"id": "body-0030", "role": "body", "section": "CIFAR noisy label experiments", "weight": 1.0} -->

S-Model, proposed by Goldberger & Ben-Reuven, adds a fully connected softmax layer after the regular classification output layer to model the noise transition matrix.

<!-- chunk {"id": "body-0031", "role": "body", "section": "CIFAR noisy label experiments", "weight": 1.0} -->

MentorNet, proposed by Jiang et al., is an RNN-based meta-learning model that takes in a sequence of loss values and outputs the example weights. We compare numbers reported in their paper with a base model that achieves similar test accuracy under 0% noise.

<!-- chunk {"id": "body-0032", "role": "body", "section": "CIFAR noisy label experiments", "weight": 1.0} -->

In addition, we propose two simple baselines: 1) Random, which assigns weights according to a rectified Gaussian (see Eq. 16); 2) Weighted, designed for BackgroundFlip, where the model knows the oracle noise ratio for each class and reweights the training loss proportional to the percentage of clean images of that label class.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Clean validation set", "weight": 1.0} -->

For UniformFlip, we use 1,000 clean images in the validation set; for BackgroundFlip, we use 10 clean images per label class. Since our method uses information from the clean validation, for a fair comparison, we conduct an additional finetuning on the clean data based on the pre-trained baselines. We also study the effect on the size of the clean validation set in an ablation study.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Hyper-validation set", "weight": 1.0} -->

For monitoring training progress and tuning baseline hyperparameters, we split out another 5,000 hyper-validation set from the 50,000 training images. We also corrupt the hyper-validation set with the same noise type.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Hyper-validation set", "weight": 1.0} -->

Using 1,000 clean images Table 1: CIFAR UniformFlip under 40% noise ratio using a WideResNet-28-10 model. Test accuracy shown in percentage. Top rows use only noisy data, and bottom uses additional 1000 clean images. “FT” denotes fine-tuning on clean data.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Hyper-validation set", "weight": 1.0} -->

Using 10 clean images per class Table 2: CIFAR BackgroundFlip under 40% noise ratio using a ResNet-32 model. Test accuracy shown in percentage. Top rows use only noisy data, and bottom rows use additional 10 clean images per class. “+ES” denotes early stopping; “FT” denotes fine-tuning.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experimental details", "weight": 1.0} -->

For Reed model, we use the best $\beta$ reported in Reed et al. ($\beta = 0.8$ for hard bootstrapping and $\beta = 0.95$ for soft bootstrapping). For the S-Model, we explore two versions to initialize the transition weights: 1) a smoothed identity matrix; 2) in background flip experiments we consider initializing the transition matrix with the confusion matrix of a pre-trained baseline model (S-Model +Conf). We find baselines can easily overfit the training noise, and therefore we also study early stopped versions of the baselines to provide a stronger comparison. In contrast, we find early stopping not necessary for our method.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experimental details", "weight": 1.0} -->

To make our results comparable with the ones reported in MentorNet and to save computation time, we exchange their Wide ResNet-101-10 with a Wide ResNet-28-10 (WRN-28-10) with dropout 0.3 as our base model in the UniformFlip experiments. We find that test accuracy differences between the two base models are within 0.5% on CIFAR datasets under 0% noise. In the BackgroundFlip experiments, we use a ResNet-32 as our base model.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experimental details", "weight": 1.0} -->

We train the models with SGD with momentum, at an initial learning rate 0.1 and a momentum 0.9 with mini-batch size 100. For ResNet-32 models, the learning rate decays $\times 0.1$ at 40K and 60K steps, for a total of 80K steps. For WRN and early stopped versions of ResNet-32 models, the learning rate decays at 40K and 50K steps, for a total of 60K steps. Under regular 0% noise settings, our base ResNet-32 gets 92.5% and 68.1% classification accuracy on CIFAR-10 and 100, and the WRN-28-10 gets 95.5% and 78.2%. For the finetuning stage, we run extra 5K steps of training on the limited clean data.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experimental details", "weight": 1.0} -->

We report the average test accuracy for 5 different random splits of clean and noisy labels, with 95% confidence interval in Table 1 and 2. The background classes for the 5 trials are (CIFAR-10) and (CIFAR-100).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Results and Discussion", "weight": 1.0} -->

The first result that draws our attention is that "Random" performs surprisingly well on the UniformFlip benchmark, outperforming all historical methods that we compared. Given that its performance is comparable with Baseline on BackgroundFlip and MNIST class imbalance, we hypothesize that random example weights act as a strong regularizer and under which the learning objective on UniformFlip is still consistent.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Results and Discussion", "weight": 1.0} -->

Regardless of the strong baseline, our method ranks the top on both UniformFlip and BackgroundFlip, showing our method is less affected by the changes in the noise type. On CIFAR-100, our method wins more than 3% compared to the state-of-the-art method.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Understanding the reweighting mechanism", "weight": 1.0} -->

It is beneficial to understand how our reweighting algorithm contributes to learning more robust models during training. First, we use a pre-trained model (trained at half of the total iterations without learning rate decay) and measure the example weight distribution of a randomly sampled batch of validation images, which the model has never seen. As shown in the left figure of Figure 3, our model correctly pushes most noisy images to zero weights. Secondly, we conditioned the input mini-batch to be a single non-background class and randomly flip 40% of the images to the background, and we would like to see how well our model can distinguish clean and noisy images. As shown in Figure 3 right, the model is able to reliably detect images that are flipped to the background class.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Robustness to overfitting noise", "weight": 1.0} -->

Throughout experimentation, we find baseline models can easily overfit to the noise in the training set. For example, shown in Table 2, applying early stopping ("ES") helps the classification performance of "S-Model" by over 10% on CIFAR-10. Figure 6 compares the final confusion matrices of the baseline and the proposed algorithm, where a large proportion of noise transition probability is cleared in the final prediction. Figure 7 shows training curves on the BackgroundFlip experiments. After the first learning rate decay, both "Baseline" and "S-Model" quickly degrade their validation performance due to overfitting, while our model remains the same validation accuracy until termination. Note that here "S-Model" knows the oracle noise ratio in each class, and this information is not available in our method.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Impact of the noise level", "weight": 1.0} -->

We would like to investigate how strongly our method can perform on a variety of noise levels. Shown in Figure 5, our method only drops 6% accuracy when the noise ratio increased from 0% to 50%; whereas the baseline has dropped more than 40%. At 0% noise, our method only slightly underperforms baseline. This is reasonable since we are optimizing on the validation set, which is strictly a subset of the full training set, and therefore suffers from its own subsample bias.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Size of the clean validation set", "weight": 1.0} -->

When the size of the clean validation set grows larger, fine-tuning on the validation set will be a reasonble approach. Here, we make an attempt to explore the tradeoff and understand when fine-tuning becomes beneficial. Figure 4 plots the classification performance when we varied the size of the clean validation on BackgroundFlip. Surprisingly, using 15 validation images for all classes only results in a 2% drop in performance, and the overall classification performance does not grow after having more than 100 validation images. In comparison, we observe a significant drop in performance when only fine-tuning on these 15 validation images for the baselines, and the performance catches up around using 1,000 validation images (100 per class). This phenomenon suggests that in our method the clean validation acts more like a regularizer rather than a data source for parameter fine-tuning, and potentially our method can be complementary with fine-tuning based method when the size of the clean set grows larger.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we propose an online meta-learning algorithm for reweighting training examples and training more robust deep learning models. While various types of training set biases exist and manually designed reweighting objectives have their own bias, our automatic reweighting algorithm shows superior performance dealing with class imbalance, noisy labels, and both. Our method can be directly applied to any deep learning architecture and is expected to train end-to-end without any additional hyperparameter search. Validating on every training step is a novel setting and we show that it has links with model regularization, which can be a fruitful future research direction.
