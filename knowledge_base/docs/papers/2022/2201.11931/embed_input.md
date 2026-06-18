Fast Interpretable Greedy-Tree Sums

Topics include Interpretable machine learning, Decision trees, Tree ensembles, Additive models, Greedy algorithms, Clinical decision instruments, Bagging, Model interpretability.

Introduces FIGS, an interpretable model class that greedily builds a sum of decision trees rather than a single tree or opaque ensemble. The method keeps rule-level readability while capturing additive structure, and the paper connects this behavior to disentanglement properties of additive target functions.

Modern machine learning has achieved impressive prediction performance, but often sacrifices interpretability, a critical consideration in high-stakes domains such as medicine. In such settings, practitioners often use highly interpretable decision tree models, but these suffer from inductive bias against additive structure. To overcome this bias, we propose Fast Interpretable Greedy-Tree Sums (FIGS), which generalizes the CART algorithm to simultaneously grow a flexible number of trees in summation. By combining logical rules with addition, FIGS is able to adapt to additive structure while remaining highly interpretable. Extensive experiments on real-world datasets show that FIGS achieves state-of-the-art prediction performance. To demonstrate the usefulness of FIGS in high-stakes domains, we adapt FIGS to learn clinical decision instruments (CDIs), which are tools for guiding clinical decision-making. Specifically, we introduce a variant of FIGS known as G-FIGS that accounts for the heterogeneity in medical data. G-FIGS derives CDIs that reflect domain knowledge and enjoy improved specificity (by up to 20% over CART) without sacrificing sensitivity or interpretability.

## Introduction

Modern machine learning methods such as random forests, gradient boosting, and deep learning display impressive predictive performance, but are complex and opaque, leading many to call them "black-box" models. Model interpretability is critical in many applications, particularly in high-stakes settings such as clinical decision instrument (CDI) modeling. Interpretability allows models to be audited for general validation, errors, or biases, and therefore also more amenable to improvement by domain experts.

To address these weaknesses of decision trees, we propose Fast Interpretable Greedy-Tree Sums (FIGS), a novel yet natural algorithm that is able to *grow a flexible number of trees simultaneously*. FIGS is based on a simple yet effective modification to Classification and Regression Trees (CART), allowing it to adapt to additive structure (if present) by starting new trees, while still maintaining the ability of CART to adapt to higher-order interaction terms. By capping the total number of splits allowed, FIGS produces a model that is also easily visualized, memorized, and emulated by hand.

We performed extensive experiments across a wide array of real-world datasets to compare the predictive performance of FIGS to a number of popular decision rule models. Specifically, we took the number of rules (splits in the case of trees) as a common measure of interpretability for this model class, and constructed decision rule models at a prescribed level of interpretability. Our results show that FIGS often achieved the best predictive performance across various levels of interpretability (i.e., number of splits).

## Discussion

FIGS is a powerful and natural extension to CART which achieves improved predictive performance over popular baseline tree-based methods across a wide array of datasets while maintaining interpretability by using very few splits. Furthermore, when the number of splits is unconstrained, an ensemble version of FIGS has prediction performance that compares favorably to random forest and XGBoost.
