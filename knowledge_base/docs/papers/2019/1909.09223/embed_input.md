InterpretML: A Unified Framework for Machine Learning Interpretability

Topics include Learning, InterpretML, Machine learning.

InterpretML is an open-source Python package which exposes machine learning interpretability algorithms to practitioners and researchers. InterpretML exposes two types of interpretability - glassbox models, which are machine learning models designed for interpretability (ex: linear models, rule lists, generalized additive models), and blackbox explainability techniques for explaining existing systems (ex: Partial Dependence, LIME). The package enables practitioners to easily compare interpretability algorithms by exposing multiple methods under a unified API, and by having a built-, extensible visualization platform. InterpretML also includes the first implementation of the Explainable Boosting Machine, a powerful, interpretable, glassbox model that can be as accurate as many blackbox models. The MIT licensed source code can be downloaded from github.com/microsoft/interpret.

## Introduction

As machine learning has matured into wide-spread adoption, building models that users can understand is becoming increasingly important. This can easily be observed in high-risk applications such as healthcare, finance and judicial environments. Interpretability is also important in general applied machine learning problems such as model debugging, regulatory compliance, and human computer interaction.

We address these needs with InterpretML by exposing many state of the art interpretability algorithms under a unified API. This API covers two major interpretability forms: "glassbox" models, which are inherently intelligible and explainable to the user, and "blackbox" interpretability, methods that generate explanations for any machine learning pipeline, no matter how opaque it is. This is further supported with interactive visualizations and a built-in dashboard designed for interpretability algorithm comparison.

## Package Design

InterpretML follows four key design principles that influence its architecture and API.

Ease of comparison. Make it as easy as possible to compare multiple algorithms. ML interpretability is in its infancy, and many algorithmic approaches have emerged from research, each of which has pros and cons. Comparison is critical to find the algorithm that best suits the users' needs. InterpretML enables this by enforcing a scikit-learn style uniform API, and providing a visualization platform centered around algorithmic comparison.
