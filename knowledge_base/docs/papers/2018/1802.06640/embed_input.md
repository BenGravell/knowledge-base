Finding Influential Training Samples for Gradient Boosted Decision Trees

Topics include Computational complexity, RF, Gradient boosting, GBDT, Decision trees, Random forest.

We address the problem of finding influential training samples for a particular case of tree ensemble-based models, e.g., Random Forest (RF) or Gradient Boosted Decision Trees (GBDT). A natural way of formalizing this problem is studying how the model's predictions change upon leave-one-out retraining, leaving out each individual training sample. Recent work has shown that, for parametric models, this analysis can be conducted in a computationally efficient way. We propose several ways of extending this framework to non-parametric GBDT ensembles under the assumption that tree structures remain fixed. Furthermore, we introduce a general scheme of obtaining further approximations to our method that balance the trade-off between performance and computational complexity. We evaluate our approaches on various experimental setups and use-case scenarios and demonstrate both the quality of our approach to finding influential training samples in comparison to the baselines and its computational efficiency.

## Introduction and Background

As machine learning-based models become more widespread and grow in both scale and complexity, methods of interpreting their predictions are increasingly attracting attention from the machine learning community. Some of the applications and benefits of employing these methods outlined in previous work include "debugging" the model to expose ways of model failures not discoverable via conventional test set performance measuring (e.g., data or target leakages); boosting developer's trust in the model's performance in scenarios when on-line evaluation is not available before deployment; and increasing user satisfaction and/or confidence in...

A common trait shared by the majority of these methods is that they treat the provided model as a *fixed* function of input objects and study which features had the largest effect on the prediction, how the model responds to feature perturbations, etc. However useful they are, the obtained interpretations do not provide a way of automatically *improving* the model, since the model is fixed; the main use-case thus becomes manual analytics by the user or the developer, which is both time and resource-consuming....

## Conclusion

In this work, we addressed the problem of finding train objects that exerted the largest influence on the GBDT's prediction on a particular test object. Building on the Influence Function framework for parametric models, we derived LeafRefit and LeafInfluence, methods for estimating influences based on their respective proxy metrics, Proxies [1 and 2. By utilizing the structure of tree ensembles, we also derived computationally efficient approximations to these methods, FastLeafRefit and FastLeafInfluence....

### Proof

### Selecting the update set

RQ2. Do smaller update sets significantly reduce the runtimes of FastLeafRefit and FastLeafInfluence? Does FastLeafInfluence yield a notable runtime speedup over FastLeafRefit?

One such framework has recently been introduced by Koh & Liang; it deals with finding the most influential training objects. They formalize the notion of "influence" via an infinitesimal approximation to leave-one-out retraining: the core question that this work aims to answer is "how would the model's performance on a test object $\mathbf{x}_{test}$ change if the weight of a training object $\mathbf{x}_{train}$ is perturbed?" Assuming a...
