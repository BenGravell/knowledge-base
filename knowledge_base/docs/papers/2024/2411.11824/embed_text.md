## Introduction

Conformal prediction is a statistical technique that quantifies uncertainty in predictive models, without any assumptions at all on the model and with minimal assumptions on the distribution of the data. Predictive models can be prone to unexpected inaccuracies and errors, complicating their practical usage. Conformal prediction guards against these issues, giving rigorous error bounds on predictions. This book presents the foundational statistical theory of conformal prediction and related methods.

## Uncertainty quantification for prediction

We now describe the problem of uncertainty quantification for prediction. Consider a sequence of data points (X i, Y i) ∈ X × Y, for i = 1,..., n. Here, X i is the feature vector and Y i is the response variable. We are then given a new feature vector X n +1, with the task of predicting its corresponding response value Y n +1 (which is unobserved). Given a predictive model ˆ f, we can return a prediction ˆ f (X n +1). To communicate our uncertainty in this prediction, we can provide a margin of error around our prediction ˆ f (X n +1), or more generally, a prediction set C (X n +1) ⊆ Y. A common aim for this set is the property of marginal coverage, where α ∈ is a user-specified error level (e.g., α = 0. 1 for 90% coverage). If the size of the set C (X n +1) is large, this indicates high uncertainty in the prediction.

Conformal prediction is a technique for constructing sets C ( X n +1 ) that satisfy (1.1) under no assumptions on ˆ f or the form of the data distribution. In particular, if the underlying predictive model ˆ f is a poor fit to the data, then the accompanying set C ( X n +1 ) will be large-potentially even infinite. On the other hand, accurate models will result in smaller sets, and under additional conditions can lead to stronger notions of coverage than that in (1.1). In either case, the role of conformal prediction is to accurately quantify the level of uncertainty present when using a predictive model on the current data distribution.

## Preview of split conformal prediction

We begin by presenting a version of the split conformal prediction algorithm. As before, suppose we have training data points ( X i, Y i ) for i = 1,..., n, and a test point ( X n +1, Y n +1 ). Taking n to be an even number for simplicity, the training data will be split into n/ 2 points used for model fitting, and n/ 2 points used for calibration.

We consider the setting Y = R -that is, a regression problem with a real-valued response.We can construct prediction intervals for Y n +1 via the following algorithm (which is one specific case of the more general split conformal algorithm, presented in Section 1.3 below).

## Algorithm 1.1: Split conformal prediction, special case

1. Use data (X i, Y i) for i = 1,..., n/ 2 to fit a predictive model ˆ f: X → R. 2. For i = n/ 2 + 1,..., n, compute the absolute residual S i = | Y i -ˆ f (X i) |. 3. Sort S n/ 2+1,..., S n in increasing order, and let ˆ q be the ⌈ (1 -α)(n 2 +1) ⌉ -th element in the sorted list. 4. Return the prediction interval C (X n +1) = [ˆ f (X n +1) -ˆ q, ˆ f (X n +1) + ˆ q].

This algorithm's output is the prediction interval C ( X n +1 ) = [ ˆ f ( X n +1 ) -ˆ q, ˆ f ( X n +1 ) + ˆ q ], which represents our uncertainty about the prediction ˆ f ( X n +1 ) for the target value Y n +1.

The predictive model ˆ f in the first step of Algorithm 1.1 can be any function that is based only on ( X 1, Y 1 ),..., ( X n/ 2, Y n/ 2 ). For example, it might be a linear model fitted via least-squares regression. The final set is an interval centered at the model's prediction, ˆ f ( X n +1 ) ± ˆ q. To interpret this choice of ˆ q, we observe ˆ q is chosen such that the intervals [ ˆ f ( X i ) -ˆ q, ˆ f ( X i ) + ˆ q ] contain the response variable Y i for approximately a (1 -α ) fraction of the points i = n/ 2 + 1,..., n (i.e., the data points that were not used for training the model ˆ f ).

If the data points are independent and identically distributed (i.i.d.), then for any choice of the predictive model ˆ f, the prediction set above satisfies marginal coverage:

## Theorem 1.2: Split conformal coverage guarantee, special case

Suppose ( X 1, Y 1 ),..., ( X n +1, Y n +1 ) are i.i.d., and let C ( X n +1 ) be the output of Algorithm 1.1. Then the marginal coverage property (1.1) holds.

In other words, if the data points are drawn i.i.d. from any distribution, then split conformal prediction offers marginal coverage-even if the fitted model ˆ f is an extremely poor fit to the data, and even if the sample size n is small. In fact, while the i.i.d. assumption is sufficient here, it is stronger than necessary-a weaker property known as exchangeability, which will be introduced in Chapter 2, is the fundamental property required for conformal prediction.

## Conformal scores

The example above builds intuition for valid coverage with any predictive model and dataset, but the exact form of the algorithm above is rather constrained: by construction, the prediction set will always be of the form ˆ f ( X n +1 ) ± ˆ q, i.e., a band of constant width around the fitted predictive model ˆ f; see Figure 1.1. Fortunately, the conformal framework is much more flexible than the above example, allowing for nearly unlimited choice in how C ( X n +1 ) is constructed. The key concept is the conformal score function, which is a function s ( x, y ) such that larger values indicate that the data point ( x, y ) does not agree with (does not 'conform' to) the trends observed in the training data. For instance, given a fitted model ˆ f, a common choice for s is the residual score, s ( x, y ) = | y -ˆ f ( x ) |, since a large value of the residual indicates that ( x, y ) does not appear to agree with the model trained on the available data. We will give additional examples of score functions shortly.

We now state a more general version of the split conformal prediction algorithm, using a generic conformal score function. As before, we again assume n is even for simplicity.

## Algorithm 1.3: Split conformal prediction, general case

1. Use data (X i, Y i) for i = 1,..., n/ 2 to construct a conformal score function s: X ×Y → R, with the intuition that s (x, y) measures how unusual (x, y) is based on a model fit on data from this split. 2. For i = n/ 2 + 1,..., n, compute the score S i = s (X i, Y i). 3. Sort S n/ 2+1,..., S n in increasing order, and let ˆ q be the ⌈ (1 -α)(n 2 +1) ⌉ -th element in the sorted list. 4. Return the prediction set C (X n +1) = { y ∈ Y: s (X n +1, y) ≤ ˆ q }.

It may not be immediately clear that the set C ( X n +1 ) can be computed efficiently, since it nominally requires iterating through all y ∈ Y. However, in many cases, it simplifies to an interval that can be computed explicitly, just as in Algorithm 1.1-we will see some examples below.

While we are referring to split conformal prediction as 'an algorithm', the flexibility in choosing the score function s means that we should actually think of this as a family of algorithms-any given choice of the conformal score function s specifies a particular algorithm. For example, by choosing the residual score function s ( x, y ) = | y -ˆ f ( x ) |, we can obtain Algorithm 1.1 as a special case of Algorithm 1.3.

The following result states that the marginal coverage guarantee holds with any score function.

## Theorem 1.4: Split conformal coverage guarantee, general case

Suppose ( X 1, Y 1 ),..., ( X n +1, Y n +1 ) are i.i.d., and let C ( X n +1 ) be the output of Algorithm 1.3. Then the marginal coverage property (1.1) holds.

Although any score function results in marginal coverage, in practice the choice of the conformal score function s is the single most important decision when implementing conformal prediction: different choices can lead to very different procedures, and a poorly chosen conformal score function s can lead to uninformative or overly large prediction sets. We next outline several of the most common conformal score functions and give intuition for the properties of the resulting conformal prediction method. Figure 1.1 gives an illustration of the sets resulting from some of these conformal score functions.

The residual score. We first return to the residual score, s ( x, y ) = | y -ˆ f ( x ) |, as used in Algorithm 1.1 above, where ˆ f is fitted on the data points ( X 1, Y 1 ),..., ( X n/ 2, Y n/ 2 ). This construction will always return a prediction set C ( X n +1 ) of the same form: a symmetric interval, centered around the point prediction ˆ f ( X n +1 ) with the same width for all values of X n +1. This is a simple and natural choice. However, the width of the interval does not adapt to X, making it far from ideal in many settings-for instance, if the response variable Y has higher or lower noise variance depending on the value of X.

The scaled residual score. We can modify the residual score to result in intervals of different width (e.g., in settings where the variance of Y is different at different values of X). This construction will again use a trained predictive model ˆ f, and will also require an estimate ˆ σ (x) of the scale of the noise in Y given X = x (e.g., an estimate of the standard deviation), where ˆ f and ˆ σ are both fitted using data points (X 1, Y 1),..., (X n/ 2, Y n/ 2). The scaled residual score is then defined as Figure 1.1: The conformal score function determines the shape of the sets. The shaded band is a visualization of the prediction set C (X n +1) ⊆ Y as a function of X n +1 ∈ X. On the left, the residual score gives a fixed-width band around a fitted model ˆ f. In the middle, the scaled residual score gives a symmetric band that adapts to the non-constant noise variance. On the right, the CQR score gives an asymmetric band that follows the quantiles of the distribution. and results in the prediction set This can lead to prediction intervals that are a better fit to the data as compared to the residual score, since the function ˆ σ (x) can capture the nonconstant variance of the noise in Y.

The CQR score. Both the residual score and the scaled residual score will return symmetric intervals, which may be a poor fit for certain data distributions. This motivates a more nonparametric approach towards choosing the score. Suppose we use the data points (X 1, Y 1),..., (X n/ 2, Y n/ 2) to obtain an estimate ˆ τ (x; α/ 2) of the α/ 2 quantile of the distribution of Y given X = x, and an estimate ˆ τ (x; 1 -α/ 2) of the 1 -α/ 2 quantile-for instance, we might fit these models by running a quantile regression method. A straightforward way to use these estimates when confronted with a test point X n +1 would be to output the interval [ˆ τ (X n +1; α/ 2), ˆ τ (X n +1; 1 -α/ 2)], using the estimated quantiles-but this may not give a coverage level of 1 -α if the estimates ˆ τ are imperfect. Instead, the conformalized quantile regression (CQR) method uses these initial quantile estimates to construct a conformal score, so that the resulting prediction set is an adjusted version of the initial interval. Specifically, the CQR score is given by which is the signed distance of y to the interval [ˆ τ (x; α/ 2), ˆ τ (x; 1 -α)]. With this choice of s, the resulting conformal prediction set takes the form That is, conformal prediction with this score function takes the prediction interval from the initial quantile estimates, and then either inflates it if ˆ q is positive or shrinks it if ˆ q is negative.

The high-probability score. The split conformal prediction algorithm can also be applied to classification problems, i.e., when the response variable takes values in a discrete set. Suppose that Y = { 1,..., K } is the set of possible labels, and suppose we have an estimate ˆ π (y | x) of the probability of label Y = y given features X = x, which was trained on the data points (X 1, Y 1),..., (X n/ 2, Y n/ 2). The high-probability score is then given by It is important to note that the score is the negative of the estimated probability; this is because a conformal score is intended to return larger values when the data point (x, y) appears more unlikely, i.e., when ˆ π (y | x) is small. If we use this score for split conformal prediction, the resulting prediction set is given by which is the set of all labels y ∈ { 1,..., K } with a sufficiently high estimated probability, given the test point features X n +1. Of course, this type of score function may also be used in the case of a continuous response Y, if we use an estimated conditional density in place of the estimated conditional probability.

At this point, we have seen that conformal prediction can provide a marginal coverage guarantee with only weak assumptions, and can leverage the power of arbitrary predictive models-the better the predictive model, the more precise the prediction set will be. Nonetheless, there are many natural questions at this stage. Is it necessary to split the data into two parts, one for model fitting and one for the calibration of confidence intervals, as in split conformal prediction-or can the data splitting step be avoided? Which conformal score functions are optimal? Can the method be extended to cases where the data are not i.i.d.? Can distribution-free guarantees be extended to address statistical problems beyond predictive coverage? We will address these questions throughout the book as we develop conformal prediction in full generality.

## The conformal prediction framework in context

This book discusses the statistical theory underlying conformal prediction and related techniques for providing uncertainty quantification for our predictive models-but of course, this question has long been studied in the statistics literature. What distinguishes the conformal prediction framework from other methods?

As we have seen above, conformal prediction guarantees a marginal coverage property for data drawn i.i.d. from any distribution. We do not need to place conditions on the distribution (such as smoothness, or, a parametric model)-because of this, conformal prediction is often described as a distribution-free approach to inference. Moreover, we do not need to place conditions on the underlying model fitted to the data (such as assuming that ˆ f is a consistent estimator of the true association between Y and X ), and the result is finite-sample, in the sense that it holds at any value of n rather than offering only an asymptotic guarantee.

Conformal prediction is closely related to the field of nonparametric statistics, which has also aimed to provide statistical methods that can flexibly handle data distributions that do not fall within some simple parametric model. However, there are some fundamental differences between these fields. In nonparametric and semiparametric statistics, most methods and results rely on regularity conditions that, while weaker than a parametric model assumption, are nonetheless much stronger than the minimal assumptions required by conformal prediction. For example, in nonparametric statistics it is common to assume smoothness conditions on the distribution of the data. With these types of assumptions, it is often possible to provide guarantees not only for predictive inference but also for estimation (for instance, estimating the mean of Y given X ). By contrast, exchangeability is a far weaker assumption than what is usually considered in nonparametric statistics. Without regularity conditions, it is still possible to provide useful and powerful methods for predictive inference, as we have seen with the marginal coverage guarantee for split conformal, above-but, as we will see in some of the hardness results presented in Chapter 4 and in Part IV of this book, other types of inference questions become more challenging or even impossible.

Conformal prediction is intimately connected with permutation testing-we will soon see that it can be formulated as the inversion of a particular permutation test. It is also closely connected to quantile estimation and distribution estimation: a natural use of quantile estimation is to give prediction intervals for test points, although such a procedure would again require assumptions on the regularity of the distribution in order to have guaranteed coverage. Farther afield are resampling approaches, such as the bootstrap and cross-validation. Unlike conformal prediction, these are most commonly applied for confidence intervals on functionals of the distribution, and require regularity conditions for validity. However, we will explore distribution-free variants of cross-validation for the purpose of predictive inference later on in the book.

## Scope of this book

After this introductory chapter, the remainder of Part I is an introduction to exchangeability, with a glossary of facts and properties that will be useful for the statistical results developed later in the book. We pay special attention to permutation tests, since conformal prediction can be reframed as inverting a permutation test. These tools will be critical to many of the proofs and intuitions in the remainder of the book.

Part II of the book then turns to the conformal prediction framework. In particular, we discuss full conformal prediction, a generalization of the split conformal prediction method we have already introduced, which reveals the basic statistical logic at play. We then describe stronger properties than marginal coverage, with a mix of positive results for various methods, and hardness results that show the limits of what is possible without more assumptions. We also examine conformal prediction from a model-based perspective, to see how prior knowledge about the distribution of the data can be incorporated into the workflow of the conformal prediction framework.

Part III of the book focuses on a broad range of different extensions to the conformal prediction methodology, including cross-validation based methods within the conformal framework, weighted versions of conformal prediction that allow us to move beyond the i.i.d. setting, online versions of conformal methods that are designed for streaming data, and computational shortcuts for conformal prediction. We also briefly cover additional topics such as variants of conformal prediction that can handle broader notions of risk, and connections with selective inference, multiple testing, and model aggregation-these topics are a sample of some recent work in the field, and are suggestive of the many directions for continued study.

Finally, in Part IV, we depart from our focus on predictive coverage, and study the problem of distribution-free inference for a range of other questions: estimating a regression function, calibrating probability estimates, and testing conditional independence.

## Bibliographic notes

We refer the reader to the bibliographic notes in Chapter 3 for references about the most common variants of conformal prediction and a detailed history of the field. Here, we will briefly mention some other textbooks and tutorials on conformal prediction. The first such book was Algorithmic Learning in a Random World by Vovk et al., which introduced the mathematical framework behind conformal prediction. More recent textbooks and tutorials include the works of Shafer and Vovk, Balasubramanian et al., and Angelopoulos and Bates. Turning to the specific algorithms in this section, split conformal prediction is first described in Papadopoulos et al., with the residual score function as a canonical example. The same paper also introduced the scaled residual score function as an alternative; see also Lei et al.. Lastly, the CQR score function is due to Romano et al., while the high-probability score is studied in Sadinle et al. (see also earlier work by Papadopoulos, which studies a related score).

## Exercises

- 1.1 Consider split conformal prediction with Y = R. Suppose we are given an initial model ˆ f: X → R. Construct a score function s (x, y) that would yield intervals that are twice as wide above ˆ f as below ˆ f, i.e., intervals of the form C (x) = [ˆ f (x) -γ, ˆ f (x) + 2 γ] for some γ. - 1.2 Consider split conformal prediction in the setting of a multivariate response, Y = R d. Suppose we are given an initial model ˆ f: X → R d, which returns predictions ˆ f (x) = (ˆ f (x) 1,..., ˆ f (x) d). Construct a score function s (x, y) that would return prediction sets of the form 1.3 Suppose we have a regression problem with Y = R and two models ˆ f 1: X → R and ˆ f 2: X → R. Consider split conformal prediction with the score function s (x, y) = min {| y -ˆ f 1 (x) |, | y -ˆ f 2 (x) |}. Derive an explicit expression for the set C (X n +1) in terms of ˆ f 1, ˆ f 2, and ˆ q. What is the shape of the prediction set when ˆ q is small, or when ˆ q is large? Briefly explain why this might be attractive if we expect the distribution of Y given X = x to be bimodal for some values of x.

## Chapter 2

## Exchangeability and Permutations

In this chapter, we provide an introduction to the idea of exchangeability, laying the core mathematical foundation of conformal prediction and many related methodologies. Exchangeability is a property of a sequence of random variables-informally, it expresses the idea that the sequence is equally likely to appear in any order. A formal definition is as follows:

## Definition 2.1: Exchangeability

Let Z 1,..., Z n ∈ Z be random variables with a joint distribution. We say that the random vector (Z 1,..., Z n) is exchangeable if, for every permutation σ ∈ S n, where d = denotes equality in distribution, and S n is the set of all permutations on [n]:= { 1,..., n }.

Similarly, we say that an infinite sequence Z 1, Z 2, · · · ∈ Z is exchangeable if ( Z 1,..., Z n ) is exchangeable for every n ≥ 1.

The elements of an exchangeable sequence are identically distributed, but not necessarily independent. Exchangeability constrains the dependence structure so that all permutations are equally likely. Throughout this book, we might interchangeably say that a random vector ( Z 1,..., Z n ) is exchangeable, or that the random variables Z 1,..., Z n are exchangeable.

Exchangeability can arise in a broad range of scenarios. In particular, exchangeability of a sequence Z 1,..., Z n arises in the following important special cases:

- Z 1,..., Z n are sampled uniformly without replacement from a finite set { z 1,..., z N } ⊆ Z. - Z 1,..., Z n are drawn i.i.d. from a distribution P on Z.

However, these common scenarios are far from exhaustive. As an intuitive example, consider the distribution on (Z 1, Z 2) ∈ { 0, 1 } 2 given by (Here and throughout the book, we will use the notation δ z to denote the point mass at a value z, i.e., the probability distribution that places probability 1 on the value z. This is sometimes referred to as the Dirac delta function.) In other words, the joint distribution of (Z 1, Z 2) is defined by the probability mass function This joint distribution is exchangeable, but cannot be expressed either via sampling without replacement or via i.i.d. sampling. It instead illustrates a different way that exchangeability can arise: any mixture of exchangeable distributions is itself an exchangeable distribution. Indeed, the above example can be derived as a mixture, where with probability 1 2 we sample Z 1, Z 2 uniformly without replacement from the set { 0, 1 }, and with probability 1 2 we draw Z 1, Z 2 i.i.d. from the Bernoulli (0. 5) distribution.

As a technical note, here and throughout the remainder of the book, wherever needed we will assume mild regularity conditions on the underlying measure spaces, without comment: for instance, the assumption that σ -algebras are countably generated, and the existence of regular conditional probabilities (i.e., existence of measurable functions such as x ↦→ P ( Y ∈ A | X = x ) ), both of which hold in most common settings, such as R d or any standard Borel space.

## Alternative characterizations of exchangeability

Exchangeability can be formally described in a number of different ways. Here, we give several characterizations and properties of exchangeability of a random vector ( Z 1,..., Z n ), to help build intuition.

Symmetry of the joint density. Exchangeability has a simple characterization if the random vector (Z 1,..., Z n) is either discrete, or has a joint density. First, supposing Z is a countable space so that the Z i 's are discrete, let p: Z n → be the probability mass function for the joint distribution of (Z 1,..., Z n). Then this joint distribution is exchangeable if and only if Analogously, if Z = R and the random vector (Z 1,..., Z n) has a joint density f (with respect to Lebesgue measure on R n), then this joint distribution is exchangeable if and only if Conditioning on the order statistics. For this next interpretation, we will consider the special case of real-valued random variables, Z = R. In this setting, we define the order statistics Z ≤ · · · ≤ Z (n) as the sorted values of the vector (Z 1,..., Z n). In the simple setting where these n values are distinct almost surely, exchangeability implies that, conditioning on the order statistics, the random vector (Z 1,..., Z n) is equally likely to be any one of the n ! unique permutations of the order statistics. More generally, without assuming that the Z i 's are necessarily distinct, we can calculate the distribution of (Z 1,..., Z n), conditional on the order statistics, as placing mass 1 n ! on each of the n ! (potentially non-unique) possible orderings of the order statistics (Z,..., Z (n)). To put it more simply, we can say that conditional on the unordered collection of values in the sequence, the order in which they appear is simply a random shuffle.

We next highlight an important consequence of this equivalent characterization: under exchangeability of Z 1,..., Z n, it must hold that (i.e., each individual entry Z i is equally likely to be any one of the n order statistics), and consequently, for each index i ∈ [n] and each rank k ∈ [n] (see Fact 2.15 below). Moreover, if the values Z 1,..., Z n are distinct almost surely, then this becomes an equality.

Conditioning on the empirical distribution. In the real-valued setting discussed above, we saw that each entry Z i can be viewed as a random draw from the values Z,..., Z (n). In fact, this intuition can be extended to the general setting, beyond the case Z = R. Define which is the empirical distribution of the random vector (Z 1,..., Z n). The following proposition tells us an important implication of exchangeability: essentially, each Z i is a draw from this empirical distribution ̂ P n. This is simply an extension of the result (2.1) to the case of a general space Z.

## Proposition 2.2: Exchangeability and the empirical distribution

Let (Z 1,..., Z n) ∈ Z n be an exchangeable random vector, and let ̂ P n be the empirical distribution of this vector. Then for all i ∈ [n], i.e., if we condition on ̂ P n, then ̂ P n is itself the conditional distribution of Z i.

## Proof of Proposition 2.2

Since ̂ P n is a symmetric function of the random variables Z 1,..., Z n, by Lemma 2.3 below it holds almost surely that Z 1,..., Z n are exchangeable conditional on ̂ P n, and consequently, it holds almost surely that for each j ∈ [n] and every (measurable) A ⊆ Z. Assuming this holds, we then have which proves the desired claim.

The proof of Proposition 2.2 relies on the fact that Z 1,..., Z n are exchangeable even after conditioning on ̂ P n. In fact, this is a special case of the following lemma, which verifies that exchangeability continues to hold after conditioning on any symmetric function of Z 1,..., Z n.

## Lemma 2.3: Conditional exchangeability given a symmetric function

Let Z 1,..., Z n ∈ Z be exchangeable, and let f: Z n → W be a symmetric function, i.e., f (z 1,..., z n) = f (z σ,..., z σ (n)) for all z 1,..., z n ∈ Z and all σ ∈ S n. Then (Z 1,..., Z n) is conditionally exchangeable given f (Z 1,..., Z n), in the sense that the conditional distribution is, almost surely, an exchangeable distribution.

## Proof of Lemma 2.3

By definition of exchangeability, it suffices to verify that for any σ ∈ S n and any measurable set A, the following statement holds almost surely: Equivalently, we need to show that for all measurable A ⊆ Z n, B ⊆ W. This holds because where the first step holds since (Z 1,..., Z n) is exchangeable, while the second step holds by symmetry of f.

## Permutation tests

Permutation tests are used in statistics for a wide range of different inference tasks. In fact, permutation tests can be viewed as testing the null hypothesis of exchangeability. We turn to this next, and then examine two concrete examples of commonly used permutation tests within the framework of exchangeability.

Let P be the set of all distributions on Z n, and let P exch ⊆ P be the subset of distributions for which exchangeability is satisfied. Consider a random vector (Z 1,..., Z n) drawn from some joint distribution P. We would like to perform a hypothesis test of Before observing the data, we fix any function T: Z n → R, with the intuition that a large value of our test statistic T (Z 1,..., Z n) will indicate evidence against exchangeability. Then we define the quantity which compares the observed value of the test statistic, T (Z 1,..., Z n), against all possible values obtained via permutations of the data. (Note that the identity permutation, σ = Id, is one of the n ! many permutations included in the sum, and thus it is not possible for p to be smaller than 1 n !.) The following well-known result shows that the quantity defined in (2.3) is a valid p-value for testing the null hypothesis of exchangeability.

## Theorem 2.4: Validity of the permutation test

For any function T: Z n → R, the p-value p defined in (2.3) satisfies P P ( p ≤ τ ) ≤ τ for all τ ∈ and all P ∈ P exch.

In many settings, it is common to avoid the computational burden of computing all n ! permutations by instead sampling a smaller number M of permutations σ 1,..., σ M ∈ S n uniformly at random, to obtain the p-value Figure 2.1: Illustration of a permutation test for the equality of two real-valued distributions, where the test statistic used is the difference in means between two groups of data points, as in (2.5). In each plot, these two group means are shown as two dashed lines. In the left plot, we show the values computed on the real ordering of the data Z. The middle and right plots show the values for two typical permutations Z σ. The difference in means on the real data is far more extreme than on the permuted data, indicating evidence against the null hypothesis of exchangeability.

This p-value is again valid against the null hypothesis of exchangeability:

## Theorem 2.5: Validity of the permutation test with random permutations

For any function T: Z n → R, the p-value p defined in (2.4) satisfies P P ( p ≤ τ ) ≤ τ for all τ ∈ and all P ∈ P exch, where the probability is now taken with respect to both the random draw of ( Z 1,..., Z n ) ∼ P, and the permutations σ 1,..., σ M sampled uniformly at random (with replacement) from S n.

The ' +1 ' term appearing in the numerator and denominator of the p-value p constructed in (2.4) is necessary for obtaining this validity result-indeed, without this correction, the event p = 0 could have nonzero probability under the null hypothesis.

## Examples

To apply the permutation test, we need to specify a choice of the test statistic T. If the statistic captures the deviations from exchangeability that we expect may occur, then it will lead to a powerful test. We illustrate this with several common examples in the case of real-valued data, Z = R -namely, testing for equality of distributions, and testing for outliers. We will study another common application of permutation tests, testing independence between two random variables, in Chapter 13.

Testing equality of distributions. Suppose that we have two independent samples from two potentially different distributions, with n 0 draws from P 0 and n 1 = n -n 0 draws from P 1. Without loss of generality, we can take Z 1,..., Z n 0 i.i.d. ∼ P 0 and Z n 0 +1,..., Z n i.i.d. ∼ P 1. If P 0 = P 1, then the Z i 's are i.i.d. from a single shared distribution P 0 = P 1, and therefore exchangeability holds. If we conjecture that any potential difference between P 0 and P 1 would likely lead to a difference of means, we might choose the test statistic the difference in the sample means. Alternatively, we might make a choice that is more agnostic to the type of difference between the two distributions: the Kolmogorov-Smirnov statistic, which measures the maximum difference between the two empirical cumulative distribution functions (CDFs).

Testing if a new data point is an outlier. Next, suppose that we would like to test whether a particular data point-say, the last data point Z n -is an outlier relative to the rest of the sequence. In fact, as we will see later , this use of the permutation test is central to the development of conformal prediction.

For example, we might conjecture that Z n is more likely to be unusually large relative to the other Z i 's. In this case, we could consider the test statistic which is large when the rank of the last value is large among the rest of the list. For this particular test statistic, the permutation test p-value can be simplified. Observe that which simply captures the position of Z σ (n) relative to the original (unpermuted) sequence Z 1,..., Z n. Examining this quantity, we can then see that T (Z σ,..., Z σ (n)) ≥ T (Z 1,..., Z n) if and only if Z σ (n) ≥ Z n, and therefore, the p-value can be simplified as Here the last step holds since, for each i ∈ [n], there are exactly (n -1)! = n ! n permutations σ ∈ S n for which σ (n) = i.

In fact, this example can be derived in a simpler way, without the terminology of permutation tests. By definition of p, we can verify that, for any τ ∈ [0, 1), By (2.2) we know that exchangeability of Z 1,..., Z n implies that P (Z n > Z (k)) ≤ 1 -k/n ≤ τ, which directly verifies the validity of the p-value p. We state this result formally in the following corollary:

## Corollary 2.6

Let Z 1,..., Z n ∈ R be exchangeable. Then p = ∑ n i =1 ✶ { Z i ≥ Z n } n satisfies P ( p ≤ τ ) ≤ τ for all τ ∈.

## Proving validity of permutation tests

We next turn to building a theoretical understanding of permutation tests, within the framework of exchangeability. While the intuition behind permutation tests is very natural, here we will dive into the details that underlie their validity. The proofs of Theorem 2.4 and Theorem 2.5 are similar, so we only give the proof of the first.

## Proof of Theorem 2.4

Step 1: a CDF inequality. First, for any z ∈ Z n, write z σ = (z σ,..., z σ (n)) to denote the permuted vector for any permutation σ ∈ S n. We define We can observe that F (·; z) is the cumulative distribution function (CDF) for the distribution of the quantity -T (z σ), when σ ∈ S n is drawn uniformly at random (while z is treated as fixed). We therefore have where the probability is taken with respect to σ ∈ S n drawn uniformly at random, which is implied directly from the following basic property of CDFs: If the random variable X has CDF F, then P (F (X) ≤ τ) ≤ τ for all τ ∈. (2.7) Step 2: using exchangeability. Now, we incorporate the exchangeability assumption on Z = (Z 1,..., Z n). For any fi xed permutation σ ∈ S n, Z d = Z σ by exchangeability; therefore it also holds that Z d = Z σ when σ ∈ S n is drawn uniformly at random (independently of Z).

Next, we observe that the p-value p defined in (2.3) is equal to p = F (-T (Z); Z). Therefore, where the last two probabilities are calculated with respect to the distribution of both Z and the randomly drawn σ. Here the second equality holds since Z d = Z σ, while the last step holds since F (v; z) = F (v; z σ) for any v, z, and σ, by construction. Finally, we know that P (F (-T (Z σ); Z) ≤ τ | Z) ≤ τ, almost surely, by Step 1, which implies that P (F (-T (Z σ); Z) ≤ τ) ≤ τ by the tower law.

The key tool in this proof is the CDF of the negative values of the test statistic, i.e., -T ( Z ) (and its permuted version, -T ( Z σ ) ). The reason for taking the negative is simply that the permutation test in (2.3) has a small p-value when T ( Z ) is sufficiently large, while the CDF measures the probability of observing a value that is sufficiently small; by taking the negative, we can express the p-value as a CDF.
