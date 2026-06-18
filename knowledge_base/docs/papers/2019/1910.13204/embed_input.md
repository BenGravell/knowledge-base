<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Minimal Variance Sampling in Stochastic Gradient Boosting

Topics include Stochastic gradients, Accuracy, Generalization, Optimization, Learning, Sampling, MVS, SGB, Minimal variance sampling, Gradient boosting, Decision trees, Machine learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Stochastic Gradient Boosting (SGB) is a widely used approach to regularization of boosting models based on decision trees. It was shown that, in many cases, random sampling at each iteration can lead to better generalization performance of the model and can also decrease the learning time. Different sampling approaches were proposed, where probabilities are not uniform, and it is not currently clear which approach is the most effective. In this paper, we formulate the problem of randomization in SGB in terms of optimization of sampling probabilities to maximize the estimation accuracy of split scoring used to train decision trees. This optimization problem has a closed-form nearly optimal solution, and it leads to a new sampling technique, which we call Minimal Variance Sampling (MVS). The method both decreases the number of examples needed for each iteration of boosting and increases the quality of the model significantly as compared to the state-of-the art sampling methods. The superiority of the algorithm was confirmed by introducing MVS as a new default option for subsampling in CatBoost, a gradient boosting library achieving state-of-the-art quality on various machine learning tasks.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Gradient boosted decision trees (GBDT) is one of the most popular machine learning algorithms as it provides high-quality models in a large number of machine learning problems containing heterogeneous features, noisy data, and complex dependencies. There are many fields where gradient boosting achieves state-of-the-art results, e.g., search engines, recommendation systems, and other applications.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

One problem of GBDT is the computational cost of the learning process. GBDT may be described as an iterative process of constructing decision tree models, each of which estimates negative gradients of examples' errors. At each step, GBDT greedily builds a tree. GBDT scores every possible feature split and chooses the best one, which requires computational time proportional to the number of data instances. Since most GBDT models consist of an ensemble of many trees, as the number of examples grows, more learning time is required, what imposes restrictions on using GBDT models for large industry datasets.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Another problem is the trade-off between the capacity of the GBDT model and its generalization ability. One of the most critical parameters that influence the capacity of boosting is the number of iterations or the size of the ensemble. The more components are used in the algorithm, the more complex dependencies can be modeled. However, an increase in the number of models in the ensemble does not always lead to an increase in accuracy and, moreover, can decrease its generalization ability. Therefore boosting algorithms are usually provided with regularization methods, which are needed to prevent overfitting.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A common approach to handle both of the problems described above is to use random subsampling (or bootstrap) at every iteration of the algorithm. Before fitting a next tree, we select a subset of training objects, which is smaller than the original training dataset, and perform learning algorithm on a chosen subsample. The fraction of chosen objects is called sample rate. Studies in this area show that this demonstrates excellent performance in terms of learning time and quality. It helps to speed up the learning process for each decision tree model as it uses less data. Also, the accuracy can increase because, despite the fact that the variance of each component of the ensemble goes up, the pairwise correlation between trees of the ensemble decreases, what can lead to a reduction in the total variance of the model.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose a new approach to theoretical analysis of random sampling in GBDT. In GBDT, random subsamples are used for evaluation of candidate splits, when each next decision tree is constructed. Random sampling decreases the size of the active training dataset, and the training procedure becomes more noisy, what can entail a decrease in the quality. Therefore, sampling algorithm should select the most informative training examples, given a constrained number of instances the algorithm is allowed to choose. We propose a mathematical formulation of this optimization problem in SGB, where the accuracy of estimated scores of candidate splits is maximized. For every fixed sample rate (ratio of sampled objects), we propose a solution to this sampling problem and provide a novel algorithm Minimal Variance Sampling (MVS). MVS relies on the distribution of loss derivatives and assigns probabilities and weights with which the sampling should be done. That makes the procedure adaptive to any data distribution and allows to significantly outperform the state of the art SGB methods, operating with way less number of data instances.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Gradient Boosting", "weight": 1.0} -->

Gradient boosting (GB) is a method of constructing the desired function $F$ in the form

<!-- chunk {"id": "body-0009", "role": "body", "section": "Gradient Boosting", "weight": 1.0} -->

where $n$ is the number of iterations, i.e., the amount of base functions $f_{k}$ chosen from a simple parametric family $\mathcal{F}$, such as linear models or decision trees with small depth. The learning rate, or step size in functional space, is denoted by $\alpha$. Base learners $\{ f_{k}\}$ are learned sequentially in the following way.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Gradient Boosting", "weight": 1.0} -->

If a subfamily of decision tree functions is taken as a set of base functions $\mathcal{F}$ (e.g., all decision trees of depth 5), the algorithm is called Gradient Boosted Decision Trees (GBDT). A decision tree divides the original feature space ${\mathbb{R}}^{d}$ into disjoint areas, also called leaves, with a constant value in each region.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Gradient Boosting", "weight": 1.0} -->

In other words, the result of a decision tree learning is a disjoint union of subsets $\{{X_{1},X_{2},\ldots,X_{q}}:{{\bigsqcup\limits_{i = 1}^{q}X_{i}} = \mathcal{X}}\}$ and a piecewise constant function ${f{(\overset{\rightarrow}{x})}} = {\sum\limits_{i = 1}^{q}{{\mathbb{I}}{\{{\overset{\rightarrow}{x} \in X_{i}}\}}c_{i}}}$. The learning procedure is recursive. It starts from the whole set ${\mathbb{R}}^{d}$ as the only region. For every of the already built regions, the algorithm looks out all split candidates by one feature and sets a score for each split. The score is usually a measure of accuracy gain based on target distributions in the regions before and after splitting.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Gradient Boosting", "weight": 1.0} -->

The process continues until a stopping criterion is reached.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Stochastic Gradient Boosting", "weight": 1.0} -->

Stochastic Gradient Boosting is a randomized version of standard Gradient Boosting algorithm. Motivated by Breiman's work about adaptive bagging, Friedman came to the idea of adding randomness into the tree building procedure by using a subsampling of the full dataset. For each iteration of the boosting process, the sampling algorithm of SGB selects random $s \cdot N$ objects without replacement and uniformly. It effectively reduces the complexity of each iteration down to the factor of $s$. It is also proved by experiments that, in some cases, the quality of the learned model can be improved by using SGB.

<!-- chunk {"id": "body-0014", "role": "body", "section": "GOSS", "weight": 1.0} -->

SGB algorithm makes all objects to be selected equally likely. However, different objects have different impacts on the learning process. Gradient-based one-side sampling (GOSS) implements an idea that objects ${\overset{\rightarrow}{x}}_{i}$ with larger absolute value of the gradient $|g_{i}|$ are more important than the ones that have smaller gradients. A large gradient value indicates that the model can be improved significantly with respect to the object, and it should be sampled with higher probability compared to well-trained instances with small gradients. So, GOSS takes the most important objects with probability 1 and chooses a random sample of other objects. To avoid distribution bias, GOSS re-weighs selected samples by setting higher weights to the examples with smaller gradients. More formally, the training sample consists of ${top\_rate} \times N$ instances with largest $|g_{i}|$ with weight equal to 1 and of ${other\_rate} \times N$ instances from the rest of the data with weights equal to $\frac{1 - {top\_rate}}{other\_rate}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem setting", "weight": 1.0} -->

As it was mentioned in Section 2.1, training a decision tree is a recursive process of selecting the best data partition (or split), which is based on a value of some feature. So, given a subset $A$ of original feature space $\mathcal{X}$, split is a pair of feature $f$ and its value $v$ such that data is partitioned into two sets: $A_{1} = {\{{\overset{\rightarrow}{x} \in A}:{x_{f} < v}\}}$, $A_{2} = {\{{\overset{\rightarrow}{x} \in A}:{x_{f} \geq v}\}}$. Every split is evaluated by some score, which is used to select the best one among them.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem setting", "weight": 1.0} -->

There are various scoring metrics, e.g., Gini index and entropy criterion for classification tasks, mean squared error (MSE) and mean absolute error (MAE) for regression trees. Most of GB implementations (e.g. ) consider hessian while learning next tree (second-order approximation). The solution to in a leaf $l$ is the constant equal to the ratio $\frac{\sum\limits_{i \in l}g_{i}}{\sum\limits_{i \in l}h_{i}}$ of the sum of gradients and the sum of hessian diagonal elements. The score $S{(f,v)}$ of a split $(f,v)$ is calculated as

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem setting", "weight": 1.0} -->

where $L$ is the set of obtained leaves, and leaf $l$ consists of objects that belong to this leaf. This score is, up to a common constant, the opposite to the value of the functional minimized in Equation 3 when we add this split to the tree. For classical GB based on the first-order gradient steps, according to Equation 2, score $S{(f,v)}$ should be calculated by setting $h_{i} = 1$ in Equation 4.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem setting", "weight": 1.0} -->

To formulate the problem, we first describe the general sampling procedure, which generalizes SGB and GOSS. Sampling from a set of size $N$ may be described as a sequence of random variables $(\xi_{1},\xi_{2},\ldots,\xi_{N})$, where $\xi_{i} \sim {\text{Bernoulli}{(p_{i})}}$, and $\xi_{i} = 1$ indicates that $i$-th example was sampled and should be used to estimate scores $S{(f,v)}$ of different candidates $(f,v)$. Let $n_{sampled}$ be the number of selected instances.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem setting", "weight": 1.0} -->

To make all key statistics (sum of gradients and sum of hessians in the leaf) unbiased, we perform inverse probability weighting estimation (IPWE), which assigns weight $w_{i} = \frac{1}{p_{i}}$ to instance $i$. In GB with sampling, score $S{(f,v)}$ is approximated by

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem setting", "weight": 1.0} -->

where the numerator and denominator are estimators of $\left( {\sum\limits_{i \in l}g_{i}} \right)^{2}$ and $\sum\limits_{i \in l}h_{i}$ correspondingly.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem setting", "weight": 1.0} -->

We are aimed at minimization of squared deviation $\Delta^{2} = \left( {{\hat{S}{(f,v)}} - {S{(f,v)}}} \right)^{2}$, under the assumption that previous splits of the tree are fixed and the same for subsampled and full data. Deviation $\Delta$ is a random variable due to the randomness of the sampling procedure (randomness of $\xi_{i}$). Therefore, we consider the minimization of the expectation ${\mathbb{E}}\Delta^{2}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Theoretical analysis", "weight": 1.0} -->

Here we show that Problem 9 has a simple solution and leads to an effective sampling algorithm. First, we discuss its meaning in the case of first-order optimization, where we have $h_{i} = 1$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Theoretical analysis", "weight": 1.0} -->

The first term of the minimized expression is responsible for gradient distribution over the leaves of the decision tree, while the second one is responsible for the distribution of sample sizes. Coefficient $\lambda$ controls the magnitude of each of the component. It can be seen as a tradeoff between the variance of a single model and the variance of the ensemble. The variance of the ensemble consists of individual variances of every single algorithm and pairwise correlations between models. On the one hand, it is crucial to reduce individual variances of each model; on the other hand, the more dissimilar subsamples are, the less the total variance of the ensemble is. This is reflected in the accuracy dependence on the number of sampled examples: the slight reduction of this number usually leads to increase in the quality as the variance of each model is not corrupted a lot, but, when the sample size goes down to smaller numbers, the sum of variances prevails over the loss in correlations and the accuracy dramatically decreases.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Theoretical analysis", "weight": 1.0} -->

It is easy to derive that setting $\lambda$ to 0 implies the procedure of Importance Sampling. As it was mentioned before, the applicability of this procedure in GBDT is constrained since it is still important to estimate the number of instances accurately in each node of the tree. Besides, Importance Sampling is suffering from numerical instability while dealing with small gradients close to zero, what usually happens on the latter gradient boosting iterations. In this case, the second part of the expression may be interpreted as a regularisation member prohibiting enormous weights.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Theoretical analysis", "weight": 1.0} -->

Setting $\lambda$ to $\infty$ implies the SGB algorithm.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Algorithm", "weight": 1.0} -->

Now we are ready to derive the MVS algorithm from Theorem 2, which can be directly applied to general scheme of Stochastic Gradient Boosting. First, for given sample rate $s$, MVS finds the threshold $\mu$ to decide, which gradients are considered to be large. Example $i$ with regularized absolute value $\sqrt{g_{i}^{2} + {\lambdah_{i}^{2}}}$ higher than chosen $\mu$ is sampled with probability equal to 1. Every object with small gradient is sampled independently with probability $p_{i} = \frac{\sqrt{g_{i}^{2} + {\lambdah_{i}^{2}}}}{\mu}$ and is assigned weight $w_{i} = \frac{1}{p_{i}}$. Still, it is not apparent how to find such a threshold $\mu^{\ast}$ that will give the required sampling ratio $s = s^{\ast}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Algorithm", "weight": 1.0} -->

A brute-force algorithm relies on the fact that the sampling ratio has an inverse dependence on the threshold: the higher the threshold, the lower the fraction of sampled instances. First, we sort the data by regularized absolute value in descending order. Note that now, given a threshold $\mu$, the sampling ratio $s$ can be calculated as ${s{(\mu)}} = {{\frac{1}{\mu}{\sum\limits_{i = {k + 1}}^{N}\sqrt{g_{i}^{2} + {\lambdah_{i}^{2}}}}} + k}$, where $k + 1$ is the number of the first element in sorted sequence, which is less than $\mu$. Then the binary search is applied to find a threshold $\mu^{\ast}$ with the desired property ${s{(\mu^{\ast})}} = s^{\ast}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Algorithm", "weight": 1.0} -->

To speed up this algorithm, the precalculation of cumulative sums of regularized absolute values $\sum\limits_{i = {k + 1}}^{N}\sqrt{g_{i}^{2} + {\lambdah_{i}^{2}}}$ for every $k$ is performed, so the calculation of sampling ratio at each step of binary search has $O{}$ time complexity. The total complexity of this procedure is $O{({N{\log N}})}$, due to sorting at the beginning. To compare, SGB and GOSS algorithms have $O{(N)}$ complexity for sampling.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Algorithm", "weight": 1.0} -->

We propose a more efficient algorithm, which is similar to the quick select algorithm. In the beginning, the algorithm randomly selects the gradient, which is a candidate to be a threshold. The data is partitioned in such a way that all the instances with smaller gradients and larger gradients are on the opposite sides of the candidate. To calculate the current sample rate, it is sufficient to calculate the number of examples on the larger side and the sum of regularized absolute values on the other side. Then, estimated sample rate is used to determine the side where to continue the search for the desired threshold. If the current sample rate is higher, then algorithms searches threshold on the side with smaller gradients, otherwise on the side with greater. Calculated statistics for each side may be reused in further steps of the algorithm, so the number of the operations at each step is reduced by the number of rejected examples. The time complexity analysis can be carried out by analogy with the quick select algorithm, which results in $O{(N)}$ complexity.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Algorithm", "weight": 1.0} -->

c u r S a m p l e R a t e = $\frac{{\text{Sum}{({smallArray})}} + {sumSmall}}{candidateThreshold}$ + Length(l a r g e A r r a y) + n L a r g e + 1 if Length(s m a l l A r r a y) == 0 and c u r S a m p l e R a t e &lt; s a m p l e R a t e then return $\frac{sumSmall}{{sampleRate} - {nLarge} - {\text{Length}{({largeArray})}} - 1}$ else if Length(l a r g e A r r a y) == 0 and c u r S a m p l e R a t e &gt; s a m p l e R a t e then return $\frac{{sumSmall} + {\text{Sum}{({smallArray})}} + {candidateThreshold}}{{sampleRate} - {nLarge}}$

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments", "weight": 1.0} -->

Here we provide experimental results of MVS algorithm on two popular open-source implementations of gradient boosting: CatBoost and LightGBM.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiments", "weight": 1.0} -->

CatBoost. The default setting of CatBoost is known to achieve state-of-the-art quality on various machine learning tasks. We implemented MVS in CatBoost and performed benchmark comparison of MVS with sampling ratio 80% and default CatBoost with no sampling on 153 publicly available and proprietary binary classification datasets of different sizes up to 45 millions instances. The algorithms were compared by the ROC-AUC metric, and we calculated the number of wins for each algorithm. The results show significant improvement over the existing default: 97 wins of MVS versus 55 wins of default setting and $+ {0.12\%}$ mean ROC-AUC improvement.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

The source code of MVS is publicly available and ready to be used as a default option of CatBoost algorithm. The latter means that MVS is already acknowledged as a new benchmark in SGB implementations.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments", "weight": 1.0} -->

LightGBM. To perform a fair comparison with previous sampling techniques (GOSS and SGB), MVS was also implemented in LightGBM, as it is a popular open-source library with GOSS inside. The MVS source code for LightGBM may be found.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiments", "weight": 1.0} -->

Datasets' descriptions used in this section are placed in Table 1. All the datasets are publicly available and were preprocessed according to.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiments", "weight": 1.0} -->

## Examples
## Features

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiments", "weight": 1.0} -->

We used the tuned parameters and train-test splitting for each dataset from as baselines, presetting the sampling ratio to 1. For tuning sampling parameters of each algorithm (sample rate and $\lambda$ coefficient for MVS, large gradients fraction and small gradients fraction for GOSS, sample rate for SGB), we use 5-fold cross-validation on train subset of the data. Then the tuned models are evaluated on test subsets (which is 20% of the original size of the data). Here we use the $1 - \text{ROC-AUC}$ score as an error measure (lower is better). To make the results more statistically significant, the evaluation part is run 10 times with different seeds. The final result is defined as the mean over these 10 runs.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experiments", "weight": 1.0} -->

Here we also introduce hyperparameter-free MVS algorithm modification. Since $\lambda$ (see Equation 9) is an approximation of squared mean leaf value upper bound, we replace it with a squared mean of the initial leaf. As it will be shown, it achieves near-optimal results and dramatically reduces time spent on parameter tuning. Since it sets $\lambda$ adaptively at each iteration, we refer to this method as MVS Adaptive.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experiments", "weight": 1.0} -->

Quality comparison. The first experiments are devoted to testing MVS as a regularization method. We state the following question: how much the quality changes when using different sampling techniques? To answer this question, we tuned the sampling parameters of algorithms to get the best quality. This quality scores compared to baselines quality are presented in Table 2. From this results, we can see that MVS demonstrates the best generalization ability among given sampling approaches. The best parameter $\lambda$ for MVS is about $10^{- 1}$, it shows good performance on most of the datasets. For GOSS, the best ratio of large and small gradients varies a lot from the predominance of large to the predominance of small.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experiments", "weight": 1.0} -->

The next research question is whether MVS is capable of reducing sample size per each iteration needed to achieve acceptable quality. Furthermore, whether MVS is harmful to accuracy while using small subsamples. For this experiment, we tuned parameters, so that the algorithms achieve the baseline score (or their best score if it is not possible) using the least number of instances. Figure 1 shows the dependence of error on the sample size for two datasets and its $\pm \sigma$ confidence interval. Table 3 demonstrates average relative error change with respect to the baseline over all datasets used in this paper. From these results, we can conclude that MVS reaches the goal of reducing the variance of the models, and a decrease in sample size affects the accuracy much less than it does for other algorithms.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Experiments", "weight": 1.0} -->

Learning time comparison. To compare the speed-up ability of MVS, GOSS and SGB, we used runs from the previous experiment setting, i.e., parameters were chosen in order to have the smallest sample rate with no quality loss. Among them, we choose the ones which have the least training time (if it is impossible to beat baseline, the best score point is chosen). The summary is shown in Table 4, which demonstrates the average learning time gain relative to the baseline learning time (using all examples). One can see that the usage of MVS has an advantage in training time over other methods at the amount of about 10% for datasets presented in this paper. Also, it is important to mention that tuning the hyperparemeters is a main part of training a model. There is one common hyperparameter for all sampling algorithms - sample rate. GOSS has one additional hyperparameter - ratio of large and small gradients in the subsample, and MVS has a hyperparameter $\lambda$. So tuning GOSS and MVS may potentially take more time than SGB.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Experiments", "weight": 1.0} -->

But introducing MVS Adaptive algorithm dramatically reduces tuning time due to hyperparameter-free sampling procedure, and we can conclude from Tables 2 and 3 that it achieves approximately optimal results on the test data

<!-- chunk {"id": "body-0043", "role": "body", "section": "Experiments", "weight": 1.0} -->

Large datasets. Experiments with CatBoost show that regularization effect of MVS is efficient for any size of the data. But for large datasets it is more crucial to reduce learning time of the model. To prove that MVS is efficient in accelerating the training we use Higgs dataset (11000000 instances and 28 features) and Recsys datasets (16549802 instances and 31 features). The set up of experiment remains the same as in the previous paragraph. For Higgs dataset SGB is not able to achieve the baseline quality with less than 100% sample size, while GOSS and MVS managed to do this with 80% of samples and MVS was faster than GOSS (-17.7% versus -8.5%) as it converges earlier. For Recsys dataset relative learning time differences are -50.3% for SGB (sample rate 20%), -39.9% for SGB (sample rate 20%) and -61.5% for MVS (sample rate 10%).

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we addressed a surprisingly understudied problem of weighted sampling in GBDT. We proposed a novel technique, which directly maximizes the accuracy of split scoring, a core step of the tree construction procedure. We rigorously formulated this goal as an optimization problem and derived a near-optimal closed-form solution. This solution led to a novel sampling technique MVS. We provided our work with necessary theoretical statements and empirical observations that show the superiority of MVS over the well-known state-of-the-art approaches to data sampling in SGB. MVS is implemented and used by default in CatBoost open-source library. Also, one can find MVS implementation in LightGBM package, and its source code is publicly available for further research.
