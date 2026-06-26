<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

"Why Should I Trust You? ": Explaining the Predictions of Any Classifier

Topics include Neural networks, Classification, Classifiers, Optimization, Learning, LIME, Machine learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Despite widespread adoption, machine learning models remain mostly black boxes. Understanding the reasons behind predictions is, however, quite important in assessing trust, which is fundamental if one plans to take action based on a prediction, or when choosing whether to deploy a new model. Such understanding also provides insights into the model, which can be used to transform an untrustworthy model or prediction into a trustworthy one. In this work, we propose LIME, a novel explanation technique that explains the predictions of any classifier in an interpretable and faithful manner, by learning an interpretable model locally around the prediction. We also propose a method to explain models by presenting representative individual predictions and their explanations in a non-redundant way, framing the task as a submodular optimization problem. We demonstrate the flexibility of these methods by explaining different models for text (e.g. random forests) and image classification (e.g. neural networks). We show the utility of explanations via novel experiments, both simulated and with human subjects, on various scenarios that require trust: deciding if one should trust a prediction, choosing between models, improving an untrustworthy classifier, and identifying why a classifier should not be trusted.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Machine learning is at the core of many recent advances in science and technology. Unfortunately, the important role of humans is an oft-overlooked aspect in the field. Whether humans are directly using machine learning classifiers as tools, or are deploying models within other products, a vital concern remains: *if the users do not trust a model or a prediction, they will not use it*. It is important to differentiate between two different (but related) definitions of trust: *trusting a prediction*, i.e. whether a user trusts an individual prediction sufficiently to take some action based on it, and *trusting a model*, i.e. whether the user trusts a model to behave in reasonable ways if deployed. Both are directly impacted by how much the human understands a model's behaviour, as opposed to seeing it as a black box.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Determining trust in individual predictions is an important problem when the model is used for decision making. When using machine learning for medical diagnosis or terrorism detection, for example, predictions cannot be acted upon on blind faith, as the consequences may be catastrophic.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Apart from trusting individual predictions, there is also a need to evaluate the model as a whole before deploying it "in the wild". To make this decision, users need to be confident that the model will perform well on real-world data, according to the metrics of interest. Currently, models are evaluated using accuracy metrics on an available validation dataset. However, real-world data is often significantly different, and further, the evaluation metric may not be indicative of the product's goal. Inspecting individual predictions and their explanations is a worthwhile solution, in addition to such metrics. In this case, it is important to aid users by suggesting which instances to inspect, especially for large datasets.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose providing explanations for individual predictions as a solution to the "trusting a prediction" problem, and selecting multiple such predictions (and explanations) as a solution to the "trusting the model" problem. Our main contributions are summarized as follows.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

LIME, an algorithm that can explain the predictions of *any* classifier or regressor in a faithful way, by approximating it locally with an interpretable model.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

SP-LIME, a method that selects a set of representative instances with explanations to address the "trusting the model" problem, via submodular optimization.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Comprehensive evaluation with simulated and human subjects, where we measure the impact of explanations on trust and associated tasks. In our experiments, non-experts using LIME are able to pick which classifier from a pair generalizes better in the real world. Further, they are able to greatly improve an untrustworthy classifier trained on 20 newsgroups, by doing feature engineering using LIME. We also show how understanding the predictions of a neural network on images helps practitioners know when and why they should not trust a model.

<!-- chunk {"id": "body-0010", "role": "body", "section": "The case for explanations", "weight": 1.0} -->

By "explaining a prediction", we mean presenting textual or visual artifacts that provide qualitative understanding of the relationship between the instance's components (e.g. words in text, patches in an image) and the model's prediction. We argue that explaining predictions is an important aspect in getting humans to trust and use machine learning effectively, if the explanations are faithful and intelligible.

<!-- chunk {"id": "body-0011", "role": "body", "section": "The case for explanations", "weight": 1.0} -->

The process of explaining individual predictions is illustrated in Figure 1. It is clear that a doctor is much better positioned to make a decision with the help of a model if intelligible explanations are provided. In this case, an explanation is a small list of symptoms with relative weights -- symptoms that either contribute to the prediction (in green) or are evidence against it (in red). Humans usually have prior knowledge about the application domain, which they can use to accept (trust) or reject a prediction if they understand the reasoning behind it. It has been observed, for example, that providing explanations can increase the acceptance of movie recommendations and other automated systems.

<!-- chunk {"id": "body-0012", "role": "body", "section": "The case for explanations", "weight": 1.0} -->

Every machine learning application also requires a certain measure of overall trust in the model. Development and evaluation of a classification model often consists of collecting annotated data, of which a held-out subset is used for automated evaluation. Although this is a useful pipeline for many applications, evaluation on validation data may not correspond to performance "in the wild", as practitioners often overestimate the accuracy of their models, and thus trust cannot rely solely on it. Looking at examples offers an alternative method to assess truth in the model, especially if the examples are explained. We thus propose explaining several representative individual predictions of a model as a way to provide a global understanding.

<!-- chunk {"id": "body-0013", "role": "body", "section": "The case for explanations", "weight": 1.0} -->

There are several ways a model or its evaluation can go wrong. Data leakage, for example, defined as the unintentional leakage of signal into the training (and validation) data that would not appear when deployed, potentially increases accuracy. A challenging example cited by Kaufman et al. is one where the patient ID was found to be heavily correlated with the target class in the training and validation data. This issue would be incredibly challenging to identify just by observing the predictions and the raw data, but much easier if explanations such as the one in Figure 1 are provided, as patient ID would be listed as an explanation for predictions. Another particularly hard to detect problem is dataset shift, where training data is different than test data (we give an example in the famous 20 newsgroups dataset later on). The insights given by explanations are particularly helpful in identifying what must be done to convert an untrustworthy model into a trustworthy one -- for example, removing leaked data or changing the training data to avoid dataset shift.

<!-- chunk {"id": "body-0014", "role": "body", "section": "The case for explanations", "weight": 1.0} -->

Machine learning practitioners often have to select a model from a number of alternatives, requiring them to assess the relative trust between two or more models. In Figure 2, we show how individual prediction explanations can be used to select between models, in conjunction with accuracy. In this case, the algorithm with higher accuracy on the validation set is actually much worse, a fact that is easy to see when explanations are provided (again, due to human prior knowledge), but hard otherwise. Further, there is frequently a mismatch between the metrics that we can compute and optimize (e.g. accuracy) and the actual metrics of interest such as user engagement and retention. While we may not be able to measure such metrics, we have knowledge about how certain model behaviors can influence them. Therefore, a practitioner may wish to choose a less accurate model for content recommendation that does not place high importance in features related to "clickbait" articles (which may hurt user retention), even if exploiting such features increases the accuracy of the model in cross validation. We note that explanations are particularly useful in these (and other) scenarios if a method can produce them for *any* model, so that a variety of models can be compared.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Desired Characteristics for Explainers", "weight": 1.0} -->

We now outline a number of desired characteristics from explanation methods.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Desired Characteristics for Explainers", "weight": 1.0} -->

An essential criterion for explanations is that they must be interpretable, i.e., provide qualitative understanding between the input variables and the response. We note that interpretability must take into account the user's limitations. Thus, a linear model, a gradient vector or an additive model may or may not be interpretable. For example, if hundreds or thousands of features significantly contribute to a prediction, it is not reasonable to expect any user to comprehend why the prediction was made, even if individual weights can be inspected. This requirement further implies that explanations should be easy to understand, which is not necessarily true of the features used by the model, and thus the "input variables" in the explanations may need to be different than the features. Finally, we note that the notion of interpretability also depends on the target audience. Machine learning practitioners may be able to interpret small Bayesian networks, but laymen may be more comfortable with a small number of weighted features as an explanation.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Desired Characteristics for Explainers", "weight": 1.0} -->

Another essential criterion is local fidelity. Although it is often impossible for an explanation to be completely faithful unless it is the complete description of the model itself, for an explanation to be meaningful it must at least be *locally faithful*, i.e. it must correspond to how the model behaves in the vicinity of the instance being predicted. We note that local fidelity does not imply global fidelity: features that are globally important may not be important in the local context, and vice versa. While global fidelity would imply local fidelity, identifying globally faithful explanations that are interpretable remains a challenge for complex models.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Desired Characteristics for Explainers", "weight": 1.0} -->

While there are models that are inherently interpretable, an explainer should be able to explain *any* model, and thus be model-agnostic (i.e. treat the original model as a black box). Apart from the fact that many state-of-the-art classifiers are not currently interpretable, this also provides flexibility to explain future classifiers.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Desired Characteristics for Explainers", "weight": 1.0} -->

In addition to explaining predictions, providing a global perspective is important to ascertain trust in the model. As mentioned before, accuracy may often not be a suitable metric to evaluate the model, and thus we want to *explain the model*. Building upon the explanations for individual predictions, we select a few explanations to present to the user, such that they are representative of the model.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Local Interpretable Model-Agnostic Explanations", "weight": 1.0} -->

We now present Local Interpretable Model-agnostic Explanations (LIME). The overall goal of LIME is to identify an interpretable model over the *interpretable representation* that is locally faithful to the classifier.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Interpretable Data Representations", "weight": 1.0} -->

Before we present the explanation system, it is important to distinguish between features and interpretable data representations. As mentioned before, interpretable explanations need to use a representation that is understandable to humans, regardless of the actual features used by the model. For example, a possible *interpretable representation* for text classification is a binary vector indicating the presence or absence of a word, even though the classifier may use more complex (and incomprehensible) features such as word embeddings. Likewise for image classification, an *interpretable representation* may be a binary vector indicating the "presence" or "absence" of a contiguous patch of similar pixels (a super-pixel), while the classifier may represent the image as a tensor with three color channels per pixel. We denote $x \in {\mathbb{R}}^{d}$ be the original representation of an instance being explained, and we use $x' \in {\{ 0,1\}}^{d'}$ to denote a binary vector for its interpretable representation.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Fidelity-Interpretability Trade-off", "weight": 1.0} -->

Formally, we define an explanation as a model $g \in G$, where $G$ is a class of potentially *interpretable* models, such as linear models, decision trees, or falling rule lists, i.e. a model $g \in G$ can be readily presented to the user with visual or textual artifacts. The domain of $g$ is ${\{ 0,1\}}^{d'}$, i.e. $g$ acts over absence/presence of the *interpretable components*. As not every $g \in G$ may be simple enough to be interpretable - thus we let $\Omega{(g)}$ be a measure of *complexity* (as opposed to *interpretability*) of the explanation $g \in G$. For example, for decision trees $\Omega{(g)}$ may be the depth of the tree, while for linear models, $\Omega{(g)}$ may be the number of non-zero weights.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Fidelity-Interpretability Trade-off", "weight": 1.0} -->

Let the model being explained be denoted $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$. In classification, $f{(x)}$ is the probability (or a binary indicator) that $x$ belongs to a certain class^11^1For multiple classes, we explain each class separately, thus $f{(x)}$ is the prediction of the relevant class.. We further use $\pi_{x}{(z)}$ as a proximity measure between an instance $z$ to $x$, so as to define locality around $x$. Finally, let $\mathcal{L}{(f,g,\pi_{x})}$ be a measure of how unfaithful $g$ is in approximating $f$ in the locality defined by $\pi_{x}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Fidelity-Interpretability Trade-off", "weight": 1.0} -->

In order to ensure both interpretability and local fidelity, we must minimize $\mathcal{L}{(f,g,\pi_{x})}$ while having $\Omega{(g)}$ be low enough to be interpretable by humans. The explanation produced by LIME is obtained by the following: This formulation can be used with different explanation families $G$, fidelity functions $\mathcal{L}$, and complexity measures $\Omega$. Here we focus on sparse linear models as explanations, and on performing the search using perturbations.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Sampling for Local Exploration", "weight": 1.0} -->

We want to minimize the locality-aware loss $\mathcal{L}{(f,g,\pi_{x})}$ without making any assumptions about $f$, since we want the explainer to be model-agnostic. Thus, in order to learn the local behavior of $f$ as the interpretable inputs vary, we approximate $\mathcal{L}{(f,g,\pi_{x})}$ by drawing samples, weighted by $\pi_{x}$. We sample instances around $x'$ by drawing nonzero elements of $x'$ uniformly at random (where the number of such draws is also uniformly sampled). Given a perturbed sample $z' \in {\{ 0,1\}}^{d'}$ (which contains a fraction of the nonzero elements of $x'$), we recover the sample in the original representation $z \in R^{d}$ and obtain $f{(z)}$, which is used as a *label* for the explanation model.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Sampling for Local Exploration", "weight": 1.0} -->

Given this dataset $\mathcal{Z}$ of perturbed samples with the associated labels, we optimize Eq. to get an explanation $\xi{(x)}$. The primary intuition behind LIME is presented in Figure 3, where we sample instances both in the vicinity of $x$ (which have a high weight due to $\pi_{x}$) and far away from $x$ (low weight from $\pi_{x}$). Even though the original model may be too complex to explain globally, LIME presents an explanation that is locally faithful (linear in this case), where the locality is captured by $\pi_{x}$. It is worth noting that our method is fairly robust to sampling noise since the samples are weighted by $\pi_{x}$ in Eq.. We now present a concrete instance of this general framework.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Sparse Linear Explanations", "weight": 1.0} -->

For the rest of this paper, we let $G$ be the class of linear models, such that ${g{(z')}} = {w_{g} \cdot z'}$. We use the locally weighted square loss as $\mathcal{L}$, as defined in Eq., where we let ${\pi_{x}{(z)}} = {exp{({- {{D{(x,z)}^{2}}/\sigma^{2}}})}}$ be an exponential kernel defined on some distance function $D$ (e.g. cosine distance for text, $L2$ distance for images) with width $\sigma$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Sparse Linear Explanations", "weight": 1.0} -->

For text classification, we ensure that the explanation is interpretable by letting the *interpretable representation* be a bag of words, and by setting a limit $K$ on the number of words, i.e. ${\Omega{(g)}} = {\infty\mathbb{1}{\lbrack{\left. \parallel w_{g}\parallel \right._{0} > K}\rbrack}}$. Potentially, $K$ can be adapted to be as big as the user can handle, or we could have different values of $K$ for different instances. In this paper we use a constant value for $K$, leaving the exploration of different values to future work. We use the same $\Omega$ for image classification, using "super-pixels" (computed using any standard algorithm) instead of words, such that the interpretable representation of an image is a binary vector where $1$ indicates the original super-pixel and $0$ indicates a grayed out super-pixel.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Sparse Linear Explanations", "weight": 1.0} -->

This particular choice of $\Omega$ makes directly solving Eq. intractable, but we approximate it by first selecting $K$ features with Lasso (using the regularization path ) and then learning the weights via least squares (a procedure we call K-LASSO in Algorithm 1). Since Algorithm 1 produces an explanation for an individual prediction, its complexity does not depend on the size of the dataset, but instead on time to compute $f{(x)}$ and on the number of samples $N$. In practice, explaining random forests with $1000$ trees using scikit-learn on a laptop with $N = 5000$ takes under 3 seconds without any optimizations such as using gpus or parallelization. Explaining each prediction of the Inception network for image classification takes around 10 minutes.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Sparse Linear Explanations", "weight": 1.0} -->

Any choice of interpretable representations and $G$ will have some inherent drawbacks. First, while the underlying model can be treated as a black-box, certain interpretable representations will not be powerful enough to explain certain behaviors. For example, a model that predicts sepia-toned images to be *retro* cannot be explained by presence of absence of super pixels. Second, our choice of $G$ (sparse linear models) means that if the underlying model is highly non-linear even in the locality of the prediction, there may not be a faithful explanation. However, we can estimate the faithfulness of the explanation on $\mathcal{Z}$, and present this information to the user. This estimate of faithfulness can also be used for selecting an appropriate family of explanations from a set of multiple interpretable model classes, thus adapting to the given dataset and the classifier. We leave such exploration for future work, as linear explanations work quite well for multiple black-box models in our experiments.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Sparse Linear Explanations", "weight": 1.0} -->

Classifier f, Number of samples N Instance x, and its interpretable version x′ Similarity kernel πx, Length of explanation K w ← K-Lasso (𝒵, K) ⊳ with zi′ as features, f (z) as target return w Algorithm 1 Sparse Linear Explanations using LIME (b) Explaining Electric guitar (c) Explaining Acoustic guitar Figure 4: Explaining an image classification prediction made by Google’s Inception neural network. The top 3 classes predicted are “Electric Guitar” (p = 0.32), “Acoustic guitar” (p = 0.24) and “Labrador” (p = 0.21)

<!-- chunk {"id": "body-0032", "role": "body", "section": "Example 1: Text classification with SVMs", "weight": 1.0} -->

In Figure 2 (right side), we explain the predictions of a support vector machine with RBF kernel trained on unigrams to differentiate "Christianity" from "Atheism" (on a subset of the 20 newsgroup dataset). Although this classifier achieves $94\%$ held-out accuracy, and one would be tempted to trust it based on this, the explanation for an instance shows that predictions are made for quite arbitrary reasons (words "Posting", "Host", and "Re" have no connection to either Christianity or Atheism). The word "Posting" appears in 22% of examples in the training set, 99% of them in the class "Atheism". Even if headers are removed, proper names of prolific posters in the original newsgroups are selected by the classifier, which would also not generalize.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Example 1: Text classification with SVMs", "weight": 1.0} -->

After getting such insights from explanations, it is clear that this dataset has serious issues (which are not evident just by studying the raw data or predictions), and that this classifier, or held-out evaluation, cannot be trusted. It is also clear what the problems are, and the steps that can be taken to fix these issues and train a more trustworthy classifier.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Example 2: Deep networks for images", "weight": 1.0} -->

When using sparse linear explanations for image classifiers, one may wish to just highlight the super-pixels with positive weight towards a specific class, as they give intuition as to why the model would think that class may be present. We explain the prediction of Google's pre-trained Inception neural network in this fashion on an arbitrary image (Figure 4a). Figures 4b, 4c, 4d show the superpixels explanations for the top $3$ predicted classes (with the rest of the image grayed out), having set $K = 10$. What the neural network picks up on for each of the classes is quite natural to humans - Figure 4b in particular provides insight as to why acoustic guitar was predicted to be electric: due to the fretboard. This kind of explanation enhances trust in the classifier (even if the top predicted class is wrong), as it shows that it is not acting in an unreasonable manner.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Submodular Pick for Explaining Models", "weight": 1.0} -->

inline,color=green!20\]more structure: problem, related work, our proposal,.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Submodular Pick for Explaining Models", "weight": 1.0} -->

Although an explanation of a single prediction provides some understanding into the reliability of the classifier to the user, it is not sufficient to evaluate and assess trust in the model as a whole. We propose to give a global understanding of the model by explaining a set of individual instances. This approach is still model agnostic, and is complementary to computing summary statistics such as held-out accuracy.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Submodular Pick for Explaining Models", "weight": 1.0} -->

Even though explanations of multiple instances can be insightful, these instances need to be selected judiciously, since users may not have the time to examine a large number of explanations. We represent the time/patience that humans have by a budget $B$ that denotes the number of explanations they are willing to look at in order to understand a model. Given a set of instances $X$, we define the pick step as the task of selecting $B$ instances for the user to inspect.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Submodular Pick for Explaining Models", "weight": 1.0} -->

The pick step is not dependent on the existence of explanations - one of the main purpose of tools like Modeltracker and others is to assist users in selecting instances themselves, and examining the raw data and predictions. However, since looking at raw data is not enough to understand predictions and get insights, the pick step should take into account the explanations that accompany each prediction. Moreover, this method should pick a diverse, representative set of explanations to show the user -- i.e. non-redundant explanations that represent how the model behaves globally.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Submodular Pick for Explaining Models", "weight": 1.0} -->

Given the explanations for a set of instances $X$ (${|X|} = n$), we construct an $n \times d'$ *explanation matrix* $\mathcal{W}$ that represents the local importance of the interpretable components for each instance. When using linear models as explanations, for an instance $x_{i}$ and explanation $g_{i} = {\xi{(x_{i})}}$, we set $\mathcal{W}_{ij} = {|w_{g_{ij}}|}$. Further, for each component (column) $j$ in $\mathcal{W}$, we let $I_{j}$ denote the *global* importance of that component in the explanation space. Intuitively, we want $I$ such that features that explain many different instances have higher importance scores. In Figure 5, we show a toy example $\mathcal{W}$, with $n = d' = 5$, where $\mathcal{W}$ is binary (for simplicity).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Submodular Pick for Explaining Models", "weight": 1.0} -->

inline,color=blue!20\]Rething if we want to change f1 and f2 in figure and here The importance function $I$ should score feature f2 higher than feature f1, i.e. $I_{2} > I_{1}$, since feature f2 is used to explain more instances. Concretely for the text applications, we set $I_{j} = \sqrt{\sum_{i = 1}^{n}\mathcal{W}_{ij}}$. For images, $I$ must measure something that is comparable across the super-pixels in different images, such as color histograms or other features of super-pixels; we leave further exploration of these ideas for future work.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Submodular Pick for Explaining Models", "weight": 1.0} -->

𝒲i ← explain (xi, xi′) ⊳ Using Algorithm 1 $I_{j}\leftarrow\sqrt{\sum_{i = 1}^{n}{|\mathcal{W}_{ij}|}}$ ⊳ Compute feature importances while |V| < B do ⊳ Greedy optimization of Eq Algorithm 2 Submodular pick (SP) algorithm While we want to pick instances that cover the important components, the set of explanations must not be redundant in the components they show the users, i.e. avoid selecting instances with similar explanations. In Figure 5, after the second row is picked, the third row adds no value, as the user has already seen features f2 and f3 - while the last row exposes the user to completely new features. Selecting the second and last row results in the coverage of almost all the features. We formalize this non-redundant coverage intuition in Eq., where we define coverage as the set function $c$ that, given $\mathcal{W}$ and $I$, computes the total importance of the features that appear in at least one instance in a set $V$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Submodular Pick for Explaining Models", "weight": 1.0} -->

The pick problem, defined in Eq., consists of finding the set ${V,{|V|}} \leq B$ that achieves highest coverage.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Submodular Pick for Explaining Models", "weight": 1.0} -->

The problem in Eq. is maximizing a weighted coverage function, and is NP-hard. Let ${c{({V \cup {\{ i\}}},\mathcal{W},I)}} - {c{(V,\mathcal{W},I)}}$ be the marginal coverage gain of adding an instance $i$ to a set $V$. Due to submodularity, a greedy algorithm that iteratively adds the instance with the highest marginal coverage gain to the solution offers a constant-factor approximation guarantee of $1 - {1/e}$ to the optimum. We outline this approximation in Algorithm 2, and call it submodular pick.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Simulated User Experiments", "weight": 1.0} -->

In this section, we present simulated user experiments to evaluate the utility of explanations in trust-related tasks. In particular, we address the following questions: Are the explanations faithful to the model, Can the explanations aid users in ascertaining trust in predictions, and Are the explanations useful for evaluating the model as a whole. Code and data for replicating our experiments are available at

<!-- chunk {"id": "body-0045", "role": "body", "section": "Experiment Setup", "weight": 1.0} -->

We use two sentiment analysis datasets where the task is to classify product reviews as positive or negative. We train decision trees (DT), logistic regression with L2 regularization (LR), nearest neighbors (NN), and support vector machines with RBF kernel (SVM), all using bag of words as features. We also include random forests (with $1000$ trees) trained with the average word2vec embedding (RF), a model that is impossible to interpret without a technique like LIME. We use the implementations and default parameters of scikit-learn, unless noted otherwise. We divide each dataset into train (1600 instances) and test (400 instances).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Experiment Setup", "weight": 1.0} -->

To explain individual predictions, we compare our proposed approach (LIME), with parzen, a method that approximates the black box classifier globally with Parzen windows, and explains individual predictions by taking the gradient of the prediction probability function. For parzen, we take the $K$ features with the highest absolute gradients as explanations. We set the hyper-parameters for parzen and LIME using cross validation, and set $N = {15,000}$. We also compare against a greedy procedure (similar to Martens and Provost ) in which we greedily remove features that contribute the most to the predicted class until the prediction changes (or we reach the maximum of $K$ features), and a random procedure that randomly picks $K$ features as an explanation. We set $K$ to $10$ for our experiments.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Experiment Setup", "weight": 1.0} -->

For experiments where the pick procedure applies, we either do random selection (random pick, RP) or the procedure described in §4 (submodular pick, SP). We refer to pick-explainer combinations by adding RP or SP as a prefix.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Are explanations faithful to the model?", "weight": 1.0} -->

We measure faithfulness of explanations on classifiers that are by themselves interpretable (sparse logistic regression and decision trees). In particular, we train both classifiers such that the maximum number of features they use for any instance is $10$, and thus we know the *gold* set of features that the are considered important by these models. For each prediction on the test set, we generate explanations and compute the fraction of these *gold* features that are recovered by the explanations. We report this recall averaged over all the test instances in Figures 6 and 7. We observe that the greedy approach is comparable to parzen on logistic regression, but is substantially worse on decision trees since changing a single feature at a time often does not have an effect on the prediction. The overall recall by parzen is low, likely due to the difficulty in approximating the original high-dimensional classifier. LIME consistently provides $> {90\%}$ recall for both classifiers on both datasets, demonstrating that LIME explanations are faithful to the models.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Should I trust this prediction?", "weight": 1.0} -->

In order to simulate trust in individual predictions, we first randomly select $25\%$ of the features to be "untrustworthy", and assume that the users can identify and would not want to trust these features (such as the headers in 20 newsgroups, leaked data, etc). We thus develop *oracle* "trustworthiness" by labeling test set predictions from a black box classifier as "untrustworthy" if the prediction changes when untrustworthy features are removed from the instance, and "trustworthy" otherwise. In order to simulate users, we assume that users deem predictions untrustworthy from LIME and parzen explanations if the prediction from the linear approximation changes when all untrustworthy features that appear in the explanations are removed (the simulated human "discounts" the effect of untrustworthy features). For greedy and random, the prediction is mistrusted if any untrustworthy features are present in the explanation, since these methods do not provide a notion of the contribution of each feature to the prediction. Thus for each test set prediction, we can evaluate whether the simulated user trusts it using each explanation method, and compare it to the trustworthiness oracle.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Should I trust this prediction?", "weight": 1.0} -->

Using this setup, we report the F1 on the trustworthy predictions for each explanation method, averaged over $100$ runs, in Table 1. The results indicate that LIME dominates others (all results are significant at $p = 0.01$) on both datasets, and for all of the black box models. The other methods either achieve a lower recall (i.e. they mistrust predictions more than they should) or lower precision (i.e. they trust too many predictions), while LIME maintains both high precision and high recall. Even though we artificially select which features are untrustworthy, these results indicate that LIME is helpful in assessing trust in individual predictions.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Can I trust this model?", "weight": 1.0} -->

In the final simulated user experiment, we evaluate whether the explanations can be used for model selection, simulating the case where a human has to decide between two competing models with similar accuracy on validation data. For this purpose, we add $10$ artificially "noisy" features. Specifically, on training and validation sets ($80/20$ split of the original training data), each artificial feature appears in $10\%$ of the examples in one class, and $20\%$ of the other, while on the test instances, each artificial feature appears in $10\%$ of the examples in each class. This recreates the situation where the models use not only features that are informative in the real world, but also ones that introduce spurious correlations. We create pairs of competing classifiers by repeatedly training pairs of random forests with $30$ trees until their validation accuracy is within $0.1\%$ of each other, but their test accuracy differs by at least $5\%$. Thus, it is not possible to identify the *better* classifier (the one with higher test accuracy) from the accuracy on the validation data.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Can I trust this model?", "weight": 1.0} -->

The goal of this experiment is to evaluate whether a user can identify the better classifier based on the explanations of $B$ instances from the validation set. The simulated human marks the set of artificial features that appear in the $B$ explanations as untrustworthy, following which we evaluate how many total predictions in the validation set should be trusted (as in the previous section, treating only marked features as untrustworthy). Then, we select the classifier with fewer untrustworthy predictions, and compare this choice to the classifier with higher held-out test set accuracy.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Can I trust this model?", "weight": 1.0} -->

We present the accuracy of picking the correct classifier as $B$ varies, averaged over $800$ runs, in Figure 8. We omit SP-parzen and RP-parzen from the figure since they did not produce useful explanations, performing only slightly better than random. LIME is consistently better than greedy, irrespective of the pick method. Further, combining submodular pick with LIME outperforms all other methods, in particular it is much better than RP-LIME when only a few examples are shown to the users. These results demonstrate that the trust assessments provided by SP-selected LIME explanations are good indicators of generalization, which we validate with human experiments in the next section.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Evaluation with human subjects", "weight": 1.0} -->

In this section, we recreate three scenarios in machine learning that require trust and understanding of predictions and models. In particular, we evaluate LIME and SP-LIME in the following settings: Can users choose which of two classifiers generalizes better (§ 6.2), based on the explanations, can users perform feature engineering to improve the model (§ 6.3), and are users able to identify and describe classifier irregularities by looking at explanations (§ 6.4).

<!-- chunk {"id": "body-0055", "role": "body", "section": "Experiment setup", "weight": 1.0} -->

For experiments in §6.2 and §6.3, we use the "Christianity" and "Atheism" documents from the 20 newsgroups dataset mentioned beforehand. This dataset is problematic since it contains features that do not generalize (e.g. very informative header information and author names), and thus validation accuracy considerably overestimates real-world performance.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Experiment setup", "weight": 1.0} -->

In order to estimate the real world performance, we create a new *religion dataset* for evaluation. We download Atheism and Christianity websites from the DMOZ directory and human curated lists, yielding $819$ webpages in each class. High accuracy on this dataset by a classifier trained on 20 newsgroups indicates that the classifier is generalizing using semantic content, instead of placing importance on the data specific issues outlined above. Unless noted otherwise, we use SVM with RBF kernel, trained on the 20 newsgroups data with hyper-parameters tuned via the cross-validation.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Can users select the best classifier?", "weight": 1.0} -->

In this section, we want to evaluate whether explanations can help users decide which classifier generalizes better, i.e., which classifier would the user deploy "in the wild". Specifically, users have to decide between two classifiers: SVM trained on the original 20 newsgroups dataset, and a version of the same classifier trained on a "cleaned" dataset where many of the features that do not generalize have been manually removed. The original classifier achieves an accuracy score of $57.3\%$ on the *religion dataset*, while the "cleaned" classifier achieves a score of $69.0\%$. In contrast, the test accuracy on the original 20 newsgroups split is $94.0\%$ and $88.6\%$, respectively -- suggesting that the worse classifier would be selected if accuracy alone is used as a measure of trust.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Can users select the best classifier?", "weight": 1.0} -->

We recruit human subjects on Amazon Mechanical Turk -- by no means machine learning experts, but instead people with basic knowledge about religion. We measure their ability to choose the better algorithm by seeing side-by-side explanations with the associated raw data (as shown in Figure 2). We restrict both the number of words in each explanation ($K$) and the number of documents that each person inspects ($B$) to $6$. The position of each algorithm and the order of the instances seen are randomized between subjects. After examining the explanations, users are asked to select which algorithm will perform best in the real world. The explanations are produced by either greedy (chosen as a baseline due to its performance in the simulated user experiment) or LIME, and the instances are selected either by random (RP) or submodular pick (SP). We modify the greedy step in Algorithm 2 slightly so it alternates between explanations of the two classifiers. For each setting, we repeat the experiment with $100$ users.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Can users select the best classifier?", "weight": 1.0} -->

The results are presented in Figure 9. Note that all of the methods are good at identifying the better classifier, demonstrating that the explanations are useful in determining which classifier to trust, while using test set accuracy would result in the selection of the wrong classifier. Further, we see that the submodular pick (SP) greatly improves the user's ability to select the best classifier when compared to random pick (RP), with LIME outperforming greedy in both cases.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Can non-experts improve a classifier?", "weight": 1.0} -->

If one notes that a classifier is untrustworthy, a common task in machine learning is feature engineering, i.e. modifying the set of features and retraining in order to improve generalization. Explanations can aid in this process by presenting the important features, particularly for removing features that the users feel do not generalize.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Can non-experts improve a classifier?", "weight": 1.0} -->

We use the 20 newsgroups data here as well, and ask Amazon Mechanical Turk users to identify which words from the explanations should be removed from subsequent training, for the worse classifier from the previous section (§6.2). In each round, the subject marks words for deletion after observing $B = 10$ instances with $K = 10$ words in each explanation (an interface similar to Figure 2, but with a single algorithm). As a reminder, the users here are not experts in machine learning and are unfamiliar with feature engineering, thus are only identifying words based on their semantic content. Further, users do not have any access to the *religion* dataset -- they do not even know of its existence. We start the experiment with $10$ subjects. After they mark words for deletion, we train $10$ different classifiers, one for each subject (with the corresponding words removed). The explanations for each classifier are then presented to a set of $5$ users in a new round of interaction, which results in $50$ new classifiers.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Can non-experts improve a classifier?", "weight": 1.0} -->

We do a final round, after which we have $250$ classifiers, each with a path of interaction tracing back to the first $10$ subjects.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Can non-experts improve a classifier?", "weight": 1.0} -->

The explanations and instances shown to each user are produced by SP-LIME or RP-LIME. We show the average accuracy on the *religion* dataset at each interaction round for the paths originating from each of the original $10$ subjects (shaded lines), and the average across all paths (solid lines) in Figure 10. It is clear from the figure that the crowd workers are able to improve the model by removing features they deem unimportant for the task. Further, SP-LIME outperforms RP-LIME, indicating selection of the instances to show the users is crucial for efficient feature engineering.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Can non-experts improve a classifier?", "weight": 1.0} -->

Each subject took an average of $3.6$ minutes per round of cleaning, resulting in just under 11 minutes to produce a classifier that generalizes much better to real world data. Each path had on average $200$ words removed with SP, and $157$ with RP, indicating that incorporating coverage of important features is useful for feature engineering. Further, out of an average of $200$ words selected with SP, $174$ were selected by at least half of the users, while $68$ by *all* the users. Along with the fact that the variance in the accuracy decreases across rounds, this high agreement demonstrates that the users are converging to similar *correct* models. This evaluation is an example of how explanations make it easy to improve an untrustworthy classifier -- in this case easy enough that machine learning knowledge is not required.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Do explanations lead to insights?", "weight": 1.0} -->

Often artifacts of data collection can induce undesirable correlations that the classifiers pick up during training. These issues can be very difficult to identify just by looking at the raw data and predictions. In an effort to reproduce such a setting, we take the task of distinguishing between photos of Wolves and Eskimo Dogs (huskies). We train a logistic regression classifier on a training set of $20$ images, hand selected such that all pictures of wolves had snow in the background, while pictures of huskies did not. As the features for the images, we use the first max-pooling layer of Google's pre-trained Inception neural network. On a collection of additional $60$ images, the classifier predicts "Wolf" if there is snow (or light background at the bottom), and "Husky" otherwise, regardless of animal color, position, pose, etc. We trained this *bad* classifier intentionally, to evaluate whether subjects are able to detect it.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Do explanations lead to insights?", "weight": 1.0} -->

The experiment proceeds as follows: we first present a balanced set of $10$ test predictions (without explanations), where one wolf is not in a snowy background (and thus the prediction is "Husky") and one husky is (and is thus predicted as "Wolf"). We show the "Husky" mistake in Figure 11a. The other $8$ examples are classified correctly. We then ask the subject three questions: Do they trust this algorithm to work well in the real world, why, and how do they think the algorithm is able to distinguish between these photos of wolves and huskies. After getting these responses, we show the same images with the associated explanations, such as in Figure 11b, and ask the same questions.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Do explanations lead to insights?", "weight": 1.0} -->

(a) Husky classified as wolf Figure 11: Raw data and explanation of a bad model’s prediction in the “Husky vs Wolf” task.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Do explanations lead to insights?", "weight": 1.0} -->

Since this task requires some familiarity with the notion of spurious correlations and generalization, the set of subjects for this experiment were graduate students who have taken at least one graduate machine learning course. After gathering the responses, we had $3$ independent evaluators read their reasoning and determine if each subject mentioned snow, background, or equivalent as a feature the model may be using. We pick the majority to decide whether the subject was correct about the insight, and report these numbers before and after showing the explanations in Table 2.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Do explanations lead to insights?", "weight": 1.0} -->

Trusted the bad model Snow as a potential feature Table 2: “Husky vs Wolf” experiment results.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Do explanations lead to insights?", "weight": 1.0} -->

Before observing the explanations, more than a third trusted the classifier, and a little less than half mentioned the snow pattern as something the neural network was using -- although all speculated on other patterns. After examining the explanations, however, almost all of the subjects identified the correct insight, with much more certainty that it was a determining factor. Further, the trust in the classifier also dropped substantially. Although our sample size is small, this experiment demonstrates the utility of explaining individual predictions for getting insights into classifiers knowing when not to trust them and why.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

In this paper, we argued that trust is crucial for effective human interaction with machine learning systems, and that explaining individual predictions is important in assessing trust. We proposed LIME, a modular and extensible approach to faithfully explain the predictions of *any* model in an interpretable manner. We also introduced SP-LIME, a method to select representative and non-redundant predictions, providing a global view of the model to users. Our experiments demonstrated that explanations are useful for a variety of models in trust-related tasks in the text and image domains, with both expert and non-expert users: deciding between models, assessing trust, improving untrustworthy models, and getting insights into predictions.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

There are a number of avenues of future work that we would like to explore. Although we describe only sparse linear models as explanations, our framework supports the exploration of a variety of explanation families, such as decision trees; it would be interesting to see a comparative study on these with real users. One issue that we do not mention in this work was how to perform the pick step for images, and we would like to address this limitation in the future. The domain and model agnosticism enables us to explore a variety of applications, and we would like to investigate potential uses in speech, video, and medical domains, as well as recommendation systems. Finally, we would like to explore theoretical properties (such as the appropriate number of samples) and computational optimizations (such as using parallelization and GPU processing), in order to provide the accurate, real-time explanations that are critical for any human-in-the-loop machine learning system.
