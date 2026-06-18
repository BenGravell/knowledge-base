Consistent Individualized Feature Attribution for Tree Ensembles

Topics include Game theory.

Interpreting predictions from tree ensemble methods such as gradient boosting machines and random forests is important, yet feature attribution for trees is often heuristic and not individualized for each prediction. Here we show that popular feature attribution methods are inconsistent, meaning they can lower a feature's assigned importance when the true impact of that feature actually increases. This is a fundamental problem that casts doubt on any comparison between features. To address it we turn to recent applications of game theory and develop fast exact tree solutions for SHAP (SHapley Additive exPlanation) values, which are the unique consistent and locally accurate attribution values. We then extend SHAP values to interaction effects and define SHAP interaction values.

## Introduction

Understanding why a model made a prediction is important for trust, actionability, accountability, debugging, and many other tasks. To understand predictions from tree ensemble methods, such as gradient boosting machines or random forests, importance values are typically attributed to each input feature. These importance values can be computed either for a single prediction (individualized), or an entire dataset to explain a model's overall behavior (global).

Concerningly, popular current feature attribution methods for tree ensembles are inconsistent. This means that when a model is changed such that a feature has a higher impact on the model's output, current methods can actually lower the importance of that feature. Inconsistency strikes at the heart of what it means to be a good attribution method, because it prevents the meaningful comparison of attribution values across features. This is because inconsistency implies that a feature with a large attribution value might be less important than another feature with a smaller attribution (see Figure 1 and Section 2).

## Conclusion

Several common feature attribution methods for tree ensembles are inconsistent, meaning they can lower a feature's assigned importance when the true impact of that feature actually increases. This can prevent the meaningful comparison of feature attribution values. In contrast, SHAP values consistently attribute feature importance, better align with human intuition, and better recover influential features. By presenting the first polynomial time algorithm for SHAP values in tree ensembles, we make them a practical replacement for previous methods....

In Algorithm 2 time ‣ 3. Tree SHAP: Fast SHAP value computation for trees ‣ Consistent Individualized Feature Attribution for Tree Ensembles"), $m$ is the path of unique features we have split on so far, and contains four attributes: $d$ the feature index, $z$ the fraction of "zero" paths (where this feature is not in the set $S$) that flow through this branch, $o$ the fraction of "one" paths (where this feature is in the set $S$) that flow through this branch, and $w$ which is used to hold the proportion of sets of a given cardinality that are present....

To compute SHAP values we define ${f_{x}{(S)}} = {f{({h_{x}{(z^{\prime})}})}} = {E{\lbrack{{f{(x)}} \mid x_{S}}\rbrack}}$ where $S$ is the set of non-zero...
