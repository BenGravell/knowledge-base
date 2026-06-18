Consistent Individualized Feature Attribution for Tree Ensembles

Topics include Game theory.

Interpreting predictions from tree ensemble methods such as gradient boosting machines and random forests is important, yet feature attribution for trees is often heuristic and not individualized for each prediction. Here we show that popular feature attribution methods are inconsistent, meaning they can lower a feature's assigned importance when the true impact of that feature actually increases. This is a fundamental problem that casts doubt on any comparison between features. To address it we turn to recent applications of game theory and develop fast exact tree solutions for SHAP (SHapley Additive exPlanation) values, which are the unique consistent and locally accurate attribution values. We then extend SHAP values to interaction effects and define SHAP interaction values.

## Introduction

Understanding why a model made a prediction is important for trust, actionability, accountability, debugging, and many other tasks. To understand predictions from tree ensemble methods, such as gradient boosting machines or random forests, importance values are typically attributed to each input feature. These importance values can be computed either for a single prediction (individualized), or an entire dataset to explain a model's overall behavior (global).

To address this problem we turn to the recently proposed SHAP (SHapley Additive exPlanation) values, which are based on a unification of ideas from game theory and local explanations. Here we show that by connecting tree ensemble feature attribution methods with the class of additive feature attribution methods we can motivate SHAP values as the only possible consistent feature attribution method with several desirable properties.

Current attribution methods cannot directly represent interactions, but must divide the impact of an interaction among each feature. To directly capture pairwise interaction effects we propose SHAP interaction values; an extension of SHAP values based on the Shapley interaction index from game theory. SHAP interaction values bring the benefits of guaranteed consistency to explanations of interaction effects for individual predictions.

## Conclusion

Several common feature attribution methods for tree ensembles are inconsistent, meaning they can lower a feature's assigned importance when the true impact of that feature actually increases. This can prevent the meaningful comparison of feature attribution values. In contrast, SHAP values consistently attribute feature importance, better align with human intuition, and better recover influential features. By presenting the first polynomial time algorithm for SHAP values in tree ensembles, we make them a practical replacement for previous methods.
