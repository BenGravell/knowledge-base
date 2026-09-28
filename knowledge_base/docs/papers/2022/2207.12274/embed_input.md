<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

MAPIE: An Open-source Library for Distribution-free Uncertainty Quantification

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Estimating uncertainties associated with the predictions of Machine Learning (ML) models is of crucial importance to assess their robustness and predictive power. In this submission, we introduce MAPIE (Model Agnostic Prediction Interval Estimator), an open-source Python library that quantifies the uncertainties of ML models for single-output regression and multi-class classification tasks. MAPIE implements conformal prediction methods, allowing the user to easily compute uncertainties with strong theoretical guarantees on the marginal coverages and with mild assumptions on the model or on the underlying data distribution. MAPIE is hosted on scikit-learn-contrib and is fully "scikit-learn-compatible". As such, it accepts any type of regressor or classifier coming with a scikit-learn API.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Quantifying the uncertainties of ML model predictions is of crucial importance for developing and deploying reliable artificial intelligence (AI) systems. Uncertainty quantification (UQ) involves all the stakeholders who develop and use AI models. First, UQ allows the designers of AI systems to better understand the predictive power of their model and assess the validity of the model predictions on new data points. Second, UQ allows AI operators, such as business stakeholders, to optimize the risk management when making business decisions based on AI system predictions. Third, UQ helps AI regulators to assess the compliance of the AI system with the regulation in force. Fourth, UQ allows the AI systems to be more transparent and trustworthy for people impacted by the decisions made from AI.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

There is therefore a strong need for libraries of uncertainty quantification that respect three fundamental pillars. First, implemented methods have to be model and use case agnostic in order to address all relevant use cases tackled in industry, such as natural language processing, time series, or computer vision, using state-of-the-art ML models, like neural networks or gradient boosting models. Second, methods must have strong theoretical guarantees at least on the marginal coverage (and possibly on the conditional coverage) of the estimated uncertainties with as little assumption on the data or the model as possible. This ensures AI system designers, operators, and regulators to be confident about the predictions provided by the models. Third, libraries need to be open-source and respect state-of-the-art programming standards to develop trustworthy AI systems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Resampling or undersampling methods have been used for a few decades to estimate the robustness of predictions. Among other, Bootstrap is probably the most commonly used methods since it is easy to implement and allow the user to easily obtain confidence intervals associated with the predictions. However, the standard jackknife technique suffers from instabilities in some cases and can be unusable on practical use cases when the number of training data samples is high.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although modern resampling techniques have been implemented in recent R packages (see for instance ), they are not yet implemented in Python and in particular within the standard scikit-learn framework. Some scikit-learn regressors allow the users to estimate confidence intervals associated with the model predictions but they are either simple regressors, such as the Bayesian Ridge model, or based on quantile regression for gradient boosting. IBM's UQ360 is noteworthy as this library aims at incorporating several complementary UQ methods (Bayesian inference, quantile regression, jackknife, etc). However, it is still in its early stages and has been inactive for the past 6 months.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Since 2021, we develop the MAPIE (Model Agnostic Prediction Interval Estimator) library in order to address the three aforementioned pillars. MAPIE is an open-source Python library hosted on scikit-learn-contrib. It follows the scikit-learn guidelines; the only technical requirement is to have a scikit-learn API and accepts base scikit-learn-compatible estimators. Importantly, MAPIE implements conformal prediction methods for regression and classification settings and is therefore model and (soon to be) use case agnostic. Conformal prediction methods allow MAPIE to have mathematical guarantees on the marginal coverages on the uncertainties.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Section 2 presents the conformal prediction methods implemented in MAPIE. Section 3 describes MAPIE in practice by listing the main input parameters and how to use them. Section 4 presents two illustrative examples. Section 5 concludes with our perspectives.

<!-- chunk {"id": "body-0009", "role": "body", "section": "General settings", "weight": 1.0} -->

Before describing the methods, we briefly present the mathematical setting. For a regression or a classification problem in a standard independent and identically distributed (i.i.d) case, our training data $(X,Y)=\{(x_{1},y_{1}),\ldots,(x_{n},y_{n})\}$ has an unknown distribution $P_{X,Y}$. For any risk level $\alpha$ between 0 and 1, we aim at constructing a prediction interval or a prediction set $\hat{C}_{n,\alpha}(X_{n+1})$ for a new observation $\left(X_{n+1},Y_{n+1}\right)$ such that: In words, for a typical risk level $\alpha$ of $10\%$, we want to construct prediction intervals or prediction sets that contain the true observations for at least $90\%$ of the new test data points. To achieve this objective, MAPIE includes several split- or cross-conformal methods for constructing prediction intervals or prediction sets for regression or classification tasks, respectively.

<!-- chunk {"id": "body-0010", "role": "body", "section": "General settings", "weight": 1.0} -->

We can sum up UQ with split-conformal prediction as follows: Choose a \"conformity score\" that quantifies how well the observation conforms with the prediction of the ML model. The higher the value, the more atypical the point. For regression, the conformity scores can be the residuals. For classification, they can be the cumulative sum of ranked softmax scores.

<!-- chunk {"id": "body-0011", "role": "body", "section": "General settings", "weight": 1.0} -->

Train the model on a training set and calibrate the conformity scores on a calibration set apart from the training set to avoid over-fitting.

<!-- chunk {"id": "body-0012", "role": "body", "section": "General settings", "weight": 1.0} -->

Estimate the quantile of the conformity score distribution associated with the chosen risk level $\alpha$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "General settings", "weight": 1.0} -->

Construct prediction intervals or prediction sets for new test points based on this quantile.

<!-- chunk {"id": "body-0014", "role": "body", "section": "MAPIE for tabular regression", "weight": 1.0} -->

MAPIE has three state-of-the-art conformal prediction methods (along with their derivatives) for tabular regression: Jackknife+, CV+ and Jackknife+-after-Bootstrap.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Jackknife+", "weight": 1.0} -->

Presented, the Jackknife+ method is based on the standard Jackknife, which constructs a set of leave-one-out models. Estimating the prediction intervals is carried out in three main steps. First, train $n$ leave-one-out models (one for each training instance), each leave-one-out model is trained on the entire training set except the corresponding training point. Second, compute the corresponding conformity scores (here, the leave-one-out residuals) $|Y_{i}-\hat{\mu}_{-i}(X_{i})|$. Third, fit the regression function $\hat{\mu}$ on the entire training set and construct the prediction intervals from the distribution of the computed leave-one-out residuals and the desired $1-\alpha$ quantile. This method avoids over-fitting but still does not guarantee the targeted coverage if $\hat{\mu}$ is unstable, for example when the sample size is close to the number of features.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Jackknife+", "weight": 1.0} -->

Unlike the standard jackknife method which returns a prediction interval centered around the prediction of the model trained on the entire dataset, the so-called Jackknife+ method also uses the predictions from all leave-one-out models on the new test point to take the variability of the regression function into account. The resulting confidence interval can therefore be summarized as follows As described, this method guarantees a higher stability with a coverage level of $1-2\alpha$ for a target coverage level of $1-\alpha$, under the assumption of independence of the distribution of the data $(X,Y)$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "CV+", "weight": 1.0} -->

In order to reduce the computational cost, one can adopt a cross-validation approach instead of a leave-one-out approach, with the so-called CV+ method. Similar to the Jackknife+ method, estimating the prediction intervals with CV+ is performed in four main steps. First, split the training set into $K$ disjoint subsets $S_{1},S_{2},...,S_{K}$ of equal size. Second, regression functions $\hat{\mu}_{-S_{k}}$ are fitted on the training set with the corresponding $k^{th}$ fold removed. Third, the corresponding out-of-fold residuals are computed for each $i^{th}$ point $|Y_{i}-\hat{\mu}_{-S_{k(i)}}(X_{i})|$ where $k(i)$ is the fold containing $i$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "CV+", "weight": 1.0} -->

Finally, similar to Jackknife+, the regression functions $\hat{\mu}_{-S_{k(i)}}(X_{i})$ are used to estimate the prediction intervals.

<!-- chunk {"id": "body-0019", "role": "body", "section": "CV+", "weight": 1.0} -->

As for Jackknife+, this method guarantees a coverage level higher than $1-2\alpha$ for a target coverage level of $1-\alpha$, assuming essentially the independence of the data. As pointed out, Jackknife+ can be considered as a special case of CV+ with $K=n$. In practice, this method results in slightly wider prediction intervals and is therefore likely more conservative, but gives a reasonable compromise for large datasets when the Jacknife+ method is unfeasible.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Jackknife+-after-Bootstrap", "weight": 1.0} -->

An alternative way to reduce the computational cost is to adopt a bootstrap approach instead of cross-validation, called the Jackknife+-after-bootstrap method, offered. Similar to CV+, estimating the prediction intervals with Jackknife+-after-bootstrap is performed in four main steps. First, resample the training set with replacement (bootstrap) $K$ times, to get the (non disjoint) bootstraps $B_{1},...,B_{K}$ of equal size. Second, fit $K$ regressions functions $\hat{\mu}_{B_{k}}$ on the bootstraps ($B_{k}$), and compute the predictions on the complementary sets $B_{k}^{c}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Jackknife+-after-Bootstrap", "weight": 1.0} -->

Third, aggregate these predictions according to a given aggregation function, typically mean or median, and compute the residuals $|Y_{j}-{\rm agg}(\hat{\mu}(B_{K(j)}(X_{j})))|$ are computed for each $X_{j}$ (with $K(j)$ the boostraps not containing $X_{j}$). The sets $\{{\rm agg}(\hat{\mu}_{K(j)}(X_{i})+r_{j}\}$ (where $j$ indexes the training set) are used to estimate the prediction intervals.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Jackknife+-after-Bootstrap", "weight": 1.0} -->

As for Jackknife+, this distribution-free method guarantees a coverage level higher than $1-2\alpha$ for a target coverage level of $1-\alpha$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "MAPIE for Time Series", "weight": 1.0} -->

The methods implemented in MAPIE for tabular regression assume that data are exchangeable. This hypothesis is hardly reasonable for dynamical time series, thus requiring a specific method. The method implemented in MAPIE is based on the algorithm Ensemble Batch Prediction Intervals (EnbPI, see ). In this method, the assumption on data exchangeability is replaced with assumptions on the residuals of the estimators (errors process and estimations quality). Moreover the coverage guaranty is not absolutely but approximately valid up to these assumptions validity.

<!-- chunk {"id": "body-0024", "role": "body", "section": "MAPIE for Time Series", "weight": 1.0} -->

The corresponding algorithm is very closed to Jackknife+-after-Bootstrap. It is notably based on bootstrapping (with a block bootstrap that suits to time series). The predictions are the aggregations of the predictions of the refitted estimators. The bounds of the prediction intervals are the predictions plus or minus suitable quantiles of the conformity scores. So the widths of the intervals only depend on the conformity scores and not on the variability of the predictions of the refitted estimators, contrary to Jackknife+.

<!-- chunk {"id": "body-0025", "role": "body", "section": "MAPIE for Time Series", "weight": 1.0} -->

The conformity scores are no longer the absolute values of the residuals but the relative values. So the prediction intervals are not symmetric with respect to the predictions. Moreover, the levels of the quantiles are optimized so that the widths of the intervals are minimum while the difference between the quantiles' level is $1-\alpha$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "MAPIE for Time Series", "weight": 1.0} -->

Finally, the conformity scores are updated during the prediction process. So they can dynamically take into account, for example, an increase in the variance of the residuals or a model deterioration.

<!-- chunk {"id": "body-0027", "role": "body", "section": "MAPIE for classification", "weight": 1.0} -->

Three methods for multi-class classification UQ have been implemented in MAPIE so far: LABEL, Adaptive Prediction Sets and Top-K. The difference between these methods is the way the conformity scores are computed.

<!-- chunk {"id": "body-0028", "role": "body", "section": "LABEL", "weight": 1.0} -->

In the LABEL method, the conformity score is defined as as one minus the score of the true label. For each point $i$ of the calibration set: Once the conformity scores ${s_{1},...,s_{n}}$ are estimated for all calibration points, we compute the $(n+1)*(1-\alpha)/n$ quantile $\hat{q}$ as follows: Finally, we construct a prediction set by including all labels with a score higher than the estimated quantile: This simple approach allows us to construct prediction sets coming with a theoretical guarantee on the marginal coverage. However, although this method generally results in small prediction sets, it tends to produce empty ones when the model is uncertain, for example at the border between two classes.

<!-- chunk {"id": "body-0029", "role": "body", "section": "APS", "weight": 1.0} -->

The so-called Adaptive Prediction Set (APS) method overcomes the problem encountered by the LABEL method through the construction of prediction sets which are by definition non-empty. The conformity scores are computed by summing the ranked scores of each label, from the higher to the lower until reaching the true label of the observation: The quantile $\hat{q}$ is then computed the same way as the score method. For the construction of the prediction sets for a new test point, the same procedure of ranked summing is applied until reaching the quantile, as described in the following equation: By default, the label whose cumulative score is above the quantile is included in the prediction set. However, its incorporation can also be chosen randomly based on the difference between its cumulative score and the quantile so the effective coverage remains close to the target (marginal) coverage. We refer the reader to and for more details about this aspect.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Top-K", "weight": 1.0} -->

Introduced, the specificity of the Top-K method is that it will give the same prediction set size for all observations. The conformity score is the rank of the true label, with scores ranked from higher to lower. The prediction sets are build by taking the $\hat{q}^{th}$ higher scores. The procedure is described in equation 5.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Top-K", "weight": 1.0} -->

Finally, it should be noted that MAPIE includes split- and cross-conformal strategies for the LABEL and APS methods, but only the split-conformal one for Top-K.

<!-- chunk {"id": "body-0032", "role": "body", "section": "MAPIE in practice", "weight": 1.0} -->

The MAPIE library offers two base Pythonic classes, called MapieRegressor and MapieClassifier for estimating prediction intervals and prediction sets, respectively, via the construction of conformity scores. Figure 1 presents the typical commands needed for quantifying the uncertainties. As the MAPIE base classes are inherited from scikit-learn BaseEstimator classes, the API is very intuitive to anyone familiar with scikit-learn and follows a initialization-fit-predict process.

<!-- chunk {"id": "body-0033", "role": "body", "section": "MAPIE in practice", "weight": 1.0} -->

After initializing the base scikit-learn-compatible base model, one needs to initialize the desired MAPIE class with two main arguments that define the strategy for uncertainty quantification: \"cv\" defines the train / calibration set splitting strategy for training the model and calibrating the conformity scores. It can be \"prefit\" in the split-conformal case where the base model is already fitted on a given training set while the set given to MAPIE is used directly for calibrating the conformity scores. For cross-conformal methods, one can simply define an integer that sets the number of splits and MAPIE will call internally the corresponding BaseCrossValidator object, such as LeaveOneOut and KFold for the Jackknife or CV strategies, respectively.

<!-- chunk {"id": "body-0034", "role": "body", "section": "MAPIE in practice", "weight": 1.0} -->

\"method\" controls the strategy for constructing the prediction intervals or prediction sets. For regression tasks, one can choose among \"base\", \"plus\", or \"minmax\". For example, method=\"plus\" together with cv=KFold defines the CV+ method with 5 folds. For classification, one can choose \"score\" for the LABEL method, \"cumulated_score\" for the Adaptive Prediction Set (APS) method, and \"top_k\" for the Top-K method. For example, method=\"cumulated_score\" together with cv=KFold defines the APS method with the CV+ strategy as defined in Algorithm 2 of.

<!-- chunk {"id": "body-0035", "role": "body", "section": "MAPIE in practice", "weight": 1.0} -->

Methods that deviate from these standard cases (i.e. training and test i.i.d. datasets sampled from similar distribution) need to be implemented in other classes using MapieRegressor or MapieClassifier as base classes. For instance, the EnbPI method is implemented in the MapieTimeSeriesRegressor class that inherits from MapieRegressor. This process allows anyone to suggest an implementation of a new conformal prediction method through a dedicated Pull Request that follows the MAPIE guidelines without modifying the base classes.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Examples", "weight": 1.0} -->

We present two simple examples of uncertainty quantification on time series and computer vision settings using MAPIE. The notebooks for both examples can be found in the github repository

<!-- chunk {"id": "body-0037", "role": "body", "section": "MAPIE for Time series", "weight": 1.0} -->

We illustrate the EnbPI algorithm with MapieTimeSeriesRegressor on the Victoria electricity demand dataset with an artificial change point on the test set. The Victoria electricity demand dataset consists in the hourly demand of electricity in the Victoria state in Australia between January 1st and February 23rd of 2014. The test set is the last week, and the remaining weeks are included in the training set. We added a sudden decrease of the electricity demand of 2 GW on February 22 to simulate a change point in the test set. The explanatory variables are the lags of the demand up to 5 previous hours and the temperature. The base ML model is a Random Forest whose hyperparameters are optimized through chronological cross-validation. We then use this tuned Random Forest as the base model for the EnbPI method, using 100 block bootstrap resamplings and with a block length of 48 hours. We sequentially estimate the prediction interval on the electricity demand one step ahead.

<!-- chunk {"id": "body-0038", "role": "body", "section": "MAPIE for image classification", "weight": 1.0} -->

We illustrate uncertainty quantification on image classification with the famous dataset which consists in images belonging to 10 classes: airplane, automobile, bird, cat, deer, dog, frog, horse, ship and truck.

<!-- chunk {"id": "body-0039", "role": "body", "section": "MAPIE for image classification", "weight": 1.0} -->

As mentioned before, MAPIE is a \"scikit-learn compatible\" library, meaning that the base classifier must include the classes\_, trained\_ attributes and the fit, train, predict, predict_proba, \_\_sklearn_is_fitted\_\_ methods in order to be accepted by MapieClassifier. Hence, for computer vision settings, one can create a wrapper around a deep learning model object (or any other non-scikit-learn compatible ML model) to be digested by MapieClassifier. An example of such a wrapper can be found in the notebook of the MAPIE repository ^11^ 1 After training a small convolutional neural network on the dataset, we used this wrapper to fit MAPIE on a calibration set and create prediction sets on a test set. Figure 3 compares the different aforedescribed methods implemented in MAPIE with a naive one which directly includes all the labels such that their sum is just above the target coverage level.

<!-- chunk {"id": "body-0040", "role": "body", "section": "MAPIE for image classification", "weight": 1.0} -->

As expected, the \"naive\" method has a coverage which is below the target coverage for $\alpha$ values higher than 0.6: this is because output scores of the model do not represent probabilities. Thus, even by adding the labels, there are no guarantees that the coverage will be achieved. Other methods, on the other hand, all achieve the required coverage regardless the $\alpha$ value because they calibrate the scores with a dataset not seen by the model during training.

<!-- chunk {"id": "body-0041", "role": "body", "section": "MAPIE for image classification", "weight": 1.0} -->

Even though the methods all achieve the required coverages, the averaged sizes of their prediction sets are quite different, especially at low $\alpha$ values. As discussed in the previous section, the \"score\" method achieves the lowest averaged size for all target coverages compared to the \"cumulated_score\" and \"top_k\" methods. However, the \"score\" method may also result in empty prediction sets. This situation arises in uncertain cases where the predicted scores of all labels do not reach the target quantile. On the second hand, the \"cumulated_score\", by definition, always includes at least one label, the one whose cumulated score is higher than the quantile, but induces over-estimated marginal coverages for low $\alpha$ values. To force the marginal coverage to stay close to the target one, one can choose the \"random_cumulated_score\" which includes randomly the last label. The major drawback of the latter method is that it creates empty prediction sets which indicate low uncertainties, unlike the \"score\" method.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Current implementations", "weight": 1.0} -->

In addition to the extension of MAPIE to time series settings, other methods derived from standard i.i.d. split-/cross-conformal paradigms are being implemented, such as conformalized quantile regression or covariate shift.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conformalized Quantile Regression (LLA)", "weight": 1.0} -->

Where all the previously mentioned methods from MapieRegressor guarantee the targeted coverage, the width does not vary locally and therefore fails to undertake heteroscedastic noise. Through the implementation of Conformalized Quantile Regression, we created a new class MapieQuantileRegressor that offers a new \"quantile\" method which adapts the width of the prediction intervals to the noise in the data.

<!-- chunk {"id": "body-0044", "role": "body", "section": "A framework for straightforward implementation of new conformal prediction methods", "weight": 1.0} -->

Motivated by the implementation of various conformal prediction methods, we are also working on the refactorization of the base MapieRegressor and MapieClassifier class in order to offer a more robust framework for optimizing the implementation of new conformal prediction algorithms by external collaborators.

<!-- chunk {"id": "body-0045", "role": "body", "section": "A framework for straightforward implementation of new conformal prediction methods", "weight": 1.0} -->

Future implementations that would benefit from this refactorization could adaptive conformal inference, multi-target regression through copula-based conformal prediction for regression settings or regularized adaptive prediction sets or conformal label shift for classification settings.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Extension to new settings", "weight": 1.0} -->

Finally, we also plan to extend MAPIE to other computer vision settings, such as image segmentation or object detection for instance through the implementation of the Risk-controlling Prediction Sets or the Learn Then Test frameworks.
