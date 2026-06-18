<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification

Topics include Conformal prediction, Distribution-free uncertainty quantification, Prediction sets, Prediction intervals, Split conformal prediction, Distribution shift, Structured prediction, Tutorial.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Gives a practical, example-driven introduction to conformal prediction as a wrapper for producing finite-sample-valid uncertainty sets around black-box models. Its main value is pedagogical breadth: it connects the basic split conformal recipe to modern applications involving images, language, time series, abstention, distribution shift, and structured outputs.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Black-box machine learning models are now routinely used in high-risk settings, like medical diagnostics, which demand uncertainty quantification to avoid consequential model failures. Conformal prediction is a user-friendly paradigm for creating statistically rigorous uncertainty sets/intervals for the predictions of such models. Critically, the sets are valid in a distribution-free sense: they possess explicit, non-asymptotic guarantees even without distributional assumptions or model assumptions. One can use conformal prediction with any pre-trained model, such as a neural network, to produce sets that are guaranteed to contain the ground truth with a user-specified probability, such as 90%. It is easy-to-understand, easy-to-use, and general, applying naturally to problems arising in the fields of computer vision, natural language processing, deep reinforcement learning, and so . This hands-on introduction is aimed to provide the reader a working understanding of conformal prediction and related distribution-free uncertainty quantification techniques with one self-contained document.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We lead the reader through practical theory for and examples of conformal prediction and describe its extensions to complex machine learning tasks involving structured outputs, distribution shift, time-series, outliers, models that abstain, and more. Throughout, there are many explanatory illustrations, examples, and code samples in Python. With each code sample comes a Jupyter notebook implementing the method on a real-data example; the notebooks can be accessed and easily run using our codebase.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Abstract", "weight": 1.5} -->

Black-box machine learning models are now routinely used in high-risk settings, like medical diagnostics, which demand uncertainty quantification to avoid consequential model failures. Conformal prediction (a.k.a. conformal inference) is a user-friendly paradigm for creating statistically rigorous uncertainty sets/intervals for the predictions of such models. Critically, the sets are valid in a *distribution-free* sense: they possess explicit, non-asymptotic guarantees even without distributional assumptions or model assumptions. One can use conformal prediction with any pre-trained model, such as a neural network, to produce sets that are guaranteed to contain the ground truth with a user-specified probability, such as $90\%$. It is easy-to-understand, easy-to-use, and general, applying naturally to problems arising in the fields of computer vision, natural language processing, deep reinforcement learning, and so.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Abstract", "weight": 1.5} -->

This hands-on introduction is aimed to provide the reader a working understanding of conformal prediction and related distribution-free uncertainty quantification techniques with one self-contained document. We lead the reader through practical theory for and examples of conformal prediction and describe its extensions to complex machine learning tasks involving structured outputs, distribution shift, time-series, outliers, models that abstain, and more. Throughout, there are many explanatory illustrations, examples, and code samples in Python. With each code sample comes a Jupyter notebook implementing the method on a real-data example; the notebooks can be accessed and easily run by clicking on the following icons:.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Contents", "weight": 1.0} -->

1. 1.1 Instructions for Conformal Prediction
2. 2 Examples of Conformal Procedures
1. 2.1 Classification with Adaptive Prediction Sets
2. 2.2 Conformalized Quantile Regression
3. 2.3 Conformalizing Scalar Uncertainty Estimates
1. 2.3.1 The Estimated Standard Deviation
2. 2.3.2 Other 1-D Uncertainty Estimates
3. 3 Evaluating Conformal Prediction
2. 3.2 The Effect of the Size of the Calibration Set
3. 3.3 Checking for Correct Coverage
4. 4 Extensions of Conformal Prediction
1. 4.1 Group-Balanced Conformal Prediction
2. 4.2 Class-Conditional Conformal Prediction
3. 4.3 Conformal Risk Control
5. 4.5 Conformal Prediction Under Covariate Shift
6. 4.6 Conformal Prediction Under Distribution Drift
3. 5.3 Weather Prediction with Time-Series Distribution Shift
4. 5.4 Toxic Online Comment Identification via Outlier Detection
6. 6 Full conformal prediction
1. 6.1 Full Conformal Prediction
2. 6.2 Cross-Conformal Prediction, CV+, and Jackknife+
7. 7 Historical Notes on Conformal Prediction

<!-- chunk {"id": "body-0008", "role": "body", "section": "Conformal Prediction", "weight": 1.0} -->

Conformal prediction \[vovk2005algorithmic, papadopoulos2002inductive, lei2014distribution\] (a.k.a. conformal inference) is a straightforward way to generate prediction sets for any model. We will introduce it with a short, pragmatic image classification example, and follow up in later paragraphs with a general explanation. The high-level outline of conformal prediction is as follows. First, we begin with a fitted predicted model (such as a neural network classifier) which we will call $\hat{f}$. Then, we will create prediction sets (a set of possible labels) for this classifier using a small amount of additional *calibration data*---we will sometimes call this the *calibration step*.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Conformal Prediction", "weight": 1.0} -->

Formally, suppose we have images as input and they each contain one of $K$ classes. We begin with a classifier that outputs estimated probabilities (softmax scores) for each class: ${\hat{f}{(x)}} \in {\lbrack 0,1\rbrack}^{K}$. Then, we reserve a moderate number (e.g., 500) of fresh i.i.d. pairs of images and classes unseen during training, ${(X_{1},Y_{1})},\ldots,{(X_{n},Y_{n})}$, for use as calibration data.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Conformal Prediction", "weight": 1.0} -->

where $(X_{test},Y_{test})$ is a fresh test point from the same distribution, and $\alpha \in {\lbrack 0,1\rbrack}$ is a user-chosen error rate. In words, the probability that the prediction set contains the correct label is almost exactly $1 - \alpha$; we call this property *marginal coverage*, since the probability is marginal (averaged) over the randomness in the calibration and test points. See Figure 1 for examples of prediction sets on the Imagenet dataset.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Conformal Prediction", "weight": 1.0} -->

## get conformal scores. n = calib_Y.shape
cal_smx = model(calib_X).softmax(dim=1).numpy
cal_scores = 1-cal_smx[np.arange(n),cal_labels]
## get adjusted quantile
q_level = np.ceil((n+1)*(1-alpha))/n
qhat = np.quantile(cal_scores, q_level, method=’higher’)
val_smx = model(val_X).softmax(dim=1).numpy
prediction_sets = val_smx &gt;= (1-qhat) # 3: form prediction sets
Figure 2: Illustration of conformal prediction with matching Python code.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Conformal Prediction", "weight": 1.0} -->

To construct $\mathcal{C}$ from $\hat{f}$ and the calibration data, we will perform a simple calibration step that requires only a few lines of code; see the right panel of Figure 2. We now describe the calibration step in more detail, introducing some terms that will be helpful later. First, we set the *conformal score* $s_{i} = {1 - {\hat{f}{(X_{i})}_{Y_{i}}}}$ to be one minus the softmax output of the true class. The score is high when the softmax output of the true class is low, i.e., when the model is badly wrong.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Conformal Prediction", "weight": 1.0} -->

Next comes the critical step: define $\hat{q}$ to be the ${\lceil{{({n + 1})}{({1 - \alpha})}}\rceil}/n$ empirical quantile of $s_{1},\ldots,s_{n}$, where $\lceil \cdot \rceil$ is the ceiling function ($\hat{q}$ is essentially the $1 - \alpha$ quantile, but with a small correction). Finally, for a new test data point (where $X_{test}$ is known but $Y_{test}$ is not), create a prediction set ${\mathcal{C}{(X_{test})}} = {\{ y:{{\hat{f}{(X_{test})}_{y}} \geq {1 - \hat{q}}}\}}$ that includes all classes with a high enough softmax output (see Figure 2).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Conformal Prediction", "weight": 1.0} -->

Remarkably, this algorithm gives prediction sets that are guaranteed to satisfy, no matter what (possibly incorrect) model is used or what the (unknown) distribution of the data is.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Remarks", "weight": 1.0} -->

Let us think about the interpretation of $\mathcal{C}$. The function $\mathcal{C}$ is *set-valued*---it takes in an image, and it outputs a set of classes as in Figure 1. The model's softmax outputs help to generate the set. This method constructs a different output set *adaptively to each particular input*. The sets become larger when the model is uncertain or the image is intrinsically hard. This is a property we want, because the size of the set gives you an indicator of the model's certainty. Furthermore, $\mathcal{C}{(X_{test})}$ can be interpreted as a set of plausible classes that the image $X_{test}$ could be assigned to. Finally, $\mathcal{C}$ is *valid*, meaning it satisfies.^11^1Due to the discreteness of $Y$, a small modification involving tie-breaking is needed to additionally satisfy the upper bound (see \[angelopoulos2020sets\] for details; this randomization is usually ignored in practice). We will henceforth ignore such tie-breaking.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Remarks", "weight": 1.0} -->

These properties of $\mathcal{C}$ translate naturally to other machine learning problems, like regression, as we will see.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Remarks", "weight": 1.0} -->

With an eye towards generalization, let us review in detail what happened in our classification problem. To begin, we were handed a model that had an inbuilt, but heuristic, notion of uncertainty: softmax outputs. The softmax outputs attempted to measure the conditional probability of each class; in other words, the $j$th entry of the softmax vector estimated ${\mathbb{P}}{({Y = {j \mid X} = x})}$, the probability of class $j$ conditionally on an input image $x$. However, we had no guarantee that the softmax outputs were any good; they may have been arbitrarily overfit or otherwise untrustworthy. Therefore, instead of taking the softmax outputs at face value, we used the holdout set to adjust for their deficiencies.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Remarks", "weight": 1.0} -->

The holdout set contained $n \approx 500$ fresh data points that the model never saw during training, which allowed us to get an honest appraisal of its performance. The adjustment involved computing conformal scores, which grow when the model is uncertain, but are not valid prediction intervals on their own. In our case, the conformal score was one minus the softmax output of the true class, but in general, the score can be any function of $x$ and $y$. We then took $\hat{q}$ to be roughly the $1 - \alpha$ quantile of the scores. In this case, the quantile had a simple interpretation---when setting $\alpha = 0.1$, at least $90\%$ of ground truth softmax outputs are guaranteed to be above the level $1 - \hat{q}$ (we prove this rigorously in Appendix LABEL:app:coverage-proof).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Remarks", "weight": 1.0} -->

Taking advantage of this fact, at test-time, we got the softmax outputs of a new image $X_{test}$ and collected all classes with outputs above $1 - \hat{q}$ into a prediction set $\mathcal{C}{(X_{test})}$. Since the softmax output of the new true class $Y_{test}$ is guaranteed to be above $1 - \hat{q}$ with probability at least $90\%$, we finally got the guarantee in Eq..

<!-- chunk {"id": "body-0020", "role": "body", "section": "Instructions for Conformal Prediction", "weight": 1.0} -->

As we said during the summary, conformal prediction is not specific to softmax outputs or classification problems. In fact, conformal prediction can be seen as a method for taking any heuristic notion of uncertainty from any model and converting it to a rigorous one (see the diagram below). Conformal prediction does not care if the underlying prediction problem is discrete/continuous or classification/regression.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Instructions for Conformal Prediction", "weight": 1.0} -->

We next outline conformal prediction for a general input $x$ and output $y$ (not necessarily discrete).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Instructions for Conformal Prediction", "weight": 1.0} -->

Identify a heuristic notion of uncertainty using the pre-trained model.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Instructions for Conformal Prediction", "weight": 1.0} -->

Define the score function ${s{(x,y)}} \in {\mathbb{R}}$. (Larger scores encode worse agreement between $x$ and $y$.)

<!-- chunk {"id": "body-0024", "role": "body", "section": "Instructions for Conformal Prediction", "weight": 1.0} -->

As before, these sets satisfy the validity property, for any (possibly uninformative) score function and (possibly unknown) distribution of the data. We formally state the coverage guarantee next.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Choice of score function", "weight": 1.0} -->

*How is it possible to construct a statistically valid prediction set even if the heuristic notion of uncertainty of the underlying model is arbitrarily bad?*

<!-- chunk {"id": "body-0026", "role": "body", "section": "Choice of score function", "weight": 1.0} -->

Let's give some intuition to supplement the mathematical understanding from the proof in Appendix LABEL:app:coverage-proof. Roughly, if the scores $s_{i}$ correctly rank the inputs from lowest to highest magnitude of model error, then the resulting sets will be smaller for easy inputs and bigger for hard ones. If the scores are bad, in the sense that they do not approximate this ranking, then the sets will be useless. For example, if the scores are random noise, then the sets will contain a random sample of the label space, where that random sample is large enough to provide valid marginal coverage. This illustrates an important underlying fact about conformal prediction: although the guarantee always holds, the usefulness of the prediction sets is primarily determined by the score function. This should be no surprise---the score function incorporates almost all the information we know about our problem and data, including the underlying model itself. For example, the main difference between applying conformal prediction on classification problems versus regression problems is the choice of score. There are also many possible score functions for a single underlying model, which have different properties. Therefore, constructing the right score function is an important engineering choice. We will next show a few examples of good score functions.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Examples of Conformal Procedures", "weight": 1.0} -->

In this section we give examples of conformal prediction applied in many settings, with the goal of providing the reader a bank of techniques to practically deploy. Note that we will focus only on one-dimensional $Y$ in this section, and smaller conformal scores will correspond to more model confidence (such scores are called nonconformity scores). Richer settings, such as high-dimensional $Y$, complicated (or multiple) notions of error, or where different mistakes cost different amounts, often require the language of *risk control*, outlined in Section LABEL:app:ltt.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Classification with Adaptive Prediction Sets", "weight": 1.0} -->

## Get scores. calib_X.shape == calib_Y.shape == n cal_pi = cal_smx.argsort; cal_srt = np.take_along_axis(cal_smx,cal_pi,axis=1).cumsum(axis=1) cal_scores = np.take_along_axis(cal_srt,cal_pi.argsort(axis=1),axis=1)[range(n),cal_labels] ## Get the score quantile qhat = np.quantile(cal_scores, np.ceil((n+1)*(1-alpha))/n, interpolation=’higher’) ## Deploy (output=list of length n, each element is tensor of classes) val_pi = val_smx.argsort; val_srt = np.take_along_axis(val_smx,val_pi,axis=1).cumsum(axis=1) prediction_sets = np.take_along_axis(val_srt &lt;=

<!-- chunk {"id": "body-0029", "role": "body", "section": "Classification with Adaptive Prediction Sets", "weight": 1.0} -->

qhat,val_pi.argsort(axis=1),axis=1)

<!-- chunk {"id": "body-0030", "role": "body", "section": "Classification with Adaptive Prediction Sets", "weight": 1.0} -->

Let's begin our sequence of examples with an improvement to the classification example in Section 1. The previous method produces prediction sets with the smallest average size \[Sadinle2016LeastAS\], but it tends to undercover hard subgroups and overcover easy ones. Here we develop a different method called *adaptive prediction sets* (APS) that avoids this problem. We will follow \[romano2020classification\] and \[angelopoulos2020sets\].

<!-- chunk {"id": "body-0031", "role": "body", "section": "Classification with Adaptive Prediction Sets", "weight": 1.0} -->

As motivation for this new procedure, note that if the softmax outputs $\hat{f}{(X_{test})}$ were a perfect model of $\left. Y_{test} \middle| X_{test} \right.$, we would greedily include the top-scoring classes until their total mass just exceeded $1 - \alpha$. Formally, we can describe this oracle algorithm as

<!-- chunk {"id": "body-0032", "role": "body", "section": "Classification with Adaptive Prediction Sets", "weight": 1.0} -->

and $\pi{(x)}$ is the permutation of $\{ 1,\ldots,K\}$ that sorts $\hat{f}{(X_{test})}$ from most likely to least likely. In practice, however, this procedure fails to provide coverage, since $\hat{f}{(X_{test})}$ is not perfect; it only provides us a heuristic notion of uncertainty. Therefore, we will use conformal prediction to turn this into a rigorous notion of uncertainty.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Classification with Adaptive Prediction Sets", "weight": 1.0} -->

In other words, we greedily include classes in our set until we reach the true label, then we stop. Unlike the score from Section 1, this one utilizes the softmax outputs of all classes, not just the true class.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Conformalized Quantile Regression", "weight": 1.0} -->

We will next show how to incorporate uncertainty into regression problems with a continuous output, following the algorithm in \[romano2019conformalized\]. We use quantile regression \[koenker1978regression\] as our base model. As a reminder, the quantile regression algorithm attempts to learn the $\gamma$ quantile of $\left. Y_{test} \middle| X_{test} \right. = x$ for each possible value of $x$. We will call the true quantile $t_{\gamma}{(x)}$ and the fitted model ${\hat{t}}_{\gamma}{(x)}$. Since by definition $\left. Y_{test} \middle| X_{test} \right.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Conformalized Quantile Regression", "weight": 1.0} -->

= x$ lands below $t_{0.05}{(x)}$ with $5\%$ probability and above $t_{0.95}{(x)}$ with $5\%$ probability, we would expect the interval $\left\lbrack {{\hat{t}}_{0.05}{(x)}},{{\hat{t}}_{0.95}{(x)}} \right\rbrack$ to have approximately 90% coverage. However, because the fitted quantiles may be inaccurate, we will conformalize them. Python pseudocode for conformalized quantile regression is in Figure 5.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Conformalized Quantile Regression", "weight": 1.0} -->

After training an algorithm to output two such quantiles (this can be done with a standard loss function, see below), $t_{\alpha/2}$ and $t_{1 - {\alpha/2}}$, we can define the score to be the difference between $y$ and its nearest quantile,

<!-- chunk {"id": "body-0037", "role": "body", "section": "Conformalized Quantile Regression", "weight": 1.0} -->

After computing the scores on our calibration set and setting $\hat{q} = {{Quantile}{(s_{1},\ldots,s_{n};\frac{\lceil{{({n + 1})}{({1 - \alpha})}}\rceil}{n})}}$, we can form valid prediction intervals by taking

<!-- chunk {"id": "body-0038", "role": "body", "section": "Conformalized Quantile Regression", "weight": 1.0} -->

Intuitively, the set $\mathcal{C}{(x)}$ just grows or shrinks the distance between the quantiles by $\hat{q}$ to achieve coverage.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Conformalized Quantile Regression", "weight": 1.0} -->

## Get scores
cal_scores = np.maximum(cal_labels-model_upper(cal_X), model_lower(cal_X)-cal_labels)
## Get the score quantile
qhat = np.quantile(cal_scores, np.ceil((n+1)*(1-alpha))/n, interpolation=’higher’)
## Deploy (output=lower and upper adjusted quantiles)
prediction_sets = [val_lower - qhat, val_upper + qhat]
Figure 5: Python code for conformalized quantile regression.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Conformalized Quantile Regression", "weight": 1.0} -->

As before, $\mathcal{C}$ satisfies the coverage property in Eq.. However, unlike our previous example in Section 1, $\mathcal{C}$ is no longer a set of classes, but instead a *continuous interval* in $\mathbb{R}$. Quantile regression is not the only way to get such continuous-valued intervals. However, it is often the best way, especially if $\alpha$ is known in advance. The reason is that the intervals generated via quantile regression even without conformal prediction, i.e. $\lbrack{{\hat{t}}_{\alpha/2}{(x)}},{{\hat{t}}_{1 - {\alpha/2}}{(x)}}\rbrack$, have good coverage to begin. Furthermore, they have asymptotically valid conditional coverage (a concept we will explain in Section 3). These properties propagate through the conformal procedure and lead to prediction sets with good performance.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Conformalized Quantile Regression", "weight": 1.0} -->

One attractive feature of quantile regression is that it can easily be added on top of any base model simply by changing the loss function to a *quantile loss* (informally referred to as a *pinball loss*),

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conformalized Quantile Regression", "weight": 1.0} -->

The reader can think of quantile regression as a generalization of L1-norm regression: when $\gamma = 0.5$, the loss function reduces to $L_{0.5} = {{|{{{\hat{t}}_{\gamma}{(x)}} - y}|}/2}$, which encourages ${\hat{t}}_{0.5}{(x)}$ to converge to the conditional median. Changing $\gamma$ just modifies the L1 norm as in the illustration above to target other quantiles. In practice, one can just use a quantile loss instead of MSE at the end of any algorithm, like a neural network, in order to regress to a quantile.

<!-- chunk {"id": "body-0043", "role": "body", "section": "The Estimated Standard Deviation", "weight": 1.0} -->

As an alternative to quantile regression, our next example is a different way of constructing prediction sets for continuous $y$ with a less rich but more common notion of heuristic uncertainty: an estimate of the standard deviation $\hat{\sigma}{(x)}$. For example, one can produce uncertainty scalars by assuming ${Y_{test} \mid X_{test}} = x$ follows some parametric distribution---like a Gaussian distribution---and training a model to output the mean and variance of that distribution.

<!-- chunk {"id": "body-0044", "role": "body", "section": "The Estimated Standard Deviation", "weight": 1.0} -->

This strategy is so common that it is commoditized: there are inbuilt PyTorch losses, such as GaussianNLLLoss, that enable training a neural network this way. However, we usually know $Y_{test} \mid X_{test}$ isn't Gaussian, so even if we had infinite data, $\hat{\sigma}{(x)}$ would not necessarily be reliable. We can use conformal prediction to turn this heuristic uncertainty notion into rigorous prediction intervals of the form ${\hat{f}{(x)}} \pm {\hat{q}\hat{\sigma}{(x)}}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Other 1-D Uncertainty Estimates", "weight": 1.0} -->

More generally, we assume there is a function $u{(x)}$ such that larger values encode more uncertainty. This single number can have many interpretations beyond the standard deviation. For example, one instance of an uncertainty scalar simply involves the user creating a model for the magnitude of the residual. In that setting, the user would first fit a model $\hat{f}$ that predicts $y$ from $x$. Then, they would fit a second model $\hat{r}$ (possibly the same neural network), that predicts $\left| {y - {\hat{f}{(x)}}} \right|$. If $\hat{r}$ were perfect, we would expect the set $\left\lbrack {{\hat{f}{(x)}} - {\hat{r}{(x)}}},{{\hat{f}{(x)}} + {\hat{r}{(x)}}} \right\rbrack$ to have perfect coverage. However, our learned model of the error $\hat{r}$ is often poor in practice.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Other 1-D Uncertainty Estimates", "weight": 1.0} -->

There are many more such uncertainty scalars than we can discuss in this document in detail, including

<!-- chunk {"id": "body-0047", "role": "body", "section": "Other 1-D Uncertainty Estimates", "weight": 1.0} -->

measuring the variance of $\hat{f}{(x)}$ across an ensemble of models,

<!-- chunk {"id": "body-0048", "role": "body", "section": "Other 1-D Uncertainty Estimates", "weight": 1.0} -->

measuring the variance of $\hat{f}{(x)}$ when randomly dropping out a fraction of nodes in a neural net,

<!-- chunk {"id": "body-0049", "role": "body", "section": "Other 1-D Uncertainty Estimates", "weight": 1.0} -->

measuring the variance of $\hat{f}{(x)}$ to small, random input perturbations,

<!-- chunk {"id": "body-0050", "role": "body", "section": "Other 1-D Uncertainty Estimates", "weight": 1.0} -->

measuring the variance of $\hat{f}{(x)}$ over different noise samples input to a generative model,

<!-- chunk {"id": "body-0051", "role": "body", "section": "Other 1-D Uncertainty Estimates", "weight": 1.0} -->

measuring the magnitude of change in $\hat{f}{(x)}$ when applying an adversarial perturbation, etc.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Other 1-D Uncertainty Estimates", "weight": 1.0} -->

These cases will all be treated the same way. There will be some point prediction $\hat{f}{(x)}$, and some uncertainty scalar $u{(x)}$ that is large when the model is uncertain and small otherwise (in the residual setting, ${u{(x)}}:={\hat{r}{(x)}}$, and in the Gaussian setting, ${u{(x)}}:={\hat{\sigma}{(x)}}$). We will proceed with this notation for the sake of generality, but the reader should understand that $u$ can be replaced with any function.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Other 1-D Uncertainty Estimates", "weight": 1.0} -->

Now that we have our heuristic notion of uncertainty in hand, we can define a score function,

<!-- chunk {"id": "body-0054", "role": "body", "section": "Other 1-D Uncertainty Estimates", "weight": 1.0} -->

This score function has a natural interpretation: it is a multiplicative correction factor of the uncertainty scalar (i.e., ${s{(x,y)}u{(x)}} = \left| {y - {\hat{f}{(x)}}} \right|$). As before, taking $\hat{q}$ to be the $\frac{\lceil{{({1 - \alpha})}{({n + 1})}}\rceil}{n}$ quantile of the calibration scores guarantees us that for a new example,

<!-- chunk {"id": "body-0055", "role": "body", "section": "Other 1-D Uncertainty Estimates", "weight": 1.0} -->

Naturally, we can then form prediction sets using the rule

<!-- chunk {"id": "body-0056", "role": "body", "section": "Other 1-D Uncertainty Estimates", "weight": 1.0} -->

## model(X)=E(Y|X), and model(X)=stddev(Y|X)
scores = abs(model(calib_X)-calib_Y)/model(calib_X)
## Get the score quantile
qhat = torch.quantile(scores,np.ceil((n+1)*(1-alpha))/n)
## Deploy (represent sets as tuple of lower and upper endpoints)
muhat, stdhat = (model(test_X), model(test_X))
prediction_sets = (muhat-stdhat*qhat, muhat+stdhat*qhat)
Figure 7: Python code for conformalized uncertainty scalars.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Other 1-D Uncertainty Estimates", "weight": 1.0} -->

Let's reflect a bit on the nature of these prediction sets. The prediction sets are valid, as we desired. Due to our construction, they are also symmetric about the prediction, $\hat{f}{(x)}$, although symmetry could be relaxed with minor modifications. However, uncertainty scalars do not necessarily scale properly with $\alpha$. In other words, there is no reason to believe that a quantity like $\hat{\sigma}$ would be directly related to quantiles of the label distribution. We tend to prefer quantile regression when possible, since it directly estimates this quantity and thus should be a better heuristic (and in practice it usually is; see \[angelopoulos2022image\] for some evaluations). Nonetheless, uncertainty scalars remain in use because they are easy to deploy and have been commoditized in popular machine learning libraries. See Figure 7 for a Python implementation of this method.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conformalizing Bayes", "weight": 1.0} -->

Our final example of conformal prediction will use a Bayesian model. Bayesian predictors, like Bayesian neural networks, are commonly studied in the field of uncertainty quantification, but rely on many unverifiable and/or incorrect assumptions to provide coverage. Nonetheless, we should incorporate any prior information we have into our prediction sets. We will now show how to create valid prediction sets that are also Bayes optimal among all prediction sets that achieve $1 - \alpha$ coverage. These prediction sets use the posterior predictive density as a conformal score. The Bayes optimality of this procedure was first proven in \[hoff2021bayes\], and was previously studied in \[wasserman2011frasian, melluish2001comparing\]. Because our algorithm reduces to picking the labels with high posterior predictive density, the Python code will look exactly the same as in Figure 2. The only difference is interpretation, since the softmax now represents an approximation of a continuous distribution rather than a categorical one.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conformalizing Bayes", "weight": 1.0} -->

Let us first describe what a Bayesian would do, given a Bayesian model $\hat{f}{({y \mid x})}$, which estimates the value of the posterior distribution of $Y_{test}$ at label $y$ with input $X_{test} = x$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Conformalizing Bayes", "weight": 1.0} -->

However, because we cannot make assumptions on the model and data, we can only consider $\hat{f}{({y \mid x})}$ to be a heuristic notion of uncertainty.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Conformalizing Bayes", "weight": 1.0} -->

Following our now-familiar checklist, we can define a conformal score,

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conformalizing Bayes", "weight": 1.0} -->

which is high when the model is uncertain and otherwise low.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Conformalizing Bayes", "weight": 1.0} -->

This set is valid because we chose the threshold $\hat{q}$ via conformal prediction. Furthermore, when certain technical assumptions are satisfied, it has the best Bayes risk among all prediction sets with $1 - \alpha$ coverage. To be more precise, under the assumptions in \[hoff2021bayes\], $\mathcal{C}{(X_{test})}$ has the smallest average size of any conformal procedure with $1 - \alpha$ coverage, where the average is taken over the data *and* the parameters. This result should not be a surprise to those familiar with decision theory, as the argument we are making feels similar to that of the Neyman-Pearson lemma. This concludes the final example.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Discussion", "weight": 1.5} -->

As our examples have shown, conformal prediction is a simple and pragmatic technique with many use cases. It is also easy to implement and computationally trivial. Additionally, the above four examples serve as roadmaps to the user for designing score functions with various notions of optimality, including average size, adaptivity, and Bayes risk. Still more is yet to come---conformal prediction can be applied more broadly than it may first seem at this point. We will outline extensions of conformal prediction to other prediction tasks such as outlier detection, image segmentation, serial time-series prediction, and so on in Section 4. Before addressing these extensions, we will take a deep dive into diagnostics for conformal prediction in the standard setting, including the important topic of conditional coverage.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Evaluating Conformal Prediction", "weight": 1.0} -->

We have spent the last two sections learning how to form valid prediction sets satisfying rigorous statistical guarantees. Now we will discuss how to evaluate them. Our evaluations will fall into one of two categories.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Evaluating Conformal Prediction", "weight": 1.0} -->

Evaluating adaptivity. It is extremely important to keep in mind that the conformal prediction procedure with the smallest average set size is not necessarily the best. A good conformal prediction procedure will give small sets on easy inputs and large sets on hard inputs in a way that faithfully reflects the model's uncertainty. This *adaptivity* is not implied by conformal prediction's coverage guarantee, but it is non-negotiable in practical deployments of conformal prediction. We will formalize adaptivity, explore its consequences, and suggest practical algorithms for evaluating it.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Evaluating Conformal Prediction", "weight": 1.0} -->

Correctness checks. Correctness checks help you test whether you've implemented conformal prediction correctly. We will empirically check that the coverage satisfies Theorem 1. ‣ 1.1 Instructions for Conformal Prediction ‣ 1 Conformal Prediction ‣ A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification"). Rigorously evaluating whether this property holds requires a careful accounting of the finite-sample variability present with real datasets. We develop explicit formulae for the size of the benign fluctuations---if one observes deviations from $1 - \alpha$ in coverage that are larger than these formulae dictate, then there is a problem with the implementation.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Evaluating Conformal Prediction", "weight": 1.0} -->

Many of the evaluations we suggest are computationally intensive, and require running the entire conformal procedure on different splits of data at least $100$ times. Naïve implementations of these evaluations can be slow when the score takes a long time to compute. With some simple computational tricks and strategic caching, we can speed this process up by orders of magnitude. Therefore to aid the reader, we intersperse the mathematical descriptions with code to efficiently implement these computations.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Evaluating Adaptivity", "weight": 1.0} -->

Although any conformal procedure yields prediction intervals that satisfy, there are many such procedures, and they differ in other important ways. In particular, a key design consideration for conformal prediction is *adaptivity*: we want the procedure to return larger sets for harder inputs and smaller sets for easier inputs. While most reasonable conformal procedures will satisfy this to some extent, we now discuss precise metrics for adaptivity that allow the user to check a conformal procedure and to compare multiple alternative conformal procedures.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Set size", "weight": 1.0} -->

The first step is to plot histograms of set sizes. This histogram helps us in two ways. Firstly, a large average set size indicates the conformal procedure is not very precise, indicating a possible problem with the score or underlying model. Secondly, the spread of the set sizes shows whether the prediction sets properly adapt to the difficulty of examples. A wider spread is generally desirable, since it means that the procedure is effectively distinguishing between easy and hard inputs.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Set size", "weight": 1.0} -->

It can be tempting to stop evaluations after plotting the coverage and set size, but certain important questions remain unanswered. A good spread of set sizes is generally better, but it does not necessarily indicate that the sets adapt properly to the difficulty of $X$. Above seeing that the set sizes have dynamic range, we will need to verify that large sets occur for hard examples. We next formalize this notion and give metrics for evaluating it.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Conditional coverage", "weight": 1.0} -->

That is, for every value of the input $X_{test}$, we seek to return prediction sets with $1 - \alpha$ coverage. This is a stronger property than the *marginal coverage* property in that conformal prediction is guaranteed to achieve---indeed, in the most general case, conditional coverage is impossible to achieve \[vovk2012conditional\]. In other words, conformal procedures are not guaranteed to satisfy, so we must check how close our procedure comes to approximating it.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Conditional coverage", "weight": 1.0} -->

The difference between marginal and conditional coverage is subtle but of great practical importance, so we will spend some time think about the differences here. Imagine there are two groups of people, group A and group B, with frequencies 90% and 10%. The prediction sets always cover $Y$ among people in group A and never cover $Y$ when the person comes from group B. Then the prediction sets have 90% coverage, but not conditional coverage. Conditional coverage would imply that the prediction sets cover $Y$ at least 90% of the time in both groups. This is necessary, but not sufficient; conditional coverage is a very strong property that states the probability of the prediction set needs to be $\geq {90\%}$ *for a particular person*. In other words, for any subset of the population, the coverage should be $\geq {90\%}$. See Figure 10 for a visualization of the difference between conditional and marginal coverage.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Feature-stratified coverage metric", "weight": 1.0} -->

As a first metric for conditional coverage, we will formalize the example we gave earlier, where coverage is unequal over some groups. The reader can think of these groups as discrete categories, like race, or as a discretization of continuous features, like age ranges. Formally, suppose we have features $X_{i,1}^{({val})}$ that take values in $\{ 1,\ldots,G\}$ for some $G$. (Here, $i = {1,\ldots,n_{val}}$ indexes the example in the validation set, and the first coordinate of each feature is the group.) Let $\mathcal{I}_{g} \subset {\{ 1,\ldots,n_{val}\}}$ be the set of observations such that $X_{i,1}^{({val})} = g$ for $g = {1,\ldots,G}$.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Feature-stratified coverage metric", "weight": 1.0} -->

In words, this is the observed coverage among all instances where the discrete feature takes the value $g$. If conditional coverage were achieved, this would be $1 - \alpha$, and values farther below $1 - \alpha$ indicate a greater violation of conditional coverage. Note that this metric can also be used with a continuous feature by binning the features into a finite number of categories.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Size-stratified coverage metric", "weight": 1.0} -->

We next consider a more general-purpose metric for how close a conformal procedure comes to satisfying, introduced in \[angelopoulos2020sets\]. First, we discretize the possible cardinalities of $\mathcal{C}{(x)}$, into $G$ bins, $B_{1},\ldots,B_{G}$. For example, in classification we might divide the observations into three groups, depending on whether $\mathcal{C}{(x)}$ has one element, two elements, or more than two elements. Let $\mathcal{I}_{g} \subset {\{ 1,\ldots,n_{val}\}}$ be the set of observations falling in bin $g$ for $g = {1,\ldots,G}$. Then we consider the following

<!-- chunk {"id": "body-0077", "role": "body", "section": "Size-stratified coverage metric", "weight": 1.0} -->

In words, this is the observed coverage for all units for which the set size $|{\mathcal{C}{(x)}}|$ falls into bin $g$. As before, if conditional coverage were achieved, this would be $1 - \alpha$, and values farther below $1 - \alpha$ indicate a greater violation of conditional coverage. Note that this is the same expression as for the FSC metric, except that the definition of $\mathcal{I}_{g}$ has changed. Unlike the FSC metric, the user does not have to define an important set of discrete features a-priori---it is a general metric that can apply to any example.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Size-stratified coverage metric", "weight": 1.0} -->

See \[cauchois2020knowing\] and \[feldman2021improving\] for additional metrics of conditional coverage.

<!-- chunk {"id": "body-0079", "role": "body", "section": "The Effect of the Size of the Calibration Set", "weight": 1.0} -->

We first pause to discuss how the size of the calibration set affects conformal prediction. We consider this question for two reasons. First, the user must choose this for a practical deployment. Roughly speaking, our conclusion will that be choosing a calibration set of size $n = 1000$ is sufficient for most purposes. Second, the size of the calibration set is one source of finite-sample variability that we will need to analyze to correctly check the coverage. We will build on the results here in the next section, where we give a complete description of how to check coverage in practice.

<!-- chunk {"id": "body-0080", "role": "body", "section": "The Effect of the Size of the Calibration Set", "weight": 1.0} -->

How does the size of the calibration set, $n$, affect conformal prediction? The coverage guarantee in holds for any $n$, so we can see that our prediction sets have coverage at least $1 - \alpha$ even with a very small calibration set. Intuitively, however, it may seem that larger $n$ is better, and leads to more stable procedures. This intuition is correct, and it explains why using a larger calibration set is beneficial in practice. The details are subtle, so we carefully work through them here.

<!-- chunk {"id": "body-0081", "role": "body", "section": "The Effect of the Size of the Calibration Set", "weight": 1.0} -->

The key idea is that *the coverage of conformal prediction conditionally on the calibration set is a random quantity*. That is, if we run the conformal prediction algorithm twice, each time sampling a new calibration dataset, then check the coverage on an infinite number of validation points, those two numbers will not be equal. The coverage property in says that coverage will be at least $1 - \alpha$ on average over the randomness in the calibration set, but with any one fixed calibration set, the coverage on an infinite validation set will be some number that is not exactly $1 - \alpha$. Nonetheless, we can choose $n$ large enough to control these fluctuations in coverage by analyzing its distribution.

<!-- chunk {"id": "body-0082", "role": "body", "section": "The Effect of the Size of the Calibration Set", "weight": 1.0} -->

In particular, the distribution of coverage has an analytic form, first introduced by Vladimir Vovk in \[vovk2012conditional\], namely,

<!-- chunk {"id": "body-0083", "role": "body", "section": "The Effect of the Size of the Calibration Set", "weight": 1.0} -->

Notice that the conditional expectation above is the coverage with an infinite validation data set, holding the calibration data fixed. A simple proof of this fact is available in \[vovk2012conditional\]. We plot the distribution of coverage for several values of $n$ in Figure 11.

<!-- chunk {"id": "body-0084", "role": "body", "section": "The Effect of the Size of the Calibration Set", "weight": 1.0} -->

Inspecting Figure 11, we see that choosing $n = 1000$ calibration points leads to coverage that is typically between $.88$ and $.92$, hence our rough guideline of choosing about $1000$ calibration points. More formally, we can compute exactly the number of calibration points $n$ needed to achieve a coverage of ${1 - \alpha} \pm \epsilon$ with probability $1 - \delta$. Again, the average coverage is always at least $1 - \alpha$; the parameter $\delta$ controls the tail probabilities of the coverage conditionally on the calibration data. For any $\delta$, the required calibration set size $n$ can be explicitly computed from a simple expression, and we report on several values in Table 1 for the reader's reference. Code allowing the user to produce results for any choice of $n$ and $\alpha$ accompanies the table.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Checking for Correct Coverage", "weight": 1.0} -->

As an obvious diagnostic, the user will want to assess whether the conformal procedure has the correct coverage. This can be accomplished by running the procedure over $R$ trials with new calibration and validation sets, and then calculating the empirical coverage for each,

<!-- chunk {"id": "body-0086", "role": "body", "section": "Checking for Correct Coverage", "weight": 1.0} -->

where $n_{\text{val}}$ is the size of the validation set, $(X_{i,j}^{(\text{val})},Y_{i,j}^{(\text{val})})$ is the $i$th validation example in trial $j$, and $\mathcal{C}_{j}$ is calibrated using the calibration data from the $j$th trial. A histogram of the $C_{j}$ should be centered at roughly $1 - \alpha$, as in Figure 11. Likewise, the mean value,

<!-- chunk {"id": "body-0087", "role": "body", "section": "Checking for Correct Coverage", "weight": 1.0} -->

With real datasets, we only have $n + n_{\text{val}}$ data points total to evaluate our conformal algorithm and therefore cannot draw new data for each of the $R$ rounds. So, we compute the coverage values by randomly splitting the $n + n_{\text{val}}$ data points $R$ times into calibration and validation datasets, then running conformal. Notice that rather than splitting the data points themselves many times, we can instead first cache all conformal scores and then compute the coverage values over many random splits, as in the code sample in Figure 12.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Checking for Correct Coverage", "weight": 1.0} -->

try: # try loading the scores first
scores = np.load(’scores.npy’)
## and Y have n + n_val rows each
scores = get_scores(X,Y)
np.save(scores, ’scores.npy’)
## calculate the coverage R times and store in list
np.random.shuffle(scores) # shuffle
calib_scores, val_scores = (scores[:n],scores[n:]) # split
qhat = np.quantile(calib_scores, np.ceil((n+1)*(1-alpha)/n), method=’higher’) # calibrate
coverages[r] = (val_scores &lt;= qhat).astype(float).mean # see caption
average_coverage = coverages.mean # should be close to 1-alpha
plt.hist(coverages) # should be roughly centered at 1-alpha
Figure 12: Python code for computing coverage with efficient score caching.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Checking for Correct Coverage", "weight": 1.0} -->

Notice that from the expression for conformal sets, a validation point is covered if and only if s (X,Y) ≤ q̂, which is how the third to last line is succinctly computing the coverage.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Checking for Correct Coverage", "weight": 1.0} -->

If properly implemented, conformal prediction is guaranteed to satisfy the inequality. However, if the reader sees minor fluctuations in the observed coverage, they may not need to worry: the finiteness of $n$, $n_{\text{val}}$, and $R$ can lead to benign fluctuations in coverage which add some width to the Beta distribution in Figure 11. Appendix LABEL:app:empirical-coverage gives exact theory for analyzing the mean and standard deviation of $\overline{C}$. From this, we will be able to tell if any deviation from $1 - \alpha$ indicates a problem with the implementation, or if it is benign. Code for checking the coverage at all different values of $n$, $n_{\text{val}}$, and $R$ is available in the accompanying Jupyter notebook of Figure 12.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Extensions of Conformal Prediction", "weight": 1.0} -->

At this point, we have seen the core of the matter: how to construct prediction sets with coverage in any standard supervised prediction problem. We now broaden our horizons towards prediction tasks with different structure, such as side information, covariate shift, and so. These more exotic problems arise quite frequently in the real world, so we present practical conformal algorithms to address them.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Group-Balanced Conformal Prediction", "weight": 1.0} -->

In certain settings, we might want prediction intervals that have equal error rates across certain subsets of the data. For example, we may require our medical classifier to have coverage that is correct for all racial and ethnic groups. To formalize this, we suppose that the first feature of our inputs, $X_{i,1}$, $i = {1,\ldots,n}$ takes values in some discrete set $\{ 1,\ldots,G\}$ corresponding to categorical groups.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Group-Balanced Conformal Prediction", "weight": 1.0} -->

for all groups $g \in {\{ 1,\ldots,G\}}$. In words, this means we have a $1 - \alpha$ coverage rate for all groups. Notice that the group output could be a post-processing of the original features in the data. For example, we might bin the values of $X_{test}$ into a discrete set.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Group-Balanced Conformal Prediction", "weight": 1.0} -->

Recall that a standard application of conformal prediction will not necessarily yield coverage within each group simultaneously---that is, may not be satisfied. We saw an example in Figure 10; the marginal guarantee from normal conformal prediction can still be satisfied even if all errors happen in one group.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Group-Balanced Conformal Prediction", "weight": 1.0} -->

In order to achieve group-balanced coverage, we will simply run conformal prediction seperately for each group, as visualized below.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Group-Balanced Conformal Prediction", "weight": 1.0} -->

Making this formal, given a conformal score function $s$, we stratify the scores on the calibration set by group,

<!-- chunk {"id": "body-0097", "role": "body", "section": "Group-Balanced Conformal Prediction", "weight": 1.0} -->

Then, within each group, we calculate the conformal quantile

<!-- chunk {"id": "body-0098", "role": "body", "section": "Group-Balanced Conformal Prediction", "weight": 1.0} -->

Finally, we form prediction sets by first picking the relevant quantile,

<!-- chunk {"id": "body-0099", "role": "body", "section": "Group-Balanced Conformal Prediction", "weight": 1.0} -->

That is, for a point $x$ that we see falls in group $x_{1}$, we use the threshold ${\hat{q}}^{(x_{1})}$ to form the prediction set, and so. This choice of $\mathcal{C}$ satisfies, as was first documented by Vovk in \[vovk2012conditional\].

<!-- chunk {"id": "body-0100", "role": "body", "section": "Class-Conditional Conformal Prediction", "weight": 1.0} -->

In classification problems, we might similarly ask for coverage on *every* ground truth class. For example, if we had a medical classifier assigning inputs to class normal or class cancer, we might ask that the prediction sets are 95% accurate both when the ground truth is class cancer and also when the ground truth is class normal. Formally, we return to the classification setting, where $\mathcal{Y} = {\{ 1,\ldots,K\}}$. We seek to achieve *class-balanced* coverage,

<!-- chunk {"id": "body-0101", "role": "body", "section": "Class-Conditional Conformal Prediction", "weight": 1.0} -->

To achieve class-balanced coverage, we will calibrate within each class separately. The algorithm will be similar to the group-balanced coverage of Section 4.1, but we must modify it because we do not know the correct class at test time. (In contrast, in Section 4.1, we observed the group information $X_{{test},1}$ as an input feature.) See the visualization below.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Class-Conditional Conformal Prediction", "weight": 1.0} -->

Turning to the algorithm, given a conformal score function $s$, stratify the scores on the calibration set by class,

<!-- chunk {"id": "body-0103", "role": "body", "section": "Class-Conditional Conformal Prediction", "weight": 1.0} -->

Then, within each class, we calculate the conformal quantile,

<!-- chunk {"id": "body-0104", "role": "body", "section": "Class-Conditional Conformal Prediction", "weight": 1.0} -->

Notice that in the preceding display, we take a provisional value of the response, $y$, and then use the conformal threshold ${\hat{q}}^{(y)}$ to determine if it is included in the prediction set. This choice of $\mathcal{C}$ satisfies, as proven by Vovk in \[vovk2012conditional\]; another version can be found in \[Sadinle2016LeastAS\].

<!-- chunk {"id": "body-0105", "role": "body", "section": "Conformal Risk Control", "weight": 1.0} -->

So far, we have used conformal prediction to construct prediction sets that bound the *miscoverage*,

<!-- chunk {"id": "body-0106", "role": "body", "section": "Conformal Risk Control", "weight": 1.0} -->

However, for many machine learning problems, the natural notion of error is not miscoverage. Here we show that conformal prediction can also provide guarantees of the form

<!-- chunk {"id": "body-0107", "role": "body", "section": "Conformal Risk Control", "weight": 1.0} -->

for any bounded *loss function* $\ell$ that shrinks as $\mathcal{C}$ grows. This is called a *conformal risk control* guarantee. Note that recovers when using the miscoverage loss, ${\ell\left( {C{(X_{test})}},Y_{test} \right)} = {\mathbb{1}\left\{ {Y_{test} \notin {C{(X_{test})}}} \right\}}$. However, this algorithm also extends conformal prediction to situations where other loss functions, such as the false negative rate (FNR), are more appropriate.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Conformal Risk Control", "weight": 1.0} -->

As an example, consider multilabel classification. Here, the response $Y_{i} \subseteq {\{ 1,\ldots,K\}}$ a subset of $K$ classes. Given a trained model $f:{\mathcal{X}\rightarrow{\lbrack 0,1\rbrack}^{K}}$, we wish to output sets that include a large fraction of the true classes in $Y_{i}$. To that end, we post-process the model's raw outputs into the set of classes with sufficiently high scores, ${\mathcal{C}_{\lambda}{(x)}} = {\{ k:{{f{(X)}_{k}} \geq {1 - \lambda}}\}}$. Note that as the threshold $\lambda$ grows, we include more classes in $\mathcal{C}_{\lambda}{(x)}$---it becomes more conservative in that we are less likely to omit true classes.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Conformal Risk Control", "weight": 1.0} -->

Conformal risk control can be used to find a threshold value $\hat{\lambda}$ that controls the fraction of missed classes. That is, $\hat{\lambda}$ can be chosen so that the expected value of ${\ell\left( {\mathcal{C}_{\hat{\lambda}}{(X_{test})}},Y_{test} \right)} = {1 - {{|{Y_{test} \cap {\mathcal{C}_{\lambda}{(X_{test})}}}|}/{|Y_{test}|}}}$ is guaranteed to fall below a user-specified error rate $\alpha$. For example, setting $\alpha = 0.1$ ensures that $\mathcal{C}_{\hat{\lambda}}{(X_{test})}$ contains $90\%$ of the true classes in $Y_{test}$ on average. We will work through a multilabel classification example in detail in Section 5.1.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Conformal Risk Control", "weight": 1.0} -->

Formally, we will consider post-processing the predictions of the model $f$ to create a prediction set $\mathcal{C}_{\lambda}{( \cdot )}$. The prediction set has a parameter $\lambda$ that encodes its level of conservativeness: larger $\lambda$ values yield more conservative outputs (e.g., larger prediction sets). To measure the quality of the output of $\mathcal{C}_{\lambda}$, we consider a loss function ${\ell{({\mathcal{C}_{\lambda}{(x)}},y)}} \in {({- \infty},B\rbrack}$ for some $B < \infty$. We require the loss function to be non-increasing as a function of $\lambda$.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Conformal Risk Control", "weight": 1.0} -->

where ${\hat{R}{(\lambda)}} = {\left( {{\ell\left( {\mathcal{C}_{\lambda}{(X_{1})}},Y_{1} \right)} + \ldots + {\ell\left( {\mathcal{C}_{\lambda}{(X_{n})}},Y_{n} \right)}} \right)/n}$ is the empirical risk on the calibration data. Note that this algorithm simply corresponds to tuning based on the empirical risk at a slightly more conservative level than $\alpha$. For example, if $B = 1$, $\alpha = 0.1$, and we have $n = 1000$ calibration points, then we select $\hat{\lambda}$ to be the value where empirical risk hits level $\hat{\lambda} = 0.0991$ instead of $0.1$.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Outlier Detection", "weight": 1.0} -->

Conformal prediction can also be adapted to handle unsupervised outlier detection. Here, we have access to a clean dataset $X_{1},\ldots,X_{n}$ and wish to detect when test points do not come from the same distribution. As before, we begin with a heuristic model that tries to identify outliers; a larger score means that the model judges the point more likely to be an outlier. We will then use a variant of conformal prediction to calibrate it to have statistical guarantees. In particular, we will guarantee that it does not return too many false positives.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Outlier Detection", "weight": 1.0} -->

Formally, we will construct a function that labels test points as outliers or inliers, $\mathcal{C}:{\mathcal{X}\rightarrow{\{\text{outlier},\text{inlier}\}}}$, such that

<!-- chunk {"id": "body-0114", "role": "body", "section": "Outlier Detection", "weight": 1.0} -->

where the probability is over $X_{test}$, a fresh sample from the clean-data distribution. The algorithm for achieving is similar to the usual conformal algorithm. We start with a conformal score $s:{\mathcal{X}\rightarrow{\mathbb{R}}}$ (note that since we are in the unsupervised setting, the score only depends on the features). Next, we compute the conformal score on the clean data: $s_{i} = {s{(X_{i})}}$ for $i = {1,\ldots,n}$.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Outlier Detection", "weight": 1.0} -->

This construction guarantees error control, as we record next.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Conformal Prediction Under Covariate Shift", "weight": 1.0} -->

All previous conformal methods rely on Theorem 1. ‣ 1.1 Instructions for Conformal Prediction ‣ 1 Conformal Prediction ‣ A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification"), which assumes that the incoming test points come from the same distribution as the calibration points. However, past data is not necessarily representative of future data in practice.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Conformal Prediction Under Covariate Shift", "weight": 1.0} -->

One type of distribution shift that conformal prediction can handle is *covariate shift*. Covariate shift refers to the situation where the distribution of $X_{test}$ changes from $\mathcal{P}$ to $\mathcal{P}_{test}$, but the relationship between $X_{test}$ and $Y_{test}$, i.e. the distribution of $\left. Y_{test} \middle| X_{test} \right.$, stays fixed.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Conformal Prediction Under Covariate Shift", "weight": 1.0} -->

Imagine our calibration features ${\{ X_{i}\}}_{i = 1}^{n}$ are drawn independently from $\mathcal{P}$ but our test feature $X_{test}$ is drawn from $\mathcal{P}_{test}$. Then, there has been a covariate shift, and the data are no longer i.i.d. This problem is common in the real world. For example,

<!-- chunk {"id": "body-0119", "role": "body", "section": "Conformal Prediction Under Covariate Shift", "weight": 1.0} -->

You are trying to predict diseases from MRI scans. You conformalized on a balanced dataset of 50% infants and 50% adults, but in reality, the frequency is 5% infants and 95% adults. Deploying the model in the real world would invalidate coverage; the infants are over-represented in our sample, so diseases present during infancy will be over-predicted. This was a covariate shift in age.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Conformal Prediction Under Covariate Shift", "weight": 1.0} -->

You are trying to do instance segmentation, i.e., to segment each object in an image from the background. You collected your calibration images in the morning but seek to deploy your system in the afternoon. The amount of sunlight has changed, and more people are eating lunch. This was a covariate shift in the time of day.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Conformal Prediction Under Covariate Shift", "weight": 1.0} -->

To address the covariate shift from $\mathcal{P}$ to $\mathcal{P}_{test}$, one can form valid prediction sets with *weighted conformal prediction*, first developed in \[tibshirani2019conformal\].

<!-- chunk {"id": "body-0122", "role": "body", "section": "Conformal Prediction Under Covariate Shift", "weight": 1.0} -->

In weighted conformal prediction, we account for covariate shift by upweighting conformal scores from calibration points that would be more likely under the new distribution. We will be using the *likelihood ratio*

<!-- chunk {"id": "body-0123", "role": "body", "section": "Conformal Prediction Under Covariate Shift", "weight": 1.0} -->

usually this is just the ratio of the new PDF to the old PDF at the point $x$. Now we define our weights,

<!-- chunk {"id": "body-0124", "role": "body", "section": "Conformal Prediction Under Covariate Shift", "weight": 1.0} -->

Intuitively, the weight $p_{i}^{w}{(x)}$ is large when $X_{i}$ is likely under the new distribution, and $p_{test}^{w}{(x)}$ is large when the input $x$ is likely under the new distribution. We can then express our conformal quantile as the $1 - \alpha$ quantile of a reweighted distribution,

<!-- chunk {"id": "body-0125", "role": "body", "section": "Conformal Prediction Under Covariate Shift", "weight": 1.0} -->

where above for notational convenience we assume that the scores are ordered from smallest to largest a-priori. The choice of quantile is the key step in this algorithm, so we pause to parse it. First of all, notice that the quantile is now a function of an input $x$, although the dependence is only minor. Choosing ${p_{i}^{w}{(x)}} = {p_{test}^{w}{(x)}} = \frac{1}{n + 1}$ gives the familiar case of conformal prediction---all points are equally weighted, so we end up choosing the $\left\lceil {{({n + 1})}{({1 - \alpha})}} \right\rceil$th-smallest score as our quantile. When there is covariate shift, we instead re-weight the calibration points with non-equal weights to match the test distribution. If the covariate shift makes easier values of $x$ more likely, it makes our quantile smaller.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Conformal Prediction Under Covariate Shift", "weight": 1.0} -->

This happens because the covariate shift puts more weight on small scores---see the diagram below. Of course, the opposite holds the covariate shift upweights difficult values of $x$: so the covariate-shift-adjusted quantile grows.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Conformal Prediction Under Covariate Shift", "weight": 1.0} -->

With this quantile function in hand, we form our prediction set in the standard way,

<!-- chunk {"id": "body-0128", "role": "body", "section": "Conformal Prediction Under Covariate Shift", "weight": 1.0} -->

By accounting for the covariate shift in our choice of $\hat{q}$, we were able to make our calibration data look exchangeable with the test point, achieving the following guarantee.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Conformal Prediction Under Distribution Drift", "weight": 1.0} -->

Another common form of distribution shift is *distribution drift*: slowly varying changes in the data distribution. For example, when collecting time-series data, the data distribution may change---furthermore, it may change in a way that is unknown or difficult to estimate. Here, one can imagine using weights that give more weight to recent conformal scores. The following theory provides some justification for such *weighted conformal* procedures; in particular, they always satisfy marginal coverage, and are exact when the magnitude of the distribution shift is known.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Conformal Prediction Under Distribution Drift", "weight": 1.0} -->

Then we can construct prediction sets in the usual way,

<!-- chunk {"id": "body-0131", "role": "body", "section": "Conformal Prediction Under Distribution Drift", "weight": 1.0} -->

We now state a theorem showing that when the distribution is shifting, it is a good idea to apply a discount factor to old samples. In particular, let $\epsilon_{i} = {d_{TV}\left( {(X_{i},Y_{i})},{(X_{test},Y_{test})} \right)}$ be the TV distance between the $i$th data point and the test data point. The TV distance is a measure of how much the distribution has shifted---a large $\epsilon_{i}$ (close to $1$) means the $i$th data point is not representative of the new test point. The result states that if $w$ discounts those points with large shifts, the coverage remains close to $1 - \alpha$.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Worked Examples", "weight": 1.0} -->

We now show several worked examples of the techniques described in Section 4. For each example, we provide Jupyter notebooks that allow the results to be conveniently replicated and extended.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Multilabel Classification", "weight": 1.0} -->

In the multilabel classification setting, we receive an image and predict which of $K$ objects are in an image. We have a pretrained model $\hat{f}$ that outputs estimated probabilities for each of the $K$ classes. We wish to report on the possible classes contained in the image, returning most of the true labels. To this end, we will threshold the model's outputs to get the subset of $K$ classes that the model thinks is most likely, ${\mathcal{C}_{\lambda}{(x)}} = {\{ y:{{\hat{f}{(x)}} \geq \lambda}\}}$, which we call the prediction. We will use conformal risk control (Section 4.3) to pick the threshold value $\lambda$ certifying a low *false negative rate* (FNR), i.e., to guarantee the average fraction of ground truth classes that the model missed is less than $\alpha$.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Tumor Segmentation", "weight": 1.0} -->

In the tumor segmentation setting, we receive an $M \times N \times 3$ image of a tumor and predict an $M \times N$ binary mask, where '1' indicates a tumor pixel. We start with a pretrained segmentation model $\hat{f}$ that outputs an $M \times N$ grid of the estimated probabilities that each pixel is a tumor pixel. We will threshold the model's outputs to get our predicted binary mask, ${\mathcal{C}_{\lambda}{(x)}} = {\{{(i,j)}:{{\hat{f}{(x)}_{(i,j)}} \geq \lambda}\}}$, which we call the prediction. We will use conformal risk control (Section 4.3) to pick the threshold value $\lambda$ certifying a low FNR, i.e., guaranteeing the average fraction of tumor pixels missed is less than $\alpha$.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Tumor Segmentation", "weight": 1.0} -->

More formally, our calibration set ${\{{(X_{i},Y_{i})}\}}_{i = 1}^{n}$ contains exchangeable images $X_{i}$ and sets of tumor pixels $Y_{i} \subseteq {{\{ 1,\ldots,M\}} \times {\{ 1,\ldots,N\}}}$. As in the previous example, we let the loss be the false negative proportion, $\ell_{FNR}$. Then, picking $\hat{\lambda}$ as in 29 yields the bound on the FNR in 44. Figure 14 gives results and code on a dataset of gut polyps.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Weather Prediction with Time-Series Distribution Shift", "weight": 1.0} -->

In this example we seek to predict the temperature of different locations on Earth given covariates such as the latitude, longitude, altitude, atmospheric pressure, and so. We will make these predictions serially in time. Dependencies between adjacent data points induced by local and global weather changes violate the standard exchangeability assumption, so we will need to apply the method from Section 4.6.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Weather Prediction with Time-Series Distribution Shift", "weight": 1.0} -->

In this setting, we have a time series $\left\{ {(X_{t},Y_{t})} \right\}_{t = 1}^{T}$, where the $X_{t}$ are tabular covariates and the $Y_{t} \in {\mathbb{R}}$ are temperatures in degrees Celsius. Note that these data points are not exchangeable or i.i.d.; adjacent data points will be correlated. We start with a pretrained model $\hat{f}$ taking features and predicting temperature and an uncertainty model $\hat{u}$ takes features and outputs a scalar notion of uncertainty. Following Section 2.3, we compute the conformal scores

<!-- chunk {"id": "body-0138", "role": "body", "section": "Weather Prediction with Time-Series Distribution Shift", "weight": 1.0} -->

Since we observe the data points sequentially, we also observe the scores sequentially, and we will need to pick a different conformal quantile for each incoming data point. More formally, consider the task of predicting the temperature at time $t \leq T$. We use the weighted conformal technique in Section 5.3 with the fixed $K$-sized window $w_{t^{\prime}} = {\mathbb{1}\left\{ {t^{\prime} \geq {t - K}} \right\}}$ for all $t^{\prime} < t$. This yields the quantiles

<!-- chunk {"id": "body-0139", "role": "body", "section": "Weather Prediction with Time-Series Distribution Shift", "weight": 1.0} -->

With these adjusted quantiles in hand, we form prediction sets at each time step in the usual way,

<!-- chunk {"id": "body-0140", "role": "body", "section": "Weather Prediction with Time-Series Distribution Shift", "weight": 1.0} -->

We run this procedure on the Yandex Weather Prediction dataset. This dataset is part of the Shifts Project \[malinin2021shifts\], which also provides an ensemble of 10 pretrained CatBoost \[dorogush2018catboost\] models for making the temperature predictions. We take the average prediction of these models as our base model $\hat{f}$. Each of the models has its own internal variance; we take the average of these variances as our uncertainty scalar $\hat{u}$. The dataset includes an in-distribution split of fresh data from the same time frame that the base model was trained and an out-of-distribution split consisting of time windows the model has never seen. We concatenate these datasets in time, leading to a large change point in the score distribution. Results in Figure 15 show that the weighted method works better than a naive unweighted conformal baseline, achieving the desired coverage in steady-state and recovering quickly from the change point. There is no hope of measuring the TV distance between adjacent data points in order to apply Theorem 4.

<!-- chunk {"id": "body-0141", "role": "body", "section": "Weather Prediction with Time-Series Distribution Shift", "weight": 1.0} -->

‣ 4.6 Conformal Prediction Under Distribution Drift ‣ 4 Extensions of Conformal Prediction ‣ A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification"), so we cannot get a formal coverage bound. Nonetheless, the procedure is useful with this simple fixed window of weights, which we chose with only a heuristic understanding of the distribution drift speed. It is worth noting that conformal prediction for time-series applications is a particularly active area of research currently, and the method we have presented is not clearly the best. See \[gibbs2021adaptive, zaffran2022adaptive, gibbs2022conformal\] and \[xu2021conformal\] for two differing perspectives.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Toxic Online Comment Identification via Outlier Detection", "weight": 1.0} -->

We provide a type-1 error guarantee on a model that flags toxic online comments, such as threats, obscenity, insults, and identity-based hate. Suppose we are given $n$ non-toxic text samples $X_{1},\ldots,X_{n}$ and asked whether a new text sample $X_{test}$ is toxic. We also have a pre-trained toxicity prediction model ${\hat{f}{(x)}} \in {\lbrack 0,1\rbrack}$, where values closer to 1 indicate a higher level of toxicity. The goal is to flag as many toxic comments as possible while not flagging more than $\alpha$ proportion of non-toxic comments.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Toxic Online Comment Identification via Outlier Detection", "weight": 1.0} -->

The outlier detection procedure in Section 4.4 applies immediately. First, we run the model on each calibration point, yielding conformal scores $s_{i} = {\hat{f}{(X_{i})}}$. Taking the toxicity threshold $\hat{q}$ to be the $\lceil{{({n + 1})}{({1 - \alpha})}}\rceil$-smallest of the $s_{i}$, we construct the function

<!-- chunk {"id": "body-0144", "role": "body", "section": "Toxic Online Comment Identification via Outlier Detection", "weight": 1.0} -->

This gives the guarantee in Proposition 3. ‣ 4.4 Outlier Detection ‣ 4 Extensions of Conformal Prediction ‣ A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification")---no more than $\alpha$ fraction of future nontoxic text will be classified as toxic.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Selective Classification", "weight": 1.0} -->

In many situations, we only want to show a model's predictions when it is confident. For example, we may only want to make medical diagnoses when the model will be 95% accurate, and otherwise to say "I don't know." We next demonstrate a system that strategically abstains in order to achieve a higher accuracy than the base model in the problem of image classification.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Selective Classification", "weight": 1.0} -->

where ${\hat{Y}{(x)}} = {{\arg{\max_{y}\hat{f}}}{(x)}_{y}}$, ${\hat{P}{(X_{test})}} = {{\max_{y}\hat{f}}{(x)}_{y}}$, and $\hat{\lambda}$ is a threshold chosen using the calibration data. This is called a *selective accuracy* guarantee, because the accuracy is only computed over a subset of high-confidence predictions. This quantity cannot be controlled with techniques we've seen so far, since we are not guaranteed that model accuracy is monotone in the cutoff $\lambda$. Nonetheless, it can be handled with Learn then Test---a framework for controlling arbitrary risks (see Appendix LABEL:app:ltt). We show only the special case of controlling selective classification accuracy here.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Selective Classification", "weight": 1.0} -->

We pick the threshold using based on the empirical estimate of selective accuracy on the calibration set,

<!-- chunk {"id": "body-0148", "role": "body", "section": "Selective Classification", "weight": 1.0} -->

Since this function is not monotone in $\lambda$, we will choose $\hat{\lambda}$ differently than in Section 4.3. In particular, we will scan across values of $\lambda$ looking at a conservative upper bound for the true risk (i.e., the top end of a confidence interval for the selective misclassification rate). Realizing that $\hat{R}{(\lambda)}$ is a Binomial random variable with $n{(\lambda)}$ trials, we upper-bound the misclassification error as

<!-- chunk {"id": "body-0149", "role": "body", "section": "Selective Classification", "weight": 1.0} -->

for some user-specified failure rate $\delta \in {\lbrack 0,1\rbrack}$. Then, scan the upper bound until the last time the bound exceeds $\alpha$,

<!-- chunk {"id": "body-0150", "role": "body", "section": "Selective Classification", "weight": 1.0} -->

Deploying the threshold $\hat{\lambda}$ will satisfy with high probability.

<!-- chunk {"id": "body-0151", "role": "body", "section": "Full conformal prediction", "weight": 1.0} -->

Up to this point, we have only considered *split conformal prediction*, otherwise known as inductive conformal prediction. This version of conformal prediction is computationally attractive, since it only requires fitting the model one time, but it sacrifices statistical efficiency because it requires splitting the data into training and calibration datasets. Next, we consider *full conformal prediction*, or transductive conformal prediction, which avoids data splitting at the cost of many more model fits. Historically, full conformal prediction was developed first, and then split conformal prediction was later recognized as an important special case. Next, we describe full conformal prediction. This discussion is motivated from three points of view. First, full conformal prediction is an elegant, historically important idea in our field. Second, the exposition will reveal a complimentary interpretation of conformal prediction as a hypothesis test. Lastly, full conformal prediction is a useful algorithm when statistical efficiency is of paramount importance.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Full Conformal Prediction", "weight": 1.0} -->

This topic requires expanded notation. Let ${(X_{1},Y_{1})},\ldots,{(X_{n + 1},Y_{n + 1})}$ be $n + 1$ exchangeable data points. As before, the user sees ${(X_{1},Y_{1})},\ldots,{(X_{n},Y_{n})}$ and $X_{n + 1}$, and wishes to make a prediction set that contains $Y_{n + 1}$. But unlike split conformal prediction, we allow the model to train on all the data points, so there is no separate calibration dataset.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Full Conformal Prediction", "weight": 1.0} -->

The core idea of full conformal prediction is as follows. We know that the true label, $Y_{n + 1}$, lives somewhere in $\mathcal{Y}$ --- so if we loop over all possible $y \in \mathcal{Y}$, then we will eventually hit the data point $(X_{n + 1},Y_{n + 1})$, which is exchangeable with the first $n$ data points. Full conformal prediction is so-named because it directly computes this loop. For each $y \in \mathcal{Y}$, we fit a new model ${\hat{f}}^{y}$ to the augmented dataset ${(X_{1},Y_{1})},\ldots,{(X_{n + 1},y)}$. Importantly, the model fitting for $\hat{f}$ must be invariant to permutations of the data.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Full Conformal Prediction", "weight": 1.0} -->

Then, we compute a score function $s_{i}^{y} = {s{(X_{i},Y_{i},{\hat{f}}^{y})}}$ for i = 1,...,n and $s_{n + 1}^{y} = {s{(X_{n + 1},y,{\hat{f}}^{y})}}$. This score function is exactly the same as those from Section 2, except that the model ${\hat{f}}^{y}$ is now given as an argument because it is no longer fixed. Then, we calculate the conformal quantile,

<!-- chunk {"id": "body-0155", "role": "body", "section": "Cross-Conformal Prediction, CV+, and Jackknife+", "weight": 1.0} -->

Split conformal prediction requires only one model fitting step, but sacrifices statistical efficiency. On the other hand, full conformal prediction requires a very large number of model fitting steps, but has high statistical efficiency. These are not the only two achievable points on the spectrum---there are techniques that fall in between, trading off statistical efficiency and computational efficiency differently. In particular, cross-conformal prediction \[vovk2015cross\] and CV+/Jackknife+ \[barber2021predictive\] both use a small number of model fits, but still use all data for both model fitting and calibration. We refer the reader to those works for a precise description of the algorithms and corresponding statistical guarantees.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Historical Notes on Conformal Prediction", "weight": 1.0} -->

We hope the reader has enjoyed reading the technical content in our gentle introduction. As a dénouement, we now pay homage to the history of conformal prediction. Specifically, we will trace the history of techniques related to conformal prediction that are distribution-free, i.e., agnostic to the model, agnostic to the data distribution, and valid in finite samples. There are other lines of work in statistics with equal claim to the term "distribution-free" especially when it is interpreted asymptotically, such as permutation tests \[chung2013exact\], quantile regression \[koenker1978regression\], rank tests \[mann1947test, lehmann1953power, sidak1999theory\], and even the bootstrap \[efron1994introduction, chatterjee2009distribution\]---the following is not a history of those topics. Rather, we focus on the progenitors and progeny of conformal prediction.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Origins", "weight": 1.0} -->

The story of conformal prediction begins sixty-three kilometers north of the seventh-largest city in Ukraine, in the mining town of Chervonohrad in the Oblast of Lviv, where Vladimir Vovk spent his childhood. Vladimir's parents were both medical professionals, of Ukrainian descent, although the Lviv region changed hands many times over the years. During his early education, Vovk recalls having very few exams, with grades mostly based on oral answers. He did well in school and eventually took first place in the Mathematics Olympiad in Ukraine; he also got a Gold Medal, meaning he was one of the top graduating secondary school students. Perhaps because he was precocious, his math teacher would occupy him in class by giving him copies of a magazine formerly edited by Isaak Kikoin and Andrey Kolmogorov, Kvant, where he learned about physics, mathematics, and engineering---see Figure 18. Vladimir originally attended the Moscow Second Medical Institute (now called the Russian National Research Medical University) studying Biological Cybernetics, but eventually became disillusioned with the program, which had too much of a medical emphasis and imposed requirements to take classes like anatomy and physiology (there were "too many bones with strange Latin names").

<!-- chunk {"id": "body-0158", "role": "body", "section": "Origins", "weight": 1.0} -->

Therefore, he sat the entrance exams a second time and restarted school at the Mekh-Mat (faculty of mechanics and mathematics) in Moscow State University. In his third year there, he became the student of Andrey Kolmogorov. This was when the seeds of conformal prediction were first laid. Today, Vladimir Vovk is widely recognized for being the co-inventor of conformal prediction, along with collaborators Alexander Gammerman, Vladimir Vapnik, and others, whose contributions we will soon discuss. First, we will relay some of the historical roots of conformal prediction, along with some oral history related by Vovk that may be forgotten if never written.

<!-- chunk {"id": "body-0159", "role": "body", "section": "Origins", "weight": 1.0} -->

Kolmogorov and Vovk met approximately once a week during his three remaining years as an undergraduate at MSU. At that time, Kolmogorov took an interest in Vovk, and encouraged him to work on difficult mathematical problems. Ultimately, Vovk settled on studying a topic of interest to Kolmogorov: algorithmically random sequences, then known as *collectives*, and which were modified into *Bernoulli sequences* by Kolmogorov.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Origins", "weight": 1.0} -->

Work on collectives began at the turn of the 20th century, with Gustav Fechner's *Kollectivmasslehre* \[fechner1897kollektivmasslehre\], and was developed significantly by von Mises \[mises1919grundlagen\], Abraham Wald \[wald1937widerspruchfreiheit\], Alonzo Church \[church1940concept\], and so. A long debate ensued among these statisticians as to whether von Mises' axioms formed a valid foundation for probability, with Jean Ville being a notable opponent \[ville1939etude\]. Although the theory of von Mises' collectives is somewhat defunct, the mathematical ideas generated during this time continue to have a broad impact on statistics, as we will see. More careful historical reviews of the original debate on collectives exist elsewhere \[shafer2006sources, church1940concept, vovk2001kolmogorov, porter2014kolmogorov\]. We focus on its connection to the development of conformal prediction.

<!-- chunk {"id": "body-0161", "role": "body", "section": "Origins", "weight": 1.0} -->

Kolmogorov's interest in *Bernoulli sequences* continued into the 1970s and 1980s, when Vovk was his student. Vovk recalls that, on the way to the train station, Kolmogorov told him (not in these exact words),

<!-- chunk {"id": "body-0162", "role": "body", "section": "Origins", "weight": 1.0} -->

"Look around you; you do not only see infinite sequences. There are finite sequences."

<!-- chunk {"id": "body-0163", "role": "body", "section": "Origins", "weight": 1.0} -->

Feeling that the finite case was practically important, Kolmogorov extended the idea of collectives via Bernoulli sequences.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Enter Conformal Prediction", "weight": 1.0} -->

The framework we now call conformal prediction was hatched by Vladimir Vovk, Alexander Gammerman, Craig Saunders, and Vladimir Vapnik in the years 1996-1999, first using e-values \[gammerman1998learning\] and then with p-values \[saunders1999transduction, vovk1999machine\]. For decades, Vovk and collaborators developed the theory and applications of conformal prediction.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Enter Conformal Prediction", "weight": 1.0} -->

the 2002 proof that in online conformal prediction, the probability of error is independent across time-steps \[vovk2002line\];

<!-- chunk {"id": "body-0166", "role": "body", "section": "Enter Conformal Prediction", "weight": 1.0} -->

the 2002 development, along with Harris Papadopoulos and Kostas Proedrou, of split-conformal predictors \[papadopoulos2002inductive\];

<!-- chunk {"id": "body-0167", "role": "body", "section": "Enter Conformal Prediction", "weight": 1.0} -->

Glenn Shafer coins the term "conformal predictor" on December 1, 2003 while writing *Algorithmic Learning in a Random World* with Vovk \[vovk2005algorithmic\].

<!-- chunk {"id": "body-0168", "role": "body", "section": "Enter Conformal Prediction", "weight": 1.0} -->

the 2003 development of Venn Predictors \[vovk2003self\] (Vovk says this idea came to him on a bus in Germany during the Dagstuhl seminar "Kolmogorov Complexity & Applications");

<!-- chunk {"id": "body-0169", "role": "body", "section": "Enter Conformal Prediction", "weight": 1.0} -->

the 2012 founding of the Symposium on Conformal and Probabilistic Prediction and its Applications (COPA), hosted in Greece by Harris Papadopoulos and colleagues;

<!-- chunk {"id": "body-0170", "role": "body", "section": "Enter Conformal Prediction", "weight": 1.0} -->

the 2012 creation of cross-conformal predictors \[vovk2015cross\] and Venn-Abers predictors \[vovk2012venn\];

<!-- chunk {"id": "body-0171", "role": "body", "section": "Enter Conformal Prediction", "weight": 1.0} -->

The 2017 invention of conformal predictive distributions \[vovk2017nonparametric\].

<!-- chunk {"id": "body-0172", "role": "body", "section": "Enter Conformal Prediction", "weight": 1.0} -->

*Algorithmic Learning in a Random World* \[vovk2005algorithmic\], by Vovk, Gammerman, and Glenn Shafer, contains further perspective on the history described above in the bibliography of Chapter 2 and the main text of Chapter 10. Also, the book's website links to several dozen technical reports on conformal prediction and related topics. We now help the reader understand some of these key developments.

<!-- chunk {"id": "body-0173", "role": "body", "section": "Enter Conformal Prediction", "weight": 1.0} -->

Conformal prediction was recently popularized in the United States by the pioneering work of Jing Lei, Larry Wasserman, and colleagues \[lei2011efficient, lei2014distribution, lei2013distribution, poczos2013distribution, lei2014distribution, lei2018distribution\]. Vovk himself remembers Wasserman's involvement as a landmark moment in the history of the field. In particular, their general framework for distribution-free predictive inference in regression \[lei2018distribution\] has been a seminal work. They have also, in the special cases of kernel density estimation and kernel regression, created efficient approximations to full conformal prediction \[lei2013conformal, lei2014distribution\]. Jing Lei also created a fast and exact conformalization of the Lasso and elastic net procedures \[lei2019fast\]. Another equally important contribution of theirs was to introduce conformal prediction to thousands of researchers, including the authors of this paper, and also Rina Barber, Emmanuel Candès, Aaditya Ramdas, Ryan Tibshirani who themselves have made recent fundamental contributions.

<!-- chunk {"id": "body-0174", "role": "body", "section": "Enter Conformal Prediction", "weight": 1.0} -->

Some of these we have already touched upon in Section 2, such as adaptive prediction sets, conformalized quantile regression, covariate-shift conformal, and the idea of conformal prediction as indexing nested sets \[gupta2020nested\].

<!-- chunk {"id": "body-0175", "role": "body", "section": "Enter Conformal Prediction", "weight": 1.0} -->

This group also did fundamental work circumscribing the conditions under which distribution-free conditional guarantees can exist \[foygel2021limits\], building on previous works by Vovk, Lei, and Wasserman that showed for an arbitrary continuous distribution, conditional coverage is impossible \[vovk2012conditional, lei2014distribution, lei2018distribution\]. More fine-grained analysis of this fact has also recently been done in \[lee2021distribution\], showing that vanishing-width intervals are achievable if and only if the effective support size of the distribution of $X_{test}$ is smaller than the square of the sample size.

<!-- chunk {"id": "body-0176", "role": "body", "section": "Current Trends", "weight": 1.0} -->

We now discuss recent work in conformal prediction and distribution-free uncertainty quantification more generally, providing pointers to topics we did not discuss in earlier sections. Many of the papers we cite here would be great starting points for novel research on distribution-free methods.

<!-- chunk {"id": "body-0177", "role": "body", "section": "Current Trends", "weight": 1.0} -->

Many recent papers have focused on designing conformal procedures to have good practical performance according to specific desiderata like small set sizes \[Sadinle2016LeastAS\], coverage that is approximately balanced across regions of feature space \[foygel2021limits, izbicki2019flexible, romano2020classification, cauchois2020knowing, guan2020conformal, angelopoulos2020sets\], and errors balanced across classes \[lei2014classification, Sadinle2016LeastAS, hechtlinger2018cautious, guan2019prediction\]. This usually involves adjusting the conformal score; we gave many examples of such adjustments in Section 2. Good conformal scores can also be trained with data to optimize more complicated desiderata \[stutz2021learning\].

<!-- chunk {"id": "body-0178", "role": "body", "section": "Current Trends", "weight": 1.0} -->

Many statistical extensions to conformal prediction have also emerged. Such extensions include the ideas of risk control \[angelopoulos2020sets, angelopoulos2021learn\] and covariate shift \[tibshirani2019conformal\] that we previously discussed. One important and continual area of work is distribution shift, where our test point has a different distribution from our calibration data. For example, \[cauchois2020robust\] builds a conformal procedure robust to shifts of known $f$-divergence in the score function, and adaptive conformal prediction \[gibbs2021adaptive\] forms prediction sets in a data stream where the distribution varies over time in an unknown fashion by constantly re-estimating the conformal quantile. A weighted version of conformal prediction pioneered by \[barber2022conformal\] provides tools for addressing non-exchangeable data, most notably slowly changing time-series. This same work develops techniques for applying full conformal prediction to asymmetric algorithms.

<!-- chunk {"id": "body-0179", "role": "body", "section": "Current Trends", "weight": 1.0} -->

Beyond distribution shift, recent statistical extensions also address topics such as creating reliable conformal prediction intervals for counterfactuals and individual treatment effects \[lei2020conformal, yin2021conformal, chernozhukov2021exact\], covariate-dependent lower bounds on survival times \[candes2021conformalized\], prediction sets that preserve the privacy of the calibration data \[angelopoulos2021private\], handling dependent data \[chernozhukov2018exact, dunn2018distribution, oliveira2022split\], and achieving 'multivalid' coverage that is conditionally valid with respect to several possibly overlapping groups \[bastani2022practical, jung2022batch\].

<!-- chunk {"id": "body-0180", "role": "body", "section": "Current Trends", "weight": 1.0} -->

Furthermore, prediction sets are not the only important form of distribution-free uncertainty quantification. One alternative form is a *conformal predictive distribution*, which outputs a probability distribution over the response space $\mathcal{Y}$ in a regression problem \[vovk2017nonparametric\]. Recent work also addresses the issue of calibrating a scalar notion of uncertainty to have probabilistic meaning via histogram binning \[gupta2021distribution, park2021pac\]---this is like a rigorous version of Platt scaling or isotonic regression. The tools from conformal prediction can also be used to identify times when the distribution of data has changed by examining the score function's behavior on new data points.

<!-- chunk {"id": "body-0181", "role": "body", "section": "Current Trends", "weight": 1.0} -->

For example, \[bates2021multiple\] performs outlier detection using conformal prediction, \[vovk2021testing, volkhonskiy2017inductive\] detect change points in time-series data, \[hu2020distributionfree\] tests for covariate shift between two datasets, and \[podkopaev2021tracking\] tracks the risk of a predictor on a data-stream to identify when harmful changes in its distribution (one that increases the risk) occur.

<!-- chunk {"id": "body-0182", "role": "body", "section": "Current Trends", "weight": 1.0} -->

Developing better estimators of uncertainty improves the practical effectiveness of conformal prediction. The literature on this topic is too wide to even begin discussing; instead, we point to quantile regression as an example of a fruitful line of work that mingled especially nicely with conformal prediction in Section 2.2. Quantile regression was first proposed in \[koenker1978regression\] and extended to the locally polynomial case in \[chaudhuri1991global\]. Under sufficient regularity, quantile regression converges uniformly to the true quantile function \[chaudhuri1991global, steinwart2011estimating, takeuchi2006nonparametric, zhou1996direct, zhou1998statistical\]. Practical and accessible references for quantile regression have been written by Koenker and collaborators \[koenker2005quantile, koenker2018handbook\].

<!-- chunk {"id": "body-0183", "role": "body", "section": "Current Trends", "weight": 1.0} -->

Active work continues today to analyze the statistical properties of quantile regression and its variants under different conditions, for example in additive models \[koenker2011additive\] or to improve conditional coverage when the size of the intervals may correlate with miscoverage events \[feldman2021improving\]. The Handbook of Quantile Regression \[koenker2018handbook\] includes more detail on such topics, and a memoir of quantile regression for the interested reader. Since quantile regression provides intervals with near-conditional coverage asymptotically, the conformalized version inherits this good behavior as well.

<!-- chunk {"id": "body-0184", "role": "body", "section": "Current Trends", "weight": 1.0} -->

Along with such statistical advances has come a recent wave of practical applications of conformal prediction. Conformal prediction in large-scale deep learning was studied in \[angelopoulos2020sets\], focusing on image classification. One compelling use-case of conformal prediction is speeding up and decreasing the computational cost of the test-time evaluation of complex models \[fisch2020efficient, schuster2021consistent\]. The same researchers pooled information across multiple tasks in a meta-learning setup to form tight prediction sets for few-shot prediction \[fisch2021few\]. There is also an earlier line of work, appearing slightly after that of Lei and Wasserman, applying conformal prediction to decision trees \[johansson2014regression, linusson2017calibration, bostrom2017accelerating\]. Closer to end-users, we are aware of several real applications of conformal prediction. The Washington Post estimated the number of outstanding Democratic and Republican votes in the 2020 United States presidential election using conformal prediction \[cherian2020washington\].

<!-- chunk {"id": "body-0185", "role": "body", "section": "Current Trends", "weight": 1.0} -->

Early clinical experiments in hospitals underscore the utility of conformal prediction in that setting as well, although real deployments are still to come \[lu2021distribution, lu2021fair\]. Fairness and reliability of algorithmic risk forecasts in the criminal justice system improves (on controlled datasets) when applying conformal prediction \[Romano2020With, kuchibhotla2021nested, lu2021fair\]. Conformal prediction was recently applied to create safe robotic planning algorithms that avoid bumping into objects \[lindemann2022safe, dixit2022adaptive\]. Recently a scikit-learn compatible open-source library, MAPIE, has been developed for constructing conformal prediction intervals. There remains a mountain of future work in these applications of conformal prediction and many others.

<!-- chunk {"id": "body-0186", "role": "body", "section": "Current Trends", "weight": 1.0} -->

Today, the field of distribution-free uncertainty quantification remains small, but grows rapidly year-on-year. The promulgation of machine learning deployments has caused a reckoning that point predictions are not enough and shown that we still need rigorous statistical inference for reliable decision-making. Many researchers around the world have keyed into this fact and have created new algorithms and software using distribution-free ideas like conformal prediction. These developments are numerous and high-quality, so most reviews are out-of-date. To keep track of what gets released, the reader may want to see the Awesome Conformal Prediction repository \[acp\], which provides a frequently-updated list of resources in this area.

<!-- chunk {"id": "body-0187", "role": "body", "section": "Current Trends", "weight": 1.0} -->

We will end our Gentle Introduction with a personal note to the reader---you can be part of this story too. The infant field of distribution-free uncertainty quantification has ample room for significant technical contributions. Furthermore, the concepts are practical and approachable; they can easily be understood and implemented in code. Thus, we encourage the reader to try their hand at distribution-free uncertainty quantification; there is a lot more to be done!
