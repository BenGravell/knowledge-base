<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Learning Imbalanced Datasets with Label-Distribution-Aware Margin Loss

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Deep learning algorithms can fare poorly when the training dataset suffers from heavy class-imbalance but the testing criterion requires good generalization on less frequent classes. We design two novel methods to improve performance in such scenarios. First, we propose a theoretically-principled label-distribution-aware margin (LDAM) loss motivated by minimizing a margin-based generalization bound. This loss replaces the standard cross-entropy objective during training and can be applied with prior strategies for training with class-imbalance such as re-weighting or re-sampling. Second, we propose a simple, yet effective, training schedule that defers re-weighting until after the initial stage, allowing the model to learn an initial representation while avoiding some of the complications associated with re-weighting or re-sampling. We test our methods on several benchmark vision tasks including the real-world imbalanced dataset iNaturalist 2018. Our experiments show that either of these methods alone can already improve over existing techniques and their combination achieves even better performance gains.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Modern real-world large-scale datasets often have long-tailed label distributions. On these datasets, deep neural networks have been found to perform poorly on less represented classes. This is particularly detrimental if the testing criterion places more emphasis on minority classes. For example, accuracy on a uniform label distribution or the minimum accuracy among all classes are examples of such criteria. These are common scenarios in many applications due to various practical concerns such as transferability to new domains, fairness, etc.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The two common approaches for learning long-tailed data are re-weighting the losses of the examples and re-sampling the examples in the SGD mini-batch (see and the references therein). They both devise a training loss that is in expectation closer to the test distribution, and therefore can achieve better trade-offs between the accuracies of the frequent classes and the minority classes. However, because we have fundamentally less information about the minority classes and the models deployed are often huge, over-fitting to the minority classes appears to be one of the challenges in improving these methods.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose to regularize the minority classes more strongly than the frequent classes so that we can improve the generalization error of minority classes without sacrificing the model's ability to fit the frequent classes. Implementing this general idea requires a data-dependent or label-dependent regularizer --- which in contrast to standard $\ell_{2}$ regularization depends not only on the weight matrices but also on the labels --- to differentiate frequent and minority classes. The theoretical understanding of data-dependent regularizers is sparse (see for a few recent works.)

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We explore one of the simplest and most well-understood data-dependent properties: the margins of the training examples. Encouraging a large margin can be viewed as regularization, as standard generalization error bounds (e.g., ) depend on the inverse of the minimum margin among all the examples. Motivated by the question of generalization with respect to minority classes, we instead study the minimum margin per class and obtain per-class and uniform-label test error bounds.^22^2The same technique can also be used for other test label distribution as long as the test label distribution is known. See Section C.5 for some experimental results. Minimizing the obtained bounds gives an optimal trade-off between the margins of the classes. See Figure 1 for an illustration in the binary classification case.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Inspired by the theory, we design a label-distribution-aware loss function that encourages the model to have the optimal trade-off between per-class margins. The proposed loss extends the existing soft margin loss by encouraging the minority classes to have larger margins. As a label-dependent regularization technique, our modified loss function is orthogonal to the re-weighting and re-sampling approach. In fact, we also design a deferred re-balancing optimization procedure that allows us to combine the re-weighting strategy with our loss (or other losses) in a more efficient way.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In summary, our main contributions are (i) we design a label-distribution-aware loss function to encourage larger margins for minority classes, (ii) we propose a simple deferred re-balancing optimization procedure to apply re-weighting more effectively, and (iii) our practical implementation shows significant improvements on several benchmark vision tasks, such as artificially imbalanced CIFAR and Tiny ImageNet (tin, ), and the real-world large-scale imbalanced dataset iNaturalist'18.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Related Works", "weight": 1.0} -->

Most existing algorithms for learning imbalanced datasets can be divided in to two categories: re-sampling and re-weighting.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Related Works", "weight": 1.0} -->

Re-sampling. There are two types of re-sampling techniques: over-sampling the minority classes (see e.g., and references therein) and under-sampling the frequent classes (see, e.g., and the references therein.) The downside of under-sampling is that it discards a large portion of the data and thus is not feasible when data imbalance is extreme. Over-sampling is effective in a lot of cases but can lead to over-fitting of the minority classes. Stronger data augmentation for minority classes can help alleviate the over-fitting.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Related Works", "weight": 1.0} -->

Re-weighting. Cost-sensitive re-weighting assigns (adaptive) weights for different classes or even different samples. The vanilla scheme re-weights classes proportionally to the inverse of their frequency. Re-weighting methods tend to make the optimization of deep models difficult under extreme data imbalanced settings and large-scale scenarios. Cui et al. observe that re-weighting by inverse class frequency yields poor performance on frequent classes, and thus propose re-weighting by the inverse effective number of samples. This is the main prior work that we empirically compare.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Related Works", "weight": 1.0} -->

Another line of work assigns weights to each sample based on their individual properties. Focal loss down-weights the well-classified examples; Li et al. suggests an improved technique which down-weights examples with either very small gradients or large gradients because examples with small gradients are well-classified and those with large gradients tend to be outliers.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Related Works", "weight": 1.0} -->

In a recent work, Byrd and Lipton study the effect of importance weighting and show that empirically importance weighting does not have a significant effect when no regularization is applied, which is consistent with the theoretical prediction in that logistical regression without regularization converges to the max margin solution. In our work, we explicitly encourage rare classes to have higher margin, and therefore we don't converge to a max margin solution. Moreover, in our experiments, we apply non-trivial $\ell_{2}$-regularization to achieve the best generalization performance. We also found deferred re-weighting (or deferred re-sampling) are more effective than re-weighting and re-sampling from the beginning of the training.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Related Works", "weight": 1.0} -->

In contrast, and orthogonally to these papers above, our main technique aims to improve the generalization of the minority classes by applying additional regularization that is orthogonal to the re-weighting scheme. We also propose a deferred re-balancing optimization procedure to improve the optimization and generalization of a generic re-weighting scheme.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Related Works", "weight": 1.0} -->

Margin loss. The hinge loss is often used to obtain a "max-margin" classifier, most notably in SVMs. Recently, Large-Margin Softmax, Angular Softmax, and Additive Margin Softmax have been proposed to minimize intra-class variation in predictions and enlarge the inter-class margin by incorporating the idea of angular margin. In contrast to the class-independent margins in these papers, our approach encourages bigger margins for minority classes. Uneven margins for imbalanced datasets are also proposed and studied in and the recent work. Our theory put this idea on a more theoretical footing by providing a concrete formula for the desired margins of the classes alongside good empirical progress.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Related Works", "weight": 1.0} -->

Label shift in domain adaptation. The problem of learning imbalanced datasets can be also viewed as a label shift problem in transfer learning or domain adaptation (for which we refer the readers to the survey and the reference therein). In a typical label shift formulation, the difficulty is to detect and estimate the label shift, and after estimating the label shift, re-weighting or re-sampling is applied. We are addressing a largely different question: can we do better than re-weighting or re-sampling when the label shift is known? In fact, our algorithms can be used to replace the re-weighting steps of some of the recent interesting work on detecting and correcting label shift.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Related Works", "weight": 1.0} -->

Distributionally robust optimization (DRO) is another technique for domain adaptation (see and the reference therein.) However, the formulation assumes no knowledge of the target label distribution beyond a bound on the amount of shift, which makes the problem very challenging. We here assume the knowledge of the test label distribution, using which we design efficient methods that can scale easily to large-scale vision datasets with significant improvements.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Related Works", "weight": 1.0} -->

Meta-learning. Meta-learning is also used in improving the performance on imbalanced datasets or the few shot learning settings. We refer the readers to and the references therein. So far, we generally believe that our approaches that modify the losses are more computationally efficient than meta-learning based approaches.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem setup and notations", "weight": 1.0} -->

We assume the input space is ${\mathbb{R}}^{d}$ and the label space is $\{ 1,\ldots,k\}$. Let $x$ denote the input and $y$ denote the corresponding label. We assume that the class-conditional distribution $\mathcal{P}{({x \mid y})}$ is the same at training and test time. Let $\mathcal{P}_{j}$ denote the class-conditional distribution, i.e. $\mathcal{P}_{j} = {\mathcal{P}{({{x \mid y} = j})}}$. We will use $\mathcal{P}_{\text{bal}}$ to denote the balanced test distribution which first samples a class uniformly and then samples data from $\mathcal{P}_{j}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem setup and notations", "weight": 1.0} -->

We consider the separable cases (meaning that all the training examples are classified correctly) because neural networks are often over-parameterized and can fit the training data well. We also note that the minimum margin of all the classes, $\gamma_{\min} = {\min{\{\gamma_{1},\ldots,\gamma_{k}\}}}$, is the classical notion of training margin studied in the past.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Fine-grained generalization error bounds", "weight": 1.0} -->

Let $\mathcal{F}$ be the family of hypothesis class. Let $\text{C}{(\mathcal{F})}$ be some proper complexity measure of the hypothesis class $\mathcal{F}$. There is a large body of recent work on measuring the complexity of neural networks (see and references therein), and our discussion below is orthogonal to the precise choices. When the training distribution and the test distribution are the same, the typical generalization error bounds scale in ${\text{C}{(\mathcal{F})}}/\sqrt{n}$. That is, in our case, if the test distribution is also imbalanced as the training distribution, then

<!-- chunk {"id": "body-0022", "role": "body", "section": "Fine-grained generalization error bounds", "weight": 1.0} -->

Note that the bound is oblivious to the label distribution, and only involves the minimum margin across all examples and the total number of data points. We extend such bounds to the setting with balanced test distribution by considering the margin of each class. As we will see, the more fine-grained bound below allows us to design new training loss function that is customized to the imbalanced dataset.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Class-distribution-aware margin trade-off", "weight": 1.0} -->

The generalization error bound (4. ‣ Fine-grained generalization error bounds. ‣ 3.1 Theoretical Motivations ‣ 3 Main Approach ‣ Learning Imbalanced Datasets with Label-Distribution-Aware Margin Loss")) for each class suggests that if we wish to improve the generalization of minority classes (those with small $n_{j}$'s), we should aim to enforce bigger margins $\gamma_{j}$'s for them. However, enforcing bigger margins for minority classes may hurt the margins of the frequent classes. What is the optimal trade-off between the margins of the classes? An answer for the general case may be difficult, but fortunately we can obtain the optimal trade-off for the binary classification problem.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Class-distribution-aware margin trade-off", "weight": 1.0} -->

With $k = 2$ classes, we aim to optimize the balanced generalization error bound provided in (5. ‣ Fine-grained generalization error bounds. ‣ 3.1 Theoretical Motivations ‣ 3 Main Approach ‣ Learning Imbalanced Datasets with Label-Distribution-Aware Margin Loss")), which can be simplified to (by removing the low order term $\frac{\log n}{\sqrt{n_{j}}}$ and the common factor $\text{C}{(\mathcal{F})}$)

<!-- chunk {"id": "body-0025", "role": "body", "section": "Class-distribution-aware margin trade-off", "weight": 1.0} -->

At the first sight, because $\gamma_{1}$ and $\gamma_{2}$ are complicated functions of the weight matrices, it appears difficult to understand the optimal margins. However, we can figure out the relative scales between $\gamma_{1}$ and $\gamma_{2}$. Suppose ${\gamma_{1},\gamma_{2}} > 0$ minimize the equation above, we observe that any $\gamma_{1}^{\prime} = {\gamma_{1} - \delta}$ and $\gamma_{2}^{\prime} = {\gamma_{2} + \delta}$ (for $\delta \in {({- \gamma_{2}},\gamma_{1})}$) can be realized by the same weight matrices with a shifted bias term (See Figure 1 for an illustration). Therefore, for $\gamma_{1},\gamma_{2}$ to be optimal, they should satisfy

<!-- chunk {"id": "body-0026", "role": "body", "section": "Class-distribution-aware margin trade-off", "weight": 1.0} -->

The equation above implies that

<!-- chunk {"id": "body-0027", "role": "body", "section": "Class-distribution-aware margin trade-off", "weight": 1.0} -->

for some constant $C$. Please see a detailed derivation in the Section A.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Class-distribution-aware margin trade-off", "weight": 1.0} -->

Fast rate vs slow rate, and the implication on the choice of margins. The bound in Theorem 1. ‣ Fine-grained generalization error bounds. ‣ 3.1 Theoretical Motivations ‣ 3 Main Approach ‣ Learning Imbalanced Datasets with Label-Distribution-Aware Margin Loss") may not necessarily be tight. The generalization bounds that scale in $1/\sqrt{n}$ (or $1/\sqrt{n_{i}}$ here with imbalanced classes) are generally referred to the "slow rate" and those that scale in $1/n$ are referred to the "fast rate". With deep neural networks and when the model is sufficiently big enough, it is possible that some of these bounds can be improved to the fast rate. See for some recent development. In those cases, we can derive the optimal trade-off of the margin to be $n_{i} \propto n_{i}^{- {1/3}}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Label-Distribution-Aware Margin Loss", "weight": 1.0} -->

Inspired by the trade-off between the class margins in Section 3.1 for two classes, we propose to enforce a class-dependent margin for multiple classes of the form

<!-- chunk {"id": "body-0030", "role": "body", "section": "Label-Distribution-Aware Margin Loss", "weight": 1.0} -->

We will design a soft margin loss function to encourage the network to have the margins above. Let $(x,y)$ be an example and $f$ be a model. For simplicity, we use $z_{j} = {f{(x)}_{j}}$ to denote the $j$-th output of the model for the $j$-th class.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Label-Distribution-Aware Margin Loss", "weight": 1.0} -->

Here $C$ is a hyper-parameter to be tuned. In order to tune the margin more easily, we effectively normalize the logits (the input to the loss function) by normalizing last hidden activation to $\ell_{2}$ norm 1, and normalizing the weight vectors of the last fully-connected layer to $\ell_{2}$ norm 1, following the previous work. Empirically, the non-smoothness of hinge loss may pose difficulties for optimization.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Label-Distribution-Aware Margin Loss", "weight": 1.0} -->

In the previous work where the training set is usually balanced, the margin $\Delta_{y}$ is chosen to be a label independent constant $C$, whereas our margin depends on the label distribution.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Label-Distribution-Aware Margin Loss", "weight": 1.0} -->

Remark: Attentive readers may find the loss $\mathcal{L}_{\text{LDAM}}$ somewhat reminiscent of the re-weighting because in the binary classification case --- where the model outputs a single real number which is passed through a sigmoid to be converted into a probability, --- both the two approaches change the gradient of an example by a scalar factor. However, we remark two key differences: the scalar factor introduced by the re-weighting only depends on the class, whereas the scalar introduced by $\mathcal{L}_{\text{LDAM}}$ also depends on the output of the model; for multiclass classification problems, the proposed loss $\mathcal{L}_{\text{LDAM}}$ affects the gradient of the example in a more involved way than only introducing a scalar factor. Moreover, recent work has shown that, under separable assumptions, the logistical loss, with weak regularization or without regularization, gives the max margin solution, which is in turn not effected by any re-weighting by its definition.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Label-Distribution-Aware Margin Loss", "weight": 1.0} -->

This further suggests that the loss $\mathcal{L}_{\text{LDAM}}$ and the re-weighting may complement each other, as we have seen in the experiments. (Re-weighting would affect the margin in the non-separable data case, which is left for future work.)

<!-- chunk {"id": "body-0035", "role": "body", "section": "Deferred Re-balancing Optimization Schedule", "weight": 1.0} -->

Cost-sensitive re-weighting and re-sampling are two well-known and successful strategies to cope with imbalanced datasets because, in expectation, they effectively make the imbalanced training distribution closer to the uniform test distribution. The known issues with applying these techniques are (a) re-sampling the examples in minority classes often causes heavy over-fitting to the minority classes when the model is a deep neural network, as pointed out in prior work (e.g., ), and (b) weighting up the minority classes' losses can cause difficulties and instability in optimization, especially when the classes are extremely imbalanced. In fact, Cui et al. develop a novel and sophisticated learning rate schedule to cope with the optimization difficulty.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Deferred Re-balancing Optimization Schedule", "weight": 1.0} -->

We observe empirically that re-weighting and re-sampling are both inferior to the vanilla empirical risk minimization (ERM) algorithm (where all training examples have the same weight) before annealing the learning rate in the following sense. The features produced before annealing the learning rate by re-weighting and re-sampling are worse than those produced by ERM. (See Figure 6 for an ablation study of the feature quality performed by training linear classifiers on top of the features on a large balanced dataset.)

<!-- chunk {"id": "body-0037", "role": "body", "section": "Deferred Re-balancing Optimization Schedule", "weight": 1.0} -->

Inspired by this, we develop a deferred re-balancing training procedure (Algorithm 1), which first trains using vanilla ERM with the LDAM loss before annealing the learning rate, and then deploys a re-weighted LDAM loss with a smaller learning rate. Empirically, the first stage of training leads to a good initialization for the second stage of training with re-weighted losses. Because the loss is non-convex and the learning rate in the second stage is relatively small, the second stage does not move the weights very far. Interestingly, with our LDAM loss and deferred re-balancing training, the vanilla re-weighting scheme (which re-weights by the inverse of the number of examples in each class) works as well as the re-weighting scheme introduced in prior work. We also found that with our re-weighting scheme and LDAM, we are less sensitive to early stopping than.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Deferred Re-balancing Optimization Schedule", "weight": 1.0} -->

A parameterized model fθ 2:Initialize the model parameters θ randomly 4: ℬ ← SampleMiniBatch (𝒟,m) ⊳ a mini-batch of m examples 5: ${\mathcal{L}{(f_{\theta})}}\leftarrow{\frac{1}{m}{\sum_{{(x,y)} \in \mathcal{B}}{\mathcal{L}_{\text{LDAM}}{({(x,y)};f_{\theta})}}}}$ 6: fθ ← fθ − α ∇θℒ (fθ) ⊳ one SGD step 7: Optional: α ← α/τ ⊳ anneal learning rate by a factor τ if necessary 10: ℬ ← SampleMiniBatch (𝒟,m) ⊳ A mini-batch of m examples 11: ${\mathcal{L}{(f_{\theta})}}\leftarrow{\frac{1}{m}{\sum_{{(x,y)} \in

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate our proposed algorithm on artificially created versions of IMDB review, CIFAR-10, CIFAR-100 and Tiny ImageNet with controllable degrees of data imbalance, as well as a real-world large-scale imbalanced dataset, iNaturalist 2018. Our core algorithm is developed using PyTorch.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Baselines", "weight": 1.0} -->

We compare our methods with the standard training and several state-of-the-art techniques and their combinations that have been widely adopted to mitigate the issues with training on imbalanced datasets: Empirical risk minimization (ERM) loss: all the examples have the same weights; by default, we use standard cross-entropy loss. Re-Weighting (RW): we re-weight each sample by the inverse of the sample size of its class, and then re-normalize to make the weights 1 on average in the mini-batch. Re-Sampling (RS): each example is sampled with probability proportional to the inverse sample size of its class. CB: the examples are re-weighted or re-sampled according to the inverse of the effective number of samples in each class, defined as ${({1 - \beta^{n_{i}}})}/{({1 - \beta})}$, instead of inverse class frequencies. This idea can be combined with either re-weighting or re-sampling. Focal: we use the recently proposed focal loss as another baseline.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Baselines", "weight": 1.0} -->

SGD schedule: by SGD, we refer to the standard schedule where the learning rates are decayed a constant factor at certain steps; we use a standard learning rate decay schedule.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Our proposed algorithm and variants", "weight": 1.0} -->

We test combinations of the following techniques proposed by us. DRW and DRS: following the proposed training Algorithm 1, we use the standard ERM optimization schedule until the last learning rate decay, and then apply re-weighting or re-sampling for optimization in the second stage. LDAM: the proposed Label-Distribution-Aware Margin losses as described in Section 3.2.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Our proposed algorithm and variants", "weight": 1.0} -->

When two of these methods can be combined, we will concatenate the acronyms with a dash in between as an abbreviation. The main algorithm we propose is LDAM-DRW. Please refer to Section B for additional implementation details.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Experimental results on IMDB review dataset", "weight": 1.0} -->

IMDB review dataset consists of 50,000 movie reviews for binary sentiment classification. The original dataset contains an evenly distributed number of positive and negative reviews. We manually created an imbalanced training set by removing 90% of negative reviews. We train a two-layer bidirectional LSTM with Adam optimizer. The results are reported in Table 1.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Experimental results on IMDB review dataset", "weight": 1.0} -->

Error on positive reviews
Error on negative reviews

<!-- chunk {"id": "body-0046", "role": "body", "section": "Experimental results on CIFAR", "weight": 1.0} -->

Imbalanced CIFAR-10 and CIFAR-100. The original version of CIFAR-10 and CIFAR-100 contains 50,000 training images and 10,000 validation images of size $32 \times 32$ with 10 and 100 classes, respectively. To create their imbalanced version, we reduce the number of training examples per class and keep the validation set unchanged. To ensure that our methods apply to a variety of settings, we consider two types of imbalance: long-tailed imbalance and step imbalance. We use imbalance ratio $\rho$ to denote the ratio between sample sizes of the most frequent and least frequent class, i.e., $\rho = {{\max_{i}{\{ n_{i}\}}}/{\min_{i}{\{ n_{i}\}}}}$. Long-tailed imbalance follows an exponential decay in sample sizes across different classes. For step imbalance setting, all minority classes have the same sample size, as do all frequent classes. This gives a clear distinction between minority classes and frequent classes, which is particularly useful for ablation study.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Experimental results on CIFAR", "weight": 1.0} -->

We further define the fraction of minority classes as $\mu$. By default we set $\mu = 0.5$ for all experiments.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Experimental results on CIFAR", "weight": 1.0} -->

We report the top-1 validation error of various methods for imbalanced versions of CIFAR-10 and CIFAR-100 in Table 2. Our proposed approach is LDAM-DRW, but we also include a various combination of our two techniques with other losses and training schedule for our ablation study.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Experimental results on CIFAR", "weight": 1.0} -->

We first show that the proposed label-distribution-aware margin cross-entropy loss is superior to pure cross-entropy loss and one of its variants tailored for imbalanced data, focal loss, while no data-rebalance learning schedule is applied. We also demonstrate that our full pipeline outperforms the previous state-of-the-arts by a large margin. To further demonstrate that the proposed LDAM loss is essential, we compare it with regularizing by a uniform margin across all classes under the setting of cross-entropy loss and hinge loss. We use M-DRW to denote the algorithm that uses a cross-entropy loss with uniform margin to replace LDAM, namely, the $\Delta_{j}$ in equation is chosen to be a tuned constant that does not depend on the class $j$. Hinge loss (HG) suffers from optimization issues with 100 classes so we constrain its experiment setting with CIFAR-10 only.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Experimental results on CIFAR", "weight": 1.0} -->

Imbalanced but known test label distribution: We also test the performance of an extension of our algorithm in the setting where the test label distribution is known but not uniform. Please see Section C.5 for details.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Visual recognition on iNaturalist 2018 and imbalanced Tiny ImageNet", "weight": 1.0} -->

We further verify the effectiveness of our method on large-scale imbalanced datasets. The iNatualist species classification and detection dataset is a real-world large-scale imbalanced dataset which has 437,513 training images with a total of 8,142 classes in its 2018 version. We adopt the official training and validation splits for our experiments. The training datasets have a long-tailed label distribution and the validation set is designed to have a balanced label distribution. We use ResNet-50 as the backbone network across all experiments for iNaturalist 2018. Table 3 summarizes top-1 validation error for iNaturalist 2018. Notably, our full pipeline is able to outperform the ERM baseline by 10.86% and previous state-of-the-art by 6.88% in top-1 error. Please refer to Appendix C.2 for results on imbalanced Tiny ImageNet.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Ablation study", "weight": 1.0} -->

Evaluating generalization on minority classes. To better understand the improvement of our algorithms, we show per-class errors of different methods in Figure 3 on imbalanced CIFAR-10. Please see the caption there for discussions.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Ablation study", "weight": 1.0} -->

Evaluating deferred re-balancing schedule. We compare the learning curves of deferred re-balancing schedule with other baselines in Figure 3. In Figure 6 of Section C.3, we further show that even though ERM in the first stage has slightly worse or comparable balanced test error compared to RW and RS, in fact the features (the last-but-one layer activations) learned by ERM are better than those by RW and RS. This agrees with our intuition that the second stage of DRW, starting from better features, adjusts the decision boundary and locally fine-tunes the features.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We propose two methods for training on imbalanced datasets, label-distribution-aware margin loss (LDAM), and a deferred re-weighting (DRW) training schedule. Our methods achieve significantly improved performance on a variety of benchmark vision tasks. Furthermore, we provide a theoretically-principled justification of LDAM by showing that it optimizes a uniform-label generalization error bound. For DRW, we believe that deferring re-weighting lets the model avoid the drawbacks associated with re-weighting or re-sampling until after it learns a good initial representation (see some analysis in Figure 3 and Figure 6). However, the precise explanation for DRW's success is not fully theoretically clear, and we leave this as a direction for future work.
