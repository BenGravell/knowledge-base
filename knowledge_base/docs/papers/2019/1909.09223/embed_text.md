## Introduction

As machine learning has matured into wide-spread adoption, building models that users can understand is becoming increasingly important. This can easily be observed in high-risk applications such as healthcare, finance and judicial environments. Interpretability is also important in general applied machine learning problems such as model debugging, regulatory compliance, and human computer interaction.

We address these needs with InterpretML by exposing many state of the art interpretability algorithms under a unified API. This API covers two major interpretability forms: "glassbox" models, which are inherently intelligible and explainable to the user, and "blackbox" interpretability, methods that generate explanations for any machine learning pipeline, no matter how opaque it is. This is further supported with interactive visualizations and a built-in dashboard designed for interpretability algorithm comparison. InterpretML is MIT licensed, and emphasizes extensibility and compatibility with popular open-source projects such as scikit-learn and Jupyter Notebook environments.

## Package Design

InterpretML follows four key design principles that influence its architecture and API.

Ease of comparison. Make it as easy as possible to compare multiple algorithms. ML interpretability is in its infancy, and many algorithmic approaches have emerged from research, each of which has pros and cons. Comparison is critical to find the algorithm that best suits the users' needs. InterpretML enables this by enforcing a scikit-learn style uniform API, and providing a visualization platform centered around algorithmic comparison.

Stay true to the source. Use reference algorithms and visualizations as much as possible. Our goal is to expose interpretability algorithms to the world, in their most accurate form.

Play nice with others. Leverage the open-source ecosystem, and don't reinvent the wheel. InterpretML is highly compatible with popular projects like Jupyter Notebook and scikit-learn, and builds off of many libraries like plotly, lime, shap, and SALib.

Take what you want. Use and extend any component of InterpretML without pulling in the whole framework. For example, it's possible to produce a computationally intensive explanation on a server, without InterpretML's visualization and its related dependencies.

The code architecture and unified API is best expressed in Figure 1, providing an overview and relevant example code.

Figure 1: API architecture and code examples

## Explainable Boosting Machine

As part of the framework, InterpretML also includes a new interpretability algorithm -- the Explainable Boosting Machine (EBM). EBM is a glassbox model, designed to have accuracy comparable to state-of-the-art machine learning methods like Random Forest and Boosted Trees, while being highly intelligibile and explainable. EBM is a generalized additive model (GAM) of the form: where g is the link function that adapts the GAM to different settings such as regression or classification. EBM has a few major improvements over traditional GAMs. First, EBM learns each feature function f~j~ using modern machine learning techniques such as bagging and gradient boosting. The boosting procedure is carefully restricted to train on one feature at a time in round-robin fashion using a very low learning rate so that feature order does not matter. It round-robin cycles through features to mitigate the effects of co-linearity and to learn the best feature function f~j~ for each feature to show how each feature contributes to the model's prediction for the problem. Second, EBM can automatically detect and include pairwise interaction terms of the form: which further increases accuracy while maintaining intelligibility. EBM is a fast implementation of the GA^2^M algorithm, written in C++ and Python. The implementation is parallelizable, and takes advantage of joblib to provide multi-core and multi-machine parallelization. The algorithmic details for the training procedure, selection of pairwise interaction terms, and case studies can be found.

EBMs are highly intelligible, because the contribution of each feature to a final prediction can be visualized and understood by plotting f~j~. Because EBM is an additive model, each feature contributes to predictions in a modular way that makes it easy to reason about the contribution of each feature to the prediction.

Figure 2: Left: Function fAge. As ’Age’ increases from 20 to 50, p increases significantly. Right: Individual prediction, where the ’CapitalGain’ feature dominates.

To make individual predictions, each function f~j~ acts as a lookup table per feature, and returns a term contribution. These term contributions are simply added up, and passed through the link function g to compute the final prediction. Because of the modularity (additivity), term contributions can be sorted and visualized to show which features had the most impact on any individual prediction.

Classification Performance (AUROC) Figure 3: Classification performance for models across datasets (rows, columns).

Figure 4: Computational performance for models across datasets (rows, columns).

In terms of predictive power, EBM often performs surprisingly well, and is comparable with state of the art methods like Random Forest and XGBoost.^11^1All models were trained with their default parameters. EBM's current default parameters are chosen for computational speed, to enable ease of experimentation. For the best accuracy and interpretability, we recommend using reference parameters: 100 inner bags, 100 outer bags, 5000 epochs, and a learning rate of 0.01. To keep the individual terms additive, EBM pays an additional training cost, making it somewhat slower than similar methods. However, because making predictions involves simple additions and lookups inside of the feature functions f~j~, EBMs are one of the fastest models to execute at prediction time. EBM's light memory usage and fast predict times makes it particularly attractive for model deployment in production.
