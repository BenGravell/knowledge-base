<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Conditional Validity of Inductive Conformal Predictors

Topics include Conformal prediction, Inductive conformal prediction, Conditional validity, Marginal coverage, Prediction sets, Distribution-free inference, Machine learning theory.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Studies what kinds of conditional coverage guarantees can and cannot be obtained by inductive, split-sample conformal predictors. The paper is a key bridge between the practical efficiency of inductive conformal prediction and the stronger validity notions that are often desired in deployment.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Conformal predictors are set predictors that are automatically valid in the sense of having coverage probability equal to or exceeding a given confidence level. Inductive conformal predictors are a computationally efficient version of conformal predictors satisfying the same property of validity. However, inductive conformal predictors have been only known to control unconditional coverage probability. This paper explores various versions of conditional validity and various ways to achieve them using inductive conformal predictors and their modifications.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper continues study of the method of conformal prediction, introduced in Vovk et al. and Saunders et al. and further developed in Vovk et al.. An advantage of the method is that its predictions (which are set rather than point predictions) automatically satisfy a finite-sample property of validity. Its disadvantage is its relative computational inefficiency in many situations. A modification of conformal predictors, called inductive conformal predictors, was proposed in Papadopoulos et al. with the purpose of improving on the computational efficiency of conformal predictors.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Most of the literature on conformal prediction studies the behavior of set predictors in the online mode of prediction, perhaps because the property of validity can be stated in an especially strong form in the on-line mode. The online mode, however, is much less popular in applications of machine learning than the batch mode of prediction. This paper follows the recent papers by Lei et al., Lei and Wasserman, and Lei et al. studying properties of conformal prediction in the batch mode; we, however, concentrate on inductive conformal prediction. The performance of inductive conformal predictors in the batch mode is illustrated using the well-known Spambase data set; for earlier empirical studies of conformal prediction in the batch mode see, e.g., Vanderlooy et al.. The conference version of this paper is published as Vovk.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We will usually be making the *assumption of randomness*, which is standard in machine learning and nonparametric statistics: the available data is a sequence of *examples* generated independently from the same probability distribution $P$. (In some cases we will make the weaker assumption of exchangeability; for some of our results even weaker assumptions, such as conditional randomness or exchangeability, would have been sufficient.) Each example consists of two components: an *object* and a *label*. We are given a *training set* of examples and a new object, and our goal is to predict the label of the new object. (If we have a whole *test set* of new objects, we can apply the procedure for predicting one new object to each of the objects in the test set.)

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The two desiderata for inductive conformal predictors are their validity and efficiency: validity requires that the coverage probability of the prediction sets should be at least equal to a preset confidence level, and efficiency requires that the prediction sets should be as small as possible. However, there is a wide variety of notions of validity, since the "coverage probability" is, in general, conditional probability. The simplest case is where we condition on the trivial $\sigma$-algebra, i.e., the probability is in fact unconditional probability, but several other notions of conditional validity are depicted in Figure 1, where T refers to conditioning on the training set, O to conditioning on the test object, and L to conditioning on the test label. The arrows in Figure 1 lead from stronger to weaker notions of conditional validity; U is the sink and TOL is the source (the latter is not shown).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Inductive conformal predictors will be defined in Section 2. They are automatically valid, in the sense of unconditional validity. It should be said that, in general, the unconditional error probability is easier to deal with than conditional error probabilities; e.g., the standard statistical methods of cross-validation and bootstrap provide decent estimates of the unconditional error probability but poor estimates for the training conditional error probability: see Hastie et al., Section 7.12.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Section 3 we explore training conditional validity of inductive conformal predictors. Our simple results (Propositions 2a and 2b) are of the PAC type, involving two parameters: the target training conditional coverage probability $1 - \epsilon$ and the probability $1 - \delta$ with which $1 - \epsilon$ is attained. They show that inductive conformal predictors achieve training conditional validity automatically (whereas for other notions of conditional validity the method has to be modified). We give self-contained proofs of Propositions 2a and 2b, but Appendix A explains how they can be deduced from classical results about tolerance regions.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the following section, Section 4, we introduce a conditional version of inductive conformal predictors and explain, in particular, how it achieves label conditional validity. Label conditional validity is important as it allows the learner to control the set-prediction analogues of false positive and false negative rates. Section 5 is about object conditional validity and its main result is negative: precise object conditional validity cannot be achieved in a useful way unless the test object has a positive probability. Whereas precise object conditional validity is usually not achievable, we should aim for approximate and asymptotic object conditional validity when given enough data.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Section 6 reports on the results of empirical studies for the standard Spambase data set. Section 7 discusses close connections between an important class of ICPs and ROC curves. Section 8 concludes and Appendix A discusses connections with the classical theory of tolerance regions (in particular, it explains how Propositions 2a and 2b can be deduced from classical results about tolerance regions).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Inductive conformal predictors", "weight": 1.0} -->

The example space will be denoted $\mathbf{Z}$; it is the Cartesian product $\mathbf{X} \times \mathbf{Y}$ of two measurable spaces, the object space and the label space. In other words, each example $z \in \mathbf{Z}$ consists of two components: $z = {(x,y)}$, where $x \in \mathbf{X}$ is its object and $y \in \mathbf{Y}$ is its label. Two important special cases are the problem of *classification*, where $\mathbf{Y}$ is a finite set (equipped with the discrete $\sigma$-algebra), and the problem of *regression*, where $\mathbf{Y} = {\mathbb{R}}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Inductive conformal predictors", "weight": 1.0} -->

Let $(z_{1},\ldots,z_{l})$ be the training set, $z_{i} = {(x_{i},y_{i})} \in \mathbf{Z}$. We split it into two parts, the *proper training set* $(z_{1},\ldots,z_{m})$ of size $m < l$ and the *calibration set* of size $l - m$. An *inductive conformity $m$-measure* is a measurable function $A:{{\mathbf{Z}^{m} \times \mathbf{Z}}\rightarrow{\mathbb{R}}}$; the idea behind the *conformity score* $A{({(z_{1},\ldots,z_{m})},z)}$ is that it should measure how well $z$ conforms to the proper training set.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Inductive conformal predictors", "weight": 1.0} -->

A standard choice is where $f:{\mathbf{X}\rightarrow\mathbf{Y}'}$ is a prediction rule found from $(z_{1},\ldots,z_{m})$ as the training set and $\Delta:{{\mathbf{Y} \times \mathbf{Y}'}\rightarrow{\mathbb{R}}}$ is a measure of similarity between a label and a prediction. Allowing $\mathbf{Y}'$ to be different from $\mathbf{Y}$ (often $\mathbf{Y}' \supset \mathbf{Y}$) may be useful when the underlying prediction method gives additional information to the predicted label; e.g., the MART procedure used in Section 6 gives the logit of the predicted probability that the label is $1$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Remark", "weight": 1.0} -->

The idea behind the term "calibration set" is that this set allows us to calibrate the conformity scores for test examples by translating them into a probability-type scale.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Remark", "weight": 1.0} -->

The *inductive conformal predictor* (ICP) corresponding to $A$ is defined as the set predictor where $\epsilon \in {\lbrack 0,1\rbrack}$ is the chosen *significance level* ($1 - \epsilon$ is known as the *confidence level*), the *p-values* $p^{y}$, $y \in \mathbf{Y}$, are defined by are the conformity scores. Given the training set and a new object $x$ the ICP predicts its label $y$; it *makes an error* if $y \notin {\Gamma^{\epsilon}{(z_{1},\ldots,z_{l},x)}}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Remark", "weight": 1.0} -->

The random variables whose realizations are $x_{i}$, $y_{i}$, $z_{i}$, $z$ will be denoted by the corresponding upper case letters ($X_{i}$, $Y_{i}$, $Z_{i}$, $Z$, respectively). The following proposition of validity is almost obvious.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Training conditional validity", "weight": 1.0} -->

As discussed in Section 1, the property of validity of inductive conformal predictors is unconditional. The property of conditional validity can be formalized using a PAC-type 2-parameter definition. It will be convenient to represent the ICP in a slightly different form downplaying the structure $(x_{i},y_{i})$ of $z_{i}$. Define ${\Gamma^{\epsilon}{(z_{1},\ldots,z_{l})}}:={\{{(x,y)}\mid{p^{y} > \epsilon}\}}$, where $p^{y}$ is defined, as before, by and (therefore, $p^{y}$ depends implicitly on $x$). Proposition 1.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Training conditional validity", "weight": 1.0} -->

‣ 2 Inductive conformal predictors ‣ Conditional validity of inductive conformal predictors") can be restated by saying that the probability of error $Z_{l + 1} \notin {\Gamma^{\epsilon}{(Z_{1},\ldots,Z_{l})}}$ does not exceed $\epsilon$ provided $Z_{1},\ldots,Z_{l + 1}$ are exchangeable.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Training conditional validity", "weight": 1.0} -->

We consider a canonical probability space in which $Z_{i} = {(X_{i},Y_{i})}$, $i = {1,\ldots,{l + 1}}$, are i.i.d. random examples. A set predictor $\Gamma$ (outputting a subset of $\mathbf{Z}$ given $l$ examples and measurable in a suitable sense) is *$(\epsilon,\delta)$-valid* if, for any probability distribution $P$ on $\mathbf{Z}$, It is easy to see that ICPs satisfy this property for suitable $\epsilon$ and $\delta$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark", "weight": 1.0} -->

The training conditional guarantees discussed in this section are very similar to those for the hold-out estimate: compare, e.g., Proposition 2b above and Theorem 3.3 in Langford. The former says that $\Gamma^{\epsilon}$ is $(E,\delta)$-valid for where $\overline{bin}$ is the inverse function to $bin$: (unless $k = n$, we can also say that ${\overline{bin}}_{n,\delta}{(k)}$ is the only value of $p$ such that ${{bin}_{n,p}{(k)}} = \delta$: cf. Lemma 1 above). And the latter says that a point predictor's error probability (over the test example) does not exceed with probability at least $1 - \delta$ (over the training set), where $k$ is the number of errors on a held-out set of size $n$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Remark", "weight": 1.0} -->

The main difference between and is that whereas one inequality contains the approximate expected number of errors $\epsilonn$ for $n$ new examples the other contains the actual number of errors $k$ on $n$ examples. Several researchers have found that the hold-out estimate is surprisingly difficult to beat; however, like the ICP of this section, it is not example conditional at all.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark", "weight": 1.0} -->

Inequality can be rewritten as In combination with inequality 2. in Langford, p. 278, this shows that Proposition 2a will continue to hold if is replaced by The last inequality is weaker than for small $\epsilon$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Conditional inductive conformal predictors", "weight": 1.0} -->

The motivation behind conditional inductive conformal predictors is that ICPs do not always achieve the required probability $\epsilon$ of error $Y_{l + 1} \notin {\Gamma^{\epsilon}{(Z_{1},\ldots,Z_{l},X_{l + 1})}}$ conditional on ${(X_{l + 1},Y_{l + 1})} \in E$ for important sets $E \subseteq \mathbf{Z}$. This is often undesirable. If, e.g., our set predictor is valid at the significance level $5\%$ but makes an error with probability $10\%$ for men and $0\%$ for women, both men and women can be unhappy with calling $5\%$ the probability of error. Moreover, in many problems we might want different significance levels for different regions of the example space: e.g., in the problem of spam detection (considered in Section 6) classifying spam as email usually makes much less harm than classifying email as spam.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Conditional inductive conformal predictors", "weight": 1.0} -->

An *inductive $m$-taxonomy* is a measurable function $K:{{\mathbf{Z}^{m} \times \mathbf{Z}}\rightarrow\mathbf{K}}$, where $\mathbf{K}$ is a measurable space. Usually the *category* $K{({(z_{1},\ldots,z_{m})},z)}$ of an example $z$ is a kind of classification of $z$, which may depend on the proper training set $(z_{1},\ldots,z_{m})$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Conditional inductive conformal predictors", "weight": 1.0} -->

The *conditional inductive conformal predictor* (conditional ICP) corresponding to $K$ and an inductive conformity $m$-measure $A$ is defined as the set predictor, where the p-values $p^{y}$ are now defined by the categories $\kappa$ are defined by and the conformity scores $\alpha$ are defined as before. A *label conditional ICP* is a conditional ICP with the inductive $m$-taxonomy ${K{(\cdot,{(x,y)})}}:=y$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Conditional inductive conformal predictors", "weight": 1.0} -->

The following proposition is the conditional analogue of Proposition 1. ‣ 2 Inductive conformal predictors ‣ Conditional validity of inductive conformal predictors"); in particular, it shows that in classification problems label conditional ICPs achieve label conditional validity.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Object conditional validity", "weight": 1.0} -->

In this section we prove a negative result which says that the requirement of precise object conditional validity cannot be satisfied in a non-trivial way for rich object spaces (such as $\mathbb{R}$). If $P$ is a probability distribution on $\mathbf{Z}$, we let $P_{\mathbf{X}}$ stand for its marginal distribution on $\mathbf{X}$: ${P_{\mathbf{X}}{(A)}}:={P{({A \times \mathbf{Y}})}}$. Let us say that a set predictor $\Gamma$ *has $1 - \epsilon$ object conditional validity*, where $\epsilon \in {}$, if, for all probability distributions $P$ on $\mathbf{Z}$ and $P_{\mathbf{X}}$-almost all $x \in \mathbf{X}$, The Lebesgue measure on $\mathbb{R}$ will be denoted $\Lambda$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Object conditional validity", "weight": 1.0} -->

If $Q$ is a probability distribution, we say that a property $F$ holds for *$Q$-almost all* elements of a set $E$ if ${Q{({E \smallsetminus F})}} = 0$; a *$Q$-non-atom* is an element $x$ such that ${Q{({\{ x\}})}} = 0$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark", "weight": 1.0} -->

Nontrivial set predictors having $1 - \epsilon$ object conditional validity are constructed by McCullagh et al. assuming the Gauss linear model.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments", "weight": 1.0} -->

This section describes some simple experiments on the well-known Spambase data set contributed by George Forman to the UCI Machine Learning Repository. Its overall size is 4601 examples and it contains examples of two classes: email (also written as 0) and spam (also written as 1). Hastie et al. report results of several machine-learning algorithms on this data set split randomly into a training set of size 3065 and test set of size 1536. The best result is achieved by MART.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiments", "weight": 1.0} -->

We randomly permute the data set and divide it into 2602 examples for the proper training set, 999 for the calibration set, and 1000 for the test set. Our split between the proper training, calibration, and test sets, approximately 4:1:1, is inspired by the standard recommendation for the allocation of data into training, validation, and test sets. We consider the ICP whose conformity measure is defined by where $f$ is output by MART and MART's output $f{(x)}$ models the log-odds of spam vs email, which makes the interpretation of as conformity score very natural.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

The R programs used in the experiments described in this section are available from the web site the programs use the gbm package with virtually all parameters set to the default values (given in the description provided in response to `help("gbm")`).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments", "weight": 1.0} -->

The upper left plot in Figure 2 is the scatter plot of the pairs $(p^{email},p^{spam})$ produced by the ICP for all examples in the test set. Email is shown as green noughts and spam as red crosses (and it is noticeable that the noughts were drawn after the crosses). The other two plots in the upper row are for email and spam separately. Ideally, email should be close to the horizontal axis and spam to the vertical axis; we can see that this is often true, with a few exceptions. The picture for the label conditional ICP looks almost identical: see the lower row of Figure 2. However, on the log scale the difference becomes more noticeable: see Figure 3.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Experiments", "weight": 1.0} -->

Table 1 gives some statistics for the numbers of errors, multiple, and empty set predictions in the case of the (unconditional) ICP $\Gamma^{5\%}$ at significance level $5\%$ (we obtain different numbers not only because of different splits but also because MART is randomized; the columns of the table correspond to the pseudorandom number generator seeds 0, 1, 2, etc.). The table demonstrates the validity, (lack of) conditional validity, and efficiency of the algorithm (the latter is of course inherited from the efficiency of MART). We give two kinds of conditional figures: the percentages of errors, multiple, and empty predictions for different labels and for two different kinds of objects. The two kinds of objects are obtained by splitting the object space $\mathbf{X}$ by the value of an attribute that we denote $\$$: it shows the percentage of the character $\$$ in the text of the message.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Experiments", "weight": 1.0} -->

The condition $\$ < {5.55\%}$ was the root of the decision tree chosen both by Hastie et al., who use all attributes in their analysis, and by Maindonald and Braun, who use 6 attributes chosen by them manually. (Both books use the rpart R package for decision trees.)

<!-- chunk {"id": "body-0037", "role": "body", "section": "Experiments", "weight": 1.0} -->

Notice that the numbers of errors, multiple predictions, and empty predictions tend to be greater for spam than for email. Somewhat counter-intuitively, they also tend to be greater for "email-like" objects containing few $\$$ characters than for "spam-like" objects. The percentage of multiple and empty predictions is relatively small since the error rate of the underlying predictor happens to be close to our significance level of $5\%$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Experiments", "weight": 1.0} -->

In practice, using a fixed significance level (such as the standard $5\%$) is not a good idea; we should at least pay attention to what happens at several significance levels. However, experimenting with prediction sets at a fixed significance level facilitates a comparison with theoretical results.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Experiments", "weight": 1.0} -->

Table 2 gives similar statistics in the case of the label conditional ICP. The error rates are now about equal for email and spam, as expected. We refrain from giving similar predictable results for "object conditional" ICP with $\$ < {5.55\%}$ and $\$ > {5.55\%}$ as categories.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Experiments", "weight": 1.0} -->

From the numbers given in the "errors overall" row of Table 1 we can extract the corresponding confidence intervals for the probability of error conditional on the training set and MART's internal coin tosses; these are shown in Figure 7. It can be seen that training conditional validity is not grossly violated. (Notice that the 8 training sets used for producing this figure are not completely independent. Besides, the assumption of randomness might not be completely satisfied: permuting the data set ensures exchangeability but not necessarily randomness.) It is instructive to compare Figure 7 with the "theoretical" Figure 8 obtained from Propositions 2b (the thick blue line) and 2a (the thin red line). The dotted green line corresponds to the significance level $5\%$, and the black dot roughly corresponds to the maximal expected probability of error among 8 randomly chosen training sets. (It might appear that there is a discrepancy between Figures 7 and 8, but choosing different seeds usually leads to smaller numbers of errors than in Figure 7.)

<!-- chunk {"id": "body-0041", "role": "body", "section": "ICPs and ROC curves", "weight": 1.0} -->

This section will discuss a close connection between an important class of ICPs ("probability-type" label conditional ICPs) and ROC curves. Let us say that an ICP or a label conditional ICP is *probability-type* if its inductive conformity measure is defined by where $f$ takes values in $\mathbb{R}$ and $\Delta$ is defined.

<!-- chunk {"id": "body-0042", "role": "body", "section": "ICPs and ROC curves", "weight": 1.0} -->

The reader might have noticed that the two leftmost plots in Figure 2 look similar to a ROC curve. The following proposition will show that this is not coincidental in the case of the lower left one. However, before we state it, we need a few definitions. We will now consider a general binary classification problem and will denote the labels as 0 and 1. For a threshold $c \in {\mathbb{R}}$, the *type I error on the calibration set* is and the *type II error on the calibration set* is (with $0/0$ set, e.g., to $1/2$). Intuitively, these are the error rates for the classifier that predicts $1$ when ${f{(x)}} > c$ and predicts $0$ when ${f{(x)}} < c$; our definition is conservative in that it counts the prediction as error whenever ${f{(x)}} = c$. The *ROC curve* is the parametric curve

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The goal of this paper has been to explore various versions of the requirement of conditional validity. With a small training set, we have to content ourselves with unconditional validity (or abandon any formal requirement of validity altogether). For bigger training sets training conditional validity will be approached by ICPs automatically, and we can approach example conditional validity by using conditional ICPs but making sure that the size of a typical category does not become too small (say, less than 100). In problems of binary classification, we can control false positive and false negative rates by using label conditional ICPs.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The known property of validity of inductive conformal predictors (Proposition 1. ‣ 2 Inductive conformal predictors ‣ Conditional validity of inductive conformal predictors")) can be stated in the traditional statistical language by saying that they are $1 - \epsilon$ expectation tolerance regions, where $\epsilon$ is the significance level. In classical statistics, however, there are two kinds of tolerance regions: $1 - \epsilon$ expectation tolerance regions and PAC-type $1 - \delta$ tolerance regions for a proportion $1 - \epsilon$, in the terminology of Fraser. We have seen (Proposition 2a) that inductive conformal predictors are tolerance regions in the second sense as well (cf. Appendix A).

<!-- chunk {"id": "body-0045", "role": "body", "section": "Conclusion", "weight": 1.5} -->

A disadvantage of inductive conformal predictors is their potential predictive inefficiency: indeed, the calibration set is wasted as far as the development of the prediction rule $f$ in is concerned, and the proper training set is wasted as far as the calibration of conformity scores into p-values is concerned. Conformal predictors use the full training set for both purposes, and so can be expected to be significantly more efficient. (There have been reports of comparable and even better predictive efficiency of ICPs as compared to conformal predictors but they may be unusual artefacts of the methods used and particular data sets.) It is an open question whether we can guarantee training conditional validity under or a similar condition for conformal predictors different from classical tolerance regions. Perhaps no universal results of this kind exist, and different families of conformal predictors will require different methods.
