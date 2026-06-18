<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Calibrating Predictions to Decisions: A Novel Approach to Multi-Class Calibration

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

When facing uncertainty, decision-makers want predictions they can trust. A machine learning provider can convey confidence to decision-makers by guaranteeing their predictions are distribution calibrated - amongst the inputs that receive a predicted class probabilities vector q, the actual distribution over classes is q. For multi-class prediction problems, however, achieving distribution calibration tends to be infeasible, requiring sample complexity exponential in the number of classes C. In this work, we introduce a new notion - decision calibration - that requires the predicted distribution and true distribution to be ``indistinguishable'' to a set of downstream decision-makers. When all possible decision makers are under consideration, decision calibration is the same as distribution calibration. However, when we only consider decision makers choosing between a bounded number of actions (e.g. polynomial in C), our main result shows that decisions calibration becomes feasible - we design a recalibration algorithm that requires sample complexity polynomial in the number of actions and the number of classes.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We validate our recalibration algorithm empirically: compared to existing methods, decision calibration improves decision-making on skin lesion and ImageNet classification with modern neural network predictors.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Machine learning predictions are increasingly employed by downstream decision makers who have little or no visibility on how the models were designed and trained. In high-stakes settings, such as healthcare applications, decision makers want predictions they can trust. For example in healthcare, suppose a machine learning service offers a supervised learning model to healthcare providers that claims to predict the probability of various skin diseases, given an image of a lesion. Each healthcare provider want assurance that the model's predictions lead to beneficial decisions, according to their own loss functions. As a result, the healthcare providers may reasonably worry that the model was trained using a loss function different than their own. This mismatch is often inevitable because the ML service may provide the same prediction model to many healthcare providers, which may have different treatment options available and loss functions. Even the same healthcare provider could have different loss functions throughout time, due to changes in treatment availability.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

If predicted probabilities perfectly equal the true probability of the event, this issue of trust would not arise because they would lead to optimal decision making regardless of the loss function or task considered by downstream decision makers. In practice, however, predicted probabilities are never perfect. To address this, the healthcare providers may insist that the prediction function be *distribution calibrated*, requiring that amongst the inputs that receive predicted class probability vectors $q$, the actual distribution over classes is $q$. This solves the trust issue because among the patients who receive prediction $q$, the healthcare providers knows that the true label distribution is $q$, and hence knows the true expected loss of a treatment on these patients. Unfortunately, to achieve distribution calibration, we need to reason about the set of individuals $x$ who receive prediction $q$, for *every* possible predicted $q$. As the number of distinct predictions may naturally grow exponentially in the number of classes $C$, the amount of data needed to accurately certify distribution calibration tends to be prohibitive. Due to this statistical barrier, most work on calibrated multi-class predictions focuses on obtaining relaxed variants of calibration.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

These include *confidence calibration*, which calibrates predictions only over the most likely class, and *classwise calibration*, which calibrates predictions for each class marginally. While feasible, these notions are significantly weaker than distribution calibration and do not address the trust issue highlighted above. Is there a calibration notion that addresses the issue of trust, but can also be verified and achieved efficiently? Our paper answers this question affirmatively.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

We introduce a new notion of calibration---*decision calibration*---where we take the perspective of potential decision-makers: the only differences in predictions that matter are those that could lead to different decisions. Inspired by Dwork et al., we formalize this intuition by requiring that predictions are "indistinguishable" from the true outcomes, according to a collection of decision-makers.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

First, we show that prior notions of calibration can be characterized as special cases of decision calibration under different collections of decision-makers. This framing explains the strengths and weakness of existing notions of calibration, and clarifies the guarantees they offer to decision makers. For example, we show that a predictor is distribution calibrated if and only if it is decision calibrated with respect to *all* loss functions and decision rules. This characterization demonstrates why distribution calibration is so challenging: achieving distribution calibration requires simultaneously reasoning about all possible decision tasks.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

The set of *all* decision rules include those that choose between exponentially (in number of classes $C$) many actions. In practice, however, decision-makers typically choose from a bounded (or slowly-growing as a function of $C$) set of actions. Our main contribution is an algorithm that *guarantees decision calibration for such more realistic decision-makers*. In particular, we give a sample-efficient algorithm that takes a pre-trained predictor and post-processes it to achieve decision calibration with respect to *all* decision-makers choosing from a bounded set of actions. Our recalibration procedure does not harm other common performance metrics, and actually improves accuracy and likelihood of the predictions. In fact, we argue formally that, in the setting of bounded actions, optimizing for decision calibration recovers many of the benefits of distribution calibration, while drastically improving the sample complexity. Empirically, we use our algorithm to recalibrate deep network predictors on two large scale datasets: skin lesion classification (HAM10000) and Imagenet.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Our Contributions", "weight": 1.0} -->

Our recalibration algorithm improves decision making, and allow for more accurate decision loss estimation compared to existing recalibration methods.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Setup and Notation", "weight": 1.0} -->

We consider the prediction problem with random variables $X$ and $Y$, where $X \in \mathcal{X}$ denotes the input features, and $Y \in \mathcal{Y}$ denotes the label. We focus on classification where $\mathcal{Y} = {\{{(1,0,\cdots,0)},{(0,1,\cdots,0)},\cdots,{(0,0,\cdots,1)}\}}$ where each $y \in \mathcal{Y}$ is a one-hot vector with $C \in {\mathbb{N}}$ classes. ^11^1We can also equivalently define $\mathcal{Y} = {\{ 1,2,\cdots,C\}}$, here we denote $y$ by a one-hot vector for notation convenience when taking expectations.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Setup and Notation", "weight": 1.0} -->

A probability prediction function is a map $\hat{p}:{\mathcal{X}\rightarrow\Delta^{C}}$ where $\Delta^{C}$ is the $C$-dimensional simplex. We define the support of $\hat{p}$ as the set of distributions it could predict, i.e. $\left. \{{\hat{p}{(x)}} \middle| {x \in \mathcal{X}}\} \right.$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Decision Making Tasks and Loss Functions", "weight": 1.0} -->

We formalize a decision making task as a loss minimization problem. The decision maker has some set of available actions $\mathcal{A}$ and a loss function $\ell:{{\mathcal{Y} \times \mathcal{A}}\rightarrow{\mathbb{R}}}$. In this paper we assume the loss function does not directly depend on the input features $X$. For notational simplicity we often refer to a (action set, loss function) pair $(\mathcal{A},\ell)$ only by the loss function $\ell$: the set of actions $\mathcal{A}$ is implicitly defined by the domain of $\ell$. We denote the set of all possible loss functions as $\mathcal{L}_{all} = {\{\ell:{{\mathcal{Y} \times \mathcal{A}}\rightarrow{\mathbb{R}}}\}}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Decision Making Tasks and Loss Functions", "weight": 1.0} -->

We treat all action sets $\mathcal{A}$ with the same cardinality as the same set --- they are equivalent up to renaming the actions. A convenient way to think about this is that we only consider actions sets $\mathcal{A} \in {\{{\lbrack 1\rbrack},{\lbrack 2\rbrack},\cdots,{\lbrack K\rbrack},\cdots,{\mathbb{N}},{\mathbb{R}}\}}$ where ${\lbrack K\rbrack} = {\{ 1,\cdots,K\}}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Bayes Decision Making", "weight": 1.0} -->

Given some predicted probability $\hat{p}{(X)}$ on $Y$, a decision maker selects an action in $\mathcal{A}$. We assume that the decision maker selects the action based on the predicted probability. That is, we define a decision function as any map from the predicted probability to an action $\delta:{\Delta^{C}\rightarrow\mathcal{A}}$. and denote by ~all~ as the set of all decision functions.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Bayes Decision Making", "weight": 1.0} -->

Typically a decision maker selects the action that minimizes the expected loss (under the predicted probability). This strategy is formalized by the following definition of Bayes decision making.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Calibration: A Decision Making Perspective", "weight": 1.0} -->

In our setup, the decision maker outsources the prediction task and uses a prediction function $\hat{p}$ provided by a third-party forecaster (e.g., an ML Prediction API). Thus, we imagine a forecaster who trains a generic prediction function without knowledge of the exact loss $\ell$ downstream decision makers will use (or worse, will be used by multiple decision-makers with different loss functions). For example, the prediction function may be trained to minimize a standard objective such as L2 error or log likelihood, then sold to decision makers as an off-the-shelf solution.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Calibration: A Decision Making Perspective", "weight": 1.0} -->

In such a setting, the decision makers may be concerned that the off-the-shelf solution may not perform well according to their loss function. If the forecaster could predict optimally (i.e. ${\hat{p}{(X)}} = {p^{\ast}{(X)}}$ almost surely), then there would be no issue of trust; of course, perfect predictions are usually impossible, so the forecaster needs feasible ways of conveying trust to the decision makers. To mitigate concerns about the performance of the prediction function, the forecaster might aim to offer performance guarantees applicable to decision makers whose loss functions come from class of losses $\mathcal{L} \subset \mathcal{L}_{all}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Decision Calibration", "weight": 1.0} -->

First and foremost, a decision maker wants assurance that making decisions based on the prediction function $\hat{p}$ give low expected loss. In particular, a decision maker with loss $\ell$ wants assurance that the Bayes decision rule $\delta_{\ell}$ is the best decision making strategy, given $\hat{p}$. In other words, she wants $\delta_{\ell}$ to incur a lower loss compared to alternative decision rules. Second, the decision maker wants to know how much loss is going to be incurred (before the actions are deployed and outcomes are revealed); the decision maker does not want to incur any additional loss in surprise that she has not prepared.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Decision Calibration", "weight": 1.0} -->

To capture these desiderata we formalize a definition based on the following intuition: suppose a decision maker with some loss function $\ell$ considers a decision rule $\delta \in_{all}$ (that may or may not be the Bayes decision rule), the decision maker should be able to correctly compute the expected loss of using $\delta$ to make decisions, as a function of *the predictions* $\hat{p}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Decision Calibration Generalizes Existing Notions of Calibration", "weight": 1.0} -->

We show that by varying the choice of loss class $\mathcal{L}$, decision calibration can actually express prior notions of calibration. For example, consider confidence calibration, where among the samples whose the top probability is $\beta$, the top accuracy is indeed $\beta$. Formally, confidence calibration requires that

<!-- chunk {"id": "body-0022", "role": "body", "section": "Decision Calibration Generalizes Existing Notions of Calibration", "weight": 1.0} -->

We show that a prediction function $\hat{p}$ is confidence calibrated if and only if it is $\mathcal{L}_{r}$-decision calibration, where $\mathcal{L}_{r}$ is defined by

<!-- chunk {"id": "body-0023", "role": "body", "section": "Decision Calibration Generalizes Existing Notions of Calibration", "weight": 1.0} -->

Intuitively, loss functions in $\mathcal{L}_{r}$ corresponds to the refrained prediction task: a decision maker chooses between reporting a class label, or reporting "I don't know," denoted $\bot$. She incurs a loss of $0$ for correctly predicting the label $y$, a loss of $1$ for reporting an incorrect class label, and a loss of $\beta < 1$ for reporting "I don't know". If a decision maker's loss function belong to this simple class of losses $\mathcal{L}_{r}$, she can use a confidence calibrated prediction function $\hat{p}$, because the two desiderata (no regret and accurate loss estimation) in Proposition 1 are true for her. However, such "refrained prediction" decision tasks only account for a tiny subset of all possible tasks that are interesting to decision makers. Similarly, classwise calibration is characterized through decision calibration using a class of loss functions that penalizes class-specific false positives and negatives.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Decision Calibration Generalizes Existing Notions of Calibration", "weight": 1.0} -->

In this way, decision calibration clarifies the implications of existing notions of calibration on decision making: relaxed notions of calibration correspond to decision calibration over restricted classes of losses. In general, decision calibration provides a unified view of most existing notions of calibration as the following theorem shows.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Decision Calibration Generalizes Existing Notions of Calibration", "weight": 1.0} -->

Existing Calibration Definitions
Associated Loss Functions

<!-- chunk {"id": "body-0026", "role": "body", "section": "Decision Calibration over Bounded Action Space", "weight": 1.0} -->

In many contexts, directly optimizing for distribution calibration may be overkill. In particular, in most realistic settings, decision makers tend to have a bounded number of possible actions, so the relevant losses come from $\mathcal{L}^{K}$ for reasonable $K \in {\mathbb{N}}$. Thus, we consider obtaining decision calibration for all loss functions defined over a bounded number of actions $K$. In the remainder of the paper, we focus on this restriction of decision calibration to the class of losses with bounded action space; we reiterate the definition of decision calibration for the special case of $\mathcal{L}^{K}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "From decision calibration to distribution calibration", "weight": 1.0} -->

We argue that in the practical context where decision makers have a bounded number of actions, $\mathcal{L}^{K}$-decision calibration is actually as strong as distribution calibration. Specifically, we show that given a $\mathcal{L}^{K}$-decision calibrated predictor $\hat{p}$ and a chosen loss $\ell \in \mathcal{L}^{K}$, a decision maker can construct a post-processed predictor ${\hat{p}}_{\ell}$ that is distribution calibrated; and the Bayes action remains unchanged under ${\hat{p}}_{\ell}$ (i.e. ${\delta_{\ell}{({\hat{p}{(x)}})}} = {\delta_{\ell}{({{\hat{p}}_{\ell}{(x)}})}}$).

<!-- chunk {"id": "body-0028", "role": "body", "section": "From decision calibration to distribution calibration", "weight": 1.0} -->

This means the expected loss $\ell$ of decision making under $\hat{p}$ is maintained under the post-processed predictor ${\hat{p}}_{\ell}$. In other words, for the purposes of decision making, the decision calibrated predictor $\hat{p}$ is identical to the derived predictor that satisfies distribution calibration ${\hat{p}}_{\ell}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "From decision calibration to distribution calibration", "weight": 1.0} -->

This argument is subtle: on the surface, the idea that decision calibration (which is feasible) goes against the intuition that distribution calibration is difficult to achieve. Note, however, that the difficulty in achieving distribution calibration comes from the large support of $\hat{p}$. The key insight behind our construction is that, given a fixed loss function $\ell$ over $K$ actions, it is possible to construct a ${\hat{p}}_{\ell}$ with small support without losing any information necessary for making decisions according to $\ell$. In other words, for making good decisions according to *all* loss functions $\ell$, $\hat{p}$ might need to have large support; but for a *fixed* $\ell$ with $K$ actions, ${\hat{p}}_{\ell}$ does not need to have large support.

<!-- chunk {"id": "body-0030", "role": "body", "section": "From decision calibration to distribution calibration", "weight": 1.0} -->

In this way, we can learn a single $\mathcal{L}^{K}$-decision calibrated predictor (with possibly large support), but view it as giving rise to many different loss-specific distribution calibrated predictors ${\hat{p}}_{\ell}$ for each $\ell \in \mathcal{L}^{K}$. Formally, we show the following proposition.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Approximate $\\mathcal{L}^{K}$ Decision Calibration is Verifiable and Achievable", "weight": 1.0} -->

Decision calibration in Definition 2. ‣ 3.1 Decision Calibration ‣ 3 Calibration: A Decision Making Perspective ‣ Calibrating Predictions to Decisions: A Novel Approach to Multi-Class Calibration") usually cannot be achieved perfectly. The definition has to be relaxed to allow for statistical and numerical errors. To meaningfully define approximate calibration we must assume that the loss functions are bounded, i.e. no outcome $y \in \mathcal{Y}$ and action $a \in \mathcal{A}$ can incur an infinite loss. In particular, we bound $\ell$ by its 2-norm $\max_{a}{\parallel\ell{( \cdot,a)}\parallel}_{2}:=\max_{a}\sqrt{\sum_{y \in \mathcal{Y}}{\ell{(y,a)}^{2}}}$. ^33^3The choice of 2-norm is for convenience. All $p$-norms are equivalent up to a multiplicative factor polynomial in $C$, so our main theorem (Theorem 2.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Approximate $\\mathcal{L}^{K}$ Decision Calibration is Verifiable and Achievable", "weight": 1.0} -->

‣ 4.1 Approximate ℒ^𝐾 Decision Calibration is Verifiable and Achievable ‣ 4 Achieving Decision Calibration with PAC Guarantees ‣ Calibrating Predictions to Decisions: A Novel Approach to Multi-Class Calibration")) still hold for any $p$-norms up to the polynomial factor. Now we can proceed to define approximate decision calibration. In particular, we compare the difference between the two sides in Eq.(2. ‣ 3.3 Decision Calibration over Bounded Action Space ‣ 3 Calibration: A Decision Making Perspective ‣ Calibrating Predictions to Decisions: A Novel Approach to Multi-Class Calibration")) of Definition 2. ‣ 3.1 Decision Calibration ‣ 3 Calibration: A Decision Making Perspective ‣ Calibrating Predictions to Decisions: A Novel Approach to Multi-Class Calibration") with the maximum magnitude of the loss function.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Verification of Decision Calibration", "weight": 1.0} -->

This section focuses on the first part of Theorem 2. ‣ 4.1 Approximate ℒ^𝐾 Decision Calibration is Verifiable and Achievable ‣ 4 Achieving Decision Calibration with PAC Guarantees ‣ Calibrating Predictions to Decisions: A Novel Approach to Multi-Class Calibration") where we certify $(\mathcal{L}^{K},\epsilon)$-decision calibration. A naive approach would use samples to directly estimate

<!-- chunk {"id": "body-0034", "role": "body", "section": "Verification of Decision Calibration", "weight": 1.0} -->

and compare it with $\epsilon$. However, the complexity of this optimization problem poses challenges to analysis. We will make several observations to transform this complex optimization problem to a simple problem that resembles linear classification.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Observation 1", "weight": 1.0} -->

The first observation is that we do not have to take the supremum over $\mathcal{L}^{K}$ because for any choice of $\delta \in$ by simple calculations (details in the Appendix) we have

<!-- chunk {"id": "body-0036", "role": "body", "section": "Observation 2", "weight": 1.0} -->

We observe that the partitions of $\Delta^{C}$ are defined by linear classification boundaries. Formally, we introduce a new notation for the linear multi-class classification functions

<!-- chunk {"id": "body-0037", "role": "body", "section": "Observation 2", "weight": 1.0} -->

Note that this new classification task is a tool to aid in understanding decision calibration, and bears no relationship with the original prediction task (predicting $Y$ from $X$). Intuitively $w$ defines the weights of a linear classifier; given input features $q \in \Delta^{C}$ and a candidate class $a$, $b_{w}$ outputs an indicator: ${b_{w}{(q,a)}} = 1$ if the optimal decision of $q$ is equal to $a$ and $0$ otherwise.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Observation 2", "weight": 1.0} -->

The following equality draws the connection between Eq. and linear classification. The proof is simply a translation from the original notations to the new notations.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Observation 2", "weight": 1.0} -->

The final outcome of our derivations is the following proposition (Proof in Appendix C.3)

<!-- chunk {"id": "body-0040", "role": "body", "section": "Recalibration Algorithm", "weight": 1.0} -->

This section discusses the second part of Theorem 2. ‣ 4.1 Approximate ℒ^𝐾 Decision Calibration is Verifiable and Achievable ‣ 4 Achieving Decision Calibration with PAC Guarantees ‣ Calibrating Predictions to Decisions: A Novel Approach to Multi-Class Calibration") where we design a post-processing recalibration algorithm. The algorithm is based on the following intuition, inspired: given a predictor $\hat{p}$ we find the worst $b \in B^{K}$ that violates Eq. (line 3 of Algorithm 1); then, we make an update to $\hat{p}$ to minimize the violation of Eq. for the worst $b$ (line 4,5 of Algorithm 1). This process is be repeated until we get a $(B^{K},\epsilon)$-decision calibrated prediction (line 2). The sketch of the algorithm is shown in Algorithm 1 and the detailed algorithm is in the Appendix.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Recalibration Algorithm", "weight": 1.0} -->

1 Input current prediction function p̂, tolerance ϵ. Initialize p̂ = p̂;
2 for t = 1, 2, ⋯, T until output p̂(T) when it satisfies Eq. do
3 Find b ∈ BK that maximizes $\sum_{a = 1}^{K}\left. \parallel{\mathbb{E}}\left. \lbrack{(Y - {\hat{p}}^{({t - 1})}{(X)})}b{({\hat{p}}^{({t - 1})}{(X)},a)}\parallel \right.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Recalibration Algorithm", "weight": 1.0} -->

\right.$;
4 Compute the adjustments da = 𝔼 [(Y−p̂(t−1) (X)) b (p̂(t−1) (X),a)]/𝔼 [b (p̂(t−1) (X),a)];
5 Set ${\hat{p}}^{(t)}:{x\mapsto{{{\hat{p}}^{({t - 1})}{(x)}} + {\sum_{a = 1}^{K}{{b{({{\hat{p}}^{({t - 1})}{(x)}},a)}} \cdot d_{a}}}}}$ (projecting onto if necessary);
Algorithm 1 Recalibration algorithm to achieve ℒK decision calibration.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Recalibration Algorithm", "weight": 1.0} -->

Given a dataset with $N$ samples, the expectations in Algorithm 1 are replaced with empirical averages. The following theorem demonstrates that Algorithm 1 satisfies the conditions stated in Theorem 2. ‣ 4.1 Approximate ℒ^𝐾 Decision Calibration is Verifiable and Achievable ‣ 4 Achieving Decision Calibration with PAC Guarantees ‣ Calibrating Predictions to Decisions: A Novel Approach to Multi-Class Calibration").

<!-- chunk {"id": "body-0044", "role": "body", "section": "Relaxation of Decision Calibration for Computational Efficiency", "weight": 1.0} -->

We complete the discussion by addressing the open computational question. Directly optimizing over $B^{K}$ is difficult, so we instead define the softmax relaxation.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Relaxation of Decision Calibration for Computational Efficiency", "weight": 1.0} -->

The key motivation behind this relaxation is that ${\overline{b}}_{w} \in {\overline{B}}^{K}$ is now differentiable in $w$, so we can optimize over ${\overline{B}}^{K}$ using gradient descent. Correspondingly some technical details in Algorithm 1 change to accommodate soft partitions; we address these modifications in Appendix A and show that after these modifications Theorem 2.2 still holds. Intuitively, the main reason that we can still achieve decision calibration with softmax relaxation is because $B^{K}$ is a subset of the closure of ${\overline{B}}^{K}$. Therefore, compared to Eq., we enforce a slightly stronger condition with the softmax relaxation. This can be formalized in the following proposition.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Empirical Evaluation", "weight": 1.0} -->

^††^Decision calibration is implemented in the torchuq package at Code to reproduce these experiments can be found in following directory of the torchuq package "torchuq/applications/decision_calibration"

<!-- chunk {"id": "body-0047", "role": "body", "section": "Skin Legion Classification", "weight": 1.0} -->

This experiment materializes our motivating example in the introduction. We aim to show on a real medical prediction dataset, our recalibration algorithm improves both the decision loss and reduces the decision loss estimation error. For the estimation error, as in Definition 4. ‣ 4.1 Approximate ℒ^𝐾 Decision Calibration is Verifiable and Achievable ‣ 4 Achieving Decision Calibration with PAC Guarantees ‣ Calibrating Predictions to Decisions: A Novel Approach to Multi-Class Calibration") for any loss function $\ell$ and corresponding Bayes decision rule $\delta_{\ell}$ we measure

<!-- chunk {"id": "body-0048", "role": "body", "section": "Skin Legion Classification", "weight": 1.0} -->

In addition to the loss function in Figure 1 (which is motivated by medical domain knowledge), we also consider a set of 500 random loss functions where for each ${y \in \mathcal{Y}},{a \in \mathcal{A}}$, ${\ell{(y,a)}} \sim {\text{Normal}{}}$, and report both the average loss gap and the maximum loss gap across the loss functions.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Setup", "weight": 1.0} -->

We use the HAM10000 dataset. We partition the dataset into train/validation/test sets, where approximately 15% of the data are used for validation, while 10% are used for the test set. We use the train set to learn the baseline classifier $\hat{p}$, validation set to recalibrate, and the test set to measure final performance. For modeling we use the densenet-121 architecture, which achieves around 90% accuracy.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Methods", "weight": 1.0} -->

For our method we use Algorithm 2 in Appendix A (which is a small extension of Algorithm 1 explained in Section 4.4). We compare with temperature scaling and Dirichlet calibration. We observe that all recalibration methods (including ours) work better if we first apply temperature scaling, hence we first apply it in all experiments. For example, in Figure 2 temperature scaling corresponds to $0$ decision recalibration steps.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Results", "weight": 1.0} -->

The results are shown in Figure 2. For these experiments we set the number of actions $K = 3$. For other choices we obtain qualitatively similar results in Appendix B. The main observation is that decision recalibration improves the loss gap in Eq. and slightly improves the decision loss. Our recalibration algorithm converges rather quickly (in about 5 steps). We also observe that our recalibration algorithm slightly improves top-1 accuracy (the average improvement is $0.40 \pm 0.08$%) and L2 loss (the average decrease is $0.010 \pm 0.001$) on the test set.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Imagenet Classification", "weight": 1.0} -->

We stress test our algorithm on Imagenet. The aim is to show that even with deeply optimized classifiers (such as inception-v3 and resnet) that are tailor made for the Imagenet benchmark and a large number of classes (1000 classes), our recalibration algorithm can improve the loss gap in Eq..

<!-- chunk {"id": "body-0053", "role": "body", "section": "Setup", "weight": 1.0} -->

The setup and baselines are identical to the HAM10000 experiment with two differences: we use pretrained models provided by pytorch, and among the 50000 standard validation samples, we use 40000 samples for recalibration and 10000 samples for testing. Similar to the previous experiment, we randomly generate a set of 500 loss functions from normal distributions.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Results", "weight": 1.0} -->

The results are shown in Figure 3 with additional plots in Appendix B. Decision calibration can generalize to a larger number of classes, and still provides some (albeit smaller) benefits with 1000 classes. Recalibration does not hurt accuracy and L2 error, as we observe that both improve by a modest amount (on average by $0.30$% and $0.00173$ respectively). We contrast decision calibration with Dirichlet calibration. Dirichlet calibration also reduces the loss gap when the number of classes is small (e.g. 10 classes), but is less scaleble than decision recalibration. With more classes its performance degrades much more than decision calibration.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Calibration", "weight": 1.0} -->

Early calibration research focus on binary classification. For multiclass classification, the strongest definition is distribution (strong) calibration but is hindered by sample complexity. Weaker notions such as confidence (weak) calibration, class-wise calibration or average calibration average calibration are more commonly used in practice. To unify these notions, proposes $\mathcal{F}$-calibration but lacks detailed guidance on which notions to use.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Individual calibration", "weight": 1.0} -->

Our paper discusses the average decision loss over the population $X$. A stronger requirement is to guarantee the loss for each individual decision. Usually individual guarantees are near-impossible and are only achievable with hedging or randomization.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Multi-calibration and Outcome Indistinguishability", "weight": 1.0} -->

Calibration have been the focus of many works on fairness, starting. Multi-calibration has emerged as a noteworthy notion of fairness because it goes beyond "protected" groups, and guarantees calibration for any group that is identifiable within some computational bound. Recently, generalizes multicalibration to outcome indistinguishability (OI). Decision calibration is a special form of OI.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

Notions of calibration are important to decision makers. Specifically, we argue that many of the benefits of calibration can be summarized in two key properties---no regret decision making and accurate loss estimation. Our results demonstrate that it is possible to achieve these desiderata for realistic decision makers choosing between a bounded number of actions, through the framework of decision calibration.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

Our results should not be interpreted as guarantees about the quality of individual predictions. For example, the medical provider cannot guarantee to each patient that their expected loss is low. Instead the guarantee should be interpreted as from the machine learning provider to the medical provider (who treats a group of patients). Misuse of our results can lead to unjustified claims about the trustworthiness of a prediction. Still, a clear benefit of the framework is that---due to accurate loss estimation---the overall quality of the predictor can be evaluated using unlabeled data.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Conclusion and Discussion", "weight": 1.5} -->

One natural way to strengthen the guarantees of decision calibration would be extend the results to give decision "multi-calibration," as in Hébert-Johnson et al.; Dwork et al.. Multi-calibration guarantees that predictions are calibrated, not just overall, but also when restricting our attention to structured (identifiable) subpopulations. In this paper, we consider loss functions that only depend on $x$ through $\hat{p}{(x)}$; extending decision calibration to a multi-group notion would correspond to including loss functions that can depend directly on the input features in $x$. However, when the input features are complex and high-dimensional (e.g. medical images), strong results (such as the feasibility of achieving $\mathcal{L}^{K}$-decision calibration) become much more difficult. As in Hébert-Johnson et al., some parametric assumptions on how the loss can depend on the input feature $x$ would be necessary.
