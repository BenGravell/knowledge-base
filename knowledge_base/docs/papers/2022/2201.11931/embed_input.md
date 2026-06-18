Fast Interpretable Greedy-Tree Sums

Topics include Interpretable machine learning, Decision trees, Tree ensembles, Additive models, Greedy algorithms, Clinical decision instruments, Bagging, Model interpretability.

Introduces FIGS, an interpretable model class that greedily builds a sum of decision trees rather than a single tree or opaque ensemble. The method keeps rule-level readability while capturing additive structure, and the paper connects this behavior to disentanglement properties of additive target functions.

Modern machine learning has achieved impressive prediction performance, but often sacrifices interpretability, a critical consideration in high-stakes domains such as medicine. In such settings, practitioners often use highly interpretable decision tree models, but these suffer from inductive bias against additive structure. To overcome this bias, we propose Fast Interpretable Greedy-Tree Sums (FIGS), which generalizes the CART algorithm to simultaneously grow a flexible number of trees in summation. By combining logical rules with addition, FIGS is able to adapt to additive structure while remaining highly interpretable. Extensive experiments on real-world datasets show that FIGS achieves state-of-the-art prediction performance. To demonstrate the usefulness of FIGS in high-stakes domains, we adapt FIGS to learn clinical decision instruments (CDIs), which are tools for guiding clinical decision-making. Specifically, we introduce a variant of FIGS known as G-FIGS that accounts for the heterogeneity in medical data. G-FIGS derives CDIs that reflect domain knowledge and enjoy improved specificity (by up to 20% over CART) without sacrificing sensitivity or interpretability....

## Introduction

Modern machine learning methods such as random forests, gradient boosting, and deep learning display impressive predictive performance, but are complex and opaque, leading many to call them "black-box" models. Model interpretability is critical in many applications, particularly in high-stakes settings such as clinical decision instrument (CDI) modeling. Interpretability allows models to be audited for general validation, errors, or biases, and therefore also more amenable to improvement by domain experts....

Decision trees are a prime example of interpretable models. They can be easily visualized, memorized, and emulated by hand, even by non-experts, and thus fit naturally into high-stakes use-cases, such as decision-making in medicine (e.g., the emergency department^22^2For example, in the popular tool mdcalc, over 90% of available CDIs take the form of a decision tree.), law, and public policy. While decision trees have the potential to adapt to complex data, they are often outperformed by black-box models in terms of prediction performance....

The class of FIGS models could be further extended to include linear terms or allow for summations of trees to be present at split nodes, rather than just at the root.

We hope FIGS and G-FIGS can pave the way towards more transparent and interpretable modeling that can improve machine-learning practice, particularly in high-stakes domains such as medicine, law, and policy making.

As before, we assume a supervised learning setting with features $X$, outcome $Y$, and a group label $G$ (e.g., treatment site or age group). G-FIGS is a two-step algorithm: (i) For a given group label $g$, G-FIGS first estimates group membership probabilities for each sample (e.g., by fitting a logistic regression model to predict group-membership)^77^7This is methodologically analogous to a propensity score in the causal inference literature. That is, it estimates ${\mathbb{P}}{({G = \left. g \middle| X \right.})}$. (ii) For a given group $g$, G-FIGS then uses the group probabilities ${\mathbb{P}}{({G = \left....

## FIGS results on real-world benchmark datasets

### G-FIGS disentangles clinical risk factors

Our starting point is the observation that *decision trees can be statistically inefficient at fitting regression functions with additive components*....
