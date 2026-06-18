<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Do CIFAR-10 Classifiers Generalize to CIFAR-10?

Topics include Deep learning, Classifiers, Accuracy, Learning, Machine learning, Test set.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Machine learning is currently dominated by largely experimental work focused on improvements in a few key tasks. However, the impressive accuracy numbers of the best performing models are questionable because the same test sets have been used to select these models for multiple years now. To understand the danger of overfitting, we measure the accuracy of CIFAR-10 classifiers by creating a new test set of truly unseen images. Although we ensure that the new test set is as close to the original data distribution as possible, we find a large drop in accuracy (4% to 10%) for a broad range of deep learning models. Yet more recent models with higher original accuracy show a smaller drop and better overall performance, indicating that this drop is likely not due to overfitting based on adaptivity. Instead, we view our results as evidence that current accuracy numbers are brittle and susceptible to even minute natural variations in the data distribution.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Over the past five years, machine learning has become a decidedly experimental field. Driven by a surge of research in deep learning, the majority of published papers has embraced a paradigm where the main justification for a new learning technique is its improved performance on a few key benchmarks. At the same time, there are few explanations as to *why* a proposed technique is a reliable improvement over prior work. Instead, our sense of progress largely rests on a small number of standard benchmarks such as CIFAR-10, ImageNet, or MuJoCo.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

*How reliable are our current measures of progress in machine learning?*

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Properly evaluating progress in machine learning is subtle. After all, the goal of a learning algorithm is to produce a model that generalizes well to *unseen data*. Since we usually do not have access to the ground truth data distribution, we instead evaluate a model's performance on a separate test set. This is indeed a principled evaluation protocol, *as long as we do not use the test set to select our models.*

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Unfortunately, we typically have limited access to new data from the same distribution. It is now commonly accepted to re-use the same test set multiple times throughout the algorithm and model design process. Examples of this practice are abundant and include both tuning hyperparameters (number of layers, etc.) within a single publication, and building on other researchers' work across publications. While there is a natural desire to compare new models to previous results, it is evident that the current research methodology undermines the key assumption that the classifiers are independent of the test set. This mismatch presents a clear danger because the research community could easily be designing models that only work well on the specific test set but actually fail to generalize to new data.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Reproducibility Study on CIFAR-10", "weight": 1.0} -->

To understand how reliable current progress in machine learning is, we design and conduct a new type of reproducibility study. Its main goal is to measure how well contemporary classifiers generalize to new, truly unseen data from the same distribution. We focus on the standard CIFAR-10 dataset since its transparent creation process makes it particularly well suited to this task. Moreover, CIFAR-10 has been the focus of intense research for almost 10 years now. Due to the competitive nature of this process, it is an excellent test case for investigating whether adaptivity has led to overfitting.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Reproducibility Study on CIFAR-10", "weight": 1.0} -->

First, we curate a new test set where we carefully match the *sub*-class distribution of our new test set to the original CIFAR-10 dataset.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Reproducibility Study on CIFAR-10", "weight": 1.0} -->

After collecting about 2000 new images, we evaluate the performance of 30 image classification models on our new test set. The results show two overarching phenomena. On the one hand, there is a significant drop in accuracy from the original test set to our new test set. For instance, VGG and ResNet architectures drop from their well-established 93% accuracy to about 85% on our new test set. On the other hand, we find the performance on the existing test set to be highly predictive of the performance on our new test set. Even small incremental improvements on CIFAR-10 often transfer to truly held-out data.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Reproducibility Study on CIFAR-10", "weight": 1.0} -->

Motivated by this discrepancy between the original and new accuracies, the third step investigates multiple hypotheses for explaining this gap. A natural conjecture is that re-tuning standard hyperparameters recovers some of the observed gap, but we find only a small effect of about 0.6% improvement. While this and further experiments can explain some of the accuracy loss, a significant gap remains.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Reproducibility Study on CIFAR-10", "weight": 1.0} -->

Overall, our results paint an unexpected picture of progress in contemporary machine learning. In spite of adapting to the CIFAR-10 test set for several years, there has been no stagnation. The top model is still a recent Shake-Shake network with Cutout regularization. Moreover, its advantage over a standard ResNet *increased* from 4% to 8% on our new test set. This shows that the current research methodology of "attacking" a test set for an extended period of time is surprisingly resilient to overfitting.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Reproducibility Study on CIFAR-10", "weight": 1.0} -->

But our results also cast doubt on the robustness of current classifiers. While our new dataset presents only a minute distributional shift, the classification accuracy of widely used models drops significantly. For instance, the aforementioned accuracy loss of VGG and ResNet architectures corresponds to multiple years of progress on CIFAR-10. Note that the distributional shift induced by our experiment is neither adversarial nor the result of a different data source. So even in benign settings, distribution shift poses a serious challenge and questions to what extent current models truly generalize.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Formal Setup", "weight": 1.0} -->

Before we describe our specific experiment on CIFAR-10, we start with a formal description of our problem of interest. We adopt the standard classification setup and posit the existence of a "true" underlying data distribution $\mathcal{D}$ over labeled examples $(x,y)$. The goal is to find a model $\hat{f}$ that minimizes the population loss

<!-- chunk {"id": "body-0014", "role": "body", "section": "Formal Setup", "weight": 1.0} -->

For a sufficiently large test set $D_{\text{test}}$, standard concentration results show that $L_{D_{\text{test}}}{(\hat{f})}$ is a good approximation of $L_{\mathcal{D}}{(\hat{f})}$ as long as the classifier $\hat{f}$ does not depend on $D_{\text{test}}$. This is arguably the core assumption underlying machine learning since it allows us to argue that our classifier $\hat{f}$ truly *generalizes* (as opposed to say only memorizing the data).

<!-- chunk {"id": "body-0015", "role": "body", "section": "Formal Setup", "weight": 1.0} -->

However, it is often hard to argue when a new test set is drawn from exactly the same distribution $\mathcal{D}$ since we usually lack a precise definition of this distribution. So to obtain truly i.i.d. test sets, we ideally would have collected a larger initial dataset that we then randomly split into $D_{\text{train}}$, $D_{\text{test}}$, and $D_{\text{test}}^{\prime}$. Unfortunately, we usually do not have such an exact setup to reproduce accuracy numbers on a new test set. In this paper, we instead mimic the data generating distribution $\mathcal{D}$ as closely as possible by repeating the dataset creation process that originally derived $D_{\text{train}}$ and $D_{\text{test}}$ from a larger dataset. While this method does not necessarily generate a test set that is an i.i.d. draw from the original data generating distribution, it is a close approximation.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Dataset Creation Methodology", "weight": 1.0} -->

To investigate how well current image classifiers generalize to truly unseen data, we collect a new test set for the CIFAR-10 image classification dataset.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Dataset Creation Methodology", "weight": 1.0} -->

CIFAR-10 is currently one of the most widely used datasets in machine learning and serves as a test ground for many computer vision methods. A concrete measure of popularity is the fact that CIFAR-10 was the second most common dataset in NIPS 2017 (after MNIST).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Dataset Creation Methodology", "weight": 1.0} -->

The dataset creation process for CIFAR-10 is transparent and well documented. Importantly, CIFAR-10 draws from the larger Tiny Images repository that has significantly more fine-grained labels. This makes it possible to conduct an experiment where we minimize various forms of distribution shift in our new test set.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Dataset Creation Methodology", "weight": 1.0} -->

CIFAR-10 poses a difficult enough problem so that the dataset is still the subject of active research (e.g., see ). Moreover, there is a wide range of classification models that achieve significantly different accuracy scores. Since code for these models is published in a variety of open source repositories, they can be treated as truly independent of our new test set.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Tiny Images", "weight": 1.0} -->

The dataset contains 80 million RGB color images with resolution 32 $\times$ 32 pixels. The images are organized by roughly 75,000 *keywords* that correspond to the non-abstract nouns from the WordNet database. Each keyword was entered into multiple Internet search engines to collect roughly 1,000 to 2,500 images per keyword. It is important to note that Tiny Images is a fairly noisy dataset. Many of the images filed under a certain keyword do not clearly (or not at all) correspond to the respective keyword.

<!-- chunk {"id": "body-0021", "role": "body", "section": "CIFAR-10", "weight": 1.0} -->

The goal for the CIFAR-10 dataset was to create a cleanly labeled subset of Tiny Images. To this end, the researchers assembled a dataset consisting of ten classes with 6,000 images per class. These classes are airplane, automobile, bird, cat, deer, dog, frog, horse, ship, and truck. The standard train / test split is class-balanced and contains 50,000 training images and 10,000 test images.

<!-- chunk {"id": "body-0022", "role": "body", "section": "CIFAR-10", "weight": 1.0} -->

The CIFAR-10 creation process is well-documented. First, the researchers assembled a set of relevant keywords for each class by using the hyponym relations in WordNet. Since directly using the corresponding images from Tiny Images would not give a high quality dataset, the researchers paid student annotators to label the images from Tiny Images. The labeler instructions can be found in Appendix C of and include a set of specific guidelines (e.g., an image should not contain two object of the corresponding class). The researchers then verified the labels of the images selected by the annotators and removed near-duplicates from the dataset via an $\ell_{2}$ nearest neighbor search.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Building the New Test Set", "weight": 1.0} -->

Our overall goal was to create a new test set that is as close as possible to being drawn from the same distribution as the original CIFAR-10 dataset. One crucial aspect here is that the CIFAR-10 dataset did not exhaust any of the Tiny Image keywords it is drawn. So by collecting new images from the same keywords as CIFAR-10, our new test set can match the sub-class distribution of the original dataset.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Understanding the Sub-Class Distribution", "weight": 1.0} -->

As the first step, we determined the Tiny Image keyword for every image in the CIFAR-10 dataset. A simple nearest-neighbor search sufficed since every image in CIFAR-10 had an exact duplicate ($\ell_{2}$-distance $0$) in Tiny Images. Based on this information, we then assembled a list of the 25 most common keywords for each class. We decided on 25 keywords per class since the 250 total keywords make up more than 95% of CIFAR-10. Moreover, we wanted to avoid accidentally creating a harder dataset with infrequent keywords that the classifiers had little incentive to learn based on the original CIFAR-10 dataset.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Understanding the Sub-Class Distribution", "weight": 1.0} -->

The keyword distribution can be found in Appendix E. Inspecting this list reveals the importance of matching the sub-class distribution. For instance, the most common keyword in the airplane class is stealth_bomber and not an arguably more ordinary civilian type of airplane. In addition, the third most common keyword for the airplane class is stealth_fighter. Both types of planes are highly distinctive. There are more examples where certain sub-classes are considerably different, e.g., images from the fire_truck keyword have image statistics that are rather different from say pictures for dump_truck.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Collecting New Images", "weight": 1.0} -->

After determining the keywords, we collected corresponding images. To simulate the student / researcher split in the original CIFAR-10 collection procedure, we introduced a similar split among two authors of this paper. Author A took the role of the original student annotators and selected new suitable images for the 250 keywords. In order to ensure a close match between the original and new images for each keyword, we built a user interface that allowed Author A to first look through existing CIFAR-10 images for a given keyword and then select new candidates from the remaining pictures in Tiny Images. Author A followed the labeling guidelines in the original instruction sheet. The number of images Author A selected per keyword was so that our final dataset would contain between 2,000 and 4,000 images.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Collecting New Images", "weight": 1.0} -->

While the original CIFAR-10 test set contains 10,000 images, a test set of size 2,000 is already sufficient for a fairly small confidence interval. In particular, a conservative confidence interval (Clopper-Pearson at confidence level 95%) for accuracy 90% has size about $\pm {1\%}$ with $n =$ 2,000 (to be precise, $\lbrack{88.6\%},{\, 91.3\%}\rbrack$). Since we considered a potential discrepancy between original and new test accuracy only interesting if it was significantly larger than 1%, we decided that a new test set of size 2,000 was large enough for our study.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Collecting New Images", "weight": 1.0} -->

As with very infrequent keywords, our goal was to avoid accidentally creating a harder test set. Since some of the Tiny Image keywords have only a limited supply of remaining adequate images, we decided that a smaller target size for the new dataset would reduce bias to include images of more questionable difficulty.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Collecting New Images", "weight": 1.0} -->

After Author A had selected a set of about 9,000 candidate images, Author B adopted the role of the researchers in the original CIFAR-10 dataset creation process. In particular, Author B reviewed all candidate images and removed images that were unclear to Author B or did not conform to the labeling instructions in their opinion (some of the criteria are subjective). In the process, a small number of keywords did not have enough images remaining to reach the $n =$ 2,000 threshold. Author B then notified Author A about the respective keywords and Author A selected a further set of images for these keywords. In this process, there was only one keyword where Author A had to carefully go through all available images in Tiny Images. This keyword was alley_cat and comprises less than 0.3% of the overall CIFAR-10 dataset.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Final Assembly", "weight": 1.0} -->

After collecting a sufficient number of high-quality images for each keyword, we sampled a random subset from our pruned candidate set. The sampling procedure was such that the keyword-level distribution of our new dataset matches the keyword-level distribution of CIFAR-10 (see Appendix E). In the final stage, we again proceeded similar to the original CIFAR-10 dataset creation process and used $\ell_{2}$-nearest neighbors to filter out near duplicates. In particular, we removed near-duplicates within our new dataset and also images that had a near duplicate in the original CIFAR-10 dataset (train or test). The latter aspect is particularly important since our reproducibility study is only interesting if we evaluate on truly unseen data. Hence we manually reviewed the top-10 nearest neighbors for each image in our new test set. After removing near-duplicates in our dataset, we re-sampled the respective keywords until this process converged to our final dataset.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Final Assembly", "weight": 1.0} -->

We remark that we did not run any classifiers on our new dataset during the data collection phase of our study. In order to ensure that the new data does not depend on the existing classifiers, it is important to strictly separate the data collection phase from the following evaluation phase.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Model Performance Results", "weight": 1.0} -->

After we completed the new test set, we evaluated a broad range of image classification models. The main question was how the accuracy on the original CIFAR-10 test set compares to the accuracy on our new test set. To this end, we experimented with a broad range of classifiers spanning multiple years of machine learning research. The models include widely used convolutional networks (VGG and ResNet ), more recent architectures (ResNeXt, PyramidNet, DenseNet ), the published state-of-the-art (Shake-Drop ), and a model derived from RL-based hyperparameter search (NASNet). In addition, we also evaluated "shallow" approaches based on random features. Overall, the accuracies on the original CIFAR-10 test set range from about 80% to 97%.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Model Performance Results", "weight": 1.0} -->

For all deep architectures, we used code previously published online (see Appendix A for a list). To avoid bias due to specific model repositories or frameworks, we also evaluated two widely used architectures (VGG and ResNets) from two different sources implemented in different deep learning libraries. We wrote our own implementation for the models based on random features.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Model Performance Results", "weight": 1.0} -->

Our main results are summarized in Table 1 and Figure 2. We now describe the two important trends here and then discuss our results in Section 6.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Significant Drop in Accuracy", "weight": 1.0} -->

All models see a large drop in accuracy from the original to the new test set. The *absolute* gap is larger for models that perform worse on the original test set and smaller for models with better published CIFAR-10 accuracy. For instance, VGG and ResNet architectures see a gap of about 8% between their original accuracy (around 93%) and their new accuracy (around 85%). The best original accuracy is achieved by shake_shake_64d_cutout, which sees a roughly 4% drop from 97% to 93%. While there is some variation in the accuracy drop, no model is a clear outlier.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Significant Drop in Accuracy", "weight": 1.0} -->

In terms of *relative* error, the models with higher original accuracy tend to have a larger increase. Some of the models such as DARC, shake_shake_32d, and resnext_29_4x64d see a $3 \times$ increase in their error rate. For simpler models such as VGG, AlexNet, or ResNet, the relative error increase is in the range $1.7 \times$ to $2.3 \times$. We refer the reader to Appendix C for a table with all relative error numbers.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Few Changes in the Relative Order", "weight": 1.0} -->

When sorting the models in order of their original and new accuracy, there are few changes in the overall ranking. Models with comparable original accuracy tend to see a similar decrease in performance. In fact, Figure 2 shows that the relationship between original and new accuracy can be explained well with a linear function derived from a least squares fit.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Few Changes in the Relative Order", "weight": 1.0} -->

On the other hand, it is worth noting that some techniques give a consistently larger increase on the new test set. For instance, adding the Cutout data augmentation to a shake_shake_64d network adds only 0.12% accuracy on the original test set but gives an accuracy increase of about 1.5% on the new test set. Similarly, adding Cutout to a wide_resnet_28_10 classifiers improves the accuracy by about 1% on the original test set and 2.2% on the new test set. As another example, note that increasing the *width* of a ResNet as opposed to its *depth* provides larger benefits on the new test set.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Model for the Linear Fit", "weight": 1.0} -->

Though the linear fit observed in Figure 2 rules out that the new test set is identically distributed as the original test set, the linear relationship between the old and new test errors is striking. There are a variety of plausible explanations for this effect. For instance, posit that the original test set is composed of two sub-populations. On the "easy" sub-population, a classifier achieves an accuracy of $a_{0}$. The "hard" sub-population is $\kappa$ times more difficult in the sense that the classification error on these examples is $\kappa$ times larger. Hence the accuracy on this sub-population is $1 - {\kappa{({1 - a_{0}})}}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Model for the Linear Fit", "weight": 1.0} -->

For the new test set, we also assume a mixture distribution consisting of a different proportion of the same two components, with relative frequencies now $q_{1}$ and $q_{2}$. We can then write the accuracy on the new test set as

<!-- chunk {"id": "body-0041", "role": "body", "section": "Model for the Linear Fit", "weight": 1.0} -->

where we collected terms into a simple linear function as before.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Model for the Linear Fit", "weight": 1.0} -->

We remark that we do not see this mixture model as a ground truth explanation, but rather as an illustrative example for how a linear dependency between the original and new test accuracies naturally arises with small distribution shifts between data sets. In reality, the two test sets have a more complex composition with different accuracies on various sub-populations. Nevertheless, this model reveals surprising sensitivities can exist from distribution shift even while relative ordering of classifiers remain constant. We hope that such sensitivities to distribution shift can be experimentally validated in future work.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Explaining the Gap", "weight": 1.0} -->

Since the gap between original and new accuracy is concerningly large, we investigated multiple hypotheses for explaining this gap.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Statistical error", "weight": 1.0} -->

A first natural guess is that the gap is simply due to statistical fluctuations. But as noted before, the sample size of our new test set is large enough so that a 95% confidence interval has size about $\pm {1.2\%}$. Since a 95% confidence interval for the original CIFAR-10 test accuracy is even smaller (roughly $\pm {0.6\%}$ for 90% classification accuracy and $\pm {0.3\%}$ for 97% classification accuracy), we can rule out statistical error as the sole explanation.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Differences in near-duplicate removal", "weight": 1.0} -->

As mentioned in Section 3.2, the final step of both the original CIFAR-10 and our dataset creation procedure is a near-duplicate removal. While removing near-duplicates between our new test set and the original CIFAR-10 dataset, we noticed that the latter contained images that we would have ruled out as near-duplicates. A large number of near-duplicates between CIFAR-10 train and test, combined with our more stringent near-duplicate removal, could explain some of the accuracy drop. Indeed, we found about 800 images in the CIFAR-10 test set that we would classify as near-duplicates. Moreover, most classifiers have accuracy between 99% and 100% on these near-duplicates (recall that most models achieve 100% training error). But since the 800 images comprise only 8% of the original test set, the near-duplicates can explain at most 1% of the observed difference.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Differences in near-duplicate removal", "weight": 1.0} -->

For completeness, we describe our process for finding near duplicates in detail. For every test image, we visually inspected the top-10 nearest neighbors in both $\ell_{2}$-distance and the SSIM (structural similarity) metric. We compared the original test set to the CIFAR-10 training set, and our new test set to both the original training and test sets. We consider an image pair as near-duplicates if both images have the same object in the same pose. We include images that have different zoom, color scale, stretch in the horizontal or vertical direction, or small shifts in vertical or horizontal position. If the object was rotated or in a different pose, we did not include it as a near-duplicate.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Hyperparameter tuning", "weight": 1.0} -->

Another conjecture is that we can recover some of the missing accuracy by re-tuning hyperparameters of a model. To this end, we performed a grid search over multiple parameters of a VGG model. We selected three standard hyperparameters known to strongly influence test set performance: initial learning rate, dropout, and weight decay. The vgg16_keras architecture uses different amounts of dropout across different layers of the network, so we chose to tune a multiplicative scaling factor for the amount of dropout, keeping the ratio of dropout across different layers constant.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Hyperparameter tuning", "weight": 1.0} -->

We initialized a hyperparameter configuration from values tuned to the original test set (learning rate = $0.1$,

<!-- chunk {"id": "body-0049", "role": "body", "section": "Hyperparameter tuning", "weight": 1.0} -->

We ensured that the best performance was never at an extreme point of any of the ranges we tested for an individual hyperparameter. However, we did not find a setting with a significantly better accuracy on the new test set (the biggest improvement was from 85.25% to 85.84%).

<!-- chunk {"id": "body-0050", "role": "body", "section": "Inspecting hard images", "weight": 1.0} -->

It is also possible that we accidentally created a more difficult test set by including a set of \"harder\" images. To explore this, we visually inspected the set of images that the majority of models incorrectly classified. We find that all the new images are natural images that are recognizable to humans. Figure 3 in Appendix B shows examples of the hard images in our new test set that no model correctly classified.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Training on part of our new test set", "weight": 1.0} -->

If our new test set came from a significantly different data distribution than the original CIFAR-10 dataset, then retraining on half of our new test set plus the original training set should improve the accuracy scores on the held-out fraction of the new test set.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Training on part of our new test set", "weight": 1.0} -->

We conducted this experiment by randomly drawing a class-balanced split containing 1010 images from the new test set. We then added these images to the full CIFAR-10 training set and retrained the vgg16_keras model. After training, we tested the model on the 1011 held-out images from the new test set. We repeated this experiment twice with different randomly selected splits from our test set, obtaining accuracies of 85.06% and 85.36% (compared to 84.9% without the extra training data). This provides further evidence that there are no large distribution shifts between our new test set and the original CIFAR-10 dataset.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Cross-validation", "weight": 1.0} -->

Since cross-validation is a more principled way of measuring a model's generalization ability, we tested if cross-validation on the original CIFAR-10 dataset could predict a model's error on our new test set. We created cross-validation data by randomly dividing the training set into 5 class-balanced splits. We then randomly shuffled together 4 out of the 5 training splits with toe original test set. The leftover held-out split from the training set then became the new test set.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Cross-validation", "weight": 1.0} -->

We retrained the models vgg_15_BN_64, wide_resnet_28_10, and shake_shake_64d_cutout on each of the 5 new datasets we created. The accuracies are reported in Table 2. The accuracies on each of the cross validation splits did not vary much from the accuracies on the original test set.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Overfitting", "weight": 1.0} -->

Do our experiments reveal overfitting? This is arguably the main question when interpreting our results.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Overfitting", "weight": 1.0} -->

Training set overfitting. One way to quantify overfitting is as the difference between the training accuracy and the test accuracy. Note that the deep neural networks in our experiments usually achieve 100% training accuracy. So this notion of overfitting already occurs on the existing dataset.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Overfitting", "weight": 1.0} -->

Test set overfitting. Another notion of overfitting is the gap between the test accuracy and the accuracy on the underlying data distribution. By adapting model design choices to the test set, the concern is that we implicitly fit the model to the test set. The test accuracy then loses its validity as an accurate measure of performance on truly unseen data.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Overfitting", "weight": 1.0} -->

Since the overall goal in machine learning is to generalize to unseen data, we argue that the second notion of overfitting through test set adaptivity is more important. Surprisingly, our results show no signs of such overfitting on CIFAR-10. Despite multiple years of competitive adaptivity on this dataset, there has been no stagnation on truly held out data. In fact, the best performing models on our new test set see an *increased* advantage over more established baselines. Though this trend is opposite to what overfitting through adaptivity would suggest. While a conclusive picture will require further replication experiments, we view our results as support of the competition-based approach to increasing accuracy scores.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Overfitting", "weight": 1.0} -->

We note that one can read the analysis of Blum and Hardt's Ladder algorithm as supporting this claim. Indeed, they show that adding a minor modification of standard machine learning competitions avoids the sort of overfitting that can be achieved with aggressive adaptivity. Our results show that even without these modifications, model tuning based on the test error does not lead to overfitting on a standard data set.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Distribution shift", "weight": 1.0} -->

Although our results do not support the hypothesis of adaptivity-based overfitting, there is still a significant gap between original and new accuracy scores that needs to be explained. We view this gap as the result of a small distribution shift between the original CIFAR-10 dataset and our new test set. The fact that this gap is large, affects all models, and occurs despite our efforts to replicate the CIFAR-10 creation process is concerning. Normally, distribution shift is studied for specific changes in the data generation process (e.g., changes in lighting conditions) or for worst-case attacks in an adversarial setting. Our experiment is more benign and poses neither of these challenges. Nevertheless, the accuracy of all models drops by 4 - 15% and the relative increase in error rates is up to $3 \times$. This indicates that current CIFAR-10 classifiers have difficulty generalizing to natural variations in image data.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Future work", "weight": 1.5} -->

Concrete future experiments should explore whether the competition approach is similarly resilient to overfitting on other datasets (e.g., ImageNet) and other tasks (such as language modeling). An important aspect here is to ensure that the data distribution of a new test set stays as close to the original dataset as possible. Furthermore, we should understand what types of naturally occurring distribution shifts are challenging for image classifiers. For instance, are there certain sub-populations that the models fail to learn on CIFAR-10 but appear trivial to a human? In Section 4.3, we described a simple mixture model based on sub-population shifts that could serve as a starting point for such an investigation.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Future work", "weight": 1.5} -->

More broadly, we view our results as motivation for a more thorough evaluation of machine learning research. Currently, the dominant paradigm is to propose a new algorithm and evaluate its performance on existing data. Unfortunately, there is often little understanding to what extent the improvements are broadly applicable. To truly understand *generalization* questions, more studies should collect insightful new data and evaluate existing algorithms on such data. Since we now have a large body of essentially pre-registered classifiers in open-source repositories, such studies would conform to well established standards of statistically valid research. It is important to note the distinction to current reproducibility efforts in machine learning that usually focus on *computational* reproducibility, i.e., running published code on the same test data. In contrast, generalization experiments such as ours focus on *statistical* reproducibility by evaluating classifiers on truly new data (similar to recruiting new participants for a reproducibility experiment in medicine or psychology).
