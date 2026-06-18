A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification

Topics include Conformal prediction, Distribution-free uncertainty quantification, Prediction sets, Prediction intervals, Split conformal prediction, Distribution shift, Structured prediction, Tutorial.

Gives a practical, example-driven introduction to conformal prediction as a wrapper for producing finite-sample-valid uncertainty sets around black-box models. Its main value is pedagogical breadth: it connects the basic split conformal recipe to modern applications involving images, language, time series, abstention, distribution shift, and structured outputs.

Black-box machine learning models are now routinely used in high-risk settings, like medical diagnostics, which demand uncertainty quantification to avoid consequential model failures. Conformal prediction is a user-friendly paradigm for creating statistically rigorous uncertainty sets/intervals for the predictions of such models. Critically, the sets are valid in a distribution-free sense: they possess explicit, non-asymptotic guarantees even without distributional assumptions or model assumptions. One can use conformal prediction with any pre-trained model, such as a neural network, to produce sets that are guaranteed to contain the ground truth with a user-specified probability, such as 90%. It is easy-to-understand, easy-to-use, and general, applying naturally to problems arising in the fields of computer vision, natural language processing, deep reinforcement learning, and so . This hands-on introduction is aimed to provide the reader a working understanding of conformal prediction and related distribution-free uncertainty quantification techniques with one self-contained document.

## Abstract

Black-box machine learning models are now routinely used in high-risk settings, like medical diagnostics, which demand uncertainty quantification to avoid consequential model failures. Conformal prediction (a.k.a. conformal inference) is a user-friendly paradigm for creating statistically rigorous uncertainty sets/intervals for the predictions of such models. Critically, the sets are valid in a *distribution-free* sense: they possess explicit, non-asymptotic guarantees even without distributional assumptions or model assumptions.

This hands-on introduction is aimed to provide the reader a working understanding of conformal prediction and related distribution-free uncertainty quantification techniques with one self-contained document. We lead the reader through practical theory for and examples of conformal prediction and describe its extensions to complex machine learning tasks involving structured outputs, distribution shift, time-series, outliers, models that abstain, and more. Throughout, there are many explanatory illustrations, examples, and code samples in Python.

## Conformal Prediction

Conformal prediction \[vovk2005algorithmic, papadopoulos2002inductive, lei2014distribution\] (a.k.a. conformal inference) is a straightforward way to generate prediction sets for any model. We will introduce it with a short, pragmatic image classification example, and follow up in later paragraphs with a general explanation. The high-level outline of conformal prediction is as follows. First, we begin with a fitted predicted model (such as a neural network classifier) which we will call $\hat{f}$.

## Discussion

As our examples have shown, conformal prediction is a simple and pragmatic technique with many use cases. It is also easy to implement and computationally trivial. Additionally, the above four examples serve as roadmaps to the user for designing score functions with various notions of optimality, including average size, adaptivity, and Bayes risk. Still more is yet to come---conformal prediction can be applied more broadly than it may first seem at this point. We will outline extensions of conformal prediction to other prediction tasks such as outlier detection, image segmentation, serial time-series prediction, and so on in Section 4.
