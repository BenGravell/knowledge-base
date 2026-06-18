Greedy Function Approximation: A Gradient Boosting Machine

Topics include Gradient boosting, Ensemble methods, Decision trees, Boosting, Function approximation, TreeBoost, Machine learning.

Derives gradient boosted trees from first principles as steepest-descent optimization in function space, unifying boosting with numerical optimization. Introduces the TreeBoost algorithm and specific gradient update rules for regression and classification, forming the basis for XGBoost, LightGBM, CatBoost, and all modern gradient boosting libraries.

Function estimation/approximation is viewed from the perspective of numerical optimization in function space, rather than parameter space. A connection is made between stagewise additive expansions and steepest-descent minimization. A general gradient descent "boosting" paradigm is developed for additive expansions based on any fitting criterion. Specific algorithms are presented for least-squares, least absolute deviation, and Huber-M loss functions for regression, and multiclass logistic likelihood for classification. Special enhancements are derived for the particular case where the individual additive components are regression trees, and tools for interpreting such "TreeBoost" models are presented.
