<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Finding Influential Training Samples for Gradient Boosted Decision Trees

Topics include Computational complexity, RF, Gradient boosting, GBDT, Decision trees, Random forest.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We address the problem of finding influential training samples for a particular case of tree ensemble-based models, e.g., Random Forest (RF) or Gradient Boosted Decision Trees (GBDT). A natural way of formalizing this problem is studying how the model's predictions change upon leave-one-out retraining, leaving out each individual training sample. Recent work has shown that, for parametric models, this analysis can be conducted in a computationally efficient way. We propose several ways of extending this framework to non-parametric GBDT ensembles under the assumption that tree structures remain fixed. Furthermore, we introduce a general scheme of obtaining further approximations to our method that balance the trade-off between performance and computational complexity. We evaluate our approaches on various experimental setups and use-case scenarios and demonstrate both the quality of our approach to finding influential training samples in comparison to the baselines and its computational efficiency.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction and Background", "weight": 1.5} -->

As machine learning-based models become more widespread and grow in both scale and complexity, methods of interpreting their predictions are increasingly attracting attention from the machine learning community. Some of the applications and benefits of employing these methods outlined in previous work include "debugging" the model to expose ways of model failures not discoverable via conventional test set performance measuring (e.g., data or target leakages); boosting developer's trust in the model's performance in scenarios when on-line evaluation is not available before deployment; and increasing user satisfaction and/or confidence in provided predictions, etc. Various problem setups and interpretation methods, both model-agnostic and model-specific, have recently been proposed in the literature.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction and Background", "weight": 1.5} -->

A common trait shared by the majority of these methods is that they treat the provided model as a *fixed* function of input objects and study which features had the largest effect on the prediction, how the model responds to feature perturbations, etc. However useful they are, the obtained interpretations do not provide a way of automatically *improving* the model, since the model is fixed; the main use-case thus becomes manual analytics by the user or the developer, which is both time and resource-consuming. It is thus desirable to derive a framework for obtaining *actionable* insights into the model's behavior allowing us to automatically improve a model's performance.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction and Background", "weight": 1.5} -->

One such framework has recently been introduced by Koh & Liang; it deals with finding the most influential training objects. They formalize the notion of "influence" via an infinitesimal approximation to leave-one-out retraining: the core question that this work aims to answer is "how would the model's performance on a test object $\mathbf{x}_{test}$ change if the weight of a training object $\mathbf{x}_{train}$ is perturbed?" Assuming a smooth parametric model family (e.g., linear models or neural networks), the authors employ the Influence Functions framework from classical statistics to show that this quantity can be estimated much faster than via straightforward model retraining, which makes their method tractable in a real-world scenario. A natural use-case of such a framework is to consider individual test objects (or groups of them) on which the model performs poorly and either remove the most "harmful" training objects or prioritize a batch of new objects for labeling based on which ones are expected to be the most "helpful," akin to active learning.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction and Background", "weight": 1.5} -->

Unfortunately, the method suggested by Koh & Liang heavily relies on the smooth parametric nature of the model family. While this is a large class of machine learning models, it is by far not the only one. In particular, decision tree ensembles such as Random Forests and Gradient Boosted Decision Trees are probably the most widely used model family in industry, largely due to their state-of-the-art performance on structured and/or multimodal data. Thus, it is important to extend the aforementioned Influence Functions framework to tree ensembles.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction and Background", "weight": 1.5} -->

In this paper, we propose a way of doing so, while focusing specifically on GBDT. We consider two *proxy* metrics for the informal notion of influence. For the first one, leave-one-out retraining, we utilize the inner mechanics of fitting decision trees (in particular, assuming that a small training sample perturbation does not change the trees' structures) to derive LeafRefit and FastLeafRefit, a well-founded family of approximations to leave-one-out retraining that trade off approximation accuracy for computational complexity. For the second, analogously to the Influence Functions framework, we consider infinitesimal training sample weight perturbations and derive LeafInfluence and FastLeafInfluence, methods for estimating gradients of the model's predictions with respect to training objects' weights. From a theoretical perspective, LeafInfluence and FastLeafInfluence allow us to deal with the discontinuous dependency of tree structure on training sample perturbations; from a practical one, they allow us to further reduce computational complexity due to the possibility of precomputing certain derivatives.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction and Background", "weight": 1.5} -->

In our experiments we study the conditions under which our methods, FastLeafRefit and FastLeafInfluence, successfully approximate their proxy metrics, demonstrate our methods' ability to target training objects which are influential for specific test objects, and show that our algorithms run much faster than straightforward retraining, which makes them applicable in practical scenarios.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction and Background", "weight": 1.5} -->

Training points belonging to leaf l at step t

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction and Background", "weight": 1.5} -->

Glt (At − 1):= ∑j ∈ Iltwj gjt (Ajt − 1)
Sum of leaf derivatives

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction and Background", "weight": 1.5} -->

HH; lt (At − 1):= ∑j ∈ Iltwj hjt (Ajt − 1)
Sum of leaf second derivatives

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

First, we formally define the problem setup. We consider standard supervised training of a GBDT ensemble^22^2Mathematical notations are defined in Table 1. ${F{(x;\mathbf{w})}}:={\sum_{t = 1}^{T}{f_{P{(x)}_{t}}^{t}{(\mathbf{A}^{\mathbf{t} - \mathbf{1}})}}}$ on a training sample $\mathbf{X}_{train}$. Learning consists of two separate stages: *model structure selection* and *picking the optimal leaf values*. The way of choosing the model structure is not important for our work; we refer the interested reader to existing implementations, e.g., Chen & Guestrin; Dorogush et al..

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

This is equivalent to minimizing the empirical loss function w.r.t. the current leaf value by doing a single gradient step in function space.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

This is equivalent to minimizing the empirical loss function w.r.t. the current leaf value by doing a single Newton step in function space.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Approach", "weight": 1.0} -->

In this section, we describe our approach to efficiently calculating the influence of training points. Since the notion of "influence" is not rigorously defined and partly intuitive, we need to introduce a well-defined, measurable quantity that aims to capture the desired intuition; we refer to it as a *proxy* for influence. In this work, we follow the general framework of Koh & Liang and quantify influence through train set perturbations. We consider two proxies that reflect two natural variations of this approach. First, we describe an algorithm for faster exact leave-one-out retraining of GBDT under the assumption that the model structure remains fixed, and explain how to use that framework for estimating the influence of training points on specific test samples; we then introduce a general approach to obtaining approximations to this scheme for increased computational efficiency. Finally, we derive an iterative algorithm to compute gradients of GBDT predictions w.r.t. the weights of training sample and analyze the resulting expressions.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Proxy 1", "weight": 1.0} -->

Since, in order to rank the training points according to ${Inf}_{grad}{(\mathbf{x}_{train},\mathbf{x}_{test})}$, we would have to compute Proxy 1 for each $\mathbf{x}_{train}$, straightforward leave-one-out retraining would be prohibitively expensive even for moderately-sized datasets. Moreover, as mentioned in Section 1, the parametric model framework of Koh & Liang is not directly applicable here. Thus, a solution tailored specifically for tree ensembles is required.

<!-- chunk {"id": "body-0017", "role": "body", "section": "LeafRefit", "weight": 1.0} -->

In the problem definition (Section 2) we noted that training each tree requires picking its structure and leaf values. Moreover, these two operations respond to small training set perturbations differently: the tree structure is piecewise constant (i.e., it either stays the same or changes abruptly), whereas leaf values change more smoothly.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The effect of removing a single training point can be estimated while treating each tree's structure as fixed.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Under Assumption 1, it is thus sufficient to estimate how the leaf values of each tree are going to change. Since selecting optimal feature splits, e.g. via CART or C4.5 algorithms, is often the computational bottleneck in fitting decision trees, this observation already yields a significant complexity reduction.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Thus, our first algorithm for approximate leave-one-out retraining, LeafRefit, is equivalent to fixing the structure of every tree and fitting leaf values without the removed point. A formal listing of the resulting algorithm is given in Algorithm 1.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

1: Input: training point index to remove i0, sample-to-leaf assignments {Ilt}t = 1, l = 1T, L, leaf formula type formula
2: Output: new leaf values {f̂lt}t = 1, l = 1T, L
8: if formula = = Gradient then

<!-- chunk {"id": "body-0022", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Note that the effect of removing a training object $\mathbf{x}_{i}$ is twofold: on each step, we have to remove $\mathbf{x}_{i}$ from its leaf (Algorithm 1, line 7) and recalculate the leaf values and record the resulting changes of intermediate predictions for each training object (line 14). Thus, despite improving upon straightforward retraining by not having to search for the optimal tree splits, LeafRefit is still an expensive algorithm. Running it for each training sample has an asymptotic complexity of $O{({Tn^{2}})}$; moreover, in practice, for each training step $t$ it involves an expensive routine of recalculating derivatives for each training point.

<!-- chunk {"id": "body-0023", "role": "body", "section": "FastLeafRefit", "weight": 1.0} -->

We seek to limit the number of calculations at each step of LeafRefit. Note that, in LeafRefit, we generally cannot make any use of caching the original first and/or second derivatives, since any $\Delta_{i}^{t - 1}$ (Algorithm 1, line 14) can be nonzero, which forces us to recompute the derivatives for each object. We build on the intuition that, in practice, a lot of $\Delta_{i}^{t - 1}$ may be negligible; an extreme example is when training samples can be separated in disjoint cliques, i.e., ${I_{l}^{t_{1}} = {I_{l}^{t_{2}}{\forall t_{1}}}},{t_{2} = {1,\ldots,T}}$, $l = {1\ldotsL}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "FastLeafRefit", "weight": 1.0} -->

In this case, removing each training point only affects its clique $I_{l_{0}}:=I_{l_{0}}^{1}$, since objects not sharing leaves with $i$ will not be affected: ${\Delta_{i}^{t - 1} = {0{\forall t}} = {1\ldotsT}},{i \notin I_{l_{0}}}$. Thus, at each training step $t$, we may select a subset of training samples^33^3Methods of selecting $U^{t}$ will be given below. $U^{t}$ whose deltas we take into account, and suppose ${\hat{A}}_{i}^{t - 1} = {A_{i}^{t - 1}{\forall i}} \notin U^{t}$. We refer to $U^{t}$ as the *update set*.

<!-- chunk {"id": "body-0025", "role": "body", "section": "FastLeafRefit", "weight": 1.0} -->

Combining this with caching the original $A_{i}^{t - 1}$ and sums of derivatives in each leaf, we reduce the asymptotic complexity to $O{({TnC})}$, where $C = {\max_{t}{|U^{t}|}}$, which is a significant reduction if $C \ll n$. A formal listing of the resulting algorithm, FastLeafRefit, is given in Algorithm 2.

<!-- chunk {"id": "body-0026", "role": "body", "section": "FastLeafRefit", "weight": 1.0} -->

Input: boosting step t, leaf index l, {Ilt}t = 1, l = 1T, L, {git (Ait − 1)}t = 1, i = 1T, n, {hit (Ait − 1)}t = 1, i = 1T, n, Glt (At − 1), Hlt (At − 1), Ult, leaf formula type f o r m u l a Output: New leaf value f̂lt Δ gjt ← gjt (Ajt − 1+Δjt − 1) − gjt (Ajt − 1), j ∈ Ult Ĝlt ← Glt (At − 1) + ∑j ∈ Ultwj Δ gjt − I wi0 gi0t (Ai0t − 1) if formula = = Gradient then Δ hjt ← hjt (Ajt − 1+Δjt − 1) − hjt (Ajt − 1), j ∈ Ult Ĥlt ← Hlt (At − 1) + ∑j ∈ Ultwj Δ hjt − I wi0 hi0t (Ai0t − 1) return $-

<!-- chunk {"id": "body-0027", "role": "body", "section": "Selecting the update set", "weight": 1.0} -->

In Section 3.1.2, we introduced FastLeafRefit, an approximate algorithm potentially achieving lower complexity than LeafRefit. Its definition, however, allowed for an arbitrary choice of the *update set* $U^{t}$ telling us which training points' prediction changes to take into account at boosting step $t$. It is intuitively clear that different strategies of selecting $U^{t}$ allow us to optimize the trade-off between computational complexity and quality of approximating leave-one-out retraining; thus, FastLeafRefit provides a principled way of obtaining approximations of different rigor to LeafRefit.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Selecting the update set", "weight": 1.0} -->

SinglePoint: don't update any points' predictions and only ignore the derivatives of $i$ (the index of the training point to be removed) in each leaf, i.e., $U^{t} = \varnothing$. Also note that this strategy is equivalent to disregarding dependencies between consecutive trees in GBDT and treating the ensemble like a Random Forest. Its complexity is $O{({Tn})}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Selecting the update set", "weight": 1.0} -->

AllPoints: make no approximations and update each point at each step, i.e., $U^{t} = {\{ 1,\ldots,{|\mathbf{X}_{train}|}\}}$. This reduces FastLeafRefit to LeafRefit.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Selecting the update set", "weight": 1.0} -->

TopKLeaves(k): this heuristic builds on the observation that, at each step $t$, each ${\Delta_{j}^{t},j} \in I_{l}^{t}$ increases over $\Delta_{j}^{t - 1}$ by the same amount $\Deltaf_{l}^{t}$ across the leaf $l$ (see Algorithm 2). $\Deltaf_{l}^{t}$'s magnitude, in turn, is expected to be larger for leaves where ${\Delta_{j}^{t - 1},j} \in I_{l}^{t}$ (and, subsequently, $\Deltag_{j}^{t}$) are already large. Informally, the "snowball" effect holds: the larger the change accumulated in the leaf so far, the greater its value will change.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Selecting the update set", "weight": 1.0} -->

Note: despite the speedup from omitting unimportant leaves, this strategy is formally still $O{({Tn^{2}})}$ due to the fact that computing $U^{t}$ according to Eq. 3 takes $O{(n)}$. In practice, overhead for computing Eq. 3 may be negligible because, firstly, sums of $\Delta_{i}^{t - 1}$ can be quickly computed in a parallel or vectorized fashion and, secondly, because the complexity of addition is negligible compared to, e.g., calculating derivatives. However, if this still poses a problem, a natural way of getting around it is sampling $m$ training points uniformly from $\mathbf{X}_{train}$ and using a sample estimator of Eq. 3. The complexity of FastLeafRefit thus becomes $O{({Tn{\lbrack{C + m}\rbrack}})}$, which is useful if $m \ll n$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Prediction gradients", "weight": 1.0} -->

In the previous sections we introduced LeafRefit and FastLeafRefit, fast methods of estimating the effect of a training sample on the GBDT ensemble, which can then be used to rank training points, e.g., by their influence on a test point of interest. Under Assumption 1, these methods are valid approximations of leave-one-out retraining, which gives them theoretical grounding. However, as shown in Section 4.3, when Assumption 1 is violated, LeafRefit and FastLeafRefit are no longer valid approximations to Proxy 1.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Prediction gradients", "weight": 1.0} -->

The intuition underlying Assumption 1, however, still holds: for a small enough perturbation to the training data, the structure will remain fixed, whereas leaf values will still be changing smoothly. Note that retraining the model without a sample $i$ is equivalent to setting ${w_{i}^{new} = {w_{i}^{old} + {\Deltaw_{i}}}};{{\Deltaw_{i}} = {- w_{i}^{old}}}$. This change may be large enough to trigger structural shifts in the ensemble; thus, we need a tool to study a model's response to smaller (arbitrarily small) perturbations.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Prediction gradients", "weight": 1.0} -->

An obvious choice for such a tool is the derivative of a model's prediction w.r.t.

<!-- chunk {"id": "body-0035", "role": "body", "section": "LeafInfluence", "weight": 1.0} -->

As mentioned above, in the setup of Proxy 2 the statement of Assumption 1 is now guaranteed to hold and is no longer an assumption; we may consider the tree structures to be fixed and only study perturbations of leaf values, which smoothly depend on the weights. Using the chain rule

<!-- chunk {"id": "body-0036", "role": "body", "section": "LeafInfluence", "weight": 1.0} -->

we can then derive various counterfactuals (e.g., "how would the loss on a test point change if we upweight a training point $i$?"), similarly to Koh & Liang. Since we have

<!-- chunk {"id": "body-0037", "role": "body", "section": "LeafInfluence", "weight": 1.0} -->

Expressions for leaf value derivatives depend on the type of leaf formula:^44^4In Proposition 1's statement, arguments such as $\mathbf{w}$ or $A_{i}^{t}$ are dropped for brevity.

<!-- chunk {"id": "body-0038", "role": "body", "section": "FastLeafInfluence", "weight": 1.0} -->

The final step to be made is analogous to the transition from LeafRefit to FastLeafRefit: LeafInfluence is, again, $O{({Tn^{2}})}$ because it has to compute matrix/vector products with the matrix $J{(\mathbf{A}^{\mathbf{t} - \mathbf{1}})}_{ij}$ for every $t$. The same approximation that powers FastLeafRefit can be made here as well: at each step, we can select an update set $U^{t}$ and only take into account the influences of a subset of training objects on $\mathbf{A}^{\mathbf{t} - \mathbf{1}}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "FastLeafInfluence", "weight": 1.0} -->

This is equivalent to assuming ${J{(\mathbf{A}^{\mathbf{t} - \mathbf{1}})}_{ij}} = {0{\forall j}} \notin U^{t}$, making $J{(\mathbf{A}^{\mathbf{t} - \mathbf{1}})}_{ij}$ a sparse matrix with the number of nonzero elements in each row bounded by $C:={\max_{t}{|U^{t}|}}$. Strategies of selecting $U^{t}$ and the resulting asymptotics become the same as described in Section 3.1.3, with the additional benefit of being able to compute the derivatives "off-line."

<!-- chunk {"id": "body-0040", "role": "body", "section": "Research Questions", "weight": 1.0} -->

The experiments that we conduct can be broadly categorized as serving two purposes: studying the fundamentals of our framework and evaluating its quality in two applied problem setups.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Research Questions", "weight": 1.0} -->

RQ1. How well do the different methods introduced in Sections 3.1 and 3.2 approximate their respective influence proxies?

<!-- chunk {"id": "body-0042", "role": "body", "section": "Research Questions", "weight": 1.0} -->

RQ2. Do smaller update sets significantly reduce the runtimes of FastLeafRefit and FastLeafInfluence? Does FastLeafInfluence yield a notable runtime speedup over FastLeafRefit?

<!-- chunk {"id": "body-0043", "role": "body", "section": "Research Questions", "weight": 1.0} -->

For the second part, we proceed by considering two applied scenarios: classification in the presence of label noise, and classification with train/test domain mismatch.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Research Questions", "weight": 1.0} -->

RQ3. For Scenario 1, do our methods allow to detect noise in general and, more specifically, to identify training objects most harmful for specific test points?

<!-- chunk {"id": "body-0045", "role": "body", "section": "Research Questions", "weight": 1.0} -->

RQ4. For Scenario 1, how do the proxies and their respective approximations compare in terms of quality?

<!-- chunk {"id": "body-0046", "role": "body", "section": "Research Questions", "weight": 1.0} -->

RQ5. For Scenario 2, are our methods capable of detecting domain mismatch and, moreover, providing recommendations on how to fix it?

<!-- chunk {"id": "body-0047", "role": "body", "section": "Datasets and Framework", "weight": 1.0} -->

For our experiments with GBDT, we use CatBoost an open-source implementation of GBDT by Yandex^66^6We use the "Plain" mode which disables CatBoost's conceptual modifications to the standard GBDT scheme.. The datasets used for evaluation are: Adult Data Set (Adult, ), Amazon Employee Access Challenge dataset (Amazon, ), the KDD Cup 2009 Upselling dataset (Upselling, ) and, for the domain mismatch experiment, the Hospital Readmission dataset. Dataset statistics and corresponding CatBoost parameters can be found in the supplementary material. Since we approach the problem as a search (for influential examples) problem, the main metrics we will be using are ranking metrics - specifically, DCG and NDCG with linear gains.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Proxy Approximation Quality", "weight": 1.0} -->

Here, we evaluate how well do variations of FastLeafRefit and FastLeafInfluence match their respective Proxies 1 and 2. For that, we use the Adult Data Set. For LeafRefit, its validity heavily depends on whether Assumption 1 holds; thus, we split the training points into two disjoint sets based on whether they violate Assumption 1 (*Changed* in Table 2) or not. We then randomly sample $n = 2000$ points from both groups to ensure that they are equal in size and, in both of them, for each test object, we rank the train points with respect to their influence on this test object. We then measure NDCG@100 with respect to the relevance labels produced by ground-truth rankings induced by the respective proxies for LeafRefit and FastLeafRefit, Proxy 1 and Proxy 2. Finally, we average the results over the test objects. Results are given in Table 2.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Proxy Approximation Quality", "weight": 1.0} -->

Analysis of Table 2 answers our RQ1. Firstly, as expected, LeafRefit and its faster variations only approximate Proxy 1 when Assumption 1 holds. When it does, the quality of FastLeafRefit uniformly increases with the update set size, reaching perfect results for *Top64Leaves*, which is equivalent to LeafRefit. On the other hand, LeafInfluence approximates Proxy 2 regardless of Assumption 1; the dependency of FastLeafInfluence on the update set is analogous to that of FastLeafRefit. This shows that LeafInfluence is more robust in approximating its corresponding proxy than LeafRefit.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Runtime Comparison", "weight": 1.0} -->

In this section, we compare different variations (update set choices) of FastLeafRefit and FastLeafInfluence in terms of their runtimes. For each dataset used in the study, we randomly pick $k = 100$ training objects for influence evaluation, calculate the resulting change in the model (new leaf values for FastLeafRefit and leaf value derivatives for FastLeafInfluence), measure the total elapsed wall time and divide the result by $k$ to obtain the average time elapsed per one training object. The results are given in Fig. 1.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Runtime Comparison", "weight": 1.0} -->

Firstly, as expected, we observe that smaller update sets considerably reduce the runtimes of our algorithms, with the most radical speedup yielded by *SinglePoint* due to not having to recalculate any derivatives at all. Secondly, quite naturally, FastLeafInfluence performs much faster than FastLeafRefit, presumably due to vectorization and gradient precomputation (see end of Section 3.2.1). These observations confirm RQ2.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Harmful Object Removal", "weight": 1.0} -->

In this experiment, we consider a particular use-case scenario, classification in the presence of label noise, and evaluate whether our methods are able to identify training objects that are noisy, harmful for specific test objects. In order to do that, we randomly select $k$ training samples,^77^7We set $k = 4000$ for Adult and Amazon, and $k = 3500$ for Upselling. flip their labels, and obtain GBDT's predictions on test data before and after noise injection.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Harmful Object Removal", "weight": 1.0} -->

(a) Logloss reduction on a particular test index.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Harmful Object Removal", "weight": 1.0} -->

(b) Logloss reduction on the whole test set.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Harmful Object Removal", "weight": 1.0} -->

A. We sort the training points in ascending order of average influence on test objects and measure ROC-AUC of noise detection. In addition to variations of FastLeafRefit and FastLeafInfluence, we also compare against A noise detection method exploiting the problem structure, which scores the training points using GBDT's prediction in favor of the class opposite to its observed label (*Detector*), actual loss changes after leave-one-out retraining (*Leave-One-Out*), and ground-truth binary labels of the train object being noisy (*Oracle*). The results are given in Fig. 2.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Harmful Object Removal", "weight": 1.0} -->

B. We select $n = 50$ test points that suffered the largest Logloss increase, thus simulating problematic test objects. For each of these objects, we sort the training points in ascending order of influence and incrementally remove them from the training set in batches of $m = 50$ objects; on each iteration we measure the relative Logloss reduction both on this given test object and on the whole test set $\mathbf{X}_{test}$ and, similarly to ranking, calculate DCG using these reductions as gains. Finally, we average these metrics over the $n$ test points. The results are given in Fig. 3(a) and 3(b).

<!-- chunk {"id": "body-0057", "role": "body", "section": "Harmful Object Removal", "weight": 1.0} -->

Firstly, from Fig. 2, we note that all variations of FastLeafRefit and FastLeafInfluence perform strongly on the overall noise detection problem, where they score close to the top-performing *Detector*. Secondly, our methods greatly outperform their competitors (shown in blue on Fig. 3(a)) in targeting training objects harmful for a particular test object. These two observations confirm the hypothesis of RQ3. Finally, the two parts on Fig. 3 address RQ4 by clearly showing the way in which larger update sets increase quality: while all approximations score comparably in targeting particular test objects, smaller update sets lead to worsening the overall test quality (except for Upselling); in other words, *smaller update sets lead to overfitting the targeted test object*. Proper configurations of TopKLeaves, on the other hand, allow to "fix" a specific test object without overfitting it (k=8, 22, 64 for Adult and Amazon).

<!-- chunk {"id": "body-0058", "role": "body", "section": "Debugging Domain Mismatch", "weight": 1.0} -->

A common issue in the supervised machine learning is *domain mismatch*. This is a situation, when the joint distribution of points in the test dataset $\mathbf{X}_{test}$ differs from the one in the labeled training dataset $\mathbf{X}_{train}$. Often in such scenarios, a model fine-tuned on the training dataset fails to produce accurate predictions on the test data. A standard way to cope with this problem is re-weighting $\mathbf{X}_{train}$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Debugging Domain Mismatch", "weight": 1.0} -->

In the following experiment we demonstrate that by identifying influential samples in $\mathbf{X}_{train}$ for certain subsamples in $\mathbf{X}_{test}$ we are able to detect domain mismatch and get a hint on how the distribution of points in $\mathbf{X}_{train}$ should be modified in order to match better the distribution of points in $\mathbf{X}_{test}$. The design of this experiment is a modification of the corresponding use-case of Koh & Liang. We use the same Hospital dataset (see Section 4.2), with each point being a hospital patient represented by 127 features and the goal is to predict the readmission. To introduce domain mismatch we bias the distribution in the training dataset by filtering out a subsample of patients with ${age} \in {\lbrack 40;50)}$ and label $y = 1$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Debugging Domain Mismatch", "weight": 1.0} -->

Originally we had 169/1853 readmitted patients in this group and 2140/20000 overall; after we get 17/1601 in the ${age} \in {\lbrack 40;50)}$ group and 1988/19848 overall. Clearly, the distribution of labels in this specific age group becomes highly biased, while the proportion of positive labels in the whole dataset changes slightly (from 10.7% to 10.0%).

<!-- chunk {"id": "body-0061", "role": "body", "section": "Debugging Domain Mismatch", "weight": 1.0} -->

Training set $\mathbf{X}_{train}$ is naturally split into four parts ${\{\mathbf{X}_{train}^{i}\}}_{i = 1}^{4}$ depending on the value of $y$ and whether ${age} \in {\lbrack 40;50)}$. One would expect that in the modified training dataset, samples with ${age} \in {\lbrack 40;50)}$ and $y = 1$ are the most (positively) influential, so their removal will be the most harmful for the performance on the test dataset, while the removal of the samples with ${age} \in {\lbrack 40;50)}$ and $y = 0$ might even be beneficial, since it is the most straightforward way to align the distributions in the test and train datasets. Below we confirm this expectation.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Debugging Domain Mismatch", "weight": 1.0} -->

Let us focus on the subset $\mathbf{X}_{test}^{0}:=\left. \{{\mathbf{x} \in \mathbf{X}_{test}} \middle| {{{age}{(\mathbf{x})}} \in {\lbrack 40;50)}}\} \right.$, since its elements are expected to be the most affected by the introduced domain mismatch. We sample 100 points from every part ${\{\mathbf{X}_{train}^{i}\}}_{i = 1}^{4}$ (or take the whole part, if it has $< 100$ points). For each of the methods *FastLeafRefit* and *FastLeafInfluence* with various update sets we compute the influence of the training samples on $\mathbf{X}_{test}^{0}$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Debugging Domain Mismatch", "weight": 1.0} -->

Specifically, (a) with *FastLeafRefit*, for an element $\mathbf{x} \in \mathbf{X}_{train}$ we find the average Logloss reduction on $\mathbf{X}_{test}^{0}$, introduced by removing $\mathbf{x}$; (b) with *FastLeafInfluence*, for an element $\mathbf{x} \in \mathbf{X}_{train}$ we find the derivative of the average Logloss on $\mathbf{X}_{test}^{0}$ with respect to the weight $w$ of $\mathbf{x}$ at $w = 1$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Debugging Domain Mismatch", "weight": 1.0} -->

Table 3 provides the average influence among the sampled train points with the fixed label $y \in {\{ 0,1\}}$ and the fixed indicator ${I{({{age} \in {\lbrack 40;50)}})}} \in {\{ 0,1\}}$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Debugging Domain Mismatch", "weight": 1.0} -->

As expected, with all methods, the samples of the same type, as the filtered samples, are consistently the most influential. Indeed, removal of these samples increases the most the loss on $\mathbf{X}_{test}$, and the derivative of the loss with respect to the weights of these samples is negative indicating that *FastLeafInfluence* favors upweighting them. In all cases removal of elements with $y = 0$ and ${age} \in {\lbrack 40;50)}$ is estimated to be profitable, also confirming the initial expectations. These results allow us to answer RQ5 in the positive.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we addressed the problem of finding train objects that exerted the largest influence on the GBDT's prediction on a particular test object. Building on the Influence Function framework for parametric models, we derived LeafRefit and LeafInfluence, methods for estimating influences based on their respective proxy metrics, Proxies [1 and 2. By utilizing the structure of tree ensembles, we also derived computationally efficient approximations to these methods, FastLeafRefit and FastLeafInfluence. In our experiments, through considering several applied scenarios, we showed the practical applicability of these approaches, as well as their ability to produce actionable insights allowing to improve the existing model.
