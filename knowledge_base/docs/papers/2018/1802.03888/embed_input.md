<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Consistent Individualized Feature Attribution for Tree Ensembles

Topics include Game theory.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Interpreting predictions from tree ensemble methods such as gradient boosting machines and random forests is important, yet feature attribution for trees is often heuristic and not individualized for each prediction. Here we show that popular feature attribution methods are inconsistent, meaning they can lower a feature's assigned importance when the true impact of that feature actually increases. This is a fundamental problem that casts doubt on any comparison between features. To address it we turn to recent applications of game theory and develop fast exact tree solutions for SHAP (SHapley Additive exPlanation) values, which are the unique consistent and locally accurate attribution values. We then extend SHAP values to interaction effects and define SHAP interaction values.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Understanding why a model made a prediction is important for trust, actionability, accountability, debugging, and many other tasks. To understand predictions from tree ensemble methods, such as gradient boosting machines or random forests, importance values are typically attributed to each input feature. These importance values can be computed either for a single prediction (individualized), or an entire dataset to explain a model's overall behavior (global).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Concerningly, popular current feature attribution methods for tree ensembles are inconsistent. This means that when a model is changed such that a feature has a higher impact on the model's output, current methods can actually lower the importance of that feature. Inconsistency strikes at the heart of what it means to be a good attribution method, because it prevents the meaningful comparison of attribution values across features. This is because inconsistency implies that a feature with a large attribution value might be less important than another feature with a smaller attribution (see Figure 1 and Section 2).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To address this problem we turn to the recently proposed SHAP (SHapley Additive exPlanation) values, which are based on a unification of ideas from game theory and local explanations. Here we show that by connecting tree ensemble feature attribution methods with the class of additive feature attribution methods we can motivate SHAP values as the only possible consistent feature attribution method with several desirable properties.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

SHAP values are theoretically optimal, but like other model agnostic feature attribution methods, they can be challenging to compute. To solve this we derive an algorithm for tree ensembles that reduces the complexity of computing exact SHAP values from $O{({TL2^{M}})}$ to $O{({TLD^{2}})}$ where $T$ is the number of trees, $L$ is the maximum number of leaves in any tree, $M$ is the number of features, and $D$ is the maximum depth of any tree. This exponential reduction in complexity allows predictions from previously intractable models with thousands of trees and features to now be explained in a fraction of a second. Entire datasets can now be explained, which enables new alternatives to traditional partial dependence plots and feature importance plots, which we term SHAP dependence plots and SHAP summary plots, respectively.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Current attribution methods cannot directly represent interactions, but must divide the impact of an interaction among each feature. To directly capture pairwise interaction effects we propose SHAP interaction values; an extension of SHAP values based on the Shapley interaction index from game theory. SHAP interaction values bring the benefits of guaranteed consistency to explanations of interaction effects for individual predictions.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In what follows we first discuss current tree feature attribution methods and their inconsistencies. We then introduce SHAP values as the only possible consistent and locally accurate attributions, present Tree SHAP as a high speed algorithm for estimating SHAP values of tree ensembles, then extend this to SHAP interaction values. We use user study data, computational performance, influential feature identification, and supervised clustering to compare with previous methods. Finally, we illustrate SHAP dependence plots and SHAP summary plots with XGBoost and NHANES I national health study data.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Inconsistencies in current feature attribution methods", "weight": 1.0} -->

Tree ensemble implementations in popular packages such as XGBoost, scikit-learn, and the gbm R package allow a user to compute a measure of feature importance. These values are meant to summarize a complicated ensemble model and provide insight into what features drive the model's prediction.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Inconsistencies in current feature attribution methods", "weight": 1.0} -->

Global feature importance values are calculated for an entire dataset (i.e.,

<!-- chunk {"id": "body-0011", "role": "body", "section": "Inconsistencies in current feature attribution methods", "weight": 1.0} -->

Gain: A classic approach to feature importance introduced by Breiman et al. in 1984 is based on gain. Gain is the total reduction of loss or impurity contributed by all splits for a given feature. Though its motivation is largely heuristic, gain is widely used as the basis for feature selection methods.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Inconsistencies in current feature attribution methods", "weight": 1.0} -->

Split Count: A second common approach is simply to count how many times a feature is used to split. Since feature splits are chosen to be the most informative, this can represent a feature's importance.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Inconsistencies in current feature attribution methods", "weight": 1.0} -->

Permutation: A third common approach is to randomly permute the values of a feature in the test set and then observe the change in the model's error. If a feature's value is important then permuting it should create a large increase in the model's error. Different choices about the method of feature value permutation lead to variations of this basic approach.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Inconsistencies in current feature attribution methods", "weight": 1.0} -->

Individualized methods that compute feature importance values for a single prediction are less established for trees. While model agnostic individualized explanation methods can be applied to trees, they are significantly slower than tree-specific methods and have sampling variability (see Section 5.3 for a computational comparison, or for an overview). The only current tree-specific individualized explanation method we are aware of is by Sabbas. The Saabas method is similar to the classic dataset-level gain method, but instead of measuring the reduction of loss, it measures the change in the model's expected output. It proceeds by comparing the expected value of the model output at the root of the tree with the expected output of the sub-tree rooted at the child node followed by the decision path of the current input. The difference between these expectations is then attributed to the feature split on at the root node. By repeating this process recursively the method allocates the difference between the expected model output and the current output among the features on the decision path.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Inconsistencies in current feature attribution methods", "weight": 1.0} -->

*Unfortunately, the feature importance values from the gain, split count, and Saabas methods are all inconsistent.* This means that a model can change such that it relies more on a given feature, yet the importance estimate assigned to that feature decreases. Of the methods we consider, only SHAP values and permutation-based methods are consistent. Figure 1 shows the result of applying all these methods to two simple regression trees.^11^1For clarity we rounded small values in Figure 1. These small values are why the lower left splits in both models were not pruned during training. For the global calculations we assume an equal number of dataset points fall in each leaf, and the label of those points is exactly equal to the prediction of the leaf. Model A represents a simple AND function, while Model B represents the same AND function but with an additional increase in the predicted value when Cough is "Yes". Note that because Cough is now more important it gets split on first in Model B.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Inconsistencies in current feature attribution methods", "weight": 1.0} -->

Individualized feature attribution is represented by Tree SHAP and Sabbas for the input Fever=Yes and Cough=Yes. Both methods allocate the difference between the current model output and the expected model output among the input features ($80 - 20$ for Model A). But the SHAP values are guaranteed to reflect the importance of the feature (see Section 2.1), while the Saabas values can give erroneous results, such as a larger attribution to Fever than to Cough in Model B.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Inconsistencies in current feature attribution methods", "weight": 1.0} -->

Global feature attribution is represented by four methods: the mean magnitude of the SHAP values, gain, split count, and feature permutation. Only the mean SHAP value magnitude and permutation correctly give Cough more importance than Fever in Model B. This means gain and split count are not reliable measures of global feature importance, which is important to note given their widespread use.

<!-- chunk {"id": "body-0018", "role": "body", "section": "SHAP values as the only consistent and locally accurate individualized feature attributions", "weight": 1.0} -->

It was recently noted that many current methods for interpreting individual machine learning model predictions fall into the class of additive feature attribution methods. This class covers methods that explain a model's output as a sum of real values attributed to each input feature.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Tree SHAP: Fast SHAP value computation for trees", "weight": 1.0} -->

The challenge of estimating $E{\lbrack{{f{(x)}} \mid x_{S}}\rbrack}$ efficiently.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Tree SHAP: Fast SHAP value computation for trees", "weight": 1.0} -->

Here we focus on tree models and propose fast SHAP value estimation methods specific to trees and ensembles of trees. We start by defining a slow but straightforward algorithm, then present the much faster and more complex Tree SHAP algorithm.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Estimating SHAP values directly in $O{({TL2^{M}})}$ time", "weight": 1.0} -->

If we ignore computational complexity then we can compute the SHAP values for a tree by estimating $E{\lbrack{{f{(x)}} \mid x_{S}}\rbrack}$ and then using Equation 2 where ${f_{x}{(S)}} = {E{\lbrack{{f{(x)}} \mid x_{S}}\rbrack}}$. For a tree model $E{\lbrack{{f{(x)}} \mid x_{S}}\rbrack}$ can be estimated recursively using Algorithm 1 time ‣ 3. Tree SHAP: Fast SHAP value computation for trees ‣ Consistent Individualized Feature Attribution for Tree Ensembles"), where $v$ is a vector of node values, which takes the value $internal$ for internal nodes. The vectors $a$ and $b$ represent the left and right node indexes for each internal node. The vector $t$ contains the thresholds for each internal node, and $d$ is a vector of indexes of the features used for splitting in internal nodes.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Estimating SHAP values directly in $O{({TL2^{M}})}$ time", "weight": 1.0} -->

The vector $r$ represents the cover of each node (i.e., how many data samples fall in that sub-tree). The weight $w$ measures what proportion of the training samples matching the conditioning set $S$ fall into each leaf.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Estimating SHAP values directly in $O{({TL2^{M}})}$ time", "weight": 1.0} -->

return G(aj, w) if xdj ≤ tj else G(bj, w)
return G(aj, w raj/rj) + G(bj, w rbj/rj)

<!-- chunk {"id": "body-0024", "role": "body", "section": "Estimating SHAP values in $O{({TLD^{2}})}$ time", "weight": 1.0} -->

Here we propose a novel algorithm to calculate the same values as above, but in polynomial time instead of exponential time. Specifically, we propose an algorithm that runs in $O{({TLD^{2}})}$ time and $O{({D^{2} + M})}$ memory, where for balanced trees the depth becomes $D = {\log L}$. Recall $T$ is the number of trees, $L$ is the maximum number of leaves in any tree, and $M$ is the number of features.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Estimating SHAP values in $O{({TLD^{2}})}$ time", "weight": 1.0} -->

The intuition of the polynomial time algorithm is to recursively keep track of what proportion of all possible subsets flow down into each of the leaves of the tree. This is similar to running Algorithm 1 time ‣ 3. Tree SHAP: Fast SHAP value computation for trees ‣ Consistent Individualized Feature Attribution for Tree Ensembles") simultaneously for all $2^{M}$ subsets $S$ in Equation 2. It may seem reasonable to simply keep track of how many subsets (weighted by the cover splitting of Algorithm 1 time ‣ 3. Tree SHAP: Fast SHAP value computation for trees ‣ Consistent Individualized Feature Attribution for Tree Ensembles")) pass down each branch of the tree. However, this combines subsets of different sizes and so prevents the proper weighting of these subsets, since the weights in Equation 2 depend on $|S|$. To address this we keep track of each possible subset size during the recursion. The EXTEND method in Algorithm 2 time ‣ 3.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Estimating SHAP values in $O{({TLD^{2}})}$ time", "weight": 1.0} -->

Tree SHAP: Fast SHAP value computation for trees ‣ Consistent Individualized Feature Attribution for Tree Ensembles") grows all these subsets according to a given fraction of ones and zeros, while the UNWIND method reverses this process and is commutative with EXTEND. The EXTEND method is used as we descend the tree. The UNWIND method is used to undo previous extensions when we split on the same feature twice, and to undo each extension of the path inside a leaf to compute weights for each feature in the path.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Estimating SHAP values in $O{({TLD^{2}})}$ time", "weight": 1.0} -->

In Algorithm 2 time ‣ 3. Tree SHAP: Fast SHAP value computation for trees ‣ Consistent Individualized Feature Attribution for Tree Ensembles"), $m$ is the path of unique features we have split on so far, and contains four attributes: $d$ the feature index, $z$ the fraction of "zero" paths (where this feature is not in the set $S$) that flow through this branch, $o$ the fraction of "one" paths (where this feature is in the set $S$) that flow through this branch, and $w$ which is used to hold the proportion of sets of a given cardinality that are present. We use the dot notation to access these members, and for the whole vector $m.d$ represents a vector of all the feature indexes.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Estimating SHAP values in $O{({TLD^{2}})}$ time", "weight": 1.0} -->

Algorithm 2 time ‣ 3. Tree SHAP: Fast SHAP value computation for trees ‣ Consistent Individualized Feature Attribution for Tree Ensembles") reduces the computational complexity of exact SHAP value computation from exponential to low order polynomial for trees and sums of trees (since the SHAP values of a sum of two functions is the sum of the original functions' SHAP values).

<!-- chunk {"id": "body-0029", "role": "body", "section": "SHAP Interaction Values", "weight": 1.0} -->

Feature attributions are typically allocated among the input features, one for each feature, but we can gain additional insight by separating *interaction effects* from main effects. If we consider pairwise interactions this leads to a matrix of attribution values representing the impact of all pairs of features on a given model prediction.

<!-- chunk {"id": "body-0030", "role": "body", "section": "SHAP Interaction Values", "weight": 1.0} -->

In Equation 3 the SHAP interaction value between feature $i$ and feature $j$ is split equally between each feature so $\Phi_{i,j} = \Phi_{j,i}$ and the total interaction effect is $\Phi_{i,j} + \Phi_{j,i}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "SHAP Interaction Values", "weight": 1.0} -->

These SHAP interaction values follow from similar axioms as SHAP values, and allow the separate consideration of main and interaction effects for individual model predictions. This separation can uncover important interactions captured by tree ensembles that might otherwise be missed (Figure 10 in Section 5.5).

<!-- chunk {"id": "body-0032", "role": "body", "section": "SHAP Interaction Values", "weight": 1.0} -->

While SHAP interaction values can be computed directly from Equation 3, we can leverage Algorithm 2 time ‣ 3. Tree SHAP: Fast SHAP value computation for trees ‣ Consistent Individualized Feature Attribution for Tree Ensembles") to drastically reduce their computational cost for tree models. As highlighted in Equation 5 SHAP interaction values can be interpreted as the difference between the SHAP values for feature $i$ when feature $j$ is present and the SHAP values for feature $i$ when feature $j$ is absent. This allows us to use Algorithm 2 time ‣ 3. Tree SHAP: Fast SHAP value computation for trees ‣ Consistent Individualized Feature Attribution for Tree Ensembles") twice, once while ignoring feature $j$ as fixed to present, and once with feature $j$ absent. This leads to a run time of $O{({TMLD^{2}})}$, since we repeat the process for each feature. Note that even though this computational approach does not seem to directly enforce symmetry, the resulting $\Phi$ matrix is always symmetric.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments and Applications", "weight": 1.0} -->

We compare Tree SHAP and SHAP interaction values with previous methods through both traditional metrics and three new applications we propose for individualized feature attributions: supervised clustering, SHAP summary plots, and SHAP dependence plots.^22^2Jupyter notebooks to compute all results are available at

<!-- chunk {"id": "body-0034", "role": "body", "section": "Agreement with Human Intuition", "weight": 1.0} -->

To validate that the SHAP values in Model A of Figure 1 are the most natural assignment of credit we ran a user study to measure people's intuitive feature attribution values. Model A's tree was shown to participants and said to represent risk for a certain disease. They were told that when a given person was found to have both a cough and fever their risk went up from the prior risk of 20 (the expected value of risk) to a risk of 80. Participants were then asked to apportion the 60 point change in risk among the Cough and Fever features as they saw best.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Supervised Clustering", "weight": 1.0} -->

One intriguing application enabled by individualized feature attributions is what we term "supervised clustering," where instead of using an unsupervised clustering method directly on the data features, you run clustering on the feature attributions.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Supervised Clustering", "weight": 1.0} -->

Supervised clustering naturally handles one of the most challenging problems in unsupervised clustering: determining feature weightings (or equivalently, determining a distance metric). Many times we want to cluster data using features with very different units. Features may be in dollars, meters, unit-less scores, etc. but whenever we use them as dimensions in a single multidimensional space it forces any distance metric to compare the relative importance of a change in different units (such as dollars vs. meters). Even if all our inputs are in the same units, often some features are more important than others. Supervised clustering uses feature attributions to naturally convert all the input features into values with the same units as the model output. This means that a unit change in any of the feature attributions is comparable to a unit change in any other feature attribution. It also means that fluctuations in the feature values only effect the clustering if those fluctuations have an impact on the outcome of interest.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Supervised Clustering", "weight": 1.0} -->

Here we demonstrate the use of supervised clustering on the classic UCI census dataset. For this dataset the goal is to predict from basic demographic data if a person is likely to make more than \$50K annually. By representing the positive feature attributions as red bars and the negative feature attributions as blue bars (as in Figure 2), we can stack them against each other to visually represent the model output as their sum. Figure 4 does this vertically for predictions from 2,000 people from the census dataset. The explanations for each person are stacked horizontally according the leaf order of a hierarchical clustering of the SHAP values. This groups people with similar reasons for a predicted outcome together. The formation of distinct subgroups of people demonstrates the power of supervised clustering to identify groups that share common factors related to income level.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Supervised Clustering", "weight": 1.0} -->

One way to quantify the improvement provided by SHAP values over the heuristic Saabas attributions is by examining how well supervised clustering based on each method explains the variance of the model output (note global feature attributions are not considered since they do not enable this type of supervised clustering). If feature attribution values well-represent the model then supervised clustering groups will have similar function outputs. Since hierarchical clusterings encode many possible groupings, we plot in Figure 6 the change in the $R^{2}$ value as the number of groups shrinks from one group per sample ($R^{2} = 1$) to a single group ($R^{2} = 0$). For the census dataset, groupings based on SHAP values outperform those from Saabas values (Figure 6A). For a dataset based on cognitive scores for Alzheimer's disease SHAP values significantly outperform Saabas values (Figure 6B). This second dataset contains 200 gene expression module levels as features and CERAD cognitive scores as labels.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Identification of Influential Features", "weight": 1.0} -->

Feature attribution values are commonly used to identify which features influenced a model's prediction the most. To compare methods, the change in a model's prediction can be computed when the most influential feature is perturbed. Figure 7 shows the result of this experiment on a sentiment analysis model of airline tweets. An XGBoost model with 50 trees of maximum depth 30 was trained on 11,712 tweets with 1,686 bag-of-words features. Each tweet had a sentiment score label between -1 (negative) and 1 (positive). The predictions of the XGBoost model were then explained for 2,928 test tweets. For each method we choose the most influential negative feature and replaced it with the value of the same feature in another random tweet from the training set (this is designed to mimic the feature being unknown). The new input is then re-run through the model to produce an updated output. If the chosen feature significantly lowered the model output, then the updated model output should be higher than the original.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Identification of Influential Features", "weight": 1.0} -->

By tracking the total change in model output as we progress through the test tweets we observe that SHAP values best identify the most influential negative feature. Since global methods only select a single feature for the whole dataset we only replaced this feature when it would likely increase the sentiment score (for gain and permutation this meant randomly replacing the "thank" feature when it was missing, for split count it was the word "to").

<!-- chunk {"id": "body-0041", "role": "body", "section": "SHAP Plots", "weight": 1.0} -->

Plotting the impact of features in a tree ensemble model is typically done with a bar chart to represent global feature importance, or a partial dependence plot to represent the effect of changing a single feature. However, since SHAP values are individualized feature attributions, unique to every prediction, they enable new, richer visual representations. SHAP summary plots replace typical bar charts of global feature importance, and SHAP dependence plots provide an alternative to partial dependence plots that better capture interaction effects.

<!-- chunk {"id": "body-0042", "role": "body", "section": "SHAP Plots", "weight": 1.0} -->

To explore these visualizations we trained an XGBoost Cox proportional hazards model on survival data from the classic NHANES I dataset using the NHANES I Epidemiologic Followup Study. After selection for the presence of basic blood test data we obtained data for 9,932 individuals followed for up to 20 years after baseline data collection for mortality. Based on a 80/20 train/test split we chose to use 7,000 trees of maximum depth 3, $\eta = 0.001$, and $50\%$ instance sub-sampling. We then used these parameters and trained on all individuals to generate the final model.

<!-- chunk {"id": "body-0043", "role": "body", "section": "SHAP Summary Plots", "weight": 1.0} -->

Standard feature importance bar charts give a notion of relative importance in the training dataset, but they do not represent the range and distribution of impacts that feature has on the model's output, and how the feature's value relates to it's impact. SHAP summary plots leverage individualized feature attributions to convey all these aspects of a feature's importance while remaining visually concise (Figure 8). Features are first sorted by their global impact $\sum_{j = 1}^{N}{|\phi_{i}^{(j)}|}$, then dots representing the SHAP values $\phi_{i}^{(j)}$ are plotted horizontally, stacking vertically when they run out of space. This vertical stacking creates an effect similar to violin plots but without an arbitrary smoothing kernel width. Each dot is colored by the value of that feature, from low (blue) to high (red). If the impact of the feature on the model's output varies smoothly as its value changes then this coloring will also have a smooth gradation.

<!-- chunk {"id": "body-0044", "role": "body", "section": "SHAP Summary Plots", "weight": 1.0} -->

In Figure 8 we see (unsurprisingly) that age at baseline is the most important risk factor for death over the next 20 years. The density of the age plot shows how common different ages are in the dataset, and the coloring shows a smooth increase in the model's output (a log odds ratio) as age increases. In contrast to age, systolic blood pressure only has a large impact for a minority of people with high blood pressure. The general trend of long tails reaching to the right, but not to the left, means that extreme values of these measurements can significantly raise your risk of death, but cannot significantly lower your risk.

<!-- chunk {"id": "body-0045", "role": "body", "section": "SHAP Dependence Plots", "weight": 1.0} -->

As described in Equation 10.47 of Friedman et al., partial dependence plots represent the expected output of a model when the value of a specific variable (or group of variables) is fixed. The values of the fixed variables are varied and the resulting expected model output is plotted. Plotting how the expected output of a function changes as we change a feature helps explain how the model depends on that feature.

<!-- chunk {"id": "body-0046", "role": "body", "section": "SHAP Dependence Plots", "weight": 1.0} -->

SHAP values can be used to create a rich alternative to partial dependence plots, which we term SHAP dependence plots. SHAP dependence plots use the SHAP value of a feature for the y-axis and the value of the feature for the x-axis. By plotting these values for many individuals from the dataset we can see how the feature's attributed importance changes as its value varies (Figure 9). While standard partial dependence plots only produce lines, SHAP dependence plots capture vertical dispersion due to interaction effects in the model. These effects can be visualized by coloring each dot with the value of an interacting feature. In Figure 9 coloring by age shows that high blood pressure is more alarming when you are young. Presumably because it is both less surprising as you age, and possibly because it takes time for high blood pressure to lead to fatal complications.

<!-- chunk {"id": "body-0047", "role": "body", "section": "SHAP Dependence Plots", "weight": 1.0} -->

Combining SHAP dependence plots with SHAP interaction values can reveal global interaction patterns. Figure 10A plots the SHAP main effect value for systolic blood pressure. Since SHAP main effect values represents the impact of systolic blood pressure after all interaction effects have been removed (Equation 6), there is very little vertical dispersion in Figure 10A. Figure 10B shows the SHAP interaction value of systolic blood pressure and age. As suggested by the coloring in Figure 9, this interaction accounts for most of the vertical variance in the systolic blood pressure SHAP values.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Several common feature attribution methods for tree ensembles are inconsistent, meaning they can lower a feature's assigned importance when the true impact of that feature actually increases. This can prevent the meaningful comparison of feature attribution values. In contrast, SHAP values consistently attribute feature importance, better align with human intuition, and better recover influential features. By presenting the first polynomial time algorithm for SHAP values in tree ensembles, we make them a practical replacement for previous methods. We further defined SHAP interaction values as a consistent way of measuring potentially hidden pairwise interaction relationships. Tree SHAP's exponential speed improvements open up new practical opportunities, such as supervised clustering, SHAP summary plots, and SHAP dependence plots, that advance our understanding of tree models.
