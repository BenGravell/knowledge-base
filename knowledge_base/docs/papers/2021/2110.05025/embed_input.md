<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Self-supervised Learning Is More Robust to Dataset Imbalance

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Self-supervised learning (SSL) is a scalable way to learn general visual representations since it learns without labels. However, large-scale unlabeled datasets in the wild often have long-tailed label distributions, where we know little about the behavior of SSL. In this work, we systematically investigate self-supervised learning under dataset imbalance. First, we find out via extensive experiments that off-the-shelf self-supervised representations are already more robust to class imbalance than supervised representations. The performance gap between balanced and imbalanced pre-training with SSL is significantly smaller than the gap with supervised learning, across sample sizes, for both in-domain and, especially, out-of-domain evaluation. Second, towards understanding the robustness of SSL, we hypothesize that SSL learns richer features from frequent data: it may learn label-irrelevant-but-transferable features that help classify the rare classes and downstream tasks. In contrast, supervised learning has no incentive to learn features irrelevant to the labels from frequent examples. We validate this hypothesis with semi-synthetic experiments and theoretical analyses on a simplified setting.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Third, inspired by the theoretical insights, we devise a re-weighted regularization technique that consistently improves the SSL representation quality on imbalanced datasets with several evaluation criteria, closing the small gap between balanced and imbalanced datasets with the same number of examples.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Self-supervised learning (SSL) is an important paradigm of machine learning, because it can leverage the availability of large-scale unlabeled datasets to learn representations for a wide range of downstream tasks and datasets. Current SSL algorithms are mostly trained on curated, balanced datasets, but large-scale unlabeled datasets in the wild are inevitably imbalanced with a long-tailed label distribution. Curating a class-balanced unlabeled dataset requires the knowledge of labels, which defeats the purpose of leveraging unlabeled data by SSL.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The behavior of SSL algorithms under dataset imbalance remains largely underexplored in the literature, but extensive studies do not bode well for supervised learning (SL) with imbalanced datasets. The performance of vanilla supervised methods degrades significantly on class-imbalanced datasets, posing challenges to practical applications such as instance segmentation and depth estimation. Many recent works address this issue with various regularization and re-weighting/re-sampling techniques.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we systematically investigate the representation quality of SSL algorithms under class imbalance. Perhaps surprisingly, we find out that off-the-shelf SSL representations are already more robust to dataset imbalance than the representations learned by supervised pre-training. We evaluate the representation quality by linear probe on in-domain (ID) data and finetuning on out-of-domain (OOD) data. We compare the robustness of SL and SSL representations by computing the gap between the performance of the representations pre-trained on balanced and imbalanced datasets of the same sizes. We observe that the balance-imbalance gap for SSL is much smaller than SL, under a variety of configurations with varying dataset sizes and imbalance ratios and with both ID and OOD evaluations (see Figure 1 and Section 2 for more details). This robustness holds even with the same number of samples for SL and SSL, although SSL does not require labels and hence can be more easily applied to larger datasets than SL.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Why is SSL more robust to dataset imbalance? We identify the following underlying cause to answer this fundamental question: SSL learns richer features from the frequent classes than SL does. These features may help classify the rare classes under ID evaluation and are transferable to the downstream tasks under OOD evaluation. For simplicity, consider the situation where rare classes have so limited data that both SL and SSL models overfit to the rare data. In this case, it is important for the models to learn diverse features from the frequent classes which can help classify the rare classes. Supervised learning is only incentivized to learn those features relevant to predicting frequent classes and may ignore other features. In contrast, SSL may learn the structures within the frequent classes better---because it is not supervised or incentivized by any labels, it can learn not only the label-relevant features but also other interesting features capturing the intrinsic properties of the input distribution, which may generalize/transfer better to rare classes and downstream tasks.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We empirically validate this intuition by visualizing the features on a semi-synthetic dataset where the label-relevant features and label-irrelevant-but-transferable features are prominently seen by design (cf. Section 3.2). In addition, we construct a toy example where we can rigorously prove the difference between self-supervised and supervised features in Section 3.1.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, given our theoretical insights, we take a step towards further improving SSL algorithms, closing the small gap between SSL on balanced and imbalanced datasets. We identify the generalization gap between the empirical and population pre-training losses on rare data as the key to improvements.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

To this end, we design a simple algorithm that first roughly estimates the density of examples with kernel density estimation and then applies a larger sharpness-based regularization to the estimated rare examples. Our algorithm consistently improves the representation quality under several evaluation protocols.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We sum up our contributions as follows. We are the first to systematically investigate the robustness of self-supervised representation learning to dataset imbalance. We propose and validate an explanation of this robustness of SSL, empirically and theoretically. We propose a principled method to improve SSL under unknown dataset imbalance.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Exploring the Effect of Class Imbalance on SSL", "weight": 1.0} -->

Dataset class imbalance can pose challenge to self-supervised learning in the wild. Without access to labels, we cannot know in advance whether a large-scale unlabeled dataset is imbalanced. Hence, we need to study how SSL will behave under dataset imbalance to deploy SSL in the wild safely. In this section, we systematically investigate the effect of class imbalance on self-supervised representations with experiments.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Class-imbalanced pre-training datasets. We assume the datapoints / inputs are in ${\mathbb{R}}^{d}$ and come from $C$ underlying classes. Let $x$ denote the input and $y$ denote the corresponding label. Supervised pre-training algorithms have access to the inputs and corresponding labels, whereas self-supervised pre-training only observes the inputs. Given a pre-training distribution $\mathcal{P}$ over over ${\mathbb{R}}^{d} \times {\lbrack C\rbrack}$, let $r$ denote the ratio of class imbalance. That is, $r$ is the ratio between the probability of the rarest class and the most frequent class: $r = \frac{\min_{j \in {\lbrack C\rbrack}}{\mathcal{P}{({y = j})}}}{\max_{j \in {\lbrack C\rbrack}}{\mathcal{P}{({y = j})}}} \leq 1$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We will construct distributions with varying imbalance ratios and use $\mathcal{P}^{r}$ to denote the distribution with ratio $r$. We also use $\mathcal{P}^{\text{bal}}$ for the case where $r = 1$, i.e. the dataset is balanced. Large-scale data in the wild often follow heavily long-tailed label distributions where $r$ is small. We assume that for any class $j \in {\lbrack C\rbrack}$, the class-conditional distribution $\mathcal{P}^{r}{({\left. x \middle| y \right. = j})}$ is the same across balanced and imbalanced datasets for all $r$. The pre-training dataset ${\hat{\mathcal{P}}}_{n}^{r}$ consists of $n$ i.i.d. samples from $\mathcal{P}^{r}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Pre-trained models. A feature extractor is a function $f_{\phi}:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{m}}$ parameterized by neural network parameters $\phi$, which maps inputs to representations. A linear head is a linear function $g_{\theta}:{{\mathbb{R}}^{m}\rightarrow{\mathbb{R}}^{C}}$, which can be composed with $f_{\phi}$ to produce the predictions. SSL algorithms learn $\phi$ from unlabeled data. Supervised pre-training learns the feature extractor and the linear head from labeled data. We drop the head and only evaluate the quality of feature extractor $\phi$.^11^1It is well-known that the composition of the head and features learned from supervised learning is more sensitive to imbalanced dataset than feature extractor $\phi$ itself. Please also see Table 3 in Appendix C for a comparison between CRT and Supervised.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Following the standard evaluation protocol in prior works, we measure the quality of learned representations on both in-domain and out-of-domain datasets with either linear probe or fine-tuning, as detailed below.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

In-domain (ID) evaluation tests the performance of representations on the balanced in-domain distribution $\mathcal{P}^{\text{bal}}$ with linear probe. Given a feature extractor $f_{\phi}$ pre-trained on a pre-training dataset ${\hat{\mathcal{P}}}_{n}^{r}$ with $n$ data points and imbalance ratio $r$, we train a $C$-way linear classifier $\theta$ on top of $f_{\phi}$ on a balanced dataset^22^2We essentially use the largest balanced labeled ID dataset for this evaluation, which oftentimes means the entire curated training dataset, such as CIFAR-10 with 50,000 examples and ImageNet with 1,281,167 examples. sampled i.i.d. from $\mathcal{P}^{\text{bal}}$. We evaluate the representation quality with the top-1 accuracy of the learned linear head on $\mathcal{P}^{\text{bal}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We denote the ID accuracy of supervised pre-trained representations by $A_{\text{ID}}^{\text{SL}}{(n,r)}$. Note that $A_{\text{ID}}^{\text{SL}}{(n,1)}$ stands for the result with balanced pre-training dataset. For SSL representations, we denote the accuracy by $A_{\text{ID}}^{\text{SSL}}{(n,r)}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Out-of-domain (OOD) evaluation tests the performance of representations by fine-tuning the feature extractor and the head on a (or multiple) downstream target distribution $\mathcal{P}_{t}$. Starting from a feature extractor $f_{\phi}$ (pre-trained on a dataset of size $n$ and imbalance ratio $r$) and a randomly initialized classifier $\theta$, we fine-tune $\phi$ and $\theta$ on the target dataset ${\hat{\mathcal{P}}}_{t}$, and evaluate the representation quality by the expected top-1 accuracy on $\mathcal{P}_{t}$. We use $A_{\text{OOD}}^{\text{SL}}{(n,r)}$ and $A_{\text{OOD}}^{\text{SSL}}{(n,r)}$ to denote the resulting accuracies of supervised and self-supervised representations, respectively.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Summary of varying factors. We aim to study the effect of class imbalance to feature qualities on a diverse set of configurations with the following varying factors: the number of examples in pre-training $n$, the imbalance ratio of the pre-training dataset $r$, ID or OOD evaluation, and self-supervised learning algorithms: MoCo v2, or SimSiam.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Datasets. We pre-train the representations on variants of ImageNet or CIFAR-10 with a wide range of numbers of examples and ratios of imbalance. Following Liu et al., we consider exponential and Pareto distributions, which closely simulate the natural long-tailed distributions. We consider imbalance ratio in $\{ 1,0.004,0.0025\}$ for ImageNet and $\{ 1,0.1,0.01\}$ for CIFAR-10. For each imbalance ratio, we further downsample the dataset with a sampling ratio in $\{ 0.75,0.5,0.25,0.125\}$ to form datasets with varying sizes. Note that we fix the variant of the dataset when comparing different algorithms. For ID evaluation, we use the original CIFAR-10 or ImageNet training set for the training phase of linear probe and use the original validation set for the final evaluation. For OOD evaluation of representations learned on CIFAR-10, we use STL-10 as the target /downstream dataset.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

For OOD evaluation of representations learned on ImageNet, we fine-tune the pre-trained feature extractors on CUB-200, Stanford Cars, Oxford Pets, and Aircrafts, and measure the representation quality with average accuracy on the downstream tasks.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Experimental Setup", "weight": 1.0} -->

Models. We use ResNet-18 on CIFAR-10 and ResNet-50 on ImageNet as backbones. For supervised pre-training, we follow the standard protocol of He et al. and Kang et al.. For self-supervised pre-training, we consider MoCo v2 and SimSiam. We run each evaluation experiment with $3$ seeds and report the average and standard deviation in the figures. Further implementation details and additional results are deferred to Section A.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Self-supervised Learning is More Robust than Supervised Learning to Dataset Imbalance", "weight": 1.0} -->

In Figure 2, we plot the results of ID and OOD evaluations, respectively. For both ID and OOD evaluations, the gap between SSL representations learned on balanced and imbalanced datasets with the same number of pre-training examples, i.e., ${A^{\text{SSL}}{(n,1)}} - {A^{\text{SSL}}{(n,r)}}$, is smaller than the gap of supervised representations, i.e., ${A^{\text{SL}}{(n,1)}} - {A^{\text{SL}}{(n,r)}}$, consistently in all configurations.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Self-supervised Learning is More Robust than Supervised Learning to Dataset Imbalance", "weight": 1.0} -->

Furthermore, we compute the relative accuracy gap to balanced dataset ${\Delta^{\text{SSL}}{(n,r)}} \triangleq {{{({{A^{\text{SSL}}{(n,1)}} - {A^{\text{SSL}}{(n,r)}}})}/A^{\text{SSL}}}{(n,1)}}$ in Figure 1. We observe that with the same number of pre-training examples, the relative gap of SSL representations between balanced and imbalanced datasets is smaller than that of SL representations across the board, Also note that comparing the robustness with the same number of data is actually in favor of SL, because SSL is more easily applied to larger datasets without the need of collecting labels.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Self-supervised Learning is More Robust than Supervised Learning to Dataset Imbalance", "weight": 1.0} -->

ID vs. OOD. As shown in Figure 2, we observe that representations from supervised pre-training perform better than self-supervised pre-training in ID evaluation with reasonably large $n$, while self-supervised pre-training is better in OOD evaluation. This phenomenon is orthogonal to our observation that SSL is more robust to dataset imbalance, and is consistent with recent works (e.g., Chen et al.; He et al. ) which also observed that SSL performs slightly worse than supervised learning on balanced ID evaluation but better on OOD tasks.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Analysis", "weight": 1.0} -->

We have found out with extensive experiments that self-supervised representations are more robust to class imbalance than supervised representations. A natural and fundamental question arises: where does the robustness stem from? In this section, we propose a possible reason and justify it with theoretical and empirical analyses.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Analysis", "weight": 1.0} -->

SSL learns richer features from frequent data that are transferable to rare data. The rare classes of the imbalanced dataset can contain only a few examples, making it hard to learn proper features to classify the rare classes. In this case, one may want to resort to the features learned from the frequent classes for help. However, due to the supervised nature of classification tasks, the supervised model mainly learns the features that help classify the frequent classes and may neglect other features which can transfer to the rare classes and potentially the downstream tasks. Partly because of this, Jamal et al. explicitly encourage the model to learn features transferable from the frequent to the rare classes with meta-learning. In contrast, in self-supervised learning, without the bias or incentive from the labels, the models can learn richer features that capture the intrinsic structures of the inputs---both features useful for classifying the frequent classes and features transferable to the rare classes.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Rigorous Analysis on A Toy Setting", "weight": 1.0} -->

To justify the above conjecture, we instantiate supervised and self-supervised learning in a setting where the features helpful to classify the frequent classes and features transferable to the rare classes can be clearly separated. In this case, we prove that self-supervised learning learns better features than supervised learning.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Rigorous Analysis on A Toy Setting", "weight": 1.0} -->

Data distribution. Let $e_{1},e_{2}$ be two orthogonal unit-norm vectors in the $d$-dimensional Euclidean space. Consider the following pre-training distribution $\mathcal{P}$ of a 3-way classification problem, where the class label $y \in {\lbrack 3\rbrack}$. The input $x$ is generated as follows. Let $\tau > 0$ and $\rho > 0$ be hyperparameters of the distribution. First sample $q$ uniformly from $\{ 0,1\}$ and $\xi \sim {\mathcal{N}{(0,I)}}$ from Gaussian distribution. For the first class ($y = 1$), set $x = {{e_{1} - {q\taue_{2}}} + {\rho\xi}}$. For the second class ($y = 2$), set $x = {{{- e_{1}} - {q\taue_{2}}} + {\rho\xi}}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Rigorous Analysis on A Toy Setting", "weight": 1.0} -->

For the third class ($y = 3$), set $x = {e_{2} + {\rho\xi}}$. Classes 1 and 2 are frequent classes, while class 3 is the rare class, i.e., ${\frac{\mathcal{P}{({y = 3})}}{\mathcal{P}{({y = 1})}},\frac{\mathcal{P}{({y = 3})}}{\mathcal{P}{({y = 2})}}} = {o{}}$. See Figure 3 for an illustration of this data distribution. In this case, both $e_{1}$ and $e_{2}$ are features from the frequent classes 1 and 2. However, only $e_{1}$ helps classify the frequent classes and only $e_{2}$ can be transferred to the rare classes.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Rigorous Analysis on A Toy Setting", "weight": 1.0} -->

Main intuitions. We compare the features learned by SSL and supervised learning on an imbalanced dataset that contains an abundant (poly in $d$) number of data from the frequent classes but only a small (sublinear in $d$) number of data from the rare class. The key intuition behind our analysis is that supervised learning learns only the $e_{1}$ direction (which helps classify class 1 vs. class 2) and some random direction that overfits to the rare class. In contrast, self-supervised learning learns both $e_{1}$ and $e_{2}$ directions from the frequent classes. Since how well the feature helps classify the rare class (in ID evaluation) depends on how much it correlates with the $e_{2}$ direction, SSL provably learns features that help classify the rare class, while supervised learning fails. This intuition is formalized by the following theorem.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Illustrative Semi-synthetic Experiments", "weight": 1.0} -->

In the previous subsection, we have shown that self-supervised learning provably learns label-irrelevant-but-transferable features from the frequent classes which can help classify the rare class in the toy case, while supervised learning mainly focuses on the label-relevant features. However, in real-world datasets, it is intractable to distinguish the two groups of features. To amplify this effect in a real-world dataset and highlight the insight of the theoretical analysis, we design a semi-synthetic experiment on SimCLR to validate our conclusion.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Illustrative Semi-synthetic Experiments", "weight": 1.0} -->

Dataset. In the theoretical analysis above, the frequent classes contain both features related to the classification of frequent classes and features transferable to the the rare classes. Similarly, we consider an imbalanced pre-training dataset with two groups of features modified from CIFAR-10 as shown in Figure 4 (Left). We construct classes 1-5 as the frequent classes, where each class contains 5000 examples. Classes 6-10 are the rare classes, where each class has 10 examples. In this case, the ratio of imbalance $r = 0.002$. Each image from classes 1-5 consists of a left half and a right half. The left half of an example is from classes 1-5 of the original CIFAR-10 and corresponds to the label of that example. The right half is from a random image of CIFAR-10, which is label-irrelevant.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Illustrative Semi-synthetic Experiments", "weight": 1.0} -->

In contrast, the left half of an example from classes 6-10 is blank, whereas the right half is label-relevant and from classes 6-10 of the original CIFAR-10. In this setting, features from the left halves of the images are correlated to the classification of the frequent classes, while features from the right halves are label-irrelevant for the frequent classes, but can help classify the rare classes. Note that features from the right halves cannot be directly learned from the rare classes since they have only 10 examples per class. This is consistent with the setting of Theorem 3.1.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Illustrative Semi-synthetic Experiments", "weight": 1.0} -->

Pre-training. We pre-train the representations on the semi-synthetic imbalanced dataset. For supervised learning, we use ResNet-50 on this 10-way classification task. For self-supervised learning, we use SimCLR with ResNet-50. To avoid confusing the left and right parts, we disable the random horizontal flip in the data augmentation. After pre-training, we fix the representations and train a linear classifier on top of the representations with balanced data from the 5 rare classes (25000 examples in total) to test if the model learns proper features for the rare classes during pre-training. In Figure 4 (Right), we test the classifier on the rare classes. In Figure 4 (Middle), we further visualize the Grad-CAM of the representations on the held-out set^66^6CIFAR images are of low resolution. For visualization, we use high resolution version of the CIFAR-10 images in Figure 4 (Middle). We also provide the visualization on original CIFAR-10 images in Figure 7..

<!-- chunk {"id": "body-0037", "role": "body", "section": "Illustrative Semi-synthetic Experiments", "weight": 1.0} -->

Results. As a sanity check, we first pre-train a supervised model with only the 50 rare examples and train the linear head classifier with 25000 examples from the rare classes (5-way classification) to see if the model can learn proper features for the rare classes with only rare examples (Supervised-rare in Figure 4 (Right)). As expected, the accuracy is $36.5\%$, which is almost the same as randomly initialized representations with trained head classifier, indicating that the model cannot learn the features for the rare classes with only rare examples due to the limited number of examples. We then compare supervised learning with self-supervised learning on the whole semi-synthetic dataset. In Figure 4 (Right), self-supervised representations perform much better than supervised representations on the rare classes ($70.1\%$ vs $44.3\%$). We further visualize the activation maps of representations with Grad-CAM. Supervised learning mostly activate the left halves of the examples for both frequent and rare classes, indicating that it mainly learn features on the left.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Illustrative Semi-synthetic Experiments", "weight": 1.0} -->

In sharp contrast, self-supervised learning activates the whole image on the frequent examples and the right part on the rare examples, indicating that it learns features from both parts.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Improving SSL on Imbalanced Datasets with Regularization", "weight": 1.0} -->

In this section, we aim to further improve the performance of SSL to close the gap between imbalanced and balanced datasets. Many prior works on imbalanced supervised learning regularize the rare classes more strongly, motivated by the observation that the rare classes suffer from more overfitting. Inspired by these works, we compute the generalization gaps (i.e., the differences between empirical and validation pre-training losses) on frequent and rare classes for the step-imbalance CIFAR-10 datasets (where 5 classes are frequent class with 5000 examples per class and the rest are rare with 50 examples per class). Indeed, as shown in Table 1 (a), we still observe a similar phenomenon---the frequent classes have much smaller pre-training generalization gap than the rare classes (0.035 vs. 0.081), which indicates the necessity of more regularization on the rare classes.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Improving SSL on Imbalanced Datasets with Regularization", "weight": 1.0} -->

We need a data-dependent regularizer that can have different effects on rare and frequent examples. Thus, weight decay or dropout are not suitable. The prior work of Cao et al. regularizes the rare classes more strongly with larger margin, but it does not apply to SSL where no labels are available. Inspired by Cao et al., we adapt sharpness-aware minimization (SAM) to imbalanced SSL.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Improving SSL on Imbalanced Datasets with Regularization", "weight": 1.0} -->

Reweighted SAM (rwSAM). SAM improves model generalization by penalizing loss sharpness. Suppose the training loss of the representation $f_{\phi}$ is $\hat{L}{(\phi)}$, i.e. ${\hat{L}{(\phi)}} = {\frac{1}{n}{\sum_{j = 1}^{n}{\ell{(x_{j},\phi)}}}}$. SAM seeks parameters where the loss is uniformly low in the neighboring area, To take the weight of different examples into account, we add reweighting to the inner maximization step of SAM. Intuitively, we wish the optimization landscape to be flatter for rare examples, which is in effect regularizing the model more on rare examples.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Improving SSL on Imbalanced Datasets with Regularization", "weight": 1.0} -->

Concretely, consider the reweighted training loss associated with weight vector $w \in {\mathbb{R}}^{n}$, ${{\hat{L}}_{w}{(\phi)}} = {\frac{1}{n}{\sum_{j = 1}^{n}{w_{j}\ell{(x_{j},\phi)}}}}$. The reweighted SAM objective re-weights the regularization-related terms (e.g., $\epsilon_{w}$) but not the training loss $\hat{L}$: Assigning Weight with Kernel Density Estimation. The weight $w_{j}$ of an example $x_{j}$ should be inversely correlated with the frequency of the corresponding class $y_{j}$. However, we have no access to the labels. In order to approximate the frequency of examples, we use kernel density estimation on top of the representations $f_{\phi}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Experiments", "weight": 1.0} -->

We test the proposed rwSAM on CIFAR-10 with step or exponential imbalance and ImageNet-LT. After self-supervised pre-training on the long-tailed dataset, we evaluate the representations by linear probing on the balanced in-domain dataset and fine-tuning on downstream target datasets. For and, we compare with SSL, SSL+SAM (w/o reweighting), and SSL balanced, which learns the representations on the balanced dataset with the same number of examples. Implementation details and additional results are deferred to Section C. Code is available at Results. Table 1 (a) summarizes results on long tailed CIFAR-10. With both step and exponential imbalance, rwSAM improves the performance of SimSiam over $1\%$, and even surpasses the performance of SimSiam on balanced CIFAR-10 with the same number of examples. Note that compared to SimSiam, rwSAM closes the generalization gap of pre-training loss on rare examples from $0.081$ to $0.066$, which verifies the effect of re-weighted regularization.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Experiments", "weight": 1.0} -->

In Table 1 (b), we provide the result of fine-tuning on downstream tasks with representations pre-trained on ImageNet-LT. The proposed method improves the transferability of representations to downstream tasks consistently.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Supervised Learning with Dataset Imbalance", "weight": 1.0} -->

There exists a long line of works studying supervised imbalanced classification. Early works on ensemble learning adjusted the boosting and bagging algorithms with resampling in the imbalanced setting. Classical methods include resampling and reweighting. Hart; Kubat et al.; Chawla et al.; He et al.; Ando and Huang; Buda et al.; Hu et al. proposed to re-sample the data to make the frequent and rare classes appear with equal frequency in training. Re-weighting assigns different weights for head and tail classes and eases the optimization difficulty under class imbalance. Byrd and Lipton empirically studied the effect of importance weighting and found out that importance weighting does not change the solution without regularization. Xu et al. justified this finding with theoretical analysis based on the implicit bias of gradient descend on separable data.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Supervised Learning with Dataset Imbalance", "weight": 1.0} -->

Cao et al. initiated the idea of using re-weighted regularization and proposed the principle of regularizing rare classes more heavily. Re-weighted regularizaton is shown to be typically more effective than re-weighting or re-sampling the losses. Cao et al. proposed to regularize the local curvature of loss on imbalanced and noisy datasets.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Supervised Learning with Dataset Imbalance", "weight": 1.0} -->

Works in the modern deep learning era also designed specific losses or training pipelines for imbalanced recognition. Lin et al. proposed to focus on hard examples to prevents easy examples from overwhelming the models during training. Meta-learning approaches meta-learned the weight or the ensemble. Liu et al.; Jamal et al.; Liu et al. improved the performance on the rare examples by explicitly encourages transfer learning. Re-calibration methods adjust the logits of the outputs with re-weighting.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Supervised Learning with Dataset Imbalance", "weight": 1.0} -->

Several works also studied the supervised representations under dataset imbalance. Kang et al.; Wang et al. found out that the representations of supervised learning perform better than the classifier itself with class imbalance. Yang and Xu studied the effect of self-training and self-supervised pre-training on supervised imbalanced recognition classifiers. In contrast, the focus of our paper is the effect of class imbalance on self-supervised representations.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Self-supervised Learning", "weight": 1.0} -->

Earlier works on self-supervised learning learned visual representations by context prediction, solving puzzles, and rotation prediction. Recent works on self-supervised learning successfully learn representations that approach the supervised baseline on ImageNet and various downstream tasks, and closed the gap with supervised pre-training. Contrastive learning methods attract positive pairs and drive apart negative pairs. Siamese networks predict the output of the other branch, and use stop-gradient to avoid collapsing. Clustering methods learn representations by performing clustering on the representations and improve the representations with cluster index. Cole et al. investigated the effect of data quantity and task granularity on self-supervised representations. Goyal et al. studied self-supervised methods on large scale datasets in the wild, but they do not consider dataset imbalance explicitly. Kotar et al. studied whether dataset imbalance can have a significant impact on contrastive learning representations. Madaan et al. found out that self-supervised representations are better at continual learning than supervised representations. Several works have also theoretically studied the success of self-supervised learning. Our analysis in Section 3.1 is partially inspired by the work HaoChen et al..

<!-- chunk {"id": "body-0050", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Our paper is the first to study the problem of robustness to imbalanced training of self-supervised representations. We discover that self-supervised representations are more robust to class imbalance than supervised representations and explore the underlying cause of this phenomenon. As supervised learning is still the de facto standard for pre-training, our work should encourage practitioners to use SSL for pre-training instead, or at least consider evaluating the impact of imbalanced pre-training on their downstream task. Our experiments mainly focus on vision datasets. Future works can study the effect of dataset imbalance on NLP datasets, where self-supervised pre-training is a dominant approach. We hope our study can inspire analysis of self-supervised learning in broader environments in the wild such as domain shift, and provide insights for the design of future unsupervised learning methods.
