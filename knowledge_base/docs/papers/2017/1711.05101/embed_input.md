<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Decoupled Weight Decay Regularization

Topics include Gradient descent, Stochastic gradients, Classification, Datasets, Generalization, Optimization, Learning, AdamW.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

L_2 regularization and weight decay regularization are equivalent for standard stochastic gradient descent (when rescaled by the learning rate), but as we demonstrate this is not the case for adaptive gradient algorithms, such as Adam. While common implementations of these algorithms employ L_2 regularization (often calling it "weight decay" in what may be misleading due to the inequivalence we expose), we propose a simple modification to recover the original formulation of weight decay regularization by decoupling the weight decay from the optimization steps taken w.r.t. the loss function. We provide empirical evidence that our proposed modification (i) decouples the optimal choice of weight decay factor from the setting of the learning rate for both standard SGD and Adam and (ii) substantially improves Adam's generalization performance, allowing it to compete with SGD with momentum on image classification datasets (on which it was previously typically outperformed by the latter). Our proposed decoupled weight decay has already been adopted by many researchers, and the community has implemented it in TensorFlow and PyTorch; the complete source code for our experiments is available at

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Adaptive gradient methods, such as AdaGrad, RMSProp, Adam and most recently AMSGrad have become a default method of choice for training feed-forward and recurrent neural networks. Nevertheless, state-of-the-art results for popular image classification datasets, such as CIFAR-10 and CIFAR-100 Krizhevsky, are still obtained by applying SGD with momentum. Furthermore, Wilson et al. suggested that adaptive gradient methods do not generalize as well as SGD with momentum when tested on a diverse set of deep learning tasks, such as image classification, character-level language modeling and constituency parsing. Different hypotheses about the origins of this worse generalization have been investigated, such as the presence of sharp local minima and inherent problems of adaptive gradient methods. In this paper, we investigate whether it is better to use L~2~ regularization or weight decay regularization to train deep neural networks with SGD and Adam. We show that a major factor of the poor generalization of the most popular adaptive gradient method, Adam, is due to the fact that L~2~ regularization is not nearly as effective for it as for SGD.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Specifically, our analysis of Adam leads to the following observations:: L~2~ regularization and weight decay are not identical. The two techniques can be made equivalent for SGD by a reparameterization of the weight decay factor based on the learning rate; however, as is often overlooked, this is not the case for Adam. In particular, when combined with adaptive gradients, L~2~ regularization leads to weights with large historic parameter and/or gradient amplitudes being regularized less than they would be when using weight decay.: L~2~ regularization is not effective in Adam. One possible explanation why Adam and other adaptive gradient methods might be outperformed by SGD with momentum is that common deep learning libraries only implement L~2~ regularization, not the original weight decay. Therefore, on tasks/datasets where the use of L~2~ regularization is beneficial for SGD (e.g., on many popular image classification datasets), Adam leads to worse results than SGD with momentum (for which L~2~ regularization behaves as expected).: Weight decay is equally effective in both SGD and Adam.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

For SGD, it is equivalent to L~2~ regularization, while for Adam it is not.: Optimal weight decay depends on the total number of batch passes/weight updates. Our empirical analysis of SGD and Adam suggests that the larger the runtime/number of batch passes to be performed, the smaller the optimal weight decay.: Adam can substantially benefit from a scheduled learning rate multiplier. The fact that Adam is an adaptive gradient algorithm and as such adapts the learning rate for each parameter does *not* rule out the possibility to substantially improve its performance by using a global learning rate multiplier, scheduled, e.g., by cosine annealing.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main contribution of this paper is to *improve regularization in Adam by decoupling the weight decay from the gradient-based update*. In a comprehensive analysis, we show that Adam generalizes substantially better with decoupled weight decay than with L~2~ regularization, achieving 15% relative improvement in test error (see Figures 2 and 3); this holds true for various image recognition datasets (CIFAR-10 and ImageNet32x32), training budgets (ranging from 100 to 1800 epochs), and learning rate schedules (fixed, drop-step, and cosine annealing; see Figure 1). We also demonstrate that our decoupled weight decay renders the optimal settings of the learning rate and the weight decay factor much more independent, thereby easing hyperparameter optimization (see Figure 2).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main motivation of this paper is to improve Adam to make it competitive w.r.t. SGD with momentum even for those problems where it did not use to be competitive. We hope that as a result, practitioners do not need to switch between Adam and SGD anymore, which in turn should reduce the common issue of selecting dataset/task-specific training algorithms and their hyperparameters.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Decoupling the Weight Decay from the Gradient-based Update", "weight": 1.0} -->

In the weight decay described by Hanson & Pratt, the weights $\mathbf{θ}$ decay exponentially as where $\lambda$ defines the rate of the weight decay per step and ${\nabla f_{t}}{({\mathbf{θ}}_{t})}$ is the $t$-th batch gradient to be multiplied by a learning rate $\alpha$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Justification of Decoupled Weight Decay via a View of Adaptive Gradient Methods as Bayesian Filtering", "weight": 1.0} -->

We now discuss a justification of decoupled weight decay in the framework of Bayesian filtering for a unified theory of adaptive gradient algorithms due to Aitchison. After we posted a preliminary version of our current paper on arXiv, Aitchison noted that his theory "gives us a theoretical framework in which we can understand the superiority of this weight decay over $L_{2}$ regularization, because it is weight decay, rather than $L_{2}$ regularization that emerges through the straightforward application of Bayesian filtering.". While full credit for this theory goes to Aitchison, we summarize it here to shed some light on why weight decay may be favored over $L_{2}$ regularization.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Justification of Decoupled Weight Decay via a View of Adaptive Gradient Methods as Bayesian Filtering", "weight": 1.0} -->

Aitchison views stochastic optimization of $n$ parameters $\theta_{1},\ldots,\theta_{n}$ as a Bayesian filtering problem with the goal of inferring a distribution over the optimal values of each of the parameters $\theta_{i}$ given the current values of the other parameters ${\mathbf{θ}}_{- i}{(t)}$ at time step $t$. When the other parameters do not change this is an optimization problem, but when they do change it becomes one of "tracking" the optimizer using Bayesian filtering as follows.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Justification of Decoupled Weight Decay via a View of Adaptive Gradient Methods as Bayesian Filtering", "weight": 1.0} -->

One is given a probability distribution $P{({{\mathbf{θ}}_{t} \mid {\mathbf{y}}_{\mathbf{1}:{\mathbf{t}}}})}$ of the optimizer at time step $t$ that takes into account the data ${\mathbf{y}}_{\mathbf{1}:{\mathbf{t}}}$ from the first $t$ mini batches, a state transition prior $P{({{\mathbf{θ}}_{t + 1} \mid {\mathbf{θ}}_{t}})}$ reflecting a (small) data-independent change in this distribution from one step to the next, and a likelihood $P{({{\mathbf{y}}_{t + 1} \mid {\mathbf{θ}}_{t + 1}})}$ derived from the mini batch at step $t + 1$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Justification of Decoupled Weight Decay via a View of Adaptive Gradient Methods as Bayesian Filtering", "weight": 1.0} -->

Aitchison assumes a Gaussian state transition distribution $P{({{\mathbf{θ}}_{t + 1} \mid {\mathbf{θ}}_{t}})}$ and an approximate conjugate likelihood $P{({{\mathbf{y}}_{t + 1} \mid {\mathbf{θ}}_{t + 1}})}$, leading to the following closed-form update of the filtering distribution's mean: where $\mathbf{g}$ is the gradient of the log likelihood of the mini batch at time $t$. This result implies a preconditioner of the gradients that is given by the posterior uncertainty $\mathbf{\Sigma}_{post}$ of the filtering distribution: updates are larger for parameters we are more uncertain about and smaller for parameters we are more certain about. Aitchison goes on to show that popular adaptive gradient methods, such as Adam and RMSprop, as well as Kronecker-factorized methods are special cases of this framework.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Justification of Decoupled Weight Decay via a View of Adaptive Gradient Methods as Bayesian Filtering", "weight": 1.0} -->

Decoupled weight decay very naturally fits into this unified framework as part of the state-transition distribution: Aitchison assumes a slow change of the optimizer according to the following Gaussian: where $\mathbf{Q}$ is the covariance of Gaussian perturbations of the weights, and $\mathbf{A}$ is a regularizer to avoid values growing unboundedly over time. When instantiated as ${\mathbf{A}} = {\lambda \times {\mathbf{I}}}$, this regularizer $\mathbf{A}$ plays exactly the role of decoupled weight decay as described in Equation 1, since this leads to multiplying the current mean estimate ${\mathbf{θ}}_{t}$ by $({1 - \lambda})$ at each step. Notably, this regularization is also directly applied to the prior and does not depend on the uncertainty in each of the parameters (which would be required for $L_{2}$ regularization).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Experimental Validation", "weight": 1.0} -->

We now evaluate the performance of decoupled weight decay under various training budgets and learning rate schedules. Our experimental setup follows that of Gastaldi, who proposed, in addition to L~2~ regularization, to apply the new Shake-Shake regularization to a 3-branch residual DNN that allowed to achieve new state-of-the-art results of 2.86% on the CIFAR-10 dataset. We used the same model/source code based on fb.resnet.torch ^11^1 We always used a batch size of 128 and applied the regular data augmentation procedure for the CIFAR datasets. The base networks are a 26 2x64d ResNet (i.e. the network has a depth of 26, 2 residual branches and the first residual block has a width of 64) and a 26 2x96d ResNet with 11.6M and 25.6M parameters, respectively. For a detailed description of the network and the Shake-Shake method, we refer the interested reader to Gastaldi.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Experimental Validation", "weight": 1.0} -->

We also perform experiments on the ImageNet32x32 dataset, a downsampled version of the original ImageNet dataset with 1.2 million 32$\times$`<!-- -->`{=html}32 pixels images.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Evaluating Decoupled Weight Decay With Different Learning Rate Schedules", "weight": 1.0} -->

In our first experiment, we compare Adam with $L_{2}$ regularization to Adam with decoupled weight decay (AdamW), using three different learning rate schedules: a fixed learning rate, a drop-step schedule, and a cosine annealing schedule. Since Adam already adapts its parameterwise learning rates it is not as common to use a learning rate multiplier schedule with it as it is with SGD, but as our results show such schedules can substantially improve Adam's performance, and we advocate not to overlook their use for adaptive gradient algorithms.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Evaluating Decoupled Weight Decay With Different Learning Rate Schedules", "weight": 1.0} -->

For each learning rate schedule and weight decay variant, we trained a 2x64d ResNet for 100 epochs, using different settings of the initial learning rate $\alpha$ and the weight decay factor $\lambda$. Figure 1 shows that decoupled weight decay outperforms $L_{2}$ regularization for all learning rate schedules, with larger differences for better learning rate schedules. We also note that decoupled weight decay leads to a more separable hyperparameter search space, especially when a learning rate schedule, such as step-drop and cosine annealing is applied. The figure also shows that cosine annealing clearly outperforms the other learning rate schedules; we thus used cosine annealing for the remainder of the experiments.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Decoupling the Weight Decay and Initial Learning Rate Parameters", "weight": 1.0} -->

In order to verify our hypothesis about the coupling of $\alpha$ and $\lambda$, in Figure 2 we compare the performance of L~2~ regularization vs. decoupled weight decay in SGD (SGD vs. SGDW, top row) and in Adam (Adam vs. AdamW, bottom row). In SGD (Figure 2, top left), L~2~ regularization is not decoupled from the learning rate (the common way as described in Algorithm 1), and the figure clearly shows that the basin of best hyperparameter settings (depicted by color and top-10 hyperparameter settings by black circles) is not aligned with the x-axis or y-axis but lies on the diagonal. This suggests that the two hyperparameters are interdependent and need to be changed simultaneously, while only changing one of them might substantially worsen results.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Decoupling the Weight Decay and Initial Learning Rate Parameters", "weight": 1.0} -->

Consider, e.g., the setting at the top left black circle ($\alpha = {1/2}$, $\lambda = {{1/8} \ast 0.001}$); only changing either $\alpha$ or $\lambda$ by itself would worsen results, while changing both of them could still yield clear improvements. We note that this coupling of initial learning rate and L~2~ regularization factor might have contributed to SGD's reputation of being very sensitive to its hyperparameter settings.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Decoupling the Weight Decay and Initial Learning Rate Parameters", "weight": 1.0} -->

In contrast, the results for SGD with decoupled weight decay (SGDW) in Figure 2 (top right) show that weight decay and initial learning rate are decoupled. The proposed approach renders the two hyperparameters more separable: even if the learning rate is not well tuned yet (e.g., consider the value of 1/1024 in Figure 2, top right), leaving it fixed and only optimizing the weight decay factor would yield a good value (of 1/4\*0.001). This is not the case for SGD with L~2~ regularization (see Figure 2, top left).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Decoupling the Weight Decay and Initial Learning Rate Parameters", "weight": 1.0} -->

The results for Adam with L~2~ regularization are given in Figure 2 (bottom left). Adam's best hyperparameter settings performed clearly worse than SGD's best ones (compare Figure 2, top left). While both methods used L~2~ regularization, Adam did not benefit from it at all: its best results obtained for non-zero L~2~ regularization factors were comparable to the best ones obtained without the L~2~ regularization, i.e., when $\lambda = 0$. Similarly to the original SGD, the shape of the hyperparameter landscape suggests that the two hyperparameters are coupled.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Decoupling the Weight Decay and Initial Learning Rate Parameters", "weight": 1.0} -->

In contrast, the results for our new variant of Adam with decoupled weight decay (AdamW) in Figure 2 (bottom right) show that AdamW largely decouples weight decay and learning rate. The results for the best hyperparameter settings were substantially better than the best ones of Adam with L~2~ regularization and rivaled those of SGD and SGDW.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Decoupling the Weight Decay and Initial Learning Rate Parameters", "weight": 1.0} -->

In summary, the results in Figure 2 support our hypothesis that the weight decay and learning rate hyperparameters can be decoupled, and that this in turn simplifies the problem of hyperparameter tuning in SGD and improves Adam's performance to be competitive w.r.t. SGD with momentum.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Better Generalization of AdamW", "weight": 1.0} -->

While the previous experiment suggested that the basin of optimal hyperparameters of AdamW is broader and deeper than the one of Adam, we next investigated the results for much longer runs of 1800 epochs to compare the generalization capabilities of AdamW and Adam.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Better Generalization of AdamW", "weight": 1.0} -->

We fixed the initial learning rate to 0.001 which represents both the default learning rate for Adam and the one which showed reasonably good results in our experiments. Figure 3 shows the results for 12 settings of the L~2~ regularization of Adam and 7 settings of the normalized weight decay of AdamW (the normalized weight decay represents a rescaling formally defined in Appendix B.1; it amounts to a multiplicative factor which depends on the number of batch passes). Interestingly, while the dynamics of the learning curves of Adam and AdamW often coincided for the first half of the training run, AdamW often led to lower training loss and test errors (see Figure 3 top left and top right, respectively). Importantly, the use of L~2~ weight decay in Adam did not yield as good results as decoupled weight decay in AdamW (see also Figure 3, bottom left). Next, we investigated whether AdamW's better results were only due to better convergence or due to better generalization. *The results in Figure 3 (bottom right) for the best settings of Adam and AdamW suggest that AdamW did not only yield better training loss but also yielded better generalization performance for similar training loss values*.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Better Generalization of AdamW", "weight": 1.0} -->

The results on ImageNet32x32 (see SuppFigure 4 in the Appendix) yield the same conclusion of substantially improved generalization performance.

<!-- chunk {"id": "body-0027", "role": "body", "section": "AdamWR with Warm Restarts for Better Anytime Performance", "weight": 1.0} -->

In order to improve the anytime performance of SGDW and AdamW we extended them with the warm restarts we introduced in Loshchilov & Hutter, to obtain SGDWR and AdamWR, respectively (see Section B.2 in the Appendix). As Figure 4 shows, AdamWR greatly sped up AdamW on CIFAR-10 and ImageNet32x32, up to a factor of 10 (see the results at the first restart). For the default learning rate of 0.001, *AdamW achieved 15% relative improvement in test error compared to Adam both on CIFAR-10* (also see SuppFigure 5) *and ImageNet32x32* (also see SuppFigure 6).

<!-- chunk {"id": "body-0028", "role": "body", "section": "AdamWR with Warm Restarts for Better Anytime Performance", "weight": 1.0} -->

*AdamWR achieved the same improved results but with a much better anytime performance.* These improvements closed most of the gap between Adam and SGDWR on CIFAR-10 and yielded comparable performance on ImageNet32x32.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Use of AdamW on other datasets and architectures", "weight": 1.0} -->

Several other research groups have already successfully applied AdamW in citable works. For example, Wang et al. used AdamW to train a novel architecture for face detection on the standard WIDER FACE dataset, obtaining almost 10x faster predictions than the previous state of the art algorithms while achieving comparable performance. Völker et al. employed AdamW with cosine annealing to train convolutional neural networks to classify and characterize error-related brain signals measured from intracranial electroencephalography (EEG) recordings. While their paper does not provide a comparison to Adam, they kindly provided us with a direct comparison of the two on their best-performing problem-specific network architecture Deep4Net and a variant of ResNet. AdamW with the same hyperparameter setting as Adam yielded higher test set accuracy on Deep4Net (73.68% versus 71.37%) and statistically significantly higher test set accuracy on ResNet (72.04% versus 61.34%). Radford et al. employed AdamW to train Transformer architectures to obtain new state-of-the-art results on a wide range of benchmarks for natural language understanding.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Use of AdamW on other datasets and architectures", "weight": 1.0} -->

Zhang et al. compared L~2~ regularization vs. weight decay for SGD, Adam and the Kronecker-Factored Approximate Curvature (K-FAC) optimizer on the CIFAR datasets with ResNet and VGG architectures, reporting that decoupled weight decay consistently outperformed L~2~ regularization in cases where they differ.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

Following suggestions that adaptive gradient methods such as Adam might lead to worse generalization than SGD with momentum, we identified and exposed the inequivalence of L~2~ regularization and weight decay for Adam. We empirically showed that our version of Adam with decoupled weight decay yields substantially better generalization performance than the common implementation of Adam with L~2~ regularization. We also proposed to use warm restarts for Adam to improve its anytime performance.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

Our results obtained on image classification datasets must be verified on a wider range of tasks, especially ones where the use of regularization is expected to be important. It would be interesting to integrate our findings on weight decay into other methods which attempt to improve Adam, e.g, normalized direction-preserving Adam. While we focused our experimental analysis on Adam, we believe that similar results also hold for other adaptive gradient methods, such as AdaGrad and AMSGrad.
