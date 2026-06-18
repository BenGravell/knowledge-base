## Introduction

This paper continues study of the method of conformal prediction, introduced in Vovk et al. and Saunders et al. and further developed in Vovk et al.. An advantage of the method is that its predictions (which are set rather than point predictions) automatically satisfy a finite-sample property of validity. Its disadvantage is its relative computational inefficiency in many situations. A modification of conformal predictors, called inductive conformal predictors, was proposed in Papadopoulos et al. with the purpose of improving on the computational efficiency of conformal predictors.

Most of the literature on conformal prediction studies the behavior of set predictors in the online mode of prediction, perhaps because the property of validity can be stated in an especially strong form in the on-line mode. The online mode, however, is much less popular in applications of machine learning than the batch mode of prediction. This paper follows the recent papers by Lei et al., Lei and Wasserman, and Lei et al. studying properties of conformal prediction in the batch mode; we, however, concentrate on inductive conformal prediction. The performance of inductive conformal predictors in the batch mode is illustrated using the well-known Spambase data set; for earlier empirical studies of conformal prediction in the batch mode see, e.g., Vanderlooy et al.. The conference version of this paper is published as Vovk.

We will usually be making the *assumption of randomness*, which is standard in machine learning and nonparametric statistics: the available data is a sequence of *examples* generated independently from the same probability distribution $P$. (In some cases we will make the weaker assumption of exchangeability; for some of our results even weaker assumptions, such as conditional randomness or exchangeability, would have been sufficient.) Each example consists of two components: an *object* and a *label*. We are given a *training set* of examples and a new object, and our goal is to predict the label of the new object. (If we have a whole *test set* of new objects, we can apply the procedure for predicting one new object to each of the objects in the test set.)

The two desiderata for inductive conformal predictors are their validity and efficiency: validity requires that the coverage probability of the prediction sets should be at least equal to a preset confidence level, and efficiency requires that the prediction sets should be as small as possible. However, there is a wide variety of notions of validity, since the "coverage probability" is, in general, conditional probability. The simplest case is where we condition on the trivial $\sigma$-algebra, i.e., the probability is in fact unconditional probability, but several other notions of conditional validity are depicted in Figure 1, where T refers to conditioning on the training set, O to conditioning on the test object, and L to conditioning on the test label. The arrows in Figure 1 lead from stronger to weaker notions of conditional validity; U is the sink and TOL is the source (the latter is not shown).

Figure 1: Eight notions of conditional validity. The visible vertices of the cube are U (unconditional), T (training conditional), O (object conditional), L (label conditional), OL (example conditional), TL (training and label conditional), TO (training and object conditional). The invisible vertex is TOL (and corresponds to conditioning on everything).

Inductive conformal predictors will be defined in Section 2. They are automatically valid, in the sense of unconditional validity. It should be said that, in general, the unconditional error probability is easier to deal with than conditional error probabilities; e.g., the standard statistical methods of cross-validation and bootstrap provide decent estimates of the unconditional error probability but poor estimates for the training conditional error probability: see Hastie et al., Section 7.12.

In Section 3 we explore training conditional validity of inductive conformal predictors. Our simple results (Propositions 2a and 2b) are of the PAC type, involving two parameters: the target training conditional coverage probability $1 - \epsilon$ and the probability $1 - \delta$ with which $1 - \epsilon$ is attained. They show that inductive conformal predictors achieve training conditional validity automatically (whereas for other notions of conditional validity the method has to be modified). We give self-contained proofs of Propositions 2a and 2b, but Appendix A explains how they can be deduced from classical results about tolerance regions.

In the following section, Section 4, we introduce a conditional version of inductive conformal predictors and explain, in particular, how it achieves label conditional validity. Label conditional validity is important as it allows the learner to control the set-prediction analogues of false positive and false negative rates. Section 5 is about object conditional validity and its main result is negative: precise object conditional validity cannot be achieved in a useful way unless the test object has a positive probability. Whereas precise object conditional validity is usually not achievable, we should aim for approximate and asymptotic object conditional validity when given enough data.

Section 6 reports on the results of empirical studies for the standard Spambase data set. Section 7 discusses close connections between an important class of ICPs and ROC curves. Section 8 concludes and Appendix A discusses connections with the classical theory of tolerance regions (in particular, it explains how Propositions 2a and 2b can be deduced from classical results about tolerance regions).

## Inductive conformal predictors

The example space will be denoted $\mathbf{Z}$; it is the Cartesian product $\mathbf{X} \times \mathbf{Y}$ of two measurable spaces, the object space and the label space. In other words, each example $z \in \mathbf{Z}$ consists of two components: $z = {(x,y)}$, where $x \in \mathbf{X}$ is its object and $y \in \mathbf{Y}$ is its label. Two important special cases are the problem of *classification*, where $\mathbf{Y}$ is a finite set (equipped with the discrete $\sigma$-algebra), and the problem of *regression*, where $\mathbf{Y} = {\mathbb{R}}$.

Let $(z_{1},\ldots,z_{l})$ be the training set, $z_{i} = {(x_{i},y_{i})} \in \mathbf{Z}$. We split it into two parts, the *proper training set* $(z_{1},\ldots,z_{m})$ of size $m < l$ and the *calibration set* of size $l - m$. An *inductive conformity $m$-measure* is a measurable function $A:{{\mathbf{Z}^{m} \times \mathbf{Z}}\rightarrow{\mathbb{R}}}$; the idea behind the *conformity score* $A{({(z_{1},\ldots,z_{m})},z)}$ is that it should measure how well $z$ conforms to the proper training set. A standard choice is

where $f:{\mathbf{X}\rightarrow\mathbf{Y}^{\prime}}$ is a prediction rule found from $(z_{1},\ldots,z_{m})$ as the training set and $\Delta:{{\mathbf{Y} \times \mathbf{Y}^{\prime}}\rightarrow{\mathbb{R}}}$ is a measure of similarity between a label and a prediction. Allowing $\mathbf{Y}^{\prime}$ to be different from $\mathbf{Y}$ (often $\mathbf{Y}^{\prime} \supset \mathbf{Y}$) may be useful when the underlying prediction method gives additional information to the predicted label; e.g., the MART procedure used in Section 6 gives the logit of the predicted probability that the label is $1$.

### Remark

The idea behind the term "calibration set" is that this set allows us to calibrate the conformity scores for test examples by translating them into a probability-type scale.

The *inductive conformal predictor* (ICP) corresponding to $A$ is defined as the set predictor

where $\epsilon \in {\lbrack 0,1\rbrack}$ is the chosen *significance level* ($1 - \epsilon$ is known as the *confidence level*), the *p-values* $p^{y}$, $y \in \mathbf{Y}$, are defined by

are the conformity scores. Given the training set and a new object $x$ the ICP predicts its label $y$; it *makes an error* if $y \notin {\Gamma^{\epsilon}{(z_{1},\ldots,z_{l},x)}}$.

The random variables whose realizations are $x_{i}$, $y_{i}$, $z_{i}$, $z$ will be denoted by the corresponding upper case letters ($X_{i}$, $Y_{i}$, $Z_{i}$, $Z$, respectively). The following proposition of validity is almost obvious.

### Proposition 1 (Vovk et al., 2005, Proposition 4.1)

If random examples ${Z_{m + 1},\ldots,Z_{l}},$ $Z_{l + 1} = {(X_{l + 1},Y_{l + 1})}$ are exchangeable (i.e., their distribution is invariant under permutations), the probability of error $Y_{l + 1} \notin {\Gamma^{\epsilon}{(Z_{1},\ldots,Z_{l},X_{l + 1})}}$ does not exceed $\epsilon$ for any $\epsilon$ and any inductive conformal predictor $\Gamma$.

In practice the probability of error is usually close to $\epsilon$ (as we will see in Section 6).

## Training conditional validity

As discussed in Section 1, the property of validity of inductive conformal predictors is unconditional. The property of conditional validity can be formalized using a PAC-type 2-parameter definition. It will be convenient to represent the ICP in a slightly different form downplaying the structure $(x_{i},y_{i})$ of $z_{i}$. Define ${\Gamma^{\epsilon}{(z_{1},\ldots,z_{l})}}:={\{{(x,y)}\mid{p^{y} > \epsilon}\}}$, where $p^{y}$ is defined, as before, by and (therefore, $p^{y}$ depends implicitly on $x$). Proposition 1. ‣ 2 Inductive conformal predictors ‣ Conditional validity of inductive conformal predictors") can be restated by saying that the probability of error $Z_{l + 1} \notin {\Gamma^{\epsilon}{(Z_{1},\ldots,Z_{l})}}$ does not exceed $\epsilon$ provided $Z_{1},\ldots,Z_{l + 1}$ are exchangeable.

We consider a canonical probability space in which $Z_{i} = {(X_{i},Y_{i})}$, $i = {1,\ldots,{l + 1}}$, are i.i.d. random examples. A set predictor $\Gamma$ (outputting a subset of $\mathbf{Z}$ given $l$ examples and measurable in a suitable sense) is *$(\epsilon,\delta)$-valid* if, for any probability distribution $P$ on $\mathbf{Z}$,

It is easy to see that ICPs satisfy this property for suitable $\epsilon$ and $\delta$.

### Proposition 2a

Suppose ${\epsilon,\delta} \in {\lbrack 0,1\rbrack}$,

where $n:={l - m}$ is the size of the calibration set, and $\Gamma$ is an inductive conformal predictor. The set predictor $\Gamma^{\epsilon}$ is then $(E,\delta)$-valid. Moreover, for any probability distribution $P$ on $\mathbf{Z}$ and any proper training set ${(z_{1},\ldots,z_{m})} \in \mathbf{Z}^{m}$,

This proposition gives the following recipe for constructing $(\epsilon,\delta)$-valid set predictors. The recipe only works if the training set is sufficiently large; in particular, its size $l$ should significantly exceed ${N:={{({- {\ln\delta}})}/{({2\epsilon^{2}})}}}.$ Choose an ICP $\Gamma$ with the size $n$ of the calibration set exceeding $N$. Then the set predictor $\Gamma^{\epsilon - \sqrt{{({- {\ln\delta}})}/{({2n})}}}$ will be $(\epsilon,\delta)$-valid.

### Proof of Proposition 2a

Let $E \in {(\epsilon,1)}$ (not necessarily satisfying ). Fix the proper training set $(z_{1},\ldots,z_{m})$. By and, the set predictor $\Gamma^{\epsilon}$ makes an error, $z_{l + 1} \notin {\Gamma^{\epsilon}{(z_{1},\ldots,z_{l})}}$, if and only if the number of $i = {{m + 1},\ldots,l}$ such that $\alpha_{i} \leq \alpha^{y}$ is at most $\lfloor{{\epsilon{({n + 1})}} - 1}\rfloor$; in other words, if and only if $\alpha^{y} < \alpha_{(k)}$, where $\alpha_{(k)}$ is the $k$th smallest $\alpha_{i}$ and $k:={{\lfloor{{\epsilon{({n + 1})}} - 1}\rfloor} + 1}$. Therefore, the $P$-probability of the complement of $\Gamma^{\epsilon}{(z_{1},\ldots,z_{l})}$ is $P{({{A{({(z_{1},\ldots,z_{m})},Z)}} < \alpha_{(k)}})}$, where $A$ is the inductive conformity $m$-measure. Set

The $\sigma$-additivity of measures implies that $E^{\prime} \leq E \leq E^{\operatorname{\prime\prime}}$, and $E^{\prime} = E = E^{\operatorname{\prime\prime}}$ unless $\alpha^{\ast}$ is an atom of $A{({(z_{1},\ldots,z_{m})},Z)}$. Both when $E^{\prime} = E$ and when $E^{\prime} < E$, the probability of error will exceed $E$ if an only if $\alpha_{(k)} > \alpha^{\ast}$. In other words, if only if we have at most $k - 1$ of the $\alpha_{i}$ below or equal to $\alpha^{\ast}$. The probability that at most ${k - 1} = {\lfloor{{\epsilon{({n + 1})}} - 1}\rfloor}$ values of the $\alpha_{i}$ are below or equal to $\alpha^{\ast}$ equals ${{\mathbb{P}}{({B_{n}^{\operatorname{\prime\prime}} \leq {\lfloor{{\epsilon{({n + 1})}} - 1}\rfloor}})}} \leq {{\mathbb{P}}{({B_{n} \leq {\lfloor{{\epsilon{({n + 1})}} - 1}\rfloor}})}}$, where $B_{n}^{\operatorname{\prime\prime}} \sim {bin}_{n,E^{\operatorname{\prime\prime}}}$, $B_{n} \sim {bin}_{n,E}$, and ${bin}_{n,p}$ stands for the binomial distribution with $n$ trials and probability of success $p$. (For the inequality, see Lemma 1 below.) By Hoeffding's inequality, the probability of error will exceed $E$ with probability at most

Solving $e^{- {2{({E - \epsilon})}^{2}n}} = \delta$ we obtain that $\Gamma^{\epsilon}$ is $(E,\delta)$-valid whenever is satisfied. ∎

In the proof of Proposition 2a we used the following lemma.

### Lemma 1

Fix the number of trials $n$. The distribution function ${bin}_{n,p}{(K)}$ of the binomial distribution is decreasing in the probability of success $p$ for a fixed $K \in {\{ 0,\ldots,n\}}$.

### Proof

It suffices to check that

is nonpositive for $p \in {}$. The last sum has the same sign as the mean of the function ${f{(k)}}:={k - {np}}$ over the set $k \in {\{ 0,\ldots,K\}}$ with respect to the binomial distribution, and so it remains to notice that the overall mean of $f$ is $0$ and that the function $f$ is increasing. ∎

The inequality in Proposition 2a is simple but somewhat crude as its derivation uses Hoeffding's inequality. The following proposition is the more precise version of Proposition 2a that stops short of that last step.

### Proposition 2b

Let ${\epsilon,\delta,E} \in {\lbrack 0,1\rbrack}$. If $\Gamma$ is an inductive conformal predictor, the set predictor $\Gamma^{\epsilon}$ is $(E,\delta)$-valid provided

where $n:={l - m}$ is the size of the calibration set and ${bin}_{n,E}$ is the cumulative binomial distribution function with $n$ trials and probability of success $E$. If the random variable $A{({(z_{1},\ldots,z_{m})},Z)}$ is continuous, $\Gamma^{\epsilon}$ is $(E,\delta)$-valid if and only if holds.

### Proof

See the left-most expression in and remember that $E^{\operatorname{\prime\prime}} = E$ unless $\alpha^{\ast}$ is an atom of $A{({(z_{1},\ldots,z_{m})},Z)}$. ∎

### Remark

The training conditional guarantees discussed in this section are very similar to those for the hold-out estimate: compare, e.g., Proposition 2b above and Theorem 3.3 in Langford. The former says that $\Gamma^{\epsilon}$ is $(E,\delta)$-valid for

where $\overline{bin}$ is the inverse function to $bin$:

(unless $k = n$, we can also say that ${\overline{bin}}_{n,\delta}{(k)}$ is the only value of $p$ such that ${{bin}_{n,p}{(k)}} = \delta$: cf. Lemma 1 above). And the latter says that a point predictor's error probability (over the test example) does not exceed

with probability at least $1 - \delta$ (over the training set), where $k$ is the number of errors on a held-out set of size $n$. The main difference between and is that whereas one inequality contains the approximate expected number of errors $\epsilonn$ for $n$ new examples the other contains the actual number of errors $k$ on $n$ examples. Several researchers have found that the hold-out estimate is surprisingly difficult to beat; however, like the ICP of this section, it is not example conditional at all.

### Remark

Inequality can be rewritten as

In combination with inequality 2. in Langford, p. 278, this shows that Proposition 2a will continue to hold if is replaced by

The last inequality is weaker than for small $\epsilon$.

## Conditional inductive conformal predictors

The motivation behind conditional inductive conformal predictors is that ICPs do not always achieve the required probability $\epsilon$ of error $Y_{l + 1} \notin {\Gamma^{\epsilon}{(Z_{1},\ldots,Z_{l},X_{l + 1})}}$ conditional on ${(X_{l + 1},Y_{l + 1})} \in E$ for important sets $E \subseteq \mathbf{Z}$. This is often undesirable. If, e.g., our set predictor is valid at the significance level $5\%$ but makes an error with probability $10\%$ for men and $0\%$ for women, both men and women can be unhappy with calling $5\%$ the probability of error. Moreover, in many problems we might want different significance levels for different regions of the example space: e.g., in the problem of spam detection (considered in Section 6) classifying spam as email usually makes much less harm than classifying email as spam.

An *inductive $m$-taxonomy* is a measurable function $K:{{\mathbf{Z}^{m} \times \mathbf{Z}}\rightarrow\mathbf{K}}$, where $\mathbf{K}$ is a measurable space. Usually the *category* $K{({(z_{1},\ldots,z_{m})},z)}$ of an example $z$ is a kind of classification of $z$, which may depend on the proper training set $(z_{1},\ldots,z_{m})$.

The *conditional inductive conformal predictor* (conditional ICP) corresponding to $K$ and an inductive conformity $m$-measure $A$ is defined as the set predictor, where the p-values $p^{y}$ are now defined by

the categories $\kappa$ are defined by

and the conformity scores $\alpha$ are defined as before by. A *label conditional ICP* is a conditional ICP with the inductive $m$-taxonomy ${K{( \cdot,{(x,y)})}}:=y$.

The following proposition is the conditional analogue of Proposition 1. ‣ 2 Inductive conformal predictors ‣ Conditional validity of inductive conformal predictors"); in particular, it shows that in classification problems label conditional ICPs achieve label conditional validity.

### Proposition 3

If random examples ${Z_{m + 1},\ldots,Z_{l},Z_{l + 1}} = {(X_{l + 1},Y_{l + 1})}$ are exchangeable, the probability of error $Y_{l + 1} \notin {\Gamma^{\epsilon}{(Z_{1},\ldots,Z_{l},X_{l + 1})}}$ given the category $K{({(Z_{1},\ldots,Z_{m})},Z_{l + 1})}$ of $Z_{l + 1}$ does not exceed $\epsilon$ for any $\epsilon$ and any conditional inductive conformal predictor $\Gamma$ corresponding to $K$.

## Object conditional validity

In this section we prove a negative result which says that the requirement of precise object conditional validity cannot be satisfied in a non-trivial way for rich object spaces (such as $\mathbb{R}$). If $P$ is a probability distribution on $\mathbf{Z}$, we let $P_{\mathbf{X}}$ stand for its marginal distribution on $\mathbf{X}$: ${P_{\mathbf{X}}{(A)}}:={P{({A \times \mathbf{Y}})}}$. Let us say that a set predictor $\Gamma$ *has $1 - \epsilon$ object conditional validity*, where $\epsilon \in {}$, if, for all probability distributions $P$ on $\mathbf{Z}$ and $P_{\mathbf{X}}$-almost all $x \in \mathbf{X}$,

The Lebesgue measure on $\mathbb{R}$ will be denoted $\Lambda$. If $Q$ is a probability distribution, we say that a property $F$ holds for *$Q$-almost all* elements of a set $E$ if ${Q{({E \smallsetminus F})}} = 0$; a *$Q$-non-atom* is an element $x$ such that ${Q{({\{ x\}})}} = 0$.

### Proposition 4

Suppose $\mathbf{X}$ is a separable metric space equipped with the Borel $\sigma$-algebra. Let $\epsilon \in {}$. Suppose that a set predictor $\Gamma$ has $1 - \epsilon$ object conditional validity. In the case of regression, we have, for all $P$ and for $P_{\mathbf{X}}$-almost all $P_{\mathbf{X}}$-non-atoms $x \in \mathbf{X}$,

In the case of classification, we have, for all $P$, all $y \in \mathbf{Y}$, and $P_{\mathbf{X}}$-almost all $P_{\mathbf{X}}$-non-atoms $x$,

We are mainly interested in the case of a small $\epsilon$ (corresponding to high confidence), and in this case implies that, in the case of regression, prediction intervals (i.e., the convex hulls of prediction sets) can be expected to be infinitely long unless the new object is an atom. In the case of classification, says that each particular $y \in \mathbf{Y}$ is likely to be included in the prediction set, and so the prediction set is likely to be large. In particular, implies that the expected size of the prediction set is a least ${({1 - \epsilon})}|\mathbf{Y}|$.

Of course, the condition that $x$ be a non-atom is essential: if ${P_{\mathbf{X}}{({\{ x\}})}} > 0$, an inductive conformal predictor that ignores all examples with objects different from $x$ will have $1 - \epsilon$ object conditional validity and can give narrow predictions if the training set is big enough to contain many examples with $x$ as their object.

### Remark

Nontrivial set predictors having $1 - \epsilon$ object conditional validity are constructed by McCullagh et al. assuming the Gauss linear model.

### Proof of Proposition 4

The proof will be based on the ideas of Lei and Wasserman.

Suppose does not hold on a measurable set $E$ of $P_{\mathbf{X}}$-non-atoms $x \in \mathbf{X}$ such that ${P_{\mathbf{X}}{(E)}} > 0$. Shrink $E$ in such a way that ${P_{\mathbf{X}}{(E)}} > 0$ still holds but there exists $\delta > 0$ and $C > 0$ such that, for each $x \in E$,

Let $V$ be the total variation distance between probability measures, ${V{(P,Q)}}:={\sup_{A}\left| {{P{(A)}} - {Q{(A)}}} \right|}$; we then have

. Shrink $E$ further so that ${P_{\mathbf{X}}{(E)}} > 0$ still holds but

(This can be done under our assumption that $\mathbf{X}$ is a separable metric space: see Lemma 2 below.) Define another probability distribution $Q$ on $\mathbf{Z}$ by the requirements that ${Q{({A \times B})}} = {P{({A \times B})}}$ for all measurable $A \subseteq {({\mathbf{X} \smallsetminus E})}$, $B \subseteq {\mathbb{R}}$ and ${Q{({A \times B})}} = {{{P_{\mathbf{X}}{(A)}} \times U}{(B)}}$ for all measurable $A \subseteq E$, $B \subseteq {\mathbb{R}}$, where $U$ is the uniform probability distribution on the interval $\lbrack{- {DC}},{DC}\rbrack$ and $D > 0$ will be chosen below. Since ${V{(P,Q)}} \leq {P_{\mathbf{X}}{(E)}}$, we have ${V{(P^{l},Q^{l})}} \leq {\delta/2}$; therefore, by,

for each $x \in E$. The last inequality implies, by Fubini's theorem,

where ${Q_{\mathbf{X}}{(E)}} = {P_{\mathbf{X}}{(E)}} > 0$ is the marginal $Q$-probability of $E$. When $D = {D{({\deltaQ_{\mathbf{X}}{(E)}},C)}}$ is sufficiently large this in turn implies

However, the last inequality contradicts

which follows from $\Gamma$ having $1 - \epsilon$ object conditional validity and the definition of conditional probability.

It remains to consider the case of classification. Suppose does not hold on a measurable set $E$ of $P_{\mathbf{X}}$-non-atoms $x \in \mathbf{X}$ such that ${P_{\mathbf{X}}{(E)}} > 0$. Shrink $E$ in such a way that ${P_{\mathbf{X}}{(E)}} > 0$ still holds but there exists $\delta > 0$ such that, for each $x \in E$,

Without loss of generality we further assume that also holds. Define a probability distribution $Q$ on $\mathbf{Z}$ by the requirements that ${Q{({A \times B})}} = {P{({A \times B})}}$ for all measurable $A \subseteq {({\mathbf{X} \smallsetminus E})}$ and all $B \subseteq \mathbf{Y}$ and that ${Q{({A \times {\{ y\}}})}} = {P_{\mathbf{X}}{(A)}}$ for all measurable $A \subseteq E$ (i.e., modify $P$ setting the conditional distribution of $Y$ given $X \in E$ to the unit mass concentrated at $y$). Then for each $x \in E$ we have

The last inequality contradicts $\Gamma$ having $1 - \epsilon$ object conditional validity. ∎

In the proof of Proposition 4 we used the following lemma.

### Lemma 2

If $Q$ is a probability measure on $\mathbf{X}$, which a separable metric space, $E$ is a set of $Q$-non-atoms such that ${Q{(E)}} > 0$, and $\delta > 0$ is an arbitrarily small number, then there is $E^{\prime} \subseteq E$ such that ${Q{(E^{\prime})}} < \delta$.

### Proof

We can take the intersection of $E$ and an open ball centered at any element of $\mathbf{X}$ for which all such intersections have a positive $Q$-probability. Let us prove that such elements exist. Suppose they do not.

Fix a countable dense subset $A_{1}$ of $\mathbf{X}$. Let $A_{2}$ be the union of all open balls $B$ with rational radii centered at points in $A_{1}$ such that ${Q{({B \cap E})}} = 0$. On one hand, the $\sigma$-additivity of measures implies ${Q{({A_{2} \cap E})}} = 0$. On the other hand, $A_{2} = \mathbf{X}$: indeed, for each $x \in \mathbf{X}$ there is an open ball $B$ of some radius $\delta > 0$ centered at $x$ that satisfies ${Q{({B \cap E})}} = 0$; since $x$ belongs to the radius $\delta/2$ open ball centered at a point in $A_{1}$ at a distance of less than $\delta/2$ from $x$, we have $x \in A_{2}$. This contradicts ${Q{(E)}} > 0$. ∎

Proposition 4 can be extended to randomized set predictors $\Gamma$ (in which case $P^{l}$ and $P^{l + 1}$ in expressions such as and should be replaced by the probability distribution comprising both $P$ and the internal coin tossing of $\Gamma$). This clarifies the provenance of $\epsilon$ in and: $\epsilon$ cannot be replaced by a smaller constant since the set predictor predicting $\mathbf{Y}$ with probability $1 - \epsilon$ and $\varnothing$ with probability $\epsilon$ has $1 - \epsilon$ object conditional validity.

Proposition 4 does not prevent the existence of efficient set predictors that are conditionally valid in an asymptotic sense; indeed, the paper by Lei and Wasserman is devoted to constructing asymptotically efficient and asymptotically conditionally valid set predictors in the case of regression.

## Experiments

This section describes some simple experiments on the well-known Spambase data set contributed by George Forman to the UCI Machine Learning Repository. Its overall size is 4601 examples and it contains examples of two classes: email (also written as 0) and spam (also written as 1). Hastie et al. report results of several machine-learning algorithms on this data set split randomly into a training set of size 3065 and test set of size 1536. The best result is achieved by MART.

We randomly permute the data set and divide it into 2602 examples for the proper training set, 999 for the calibration set, and 1000 for the test set. Our split between the proper training, calibration, and test sets, approximately 4:1:1, is inspired by the standard recommendation for the allocation of data into training, validation, and test sets. We consider the ICP whose conformity measure is defined by where $f$ is output by MART and

MART's output $f{(x)}$ models the log-odds of spam vs email,

which makes the interpretation of as conformity score very natural.

The R programs used in the experiments described in this section are available from the web site http://alrw.net; the programs use the gbm package with virtually all parameters set to the default values (given in the description provided in response to `help("gbm")`).

The upper left plot in Figure 2 is the scatter plot of the pairs $(p^{email},p^{spam})$ produced by the ICP for all examples in the test set. Email is shown as green noughts and spam as red crosses (and it is noticeable that the noughts were drawn after the crosses). The other two plots in the upper row are for email and spam separately. Ideally, email should be close to the horizontal axis and spam to the vertical axis; we can see that this is often true, with a few exceptions. The picture for the label conditional ICP looks almost identical: see the lower row of Figure 2. However, on the log scale the difference becomes more noticeable: see Figure 3.

Figure 2: Scatter plots of the pairs (pemail,pspam) for all examples in the test set (left plots), for email only (middle), and for spam only (right). The three upper plots are for the ICP and the three lower ones are for the label conditional ICP.

Figure 3: The analogue of Figure 2 on the log scale.

Table 1 gives some statistics for the numbers of errors, multiple, and empty set predictions in the case of the (unconditional) ICP $\Gamma^{5\%}$ at significance level $5\%$ (we obtain different numbers not only because of different splits but also because MART is randomized; the columns of the table correspond to the pseudorandom number generator seeds 0, 1, 2, etc.). The table demonstrates the validity, (lack of) conditional validity, and efficiency of the algorithm (the latter is of course inherited from the efficiency of MART). We give two kinds of conditional figures: the percentages of errors, multiple, and empty predictions for different labels and for two different kinds of objects. The two kinds of objects are obtained by splitting the object space $\mathbf{X}$ by the value of an attribute that we denote $\$$: it shows the percentage of the character $\$$ in the text of the message. The condition $\$ < {5.55\%}$ was the root of the decision tree chosen both by Hastie et al., who use all attributes in their analysis, and by Maindonald and Braun, who use 6 attributes chosen by them manually. (Both books use the rpart R package for decision trees.)

Notice that the numbers of errors, multiple predictions, and empty predictions tend to be greater for spam than for email. Somewhat counter-intuitively, they also tend to be greater for "email-like" objects containing few $\$$ characters than for "spam-like" objects. The percentage of multiple and empty predictions is relatively small since the error rate of the underlying predictor happens to be close to our significance level of $5\%$.

In practice, using a fixed significance level (such as the standard $5\%$) is not a good idea; we should at least pay attention to what happens at several significance levels. However, experimenting with prediction sets at a fixed significance level facilitates a comparison with theoretical results.

Table 1: Percentage of errors, multiple predictions, and empty predictions on the full test set and separately on email and spam. The results are given for various values of the seed for the R (pseudo)random number generator (RNG); column “Average” gives the average values for all 8 seeds 0–7.

Table 2 gives similar statistics in the case of the label conditional ICP. The error rates are now about equal for email and spam, as expected. We refrain from giving similar predictable results for "object conditional" ICP with $\$ < {5.55\%}$ and $\$ > {5.55\%}$ as categories.

Table 2: The analogue of a subset of Table 1 in the case of the label conditional ICP.

Figure 4 gives the calibration plots of the ICP for the test set. It shows approximate validity even for email and spam separately, except for the all-important lower-left corners. The latter are shown separately in Figure 5, where the lack of conditional validity becomes evident; cf. Figure 6 for the label conditional ICP.

Figure 4: The calibration plot for the test set overall, the email in the test set, and the spam in the test set (for the first 8 seeds, 0–7).

Figure 5: The lower left corners of the plots in Figure 4.

Figure 6: The analogue of Figure 5 for the label conditional ICP.

From the numbers given in the "errors overall" row of Table 1 we can extract the corresponding confidence intervals for the probability of error conditional on the training set and MART's internal coin tosses; these are shown in Figure 7. It can be seen that training conditional validity is not grossly violated. (Notice that the 8 training sets used for producing this figure are not completely independent. Besides, the assumption of randomness might not be completely satisfied: permuting the data set ensures exchangeability but not necessarily randomness.) It is instructive to compare Figure 7 with the "theoretical" Figure 8 obtained from Propositions 2b (the thick blue line) and 2a (the thin red line). The dotted green line corresponds to the significance level $5\%$, and the black dot roughly corresponds to the maximal expected probability of error among 8 randomly chosen training sets. (It might appear that there is a discrepancy between Figures 7 and 8, but choosing different seeds usually leads to smaller numbers of errors than in Figure 7.)

Figure 7: Confidence intervals for training conditional error probabilities: 95% in black (thin lines) and 80% in blue (thick lines). The 5% significance level is shown as the horizontal red line.

Figure 8: The probability of error E vs δ from Propositions 2b (the thick blue line) and 2a (the thin red line), where ϵ = 0.05 and n = 999.

## ICPs and ROC curves

This section will discuss a close connection between an important class of ICPs ("probability-type" label conditional ICPs) and ROC curves. Let us say that an ICP or a label conditional ICP is *probability-type* if its inductive conformity measure is defined by where $f$ takes values in $\mathbb{R}$ and $\Delta$ is defined by.

The reader might have noticed that the two leftmost plots in Figure 2 look similar to a ROC curve. The following proposition will show that this is not coincidental in the case of the lower left one. However, before we state it, we need a few definitions. We will now consider a general binary classification problem and will denote the labels as 0 and 1. For a threshold $c \in {\mathbb{R}}$, the *type I error on the calibration set* is

and the *type II error on the calibration set* is

(with $0/0$ set, e.g., to $1/2$). Intuitively, these are the error rates for the classifier that predicts $1$ when ${f{(x)}} > c$ and predicts $0$ when ${f{(x)}} < c$; our definition is conservative in that it counts the prediction as error whenever ${f{(x)}} = c$. The *ROC curve* is the parametric curve

### Proposition 5

In the case of a probability-type label conditional ICP, for any object $x \in \mathbf{X}$, the distance between the pair $(p^{0},p^{1})$ (see ) and the ROC curve is at most

where $n^{y}$ is the number of examples in the calibration set labelled as $y$.

### Proof

Let $c:={f{(x)}}$. Then we have

where $n_{\geq}^{0}$ is the number of examples $(x_{i},y_{i})$ in the calibration set such that $y_{i} = 0$ and ${f{(x_{i})}} \geq c$ and $n_{\leq}^{1}$ is the number of examples in the calibration set such that $y_{i} = 1$ and ${f{(x_{i})}} \leq c$. It remains to notice that the point $\left( {n_{\geq}^{0}/n^{0}},{n_{\leq}^{1}/n^{1}} \right)$ belongs to the ROC curve: the horizontal (resp. vertical) distance between this point and does not exceed $1/{({n^{0} + 1})}$ (resp. $1/{({n^{1} + 1})}$), and the overall Euclidean distance does not exceed. ∎

So far we have discussed the *empirical ROC curve*: and are the empirical probabilities of errors of the two types on the calibration set. It corresponds to the estimate $k/n$ of the parameter of the binomial distribution based on observing $k$ successes out of $n$. The minimax estimate is ${({k + {1/2}})}/{({n + 1})}$, and the corresponding ROC curve where $\alpha{(c)}$ and $\beta{(c)}$ are defined by and with the numerators increased by $\frac{1}{2}$ and the denominators increased by $1$ will be called the *minimax ROC curve*. Notice that for the minimax ROC curve we can put a coefficient of $\frac{1}{2}$ in front of. Similarly, when using the Laplace estimate ${({k + 1})}/{({n + 2})}$, we obtain the *Laplace ROC curve*. See Figure 9 for the lower left corner of the lower left plot of Figure 2 with different ROC curves added to it.

Figure 9: The lower left corner of the lower left plot of Figure 2 with the empirical (solid blue), minimax (dashed blue), and Laplace (dotted blue) ROC curves.

In conclusion of our study of the Spambase data set, we will discuss the asymmetry of the two kinds of error in spam detection: classifying email as spam is much more harmful than letting occasional spam in. A reasonable approach is to start from a small number $\epsilon > 0$, the maximum tolerable percentage of email classified as spam, and then to try to minimize the percentage of spam classified as email under this constraint. The standard way of doing this is to classify a message $x$ as spam if and only if ${f{(x)}} \geq c$, where $c$ is the point on the ROC curve corresponding to the type I error $\epsilon$. It is not clear what this means precisely, since we only have access to an estimate of the true ROC curve (and even on the true ROC curve such a point might not exist). But roughly, this means classifying $x$ as spam if $f{(x)}$ exceeds the $k$th largest value in the set $\{\alpha_{i}\mid{i \in {{\{{m + 1},\ldots,l\}}\& y_{i}} = \text{email}}\}$, where $k$ is close to $\epsilonn^{0}$ and $n^{0}$ is the size of this set (i.e., the number of email in the calibration, or validation, set). To make this more precise, we can use the "one-sided label conditional ICP" classifying $x$ as spam if and only if^11^1In practice, we might want to improve the predictor by adding another step and changing the classification from spam to email if $p^{1}$ is also small, in which case $x$ looks neither like spam nor email. In view of Proposition 5, however, this step can be disregarded for probability-type ICP unless $\epsilon$ is very lax. $p^{0} \leq \epsilon$ for $x$. According to, this means that we classify $x$ as spam if and only if $f{(x)}$ exceeds the $k$th largest value in the set $\{\alpha_{i}\mid{i \in {{\{{m + 1},\ldots,l\}}\& y_{i}} = \text{email}}\}$, where $k:={\lfloor{\epsilon{({n^{0} + 1})}}\rfloor}$. The advantage of this version of the standard method is that it guarantees that the probability of mistaking email for spam is at most $\epsilon$ (see Proposition 3) and also enjoys the training conditional version of this property given by Proposition 2a (more accurately, its version for label conditional ICPs).

## Conclusion

The goal of this paper has been to explore various versions of the requirement of conditional validity. With a small training set, we have to content ourselves with unconditional validity (or abandon any formal requirement of validity altogether). For bigger training sets training conditional validity will be approached by ICPs automatically, and we can approach example conditional validity by using conditional ICPs but making sure that the size of a typical category does not become too small (say, less than 100). In problems of binary classification, we can control false positive and false negative rates by using label conditional ICPs.

The known property of validity of inductive conformal predictors (Proposition 1. ‣ 2 Inductive conformal predictors ‣ Conditional validity of inductive conformal predictors")) can be stated in the traditional statistical language by saying that they are $1 - \epsilon$ expectation tolerance regions, where $\epsilon$ is the significance level. In classical statistics, however, there are two kinds of tolerance regions: $1 - \epsilon$ expectation tolerance regions and PAC-type $1 - \delta$ tolerance regions for a proportion $1 - \epsilon$, in the terminology of Fraser. We have seen (Proposition 2a) that inductive conformal predictors are tolerance regions in the second sense as well (cf. Appendix A).

A disadvantage of inductive conformal predictors is their potential predictive inefficiency: indeed, the calibration set is wasted as far as the development of the prediction rule $f$ in is concerned, and the proper training set is wasted as far as the calibration of conformity scores into p-values is concerned. Conformal predictors use the full training set for both purposes, and so can be expected to be significantly more efficient. (There have been reports of comparable and even better predictive efficiency of ICPs as compared to conformal predictors but they may be unusual artefacts of the methods used and particular data sets.) It is an open question whether we can guarantee training conditional validity under or a similar condition for conformal predictors different from classical tolerance regions. Perhaps no universal results of this kind exist, and different families of conformal predictors will require different methods.
