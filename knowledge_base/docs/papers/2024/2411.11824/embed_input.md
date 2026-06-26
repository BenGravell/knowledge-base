<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Theoretical Foundations of Conformal Prediction

Topics include Conformal prediction, Distribution-free inference, Exchangeability, Permutation tests, Prediction sets, Finite-sample guarantees, Statistical learning theory, Uncertainty quantification.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Collects the main proof techniques behind conformal prediction and related distribution-free inference methods into a unified reference. The book is especially useful for understanding how exchangeability, permutation arguments, and modern conformal variants produce finite-sample guarantees when wrapped around complex learning systems.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This book is about conformal prediction and related inferential techniques that build on permutation tests and exchangeability. These techniques are useful in a diverse array of tasks, including hypothesis testing and providing uncertainty quantification guarantees for machine learning systems. Much of the current interest in conformal prediction is due to its ability to integrate into complex machine learning workflows, solving the problem of forming prediction sets without any assumptions on the form of the data generating distribution. Since contemporary machine learning algorithms have generally proven difficult to analyze directly, conformal prediction's main appeal is its ability to provide formal, finite-sample guarantees when paired with such methods. The goal of this book is to teach the reader about the fundamental technical arguments that arise when researching conformal prediction and related questions in distribution-free inference. Many of these proof strategies, especially the more recent ones, are scattered among research papers, making it difficult for researchers to understand where to look, which results are important, and how exactly the proofs work. We hope to bridge this gap by curating what we believe to be some of the most important results in the literature and presenting their proofs in a unified language, with illustrations, and with an eye towards pedagogy.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Conformal prediction is a statistical technique that quantifies uncertainty in predictive models, without any assumptions at all on the model and with minimal assumptions on the distribution of the data. Predictive models can be prone to unexpected inaccuracies and errors, complicating their practical usage. Conformal prediction guards against these issues, giving rigorous error bounds on predictions. This book presents the foundational statistical theory of conformal prediction and related methods.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Uncertainty quantification for prediction", "weight": 1.0} -->

We now describe the problem of uncertainty quantification for prediction. Consider a sequence of data points (X i, Y i) ∈ X × Y, for i = 1,..., n. Here, X i is the feature vector and Y i is the response variable. We are then given a new feature vector X n +1, with the task of predicting its corresponding response value Y n +1 (which is unobserved). Given a predictive model ˆ f, we can return a prediction ˆ f (X n +1). To communicate our uncertainty in this prediction, we can provide a margin of error around our prediction ˆ f (X n +1), or more generally, a prediction set C (X n +1) ⊆ Y. A common aim for this set is the property of marginal coverage, where α ∈ is a user-specified error level (e.g., α = 0. 1 for 90% coverage). If the size of the set C (X n +1) is large, this indicates high uncertainty in the prediction.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Uncertainty quantification for prediction", "weight": 1.0} -->

Conformal prediction is a technique for constructing sets C ( X n +1 ) that satisfy (1.1) under no assumptions on ˆ f or the form of the data distribution. In particular, if the underlying predictive model ˆ f is a poor fit to the data, then the accompanying set C ( X n +1 ) will be large-potentially even infinite. On the other hand, accurate models will result in smaller sets, and under additional conditions can lead to stronger notions of coverage than that in (1.1). In either case, the role of conformal prediction is to accurately quantify the level of uncertainty present when using a predictive model on the current data distribution.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Preview of split conformal prediction", "weight": 1.0} -->

We begin by presenting a version of the split conformal prediction algorithm. As before, suppose we have training data points ( X i, Y i ) for i = 1,..., n, and a test point ( X n +1, Y n +1 ). Taking n to be an even number for simplicity, the training data will be split into n/ 2 points used for model fitting, and n/ 2 points used for calibration.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Preview of split conformal prediction", "weight": 1.0} -->

We consider the setting Y = R -that is, a regression problem with a real-valued response.We can construct prediction intervals for Y n +1 via the following algorithm (which is one specific case of the more general split conformal algorithm, presented in Section 1.3 below).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Algorithm 1.1: Split conformal prediction, special case", "weight": 1.0} -->

1. Use data (X i, Y i) for i = 1,..., n/ 2 to fit a predictive model ˆ f: X → R. 2. For i = n/ 2 + 1,..., n, compute the absolute residual S i = | Y i -ˆ f (X i) |. 3. Sort S n/ 2+1,..., S n in increasing order, and let ˆ q be the ⌈ (1 -α)(n 2 +1) ⌉ -th element in the sorted list. 4. Return the prediction interval C (X n +1) = [ˆ f (X n +1) -ˆ q, ˆ f (X n +1) + ˆ q].

<!-- chunk {"id": "body-0010", "role": "body", "section": "Algorithm 1.1: Split conformal prediction, special case", "weight": 1.0} -->

This algorithm's output is the prediction interval C ( X n +1 ) = [ ˆ f ( X n +1 ) -ˆ q, ˆ f ( X n +1 ) + ˆ q ], which represents our uncertainty about the prediction ˆ f ( X n +1 ) for the target value Y n +1.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Algorithm 1.1: Split conformal prediction, special case", "weight": 1.0} -->

The predictive model ˆ f in the first step of Algorithm 1.1 can be any function that is based only on ( X 1, Y 1 ),..., ( X n/ 2, Y n/ 2 ). For example, it might be a linear model fitted via least-squares regression. The final set is an interval centered at the model's prediction, ˆ f ( X n +1 ) ± ˆ q. To interpret this choice of ˆ q, we observe ˆ q is chosen such that the intervals [ ˆ f ( X i ) -ˆ q, ˆ f ( X i ) + ˆ q ] contain the response variable Y i for approximately a (1 -α ) fraction of the points i = n/ 2 + 1,..., n (i.e., the data points that were not used for training the model ˆ f ).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Algorithm 1.1: Split conformal prediction, special case", "weight": 1.0} -->

If the data points are independent and identically distributed (i.i.d.),

<!-- chunk {"id": "body-0013", "role": "body", "section": "Conformal scores", "weight": 1.0} -->

The example above builds intuition for valid coverage with any predictive model and dataset, but the exact form of the algorithm above is rather constrained: by construction, the prediction set will always be of the form ˆ f ( X n +1 ) ± ˆ q, i.e., a band of constant width around the fitted predictive model ˆ f; see Figure 1.1. Fortunately, the conformal framework is much more flexible than the above example, allowing for nearly unlimited choice in how C ( X n +1 ) is constructed. The key concept is the conformal score function, which is a function s ( x, y ) such that larger values indicate that the data point ( x, y ) does not agree with (does not 'conform' to) the trends observed in the training data. For instance, given a fitted model ˆ f, a common choice for s is the residual score, s ( x, y ) = | y -ˆ f ( x ) |, since a large value of the residual indicates that ( x, y ) does not appear to agree with the model trained on the available data. We will give additional examples of score functions shortly.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Conformal scores", "weight": 1.0} -->

We now state a more general version of the split conformal prediction algorithm, using a generic conformal score function. As before, we again assume n is even for simplicity.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Algorithm 1.3: Split conformal prediction, general case", "weight": 1.0} -->

1. Use data (X i, Y i) for i = 1,..., n/ 2 to construct a conformal score function s: X ×Y → R, with the intuition that s (x, y) measures how unusual (x, y) is based on a model fit on data from this split. 2. For i = n/ 2 + 1,..., n, compute the score S i = s (X i, Y i). 3. Sort S n/ 2+1,..., S n in increasing order, and let ˆ q be the ⌈ (1 -α)(n 2 +1) ⌉ -th element in the sorted list. 4. Return the prediction set C (X n +1) = { y ∈ Y: s (X n +1, y) ≤ ˆ q }.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Algorithm 1.3: Split conformal prediction, general case", "weight": 1.0} -->

It may not be immediately clear that the set C ( X n +1 ) can be computed efficiently, since it nominally requires iterating through all y ∈ Y. However, in many cases, it simplifies to an interval that can be computed explicitly, just as in Algorithm 1.1-we will see some examples below.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Algorithm 1.3: Split conformal prediction, general case", "weight": 1.0} -->

While we are referring to split conformal prediction as 'an algorithm', the flexibility in choosing the score function s means that we should actually think of this as a family of algorithms-any given choice of the conformal score function s specifies a particular algorithm. For example, by choosing the residual score function s ( x, y ) = | y -ˆ f ( x ) |, we can obtain Algorithm 1.1 as a special case of Algorithm 1.3.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Algorithm 1.3: Split conformal prediction, general case", "weight": 1.0} -->

The following result states that the marginal coverage guarantee holds with any score function.

<!-- chunk {"id": "body-0019", "role": "body", "section": "The conformal prediction framework in context", "weight": 1.0} -->

This book discusses the statistical theory underlying conformal prediction and related techniques for providing uncertainty quantification for our predictive models-but of course, this question has long been studied in the statistics literature. What distinguishes the conformal prediction framework from other methods?

<!-- chunk {"id": "body-0020", "role": "body", "section": "The conformal prediction framework in context", "weight": 1.0} -->

As we have seen above, conformal prediction guarantees a marginal coverage property for data drawn i.i.d. from any distribution. We do not need to place conditions on the distribution (such as smoothness, or, a parametric model)-because of this, conformal prediction is often described as a distribution-free approach to inference. Moreover, we do not need to place conditions on the underlying model fitted to the data (such as assuming that ˆ f is a consistent estimator of the true association between Y and X ), and the result is finite-sample, in the sense that it holds at any value of n rather than offering only an asymptotic guarantee.

<!-- chunk {"id": "body-0021", "role": "body", "section": "The conformal prediction framework in context", "weight": 1.0} -->

Conformal prediction is closely related to the field of nonparametric statistics, which has also aimed to provide statistical methods that can flexibly handle data distributions that do not fall within some simple parametric model. However, there are some fundamental differences between these fields. In nonparametric and semiparametric statistics, most methods and results rely on regularity conditions that, while weaker than a parametric model assumption, are nonetheless much stronger than the minimal assumptions required by conformal prediction. For example, in nonparametric statistics it is common to assume smoothness conditions on the distribution of the data. With these types of assumptions, it is often possible to provide guarantees not only for predictive inference but also for estimation (for instance, estimating the mean of Y given X ). By contrast, exchangeability is a far weaker assumption than what is usually considered in nonparametric statistics. Without regularity conditions, it is still possible to provide useful and powerful methods for predictive inference, as we have seen with the marginal coverage guarantee for split conformal, above-but, as we will see in some of the hardness results presented in Chapter 4 and in Part IV of this book, other types of inference questions become more challenging or even impossible.

<!-- chunk {"id": "body-0022", "role": "body", "section": "The conformal prediction framework in context", "weight": 1.0} -->

Conformal prediction is intimately connected with permutation testing-we will soon see that it can be formulated as the inversion of a particular permutation test. It is also closely connected to quantile estimation and distribution estimation: a natural use of quantile estimation is to give prediction intervals for test points, although such a procedure would again require assumptions on the regularity of the distribution in order to have guaranteed coverage. Farther afield are resampling approaches, such as the bootstrap and cross-validation. Unlike conformal prediction, these are most commonly applied for confidence intervals on functionals of the distribution, and require regularity conditions for validity. However, we will explore distribution-free variants of cross-validation for the purpose of predictive inference later on in the book.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Scope of this book", "weight": 1.0} -->

After this introductory chapter, the remainder of Part I is an introduction to exchangeability, with a glossary of facts and properties that will be useful for the statistical results developed later in the book. We pay special attention to permutation tests, since conformal prediction can be reframed as inverting a permutation test. These tools will be critical to many of the proofs and intuitions in the remainder of the book.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Scope of this book", "weight": 1.0} -->

Part II of the book then turns to the conformal prediction framework. In particular, we discuss full conformal prediction, a generalization of the split conformal prediction method we have already introduced, which reveals the basic statistical logic at play. We then describe stronger properties than marginal coverage, with a mix of positive results for various methods, and hardness results that show the limits of what is possible without more assumptions. We also examine conformal prediction from a model-based perspective, to see how prior knowledge about the distribution of the data can be incorporated into the workflow of the conformal prediction framework.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Scope of this book", "weight": 1.0} -->

Part III of the book focuses on a broad range of different extensions to the conformal prediction methodology, including cross-validation based methods within the conformal framework, weighted versions of conformal prediction that allow us to move beyond the i.i.d. setting, online versions of conformal methods that are designed for streaming data, and computational shortcuts for conformal prediction. We also briefly cover additional topics such as variants of conformal prediction that can handle broader notions of risk, and connections with selective inference, multiple testing, and model aggregation-these topics are a sample of some recent work in the field, and are suggestive of the many directions for continued study.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Scope of this book", "weight": 1.0} -->

Finally, in Part IV, we depart from our focus on predictive coverage, and study the problem of distribution-free inference for a range of other questions: estimating a regression function, calibrating probability estimates, and testing conditional independence.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Bibliographic notes", "weight": 1.0} -->

We refer the reader to the bibliographic notes in Chapter 3 for references about the most common variants of conformal prediction and a detailed history of the field. Here, we will briefly mention some other textbooks and tutorials on conformal prediction. The first such book was Algorithmic Learning in a Random World by Vovk et al., which introduced the mathematical framework behind conformal prediction. More recent textbooks and tutorials include the works of Shafer and Vovk, Balasubramanian et al., and Angelopoulos and Bates. Turning to the specific algorithms in this section, split conformal prediction is first described in Papadopoulos et al., with the residual score function as a canonical example. The same paper also introduced the scaled residual score function as an alternative; see also Lei et al.. Lastly, the CQR score function is due to Romano et al., while the high-probability score is studied in Sadinle et al. (see also earlier work by Papadopoulos, which studies a related score).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Exercises", "weight": 1.0} -->

- 1.1 Consider split conformal prediction with Y = R. Suppose we are given an initial model ˆ f: X → R. Construct a score function s (x, y) that would yield intervals that are twice as wide above ˆ f as below ˆ f, i.e., intervals of the form C (x) = [ˆ f (x) -γ, ˆ f (x) + 2 γ] for some γ. - 1.2 Consider split conformal prediction in the setting of a multivariate response, Y = R d. Suppose we are given an initial model ˆ f: X → R d, which returns predictions ˆ f (x) = (ˆ f (x) 1,..., ˆ f (x) d). Construct a score function s (x, y) that would return prediction sets of the form 1.3 Suppose we have a regression problem with Y = R and two models ˆ f 1: X → R and ˆ f 2: X → R. Consider split conformal prediction with the score function s (x, y) = min {| y -ˆ f 1 (x) |, | y -ˆ f 2 (x) |}.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Exercises", "weight": 1.0} -->

Derive an explicit expression for the set C (X n +1) in terms of ˆ f 1, ˆ f 2, and ˆ q. What is the shape of the prediction set when ˆ q is small, or when ˆ q is large? Briefly explain why this might be attractive if we expect the distribution of Y given X = x to be bimodal for some values of x.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Exchangeability and Permutations", "weight": 1.0} -->

In this chapter, we provide an introduction to the idea of exchangeability, laying the core mathematical foundation of conformal prediction and many related methodologies. Exchangeability is a property of a sequence of random variables-informally, it expresses the idea that the sequence is equally likely to appear in any order.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Alternative characterizations of exchangeability", "weight": 1.0} -->

Exchangeability can be formally described in a number of different ways. Here, we give several characterizations and properties of exchangeability of a random vector ( Z 1,..., Z n ), to help build intuition.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Alternative characterizations of exchangeability", "weight": 1.0} -->

Symmetry of the joint density. Exchangeability has a simple characterization if the random vector (Z 1,..., Z n) is either discrete, or has a joint density. First, supposing Z is a countable space so that the Z i 's are discrete, let p: Z n → be the probability mass function for the joint distribution of (Z 1,..., Z n). Then this joint distribution is exchangeable if and only if Analogously, if Z = R and the random vector (Z 1,..., Z n) has a joint density f (with respect to Lebesgue measure on R n), then this joint distribution is exchangeable if and only if Conditioning on the order statistics. For this next interpretation, we will consider the special case of real-valued random variables, Z = R. In this setting, we define the order statistics Z ≤ · · · ≤ Z (n) as the sorted values of the vector (Z 1,..., Z n).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Alternative characterizations of exchangeability", "weight": 1.0} -->

In the simple setting where these n values are distinct almost surely, exchangeability implies that, conditioning on the order statistics, the random vector (Z 1,..., Z n) is equally likely to be any one of the n ! unique permutations of the order statistics. More generally, without assuming that the Z i 's are necessarily distinct, we can calculate the distribution of (Z 1,..., Z n), conditional on the order statistics, as placing mass 1 n ! on each of the n ! (potentially non-unique) possible orderings of the order statistics (Z,..., Z (n)). To put it more simply, we can say that conditional on the unordered collection of values in the sequence, the order in which they appear is simply a random shuffle.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Alternative characterizations of exchangeability", "weight": 1.0} -->

We next highlight an important consequence of this equivalent characterization: under exchangeability of Z 1,..., Z n, it must hold that (i.e., each individual entry Z i is equally likely to be any one of the n order statistics), and consequently, for each index i ∈ [n] and each rank k ∈ [n] (see Fact 2.15 below). Moreover, if the values Z 1,..., Z n are distinct almost surely, then this becomes an equality.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Alternative characterizations of exchangeability", "weight": 1.0} -->

Conditioning on the empirical distribution. In the real-valued setting discussed above, we saw that each entry Z i can be viewed as a random draw from the values Z,..., Z (n). In fact, this intuition can be extended to the general setting, beyond the case Z = R. Define which is the empirical distribution of the random vector (Z 1,..., Z n). The following proposition tells us an important implication of exchangeability: essentially, each Z i is a draw from this empirical distribution ̂ P n. This is simply an extension of the result (2.1) to the case of a general space Z.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Permutation tests", "weight": 1.0} -->

Permutation tests are used in statistics for a wide range of different inference tasks. In fact, permutation tests can be viewed as testing the null hypothesis of exchangeability. We turn to this next, and then examine two concrete examples of commonly used permutation tests within the framework of exchangeability.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Permutation tests", "weight": 1.0} -->

Let P be the set of all distributions on Z n, and let P exch ⊆ P be the subset of distributions for which exchangeability is satisfied. Consider a random vector (Z 1,..., Z n) drawn from some joint distribution P. We would like to perform a hypothesis test of Before observing the data, we fix any function T: Z n → R, with the intuition that a large value of our test statistic T (Z 1,..., Z n) will indicate evidence against exchangeability. Then we define the quantity which compares the observed value of the test statistic, T (Z 1,..., Z n), against all possible values obtained via permutations of the data. (Note that the identity permutation, σ = Id, is one of the n ! many permutations included in the sum, and thus it is not possible for p to be smaller than 1 n !.) The following well-known result shows that the quantity defined in (2.3) is a valid p-value for testing the null hypothesis of exchangeability.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Examples", "weight": 1.0} -->

To apply the permutation test, we need to specify a choice of the test statistic T. If the statistic captures the deviations from exchangeability that we expect may occur, then it will lead to a powerful test. We illustrate this with several common examples in the case of real-valued data, Z = R -namely, testing for equality of distributions, and testing for outliers. We will study another common application of permutation tests, testing independence between two random variables, in Chapter 13.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Examples", "weight": 1.0} -->

Testing equality of distributions. Suppose that we have two independent samples from two potentially different distributions, with n 0 draws from P 0 and n 1 = n -n 0 draws from P 1. Without loss of generality, we can take Z 1,..., Z n 0 i.i.d. ∼ P 0 and Z n 0 +1,..., Z n i.i.d. ∼ P 1. If P 0 = P 1, then the Z i 's are i.i.d. from a single shared distribution P 0 = P 1, and therefore exchangeability holds. If we conjecture that any potential difference between P 0 and P 1 would likely lead to a difference of means, we might choose the test statistic the difference in the sample means. Alternatively, we might make a choice that is more agnostic to the type of difference between the two distributions: the Kolmogorov-Smirnov statistic, which measures the maximum difference between the two empirical cumulative distribution functions (CDFs).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Examples", "weight": 1.0} -->

Testing if a new data point is an outlier. Next, suppose that we would like to test whether a particular data point-say, the last data point Z n -is an outlier relative to the rest of the sequence. In fact, as we will see later, this use of the permutation test is central to the development of conformal prediction.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Examples", "weight": 1.0} -->

For example, we might conjecture that Z n is more likely to be unusually large relative to the other Z i 's. In this case, we could consider the test statistic which is large when the rank of the last value is large among the rest of the list. For this particular test statistic, the permutation test p-value can be simplified. Observe that which simply captures the position of Z σ (n) relative to the original (unpermuted) sequence Z 1,..., Z n. Examining this quantity, we can then see that T (Z σ,..., Z σ (n)) ≥ T (Z 1,..., Z n) if and only if Z σ (n) ≥ Z n, and therefore, the p-value can be simplified as Here the last step holds since, for each i ∈ [n], there are exactly (n -1)! = n ! n permutations σ ∈ S n for which σ (n) = i.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Examples", "weight": 1.0} -->

In fact, this example can be derived in a simpler way, without the terminology of permutation tests. By definition of p, we can verify that, for any τ ∈ [0, 1), By (2.2) we know that exchangeability of Z 1,..., Z n implies that P (Z n > Z (k)) ≤ 1 -k/n ≤ τ, which directly verifies the validity of the p-value p.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Proving validity of permutation tests", "weight": 1.0} -->

We next turn to building a theoretical understanding of permutation tests, within the framework of exchangeability. While the intuition behind permutation tests is very natural, here we will dive into the details that underlie their validity. The proofs of Theorem 2.4 and Theorem 2.5 are similar, so we only give the proof of the first.
