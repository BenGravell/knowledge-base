<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

InterpretML: A Unified Framework for Machine Learning Interpretability

Topics include Learning, InterpretML, Machine learning.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

InterpretML is an open-source Python package which exposes machine learning interpretability algorithms to practitioners and researchers. InterpretML exposes two types of interpretability - glassbox models, which are machine learning models designed for interpretability (ex: linear models, rule lists, generalized additive models), and blackbox explainability techniques for explaining existing systems (ex: Partial Dependence, LIME). The package enables practitioners to easily compare interpretability algorithms by exposing multiple methods under a unified API, and by having a built-, extensible visualization platform. InterpretML also includes the first implementation of the Explainable Boosting Machine, a powerful, interpretable, glassbox model that can be as accurate as many blackbox models. The MIT licensed source code can be downloaded from github.com/microsoft/interpret.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

As machine learning has matured into wide-spread adoption, building models that users can understand is becoming increasingly important. This can easily be observed in high-risk applications such as healthcare, finance and judicial environments. Interpretability is also important in general applied machine learning problems such as model debugging, regulatory compliance, and human computer interaction.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We address these needs with InterpretML by exposing many state of the art interpretability algorithms under a unified API. This API covers two major interpretability forms: "glassbox" models, which are inherently intelligible and explainable to the user, and "blackbox" interpretability, methods that generate explanations for any machine learning pipeline, no matter how opaque it is. This is further supported with interactive visualizations and a built-in dashboard designed for interpretability algorithm comparison. InterpretML is MIT licensed, and emphasizes extensibility and compatibility with popular open-source projects such as scikit-learn and Jupyter Notebook environments.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Package Design", "weight": 1.0} -->

InterpretML follows four key design principles that influence its architecture and API.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Package Design", "weight": 1.0} -->

Ease of comparison. Make it as easy as possible to compare multiple algorithms. ML interpretability is in its infancy, and many algorithmic approaches have emerged from research, each of which has pros and cons. Comparison is critical to find the algorithm that best suits the users' needs. InterpretML enables this by enforcing a scikit-learn style uniform API, and providing a visualization platform centered around algorithmic comparison.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Package Design", "weight": 1.0} -->

Stay true to the source. Use reference algorithms and visualizations as much as possible. Our goal is to expose interpretability algorithms to the world, in their most accurate form.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Package Design", "weight": 1.0} -->

Play nice with others. Leverage the open-source ecosystem, and don't reinvent the wheel. InterpretML is highly compatible with popular projects like Jupyter Notebook and scikit-learn, and builds off of many libraries like plotly, lime, shap, and SALib.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Package Design", "weight": 1.0} -->

Take what you want. Use and extend any component of InterpretML without pulling in the whole framework. For example, it's possible to produce a computationally intensive explanation on a server, without InterpretML's visualization and its related dependencies.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Package Design", "weight": 1.0} -->

The code architecture and unified API is best expressed in Figure 1, providing an overview and relevant example code.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Explainable Boosting Machine", "weight": 1.0} -->

As part of the framework, InterpretML also includes a new interpretability algorithm -- the Explainable Boosting Machine (EBM). EBM is a glassbox model, designed to have accuracy comparable to state-of-the-art machine learning methods like Random Forest and Boosted Trees, while being highly intelligibile and explainable.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Explainable Boosting Machine", "weight": 1.0} -->

where g is the link function that adapts the GAM to different settings such as regression or classification. EBM has a few major improvements over traditional GAMs. First, EBM learns each feature function f~j~ using modern machine learning techniques such as bagging and gradient boosting. The boosting procedure is carefully restricted to train on one feature at a time in round-robin fashion using a very low learning rate so that feature order does not matter. It round-robin cycles through features to mitigate the effects of co-linearity and to learn the best feature function f~j~ for each feature to show how each feature contributes to the model's prediction for the problem.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Explainable Boosting Machine", "weight": 1.0} -->

which further increases accuracy while maintaining intelligibility. EBM is a fast implementation of the GA^2^M algorithm, written in C++ and Python. The implementation is parallelizable, and takes advantage of joblib to provide multi-core and multi-machine parallelization. The algorithmic details for the training procedure, selection of pairwise interaction terms, and case studies can be found.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Explainable Boosting Machine", "weight": 1.0} -->

EBMs are highly intelligible, because the contribution of each feature to a final prediction can be visualized and understood by plotting f~j~. Because EBM is an additive model, each feature contributes to predictions in a modular way that makes it easy to reason about the contribution of each feature to the prediction.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Explainable Boosting Machine", "weight": 1.0} -->

To make individual predictions, each function f~j~ acts as a lookup table per feature, and returns a term contribution. These term contributions are simply added up, and passed through the link function g to compute the final prediction. Because of the modularity (additivity), term contributions can be sorted and visualized to show which features had the most impact on any individual prediction.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Explainable Boosting Machine", "weight": 1.0} -->

In terms of predictive power, EBM often performs surprisingly well, and is comparable with state of the art methods like Random Forest and XGBoost.^11^1All models were trained with their default parameters. EBM's current default parameters are chosen for computational speed, to enable ease of experimentation. For the best accuracy and interpretability, we recommend using reference parameters: 100 inner bags, 100 outer bags, 5000 epochs, and a learning rate of 0.01. To keep the individual terms additive, EBM pays an additional training cost, making it somewhat slower than similar methods. However, because making predictions involves simple additions and lookups inside of the feature functions f~j~, EBMs are one of the fastest models to execute at prediction time. EBM's light memory usage and fast predict times makes it particularly attractive for model deployment in production.
